"""One-shot migration: clean up Notebook tool blocks across 40 entries that pre-date notebookMeta.

Pattern 1 (24 entries): prompt body = "Add N sources: /F1, /F2, /F3. In the Notebook Instructions field, paste: '<instr>'. Then ask <question>."
Pattern 2 (14 entries): prompt body = "Create a new Copilot Notebook called '<title>'. Pin /F1, /F2, /F3. Set the Notebook Instructions field to '<instr>'. Then ask <question>."
Pattern 3 (2 entries): prompt body = "Create a new Notebook page called '<title>'. Add /F1, /F2, /F3 as sources. Ask: '<question>'."

ID variants use "Tambahkan N sumber:" / "Buat Copilot Notebook baru" / "Pada kolom Instructions Notebook, tempelkan:" / "Kemudian minta".

For each broken Notebook block:
- extract sources -> notebookMeta['sources'] (use union of all 4 prompts' file refs, deduplicated, with leading slash)
- extract instructions text -> notebookMeta['instructions'] (EN); from ID prompt -> instructionsID
- replace each prompt body with the actual question (everything after the preamble), capitalised
- set instr field to the canonical pattern: prompt 0 = "All sources are loaded ...", prompt 1+ = "Stay in the same notebook ..."
- preserve persona / personaID arrays; keep the original kwargs intact
"""
import re, sys, os
from pathlib import Path

REPO = Path(r'C:\Users\peiyiyap\zava-copilot-demo')

# Source files containing broken Notebook blocks
SOURCE_FILES = [
    'ind_batch1.py',  # commercial-banking, islamic-banking
    'ind_batch2.py',  # investment-banking, general-insurance, life-insurance, takaful
    'ind_batch3.py',  # hospital-network, pharmaceutical, og-upstream
    'ind_batch4.py',  # og-downstream, renewable-energy, industrial-manufacturing (factory)
    'ind_batch5.py',  # plantation, bpo-services, telco, diversified-conglomerate
    'ind_batch6.py',  # fintech-payments, government-agency, property-reit, logistics-3pl, coal-mining, hotel-resort, construction, aviation-airports, retail-grocery, media-entertainment
    'ind_batch7.py',  # property-reit, logistics-3pl, coal-mining, hotel-resort
    'ind_batch8.py',  # construction, aviation-airports, retail-grocery, media-entertainment
    'ind_batch9.py',  # glc-investment, financial-regulator
    'dept_data.py',   # dept-hr, dept-finance
    'dept_data2.py',  # dept-legal, dept-risk, dept-strategy
    'dept_data3.py',  # dept-marketing, dept-esg
    'dept_data4.py',  # dept-operations, dept-corpsec
    'dept_data5.py',  # dept-investor-relations, dept-procurement, dept-it-digital
]

# Block matcher — find tool(T_NOTEBOOK, ...) ... ) with all the prompt arrays inside.
# We do this with a streaming parser since the structure has nested quotes.

FILE_REF_RE = re.compile(r'/?[A-Z][A-Za-z0-9_]+\.(?:xlsx|docx|pptx|csv|pdf)')
PATTERN1_HEAD = re.compile(r"^Add\s+\d+\s+sources?:\s*", re.IGNORECASE)
PATTERN1_HEAD_ID = re.compile(r"^Tambahkan\s+\d+\s+sumber:\s*", re.IGNORECASE)
PATTERN2_HEAD = re.compile(r"^Create\s+a\s+new\s+(?:Copilot\s+)?Notebook(?:\s+page)?\s+called\s+['\"]([^'\"]+)['\"]\s*\.\s*(?:Pin|Add)\s+", re.IGNORECASE)
PATTERN2_HEAD_ID = re.compile(r"^Buat(?:lah)?\s+(?:Copilot\s+)?Notebook(?:\s+baru)?(?:\s+halaman)?\s+(?:bernama|berjudul)\s+['\"]([^'\"]+)['\"]\s*\.\s*(?:Pin|Tambahkan)\s+", re.IGNORECASE)

INSTR_RE_EN = re.compile(
    r"(?:In\s+the\s+Notebook\s+Instructions\s+field,?\s+paste|Set\s+the\s+Notebook\s+Instructions\s+field\s+to|Set\s+Instructions\s+to|Notebook\s+Instructions:|Instructions:)\s*[:\s]?\s*['\"]([^'\"]+)['\"]\s*\.?\s*",
    re.IGNORECASE,
)
INSTR_RE_ID = re.compile(
    r"(?:Pada\s+kolom\s+Instructions\s+Notebook,?\s+tempelkan|Tetapkan\s+Instructions\s+Notebook\s+ke|Set\s+Instructions\s+Notebook\s+menjadi|Pada\s+Instructions\s+Notebook,?\s+tempel|Instructions\s+Notebook:)\s*[:\s]?\s*['\"]([^'\"]+)['\"]\s*\.?\s*",
    re.IGNORECASE,
)

