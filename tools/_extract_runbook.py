"""Extract the KLK Cowork Runbook (10 UCs, multi-step prompts) and KIBB Cowork
runbook content from the customer HTML pages into a structured JSON for
injection into the Zava hub's per-entry Cowork tool blocks.

KLK page layout: <div class="rb-detail" id="rb-N"> ... </div>
  Each contains: <h2>title</h2>, <span class="rb-cat">cat</span>,
  multiple <div class="rb-prompt-block"> with P1/P2/P3...
  Plus 'What to watch' + 'Honest framing' callouts.

KIBB page layout: <div class="prompt-box" id="pN-M"> ... </div>
  Exercises 2 and 3 are the BRC pack runbook.
"""
import re, json, html as htmlmod
from pathlib import Path

KLK = Path(r"C:\Users\peiyiyap\OneDrive - Microsoft\Documents\Customers\KLK\KLK Demo\contoso-cowork-immersion\index.html")
KIBB = Path(r"C:\Users\peiyiyap\OneDrive - Microsoft\Documents\Customers\KIBB\KIBB C-Suite Demo\index.html")
OUT = Path(r"C:\Users\peiyiyap\zava-copilot-demo\tools\_customer_runbooks.json")


def clean(t: str) -> str:
    t = re.sub(r'<button[^>]*>.*?</button>', '', t, flags=re.S)
    t = re.sub(r'<[^>]+>', '', t)
    t = htmlmod.unescape(t)
    return t.strip()


def extract_klk_runbook():
    h = KLK.read_text(encoding='utf-8', errors='replace')
    # Each UC is a <div class="rb-detail" id="rb-N">...</div>
    # Use non-greedy match up to the NEXT <div class="rb-detail" or end of section
    ucs = []
    # Split by rb-detail markers
    parts = re.split(r'<div\s+class="rb-detail"\s+id="(rb-\d+)"\s*>', h)
    # parts[0] is the preamble; parts[1] = "rb-1", parts[2] = body of rb-1, etc.
    for i in range(1, len(parts), 2):
        rid = parts[i]
        body = parts[i+1]
        # Cut the body at the start of the next rb-detail (already done by split)
        # but the LAST one bleeds into the rest of the page — cap at end of section
        end = re.search(r'</section>', body)
        if end:
            body = body[:end.start()]

        # Title
        title_m = re.search(r'<h2[^>]*>(.*?)</h2>', body, re.S)
        title = clean(title_m.group(1)) if title_m else rid

        # Category
        cat_m = re.search(r'class="rb-cat"[^>]*>(.*?)</span>', body, re.S)
        cat = clean(cat_m.group(1)) if cat_m else ''

        # Subheading
        sub_m = re.search(r'<p\s+class="rb-sub"[^>]*>(.*?)</p>', body, re.S)
        sub = clean(sub_m.group(1)) if sub_m else ''

        # Pattern
        pat_m = re.search(r'<span\s+class="pill"[^>]*>(.*?)</span>', body, re.S)
        pattern = clean(pat_m.group(1)) if pat_m else ''

        # Apps pill
        apps_m = re.search(r'<span\s+class="pill\s+blue"[^>]*>(.*?)</span>', body, re.S)
        apps = clean(apps_m.group(1)) if apps_m else ''

        # Complexity
        comp_m = re.search(r'<span\s+class="pill\s+purple"[^>]*>(.*?)</span>', body, re.S)
        complexity = clean(comp_m.group(1)) if comp_m else ''

        # Sample files
        files = []
        for f in re.finditer(r'<a\s+class="rb-file[^"]*"\s+href="[^"]+"\s+download[^>]*>(.*?)</a>', body, re.S):
            ftext = clean(f.group(1))
            # ftext looks like "XLSXSite_Alpha_Mar2026.xlsx" — strip the "XLSX" / "PDF" prefix
            ftext = re.sub(r'^(XLSX|PDF|DOCX|PPTX|MSG|EML|PNG|JPG|JSON)', '', ftext).strip()
            if ftext:
                files.append(ftext)

        # Prompts — each <div class="rb-prompt-block"> ... </div> with P-num + title + <div class="prompt">body</div>
        prompts = []
        for pb in re.finditer(
            r'<div\s+class="rb-prompt-block"[^>]*>(.*?)</div>\s*</div>',
            body, re.S):
            chunk = pb.group(1)
            num_m = re.search(r'class="rb-prompt-num"[^>]*>(.*?)</span>', chunk, re.S)
            title_m = re.search(r'class="rb-prompt-title"[^>]*>(.*?)</span>', chunk, re.S)
            text_m = re.search(r'<div\s+class="prompt"[^>]*>(.*?)(?:<button|</div>)', chunk, re.S)
            num = clean(num_m.group(1)) if num_m else ''
            ptitle = clean(title_m.group(1)) if title_m else ''
            text = clean(text_m.group(1)) if text_m else ''
            if text:
                prompts.append({'num': num, 'title': ptitle, 'text': text})

        # Callouts
        watch_m = re.search(r'class="rb-callout watch"[^>]*>(.*?)</div>', body, re.S)
        honest_m = re.search(r'class="rb-callout honest"[^>]*>(.*?)</div>', body, re.S)
        watch = clean(watch_m.group(1)) if watch_m else ''
        honest = clean(honest_m.group(1)) if honest_m else ''

        ucs.append({
            'id': rid,
            'title': title,
            'category': cat,
            'subtitle': sub,
            'pattern': pattern,
            'apps': apps,
            'complexity': complexity,
            'files': files,
            'prompts': prompts,
            'watch': watch,
            'honest': honest,
        })
    return ucs


