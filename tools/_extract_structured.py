"""Structured extraction of customer prompts.

For each customer page/doc:
- Walk the document/HTML, group prompts by exercise/section
- Output a structured JSON with: source, exercise, tool, instr, prompt text

Then compare to what the hub already has for the target Zava industry/dept.
"""
import re, sys, html as htmlmod, json
from pathlib import Path
from docx import Document

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

BASE = Path(r"C:\Users\peiyiyap\OneDrive - Microsoft\Documents\Customers")

def extract_kibb():
    """KIBB uses <div class="prompt-box"> wrappers."""
    html = (BASE / "KIBB" / "KIBB C-Suite Demo" / "index.html").read_text(encoding='utf-8', errors='replace')
    # Patterns: <div class="prompt-box" id="pN-M">... <button>📋 Copy</button> PROMPT TEXT </div>
    matches = re.findall(
        r'<div\s+class="prompt-box"\s+id="(p\d+-\d+)"[^>]*>.*?Copy</button>(.*?)</div>',
        html, re.S)
    prompts = []
    for pid, raw in matches:
        clean = re.sub(r'<[^>]+>', '', raw).strip()
        clean = htmlmod.unescape(clean)
        # Exercise + task numbers
        ex_no, task_no = pid[1:].split('-')
        if len(clean) > 30:
            prompts.append({'exercise': int(ex_no), 'task': int(task_no), 'id': pid, 'len': len(clean), 'text': clean})
    return sorted(prompts, key=lambda p: (p['exercise'], p['task']))

def extract_klk():
    html = (BASE / "KLK" / "KLK Demo" / "contoso-cowork-immersion" / "index.html").read_text(encoding='utf-8', errors='replace')
    # Look for <pre>, <code>, .prompt-box
    candidates = []
    for pat in [r'<pre[^>]*>(.*?)</pre>', r'<div[^>]+class="[^"]*prompt[^"]*"[^>]*>(.*?)</div>']:
        for m in re.findall(pat, html, re.S):
            clean = re.sub(r'<[^>]+>', '', m).strip()
            clean = htmlmod.unescape(clean)
            clean = re.sub(r'Copy\s*$', '', clean).strip()
            if len(clean) > 100:
                candidates.append(clean)
    # Dedupe by first 80 chars
    seen = set(); uniq = []
    for c in candidates:
        k = c[:80]
        if k not in seen:
            seen.add(k); uniq.append({'len': len(c), 'text': c})
    return uniq

def extract_docx(path):
    doc = Document(str(path))
    paragraphs = []
    cur = []
    for para in doc.paragraphs:
        t = para.text.strip()
        if not t:
            if cur:
                joined = '\n'.join(cur).strip()
                if len(joined) > 50:
                    paragraphs.append(joined)
                cur = []
            continue
        cur.append(t)
    if cur:
        joined = '\n'.join(cur).strip()
        if len(joined) > 50:
            paragraphs.append(joined)
    return paragraphs

def main():
    kibb = extract_kibb()
    klk  = extract_klk()
    aster_demo = extract_docx(BASE / "PT Chandra Asri" / "Aster Demo" / "Contoso Energy and Chemical - Sample Prompts v3.docx")
    aster_cw   = extract_docx(BASE / "PT Chandra Asri" / "Aster Demo" / "Contoso Energy and Chemical - Cowork Prompts v2.docx")
    out = {
        'kibb': kibb,
        'klk': klk,
        'aster_demo': aster_demo,
        'aster_cowork': aster_cw,
    }
    out_path = Path(r"C:\Users\peiyiyap\zava-copilot-demo\tools\_customer_prompts_structured.json")
    out_path.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding='utf-8')
    print(f"Wrote: {out_path}")
    print(f"KIBB prompts: {len(kibb)}")
    print(f"KLK prompts: {len(klk)}")
    print(f"Aster Demo paragraphs: {len(aster_demo)}")
    print(f"Aster Cowork paragraphs: {len(aster_cw)}")

if __name__ == '__main__':
    main()
