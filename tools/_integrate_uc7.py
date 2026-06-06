"""One-shot integration script: append new UC7-style prompts from extracted demos
into existing Zava entry tool blocks.

For each (file, entry_id, tool_type), append:
  - one English prompt to prompts list
  - one Bahasa Indonesia prompt to promptsID list
  - one persona name to persona / personaID lists

Uses regex with structural anchors. Idempotent guard: skips if MARKER is found.
"""
from __future__ import annotations
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Marker placed in inserted prompts so re-runs skip already-integrated entries
MARKER = ''  # deprecated; idempotency now via prompt tail-match

# ─── Verbatim Bahasa Indonesia prompts (from saved customer demos) ─────────
SITE1_RETAIL_BI = '''Berperan sebagai retail strategy analyst untuk General Manager · Retail Operations dari Zava Lifestyle Retail.

Skenario: developer mall menawarkan kita anchor unit (450 sqm, Ground Floor) di mall lifestyle baru yang akan dibuka Q4 2026 di Surabaya Barat — catchment ~1,2 juta middle-class dalam radius 5km, proyeksi footfall mall 800k/bulan saat matang. Lease: IDR 18 miliar selama 5 tahun. Estimasi CapEx fit-out: IDR 12 miliar.

Gunakan peer benchmark dari /RT_04_Promotion_ROI_Model.xlsx dan performa same-store kita dari /RT_01_Store_Performance.xlsx.

Buat decision pack 1 halaman untuk GM dengan:
1. Catchment & competition fit (vs overlap Tunjungan + Pakuwon Surabaya)
2. Brand mix yang direkomendasikan untuk format ini (4-5 brand dari portfolio kita)
3. Forecast SSS Tahun 1 / Tahun 2 / Tahun 3 dengan asumsi yang jelas
4. Total CapEx + IRR + simple payback
5. Top 3 risiko & satu mitigasi masing-masing
6. Rekomendasi GM yang tegas: GO / NO-GO / CONDITIONAL — dengan syarat spesifik

Tandai setiap asumsi [ASSUMPTION:...]. Tidak boleh ada angka karangan. Format: Word doc 1 halaman. '''

SITE1_RETAIL_EN = '''Act as a retail strategy analyst for the General Manager · Retail Operations of Zava Lifestyle Retail.

Scenario: a mall developer has offered us an anchor unit (450 sqm, Ground Floor) in a new lifestyle mall opening Q4 2026 in West Surabaya — catchment ~1.2M middle-class within 5km, mall footfall forecast 800k/month at maturity. Lease: IDR 18bn over 5 years. Fit-out CapEx estimate: IDR 12bn.

Use peer benchmarks from /RT_04_Promotion_ROI_Model.xlsx and our same-store performance from /RT_01_Store_Performance.xlsx.

Build a 1-page GM decision pack with:
1. Catchment & competition fit (vs overlap with Tunjungan + Pakuwon Surabaya)
2. Recommended brand mix for this format (4-5 brands from our portfolio)
3. SSS forecast Year 1 / Year 2 / Year 3 with explicit assumptions
4. Total CapEx + IRR + simple payback
5. Top 3 risks & one mitigation each
6. Decisive GM recommendation: GO / NO-GO / CONDITIONAL — with specific conditions

Tag every assumption [ASSUMPTION:...]. No fabricated numbers. Format: 1-page Word doc. '''

