"""Regenerate entry-level ZIP bundles for the 5 affected entries.

Reads each entry's final post-build `files` list from data.js (regex-extracted
since it's a 14MB JS file, not JSON). Zips the listed files from files/.
"""
import re, zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = (ROOT / 'data.js').read_text(encoding='utf-8')
FILES_DIR = ROOT / 'files'
ZIPS_DIR = FILES_DIR / 'zips'
NOTEBOOK_GUIDE = '00_Copilot_Notebook_Demo_Guide.docx'

ENTRIES = ['retail-grocery', 'power-utilities', 'food-fmcg', 'coal-mining', 'dept-legal']


def extract_files(entry_id: str):
    # Match: id:"<entry_id>"  ... files:[ ... ]  before next major bracket
    m = re.search(
        r"id:\s*'" + re.escape(entry_id) + r"'.*?files:\s*\[",
        DATA, flags=re.DOTALL,
    )
    if not m:
        return None
    start = m.end()
    # Bracket-balance from start to find matching ]
    depth = 1
    i = start
    while i < len(DATA) and depth > 0:
        ch = DATA[i]
        if ch == '[':
            depth += 1
        elif ch == ']':
            depth -= 1
            if depth == 0:
                break
        elif ch == "'":
            # skip string
            j = i + 1
            while j < len(DATA) and DATA[j] != "'":
                if DATA[j] == '\\':
                    j += 2
                else:
                    j += 1
            i = j
        i += 1
    body = DATA[start:i]
    # Pull all double-quoted strings
    return re.findall(r"'((?:[^'\\]|\\.)*)'", body)


def zip_entry(entry_id: str):
    files = extract_files(entry_id)
    if files is None:
        print(f'  ✗ {entry_id}: not found in data.js')
        return
    out = ZIPS_DIR / f'entry-{entry_id}.zip'
    written, missing = 0, []
    seen = set()
    with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED) as z:
        # Always include the notebook demo guide first if present
        guide = FILES_DIR / NOTEBOOK_GUIDE
        if guide.exists():
            z.write(guide, NOTEBOOK_GUIDE)
            written += 1
            seen.add(NOTEBOOK_GUIDE)
        for f in files:
            if f in seen:
                continue
            seen.add(f)
            src = FILES_DIR / f
            if src.exists() and src.is_file():
                z.write(src, f)
                written += 1
            else:
                missing.append(f)
    sz = out.stat().st_size
    print(f'  ✓ entry-{entry_id}.zip — {written} files ({sz:,} bytes)'
          + (f' [missing: {len(missing)}]' if missing else ''))
    if missing:
        for m in missing[:5]:
            print(f'      - missing: {m}')


if __name__ == '__main__':
    print('Regenerating entry zips for 5 affected entries...')
    for e in ENTRIES:
        zip_entry(e)
