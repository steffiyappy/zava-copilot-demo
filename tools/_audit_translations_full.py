"""Comprehensive audit of EVERY localized field in data.js.

Scans every `*BM:` / `*ID:` string and array value across the entire data.js
(not just promptsBM/promptsID) — this catches whatsNew titleBM/summaryBM/tipBM,
storyboard titleBM/summaryBM, persona roleBM, top-level company/tagline/scenario,
nested exTitle/exSummary, etc.

Usage:
  python tools/_audit_translations_full.py
"""
import sys, re
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

# Reuse word lists from the original audit
from tools._audit_translations import BI_ONLY_IN_BM, BM_ONLY_IN_BI

# Skip these field names — they are codes/ids/URLs, not localized prose
SKIP_KEYS = {'id', 'badgeID', 'tagID'}  # badgeID etc are real but short — handled separately

# We'll allow short fields (badges, labels) but mark a separate bucket
SHORT_FIELDS = {'badge', 'verb', 'tag'}


def find_all_localized_fields(text):
    """Yield (key, value, kind) for every `key: 'string'` or `key: ['str',...]` 
    where key ends in BM or ID (or BI). kind in {'str','arr'}."""
    # key:  one or more letters then BM/ID at the end (case-sensitive, since
    # data.js uses titleBM not titlebm). Followed by `: ` then `'` or `[`.
    key_pat = re.compile(r"\b([a-zA-Z_]+(?:BM|ID|BI))\s*:\s*([\['])")
    for m in key_pat.finditer(text):
        key = m.group(1)
        opener = m.group(2)
        if key in SKIP_KEYS:
            continue
        start = m.end()
        if opener == "'":
            # parse single-quoted string
            j = start
            while j < len(text):
                if text[j] == '\\':
                    j += 2
                    continue
                if text[j] == "'":
                    break
                j += 1
            yield key, text[start:j], 'str'
        else:  # '['
            # parse array — pull out single-quoted strings inside
            depth = 1
            i = start
            while i < len(text) and depth > 0:
                ch = text[i]
                if ch == '[':
                    depth += 1
                elif ch == ']':
                    depth -= 1
                    if depth == 0:
                        break
                elif ch == "'":
                    j = i + 1
                    while j < len(text):
                        if text[j] == '\\':
                            j += 2; continue
                        if text[j] == "'":
                            break
                        j += 1
                    i = j
                i += 1
            body = text[start:i]
            for sm in re.finditer(r"'((?:[^'\\]|\\.)*)'", body):
                yield key, sm.group(1), 'arr'


def is_bm_key(k):
    return k.endswith('BM')


def is_bi_key(k):
    return k.endswith('ID') or k.endswith('BI')


def scan(text):
    bm_hits = defaultdict(lambda: defaultdict(int))   # word -> field -> count
    bi_hits = defaultdict(lambda: defaultdict(int))
    bm_samples = {}
    bi_samples = {}
    bm_total = bi_total = 0
    by_field_bm = defaultdict(int)
    by_field_bi = defaultdict(int)

    def _is_url(s):
        # URLs and URL-fragments must not be flagged: they are literal addresses
        # and translating tokens inside them would break the link.
        return ('http://' in s or 'https://' in s or '.aspx' in s.lower()
                or s.startswith('www.') or '/Pages/' in s)

    for key, val, kind in find_all_localized_fields(text):
        if not val.strip():
            continue
        if _is_url(val):
            continue
        if is_bm_key(key):
            bm_total += 1
            by_field_bm[key] += 1
            for w in BI_ONLY_IN_BM:
                pat = r'\b' + re.escape(w) + r'\b'
                m = re.search(pat, val, re.IGNORECASE)
                if m:
                    bm_hits[w][key] += 1
                    if w not in bm_samples:
                        idx = m.start()
                        bm_samples[w] = (key, val[max(0, idx - 40):idx + len(w) + 40])
        elif is_bi_key(key):
            bi_total += 1
            by_field_bi[key] += 1
            for w in BM_ONLY_IN_BI:
                pat = r'\b' + re.escape(w) + r'\b'
                m = re.search(pat, val, re.IGNORECASE)
                if m:
                    bi_hits[w][key] += 1
                    if w not in bi_samples:
                        idx = m.start()
                        bi_samples[w] = (key, val[max(0, idx - 40):idx + len(w) + 40])
    return (bm_total, by_field_bm, bm_hits, bm_samples,
            bi_total, by_field_bi, bi_hits, bi_samples)


def report(label, total, by_field, hits, samples):
    print(f'\n========= {label} =========')
    print(f'Total strings scanned: {total}')
    print(f'Field coverage:')
    for k, c in sorted(by_field.items(), key=lambda x: -x[1])[:20]:
        print(f'    {c:6d}  {k}')
    if not hits:
        print('OK No wrong-language words detected.')
        return 0
    flat = [(w, sum(fmap.values())) for w, fmap in hits.items()]
    flat.sort(key=lambda x: -x[1])
    print(f'Wrong-language words found:')
    grand = 0
    for w, c in flat:
        grand += c
        fields = ', '.join(f'{fk}:{fv}' for fk, fv in sorted(hits[w].items(), key=lambda x: -x[1])[:4])
        skey, sctx = samples.get(w, ('?', ''))
        sctx = sctx[:100].replace('\n', ' ')
        print(f'    {c:5d}  {w:25s}  [{fields}]   ex({skey}): ...{sctx}...')
    return grand


if __name__ == '__main__':
    data = (ROOT / 'data.js').read_text(encoding='utf-8')
    print(f'data.js loaded: {len(data):,} bytes')
    bm_total, bm_fields, bm_hits, bm_samples, bi_total, bi_fields, bi_hits, bi_samples = scan(data)
    bm_grand = report('BM-LANG FIELDS (should contain Bahasa Malaysia; flagging Indonesian words)',
                      bm_total, bm_fields, bm_hits, bm_samples)
    bi_grand = report('BI-LANG FIELDS (should contain Bahasa Indonesia; flagging Malaysian words)',
                      bi_total, bi_fields, bi_hits, bi_samples)
    print(f'\n========= GRAND TOTAL =========')
    print(f'BM-side issues (BI words in *BM fields): {bm_grand}')
    print(f'BI-side issues (BM words in *ID fields): {bi_grand}')
