"""
cowork_more_scenarios.py

Appends 3 additional Cowork delegation scenarios to every entry's Cowork tool block.

User asked for "more use cases on cowork", inspired by the structure used on
everythingischr0me/copilot-cowork-prompts (multiple distinct delegation scenarios
per role with parallel sub-tasks). Don't copy the original site — emulate the shape.

Each scenario:
- Stays in the same Cowork session (continuity across the demo)
- Delegates 5 parallel actions (Word doc draft + email + meeting + Teams post + tracker update)
- Uses the standardised named-recipients line so personas stay consistent
- Picks files/regulators that already exist as referenced artefacts in the build

Wired into build_master.py after subsidiaries merge so it walks the same merged
entries dict.
"""

# ---------------------------------------------------------------------------
# Standard named-recipients trail — appended to every prompt for consistency
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

# ---------------------------------------------------------------------------
# Scenario A — Quarterly Investor Day Sprint
# ---------------------------------------------------------------------------
_SCENARIO_A_EN = {
    'instr': "Stay in the same Cowork session — Cowork remembers prior delegations within the same chat. Paste this prompt to launch the **Quarterly Investor Day Sprint**. Cowork will delegate the 5 numbered actions in parallel and report back as each one completes.",
    'prompt': (
        "Run the FY2025 Q4 investor day delegation in parallel. Please do all 5 of the following "
        "at once and report back when each is ready.\n"
        "1. Draft a 4-page Word doc titled \"Investor Day FY2025 — Speaking Notes\" using "
        "/01_Zava_Group_Financial_Performance.xlsx and /03_Zava_Group_Strategy_Framework.docx as "
        "context. Section 1 financial highlights, Section 2 divisional performance, Section 3 "
        "capital allocation, Section 4 outlook for FY2026.\n"
        "2. Draft a 1-page Word doc titled \"Top 25 Analyst Q&A\" pulling anticipated questions "
        "from /06_Zava_Investor_QA_FY2025.docx — order by likelihood and pre-answer each in "
        "two sentences.\n"
        "3. Draft a personalised email to the top-25 covering analysts inviting them to the 9am "
        "virtual Q&A session immediately after the main investor day webcast.\n"
        "4. Schedule a 30-minute Teams dry-run tomorrow at 6pm with the Group CFO, Group Chief "
        "of Staff, Head of IR, and the IR team — pre-read the speaking notes and the analyst Q&A.\n"
        "5. Post a Teams message in the IR channel with the embargoed deck link, the Q&A doc, "
        "and the dry-run calendar invite."
        + _RECIP_EN
    ),
}
_SCENARIO_A_ID = {
    'instr': "Tetap di sesi Cowork yang sama — Cowork mengingat delegasi sebelumnya dalam chat yang sama. Tempelkan prompt ini untuk meluncurkan **Sprint Investor Day Triwulan**. Cowork akan mendelegasikan 5 tindakan bernomor secara paralel dan melaporkan saat masing-masing selesai.",
    'prompt': (
        "Jalankan delegasi Investor Day FY2025 Q4 secara paralel. Mohon kerjakan kelima hal "
        "berikut sekaligus dan laporkan begitu masing-masing siap.\n"
        "1. Susun dokumen Word 4 halaman berjudul \"Investor Day FY2025 — Naskah Pidato\" "
        "menggunakan /01_Zava_Group_Financial_Performance.xlsx dan /03_Zava_Group_Strategy_Framework.docx "
        "sebagai konteks. Bagian 1 highlight keuangan, Bagian 2 kinerja per unit usaha, Bagian 3 "
        "alokasi modal, Bagian 4 outlook FY2026.\n"
        "2. Susun dokumen Word 1 halaman berjudul \"Top 25 Q&A Analis\" menarik pertanyaan yang "
        "diantisipasi dari /06_Zava_Investor_QA_FY2025.docx — urutkan berdasarkan kemungkinan "
        "dan jawab masing-masing dalam dua kalimat.\n"
        "3. Susun email personal kepada top-25 analis covering yang mengundang mereka ke sesi "
        "Q&A virtual jam 9 pagi setelah webcast investor day utama.\n"
        "4. Jadwalkan dry-run Teams 30 menit besok jam 6 sore bersama Direktur Keuangan Grup, "
        "Kepala Staf Grup, Kepala IR, dan tim IR — pre-read naskah pidato dan Q&A analis.\n"
        "5. Posting pesan di channel Teams IR dengan link deck embargoed, dokumen Q&A, dan "
        "undangan kalender dry-run."
        + _RECIP_ID
    ),
}

