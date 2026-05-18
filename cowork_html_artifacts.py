"""
cowork_html_artifacts.py

Appends ONE additional Cowork delegation prompt to every entry's Cowork tool
block. The new prompt asks Cowork to produce an interactive HTML artifact
(executive dashboard, kanban board, risk heatmap, or pipeline timeline) as a
deliverable in the chat — exercising the Frontier-tier Cowork capability of
generating runnable HTML pages alongside Word/Excel/Outlook/Teams tasks.

User asked: "Cowork is also able to produce HTML dashboards, charts, or even
kanban boards. Can you add those across the industries and departments as an
additional task under a use case?"

Architecture:
- 4 archetypes (DASHBOARD / KANBAN / HEATMAP / PIPELINE_TIMELINE).
- Per-entry routing via ARCHETYPE_BY_ID below, defaulting to DASHBOARD for any
  entry not in the table.
- Each prompt is industry-flavoured — references files / KPIs / decisions that
  fit the entry, so the HTML render shows realistic-looking content.
- Wired into build_master.py AFTER cowork_more_scenarios but BEFORE the
  cowork-approval-gate / cowork-recipient-diversification passes, so those
  later passes also process the new prompt automatically.

License: T_COWORK = FRONTIER (no change to ruleset).
Persona: util.tool()'s auto-padder (commit 79fa5f8) covers the extra prompt
without needing per-call persona array extension.

Idempotent: detects via the unique marker string "_HTMLARTIFACT_MARK".
"""

# ---------------------------------------------------------------------------
# Standard recipient + approval trail (matches cowork_more_scenarios)
# ---------------------------------------------------------------------------
_RECIP_EN = (
    " Wait for my confirmation before sending external content. "
    "Use these named recipients consistently across the email task and the Teams meeting task — "
    "Hadar (Group CFO), Sasha (Group Chief of Staff), Daichi (Head of Investor Relations), "
    "Sonia (Head of Strategy), Will (Head of Risk) and Omar (Head of Procurement) — and adapt "
    "the precise distribution per sub-task to keep each communication focused on the right audience."
)
_RECIP_ID = (
    " Tunggu konfirmasi saya sebelum mengirim konten eksternal. "
    "Gunakan penerima bernama berikut secara konsisten lintas tugas email dan tugas rapat Teams — "
    "Hadar (Direktur Keuangan Grup), Sasha (Kepala Staf Grup), Daichi (Kepala Hubungan Investor), "
    "Sonia (Kepala Strategi), Will (Kepala Risiko) dan Omar (Kepala Pengadaan) — dan sesuaikan "
    "distribusi tepat per sub-tugas agar tiap komunikasi tetap fokus pada audiens yang tepat."
)

_MARK = "ZAVA_HTML_ART_v1"  # idempotency phrase — detected via existing prompt text below (NOT injected)

# ---------------------------------------------------------------------------
# Archetype prompt templates — placeholders {TITLE}, {KPIS}, {FILES}, {ENTITY}
# ---------------------------------------------------------------------------

