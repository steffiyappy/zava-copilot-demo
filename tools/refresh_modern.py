"""Refresh modern-feature coverage for a single tool category. Appends ONE new
showcase prompt (EN + ID) to every tool(<TOOL>, ...) block that lacks the keywords."""
import re, glob, ast, sys, argparse, io, os

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# Category catalog: tool name + keywords to look for + new EN/ID prompts
CATEGORIES = {
    'outlook': {
        'tool': 'T_OUTLOOK',
        'keywords': ['canvas', 'first draft in canvas', 'clarifying question', 'iterate in place',
                     'kanvas', 'pertanyaan klarifikasi'],
        'en': (
            "{'instr':\"Open Outlook on the Web > **New email**. In the new **first-draft-in-canvas** experience (March 2026), Copilot drafts directly in the email body (not the small Copilot pane) "
            "and asks clarifying questions on goal, audience, and tone. Paste the prompt below and answer Copilot's follow-ups in canvas — no copy-paste.\","
            " 'prompt':\"Draft a clear stakeholder email about the most pressing issue in this scenario. Copilot, in canvas, ask me 3 clarifying questions before finalising: "
            "(1) which decision the recipient must make and by when, (2) which tone fits (firm vs. collaborative vs. supervisory), and (3) audience seniority. "
            "After I answer, refine in place — no copy-paste. End with a recommended subject line and a 1-sentence preview tuned for inbox triage.\"}"
        ),
        'id': (
            "{'instr':\"Buka Outlook on the Web > **Email Baru**. Pada pengalaman **first-draft-in-canvas** baru (Maret 2026), Copilot mengetik draft langsung di badan email "
            "(bukan di panel Copilot kecil) dan mengajukan pertanyaan klarifikasi terkait tujuan, audiens, dan nada. Tempelkan prompt di bawah dan jawab pertanyaan Copilot di kanvas — tanpa copy-paste.\","
            " 'prompt':\"Susun email pemangku kepentingan yang jelas mengenai isu paling mendesak dalam skenario ini. Copilot, di kanvas, ajukan 3 pertanyaan klarifikasi sebelum finalisasi: "
            "(1) keputusan apa yang harus diambil penerima dan kapan, (2) nada mana yang sesuai (tegas vs. kolaboratif vs. supervisori), (3) seniority audiens. "
            "Setelah saya menjawab, sempurnakan langsung di kanvas — tanpa copy-paste. Akhiri dengan rekomendasi subject line dan preview 1 kalimat yang disetel untuk triage inbox.\"}"
        ),
    },
    'excel': {
        'tool': 'T_EXCEL',
        'keywords': ['Plan mode', 'plan the approach', 'use Python', 'Python in Excel',
                     'mode Plan', 'gunakan Python', 'Python di Excel'],
        'en': (
            "{'instr':\"Stay in the same workbook (or open a fresh Excel-for-the-Web file with one of the data files attached). Open the **Copilot pane** > click the **menu above the prompt box** "
            "and pick **Plan** (May 2026). Copilot will outline a step-by-step approach BEFORE making any edits — review and approve before changes land. For the second half, add **use Python** to the prompt and Copilot will run advanced analysis directly inside the workbook.\","
            " 'prompt':\"Plan mode: outline the step-by-step approach you will take to surface the 3 most material risks in the attached workbook for this scenario — list each step as a numbered plan I can review/approve before any edit. "
            "After I approve, execute the plan and create one new sheet called 'Risk Triage' with the result. "
            "Then on a second sheet 'Advanced', **use Python** to run a 12-month rolling-trend forecast on the most material risk metric and plot it as a chart with confidence bands. "
            "Cite which input columns drive the forecast and flag any data-quality gaps that would invalidate the result.\"}"
        ),
        'id': (
            "{'instr':\"Tetap di workbook yang sama (atau buka file Excel-for-the-Web baru dengan salah satu file data terlampir). Buka **Copilot pane** > klik **menu di atas kotak prompt** "
            "dan pilih **Plan** (Mei 2026). Copilot akan menguraikan pendekatan langkah-demi-langkah SEBELUM melakukan edit — tinjau dan setujui sebelum perubahan diterapkan. Pada bagian kedua, tambahkan **use Python** ke prompt dan Copilot akan menjalankan analisis lanjutan langsung di dalam workbook.\","
            " 'prompt':\"Mode Plan: uraikan pendekatan langkah-demi-langkah yang akan Anda ambil untuk memunculkan 3 risiko paling material pada workbook terlampir untuk skenario ini — daftarkan setiap langkah sebagai plan bernomor yang dapat saya tinjau/setujui sebelum edit apa pun. "
            "Setelah saya setujui, eksekusi plan dan buat satu sheet baru bernama 'Risk Triage' dengan hasilnya. "
            "Kemudian pada sheet kedua 'Advanced', **gunakan Python** untuk menjalankan rolling-trend forecast 12 bulan terhadap metrik risiko paling material dan plot sebagai chart dengan confidence bands. "
            "Sebutkan kolom input mana yang mendorong forecast dan tandai kesenjangan kualitas data yang akan membatalkan hasilnya.\"}"
        ),
    },
    'word': {
        'tool': 'T_WORD',
        'keywords': ['Claude', 'GPT model', 'model picker', 'Edit with Copilot', 'pemilih model', 'pengubah model'],
        'en': (
            "{'instr':\"Open the Word doc > **Copilot pane**. Click the **🧠 model picker** at the top of the pane and switch to **Claude Opus 4.7** for nuanced legal/policy/board-grade rewriting. Paste the prompt below. After Copilot drafts, click **Edit with Copilot** (agent mode) for inline restructuring across the whole document in one instruction.\","
            " 'prompt':\"Using Claude Opus 4.7, rewrite the most consequential section of this document for an external audience (regulator, lender, Board-level reader) — preserve every fact, but tighten the language for clarity and remove any internal jargon. "
            "Then switch the model picker back to **GPT** and ask Copilot to produce a same-length GPT version of the SAME section so I can compare nuance side-by-side. "
            "Finally, click **Edit with Copilot** (agent mode) and ask Copilot to restructure the whole document so the executive summary lands on page 1 and the appendix moves to the end — one instruction, applied across all sections.\"}"
        ),
        'id': (
            "{'instr':\"Buka dokumen Word > **Copilot pane**. Klik **🧠 model picker** di atas panel dan beralih ke **Claude Opus 4.7** untuk penulisan ulang yang bernuansa (legal/kebijakan/grade-Direksi). Tempelkan prompt di bawah ini. Setelah Copilot membuat draft, klik **Edit with Copilot** (mode agent) untuk restrukturisasi inline pada seluruh dokumen dalam satu instruksi.\","
            " 'prompt':\"Menggunakan Claude Opus 4.7, tulis ulang bagian paling penting dari dokumen ini untuk audiens eksternal (regulator, kreditor, pembaca tingkat Direksi) — pertahankan setiap fakta, tetapi rapikan bahasanya agar jelas dan hilangkan jargon internal. "
            "Lalu kembalikan model picker ke **GPT** dan minta Copilot membuat versi GPT dengan panjang yang sama dari bagian YANG SAMA sehingga saya bisa membandingkan nuansa berdampingan. "
            "Terakhir, klik **Edit with Copilot** (mode agent) dan minta Copilot merestrukturisasi seluruh dokumen sehingga ringkasan eksekutif berada di halaman 1 dan lampiran berpindah ke akhir — satu instruksi, diterapkan pada semua bagian.\"}"
        ),
    },
    'analyst': {
        'tool': 'T_ANALYST',
        'keywords': ['Python', 'forecast', 'regression', 'dashboard', 'multi-tab', 'cross-analysis',
                     'forecasting', 'regresi'],
        'en': (
            "{'instr':\"In m365.cloud.microsoft/chat > **Agents** > **Analyst**. Upload the most data-rich file from this scenario. Analyst writes **Python** under the hood — no formula needed. Paste the prompt below.\","
            " 'prompt':\"Using Python, run a multi-tab cross-analysis on the uploaded workbook: (a) profile every numeric column for distribution and outliers, "
            "(b) detect any time-series and run a 12-period forecast on the most material metric with confidence intervals, "
            "(c) cluster the rows into 3 risk tiers via k-means on the key risk drivers, and "
            "(d) generate ONE composite dashboard (chart panel + risk-tier table) with a 5-bullet executive interpretation. "
            "Surface the Python code in a collapsible block so the analyst team can re-run / extend it.\"}"
        ),
        'id': (
            "{'instr':\"Di m365.cloud.microsoft/chat > **Agents** > **Analyst**. Unggah file paling kaya data dari skenario ini. Analyst menulis **Python** di balik layar — tidak perlu formula. Tempelkan prompt di bawah.\","
            " 'prompt':\"Menggunakan Python, jalankan multi-tab cross-analysis pada workbook yang diunggah: (a) profilkan setiap kolom numerik untuk distribusi dan outlier, "
            "(b) deteksi time-series apa pun dan jalankan forecast 12-periode terhadap metrik paling material dengan confidence interval, "
            "(c) kelompokkan baris ke dalam 3 tingkat risiko via k-means pada penggerak risiko utama, dan "
            "(d) hasilkan SATU dashboard komposit (panel chart + tabel tingkat risiko) dengan interpretasi eksekutif 5 bullet. "
            "Munculkan kode Python dalam blok yang dapat dilipat sehingga tim analis dapat menjalankan ulang / mengembangkannya.\"}"
        ),
    },
}