SITE2_GEO_BI = '''Berperan sebagai Plant Reliability lead yang mendukung General Manager · Plant Operations dari Zava Power.

Kita ada quarterly PPA review dengan PLN dalam 5 hari. Gunakan /POW_02_Plant_Availability_Tracker.xlsx (Plant Availability %, Net Generation GWh, Forced Outage Rate %, Specific Steam Use, TRIR) dan /POW_05_Off_Taker_Negotiation_Brief.docx (konteks steam-decline).

Hasilkan tiga artefak:

1. SURAT KEPATUHAN PPA KUARTAL PLN (Word doc, ~1,5 halaman):
 - Availability plant per plant vs MW kontrak PPA
 - Net generation vs nominated profile
 - Kejadian force-majeure dan dampaknya (sebutkan spesifik Wayang Windu / Salak / Darajat)
 - Rencana remediasi untuk underperformance
 - Tone: faktual, regulatory, tanpa bahasa marketing

2. PAKET Q&A REGULATOR (Word doc):
 - 10 pertanyaan yang kemungkinan ditanyakan PLN, dengan jawaban kita
 - Kelompokkan: availability, safety, ESG / Scope 1/2, kontrak, komitmen ke depan

3. ONE-PAGER BOARD — KASUS MITIGASI STEAM-DECLINE (Word doc, 1 halaman):
 - Masalah dalam 3 baris
 - Tiga opsi (do nothing / mid-life workover / make-up well baru) dengan biaya & MW recovery
 - Opsi rekomendasi dengan payback dan IRR
 - Keputusan yang diminta dari Board

Tandai setiap asumsi [ASSUMPTION:...]. Jangan mengada-ada angka KPI — pakai apa yang ada di workbook. '''

SITE2_GEO_EN = '''Act as Plant Reliability lead supporting the General Manager · Plant Operations of Zava Power.

The quarterly PPA review with PLN is in 5 days. Use /POW_02_Plant_Availability_Tracker.xlsx (Plant Availability %, Net Generation GWh, Forced Outage Rate %, Specific Steam Use, TRIR) and /POW_05_Off_Taker_Negotiation_Brief.docx for steam-decline context.

Produce three artefacts:

1. PLN QUARTERLY PPA COMPLIANCE LETTER (Word doc, ~1.5 pages):
 - Plant-by-plant availability vs PPA contracted MW
 - Net generation vs nominated profile
 - Force-majeure events and their impact (call out Wayang Windu / Salak / Darajat specifically)
 - Remediation plan for underperformance
 - Tone: factual, regulatory, no marketing language

2. REGULATOR Q&A PACK (Word doc):
 - 10 likely PLN questions with our answers
 - Grouped: availability, safety, ESG / Scope 1/2, contract, forward commitments

3. BOARD ONE-PAGER — STEAM-DECLINE MITIGATION CASE (Word doc, 1 page):
 - Problem in 3 lines
 - Three options (do nothing / mid-life workover / new make-up well) with cost & MW recovery
 - Recommended option with payback and IRR
 - Decision requested from the Board

Tag every assumption [ASSUMPTION:...]. Do not fabricate KPI numbers — use what is in the workbook. '''

SITE3_PIZZA_BI = '''Berperan sebagai Marketing & Ops planner untuk General Manager · Operations & Marketing dari Zava Food (lini QSR Pizza).

Lebaran 2026 tinggal 4 minggu lagi. Gunakan /FMCG_02_SKU_Margin_Tracker.xlsx (AOV per outlet, food cost %, delivery mix %, CSAT) dan /FMCG_05_FY2026_Promo_Guardrails.docx untuk konteks.

Hasilkan promo pack siap launch:

1. DESAIN PROMO
 - 3 bundle promo (keluarga / berdua / solo) dengan menu, target AOV, food-cost %, marjin kotor
 - Price ladder vs menu saat ini — sebutkan risiko cannibalisation
 - Durasi & wave roll-out (Jakarta dulu, lalu kota sekunder)

2. CHANNEL COPY
 - GoFood listing title + description (maks 90 karakter title, 220 karakter desc)
 - GrabFood listing title + description
 - Caption Instagram × 3 varian (hangat/jenaka/Hari-Raya yang santun)
 - Copy push notification untuk app

3. PAKET BRIEFING OUTLET
 - Checklist operasional 1 halaman (prep · staffing · POS · stock-up bahan)
 - Talking points untuk briefing tim outlet
 - Rencana sampling quality-control

4. TABEL FORECAST CANNIBALISATION
 - Outlet per outlet: ekspektasi lift vs cannibalisation menu reguler, dampak AOV bersih

5. SCORECARD LAUNCH
 - 5 KPI untuk dipantau 7 hari pertama, dengan threshold merah/amber/hijau

Tandai setiap asumsi [ASSUMPTION:...]. Tone: percaya diri, food-first, tidak boleh rasis atau tone-deaf terhadap audiens Muslim Indonesia. '''

