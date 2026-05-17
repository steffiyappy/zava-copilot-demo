"""Inject KIBB customer prompts into investment-banking (ind_batch2.py).

The 4 KIBB files (01_KIBB_SegmentPnL.xlsx, 02_KIBB_VendorContract.docx,
03_KIBB_BoardRiskCommittee_Transcript.docx, 04_KIBB_GroupOutsourcingFinancePolicy.docx)
already exist in files/ as IB_07_Segment_PnL.xlsx, IB_08_Vendor_Contract.docx,
IB_09_BoardRisk_Transcript.docx, IB_10_Outsourcing_Policy.docx. Prompts reference those
hub filenames.

We APPEND one new prompt to each target tool block. No existing prompt is rewritten.
"""
import re, sys, ast

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

FILE = r'C:\Users\peiyiyap\zava-copilot-demo\ind_batch2.py'

# Map: tool token (as it appears at the start of `tool(T_X, ...)`) -> (en_dict, id_dict, persona, persona_id)
# Each value is a literal dict { 'instr': '...', 'prompt': '...' }.

KIBB_INJECTS = [
    # Researcher — Ex1-T2 Strategic Risk via Model Council
    ('T_RESEARCHER',
     {'instr':'Open `m365.cloud.microsoft/chat` > Agents > **Researcher** > select **Model Council**. Paste the prompt below — Researcher convenes a parallel multi-model report and surfaces dissent across the panel.',
      'prompt':'I am the Group CFO of Zava Capital Malaysia. Produce a strategic risk register for the top financial, regulatory, and operational risks facing Malaysian investment banks over the next 24 months. Cover: BNM Outsourcing Policy BNM/RH/PD 028-99 and Risk Management in Technology (RMiT) operational-resilience expectations; Bursa Malaysia readiness for the National Sustainability Reporting Framework aligned to ISSB IFRS S1/S2; revenue concentration risk in stockbroking as zero-commission digital brokers compress cash-equities margins; investment banking deal pipeline risk in a softer ECM/M&A market; cyber and third-party concentration risk on trading platform hosting, market data, and post-trade settlement; and talent retention for licensed dealer\'s representatives and quants. For each risk: assess likelihood and financial impact in MYR M, describe how leading regional and Malaysian peers mitigate it, and propose one concrete Board governance action in the next six months. Present as a structured risk register with an executive summary at the top.'},
     {'instr':'Buka `m365.cloud.microsoft/chat` > Agents > **Researcher** > pilih **Model Council**. Tempel prompt di bawah — Researcher menggelar debat multi-model paralel dan menampilkan perbedaan pendapat lintas panel.',
      'prompt':'Saya Group CFO Zava Capital Indonesia. Susun risk register strategis untuk risiko keuangan, regulasi, dan operasional teratas yang dihadapi bank investasi Indonesia dalam 24 bulan ke depan. Cakup: ekspektasi POJK terkait Outsourcing dan Manajemen Risiko Teknologi (operational resilience); kesiapan Bursa Efek Indonesia untuk kerangka disclosure berkelanjutan selaras ISSB IFRS S1/S2; risiko konsentrasi pendapatan pada brokerage saat platform digital zero-commission menekan margin equities; risiko pipeline transaksi ECM/M&A; risiko cyber dan konsentrasi pihak ketiga pada hosting platform trading, market data, dan post-trade settlement; serta retensi talenta wakil perantara terdaftar dan kuant. Untuk setiap risiko: nilai kemungkinan dan dampak finansial dalam miliar rupiah, jelaskan bagaimana peer Indonesia memitigasinya, dan usulkan satu tindakan governance Board konkret dalam enam bulan ke depan. Sajikan sebagai risk register terstruktur dengan ringkasan eksekutif di bagian atas.'},
     'Hadar Caspit', 'Hadar Caspit'),

    # Analyst — Ex2-T3 Segment P&L Analyst Agent
    ('T_ANALYST',
     {'instr':'Open `m365.cloud.microsoft/chat` > Agents > **Analyst**. Upload IB_07_Segment_PnL.xlsx (FY2025 segment P&L workbook). Run six quantitative outputs in one go.',
      'prompt':'You are Analyst for Zava Capital Malaysia. Using IB_07_Segment_PnL.xlsx, produce SIX outputs the Group CFO can drop straight into the Board Risk Committee pack on Thursday. (1) A horizontal bar chart of FY2025 YTD revenue variance by segment ranked worst to best in MYR M, RAG-coloured (Red over 10% adverse, Amber 5-10%, Green within 5%). (2) A clustered column chart comparing FY2025 actual vs budget operating cost by segment with the absolute MYR M gap labelled. (3) A line chart of monthly Group revenue versus budget for all 12 months. (4) A driver-tree table for the two worst-variance segments breaking the gap into Volume / Price / Mix / Cost / FX contributions. (5) A "trigger list" table of segments that breach the 10% corrective-action threshold, with proposed owner and timeline. (6) A 6-bullet executive summary the CFO can read out at the Board Risk Committee. Cite the exact tab and cell range for every figure. Flag any data-quality gaps that could invalidate the analysis.'},
     {'instr':'Buka `m365.cloud.microsoft/chat` > Agents > **Analyst**. Unggah IB_07_Segment_PnL.xlsx (workbook P&L segmen FY2025). Jalankan enam output kuantitatif sekaligus.',
      'prompt':'Anda adalah Analyst untuk Zava Capital Indonesia. Menggunakan IB_07_Segment_PnL.xlsx, hasilkan ENAM output yang dapat langsung dimasukkan Group CFO ke dalam pack Komite Risiko Dewan hari Kamis. (1) Bar chart horizontal varians pendapatan YTD FY2025 per segmen diurutkan dari terburuk ke terbaik dalam miliar rupiah, diberi warna RAG (Merah lebih dari 10% adverse, Kuning 5-10%, Hijau dalam 5%). (2) Clustered column chart yang membandingkan biaya operasional aktual vs anggaran FY2025 per segmen dengan selisih absolut dalam miliar rupiah dilabeli. (3) Line chart pendapatan Group bulanan versus anggaran untuk seluruh 12 bulan. (4) Tabel driver-tree untuk dua segmen dengan varians terburuk yang memecah gap menjadi kontribusi Volume / Harga / Mix / Biaya / Valas. (5) Tabel "trigger list" segmen yang melampaui ambang tindakan korektif 10%, dengan pemilik dan jadwal yang diusulkan. (6) Ringkasan eksekutif 6-poin yang dapat dibacakan CFO di Komite Risiko Dewan. Sertakan referensi tab dan rentang sel persis untuk setiap angka. Tandai setiap kesenjangan kualitas data yang dapat membatalkan analisis.'},
     'Hadar Caspit', 'Hadar Caspit'),

    # Copilot in Excel — Ex2-T1 Board Risk Committee variance + commentary
    ('T_EXCEL',
     {'instr':'Open IB_07_Segment_PnL.xlsx in Excel for the Web. Open the Copilot pane. The Group MD needs this for the FY2025 year-end Board Risk Committee on Thursday.',
      'prompt':'Using the Monthly_PnL sheet, produce two outputs in a new sheet called "Board Summary". First, build a Board Risk Committee variance table covering every business segment, with columns for Actual Revenue YTD, Budget YTD, Operating Cost YTD, RM Variance, Variance %, and a RAG status (Red over 10% adverse, Amber 5-10%, Green within 5%). Flag any segment breaching the 10% threshold that triggers a mandatory corrective action plan under internal policy, and add a one-sentence commercial driver explanation for each. Second, immediately below the table in the same sheet, draft the Group CFO narrative commentary in 200-220 words of continuous formal prose: state full-year PBT versus budget in MYR M and %, name the two segments with the most significant adverse variances and explain what drives each shortfall, acknowledge the best-performing segment for balance, state explicitly which segments triggered the corrective-action threshold, and close with management actions proposed and timeline for resolution before the next Board cycle. Match Bursa-listed disclosure standards.'},
     {'instr':'Buka IB_07_Segment_PnL.xlsx di Excel for the Web. Buka panel Copilot. Group MD membutuhkan ini untuk rapat Komite Risiko Dewan akhir tahun FY2025 pada hari Kamis.',
      'prompt':'Menggunakan sheet Monthly_PnL, hasilkan dua output dalam sheet baru bernama "Board Summary". Pertama, bangun tabel varians Komite Risiko Dewan yang mencakup setiap segmen bisnis, dengan kolom Pendapatan Aktual YTD, Anggaran YTD, Biaya Operasional YTD, Varians (miliar rupiah), Varians %, dan status RAG (Merah jika lebih dari 10% adverse, Kuning 5-10%, Hijau dalam 5%). Tandai segmen yang melampaui ambang 10% yang memicu rencana tindakan korektif wajib berdasarkan kebijakan internal, dan tambahkan satu kalimat penjelasan driver komersial untuk setiap segmen. Kedua, langsung di bawah tabel di sheet yang sama, susun narasi komentari Group CFO sepanjang 200-220 kata dalam prosa formal kontinu: nyatakan PBT setahun penuh versus anggaran dalam miliar rupiah dan %, sebutkan dua segmen dengan varians adverse paling signifikan dan jelaskan apa yang menggerakkan setiap kekurangan, akui segmen berkinerja terbaik untuk keseimbangan, nyatakan secara eksplisit segmen mana yang memicu ambang tindakan korektif, dan tutup dengan tindakan manajemen yang diusulkan dan jadwal penyelesaian sebelum siklus Dewan berikutnya. Sesuaikan dengan standar pengungkapan tercatat BEI.'},
     'Hadar Caspit', 'Hadar Caspit'),

    # Copilot in Word — Ex3-T1 Vendor Contract Review (BNM Outsourcing Policy breaches)
    ('T_WORD',
     {'instr':'Open IB_08_Vendor_Contract.docx in Word for the Web. Open the Copilot pane. The CFO has 24 hours to spot any clause that breaches BNM Outsourcing Policy before signing.',
      'prompt':'Review IB_08_Vendor_Contract.docx against IB_10_Outsourcing_Policy.docx (the Group Outsourcing & Finance Policy aligned to BNM/RH/PD 028-99). Produce three outputs in a new Word document. (1) A clause-by-clause compliance matrix: clause number, clause subject, contract wording, BNM policy expectation, gap severity (High / Medium / Low), and proposed redline. (2) A focused redline pack for the High-severity clauses with proposed replacement wording the legal team can paste into negotiation. Cover at minimum: data residency, sub-contracting and chain-outsourcing consent, audit rights including BNM and internal audit on-site rights, business continuity and exit-management obligations, service levels and credit regime, and confidentiality + IP. (3) A 200-word executive memo to the Group MD recommending whether the contract can be signed as drafted, signed with the proposed redlines, or returned to the vendor with a stop-light list of must-fix items. Cite the exact clause number for every finding.'},
     {'instr':'Buka IB_08_Vendor_Contract.docx di Word for the Web. Buka panel Copilot. CFO memiliki 24 jam untuk menemukan klausul yang melanggar kebijakan outsourcing regulator sebelum penandatanganan.',
      'prompt':'Tinjau IB_08_Vendor_Contract.docx terhadap IB_10_Outsourcing_Policy.docx (Group Outsourcing & Finance Policy yang selaras dengan POJK terkait alih daya dan manajemen risiko teknologi). Hasilkan tiga output dalam dokumen Word baru. (1) Matriks kepatuhan klausul-per-klausul: nomor klausul, subjek klausul, redaksi kontrak, ekspektasi kebijakan regulator, tingkat keparahan gap (Tinggi / Sedang / Rendah), dan redline yang diusulkan. (2) Paket redline terfokus untuk klausul dengan keparahan Tinggi dengan redaksi pengganti yang dapat ditempel tim legal ke dalam negosiasi. Minimal cakup: residensi data, persetujuan sub-kontrak dan rantai alih daya, hak audit termasuk hak audit on-site oleh regulator dan audit internal, kewajiban business continuity dan exit-management, service level dan rezim kredit, serta kerahasiaan + HKI. (3) Memo eksekutif 200 kata kepada Group MD merekomendasikan apakah kontrak dapat ditandatangani apa adanya, ditandatangani dengan redline yang diusulkan, atau dikembalikan ke vendor dengan daftar stop-light item wajib-perbaikan. Sertakan nomor klausul persis untuk setiap temuan.'},
     'Hadar Caspit', 'Hadar Caspit'),

    # PowerPoint — Ex3-T2 Board Risk Committee deck
    ('T_PPT',
     {'instr':'Open a new PowerPoint or use the workshop template. Open the Copilot pane. Reference IB_08_Vendor_Contract.docx and IB_07_Segment_PnL.xlsx for content. The deck goes to the Board Risk Committee on Thursday.',
      'prompt':'Build a 7-slide Board Risk Committee deck for Zava Capital Malaysia. Slide 1 cover: "FY2025 Year-End Board Risk Committee — Vendor & Segment Risk Review". Slide 2 executive summary: 4 bullets — the FY2025 PBT position vs budget in MYR M and %, the 2 worst-performing segments by name, the principal vendor-contract risk identified in IB_08, and the recommended Board decision. Slide 3 segment variance: a table of all segments with Actual vs Budget vs Variance MYR M vs Variance % vs RAG status, plus a horizontal bar chart of variance ranked worst to best. Slide 4 segment commentary: 200-word narrative on the 2 worst segments and what is driving each shortfall. Slide 5 vendor contract findings: a 3-column table — clause subject, BNM Outsourcing Policy gap (per IB_10), proposed redline. Slide 6 management actions: a 5-row RACI for the segments that triggered corrective action plus the vendor remediation. Slide 7 ask of the Board: 3 specific decisions the Board must ratify Thursday. Apply the workshop colour palette and put the Bursa-listed disclosure-standard footer on every slide.'},
     {'instr':'Buka PowerPoint baru atau gunakan template workshop. Buka panel Copilot. Rujuk IB_08_Vendor_Contract.docx dan IB_07_Segment_PnL.xlsx untuk konten. Deck untuk Komite Risiko Dewan hari Kamis.',
      'prompt':'Bangun deck 7-slide Komite Risiko Dewan untuk Zava Capital Indonesia. Slide 1 cover: "Komite Risiko Dewan Akhir Tahun FY2025 — Tinjauan Risiko Vendor & Segmen". Slide 2 ringkasan eksekutif: 4 bullet — posisi PBT FY2025 vs anggaran dalam miliar rupiah dan %, 2 segmen berkinerja terburuk dengan nama, risiko utama kontrak vendor yang diidentifikasi di IB_08, dan rekomendasi keputusan Dewan. Slide 3 varians segmen: tabel semua segmen dengan Aktual vs Anggaran vs Varians (miliar rupiah) vs Varians % vs status RAG, ditambah bar chart horizontal varians diurutkan dari terburuk ke terbaik. Slide 4 komentar segmen: narasi 200 kata tentang 2 segmen terburuk dan apa yang menggerakkan setiap kekurangan. Slide 5 temuan kontrak vendor: tabel 3 kolom — subjek klausul, gap kebijakan outsourcing regulator (per IB_10), redline yang diusulkan. Slide 6 tindakan manajemen: RACI 5-baris untuk segmen yang memicu tindakan korektif ditambah remediasi vendor. Slide 7 permintaan kepada Dewan: 3 keputusan spesifik yang harus diratifikasi Dewan hari Kamis. Terapkan palet warna workshop dan letakkan footer standar pengungkapan tercatat BEI di setiap slide.'},
     'Hadar Caspit', 'Hadar Caspit'),

    # Cowork — Ex3-T3 Pre-Board fan-out (BRC prep in parallel)
    ('T_COWORK',
     {'instr':'Open `m365.cloud.microsoft` > left nav > Agents > **Cowork**. Cowork delegates 5 parallel sub-tasks. Approve each action before files are saved or messages are sent. (Frontier Program required.)',
      'prompt':'I am Hadar (Group CFO) preparing for the FY2025 Board Risk Committee on Thursday at Zava Capital Malaysia. Please complete in parallel: (1) Draft a Word document titled "BRC_Vendor_Risk_Brief.docx" — 3 pages, referencing IB_08_Vendor_Contract.docx and IB_10_Outsourcing_Policy.docx, summarising the 5 highest-severity BNM Outsourcing Policy gaps and the proposed redlines. (2) Draft a Word document titled "BRC_Segment_Variance_Brief.docx" — 3 pages, referencing IB_07_Segment_PnL.xlsx, covering the 2 worst-performing segments, the 10% corrective-action triggers, and the proposed management actions with owners. (3) Draft an email to the Board Risk Committee chair and members previewing the two briefs and confirming Thursday\'s agenda — use the named recipients consistently: Hadar (Group CFO), Sasha (Group Chief of Staff), Daichi (Head of IR), Sonia (Head of Strategy), Will (Head of Risk) and Omar (Head of Procurement), and adapt the precise distribution per sub-task. (4) Schedule a 60-minute pre-read review with Hadar, Will, and Omar tomorrow morning. (5) Post a Teams message to the Group ExCo channel summarising what is going to the BRC and inviting last-call inputs by end of day.'},
     {'instr':'Buka `m365.cloud.microsoft` > navigasi kiri > Agents > **Cowork**. Cowork mendelegasikan 5 sub-tugas paralel. Setujui setiap tindakan sebelum file disimpan atau pesan dikirim. (Membutuhkan Frontier Program.)',
      'prompt':'Saya Hadar (Group CFO) menyiapkan Komite Risiko Dewan FY2025 hari Kamis di Zava Capital Indonesia. Selesaikan secara paralel: (1) Susun dokumen Word "BRC_Vendor_Risk_Brief.docx" — 3 halaman, merujuk IB_08_Vendor_Contract.docx dan IB_10_Outsourcing_Policy.docx, merangkum 5 gap kepatuhan outsourcing regulator dengan tingkat keparahan tertinggi dan redline yang diusulkan. (2) Susun dokumen Word "BRC_Segment_Variance_Brief.docx" — 3 halaman, merujuk IB_07_Segment_PnL.xlsx, mencakup 2 segmen berkinerja terburuk, pemicu tindakan korektif 10%, dan tindakan manajemen yang diusulkan dengan pemilik. (3) Susun email kepada ketua Komite Risiko Dewan dan anggota yang memberi pratinjau dua brief dan mengonfirmasi agenda hari Kamis — gunakan penerima bernama secara konsisten: Hadar (Group CFO), Sasha (Group Chief of Staff), Daichi (Head of IR), Sonia (Head of Strategy), Will (Head of Risk), dan Omar (Head of Procurement), serta sesuaikan distribusi persis per sub-tugas. (4) Jadwalkan tinjauan pra-baca 60 menit dengan Hadar, Will, dan Omar besok pagi. (5) Posting pesan Teams di kanal Group ExCo yang merangkum apa yang akan masuk ke BRC dan mengundang masukan akhir sebelum akhir hari.'},
     'Hadar Caspit', 'Hadar Caspit'),
]


