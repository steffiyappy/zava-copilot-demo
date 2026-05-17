"""Refresh modern-feature coverage across all ind() blocks.

Phase 1: PowerPoint — inject a 4th EN + ID prompt that showcases the April-2026
web-grounding + image-model-picker (GPT-Image / Flux / Auto) features.

The injection is surgical: it appends ONE new prompt dict to BOTH the EN
prompts=[...] list and the promptsID=[...] list inside every tool(T_PPT, ...)
call across the data files.

Safety:
- Validate with ast.parse on each file after edits before commit.
- Skip any block that already contains a PPT modern-feature keyword.
- Print the dry-run diff first; only mutates when --apply is passed.
"""
import re, glob, ast, sys, argparse, io

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

TOOL = 'T_PPT'
KEYWORDS = ['web grounding', 'web reference', 'webpage URL', 'public web',
            'image model', 'Flux', 'GPT-Image', 'image-model gear',
            'grounding web', 'referensi web', 'model gambar']

# New showcase prompts (EN + ID) — generic enough for any scenario.
NEW_EN = (
    "{'instr':\"Stay in the same deck (or open a fresh PowerPoint for the Web file). Open the **Copilot pane** > click the **🌐 web reference** chip and paste ONE relevant public web URL "
    "(e.g. a regulator microsite, a Bursa Malaysia announcement page, a peer's investor-relations page, or a recent industry research page) as a deck-wide reference. "
    "Then click the **image-model gear** above the image prompt and select **GPT-Image** for photoreal hero artwork (or **Flux** for stylised). Paste the prompt below.\","
    " 'prompt':\"Refresh the cover slide and one mid-deck slide using the public-web reference I just attached — pull in the 2 most relevant facts/headlines from that page and surface them as concise, dated bullets with a citation footer "
    "('Source: <publisher>, <date>'). On the cover slide, generate ONE photoreal hero image with **GPT-Image** that captures the strategic theme of this deck in an executive style — no text-on-image, 16:9, neutral palette. "
    "Add a footer disclaimer that the web-grounding facts are point-in-time and must be re-verified before final external use.\"}"
)
NEW_ID = (
    "{'instr':\"Tetap di deck yang sama (atau buka file PowerPoint for the Web baru). Buka **Copilot pane** > klik chip **🌐 referensi web** dan tempelkan SATU URL publik yang relevan "
    "(misalnya microsite regulator, halaman pengumuman BEI, halaman investor-relations peer, atau halaman riset industri terbaru) sebagai referensi seluruh deck. "
    "Kemudian klik **roda gigi model gambar** di atas prompt gambar dan pilih **GPT-Image** untuk hero photoreal (atau **Flux** untuk stilisasi). Tempelkan prompt di bawah ini.\","
    " 'prompt':\"Segarkan slide cover dan satu slide tengah deck menggunakan referensi web publik yang baru saja dilampirkan — tarik 2 fakta/headline paling relevan dari halaman tersebut dan munculkan sebagai bullet ringkas bertanggal dengan footer kutipan "
    "('Sumber: <penerbit>, <tanggal>'). Pada slide cover, hasilkan SATU hero image photoreal dengan **GPT-Image** yang menangkap tema strategis deck dalam gaya eksekutif — tanpa teks di gambar, 16:9, palet netral. "
    "Tambahkan disclaimer footer bahwa fakta web-grounding bersifat point-in-time dan harus diverifikasi ulang sebelum penggunaan eksternal final.\"}"
)

def find_tool_block_ranges(text, tool_name):
    """Return list of (open_paren_idx, close_paren_idx) for each tool(TOOL, ...) call."""
    ranges = []
    for m in re.finditer(rf"tool\(\s*{tool_name}\b", text):
        i = m.end()
        # advance to the opening paren of tool(
        op = text.rfind('(', m.start(), i)
        if op < 0: continue
        depth = 1
        j = op + 1
        while j < len(text) and depth > 0:
            ch = text[j]
            if ch == '(': depth += 1
            elif ch == ')':
                depth -= 1
                if depth == 0:
                    ranges.append((op, j))
                    break
            j += 1
    return ranges