SITE3_PIZZA_EN = '''Act as a Marketing & Ops planner for the General Manager · Operations & Marketing of Zava Food (QSR Pizza line).

Lebaran 2026 is 4 weeks away. Use /FMCG_02_SKU_Margin_Tracker.xlsx (AOV per outlet, food cost %, delivery mix %, CSAT) and /FMCG_05_FY2026_Promo_Guardrails.docx for context.

Produce a launch-ready promo pack:

1. PROMO DESIGN
 - 3 promo bundles (family / duo / solo) with menu, target AOV, food-cost %, gross margin
 - Price ladder vs current menu — call out cannibalisation risk
 - Duration & wave roll-out (Jakarta first, then secondary cities)

2. CHANNEL COPY
 - GoFood listing title + description (max 90 char title, 220 char desc)
 - GrabFood listing title + description
 - Instagram caption × 3 variants (warm / playful / respectful Hari Raya tone)
 - Push notification copy for app

3. OUTLET BRIEFING PACK
 - 1-page operational checklist (prep · staffing · POS · ingredient stock-up)
 - Talking points for outlet team briefing
 - Quality-control sampling plan

4. CANNIBALISATION FORECAST TABLE
 - Outlet by outlet: expected lift vs cannibalisation of regular menu, net AOV impact

5. LAUNCH SCORECARD
 - 5 KPIs to monitor for the first 7 days, with red/amber/green thresholds

Tag every assumption [ASSUMPTION:...]. Tone: confident, food-first, never racist or tone-deaf to the Indonesian Muslim audience. '''

SITE4_MINING_BI = '''Berperan sebagai Bid Manager yang mendukung General Manager · Operations dari Zava Mining (lini mining services).

Kita menanggapi RFP EPC 240 halaman dari klien gold mining untuk paket open-pit overburden + ore-haul, durasi 36 bulan, armada ~120 unit, lokasi Kalimantan Timur. Submission dalam 14 hari.

Gunakan /COAL_05_Marketing_Pricing_Pack.xlsx (peer benchmark vs Pamapersada, BUMA, Thiess) dan /COAL_06_Stakeholder_Holding_Lines.docx (narasi kapabilitas kita).

Hasilkan empat artefak:

1. WIN-THEMES (1 halaman)
 - Prioritas yang disebut klien (safety, cost, schedule, ESG) — diranking
 - 3 win-theme kita yang paling berdampak dengan bukti spesifik (project / KPI)
 - 2 kelemahan kompetitor yang bisa kita highlight (secara faktual)

2. BID EXECUTIVE SUMMARY (Word doc, 2 halaman)
 - Opening kuat yang merujuk pada bahasa klien sendiri
 - Mengapa kita (3 alasan, anchored ke bukti)
 - Pendekatan schedule & mobilisasi
 - Komitmen Safety & ESG
 - Pricing positioning (tanpa angka — itu terpisah)
 - Closing call-to-action

3. COMPLIANCE MATRIX STARTER (tabel)
 - Tarik setiap requirement bernomor dari spec RFP
 - Map ke: Compliant / Compliant-with-comment / Non-compliant
 - Pre-fill respon standar kita di mana sudah ada
 - Tandai 5 item paling kontensius untuk legal review

4. RISK REGISTER (top 10)
 - Operasional, komersial, HSE, regulatori, cuaca/musim
 - Untuk masing-masing: probabilitas, dampak, mitigasi, owner

Tandai setiap asumsi [ASSUMPTION:...]. Gunakan terminologi mining-services yang presisi (Mbcm, strip ratio, OEE, TKDN, TRIR). Jangan mengada-ada riwayat project. '''

