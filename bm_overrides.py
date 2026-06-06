"""Hand-authored Bahasa Malaysia overrides for the 9 prompts integrated
from the 5 customer demo sites (Sites 1-5 UC7 integration, June 2026).

The default build pipeline (`id_to_bm_swaps.fill_missing_bm_from_id`) clones
promptsID into promptsBM with a shallow token swap. For the 9 new customer
prompts that is not enough — the prose is long, technical, and full of words
that differ meaningfully between BI and BM (perusahaan→syarikat, tabel→jadual,
rapat→mesyuarat, kantor→pejabat, anak perusahaan→anak syarikat, jadwal→jadual,
mengelola→menguruskan, mendukung→menyokong, etc.). This module overrides the
auto-filled promptsBM slots for the 9 specific prompts with proper Bahasa
Malaysia translations.

Match key: (entry_id, tool_type_name, persona_name). When all three match,
the prompt's `prompt` field in promptsBM is replaced with the BM authored
text below. Idempotent — runs every build, always produces same result.
"""

# (entry_id, tool_name, persona_name) -> Bahasa Malaysia prompt text
from util import T_CHAT, T_WORD, T_PPT, T_EXCEL, T_OUTLOOK, T_COWORK, T_WORD_AGT

# (entry_id, tool_name, persona_name) -> Bahasa Malaysia prompt text
_OVERRIDES = {
    # ── Site 1: Retail (retail-grocery T_CHAT) ────────────────────────────────
    ('retail-grocery', T_CHAT, 'Pak Andi Wijaya'):
        'Berperanan sebagai retail strategy analyst untuk General Manager · '
        'Retail Operations dari Zava Lifestyle Retail.\n\n'
        'Senario: pemaju mall menawarkan kita anchor unit (450 sqm, Ground Floor) '
        'di sebuah mall lifestyle baharu yang akan dibuka Q4 2026 di Surabaya '
        'Barat — catchment ~1.2 juta middle-class dalam radius 5km, unjuran '
        'footfall mall 800k sebulan ketika matang. Pajakan: IDR 18 bilion bagi '
        'tempoh 5 tahun. Anggaran CapEx fit-out: IDR 12 bilion.\n\n'
        'Gunakan peer benchmark dari /RT_04_Promotion_ROI_Model.xlsx dan '
        'prestasi same-store kita dari /RT_01_Store_Performance.xlsx.\n\n'
        'Bina decision pack 1 muka surat untuk GM dengan:\n'
        '1. Catchment & competition fit (vs overlap Tunjungan + Pakuwon Surabaya)\n'
        '2. Brand mix yang disyorkan untuk format ini (4-5 jenama dari portfolio kita)\n'
        '3. Unjuran SSS Tahun 1 / Tahun 2 / Tahun 3 dengan andaian yang jelas\n'
        '4. Jumlah CapEx + IRR + simple payback\n'
        '5. Top 3 risiko & satu mitigasi bagi setiap satu\n'
        '6. Syor GM yang tegas: GO / NO-GO / CONDITIONAL — dengan syarat spesifik\n\n'
        'Tag setiap andaian [ASSUMPTION:...]. Tiada angka direka. Format: Word doc 1 muka surat.',

    # ── Site 2: Power Utilities (power-utilities T_WORD) ──────────────────────
    ('power-utilities', T_WORD, 'Pak Hendra Setiawan'):
        'Berperanan sebagai Plant Reliability lead yang menyokong General Manager '
        '· Plant Operations dari Zava Power.\n\n'
        'Kita ada quarterly PPA review dengan PLN dalam 5 hari. Gunakan '
        '/POW_02_Plant_Availability_Tracker.xlsx (Plant Availability %, Net '
        'Generation GWh, Forced Outage Rate %, Specific Steam Use, TRIR) dan '
        '/POW_05_Off_Taker_Negotiation_Brief.docx (konteks steam-decline).\n\n'
        'Hasilkan tiga artifak:\n\n'
        '1. SURAT PEMATUHAN PPA SUKU TAHUNAN PLN (Word doc, ~1.5 muka surat):\n'
        ' - Availability loji demi loji vs MW kontrak PPA\n'
        ' - Net generation vs nominated profile\n'
        ' - Kejadian force-majeure dan kesannya (sebut spesifik Wayang Windu / Salak / Darajat)\n'
        ' - Pelan pemulihan bagi underperformance\n'
        ' - Nada: faktual, regulatori, tanpa bahasa pemasaran\n\n'
        '2. PAKEJ Q&A REGULATOR (Word doc):\n'
        ' - 10 soalan berkemungkinan ditanya PLN, dengan jawapan kita\n'
        ' - Dikumpulkan: availability, keselamatan, ESG / Scope 1/2, kontrak, komitmen ke hadapan\n\n'
        '3. ONE-PAGER LEMBAGA PENGARAH — KES MITIGASI STEAM-DECLINE (Word doc, 1 muka surat):\n'
        ' - Masalah dalam 3 baris\n'
        ' - Tiga pilihan (do nothing / mid-life workover / make-up well baharu) dengan kos & MW recovery\n'
        ' - Pilihan yang disyorkan dengan payback dan IRR\n'
        ' - Keputusan yang diminta daripada Lembaga Pengarah\n\n'
        'Tag setiap andaian [ASSUMPTION:...]. Jangan reka angka KPI — guna apa yang ada dalam workbook.',

    # ── Site 3: Food FMCG (food-fmcg T_PPT) ───────────────────────────────────
    ('food-fmcg', T_PPT, 'Bu Lisa Hartono'):
        'Berperanan sebagai Marketing & Ops planner untuk General Manager · '
        'Operations & Marketing dari Zava Food (lini QSR Pizza).\n\n'
        'Hari Raya 2026 tinggal 4 minggu lagi. Gunakan '
        '/FMCG_02_SKU_Margin_Tracker.xlsx (AOV per outlet, food cost %, delivery '
        'mix %, CSAT) dan /FMCG_05_FY2026_Promo_Guardrails.docx untuk konteks.\n\n'
        'Hasilkan promo pack siap launch:\n\n'
        '1. REKA BENTUK PROMO\n'
        ' - 3 bundle promo (keluarga / berdua / solo) dengan menu, target AOV, food-cost %, margin kasar\n'
        ' - Price ladder vs menu semasa — sebut risiko cannibalisation\n'
        ' - Tempoh & wave roll-out (Jakarta dahulu, kemudian bandar sekunder)\n\n'
        '2. COPY SALURAN\n'
        ' - GoFood listing title + description (maks 90 aksara title, 220 aksara desc)\n'
        ' - GrabFood listing title + description\n'
        ' - Caption Instagram × 3 varian (mesra / jenaka / Hari Raya yang sopan)\n'
        ' - Copy push notification untuk app\n\n'
        '3. PAKEJ BRIEFING OUTLET\n'
        ' - Checklist operasi 1 muka surat (prep · staffing · POS · stock-up bahan)\n'
        ' - Talking points untuk briefing pasukan outlet\n'
        ' - Pelan sampling quality-control\n\n'
        '4. JADUAL FORECAST CANNIBALISATION\n'
        ' - Outlet demi outlet: jangkaan lift vs cannibalisation menu reguler, kesan AOV bersih\n\n'
        '5. SCORECARD LAUNCH\n'
        ' - 5 KPI untuk dipantau dalam 7 hari pertama, dengan threshold merah/amber/hijau\n\n'
        'Tag setiap andaian [ASSUMPTION:...]. Nada: yakin, food-first, tidak boleh perkauman atau tidak peka terhadap audiens Muslim Indonesia.',

    # ── Site 4: Coal Mining (coal-mining T_WORD) ──────────────────────────────
    ('coal-mining', T_WORD, 'Pak Surya Wibawa'):
        'Berperanan sebagai Bid Manager yang menyokong General Manager · '
        'Operations dari Zava Mining (lini mining services).\n\n'
        'Kita sedang membalas RFP EPC 240 muka surat dari klien gold mining '
        'untuk pakej open-pit overburden + ore-haul, tempoh 36 bulan, armada '
        '~120 unit, di Kalimantan Timur. Submission dalam 14 hari.\n\n'
        'Gunakan /COAL_05_Marketing_Pricing_Pack.xlsx (peer benchmark vs '
        'Pamapersada, BUMA, Thiess) dan /COAL_06_Stakeholder_Holding_Lines.docx '
        '(naratif keupayaan kita).\n\n'
        'Hasilkan empat artifak:\n\n'
        '1. WIN-THEMES (1 muka surat)\n'
        ' - Keutamaan yang dinyatakan klien (safety, cost, schedule, ESG) — dirank\n'
        ' - 3 win-theme kita yang paling berkesan dengan bukti spesifik (projek / KPI)\n'
        ' - 2 kelemahan pesaing yang boleh kita ketengahkan (secara faktual)\n\n'
        '2. BID EXECUTIVE SUMMARY (Word doc, 2 muka surat)\n'
        ' - Pembukaan yang kuat dan merujuk bahasa klien sendiri\n'
        ' - Mengapa kita (3 sebab, anchored kepada bukti)\n'
        ' - Pendekatan schedule & mobilisasi\n'
        ' - Komitmen Keselamatan & ESG\n'
        ' - Pricing positioning (tanpa angka — itu berasingan)\n'
        ' - Closing call-to-action\n\n'
        '3. COMPLIANCE MATRIX STARTER (jadual)\n'
        ' - Tarik setiap requirement bernombor dari spec RFP\n'
        ' - Map kepada: Compliant / Compliant-with-comment / Non-compliant\n'
        ' - Pre-fill respon piawai kita di mana sudah ada\n'
        ' - Tandakan 5 item paling kontensius untuk semakan undang-undang\n\n'
        '4. RISK REGISTER (top 10)\n'
        ' - Operasi, komersial, HSE, regulatori, cuaca/musim\n'
        ' - Untuk setiap satu: kebarangkalian, kesan, mitigasi, owner\n\n'
        'Tag setiap andaian [ASSUMPTION:...]. Gunakan terminologi mining-services '
        'yang tepat (Mbcm, strip ratio, OEE, TKDN, TRIR). Jangan reka sejarah projek.',

    # ── Site 5: Legal — UC2 Legal Memo (dept-legal T_WORD, Ratna Sari) ────────
    ('dept-legal', T_WORD, 'Ratna Sari'):
        '/LEG_07_Mining_Regulation_Brief.docx /LEG_08_Legal_Knowledge_Base.docx '
        '/LEG_09_Legal_Memo_Template.docx — Berdasarkan ketiga-tiga dokumen ini, '
        'sediakan Legal Memo lengkap (struktur IRAC) yang ditujukan kepada '
        'Pengarah Urusan Kumpulan. Kenal pasti 3 isu undang-undang paling kritikal '
        'di bawah Permen ESDM No. 7 Tahun 2026, dan untuk setiap satu nyatakan: '
        '(a) klausa spesifik yang terjejas, (b) rujukan SOP/polisi dalaman yang '
        'berkaitan, dan (c) jurisprudensi Mahkamah Agung yang relevan. Isi '
        'kesemua 6 bahagian template: I. Latar Belakang, II. Soalan Undang-Undang, '
        'III. Analisis Undang-Undang (IRAC), IV. Kesimpulan, V. Syor & Mitigasi '
        'Risiko (sertakan jadual risk register: Risk ID | Deskripsi | Severity | '
        'Owner | Mitigasi | Tarikh Akhir dengan sekurang-kurangnya 6 risiko), '
        'VI. Limitasi & Disclaimer. Daftar bahasa undang-undang formal. '
        'Maksimum 1.5 muka surat.',

    # ── Site 5: Legal — UC3 NDA Review (dept-legal T_OUTLOOK, Ratna Sari) ─────
    ('dept-legal', T_OUTLOOK, 'Ratna Sari'):
        '/LEG_10_NDA_Draft.docx /LEG_11_MA_Playbook.docx — Bandingkan NDA pihak '
        'lawan dengan M&A Playbook v4.0 kita. Hasilkan: (1) jadual red-flag '
        'dengan lajur Klausa # | Isu | Mengapa ia melanggar Playbook | Cadangan '
        'mark-up; (2) tulis semula klausa 3 (Tempoh), 5 (Indemniti), 6 '
        '(Undang-Undang & Pertikaian), 7 (Eksklusiviti), 9 (Penyerahan) dalam '
        'gaya mark-up — tambahan bold, padaman struck-through; (3) e-mel '
        'pengiringan dwibahasa (Bahasa Indonesia di atas, Bahasa Inggeris di '
        'bawah) kepada pihak lawan yang merumuskan 5 pindaan utama dengan '
        'justifikasi ringkas berasaskan KUHPerdata Pasal 1247-1248, POJK '
        '17/2020, dan UU PT 40/2007. Cadangkan panggilan 30 minit dalam tempoh '
        '5 hari bekerja.',

    # ── Site 5: Legal — UC4 Litigation Analytics (dept-legal T_EXCEL, Ratna Sari) ─
    ('dept-legal', T_EXCEL, 'Ratna Sari'):
        'Profilkan /LEG_12_Litigation_Cases.xlsx (50 kes, 6 anak syarikat '
        'holding). Mod Plan: rangka langkah analisis dan sahkan sebelum '
        'pelaksanaan. Kemudian jalankan: (1) sheet Summary dengan jumlah kes, '
        'ongoing vs closed, breakdown per Anak_Holding, breakdown per '
        'Case_Type, jumlah exposure tuntutan (IDR Bn), jumlah penyelesaian, '
        'kadar menang keseluruhan dengan conditional formatting (hijau ≥ 60%, '
        'kuning 40-60%, merah < 40%); (2) purata tempoh per Case_Type & '
        'Forum_Level; (3) top 5 kes ongoing high-value berdasarkan '
        'Claim_Amount; (4) kadar menang/kalah per Anak_Holding; (5) tandakan '
        '"Aging" untuk kes dengan Duration_Days > 730; (6) carta bar jumlah '
        'exposure per Province. Kemudian gunakan Analyst Agent untuk analisis '
        'punca utama: 3 punca utama yang memacu exposure tertinggi, dengan '
        'jumlah tuntutan, purata tempoh, nisbah menang/kalah; sarankan 2 '
        'tindakan pencegahan setiap punca dengan sitasi UU/PP/Permen.',

    # ── Site 5: Legal — UC5 Cowork Sync (dept-legal T_COWORK, Ratna Sari) ─────
    ('dept-legal', T_COWORK, 'Ratna Sari'):
        'Berdasarkan transkrip mesyuarat Legal Weekly Sync (12 Mei 2026) di '
        '/LEG_13_Legal_Sync_Transcript.docx, jalankan secara selari: '
        '(1) hantar e-mel ringkasan kepada semua peserta dengan tindakan '
        'spesifik mereka, tarikh akhir, dan pautan dokumen sumber; (2) cipta '
        'mesyuarat susulan 30 minit dalam masa 5 hari bekerja untuk semakan '
        'kemajuan Item A1, A2, A5; (3) kemas kini hamparan Legal Matter '
        'Register (/LEG_01) dengan 7 perkara tindakan baharu; (4) hantar '
        'mesej Teams kepada saluran "Group Legal Counsel" dengan 3 keputusan '
        'utama dari mesyuarat. Mod pelaksanaan: paparkan setiap langkah '
        '(Thinking → Skill → Step-by-step), minta kelulusan untuk tindakan '
        'medium-risk (e-mel keluar + perubahan kalendar), dan teruskan '
        'tindakan low-risk (kemas kini sheet + mesej Teams dalaman).',

    # ── Site 5: Legal — UC6 Agent Builder (dept-legal T_WORD_AGT, Ratna Sari) ─
    ('dept-legal', T_WORD_AGT, 'Ratna Sari'):
        'Cipta agen "Group Legal Counsel" melalui Agent Builder (m365.cloud.microsoft/chat '
        '> Agents > + Create an agent). Konfigurasi: (1) Nama: "Group Legal Counsel"; '
        '(2) Deskripsi: "Penasihat undang-undang dalaman untuk Zava Group yang memberi '
        'analisis IRAC, sitasi UU/PP/Permen Indonesia & Malaysia, serta menggesa '
        'eskalasi kepada General Counsel apabila wajar"; (3) Arahan: utamakan citation '
        'authoritative, tandakan setiap andaian, tolak nasihat di luar bidang '
        '(litigasi forensik, undang-undang cukai), dan sentiasa selitkan disclaimer '
        '"Bukan nasihat undang-undang formal — sahkan dengan General Counsel"; '
        '(4) Pengetahuan: muat naik LEG_02 (Compliance Manual), LEG_07 (Mining '
        'Regulation Brief), LEG_08 (Legal Knowledge Base), LEG_11 (M&A Playbook); '
        '(5) Starter prompts: 4 prompt dari template Legal Memo IRAC. Uji di anak '
        'tetingkap kanan, kemudian Cipta + serahkan untuk kelulusan pentadbir bagi '
        'penerbitan ke katalog "Built by your org" Agent Store.',
}


def apply_bm_overrides(entries):
    """Walk industry/department entries and override promptsBM slots where
    the persona name matches one of the registered overrides. Returns count
    of slots overridden. Idempotent.
    """
    overridden = 0
    for entry in entries:
        if not isinstance(entry, dict):
            continue
        eid = entry.get('id')
        tools = entry.get('prompts')
        if not eid or not isinstance(tools, list):
            continue
        for tool in tools:
            if not isinstance(tool, dict):
                continue
            tname = tool.get('tool')
            personas = tool.get('persona') or []
            bm = tool.get('promptsBM') or []
            for i, pname in enumerate(personas):
                key = (eid, tname, pname)
                if key in _OVERRIDES and i < len(bm) and isinstance(bm[i], dict):
                    bm[i]['prompt'] = _OVERRIDES[key]
                    overridden += 1
    return overridden