def extract_kibb_brc():
    """Extract KIBB Exercise 2 + 3 — the Board Risk Committee runbook."""
    h = KIBB.read_text(encoding='utf-8', errors='replace')
    matches = re.findall(
        r'<div\s+class="prompt-box"\s+id="(p\d+-\d+)"[^>]*>.*?Copy</button>(.*?)</div>',
        h, re.S)
    out = []
    for pid, raw in matches:
        text = clean(raw)
        ex, task = pid[1:].split('-')
        if int(ex) in (2, 3):
            out.append({'exercise': int(ex), 'task': int(task), 'id': pid, 'text': text})
    return sorted(out, key=lambda p: (p['exercise'], p['task']))


def extract_kibb_cowork_cards():
    """Extract the 15 KIBB Cowork UCs from <article class="cw-card"> blocks
    in page-cowork. Each card has data-industry / data-dept / data-complexity,
    title, badges, description, apps, sample-files, multi-step prompts, and
    watch/honest callouts."""
    h = KIBB.read_text(encoding='utf-8', errors='replace')

    # Each card: <article class="cw-card" ...> ... </article>
    # Splitting on <article class="cw-card" markers
    parts = re.split(r'<article\s+class="cw-card"\s*([^>]*)>', h)
    cards = []
    for i in range(1, len(parts), 2):
        attrs = parts[i]
        body = parts[i+1]
        # Cut body at next </article>
        end = body.find('</article>')
        if end != -1:
            body = body[:end]

        ind_m = re.search(r'data-industry="([^"]+)"', attrs)
        dept_m = re.search(r'data-dept="([^"]+)"', attrs)
        comp_m = re.search(r'data-complexity="([^"]+)"', attrs)
        industry = ind_m.group(1) if ind_m else ''
        dept = dept_m.group(1) if dept_m else ''
        complexity = comp_m.group(1) if comp_m else ''

        num_m = re.search(r'class="cw-num"[^>]*>(.*?)</div>', body, re.S)
        title_m = re.search(r'class="cw-title"[^>]*>(.*?)</h3>', body, re.S)
        desc_m = re.search(r'class="cw-desc"[^>]*>(.*?)</p>', body, re.S)
        num = clean(num_m.group(1)) if num_m else ''
        title = clean(title_m.group(1)) if title_m else ''
        desc = clean(desc_m.group(1)) if desc_m else ''

        # Apps pills (first cw-pills block after APPS INVOLVED)
        apps_m = re.search(r'APPS INVOLVED.*?<div\s+class="cw-pills">(.*?)</div>', body, re.S)
        apps = []
        if apps_m:
            for ap in re.finditer(r'<span\s+class="app-pill"[^>]*>(.*?)</span>', apps_m.group(1), re.S):
                apps.append(clean(ap.group(1)))

        # Sample files
        files = []
        for f in re.finditer(r'<a\s+class="file-pill"[^>]*>(.*?)</a>', body, re.S):
            ft = clean(f.group(1))
            ft = re.sub(r'^(XLSX|PDF|DOCX|PPTX|MSG|EML|PNG|JPG|JSON|CSV|TXT)\s*', '', ft).strip()
            if ft:
                files.append(ft)

        # Prompts (multiple cw-prompt blocks)
        prompts = []
        for pm in re.finditer(
            r'<div\s+class="cw-prompt"[^>]*>\s*<div\s+class="cw-prompt-head"[^>]*>(.*?)</div>\s*<div\s+class="prompt-box"\s+id="([^"]+)"[^>]*>(.*?)</div>',
            body, re.S):
            head = pm.group(1)
            pid = pm.group(2)
            text_raw = pm.group(3)
            # Strip Copy button
            text_raw = re.sub(r'<button[^>]*>.*?</button>', '', text_raw, flags=re.S)
            text = clean(text_raw)
            label_m = re.search(r'class="cw-plabel"[^>]*>(.*?)</span>', head, re.S)
            label = clean(label_m.group(1)) if label_m else ''
            prompts.append({'id': pid, 'label': label, 'text': text})

        # Callouts
        watch_m = re.search(r'class="cw-callout cw-watch"[^>]*>.*?<p[^>]*>(.*?)</p>', body, re.S)
        honest_m = re.search(r'class="cw-callout cw-honest"[^>]*>.*?<p[^>]*>(.*?)</p>', body, re.S)
        watch = clean(watch_m.group(1)) if watch_m else ''
        honest = clean(honest_m.group(1)) if honest_m else ''

        # Use first prompt id's slug as card slug
        slug = ''
        if prompts:
            m = re.match(r'cw-uc-(.*?)-\d+$', prompts[0]['id'])
            slug = m.group(1) if m else prompts[0]['id']

        if title:  # skip the template/example placeholder if any
            cards.append({
                'slug': slug,
                'num': num,
                'title': title,
                'description': desc,
                'industry_tag': industry,
                'dept_tag': dept,
                'complexity': complexity,
                'apps': apps,
                'files': files,
                'prompts': prompts,
                'watch': watch,
                'honest': honest,
            })
    return cards