SITE4_MINING_EN = '''Act as a Bid Manager supporting the General Manager · Operations of Zava Mining (mining services line).

We are responding to a 240-page EPC RFP from a gold-mining client for an open-pit overburden + ore-haul package, 36-month duration, ~120-unit fleet, East Kalimantan. Submission in 14 days.

Use /COAL_05_Marketing_Pricing_Pack.xlsx (peer benchmark vs Pamapersada, BUMA, Thiess) and /COAL_06_Stakeholder_Holding_Lines.docx (our capability narrative).

Produce four artefacts:

1. WIN-THEMES (1 page)
 - Client-stated priorities (safety, cost, schedule, ESG) — ranked
 - Our top 3 most impactful win-themes with specific evidence (project / KPI)
 - 2 competitor weaknesses we can highlight (factually)

2. BID EXECUTIVE SUMMARY (Word doc, 2 pages)
 - Strong opening referencing the client's own language
 - Why us (3 reasons, anchored to evidence)
 - Schedule & mobilisation approach
 - Safety & ESG commitments
 - Pricing positioning (no numbers — that is separate)
 - Closing call-to-action

3. COMPLIANCE MATRIX STARTER (table)
 - Pull every numbered requirement from the RFP spec
 - Map to: Compliant / Compliant-with-comment / Non-compliant
 - Pre-fill our standard response where one exists
 - Flag the 5 most contentious items for legal review

4. RISK REGISTER (top 10)
 - Operational, commercial, HSE, regulatory, weather/seasonal
 - For each: probability, impact, mitigation, owner

Tag every assumption [ASSUMPTION:...]. Use precise mining-services terminology (Mbcm, strip ratio, OEE, TKDN, TRIR). Do not fabricate project history. '''


# ─── Site 5 — Legal (multiple UCs into dept-legal) ──────────────────────────

LEG_UC2_MEMO_BI = '''/LEG_07_Mining_Regulation_Brief.docx /LEG_08_Legal_Knowledge_Base.docx /LEG_09_Legal_Memo_Template.docx — Berdasarkan ketiga dokumen ini, susun Legal Memo lengkap (struktur IRAC) yang ditujukan kepada Direktur Utama Grup. Identifikasi 3 isu hukum paling kritis terkait Permen ESDM No. 7 Tahun 2026, lalu untuk masing-masing sebutkan: (a) pasal spesifik yang terdampak, (b) referensi SOP/kebijakan internal, dan (c) yurisprudensi Mahkamah Agung relevan. Isi seluruh 6 bagian template: I. Latar Belakang, II. Pertanyaan Hukum, III. Analisis Hukum (IRAC), IV. Kesimpulan, V. Rekomendasi & Mitigasi Risiko (sertakan tabel risk register: Risk ID | Deskripsi | Severity | Owner | Mitigasi | Tenggat dengan minimal 6 risiko), VI. Limitasi & Disclaimer. Bahasa hukum Indonesia formal. Maksimum 1,5 halaman. '''

LEG_UC2_MEMO_EN = '''/LEG_07_Mining_Regulation_Brief.docx /LEG_08_Legal_Knowledge_Base.docx /LEG_09_Legal_Memo_Template.docx — Based on these three documents, draft a full IRAC-structured Legal Memo addressed to the Group Managing Director. Identify the 3 most critical legal issues under Permen ESDM No. 7 of 2026, and for each state: (a) the specific clause impacted, (b) the relevant internal SOP/policy reference, and (c) relevant Supreme Court jurisprudence. Fill all 6 template sections: I. Background, II. Legal Questions, III. Legal Analysis (IRAC), IV. Conclusion, V. Recommendation & Risk Mitigation (include risk register table: Risk ID | Description | Severity | Owner | Mitigation | Deadline with at least 6 risks), VI. Limitations & Disclaimer. Formal Indonesian legal register. Maximum 1.5 pages. '''

LEG_UC3_NDA_BI = '''/LEG_10_NDA_Draft.docx /LEG_11_MA_Playbook.docx — Bandingkan NDA counterparty dengan M&A Playbook v4.0 kita. Hasilkan: (1) tabel red-flag dengan kolom Klausul # | Isu | Alasan melanggar Playbook | Usulan mark-up; (2) rewrite klausul 3 (Jangka Waktu), 5 (Indemnity), 6 (Hukum & Penyelesaian Sengketa), 7 (Eksklusivitas), 9 (Pengalihan) dalam gaya mark-up — penambahan tebal, penghapusan dicoret; (3) email pengantar bilingual (BI di atas, English di bawah) ke counterparty merangkum 5 amandemen utama dengan justifikasi singkat berdasarkan KUHPerdata Pasal 1247–1248, POJK 17/2020, dan UU PT 40/2007. Usulkan call 30 menit dalam 5 hari kerja. '''