def find_list_ranges_in_tool(text, op, cl):
    """Return ((en_open_bracket, en_close_bracket), (id_open_bracket, id_close_bracket)) inside tool() span.

    The first square-bracket list opens immediately after `tool(NAME, LIC, ACCT,` —
    that's the EN prompts list. The ID list opens after `promptsID=` later in the call.
    """
    span = text[op:cl+1]
    # EN list: first '[' at top-level after the first three comma-separated args.
    # We just find the first '[' after position 0.
    depth_paren = 0
    en_open = en_close = None
    # Track the FIRST list whose depth_paren == 1 (we are inside the tool() call).
    i = 0
    while i < len(span):
        ch = span[i]
        if ch == '(':
            depth_paren += 1
        elif ch == ')':
            depth_paren -= 1
        elif ch == '[' and depth_paren == 1 and en_open is None:
            # found first list — walk to matching ']'
            en_open = i
            d = 1
            j = i + 1
            while j < len(span) and d > 0:
                if span[j] == '[': d += 1
                elif span[j] == ']':
                    d -= 1
                    if d == 0:
                        en_close = j
                        break
                j += 1
            break
        i += 1

    # ID list: search for 'promptsID=[' after en_close
    id_open = id_close = None
    if en_close is not None:
        m2 = re.search(r"promptsID\s*=\s*\[", span[en_close:])
        if m2:
            id_open = en_close + m2.end() - 1  # position of '['
            d = 1
            j = id_open + 1
            while j < len(span) and d > 0:
                if span[j] == '[': d += 1
                elif span[j] == ']':
                    d -= 1
                    if d == 0:
                        id_close = j
                        break
                j += 1

    return (
        (op + en_open, op + en_close) if en_open is not None and en_close is not None else None,
        (op + id_open, op + id_close) if id_open is not None and id_close is not None else None,
    )


def block_has_modern(text, op, cl):
    span = text[op:cl+1].lower()
    return any(k.lower() in span for k in KEYWORDS)


def inject_into_file(path, dry=True):
    text = open(path, encoding='utf-8').read()
    ranges = find_tool_block_ranges(text, TOOL)
    if not ranges:
        return 0, 0, []
    # Process from the END so indices stay valid as we splice.
    edits = []
    for op, cl in reversed(ranges):
        if block_has_modern(text, op, cl):
            edits.append((op, cl, 'skip-already-has-modern'))
            continue
        en_range, id_range = find_list_ranges_in_tool(text, op, cl)
        if en_range is None:
            edits.append((op, cl, 'skip-no-en-list'))
            continue
        en_open, en_close = en_range
        # Insert ", NEW_EN" just before the closing ']' at en_close.
        # Detect trailing whitespace before ']' to preserve indentation.
        before_close = text[max(en_open, en_close-200):en_close]
        # Look at indentation of last prompt dict
        m_indent = re.search(r"\n([ \t]+)\{['\"]instr", before_close)
        indent = m_indent.group(1) if m_indent else '        '

        new_en_block = f",\n{indent}{NEW_EN}"
        text = text[:en_close] + new_en_block + text[en_close:]

        if id_range is not None:
            id_open, id_close = id_range
            # id_close shifted because we just inserted into EN list AFTER id_close? NO —
            # we're processing in REVERSE order so id_close is AFTER en_close numerically.
            # Wait: id_range is computed BEFORE we mutated; we just mutated at en_close.
            # The mutation inserted text at en_close. id_close > en_close. So we must shift id_close
            # by len(new_en_block).
            shift = len(new_en_block)
            id_close += shift
            new_id_block = f",\n{indent}{NEW_ID}"
            text = text[:id_close] + new_id_block + text[id_close:]
        edits.append((op, cl, 'injected'))

    if not dry:
        # Validate via ast.parse before writing
        try:
            ast.parse(text)
        except SyntaxError as e:
            print(f"  ❌ SYNTAX ERROR in {path}: {e}")
            return 0, 0, edits
        open(path, 'w', encoding='utf-8').write(text)
    injected = sum(1 for _,_,s in edits if s == 'injected')
    skipped = sum(1 for _,_,s in edits if s != 'injected')
    return injected, skipped, edits


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--apply', action='store_true', help='Mutate files in place. Default = dry run.')
    ap.add_argument('--files', nargs='*', help='Limit to specific files')
    args = ap.parse_args()

    files = args.files or sorted(glob.glob('ind_batch*.py') + glob.glob('dept_data*.py'))
    total_inj = total_skip = 0
    for f in files:
        if not os.path.exists(f):
            print(f"  ⚠️  skip {f} (not found)")
            continue
        injected, skipped, _ = inject_into_file(f, dry=not args.apply)
        total_inj += injected
        total_skip += skipped
        print(f"{f:30}  injected={injected:2}  skipped={skipped:2}")
    mode = 'APPLIED' if args.apply else 'DRY-RUN'
    print(f"\n{mode}: total injected={total_inj}, skipped={total_skip}")


if __name__ == '__main__':
    import os
    main()
