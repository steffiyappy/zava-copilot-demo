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


def main():
    out = {
        'klk_runbook': extract_klk_runbook(),
        'kibb_brc_runbook': extract_kibb_brc(),
    }
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding='utf-8')

    # Summary
    print(f"Wrote: {OUT}")
    print(f"KLK UCs: {len(out['klk_runbook'])}")
    for uc in out['klk_runbook']:
        n_prompts = len(uc['prompts'])
        print(f"  {uc['id']:<8} [{uc['category']}] {uc['title']}  ({n_prompts} prompts)")
    print(f"\nKIBB BRC items: {len(out['kibb_brc_runbook'])}")
    for it in out['kibb_brc_runbook']:
        print(f"  p{it['exercise']}-{it['task']}  ({len(it['text'])} chars) {it['text'][:70]}...")


if __name__ == '__main__':
    main()