THEN_ASK_RE_EN = re.compile(r"^\s*(?:Then\s+ask\s+(?:the\s+Notebook\s+(?:to|for)\s+)?|Then\s+request\s+|Ask:\s+['\"]?|Then:\s+|Then\s+(?:summarise|synthesise|produce|create|generate|draft|build|score|compare|score)\s+)", re.IGNORECASE)
THEN_ASK_RE_ID = re.compile(r"^\s*(?:Kemudian\s+minta\s+(?:Notebook\s+)?|Lalu\s+minta\s+|Kemudian\s+tanyakan\s+|Tanyakan:\s+['\"]?|Lalu:\s+)", re.IGNORECASE)

CANONICAL_INSTR_P0_EN = "All sources are loaded in the notebook (see Notebook setup above). The Instructions field is set. Type the prompt below in the notebook chat."
CANONICAL_INSTR_PN_EN = "Stay in the same notebook chat. Type the next prompt — Copilot remembers earlier prompts."
CANONICAL_INSTR_P0_ID = "Semua sumber sudah dimuat di notebook (lihat setup Notebook di atas). Field Instructions sudah diset. Ketik prompt di bawah pada chat notebook."
CANONICAL_INSTR_PN_ID = "Tetap di chat notebook yang sama. Ketik prompt berikut — Copilot mengingat prompt sebelumnya."


def parse_files_from_text(text):
    raw = FILE_REF_RE.findall(text)
    # Normalise: ensure leading slash on every source
    return ['/' + s.lstrip('/') for s in raw]


def clean_prompt_en(body):
    """Extract sources, instructions, cleaned-question from one English Notebook prompt body.
    Returns (sources_list, instructions_text_or_None, cleaned_question)."""
    sources = parse_files_from_text(body)
    rest = body
    # Strip P1: "Add N sources: /F1, /F2, /F3."
    m = PATTERN1_HEAD.search(rest)
    if m:
        # find the period that ends the file list
        after = rest[m.end():]
        end_idx = after.find('. ')
        if end_idx == -1:
            end_idx = after.find('.')
        if end_idx == -1:
            return sources, None, body
        rest = after[end_idx+1:].lstrip()
    # Strip P2: "Create a new Copilot Notebook called 'X'. Pin /F1, /F2."
    m2 = PATTERN2_HEAD.search(rest)
    if m2:
        after = rest[m2.end():]
        end_idx = after.find('. ')
        if end_idx == -1:
            end_idx = after.find('.')
        if end_idx == -1:
            return sources, None, body
        rest = after[end_idx+1:].lstrip()
    # Extract Instructions text
    instructions = None
    m3 = INSTR_RE_EN.search(rest)
    if m3:
        instructions = m3.group(1).strip()
        rest = (rest[:m3.start()] + rest[m3.end():]).strip()
    # Strip "Then ask" / "Ask:" prefix
    m4 = THEN_ASK_RE_EN.match(rest)
    if m4:
        rest = rest[m4.end():].strip()
    # Strip trailing closing quote if any
    if rest.endswith("'") or rest.endswith('"'):
        rest = rest[:-1].rstrip('. ')
    # Capitalise first letter
    if rest and rest[0].islower():
        rest = rest[0].upper() + rest[1:]
    # If the rest is empty, fall back to original body (don't blank a prompt)
    if not rest or len(rest) < 30:
        rest = body
    return sources, instructions, rest


def clean_prompt_id(body):
    sources = parse_files_from_text(body)
    rest = body
    m = PATTERN1_HEAD_ID.search(rest)
    if m:
        after = rest[m.end():]
        end_idx = after.find('. ')
        if end_idx == -1:
            end_idx = after.find('.')
        if end_idx == -1:
            return sources, None, body
        rest = after[end_idx+1:].lstrip()
    m2 = PATTERN2_HEAD_ID.search(rest)
    if m2:
        after = rest[m2.end():]
        end_idx = after.find('. ')
        if end_idx == -1:
            end_idx = after.find('.')
        if end_idx == -1:
            return sources, None, body
        rest = after[end_idx+1:].lstrip()
    instructions = None
    m3 = INSTR_RE_ID.search(rest)
    if m3:
        instructions = m3.group(1).strip()
        rest = (rest[:m3.start()] + rest[m3.end():]).strip()
    m4 = THEN_ASK_RE_ID.match(rest)
    if m4:
        rest = rest[m4.end():].strip()
    if rest.endswith("'") or rest.endswith('"'):
        rest = rest[:-1].rstrip('. ')
    if rest and rest[0].islower():
        rest = rest[0].upper() + rest[1:]
    if not rest or len(rest) < 30:
        rest = body
    return sources, instructions, rest


