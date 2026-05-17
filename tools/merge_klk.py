"""Inject KLK customer prompts across multiple industry/dept targets.

KLK source: 86 prompts (steffiyappy.github.io/klk-immersion, password protected).
We pick the most comprehensive/realistic prompts and map them to existing tool
blocks in their natural target. APPEND only — never rewrite existing prompts.

Targets handled (each gets 1-2 prompts):
- plantation (ind_batch5.py)       : Site spreading + parity
- property-development (ind_batch12): Riverside Phase 3 council
- dept-finance (dept_data.py)      : Bank statements reconciliation + GL match
- dept-procurement (dept_data5.py) : UBO sanctions sweep
- dept-hr (dept_data.py)           : Top-50 talent council
- dept-investor-relations (dept_data5): NYSE Quarterly Filing spread
- dept-esg (dept_data3.py)         : GHG Scope 1+2+3 extraction
- dept-strategy (dept_data2.py)    : FY27 plan model walk
- industrial-manufacturing — handled separately (dict factory).

The injector uses the same paren+bracket walker as merge_kibb.py. It supports
positional EN prompts (4th arg of tool()) OR keyword `prompts=[` — because
both forms produce the same "first depth-1 `[` inside tool()" target.
"""
import re, sys, ast, os

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

REPO = r'C:\Users\peiyiyap\zava-copilot-demo'

# ─────────────────────────────────────────────────────────────────────────────
# KLK prompts to inject. Each entry: (file, entry_id, tool_token, en_dict, id_dict, en_persona, id_persona)
# ─────────────────────────────────────────────────────────────────────────────