# A. Executive KPI Dashboard — metric cards, sparkline trends, alerts panel
_DASHBOARD_EN = {
    'instr': "Same Cowork session — paste this prompt to ask Cowork to **build a single self-contained HTML executive dashboard** as a deliverable in chat. Cowork will read the attached data, generate the HTML/CSS/JS inline (no external CDN), and render it for download. While the HTML renders, Cowork runs the 4 parallel follow-up tasks below.",
    'prompt': (
        "Cowork: produce a SELF-CONTAINED interactive HTML dashboard titled "
        '"{TITLE}" using {FILES} as the source of truth. The HTML must be a '
        "single .html file (inline CSS + inline JS, no external CDN) styled "
        "for executive review — top strip of 5 KPI cards ({KPIS}), a "
        "trend chart (last 12 periods) per KPI built with the Canvas API, an "
        "alerts panel listing any KPI breaching its target threshold in red, "
        "and a notes panel summarising the 'so what'. While the HTML is "
        "generating, ALSO complete these 4 tasks in parallel and report back "
        "as each finishes:\n"
        "1. Word — a 2-page narrative memo walking the dashboard top-down for {ENTITY} leadership.\n"
        "2. Email — covering note from the Group CFO with the HTML + memo attached.\n"
        "3. Teams meeting — 30-min review block tomorrow morning to walk the dashboard.\n"
        "4. Tracker — update the {ENTITY} KPI tracker workbook with this period's actuals and the breach list.\n"
        + _RECIP_EN
    ),
}
_DASHBOARD_ID = {
    'instr': "Sesi Cowork yang sama — tempelkan prompt ini untuk meminta Cowork **membuat satu dashboard HTML eksekutif mandiri** sebagai deliverable di chat. Cowork akan membaca data terlampir, men-generate HTML/CSS/JS inline (tanpa CDN eksternal), dan menampilkannya untuk diunduh. Sambil HTML di-generate, Cowork menjalankan 4 tugas paralel di bawah.",
    'prompt': (
        "Cowork: buat dashboard HTML interaktif mandiri berjudul "
        '"{TITLE}" menggunakan {FILES} sebagai sumber kebenaran. HTML harus '
        "berupa satu file .html (CSS + JS inline, tanpa CDN eksternal), ditata "
        "untuk review eksekutif — strip atas berisi 5 kartu KPI ({KPIS}), "
        "chart tren (12 periode terakhir) per KPI dibangun dengan Canvas API, "
        "panel alert mencantumkan KPI yang melanggar ambang target dalam warna "
        "merah, dan panel catatan merangkum 'so what'. Sementara HTML "
        "di-generate, JUGA selesaikan 4 tugas berikut secara paralel dan "
        "laporkan saat masing-masing tuntas:\n"
        "1. Word — memo naratif 2 halaman menjelaskan dashboard top-down untuk pimpinan {ENTITY}.\n"
        "2. Email — cover note dari Direktur Keuangan Grup dengan HTML + memo terlampir.\n"
        "3. Rapat Teams — blok review 30 menit besok pagi untuk walk-through dashboard.\n"
        "4. Tracker — perbarui workbook tracker KPI {ENTITY} dengan aktual periode ini dan daftar breach.\n"
        + _RECIP_ID
    ),
}

# B. Operations Kanban — column-based status board
_KANBAN_EN = {
    'instr': "Same Cowork session — paste this prompt to ask Cowork to **build a self-contained HTML kanban board** as a deliverable. Cowork generates the kanban with drag-style columns + click-to-expand cards inline (no external CDN), then runs the 4 follow-up tasks in parallel.",
    'prompt': (
        "Cowork: produce a SELF-CONTAINED interactive HTML kanban board "
        'titled "{TITLE}" using {FILES} as the source of items. The HTML '
        "must be a single .html file (inline CSS + inline JS, no external "
        "CDN). Columns: To Do · In Progress · Blocked · Done. Each card "
        "shows {KPIS} as compact metadata chips, and clicks to expand into a "
        "details panel showing the full description, owner, due date, and "
        "blockers. Add a top-of-board summary strip with per-column counts "
        "and a 'breach' tag for anything overdue. While the HTML is "
        "generating, ALSO complete these 4 tasks in parallel and report back:\n"
        "1. Word — a 1-page status note for the {ENTITY} weekly ops meeting summarising the board state.\n"
        "2. Email — note from the Group COO to all card owners with the HTML attached, calling out 'Blocked' items.\n"
        "3. Teams meeting — schedule a 25-min stand-up tomorrow with the owners of every Blocked card.\n"
        "4. Tracker — update the {ENTITY} ops tracker with the new status snapshot and the blockers list.\n"
        + _RECIP_EN
    ),
}
_KANBAN_ID = {
    'instr': "Sesi Cowork yang sama — tempelkan prompt ini untuk meminta Cowork **membuat papan kanban HTML mandiri** sebagai deliverable. Cowork men-generate kanban dengan kolom drag-style + kartu expand-on-click inline (tanpa CDN eksternal), lalu menjalankan 4 tugas paralel.",
    'prompt': (
        "Cowork: buat papan kanban HTML interaktif mandiri berjudul "
        '"{TITLE}" menggunakan {FILES} sebagai sumber item. HTML harus '
        "berupa satu file .html (CSS + JS inline, tanpa CDN eksternal). "
        "Kolom: To Do · In Progress · Blocked · Done. Setiap kartu menampilkan "
        "{KPIS} sebagai chip metadata kompak, dan di-klik untuk membuka panel "
        "detail berisi deskripsi lengkap, owner, due date, dan blocker. "
        "Tambahkan strip ringkasan di atas papan dengan jumlah per kolom dan "
        "tag 'breach' untuk yang overdue. Sementara HTML di-generate, JUGA "
        "selesaikan 4 tugas berikut secara paralel dan laporkan:\n"
        "1. Word — status note 1 halaman untuk rapat ops mingguan {ENTITY} merangkum kondisi papan.\n"
        "2. Email — note dari Direktur Operasi Grup ke semua owner kartu dengan HTML terlampir, menyorot item 'Blocked'.\n"
        "3. Rapat Teams — jadwalkan stand-up 25 menit besok dengan owner setiap kartu Blocked.\n"
        "4. Tracker — perbarui tracker ops {ENTITY} dengan snapshot status baru dan daftar blocker.\n"
        + _RECIP_ID
    ),
}