# ---------------------------------------------------------------------------
# Scenario B — Monthly Lender Outreach Cycle
# ---------------------------------------------------------------------------
_SCENARIO_B_EN = {
    'instr': "Same Cowork session — paste this prompt to launch the **Monthly Lender Outreach Cycle**. Cowork delegates 5 lender-engagement tasks in parallel and reports back as each finishes.",
    'prompt': (
        "Run the month-end lender engagement cycle in parallel. Complete all 5 below and "
        "report back as each lands.\n"
        "1. Draft a 3-page Word doc titled \"Lender Pack — Month-End Update\" pulling current "
        "covenant headroom from /05_Zava_Lender_Covenant_Tracker.xlsx and division-level updates "
        "from /04_Zava_Divisional_Variance_FY2025.xlsx. Include a covenant-watchlist summary at "
        "the top.\n"
        "2. Draft individual cover emails (one per bank, personalised tone) to each of the top-10 "
        "relationship banks with the lender pack attached.\n"
        "3. Schedule three back-to-back 30-minute Teams calls tomorrow 2pm-3:30pm — one each "
        "with the lead facility agent, the syndicate-of-record chair, and the largest lender by "
        "facility size.\n"
        "4. Update the lender outreach tracker workbook with this month's communications, the "
        "upcoming covenant test dates, and any waiver/amendment items in flight.\n"
        "5. Post a status note in the Treasury team Teams channel summarising the lender "
        "position, covenant-watchlist items, and follow-up actions assigned."
        + _RECIP_EN
    ),
}
_SCENARIO_B_ID = {
    'instr': "Sesi Cowork yang sama — tempelkan prompt ini untuk meluncurkan **Siklus Outreach Kreditor Bulanan**. Cowork akan mendelegasikan 5 tugas keterlibatan kreditor secara paralel dan melaporkan saat masing-masing selesai.",
    'prompt': (
        "Jalankan siklus keterlibatan kreditor akhir bulan secara paralel. Selesaikan kelimanya "
        "di bawah ini dan laporkan saat masing-masing tuntas.\n"
        "1. Susun dokumen Word 3 halaman berjudul \"Lender Pack — Update Akhir Bulan\" menarik "
        "headroom covenant terkini dari /05_Zava_Lender_Covenant_Tracker.xlsx dan update level "
        "unit usaha dari /04_Zava_Divisional_Variance_FY2025.xlsx. Cantumkan ringkasan watchlist "
        "covenant di atas.\n"
        "2. Susun cover email individual (satu per bank, nada personal) ke top-10 bank relasi "
        "dengan lender pack terlampir.\n"
        "3. Jadwalkan tiga panggilan Teams 30 menit berturut-turut besok jam 14.00-15.30 — "
        "masing-masing dengan lead facility agent, ketua syndicate-of-record, dan kreditor "
        "terbesar berdasarkan ukuran fasilitas.\n"
        "4. Perbarui workbook tracker outreach kreditor dengan komunikasi bulan ini, tanggal "
        "uji covenant mendatang, dan item waiver/amendment yang sedang berjalan.\n"
        "5. Posting catatan status di channel Teams tim Treasury yang merangkum posisi kreditor, "
        "item watchlist covenant, dan tindak lanjut yang diberikan."
        + _RECIP_ID
    ),
}