INJECTS = [
    # ── plantation (ind_batch5.py) — KLK Site Alpha/Beta/Gamma spreading via Excel ──
    ('ind_batch5.py', 'plantation', 'T_EXCEL',
     {'instr':'Open `m365.cloud.microsoft/chat`. Upload the three site monthly performance logs (Site Alpha, Site Beta, Site Gamma) plus the Group Site Performance Template v3. Open the Copilot pane in Excel for the Web and target the Template workbook.',
      'prompt':'Spread the three site monthly performance logs (Site Alpha, Site Beta, Site Gamma — March 2026) into the Group Site Performance Template v3 worksheet. For each site, map the following data points into the template rows: (a) total throughput tonnes vs target tonnes vs LY same-month, (b) extraction rate / oil extraction ratio vs target, (c) operating cost RM per tonne vs budget, (d) FFB yield / hectare vs budget, (e) headcount on site, (f) safety incidents (LTI count + severity). Use the exact tab structure of the template. Where a site log uses different column headings, map to the template equivalent (e.g. "OER%" → "Extraction Rate %"). Flag any data gap with "[VERIFY — source field not found]" in red. At the bottom of the spread, add a Group Roll-up row that sums all three sites for throughput, costs, and incidents, and a one-paragraph executive summary highlighting the worst-performing site, the best-performing site, and any cross-site pattern (e.g. all 3 below FFB yield budget). Cite source file + cell range for every figure pulled.'},
     {'instr':'Buka `m365.cloud.microsoft/chat`. Unggah tiga log performa bulanan site (Site Alpha, Site Beta, Site Gamma) plus Template Group Site Performance v3. Buka panel Copilot di Excel for the Web dan target workbook Template.',
      'prompt':'Spread tiga log performa bulanan site (Site Alpha, Site Beta, Site Gamma — Maret 2026) ke worksheet Template Group Site Performance v3. Untuk setiap site, peta data berikut ke baris template: (a) total throughput ton vs target ton vs LY bulan yang sama, (b) tingkat ekstraksi / oil extraction ratio vs target, (c) biaya operasi RM per ton vs anggaran, (d) FFB yield / hektar vs anggaran, (e) headcount di site, (f) insiden keselamatan (jumlah LTI + tingkat keparahan). Pakai struktur tab template persis. Jika log site memakai heading kolom berbeda, peta ke padanan template (mis. "OER%" → "Extraction Rate %"). Tandai setiap gap data dengan "[VERIFIKASI — field sumber tidak ditemukan]" dengan warna merah. Di bawah hasil spread, tambahkan baris Group Roll-up yang menjumlahkan ketiga site untuk throughput, biaya, dan insiden, dan ringkasan eksekutif satu paragraf yang menonjolkan site dengan kinerja terburuk, terbaik, dan pola lintas site (mis. ketiga site di bawah anggaran FFB yield). Sertakan referensi file sumber + rentang sel untuk setiap angka yang ditarik.'},
     'Hadar Caspit', 'Hadar Caspit'),

    # ── property-development (ind_batch12.py) — KLK Riverside Phase 3 investment council ──
    ('ind_batch12.py', 'property-development', 'T_RESEARCHER',
     {'instr':'Open `m365.cloud.microsoft/chat` > Agents > **Researcher** > select **Model Council**. Paste the prompt below — Researcher convenes a parallel multi-model report and surfaces dissent across the panel.',
      'prompt':'You are acting as a council of AI agents helping Zava Land Malaysia assess the investment merits of the Riverside Mixed-Use Phase 3 development in Klang Valley. The total committed capex is MYR 1.25 billion over FY27-FY28. The site is 8.4 hectares, GDV MYR 2.1 billion, 4 residential towers + 1 retail podium + 1 office block, target completion Q4 FY29. Convene three model voices: (1) GPT-5.5 Thinking acting as a property-development underwriter (focus on IRR/NPV vs hurdle rate, absorption rate vs comparable Klang Valley launches Sunway/Mah Sing/SP Setia, escalation reserve), (2) Claude Opus 4.7 acting as a macro/credit analyst (focus on OPR trajectory, ringgit, HDB-comparable mass-segment pricing, refinancing risk if completion slips by 6/12 months), (3) a judge model that rates which view is more defensible given current market conditions. Each panellist must cite specific evidence. End with a single-page Investment Council recommendation: GO / GO WITH CONDITIONS / NO-GO, three binary decisions the Board must take in the next 30 days, and the top 3 risks that could swing the verdict.'},
     {'instr':'Buka `m365.cloud.microsoft/chat` > Agents > **Researcher** > pilih **Model Council**. Tempel prompt di bawah — Researcher menggelar laporan multi-model paralel dan menampilkan perbedaan pendapat lintas panel.',
      'prompt':'Anda bertindak sebagai council agen AI yang membantu Zava Land Indonesia menilai kelayakan investasi pengembangan Riverside Mixed-Use Fase 3 di Jakarta Selatan. Capex total komitmen adalah Rp 4,2 triliun selama TA27-TA28. Site 8,4 hektar, GDV Rp 7,1 triliun, 4 menara residensial + 1 podium ritel + 1 blok kantor, target rampung Q4 TA29. Kumpulkan tiga suara model: (1) GPT-5.5 Thinking sebagai underwriter pengembangan properti (fokus IRR/NPV vs hurdle rate, tingkat absorpsi vs peluncuran pembanding Sinar Mas Land/Lippo/Ciputra, cadangan eskalasi), (2) Claude Opus 4.7 sebagai analis makro/kredit (fokus lintasan BI Rate, rupiah, harga segmen massa pembanding rusunami, risiko refinancing bila completion molor 6/12 bulan), (3) model judge yang menilai pandangan mana yang lebih dapat dipertahankan di kondisi pasar saat ini. Setiap panelis harus mengutip bukti spesifik. Tutup dengan rekomendasi Investment Council satu halaman: GO / GO WITH CONDITIONS / NO-GO, tiga keputusan biner yang harus diambil Direksi dalam 30 hari, dan tiga risiko teratas yang bisa membalik vonis.'},
     'Mod Admin', 'Mod Admin'),

    # ── dept-finance (dept_data.py) — KLK bank statements → Excel reconciliation ──
    ('dept_data.py', 'dept-finance', 'T_EXCEL',
     {'instr':'Open `m365.cloud.microsoft/chat`. Upload the three bank e-statements (Bank A, Bank B, and a 3rd correspondent bank) for March 2026. Open the Copilot pane in Excel for the Web targeting a NEW blank workbook.',
      'prompt':'Extract the contents of the three bank statements into one Excel workbook with the following columns: Page No, Bank, Transaction Date, Description, Debit, Credit, Balance, GL Account (best-guess from /Group/Finance/GL/COA/), Currency, FX Rate to MYR (if FX), MYR Equivalent. Use one row per transaction. Group by Bank in sheet tabs. On a 4th sheet "Reconciliation", produce: (a) for each bank, opening balance vs closing balance vs sum of debits/credits — parity check; (b) flag any transaction >MYR 100,000 as material; (c) flag any transaction outside normal operating hours (before 7am / after 7pm local) as needing review; (d) flag any duplicate (same amount + same date + same counterparty) as potential double-posting; (e) cross-reference closing balances against /Finance/GL/Mar2026/ trial-balance and flag any account where the bank closing balance differs from GL closing balance by >MYR 1,000. Cite source page + transaction line for every row.'},
     {'instr':'Buka `m365.cloud.microsoft/chat`. Unggah ketiga e-statement bank (Bank A, Bank B, dan bank koresponden ke-3) untuk Maret 2026. Buka panel Copilot di Excel for the Web menargetkan workbook KOSONG baru.',
      'prompt':'Ekstrak isi ketiga laporan bank ke dalam satu workbook Excel dengan kolom berikut: No Halaman, Bank, Tanggal Transaksi, Deskripsi, Debit, Kredit, Saldo, Akun GL (best-guess dari /Group/Finance/GL/COA/), Mata Uang, Kurs ke IDR (bila valas), Padanan IDR. Gunakan satu baris per transaksi. Kelompokkan per Bank dalam tab sheet. Pada sheet ke-4 "Reconciliation", hasilkan: (a) untuk setiap bank, saldo pembukaan vs saldo penutupan vs jumlah debit/kredit — parity check; (b) tandai transaksi >Rp 350 juta sebagai material; (c) tandai transaksi di luar jam operasi normal (sebelum 7 pagi / setelah 7 malam WIB) sebagai perlu di-review; (d) tandai duplikasi (jumlah sama + tanggal sama + counterparty sama) sebagai potensi double-posting; (e) cross-reference saldo penutupan terhadap /Finance/GL/Mar2026/ trial-balance dan tandai akun di mana saldo penutupan bank berbeda dengan saldo penutupan GL >Rp 4 juta. Sertakan referensi halaman sumber + baris transaksi untuk setiap baris.'},
     'Hadar Caspit', 'Hadar Caspit'),

    # ── dept-hr (dept_data.py) — KLK FY26 Top-50 talent council review ──
    ('dept_data.py', 'dept-hr', 'T_RESEARCHER',
     {'instr':'Open `m365.cloud.microsoft/chat` > Agents > **Researcher** > select **Model Council**. Paste the prompt below — Researcher convenes a parallel multi-model report and surfaces dissent across the panel.',
      'prompt':'You are acting as a council of AI agents helping Zava Group HR run the FY26 Top-50 talent review. For each of the 50 critical leadership roles (CEO/CFO direct reports + 1 layer below, across Plantation, Manufacturing, Property, Finance, IR, Risk, Procurement, Strategy, IT, HR), assume the role profile, current incumbent tenure, last 2 years performance ratings, succession bench depth, and external benchmark are provided. Convene 4 model voices: (1) GPT-5.5 Thinking as a performance-management advocate (focus: who must be replaced in next 12 months, who is ready-now for promotion, who is at flight risk); (2) Claude Opus 4.7 as a succession planner (focus: which roles have NO ready successor, which need an external hire pipeline, which can be filled internally with 6-month development); (3) GPT-5.5 again as a diversity & inclusion lens (focus: female leadership representation, regional balance MY/ID/SG, age/generation mix); (4) a judge model that synthesises the three views into a single Top-50 grid with RAG status (Red = action this quarter, Amber = monitor, Green = stable) and recommended next action per role. Each panellist must cite specific role data. End with a 5-bullet executive summary for the Board Nomination & Remuneration Committee.'},
     {'instr':'Buka `m365.cloud.microsoft/chat` > Agents > **Researcher** > pilih **Model Council**. Tempel prompt di bawah — Researcher menggelar laporan multi-model paralel dan menampilkan perbedaan pendapat lintas panel.',
      'prompt':'Anda bertindak sebagai council agen AI yang membantu HR Zava Group menjalankan review talenta Top-50 TA26. Untuk masing-masing 50 posisi pimpinan kritikal (laporan langsung CEO/CFO + 1 lapis di bawahnya, lintas Plantation, Manufaktur, Properti, Keuangan, IR, Risiko, Pengadaan, Strategi, IT, HR), asumsikan profil posisi, masa jabatan incumbent saat ini, rating kinerja 2 tahun terakhir, kedalaman bench suksesi, dan benchmark eksternal telah tersedia. Kumpulkan 4 suara model: (1) GPT-5.5 Thinking sebagai advokat performance-management (fokus: siapa yang harus diganti dalam 12 bulan, siapa yang ready-now untuk promosi, siapa yang flight risk); (2) Claude Opus 4.7 sebagai succession planner (fokus: posisi mana yang TIDAK punya successor siap, mana yang butuh pipeline hire eksternal, mana yang bisa diisi internal dengan pengembangan 6 bulan); (3) GPT-5.5 lagi sebagai lensa diversity & inclusion (fokus: representasi pimpinan perempuan, keseimbangan regional MY/ID/SG, bauran usia/generasi); (4) model judge yang mensintesa tiga pandangan ke satu grid Top-50 dengan status RAG (Merah = aksi kuartal ini, Kuning = monitor, Hijau = stabil) dan rekomendasi aksi berikutnya per posisi. Setiap panelis harus mengutip data posisi spesifik. Tutup dengan ringkasan eksekutif 5-poin untuk Komite Nominasi & Remunerasi Direksi.'},
     'Sasha Ouellet', 'Sasha Ouellet'),

    # ── dept-investor-relations (dept_data5.py) — KLK NYSE Quarterly Filing Template spreading ──
    ('dept_data5.py', 'dept-investor-relations', 'T_EXCEL',
     {'instr':'Open `m365.cloud.microsoft/chat`. Upload the Q1 FY26 trial balance workbook + segment reporting workbook + the Exchange Quarterly Filing Template v6 (Bursa Malaysia / IDX format). Open the Copilot pane in Excel for the Web targeting the Template workbook.',
      'prompt':'Spread the Q1 FY26 trial balance and segment reporting workbooks into the Exchange Quarterly Filing Template v6. Map every GL account to the corresponding template line (Income Statement, Balance Sheet, Cash Flow Statement, Segment Reporting, Notes). After spreading, run a four-way parity check on a new "Reconciliation" sheet: (1) Template Group total revenue = sum of segment revenue; (2) Template Group net profit = sum of segment net profit + corporate adjustments; (3) Template closing equity = opening equity + net profit - dividends + OCI movements; (4) Template segment-reporting reconciliation = trial-balance segment totals (within MYR 1,000 tolerance). Highlight every parity check that fails in red. Where a GL account does not map cleanly to a template line, flag it as "[NEEDS REVIEW — no template line]". Cite source file + sheet + cell range for every figure mapped. End with a 4-bullet executive summary for the Head of IR: total revenue YoY, total PAT YoY, biggest segment driver, biggest non-segment surprise.'},
     {'instr':'Buka `m365.cloud.microsoft/chat`. Unggah workbook trial balance Q1 TA26 + workbook pelaporan segmen + Template Exchange Quarterly Filing v6 (format IDX/BEI). Buka panel Copilot di Excel for the Web menargetkan workbook Template.',
      'prompt':'Spread workbook trial balance Q1 TA26 dan pelaporan segmen ke dalam Template Exchange Quarterly Filing v6. Peta setiap akun GL ke baris template padanan (Laporan Laba Rugi, Neraca, Laporan Arus Kas, Pelaporan Segmen, Catatan). Setelah spread, jalankan parity check empat-arah pada sheet baru "Reconciliation": (1) Total pendapatan Grup di Template = jumlah pendapatan segmen; (2) Laba bersih Grup di Template = jumlah laba bersih segmen + penyesuaian korporat; (3) Ekuitas penutup Template = ekuitas pembukaan + laba bersih - dividen + gerakan OCI; (4) Rekonsiliasi pelaporan segmen Template = total segmen trial-balance (dalam toleransi Rp 4 juta). Tandai setiap parity check yang gagal dengan warna merah. Bila akun GL tidak memetakan rapi ke baris template, tandai "[PERLU REVIEW — tidak ada baris template]". Sertakan referensi file sumber + sheet + rentang sel untuk setiap angka yang dipetakan. Tutup dengan ringkasan eksekutif 4-poin untuk Head of IR: pendapatan total YoY, PAT total YoY, pendorong segmen terbesar, kejutan non-segmen terbesar.'},
     'Daichi Maruyama', 'Daichi Maruyama'),

    # ── dept-procurement (dept_data5.py) — KLK UBO sanctions sweep ──
    ('dept_data5.py', 'dept-procurement', 'T_RESEARCHER',
     {'instr':'Open `m365.cloud.microsoft/chat` > Agents > **Researcher** > select **Critique Mode**. Upload the vendor application form (counterparty PDF). Paste the prompt below — Researcher will self-critique every source.',
      'prompt':'Create an Ultimate Beneficial Ownership (UBO) diagram for PT Acme Industrial Lestari (the vendor on the attached application). Recursively identify all owners with >10% direct or indirect equity, all directors and commissioners, and any related-party (same surname, same registered address, same nominee director). For each node in the UBO tree, run in parallel: (a) sanctions screening against OFAC SDN, EU Consolidated List, UK HMT, MAS sanctions list, FinCEN 311 designations, and BNM Cease-and-Desist register — flag any direct or partial-name match with confidence score; (b) adverse-media sweep across the last 36 months in Reuters, Bloomberg, AsiaNews, Tempo, The Edge, The Star — focus on fraud, bribery, money-laundering, sanctions evasion, tax evasion, environmental violation, labour violation; (c) Politically-Exposed-Person (PEP) check against the regional PEP databases. For each UBO node produce a single-row risk summary: Name, Role, %, Direct/Indirect, Country of Residence, Sanctions Result (CLEAR / POTENTIAL / MATCH), Adverse Media Result (CLEAR / FINDINGS), PEP Status. End with a single-paragraph Procurement Committee recommendation: APPROVE / APPROVE WITH ENHANCED DD / DEFER / REJECT, citing the specific UBO node(s) that drive the decision.'},
     {'instr':'Buka `m365.cloud.microsoft/chat` > Agents > **Researcher** > pilih **Critique Mode**. Unggah formulir aplikasi vendor (PDF counterparty). Tempel prompt di bawah — Researcher akan mengkritik setiap sumber.',
      'prompt':'Buat diagram Ultimate Beneficial Ownership (UBO) untuk PT Acme Industrial Lestari (vendor pada aplikasi terlampir). Identifikasi rekursif semua pemilik dengan >10% ekuitas langsung atau tidak langsung, semua direktur dan komisaris, dan setiap pihak berelasi (marga sama, alamat terdaftar sama, direktur nominee sama). Untuk setiap simpul di pohon UBO, jalankan paralel: (a) screening sanksi terhadap OFAC SDN, EU Consolidated List, UK HMT, daftar sanksi MAS, designasi FinCEN 311, dan register Cease-and-Desist OJK — tandai setiap kecocokan nama langsung atau parsial dengan confidence score; (b) sapuan adverse-media 36 bulan terakhir di Reuters, Bloomberg, Tempo, Kontan, Kompas, Bisnis Indonesia — fokus pada fraud, suap, pencucian uang, evasi sanksi, evasi pajak, pelanggaran lingkungan, pelanggaran ketenagakerjaan; (c) cek Politically-Exposed-Person (PEP) terhadap database PEP regional. Untuk setiap simpul UBO hasilkan ringkasan risiko satu-baris: Nama, Peran, %, Langsung/Tidak Langsung, Negara Domisili, Hasil Sanksi (CLEAR / POTENTIAL / MATCH), Hasil Adverse Media (CLEAR / FINDINGS), Status PEP. Tutup dengan rekomendasi satu paragraf Komite Pengadaan: SETUJUI / SETUJUI DENGAN DD DIPERKUAT / TUNDA / TOLAK, dengan menyebutkan simpul UBO spesifik yang mendasari keputusan.'},
     'Hadar Caspit', 'Hadar Caspit'),

    # ── dept-strategy (dept_data2.py) — KLK FY27 group plan model walk + sensitivity ──
    ('dept_data2.py', 'dept-strategy', 'T_ANALYST',
     {'instr':'Open `m365.cloud.microsoft/chat` > Agents > **Analyst**. Upload the FY27 group plan model (multi-tab Excel covering all divisions, intercompany eliminations, group-level inputs). Analyst writes Python under the hood — no formula needed.',
      'prompt':'You are Analyst for Zava Group Strategy. Using the FY27 group plan model, run a 6-output strategic analysis the Group Strategy Director can present at the Strategy Off-site in 10 days. (1) Walk me through the model structure — divisions, drivers, intercompany eliminations, and any assumption I should challenge (highlight the 5 assumptions with the largest swing impact). (2) Run a parity report at the original plan assumptions against the spreadsheet: revenue, EBITDA, PAT by division, group total — show any cell where the model output differs from the workbook by >MYR 1M. (3) Sensitivity analysis: re-run the model with three scenarios — Base (current assumptions), Downside (commodity prices -10%, MYR -5% vs USD, OPR +50bps), Upside (commodity prices +10%, MYR +5%, OPR -25bps). For each scenario produce a one-screen table of revenue/EBITDA/PAT by division. (4) Tornado chart showing which 10 assumptions have the largest impact on FY27 group PAT (±20% test). (5) Cluster the 11 divisions into 3 strategic tiers via k-means on FY27 EBITDA margin + FY27 revenue growth + FY27 capex intensity — label as "Cash Cow / Growth / Restructure". (6) A 10-slide outline for the Strategy Off-site deck with a clear narrative arc. Show the Python code in a collapsible block so the strategy team can re-run.'},
     {'instr':'Buka `m365.cloud.microsoft/chat` > Agents > **Analyst**. Unggah model rencana grup TA27 (Excel multi-tab mencakup semua divisi, eliminasi intercompany, input level grup). Analyst menulis Python di bawah selimut — tidak perlu rumus.',
      'prompt':'Anda Analyst untuk Strategi Grup Zava. Menggunakan model rencana grup TA27, jalankan analisis strategis 6-output yang dapat dipresentasikan Direktur Strategi Grup di Strategy Off-site dalam 10 hari. (1) Jelaskan struktur model — divisi, driver, eliminasi intercompany, dan asumsi apa pun yang harus saya tantang (sorot 5 asumsi dengan dampak ayun terbesar). (2) Jalankan laporan parity pada asumsi rencana asli vs spreadsheet: pendapatan, EBITDA, PAT per divisi, total grup — tampilkan sel mana pun di mana output model berbeda dari workbook >Rp 3,5 miliar. (3) Analisis sensitivitas: re-run model dengan tiga skenario — Dasar (asumsi saat ini), Downside (harga komoditas -10%, IDR -5% vs USD, BI Rate +50bps), Upside (harga komoditas +10%, IDR +5%, BI Rate -25bps). Untuk setiap skenario hasilkan tabel satu-layar pendapatan/EBITDA/PAT per divisi. (4) Tornado chart yang menunjukkan 10 asumsi dengan dampak terbesar pada PAT grup TA27 (uji ±20%). (5) Cluster 11 divisi ke 3 tier strategis via k-means pada margin EBITDA TA27 + pertumbuhan pendapatan TA27 + intensitas capex TA27 — beri label "Cash Cow / Growth / Restructure". (6) Outline 10-slide untuk deck Strategy Off-site dengan alur narasi jelas. Tampilkan kode Python dalam blok lipat agar tim strategi dapat menjalankan ulang.'},
     'Mod Admin', 'Mod Admin'),

    # ── dept-esg (dept_data3.py) — KLK GHG Scope 1+2+3 extraction from 12 site logs ──
    ('dept_data3.py', 'dept-esg', 'T_ANALYST',
     {'instr':'Open `m365.cloud.microsoft/chat` > Agents > **Analyst**. Upload the 12 site monthly fuel/energy/consumables logs (1 per site x 12 sites). Analyst writes Python under the hood — no formula needed.',
      'prompt':'Extract diesel litres, electricity kWh, consumables tonnes (with N/P/K split where stated), and methane (kg) from the 12 attached site monthly logs for March 2026. For each site produce a row in a new workbook with columns Site / Diesel (L) / Electricity (kWh) / Consumables N (t) / Consumables P (t) / Consumables K (t) / Methane (kg). Compute Scope 1 (diesel + methane + on-site fugitive emissions) using the DEFRA 2024 emission factors. Compute Scope 2 (electricity) using location-based factors (TNB grid for Malaysia sites, PLN grid for Indonesia sites). Compute Scope 3 (consumables) using the GHG Protocol Category 1 emission factors for inorganic fertilisers. Convert all to tCO2e. Run an outlier sweep: (a) site-month combinations where diesel litres / active acre is >2 standard deviations above the cohort; (b) months where electricity kWh is >2 standard deviations above the prior 12-month rolling average; (c) any site where Scope 1+2+3 intensity per tonne of output is in the top quartile. Output: (i) a Group Scope 1+2+3 dashboard table (12 sites + Group total) with absolute tCO2e and intensity (tCO2e/tonne); (ii) an outlier table with Site / Month / Metric / Value / Cohort mean / Std Dev / Z-score; (iii) a 3-bullet narrative for the Sustainability Director. Show the Python code in a collapsible block.'},
     {'instr':'Buka `m365.cloud.microsoft/chat` > Agents > **Analyst**. Unggah 12 log bulanan site untuk bahan bakar/energi/bahan habis pakai (1 per site x 12 site). Analyst menulis Python di bawah selimut — tidak perlu rumus.',
      'prompt':'Ekstrak liter diesel, kWh listrik, ton bahan habis pakai (dengan pemisahan N/P/K bila tersedia), dan kg metana dari 12 log bulanan site terlampir untuk Maret 2026. Untuk setiap site hasilkan satu baris di workbook baru dengan kolom Site / Diesel (L) / Listrik (kWh) / Bahan habis pakai N (t) / Bahan habis pakai P (t) / Bahan habis pakai K (t) / Metana (kg). Hitung Scope 1 (diesel + metana + emisi fugitif on-site) menggunakan faktor emisi DEFRA 2024. Hitung Scope 2 (listrik) menggunakan faktor lokasi (jaringan TNB untuk site Malaysia, jaringan PLN untuk site Indonesia). Hitung Scope 3 (bahan habis pakai) menggunakan faktor emisi Kategori 1 GHG Protocol untuk pupuk anorganik. Konversi semua ke tCO2e. Jalankan sapuan outlier: (a) kombinasi site-bulan di mana liter diesel / acre aktif >2 simpangan baku di atas kohort; (b) bulan di mana kWh listrik >2 simpangan baku di atas rata-rata bergulir 12 bulan; (c) site mana pun di mana intensitas Scope 1+2+3 per ton output berada di kuartil teratas. Output: (i) tabel dashboard Scope 1+2+3 Grup (12 site + total Grup) dengan tCO2e absolut dan intensitas (tCO2e/ton); (ii) tabel outlier dengan Site / Bulan / Metrik / Nilai / Rata-rata kohort / Simpangan Baku / Z-score; (iii) narasi 3-poin untuk Direktur Keberlanjutan. Tampilkan kode Python dalam blok lipat.'},
     'Daichi Maruyama', 'Daichi Maruyama'),
]