LEG_UC3_NDA_EN = '''/LEG_10_NDA_Draft.docx /LEG_11_MA_Playbook.docx — Compare the counterparty NDA against our M&A Playbook v4.0. Produce: (1) red-flag table with columns Clause # | Issue | Why it violates Playbook | Proposed mark-up; (2) rewrite clauses 3 (Term), 5 (Indemnity), 6 (Governing Law & Dispute), 7 (Exclusivity), 9 (Assignment) in mark-up style — additions bold, deletions struck-through; (3) bilingual cover email (Bahasa Indonesia above, English below) to the counterparty summarising 5 key amendments with brief justification grounded in KUHPerdata Articles 1247-1248, POJK 17/2020, and UU PT 40/2007. Propose a 30-minute call within 5 business days. '''

LEG_UC4_LITIG_BI = '''Profilkan /LEG_12_Litigation_Cases.xlsx (50 kasus, 6 anak holding). Mode Plan: susun langkah analisis dan konfirmasi sebelum eksekusi. Lalu jalankan: (1) sheet Summary dengan total kasus, ongoing vs closed, breakdown per Anak_Holding, breakdown per Case_Type, total exposure klaim (IDR Bn), total settlement, win rate keseluruhan dengan conditional formatting (hijau ≥ 60%, kuning 40-60%, merah < 40%); (2) rata-rata durasi per Case_Type & Forum_Level; (3) top 5 kasus ongoing high-value berdasarkan Claim_Amount; (4) win/loss rate per Anak_Holding; (5) flag "Aging" untuk kasus dengan Duration_Days > 730; (6) bar chart total exposure per Province. Kemudian gunakan Analyst Agent untuk root cause analysis: 3 akar penyebab teratas yang memicu eksposur tertinggi, dengan total claim, rata-rata durasi, rasio menang/kalah; rekomendasikan 2 tindakan preventif per akar penyebab dengan sitasi UU/PP/Permen. '''

LEG_UC4_LITIG_EN = '''Profile /LEG_12_Litigation_Cases.xlsx (50 cases, 6 holding subsidiaries). Plan mode: outline the analysis steps and confirm before executing. Then run: (1) Summary sheet with total cases, ongoing vs closed, breakdown by subsidiary, breakdown by Case_Type, total claim exposure (IDR Bn), total settlement, overall win rate with conditional formatting (green ≥ 60%, amber 40-60%, red < 40%); (2) average duration by Case_Type & Forum_Level; (3) top 5 ongoing high-value cases by Claim_Amount; (4) win/loss rate by subsidiary; (5) flag "Aging" for cases with Duration_Days > 730; (6) bar chart of total exposure by Province. Then use Analyst Agent for root-cause analysis: top 3 root causes driving highest exposure, with total claim, average duration, win/loss ratio; recommend 2 preventive actions per root cause with UU/PP/Permen citations. '''

LEG_UC5_DASH_BI = '''Buatkan saya "Executive Legal Dashboard" untuk Direktur Utama Grup. Susun rencana, konfirmasi tiap langkah, lalu eksekusi: (1) Researcher menarik status terbaru Permen ESDM No. 7 Tahun 2026 + setiap surat edaran/keputusan dirjen terkait; (2) Analyst agent pada /LEG_12_Litigation_Cases.xlsx untuk hitung total exposure (IDR Bn), win rate keseluruhan, top 5 ongoing high-value, breakdown per Case_Type, tren 12 bulan kasus baru; (3) dari /LEG_13_Legal_Sync_Transcript.docx ekstrak 7 action items terbuka dengan owner & deadline; (4) hasilkan 1 halaman HTML self-contained "Executive Legal Dashboard — Mei 2026" dengan 4 KPI tile (Total Exposure, Win Rate, Ongoing Cases, Open Actions), tabel Top-5 ongoing, bar chart exposure per Case_Type, panel Regulatory Watchlist, daftar Open Action Items. Tema navy gelap + putih, font Inter/Segoe UI. Inline CSS + SVG. Tanpa dependensi eksternal. (5) simpan sebagai LEG_Dashboard.html di OneDrive. '''