def find_block_range(text, after_pos, tool_token):
    """Find the tool block starting from `after_pos` for the given tool token.
    Returns (start_idx_of_tool_call, end_idx_of_tool_call) — the parentheses range.
    """
    # Look for `tool(T_TOKEN,` or `tool(T_TOKEN ,`
    pat = re.compile(r'\btool\(\s*' + re.escape(tool_token) + r'\b')
    m = pat.search(text, after_pos)
    if not m:
        return None
    # Walk parens from m.end()-1 (the `(`)
    start = text.index('(', m.start())
    depth = 0
    i = start
    in_str = False
    quote = ''
    while i < len(text):
        c = text[i]
        if in_str:
            if c == '\\':
                i += 2
                continue
            if c == quote:
                in_str = False
            i += 1
            continue
        if c in ('"', "'"):
            # Check for triple-quote
            if text[i:i+3] in ('"""', "'''"):
                # Skip triple-string
                q3 = text[i:i+3]
                end3 = text.find(q3, i + 3)
                if end3 < 0:
                    return None
                i = end3 + 3
                continue
            in_str = True
            quote = c
            i += 1
            continue
        if c == '(':
            depth += 1
        elif c == ')':
            depth -= 1
            if depth == 0:
                return (m.start(), i)
        i += 1
    return None


