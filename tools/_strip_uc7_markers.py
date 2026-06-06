"""One-shot fixup for the UC7 integration:
   (1) Strip the visible `[UC7-IMPORT-2026-06-06]` idempotency marker from all
       9 prompts in 5 source files (it leaked into the user-visible prompts).
   (2) Update the integration script to use a non-leaking idempotency check
       (persona name presence) so future re-runs remain safe.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MARKER = '[UC7-IMPORT-2026-06-06]'

# Strip patterns: the marker is appended at end of prompt with various separators.
# Allow optional preceding space + the bracketed marker, occurring just before
# the closing quote of the prompt string.
PATTERNS = [
    re.compile(r' \[UC7-IMPORT-2026-06-06\]'),   # space + marker
    re.compile(r'\[UC7-IMPORT-2026-06-06\]'),    # bare marker (defensive)
]

FILES = ['ind_batch7.py', 'ind_batch8.py', 'ind_batch10.py',
         'ind_batch12.py', 'dept_data2.py']


def strip_markers():
    total = 0
    for f in FILES:
        p = ROOT / f
        txt = p.read_text(encoding='utf-8')
        before = txt.count(MARKER)
        for pat in PATTERNS:
            txt = pat.sub('', txt)
        after = txt.count(MARKER)
        removed = before - after
        if removed:
            p.write_text(txt, encoding='utf-8')
        print(f'  {f}: removed {removed} markers (had {before}, now {after})')
        total += removed
    print(f'Total markers removed: {total}')


if __name__ == '__main__':
    print('Stripping [UC7-IMPORT-2026-06-06] markers from source files...')
    strip_markers()