# C. Risk / ESG Heatmap — probability × impact matrix
_HEATMAP_EN = {
    'instr': "Same Cowork session — paste this prompt to ask Cowork to **build a self-contained HTML risk / ESG heatmap** as a deliverable. Cowork generates the heatmap grid + click-through risk cards inline (no external CDN), then runs the 4 follow-up tasks in parallel.",
    'prompt': (
        "Cowork: produce a SELF-CONTAINED interactive HTML heatmap titled "
        '"{TITLE}" using {FILES} as the source data. The HTML must be a '
        "single .html file (inline CSS + inline JS, no external CDN) styled "
        "as a 5×5 probability × impact matrix. Each cell is colour-coded "
        "(green 1-2 · amber 3-4 · red 5) and shows the count of {KPIS} "
        "landing in that cell. Clicking a cell opens a side-panel listing "
        "every issue in that cell with owner + mitigation status + due date. "
        "Below the matrix render two strips — 'Top 5 inherent' and 'Top 5 "
        "residual'. While the HTML is generating, ALSO complete these 4 "
        "tasks in parallel and report back:\n"
        "1. Word — a 3-page risk/ESG briefing for the {ENTITY} risk committee summarising the heatmap with mitigations.\n"
        "2. Email — note from the Head of Risk to the Audit & Risk Committee Chair with the HTML attached and the 3 red cells called out.\n"
        "3. Teams meeting — schedule a 45-min risk-deep-dive next week with the Risk Committee.\n"
        "4. Tracker — update the {ENTITY} risk register with this cycle's residual scores and mitigation status.\n"
        + _RECIP_EN
    ),
}
_HEATMAP_ID = {
    'instr': "Sesi Cowork yang sama — tempelkan prompt ini untuk meminta Cowork **membuat heatmap risiko/ESG HTML mandiri** sebagai deliverable. Cowork men-generate grid heatmap + kartu risiko click-through inline (tanpa CDN eksternal), lalu menjalankan 4 tugas paralel.",
    'prompt': (
        "Cowork: buat heatmap HTML interaktif mandiri berjudul "
        '"{TITLE}" menggunakan {FILES} sebagai data sumber. HTML harus berupa '
        "satu file .html (CSS + JS inline, tanpa CDN eksternal) ditata sebagai "
        "matriks probabilitas × dampak 5×5. Setiap sel diwarnai (hijau 1-2 · "
        "kuning 3-4 · merah 5) dan menampilkan jumlah {KPIS} yang jatuh di "
        "sel tersebut. Klik sel membuka panel samping berisi setiap issue di "
        "sel tersebut dengan owner + status mitigasi + due date. Di bawah "
        "matriks render dua strip — 'Top 5 inherent' dan 'Top 5 residual'. "
        "Sementara HTML di-generate, JUGA selesaikan 4 tugas berikut secara "
        "paralel dan laporkan:\n"
        "1. Word — briefing risiko/ESG 3 halaman untuk komite risiko {ENTITY} merangkum heatmap dengan mitigasi.\n"
        "2. Email — note dari Kepala Risiko ke Ketua Komite Audit & Risiko dengan HTML terlampir dan 3 sel merah disorot.\n"
        "3. Rapat Teams — jadwalkan risk-deep-dive 45 menit minggu depan dengan Komite Risiko.\n"
        "4. Tracker — perbarui risk register {ENTITY} dengan skor residual siklus ini dan status mitigasi.\n"
        + _RECIP_ID
    ),
}