# ─────────────────────────────────────────────────────────────────────────────
# Injector (port of merge_kibb.py find/walk logic, parametrised by entry id)
# ─────────────────────────────────────────────────────────────────────────────

def find_entry_block(text, entry_id):
    """Find the ind('X', ...) OR ind(id='X', ...) block. Return (start, end) paren range."""
    # Try positional: ind('X', ...) or ind("X", ...)
    pat1 = re.compile(r"\bind\(\s*['\"]" + re.escape(entry_id) + r"['\"]")
    m = pat1.search(text)
    if not m:
        # Try keyword: ind(id='X', ...) or ind(\n  id='X', ...)
        pat2 = re.compile(r"\bind\(\s*[\n\s]*id\s*=\s*['\"]" + re.escape(entry_id) + r"['\"]")
        m = pat2.search(text)
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
                i += 2; continue
            if c == quote:
                in_str = False
            i += 1; continue
        if c in ('"', "'"):
            if text[i:i+3] in ('"""', "'''"):
                q3 = text[i:i+3]
                end3 = text.find(q3, i + 3)
                if end3 < 0: return None
                i = end3 + 3; continue
            in_str = True; quote = c; i += 1; continue
        if c == '(': depth += 1
        elif c == ')':
            depth -= 1
            if depth == 0:
                return (m.start(), i)
        i += 1
    return None