def find_investment_banking_block(text):
    """Find the ind('investment-banking', ...) block. Return start..end paren range."""
    m = re.search(r"\bind\(\s*['\"]investment-banking['\"]", text)
    if not m:
        return None
    start = text.index('(', m.start())
    depth = 0
    i = start
    in_str = False
    quote = ''
    while i < len(text):
        c = text[i]
        if in_str:
            if c == '\\':
                i += 2
                continue
            if c == quote:
                in_str = False
            i += 1
            continue
        if c in ('"', "'"):
            if text[i:i+3] in ('"""', "'''"):
                q3 = text[i:i+3]
                end3 = text.find(q3, i + 3)
                if end3 < 0:
                    return None
                i = end3 + 3
                continue
            in_str = True
            quote = c
            i += 1
            continue
        if c == '(':
            depth += 1
        elif c == ')':
            depth -= 1
            if depth == 0:
                return (m.start(), i)
        i += 1
    return None


def py_repr_dict(d):
    """Render dict with single-quote keys + repr values. Use repr() for values."""
    parts = []
    for k, v in d.items():
        parts.append(f"'{k}':{v!r}")
    return '{' + ', '.join(parts) + '}'


def inject_into_tool_block(text, block_start, block_end, en_dict, id_dict, en_persona, id_persona):
    """Inside the tool block text[block_start..block_end], append:
    - new EN prompt dict to the first list `[ ... ]` after `tool(T_X, LIC, ACCT,`
    - new ID prompt dict to the `promptsID=[...]` list
    - new EN persona name to `persona=[...]`
    - new ID persona name to `personaID=[...]`
    Returns the modified full text + the delta (length change) for tracking subsequent edits.
    """
    block = text[block_start:block_end+1]

    # Find the first `[` at depth 1 INSIDE the block (the EN prompts list).
    # Inside the block, after `tool(T_X, LIC, ACCT,`, the next `[` at depth-1 is the EN list.
    def find_first_list_close(b):
        # Walk past tool( prefix - find the `[` that opens the EN list
        # First, get to the start of args inside tool(
        # b starts with "tool(T_X, ..."
        # Find first `[`
        depth = 0
        i = 0
        in_str = False
        quote = ''
        list_open = None
        while i < len(b):
            c = b[i]
            if in_str:
                if c == '\\':
                    i += 2
                    continue
                if c == quote:
                    in_str = False
                i += 1
                continue
            if c in ('"', "'"):
                if b[i:i+3] in ('"""', "'''"):
                    q3 = b[i:i+3]
                    end3 = b.find(q3, i + 3)
                    if end3 < 0:
                        return None
                    i = end3 + 3
                    continue
                in_str = True
                quote = c
                i += 1
                continue
            if c == '(':
                depth += 1
            elif c == ')':
                depth -= 1
            elif c == '[' and depth == 1:
                list_open = i
                # Walk to matching `]`
                d2 = 1
                j = i + 1
                in_str2 = False
                q2 = ''
                while j < len(b):
                    cc = b[j]
                    if in_str2:
                        if cc == '\\':
                            j += 2
                            continue
                        if cc == q2:
                            in_str2 = False
                        j += 1
                        continue
                    if cc in ('"', "'"):
                        if b[j:j+3] in ('"""', "'''"):
                            q3 = b[j:j+3]
                            end3 = b.find(q3, j + 3)
                            if end3 < 0:
                                return None
                            j = end3 + 3
                            continue
                        in_str2 = True
                        q2 = cc
                        j += 1
                        continue
                    if cc == '[':
                        d2 += 1
                    elif cc == ']':
                        d2 -= 1
                        if d2 == 0:
                            return (list_open, j)
                    j += 1
                return None
            i += 1
        return None

    en_range = find_first_list_close(block)
    if not en_range:
        raise RuntimeError("Cannot find EN list")
    en_open, en_close = en_range

    # Construct EN insert: comma + newline + dict
    en_insert = ',\n        ' + py_repr_dict(en_dict)
    new_block = block[:en_close] + en_insert + block[en_close:]

    # Now find promptsID=[...] in new_block. Position has shifted by len(en_insert) AFTER en_close.
    id_match = re.search(r'promptsID\s*=\s*\[', new_block)
    if not id_match:
        raise RuntimeError("Cannot find promptsID=[")
    id_list_open = id_match.end() - 1
    # Walk to matching `]`
    d3 = 1
    j = id_list_open + 1
    in_str3 = False
    q3c = ''
    while j < len(new_block):
        cc = new_block[j]
        if in_str3:
            if cc == '\\':
                j += 2
                continue
            if cc == q3c:
                in_str3 = False
            j += 1
            continue
        if cc in ('"', "'"):
            if new_block[j:j+3] in ('"""', "'''"):
                q3s = new_block[j:j+3]
                end3 = new_block.find(q3s, j + 3)
                if end3 < 0:
                    raise RuntimeError("Unterminated triple-string in ID list")
                j = end3 + 3
                continue
            in_str3 = True
            q3c = cc
            j += 1
            continue
        if cc == '[':
            d3 += 1
        elif cc == ']':
            d3 -= 1
            if d3 == 0:
                id_close = j
                break
        j += 1
    else:
        raise RuntimeError("No matching ] for promptsID")

    id_insert = ',\n        ' + py_repr_dict(id_dict)
    new_block = new_block[:id_close] + id_insert + new_block[id_close:]

    # Now add EN persona — find persona=[...] (not personaID=)
    p_match = re.search(r'(?<!ID)persona\s*=\s*\[', new_block)
    if not p_match:
        raise RuntimeError("Cannot find persona=[")
    p_list_open = p_match.end() - 1
    # Walk to ]
    d4 = 1
    j = p_list_open + 1
    while j < len(new_block):
        cc = new_block[j]
        if cc == '[':
            d4 += 1
        elif cc == ']':
            d4 -= 1
            if d4 == 0:
                p_close = j
                break
        j += 1
    else:
        raise RuntimeError("No matching ] for persona")

    p_insert = f", '{en_persona}'"
    new_block = new_block[:p_close] + p_insert + new_block[p_close:]

    # Now add ID persona — find personaID=[...]
    pid_match = re.search(r'personaID\s*=\s*\[', new_block)
    if not pid_match:
        raise RuntimeError("Cannot find personaID=[")
    pid_list_open = pid_match.end() - 1
    d5 = 1
    j = pid_list_open + 1
    while j < len(new_block):
        cc = new_block[j]
        if cc == '[':
            d5 += 1
        elif cc == ']':
            d5 -= 1
            if d5 == 0:
                pid_close = j
                break
        j += 1
    else:
        raise RuntimeError("No matching ] for personaID")

    pid_insert = f", '{id_persona}'"
    new_block = new_block[:pid_close] + pid_insert + new_block[pid_close:]

    # Stitch back into full text
    return text[:block_start] + new_block + text[block_end+1:]