LEG_UC5_DASH_EN = '''Build me an "Executive Legal Dashboard" for the Group Managing Director. Plan the steps, confirm each one, then execute: (1) Researcher pulls latest status of Permen ESDM No. 7 of 2026 + every relevant circular/director-general decision; (2) Analyst agent on /LEG_12_Litigation_Cases.xlsx to compute total exposure (IDR Bn), overall win rate, top 5 ongoing high-value, Case_Type breakdown, 12-month new-case trend; (3) from /LEG_13_Legal_Sync_Transcript.docx extract 7 open action items with owner & deadline; (4) generate one self-contained HTML page "Executive Legal Dashboard — May 2026" with 4 KPI tiles (Total Exposure, Win Rate, Ongoing Cases, Open Actions), Top-5 ongoing table, exposure-by-Case_Type bar chart, Regulatory Watchlist panel, Open Action Items list. Dark navy + white theme, Inter/Segoe UI font. Inline CSS + SVG. No external dependencies. (5) Save as LEG_Dashboard.html in OneDrive. '''

LEG_UC6_AGENT_BI = '''Buat agent baru bernama "Group Legal Counsel". Description: Asisten legal internal untuk Divisi Corporate Legal Grup, ter-grounding pada regulasi Indonesia dan Legal Knowledge Base internal. Instructions: (1) selalu jawab dalam Bahasa Indonesia kecuali pertanyaan dalam English; (2) sitasi spesifik UU, PP, Permen ESDM, POJK, KUHPerdata, atau Putusan MA pada setiap jawaban hukum; (3) gunakan struktur IRAC (Issue–Rule–Application–Conclusion) untuk setiap legal opinion; (4) bila pertanyaan butuh regulasi terbaru di luar knowledge base, sebutkan demikian dan rekomendasikan eskalasi ke VP Corporate Legal; (5) jangan pernah berikan saran definitif strategi litigasi tanpa flag bahwa internal counsel review diperlukan. Tone: Profesional, presisi, register hukum Indonesia formal. Knowledge: lampirkan /LEG_08_Legal_Knowledge_Base.docx, /LEG_09_Legal_Memo_Template.docx, /LEG_11_MA_Playbook.docx, /LEG_12_Litigation_Cases.xlsx. Aktifkan "Always cite sources". '''

LEG_UC6_AGENT_EN = '''Create a new agent named "Group Legal Counsel". Description: Internal legal assistant for the Group Corporate Legal Division, grounded on Indonesian regulation and our internal Legal Knowledge Base. Instructions: (1) always answer in Bahasa Indonesia unless asked in English; (2) cite the specific UU, PP, Permen ESDM, POJK, KUHPerdata, or Putusan MA for every legal answer; (3) use IRAC structure (Issue–Rule–Application–Conclusion) for any legal opinion; (4) if the question requires updated regulation outside the knowledge base, say so and recommend escalation to the VP Corporate Legal; (5) never give definitive litigation-strategy advice without flagging that internal counsel review is required. Tone: Professional, precise, formal Indonesian legal register. Knowledge: attach /LEG_08_Legal_Knowledge_Base.docx, /LEG_09_Legal_Memo_Template.docx, /LEG_11_MA_Playbook.docx, /LEG_12_Litigation_Cases.xlsx. Turn "Always cite sources" ON. '''