def find_tool_block(text, after_pos, tool_token, block_end_limit):
    """Find tool(T_X, ...) within text[after_pos:block_end_limit]."""
    pat = re.compile(r'\btool\(\s*' + re.escape(tool_token) + r'\b')
    m = pat.search(text, after_pos)
    if not m or m.start() > block_end_limit:
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
                i += 2; continue
            if c == quote:
                in_str = False
            i += 1; continue
        if c in ('"', "'"):
            if text[i:i+3] in ('"""', "'''"):
                q3 = text[i:i+3]
                end3 = text.find(q3, i + 3)
                if end3 < 0: return None
                i = end3 + 3; continue
            in_str = True; quote = c; i += 1; continue
        if c == '(': depth += 1
        elif c == ')':
            depth -= 1
            if depth == 0:
                return (m.start(), i)
        i += 1
    return None


def py_repr_dict(d):
    parts = []
    for k, v in d.items():
        parts.append(f"'{k}':{v!r}")
    return '{' + ', '.join(parts) + '}'


def inject_into_tool_block(text, block_start, block_end, en_dict, id_dict, en_persona, id_persona):
    block = text[block_start:block_end+1]

    # Find first `[` at depth 1 inside tool() — this is EN prompts list
    def find_first_list_close(b):
        depth = 0
        i = 0
        in_str = False
        quote = ''
        while i < len(b):
            c = b[i]
            if in_str:
                if c == '\\':
                    i += 2; continue
                if c == quote:
                    in_str = False
                i += 1; continue
            if c in ('"', "'"):
                if b[i:i+3] in ('"""', "'''"):
                    q3 = b[i:i+3]
                    end3 = b.find(q3, i + 3)
                    if end3 < 0: return None
                    i = end3 + 3; continue
                in_str = True; quote = c; i += 1; continue
            if c == '(': depth += 1
            elif c == ')': depth -= 1
            elif c == '[' and depth == 1:
                list_open = i
                d2 = 1; j = i + 1; in_str2 = False; q2 = ''
                while j < len(b):
                    cc = b[j]
                    if in_str2:
                        if cc == '\\':
                            j += 2; continue
                        if cc == q2:
                            in_str2 = False
                        j += 1; continue
                    if cc in ('"', "'"):
                        if b[j:j+3] in ('"""', "'''"):
                            q3 = b[j:j+3]
                            end3 = b.find(q3, j + 3)
                            if end3 < 0: return None
                            j = end3 + 3; continue
                        in_str2 = True; q2 = cc; j += 1; continue
                    if cc == '[': d2 += 1
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
    en_insert = ',\n        ' + py_repr_dict(en_dict)
    new_block = block[:en_close] + en_insert + block[en_close:]

    # promptsID
    id_match = re.search(r'promptsID\s*=\s*\[', new_block)
    if not id_match:
        raise RuntimeError("Cannot find promptsID=[")
    id_list_open = id_match.end() - 1
    d3 = 1; j = id_list_open + 1; in_str3 = False; q3c = ''
    while j < len(new_block):
        cc = new_block[j]
        if in_str3:
            if cc == '\\':
                j += 2; continue
            if cc == q3c:
                in_str3 = False
            j += 1; continue
        if cc in ('"', "'"):
            if new_block[j:j+3] in ('"""', "'''"):
                q3s = new_block[j:j+3]
                end3 = new_block.find(q3s, j + 3)
                if end3 < 0:
                    raise RuntimeError("Unterminated triple-string in ID list")
                j = end3 + 3; continue
            in_str3 = True; q3c = cc; j += 1; continue
        if cc == '[': d3 += 1
        elif cc == ']':
            d3 -= 1
            if d3 == 0:
                id_close = j; break
        j += 1
    else:
        raise RuntimeError("No matching ] for promptsID")

    id_insert = ',\n        ' + py_repr_dict(id_dict)
    new_block = new_block[:id_close] + id_insert + new_block[id_close:]

    # persona (NOT personaID) — optional
    p_match = re.search(r'(?<!ID)persona\s*=\s*\[', new_block)
    if p_match:
        p_list_open = p_match.end() - 1
        d4 = 1; j = p_list_open + 1
        while j < len(new_block):
            cc = new_block[j]
            if cc == '[': d4 += 1
            elif cc == ']':
                d4 -= 1
                if d4 == 0:
                    p_close = j; break
            j += 1
        else:
            raise RuntimeError("No matching ] for persona")
        new_block = new_block[:p_close] + f", '{en_persona}'" + new_block[p_close:]

    # personaID — optional
    pid_match = re.search(r'personaID\s*=\s*\[', new_block)
    if pid_match:
        pid_list_open = pid_match.end() - 1
        d5 = 1; j = pid_list_open + 1
        while j < len(new_block):
            cc = new_block[j]
            if cc == '[': d5 += 1
            elif cc == ']':
                d5 -= 1
                if d5 == 0:
                    pid_close = j; break
            j += 1
        else:
            raise RuntimeError("No matching ] for personaID")
        new_block = new_block[:pid_close] + f", '{id_persona}'" + new_block[pid_close:]

    return text[:block_start] + new_block + text[block_end+1:]