# ---------------------------------------------------------------------------
# Scenario C — Quarterly Regulator Submission Sprint
# ---------------------------------------------------------------------------
_SCENARIO_C_EN = {
    'instr': "Same Cowork session — paste this prompt to launch the **Quarterly Regulator Submission Sprint**. Cowork delegates 5 submission-prep tasks in parallel and reports back as each completes.",
    'prompt': (
        "Run the quarterly regulator submission sprint in parallel. Complete all 5 below and "
        "report back as each finishes.\n"
        "1. Draft a Word doc titled \"Regulator Submission Q4 FY2025\" formatted as a formal "
        "disclosure pack covering the items required this cycle. Pull the divisional numbers "
        "from /01_Zava_Group_Financial_Performance.xlsx and the governance language from "
        "/02_Zava_Group_Policy_Handbook.docx.\n"
        "2. Draft the cover letter email to the lead supervisor with the submission pack "
        "attached and a one-paragraph executive summary in the body.\n"
        "3. Schedule a 20-minute pre-submission alignment Teams meeting tomorrow at 8am with "
        "Compliance, Legal, and the Head of IR — agenda: walk through the pack, confirm "
        "sign-offs, agree the cover letter language.\n"
        "4. Post a private Teams message to the General Counsel asking for sign-off on Section "
        "4 (related-party disclosures) by 5pm today, with the relevant page links highlighted.\n"
        "5. Update the regulatory submission tracker workbook with this cycle's submission "
        "package, the submission date, the supervisor contact, and the expected response window."
        + _RECIP_EN
    ),
}
_SCENARIO_C_ID = {
    'instr': "Sesi Cowork yang sama — tempelkan prompt ini untuk meluncurkan **Sprint Submisi Regulator Triwulan**. Cowork akan mendelegasikan 5 tugas persiapan submisi secara paralel dan melaporkan saat masing-masing selesai.",
    'prompt': (
        "Jalankan sprint submisi regulator triwulan secara paralel. Selesaikan kelimanya di "
        "bawah ini dan laporkan saat masing-masing tuntas.\n"
        "1. Susun dokumen Word berjudul \"Submisi Regulator Q4 FY2025\" diformat sebagai paket "
        "pengungkapan formal yang mencakup item yang diperlukan siklus ini. Tarik angka per "
        "unit usaha dari /01_Zava_Group_Financial_Performance.xlsx dan bahasa tata kelola dari "
        "/02_Zava_Group_Policy_Handbook.docx.\n"
        "2. Susun cover letter email kepada supervisor utama dengan paket submisi terlampir dan "
        "ringkasan eksekutif satu paragraf di body.\n"
        "3. Jadwalkan rapat alignment pra-submisi Teams 20 menit besok jam 8 pagi bersama "
        "Compliance, Legal, dan Kepala IR — agenda: walk-through paket, konfirmasi sign-off, "
        "sepakati bahasa cover letter.\n"
        "4. Posting pesan Teams pribadi kepada General Counsel meminta sign-off Bagian 4 "
        "(pengungkapan pihak terkait) jam 5 sore hari ini, dengan link halaman terkait disorot.\n"
        "5. Perbarui workbook tracker submisi regulator dengan paket submisi siklus ini, "
        "tanggal submisi, kontak supervisor, dan jendela respons yang diharapkan."
        + _RECIP_ID
    ),
}

_SCENARIOS_EN = [_SCENARIO_A_EN, _SCENARIO_B_EN, _SCENARIO_C_EN]
_SCENARIOS_ID = [_SCENARIO_A_ID, _SCENARIO_B_ID, _SCENARIO_C_ID]


def _is_cowork(name: str) -> bool:
    return 'Cowork' in (name or '')


def expand_cowork_prompts(entries):
    """
    For every entry in entries, find its Cowork tool block and append the 3
    new scenarios to its `prompts` (English) and `promptsID` arrays.

    Idempotent: if any of the new scenario prompts already appear in the array,
    no append happens (so re-running the build is safe).

    Mutates entries in place. Returns the count of entries touched.
    """
    touched = 0
    for entry in entries:
        prompt_blocks = entry.get('prompts') or []
        for tb in prompt_blocks:
            if not _is_cowork(tb.get('tool', '')):
                continue
            existing_en = tb.get('prompts') or []
            existing_id = tb.get('promptsID') or []

            # Detect via marker text — first sentence of scenario A's prompt
            marker = "Run the FY2025 Q4 investor day delegation in parallel"
            already = any(
                isinstance(p, dict) and marker in (p.get('prompt') or '')
                for p in existing_en
            )
            if already:
                continue

            tb['prompts'] = list(existing_en) + [dict(s) for s in _SCENARIOS_EN]
            # Always provide ID alongside; if entry didn't have promptsID yet, seed an empty list.
            tb['promptsID'] = list(existing_id) + [dict(s) for s in _SCENARIOS_ID]
            touched += 1
            break  # one Cowork block per entry
    return touched