# ─── Integration spec ────────────────────────────────────────────────────────
# Each tuple: (file, ind_id, tool_type, prompt_en, prompt_id, persona_name)
INTEGRATIONS = [
    # Site 1 — retail-grocery T_CHAT (Free Chat new-store decision pack)
    ('ind_batch8.py', 'retail-grocery', 'T_CHAT',
     SITE1_RETAIL_EN, SITE1_RETAIL_BI, 'Pak Andi Wijaya'),

    # Site 2 — power-utilities T_WORD (PPA compliance briefing pack)
    ('ind_batch12.py', 'power-utilities', 'T_WORD',
     SITE2_GEO_EN, SITE2_GEO_BI, 'Pak Hendra Setiawan'),

    # Site 3 — food-fmcg T_PPT (Lebaran promo)
    ('ind_batch10.py', 'food-fmcg', 'T_PPT',
     SITE3_PIZZA_EN, SITE3_PIZZA_BI, 'Bu Lisa Hartono'),

    # Site 4 — coal-mining T_WORD (EPC bid response)
    ('ind_batch7.py', 'coal-mining', 'T_WORD',
     SITE4_MINING_EN, SITE4_MINING_BI, 'Pak Surya Wibawa'),

    # Site 5 — dept-legal multi-UC integration
    ('dept_data2.py', 'dept-legal', 'T_WORD',
     LEG_UC2_MEMO_EN, LEG_UC2_MEMO_BI, 'Ratna Sari'),
    ('dept_data2.py', 'dept-legal', 'T_OUTLOOK',
     LEG_UC3_NDA_EN, LEG_UC3_NDA_BI, 'Ratna Sari'),
    ('dept_data2.py', 'dept-legal', 'T_EXCEL',
     LEG_UC4_LITIG_EN, LEG_UC4_LITIG_BI, 'Ratna Sari'),
    ('dept_data2.py', 'dept-legal', 'T_COWORK',
     LEG_UC5_DASH_EN, LEG_UC5_DASH_BI, 'Ratna Sari'),
    ('dept_data2.py', 'dept-legal', 'T_WORD_AGT',
     LEG_UC6_AGENT_EN, LEG_UC6_AGENT_BI, 'Ratna Sari'),
]


# ─── Engine ──────────────────────────────────────────────────────────────────
def find_balanced(text: str, start: int, opener: str = '(', closer: str = ')') -> int:
    """Return index of the closer that balances the opener at `start`. start points AT the opener."""
    depth = 0
    in_str = None
    i = start
    n = len(text)
    while i < n:
        c = text[i]
        # crude string skip
        if in_str:
            if c == '\\':
                i += 2
                continue
            if c == in_str:
                in_str = None
        elif c in ('"', "'"):
            in_str = c
        elif c == opener:
            depth += 1
        elif c == closer:
            depth -= 1
            if depth == 0:
                return i
        i += 1
    raise ValueError(f"Unbalanced {opener!r} starting at {start}")


def find_ind_block(text: str, ind_id: str) -> tuple[int, int]:
    """Return (start, end) indices spanning the whole ind('<id>', ...) call.
    start = position of 'ind(' ; end = index AFTER the matching ')'."""
    pat = re.compile(r"ind\(\s*['\"]" + re.escape(ind_id) + r"['\"]\s*,")
    m = pat.search(text)
    if not m:
        raise ValueError(f"Could not find ind('{ind_id}', ...) call")
    paren_start = m.start() + len("ind") - 1  # nope, we want the '('
    paren_start = m.start() + len("ind")
    if text[paren_start] != '(':
        # locate '(' between m.start() and the first arg
        paren_start = text.index('(', m.start())
    end = find_balanced(text, paren_start, '(', ')')
    return m.start(), end + 1


def find_tool_block(text: str, range_start: int, range_end: int, tool_type: str) -> tuple[int, int]:
    """Return (start, end) of `tool(<TYPE>, ...)` call inside the given range.
    start = position of 'tool(' ; end = position AFTER matching ')'."""
    sub = text[range_start:range_end]
    pat = re.compile(r"tool\(\s*" + re.escape(tool_type) + r"\b")
    m = pat.search(sub)
    if not m:
        raise ValueError(f"Could not find tool({tool_type}, ...) inside ind block")
    abs_start = range_start + m.start()
    paren_start = text.index('(', abs_start)
    end = find_balanced(text, paren_start, '(', ')')
    return abs_start, end + 1


def insert_into_list(text: str, list_open_idx: int) -> int:
    """Given index of a `[`, return the index of its matching `]`."""
    return find_balanced(text, list_open_idx, '[', ']')


