"""Extract UC7-style differentiated use cases from saved demo HTML snapshots.

Outputs JSON dump per site with: section heading + verbatim prompts (from <code>/<pre>) + file refs.
"""
from bs4 import BeautifulSoup
import re
import os
import json

DEMO_DIR = '_demo_html'
SITES = [
    ('site1_retail', '01_lifestyle_retail.html'),
    ('site2_geothermal', '02_geothermal.html'),
    ('site3_pizza', '03_pizza.html'),
    ('site4_mining', '04_mining_services.html'),
]

UC7_HINTS = ['exercise 7', 'uc7', 'go/no', 'ppa', 'lebaran', 'epc', 'tender',
             'bid response', 'new-store', 'new store', 'decision pack',
             'compliance + steam', 'promo launch', 'bid response pack']


def survey(path):
    soup = BeautifulSoup(open(path, encoding='utf-8').read(), 'html.parser')
    headings = []
    for h in soup.find_all(['h1', 'h2', 'h3', 'h4']):
        t = h.get_text(' ', strip=True)
        headings.append((h.name, t))
    code_blocks = [c.get_text() for c in soup.find_all(['code', 'pre'])]
    return headings, code_blocks, soup


def main():
    out = {}
    for key, fname in SITES:
        path = os.path.join(DEMO_DIR, fname)
        headings, codes, soup = survey(path)
        out[key] = {
            'file': fname,
            'heading_count': len(headings),
            'code_count': len(codes),
            'headings': headings[:80],
            'first_codes': [c[:200] for c in codes[:5]],
        }
        # heading lookup for UC7
        candidates = [(i, t) for i, (tag, t) in enumerate(headings)
                      if any(k in t.lower() for k in UC7_HINTS)]
        out[key]['uc7_candidates'] = candidates
    print(json.dumps(out, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()