# D. Pipeline Timeline — Gantt-style horizontal timeline
_PIPELINE_EN = {
    'instr': "Same Cowork session — paste this prompt to ask Cowork to **build a self-contained HTML pipeline timeline** as a deliverable. Cowork generates the timeline bars + click-to-expand item cards inline (no external CDN), then runs the 4 follow-up tasks in parallel.",
    'prompt': (
        "Cowork: produce a SELF-CONTAINED interactive HTML pipeline timeline "
        'titled "{TITLE}" using {FILES} as the source of items. The HTML '
        "must be a single .html file (inline CSS + inline JS, no external "
        "CDN). Horizontal x-axis is the next 12 months. Each bar represents "
        "one {KPIS} item, colour-coded by stage (lead · qualified · "
        "in-flight · won · slipped). Clicking a bar expands an inline card "
        "with item details, owner, value, expected close, and risks. Top "
        "strip shows 4 summary chips — total value, weighted value, count "
        "by stage, and slippage rate vs last quarter. While the HTML is "
        "generating, ALSO complete these 4 tasks in parallel and report back:\n"
        "1. Word — a 2-page pipeline narrative for the {ENTITY} commercial review summarising the timeline.\n"
        "2. Email — note from the Group CCO to the segment heads with the HTML attached and the 'slipped' items called out for action.\n"
        "3. Teams meeting — schedule a 30-min pipeline review tomorrow with the segment heads.\n"
        "4. Tracker — update the {ENTITY} commercial tracker with this cycle's stage moves and the new weighted forecast.\n"
        + _RECIP_EN
    ),
}
_PIPELINE_ID = {
    'instr': "Sesi Cowork yang sama — tempelkan prompt ini untuk meminta Cowork **membuat timeline pipeline HTML mandiri** sebagai deliverable. Cowork men-generate bar timeline + kartu item expand-on-click inline (tanpa CDN eksternal), lalu menjalankan 4 tugas paralel.",
    'prompt': (
        "Cowork: buat timeline pipeline HTML interaktif mandiri berjudul "
        '"{TITLE}" menggunakan {FILES} sebagai sumber item. HTML harus '
        "berupa satu file .html (CSS + JS inline, tanpa CDN eksternal). "
        "Sumbu-x horizontal adalah 12 bulan ke depan. Setiap bar mewakili "
        "satu item {KPIS}, diwarnai berdasarkan tahap (lead · qualified · "
        "in-flight · won · slipped). Klik bar membuka kartu inline berisi "
        "detail item, owner, nilai, expected close, dan risiko. Strip atas "
        "menampilkan 4 chip ringkasan — total value, weighted value, count "
        "per tahap, dan slippage rate vs kuartal lalu. Sementara HTML "
        "di-generate, JUGA selesaikan 4 tugas berikut secara paralel dan "
        "laporkan:\n"
        "1. Word — narasi pipeline 2 halaman untuk commercial review {ENTITY} merangkum timeline.\n"
        "2. Email — note dari Group CCO ke segment heads dengan HTML terlampir dan item 'slipped' disorot untuk tindak lanjut.\n"
        "3. Rapat Teams — jadwalkan pipeline review 30 menit besok dengan segment heads.\n"
        "4. Tracker — perbarui commercial tracker {ENTITY} dengan stage move siklus ini dan forecast bertimbang baru.\n"
        + _RECIP_ID
    ),
}