def main():
    # Group injects by file
    by_file = {}
    for inj in INJECTS:
        by_file.setdefault(inj[0], []).append(inj)

    for fname, group in by_file.items():
        fpath = os.path.join(REPO, fname)
        # Make backup
        bak = fpath + '.klkbak'
        if not os.path.exists(bak):
            import shutil; shutil.copy(fpath, bak)
        text = open(fpath, 'r', encoding='utf-8').read()
        print(f'\n=== {fname} ({len(group)} injects) ===')
        orig_len = len(text)

        # Group by entry_id within file (multiple tool injections per entry)
        # Process entries in file order so cursor advances correctly
        # Find entry blocks fresh on each iteration (text shifts as we inject)
        for fname2, entry_id, tool_token, en_dict, id_dict, en_persona, id_persona in group:
            entry_range = find_entry_block(text, entry_id)
            if not entry_range:
                print(f'  [SKIP] {entry_id} not found')
                continue
            es, ee = entry_range
            tool_range = find_tool_block(text, es, tool_token, ee)
            if not tool_range:
                print(f'  [SKIP] {entry_id} :: {tool_token} not found')
                continue
            bs, be = tool_range
            before_len = len(text)
            try:
                text = inject_into_tool_block(text, bs, be, en_dict, id_dict, en_persona, id_persona)
            except Exception as e:
                print(f'  [ERR]  {entry_id} :: {tool_token} — {e}')
                continue
            delta = len(text) - before_len
            print(f'  [OK]   {entry_id} :: {tool_token} (+{delta} chars)')

        # AST parse before writing
        try:
            ast.parse(text)
        except SyntaxError as e:
            print(f'  SYNTAX ERROR after injection in {fname}: {e}')
            open(fpath + '.bad', 'w', encoding='utf-8').write(text)
            print(f'  Bad version saved to {fpath}.bad — restoring backup')
            import shutil; shutil.copy(bak, fpath)
            continue
        open(fpath, 'w', encoding='utf-8').write(text)
        print(f'  Wrote: {fpath} ({len(text)} chars, +{len(text)-orig_len})')


if __name__ == '__main__':
    main()