# Source-file mutation: scan for tool(T_NOTEBOOK, ...) blocks, rewrite each.

# The block always starts with "tool(T_NOTEBOOK," and ends with the matching closing ")," at the same indent.
# Within, we find the EN prompt array `[ {...}, {...}, ... ]`, the `promptsID=[ ... ]`, and we mutate them.

NOTEBOOK_TOOL_RE = re.compile(r'tool\(\s*T_NOTEBOOK\s*,', re.MULTILINE)
DICT_RE = re.compile(r"\{\s*'instr'\s*:\s*('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")\s*,\s*'prompt'\s*:\s*('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")\s*\}", re.DOTALL)


def py_str_decode(s):
    """Convert a Python source string literal (with quotes) to its actual value."""
    return eval(s, {}, {})


def py_str_encode(s):
    """Encode a string for safe Python source-literal output, preferring single quotes."""
    s = s.replace('\\', '\\\\')
    if "'" not in s:
        return "'" + s + "'"
    if '"' not in s:
        return '"' + s + '"'
    # Mix — escape single quotes
    return "'" + s.replace("'", "\\'") + "'"


def find_block_end(text, start):
    """Find the matching ')' that closes the tool(...) call starting at `start`.
    Returns index just AFTER the closing ')'."""
    depth = 0
    in_str = None
    esc = False
    i = start
    while i < len(text):
        ch = text[i]
        if esc:
            esc = False
        elif ch == '\\' and in_str:
            esc = True
        elif in_str:
            if ch == in_str:
                in_str = None
        elif ch in ("'", '"'):
            in_str = ch
        elif ch == '(':
            depth += 1
        elif ch == ')':
            depth -= 1
            if depth == 0:
                return i + 1
        i += 1
    return -1


def rewrite_notebook_block(block_text, source_filename, entry_id_hint):
    """Take the full text of a tool(T_NOTEBOOK, ...) call. Return the rewritten text or None if unchanged."""
    # Already has notebookMeta? skip
    if 'notebookMeta=' in block_text and 'notebookMeta=None' not in block_text:
        return None
    # Find EN prompt list — first '[' after 'tool(T_NOTEBOOK,' that starts with '{...'
    m = re.search(r"tool\(\s*T_NOTEBOOK\s*,[^\[]*?(\[)", block_text, re.DOTALL)
    if not m:
        return None
    en_list_start = m.start(1)
    # Walk to matching ']'
    en_list_end = find_matching(block_text, en_list_start, '[', ']')
    if en_list_end < 0:
        return None
    en_list_text = block_text[en_list_start:en_list_end]
    en_dicts = list(DICT_RE.finditer(en_list_text))
    if not en_dicts:
        return None

    # Find ID prompts list (promptsID=[...])
    id_match = re.search(r"promptsID\s*=\s*(\[)", block_text)
    id_dicts = []
    id_list_start = id_list_end = None
    if id_match:
        id_list_start = id_match.start(1)
        id_list_end = find_matching(block_text, id_list_start, '[', ']')
        if id_list_end > 0:
            id_list_text = block_text[id_list_start:id_list_end]
            id_dicts = list(DICT_RE.finditer(id_list_text))

    # Decode + clean each EN prompt
    en_results = []
    all_sources = []
    instructions_en = None
    for d in en_dicts:
        instr = py_str_decode(d.group(1))
        prompt = py_str_decode(d.group(2))
        srcs, instr_txt, cleaned = clean_prompt_en(prompt)
        for s in srcs:
            if s not in all_sources:
                all_sources.append(s)
        if instr_txt and not instructions_en:
            instructions_en = instr_txt
        en_results.append((instr, prompt, cleaned))
    # If no sources extracted, skip — pattern wasn't matched
    if not all_sources:
        return None
    # Decode + clean ID prompts
    id_results = []
    instructions_id = None
    for d in id_dicts:
        instr = py_str_decode(d.group(1))
        prompt = py_str_decode(d.group(2))
        srcs, instr_txt, cleaned = clean_prompt_id(prompt)
        if instr_txt and not instructions_id:
            instructions_id = instr_txt
        id_results.append((instr, prompt, cleaned))

    # Build new EN list text
    new_en_lines = []
    for i, (instr, prompt, cleaned) in enumerate(en_results):
        new_instr = CANONICAL_INSTR_P0_EN if i == 0 else CANONICAL_INSTR_PN_EN
        new_en_lines.append(
            "{'instr':" + py_str_encode(new_instr) + ", 'prompt':" + py_str_encode(cleaned) + "}"
        )
    new_en_list = "[\n        " + ",\n        ".join(new_en_lines) + "\n      ]"

    # Build new ID list text (only if id_dicts existed)
    new_id_list = None
    if id_results:
        new_id_lines = []
        for i, (instr, prompt, cleaned) in enumerate(id_results):
            new_instr = CANONICAL_INSTR_P0_ID if i == 0 else CANONICAL_INSTR_PN_ID
            new_id_lines.append(
                "{'instr':" + py_str_encode(new_instr) + ", 'prompt':" + py_str_encode(cleaned) + "}"
            )
        new_id_list = "[\n        " + ",\n        ".join(new_id_lines) + "\n      ]"

    # Reconstruct: replace EN list, replace ID list, append notebookMeta=
    new_block = block_text[:en_list_start] + new_en_list + block_text[en_list_end:]
    if new_id_list and id_list_start is not None and id_list_end is not None:
        # offsets shift because EN list size changed
        offset = len(new_en_list) - (en_list_end - en_list_start)
        adj_id_start = id_list_start + offset
        adj_id_end = id_list_end + offset
        new_block = new_block[:adj_id_start] + new_id_list + new_block[adj_id_end:]

    # Inject notebookMeta= just before the closing ')' of the tool(...) call
    # Find last ')' in new_block (the one that closes tool(...))
    close_idx = new_block.rfind(')')
    if close_idx < 0:
        return None
    # Make sure the trailing comma/whitespace is correct
    pre = new_block[:close_idx].rstrip()
    if not pre.endswith(','):
        pre = pre + ','
    sources_repr = '[' + ', '.join(py_str_encode(s) for s in all_sources) + ']'
    instr_en = instructions_en or 'Use ALL uploaded sources as the only source of truth. Always cite the file name (and tab/section if applicable) at the end of every statement. Do not speculate beyond the sources.'
    instr_id = instructions_id or 'Gunakan SEMUA file sumber yang diunggah sebagai satu-satunya sumber kebenaran. Selalu kutip nama file (dan tab/bagian jika berlaku) di akhir setiap pernyataan. Jangan berspekulasi di luar sumber.'
    nb_meta = (
        "\n      notebookMeta={\n"
        "        'sources': " + sources_repr + ",\n"
        "        'instructions': " + py_str_encode(instr_en) + ",\n"
        "        'instructionsID': " + py_str_encode(instr_id) + "\n"
        "      }"
    )
    new_block = pre + nb_meta + new_block[close_idx:]
    return new_block


def find_matching(text, start, open_ch, close_ch):
    """Given text and an index pointing at open_ch, find the index of matching close_ch+1."""
    depth = 0
    in_str = None
    esc = False
    i = start
    while i < len(text):
        ch = text[i]
        if esc:
            esc = False
        elif ch == '\\' and in_str:
            esc = True
        elif in_str:
            if ch == in_str:
                in_str = None
        elif ch in ("'", '"'):
            in_str = ch
        elif ch == open_ch:
            depth += 1
        elif ch == close_ch:
            depth -= 1
            if depth == 0:
                return i + 1
        i += 1
    return -1


def process_file(filename):
    path = REPO / filename
    if not path.exists():
        return 0, 0
    text = path.read_text(encoding='utf-8')
    original = text
    rewrites = 0
    skipped = 0
    # Find all tool(T_NOTEBOOK, blocks
    matches = list(NOTEBOOK_TOOL_RE.finditer(text))
    # Process from END to START so offsets don't shift while rewriting
    for m in reversed(matches):
        start = m.start()
        # Find matching ')' to close the tool(...) call — note start of block is `tool(`
        block_open = text.find('(', start)
        block_close = find_block_end(text, block_open)
        if block_close < 0:
            skipped += 1
            continue
        block = text[start:block_close]
        new_block = rewrite_notebook_block(block, filename, '')
        if new_block:
            text = text[:start] + new_block + text[block_close:]
            rewrites += 1
        else:
            skipped += 1
    if text != original:
        path.write_text(text, encoding='utf-8')
    return rewrites, skipped


if __name__ == '__main__':
    total_r = total_s = 0
    for f in SOURCE_FILES:
        r, s = process_file(f)
        print(f"{f:25s} rewritten={r}  skipped={s}")
        total_r += r
        total_s += s
    print(f"\nTOTAL: rewritten={total_r}  skipped={total_s}")