# ---------------------------------------------------------------------------
# Per-entry routing — id → (archetype, title, kpi list text, file refs, entity)
# ---------------------------------------------------------------------------
# 4 archetypes: 'dashboard' | 'kanban' | 'heatmap' | 'pipeline'
# Defaults to 'dashboard' if id is unknown.
ARCHETYPE_BY_ID = {
    # ── Departments (12) ────────────────────────────────────────────────
    'dept-finance': ('dashboard',
        'Group Finance Performance Dashboard',
        'group revenue YTD · group EBITDA · cash conversion · net debt / EBITDA · DSO trend',
        '/01_Zava_Group_Financial_Performance.xlsx and /04_Zava_Divisional_Variance_FY2025.xlsx',
        'Group Finance'),
    'dept-strategy': ('dashboard',
        'Group Strategy Scorecard',
        'strategic initiatives on track · pillar revenue · capital deployed · market-share delta · NPS',
        '/03_Zava_Group_Strategy_Framework.docx and /01_Zava_Group_Financial_Performance.xlsx',
        'Group Strategy'),
    'dept-investor-relations': ('dashboard',
        'Investor Relations Dashboard',
        'share price 30d · consensus EPS · top-10 holder turnover · analyst notes count · upcoming events',
        '/01_Zava_Group_Financial_Performance.xlsx and /03_Zava_Group_Strategy_Framework.docx',
        'Group IR'),
    'dept-corpsec': ('dashboard',
        'Corporate Secretariat Tracker',
        'board resolutions open · disclosure deadlines · related-party transactions · directorship register · circulars in flight',
        '/02_Zava_Group_Policy_Handbook.docx',
        'Corporate Secretariat'),
    'dept-risk': ('heatmap',
        'Group Enterprise Risk Heatmap',
        'enterprise risks',
        '/02_Zava_Group_Policy_Handbook.docx and /05_Zava_Lender_Covenant_Tracker.xlsx',
        'Group Risk'),
    'dept-esg': ('heatmap',
        'Group ESG Materiality Heatmap',
        'material ESG topics',
        '/02_Zava_Group_Policy_Handbook.docx',
        'Group ESG'),
    'dept-hr': ('kanban',
        'Talent & Onboarding Kanban',
        'requisitions',
        '/02_Zava_Group_Policy_Handbook.docx',
        'Group HR'),
    'dept-it-digital': ('kanban',
        'Digital Initiatives Kanban',
        'IT/digital projects',
        '/03_Zava_Group_Strategy_Framework.docx',
        'Group IT & Digital'),
    'dept-marketing': ('kanban',
        'Campaign Production Kanban',
        'live campaigns',
        '/03_Zava_Group_Strategy_Framework.docx',
        'Group Marketing'),
    'dept-operations': ('kanban',
        'Ops Initiatives Kanban',
        'ops improvement initiatives',
        '/04_Zava_Divisional_Variance_FY2025.xlsx',
        'Group Operations'),
    'dept-procurement': ('kanban',
        'Sourcing Events Kanban',
        'sourcing events',
        '/02_Zava_Group_Policy_Handbook.docx',
        'Group Procurement'),
    'dept-legal': ('kanban',
        'Legal Matters Kanban',
        'live legal matters',
        '/02_Zava_Group_Policy_Handbook.docx',
        'Group Legal'),

    # ── Financial-services industries ───────────────────────────────────
    'investment-banking':       ('pipeline',  'IB Mandate Pipeline Timeline',
        'live mandates', '/IB_07_Segment_PnL.xlsx and /IB_08_Vendor_Contract.docx', 'Investment Banking'),
    'commercial-banking':       ('dashboard', 'Commercial Banking Health Dashboard',
        'NIM · cost-of-risk · NPL ratio · CASA growth · CIR',
        '/01_Zava_Group_Financial_Performance.xlsx', 'Commercial Banking'),
    'islamic-banking':          ('dashboard', 'Islamic Banking Performance Dashboard',
        'shariah-compliant assets · profit-rate margin · NPF ratio · CASA · wakalah fee income',
        '/01_Zava_Group_Financial_Performance.xlsx', 'Islamic Banking'),
    'mortgage-finance':         ('pipeline', 'Mortgage Pipeline Timeline',
        'mortgage applications', '/01_Zava_Group_Financial_Performance.xlsx', 'Mortgage Finance'),
    'life-insurance':           ('dashboard', 'Life Insurance KPI Dashboard',
        'APE · VNB margin · persistency 13M · claims ratio · capital adequacy',
        '/01_Zava_Group_Financial_Performance.xlsx', 'Life Insurance'),
    'general-insurance':        ('dashboard', 'General Insurance KPI Dashboard',
        'GWP YTD · loss ratio · expense ratio · combined ratio · reinsurance recoveries',
        '/01_Zava_Group_Financial_Performance.xlsx', 'General Insurance'),
    'takaful':                  ('dashboard', 'Takaful Performance Dashboard',
        'contributions YTD · surplus distribution · claims ratio · wakalah fee · retakaful retention',
        '/01_Zava_Group_Financial_Performance.xlsx', 'Takaful'),
    'fintech-payments':         ('dashboard', 'Payments KPI Dashboard',
        'TPV YTD · take-rate · fraud loss bps · uptime · merchant churn',
        '/01_Zava_Group_Financial_Performance.xlsx', 'Fintech Payments'),
    'cross-border-remittance':  ('dashboard', 'Remittance Corridor Dashboard',
        'corridor TPV · take-rate · settle-time · KYC reject rate · STP rate',
        '/01_Zava_Group_Financial_Performance.xlsx', 'Cross-Border Remittance'),
    'financial-regulator':      ('dashboard', 'Supervisory Dashboard',
        'open enforcement actions · capital adequacy outliers · stress-test misses · disclosure backlog · circulars issued',
        '/02_Zava_Group_Policy_Handbook.docx', 'Financial Regulator'),
    'glc-investment':           ('dashboard', 'GLC Portfolio Dashboard',
        'portfolio NAV · dividend yield · ESG score · holdings count · top-5 concentration',
        '/01_Zava_Group_Financial_Performance.xlsx', 'GLC Investment'),

    # ── Energy / resources / utilities ─────────────────────────────────
    'og-upstream':              ('dashboard', 'Upstream Production Dashboard',
        'production boe/d · cost per boe · realised price · reserves life · HSE incidents',
        '/01_Zava_Group_Financial_Performance.xlsx', 'Upstream O&G'),
    'og-downstream':            ('dashboard', 'Refining & Marketing Dashboard',
        'crack spread · refinery utilisation · retail throughput · inventory days · HSE incidents',
        '/OGD_06_ESG_Performance.xlsx and /04_Zava_Divisional_Variance_FY2025.xlsx', 'Downstream O&G'),
    'power-utilities':          ('dashboard', 'Power & Utilities KPI Dashboard',
        'plant load factor · forced-outage rate · CO₂ intensity · fuel cost · grid availability',
        '/04_Zava_Divisional_Variance_FY2025.xlsx', 'Power & Utilities'),
    'renewable-energy':         ('dashboard', 'Renewable Generation Dashboard',
        'capacity MW · capacity factor · PPA tariff · grid curtailment · CO₂ avoided',
        '/04_Zava_Divisional_Variance_FY2025.xlsx', 'Renewable Energy'),
    'coal-mining':              ('heatmap', 'Coal Mining HSE & Compliance Heatmap',
        'safety and compliance issues',
        '/04_Zava_Divisional_Variance_FY2025.xlsx', 'Coal Mining'),
    'rare-earth':               ('heatmap', 'Rare-Earth Processing Risk Heatmap',
        'processing & supply-chain risks',
        '/04_Zava_Divisional_Variance_FY2025.xlsx', 'Rare-Earth'),

    # ── Industrials / manufacturing ─────────────────────────────────────
    'industrial-manufacturing': ('kanban',    'Plant Improvement Kanban',
        'OEE / quality / safety initiatives', '/04_Zava_Divisional_Variance_FY2025.xlsx', 'Industrial Manufacturing'),
    'semiconductor':            ('kanban', 'Fab Improvement Kanban',
        'yield / cycle / equipment initiatives', '/04_Zava_Divisional_Variance_FY2025.xlsx', 'Semiconductor'),
    'rubber-gloves':            ('heatmap', 'Rubber Glove Compliance Heatmap',
        'audit & compliance findings', '/04_Zava_Divisional_Variance_FY2025.xlsx', 'Rubber Gloves'),
    'automotive':               ('heatmap', 'Automotive Quality & Recall Risk Heatmap',
        'quality & recall risks', '/04_Zava_Divisional_Variance_FY2025.xlsx', 'Automotive'),
    'auto-tyres':               ('heatmap', 'Tyre Compound & Recall Risk Heatmap',
        'compound / recall risks', '/04_Zava_Divisional_Variance_FY2025.xlsx', 'Auto Tyres'),

    # ── Plantation / agri / pharma ──────────────────────────────────────
    'plantation':               ('heatmap',   'Plantation ESG & RSPO Heatmap',
        'ESG / certification issues', '/04_Zava_Divisional_Variance_FY2025.xlsx', 'Plantation'),
    'pharmaceutical':           ('heatmap', 'Pharma Compliance & Pharmacovigilance Heatmap',
        'pharmacovigilance & GMP issues', '/02_Zava_Group_Policy_Handbook.docx', 'Pharmaceutical'),

    # ── Property / construction / real-estate ───────────────────────────
    'property-development':     ('pipeline',  'Project Pipeline Timeline',
        'live projects', '/PD_Project_Feasibility.xlsx and /PD_Sales_Pipeline.xlsx', 'Property Development'),
    'property-reit':            ('pipeline',  'REIT Portfolio Timeline',
        'asset events and reversions', '/01_Zava_Group_Financial_Performance.xlsx', 'Property REIT'),
    'construction':             ('pipeline',  'Construction Project Timeline',
        'live construction projects', '/PD_Project_Feasibility.xlsx', 'Construction'),

    # ── Logistics / mobility ────────────────────────────────────────────
    'logistics-3pl':            ('kanban',    'Logistics Move Kanban',
        'live shipments', '/04_Zava_Divisional_Variance_FY2025.xlsx', 'Logistics 3PL'),
    'maritime-shipping':        ('dashboard', 'Maritime Fleet Dashboard',
        'fleet utilisation · TCE rate · bunker cost · port-stay hours · CII rating',
        '/04_Zava_Divisional_Variance_FY2025.xlsx', 'Maritime Shipping'),
    'aviation-airlines':        ('pipeline',  'Airline Schedule Timeline',
        'flight schedules', '/04_Zava_Divisional_Variance_FY2025.xlsx', 'Airline'),
    'aviation-airports':        ('pipeline',  'Airport Slot & Movement Timeline',
        'slot allocations', '/04_Zava_Divisional_Variance_FY2025.xlsx', 'Airport'),

    # ── Telco / tech / media / consumer ────────────────────────────────
    'telco':                    ('kanban',    'Network Rollout Kanban',
        'network rollout / fault tickets', '/04_Zava_Divisional_Variance_FY2025.xlsx', 'Telco'),
    'media-entertainment':      ('kanban',    'Content Production Kanban',
        'live productions', '/04_Zava_Divisional_Variance_FY2025.xlsx', 'Media & Entertainment'),
    'ecommerce-superapp':       ('dashboard', 'Superapp GMV Dashboard',
        'GMV · take-rate · MAU · retention 30d · NPS',
        '/04_Zava_Divisional_Variance_FY2025.xlsx', 'E-commerce Superapp'),
    'food-fmcg':                ('kanban',    'FMCG Trade Promotion Kanban',
        'live trade promotions', '/04_Zava_Divisional_Variance_FY2025.xlsx', 'Food & FMCG'),
    'retail-grocery':           ('kanban',    'Store Operations Kanban',
        'store ops initiatives', '/04_Zava_Divisional_Variance_FY2025.xlsx', 'Retail Grocery'),
    'bpo-services':             ('dashboard', 'BPO Operations Dashboard',
        'SLA attainment · CSAT · AHT · adherence · attrition',
        '/04_Zava_Divisional_Variance_FY2025.xlsx', 'BPO Services'),

    # ── Services / public / hospitality / education ────────────────────
    'hospital-network':         ('pipeline',  'Hospital Caseload Timeline',
        'live admissions and case conferences', '/02_Zava_Group_Policy_Handbook.docx', 'Hospital Network'),
    'hotel-resort':             ('dashboard', 'Hotel & Resort Performance Dashboard',
        'RevPAR · ADR · occupancy · F&B revenue · NPS',
        '/04_Zava_Divisional_Variance_FY2025.xlsx', 'Hotel & Resort'),
    'education':                ('kanban',    'Programme Delivery Kanban',
        'live programmes / cohorts', '/02_Zava_Group_Policy_Handbook.docx', 'Education'),
    'government-agency':        ('kanban',    'Public Service Delivery Kanban',
        'live citizen-service initiatives', '/02_Zava_Group_Policy_Handbook.docx', 'Government Agency'),

    # ── Diversified ─────────────────────────────────────────────────────
    'diversified-conglomerate': ('dashboard', 'Group Diversified Conglomerate Dashboard',
        'revenue YTD · EBITDA · cash position · capital deployed · group RoCE',
        '/01_Zava_Group_Financial_Performance.xlsx and /04_Zava_Divisional_Variance_FY2025.xlsx', 'Diversified Group'),
}