def find_tool_block_ranges(text, tool_name):
    ranges = []
    for m in re.finditer(rf"tool\(\s*{tool_name}\b", text):
        op = text.rfind('(', m.start(), m.end())
        if op < 0: continue
        depth = 1; j = op + 1
        while j < len(text) and depth > 0:
            ch = text[j]
            if ch == '(': depth += 1
            elif ch == ')':
                depth -= 1
                if depth == 0: ranges.append((op, j)); break
            j += 1
    return ranges


def find_list_ranges_in_tool(text, op, cl):
    span = text[op:cl+1]
    depth_paren = 0; en_open = en_close = None
    i = 0
    while i < len(span):
        ch = span[i]
        if ch == '(': depth_paren += 1
        elif ch == ')': depth_paren -= 1
        elif ch == '[' and depth_paren == 1 and en_open is None:
            en_open = i; d = 1; j = i + 1
            while j < len(span) and d > 0:
                if span[j] == '[': d += 1
                elif span[j] == ']':
                    d -= 1
                    if d == 0: en_close = j; break
                j += 1
            break
        i += 1

    id_open = id_close = None
    if en_close is not None:
        m2 = re.search(r"promptsID\s*=\s*\[", span[en_close:])
        if m2:
            id_open = en_close + m2.end() - 1
            d = 1; j = id_open + 1
            while j < len(span) and d > 0:
                if span[j] == '[': d += 1
                elif span[j] == ']':
                    d -= 1
                    if d == 0: id_close = j; break
                j += 1

    return (
        (op + en_open, op + en_close) if en_open is not None and en_close is not None else None,
        (op + id_open, op + id_close) if id_open is not None and id_close is not None else None,
    )