def patch_tool_block(text: str, t_start: int, t_end: int,
                     prompt_en: str, prompt_id: str, persona: str) -> str:
    """Mutate the given tool() span: append new prompt to prompts list, promptsID list,
    and persona/personaID lists. Returns new full text."""
    block = text[t_start:t_end]

    # ── 1. prompts list (the first '[' after the tool name+lic+acct) ──────
    # Find the first '[' inside block — that opens the prompts list.
    bracket_start_rel = block.index('[')
    bracket_start_abs = t_start + bracket_start_rel
    bracket_end_abs = insert_into_list(text, bracket_start_abs)

    # Insertion: before bracket_end_abs, append ",\n        {NEW_PROMPT}\n      "
    en_dict = "{'instr':'', 'prompt': " + repr(prompt_en) + "}"
    new_text = text[:bracket_end_abs] + ",\n        " + en_dict + "\n      " + text[bracket_end_abs:]

    # Recompute offsets after first insertion. Search from bracket_start_abs onward in new_text.
    # We need to re-locate promptsID, persona, personaID in new_text.
    # The tool block now ends LATER by len(insertion).
    insertion_len = len(",\n        " + en_dict + "\n      ")
    t_end_new = t_end + insertion_len

    # ── 2. promptsID list ──────────────────────────────────────────────────
    pid_match = re.search(r"promptsID\s*=\s*\[", new_text[t_start:t_end_new])
    if pid_match:
        pid_open_abs = t_start + pid_match.end() - 1  # index of '['
        pid_close_abs = insert_into_list(new_text, pid_open_abs)
        id_dict = "{'instr':'', 'prompt': " + repr(prompt_id) + "}"
        new_text = (new_text[:pid_close_abs]
                    + ",\n        " + id_dict + "\n      "
                    + new_text[pid_close_abs:])
        insertion_len2 = len(",\n        " + id_dict + "\n      ")
        t_end_new += insertion_len2

    # ── 3. persona list (append name) ─────────────────────────────────────
    persona_match = re.search(r"persona\s*=\s*\[([^\]]*)\]", new_text[t_start:t_end_new])
    if persona_match:
        list_content = persona_match.group(1).rstrip()
        new_list_content = list_content + (', ' if list_content.strip() else '') + repr(persona)
        new_chunk = f"persona=[{new_list_content}]"
        old_chunk = persona_match.group(0)
        # only replace the first occurrence within the tool block
        before = new_text[:t_start]
        within = new_text[t_start:t_end_new].replace(old_chunk, new_chunk, 1)
        after = new_text[t_end_new:]
        delta = len(within) - (t_end_new - t_start)
        new_text = before + within + after
        t_end_new += delta

    # ── 4. personaID list (append name) ───────────────────────────────────
    pidp_match = re.search(r"personaID\s*=\s*\[([^\]]*)\]", new_text[t_start:t_end_new])
    if pidp_match:
        list_content = pidp_match.group(1).rstrip()
        new_list_content = list_content + (', ' if list_content.strip() else '') + repr(persona)
        new_chunk = f"personaID=[{new_list_content}]"
        old_chunk = pidp_match.group(0)
        before = new_text[:t_start]
        within = new_text[t_start:t_end_new].replace(old_chunk, new_chunk, 1)
        after = new_text[t_end_new:]
        new_text = before + within + after

    return new_text


def integrate_one(file_path: Path, ind_id: str, tool_type: str,
                  prompt_en: str, prompt_id: str, persona: str) -> tuple[bool, str]:
    text = file_path.read_text(encoding='utf-8')
    if prompt_en[-80:] in text and prompt_id[-80:] in text:
        return False, f"already integrated (tail match): {file_path.name} :: {ind_id} :: {tool_type}"
    ind_start, ind_end = find_ind_block(text, ind_id)
    t_start, t_end = find_tool_block(text, ind_start, ind_end, tool_type)
    new_text = patch_tool_block(text, t_start, t_end, prompt_en, prompt_id, persona)
    file_path.write_text(new_text, encoding='utf-8')
    return True, f"integrated: {file_path.name} :: {ind_id} :: {tool_type} :: persona={persona}"


def main():
    print(f"=== UC7 Integration ({len(INTEGRATIONS)} prompts) ===\n")
    for spec in INTEGRATIONS:
        fname, ind_id, tool_type, p_en, p_id, persona = spec
        path = ROOT / fname
        try:
            changed, msg = integrate_one(path, ind_id, tool_type, p_en, p_id, persona)
            sym = '✓' if changed else '⊝'
            print(f"  {sym} {msg}")
        except Exception as e:
            print(f"  ✗ FAILED {fname} :: {ind_id} :: {tool_type} → {e}")


if __name__ == '__main__':
    main()