_ARCHETYPE_TPL = {
    'dashboard': (_DASHBOARD_EN, _DASHBOARD_ID),
    'kanban':    (_KANBAN_EN,    _KANBAN_ID),
    'heatmap':   (_HEATMAP_EN,   _HEATMAP_ID),
    'pipeline':  (_PIPELINE_EN,  _PIPELINE_ID),
}

_DEFAULT = ('dashboard',
            'Group Performance Dashboard',
            'revenue · EBITDA · cash · headcount · NPS',
            '/01_Zava_Group_Financial_Performance.xlsx',
            'this entity')


def _fill(tpl: dict, title: str, kpis: str, files: str, entity: str) -> dict:
    return {
        'instr': tpl['instr'],
        'prompt': (tpl['prompt']
                   .replace('{TITLE}', title)
                   .replace('{KPIS}', kpis)
                   .replace('{FILES}', files)
                   .replace('{ENTITY}', entity)),
    }


def _is_cowork(name: str) -> bool:
    return 'Cowork' in (name or '')


def append_html_artifact_prompts(entries):
    """
    For every entry in entries, append ONE HTML-artifact prompt to its Cowork
    tool block. The archetype + flavouring is picked from ARCHETYPE_BY_ID
    (or _DEFAULT for unmapped ids).

    Idempotent — re-running the build is safe (detection via _MARK).

    Mutates entries in place. Returns count of entries touched.
    """
    touched = 0
    for entry in entries:
        eid = entry.get('id') or ''
        archetype, title, kpis, files, entity = ARCHETYPE_BY_ID.get(eid, _DEFAULT)
        en_tpl, id_tpl = _ARCHETYPE_TPL[archetype]
        en_prompt = _fill(en_tpl, title, kpis, files, entity)
        id_prompt = _fill(id_tpl, title, kpis, files, entity)

        for tb in entry.get('prompts') or []:
            if not _is_cowork(tb.get('tool', '')):
                continue
            existing_en = tb.get('prompts') or []
            existing_id = tb.get('promptsID') or []

            # Detect idempotency via the unique archetype phrase — present in all 4 EN templates.
            already = any(
                isinstance(p, dict) and 'SELF-CONTAINED interactive HTML' in (p.get('prompt') or '')
                for p in existing_en
            )
            if already:
                continue

            tb['prompts']   = list(existing_en) + [en_prompt]
            tb['promptsID'] = list(existing_id) + [id_prompt]
            touched += 1
            break  # one Cowork block per entry
    return touched