def block_has_keywords(text, op, cl, keywords):
    span = text[op:cl+1].lower()
    return any(k.lower() in span for k in keywords)


def inject_into_file(path, cat_info, dry=True):
    text = open(path, encoding='utf-8').read()
    ranges = find_tool_block_ranges(text, cat_info['tool'])
    if not ranges: return 0, 0
    edits_done = []
    for op, cl in reversed(ranges):
        if block_has_keywords(text, op, cl, cat_info['keywords']):
            edits_done.append('skip')
            continue
        en_range, id_range = find_list_ranges_in_tool(text, op, cl)
        if en_range is None:
            edits_done.append('skip-no-list')
            continue
        en_open, en_close = en_range
        before_close = text[max(en_open, en_close-300):en_close]
        m_indent = re.search(r"\n([ \t]+)\{['\"]instr", before_close)
        indent = m_indent.group(1) if m_indent else '        '

        new_en_block = f",\n{indent}{cat_info['en']}"
        text = text[:en_close] + new_en_block + text[en_close:]
        if id_range is not None:
            id_open, id_close = id_range
            shift = len(new_en_block)
            id_close += shift
            new_id_block = f",\n{indent}{cat_info['id']}"
            text = text[:id_close] + new_id_block + text[id_close:]
        edits_done.append('injected')

    if not dry:
        try: ast.parse(text)
        except SyntaxError as e:
            print(f"  ❌ SYNTAX ERROR in {path}: {e}"); return 0, 0
        open(path, 'w', encoding='utf-8').write(text)
    return sum(1 for e in edits_done if e == 'injected'), sum(1 for e in edits_done if e != 'injected')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--apply', action='store_true')
    ap.add_argument('--category', required=True, choices=list(CATEGORIES.keys()))
    ap.add_argument('--files', nargs='*')
    args = ap.parse_args()
    info = CATEGORIES[args.category]
    files = args.files or sorted(glob.glob('ind_batch*.py') + glob.glob('dept_data*.py'))
    total_i = total_s = 0
    for f in files:
        if not os.path.exists(f): continue
        i, s = inject_into_file(f, info, dry=not args.apply)
        total_i += i; total_s += s
        print(f"{f:30}  injected={i:2}  skipped={s:2}")
    mode = 'APPLIED' if args.apply else 'DRY-RUN'
    print(f"\n{mode} [{args.category}]: injected={total_i} skipped={total_s}")


if __name__ == '__main__': main()