def main():
    out = {
        'klk_runbook': extract_klk_runbook(),
        'kibb_brc_runbook': extract_kibb_brc(),
        'kibb_cowork_cards': extract_kibb_cowork_cards(),
    }
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding='utf-8')

    def safe(s):
        return str(s).encode('ascii', 'replace').decode('ascii')

    # Summary
    print(f"Wrote: {OUT}")
    print(f"KLK UCs: {len(out['klk_runbook'])}")
    for uc in out['klk_runbook']:
        n_prompts = len(uc['prompts'])
        print(f"  {uc['id']:<8} [{safe(uc['category'])}] {safe(uc['title'])}  ({n_prompts} prompts)")
    print(f"\nKIBB BRC items: {len(out['kibb_brc_runbook'])}")
    for it in out['kibb_brc_runbook']:
        print(f"  p{it['exercise']}-{it['task']}  ({len(it['text'])} chars) {safe(it['text'][:70])}...")
    print(f"\nKIBB Cowork cards: {len(out['kibb_cowork_cards'])}")
    for c in out['kibb_cowork_cards']:
        np = len(c['prompts'])
        print(f"  {c['num']:<7} slug={c['slug']:<32} ind={c['industry_tag']:<18} dept={c['dept_tag']:<18} prompts={np}  {safe(c['title'])}")


if __name__ == '__main__':
    main()