def main():
    text = open(FILE, 'r', encoding='utf-8').read()
    ib_range = find_investment_banking_block(text)
    if not ib_range:
        print('investment-banking not found'); return
    ib_start, ib_end = ib_range
    print(f'investment-banking block: {ib_start}..{ib_end} ({ib_end-ib_start} chars)')

    cursor = ib_start
    for tool_token, en_dict, id_dict, en_persona, id_persona in KIBB_INJECTS:
        block_range = find_block_range(text, cursor, tool_token)
        if not block_range:
            print(f'  [SKIP] {tool_token} not found')
            continue
        bs, be = block_range
        if be > ib_end:
            print(f'  [SKIP] {tool_token} outside investment-banking block')
            continue
        before_len = len(text)
        text = inject_into_tool_block(text, bs, be, en_dict, id_dict, en_persona, id_persona)
        delta = len(text) - before_len
        # Update ib_end after insertion
        ib_end += delta
        cursor = bs + delta  # move past this block
        print(f'  [OK]   {tool_token} injected (+{delta} chars)')

    # Validate
    try:
        ast.parse(text)
    except SyntaxError as e:
        print(f'\nSYNTAX ERROR after injection: {e}')
        # Save bad version for inspection
        open(FILE + '.bad', 'w', encoding='utf-8').write(text)
        return

    open(FILE, 'w', encoding='utf-8').write(text)
    print(f'\nWrote: {FILE} ({len(text)} chars)')


if __name__ == '__main__':
    main()
