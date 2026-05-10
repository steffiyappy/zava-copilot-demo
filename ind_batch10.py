
import sys; sys.path.insert(0,'.')
from util import *

# ────────────────────────────────────────────────────────────────────────
#  Batch 10  —  Newly added industries to close coverage gaps:
#    1. Food & FMCG               (Japfa / Nippon Indosari / Mamee / F&N flavour)
#    2. Rubber Gloves Mfg         (Hartalega / Top Glove / Kossan flavour)
#    3. Mortgage Finance          (Cagamas Bhd flavour)
#    4. Cross-border Remittance   (Merchantrade Asia / Tranglo flavour)
#    5. Auto Components & Tyres   (Gajah Tunggal / Indo Kordsa flavour)
#    6. Semiconductor / E&E Mfg   (Western Digital / Micron / Pentamaster flavour)
#    7. Rare-Earth & Metals       (Lynas / Malaysia Mining Corp flavour)
#
#  Each entry:
#   • 4-phase day-in-the-life storyboard
#   • 14 Copilot tools (Chat / Researcher / Analyst / Excel / Word / PPT /
#     Outlook / Teams / Notebook / Cowork / Word-Agt / PPT-Agt / Excel-Agt /
#     Builder)
#   • EN + ID prompts
#   • 4 standard personas mapped to industry-appropriate roles
#   • 4 industry-specific reference files
# ────────────────────────────────────────────────────────────────────────

INDUSTRIES_10 = []


# ╔══════════════════════════════════════════════════════════════════════╗
# ║  1.  FOOD & FMCG                                                     ║
# ╚══════════════════════════════════════════════════════════════════════╝
INDUSTRIES_10.append(ind(
    'food-fmcg', 'sec-food', 'Food & FMCG', '🍜', '#F59E0B', '#D97706',
    'Zava Foods Indonesia',
    'Q4 FY2025 trade-spend overrun MYR 78M; key SKU recall in 2 markets — Board pack in 5 days.',
    "Zava Foods Indonesia is an ASEAN-listed food and FMCG group with 14 manufacturing plants across Indonesia, Malaysia, Singapore and the Philippines, producing instant noodles, dairy, beverages, baked goods, snacks and edible-oils for over 250 SKUs. Trade-spend in Q4 FY2025 overran budget by MYR 78M (+22%) driven by aggressive promo activity in modern trade and weaker general-trade sell-through. A Salmonella scare on one bakery SKU triggered a precautionary recall in Malaysia and Singapore — BPOM Indonesia, MOH Malaysia and SFA Singapore have all opened files. Edible-oil costs jumped 18% on CPO volatility, squeezing margins on the 4 highest-volume noodle SKUs. The Group CFO needs a Board pack in 5 days covering trade-spend control, the recall remediation programme, gross-margin recovery, and FY2026 promo guardrails. Real customer reference frame: the group operates similarly to Japfa Comfeed, Nippon Indosari Corpindo, **Sari Melati Kapital** (Pizza Hut Malaysia operator), Mamee-Double Decker, Spritzer, F&N Holdings, Malayan Flour Mills and Ajinomoto Indonesia.",
    ['FMCG_01_Trade_Spend_Tracker.xlsx','FMCG_02_SKU_Margin_Tracker.xlsx','FMCG_03_Recall_Remediation_Programme.docx','FMCG_04_Edible_Oil_Hedge_Book.xlsx','FMCG_05_FY2026_Promo_Guardrails.docx'],
    [
      tool(T_CHAT, FREE_LIC, FREE_ACCT, [
        {'instr':'', 'prompt':'Trade-spend in Q4 FY2025 overran budget by MYR 78 million (+22%) driven mainly by modern-trade promo aggression on the noodle and dairy SKUs. Draft a 1-page note for the Group CFO that frames the overrun in plain language, lists the 5 questions the Board will ask first, and identifies the 3 decisions the CFO must take before the Audit Committee opens. Present as a structured table with columns for Issue, Why It Matters, Board Question, and Recommended Answer.'},
        {'instr':'', 'prompt':'Write a 90-second verbal opening for the Board meeting in 5 days that acknowledges the MYR 78M trade-spend overrun and the precautionary Salmonella recall in Malaysia and Singapore directly, explains the role of CPO volatility and modern-trade promo intensity without sounding defensive, and signals a credible 2-quarter margin restoration path. End with 3 talking points the CFO can use if the Board challenges promo discipline or QA controls.'},
        {'instr':'', 'prompt':'Build a stakeholder communication map for the Q4 FY2025 trade-spend overrun and the active Salmonella recall ahead of the Board meeting. Identify the priority audiences (BPOM Indonesia, MOH Malaysia, SFA Singapore, top-3 modern-trade chains, the recall-affected consumers via the 24h hotline, the 4 outsourced co-packers, and the FY2026 promo-funding banks), the message each audience requires, the timing, and the main communication risk if the message is mishandled. Present as a RAG table with Red for same-day, Amber for 24-hour, and Green for monitor-only audiences.'}
      ], DESC_CHAT,
      promptsID=[
        {'instr':'', 'prompt':'Trade-spend kuartal 4 FY2025 melebihi anggaran sebesar Rp 280 miliar (+22%) terutama karena agresivitas promo di modern trade pada SKU mie dan dairy. Susun nota tajam 1 halaman untuk Direktur Keuangan Grup yang membingkai pembengkakan dalam bahasa sederhana, mendaftar 5 pertanyaan yang akan ditanyakan Direksi pertama-tama, dan mengidentifikasi 3 keputusan yang harus diambil Direktur Keuangan sebelum Komite Audit dibuka. Sajikan sebagai tabel terstruktur dengan kolom Isu, Mengapa Penting, Pertanyaan Direksi, dan Jawaban yang Direkomendasikan.'},
        {'instr':'', 'prompt':'Tulis pembukaan lisan 90 detik untuk Rapat Direksi dalam 5 hari yang mengakui pembengkakan trade-spend Rp 280 miliar dan recall pencegahan Salmonella di Malaysia dan Singapura secara langsung, menjelaskan peran volatilitas CPO dan intensitas promo modern-trade tanpa terdengar defensif, dan memberikan sinyal jalur pemulihan margin 2-kuartal yang kredibel. Akhiri dengan 3 talking points untuk dipakai Direktur Keuangan bila Direksi menantang disiplin promo atau pengendalian QA.'},
        {'instr':'', 'prompt':'Bangun peta komunikasi pemangku kepentingan untuk pembengkakan trade-spend kuartal 4 FY2025 dan recall Salmonella aktif menjelang Rapat Direksi. Identifikasi audiens prioritas (BPOM Indonesia, KKM Malaysia, SFA Singapura, 3 chain modern-trade teratas, konsumen terdampak recall via hotline 24 jam, 4 co-packer eksternal, dan bank pendana promo FY2026), pesan inti tiap audiens, timing, dan risiko komunikasi utama bila pesan keliru. Sajikan sebagai tabel RAG dengan Merah untuk hari ini juga, Kuning untuk 24 jam, dan Hijau untuk audiens monitor saja.'}
      ],
      persona=['Sasha Ouellet','Mod Admin','Hadar Caspit'],
      personaID=['Sasha Ouellet','Mod Admin','Hadar Caspit']),

      tool(T_RESEARCHER, M365_LIC, M365_ACCT, [
        {'instr':'Open `m365.cloud.microsoft/chat` > Agents > **Researcher** > select **Critique Mode**. Paste the prompt below — Researcher will draft a deep market study and a second model peer-reviews every claim and citation before it lands.', 'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. Zava Foods Indonesia is preparing a Board pack in 5 days. We need credible peer cases including but not limited to Indofood, Mayora, Wings Group, Japfa, Nippon Indosari, F&N Holdings, Mamee Double Decker and Nestlé Malaysia. Here is exactly what I need from you. I need a defensible benchmark of how listed ASEAN food and FMCG groups have managed Q4 trade-spend overruns of more than 15 percent and concurrent product-recall events between 2020 and 2025. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. For each peer, identify the trigger event, the trade-spend control programme adopted within 90 days, the recall-handling decisions, and the gross-margin trajectory 12 to 24 months later. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. Cite every source with publication date. Critically, instruct Researcher to peer-review each claim against the original publication, flag any claim it cannot independently verify, and present as a structured comparison table with columns for Peer, Trigger, 90-Day Programme, Recall Handling, Margin Outcome, Citation. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'},
        {'instr':'Open `m365.cloud.microsoft/chat` > Agents > **Researcher** > select **Model Council**. Paste the prompt below — Researcher runs the question through GPT and Claude in parallel, then a synthesis cover letter highlights agreements, disagreements and unique findings.', 'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. Zava Foods Indonesia operates across 4 ASEAN markets with regulators (BPOM, MOH, SFA, FDA Philippines) all on alert. Here is exactly what I need from you. Identify the 3 most defensible playbooks for an FMCG group dealing with simultaneous trade-spend overrun and product-recall pressure. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. Use Researcher with Model Council enabled — convene parallel reports from GPT and Claude on trade-spend rationalisation, SKU portfolio pruning, recall communication, and CPO hedge restructuring. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. Surface dissent across the panel, summarise the majority position, mark the minority view, and present as a comparison table with columns for Playbook, Council Verdict, Dissenting View, ASEAN Precedent, and Implementation Risk for a CFO-led 90-day plan. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'}
      ], DESC_RESEARCHER,
      promptsID=[
        {'instr':'Buka `m365.cloud.microsoft/chat` > Agents > **Researcher** > pilih **Critique Mode**. Tempel prompt — Researcher menyusun draf riset mendalam lalu model kedua mengkritisi tiap klaim dan kutipan sebelum hasilnya diterima.', 'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. Zava Foods Indonesia menyiapkan paket Direksi dalam 5 hari. Kami butuh studi kasus peer yang kredibel termasuk Indofood, Mayora, Wings Group, Japfa, Nippon Indosari, F&N Holdings, Mamee Double Decker dan Nestlé Malaysia. Berikut yang saya butuhkan dari Anda secara persis. Saya butuh benchmark yang dapat dipertahankan tentang bagaimana grup makanan dan FMCG ASEAN yang tercatat di bursa menangani pembengkakan trade-spend Q4 di atas 15 persen dan kejadian recall produk antara 2020 hingga 2025. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. Untuk tiap peer identifikasi peristiwa pemicu, program kendali trade-spend dalam 90 hari, keputusan penanganan recall, dan lintasan gross margin 12 sampai 24 bulan kemudian. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. Sertakan kutipan lengkap dengan tanggal publikasi. Yang kritikal, minta Researcher peer-review tiap klaim terhadap publikasi aslinya, tandai klaim yang tidak dapat diverifikasi independen, dan sajikan sebagai tabel perbandingan terstruktur dengan kolom Peer, Pemicu, Program 90-Hari, Penanganan Recall, Hasil Margin, Kutipan. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'},
        {'instr':'Buka `m365.cloud.microsoft/chat` > Agents > **Researcher** > pilih **Model Council**. Tempel prompt — Researcher menggelar laporan parallel GPT dan Claude, lalu cover letter sintesa menyorot kesepakatan dan perbedaan.', 'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. Zava Foods Indonesia beroperasi di 4 pasar ASEAN dengan regulator (BPOM, KKM, SFA, FDA Filipina) semuanya waspada. Berikut yang saya butuhkan dari Anda secara persis. Identifikasi 3 strategi paling defensible untuk grup FMCG yang menghadapi pembengkakan trade-spend dan tekanan recall produk secara bersamaan. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. Gunakan Researcher dengan Model Council aktif — gelar laporan paralel dari GPT dan Claude atas rasionalisasi trade-spend, pemangkasan portfolio SKU, komunikasi recall, dan restrukturisasi hedge CPO. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. Sorot perbedaan pendapat, rangkum posisi mayoritas, tandai pandangan minoritas, dan sajikan tabel perbandingan dengan kolom Strategi, Putusan Council, Pandangan Minoritas, Preseden ASEAN, dan Risiko Implementasi untuk rencana 90 hari yang dipimpin Direktur Keuangan. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'}
      ],
      persona=['Mod Admin','Mod Admin'],
      personaID=['Mod Admin','Mod Admin']),

      tool(T_ANALYST, M365_LIC, M365_ACCT, [
        {'instr':'Open `m365.cloud.microsoft/chat` > Agents > **Analyst**. Upload `/FMCG_01_Trade_Spend_Tracker.xlsx`. Paste the prompt below.', 'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. We are MYR 78 million over budget on trade-spend; the Group CFO presents to the Board in 5 days. Here is exactly what I need from you. Quantify and visualise the Q4 FY2025 trade-spend overrun. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. Use the uploaded /FMCG_01_Trade_Spend_Tracker.xlsx — cross-reference the Channel Spend, SKU Promo Activity AND Sell-Through tabs. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. Calculate absolute and percentage variance vs budget by channel (modern trade, general trade, e-commerce, HoReCa) and by category (noodles, dairy, beverages, snacks, edible-oils). Build (1) a horizontal bar chart of trade-spend variance ranked worst to best, and (2) a 100% stacked column showing each category contribution to the gap. Flag overrun worse than 25% as Red, 10–25% as Amber, under 10% as Green. Output a RAG dashboard with both charts embedded and one recommended corrective lever per Red row. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'},
        {'instr':'Open `m365.cloud.microsoft/chat` > Agents > **Analyst**. Upload `/FMCG_02_SKU_Margin_Tracker.xlsx` AND `/FMCG_04_Edible_Oil_Hedge_Book.xlsx`. Paste the prompt below.', 'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. Edible-oil costs jumped 18% in Q4. Here is exactly what I need from you. Identify which SKUs have lost the most gross-margin in Q4 FY2025 and how much of that is CPO-driven. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. From /FMCG_02_SKU_Margin_Tracker.xlsx pull Q3 vs Q4 GM by SKU; from /FMCG_04_Edible_Oil_Hedge_Book.xlsx pull hedge coverage and realised vs spot CPO prices. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. Build a margin-bridge waterfall (Q3 GM → Volume → Mix → Trade-spend → CPO Cost → FX → Q4 GM) with the 10 worst-impacted SKUs labelled. Output a RAG dashboard with the waterfall, a hedge-coverage donut chart, and a one-paragraph CFO note on whether to extend the hedge book through FY2026 H1. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'}
      ], DESC_ANALYST,
      promptsID=[
        {'instr':'Buka `m365.cloud.microsoft/chat` > Agents > **Analyst**. Unggah `/FMCG_01_Trade_Spend_Tracker.xlsx`. Tempel prompt.', 'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. Kami over budget Rp 280 miliar pada trade-spend; Direktur Keuangan Grup mempresentasikan ke Direksi dalam 5 hari. Berikut yang saya butuhkan dari Anda secara persis. Kuantifikasi dan visualisasikan pembengkakan trade-spend Q4 FY2025. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. Gunakan /FMCG_01_Trade_Spend_Tracker.xlsx — analisis silang antar tab Channel Spend, SKU Promo Activity DAN Sell-Through. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. Hitung selisih absolut dan persentase vs anggaran per channel (modern trade, general trade, e-commerce, HoReCa) dan per kategori (mie, dairy, minuman, snack, edible-oil). Bangun (1) bar chart horizontal selisih trade-spend diurutkan dari terburuk ke terbaik, dan (2) stacked column 100% kontribusi tiap kategori. Tandai pembengkakan >25% Merah, 10–25% Kuning, <10% Hijau. Hasilkan dashboard RAG dengan kedua chart tertanam dan satu rekomendasi perbaikan per baris Merah. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'},
        {'instr':'Buka `m365.cloud.microsoft/chat` > Agents > **Analyst**. Unggah `/FMCG_02_SKU_Margin_Tracker.xlsx` DAN `/FMCG_04_Edible_Oil_Hedge_Book.xlsx`. Tempel prompt.', 'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. Biaya edible-oil melonjak 18% di Q4. Berikut yang saya butuhkan dari Anda secara persis. Identifikasi SKU mana yang kehilangan margin kotor terbanyak di Q4 FY2025 dan berapa banyak yang didorong CPO. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. Dari /FMCG_02_SKU_Margin_Tracker.xlsx tarik GM per SKU Q3 vs Q4; dari /FMCG_04_Edible_Oil_Hedge_Book.xlsx tarik cover hedge dan harga CPO realisasi vs spot. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. Bangun margin-bridge waterfall (GM Q3 → Volume → Mix → Trade-spend → Biaya CPO → Valas → GM Q4) dengan 10 SKU paling terdampak diberi label. Sajikan dashboard RAG dengan waterfall, donut chart cover hedge, dan paragraf catatan Direktur Keuangan apakah memperpanjang hedge book hingga H1 FY2026. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'}
      ],
      persona=['Hadar Caspit','Hadar Caspit'],
      personaID=['Hadar Caspit','Hadar Caspit']),

      tool(T_EXCEL, M365_LIC, M365_ACCT, [
        {'instr':'Open `/FMCG_01_Trade_Spend_Tracker.xlsx` in Excel for the Web. Open the **Copilot pane**. Paste the prompt below.', 'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. The CFO presents in 5 days. Here is exactly what I need from you. Build a Board-ready trade-spend dashboard. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. Pull from the Channel Spend, SKU Promo Activity AND Sell-Through tabs. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. On a new sheet "Board Trade-Spend Dashboard": (1) KPI tiles for Total Variance MYR M, Variance %, Worst Channel, Worst Category; (2) horizontal bar of variance by channel; (3) clustered column of monthly run-rate; (4) sparklines per channel; (5) RAG conditional formatting >25% red, 10–25% amber, <10% green. Insert all charts on the new sheet, do not modify the source tabs. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'}
      ], '',
      promptsID=[
        {'instr':'Buka `/FMCG_01_Trade_Spend_Tracker.xlsx` di Excel for the Web. Buka **Copilot pane**. Tempel prompt.', 'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. Direktur Keuangan presentasi dalam 5 hari. Berikut yang saya butuhkan dari Anda secara persis. Bangun dashboard trade-spend siap-Direksi. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. Tarik dari tab Channel Spend, SKU Promo Activity DAN Sell-Through. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. Pada sheet baru "Dashboard Trade-Spend Direksi": (1) KPI tile Total Selisih Rp Miliar, Selisih %, Channel Terburuk, Kategori Terburuk; (2) bar horizontal selisih per channel; (3) clustered column run-rate bulanan; (4) sparkline per channel; (5) format kondisional RAG >25% merah, 10–25% kuning, <10% hijau. Sisipkan semua chart pada sheet baru, jangan modifikasi tab sumber. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'}
      ],
      persona=['Hadar Caspit'],
      personaID=['Hadar Caspit']),

      tool(T_WORD, M365_LIC, M365_ACCT, [
        {'instr':'Open a new blank Word doc in Word for the Web. Open the **Copilot pane**. Reference `/FMCG_03_Recall_Remediation_Programme.docx` and `/FMCG_05_FY2026_Promo_Guardrails.docx` using `/`. Paste the prompt below.', 'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. Board meets in 5 days. Here is exactly what I need from you. Draft the 4-page Board paper "Q4 FY2025 Trade-Spend & Recall Update — Board Discussion Pack". Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. /FMCG_03_Recall_Remediation_Programme.docx and /FMCG_05_FY2026_Promo_Guardrails.docx, plus the trade-spend variance numbers I will paste. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. Sections — (1) Executive summary in 5 bullets, (2) Trade-spend overrun bridge in plain language, (3) Salmonella recall status across MY/SG/ID, (4) Gross-margin recovery levers and their MYR impact, (5) FY2026 promo guardrail policy proposal, (6) Decisions requested from the Board. Tone: precise, Board-ready, no speculative language. Cite the source files at the end of every section. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'}
      ], DESC_WORD,
      promptsID=[
        {'instr':'Buka dokumen Word baru kosong di Word for the Web. Buka **Copilot pane**. Referensikan `/FMCG_03_Recall_Remediation_Programme.docx` dan `/FMCG_05_FY2026_Promo_Guardrails.docx` menggunakan `/`. Tempel prompt.', 'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. Direksi rapat dalam 5 hari. Berikut yang saya butuhkan dari Anda secara persis. Susun paper Direksi 4 halaman "Update Trade-Spend & Recall Q4 FY2025 — Pack Diskusi Direksi". Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. /FMCG_03_Recall_Remediation_Programme.docx dan /FMCG_05_FY2026_Promo_Guardrails.docx, plus angka selisih trade-spend yang akan saya tempelkan. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. Bagian — (1) Ringkasan eksekutif 5 bullet, (2) Bridge pembengkakan trade-spend bahasa sederhana, (3) Status recall Salmonella di MY/SG/ID, (4) Lever pemulihan gross margin dan dampak Rp Miliar, (5) Proposal policy guardrail promo FY2026, (6) Keputusan yang diminta dari Direksi. Nada: presisi, siap-Direksi, tidak spekulatif. Kutip file sumber di akhir tiap bagian. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'}
      ],
      persona=['Hadar Caspit'],
      personaID=['Hadar Caspit']),

      tool(T_PPT, M365_LIC, M365_ACCT, [
        {'instr':'Open a new PowerPoint deck in PowerPoint for the Web. Open the **Copilot pane**. Paste the prompt below.', 'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. The Board sees this on Friday. Here is exactly what I need from you. Build a 10-slide investor-grade deck on the Q4 FY2025 trade-spend overrun and recall response. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. Reference my Word draft `/Q4_Board_Paper.docx` and the trade-spend dashboard numbers I will paste. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. Cover slide; situation in 1 slide; trade-spend bridge waterfall (2 slides); recall status by market (1 slide); margin levers (2 slides); FY2026 promo guardrails (1 slide); decisions requested (1 slide); appendix (1 slide). Use Zava brand colours #F59E0B and #0F1C3F, 18pt minimum body text, 1 chart per slide, no walls of text. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'}
      ], DESC_PPT,
      promptsID=[
        {'instr':'Buka deck PowerPoint baru di PowerPoint for the Web. Buka **Copilot pane**. Tempel prompt.', 'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. Direksi melihat ini Jumat. Berikut yang saya butuhkan dari Anda secara persis. Bangun deck 10 slide kelas investor tentang pembengkakan trade-spend dan respons recall Q4 FY2025. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. Referensikan draf Word saya `/Paper_Direksi_Q4.docx` dan angka dashboard trade-spend yang akan saya tempel. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. Slide cover; situasi 1 slide; waterfall bridge trade-spend (2 slide); status recall per pasar (1 slide); lever margin (2 slide); guardrail promo FY2026 (1 slide); keputusan yang diminta (1 slide); appendix (1 slide). Gunakan warna brand Zava #F59E0B dan #0F1C3F, font tubuh minimum 18pt, 1 chart per slide, hindari dinding teks. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'}
      ],
      persona=['Sasha Ouellet'],
      personaID=['Sasha Ouellet']),

      tool(T_OUTLOOK, M365_LIC, M365_ACCT, [
        {'instr':'Open Outlook on the Web. Open the email thread titled "Q4 FY2025 Trade-Spend Variance — Group CFO follow-up". Click the **Copilot icon** in the message ribbon. Paste the prompt below.', 'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. Q4 trade-spend overran budget by MYR 78 million; Board on Friday. Here is exactly what I need from you. Draft a single, calm, board-ready email to the 6 Divisional MDs and the Group Trade-Marketing Director. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. Summarise the latest figures from the email thread above and the attached dashboard. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. Subject line, 4 short paragraphs covering (1) the headline number, (2) the 3 corrective levers I expect each Division to commit to in 48 hours, (3) the FY2026 promo guardrails coming, (4) the meeting time on Wednesday for alignment. End with a one-line note that the Board will see this on Friday. Tone: firm but collegial, not blaming. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'}
      ], DESC_OUTLOOK,
      promptsID=[
        {'instr':'Buka Outlook on the Web. Buka thread email "Selisih Trade-Spend Q4 FY2025 — tindak lanjut Direktur Keuangan". Klik **ikon Copilot** di ribbon pesan. Tempel prompt.', 'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. Trade-spend Q4 over budget Rp 280 miliar; Direksi Jumat. Berikut yang saya butuhkan dari Anda secara persis. Susun satu email tenang dan siap-Direksi kepada 6 Direktur Divisi dan Direktur Trade-Marketing Grup. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. Ringkas angka terbaru dari thread di atas dan dashboard terlampir. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. Baris subjek, 4 paragraf pendek mencakup (1) angka headline, (2) 3 lever perbaikan yang saya harapkan tiap Divisi komit dalam 48 jam, (3) guardrail promo FY2026 yang akan datang, (4) waktu rapat Rabu untuk penyelarasan. Akhiri dengan satu baris bahwa Direksi melihat ini Jumat. Nada: tegas tapi kolegial, tidak menyalahkan. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'}
      ],
      persona=['Hadar Caspit'],
      personaID=['Hadar Caspit']),

      tool(T_TEAMS, M365_LIC, M365_ACCT, 
        [
          {'instr':"**(1) In Teams**, open **Calendar** → click the past meeting **\"New Software Implementation\"**. On the Recap page, walk the audience through the **AI Notes** (auto-summary), the **Custom summary** (Copilot's per-attendee view), and the **Audio recap** (chapter markers with speaker timings). **(2) In Word for the Web**, open a **new blank document**. Type a minutes template at the top — five empty headings: Date and Attendees · Agenda Items · Decisions Taken · Action Items · Risks and Open Questions. **(3) Click the Copilot icon** in the Word ribbon and paste the prompt below — Copilot in Word will reference the meeting recap by name with `/` and fill the template.", 'prompt':"Create meeting minutes for the Teams meeting /New Software Implementation. Use the empty template already on this page and fill each heading from the meeting recap. Sections: (1) Date and Attendees; (2) Agenda Items; (3) Decisions Taken; (4) Action Items with Owner and Due Date; (5) Risks and Open Questions. Quote attendee statements verbatim where the wording matters. Tag any decision that is on the critical path as Critical Path. Save the file as Minutes_New_Software_Implementation.docx in OneDrive."},
          {'instr':'**(1) In Teams**, open **Calendar** → click the past meeting **"Marketing Campaign Performance Review"**. On the Recap page, walk through the **AI Notes**, the **Custom summary**, and the **Audio recap** chapters. **(2) In Word for the Web**, open a **new blank document**. Type a campaign-review minutes template at the top — six empty headings: Date and Attendees · Campaign KPIs Reviewed · Decisions Taken · Action Items · Budget Reallocations · Next Review Date. **(3) Click the Copilot icon** in the Word ribbon and paste the prompt below.', 'prompt':"Create meeting minutes for the Teams meeting /Marketing Campaign Performance Review. Use the empty campaign-review template already on this page. Sections: (1) Date and Attendees; (2) Campaign KPIs Reviewed; (3) Decisions Taken; (4) Action Items with Owner and Due Date; (5) Budget Reallocations Approved; (6) Next Review Date. Quote attendee statements verbatim where the wording matters. Highlight any KPI that missed target by more than 10% in amber. Save the file as Minutes_Marketing_Campaign_Review.docx in OneDrive."},
          {'instr':'**(1) In Teams**, open **Calendar** → click the past meeting **"Negotiating Marketing Contract"**. On the Recap page, walk through the **AI Notes**, the **Custom summary**, and the **Audio recap**. **(2) In Word for the Web**, open a **new blank document**. Type a vendor-negotiation minutes template at the top — seven empty headings: Vendor and Owner · Commercial Terms Discussed · Concessions Offered · Concessions Accepted · Open Items · Approval Thresholds · Next Steps. **(3) Click the Copilot icon** in the Word ribbon and paste the prompt below — then forward the result to Procurement, Legal, and the Group CFO.', 'prompt':"Create meeting minutes for the Teams meeting /Negotiating Marketing Contract. Use the empty vendor-negotiation template already on this page. Sections: (1) Vendor and Owner; (2) Commercial Terms Discussed; (3) Concessions Offered; (4) Concessions Accepted; (5) Open Items; (6) Approval Thresholds (CFO / Board); (7) Next Steps with Owner and Due Date. Highlight any term requiring CFO sign-off in amber and any term requiring Board sign-off in red. Save the file as Minutes_Marketing_Contract_Negotiation.docx in OneDrive and email the link to Procurement, Legal, and the Group CFO."}
        ], DESC_TEAMS,
        promptsID=[
          {'instr':'**(1) Di Teams**, buka **Calendar** → klik rapat **"New Software Implementation"**. Di halaman Recap, jelaskan ke peserta tentang **AI Notes** (ringkasan otomatis), **Custom summary** (tampilan per-peserta dari Copilot), dan **Audio recap** (penanda bab dengan timing pembicara). **(2) Di Word for the Web**, buka **dokumen kosong baru**. Ketik kerangka notulen di bagian atas — lima heading kosong: Tanggal dan Peserta · Agenda · Keputusan · Action Items · Risiko dan Pertanyaan Terbuka. **(3) Klik ikon Copilot** di ribbon Word lalu tempelkan prompt di bawah — Copilot in Word akan merujuk recap rapat dengan `/` dan mengisi template.', 'prompt':"Susun notulen rapat untuk rapat Teams /New Software Implementation. Gunakan template kosong yang sudah ada di halaman ini dan isi tiap heading dari recap rapat. Bagian: (1) Tanggal dan Peserta; (2) Agenda; (3) Keputusan; (4) Action Items dengan Owner dan Due Date; (5) Risiko dan Pertanyaan Terbuka. Kutip pernyataan peserta apa adanya bila kata-katanya penting. Tandai keputusan di jalur kritis sebagai Critical Path. Simpan file sebagai Minutes_New_Software_Implementation.docx di OneDrive."},
          {'instr':'**(1) Di Teams**, buka **Calendar** → klik rapat **"Marketing Campaign Performance Review"**. Di halaman Recap, jelaskan **AI Notes**, **Custom summary**, dan **Audio recap**. **(2) Di Word for the Web**, buka dokumen kosong baru. Ketik kerangka notulen tinjauan kampanye — enam heading kosong: Tanggal dan Peserta · KPI Kampanye yang Dikaji · Keputusan · Action Items · Realokasi Anggaran · Jadwal Tinjauan Berikutnya. **(3) Klik ikon Copilot** di ribbon Word lalu tempelkan prompt di bawah.', 'prompt':"Susun notulen rapat untuk rapat Teams /Marketing Campaign Performance Review. Gunakan template kosong tinjauan kampanye yang sudah ada. Bagian: (1) Tanggal dan Peserta; (2) KPI Kampanye yang Dikaji; (3) Keputusan; (4) Action Items dengan Owner dan Due Date; (5) Realokasi Anggaran yang Disetujui; (6) Jadwal Tinjauan Berikutnya. Kutip pernyataan peserta apa adanya. Tandai KPI yang meleset >10% dengan amber. Simpan sebagai Minutes_Marketing_Campaign_Review.docx di OneDrive."},
          {'instr':'**(1) Di Teams**, buka **Calendar** → klik rapat **"Negotiating Marketing Contract"**. Di halaman Recap, jelaskan **AI Notes**, **Custom summary**, dan **Audio recap**. **(2) Di Word for the Web**, buka dokumen kosong baru. Ketik kerangka notulen negosiasi vendor — tujuh heading kosong: Vendor dan Owner · Term Komersial · Konsesi yang Ditawarkan · Konsesi yang Diterima · Item Terbuka · Threshold Persetujuan · Langkah Berikutnya. **(3) Klik ikon Copilot** di ribbon Word lalu tempelkan prompt di bawah — kemudian teruskan hasilnya ke Procurement, Legal, dan Direktur Keuangan Grup.', 'prompt':"Susun notulen rapat untuk rapat Teams /Negotiating Marketing Contract. Gunakan template kosong negosiasi vendor yang sudah ada. Bagian: (1) Vendor dan Owner; (2) Term Komersial; (3) Konsesi yang Ditawarkan; (4) Konsesi yang Diterima; (5) Item Terbuka; (6) Threshold Persetujuan (CFO / Direksi); (7) Langkah Berikutnya dengan Owner dan Due Date. Tandai term yang memerlukan persetujuan CFO dengan amber dan persetujuan Direksi dengan merah. Simpan sebagai Minutes_Marketing_Contract_Negotiation.docx di OneDrive lalu email link-nya ke Procurement, Legal, dan Direktur Keuangan Grup."}
        ],
        promptsBM=[
          {'instr':'**(1) Di Teams**, buka **Calendar** → klik mesyuarat **"New Software Implementation"**. Pada halaman Recap, terangkan kepada hadirin tentang **AI Notes** (ringkasan automatik), **Custom summary** (paparan per-hadirin dari Copilot), dan **Audio recap** (penanda bab dengan masa pembicara). **(2) Di Word for the Web**, buka **dokumen kosong baharu**. Taip rangka minit di bahagian atas — lima tajuk kosong: Tarikh dan Hadirin · Agenda · Keputusan · Tindakan · Risiko dan Soalan Terbuka. **(3) Klik ikon Copilot** di ribbon Word dan tampal prompt di bawah — Copilot in Word akan merujuk recap mesyuarat dengan `/` dan mengisi templat.', 'prompt':"Hasilkan minit mesyuarat untuk mesyuarat Teams /New Software Implementation. Gunakan templat kosong yang sudah ada di halaman ini dan isi setiap tajuk daripada recap mesyuarat. Bahagian: (1) Tarikh dan Hadirin; (2) Agenda; (3) Keputusan; (4) Tindakan dengan Pemilik dan Tarikh; (5) Risiko dan Soalan Terbuka. Petik kenyataan hadirin sebagaimana asal di mana perkataannya penting. Tandakan sebarang keputusan di laluan kritikal sebagai Critical Path. Simpan fail sebagai Minutes_New_Software_Implementation.docx di OneDrive."},
          {'instr':'**(1) Di Teams**, buka **Calendar** → klik mesyuarat **"Marketing Campaign Performance Review"**. Pada halaman Recap, terangkan **AI Notes**, **Custom summary**, dan **Audio recap**. **(2) Di Word for the Web**, buka dokumen kosong baharu. Taip rangka minit ulasan kempen — enam tajuk kosong: Tarikh dan Hadirin · KPI Kempen yang Diulas · Keputusan · Tindakan · Pelarasan Bajet · Tarikh Ulasan Berikutnya. **(3) Klik ikon Copilot** di ribbon Word dan tampal prompt di bawah.', 'prompt':"Hasilkan minit mesyuarat untuk mesyuarat Teams /Marketing Campaign Performance Review. Gunakan templat kosong ulasan kempen yang sudah ada. Bahagian: (1) Tarikh dan Hadirin; (2) KPI Kempen yang Diulas; (3) Keputusan; (4) Tindakan dengan Pemilik dan Tarikh; (5) Pelarasan Bajet yang Diluluskan; (6) Tarikh Ulasan Berikutnya. Petik kenyataan hadirin sebagaimana asal. Tandakan KPI yang tersasar >10% dengan amber. Simpan sebagai Minutes_Marketing_Campaign_Review.docx di OneDrive."},
          {'instr':'**(1) Di Teams**, buka **Calendar** → klik mesyuarat **"Negotiating Marketing Contract"**. Pada halaman Recap, terangkan **AI Notes**, **Custom summary**, dan **Audio recap**. **(2) Di Word for the Web**, buka dokumen kosong baharu. Taip rangka minit perundingan vendor — tujuh tajuk kosong: Vendor dan Pemilik · Terma Komersial · Konsesi Ditawarkan · Konsesi Diterima · Item Terbuka · Ambang Kelulusan · Langkah Seterusnya. **(3) Klik ikon Copilot** di ribbon Word dan tampal prompt di bawah — kemudian majukan hasilnya kepada Procurement, Legal dan Pengarah Kewangan Kumpulan.', 'prompt':"Hasilkan minit mesyuarat untuk mesyuarat Teams /Negotiating Marketing Contract. Gunakan templat kosong perundingan vendor yang sudah ada. Bahagian: (1) Vendor dan Pemilik; (2) Terma Komersial; (3) Konsesi Ditawarkan; (4) Konsesi Diterima; (5) Item Terbuka; (6) Ambang Kelulusan (CFO / Lembaga); (7) Langkah Seterusnya dengan Pemilik dan Tarikh. Tandakan terma yang memerlukan kelulusan CFO dengan amber dan Lembaga dengan merah. Simpan sebagai Minutes_Marketing_Contract_Negotiation.docx di OneDrive dan e-mel pautan kepada Procurement, Legal dan Pengarah Kewangan Kumpulan."}
        ],
        persona=['Sasha Ouellet', 'Sasha Ouellet', 'Sasha Ouellet'],
        personaID=['Sasha Ouellet', 'Sasha Ouellet', 'Sasha Ouellet']
      ),

      tool(T_NOTEBOOK, M365_LIC, M365_ACCT, [
        {'instr':'All sources are loaded in the notebook (see Notebook setup above). The Instructions field is set. Type the prompt below in the notebook chat.',
         'prompt':'Synthesise across all 5 sources to produce a 10-bullet Board narrative for Friday. Cover: the MYR 78M trade-spend overrun in plain language, the worst 5 SKUs by margin loss, the recall status by market, the 3 levers we will pull in 90 days, and the FY2026 promo guardrails we will table for approval. Cite the source file (and tab/section where applicable) at the end of every bullet.'},
        {'instr':'In the same notebook, click **Quick Create** > **Audio Overview** to generate a 6-minute podcast-style summary; OR click **Quick Create** > **Page** to generate a collaborative Page the leadership team can comment on.',
         'prompt':'Quick Create: Audio Overview, 6 minutes, formal narration tone, focused on the Board narrative above. Listeners are the 6 Divisional MDs who will be on a flight on Thursday and need to walk into the Friday Board meeting prepared.'}
      ], DESC_NOTEBOOK,
      promptsID=[
        {'instr':'Semua sumber sudah dimuat di notebook (lihat setup Notebook di atas). Field Instructions sudah diset. Ketik prompt di bawah pada chat notebook.',
         'prompt':'Sintesakan dari kelima sumber untuk menghasilkan narasi Direksi 10-bullet untuk Jumat. Mencakup: pembengkakan trade-spend Rp 280 miliar dengan bahasa sederhana, 5 SKU terburuk dari sisi kehilangan margin, status recall per pasar, 3 lever yang akan kami tarik dalam 90 hari, dan guardrail promo FY2026 yang akan diajukan untuk disetujui. Kutip file sumber (dan tab/bagian bila relevan) di akhir tiap bullet.'},
        {'instr':'Pada notebook yang sama, klik **Quick Create** > **Audio Overview** untuk menghasilkan ringkasan podcast 6 menit; ATAU klik **Quick Create** > **Page** untuk menghasilkan Page kolaboratif yang bisa dikomentari tim leadership.',
         'prompt':'Quick Create: Audio Overview, 6 menit, gaya narasi formal, fokus pada narasi Direksi di atas. Pendengar adalah 6 Direktur Divisi yang akan terbang Kamis dan butuh siap hadir Rapat Direksi Jumat.'}
      ],
      persona=['Mod Admin','Mod Admin'],
      personaID=['Mod Admin','Mod Admin'],
      notebookMeta={
        'sources':['/FMCG_01_Trade_Spend_Tracker.xlsx','/FMCG_02_SKU_Margin_Tracker.xlsx','/FMCG_03_Recall_Remediation_Programme.docx','/FMCG_04_Edible_Oil_Hedge_Book.xlsx','/FMCG_05_FY2026_Promo_Guardrails.docx'],
        'instructions':'You are the Group CFO of Zava Foods Indonesia preparing a Friday Board pack. Cover trade-spend control, the active Salmonella recall in MY/SG/ID, gross-margin recovery, and FY2026 promo guardrails. Always cite the source file and tab/section. Tone: precise, Board-ready, no speculation. Convert IDR to MYR at 1 MYR = 3,580 IDR when reporting Group totals.',
        'instructionsID':'Anda adalah Direktur Keuangan Grup Zava Foods Indonesia yang menyiapkan paket Direksi Jumat. Cakup kendali trade-spend, recall Salmonella aktif di MY/SG/ID, pemulihan gross margin, dan guardrail promo FY2026. Selalu kutip file sumber dan tab/bagian. Nada: presisi, siap-Direksi, tanpa spekulasi. Konversi IDR ke MYR pada 1 MYR = 3.580 IDR saat melaporkan total Grup.'
      }),

      tool(T_COWORK, FRONTIER_LIC, M365_ACCT, [
        {'instr':'Open `m365.cloud.microsoft` > left nav > **Agents** > **Cowork**. Paste the single prompt below — Cowork delegates 5 parallel sub-tasks and reports back with one consolidated status panel. Frontier program required.',
         'prompt':'Cowork — Trade-Spend Sprint. Run these 5 tasks in parallel and report back: (1) 📝 Draft a Word doc — Q4 Trade-Spend Variance Brief, 4 pages, audience Group ExCo, sources /FMCG_01_Trade_Spend_Tracker.xlsx and /FMCG_05_FY2026_Promo_Guardrails.docx. (2) 📝 Draft a Word doc — Recall Holding Lines for BPOM/MOH/SFA, 1 page each, source /FMCG_03_Recall_Remediation_Programme.docx. (3) ✉️ Send an email to the 6 Divisional MDs and the Group Trade-Marketing Director summarising the variance and asking for 3 corrective levers each, due in 48 hours. (4) 📅 Schedule a 60-minute Group ExCo meeting tomorrow 9am MYT titled "Trade-Spend Crisis Alignment — Pre-Board". (5) 💬 Post a Teams message to the #group-exco channel with a one-line headline of the variance and a link to the dashboard. Use these named recipients consistently across the email task and the Teams meeting task — Hadar (Group CFO), Sasha (Group Chief of Staff), Daichi (Head of Investor Relations), Sonia (Head of Strategy), Will (Head of Risk) and Omar (Head of Procurement) — and adapt the precise distribution per sub-task to keep each communication focused on the right audience.'}
      ], DESC_COWORK,
      promptsID=[
        {'instr':'Buka `m365.cloud.microsoft` > nav kiri > **Agents** > **Cowork**. Tempel prompt tunggal di bawah — Cowork mendelegasikan 5 sub-tugas paralel dan melaporkan kembali dengan satu panel status terkonsolidasi. Membutuhkan program Frontier.',
         'prompt':'Cowork — Sprint Trade-Spend. Jalankan 5 tugas berikut paralel dan laporkan kembali: (1) 📝 Susun dokumen Word — Brief Selisih Trade-Spend Q4, 4 halaman, audiens Group ExCo, sumber /FMCG_01_Trade_Spend_Tracker.xlsx dan /FMCG_05_FY2026_Promo_Guardrails.docx. (2) 📝 Susun dokumen Word — Holding Line Recall untuk BPOM/KKM/SFA, 1 halaman per regulator, sumber /FMCG_03_Recall_Remediation_Programme.docx. (3) ✉️ Kirim email ke 6 Direktur Divisi dan Direktur Trade-Marketing Grup yang merangkum selisih dan meminta 3 lever perbaikan dari masing-masing dalam 48 jam. (4) 📅 Jadwalkan rapat Group ExCo 60 menit besok pukul 09:00 WIB berjudul "Penyelarasan Krisis Trade-Spend — Pre-Direksi". (5) 💬 Posting pesan Teams di channel #group-exco dengan headline satu baris selisih dan tautan ke dashboard. Use these named recipients consistently across the email task and the Teams meeting task — Hadar (Group CFO), Sasha (Group Chief of Staff), Daichi (Head of Investor Relations), Sonia (Head of Strategy), Will (Head of Risk) and Omar (Head of Procurement) — and adapt the precise distribution per sub-task to keep each communication focused on the right audience.'}
      ],
      persona=['Mod Admin'],
      personaID=['Mod Admin']),

      tool(T_WORD_AGT, ANY_LIC, ANY_ACCT, [
        {'instr':'Open `m365.cloud.microsoft/chat` → Agents tab → choose **Word Agent**. Paste the prompt below — the agent returns a fully drafted .docx saved to OneDrive, ready to share. Works with the free Copilot Chat account or an Microsoft 365 Copilot license.',
         'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. Q4 FY2025 trade-spend overran by MYR 78M, Salmonella recall active in MY/SG/ID, Board on Friday. Here is exactly what I need from you. Generate a 4-page Group CFO Trade-Spend & Recall Brief in Word. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. Reference /FMCG_01_Trade_Spend_Tracker.xlsx (Channel Spend tab) and /FMCG_03_Recall_Remediation_Programme.docx. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. Sections — Executive Summary 5 bullets, Trade-Spend Bridge plain English, Recall Status by Market, Margin Recovery Levers with MYR impact, FY2026 Promo Guardrails proposal, Decisions Requested. Tone: precise, Board-ready, no speculation. Save as CFO_TradeSpend_Recall_Brief.docx. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'}
      ], DESC_WORD_AGT,
      promptsID=[
        {'instr':'Buka `m365.cloud.microsoft/chat` → tab Agents → pilih **Word Agent**. Tempel prompt — agent mengembalikan .docx yang sudah didraf penuh dan tersimpan di OneDrive, siap dibagikan. Bekerja dengan akun Copilot Chat gratis atau lisensi Microsoft 365 Copilot.',
         'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. Trade-spend Q4 FY2025 over Rp 280 miliar, recall Salmonella aktif di MY/SG/ID, Direksi Jumat. Berikut yang saya butuhkan dari Anda secara persis. Hasilkan Brief Trade-Spend & Recall Direktur Keuangan Grup 4 halaman dalam Word. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. Referensikan /FMCG_01_Trade_Spend_Tracker.xlsx (tab Channel Spend) dan /FMCG_03_Recall_Remediation_Programme.docx. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. Bagian — Ringkasan Eksekutif 5 bullet, Bridge Trade-Spend bahasa sederhana, Status Recall per Pasar, Lever Pemulihan Margin dengan dampak Rp Miliar, Proposal Guardrail Promo FY2026, Keputusan yang Diminta. Nada: presisi, siap-Direksi, tanpa spekulasi. Simpan sebagai Brief_TradeSpend_Recall_Direktur_Keuangan.docx. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'}
      ],
      persona=['Sasha Ouellet'],
      personaID=['Sasha Ouellet']),

      tool(T_PPT_AGT, ANY_LIC, ANY_ACCT, [
        {'instr':'Open `m365.cloud.microsoft/chat` → Agents tab → choose **PowerPoint Agent**. Paste the prompt below — the agent returns a fully drafted .pptx saved to OneDrive, ready to share.',
         'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. Friday Board. Here is exactly what I need from you. Build a 10-slide Board deck on Q4 FY2025 trade-spend overrun and recall. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. Reference my Word brief /CFO_TradeSpend_Recall_Brief.docx and trade-spend dashboard /FMCG_01_Trade_Spend_Tracker.xlsx. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. Cover, Situation, Bridge waterfall (2 slides), Recall by market, Levers (2 slides), FY2026 Guardrails, Decisions, Appendix. Brand colours #F59E0B + #0F1C3F, 18pt minimum body text, 1 chart per slide. Save as Q4_TradeSpend_Recall_BoardDeck.pptx. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'}
      ], DESC_PPT_AGT,
      promptsID=[
        {'instr':'Buka `m365.cloud.microsoft/chat` → tab Agents → pilih **PowerPoint Agent**. Tempel prompt — agent mengembalikan .pptx yang sudah didraf penuh dan tersimpan di OneDrive, siap dibagikan.',
         'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. Direksi Jumat. Berikut yang saya butuhkan dari Anda secara persis. Bangun deck Direksi 10 slide tentang pembengkakan trade-spend dan recall Q4 FY2025. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. Referensikan brief Word saya /Brief_TradeSpend_Recall_Direktur_Keuangan.docx dan dashboard trade-spend /FMCG_01_Trade_Spend_Tracker.xlsx. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. Cover, Situasi, Waterfall Bridge (2 slide), Recall per Pasar, Lever (2 slide), Guardrail FY2026, Keputusan, Appendix. Warna brand #F59E0B + #0F1C3F, font tubuh minimum 18pt, 1 chart per slide. Simpan sebagai Deck_Direksi_TradeSpend_Recall_Q4.pptx. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'}
      ],
      persona=['Sasha Ouellet'],
      personaID=['Sasha Ouellet']),

      tool(T_XL_AGT, ANY_LIC, ANY_ACCT, [
        {'instr':'Open `m365.cloud.microsoft/chat` → Agents tab → choose **Excel Agent**. Paste the prompt below — the agent returns a fully built .xlsx saved to OneDrive, ready to share.',
         'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. 30-day rolling control workbook for the Group CFO. Here is exactly what I need from you. Build a Trade-Spend & Margin Tracker workbook from scratch. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. schema only — channels (modern trade, general trade, e-commerce, HoReCa), categories (noodles, dairy, beverages, snacks, edible-oils), 4 ASEAN markets. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. Sheet 1 Channel Spend (budget vs actual by month), Sheet 2 SKU Margin (top 50 SKUs Q3 vs Q4 GM), Sheet 3 Recall Cost Tracker (legal, logistics, replacement, comms), Sheet 4 Dashboard with KPI tiles + RAG conditional formatting. Save as FMCG_TradeSpend_Margin_Tracker.xlsx. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'}
      ], DESC_XL_AGT,
      promptsID=[
        {'instr':'Buka `m365.cloud.microsoft/chat` → tab Agents → pilih **Excel Agent**. Tempel prompt — agent mengembalikan .xlsx yang sudah dibangun penuh dan tersimpan di OneDrive, siap dibagikan.',
         'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. Workbook kontrol rolling 30-hari untuk Direktur Keuangan Grup. Berikut yang saya butuhkan dari Anda secara persis. Bangun workbook Tracker Trade-Spend & Margin dari nol. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. hanya skema — channel (modern trade, general trade, e-commerce, HoReCa), kategori (mie, dairy, minuman, snack, edible-oil), 4 pasar ASEAN. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. Sheet 1 Channel Spend (anggaran vs aktual per bulan), Sheet 2 SKU Margin (50 SKU teratas GM Q3 vs Q4), Sheet 3 Recall Cost Tracker (legal, logistik, replacement, komunikasi), Sheet 4 Dashboard dengan KPI tile + format kondisional RAG. Simpan sebagai Tracker_TradeSpend_Margin_FMCG.xlsx. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'}
      ],
      persona=['Hadar Caspit'],
      personaID=['Hadar Caspit']),

      tool_builder(M365_LIC, M365_ACCT,
        agents=[
        {
          'icon': '🥫',
          'label': 'Brand Velocity Coach',
          'name': 'Zava Food & FMCG — Brand & SKU Velocity Coach',
          'desc': 'Tracks Food & FMCG brand share, SKU velocity, and trade-spend ROI by channel.',
          'instructions': 'You are the Zava Food & FMCG Brand & SKU Velocity Coach. You support Brand Marketing. Monitor velocity (FMCG_01_Trade_Spend_Tracker.xlsx), trade-spend (FMCG_03_Recall_Remediation_Programme.docx), and channel mix (FMCG_05_FY2026_Promo_Guardrails.docx). Recommend trade-spend reallocation, range-edit, or campaign actions.',
          'knowledge': [
            {'file':'FMCG_01_Trade_Spend_Tracker.xlsx', 'note':'SKU velocity by channel.'},
            {'file':'FMCG_03_Recall_Remediation_Programme.docx', 'note':'Trade-spend ROI tracker.'},
            {'file':'FMCG_05_FY2026_Promo_Guardrails.docx', 'note':'Channel-mix data.'}
          ],
          'knowledgeNote': 'Test: "Which 3 brands at Food & FMCG are losing share this quarter?"',
          'queries': [
            'Top 10 SKUs by velocity drop — recommended action per SKU.',
            'Which trade-spend programmes are ROI-negative? Recommend cancel.',
            'Draft the quarterly Brand Steering Committee paper.'
          ],
        },
        {
          'icon': '🏭',
          'label': 'Plant & Supply Coach',
          'name': 'Zava Food & FMCG — Plant & Supply Coach',
          'desc': 'Optimises Food & FMCG plant OEE, raw-material yield, and supply-chain reliability.',
          'instructions': 'You are the Zava Food & FMCG Plant & Supply Coach. You support Manufacturing and Supply Chain. Monitor plant OEE (FMCG_02_SKU_Margin_Tracker.xlsx), raw-material yield, and OTIF (FMCG_04_Edible_Oil_Hedge_Book.xlsx). Recommend maintenance, recipe, or supply-base actions.',
          'knowledge': [
            {'file':'FMCG_02_SKU_Margin_Tracker.xlsx', 'note':'Plant OEE & yield.'},
            {'file':'FMCG_04_Edible_Oil_Hedge_Book.xlsx', 'note':'OTIF tracker.'}
          ],
          'knowledgeNote': 'Test: "Which 3 plants at Food & FMCG have the worst OEE drag?"',
          'queries': [
            'Top 10 plant lines by OEE drag — recommended action.',
            'Which suppliers have OTIF deterioration? Tabulate and recommend escalation.',
            'Draft the monthly Manufacturing & Supply review paper.'
          ],
        },
        {
          'icon': '🏛️',
          'label': 'JAKIM / BPOM Liaison',
          'name': 'Zava Food & FMCG — Food Regulator Liaison',
          'desc': 'Prepares MOH / JAKIM (MY) / BPOM (ID) halal, food-safety, and labelling filings for Food & FMCG.',
          'instructions': 'You are the Zava Food & FMCG Food Regulator Liaison. Prepare halal, food-safety, labelling, and recall filings grounded on the regulatory file (FMCG_05_FY2026_Promo_Guardrails.docx).',
          'knowledge': [],
          'knowledgeNote': 'Test: "Draft the response to BPOM\'s latest food-safety circular for Food & FMCG."',
          'queries': [
            "Prepare a cover letter for this quarter's halal / BPOM return.",
            'Which open recalls remain unclosed? Build closure plan.',
            "Draft the response letter to the regulator's latest notice."
          ],
        }
      ],
        agentsID=[
        {
          'icon': '🥫',
          'label': 'Brand Velocity Pelatih',
          'name': 'Zava Food & FMCG — Brand & SKU Velocity Pelatih',
          'desc': 'Memantau Food & FMCG brand share, SKU velocity, and trade-spend ROI by channel.',
          'instructions': 'Anda adalah Zava Food & FMCG Brand & SKU Velocity Pelatih. Anda mendukung Brand Marketing. Pantau velocity (FMCG_01_Trade_Spend_Tracker.xlsx), trade-spend (FMCG_03_Recall_Remediation_Programme.docx), and channel mix (FMCG_05_FY2026_Promo_Guardrails.docx). Rekomendasikan trade-spend reallocation, range-edit, or campaign actions.',
          'knowledge': [
            {'file':'FMCG_01_Trade_Spend_Tracker.xlsx', 'note':'SKU velocity by channel.'},
            {'file':'FMCG_03_Recall_Remediation_Programme.docx', 'note':'Trade-spend ROI tracker.'},
            {'file':'FMCG_05_FY2026_Promo_Guardrails.docx', 'note':'Channel-mix data.'}
          ],
          'knowledgeNote': 'Test: "Yang mana 3 brands at Food & FMCG are losing share kuartal ini?"',
          'queries': [
            '10 teratas SKUs by velocity drop — recommended tindakan per SKU.',
            'Yang mana trade-spend programmes are ROI-negative? Rekomendasikan cancel.',
            'Susun the kuartalan Brand Komite Pengarah paper.'
          ],
        },
        {
          'icon': '🏭',
          'label': 'Plant & Supply Pelatih',
          'name': 'Zava Food & FMCG — Plant & Supply Pelatih',
          'desc': 'Optimises Food & FMCG plant OEE, raw-material yield, and supply-chain reliability.',
          'instructions': 'Anda adalah Zava Food & FMCG Plant & Supply Pelatih. Anda mendukung Manufacturing and Supply Chain. Pantau plant OEE (FMCG_02_SKU_Margin_Tracker.xlsx), raw-material yield, and OTIF (FMCG_04_Edible_Oil_Hedge_Book.xlsx). Rekomendasikan maintenance, recipe, or supply-base actions.',
          'knowledge': [
            {'file':'FMCG_02_SKU_Margin_Tracker.xlsx', 'note':'Plant OEE & yield.'},
            {'file':'FMCG_04_Edible_Oil_Hedge_Book.xlsx', 'note':'OTIF tracker.'}
          ],
          'knowledgeNote': 'Test: "Yang mana 3 plants at Food & FMCG have terburuk OEE drag?"',
          'queries': [
            '10 teratas plant lines by OEE drag — recommended tindakan.',
            'Yang mana suppliers have OTIF deterioration? Tabulasikan and rekomendasikan escalation.',
            'Susun the bulanan Manufacturing & Supply review paper.'
          ],
        },
        {
          'icon': '🏛️',
          'label': 'JAKIM / BPOM Penghubung',
          'name': 'Zava Food & FMCG — Food Regulator Penghubung',
          'desc': 'Prepares MOH / JAKIM (MY) / BPOM (ID) halal, food-safety, and labelling filings for Food & FMCG.',
          'instructions': 'Anda adalah Zava Food & FMCG Food Regulator Penghubung. Prepare halal, food-safety, labelling, and recall filings grounded on the regulatory file (FMCG_05_FY2026_Promo_Guardrails.docx).',
          'knowledge': [],
          'knowledgeNote': 'Test: "Susun the response to BPOM\'s latest food-safety circular for Food & FMCG."',
          'queries': [
            "Prepare a cover letter for kuartal ini's halal / BPOM return.",
            'Yang mana open recalls remain unclosed? Bangun closure plan.',
            "Susun the response letter to the regulator's latest notice."
          ],
        }
      ],
        persona=['Mod Admin', 'Mod Admin', 'Mod Admin'],
        personaID=['Mod Admin', 'Mod Admin', 'Mod Admin']
      ),
    ],
    companyID='Zava Foods Indonesia',
    taglineID='Trade-spend Q4 FY2025 over Rp 280 M; recall SKU di 2 pasar — paket Direksi 5 hari.',
    scenarioID='Zava Foods Indonesia adalah grup makanan dan FMCG ASEAN yang tercatat di bursa dengan 14 pabrik di Indonesia, Malaysia, Singapura, dan Filipina, memproduksi mi instan, dairy, minuman, baked goods, snack, dan edible-oils untuk lebih dari 250 SKU. Trade-spend Q4 FY2025 melebihi anggaran Rp 280 miliar (+22%) terutama karena agresivitas promo modern-trade dan sell-through general-trade yang lemah. Indikasi Salmonella pada satu SKU bakery memicu recall pencegahan di Malaysia dan Singapura — BPOM Indonesia, KKM Malaysia, dan SFA Singapura semuanya membuka kasus. Biaya edible-oil melonjak 18% dari volatilitas CPO, menekan margin pada 4 SKU mi terlaris. Direktur Keuangan Grup butuh paket Direksi dalam 5 hari yang mencakup pengendalian trade-spend, program remediasi recall, pemulihan gross margin, dan guardrail promo FY2026. Frame customer riil: grup ini beroperasi serupa dengan Japfa Comfeed, Nippon Indosari Corpindo, Mamee-Double Decker, Spritzer, F&N Holdings, Malayan Flour Mills dan Ajinomoto Indonesia.',
    relevantDepts=['dept-finance','dept-strategy','dept-legal','dept-risk','dept-operations','dept-marketing','dept-it-digital'],
    personas=[
      {'name':'Hadar Caspit','role':'Group CFO','roleID':'Direktur Keuangan Grup','acct':'admin@ABSx62256373.onmicrosoft.com','lic':'Microsoft 365 Copilot','color':'#1E40AF'},
      {'name':'Sasha Ouellet','role':'Group Chief of Staff','roleID':'Kepala Staf Grup','acct':'SashaO@ABSx62256373.OnMicrosoft.com','lic':'Free \u2014 no Microsoft 365 Copilot license','color':'#7C3AED'},
      {'name':'Mod Admin','role':'Group Strategy Director','roleID':'Direktur Strategi Grup','acct':'admin@ABSx62256373.onmicrosoft.com','lic':'Microsoft 365 Copilot','color':'#059669'},
      {'name':'Daichi Maruyama','role':'Group QA & Regulatory Director','roleID':'Direktur QA & Regulatory Grup','acct':'admin@ABSx62256373.onmicrosoft.com','lic':'Microsoft 365 Copilot','color':'#DC2626'}
    ],
    storyboard=[
      {'ex':1,'title':'Research & Brief','titleID':'Riset & Pengarahan','minutes':18,'mode':'Show & Tell + Hands-on',
       'summary':'Frame the MYR 78M trade-spend overrun and the active recall; pull deep ASEAN peer benchmarks before the Group CFO walks into the Board on Friday.',
       'summaryID':'Bingkai pembengkakan trade-spend Rp 280 M dan recall aktif; tarik benchmark peer ASEAN mendalam sebelum Direktur Keuangan Grup masuk Rapat Direksi Jumat.',
       'tasks':[
         {'verb':'Frame the morning question and lock the day priorities','verbID':'Susun pertanyaan pagi dan kunci prioritas hari ini','toolId':T_CHAT,'mode':'Show & Tell'},
         {'verb':'Run an outside-in peer scan and pull proven plays','verbID':'Lakukan pemindaian peer dari luar dan tarik praktik terbaik','toolId':T_RESEARCHER,'mode':'Show & Tell'},
         {'verb':'Generate a board-ready brief straight from chat','verbID':'Hasilkan brief siap-Direksi langsung dari chat','toolId':T_WORD_AGT,'mode':'Hands-on'}]},
      {'ex':2,'title':'Analyse & Decide','titleID':'Analisis & Putuskan','minutes':18,'mode':'Hands-on',
       'summary':'Quantify the trade-spend variance and SKU-level margin drag; build a Board-ready dashboard.',
       'summaryID':'Kuantifikasi selisih trade-spend dan drag margin per SKU; bangun dashboard siap-Direksi.',
       'tasks':[
         {'verb':'Crunch the numbers and surface the biggest gaps','verbID':'Olah angka dan ungkap celah terbesar','toolId':T_ANALYST,'mode':'Hands-on'},
         {'verb':'Build a single-pane operating dashboard','verbID':'Bangun dashboard operasi satu-halaman','toolId':T_EXCEL,'mode':'Hands-on'},
         {'verb':'Spin up a recurring tracker workbook from chat','verbID':'Buat workbook tracker berulang dari chat','toolId':T_XL_AGT,'mode':'Hands-on'}]},
      {'ex':3,'title':'Communicate & Coordinate','titleID':'Komunikasi & Koordinasi','minutes':18,'mode':'Hands-on',
       'summary':'Brief the 6 Divisional MDs, capture the Trade-Spend Crisis Review meeting, and assemble the Board deck.',
       'summaryID':'Brief 6 Direktur Divisi, capture rapat Trade-Spend Crisis Review, dan rakit deck Direksi.',
       'tasks':[
         {'verb':'Draft the stakeholder alignment email','verbID':'Draf email penyelarasan stakeholder','toolId':T_OUTLOOK,'mode':'Hands-on'},
         {'verb':'Recap the meeting and turn it into minutes','verbID':'Recap rapat dan ubah ke notulen','toolId':T_TEAMS,'mode':'Hands-on'},
         {'verb':'Generate a board-ready deck from chat','verbID':'Hasilkan deck siap-Direksi dari chat','toolId':T_PPT_AGT,'mode':'Hands-on'},
         {'verb':'Delegate a 5-task parallel sprint','verbID':'Delegasikan 5-tugas paralel ke Cowork','toolId':T_COWORK,'mode':'Show & Tell'}]},
      {'ex':4,'title':'Build & Scale','titleID':'Bangun & Skala','minutes':15,'mode':'Show & Tell',
       'summary':'Wrap the trade-spend playbook into a reusable agent so the 6 Divisional MDs can self-serve.',
       'summaryID':'Bungkus playbook trade-spend ke dalam agent reusable agar 6 Direktur Divisi dapat self-service.',
       'tasks':[
         {'verb':'Pull every source into one synthesis notebook','verbID':'Tarik semua sumber ke satu notebook sintesis','toolId':T_NOTEBOOK,'mode':'Show & Tell'},
         {'verb':'Wrap the daily workflow into a reusable agent','verbID':'Bungkus alur kerja harian jadi agen yang dapat dipakai ulang','toolId':T_BUILDER,'mode':'Show & Tell'}]}
    ],
    geo='ID'
))


# Continued in subsequent edits — Industries 2-7 follow the same template.


# ╔══════════════════════════════════════════════════════════════════════╗
# ║  2.  RUBBER GLOVES MANUFACTURING                                     ║
# ╚══════════════════════════════════════════════════════════════════════╝
INDUSTRIES_10.append(ind(
    'rubber-gloves', 'sec-mfg', 'Rubber Gloves Mfg', '🧤', '#0EA5E9', '#0369A1',
    'Zava Glove Berhad',
    'US FDA Form 483 + USA forced-labour CBP withhold-release order — Bursa Malaysia query in 7 days.',
    "Zava Glove Berhad is a Bursa Malaysia-listed rubber-gloves manufacturer with 8 plants across Selangor, Negeri Sembilan and Kedah, producing 92 billion gloves annually for medical, exam and industrial markets across 195 countries. The US FDA issued a Form 483 with 9 observations on its Klang plant covering documentation, environmental monitoring and bioburden controls. US Customs and Border Protection has issued a Withhold Release Order against one production line citing forced-labour indicators in the migrant-worker recruitment chain. ESG ratings dropped 2 notches and the share price fell 14% in 5 sessions. Bursa Malaysia has issued an unusual market activity query and Securities Commission Malaysia has requested supplementary disclosure within 7 days. The Group CFO needs to coordinate FDA remediation, ILO-aligned migrant-worker remediation, ESG repair, lender covenant communication, and an Audit Committee briefing all at once. Real customer reference frame: this group operates similarly to Hartalega Holdings, Top Glove Corporation, Kossan Rubber, and Supermax.",
    ['GLOVE_01_FDA_483_Response_Tracker.xlsx','GLOVE_02_Migrant_Worker_Remediation_Plan.docx','GLOVE_03_ESG_Recovery_Roadmap.docx','GLOVE_04_Lender_Covenant_Tracker.xlsx','GLOVE_05_Bursa_Disclosure_Pack.docx'],
    [
      tool(T_CHAT, FREE_LIC, FREE_ACCT, [
        {'instr':'', 'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. 9 FDA observations at Klang plant, USA forced-labour finding on one line, ESG -2 notches, share -14%, Bursa query in 7 days. Here is exactly what I need from you. Frame the FDA Form 483 + CBP Withhold Release Order in plain English for the Group CEO. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. my notes from the 6am crisis call. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. 1-page note with sections — Headline, What FDA Said, What CBP Said, Bursa & SC Position, Top 5 Questions the Board Will Ask, 3 Decisions the CEO Must Take in 48 Hours. Tone: calm, precise, no industry jargon. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'},
        {'instr':'', 'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. Audience is wires + sell-side + retail investors. Here is exactly what I need from you. 90-second verbal opening for the Bursa-mandated press conference in 4 days. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. the published facts only (Form 483, CBP WRO, ESG downgrade). When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. Open with acknowledgement, explain remediation underway, signal credible 90-day FDA + ILO-aligned migrant-worker recovery, end with 3 commitments. Avoid speculative language and avoid blaming labour agents. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'},
        {'instr':'', 'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. 7-day Bursa clock. Here is exactly what I need from you. Build the stakeholder communication map. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. known stakeholders. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. RAG table — Red same-day (FDA, CBP, Bursa, SC, top-3 customers, US distributor), Amber 24h (ILO, top-5 lenders, ESG raters MSCI + Sustainalytics, migrant-worker hotline), Green monitor (sell-side, retail). Columns: Audience, Channel, Owner, Message Theme, Timing, Risk if Mishandled. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'}
      ], DESC_CHAT,
      promptsID=[
        {'instr':'', 'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. 9 observasi FDA di pabrik Klang, temuan kerja paksa CBP pada satu line, ESG -2 notch, saham -14%, query Bursa dalam 7 hari. Berikut yang saya butuhkan dari Anda secara persis. Bingkai FDA Form 483 + CBP Withhold Release Order dalam bahasa sederhana untuk Direktur Utama Grup. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. catatan saya dari rapat krisis pukul 06:00. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. nota 1 halaman dengan bagian — Headline, Apa Kata FDA, Apa Kata CBP, Posisi Bursa & SC, 5 Pertanyaan Direksi, 3 Keputusan Direktur Utama dalam 48 Jam. Nada: tenang, presisi, hindari jargon industri. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'},
        {'instr':'', 'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. Audiens kantor berita + sell-side + investor ritel. Berikut yang saya butuhkan dari Anda secara persis. Pembukaan lisan 90 detik untuk press conference yang diwajibkan Bursa dalam 4 hari. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. hanya fakta yang sudah dipublikasikan (Form 483, CBP WRO, ESG downgrade). Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. Buka dengan pengakuan, jelaskan remediasi yang berjalan, beri sinyal pemulihan FDA + selaras ILO 90-hari yang kredibel, akhiri dengan 3 komitmen. Hindari bahasa spekulatif dan hindari menyalahkan agen tenaga kerja. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'},
        {'instr':'', 'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. clock Bursa 7-hari. Berikut yang saya butuhkan dari Anda secara persis. Bangun peta komunikasi pemangku kepentingan. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. pemangku kepentingan yang dikenal. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. tabel RAG — Merah hari ini juga (FDA, CBP, Bursa, SC, 3 customer teratas, distributor AS), Kuning 24 jam (ILO, 5 lender teratas, ESG rater MSCI + Sustainalytics, hotline pekerja migran), Hijau pantau (sell-side, ritel). Kolom: Audiens, Channel, Pemilik, Tema Pesan, Timing, Risiko bila Keliru. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'}
      ],
      persona=['Sasha Ouellet','Mod Admin','Hadar Caspit'],
      personaID=['Sasha Ouellet','Mod Admin','Hadar Caspit']),

      tool(T_RESEARCHER, M365_LIC, M365_ACCT, [
        {'instr':'Open `m365.cloud.microsoft/chat` > Agents > **Researcher** > **Critique Mode**. Paste the prompt below.',
         'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. Zava Glove Berhad must respond to Bursa Malaysia in 7 days. Here is exactly what I need from you. Benchmark how listed Malaysian glove makers (Hartalega, Top Glove, Kossan, Supermax) and global peers (Ansell, Halyard) have handled simultaneous FDA Form 483 + USA CBP Withhold Release Order events between 2018 and 2025. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. peer disclosures, Bursa announcements, FDA EIRs, CBP WRO databases. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. For each peer, identify trigger, FDA timeline to closure, ILO-aligned migrant-worker programme adopted, share-price recovery 12 months later. Critique each source. Cite all with publication date. Output as comparison table: Peer, Trigger, FDA Closure Days, Worker Programme, Recovery, Citation. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'},
        {'instr':'Open `m365.cloud.microsoft/chat` > Agents > **Researcher** > **Model Council**. Paste the prompt below.',
         'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. Zava Glove must protect FDA market access AND ILO-aligned worker remediation AND ESG rating concurrently. Here is exactly what I need from you. 3 most defensible 90-day playbooks for a Malaysian glove maker hit by FDA + CBP simultaneously. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. Researcher Model Council — convene parallel reports from GPT and Claude. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. Surface dissent, mark majority and minority views. Comparison table: Playbook, Council Verdict, Dissenting View, ASEAN Precedent, Implementation Risk. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'}
      ], DESC_RESEARCHER,
      promptsID=[
        {'instr':'Buka `m365.cloud.microsoft/chat` > Agents > **Researcher** > **Critique Mode**. Tempel prompt.',
         'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. Zava Glove Berhad harus respons ke Bursa Malaysia dalam 7 hari. Berikut yang saya butuhkan dari Anda secara persis. Benchmark bagaimana produsen sarung tangan Malaysia tercatat (Hartalega, Top Glove, Kossan, Supermax) dan peer global (Ansell, Halyard) menangani peristiwa FDA Form 483 + CBP WRO AS bersamaan antara 2018 hingga 2025. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. pengungkapan peer, pengumuman Bursa, FDA EIR, database CBP WRO. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. Untuk tiap peer identifikasi pemicu, timeline penutupan FDA, program selaras-ILO untuk pekerja migran, pemulihan harga saham 12 bulan kemudian. Kritisi tiap sumber. Cantumkan kutipan lengkap dengan tanggal publikasi. Hasilkan tabel perbandingan: Peer, Pemicu, Hari Penutupan FDA, Program Pekerja, Pemulihan, Kutipan. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'},
        {'instr':'Buka `m365.cloud.microsoft/chat` > Agents > **Researcher** > **Model Council**. Tempel prompt.',
         'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. Zava Glove harus melindungi akses pasar FDA DAN remediasi pekerja selaras-ILO DAN rating ESG sekaligus. Berikut yang saya butuhkan dari Anda secara persis. 3 strategi 90-hari paling defensible untuk produsen sarung tangan Malaysia yang terkena FDA + CBP bersamaan. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. Model Council — gelar laporan paralel dari GPT dan Claude. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. Sorot perbedaan pendapat, tandai pandangan mayoritas dan minoritas. Tabel perbandingan: Strategi, Putusan Council, Pandangan Minoritas, Preseden ASEAN, Risiko Implementasi. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'}
      ],
      persona=['Mod Admin','Mod Admin'],
      personaID=['Mod Admin','Mod Admin']),

      tool(T_ANALYST, M365_LIC, M365_ACCT, [
        {'instr':'Open `m365.cloud.microsoft/chat` > Agents > **Analyst**. Upload `/GLOVE_01_FDA_483_Response_Tracker.xlsx` AND `/GLOVE_04_Lender_Covenant_Tracker.xlsx`. Paste the prompt below.',
         'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. 9 FDA observations open, 18 lenders watching covenants. Here is exactly what I need from you. Quantify open vs closed FDA observations and lender covenant headroom. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. the 2 uploaded files. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. (1) RAG bar chart of open FDA observations by closure-readiness; (2) waterfall of MYR EBITDA impact from FDA delay + CBP WRO + worker remediation costs; (3) covenant headroom tracker by lender, flag headroom <10% as Red. Output a Board-ready RAG dashboard. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'}
      ], DESC_ANALYST,
      promptsID=[
        {'instr':'Buka `m365.cloud.microsoft/chat` > Agents > **Analyst**. Unggah `/GLOVE_01_FDA_483_Response_Tracker.xlsx` DAN `/GLOVE_04_Lender_Covenant_Tracker.xlsx`. Tempel prompt.',
         'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. 9 observasi FDA terbuka, 18 lender memantau covenant. Berikut yang saya butuhkan dari Anda secara persis. Kuantifikasi observasi FDA terbuka vs tertutup dan headroom covenant lender. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. 2 file yang diunggah. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. (1) Bar chart RAG observasi FDA terbuka berdasarkan kesiapan penutupan; (2) waterfall dampak EBITDA RM dari penundaan FDA + CBP WRO + biaya remediasi pekerja; (3) tracker headroom covenant per lender, tandai headroom <10% Merah. Hasilkan dashboard RAG siap-Direksi. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'}
      ],
      persona=['Hadar Caspit'],
      personaID=['Hadar Caspit']),

      tool(T_EXCEL, M365_LIC, M365_ACCT, [
        {'instr':'Open `/GLOVE_01_FDA_483_Response_Tracker.xlsx` in Excel for the Web. Open the **Copilot pane**. Paste the prompt below.',
         'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. Audit Committee meets in 7 days. Here is exactly what I need from you. Build a single Audit-Committee-ready dashboard sheet. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. combine FDA Observations, Remediation Plan, AND Resource Plan tabs. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. New sheet "AC Dashboard" with KPI tiles (open observations, on-track, delayed, average days in remediation), bar chart of observations by closure week, sparkline column. RAG conditional formatting. Do not modify source tabs. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'}
      ], '',
      promptsID=[
        {'instr':'Buka `/GLOVE_01_FDA_483_Response_Tracker.xlsx` di Excel for the Web. Buka **Copilot pane**. Tempel prompt.',
         'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. Komite Audit rapat dalam 7 hari. Berikut yang saya butuhkan dari Anda secara persis. Bangun satu sheet dashboard siap-Komite Audit. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. gabungkan tab FDA Observations, Remediation Plan, DAN Resource Plan. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. Sheet baru "AC Dashboard" dengan KPI tile (observasi terbuka, on-track, terlambat, rata-rata hari remediasi), bar chart observasi per minggu penutupan, kolom sparkline. Format kondisional RAG. Jangan modifikasi tab sumber. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'}
      ],
      persona=['Hadar Caspit'],
      personaID=['Hadar Caspit']),

      tool(T_WORD, M365_LIC, M365_ACCT, [
        {'instr':'Open a new blank Word doc in Word for the Web. Open the **Copilot pane**. Reference `/GLOVE_02_Migrant_Worker_Remediation_Plan.docx` and `/GLOVE_05_Bursa_Disclosure_Pack.docx` using `/`. Paste the prompt below.',
         'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. 7-day clock. Here is exactly what I need from you. Draft the Bursa Malaysia supplementary disclosure (4 pages). Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. the 2 referenced docs + my notes. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. Sections — Material Facts, FDA Form 483 Status, CBP WRO Status, ILO-Aligned Worker Remediation, Financial Impact Range, Forward-Looking Statements with explicit risk language. Tone: factual, regulator-grade, no speculation. Cite source files at the end of each section. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'}
      ], DESC_WORD,
      promptsID=[
        {'instr':'Buka dokumen Word baru kosong di Word for the Web. Buka **Copilot pane**. Referensikan `/GLOVE_02_Migrant_Worker_Remediation_Plan.docx` dan `/GLOVE_05_Bursa_Disclosure_Pack.docx` menggunakan `/`. Tempel prompt.',
         'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. clock 7 hari. Berikut yang saya butuhkan dari Anda secara persis. Susun pengungkapan tambahan Bursa Malaysia (4 halaman). Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. 2 dokumen yang direferensikan + catatan saya. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. Bagian — Fakta Material, Status FDA Form 483, Status CBP WRO, Remediasi Pekerja Selaras-ILO, Rentang Dampak Finansial, Pernyataan Forward-Looking dengan bahasa risiko eksplisit. Nada: faktual, regulator-grade, tanpa spekulasi. Kutip file sumber di akhir tiap bagian. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'}
      ],
      persona=['Hadar Caspit'],
      personaID=['Hadar Caspit']),

      tool(T_PPT, M365_LIC, M365_ACCT, [
        {'instr':'Open a new PowerPoint deck in PowerPoint for the Web. Open the **Copilot pane**. Paste the prompt below.',
         'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. AC in 7 days. Here is exactly what I need from you. 8-slide Audit Committee deck on FDA + CBP joint response. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. my Bursa disclosure draft and dashboard. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. Cover; Situation; FDA Status (1 slide, RAG); CBP Status (1 slide); 90-Day Recovery Plan (2 slides); Financial Impact; Decisions Requested. Brand colours #0EA5E9 + #0F1C3F, 1 chart per slide. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'}
      ], DESC_PPT,
      promptsID=[
        {'instr':'Buka deck PowerPoint baru di PowerPoint for the Web. Buka **Copilot pane**. Tempel prompt.',
         'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. KA dalam 7 hari. Berikut yang saya butuhkan dari Anda secara persis. Deck 8 slide Komite Audit tentang respons gabungan FDA + CBP. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. draf pengungkapan Bursa dan dashboard saya. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. Cover; Situasi; Status FDA (1 slide, RAG); Status CBP (1 slide); Rencana Pemulihan 90-Hari (2 slide); Dampak Finansial; Keputusan yang Diminta. Warna brand #0EA5E9 + #0F1C3F, 1 chart per slide. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'}
      ],
      persona=['Sasha Ouellet'],
      personaID=['Sasha Ouellet']),

      tool(T_OUTLOOK, M365_LIC, M365_ACCT, [
        {'instr':'Open Outlook on the Web. Open the email thread "FDA 483 + CBP — Group CFO follow-up". Click the **Copilot icon**. Paste the prompt below.',
         'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. FDA + CBP active. Here is exactly what I need from you. Draft a single email to the 8 plant GMs and the Group HSE Director. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. the email thread above and the remediation plan. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. Subject line, 4 short paragraphs covering — situation, the 3 actions each plant must complete in 72 hours, the worker-remediation programme launch, the AC date. Tone: firm, supportive, accountable. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'}
      ], DESC_OUTLOOK,
      promptsID=[
        {'instr':'Buka Outlook on the Web. Buka thread email "FDA 483 + CBP — tindak lanjut Direktur Keuangan Grup". Klik **ikon Copilot**. Tempel prompt.',
         'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. FDA + CBP aktif. Berikut yang saya butuhkan dari Anda secara persis. Susun satu email ke 8 GM pabrik dan Direktur HSE Grup. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. thread di atas dan rencana remediasi. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. Baris subjek, 4 paragraf pendek — situasi, 3 aksi per pabrik dalam 72 jam, peluncuran program remediasi pekerja, tanggal KA. Nada: tegas, suportif, akuntabel. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'}
      ],
      persona=['Hadar Caspit'],
      personaID=['Hadar Caspit']),

      tool(T_TEAMS, M365_LIC, M365_ACCT, 
        [
          {'instr':"**(1) In Teams**, open **Calendar** → click the past meeting **\"New Software Implementation\"**. On the Recap page, walk the audience through the **AI Notes** (auto-summary), the **Custom summary** (Copilot's per-attendee view), and the **Audio recap** (chapter markers with speaker timings). **(2) In Word for the Web**, open a **new blank document**. Type a minutes template at the top — five empty headings: Date and Attendees · Agenda Items · Decisions Taken · Action Items · Risks and Open Questions. **(3) Click the Copilot icon** in the Word ribbon and paste the prompt below — Copilot in Word will reference the meeting recap by name with `/` and fill the template.", 'prompt':"Create meeting minutes for the Teams meeting /New Software Implementation. Use the empty template already on this page and fill each heading from the meeting recap. Sections: (1) Date and Attendees; (2) Agenda Items; (3) Decisions Taken; (4) Action Items with Owner and Due Date; (5) Risks and Open Questions. Quote attendee statements verbatim where the wording matters. Tag any decision that is on the critical path as Critical Path. Save the file as Minutes_New_Software_Implementation.docx in OneDrive."},
          {'instr':'**(1) In Teams**, open **Calendar** → click the past meeting **"Marketing Campaign Performance Review"**. On the Recap page, walk through the **AI Notes**, the **Custom summary**, and the **Audio recap** chapters. **(2) In Word for the Web**, open a **new blank document**. Type a campaign-review minutes template at the top — six empty headings: Date and Attendees · Campaign KPIs Reviewed · Decisions Taken · Action Items · Budget Reallocations · Next Review Date. **(3) Click the Copilot icon** in the Word ribbon and paste the prompt below.', 'prompt':"Create meeting minutes for the Teams meeting /Marketing Campaign Performance Review. Use the empty campaign-review template already on this page. Sections: (1) Date and Attendees; (2) Campaign KPIs Reviewed; (3) Decisions Taken; (4) Action Items with Owner and Due Date; (5) Budget Reallocations Approved; (6) Next Review Date. Quote attendee statements verbatim where the wording matters. Highlight any KPI that missed target by more than 10% in amber. Save the file as Minutes_Marketing_Campaign_Review.docx in OneDrive."},
          {'instr':'**(1) In Teams**, open **Calendar** → click the past meeting **"Negotiating Marketing Contract"**. On the Recap page, walk through the **AI Notes**, the **Custom summary**, and the **Audio recap**. **(2) In Word for the Web**, open a **new blank document**. Type a vendor-negotiation minutes template at the top — seven empty headings: Vendor and Owner · Commercial Terms Discussed · Concessions Offered · Concessions Accepted · Open Items · Approval Thresholds · Next Steps. **(3) Click the Copilot icon** in the Word ribbon and paste the prompt below — then forward the result to Procurement, Legal, and the Group CFO.', 'prompt':"Create meeting minutes for the Teams meeting /Negotiating Marketing Contract. Use the empty vendor-negotiation template already on this page. Sections: (1) Vendor and Owner; (2) Commercial Terms Discussed; (3) Concessions Offered; (4) Concessions Accepted; (5) Open Items; (6) Approval Thresholds (CFO / Board); (7) Next Steps with Owner and Due Date. Highlight any term requiring CFO sign-off in amber and any term requiring Board sign-off in red. Save the file as Minutes_Marketing_Contract_Negotiation.docx in OneDrive and email the link to Procurement, Legal, and the Group CFO."}
        ], DESC_TEAMS,
        promptsID=[
          {'instr':'**(1) Di Teams**, buka **Calendar** → klik rapat **"New Software Implementation"**. Di halaman Recap, jelaskan ke peserta tentang **AI Notes** (ringkasan otomatis), **Custom summary** (tampilan per-peserta dari Copilot), dan **Audio recap** (penanda bab dengan timing pembicara). **(2) Di Word for the Web**, buka **dokumen kosong baru**. Ketik kerangka notulen di bagian atas — lima heading kosong: Tanggal dan Peserta · Agenda · Keputusan · Action Items · Risiko dan Pertanyaan Terbuka. **(3) Klik ikon Copilot** di ribbon Word lalu tempelkan prompt di bawah — Copilot in Word akan merujuk recap rapat dengan `/` dan mengisi template.', 'prompt':"Susun notulen rapat untuk rapat Teams /New Software Implementation. Gunakan template kosong yang sudah ada di halaman ini dan isi tiap heading dari recap rapat. Bagian: (1) Tanggal dan Peserta; (2) Agenda; (3) Keputusan; (4) Action Items dengan Owner dan Due Date; (5) Risiko dan Pertanyaan Terbuka. Kutip pernyataan peserta apa adanya bila kata-katanya penting. Tandai keputusan di jalur kritis sebagai Critical Path. Simpan file sebagai Minutes_New_Software_Implementation.docx di OneDrive."},
          {'instr':'**(1) Di Teams**, buka **Calendar** → klik rapat **"Marketing Campaign Performance Review"**. Di halaman Recap, jelaskan **AI Notes**, **Custom summary**, dan **Audio recap**. **(2) Di Word for the Web**, buka dokumen kosong baru. Ketik kerangka notulen tinjauan kampanye — enam heading kosong: Tanggal dan Peserta · KPI Kampanye yang Dikaji · Keputusan · Action Items · Realokasi Anggaran · Jadwal Tinjauan Berikutnya. **(3) Klik ikon Copilot** di ribbon Word lalu tempelkan prompt di bawah.', 'prompt':"Susun notulen rapat untuk rapat Teams /Marketing Campaign Performance Review. Gunakan template kosong tinjauan kampanye yang sudah ada. Bagian: (1) Tanggal dan Peserta; (2) KPI Kampanye yang Dikaji; (3) Keputusan; (4) Action Items dengan Owner dan Due Date; (5) Realokasi Anggaran yang Disetujui; (6) Jadwal Tinjauan Berikutnya. Kutip pernyataan peserta apa adanya. Tandai KPI yang meleset >10% dengan amber. Simpan sebagai Minutes_Marketing_Campaign_Review.docx di OneDrive."},
          {'instr':'**(1) Di Teams**, buka **Calendar** → klik rapat **"Negotiating Marketing Contract"**. Di halaman Recap, jelaskan **AI Notes**, **Custom summary**, dan **Audio recap**. **(2) Di Word for the Web**, buka dokumen kosong baru. Ketik kerangka notulen negosiasi vendor — tujuh heading kosong: Vendor dan Owner · Term Komersial · Konsesi yang Ditawarkan · Konsesi yang Diterima · Item Terbuka · Threshold Persetujuan · Langkah Berikutnya. **(3) Klik ikon Copilot** di ribbon Word lalu tempelkan prompt di bawah — kemudian teruskan hasilnya ke Procurement, Legal, dan Direktur Keuangan Grup.', 'prompt':"Susun notulen rapat untuk rapat Teams /Negotiating Marketing Contract. Gunakan template kosong negosiasi vendor yang sudah ada. Bagian: (1) Vendor dan Owner; (2) Term Komersial; (3) Konsesi yang Ditawarkan; (4) Konsesi yang Diterima; (5) Item Terbuka; (6) Threshold Persetujuan (CFO / Direksi); (7) Langkah Berikutnya dengan Owner dan Due Date. Tandai term yang memerlukan persetujuan CFO dengan amber dan persetujuan Direksi dengan merah. Simpan sebagai Minutes_Marketing_Contract_Negotiation.docx di OneDrive lalu email link-nya ke Procurement, Legal, dan Direktur Keuangan Grup."}
        ],
        promptsBM=[
          {'instr':'**(1) Di Teams**, buka **Calendar** → klik mesyuarat **"New Software Implementation"**. Pada halaman Recap, terangkan kepada hadirin tentang **AI Notes** (ringkasan automatik), **Custom summary** (paparan per-hadirin dari Copilot), dan **Audio recap** (penanda bab dengan masa pembicara). **(2) Di Word for the Web**, buka **dokumen kosong baharu**. Taip rangka minit di bahagian atas — lima tajuk kosong: Tarikh dan Hadirin · Agenda · Keputusan · Tindakan · Risiko dan Soalan Terbuka. **(3) Klik ikon Copilot** di ribbon Word dan tampal prompt di bawah — Copilot in Word akan merujuk recap mesyuarat dengan `/` dan mengisi templat.', 'prompt':"Hasilkan minit mesyuarat untuk mesyuarat Teams /New Software Implementation. Gunakan templat kosong yang sudah ada di halaman ini dan isi setiap tajuk daripada recap mesyuarat. Bahagian: (1) Tarikh dan Hadirin; (2) Agenda; (3) Keputusan; (4) Tindakan dengan Pemilik dan Tarikh; (5) Risiko dan Soalan Terbuka. Petik kenyataan hadirin sebagaimana asal di mana perkataannya penting. Tandakan sebarang keputusan di laluan kritikal sebagai Critical Path. Simpan fail sebagai Minutes_New_Software_Implementation.docx di OneDrive."},
          {'instr':'**(1) Di Teams**, buka **Calendar** → klik mesyuarat **"Marketing Campaign Performance Review"**. Pada halaman Recap, terangkan **AI Notes**, **Custom summary**, dan **Audio recap**. **(2) Di Word for the Web**, buka dokumen kosong baharu. Taip rangka minit ulasan kempen — enam tajuk kosong: Tarikh dan Hadirin · KPI Kempen yang Diulas · Keputusan · Tindakan · Pelarasan Bajet · Tarikh Ulasan Berikutnya. **(3) Klik ikon Copilot** di ribbon Word dan tampal prompt di bawah.', 'prompt':"Hasilkan minit mesyuarat untuk mesyuarat Teams /Marketing Campaign Performance Review. Gunakan templat kosong ulasan kempen yang sudah ada. Bahagian: (1) Tarikh dan Hadirin; (2) KPI Kempen yang Diulas; (3) Keputusan; (4) Tindakan dengan Pemilik dan Tarikh; (5) Pelarasan Bajet yang Diluluskan; (6) Tarikh Ulasan Berikutnya. Petik kenyataan hadirin sebagaimana asal. Tandakan KPI yang tersasar >10% dengan amber. Simpan sebagai Minutes_Marketing_Campaign_Review.docx di OneDrive."},
          {'instr':'**(1) Di Teams**, buka **Calendar** → klik mesyuarat **"Negotiating Marketing Contract"**. Pada halaman Recap, terangkan **AI Notes**, **Custom summary**, dan **Audio recap**. **(2) Di Word for the Web**, buka dokumen kosong baharu. Taip rangka minit perundingan vendor — tujuh tajuk kosong: Vendor dan Pemilik · Terma Komersial · Konsesi Ditawarkan · Konsesi Diterima · Item Terbuka · Ambang Kelulusan · Langkah Seterusnya. **(3) Klik ikon Copilot** di ribbon Word dan tampal prompt di bawah — kemudian majukan hasilnya kepada Procurement, Legal dan Pengarah Kewangan Kumpulan.', 'prompt':"Hasilkan minit mesyuarat untuk mesyuarat Teams /Negotiating Marketing Contract. Gunakan templat kosong perundingan vendor yang sudah ada. Bahagian: (1) Vendor dan Pemilik; (2) Terma Komersial; (3) Konsesi Ditawarkan; (4) Konsesi Diterima; (5) Item Terbuka; (6) Ambang Kelulusan (CFO / Lembaga); (7) Langkah Seterusnya dengan Pemilik dan Tarikh. Tandakan terma yang memerlukan kelulusan CFO dengan amber dan Lembaga dengan merah. Simpan sebagai Minutes_Marketing_Contract_Negotiation.docx di OneDrive dan e-mel pautan kepada Procurement, Legal dan Pengarah Kewangan Kumpulan."}
        ],
        persona=['Sasha Ouellet', 'Sasha Ouellet', 'Sasha Ouellet'],
        personaID=['Sasha Ouellet', 'Sasha Ouellet', 'Sasha Ouellet']
      ),

      tool(T_NOTEBOOK, M365_LIC, M365_ACCT, [
        {'instr':'All sources are loaded. Type the prompt below in the notebook chat.',
         'prompt':'Synthesise across all 5 sources to produce a 10-bullet Audit Committee narrative. Cover: FDA 483 status, CBP WRO status, ILO-aligned migrant-worker remediation, ESG impact, lender covenant headroom, decisions requested. Cite the source file at the end of every bullet.'},
        {'instr':'Click **Quick Create** > **Audio Overview** to generate a 6-minute briefing podcast.',
         'prompt':'Quick Create: Audio Overview, 6 minutes, formal narration tone, focused on the AC narrative above. Listeners are the 8 plant GMs preparing for tomorrow morning huddles.'}
      ], DESC_NOTEBOOK,
      promptsID=[
        {'instr':'Semua sumber sudah dimuat. Ketik prompt di bawah pada chat notebook.',
         'prompt':'Sintesakan dari kelima sumber untuk menghasilkan narasi Komite Audit 10-bullet. Mencakup: status FDA 483, status CBP WRO, remediasi pekerja migran selaras-ILO, dampak ESG, headroom covenant lender, keputusan yang diminta. Kutip file sumber di akhir tiap bullet.'},
        {'instr':'Klik **Quick Create** > **Audio Overview** untuk menghasilkan podcast briefing 6 menit.',
         'prompt':'Quick Create: Audio Overview, 6 menit, gaya narasi formal, fokus pada narasi KA di atas. Pendengar adalah 8 GM pabrik yang menyiapkan huddle pagi besok.'}
      ],
      persona=['Mod Admin','Mod Admin'],
      personaID=['Mod Admin','Mod Admin'],
      notebookMeta={
        'sources':['/GLOVE_01_FDA_483_Response_Tracker.xlsx','/GLOVE_02_Migrant_Worker_Remediation_Plan.docx','/GLOVE_03_ESG_Recovery_Roadmap.docx','/GLOVE_04_Lender_Covenant_Tracker.xlsx','/GLOVE_05_Bursa_Disclosure_Pack.docx'],
        'instructions':'You are the Group CFO of Zava Glove Berhad preparing an Audit Committee pack. Cover FDA 483 remediation, CBP WRO worker programme, ESG repair, and covenant communication. Always cite the source file and tab/section. Tone: precise, regulator-grade, no speculation. Use MYR for the Group totals.',
        'instructionsID':'Anda adalah Direktur Keuangan Grup Zava Glove Berhad yang menyiapkan paket Komite Audit. Cakup remediasi FDA 483, program pekerja CBP WRO, perbaikan ESG, dan komunikasi covenant. Selalu kutip file sumber dan tab/bagian. Nada: presisi, regulator-grade, tanpa spekulasi. Gunakan MYR untuk total Grup.'
      }),

      tool(T_COWORK, FRONTIER_LIC, M365_ACCT, [
        {'instr':'Open `m365.cloud.microsoft` > Agents > **Cowork**. Paste the single prompt below — Cowork delegates 5 parallel sub-tasks. Frontier required.',
         'prompt':'Cowork — FDA + CBP Sprint. Run these in parallel: (1) 📝 Draft Word — Bursa supplementary disclosure 4 pages, source /GLOVE_05_Bursa_Disclosure_Pack.docx. (2) 📝 Draft Word — FDA 483 line-by-line response, source /GLOVE_01_FDA_483_Response_Tracker.xlsx. (3) ✉️ Send email to 8 plant GMs and Group HSE Director with the 3 actions per plant in 72h. (4) 📅 Schedule 90-min AC Pre-Read tomorrow 8am MYT. (5) 💬 Post Teams message to #group-exco with one-line headline + dashboard link. Use these named recipients consistently across the email task and the Teams meeting task — Hadar (Group CFO), Sasha (Group Chief of Staff), Daichi (Head of Investor Relations), Sonia (Head of Strategy), Will (Head of Risk) and Omar (Head of Procurement) — and adapt the precise distribution per sub-task to keep each communication focused on the right audience.'}
      ], DESC_COWORK,
      promptsID=[
        {'instr':'Buka `m365.cloud.microsoft` > Agents > **Cowork**. Tempel prompt tunggal — Cowork mendelegasikan 5 sub-tugas paralel. Frontier diperlukan.',
         'prompt':'Cowork — Sprint FDA + CBP. Jalankan paralel: (1) 📝 Susun Word — pengungkapan tambahan Bursa 4 halaman, sumber /GLOVE_05_Bursa_Disclosure_Pack.docx. (2) 📝 Susun Word — respons baris demi baris FDA 483, sumber /GLOVE_01_FDA_483_Response_Tracker.xlsx. (3) ✉️ Kirim email ke 8 GM pabrik dan Direktur HSE Grup dengan 3 aksi per pabrik dalam 72 jam. (4) 📅 Jadwalkan AC Pre-Read 90 menit besok 08:00 WIB. (5) 💬 Posting pesan Teams di #group-exco dengan headline satu baris + tautan dashboard. Use these named recipients consistently across the email task and the Teams meeting task — Hadar (Group CFO), Sasha (Group Chief of Staff), Daichi (Head of Investor Relations), Sonia (Head of Strategy), Will (Head of Risk) and Omar (Head of Procurement) — and adapt the precise distribution per sub-task to keep each communication focused on the right audience.'}
      ],
      persona=['Mod Admin'],
      personaID=['Mod Admin']),

      tool(T_WORD_AGT, ANY_LIC, ANY_ACCT, [
        {'instr':'Open `m365.cloud.microsoft/chat` → Agents tab → **Word Agent**. Paste the prompt below — the agent returns a fully drafted .docx.',
         'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. FDA 483 + CBP WRO joint response. Here is exactly what I need from you. Generate a 4-page CFO Crisis Brief in Word. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. /GLOVE_01_FDA_483_Response_Tracker.xlsx, /GLOVE_02_Migrant_Worker_Remediation_Plan.docx. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. Sections — Executive Summary 5 bullets; FDA 483 status; CBP WRO worker programme; ESG repair; Lender covenant communication; Decisions requested. Tone: precise, regulator-grade. Save as CFO_FDA_CBP_Crisis_Brief.docx. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'}
      ], DESC_WORD_AGT,
      promptsID=[
        {'instr':'Buka `m365.cloud.microsoft/chat` → tab Agents → **Word Agent**. Tempel prompt — agent mengembalikan .docx yang sudah didraf penuh.',
         'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. respons gabungan FDA 483 + CBP WRO. Berikut yang saya butuhkan dari Anda secara persis. Hasilkan Brief Krisis Direktur Keuangan 4 halaman dalam Word. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. /GLOVE_01_FDA_483_Response_Tracker.xlsx, /GLOVE_02_Migrant_Worker_Remediation_Plan.docx. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. Bagian — Ringkasan Eksekutif 5 bullet; status FDA 483; program pekerja CBP WRO; perbaikan ESG; komunikasi covenant lender; Keputusan yang diminta. Nada: presisi, regulator-grade. Simpan sebagai Brief_Krisis_FDA_CBP_Direktur_Keuangan.docx. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'}
      ],
      persona=['Sasha Ouellet'],
      personaID=['Sasha Ouellet']),

      tool(T_PPT_AGT, ANY_LIC, ANY_ACCT, [
        {'instr':'Open `m365.cloud.microsoft/chat` → Agents tab → **PowerPoint Agent**. Paste the prompt below.',
         'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. AC in 7 days. Here is exactly what I need from you. 8-slide Audit Committee deck on the FDA + CBP joint response. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. /CFO_FDA_CBP_Crisis_Brief.docx and /GLOVE_01_FDA_483_Response_Tracker.xlsx. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. Cover; Situation; FDA RAG; CBP RAG; 90-Day Plan (2); Financial Impact; Decisions. Brand #0EA5E9 + #0F1C3F, 1 chart/slide. Save as FDA_CBP_AC_Deck.pptx. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'}
      ], DESC_PPT_AGT,
      promptsID=[
        {'instr':'Buka `m365.cloud.microsoft/chat` → tab Agents → **PowerPoint Agent**. Tempel prompt.',
         'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. KA dalam 7 hari. Berikut yang saya butuhkan dari Anda secara persis. Deck 8 slide Komite Audit tentang respons gabungan FDA + CBP. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. /Brief_Krisis_FDA_CBP_Direktur_Keuangan.docx dan /GLOVE_01_FDA_483_Response_Tracker.xlsx. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. Cover; Situasi; RAG FDA; RAG CBP; Rencana 90-Hari (2); Dampak Finansial; Keputusan. Brand #0EA5E9 + #0F1C3F, 1 chart/slide. Simpan sebagai Deck_KA_FDA_CBP.pptx. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'}
      ],
      persona=['Sasha Ouellet'],
      personaID=['Sasha Ouellet']),

      tool(T_XL_AGT, ANY_LIC, ANY_ACCT, [
        {'instr':'Open `m365.cloud.microsoft/chat` → Agents tab → **Excel Agent**. Paste the prompt below.',
         'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. 90-day operating tracker for the Group COO. Here is exactly what I need from you. Build an FDA + CBP joint-response control tracker workbook. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. schema only — 9 FDA observations, 8 plants, ILO worker indicators. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. Sheet 1 FDA Observations log, Sheet 2 CBP Worker Programme milestones, Sheet 3 Cost Tracker, Sheet 4 Dashboard with KPI tiles + RAG conditional formatting. Save as Glove_FDA_CBP_Tracker.xlsx. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'}
      ], DESC_XL_AGT,
      promptsID=[
        {'instr':'Buka `m365.cloud.microsoft/chat` → tab Agents → **Excel Agent**. Tempel prompt.',
         'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. tracker operasi 90-hari untuk Direktur Operasional Grup. Berikut yang saya butuhkan dari Anda secara persis. Bangun workbook tracker respons gabungan FDA + CBP. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. hanya skema — 9 observasi FDA, 8 pabrik, indikator pekerja ILO. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. Sheet 1 Log Observasi FDA, Sheet 2 Milestone Program Pekerja CBP, Sheet 3 Tracker Biaya, Sheet 4 Dashboard dengan KPI tile + format kondisional RAG. Simpan sebagai Tracker_Glove_FDA_CBP.xlsx. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'}
      ],
      persona=['Hadar Caspit'],
      personaID=['Hadar Caspit']),

      tool_builder(M365_LIC, M365_ACCT,
        agents=[
        {
          'icon': '🧤',
          'label': 'Glove Plant Yield',
          'name': 'Zava Rubber Gloves — Plant Yield & ASP Coach',
          'desc': 'Tracks Rubber Gloves Mfg dipping-line OEE, latex-recipe yield, and ASP movements across export markets.',
          'instructions': 'You are the Zava Rubber Gloves Mfg Plant Yield & ASP Coach. You support the Plant and Commercial Directors. Monitor dipping-line OEE (GLOVE_01_FDA_483_Response_Tracker.xlsx), recipe yields, and ASP by market (GLOVE_03_ESG_Recovery_Roadmap.docx). Tabulate by line and product. Recommend dipping-line, recipe, or pricing actions.',
          'knowledge': [
            {'file':'GLOVE_01_FDA_483_Response_Tracker.xlsx', 'note':'Plant OEE & yield.'},
            {'file':'GLOVE_03_ESG_Recovery_Roadmap.docx', 'note':'ASP by region and grade.'},
            {'file':'GLOVE_05_Bursa_Disclosure_Pack.docx', 'note':'Customer order book.'}
          ],
          'knowledgeNote': 'Test: "Which lines at Rubber Gloves Mfg have the worst recipe-yield this week?"',
          'queries': [
            'Top 5 lines by yield drag — recommended recipe or maintenance action.',
            'Which export markets are showing ASP recovery? Tabulate region, % uplift, recommended pricing.',
            'Draft the monthly Plant & Commercial review.'
          ],
        },
        {
          'icon': '⛑️',
          'label': 'OSH & ESG Coach',
          'name': 'Zava Rubber Gloves — OSH & ESG Coach',
          'desc': 'Tracks Rubber Gloves Mfg OSH incidents, water/waste compliance, and migrant-labour audit findings.',
          'instructions': 'You are the Zava Rubber Gloves Mfg OSH & ESG Coach. You support the HSE Director and Sustainability Lead. Monitor incident logs (GLOVE_02_Migrant_Worker_Remediation_Plan.docx), water/waste compliance (GLOVE_04_Lender_Covenant_Tracker.xlsx), and migrant-labour audits. Tabulate findings, root cause, and CAPA. Refuse any pricing question.',
          'knowledge': [
            {'file':'GLOVE_02_Migrant_Worker_Remediation_Plan.docx', 'note':'OSH incident logs.'},
            {'file':'GLOVE_04_Lender_Covenant_Tracker.xlsx', 'note':'ESG audit findings.'}
          ],
          'knowledgeNote': 'Test: "Which OSH incidents at Rubber Gloves Mfg require board-level disclosure?"',
          'queries': [
            'Top OSH-incident drivers — root cause, recommended CAPA.',
            'Which migrant-labour-audit findings remain open? Build closure plan.',
            'Draft the quarterly ESG & OSH Steering Committee paper.'
          ],
        },
        {
          'icon': '🏛️',
          'label': 'KKM / FDA Liaison',
          'name': 'Zava Rubber Gloves — Medical-Device Regulator Liaison',
          'desc': 'Prepares MDA (MY) / Kemkes (ID) and US FDA medical-device filings for Rubber Gloves Mfg.',
          'instructions': 'You are the Zava Rubber Gloves Mfg Medical-Device Regulator Liaison. You support Regulatory Affairs. Prepare MDA / Kemkes / US FDA submissions, recall filings, and post-market surveillance grounded on the regulatory file (GLOVE_05_Bursa_Disclosure_Pack.docx) and the policy handbook (GLOVE_05_Bursa_Disclosure_Pack.docx).',
          'knowledge': [
            {'file':'GLOVE_05_Bursa_Disclosure_Pack.docx', 'note':'Regulatory submissions archive.'}
          ],
          'knowledgeNote': 'Test: "Draft the response to FDA\'s latest 510(k) deficiency letter for Rubber Gloves Mfg."',
          'queries': [
            "Prepare a cover letter for this quarter's post-market surveillance report.",
            'Which open recalls remain unclosed? Build closure plan.',
            "Draft the response letter to the regulator's latest 510(k) deficiency notice."
          ],
        }
      ],
        agentsID=[
        {
          'icon': '🧤',
          'label': 'Glove Plant Yield',
          'name': 'Zava Rubber Gloves — Plant Yield & ASP Pelatih',
          'desc': 'Memantau Rubber Gloves Mfg dipping-line OEE, latex-recipe yield, and ASP movements across export markets.',
          'instructions': 'Anda adalah Zava Rubber Gloves Mfg Plant Yield & ASP Pelatih. Anda mendukung the Plant and Commercial Directors. Pantau dipping-line OEE (GLOVE_01_FDA_483_Response_Tracker.xlsx), recipe yields, and ASP by market (GLOVE_03_ESG_Recovery_Roadmap.docx). Tabulasikan by line and product. Rekomendasikan dipping-line, recipe, or pricing actions.',
          'knowledge': [
            {'file':'GLOVE_01_FDA_483_Response_Tracker.xlsx', 'note':'Plant OEE & yield.'},
            {'file':'GLOVE_03_ESG_Recovery_Roadmap.docx', 'note':'ASP by region and grade.'},
            {'file':'GLOVE_05_Bursa_Disclosure_Pack.docx', 'note':'Customer order book.'}
          ],
          'knowledgeNote': 'Test: "Yang mana lines at Rubber Gloves Mfg have terburuk recipe-yield this week?"',
          'queries': [
            '5 teratas lines by yield drag — recommended recipe or maintenance tindakan.',
            'Yang mana export markets are showing ASP recovery? Tabulasikan region, % uplift, recommended pricing.',
            'Susun the bulanan Plant & Commercial review.'
          ],
        },
        {
          'icon': '⛑️',
          'label': 'OSH & ESG Pelatih',
          'name': 'Zava Rubber Gloves — OSH & ESG Pelatih',
          'desc': 'Memantau Rubber Gloves Mfg OSH incidents, water/waste compliance, and migrant-labour audit findings.',
          'instructions': 'Anda adalah Zava Rubber Gloves Mfg OSH & ESG Pelatih. Anda mendukung the HSE Director and Sustainability Lead. Pantau incident logs (GLOVE_02_Migrant_Worker_Remediation_Plan.docx), water/waste compliance (GLOVE_04_Lender_Covenant_Tracker.xlsx), and migrant-labour audits. Tabulasikan findings, root cause, and CAPA. Tolak any pricing question.',
          'knowledge': [
            {'file':'GLOVE_02_Migrant_Worker_Remediation_Plan.docx', 'note':'OSH incident logs.'},
            {'file':'GLOVE_04_Lender_Covenant_Tracker.xlsx', 'note':'ESG audit findings.'}
          ],
          'knowledgeNote': 'Test: "Yang mana OSH incidents at Rubber Gloves Mfg require board-level disclosure?"',
          'queries': [
            'Teratas OSH-incident drivers — root cause, recommended CAPA.',
            'Yang mana migrant-labour-audit findings remain open? Bangun closure plan.',
            'Susun the kuartalan ESG & OSH Komite Pengarah paper.'
          ],
        },
        {
          'icon': '🏛️',
          'label': 'KKM / FDA Penghubung',
          'name': 'Zava Rubber Gloves — Medical-Device Regulator Penghubung',
          'desc': 'Prepares MDA (MY) / Kemkes (ID) and US FDA medical-device filings for Rubber Gloves Mfg.',
          'instructions': 'Anda adalah Zava Rubber Gloves Mfg Medical-Device Regulator Penghubung. Anda mendukung Regulatory Affairs. Prepare MDA / Kemkes / US FDA submissions, recall filings, and post-market surveillance grounded on the regulatory file (GLOVE_05_Bursa_Disclosure_Pack.docx) and the policy handbook (GLOVE_05_Bursa_Disclosure_Pack.docx).',
          'knowledge': [
            {'file':'GLOVE_05_Bursa_Disclosure_Pack.docx', 'note':'Regulatory submissions archive.'}
          ],
          'knowledgeNote': 'Test: "Susun the response to FDA\'s latest 510(k) deficiency letter for Rubber Gloves Mfg."',
          'queries': [
            "Prepare a cover letter for kuartal ini's post-market surveillance report.",
            'Yang mana open recalls remain unclosed? Bangun closure plan.',
            "Susun the response letter to the regulator's latest 510(k) deficiency notice."
          ],
        }
      ],
        persona=['Mod Admin', 'Mod Admin', 'Mod Admin'],
        personaID=['Mod Admin', 'Mod Admin', 'Mod Admin']
      ),
    ],
    companyID='Zava Glove Berhad',
    taglineID='FDA Form 483 + CBP forced-labour WRO — query Bursa Malaysia 7 hari.',
    scenarioID='Zava Glove Berhad adalah produsen sarung tangan karet tercatat di Bursa Malaysia dengan 8 pabrik di Selangor, Negeri Sembilan, dan Kedah, memproduksi 92 miliar sarung tangan per tahun untuk pasar medis, exam, dan industri di 195 negara. US FDA menerbitkan Form 483 dengan 9 observasi pada pabrik Klang yang mencakup dokumentasi, pemantauan lingkungan, dan kendali bioburden. CBP AS menerbitkan Withhold Release Order pada satu line produksi dengan menyebut indikator kerja paksa pada rantai rekrutmen pekerja migran. Rating ESG turun 2 notch dan harga saham jatuh 14% dalam 5 sesi. Bursa Malaysia menerbitkan unusual market activity query dan SC Malaysia meminta pengungkapan tambahan dalam 7 hari. Direktur Keuangan Grup harus mengoordinasikan remediasi FDA, remediasi pekerja migran selaras-ILO, perbaikan ESG, komunikasi covenant lender, dan briefing Komite Audit semuanya sekaligus. Frame customer riil: grup ini beroperasi serupa dengan Hartalega Holdings, Top Glove Corporation, Kossan Rubber, dan Supermax.',
    relevantDepts=['dept-finance','dept-strategy','dept-legal','dept-risk','dept-operations','dept-hr','dept-esg','dept-corpsec'],
    personas=[
      {'name':'Hadar Caspit','role':'Group CFO','roleID':'Direktur Keuangan Grup','acct':'admin@ABSx62256373.onmicrosoft.com','lic':'Microsoft 365 Copilot','color':'#1E40AF'},
      {'name':'Sasha Ouellet','role':'Group Chief of Staff','roleID':'Kepala Staf Grup','acct':'SashaO@ABSx62256373.OnMicrosoft.com','lic':'Free \u2014 no Microsoft 365 Copilot license','color':'#7C3AED'},
      {'name':'Mod Admin','role':'Group Strategy Director','roleID':'Direktur Strategi Grup','acct':'admin@ABSx62256373.onmicrosoft.com','lic':'Microsoft 365 Copilot','color':'#059669'},
      {'name':'Daichi Maruyama','role':'Group HSE & Sustainability Director','roleID':'Direktur HSE & Keberlanjutan Grup','acct':'admin@ABSx62256373.onmicrosoft.com','lic':'Microsoft 365 Copilot','color':'#DC2626'}
    ],
    storyboard=[
      {'ex':1,'title':'Research & Brief','titleID':'Riset & Pengarahan','minutes':18,'mode':'Show & Tell + Hands-on',
       'summary':'Frame the FDA + CBP joint hit and pull peer playbooks before the 7-day Bursa clock starts ticking.',
       'summaryID':'Bingkai pukulan gabungan FDA + CBP dan tarik playbook peer sebelum clock Bursa 7-hari mulai berdetak.',
       'tasks':[
         {'verb':'Frame the morning question and lock the day priorities','verbID':'Susun pertanyaan pagi dan kunci prioritas hari ini','toolId':T_CHAT,'mode':'Show & Tell'},
         {'verb':'Run an outside-in peer scan and pull proven plays','verbID':'Lakukan pemindaian peer dari luar dan tarik praktik terbaik','toolId':T_RESEARCHER,'mode':'Show & Tell'},
         {'verb':'Generate a board-ready brief straight from chat','verbID':'Hasilkan brief siap-Direksi langsung dari chat','toolId':T_WORD_AGT,'mode':'Hands-on'}]},
      {'ex':2,'title':'Analyse & Decide','titleID':'Analisis & Putuskan','minutes':18,'mode':'Hands-on',
       'summary':'Quantify FDA + CBP financial impact and covenant headroom; build an AC dashboard.',
       'summaryID':'Kuantifikasi dampak finansial FDA + CBP dan headroom covenant; bangun dashboard KA.',
       'tasks':[
         {'verb':'Crunch the numbers and surface the biggest gaps','verbID':'Olah angka dan ungkap celah terbesar','toolId':T_ANALYST,'mode':'Hands-on'},
         {'verb':'Build a single-pane operating dashboard','verbID':'Bangun dashboard operasi satu-halaman','toolId':T_EXCEL,'mode':'Hands-on'},
         {'verb':'Spin up a recurring tracker workbook from chat','verbID':'Buat workbook tracker berulang dari chat','toolId':T_XL_AGT,'mode':'Hands-on'}]},
      {'ex':3,'title':'Communicate & Coordinate','titleID':'Komunikasi & Koordinasi','minutes':18,'mode':'Hands-on',
       'summary':'Brief 8 plant GMs, capture the FDA War Room recap, and assemble the AC deck and Bursa disclosure.',
       'summaryID':'Brief 8 GM pabrik, capture recap FDA War Room, dan rakit deck KA serta pengungkapan Bursa.',
       'tasks':[
         {'verb':'Draft the stakeholder alignment email','verbID':'Draf email penyelarasan stakeholder','toolId':T_OUTLOOK,'mode':'Hands-on'},
         {'verb':'Recap the meeting and turn it into minutes','verbID':'Recap rapat dan ubah ke notulen','toolId':T_TEAMS,'mode':'Hands-on'},
         {'verb':'Generate a board-ready deck from chat','verbID':'Hasilkan deck siap-Direksi dari chat','toolId':T_PPT_AGT,'mode':'Hands-on'},
         {'verb':'Delegate a 5-task parallel sprint','verbID':'Delegasikan 5-tugas paralel ke Cowork','toolId':T_COWORK,'mode':'Show & Tell'}]},
      {'ex':4,'title':'Build & Scale','titleID':'Bangun & Skala','minutes':15,'mode':'Show & Tell',
       'summary':'Wrap the FDA + CBP playbook into a reusable agent for the 8 plant GMs and the Group HSE team.',
       'summaryID':'Bungkus playbook FDA + CBP ke dalam agent reusable untuk 8 GM pabrik dan tim HSE Grup.',
       'tasks':[
         {'verb':'Pull every source into one synthesis notebook','verbID':'Tarik semua sumber ke satu notebook sintesis','toolId':T_NOTEBOOK,'mode':'Show & Tell'},
         {'verb':'Wrap the daily workflow into a reusable agent','verbID':'Bungkus alur kerja harian jadi agen yang dapat dipakai ulang','toolId':T_BUILDER,'mode':'Show & Tell'}]}
    ],
    geo='MY'
))


# (Industries 3-7 appended below in compact form)


# ╔══════════════════════════════════════════════════════════════════════╗
# ║  3.  MORTGAGE FINANCE                                        ║
# ╚══════════════════════════════════════════════════════════════════════╝
INDUSTRIES_10.append(ind(
    'mortgage-finance', 'sec-banking', 'Mortgage Finance', '🏘️', '#0F766E', '#134E4A',
    'Zava Cagamas Berhad',
    'BNM directed liquidity injection — MYR 2.4B MBS issuance window in 14 days.',
    "Zava Cagamas Berhad is the national mortgage-finance corporation supporting Malaysia's secondary mortgage market via Mortgage-Backed Securities (MBS), Sukuk Cagamas, and Purchase-with-Recourse facilities. Bank Negara Malaysia has flagged liquidity stress at 4 mid-tier banks and directed Zava Cagamas to open a MYR 2.4B MBS issuance window in 14 days. The Group CFO must coordinate origination-bank pricing, Securities Commission Malaysia approvals, RAM/MARC ratings affirmation, AAOIFI compliance for the Sukuk tranche, and an Investor Day briefing for 60 institutional investors all at once. Real customer reference frame: this group operates similarly to Cagamas Berhad and Maybank Investment Bank's mortgage-finance division.",
    ['MORT_01_MBS_Pricing_Model.xlsx', 'MORT_02_Mortgage_Pool_Stratification.xlsx', 'MORT_03_BNM_Compliance_Pack.docx', 'MORT_04_Investor_Day_Briefing.docx', 'MORT_05_Rating_Agency_Submission.docx'],
    [
      tool(T_CHAT, FREE_LIC, FREE_ACCT, [
        {'instr':'', 'prompt':"I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. Zava Cagamas Berhad is the national mortgage-finance corporation supporting Malaysia's secondary mortgage market via Mortgage-Backed Securities (MBS), Sukuk Cagamas, and Purchase-with-Recourse facilit... Here is exactly what I need from you. Frame the BNM-directed MBS issuance situation in plain English for the Group CEO. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. my notes from the morning crisis call. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. 1-page note with sections — Headline, What Happened, Stakeholder Position, Top 5 Questions the Board Will Ask, 3 Decisions the CEO Must Take in 48 Hours. Tone: calm, precise, no industry jargon. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline."},
        {'instr':'', 'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. Audience is internal ExCo + key external stakeholders. Here is exactly what I need from you. 90-second verbal opening for the Zava Cagamas Berhad stakeholder briefing. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. published facts only. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. Open with acknowledgement, explain the response programme, signal credible recovery, end with 3 commitments. Avoid speculative language. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'},
        {'instr':'', 'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. regulator clock active. Here is exactly what I need from you. Build the stakeholder communication map for the BNM-directed MBS issuance. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. known stakeholders. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. RAG table — Red same-day, Amber 24h, Green monitor. Columns: Audience, Channel, Owner, Message Theme, Timing, Risk if Mishandled. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'}
      ], DESC_CHAT,
      promptsID=[
        {'instr':'', 'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. Zava Cagamas Berhad adalah korporasi pembiayaan hipotek nasional yang mendukung pasar hipotek sekunder Malaysia via Mortgage-Backed Securities (MBS), Sukuk Cagamas, dan fasilitas Purchase-with-Recours... Berikut yang saya butuhkan dari Anda secara persis. Bingkai situasi BNM-directed MBS issuance dalam bahasa sederhana untuk Direktur Utama Grup. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. catatan saya dari rapat krisis pagi. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. nota 1 halaman dengan bagian — Headline, Apa yang Terjadi, Posisi Pemangku Kepentingan, 5 Pertanyaan Direksi, 3 Keputusan Direktur Utama dalam 48 Jam. Nada: tenang, presisi, hindari jargon industri. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'},
        {'instr':'', 'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. Audiens ExCo internal + pemangku kepentingan eksternal kunci. Berikut yang saya butuhkan dari Anda secara persis. Pembukaan lisan 90 detik untuk briefing pemangku kepentingan Zava Cagamas Berhad. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. hanya fakta yang sudah dipublikasi. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. Buka dengan pengakuan, jelaskan program respons, beri sinyal pemulihan kredibel, akhiri dengan 3 komitmen. Hindari bahasa spekulatif. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'},
        {'instr':'', 'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. clock regulator aktif. Berikut yang saya butuhkan dari Anda secara persis. Bangun peta komunikasi pemangku kepentingan untuk BNM-directed MBS issuance. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. pemangku kepentingan yang dikenal. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. tabel RAG — Merah hari ini juga, Kuning 24 jam, Hijau pantau. Kolom: Audiens, Channel, Pemilik, Tema Pesan, Timing, Risiko bila Keliru. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'}
      ],
      persona=['Sasha Ouellet','Mod Admin','Hadar Caspit'],
      personaID=['Sasha Ouellet','Mod Admin','Hadar Caspit']),

      tool(T_RESEARCHER, M365_LIC, M365_ACCT, [
        {'instr':'Open `m365.cloud.microsoft/chat` > Agents > **Researcher** > **Critique Mode**. Paste the prompt below.',
         'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. Zava Cagamas Berhad must respond to its regulator imminently. Here is exactly what I need from you. Benchmark how peers (Cagamas Berhad, Maybank IB Mortgage, RHB Investment Bank, AmInvestment Bank, CIMB Investment Bank) handled comparable BNM-directed MBS issuance events between 2020 and 2025. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. peer disclosures, regulator filings, industry press. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. For each peer, identify trigger, response timeline, programme adopted, share-price recovery 12 months later. Critique each source. Cite all with publication date. Output as comparison table. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'},
        {'instr':'Open `m365.cloud.microsoft/chat` > Agents > **Researcher** > **Model Council**. Paste the prompt below.',
         'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. must protect regulator standing AND customer trust AND financial position concurrently. Here is exactly what I need from you. 3 most defensible response playbooks for Zava Cagamas Berhad hit by BNM-directed MBS issuance. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. Researcher Model Council — convene parallel reports from GPT and Claude. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. Surface dissent, mark majority and minority views. Comparison table: Playbook, Council Verdict, Dissenting View, ASEAN Precedent, Implementation Risk. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'}
      ], DESC_RESEARCHER,
      promptsID=[
        {'instr':'Buka `m365.cloud.microsoft/chat` > Agents > **Researcher** > **Critique Mode**. Tempel prompt.',
         'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. Zava Cagamas Berhad harus respons ke regulator segera. Berikut yang saya butuhkan dari Anda secara persis. Benchmark bagaimana peer (Cagamas Berhad, Maybank IB Mortgage, RHB Investment Bank, AmInvestment Bank, CIMB Investment Bank) menangani peristiwa BNM-directed MBS issuance sebanding antara 2020 hingga 2025. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. pengungkapan peer, filing regulator, pers industri. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. Untuk tiap peer identifikasi pemicu, timeline respons, program yang diadopsi, pemulihan harga saham 12 bulan kemudian. Kritisi tiap sumber. Cantumkan kutipan lengkap dengan tanggal. Hasilkan tabel perbandingan. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'},
        {'instr':'Buka `m365.cloud.microsoft/chat` > Agents > **Researcher** > **Model Council**. Tempel prompt.',
         'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. harus melindungi posisi regulator DAN kepercayaan customer DAN posisi finansial sekaligus. Berikut yang saya butuhkan dari Anda secara persis. 3 playbook respons paling defensible untuk Zava Cagamas Berhad yang terkena BNM-directed MBS issuance. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. Model Council — gelar laporan paralel dari GPT dan Claude. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. Sorot perbedaan pendapat, tandai mayoritas dan minoritas. Tabel perbandingan: Playbook, Putusan Council, Pandangan Minoritas, Preseden ASEAN, Risiko Implementasi. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'}
      ],
      persona=['Mod Admin','Mod Admin'],
      personaID=['Mod Admin','Mod Admin']),

      tool(T_ANALYST, M365_LIC, M365_ACCT, [
        {'instr':'Open `m365.cloud.microsoft/chat` > Agents > **Analyst**. Upload /MORT_01_MBS_Pricing_Model.xlsx AND /MORT_02_Mortgage_Pool_Stratification.xlsx. Paste the prompt below.',
         'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. Group ExCo needs an evidence-based view in 48 hours. Here is exactly what I need from you. Quantify the BNM-directed MBS issuance financial and operational impact. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. the 2 uploaded files. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. (1) RAG bar chart of at-risk items by severity; (2) waterfall of MYR EBITDA impact; (3) tracker by stakeholder/segment, flag worst <10% headroom as Red. Output a Board-ready RAG dashboard. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'}
      ], DESC_ANALYST,
      promptsID=[
        {'instr':'Buka `m365.cloud.microsoft/chat` > Agents > **Analyst**. Unggah /MORT_01_MBS_Pricing_Model.xlsx DAN /MORT_02_Mortgage_Pool_Stratification.xlsx. Tempel prompt.',
         'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. ExCo Grup butuh pandangan berbasis bukti dalam 48 jam. Berikut yang saya butuhkan dari Anda secara persis. Kuantifikasi dampak finansial dan operasional dari BNM-directed MBS issuance. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. 2 file yang diunggah. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. (1) Bar chart RAG item at-risk berdasarkan severity; (2) waterfall dampak EBITDA RM; (3) tracker per stakeholder/segmen, tandai headroom terburuk <10% Merah. Hasilkan dashboard RAG siap-Direksi. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'}
      ],
      persona=['Hadar Caspit'],
      personaID=['Hadar Caspit']),

      tool(T_EXCEL, M365_LIC, M365_ACCT, [
        {'instr':'Open `/MORT_01_MBS_Pricing_Model.xlsx` in Excel for the Web. Open the **Copilot pane**. Paste the prompt below.',
         'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. Audit Committee meets in the next 14 days. Here is exactly what I need from you. Build a single Audit-Committee-ready dashboard sheet. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. combine all relevant tabs. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. New sheet "AC Dashboard" with KPI tiles, bar chart by severity, sparkline column. RAG conditional formatting. Do not modify source tabs. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'}
      ], '',
      promptsID=[
        {'instr':'Buka `/MORT_01_MBS_Pricing_Model.xlsx` di Excel for the Web. Buka **Copilot pane**. Tempel prompt.',
         'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. Komite Audit rapat dalam 14 hari ke depan. Berikut yang saya butuhkan dari Anda secara persis. Bangun satu sheet dashboard siap-Komite Audit. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. gabungkan semua tab yang relevan. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. Sheet baru "AC Dashboard" dengan KPI tile, bar chart per severity, kolom sparkline. Format kondisional RAG. Jangan modifikasi tab sumber. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'}
      ],
      persona=['Hadar Caspit'],
      personaID=['Hadar Caspit']),

      tool(T_WORD, M365_LIC, M365_ACCT, [
        {'instr':'Open a new blank Word doc in Word for the Web. Open the **Copilot pane**. Reference /MORT_03_BNM_Compliance_Pack.docx and /MORT_04_Investor_Day_Briefing.docx using `/`. Paste the prompt below.',
         'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. BNM-directed MBS issuance active. Here is exactly what I need from you. Draft the regulator-grade response brief (4 pages). Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. the referenced docs + my notes. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. Sections — Material Facts, Current Status, Programme, Financial Impact Range, Forward-Looking Statements with explicit risk language. Tone: factual, regulator-grade, no speculation. Cite source files at the end of each section. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'}
      ], DESC_WORD,
      promptsID=[
        {'instr':'Buka dokumen Word baru kosong di Word for the Web. Buka **Copilot pane**. Referensikan /MORT_03_BNM_Compliance_Pack.docx dan /MORT_04_Investor_Day_Briefing.docx menggunakan `/`. Tempel prompt.',
         'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. BNM-directed MBS issuance aktif. Berikut yang saya butuhkan dari Anda secara persis. Susun brief respons regulator-grade (4 halaman). Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. dokumen yang direferensikan + catatan saya. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. Bagian — Fakta Material, Status Saat Ini, Program, Rentang Dampak Finansial, Pernyataan Forward-Looking dengan bahasa risiko eksplisit. Nada: faktual, regulator-grade, tanpa spekulasi. Kutip file sumber di akhir tiap bagian. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'}
      ],
      persona=['Hadar Caspit'],
      personaID=['Hadar Caspit']),

      tool(T_PPT, M365_LIC, M365_ACCT, [
        {'instr':'Open a new PowerPoint deck in PowerPoint for the Web. Open the **Copilot pane**. Paste the prompt below.',
         'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. AC in 14 days. Here is exactly what I need from you. 8-slide Audit Committee deck on BNM-directed MBS issuance. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. my brief draft and dashboard. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. Cover; Situation; Status (RAG); Programme (2 slides); Financial Impact; Stakeholder Map; Decisions Requested. Brand colours #0F766E + #0F1C3F, 1 chart per slide. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'}
      ], DESC_PPT,
      promptsID=[
        {'instr':'Buka deck PowerPoint baru di PowerPoint for the Web. Buka **Copilot pane**. Tempel prompt.',
         'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. KA dalam 14 hari. Berikut yang saya butuhkan dari Anda secara persis. Deck 8 slide Komite Audit tentang BNM-directed MBS issuance. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. draf brief dan dashboard saya. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. Cover; Situasi; Status (RAG); Program (2 slide); Dampak Finansial; Peta Pemangku Kepentingan; Keputusan yang Diminta. Warna brand #0F766E + #0F1C3F, 1 chart per slide. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'}
      ],
      persona=['Sasha Ouellet'],
      personaID=['Sasha Ouellet']),

      tool(T_OUTLOOK, M365_LIC, M365_ACCT, [
        {'instr':'Open Outlook on the Web. Open the email thread "BNM-directed MBS issuance — Group CFO follow-up". Click the **Copilot icon**. Paste the prompt below.',
         'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. BNM-directed MBS issuance active. Here is exactly what I need from you. Draft a single email to the Zava Cagamas Berhad ExCo and the relevant operating heads. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. the email thread above and the response programme. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. Subject line, 4 short paragraphs covering — situation, the 3 actions each operating head must complete in 72 hours, the regulator-engagement workstream, the AC date. Tone: firm, supportive, accountable. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'}
      ], DESC_OUTLOOK,
      promptsID=[
        {'instr':'Buka Outlook on the Web. Buka thread email "BNM-directed MBS issuance — tindak lanjut Direktur Keuangan Grup". Klik **ikon Copilot**. Tempel prompt.',
         'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. BNM-directed MBS issuance aktif. Berikut yang saya butuhkan dari Anda secara persis. Susun satu email ke ExCo Zava Cagamas Berhad dan kepala operasi yang relevan. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. thread di atas dan program respons. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. Baris subjek, 4 paragraf pendek — situasi, 3 aksi per kepala operasi dalam 72 jam, workstream engagement regulator, tanggal KA. Nada: tegas, suportif, akuntabel. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'}
      ],
      persona=['Hadar Caspit'],
      personaID=['Hadar Caspit']),

      tool(T_TEAMS, M365_LIC, M365_ACCT, 
        [
          {'instr':"**(1) In Teams**, open **Calendar** → click the past meeting **\"New Software Implementation\"**. On the Recap page, walk the audience through the **AI Notes** (auto-summary), the **Custom summary** (Copilot's per-attendee view), and the **Audio recap** (chapter markers with speaker timings). **(2) In Word for the Web**, open a **new blank document**. Type a minutes template at the top — five empty headings: Date and Attendees · Agenda Items · Decisions Taken · Action Items · Risks and Open Questions. **(3) Click the Copilot icon** in the Word ribbon and paste the prompt below — Copilot in Word will reference the meeting recap by name with `/` and fill the template.", 'prompt':"Create meeting minutes for the Teams meeting /New Software Implementation. Use the empty template already on this page and fill each heading from the meeting recap. Sections: (1) Date and Attendees; (2) Agenda Items; (3) Decisions Taken; (4) Action Items with Owner and Due Date; (5) Risks and Open Questions. Quote attendee statements verbatim where the wording matters. Tag any decision that is on the critical path as Critical Path. Save the file as Minutes_New_Software_Implementation.docx in OneDrive."},
          {'instr':'**(1) In Teams**, open **Calendar** → click the past meeting **"Marketing Campaign Performance Review"**. On the Recap page, walk through the **AI Notes**, the **Custom summary**, and the **Audio recap** chapters. **(2) In Word for the Web**, open a **new blank document**. Type a campaign-review minutes template at the top — six empty headings: Date and Attendees · Campaign KPIs Reviewed · Decisions Taken · Action Items · Budget Reallocations · Next Review Date. **(3) Click the Copilot icon** in the Word ribbon and paste the prompt below.', 'prompt':"Create meeting minutes for the Teams meeting /Marketing Campaign Performance Review. Use the empty campaign-review template already on this page. Sections: (1) Date and Attendees; (2) Campaign KPIs Reviewed; (3) Decisions Taken; (4) Action Items with Owner and Due Date; (5) Budget Reallocations Approved; (6) Next Review Date. Quote attendee statements verbatim where the wording matters. Highlight any KPI that missed target by more than 10% in amber. Save the file as Minutes_Marketing_Campaign_Review.docx in OneDrive."},
          {'instr':'**(1) In Teams**, open **Calendar** → click the past meeting **"Negotiating Marketing Contract"**. On the Recap page, walk through the **AI Notes**, the **Custom summary**, and the **Audio recap**. **(2) In Word for the Web**, open a **new blank document**. Type a vendor-negotiation minutes template at the top — seven empty headings: Vendor and Owner · Commercial Terms Discussed · Concessions Offered · Concessions Accepted · Open Items · Approval Thresholds · Next Steps. **(3) Click the Copilot icon** in the Word ribbon and paste the prompt below — then forward the result to Procurement, Legal, and the Group CFO.', 'prompt':"Create meeting minutes for the Teams meeting /Negotiating Marketing Contract. Use the empty vendor-negotiation template already on this page. Sections: (1) Vendor and Owner; (2) Commercial Terms Discussed; (3) Concessions Offered; (4) Concessions Accepted; (5) Open Items; (6) Approval Thresholds (CFO / Board); (7) Next Steps with Owner and Due Date. Highlight any term requiring CFO sign-off in amber and any term requiring Board sign-off in red. Save the file as Minutes_Marketing_Contract_Negotiation.docx in OneDrive and email the link to Procurement, Legal, and the Group CFO."}
        ], DESC_TEAMS,
        promptsID=[
          {'instr':'**(1) Di Teams**, buka **Calendar** → klik rapat **"New Software Implementation"**. Di halaman Recap, jelaskan ke peserta tentang **AI Notes** (ringkasan otomatis), **Custom summary** (tampilan per-peserta dari Copilot), dan **Audio recap** (penanda bab dengan timing pembicara). **(2) Di Word for the Web**, buka **dokumen kosong baru**. Ketik kerangka notulen di bagian atas — lima heading kosong: Tanggal dan Peserta · Agenda · Keputusan · Action Items · Risiko dan Pertanyaan Terbuka. **(3) Klik ikon Copilot** di ribbon Word lalu tempelkan prompt di bawah — Copilot in Word akan merujuk recap rapat dengan `/` dan mengisi template.', 'prompt':"Susun notulen rapat untuk rapat Teams /New Software Implementation. Gunakan template kosong yang sudah ada di halaman ini dan isi tiap heading dari recap rapat. Bagian: (1) Tanggal dan Peserta; (2) Agenda; (3) Keputusan; (4) Action Items dengan Owner dan Due Date; (5) Risiko dan Pertanyaan Terbuka. Kutip pernyataan peserta apa adanya bila kata-katanya penting. Tandai keputusan di jalur kritis sebagai Critical Path. Simpan file sebagai Minutes_New_Software_Implementation.docx di OneDrive."},
          {'instr':'**(1) Di Teams**, buka **Calendar** → klik rapat **"Marketing Campaign Performance Review"**. Di halaman Recap, jelaskan **AI Notes**, **Custom summary**, dan **Audio recap**. **(2) Di Word for the Web**, buka dokumen kosong baru. Ketik kerangka notulen tinjauan kampanye — enam heading kosong: Tanggal dan Peserta · KPI Kampanye yang Dikaji · Keputusan · Action Items · Realokasi Anggaran · Jadwal Tinjauan Berikutnya. **(3) Klik ikon Copilot** di ribbon Word lalu tempelkan prompt di bawah.', 'prompt':"Susun notulen rapat untuk rapat Teams /Marketing Campaign Performance Review. Gunakan template kosong tinjauan kampanye yang sudah ada. Bagian: (1) Tanggal dan Peserta; (2) KPI Kampanye yang Dikaji; (3) Keputusan; (4) Action Items dengan Owner dan Due Date; (5) Realokasi Anggaran yang Disetujui; (6) Jadwal Tinjauan Berikutnya. Kutip pernyataan peserta apa adanya. Tandai KPI yang meleset >10% dengan amber. Simpan sebagai Minutes_Marketing_Campaign_Review.docx di OneDrive."},
          {'instr':'**(1) Di Teams**, buka **Calendar** → klik rapat **"Negotiating Marketing Contract"**. Di halaman Recap, jelaskan **AI Notes**, **Custom summary**, dan **Audio recap**. **(2) Di Word for the Web**, buka dokumen kosong baru. Ketik kerangka notulen negosiasi vendor — tujuh heading kosong: Vendor dan Owner · Term Komersial · Konsesi yang Ditawarkan · Konsesi yang Diterima · Item Terbuka · Threshold Persetujuan · Langkah Berikutnya. **(3) Klik ikon Copilot** di ribbon Word lalu tempelkan prompt di bawah — kemudian teruskan hasilnya ke Procurement, Legal, dan Direktur Keuangan Grup.', 'prompt':"Susun notulen rapat untuk rapat Teams /Negotiating Marketing Contract. Gunakan template kosong negosiasi vendor yang sudah ada. Bagian: (1) Vendor dan Owner; (2) Term Komersial; (3) Konsesi yang Ditawarkan; (4) Konsesi yang Diterima; (5) Item Terbuka; (6) Threshold Persetujuan (CFO / Direksi); (7) Langkah Berikutnya dengan Owner dan Due Date. Tandai term yang memerlukan persetujuan CFO dengan amber dan persetujuan Direksi dengan merah. Simpan sebagai Minutes_Marketing_Contract_Negotiation.docx di OneDrive lalu email link-nya ke Procurement, Legal, dan Direktur Keuangan Grup."}
        ],
        promptsBM=[
          {'instr':'**(1) Di Teams**, buka **Calendar** → klik mesyuarat **"New Software Implementation"**. Pada halaman Recap, terangkan kepada hadirin tentang **AI Notes** (ringkasan automatik), **Custom summary** (paparan per-hadirin dari Copilot), dan **Audio recap** (penanda bab dengan masa pembicara). **(2) Di Word for the Web**, buka **dokumen kosong baharu**. Taip rangka minit di bahagian atas — lima tajuk kosong: Tarikh dan Hadirin · Agenda · Keputusan · Tindakan · Risiko dan Soalan Terbuka. **(3) Klik ikon Copilot** di ribbon Word dan tampal prompt di bawah — Copilot in Word akan merujuk recap mesyuarat dengan `/` dan mengisi templat.', 'prompt':"Hasilkan minit mesyuarat untuk mesyuarat Teams /New Software Implementation. Gunakan templat kosong yang sudah ada di halaman ini dan isi setiap tajuk daripada recap mesyuarat. Bahagian: (1) Tarikh dan Hadirin; (2) Agenda; (3) Keputusan; (4) Tindakan dengan Pemilik dan Tarikh; (5) Risiko dan Soalan Terbuka. Petik kenyataan hadirin sebagaimana asal di mana perkataannya penting. Tandakan sebarang keputusan di laluan kritikal sebagai Critical Path. Simpan fail sebagai Minutes_New_Software_Implementation.docx di OneDrive."},
          {'instr':'**(1) Di Teams**, buka **Calendar** → klik mesyuarat **"Marketing Campaign Performance Review"**. Pada halaman Recap, terangkan **AI Notes**, **Custom summary**, dan **Audio recap**. **(2) Di Word for the Web**, buka dokumen kosong baharu. Taip rangka minit ulasan kempen — enam tajuk kosong: Tarikh dan Hadirin · KPI Kempen yang Diulas · Keputusan · Tindakan · Pelarasan Bajet · Tarikh Ulasan Berikutnya. **(3) Klik ikon Copilot** di ribbon Word dan tampal prompt di bawah.', 'prompt':"Hasilkan minit mesyuarat untuk mesyuarat Teams /Marketing Campaign Performance Review. Gunakan templat kosong ulasan kempen yang sudah ada. Bahagian: (1) Tarikh dan Hadirin; (2) KPI Kempen yang Diulas; (3) Keputusan; (4) Tindakan dengan Pemilik dan Tarikh; (5) Pelarasan Bajet yang Diluluskan; (6) Tarikh Ulasan Berikutnya. Petik kenyataan hadirin sebagaimana asal. Tandakan KPI yang tersasar >10% dengan amber. Simpan sebagai Minutes_Marketing_Campaign_Review.docx di OneDrive."},
          {'instr':'**(1) Di Teams**, buka **Calendar** → klik mesyuarat **"Negotiating Marketing Contract"**. Pada halaman Recap, terangkan **AI Notes**, **Custom summary**, dan **Audio recap**. **(2) Di Word for the Web**, buka dokumen kosong baharu. Taip rangka minit perundingan vendor — tujuh tajuk kosong: Vendor dan Pemilik · Terma Komersial · Konsesi Ditawarkan · Konsesi Diterima · Item Terbuka · Ambang Kelulusan · Langkah Seterusnya. **(3) Klik ikon Copilot** di ribbon Word dan tampal prompt di bawah — kemudian majukan hasilnya kepada Procurement, Legal dan Pengarah Kewangan Kumpulan.', 'prompt':"Hasilkan minit mesyuarat untuk mesyuarat Teams /Negotiating Marketing Contract. Gunakan templat kosong perundingan vendor yang sudah ada. Bahagian: (1) Vendor dan Pemilik; (2) Terma Komersial; (3) Konsesi Ditawarkan; (4) Konsesi Diterima; (5) Item Terbuka; (6) Ambang Kelulusan (CFO / Lembaga); (7) Langkah Seterusnya dengan Pemilik dan Tarikh. Tandakan terma yang memerlukan kelulusan CFO dengan amber dan Lembaga dengan merah. Simpan sebagai Minutes_Marketing_Contract_Negotiation.docx di OneDrive dan e-mel pautan kepada Procurement, Legal dan Pengarah Kewangan Kumpulan."}
        ],
        persona=['Sasha Ouellet', 'Sasha Ouellet', 'Sasha Ouellet'],
        personaID=['Sasha Ouellet', 'Sasha Ouellet', 'Sasha Ouellet']
      ),

      tool(T_NOTEBOOK, M365_LIC, M365_ACCT, [
        {'instr':'All sources are loaded. Type the prompt below in the notebook chat.',
         'prompt':'Synthesise across all sources to produce a 10-bullet Audit Committee narrative. Cover: BNM-directed MBS issuance status, programme, financial impact, stakeholder map, decisions requested. Cite the source file at the end of every bullet.'},
        {'instr':'Click **Quick Create** > **Audio Overview** to generate a 6-minute briefing podcast.',
         'prompt':'Quick Create: Audio Overview, 6 minutes, formal narration tone, focused on the AC narrative above. Listeners are the Zava Cagamas Berhad operating heads preparing for tomorrow morning huddles.'}
      ], DESC_NOTEBOOK,
      promptsID=[
        {'instr':'Semua sumber sudah dimuat. Ketik prompt di bawah pada chat notebook.',
         'prompt':'Sintesakan dari semua sumber untuk menghasilkan narasi Komite Audit 10-bullet. Cakup: status BNM-directed MBS issuance, program, dampak finansial, peta pemangku kepentingan, keputusan yang diminta. Kutip file sumber di akhir tiap bullet.'},
        {'instr':'Klik **Quick Create** > **Audio Overview** untuk menghasilkan podcast briefing 6 menit.',
         'prompt':'Quick Create: Audio Overview, 6 menit, gaya narasi formal, fokus pada narasi KA di atas. Pendengar adalah kepala operasi Zava Cagamas Berhad yang menyiapkan huddle pagi besok.'}
      ],
      persona=['Mod Admin','Mod Admin'],
      personaID=['Mod Admin','Mod Admin'],
      notebookMeta={
        'sources':['/MORT_01_MBS_Pricing_Model.xlsx', '/MORT_02_Mortgage_Pool_Stratification.xlsx', '/MORT_03_BNM_Compliance_Pack.docx', '/MORT_04_Investor_Day_Briefing.docx', '/MORT_05_Rating_Agency_Submission.docx'],
        'instructions':'You are the Group CFO of Zava Cagamas Berhad preparing an Audit Committee pack on BNM-directed MBS issuance. Always cite the source file and tab/section. Tone: precise, regulator-grade, no speculation. Use MYR for the Group totals (1 MYR ≈ 3,580 IDR).',
        'instructionsID':'Anda adalah Direktur Keuangan Grup Zava Cagamas Berhad yang menyiapkan paket Komite Audit untuk BNM-directed MBS issuance. Selalu kutip file sumber dan tab/bagian. Nada: presisi, regulator-grade, tanpa spekulasi. Gunakan MYR untuk total Grup (1 MYR ≈ 3.580 IDR).'
      }),

      tool(T_COWORK, FRONTIER_LIC, M365_ACCT, [
        {'instr':'Open `m365.cloud.microsoft` > Agents > **Cowork**. Paste the single prompt below — Cowork delegates 5 parallel sub-tasks. Frontier required.',
         'prompt':'Cowork — BNM-Directed Issuance Sprint. Run these in parallel: (1) 📝 Draft Word — regulator response brief 4 pages, source /MORT_01_MBS_Pricing_Model.xlsx, /MORT_02_Mortgage_Pool_Stratification.xlsx, /MORT_03_BNM_Compliance_Pack.docx, /MORT_04_Investor_Day_Briefing.docx, /MORT_05_Rating_Agency_Submission.docx. (2) 📝 Draft Word — internal ExCo briefing memo 2 pages, same sources. (3) ✉️ Send email to Zava Cagamas Berhad ExCo and operating heads with the 3 actions in 72h. (4) 📅 Schedule 90-min AC Pre-Read tomorrow 8am MYT. (5) 💬 Post Teams message to #group-exco with one-line headline + dashboard link. Use these named recipients consistently across the email task and the Teams meeting task — Hadar (Group CFO), Sasha (Group Chief of Staff), Daichi (Head of Investor Relations), Sonia (Head of Strategy), Will (Head of Risk) and Omar (Head of Procurement) — and adapt the precise distribution per sub-task to keep each communication focused on the right audience.'}
      ], DESC_COWORK,
      promptsID=[
        {'instr':'Buka `m365.cloud.microsoft` > Agents > **Cowork**. Tempel prompt tunggal — Cowork mendelegasikan 5 sub-tugas paralel. Frontier diperlukan.',
         'prompt':'Cowork — BNM-Directed Issuance Sprint. Jalankan paralel: (1) 📝 Susun Word — brief respons regulator 4 halaman, sumber /MORT_01_MBS_Pricing_Model.xlsx, /MORT_02_Mortgage_Pool_Stratification.xlsx, /MORT_03_BNM_Compliance_Pack.docx, /MORT_04_Investor_Day_Briefing.docx, /MORT_05_Rating_Agency_Submission.docx. (2) 📝 Susun Word — memo briefing ExCo internal 2 halaman, sumber sama. (3) ✉️ Kirim email ke ExCo Zava Cagamas Berhad dan kepala operasi dengan 3 aksi dalam 72 jam. (4) 📅 Jadwalkan AC Pre-Read 90 menit besok 08:00 WIB. (5) 💬 Posting pesan Teams di #group-exco dengan headline satu baris + tautan dashboard. Use these named recipients consistently across the email task and the Teams meeting task — Hadar (Group CFO), Sasha (Group Chief of Staff), Daichi (Head of Investor Relations), Sonia (Head of Strategy), Will (Head of Risk) and Omar (Head of Procurement) — and adapt the precise distribution per sub-task to keep each communication focused on the right audience.'}
      ],
      persona=['Mod Admin'],
      personaID=['Mod Admin']),

      tool(T_WORD_AGT, ANY_LIC, ANY_ACCT, [
        {'instr':'Open `m365.cloud.microsoft/chat` → Agents tab → **Word Agent**. Paste the prompt below — the agent returns a fully drafted .docx.',
         'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. BNM-directed MBS issuance. Here is exactly what I need from you. Generate a 4-page CFO Crisis Brief in Word. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. /MORT_01_MBS_Pricing_Model.xlsx AND /MORT_02_Mortgage_Pool_Stratification.xlsx. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. Sections — Executive Summary 5 bullets; Current Status; Programme; Financial Impact; Stakeholder Map; Decisions requested. Tone: precise, regulator-grade. Save as BNM_MBS_Issuance_Brief.docx. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'}
      ], DESC_WORD_AGT,
      promptsID=[
        {'instr':'Buka `m365.cloud.microsoft/chat` → tab Agents → **Word Agent**. Tempel prompt — agent mengembalikan .docx yang sudah didraf penuh.',
         'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. BNM-directed MBS issuance. Berikut yang saya butuhkan dari Anda secara persis. Hasilkan Brief Krisis Direktur Keuangan 4 halaman dalam Word. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. /MORT_01_MBS_Pricing_Model.xlsx DAN /MORT_02_Mortgage_Pool_Stratification.xlsx. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. Bagian — Ringkasan Eksekutif 5 bullet; Status Saat Ini; Program; Dampak Finansial; Peta Pemangku Kepentingan; Keputusan yang diminta. Nada: presisi, regulator-grade. Simpan sebagai Brief_Penerbitan_MBS_BNM.docx. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'}
      ],
      persona=['Sasha Ouellet'],
      personaID=['Sasha Ouellet']),

      tool(T_PPT_AGT, ANY_LIC, ANY_ACCT, [
        {'instr':'Open `m365.cloud.microsoft/chat` → Agents tab → **PowerPoint Agent**. Paste the prompt below.',
         'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. AC in 14 days. Here is exactly what I need from you. 8-slide Audit Committee deck on BNM-directed MBS issuance. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. /BNM_MBS_Issuance_Brief.docx and /MORT_01_MBS_Pricing_Model.xlsx. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. Cover; Situation; Status RAG; Programme (2); Financial Impact; Stakeholder Map; Decisions. Brand #0F766E + #0F1C3F, 1 chart/slide. Save as MBS_Investor_Day_Deck.pptx. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'}
      ], DESC_PPT_AGT,
      promptsID=[
        {'instr':'Buka `m365.cloud.microsoft/chat` → tab Agents → **PowerPoint Agent**. Tempel prompt.',
         'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. KA dalam 14 hari. Berikut yang saya butuhkan dari Anda secara persis. Deck 8 slide Komite Audit tentang BNM-directed MBS issuance. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. /Brief_Penerbitan_MBS_BNM.docx dan /MORT_01_MBS_Pricing_Model.xlsx. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. Cover; Situasi; Status RAG; Program (2); Dampak Finansial; Peta Pemangku Kepentingan; Keputusan. Brand #0F766E + #0F1C3F, 1 chart/slide. Simpan sebagai Deck_Investor_Day_MBS.pptx. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'}
      ],
      persona=['Sasha Ouellet'],
      personaID=['Sasha Ouellet']),

      tool(T_XL_AGT, ANY_LIC, ANY_ACCT, [
        {'instr':'Open `m365.cloud.microsoft/chat` → Agents tab → **Excel Agent**. Paste the prompt below.',
         'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. Operating tracker for the Group COO. Here is exactly what I need from you. Build a BNM-directed MBS issuance response control tracker workbook. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. schema only. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. Sheet 1 Issue Log, Sheet 2 Programme Milestones, Sheet 3 Cost Tracker, Sheet 4 Dashboard with KPI tiles + RAG conditional formatting. Save as MBS_Issuance_Tracker.xlsx. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'}
      ], DESC_XL_AGT,
      promptsID=[
        {'instr':'Buka `m365.cloud.microsoft/chat` → tab Agents → **Excel Agent**. Tempel prompt.',
         'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. tracker operasi untuk Direktur Operasional Grup. Berikut yang saya butuhkan dari Anda secara persis. Bangun workbook tracker kendali respons BNM-directed MBS issuance. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. hanya skema. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. Sheet 1 Log Isu, Sheet 2 Milestone Program, Sheet 3 Tracker Biaya, Sheet 4 Dashboard dengan KPI tile + format kondisional RAG. Simpan sebagai Tracker_Penerbitan_MBS.xlsx. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'}
      ],
      persona=['Hadar Caspit'],
      personaID=['Hadar Caspit']),

      tool_builder(M365_LIC, M365_ACCT,
        agents=[
        {
          'icon': '🏠',
          'label': 'Origination Quality',
          'name': 'Zava Mortgage Finance — Origination Quality Coach',
          'desc': 'Tracks Mortgage Finance origination quality, vintage migration, and underwriting variance.',
          'instructions': 'You are the Zava Mortgage Finance Origination Quality Coach. Monitor origination data (MORT_01_MBS_Pricing_Model.xlsx), vintage migration (MORT_03_BNM_Compliance_Pack.docx), and underwriting variance (MORT_05_Rating_Agency_Submission.docx). Recommend underwriting policy or pricing action.',
          'knowledge': [
            {'file':'MORT_01_MBS_Pricing_Model.xlsx', 'note':'Origination data.'},
            {'file':'MORT_03_BNM_Compliance_Pack.docx', 'note':'Vintage migration.'},
            {'file':'MORT_05_Rating_Agency_Submission.docx', 'note':'Underwriting variance.'}
          ],
          'knowledgeNote': 'Test: "Which 3 origination cohorts at Mortgage Finance have the worst vintage migration?"',
          'queries': [
            'Top 10 origination cohorts by deterioration — recommended action.',
            'Which underwriting variance clusters need policy review?',
            'Draft the quarterly Origination paper.'
          ],
        },
        {
          'icon': '📞',
          'label': 'Servicing & Arrears',
          'name': 'Zava Mortgage Finance — Servicing & Arrears Coach',
          'desc': 'Surfaces Mortgage Finance servicing performance, arrears clusters, and forbearance outcomes.',
          'instructions': 'You are the Zava Mortgage Finance Servicing & Arrears Coach. Monitor arrears (MORT_02_Mortgage_Pool_Stratification.xlsx) and forbearance (MORT_04_Investor_Day_Briefing.docx). Recommend collections-policy action.',
          'knowledge': [
            {'file':'MORT_02_Mortgage_Pool_Stratification.xlsx', 'note':'Arrears tracker.'},
            {'file':'MORT_04_Investor_Day_Briefing.docx', 'note':'Forbearance register.'}
          ],
          'knowledgeNote': 'Test: "Which 3 arrears clusters at Mortgage Finance have the worst roll-forward?"',
          'queries': [
            'Top 10 arrears clusters by roll-forward — recommended collections action.',
            'Which forbearance cohorts have re-default risk? Recommend triage.',
            'Draft the monthly Servicing Steering paper.'
          ],
        },
        {
          'icon': '🏛️',
          'label': 'BNM / OJK Mortgage',
          'name': 'Zava Mortgage Finance — Mortgage Regulator Liaison',
          'desc': 'Prepares BNM (MY) / OJK (ID) mortgage-quality, capital-adequacy, and securitisation filings for Mortgage Finance.',
          'instructions': 'You are the Zava Mortgage Finance Mortgage Regulator Liaison. Prepare BNM / OJK filings grounded on the regulatory file (MORT_05_Rating_Agency_Submission.docx).',
          'knowledge': [],
          'knowledgeNote': 'Test: "Draft the response to BNM\'s latest mortgage-stress-test circular for Mortgage Finance."',
          'queries': [
            'Prepare a cover letter for the next BNM / OJK return.',
            'Which securitisation tranches require regulator notification?',
            "Draft the response letter to the regulator's latest notice."
          ],
        }
      ],
        agentsID=[
        {
          'icon': '🏠',
          'label': 'Origination Quality',
          'name': 'Zava Mortgage Finance — Origination Quality Pelatih',
          'desc': 'Memantau Mortgage Finance origination quality, vintage migration, and underwriting variance.',
          'instructions': 'Anda adalah Zava Mortgage Finance Origination Quality Pelatih. Pantau origination data (MORT_01_MBS_Pricing_Model.xlsx), vintage migration (MORT_03_BNM_Compliance_Pack.docx), and underwriting variance (MORT_05_Rating_Agency_Submission.docx). Rekomendasikan underwriting policy or pricing tindakan.',
          'knowledge': [
            {'file':'MORT_01_MBS_Pricing_Model.xlsx', 'note':'Origination data.'},
            {'file':'MORT_03_BNM_Compliance_Pack.docx', 'note':'Vintage migration.'},
            {'file':'MORT_05_Rating_Agency_Submission.docx', 'note':'Underwriting variance.'}
          ],
          'knowledgeNote': 'Test: "Yang mana 3 origination cohorts at Mortgage Finance have terburuk vintage migration?"',
          'queries': [
            '10 teratas origination cohorts by deterioration — recommended tindakan.',
            'Yang mana underwriting variance clusters need policy review?',
            'Susun the kuartalan Origination paper.'
          ],
        },
        {
          'icon': '📞',
          'label': 'Servicing & Arrears',
          'name': 'Zava Mortgage Finance — Servicing & Arrears Pelatih',
          'desc': 'Menampilkan Mortgage Finance servicing performance, arrears clusters, and forbearance outcomes.',
          'instructions': 'Anda adalah Zava Mortgage Finance Servicing & Arrears Pelatih. Pantau arrears (MORT_02_Mortgage_Pool_Stratification.xlsx) and forbearance (MORT_04_Investor_Day_Briefing.docx). Rekomendasikan collections-policy tindakan.',
          'knowledge': [
            {'file':'MORT_02_Mortgage_Pool_Stratification.xlsx', 'note':'Arrears tracker.'},
            {'file':'MORT_04_Investor_Day_Briefing.docx', 'note':'Forbearance register.'}
          ],
          'knowledgeNote': 'Test: "Yang mana 3 arrears clusters at Mortgage Finance have terburuk roll-forward?"',
          'queries': [
            '10 teratas arrears clusters by roll-forward — recommended collections tindakan.',
            'Yang mana forbearance cohorts have re-default risk? Rekomendasikan triage.',
            'Susun the bulanan Servicing paper Komite Pengarah.'
          ],
        },
        {
          'icon': '🏛️',
          'label': 'BNM / OJK Mortgage',
          'name': 'Zava Mortgage Finance — Mortgage Regulator Penghubung',
          'desc': 'Prepares BNM (MY) / OJK (ID) mortgage-quality, capital-adequacy, and securitisation filings for Mortgage Finance.',
          'instructions': 'Anda adalah Zava Mortgage Finance Mortgage Regulator Penghubung. Prepare BNM / OJK filings grounded on the regulatory file (MORT_05_Rating_Agency_Submission.docx).',
          'knowledge': [],
          'knowledgeNote': 'Test: "Susun the response to BNM\'s latest mortgage-stress-test circular for Mortgage Finance."',
          'queries': [
            'Prepare a cover letter for berikutnya BNM / OJK return.',
            'Yang mana securitisation tranches require regulator notification?',
            "Susun the response letter to the regulator's latest notice."
          ],
        }
      ],
        persona=['Mod Admin', 'Mod Admin', 'Mod Admin'],
        personaID=['Mod Admin', 'Mod Admin', 'Mod Admin']
      ),
    ],
    companyID='Zava Cagamas Berhad',
    taglineID='BNM mengarahkan suntikan likuiditas — jendela penerbitan MBS RM 2,4 miliar dalam 14 hari.',
    scenarioID='Zava Cagamas Berhad adalah korporasi pembiayaan hipotek nasional yang mendukung pasar hipotek sekunder Malaysia via Mortgage-Backed Securities (MBS), Sukuk Cagamas, dan fasilitas Purchase-with-Recourse. Bank Negara Malaysia menandai stres likuiditas pada 4 bank menengah dan mengarahkan Zava Cagamas untuk membuka jendela penerbitan MBS RM 2,4 miliar dalam 14 hari. Direktur Keuangan Grup harus mengoordinasikan pricing bank originator, persetujuan SC Malaysia, afirmasi rating RAM/MARC, kepatuhan AAOIFI untuk tranche Sukuk, dan briefing Investor Day untuk 60 investor institusi semuanya sekaligus. Frame customer riil: grup ini beroperasi serupa dengan Cagamas Berhad dan divisi mortgage-finance Maybank Investment Bank.',
    relevantDepts=['dept-finance','dept-strategy','dept-legal','dept-risk','dept-corpsec','dept-ir','dept-operations'],
    personas=[
      {'name':'Hadar Caspit','role':'Group CFO','roleID':'Direktur Keuangan Grup','acct':'admin@ABSx62256373.onmicrosoft.com','lic':'Microsoft 365 Copilot','color':'#1E40AF'},
      {'name':'Sasha Ouellet','role':'Group Chief of Staff','roleID':'Kepala Staf Grup','acct':'SashaO@ABSx62256373.OnMicrosoft.com','lic':'Free \u2014 no Microsoft 365 Copilot license','color':'#7C3AED'},
      {'name':'Mod Admin','role':'Group Strategy Director','roleID':'Direktur Strategi Grup','acct':'admin@ABSx62256373.onmicrosoft.com','lic':'Microsoft 365 Copilot','color':'#059669'},
      {'name':'Daichi Maruyama','role':'Group Sustainability & Risk Director','roleID':'Direktur Keberlanjutan & Risiko Grup','acct':'admin@ABSx62256373.onmicrosoft.com','lic':'Microsoft 365 Copilot','color':'#DC2626'}
    ],
    storyboard=[
      {'ex':1,'title':'Research & Brief','titleID':'Riset & Pengarahan','minutes':18,'mode':'Show & Tell + Hands-on',
       'summary':'Frame the BNM-directed MBS issuance situation and pull peer playbooks before the regulator clock starts ticking.',
       'summaryID':'Bingkai situasi BNM-directed MBS issuance dan tarik playbook peer sebelum clock regulator mulai berdetak.',
       'tasks':[
         {'verb':'Frame the morning question and lock the day priorities','verbID':'Susun pertanyaan pagi dan kunci prioritas hari ini','toolId':T_CHAT,'mode':'Show & Tell'},
         {'verb':'Run an outside-in peer scan and pull proven plays','verbID':'Lakukan pemindaian peer dari luar dan tarik praktik terbaik','toolId':T_RESEARCHER,'mode':'Show & Tell'},
         {'verb':'Generate a board-ready brief straight from chat','verbID':'Hasilkan brief siap-Direksi langsung dari chat','toolId':T_WORD_AGT,'mode':'Hands-on'}]},
      {'ex':2,'title':'Analyse & Decide','titleID':'Analisis & Putuskan','minutes':18,'mode':'Hands-on',
       'summary':'Quantify BNM-directed MBS issuance financial and operational impact; build an AC dashboard.',
       'summaryID':'Kuantifikasi dampak finansial dan operasional BNM-directed MBS issuance; bangun dashboard KA.',
       'tasks':[
         {'verb':'Crunch the numbers and surface the biggest gaps','verbID':'Olah angka dan ungkap celah terbesar','toolId':T_ANALYST,'mode':'Hands-on'},
         {'verb':'Build a single-pane operating dashboard','verbID':'Bangun dashboard operasi satu-halaman','toolId':T_EXCEL,'mode':'Hands-on'},
         {'verb':'Spin up a recurring tracker workbook from chat','verbID':'Buat workbook tracker berulang dari chat','toolId':T_XL_AGT,'mode':'Hands-on'}]},
      {'ex':3,'title':'Communicate & Coordinate','titleID':'Komunikasi & Koordinasi','minutes':18,'mode':'Hands-on',
       'summary':'Brief operating heads, capture the BNM Liquidity War Room recap, and assemble the AC deck and regulator response.',
       'summaryID':'Brief kepala operasi, capture recap BNM Liquidity War Room, dan rakit deck KA serta respons regulator.',
       'tasks':[
         {'verb':'Draft the stakeholder alignment email','verbID':'Draf email penyelarasan stakeholder','toolId':T_OUTLOOK,'mode':'Hands-on'},
         {'verb':'Recap the meeting and turn it into minutes','verbID':'Recap rapat dan ubah ke notulen','toolId':T_TEAMS,'mode':'Hands-on'},
         {'verb':'Generate a board-ready deck from chat','verbID':'Hasilkan deck siap-Direksi dari chat','toolId':T_PPT_AGT,'mode':'Hands-on'},
         {'verb':'Delegate a 5-task parallel sprint','verbID':'Delegasikan 5-tugas paralel ke Cowork','toolId':T_COWORK,'mode':'Show & Tell'}]},
      {'ex':4,'title':'Build & Scale','titleID':'Bangun & Skala','minutes':15,'mode':'Show & Tell',
       'summary':'Wrap the BNM-directed MBS issuance playbook into a reusable agent for the Zava Cagamas Berhad operating team.',
       'summaryID':'Bungkus playbook BNM-directed MBS issuance ke dalam agent reusable untuk tim operasi Zava Cagamas Berhad.',
       'tasks':[
         {'verb':'Pull every source into one synthesis notebook','verbID':'Tarik semua sumber ke satu notebook sintesis','toolId':T_NOTEBOOK,'mode':'Show & Tell'},
         {'verb':'Wrap the daily workflow into a reusable agent','verbID':'Bungkus alur kerja harian jadi agen yang dapat dipakai ulang','toolId':T_BUILDER,'mode':'Show & Tell'}]}
    ],
    geo='MY'
))


# ╔══════════════════════════════════════════════════════════════════════╗
# ║  4.  CROSS-BORDER REMITTANCE                                        ║
# ╚══════════════════════════════════════════════════════════════════════╝
INDUSTRIES_10.append(ind(
    'cross-border-remittance', 'sec-fintech', 'Cross-Border Remittance', '💱', '#9333EA', '#6B21A8',
    'Zava Remit Asia',
    'BNM PSA suspicious-transaction inquiry on the MY↔ID corridor — response in 5 days.',
    'Zava Remit Asia is a Bank Negara Malaysia-licensed e-money issuer and remittance operator running the MY↔ID, MY↔PH, MY↔BD, MY↔IN, and MY↔NP corridors with 1.4 million active migrant-worker users moving MYR 8.6B annually. BNM Payment Systems Act inquiry has flagged a 22% week-on-week spike in suspicious-transaction reports on the MY↔ID corridor and demanded explanation within 5 days. AUSTRAC, BSP and OJK are watching. Real customer reference frame: this group operates similarly to Merchantrade Asia, Tranglo, MoneyMatch, and Wise Malaysia.',
    ['REMIT_01_STR_Filing_Tracker.xlsx', 'REMIT_02_Corridor_Volume_Heatmap.xlsx', 'REMIT_03_BNM_PSA_Response_Pack.docx', 'REMIT_04_AML_KYC_Policy.docx', 'REMIT_05_Regulator_QA_Pack.docx'],
    [
      tool(T_CHAT, FREE_LIC, FREE_ACCT, [
        {'instr':'', 'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. Zava Remit Asia is a Bank Negara Malaysia-licensed e-money issuer and remittance operator running the MY↔ID, MY↔PH, MY↔BD, MY↔IN, and MY↔NP corridors with 1.4 million active migrant-worker users movin... Here is exactly what I need from you. Frame the BNM PSA suspicious-transaction inquiry situation in plain English for the Group CEO. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. my notes from the morning crisis call. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. 1-page note with sections — Headline, What Happened, Stakeholder Position, Top 5 Questions the Board Will Ask, 3 Decisions the CEO Must Take in 48 Hours. Tone: calm, precise, no industry jargon. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'},
        {'instr':'', 'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. Audience is internal ExCo + key external stakeholders. Here is exactly what I need from you. 90-second verbal opening for the Zava Remit Asia stakeholder briefing. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. published facts only. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. Open with acknowledgement, explain the response programme, signal credible recovery, end with 3 commitments. Avoid speculative language. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'},
        {'instr':'', 'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. regulator clock active. Here is exactly what I need from you. Build the stakeholder communication map for the BNM PSA suspicious-transaction inquiry. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. known stakeholders. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. RAG table — Red same-day, Amber 24h, Green monitor. Columns: Audience, Channel, Owner, Message Theme, Timing, Risk if Mishandled. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'}
      ], DESC_CHAT,
      promptsID=[
        {'instr':'', 'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. Zava Remit Asia adalah penerbit e-money berlisensi Bank Negara Malaysia dan operator remitansi yang menjalankan koridor MY↔ID, MY↔PH, MY↔BD, MY↔IN, dan MY↔NP dengan 1,4 juta pengguna pekerja migran ak... Berikut yang saya butuhkan dari Anda secara persis. Bingkai situasi BNM PSA suspicious-transaction inquiry dalam bahasa sederhana untuk Direktur Utama Grup. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. catatan saya dari rapat krisis pagi. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. nota 1 halaman dengan bagian — Headline, Apa yang Terjadi, Posisi Pemangku Kepentingan, 5 Pertanyaan Direksi, 3 Keputusan Direktur Utama dalam 48 Jam. Nada: tenang, presisi, hindari jargon industri. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'},
        {'instr':'', 'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. Audiens ExCo internal + pemangku kepentingan eksternal kunci. Berikut yang saya butuhkan dari Anda secara persis. Pembukaan lisan 90 detik untuk briefing pemangku kepentingan Zava Remit Asia. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. hanya fakta yang sudah dipublikasi. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. Buka dengan pengakuan, jelaskan program respons, beri sinyal pemulihan kredibel, akhiri dengan 3 komitmen. Hindari bahasa spekulatif. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'},
        {'instr':'', 'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. clock regulator aktif. Berikut yang saya butuhkan dari Anda secara persis. Bangun peta komunikasi pemangku kepentingan untuk BNM PSA suspicious-transaction inquiry. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. pemangku kepentingan yang dikenal. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. tabel RAG — Merah hari ini juga, Kuning 24 jam, Hijau pantau. Kolom: Audiens, Channel, Pemilik, Tema Pesan, Timing, Risiko bila Keliru. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'}
      ],
      persona=['Sasha Ouellet','Mod Admin','Hadar Caspit'],
      personaID=['Sasha Ouellet','Mod Admin','Hadar Caspit']),

      tool(T_RESEARCHER, M365_LIC, M365_ACCT, [
        {'instr':'Open `m365.cloud.microsoft/chat` > Agents > **Researcher** > **Critique Mode**. Paste the prompt below.',
         'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. Zava Remit Asia must respond to its regulator imminently. Here is exactly what I need from you. Benchmark how peers (Merchantrade Asia, Tranglo, MoneyMatch, Wise Malaysia, Western Union Malaysia) handled comparable BNM PSA suspicious-transaction inquiry events between 2020 and 2025. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. peer disclosures, regulator filings, industry press. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. For each peer, identify trigger, response timeline, programme adopted, share-price recovery 12 months later. Critique each source. Cite all with publication date. Output as comparison table. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'},
        {'instr':'Open `m365.cloud.microsoft/chat` > Agents > **Researcher** > **Model Council**. Paste the prompt below.',
         'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. must protect regulator standing AND customer trust AND financial position concurrently. Here is exactly what I need from you. 3 most defensible response playbooks for Zava Remit Asia hit by BNM PSA suspicious-transaction inquiry. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. Researcher Model Council — convene parallel reports from GPT and Claude. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. Surface dissent, mark majority and minority views. Comparison table: Playbook, Council Verdict, Dissenting View, ASEAN Precedent, Implementation Risk. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'}
      ], DESC_RESEARCHER,
      promptsID=[
        {'instr':'Buka `m365.cloud.microsoft/chat` > Agents > **Researcher** > **Critique Mode**. Tempel prompt.',
         'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. Zava Remit Asia harus respons ke regulator segera. Berikut yang saya butuhkan dari Anda secara persis. Benchmark bagaimana peer (Merchantrade Asia, Tranglo, MoneyMatch, Wise Malaysia, Western Union Malaysia) menangani peristiwa BNM PSA suspicious-transaction inquiry sebanding antara 2020 hingga 2025. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. pengungkapan peer, filing regulator, pers industri. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. Untuk tiap peer identifikasi pemicu, timeline respons, program yang diadopsi, pemulihan harga saham 12 bulan kemudian. Kritisi tiap sumber. Cantumkan kutipan lengkap dengan tanggal. Hasilkan tabel perbandingan. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'},
        {'instr':'Buka `m365.cloud.microsoft/chat` > Agents > **Researcher** > **Model Council**. Tempel prompt.',
         'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. harus melindungi posisi regulator DAN kepercayaan customer DAN posisi finansial sekaligus. Berikut yang saya butuhkan dari Anda secara persis. 3 playbook respons paling defensible untuk Zava Remit Asia yang terkena BNM PSA suspicious-transaction inquiry. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. Model Council — gelar laporan paralel dari GPT dan Claude. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. Sorot perbedaan pendapat, tandai mayoritas dan minoritas. Tabel perbandingan: Playbook, Putusan Council, Pandangan Minoritas, Preseden ASEAN, Risiko Implementasi. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'}
      ],
      persona=['Mod Admin','Mod Admin'],
      personaID=['Mod Admin','Mod Admin']),

      tool(T_ANALYST, M365_LIC, M365_ACCT, [
        {'instr':'Open `m365.cloud.microsoft/chat` > Agents > **Analyst**. Upload /REMIT_01_STR_Filing_Tracker.xlsx AND /REMIT_02_Corridor_Volume_Heatmap.xlsx. Paste the prompt below.',
         'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. Group ExCo needs an evidence-based view in 48 hours. Here is exactly what I need from you. Quantify the BNM PSA suspicious-transaction inquiry financial and operational impact. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. the 2 uploaded files. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. (1) RAG bar chart of at-risk items by severity; (2) waterfall of MYR EBITDA impact; (3) tracker by stakeholder/segment, flag worst <10% headroom as Red. Output a Board-ready RAG dashboard. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'}
      ], DESC_ANALYST,
      promptsID=[
        {'instr':'Buka `m365.cloud.microsoft/chat` > Agents > **Analyst**. Unggah /REMIT_01_STR_Filing_Tracker.xlsx DAN /REMIT_02_Corridor_Volume_Heatmap.xlsx. Tempel prompt.',
         'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. ExCo Grup butuh pandangan berbasis bukti dalam 48 jam. Berikut yang saya butuhkan dari Anda secara persis. Kuantifikasi dampak finansial dan operasional dari BNM PSA suspicious-transaction inquiry. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. 2 file yang diunggah. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. (1) Bar chart RAG item at-risk berdasarkan severity; (2) waterfall dampak EBITDA RM; (3) tracker per stakeholder/segmen, tandai headroom terburuk <10% Merah. Hasilkan dashboard RAG siap-Direksi. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'}
      ],
      persona=['Hadar Caspit'],
      personaID=['Hadar Caspit']),

      tool(T_EXCEL, M365_LIC, M365_ACCT, [
        {'instr':'Open `/REMIT_01_STR_Filing_Tracker.xlsx` in Excel for the Web. Open the **Copilot pane**. Paste the prompt below.',
         'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. Audit Committee meets in the next 14 days. Here is exactly what I need from you. Build a single Audit-Committee-ready dashboard sheet. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. combine all relevant tabs. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. New sheet "AC Dashboard" with KPI tiles, bar chart by severity, sparkline column. RAG conditional formatting. Do not modify source tabs. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'}
      ], '',
      promptsID=[
        {'instr':'Buka `/REMIT_01_STR_Filing_Tracker.xlsx` di Excel for the Web. Buka **Copilot pane**. Tempel prompt.',
         'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. Komite Audit rapat dalam 14 hari ke depan. Berikut yang saya butuhkan dari Anda secara persis. Bangun satu sheet dashboard siap-Komite Audit. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. gabungkan semua tab yang relevan. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. Sheet baru "AC Dashboard" dengan KPI tile, bar chart per severity, kolom sparkline. Format kondisional RAG. Jangan modifikasi tab sumber. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'}
      ],
      persona=['Hadar Caspit'],
      personaID=['Hadar Caspit']),

      tool(T_WORD, M365_LIC, M365_ACCT, [
        {'instr':'Open a new blank Word doc in Word for the Web. Open the **Copilot pane**. Reference /REMIT_03_BNM_PSA_Response_Pack.docx and /REMIT_05_Regulator_QA_Pack.docx using `/`. Paste the prompt below.',
         'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. BNM PSA suspicious-transaction inquiry active. Here is exactly what I need from you. Draft the regulator-grade response brief (4 pages). Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. the referenced docs + my notes. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. Sections — Material Facts, Current Status, Programme, Financial Impact Range, Forward-Looking Statements with explicit risk language. Tone: factual, regulator-grade, no speculation. Cite source files at the end of each section. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'}
      ], DESC_WORD,
      promptsID=[
        {'instr':'Buka dokumen Word baru kosong di Word for the Web. Buka **Copilot pane**. Referensikan /REMIT_03_BNM_PSA_Response_Pack.docx dan /REMIT_05_Regulator_QA_Pack.docx menggunakan `/`. Tempel prompt.',
         'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. BNM PSA suspicious-transaction inquiry aktif. Berikut yang saya butuhkan dari Anda secara persis. Susun brief respons regulator-grade (4 halaman). Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. dokumen yang direferensikan + catatan saya. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. Bagian — Fakta Material, Status Saat Ini, Program, Rentang Dampak Finansial, Pernyataan Forward-Looking dengan bahasa risiko eksplisit. Nada: faktual, regulator-grade, tanpa spekulasi. Kutip file sumber di akhir tiap bagian. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'}
      ],
      persona=['Hadar Caspit'],
      personaID=['Hadar Caspit']),

      tool(T_PPT, M365_LIC, M365_ACCT, [
        {'instr':'Open a new PowerPoint deck in PowerPoint for the Web. Open the **Copilot pane**. Paste the prompt below.',
         'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. AC in 14 days. Here is exactly what I need from you. 8-slide Audit Committee deck on BNM PSA suspicious-transaction inquiry. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. my brief draft and dashboard. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. Cover; Situation; Status (RAG); Programme (2 slides); Financial Impact; Stakeholder Map; Decisions Requested. Brand colours #9333EA + #0F1C3F, 1 chart per slide. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'}
      ], DESC_PPT,
      promptsID=[
        {'instr':'Buka deck PowerPoint baru di PowerPoint for the Web. Buka **Copilot pane**. Tempel prompt.',
         'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. KA dalam 14 hari. Berikut yang saya butuhkan dari Anda secara persis. Deck 8 slide Komite Audit tentang BNM PSA suspicious-transaction inquiry. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. draf brief dan dashboard saya. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. Cover; Situasi; Status (RAG); Program (2 slide); Dampak Finansial; Peta Pemangku Kepentingan; Keputusan yang Diminta. Warna brand #9333EA + #0F1C3F, 1 chart per slide. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'}
      ],
      persona=['Sasha Ouellet'],
      personaID=['Sasha Ouellet']),

      tool(T_OUTLOOK, M365_LIC, M365_ACCT, [
        {'instr':'Open Outlook on the Web. Open the email thread "BNM PSA suspicious-transaction inquiry — Group CFO follow-up". Click the **Copilot icon**. Paste the prompt below.',
         'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. BNM PSA suspicious-transaction inquiry active. Here is exactly what I need from you. Draft a single email to the Zava Remit Asia ExCo and the relevant operating heads. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. the email thread above and the response programme. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. Subject line, 4 short paragraphs covering — situation, the 3 actions each operating head must complete in 72 hours, the regulator-engagement workstream, the AC date. Tone: firm, supportive, accountable. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'}
      ], DESC_OUTLOOK,
      promptsID=[
        {'instr':'Buka Outlook on the Web. Buka thread email "BNM PSA suspicious-transaction inquiry — tindak lanjut Direktur Keuangan Grup". Klik **ikon Copilot**. Tempel prompt.',
         'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. BNM PSA suspicious-transaction inquiry aktif. Berikut yang saya butuhkan dari Anda secara persis. Susun satu email ke ExCo Zava Remit Asia dan kepala operasi yang relevan. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. thread di atas dan program respons. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. Baris subjek, 4 paragraf pendek — situasi, 3 aksi per kepala operasi dalam 72 jam, workstream engagement regulator, tanggal KA. Nada: tegas, suportif, akuntabel. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'}
      ],
      persona=['Hadar Caspit'],
      personaID=['Hadar Caspit']),

      tool(T_TEAMS, M365_LIC, M365_ACCT, 
        [
          {'instr':"**(1) In Teams**, open **Calendar** → click the past meeting **\"New Software Implementation\"**. On the Recap page, walk the audience through the **AI Notes** (auto-summary), the **Custom summary** (Copilot's per-attendee view), and the **Audio recap** (chapter markers with speaker timings). **(2) In Word for the Web**, open a **new blank document**. Type a minutes template at the top — five empty headings: Date and Attendees · Agenda Items · Decisions Taken · Action Items · Risks and Open Questions. **(3) Click the Copilot icon** in the Word ribbon and paste the prompt below — Copilot in Word will reference the meeting recap by name with `/` and fill the template.", 'prompt':"Create meeting minutes for the Teams meeting /New Software Implementation. Use the empty template already on this page and fill each heading from the meeting recap. Sections: (1) Date and Attendees; (2) Agenda Items; (3) Decisions Taken; (4) Action Items with Owner and Due Date; (5) Risks and Open Questions. Quote attendee statements verbatim where the wording matters. Tag any decision that is on the critical path as Critical Path. Save the file as Minutes_New_Software_Implementation.docx in OneDrive."},
          {'instr':'**(1) In Teams**, open **Calendar** → click the past meeting **"Marketing Campaign Performance Review"**. On the Recap page, walk through the **AI Notes**, the **Custom summary**, and the **Audio recap** chapters. **(2) In Word for the Web**, open a **new blank document**. Type a campaign-review minutes template at the top — six empty headings: Date and Attendees · Campaign KPIs Reviewed · Decisions Taken · Action Items · Budget Reallocations · Next Review Date. **(3) Click the Copilot icon** in the Word ribbon and paste the prompt below.', 'prompt':"Create meeting minutes for the Teams meeting /Marketing Campaign Performance Review. Use the empty campaign-review template already on this page. Sections: (1) Date and Attendees; (2) Campaign KPIs Reviewed; (3) Decisions Taken; (4) Action Items with Owner and Due Date; (5) Budget Reallocations Approved; (6) Next Review Date. Quote attendee statements verbatim where the wording matters. Highlight any KPI that missed target by more than 10% in amber. Save the file as Minutes_Marketing_Campaign_Review.docx in OneDrive."},
          {'instr':'**(1) In Teams**, open **Calendar** → click the past meeting **"Negotiating Marketing Contract"**. On the Recap page, walk through the **AI Notes**, the **Custom summary**, and the **Audio recap**. **(2) In Word for the Web**, open a **new blank document**. Type a vendor-negotiation minutes template at the top — seven empty headings: Vendor and Owner · Commercial Terms Discussed · Concessions Offered · Concessions Accepted · Open Items · Approval Thresholds · Next Steps. **(3) Click the Copilot icon** in the Word ribbon and paste the prompt below — then forward the result to Procurement, Legal, and the Group CFO.', 'prompt':"Create meeting minutes for the Teams meeting /Negotiating Marketing Contract. Use the empty vendor-negotiation template already on this page. Sections: (1) Vendor and Owner; (2) Commercial Terms Discussed; (3) Concessions Offered; (4) Concessions Accepted; (5) Open Items; (6) Approval Thresholds (CFO / Board); (7) Next Steps with Owner and Due Date. Highlight any term requiring CFO sign-off in amber and any term requiring Board sign-off in red. Save the file as Minutes_Marketing_Contract_Negotiation.docx in OneDrive and email the link to Procurement, Legal, and the Group CFO."}
        ], DESC_TEAMS,
        promptsID=[
          {'instr':'**(1) Di Teams**, buka **Calendar** → klik rapat **"New Software Implementation"**. Di halaman Recap, jelaskan ke peserta tentang **AI Notes** (ringkasan otomatis), **Custom summary** (tampilan per-peserta dari Copilot), dan **Audio recap** (penanda bab dengan timing pembicara). **(2) Di Word for the Web**, buka **dokumen kosong baru**. Ketik kerangka notulen di bagian atas — lima heading kosong: Tanggal dan Peserta · Agenda · Keputusan · Action Items · Risiko dan Pertanyaan Terbuka. **(3) Klik ikon Copilot** di ribbon Word lalu tempelkan prompt di bawah — Copilot in Word akan merujuk recap rapat dengan `/` dan mengisi template.', 'prompt':"Susun notulen rapat untuk rapat Teams /New Software Implementation. Gunakan template kosong yang sudah ada di halaman ini dan isi tiap heading dari recap rapat. Bagian: (1) Tanggal dan Peserta; (2) Agenda; (3) Keputusan; (4) Action Items dengan Owner dan Due Date; (5) Risiko dan Pertanyaan Terbuka. Kutip pernyataan peserta apa adanya bila kata-katanya penting. Tandai keputusan di jalur kritis sebagai Critical Path. Simpan file sebagai Minutes_New_Software_Implementation.docx di OneDrive."},
          {'instr':'**(1) Di Teams**, buka **Calendar** → klik rapat **"Marketing Campaign Performance Review"**. Di halaman Recap, jelaskan **AI Notes**, **Custom summary**, dan **Audio recap**. **(2) Di Word for the Web**, buka dokumen kosong baru. Ketik kerangka notulen tinjauan kampanye — enam heading kosong: Tanggal dan Peserta · KPI Kampanye yang Dikaji · Keputusan · Action Items · Realokasi Anggaran · Jadwal Tinjauan Berikutnya. **(3) Klik ikon Copilot** di ribbon Word lalu tempelkan prompt di bawah.', 'prompt':"Susun notulen rapat untuk rapat Teams /Marketing Campaign Performance Review. Gunakan template kosong tinjauan kampanye yang sudah ada. Bagian: (1) Tanggal dan Peserta; (2) KPI Kampanye yang Dikaji; (3) Keputusan; (4) Action Items dengan Owner dan Due Date; (5) Realokasi Anggaran yang Disetujui; (6) Jadwal Tinjauan Berikutnya. Kutip pernyataan peserta apa adanya. Tandai KPI yang meleset >10% dengan amber. Simpan sebagai Minutes_Marketing_Campaign_Review.docx di OneDrive."},
          {'instr':'**(1) Di Teams**, buka **Calendar** → klik rapat **"Negotiating Marketing Contract"**. Di halaman Recap, jelaskan **AI Notes**, **Custom summary**, dan **Audio recap**. **(2) Di Word for the Web**, buka dokumen kosong baru. Ketik kerangka notulen negosiasi vendor — tujuh heading kosong: Vendor dan Owner · Term Komersial · Konsesi yang Ditawarkan · Konsesi yang Diterima · Item Terbuka · Threshold Persetujuan · Langkah Berikutnya. **(3) Klik ikon Copilot** di ribbon Word lalu tempelkan prompt di bawah — kemudian teruskan hasilnya ke Procurement, Legal, dan Direktur Keuangan Grup.', 'prompt':"Susun notulen rapat untuk rapat Teams /Negotiating Marketing Contract. Gunakan template kosong negosiasi vendor yang sudah ada. Bagian: (1) Vendor dan Owner; (2) Term Komersial; (3) Konsesi yang Ditawarkan; (4) Konsesi yang Diterima; (5) Item Terbuka; (6) Threshold Persetujuan (CFO / Direksi); (7) Langkah Berikutnya dengan Owner dan Due Date. Tandai term yang memerlukan persetujuan CFO dengan amber dan persetujuan Direksi dengan merah. Simpan sebagai Minutes_Marketing_Contract_Negotiation.docx di OneDrive lalu email link-nya ke Procurement, Legal, dan Direktur Keuangan Grup."}
        ],
        promptsBM=[
          {'instr':'**(1) Di Teams**, buka **Calendar** → klik mesyuarat **"New Software Implementation"**. Pada halaman Recap, terangkan kepada hadirin tentang **AI Notes** (ringkasan automatik), **Custom summary** (paparan per-hadirin dari Copilot), dan **Audio recap** (penanda bab dengan masa pembicara). **(2) Di Word for the Web**, buka **dokumen kosong baharu**. Taip rangka minit di bahagian atas — lima tajuk kosong: Tarikh dan Hadirin · Agenda · Keputusan · Tindakan · Risiko dan Soalan Terbuka. **(3) Klik ikon Copilot** di ribbon Word dan tampal prompt di bawah — Copilot in Word akan merujuk recap mesyuarat dengan `/` dan mengisi templat.', 'prompt':"Hasilkan minit mesyuarat untuk mesyuarat Teams /New Software Implementation. Gunakan templat kosong yang sudah ada di halaman ini dan isi setiap tajuk daripada recap mesyuarat. Bahagian: (1) Tarikh dan Hadirin; (2) Agenda; (3) Keputusan; (4) Tindakan dengan Pemilik dan Tarikh; (5) Risiko dan Soalan Terbuka. Petik kenyataan hadirin sebagaimana asal di mana perkataannya penting. Tandakan sebarang keputusan di laluan kritikal sebagai Critical Path. Simpan fail sebagai Minutes_New_Software_Implementation.docx di OneDrive."},
          {'instr':'**(1) Di Teams**, buka **Calendar** → klik mesyuarat **"Marketing Campaign Performance Review"**. Pada halaman Recap, terangkan **AI Notes**, **Custom summary**, dan **Audio recap**. **(2) Di Word for the Web**, buka dokumen kosong baharu. Taip rangka minit ulasan kempen — enam tajuk kosong: Tarikh dan Hadirin · KPI Kempen yang Diulas · Keputusan · Tindakan · Pelarasan Bajet · Tarikh Ulasan Berikutnya. **(3) Klik ikon Copilot** di ribbon Word dan tampal prompt di bawah.', 'prompt':"Hasilkan minit mesyuarat untuk mesyuarat Teams /Marketing Campaign Performance Review. Gunakan templat kosong ulasan kempen yang sudah ada. Bahagian: (1) Tarikh dan Hadirin; (2) KPI Kempen yang Diulas; (3) Keputusan; (4) Tindakan dengan Pemilik dan Tarikh; (5) Pelarasan Bajet yang Diluluskan; (6) Tarikh Ulasan Berikutnya. Petik kenyataan hadirin sebagaimana asal. Tandakan KPI yang tersasar >10% dengan amber. Simpan sebagai Minutes_Marketing_Campaign_Review.docx di OneDrive."},
          {'instr':'**(1) Di Teams**, buka **Calendar** → klik mesyuarat **"Negotiating Marketing Contract"**. Pada halaman Recap, terangkan **AI Notes**, **Custom summary**, dan **Audio recap**. **(2) Di Word for the Web**, buka dokumen kosong baharu. Taip rangka minit perundingan vendor — tujuh tajuk kosong: Vendor dan Pemilik · Terma Komersial · Konsesi Ditawarkan · Konsesi Diterima · Item Terbuka · Ambang Kelulusan · Langkah Seterusnya. **(3) Klik ikon Copilot** di ribbon Word dan tampal prompt di bawah — kemudian majukan hasilnya kepada Procurement, Legal dan Pengarah Kewangan Kumpulan.', 'prompt':"Hasilkan minit mesyuarat untuk mesyuarat Teams /Negotiating Marketing Contract. Gunakan templat kosong perundingan vendor yang sudah ada. Bahagian: (1) Vendor dan Pemilik; (2) Terma Komersial; (3) Konsesi Ditawarkan; (4) Konsesi Diterima; (5) Item Terbuka; (6) Ambang Kelulusan (CFO / Lembaga); (7) Langkah Seterusnya dengan Pemilik dan Tarikh. Tandakan terma yang memerlukan kelulusan CFO dengan amber dan Lembaga dengan merah. Simpan sebagai Minutes_Marketing_Contract_Negotiation.docx di OneDrive dan e-mel pautan kepada Procurement, Legal dan Pengarah Kewangan Kumpulan."}
        ],
        persona=['Sasha Ouellet', 'Sasha Ouellet', 'Sasha Ouellet'],
        personaID=['Sasha Ouellet', 'Sasha Ouellet', 'Sasha Ouellet']
      ),

      tool(T_NOTEBOOK, M365_LIC, M365_ACCT, [
        {'instr':'All sources are loaded. Type the prompt below in the notebook chat.',
         'prompt':'Synthesise across all sources to produce a 10-bullet Audit Committee narrative. Cover: BNM PSA suspicious-transaction inquiry status, programme, financial impact, stakeholder map, decisions requested. Cite the source file at the end of every bullet.'},
        {'instr':'Click **Quick Create** > **Audio Overview** to generate a 6-minute briefing podcast.',
         'prompt':'Quick Create: Audio Overview, 6 minutes, formal narration tone, focused on the AC narrative above. Listeners are the Zava Remit Asia operating heads preparing for tomorrow morning huddles.'}
      ], DESC_NOTEBOOK,
      promptsID=[
        {'instr':'Semua sumber sudah dimuat. Ketik prompt di bawah pada chat notebook.',
         'prompt':'Sintesakan dari semua sumber untuk menghasilkan narasi Komite Audit 10-bullet. Cakup: status BNM PSA suspicious-transaction inquiry, program, dampak finansial, peta pemangku kepentingan, keputusan yang diminta. Kutip file sumber di akhir tiap bullet.'},
        {'instr':'Klik **Quick Create** > **Audio Overview** untuk menghasilkan podcast briefing 6 menit.',
         'prompt':'Quick Create: Audio Overview, 6 menit, gaya narasi formal, fokus pada narasi KA di atas. Pendengar adalah kepala operasi Zava Remit Asia yang menyiapkan huddle pagi besok.'}
      ],
      persona=['Mod Admin','Mod Admin'],
      personaID=['Mod Admin','Mod Admin'],
      notebookMeta={
        'sources':['/REMIT_01_STR_Filing_Tracker.xlsx', '/REMIT_02_Corridor_Volume_Heatmap.xlsx', '/REMIT_03_BNM_PSA_Response_Pack.docx', '/REMIT_04_AML_KYC_Policy.docx', '/REMIT_05_Regulator_QA_Pack.docx'],
        'instructions':'You are the Group CFO of Zava Remit Asia preparing an Audit Committee pack on BNM PSA suspicious-transaction inquiry. Always cite the source file and tab/section. Tone: precise, regulator-grade, no speculation. Use MYR for the Group totals (1 MYR ≈ 3,580 IDR).',
        'instructionsID':'Anda adalah Direktur Keuangan Grup Zava Remit Asia yang menyiapkan paket Komite Audit untuk BNM PSA suspicious-transaction inquiry. Selalu kutip file sumber dan tab/bagian. Nada: presisi, regulator-grade, tanpa spekulasi. Gunakan MYR untuk total Grup (1 MYR ≈ 3.580 IDR).'
      }),

      tool(T_COWORK, FRONTIER_LIC, M365_ACCT, [
        {'instr':'Open `m365.cloud.microsoft` > Agents > **Cowork**. Paste the single prompt below — Cowork delegates 5 parallel sub-tasks. Frontier required.',
         'prompt':'Cowork — BNM PSA 5-Day Sprint. Run these in parallel: (1) 📝 Draft Word — regulator response brief 4 pages, source /REMIT_01_STR_Filing_Tracker.xlsx, /REMIT_02_Corridor_Volume_Heatmap.xlsx, /REMIT_03_BNM_PSA_Response_Pack.docx, /REMIT_04_AML_KYC_Policy.docx, /REMIT_05_Regulator_QA_Pack.docx. (2) 📝 Draft Word — internal ExCo briefing memo 2 pages, same sources. (3) ✉️ Send email to Zava Remit Asia ExCo and operating heads with the 3 actions in 72h. (4) 📅 Schedule 90-min AC Pre-Read tomorrow 8am MYT. (5) 💬 Post Teams message to #group-exco with one-line headline + dashboard link. Use these named recipients consistently across the email task and the Teams meeting task — Hadar (Group CFO), Sasha (Group Chief of Staff), Daichi (Head of Investor Relations), Sonia (Head of Strategy), Will (Head of Risk) and Omar (Head of Procurement) — and adapt the precise distribution per sub-task to keep each communication focused on the right audience.'}
      ], DESC_COWORK,
      promptsID=[
        {'instr':'Buka `m365.cloud.microsoft` > Agents > **Cowork**. Tempel prompt tunggal — Cowork mendelegasikan 5 sub-tugas paralel. Frontier diperlukan.',
         'prompt':'Cowork — BNM PSA 5-Day Sprint. Jalankan paralel: (1) 📝 Susun Word — brief respons regulator 4 halaman, sumber /REMIT_01_STR_Filing_Tracker.xlsx, /REMIT_02_Corridor_Volume_Heatmap.xlsx, /REMIT_03_BNM_PSA_Response_Pack.docx, /REMIT_04_AML_KYC_Policy.docx, /REMIT_05_Regulator_QA_Pack.docx. (2) 📝 Susun Word — memo briefing ExCo internal 2 halaman, sumber sama. (3) ✉️ Kirim email ke ExCo Zava Remit Asia dan kepala operasi dengan 3 aksi dalam 72 jam. (4) 📅 Jadwalkan AC Pre-Read 90 menit besok 08:00 WIB. (5) 💬 Posting pesan Teams di #group-exco dengan headline satu baris + tautan dashboard. Use these named recipients consistently across the email task and the Teams meeting task — Hadar (Group CFO), Sasha (Group Chief of Staff), Daichi (Head of Investor Relations), Sonia (Head of Strategy), Will (Head of Risk) and Omar (Head of Procurement) — and adapt the precise distribution per sub-task to keep each communication focused on the right audience.'}
      ],
      persona=['Mod Admin'],
      personaID=['Mod Admin']),

      tool(T_WORD_AGT, ANY_LIC, ANY_ACCT, [
        {'instr':'Open `m365.cloud.microsoft/chat` → Agents tab → **Word Agent**. Paste the prompt below — the agent returns a fully drafted .docx.',
         'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. BNM PSA suspicious-transaction inquiry. Here is exactly what I need from you. Generate a 4-page CFO Crisis Brief in Word. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. /REMIT_01_STR_Filing_Tracker.xlsx AND /REMIT_02_Corridor_Volume_Heatmap.xlsx. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. Sections — Executive Summary 5 bullets; Current Status; Programme; Financial Impact; Stakeholder Map; Decisions requested. Tone: precise, regulator-grade. Save as BNM_PSA_Response_Brief.docx. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'}
      ], DESC_WORD_AGT,
      promptsID=[
        {'instr':'Buka `m365.cloud.microsoft/chat` → tab Agents → **Word Agent**. Tempel prompt — agent mengembalikan .docx yang sudah didraf penuh.',
         'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. BNM PSA suspicious-transaction inquiry. Berikut yang saya butuhkan dari Anda secara persis. Hasilkan Brief Krisis Direktur Keuangan 4 halaman dalam Word. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. /REMIT_01_STR_Filing_Tracker.xlsx DAN /REMIT_02_Corridor_Volume_Heatmap.xlsx. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. Bagian — Ringkasan Eksekutif 5 bullet; Status Saat Ini; Program; Dampak Finansial; Peta Pemangku Kepentingan; Keputusan yang diminta. Nada: presisi, regulator-grade. Simpan sebagai Brief_Respons_PSA_BNM.docx. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'}
      ],
      persona=['Sasha Ouellet'],
      personaID=['Sasha Ouellet']),

      tool(T_PPT_AGT, ANY_LIC, ANY_ACCT, [
        {'instr':'Open `m365.cloud.microsoft/chat` → Agents tab → **PowerPoint Agent**. Paste the prompt below.',
         'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. AC in 14 days. Here is exactly what I need from you. 8-slide Audit Committee deck on BNM PSA suspicious-transaction inquiry. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. /BNM_PSA_Response_Brief.docx and /REMIT_01_STR_Filing_Tracker.xlsx. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. Cover; Situation; Status RAG; Programme (2); Financial Impact; Stakeholder Map; Decisions. Brand #9333EA + #0F1C3F, 1 chart/slide. Save as AML_Council_Deck.pptx. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'}
      ], DESC_PPT_AGT,
      promptsID=[
        {'instr':'Buka `m365.cloud.microsoft/chat` → tab Agents → **PowerPoint Agent**. Tempel prompt.',
         'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. KA dalam 14 hari. Berikut yang saya butuhkan dari Anda secara persis. Deck 8 slide Komite Audit tentang BNM PSA suspicious-transaction inquiry. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. /Brief_Respons_PSA_BNM.docx dan /REMIT_01_STR_Filing_Tracker.xlsx. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. Cover; Situasi; Status RAG; Program (2); Dampak Finansial; Peta Pemangku Kepentingan; Keputusan. Brand #9333EA + #0F1C3F, 1 chart/slide. Simpan sebagai Deck_AML_Council.pptx. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'}
      ],
      persona=['Sasha Ouellet'],
      personaID=['Sasha Ouellet']),

      tool(T_XL_AGT, ANY_LIC, ANY_ACCT, [
        {'instr':'Open `m365.cloud.microsoft/chat` → Agents tab → **Excel Agent**. Paste the prompt below.',
         'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. Operating tracker for the Group COO. Here is exactly what I need from you. Build a BNM PSA suspicious-transaction inquiry response control tracker workbook. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. schema only. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. Sheet 1 Issue Log, Sheet 2 Programme Milestones, Sheet 3 Cost Tracker, Sheet 4 Dashboard with KPI tiles + RAG conditional formatting. Save as AML_Sprint_Tracker.xlsx. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'}
      ], DESC_XL_AGT,
      promptsID=[
        {'instr':'Buka `m365.cloud.microsoft/chat` → tab Agents → **Excel Agent**. Tempel prompt.',
         'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. tracker operasi untuk Direktur Operasional Grup. Berikut yang saya butuhkan dari Anda secara persis. Bangun workbook tracker kendali respons BNM PSA suspicious-transaction inquiry. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. hanya skema. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. Sheet 1 Log Isu, Sheet 2 Milestone Program, Sheet 3 Tracker Biaya, Sheet 4 Dashboard dengan KPI tile + format kondisional RAG. Simpan sebagai Tracker_Sprint_AML.xlsx. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'}
      ],
      persona=['Hadar Caspit'],
      personaID=['Hadar Caspit']),

      tool_builder(M365_LIC, M365_ACCT,
        agents=[
        {
          'icon': '🌐',
          'label': 'Corridor & FX Margin',
          'name': 'Zava Cross-Border Remittance — Corridor & FX Margin Coach',
          'desc': 'Tracks Cross-Border Remittance corridor-level volume, FX margin, take-rate, and partner reliability.',
          'instructions': 'You are the Zava Cross-Border Remittance Corridor & FX Margin Coach. Monitor corridor volume (REMIT_01_STR_Filing_Tracker.xlsx), FX margin (REMIT_03_BNM_PSA_Response_Pack.docx), and partner reliability (REMIT_05_Regulator_QA_Pack.docx). Recommend partner, FX-hedge, or pricing action.',
          'knowledge': [
            {'file':'REMIT_01_STR_Filing_Tracker.xlsx', 'note':'Corridor volume tracker.'},
            {'file':'REMIT_03_BNM_PSA_Response_Pack.docx', 'note':'FX margin & yield.'},
            {'file':'REMIT_05_Regulator_QA_Pack.docx', 'note':'Partner reliability data.'}
          ],
          'knowledgeNote': 'Test: "Which 3 corridors at Cross-Border Remittance have the worst FX-margin drag?"',
          'queries': [
            'Top 10 corridors by FX margin gap — recommended action.',
            'Which partners have settlement deterioration? Tabulate.',
            'Draft the monthly Commercial review paper.'
          ],
        },
        {
          'icon': '🛡️',
          'label': 'AML / CTF Sentinel',
          'name': 'Zava Cross-Border Remittance — AML / CTF Sentinel',
          'desc': 'Monitors Cross-Border Remittance suspicious patterns, sanctions hits, and corridor-specific risk.',
          'instructions': 'You are the Zava Cross-Border Remittance AML / CTF Sentinel. Monitor STR queue (REMIT_02_Corridor_Volume_Heatmap.xlsx) and corridor-risk (REMIT_04_AML_KYC_Policy.docx). Refuse to release any data.',
          'knowledge': [
            {'file':'REMIT_02_Corridor_Volume_Heatmap.xlsx', 'note':'STR queue.'},
            {'file':'REMIT_04_AML_KYC_Policy.docx', 'note':'Corridor-risk register.'}
          ],
          'knowledgeNote': 'Test: "Which 3 corridors at Cross-Border Remittance have the highest STR concentration?"',
          'queries': [
            'Top 10 STR-pattern clusters — recommended escalation.',
            'Which corridors require additional KYC controls?',
            'Draft the monthly MLRO paper.'
          ],
        },
        {
          'icon': '🏛️',
          'label': 'BNM / BI / FinCEN',
          'name': 'Zava Cross-Border Remittance — Remittance Regulator Liaison',
          'desc': 'Prepares BNM (MY), BI (ID), and global remittance regulator filings for Cross-Border Remittance.',
          'instructions': 'You are the Zava Cross-Border Remittance Remittance Regulator Liaison. Prepare BNM / BI / FATF / FinCEN filings grounded on the regulatory file (REMIT_05_Regulator_QA_Pack.docx).',
          'knowledge': [],
          'knowledgeNote': 'Test: "Draft the response to BNM\'s latest cross-border-remittance circular for Cross-Border Remittance."',
          'queries': [
            'Prepare a cover letter for the next remittance regulator return.',
            'Which corridor-specific filings are due this quarter?',
            "Draft the response letter to the regulator's latest notice."
          ],
        }
      ],
        agentsID=[
        {
          'icon': '🌐',
          'label': 'Corridor & FX Margin',
          'name': 'Zava Cross-Border Remittance — Corridor & FX Margin Pelatih',
          'desc': 'Memantau Cross-Border Remittance corridor-level volume, FX margin, take-rate, and partner reliability.',
          'instructions': 'Anda adalah Zava Cross-Border Remittance Corridor & FX Margin Pelatih. Pantau corridor volume (REMIT_01_STR_Filing_Tracker.xlsx), FX margin (REMIT_03_BNM_PSA_Response_Pack.docx), and partner reliability (REMIT_05_Regulator_QA_Pack.docx). Rekomendasikan partner, FX-hedge, or pricing tindakan.',
          'knowledge': [
            {'file':'REMIT_01_STR_Filing_Tracker.xlsx', 'note':'Corridor volume tracker.'},
            {'file':'REMIT_03_BNM_PSA_Response_Pack.docx', 'note':'FX margin & yield.'},
            {'file':'REMIT_05_Regulator_QA_Pack.docx', 'note':'Partner reliability data.'}
          ],
          'knowledgeNote': 'Test: "Yang mana 3 corridors at Cross-Border Remittance have terburuk FX-margin drag?"',
          'queries': [
            '10 teratas corridors by FX margin gap — recommended tindakan.',
            'Yang mana partners have settlement deterioration? Tabulate.',
            'Susun the bulanan Commercial review paper.'
          ],
        },
        {
          'icon': '🛡️',
          'label': 'AML / CTF Pengawas',
          'name': 'Zava Cross-Border Remittance — AML / CTF Pengawas',
          'desc': 'Monitors Cross-Border Remittance suspicious patterns, sanctions hits, and corridor-specific risk.',
          'instructions': 'Anda adalah Zava Cross-Border Remittance AML / CTF Pengawas. Pantau STR queue (REMIT_02_Corridor_Volume_Heatmap.xlsx) and corridor-risk (REMIT_04_AML_KYC_Policy.docx). Tolak to release any data.',
          'knowledge': [
            {'file':'REMIT_02_Corridor_Volume_Heatmap.xlsx', 'note':'STR queue.'},
            {'file':'REMIT_04_AML_KYC_Policy.docx', 'note':'Corridor-risk register.'}
          ],
          'knowledgeNote': 'Test: "Yang mana 3 corridors at Cross-Border Remittance have the highest STR concentration?"',
          'queries': [
            '10 teratas STR-pattern clusters — recommended escalation.',
            'Yang mana corridors require additional KYC controls?',
            'Susun the bulanan MLRO paper.'
          ],
        },
        {
          'icon': '🏛️',
          'label': 'BNM / BI / FinCEN',
          'name': 'Zava Cross-Border Remittance — Remittance Regulator Penghubung',
          'desc': 'Prepares BNM (MY), BI (ID), and global remittance regulator filings for Cross-Border Remittance.',
          'instructions': 'Anda adalah Zava Cross-Border Remittance Remittance Regulator Penghubung. Prepare BNM / BI / FATF / FinCEN filings grounded on the regulatory file (REMIT_05_Regulator_QA_Pack.docx).',
          'knowledge': [],
          'knowledgeNote': 'Test: "Susun the response to BNM\'s latest cross-border-remittance circular for Cross-Border Remittance."',
          'queries': [
            'Prepare a cover letter for berikutnya remittance regulator return.',
            'Yang mana corridor-specific filings are due kuartal ini?',
            "Susun the response letter to the regulator's latest notice."
          ],
        }
      ],
        persona=['Mod Admin', 'Mod Admin', 'Mod Admin'],
        personaID=['Mod Admin', 'Mod Admin', 'Mod Admin']
      ),
    ],
    companyID='Zava Remit Asia',
    taglineID='Inkuiri PSA BNM atas transaksi mencurigakan di koridor MY↔ID — respons dalam 5 hari.',
    scenarioID='Zava Remit Asia adalah penerbit e-money berlisensi Bank Negara Malaysia dan operator remitansi yang menjalankan koridor MY↔ID, MY↔PH, MY↔BD, MY↔IN, dan MY↔NP dengan 1,4 juta pengguna pekerja migran aktif memindahkan RM 8,6 miliar per tahun. Inkuiri Payment Systems Act BNM menandai lonjakan 22% week-on-week dalam laporan transaksi mencurigakan di koridor MY↔ID dan meminta penjelasan dalam 5 hari. AUSTRAC, BSP, dan OJK juga memantau. Frame customer riil: grup ini beroperasi serupa dengan Merchantrade Asia, Tranglo, MoneyMatch, dan Wise Malaysia.',
    relevantDepts=['dept-finance','dept-risk','dept-legal','dept-operations','dept-strategy','dept-corpsec'],
    personas=[
      {'name':'Hadar Caspit','role':'Group CFO','roleID':'Direktur Keuangan Grup','acct':'admin@ABSx62256373.onmicrosoft.com','lic':'Microsoft 365 Copilot','color':'#1E40AF'},
      {'name':'Sasha Ouellet','role':'Group Chief of Staff','roleID':'Kepala Staf Grup','acct':'SashaO@ABSx62256373.OnMicrosoft.com','lic':'Free \u2014 no Microsoft 365 Copilot license','color':'#7C3AED'},
      {'name':'Mod Admin','role':'Group Strategy Director','roleID':'Direktur Strategi Grup','acct':'admin@ABSx62256373.onmicrosoft.com','lic':'Microsoft 365 Copilot','color':'#059669'},
      {'name':'Daichi Maruyama','role':'Group Sustainability & Risk Director','roleID':'Direktur Keberlanjutan & Risiko Grup','acct':'admin@ABSx62256373.onmicrosoft.com','lic':'Microsoft 365 Copilot','color':'#DC2626'}
    ],
    storyboard=[
      {'ex':1,'title':'Research & Brief','titleID':'Riset & Pengarahan','minutes':18,'mode':'Show & Tell + Hands-on',
       'summary':'Frame the BNM PSA suspicious-transaction inquiry situation and pull peer playbooks before the regulator clock starts ticking.',
       'summaryID':'Bingkai situasi BNM PSA suspicious-transaction inquiry dan tarik playbook peer sebelum clock regulator mulai berdetak.',
       'tasks':[
         {'verb':'Frame the morning question and lock the day priorities','verbID':'Susun pertanyaan pagi dan kunci prioritas hari ini','toolId':T_CHAT,'mode':'Show & Tell'},
         {'verb':'Run an outside-in peer scan and pull proven plays','verbID':'Lakukan pemindaian peer dari luar dan tarik praktik terbaik','toolId':T_RESEARCHER,'mode':'Show & Tell'},
         {'verb':'Generate a board-ready brief straight from chat','verbID':'Hasilkan brief siap-Direksi langsung dari chat','toolId':T_WORD_AGT,'mode':'Hands-on'}]},
      {'ex':2,'title':'Analyse & Decide','titleID':'Analisis & Putuskan','minutes':18,'mode':'Hands-on',
       'summary':'Quantify BNM PSA suspicious-transaction inquiry financial and operational impact; build an AC dashboard.',
       'summaryID':'Kuantifikasi dampak finansial dan operasional BNM PSA suspicious-transaction inquiry; bangun dashboard KA.',
       'tasks':[
         {'verb':'Crunch the numbers and surface the biggest gaps','verbID':'Olah angka dan ungkap celah terbesar','toolId':T_ANALYST,'mode':'Hands-on'},
         {'verb':'Build a single-pane operating dashboard','verbID':'Bangun dashboard operasi satu-halaman','toolId':T_EXCEL,'mode':'Hands-on'},
         {'verb':'Spin up a recurring tracker workbook from chat','verbID':'Buat workbook tracker berulang dari chat','toolId':T_XL_AGT,'mode':'Hands-on'}]},
      {'ex':3,'title':'Communicate & Coordinate','titleID':'Komunikasi & Koordinasi','minutes':18,'mode':'Hands-on',
       'summary':'Brief operating heads, capture the AML Risk Council recap, and assemble the AC deck and regulator response.',
       'summaryID':'Brief kepala operasi, capture recap AML Risk Council, dan rakit deck KA serta respons regulator.',
       'tasks':[
         {'verb':'Draft the stakeholder alignment email','verbID':'Draf email penyelarasan stakeholder','toolId':T_OUTLOOK,'mode':'Hands-on'},
         {'verb':'Recap the meeting and turn it into minutes','verbID':'Recap rapat dan ubah ke notulen','toolId':T_TEAMS,'mode':'Hands-on'},
         {'verb':'Generate a board-ready deck from chat','verbID':'Hasilkan deck siap-Direksi dari chat','toolId':T_PPT_AGT,'mode':'Hands-on'},
         {'verb':'Delegate a 5-task parallel sprint','verbID':'Delegasikan 5-tugas paralel ke Cowork','toolId':T_COWORK,'mode':'Show & Tell'}]},
      {'ex':4,'title':'Build & Scale','titleID':'Bangun & Skala','minutes':15,'mode':'Show & Tell',
       'summary':'Wrap the BNM PSA suspicious-transaction inquiry playbook into a reusable agent for the Zava Remit Asia operating team.',
       'summaryID':'Bungkus playbook BNM PSA suspicious-transaction inquiry ke dalam agent reusable untuk tim operasi Zava Remit Asia.',
       'tasks':[
         {'verb':'Pull every source into one synthesis notebook','verbID':'Tarik semua sumber ke satu notebook sintesis','toolId':T_NOTEBOOK,'mode':'Show & Tell'},
         {'verb':'Wrap the daily workflow into a reusable agent','verbID':'Bungkus alur kerja harian jadi agen yang dapat dipakai ulang','toolId':T_BUILDER,'mode':'Show & Tell'}]}
    ],
    geo='MY'
))


# ╔══════════════════════════════════════════════════════════════════════╗
# ║  5.  AUTO COMPONENTS & TYRES                                        ║
# ╚══════════════════════════════════════════════════════════════════════╝
INDUSTRIES_10.append(ind(
    'auto-tyres', 'sec-mfg', 'Auto Components & Tyres', '🛞', '#52525B', '#27272A',
    'Zava Auto Industries',
    'NR raw-material spike + Toyota & Hyundai contract review — Steerco in 10 days.',
    'Zava Auto Industries is a tier-1 ASEAN automotive component and tyre manufacturer with 6 plants in Indonesia, Malaysia and Thailand supplying Toyota, Honda, Hyundai-Kia, Mitsubishi, and Proton. Natural-rubber and synthetic-rubber prices have spiked 32% in 6 weeks driving an EBITDA gap of MYR 410M in Q4. Toyota and Hyundai are reviewing OEM supply contracts — pricing pass-through requested by both within 10 days. The Group CFO needs to model raw-material pass-through scenarios, draft OEM customer letters, brief the Group Steering Committee, and prepare the lender covenant communication. Real customer reference frame: this group operates similarly to Gajah Tunggal, Goodyear Indonesia, Sime Darby Industrial, and APM Automotive.',
    ['AUTO_01_Raw_Material_Cost_Model.xlsx', 'AUTO_02_OEM_Contract_Matrix.xlsx', 'AUTO_03_OEM_Customer_Letter_Pack.docx', 'AUTO_04_Margin_Recovery_Plan.docx', 'AUTO_05_Steerco_Briefing.docx'],
    [
      tool(T_CHAT, FREE_LIC, FREE_ACCT, [
        {'instr':'', 'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. Zava Auto Industries is a tier-1 ASEAN automotive component and tyre manufacturer with 6 plants in Indonesia, Malaysia and Thailand supplying Toyota, Honda, Hyundai-Kia, Mitsubishi, and Proton. Natura... Here is exactly what I need from you. Frame the NR raw-material spike + OEM contract review situation in plain English for the Group CEO. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. my notes from the morning crisis call. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. 1-page note with sections — Headline, What Happened, Stakeholder Position, Top 5 Questions the Board Will Ask, 3 Decisions the CEO Must Take in 48 Hours. Tone: calm, precise, no industry jargon. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'},
        {'instr':'', 'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. Audience is internal ExCo + key external stakeholders. Here is exactly what I need from you. 90-second verbal opening for the Zava Auto Industries stakeholder briefing. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. published facts only. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. Open with acknowledgement, explain the response programme, signal credible recovery, end with 3 commitments. Avoid speculative language. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'},
        {'instr':'', 'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. regulator clock active. Here is exactly what I need from you. Build the stakeholder communication map for the NR raw-material spike + OEM contract review. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. known stakeholders. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. RAG table — Red same-day, Amber 24h, Green monitor. Columns: Audience, Channel, Owner, Message Theme, Timing, Risk if Mishandled. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'}
      ], DESC_CHAT,
      promptsID=[
        {'instr':'', 'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. Zava Auto Industries adalah produsen tier-1 komponen otomotif dan ban ASEAN dengan 6 pabrik di Indonesia, Malaysia, dan Thailand yang memasok Toyota, Honda, Hyundai-Kia, Mitsubishi, dan Proton. Harga ... Berikut yang saya butuhkan dari Anda secara persis. Bingkai situasi NR raw-material spike + OEM contract review dalam bahasa sederhana untuk Direktur Utama Grup. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. catatan saya dari rapat krisis pagi. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. nota 1 halaman dengan bagian — Headline, Apa yang Terjadi, Posisi Pemangku Kepentingan, 5 Pertanyaan Direksi, 3 Keputusan Direktur Utama dalam 48 Jam. Nada: tenang, presisi, hindari jargon industri. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'},
        {'instr':'', 'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. Audiens ExCo internal + pemangku kepentingan eksternal kunci. Berikut yang saya butuhkan dari Anda secara persis. Pembukaan lisan 90 detik untuk briefing pemangku kepentingan Zava Auto Industries. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. hanya fakta yang sudah dipublikasi. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. Buka dengan pengakuan, jelaskan program respons, beri sinyal pemulihan kredibel, akhiri dengan 3 komitmen. Hindari bahasa spekulatif. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'},
        {'instr':'', 'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. clock regulator aktif. Berikut yang saya butuhkan dari Anda secara persis. Bangun peta komunikasi pemangku kepentingan untuk NR raw-material spike + OEM contract review. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. pemangku kepentingan yang dikenal. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. tabel RAG — Merah hari ini juga, Kuning 24 jam, Hijau pantau. Kolom: Audiens, Channel, Pemilik, Tema Pesan, Timing, Risiko bila Keliru. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'}
      ],
      persona=['Sasha Ouellet','Mod Admin','Hadar Caspit'],
      personaID=['Sasha Ouellet','Mod Admin','Hadar Caspit']),

      tool(T_RESEARCHER, M365_LIC, M365_ACCT, [
        {'instr':'Open `m365.cloud.microsoft/chat` > Agents > **Researcher** > **Critique Mode**. Paste the prompt below.',
         'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. Zava Auto Industries must respond to its regulator imminently. Here is exactly what I need from you. Benchmark how peers (Gajah Tunggal, Goodyear Indonesia, Sime Darby Industrial, APM Automotive, MBM Resources) handled comparable NR raw-material spike + OEM contract review events between 2020 and 2025. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. peer disclosures, regulator filings, industry press. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. For each peer, identify trigger, response timeline, programme adopted, share-price recovery 12 months later. Critique each source. Cite all with publication date. Output as comparison table. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'},
        {'instr':'Open `m365.cloud.microsoft/chat` > Agents > **Researcher** > **Model Council**. Paste the prompt below.',
         'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. must protect regulator standing AND customer trust AND financial position concurrently. Here is exactly what I need from you. 3 most defensible response playbooks for Zava Auto Industries hit by NR raw-material spike + OEM contract review. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. Researcher Model Council — convene parallel reports from GPT and Claude. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. Surface dissent, mark majority and minority views. Comparison table: Playbook, Council Verdict, Dissenting View, ASEAN Precedent, Implementation Risk. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'}
      ], DESC_RESEARCHER,
      promptsID=[
        {'instr':'Buka `m365.cloud.microsoft/chat` > Agents > **Researcher** > **Critique Mode**. Tempel prompt.',
         'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. Zava Auto Industries harus respons ke regulator segera. Berikut yang saya butuhkan dari Anda secara persis. Benchmark bagaimana peer (Gajah Tunggal, Goodyear Indonesia, Sime Darby Industrial, APM Automotive, MBM Resources) menangani peristiwa NR raw-material spike + OEM contract review sebanding antara 2020 hingga 2025. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. pengungkapan peer, filing regulator, pers industri. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. Untuk tiap peer identifikasi pemicu, timeline respons, program yang diadopsi, pemulihan harga saham 12 bulan kemudian. Kritisi tiap sumber. Cantumkan kutipan lengkap dengan tanggal. Hasilkan tabel perbandingan. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'},
        {'instr':'Buka `m365.cloud.microsoft/chat` > Agents > **Researcher** > **Model Council**. Tempel prompt.',
         'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. harus melindungi posisi regulator DAN kepercayaan customer DAN posisi finansial sekaligus. Berikut yang saya butuhkan dari Anda secara persis. 3 playbook respons paling defensible untuk Zava Auto Industries yang terkena NR raw-material spike + OEM contract review. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. Model Council — gelar laporan paralel dari GPT dan Claude. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. Sorot perbedaan pendapat, tandai mayoritas dan minoritas. Tabel perbandingan: Playbook, Putusan Council, Pandangan Minoritas, Preseden ASEAN, Risiko Implementasi. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'}
      ],
      persona=['Mod Admin','Mod Admin'],
      personaID=['Mod Admin','Mod Admin']),

      tool(T_ANALYST, M365_LIC, M365_ACCT, [
        {'instr':'Open `m365.cloud.microsoft/chat` > Agents > **Analyst**. Upload /AUTO_01_Raw_Material_Cost_Model.xlsx AND /AUTO_02_OEM_Contract_Matrix.xlsx. Paste the prompt below.',
         'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. Group ExCo needs an evidence-based view in 48 hours. Here is exactly what I need from you. Quantify the NR raw-material spike + OEM contract review financial and operational impact. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. the 2 uploaded files. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. (1) RAG bar chart of at-risk items by severity; (2) waterfall of MYR EBITDA impact; (3) tracker by stakeholder/segment, flag worst <10% headroom as Red. Output a Board-ready RAG dashboard. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'}
      ], DESC_ANALYST,
      promptsID=[
        {'instr':'Buka `m365.cloud.microsoft/chat` > Agents > **Analyst**. Unggah /AUTO_01_Raw_Material_Cost_Model.xlsx DAN /AUTO_02_OEM_Contract_Matrix.xlsx. Tempel prompt.',
         'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. ExCo Grup butuh pandangan berbasis bukti dalam 48 jam. Berikut yang saya butuhkan dari Anda secara persis. Kuantifikasi dampak finansial dan operasional dari NR raw-material spike + OEM contract review. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. 2 file yang diunggah. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. (1) Bar chart RAG item at-risk berdasarkan severity; (2) waterfall dampak EBITDA RM; (3) tracker per stakeholder/segmen, tandai headroom terburuk <10% Merah. Hasilkan dashboard RAG siap-Direksi. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'}
      ],
      persona=['Hadar Caspit'],
      personaID=['Hadar Caspit']),

      tool(T_EXCEL, M365_LIC, M365_ACCT, [
        {'instr':'Open `/AUTO_01_Raw_Material_Cost_Model.xlsx` in Excel for the Web. Open the **Copilot pane**. Paste the prompt below.',
         'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. Audit Committee meets in the next 14 days. Here is exactly what I need from you. Build a single Audit-Committee-ready dashboard sheet. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. combine all relevant tabs. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. New sheet "AC Dashboard" with KPI tiles, bar chart by severity, sparkline column. RAG conditional formatting. Do not modify source tabs. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'}
      ], '',
      promptsID=[
        {'instr':'Buka `/AUTO_01_Raw_Material_Cost_Model.xlsx` di Excel for the Web. Buka **Copilot pane**. Tempel prompt.',
         'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. Komite Audit rapat dalam 14 hari ke depan. Berikut yang saya butuhkan dari Anda secara persis. Bangun satu sheet dashboard siap-Komite Audit. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. gabungkan semua tab yang relevan. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. Sheet baru "AC Dashboard" dengan KPI tile, bar chart per severity, kolom sparkline. Format kondisional RAG. Jangan modifikasi tab sumber. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'}
      ],
      persona=['Hadar Caspit'],
      personaID=['Hadar Caspit']),

      tool(T_WORD, M365_LIC, M365_ACCT, [
        {'instr':'Open a new blank Word doc in Word for the Web. Open the **Copilot pane**. Reference /AUTO_03_OEM_Customer_Letter_Pack.docx and /AUTO_04_Margin_Recovery_Plan.docx using `/`. Paste the prompt below.',
         'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. NR raw-material spike + OEM contract review active. Here is exactly what I need from you. Draft the regulator-grade response brief (4 pages). Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. the referenced docs + my notes. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. Sections — Material Facts, Current Status, Programme, Financial Impact Range, Forward-Looking Statements with explicit risk language. Tone: factual, regulator-grade, no speculation. Cite source files at the end of each section. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'}
      ], DESC_WORD,
      promptsID=[
        {'instr':'Buka dokumen Word baru kosong di Word for the Web. Buka **Copilot pane**. Referensikan /AUTO_03_OEM_Customer_Letter_Pack.docx dan /AUTO_04_Margin_Recovery_Plan.docx menggunakan `/`. Tempel prompt.',
         'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. NR raw-material spike + OEM contract review aktif. Berikut yang saya butuhkan dari Anda secara persis. Susun brief respons regulator-grade (4 halaman). Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. dokumen yang direferensikan + catatan saya. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. Bagian — Fakta Material, Status Saat Ini, Program, Rentang Dampak Finansial, Pernyataan Forward-Looking dengan bahasa risiko eksplisit. Nada: faktual, regulator-grade, tanpa spekulasi. Kutip file sumber di akhir tiap bagian. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'}
      ],
      persona=['Hadar Caspit'],
      personaID=['Hadar Caspit']),

      tool(T_PPT, M365_LIC, M365_ACCT, [
        {'instr':'Open a new PowerPoint deck in PowerPoint for the Web. Open the **Copilot pane**. Paste the prompt below.',
         'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. AC in 14 days. Here is exactly what I need from you. 8-slide Audit Committee deck on NR raw-material spike + OEM contract review. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. my brief draft and dashboard. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. Cover; Situation; Status (RAG); Programme (2 slides); Financial Impact; Stakeholder Map; Decisions Requested. Brand colours #52525B + #0F1C3F, 1 chart per slide. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'}
      ], DESC_PPT,
      promptsID=[
        {'instr':'Buka deck PowerPoint baru di PowerPoint for the Web. Buka **Copilot pane**. Tempel prompt.',
         'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. KA dalam 14 hari. Berikut yang saya butuhkan dari Anda secara persis. Deck 8 slide Komite Audit tentang NR raw-material spike + OEM contract review. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. draf brief dan dashboard saya. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. Cover; Situasi; Status (RAG); Program (2 slide); Dampak Finansial; Peta Pemangku Kepentingan; Keputusan yang Diminta. Warna brand #52525B + #0F1C3F, 1 chart per slide. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'}
      ],
      persona=['Sasha Ouellet'],
      personaID=['Sasha Ouellet']),

      tool(T_OUTLOOK, M365_LIC, M365_ACCT, [
        {'instr':'Open Outlook on the Web. Open the email thread "NR raw-material spike + OEM contract review — Group CFO follow-up". Click the **Copilot icon**. Paste the prompt below.',
         'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. NR raw-material spike + OEM contract review active. Here is exactly what I need from you. Draft a single email to the Zava Auto Industries ExCo and the relevant operating heads. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. the email thread above and the response programme. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. Subject line, 4 short paragraphs covering — situation, the 3 actions each operating head must complete in 72 hours, the regulator-engagement workstream, the AC date. Tone: firm, supportive, accountable. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'}
      ], DESC_OUTLOOK,
      promptsID=[
        {'instr':'Buka Outlook on the Web. Buka thread email "NR raw-material spike + OEM contract review — tindak lanjut Direktur Keuangan Grup". Klik **ikon Copilot**. Tempel prompt.',
         'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. NR raw-material spike + OEM contract review aktif. Berikut yang saya butuhkan dari Anda secara persis. Susun satu email ke ExCo Zava Auto Industries dan kepala operasi yang relevan. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. thread di atas dan program respons. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. Baris subjek, 4 paragraf pendek — situasi, 3 aksi per kepala operasi dalam 72 jam, workstream engagement regulator, tanggal KA. Nada: tegas, suportif, akuntabel. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'}
      ],
      persona=['Hadar Caspit'],
      personaID=['Hadar Caspit']),

      tool(T_TEAMS, M365_LIC, M365_ACCT, 
        [
          {'instr':"**(1) In Teams**, open **Calendar** → click the past meeting **\"New Software Implementation\"**. On the Recap page, walk the audience through the **AI Notes** (auto-summary), the **Custom summary** (Copilot's per-attendee view), and the **Audio recap** (chapter markers with speaker timings). **(2) In Word for the Web**, open a **new blank document**. Type a minutes template at the top — five empty headings: Date and Attendees · Agenda Items · Decisions Taken · Action Items · Risks and Open Questions. **(3) Click the Copilot icon** in the Word ribbon and paste the prompt below — Copilot in Word will reference the meeting recap by name with `/` and fill the template.", 'prompt':"Create meeting minutes for the Teams meeting /New Software Implementation. Use the empty template already on this page and fill each heading from the meeting recap. Sections: (1) Date and Attendees; (2) Agenda Items; (3) Decisions Taken; (4) Action Items with Owner and Due Date; (5) Risks and Open Questions. Quote attendee statements verbatim where the wording matters. Tag any decision that is on the critical path as Critical Path. Save the file as Minutes_New_Software_Implementation.docx in OneDrive."},
          {'instr':'**(1) In Teams**, open **Calendar** → click the past meeting **"Marketing Campaign Performance Review"**. On the Recap page, walk through the **AI Notes**, the **Custom summary**, and the **Audio recap** chapters. **(2) In Word for the Web**, open a **new blank document**. Type a campaign-review minutes template at the top — six empty headings: Date and Attendees · Campaign KPIs Reviewed · Decisions Taken · Action Items · Budget Reallocations · Next Review Date. **(3) Click the Copilot icon** in the Word ribbon and paste the prompt below.', 'prompt':"Create meeting minutes for the Teams meeting /Marketing Campaign Performance Review. Use the empty campaign-review template already on this page. Sections: (1) Date and Attendees; (2) Campaign KPIs Reviewed; (3) Decisions Taken; (4) Action Items with Owner and Due Date; (5) Budget Reallocations Approved; (6) Next Review Date. Quote attendee statements verbatim where the wording matters. Highlight any KPI that missed target by more than 10% in amber. Save the file as Minutes_Marketing_Campaign_Review.docx in OneDrive."},
          {'instr':'**(1) In Teams**, open **Calendar** → click the past meeting **"Negotiating Marketing Contract"**. On the Recap page, walk through the **AI Notes**, the **Custom summary**, and the **Audio recap**. **(2) In Word for the Web**, open a **new blank document**. Type a vendor-negotiation minutes template at the top — seven empty headings: Vendor and Owner · Commercial Terms Discussed · Concessions Offered · Concessions Accepted · Open Items · Approval Thresholds · Next Steps. **(3) Click the Copilot icon** in the Word ribbon and paste the prompt below — then forward the result to Procurement, Legal, and the Group CFO.', 'prompt':"Create meeting minutes for the Teams meeting /Negotiating Marketing Contract. Use the empty vendor-negotiation template already on this page. Sections: (1) Vendor and Owner; (2) Commercial Terms Discussed; (3) Concessions Offered; (4) Concessions Accepted; (5) Open Items; (6) Approval Thresholds (CFO / Board); (7) Next Steps with Owner and Due Date. Highlight any term requiring CFO sign-off in amber and any term requiring Board sign-off in red. Save the file as Minutes_Marketing_Contract_Negotiation.docx in OneDrive and email the link to Procurement, Legal, and the Group CFO."}
        ], DESC_TEAMS,
        promptsID=[
          {'instr':'**(1) Di Teams**, buka **Calendar** → klik rapat **"New Software Implementation"**. Di halaman Recap, jelaskan ke peserta tentang **AI Notes** (ringkasan otomatis), **Custom summary** (tampilan per-peserta dari Copilot), dan **Audio recap** (penanda bab dengan timing pembicara). **(2) Di Word for the Web**, buka **dokumen kosong baru**. Ketik kerangka notulen di bagian atas — lima heading kosong: Tanggal dan Peserta · Agenda · Keputusan · Action Items · Risiko dan Pertanyaan Terbuka. **(3) Klik ikon Copilot** di ribbon Word lalu tempelkan prompt di bawah — Copilot in Word akan merujuk recap rapat dengan `/` dan mengisi template.', 'prompt':"Susun notulen rapat untuk rapat Teams /New Software Implementation. Gunakan template kosong yang sudah ada di halaman ini dan isi tiap heading dari recap rapat. Bagian: (1) Tanggal dan Peserta; (2) Agenda; (3) Keputusan; (4) Action Items dengan Owner dan Due Date; (5) Risiko dan Pertanyaan Terbuka. Kutip pernyataan peserta apa adanya bila kata-katanya penting. Tandai keputusan di jalur kritis sebagai Critical Path. Simpan file sebagai Minutes_New_Software_Implementation.docx di OneDrive."},
          {'instr':'**(1) Di Teams**, buka **Calendar** → klik rapat **"Marketing Campaign Performance Review"**. Di halaman Recap, jelaskan **AI Notes**, **Custom summary**, dan **Audio recap**. **(2) Di Word for the Web**, buka dokumen kosong baru. Ketik kerangka notulen tinjauan kampanye — enam heading kosong: Tanggal dan Peserta · KPI Kampanye yang Dikaji · Keputusan · Action Items · Realokasi Anggaran · Jadwal Tinjauan Berikutnya. **(3) Klik ikon Copilot** di ribbon Word lalu tempelkan prompt di bawah.', 'prompt':"Susun notulen rapat untuk rapat Teams /Marketing Campaign Performance Review. Gunakan template kosong tinjauan kampanye yang sudah ada. Bagian: (1) Tanggal dan Peserta; (2) KPI Kampanye yang Dikaji; (3) Keputusan; (4) Action Items dengan Owner dan Due Date; (5) Realokasi Anggaran yang Disetujui; (6) Jadwal Tinjauan Berikutnya. Kutip pernyataan peserta apa adanya. Tandai KPI yang meleset >10% dengan amber. Simpan sebagai Minutes_Marketing_Campaign_Review.docx di OneDrive."},
          {'instr':'**(1) Di Teams**, buka **Calendar** → klik rapat **"Negotiating Marketing Contract"**. Di halaman Recap, jelaskan **AI Notes**, **Custom summary**, dan **Audio recap**. **(2) Di Word for the Web**, buka dokumen kosong baru. Ketik kerangka notulen negosiasi vendor — tujuh heading kosong: Vendor dan Owner · Term Komersial · Konsesi yang Ditawarkan · Konsesi yang Diterima · Item Terbuka · Threshold Persetujuan · Langkah Berikutnya. **(3) Klik ikon Copilot** di ribbon Word lalu tempelkan prompt di bawah — kemudian teruskan hasilnya ke Procurement, Legal, dan Direktur Keuangan Grup.', 'prompt':"Susun notulen rapat untuk rapat Teams /Negotiating Marketing Contract. Gunakan template kosong negosiasi vendor yang sudah ada. Bagian: (1) Vendor dan Owner; (2) Term Komersial; (3) Konsesi yang Ditawarkan; (4) Konsesi yang Diterima; (5) Item Terbuka; (6) Threshold Persetujuan (CFO / Direksi); (7) Langkah Berikutnya dengan Owner dan Due Date. Tandai term yang memerlukan persetujuan CFO dengan amber dan persetujuan Direksi dengan merah. Simpan sebagai Minutes_Marketing_Contract_Negotiation.docx di OneDrive lalu email link-nya ke Procurement, Legal, dan Direktur Keuangan Grup."}
        ],
        promptsBM=[
          {'instr':'**(1) Di Teams**, buka **Calendar** → klik mesyuarat **"New Software Implementation"**. Pada halaman Recap, terangkan kepada hadirin tentang **AI Notes** (ringkasan automatik), **Custom summary** (paparan per-hadirin dari Copilot), dan **Audio recap** (penanda bab dengan masa pembicara). **(2) Di Word for the Web**, buka **dokumen kosong baharu**. Taip rangka minit di bahagian atas — lima tajuk kosong: Tarikh dan Hadirin · Agenda · Keputusan · Tindakan · Risiko dan Soalan Terbuka. **(3) Klik ikon Copilot** di ribbon Word dan tampal prompt di bawah — Copilot in Word akan merujuk recap mesyuarat dengan `/` dan mengisi templat.', 'prompt':"Hasilkan minit mesyuarat untuk mesyuarat Teams /New Software Implementation. Gunakan templat kosong yang sudah ada di halaman ini dan isi setiap tajuk daripada recap mesyuarat. Bahagian: (1) Tarikh dan Hadirin; (2) Agenda; (3) Keputusan; (4) Tindakan dengan Pemilik dan Tarikh; (5) Risiko dan Soalan Terbuka. Petik kenyataan hadirin sebagaimana asal di mana perkataannya penting. Tandakan sebarang keputusan di laluan kritikal sebagai Critical Path. Simpan fail sebagai Minutes_New_Software_Implementation.docx di OneDrive."},
          {'instr':'**(1) Di Teams**, buka **Calendar** → klik mesyuarat **"Marketing Campaign Performance Review"**. Pada halaman Recap, terangkan **AI Notes**, **Custom summary**, dan **Audio recap**. **(2) Di Word for the Web**, buka dokumen kosong baharu. Taip rangka minit ulasan kempen — enam tajuk kosong: Tarikh dan Hadirin · KPI Kempen yang Diulas · Keputusan · Tindakan · Pelarasan Bajet · Tarikh Ulasan Berikutnya. **(3) Klik ikon Copilot** di ribbon Word dan tampal prompt di bawah.', 'prompt':"Hasilkan minit mesyuarat untuk mesyuarat Teams /Marketing Campaign Performance Review. Gunakan templat kosong ulasan kempen yang sudah ada. Bahagian: (1) Tarikh dan Hadirin; (2) KPI Kempen yang Diulas; (3) Keputusan; (4) Tindakan dengan Pemilik dan Tarikh; (5) Pelarasan Bajet yang Diluluskan; (6) Tarikh Ulasan Berikutnya. Petik kenyataan hadirin sebagaimana asal. Tandakan KPI yang tersasar >10% dengan amber. Simpan sebagai Minutes_Marketing_Campaign_Review.docx di OneDrive."},
          {'instr':'**(1) Di Teams**, buka **Calendar** → klik mesyuarat **"Negotiating Marketing Contract"**. Pada halaman Recap, terangkan **AI Notes**, **Custom summary**, dan **Audio recap**. **(2) Di Word for the Web**, buka dokumen kosong baharu. Taip rangka minit perundingan vendor — tujuh tajuk kosong: Vendor dan Pemilik · Terma Komersial · Konsesi Ditawarkan · Konsesi Diterima · Item Terbuka · Ambang Kelulusan · Langkah Seterusnya. **(3) Klik ikon Copilot** di ribbon Word dan tampal prompt di bawah — kemudian majukan hasilnya kepada Procurement, Legal dan Pengarah Kewangan Kumpulan.', 'prompt':"Hasilkan minit mesyuarat untuk mesyuarat Teams /Negotiating Marketing Contract. Gunakan templat kosong perundingan vendor yang sudah ada. Bahagian: (1) Vendor dan Pemilik; (2) Terma Komersial; (3) Konsesi Ditawarkan; (4) Konsesi Diterima; (5) Item Terbuka; (6) Ambang Kelulusan (CFO / Lembaga); (7) Langkah Seterusnya dengan Pemilik dan Tarikh. Tandakan terma yang memerlukan kelulusan CFO dengan amber dan Lembaga dengan merah. Simpan sebagai Minutes_Marketing_Contract_Negotiation.docx di OneDrive dan e-mel pautan kepada Procurement, Legal dan Pengarah Kewangan Kumpulan."}
        ],
        persona=['Sasha Ouellet', 'Sasha Ouellet', 'Sasha Ouellet'],
        personaID=['Sasha Ouellet', 'Sasha Ouellet', 'Sasha Ouellet']
      ),

      tool(T_NOTEBOOK, M365_LIC, M365_ACCT, [
        {'instr':'All sources are loaded. Type the prompt below in the notebook chat.',
         'prompt':'Synthesise across all sources to produce a 10-bullet Audit Committee narrative. Cover: NR raw-material spike + OEM contract review status, programme, financial impact, stakeholder map, decisions requested. Cite the source file at the end of every bullet.'},
        {'instr':'Click **Quick Create** > **Audio Overview** to generate a 6-minute briefing podcast.',
         'prompt':'Quick Create: Audio Overview, 6 minutes, formal narration tone, focused on the AC narrative above. Listeners are the Zava Auto Industries operating heads preparing for tomorrow morning huddles.'}
      ], DESC_NOTEBOOK,
      promptsID=[
        {'instr':'Semua sumber sudah dimuat. Ketik prompt di bawah pada chat notebook.',
         'prompt':'Sintesakan dari semua sumber untuk menghasilkan narasi Komite Audit 10-bullet. Cakup: status NR raw-material spike + OEM contract review, program, dampak finansial, peta pemangku kepentingan, keputusan yang diminta. Kutip file sumber di akhir tiap bullet.'},
        {'instr':'Klik **Quick Create** > **Audio Overview** untuk menghasilkan podcast briefing 6 menit.',
         'prompt':'Quick Create: Audio Overview, 6 menit, gaya narasi formal, fokus pada narasi KA di atas. Pendengar adalah kepala operasi Zava Auto Industries yang menyiapkan huddle pagi besok.'}
      ],
      persona=['Mod Admin','Mod Admin'],
      personaID=['Mod Admin','Mod Admin'],
      notebookMeta={
        'sources':['/AUTO_01_Raw_Material_Cost_Model.xlsx', '/AUTO_02_OEM_Contract_Matrix.xlsx', '/AUTO_03_OEM_Customer_Letter_Pack.docx', '/AUTO_04_Margin_Recovery_Plan.docx', '/AUTO_05_Steerco_Briefing.docx'],
        'instructions':'You are the Group CFO of Zava Auto Industries preparing an Audit Committee pack on NR raw-material spike + OEM contract review. Always cite the source file and tab/section. Tone: precise, regulator-grade, no speculation. Use MYR for the Group totals (1 MYR ≈ 3,580 IDR).',
        'instructionsID':'Anda adalah Direktur Keuangan Grup Zava Auto Industries yang menyiapkan paket Komite Audit untuk NR raw-material spike + OEM contract review. Selalu kutip file sumber dan tab/bagian. Nada: presisi, regulator-grade, tanpa spekulasi. Gunakan MYR untuk total Grup (1 MYR ≈ 3.580 IDR).'
      }),

      tool(T_COWORK, FRONTIER_LIC, M365_ACCT, [
        {'instr':'Open `m365.cloud.microsoft` > Agents > **Cowork**. Paste the single prompt below — Cowork delegates 5 parallel sub-tasks. Frontier required.',
         'prompt':'Cowork — OEM Pass-Through 10-Day Sprint. Run these in parallel: (1) 📝 Draft Word — regulator response brief 4 pages, source /AUTO_01_Raw_Material_Cost_Model.xlsx, /AUTO_02_OEM_Contract_Matrix.xlsx, /AUTO_03_OEM_Customer_Letter_Pack.docx, /AUTO_04_Margin_Recovery_Plan.docx, /AUTO_05_Steerco_Briefing.docx. (2) 📝 Draft Word — internal ExCo briefing memo 2 pages, same sources. (3) ✉️ Send email to Zava Auto Industries ExCo and operating heads with the 3 actions in 72h. (4) 📅 Schedule 90-min AC Pre-Read tomorrow 8am MYT. (5) 💬 Post Teams message to #group-exco with one-line headline + dashboard link. Use these named recipients consistently across the email task and the Teams meeting task — Hadar (Group CFO), Sasha (Group Chief of Staff), Daichi (Head of Investor Relations), Sonia (Head of Strategy), Will (Head of Risk) and Omar (Head of Procurement) — and adapt the precise distribution per sub-task to keep each communication focused on the right audience.'}
      ], DESC_COWORK,
      promptsID=[
        {'instr':'Buka `m365.cloud.microsoft` > Agents > **Cowork**. Tempel prompt tunggal — Cowork mendelegasikan 5 sub-tugas paralel. Frontier diperlukan.',
         'prompt':'Cowork — OEM Pass-Through 10-Day Sprint. Jalankan paralel: (1) 📝 Susun Word — brief respons regulator 4 halaman, sumber /AUTO_01_Raw_Material_Cost_Model.xlsx, /AUTO_02_OEM_Contract_Matrix.xlsx, /AUTO_03_OEM_Customer_Letter_Pack.docx, /AUTO_04_Margin_Recovery_Plan.docx, /AUTO_05_Steerco_Briefing.docx. (2) 📝 Susun Word — memo briefing ExCo internal 2 halaman, sumber sama. (3) ✉️ Kirim email ke ExCo Zava Auto Industries dan kepala operasi dengan 3 aksi dalam 72 jam. (4) 📅 Jadwalkan AC Pre-Read 90 menit besok 08:00 WIB. (5) 💬 Posting pesan Teams di #group-exco dengan headline satu baris + tautan dashboard. Use these named recipients consistently across the email task and the Teams meeting task — Hadar (Group CFO), Sasha (Group Chief of Staff), Daichi (Head of Investor Relations), Sonia (Head of Strategy), Will (Head of Risk) and Omar (Head of Procurement) — and adapt the precise distribution per sub-task to keep each communication focused on the right audience.'}
      ],
      persona=['Mod Admin'],
      personaID=['Mod Admin']),

      tool(T_WORD_AGT, ANY_LIC, ANY_ACCT, [
        {'instr':'Open `m365.cloud.microsoft/chat` → Agents tab → **Word Agent**. Paste the prompt below — the agent returns a fully drafted .docx.',
         'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. NR raw-material spike + OEM contract review. Here is exactly what I need from you. Generate a 4-page CFO Crisis Brief in Word. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. /AUTO_01_Raw_Material_Cost_Model.xlsx AND /AUTO_02_OEM_Contract_Matrix.xlsx. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. Sections — Executive Summary 5 bullets; Current Status; Programme; Financial Impact; Stakeholder Map; Decisions requested. Tone: precise, regulator-grade. Save as OEM_PassThrough_Brief.docx. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'}
      ], DESC_WORD_AGT,
      promptsID=[
        {'instr':'Buka `m365.cloud.microsoft/chat` → tab Agents → **Word Agent**. Tempel prompt — agent mengembalikan .docx yang sudah didraf penuh.',
         'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. NR raw-material spike + OEM contract review. Berikut yang saya butuhkan dari Anda secara persis. Hasilkan Brief Krisis Direktur Keuangan 4 halaman dalam Word. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. /AUTO_01_Raw_Material_Cost_Model.xlsx DAN /AUTO_02_OEM_Contract_Matrix.xlsx. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. Bagian — Ringkasan Eksekutif 5 bullet; Status Saat Ini; Program; Dampak Finansial; Peta Pemangku Kepentingan; Keputusan yang diminta. Nada: presisi, regulator-grade. Simpan sebagai Brief_PassThrough_OEM.docx. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'}
      ],
      persona=['Sasha Ouellet'],
      personaID=['Sasha Ouellet']),

      tool(T_PPT_AGT, ANY_LIC, ANY_ACCT, [
        {'instr':'Open `m365.cloud.microsoft/chat` → Agents tab → **PowerPoint Agent**. Paste the prompt below.',
         'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. AC in 14 days. Here is exactly what I need from you. 8-slide Audit Committee deck on NR raw-material spike + OEM contract review. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. /OEM_PassThrough_Brief.docx and /AUTO_01_Raw_Material_Cost_Model.xlsx. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. Cover; Situation; Status RAG; Programme (2); Financial Impact; Stakeholder Map; Decisions. Brand #52525B + #0F1C3F, 1 chart/slide. Save as OEM_Steerco_Deck.pptx. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'}
      ], DESC_PPT_AGT,
      promptsID=[
        {'instr':'Buka `m365.cloud.microsoft/chat` → tab Agents → **PowerPoint Agent**. Tempel prompt.',
         'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. KA dalam 14 hari. Berikut yang saya butuhkan dari Anda secara persis. Deck 8 slide Komite Audit tentang NR raw-material spike + OEM contract review. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. /Brief_PassThrough_OEM.docx dan /AUTO_01_Raw_Material_Cost_Model.xlsx. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. Cover; Situasi; Status RAG; Program (2); Dampak Finansial; Peta Pemangku Kepentingan; Keputusan. Brand #52525B + #0F1C3F, 1 chart/slide. Simpan sebagai Deck_Steerco_OEM.pptx. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'}
      ],
      persona=['Sasha Ouellet'],
      personaID=['Sasha Ouellet']),

      tool(T_XL_AGT, ANY_LIC, ANY_ACCT, [
        {'instr':'Open `m365.cloud.microsoft/chat` → Agents tab → **Excel Agent**. Paste the prompt below.',
         'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. Operating tracker for the Group COO. Here is exactly what I need from you. Build a NR raw-material spike + OEM contract review response control tracker workbook. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. schema only. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. Sheet 1 Issue Log, Sheet 2 Programme Milestones, Sheet 3 Cost Tracker, Sheet 4 Dashboard with KPI tiles + RAG conditional formatting. Save as OEM_PassThrough_Tracker.xlsx. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'}
      ], DESC_XL_AGT,
      promptsID=[
        {'instr':'Buka `m365.cloud.microsoft/chat` → tab Agents → **Excel Agent**. Tempel prompt.',
         'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. tracker operasi untuk Direktur Operasional Grup. Berikut yang saya butuhkan dari Anda secara persis. Bangun workbook tracker kendali respons NR raw-material spike + OEM contract review. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. hanya skema. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. Sheet 1 Log Isu, Sheet 2 Milestone Program, Sheet 3 Tracker Biaya, Sheet 4 Dashboard dengan KPI tile + format kondisional RAG. Simpan sebagai Tracker_PassThrough_OEM.xlsx. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'}
      ],
      persona=['Hadar Caspit'],
      personaID=['Hadar Caspit']),

      tool_builder(M365_LIC, M365_ACCT,
        agents=[
        {
          'icon': '🛞',
          'label': 'Plant OEE Coach',
          'name': 'Zava Auto Components & Tyres — Plant OEE Coach',
          'desc': 'Optimises Auto Components & Tyres OEE by line, shift, and SKU, and surfaces yield-loss drivers.',
          'instructions': 'You are the Zava Auto Components & Tyres Plant OEE Coach. You support the Plant Director. Monitor plant OEE (AUTO_01_Raw_Material_Cost_Model.xlsx) and downtime logs (AUTO_02_OEM_Contract_Matrix.xlsx) for OEE deterioration, root-cause clusters, and intervention candidates. Recommend a maintenance, process, or operational action per cluster.',
          'knowledge': [
            {'file':'AUTO_01_Raw_Material_Cost_Model.xlsx', 'note':'OEE by line, shift, SKU.'},
            {'file':'AUTO_02_OEM_Contract_Matrix.xlsx', 'note':'Downtime logs.'},
            {'file':'AUTO_04_Margin_Recovery_Plan.docx', 'note':'Maintenance plan and CAPA register.'}
          ],
          'knowledgeNote': 'Test: "Which 3 lines at Auto Components & Tyres have the worst OEE drag this month?"',
          'queries': [
            'Top 10 OEE-loss line/shift/SKU — recommended actions.',
            'Which downtime causes are recurring across plants? Recommend cross-plant corrective programme.',
            'Draft the monthly Plant Performance review.'
          ],
        },
        {
          'icon': '🤝',
          'label': 'OEM Account Coach',
          'name': 'Zava Auto Components & Tyres — OEM Account Coach',
          'desc': 'Helps Auto Components & Tyres OEM-account managers track program ramps, PPAP status, and quality-incident closure.',
          'instructions': 'You are the Zava Auto Components & Tyres OEM Account Coach. You support the Sales Director. Track program ramps (AUTO_03_OEM_Customer_Letter_Pack.docx), PPAP status, and OEM quality-incident logs (AUTO_05_Steerco_Briefing.docx). Recommend customer escalations, ramp acceleration, or quality CAPA per incident.',
          'knowledge': [
            {'file':'AUTO_03_OEM_Customer_Letter_Pack.docx', 'note':'Programme ramps and forecasts.'},
            {'file':'AUTO_05_Steerco_Briefing.docx', 'note':'OEM quality-incident log.'}
          ],
          'knowledgeNote': 'Test: "Which OEM programme at Auto Components & Tyres has the worst PPAP slippage?"',
          'queries': [
            'Top 5 OEM programmes by PPAP-slippage — recommended action per programme.',
            'Which OEM quality incidents remain open beyond 30 days? Build a CAPA tracker.',
            'Draft the monthly OEM Account Review for the largest customer.'
          ],
        },
        {
          'icon': '🏛️',
          'label': 'JKKP / Disnaker',
          'name': 'Zava Auto Components & Tyres — Industrial Regulator Liaison',
          'desc': 'Prepares JKKP (MY) / Disnaker (ID) safety, OSH, and type-approval filings for Auto Components & Tyres.',
          'instructions': 'You are the Zava Auto Components & Tyres Industrial Regulator Liaison. You support Government Relations. Prepare OSH, environmental, and type-approval filings grounded on the regulatory file (AUTO_04_Margin_Recovery_Plan.docx) and the policy handbook (AUTO_05_Steerco_Briefing.docx). Quote every clause.',
          'knowledge': [
            {'file':'AUTO_04_Margin_Recovery_Plan.docx', 'note':'Industrial regulatory returns.'}
          ],
          'knowledgeNote': 'Test: "Draft the response to JKKP\'s latest workplace-safety circular for Auto Components & Tyres."',
          'queries': [
            "Prepare a cover letter for this quarter's OSH return.",
            'Which environmental-permit items are at risk of breach? Recommend mitigation.',
            "Draft the response letter to the regulator's latest notice."
          ],
        }
      ],
        agentsID=[
        {
          'icon': '🛞',
          'label': 'Plant OEE Pelatih',
          'name': 'Zava Auto Components & Tyres — Plant OEE Pelatih',
          'desc': 'Optimises Auto Components & Tyres OEE by line, shift, and SKU, and surfaces yield-loss drivers.',
          'instructions': 'Anda adalah Zava Auto Components & Tyres Plant OEE Pelatih. Anda mendukung the Plant Director. Pantau plant OEE (AUTO_01_Raw_Material_Cost_Model.xlsx) and downtime logs (AUTO_02_OEM_Contract_Matrix.xlsx) for OEE deterioration, root-cause clusters, and intervention candidates. Rekomendasikan a maintenance, process, or operational tindakan per klaster.',
          'knowledge': [
            {'file':'AUTO_01_Raw_Material_Cost_Model.xlsx', 'note':'OEE by line, shift, SKU.'},
            {'file':'AUTO_02_OEM_Contract_Matrix.xlsx', 'note':'Downtime logs.'},
            {'file':'AUTO_04_Margin_Recovery_Plan.docx', 'note':'Maintenance plan and CAPA register.'}
          ],
          'knowledgeNote': 'Test: "Yang mana 3 lines at Auto Components & Tyres have terburuk OEE drag bulan ini?"',
          'queries': [
            '10 teratas OEE-loss line/shift/SKU — recommended actions.',
            'Yang mana downtime causes are recurring across plants? Rekomendasikan cross-plant corrective programme.',
            'Susun the bulanan Plant Performance review.'
          ],
        },
        {
          'icon': '🤝',
          'label': 'OEM Account Pelatih',
          'name': 'Zava Auto Components & Tyres — OEM Account Pelatih',
          'desc': 'Helps Auto Components & Tyres OEM-account managers track program ramps, PPAP status, and quality-incident closure.',
          'instructions': 'Anda adalah Zava Auto Components & Tyres OEM Account Pelatih. Anda mendukung the Sales Director. Lacak program ramps (AUTO_03_OEM_Customer_Letter_Pack.docx), PPAP status, and OEM quality-incident logs (AUTO_05_Steerco_Briefing.docx). Rekomendasikan customer escalations, ramp acceleration, or quality CAPA per incident.',
          'knowledge': [
            {'file':'AUTO_03_OEM_Customer_Letter_Pack.docx', 'note':'Programme ramps and forecasts.'},
            {'file':'AUTO_05_Steerco_Briefing.docx', 'note':'OEM quality-incident log.'}
          ],
          'knowledgeNote': 'Test: "Yang mana OEM programme at Auto Components & Tyres has terburuk PPAP slippage?"',
          'queries': [
            '5 teratas OEM programmes by PPAP-slippage — recommended tindakan per program.',
            'Yang mana OEM quality incidents remain open beyond 30 days? Bangun a CAPA tracker.',
            'Susun the bulanan OEM Account Review for terbesar customer.'
          ],
        },
        {
          'icon': '🏛️',
          'label': 'JKKP / Disnaker',
          'name': 'Zava Auto Components & Tyres — Industrial Regulator Penghubung',
          'desc': 'Prepares JKKP (MY) / Disnaker (ID) safety, OSH, and type-approval filings for Auto Components & Tyres.',
          'instructions': 'Anda adalah Zava Auto Components & Tyres Industrial Regulator Penghubung. Anda mendukung Government Relations. Prepare OSH, environmental, and type-approval filings grounded on the regulatory file (AUTO_04_Margin_Recovery_Plan.docx) and the policy handbook (AUTO_05_Steerco_Briefing.docx). Quote every clause.',
          'knowledge': [
            {'file':'AUTO_04_Margin_Recovery_Plan.docx', 'note':'Industrial regulatory returns.'}
          ],
          'knowledgeNote': 'Test: "Susun the response to JKKP\'s latest workplace-safety circular for Auto Components & Tyres."',
          'queries': [
            "Prepare a cover letter for kuartal ini's OSH return.",
            'Yang mana environmental-permit items are at risk of breach? Rekomendasikan mitigation.',
            "Susun the response letter to the regulator's latest notice."
          ],
        }
      ],
        persona=['Mod Admin', 'Mod Admin', 'Mod Admin'],
        personaID=['Mod Admin', 'Mod Admin', 'Mod Admin']
      ),
    ],
    companyID='Zava Auto Industries',
    taglineID='Lonjakan bahan baku NR + review kontrak Toyota & Hyundai — Steerco dalam 10 hari.',
    scenarioID='Zava Auto Industries adalah produsen tier-1 komponen otomotif dan ban ASEAN dengan 6 pabrik di Indonesia, Malaysia, dan Thailand yang memasok Toyota, Honda, Hyundai-Kia, Mitsubishi, dan Proton. Harga natural-rubber dan synthetic-rubber melonjak 32% dalam 6 minggu mendorong gap EBITDA RM 410 juta di Q4. Toyota dan Hyundai me-review kontrak supply OEM — pricing pass-through diminta keduanya dalam 10 hari. Direktur Keuangan Grup harus memodelkan skenario pass-through bahan baku, menyusun surat customer OEM, brief Steering Committee Grup, dan menyiapkan komunikasi covenant lender. Frame customer riil: grup ini beroperasi serupa dengan Gajah Tunggal, Goodyear Indonesia, Sime Darby Industrial, dan APM Automotive.',
    relevantDepts=['dept-finance','dept-strategy','dept-operations','dept-procurement','dept-risk','dept-legal'],
    personas=[
      {'name':'Hadar Caspit','role':'Group CFO','roleID':'Direktur Keuangan Grup','acct':'admin@ABSx62256373.onmicrosoft.com','lic':'Microsoft 365 Copilot','color':'#1E40AF'},
      {'name':'Sasha Ouellet','role':'Group Chief of Staff','roleID':'Kepala Staf Grup','acct':'SashaO@ABSx62256373.OnMicrosoft.com','lic':'Free \u2014 no Microsoft 365 Copilot license','color':'#7C3AED'},
      {'name':'Mod Admin','role':'Group Strategy Director','roleID':'Direktur Strategi Grup','acct':'admin@ABSx62256373.onmicrosoft.com','lic':'Microsoft 365 Copilot','color':'#059669'},
      {'name':'Daichi Maruyama','role':'Group Sustainability & Risk Director','roleID':'Direktur Keberlanjutan & Risiko Grup','acct':'admin@ABSx62256373.onmicrosoft.com','lic':'Microsoft 365 Copilot','color':'#DC2626'}
    ],
    storyboard=[
      {'ex':1,'title':'Research & Brief','titleID':'Riset & Pengarahan','minutes':18,'mode':'Show & Tell + Hands-on',
       'summary':'Frame the NR raw-material spike + OEM contract review situation and pull peer playbooks before the regulator clock starts ticking.',
       'summaryID':'Bingkai situasi NR raw-material spike + OEM contract review dan tarik playbook peer sebelum clock regulator mulai berdetak.',
       'tasks':[
         {'verb':'Frame the morning question and lock the day priorities','verbID':'Susun pertanyaan pagi dan kunci prioritas hari ini','toolId':T_CHAT,'mode':'Show & Tell'},
         {'verb':'Run an outside-in peer scan and pull proven plays','verbID':'Lakukan pemindaian peer dari luar dan tarik praktik terbaik','toolId':T_RESEARCHER,'mode':'Show & Tell'},
         {'verb':'Generate a board-ready brief straight from chat','verbID':'Hasilkan brief siap-Direksi langsung dari chat','toolId':T_WORD_AGT,'mode':'Hands-on'}]},
      {'ex':2,'title':'Analyse & Decide','titleID':'Analisis & Putuskan','minutes':18,'mode':'Hands-on',
       'summary':'Quantify NR raw-material spike + OEM contract review financial and operational impact; build an AC dashboard.',
       'summaryID':'Kuantifikasi dampak finansial dan operasional NR raw-material spike + OEM contract review; bangun dashboard KA.',
       'tasks':[
         {'verb':'Crunch the numbers and surface the biggest gaps','verbID':'Olah angka dan ungkap celah terbesar','toolId':T_ANALYST,'mode':'Hands-on'},
         {'verb':'Build a single-pane operating dashboard','verbID':'Bangun dashboard operasi satu-halaman','toolId':T_EXCEL,'mode':'Hands-on'},
         {'verb':'Spin up a recurring tracker workbook from chat','verbID':'Buat workbook tracker berulang dari chat','toolId':T_XL_AGT,'mode':'Hands-on'}]},
      {'ex':3,'title':'Communicate & Coordinate','titleID':'Komunikasi & Koordinasi','minutes':18,'mode':'Hands-on',
       'summary':'Brief operating heads, capture the OEM Pass-Through Steerco recap, and assemble the AC deck and regulator response.',
       'summaryID':'Brief kepala operasi, capture recap OEM Pass-Through Steerco, dan rakit deck KA serta respons regulator.',
       'tasks':[
         {'verb':'Draft the stakeholder alignment email','verbID':'Draf email penyelarasan stakeholder','toolId':T_OUTLOOK,'mode':'Hands-on'},
         {'verb':'Recap the meeting and turn it into minutes','verbID':'Recap rapat dan ubah ke notulen','toolId':T_TEAMS,'mode':'Hands-on'},
         {'verb':'Generate a board-ready deck from chat','verbID':'Hasilkan deck siap-Direksi dari chat','toolId':T_PPT_AGT,'mode':'Hands-on'},
         {'verb':'Delegate a 5-task parallel sprint','verbID':'Delegasikan 5-tugas paralel ke Cowork','toolId':T_COWORK,'mode':'Show & Tell'}]},
      {'ex':4,'title':'Build & Scale','titleID':'Bangun & Skala','minutes':15,'mode':'Show & Tell',
       'summary':'Wrap the NR raw-material spike + OEM contract review playbook into a reusable agent for the Zava Auto Industries operating team.',
       'summaryID':'Bungkus playbook NR raw-material spike + OEM contract review ke dalam agent reusable untuk tim operasi Zava Auto Industries.',
       'tasks':[
         {'verb':'Pull every source into one synthesis notebook','verbID':'Tarik semua sumber ke satu notebook sintesis','toolId':T_NOTEBOOK,'mode':'Show & Tell'},
         {'verb':'Wrap the daily workflow into a reusable agent','verbID':'Bungkus alur kerja harian jadi agen yang dapat dipakai ulang','toolId':T_BUILDER,'mode':'Show & Tell'}]}
    ],
    geo='MY'
))


# ╔══════════════════════════════════════════════════════════════════════╗
# ║  6.  SEMICONDUCTOR / E&E                                        ║
# ╚══════════════════════════════════════════════════════════════════════╝
INDUSTRIES_10.append(ind(
    'semiconductor', 'sec-mfg', 'Semiconductor / E&E', '🔌', '#7C3AED', '#5B21B6',
    'Zava Electronics MY',
    'US BIS export-control update — 14 customer SKUs at risk, MITI brief in 7 days.',
    'Zava Electronics MY operates 4 semiconductor assembly-and-test plants in Penang, Kulim and Melaka with hard-disk-drive heads, NAND flash packaging, and IC substrates as the core revenue lines (USD 1.9B FY2025 revenue). The US Bureau of Industry and Security has updated export-control rules adding 14 customer SKUs to the Entity-List exposure register. MITI Malaysia has requested a brief in 7 days. The Group CFO needs a quantified at-risk SKU schedule, customer-by-customer holding lines, US export-counsel guidance memo, capex re-prioritisation, and the Audit Committee narrative. Real customer reference frame: this group operates similarly to Western Digital Penang, Micron, Inari Amertron, ESCATEC, and Pentamaster.',
    ['SEMI_01_BIS_SKU_Exposure.xlsx', 'SEMI_02_Customer_Concentration_Heatmap.xlsx', 'SEMI_03_MITI_Brief_Pack.docx', 'SEMI_04_Capex_Reprioritisation.xlsx', 'SEMI_05_Customer_Holding_Lines.docx'],
    [
      tool(T_CHAT, FREE_LIC, FREE_ACCT, [
        {'instr':'', 'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. Zava Electronics MY operates 4 semiconductor assembly-and-test plants in Penang, Kulim and Melaka with hard-disk-drive heads, NAND flash packaging, and IC substrates as the core revenue lines (USD 1.9... Here is exactly what I need from you. Frame the US BIS export-control update situation in plain English for the Group CEO. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. my notes from the morning crisis call. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. 1-page note with sections — Headline, What Happened, Stakeholder Position, Top 5 Questions the Board Will Ask, 3 Decisions the CEO Must Take in 48 Hours. Tone: calm, precise, no industry jargon. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'},
        {'instr':'', 'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. Audience is internal ExCo + key external stakeholders. Here is exactly what I need from you. 90-second verbal opening for the Zava Electronics MY stakeholder briefing. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. published facts only. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. Open with acknowledgement, explain the response programme, signal credible recovery, end with 3 commitments. Avoid speculative language. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'},
        {'instr':'', 'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. regulator clock active. Here is exactly what I need from you. Build the stakeholder communication map for the US BIS export-control update. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. known stakeholders. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. RAG table — Red same-day, Amber 24h, Green monitor. Columns: Audience, Channel, Owner, Message Theme, Timing, Risk if Mishandled. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'}
      ], DESC_CHAT,
      promptsID=[
        {'instr':'', 'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. Zava Electronics MY mengoperasikan 4 pabrik assembly-and-test semikonduktor di Penang, Kulim, dan Melaka dengan hard-disk-drive heads, NAND flash packaging, dan IC substrates sebagai lini pendapatan i... Berikut yang saya butuhkan dari Anda secara persis. Bingkai situasi US BIS export-control update dalam bahasa sederhana untuk Direktur Utama Grup. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. catatan saya dari rapat krisis pagi. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. nota 1 halaman dengan bagian — Headline, Apa yang Terjadi, Posisi Pemangku Kepentingan, 5 Pertanyaan Direksi, 3 Keputusan Direktur Utama dalam 48 Jam. Nada: tenang, presisi, hindari jargon industri. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'},
        {'instr':'', 'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. Audiens ExCo internal + pemangku kepentingan eksternal kunci. Berikut yang saya butuhkan dari Anda secara persis. Pembukaan lisan 90 detik untuk briefing pemangku kepentingan Zava Electronics MY. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. hanya fakta yang sudah dipublikasi. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. Buka dengan pengakuan, jelaskan program respons, beri sinyal pemulihan kredibel, akhiri dengan 3 komitmen. Hindari bahasa spekulatif. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'},
        {'instr':'', 'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. clock regulator aktif. Berikut yang saya butuhkan dari Anda secara persis. Bangun peta komunikasi pemangku kepentingan untuk US BIS export-control update. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. pemangku kepentingan yang dikenal. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. tabel RAG — Merah hari ini juga, Kuning 24 jam, Hijau pantau. Kolom: Audiens, Channel, Pemilik, Tema Pesan, Timing, Risiko bila Keliru. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'}
      ],
      persona=['Sasha Ouellet','Mod Admin','Hadar Caspit'],
      personaID=['Sasha Ouellet','Mod Admin','Hadar Caspit']),

      tool(T_RESEARCHER, M365_LIC, M365_ACCT, [
        {'instr':'Open `m365.cloud.microsoft/chat` > Agents > **Researcher** > **Critique Mode**. Paste the prompt below.',
         'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. Zava Electronics MY must respond to its regulator imminently. Here is exactly what I need from you. Benchmark how peers (Western Digital Penang, Micron, Inari Amertron, ESCATEC, Pentamaster) handled comparable US BIS export-control update events between 2020 and 2025. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. peer disclosures, regulator filings, industry press. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. For each peer, identify trigger, response timeline, programme adopted, share-price recovery 12 months later. Critique each source. Cite all with publication date. Output as comparison table. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'},
        {'instr':'Open `m365.cloud.microsoft/chat` > Agents > **Researcher** > **Model Council**. Paste the prompt below.',
         'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. must protect regulator standing AND customer trust AND financial position concurrently. Here is exactly what I need from you. 3 most defensible response playbooks for Zava Electronics MY hit by US BIS export-control update. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. Researcher Model Council — convene parallel reports from GPT and Claude. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. Surface dissent, mark majority and minority views. Comparison table: Playbook, Council Verdict, Dissenting View, ASEAN Precedent, Implementation Risk. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'}
      ], DESC_RESEARCHER,
      promptsID=[
        {'instr':'Buka `m365.cloud.microsoft/chat` > Agents > **Researcher** > **Critique Mode**. Tempel prompt.',
         'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. Zava Electronics MY harus respons ke regulator segera. Berikut yang saya butuhkan dari Anda secara persis. Benchmark bagaimana peer (Western Digital Penang, Micron, Inari Amertron, ESCATEC, Pentamaster) menangani peristiwa US BIS export-control update sebanding antara 2020 hingga 2025. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. pengungkapan peer, filing regulator, pers industri. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. Untuk tiap peer identifikasi pemicu, timeline respons, program yang diadopsi, pemulihan harga saham 12 bulan kemudian. Kritisi tiap sumber. Cantumkan kutipan lengkap dengan tanggal. Hasilkan tabel perbandingan. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'},
        {'instr':'Buka `m365.cloud.microsoft/chat` > Agents > **Researcher** > **Model Council**. Tempel prompt.',
         'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. harus melindungi posisi regulator DAN kepercayaan customer DAN posisi finansial sekaligus. Berikut yang saya butuhkan dari Anda secara persis. 3 playbook respons paling defensible untuk Zava Electronics MY yang terkena US BIS export-control update. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. Model Council — gelar laporan paralel dari GPT dan Claude. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. Sorot perbedaan pendapat, tandai mayoritas dan minoritas. Tabel perbandingan: Playbook, Putusan Council, Pandangan Minoritas, Preseden ASEAN, Risiko Implementasi. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'}
      ],
      persona=['Mod Admin','Mod Admin'],
      personaID=['Mod Admin','Mod Admin']),

      tool(T_ANALYST, M365_LIC, M365_ACCT, [
        {'instr':'Open `m365.cloud.microsoft/chat` > Agents > **Analyst**. Upload /SEMI_01_BIS_SKU_Exposure.xlsx AND /SEMI_02_Customer_Concentration_Heatmap.xlsx. Paste the prompt below.',
         'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. Group ExCo needs an evidence-based view in 48 hours. Here is exactly what I need from you. Quantify the US BIS export-control update financial and operational impact. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. the 2 uploaded files. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. (1) RAG bar chart of at-risk items by severity; (2) waterfall of MYR EBITDA impact; (3) tracker by stakeholder/segment, flag worst <10% headroom as Red. Output a Board-ready RAG dashboard. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'}
      ], DESC_ANALYST,
      promptsID=[
        {'instr':'Buka `m365.cloud.microsoft/chat` > Agents > **Analyst**. Unggah /SEMI_01_BIS_SKU_Exposure.xlsx DAN /SEMI_02_Customer_Concentration_Heatmap.xlsx. Tempel prompt.',
         'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. ExCo Grup butuh pandangan berbasis bukti dalam 48 jam. Berikut yang saya butuhkan dari Anda secara persis. Kuantifikasi dampak finansial dan operasional dari US BIS export-control update. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. 2 file yang diunggah. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. (1) Bar chart RAG item at-risk berdasarkan severity; (2) waterfall dampak EBITDA RM; (3) tracker per stakeholder/segmen, tandai headroom terburuk <10% Merah. Hasilkan dashboard RAG siap-Direksi. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'}
      ],
      persona=['Hadar Caspit'],
      personaID=['Hadar Caspit']),

      tool(T_EXCEL, M365_LIC, M365_ACCT, [
        {'instr':'Open `/SEMI_01_BIS_SKU_Exposure.xlsx` in Excel for the Web. Open the **Copilot pane**. Paste the prompt below.',
         'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. Audit Committee meets in the next 14 days. Here is exactly what I need from you. Build a single Audit-Committee-ready dashboard sheet. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. combine all relevant tabs. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. New sheet "AC Dashboard" with KPI tiles, bar chart by severity, sparkline column. RAG conditional formatting. Do not modify source tabs. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'}
      ], '',
      promptsID=[
        {'instr':'Buka `/SEMI_01_BIS_SKU_Exposure.xlsx` di Excel for the Web. Buka **Copilot pane**. Tempel prompt.',
         'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. Komite Audit rapat dalam 14 hari ke depan. Berikut yang saya butuhkan dari Anda secara persis. Bangun satu sheet dashboard siap-Komite Audit. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. gabungkan semua tab yang relevan. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. Sheet baru "AC Dashboard" dengan KPI tile, bar chart per severity, kolom sparkline. Format kondisional RAG. Jangan modifikasi tab sumber. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'}
      ],
      persona=['Hadar Caspit'],
      personaID=['Hadar Caspit']),

      tool(T_WORD, M365_LIC, M365_ACCT, [
        {'instr':'Open a new blank Word doc in Word for the Web. Open the **Copilot pane**. Reference /SEMI_03_MITI_Brief_Pack.docx and /SEMI_05_Customer_Holding_Lines.docx using `/`. Paste the prompt below.',
         'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. US BIS export-control update active. Here is exactly what I need from you. Draft the regulator-grade response brief (4 pages). Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. the referenced docs + my notes. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. Sections — Material Facts, Current Status, Programme, Financial Impact Range, Forward-Looking Statements with explicit risk language. Tone: factual, regulator-grade, no speculation. Cite source files at the end of each section. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'}
      ], DESC_WORD,
      promptsID=[
        {'instr':'Buka dokumen Word baru kosong di Word for the Web. Buka **Copilot pane**. Referensikan /SEMI_03_MITI_Brief_Pack.docx dan /SEMI_05_Customer_Holding_Lines.docx menggunakan `/`. Tempel prompt.',
         'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. US BIS export-control update aktif. Berikut yang saya butuhkan dari Anda secara persis. Susun brief respons regulator-grade (4 halaman). Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. dokumen yang direferensikan + catatan saya. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. Bagian — Fakta Material, Status Saat Ini, Program, Rentang Dampak Finansial, Pernyataan Forward-Looking dengan bahasa risiko eksplisit. Nada: faktual, regulator-grade, tanpa spekulasi. Kutip file sumber di akhir tiap bagian. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'}
      ],
      persona=['Hadar Caspit'],
      personaID=['Hadar Caspit']),

      tool(T_PPT, M365_LIC, M365_ACCT, [
        {'instr':'Open a new PowerPoint deck in PowerPoint for the Web. Open the **Copilot pane**. Paste the prompt below.',
         'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. AC in 14 days. Here is exactly what I need from you. 8-slide Audit Committee deck on US BIS export-control update. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. my brief draft and dashboard. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. Cover; Situation; Status (RAG); Programme (2 slides); Financial Impact; Stakeholder Map; Decisions Requested. Brand colours #7C3AED + #0F1C3F, 1 chart per slide. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'}
      ], DESC_PPT,
      promptsID=[
        {'instr':'Buka deck PowerPoint baru di PowerPoint for the Web. Buka **Copilot pane**. Tempel prompt.',
         'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. KA dalam 14 hari. Berikut yang saya butuhkan dari Anda secara persis. Deck 8 slide Komite Audit tentang US BIS export-control update. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. draf brief dan dashboard saya. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. Cover; Situasi; Status (RAG); Program (2 slide); Dampak Finansial; Peta Pemangku Kepentingan; Keputusan yang Diminta. Warna brand #7C3AED + #0F1C3F, 1 chart per slide. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'}
      ],
      persona=['Sasha Ouellet'],
      personaID=['Sasha Ouellet']),

      tool(T_OUTLOOK, M365_LIC, M365_ACCT, [
        {'instr':'Open Outlook on the Web. Open the email thread "US BIS export-control update — Group CFO follow-up". Click the **Copilot icon**. Paste the prompt below.',
         'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. US BIS export-control update active. Here is exactly what I need from you. Draft a single email to the Zava Electronics MY ExCo and the relevant operating heads. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. the email thread above and the response programme. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. Subject line, 4 short paragraphs covering — situation, the 3 actions each operating head must complete in 72 hours, the regulator-engagement workstream, the AC date. Tone: firm, supportive, accountable. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'}
      ], DESC_OUTLOOK,
      promptsID=[
        {'instr':'Buka Outlook on the Web. Buka thread email "US BIS export-control update — tindak lanjut Direktur Keuangan Grup". Klik **ikon Copilot**. Tempel prompt.',
         'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. US BIS export-control update aktif. Berikut yang saya butuhkan dari Anda secara persis. Susun satu email ke ExCo Zava Electronics MY dan kepala operasi yang relevan. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. thread di atas dan program respons. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. Baris subjek, 4 paragraf pendek — situasi, 3 aksi per kepala operasi dalam 72 jam, workstream engagement regulator, tanggal KA. Nada: tegas, suportif, akuntabel. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'}
      ],
      persona=['Hadar Caspit'],
      personaID=['Hadar Caspit']),

      tool(T_TEAMS, M365_LIC, M365_ACCT, 
        [
          {'instr':"**(1) In Teams**, open **Calendar** → click the past meeting **\"New Software Implementation\"**. On the Recap page, walk the audience through the **AI Notes** (auto-summary), the **Custom summary** (Copilot's per-attendee view), and the **Audio recap** (chapter markers with speaker timings). **(2) In Word for the Web**, open a **new blank document**. Type a minutes template at the top — five empty headings: Date and Attendees · Agenda Items · Decisions Taken · Action Items · Risks and Open Questions. **(3) Click the Copilot icon** in the Word ribbon and paste the prompt below — Copilot in Word will reference the meeting recap by name with `/` and fill the template.", 'prompt':"Create meeting minutes for the Teams meeting /New Software Implementation. Use the empty template already on this page and fill each heading from the meeting recap. Sections: (1) Date and Attendees; (2) Agenda Items; (3) Decisions Taken; (4) Action Items with Owner and Due Date; (5) Risks and Open Questions. Quote attendee statements verbatim where the wording matters. Tag any decision that is on the critical path as Critical Path. Save the file as Minutes_New_Software_Implementation.docx in OneDrive."},
          {'instr':'**(1) In Teams**, open **Calendar** → click the past meeting **"Marketing Campaign Performance Review"**. On the Recap page, walk through the **AI Notes**, the **Custom summary**, and the **Audio recap** chapters. **(2) In Word for the Web**, open a **new blank document**. Type a campaign-review minutes template at the top — six empty headings: Date and Attendees · Campaign KPIs Reviewed · Decisions Taken · Action Items · Budget Reallocations · Next Review Date. **(3) Click the Copilot icon** in the Word ribbon and paste the prompt below.', 'prompt':"Create meeting minutes for the Teams meeting /Marketing Campaign Performance Review. Use the empty campaign-review template already on this page. Sections: (1) Date and Attendees; (2) Campaign KPIs Reviewed; (3) Decisions Taken; (4) Action Items with Owner and Due Date; (5) Budget Reallocations Approved; (6) Next Review Date. Quote attendee statements verbatim where the wording matters. Highlight any KPI that missed target by more than 10% in amber. Save the file as Minutes_Marketing_Campaign_Review.docx in OneDrive."},
          {'instr':'**(1) In Teams**, open **Calendar** → click the past meeting **"Negotiating Marketing Contract"**. On the Recap page, walk through the **AI Notes**, the **Custom summary**, and the **Audio recap**. **(2) In Word for the Web**, open a **new blank document**. Type a vendor-negotiation minutes template at the top — seven empty headings: Vendor and Owner · Commercial Terms Discussed · Concessions Offered · Concessions Accepted · Open Items · Approval Thresholds · Next Steps. **(3) Click the Copilot icon** in the Word ribbon and paste the prompt below — then forward the result to Procurement, Legal, and the Group CFO.', 'prompt':"Create meeting minutes for the Teams meeting /Negotiating Marketing Contract. Use the empty vendor-negotiation template already on this page. Sections: (1) Vendor and Owner; (2) Commercial Terms Discussed; (3) Concessions Offered; (4) Concessions Accepted; (5) Open Items; (6) Approval Thresholds (CFO / Board); (7) Next Steps with Owner and Due Date. Highlight any term requiring CFO sign-off in amber and any term requiring Board sign-off in red. Save the file as Minutes_Marketing_Contract_Negotiation.docx in OneDrive and email the link to Procurement, Legal, and the Group CFO."}
        ], DESC_TEAMS,
        promptsID=[
          {'instr':'**(1) Di Teams**, buka **Calendar** → klik rapat **"New Software Implementation"**. Di halaman Recap, jelaskan ke peserta tentang **AI Notes** (ringkasan otomatis), **Custom summary** (tampilan per-peserta dari Copilot), dan **Audio recap** (penanda bab dengan timing pembicara). **(2) Di Word for the Web**, buka **dokumen kosong baru**. Ketik kerangka notulen di bagian atas — lima heading kosong: Tanggal dan Peserta · Agenda · Keputusan · Action Items · Risiko dan Pertanyaan Terbuka. **(3) Klik ikon Copilot** di ribbon Word lalu tempelkan prompt di bawah — Copilot in Word akan merujuk recap rapat dengan `/` dan mengisi template.', 'prompt':"Susun notulen rapat untuk rapat Teams /New Software Implementation. Gunakan template kosong yang sudah ada di halaman ini dan isi tiap heading dari recap rapat. Bagian: (1) Tanggal dan Peserta; (2) Agenda; (3) Keputusan; (4) Action Items dengan Owner dan Due Date; (5) Risiko dan Pertanyaan Terbuka. Kutip pernyataan peserta apa adanya bila kata-katanya penting. Tandai keputusan di jalur kritis sebagai Critical Path. Simpan file sebagai Minutes_New_Software_Implementation.docx di OneDrive."},
          {'instr':'**(1) Di Teams**, buka **Calendar** → klik rapat **"Marketing Campaign Performance Review"**. Di halaman Recap, jelaskan **AI Notes**, **Custom summary**, dan **Audio recap**. **(2) Di Word for the Web**, buka dokumen kosong baru. Ketik kerangka notulen tinjauan kampanye — enam heading kosong: Tanggal dan Peserta · KPI Kampanye yang Dikaji · Keputusan · Action Items · Realokasi Anggaran · Jadwal Tinjauan Berikutnya. **(3) Klik ikon Copilot** di ribbon Word lalu tempelkan prompt di bawah.', 'prompt':"Susun notulen rapat untuk rapat Teams /Marketing Campaign Performance Review. Gunakan template kosong tinjauan kampanye yang sudah ada. Bagian: (1) Tanggal dan Peserta; (2) KPI Kampanye yang Dikaji; (3) Keputusan; (4) Action Items dengan Owner dan Due Date; (5) Realokasi Anggaran yang Disetujui; (6) Jadwal Tinjauan Berikutnya. Kutip pernyataan peserta apa adanya. Tandai KPI yang meleset >10% dengan amber. Simpan sebagai Minutes_Marketing_Campaign_Review.docx di OneDrive."},
          {'instr':'**(1) Di Teams**, buka **Calendar** → klik rapat **"Negotiating Marketing Contract"**. Di halaman Recap, jelaskan **AI Notes**, **Custom summary**, dan **Audio recap**. **(2) Di Word for the Web**, buka dokumen kosong baru. Ketik kerangka notulen negosiasi vendor — tujuh heading kosong: Vendor dan Owner · Term Komersial · Konsesi yang Ditawarkan · Konsesi yang Diterima · Item Terbuka · Threshold Persetujuan · Langkah Berikutnya. **(3) Klik ikon Copilot** di ribbon Word lalu tempelkan prompt di bawah — kemudian teruskan hasilnya ke Procurement, Legal, dan Direktur Keuangan Grup.', 'prompt':"Susun notulen rapat untuk rapat Teams /Negotiating Marketing Contract. Gunakan template kosong negosiasi vendor yang sudah ada. Bagian: (1) Vendor dan Owner; (2) Term Komersial; (3) Konsesi yang Ditawarkan; (4) Konsesi yang Diterima; (5) Item Terbuka; (6) Threshold Persetujuan (CFO / Direksi); (7) Langkah Berikutnya dengan Owner dan Due Date. Tandai term yang memerlukan persetujuan CFO dengan amber dan persetujuan Direksi dengan merah. Simpan sebagai Minutes_Marketing_Contract_Negotiation.docx di OneDrive lalu email link-nya ke Procurement, Legal, dan Direktur Keuangan Grup."}
        ],
        promptsBM=[
          {'instr':'**(1) Di Teams**, buka **Calendar** → klik mesyuarat **"New Software Implementation"**. Pada halaman Recap, terangkan kepada hadirin tentang **AI Notes** (ringkasan automatik), **Custom summary** (paparan per-hadirin dari Copilot), dan **Audio recap** (penanda bab dengan masa pembicara). **(2) Di Word for the Web**, buka **dokumen kosong baharu**. Taip rangka minit di bahagian atas — lima tajuk kosong: Tarikh dan Hadirin · Agenda · Keputusan · Tindakan · Risiko dan Soalan Terbuka. **(3) Klik ikon Copilot** di ribbon Word dan tampal prompt di bawah — Copilot in Word akan merujuk recap mesyuarat dengan `/` dan mengisi templat.', 'prompt':"Hasilkan minit mesyuarat untuk mesyuarat Teams /New Software Implementation. Gunakan templat kosong yang sudah ada di halaman ini dan isi setiap tajuk daripada recap mesyuarat. Bahagian: (1) Tarikh dan Hadirin; (2) Agenda; (3) Keputusan; (4) Tindakan dengan Pemilik dan Tarikh; (5) Risiko dan Soalan Terbuka. Petik kenyataan hadirin sebagaimana asal di mana perkataannya penting. Tandakan sebarang keputusan di laluan kritikal sebagai Critical Path. Simpan fail sebagai Minutes_New_Software_Implementation.docx di OneDrive."},
          {'instr':'**(1) Di Teams**, buka **Calendar** → klik mesyuarat **"Marketing Campaign Performance Review"**. Pada halaman Recap, terangkan **AI Notes**, **Custom summary**, dan **Audio recap**. **(2) Di Word for the Web**, buka dokumen kosong baharu. Taip rangka minit ulasan kempen — enam tajuk kosong: Tarikh dan Hadirin · KPI Kempen yang Diulas · Keputusan · Tindakan · Pelarasan Bajet · Tarikh Ulasan Berikutnya. **(3) Klik ikon Copilot** di ribbon Word dan tampal prompt di bawah.', 'prompt':"Hasilkan minit mesyuarat untuk mesyuarat Teams /Marketing Campaign Performance Review. Gunakan templat kosong ulasan kempen yang sudah ada. Bahagian: (1) Tarikh dan Hadirin; (2) KPI Kempen yang Diulas; (3) Keputusan; (4) Tindakan dengan Pemilik dan Tarikh; (5) Pelarasan Bajet yang Diluluskan; (6) Tarikh Ulasan Berikutnya. Petik kenyataan hadirin sebagaimana asal. Tandakan KPI yang tersasar >10% dengan amber. Simpan sebagai Minutes_Marketing_Campaign_Review.docx di OneDrive."},
          {'instr':'**(1) Di Teams**, buka **Calendar** → klik mesyuarat **"Negotiating Marketing Contract"**. Pada halaman Recap, terangkan **AI Notes**, **Custom summary**, dan **Audio recap**. **(2) Di Word for the Web**, buka dokumen kosong baharu. Taip rangka minit perundingan vendor — tujuh tajuk kosong: Vendor dan Pemilik · Terma Komersial · Konsesi Ditawarkan · Konsesi Diterima · Item Terbuka · Ambang Kelulusan · Langkah Seterusnya. **(3) Klik ikon Copilot** di ribbon Word dan tampal prompt di bawah — kemudian majukan hasilnya kepada Procurement, Legal dan Pengarah Kewangan Kumpulan.', 'prompt':"Hasilkan minit mesyuarat untuk mesyuarat Teams /Negotiating Marketing Contract. Gunakan templat kosong perundingan vendor yang sudah ada. Bahagian: (1) Vendor dan Pemilik; (2) Terma Komersial; (3) Konsesi Ditawarkan; (4) Konsesi Diterima; (5) Item Terbuka; (6) Ambang Kelulusan (CFO / Lembaga); (7) Langkah Seterusnya dengan Pemilik dan Tarikh. Tandakan terma yang memerlukan kelulusan CFO dengan amber dan Lembaga dengan merah. Simpan sebagai Minutes_Marketing_Contract_Negotiation.docx di OneDrive dan e-mel pautan kepada Procurement, Legal dan Pengarah Kewangan Kumpulan."}
        ],
        persona=['Sasha Ouellet', 'Sasha Ouellet', 'Sasha Ouellet'],
        personaID=['Sasha Ouellet', 'Sasha Ouellet', 'Sasha Ouellet']
      ),

      tool(T_NOTEBOOK, M365_LIC, M365_ACCT, [
        {'instr':'All sources are loaded. Type the prompt below in the notebook chat.',
         'prompt':'Synthesise across all sources to produce a 10-bullet Audit Committee narrative. Cover: US BIS export-control update status, programme, financial impact, stakeholder map, decisions requested. Cite the source file at the end of every bullet.'},
        {'instr':'Click **Quick Create** > **Audio Overview** to generate a 6-minute briefing podcast.',
         'prompt':'Quick Create: Audio Overview, 6 minutes, formal narration tone, focused on the AC narrative above. Listeners are the Zava Electronics MY operating heads preparing for tomorrow morning huddles.'}
      ], DESC_NOTEBOOK,
      promptsID=[
        {'instr':'Semua sumber sudah dimuat. Ketik prompt di bawah pada chat notebook.',
         'prompt':'Sintesakan dari semua sumber untuk menghasilkan narasi Komite Audit 10-bullet. Cakup: status US BIS export-control update, program, dampak finansial, peta pemangku kepentingan, keputusan yang diminta. Kutip file sumber di akhir tiap bullet.'},
        {'instr':'Klik **Quick Create** > **Audio Overview** untuk menghasilkan podcast briefing 6 menit.',
         'prompt':'Quick Create: Audio Overview, 6 menit, gaya narasi formal, fokus pada narasi KA di atas. Pendengar adalah kepala operasi Zava Electronics MY yang menyiapkan huddle pagi besok.'}
      ],
      persona=['Mod Admin','Mod Admin'],
      personaID=['Mod Admin','Mod Admin'],
      notebookMeta={
        'sources':['/SEMI_01_BIS_SKU_Exposure.xlsx', '/SEMI_02_Customer_Concentration_Heatmap.xlsx', '/SEMI_03_MITI_Brief_Pack.docx', '/SEMI_04_Capex_Reprioritisation.xlsx', '/SEMI_05_Customer_Holding_Lines.docx'],
        'instructions':'You are the Group CFO of Zava Electronics MY preparing an Audit Committee pack on US BIS export-control update. Always cite the source file and tab/section. Tone: precise, regulator-grade, no speculation. Use MYR for the Group totals (1 MYR ≈ 3,580 IDR).',
        'instructionsID':'Anda adalah Direktur Keuangan Grup Zava Electronics MY yang menyiapkan paket Komite Audit untuk US BIS export-control update. Selalu kutip file sumber dan tab/bagian. Nada: presisi, regulator-grade, tanpa spekulasi. Gunakan MYR untuk total Grup (1 MYR ≈ 3.580 IDR).'
      }),

      tool(T_COWORK, FRONTIER_LIC, M365_ACCT, [
        {'instr':'Open `m365.cloud.microsoft` > Agents > **Cowork**. Paste the single prompt below — Cowork delegates 5 parallel sub-tasks. Frontier required.',
         'prompt':'Cowork — BIS 7-Day MITI Brief Sprint. Run these in parallel: (1) 📝 Draft Word — regulator response brief 4 pages, source /SEMI_01_BIS_SKU_Exposure.xlsx, /SEMI_02_Customer_Concentration_Heatmap.xlsx, /SEMI_03_MITI_Brief_Pack.docx, /SEMI_04_Capex_Reprioritisation.xlsx, /SEMI_05_Customer_Holding_Lines.docx. (2) 📝 Draft Word — internal ExCo briefing memo 2 pages, same sources. (3) ✉️ Send email to Zava Electronics MY ExCo and operating heads with the 3 actions in 72h. (4) 📅 Schedule 90-min AC Pre-Read tomorrow 8am MYT. (5) 💬 Post Teams message to #group-exco with one-line headline + dashboard link. Use these named recipients consistently across the email task and the Teams meeting task — Hadar (Group CFO), Sasha (Group Chief of Staff), Daichi (Head of Investor Relations), Sonia (Head of Strategy), Will (Head of Risk) and Omar (Head of Procurement) — and adapt the precise distribution per sub-task to keep each communication focused on the right audience.'}
      ], DESC_COWORK,
      promptsID=[
        {'instr':'Buka `m365.cloud.microsoft` > Agents > **Cowork**. Tempel prompt tunggal — Cowork mendelegasikan 5 sub-tugas paralel. Frontier diperlukan.',
         'prompt':'Cowork — BIS 7-Day MITI Brief Sprint. Jalankan paralel: (1) 📝 Susun Word — brief respons regulator 4 halaman, sumber /SEMI_01_BIS_SKU_Exposure.xlsx, /SEMI_02_Customer_Concentration_Heatmap.xlsx, /SEMI_03_MITI_Brief_Pack.docx, /SEMI_04_Capex_Reprioritisation.xlsx, /SEMI_05_Customer_Holding_Lines.docx. (2) 📝 Susun Word — memo briefing ExCo internal 2 halaman, sumber sama. (3) ✉️ Kirim email ke ExCo Zava Electronics MY dan kepala operasi dengan 3 aksi dalam 72 jam. (4) 📅 Jadwalkan AC Pre-Read 90 menit besok 08:00 WIB. (5) 💬 Posting pesan Teams di #group-exco dengan headline satu baris + tautan dashboard. Use these named recipients consistently across the email task and the Teams meeting task — Hadar (Group CFO), Sasha (Group Chief of Staff), Daichi (Head of Investor Relations), Sonia (Head of Strategy), Will (Head of Risk) and Omar (Head of Procurement) — and adapt the precise distribution per sub-task to keep each communication focused on the right audience.'}
      ],
      persona=['Mod Admin'],
      personaID=['Mod Admin']),

      tool(T_WORD_AGT, ANY_LIC, ANY_ACCT, [
        {'instr':'Open `m365.cloud.microsoft/chat` → Agents tab → **Word Agent**. Paste the prompt below — the agent returns a fully drafted .docx.',
         'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. US BIS export-control update. Here is exactly what I need from you. Generate a 4-page CFO Crisis Brief in Word. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. /SEMI_01_BIS_SKU_Exposure.xlsx AND /SEMI_02_Customer_Concentration_Heatmap.xlsx. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. Sections — Executive Summary 5 bullets; Current Status; Programme; Financial Impact; Stakeholder Map; Decisions requested. Tone: precise, regulator-grade. Save as MITI_BIS_Brief.docx. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'}
      ], DESC_WORD_AGT,
      promptsID=[
        {'instr':'Buka `m365.cloud.microsoft/chat` → tab Agents → **Word Agent**. Tempel prompt — agent mengembalikan .docx yang sudah didraf penuh.',
         'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. US BIS export-control update. Berikut yang saya butuhkan dari Anda secara persis. Hasilkan Brief Krisis Direktur Keuangan 4 halaman dalam Word. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. /SEMI_01_BIS_SKU_Exposure.xlsx DAN /SEMI_02_Customer_Concentration_Heatmap.xlsx. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. Bagian — Ringkasan Eksekutif 5 bullet; Status Saat Ini; Program; Dampak Finansial; Peta Pemangku Kepentingan; Keputusan yang diminta. Nada: presisi, regulator-grade. Simpan sebagai Brief_BIS_MITI.docx. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'}
      ],
      persona=['Sasha Ouellet'],
      personaID=['Sasha Ouellet']),

      tool(T_PPT_AGT, ANY_LIC, ANY_ACCT, [
        {'instr':'Open `m365.cloud.microsoft/chat` → Agents tab → **PowerPoint Agent**. Paste the prompt below.',
         'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. AC in 14 days. Here is exactly what I need from you. 8-slide Audit Committee deck on US BIS export-control update. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. /MITI_BIS_Brief.docx and /SEMI_01_BIS_SKU_Exposure.xlsx. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. Cover; Situation; Status RAG; Programme (2); Financial Impact; Stakeholder Map; Decisions. Brand #7C3AED + #0F1C3F, 1 chart/slide. Save as BIS_AC_Deck.pptx. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'}
      ], DESC_PPT_AGT,
      promptsID=[
        {'instr':'Buka `m365.cloud.microsoft/chat` → tab Agents → **PowerPoint Agent**. Tempel prompt.',
         'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. KA dalam 14 hari. Berikut yang saya butuhkan dari Anda secara persis. Deck 8 slide Komite Audit tentang US BIS export-control update. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. /Brief_BIS_MITI.docx dan /SEMI_01_BIS_SKU_Exposure.xlsx. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. Cover; Situasi; Status RAG; Program (2); Dampak Finansial; Peta Pemangku Kepentingan; Keputusan. Brand #7C3AED + #0F1C3F, 1 chart/slide. Simpan sebagai Deck_KA_BIS.pptx. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'}
      ],
      persona=['Sasha Ouellet'],
      personaID=['Sasha Ouellet']),

      tool(T_XL_AGT, ANY_LIC, ANY_ACCT, [
        {'instr':'Open `m365.cloud.microsoft/chat` → Agents tab → **Excel Agent**. Paste the prompt below.',
         'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. Operating tracker for the Group COO. Here is exactly what I need from you. Build a US BIS export-control update response control tracker workbook. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. schema only. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. Sheet 1 Issue Log, Sheet 2 Programme Milestones, Sheet 3 Cost Tracker, Sheet 4 Dashboard with KPI tiles + RAG conditional formatting. Save as BIS_Exposure_Tracker.xlsx. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'}
      ], DESC_XL_AGT,
      promptsID=[
        {'instr':'Buka `m365.cloud.microsoft/chat` → tab Agents → **Excel Agent**. Tempel prompt.',
         'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. tracker operasi untuk Direktur Operasional Grup. Berikut yang saya butuhkan dari Anda secara persis. Bangun workbook tracker kendali respons US BIS export-control update. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. hanya skema. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. Sheet 1 Log Isu, Sheet 2 Milestone Program, Sheet 3 Tracker Biaya, Sheet 4 Dashboard dengan KPI tile + format kondisional RAG. Simpan sebagai Tracker_Paparan_BIS.xlsx. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'}
      ],
      persona=['Hadar Caspit'],
      personaID=['Hadar Caspit']),

      tool_builder(M365_LIC, M365_ACCT,
        agents=[
        {
          'icon': '🔬',
          'label': 'Wafer Yield & Cycle',
          'name': 'Zava Semiconductor — Wafer Yield & Cycle-Time Coach',
          'desc': 'Optimises Semiconductor / E&E fab yield, cycle time, and defect-density by lot, tool, and recipe.',
          'instructions': 'You are the Zava Semiconductor / E&E Wafer Yield & Cycle-Time Coach. You support the Fab Director and Process Engineering. Scan yield data (SEMI_01_BIS_SKU_Exposure.xlsx), tool-availability data (SEMI_02_Customer_Concentration_Heatmap.xlsx), and the defect-density register (SEMI_04_Capex_Reprioritisation.xlsx) for yield-loss drivers and cycle-time bottlenecks. Tabulate by tool / recipe. Recommend one process or maintenance action per Red item. Refuse any commercial pricing question.',
          'knowledge': [
            {'file':'SEMI_01_BIS_SKU_Exposure.xlsx', 'note':'Wafer yield and bin data.'},
            {'file':'SEMI_02_Customer_Concentration_Heatmap.xlsx', 'note':'Tool-availability and OEE data.'},
            {'file':'SEMI_04_Capex_Reprioritisation.xlsx', 'note':'Defect-density register.'}
          ],
          'knowledgeNote': 'Test: "Which 3 process steps at Semiconductor / E&E are causing the worst yield drag this week?"',
          'queries': [
            'Top 10 yield-loss product/lot/tool combinations — tabulate yield %, defect density, recommended action.',
            'Which tools have the worst OEE deterioration this quarter? Recommend maintenance and process tuning.',
            'Draft the weekly Process Engineering review paper.'
          ],
        },
        {
          'icon': '🏗️',
          'label': 'Foundry Capex Watch',
          'name': 'Zava Semiconductor — Foundry Capex & Capacity Watch',
          'desc': 'Tracks Semiconductor / E&E capacity expansion projects, equipment-lead-time risk, and customer commit alignment.',
          'instructions': 'You are the Zava Semiconductor / E&E Foundry Capex & Capacity Watch agent. You support the Capex Steering Committee. Monitor capex programme data (SEMI_03_MITI_Brief_Pack.docx) and customer commit data (SEMI_05_Customer_Holding_Lines.docx) for slippage, equipment lead-time risk, and capacity-vs-commit gaps. Recommend escalation or commercial actions per Red.',
          'knowledge': [
            {'file':'SEMI_03_MITI_Brief_Pack.docx', 'note':'Capex programme — milestones, spend, slippage.'},
            {'file':'SEMI_05_Customer_Holding_Lines.docx', 'note':'Customer commit register — volume, ramp date.'}
          ],
          'knowledgeNote': 'Test: "Which capex projects at Semiconductor / E&E are most at risk of slipping past the customer ramp date?"',
          'queries': [
            'Top 10 capex projects by RAG — name, spend, slippage days, customer-commit risk, recommended action.',
            'Which equipment items have lead-time slippage? Tabulate item, slip days, and mitigation.',
            'Draft the monthly Capex Committee paper on the proposed re-baseline of the largest project.'
          ],
        },
        {
          'icon': '🏛️',
          'label': 'MIDA / BKPM Liaison',
          'name': 'Zava Semiconductor — Industry Regulator Liaison',
          'desc': 'Prepares MIDA (MY) / BKPM (ID) incentive filings, export-control declarations, and FTZ compliance for Semiconductor / E&E.',
          'instructions': 'You are the Zava Semiconductor / E&E Industry Regulator Liaison. You support Government Relations. Prepare incentive filings, export-control declarations (US BIS, EU Wassenaar), and FTZ compliance grounded on the regulatory file (SEMI_04_Capex_Reprioritisation.xlsx) and the policy handbook (SEMI_05_Customer_Holding_Lines.docx). Quote every clause with section number.',
          'knowledge': [
            {'file':'SEMI_04_Capex_Reprioritisation.xlsx', 'note':'Industry regulatory returns and incentive submissions.'}
          ],
          'knowledgeNote': 'Test: "Draft the response to MIDA\'s latest circular on incentive-claim documentation for Semiconductor / E&E."',
          'queries': [
            "Prepare a cover letter for this year's MIDA / BKPM incentive claim.",
            'Which export-control items shipped this quarter? Verify against the BIS and Wassenaar lists.',
            'Draft the FTZ annual compliance return.'
          ],
        }
      ],
        agentsID=[
        {
          'icon': '🔬',
          'label': 'Wafer Yield & Cycle',
          'name': 'Zava Semiconductor — Wafer Yield & Cycle-Time Pelatih',
          'desc': 'Optimises Semiconductor / E&E fab yield, cycle time, and defect-density by lot, tool, and recipe.',
          'instructions': 'Anda adalah Zava Semiconductor / E&E Wafer Yield & Cycle-Time Pelatih. Anda mendukung the Fab Director and Process Engineering. Scan yield data (SEMI_01_BIS_SKU_Exposure.xlsx), tool-availability data (SEMI_02_Customer_Concentration_Heatmap.xlsx), and the defect-density register (SEMI_04_Capex_Reprioritisation.xlsx) for yield-loss drivers and cycle-time bottlenecks. Tabulasikan by tool / recipe. Rekomendasikan one process or maintenance tindakan per Red item. Tolak any commercial pricing question.',
          'knowledge': [
            {'file':'SEMI_01_BIS_SKU_Exposure.xlsx', 'note':'Wafer yield and bin data.'},
            {'file':'SEMI_02_Customer_Concentration_Heatmap.xlsx', 'note':'Tool-availability and OEE data.'},
            {'file':'SEMI_04_Capex_Reprioritisation.xlsx', 'note':'Defect-density register.'}
          ],
          'knowledgeNote': 'Test: "Yang mana 3 process steps at Semiconductor / E&E are causing terburuk yield drag this week?"',
          'queries': [
            '10 teratas yield-loss product/lot/tool combinations — tabulasikan yield %, defect density, recommended tindakan.',
            'Yang mana tools have terburuk OEE deterioration kuartal ini? Rekomendasikan maintenance and process tuning.',
            'Susun the mingguan Process Engineering review paper.'
          ],
        },
        {
          'icon': '🏗️',
          'label': 'Foundry Capex Watch',
          'name': 'Zava Semiconductor — Foundry Capex & Capacity Watch',
          'desc': 'Memantau Semiconductor / E&E capacity expansion projects, equipment-lead-time risk, and customer commit alignment.',
          'instructions': 'Anda adalah Zava Semiconductor / E&E Foundry Capex & Capacity Pemantau agen. Anda mendukung the Capex Komite Pengarah. Pantau capex programme data (SEMI_03_MITI_Brief_Pack.docx) and customer commit data (SEMI_05_Customer_Holding_Lines.docx) for slippage, equipment lead-time risk, and capacity-vs-commit gaps. Rekomendasikan escalation or commercial actions per Red.',
          'knowledge': [
            {'file':'SEMI_03_MITI_Brief_Pack.docx', 'note':'Capex programme — milestones, spend, slippage.'},
            {'file':'SEMI_05_Customer_Holding_Lines.docx', 'note':'Customer commit register — volume, ramp date.'}
          ],
          'knowledgeNote': 'Test: "Yang mana capex projects at Semiconductor / E&E are most at risk of slipping past the customer ramp date?"',
          'queries': [
            '10 teratas capex projects by RAG — name, spend, slippage days, customer-commit risk, recommended tindakan.',
            'Yang mana equipment items have lead-time slippage? Tabulasikan item, slip days, and mitigation.',
            'Susun the bulanan Capex Committee paper on the proposed re-baseline of terbesar project.'
          ],
        },
        {
          'icon': '🏛️',
          'label': 'MIDA / BKPM Penghubung',
          'name': 'Zava Semiconductor — Industry Regulator Penghubung',
          'desc': 'Prepares MIDA (MY) / BKPM (ID) incentive filings, export-control declarations, and FTZ compliance for Semiconductor / E&E.',
          'instructions': 'Anda adalah Zava Semiconductor / E&E Industry Regulator Penghubung. Anda mendukung Government Relations. Prepare incentive filings, export-control declarations (US BIS, EU Wassenaar), and FTZ compliance grounded on the regulatory file (SEMI_04_Capex_Reprioritisation.xlsx) and the policy handbook (SEMI_05_Customer_Holding_Lines.docx). Quote every clause with section number.',
          'knowledge': [
            {'file':'SEMI_04_Capex_Reprioritisation.xlsx', 'note':'Industry regulatory returns and incentive submissions.'}
          ],
          'knowledgeNote': 'Test: "Susun the response to MIDA\'s latest circular on incentive-claim documentation for Semiconductor / E&E."',
          'queries': [
            "Prepare a cover letter for this year's MIDA / BKPM incentive claim.",
            'Yang mana export-control items shipped kuartal ini? Verify against the BIS and Wassenaar lists.',
            'Susun the FTZ tahunan compliance return.'
          ],
        }
      ],
        persona=['Mod Admin', 'Mod Admin', 'Mod Admin'],
        personaID=['Mod Admin', 'Mod Admin', 'Mod Admin']
      ),
    ],
    companyID='Zava Electronics MY',
    taglineID='Update US BIS export-control — 14 customer SKU berisiko, brief MITI dalam 7 hari.',
    scenarioID='Zava Electronics MY mengoperasikan 4 pabrik assembly-and-test semikonduktor di Penang, Kulim, dan Melaka dengan hard-disk-drive heads, NAND flash packaging, dan IC substrates sebagai lini pendapatan inti (USD 1,9 miliar FY2025). US Bureau of Industry and Security memperbarui aturan export-control menambahkan 14 customer SKU ke register paparan Entity-List. MITI Malaysia meminta brief dalam 7 hari. Direktur Keuangan Grup butuh jadwal SKU at-risk yang terkuantifikasi, holding line per customer, memo guidance dari export-counsel AS, re-prioritisasi capex, dan narasi Komite Audit. Frame customer riil: grup ini beroperasi serupa dengan Western Digital Penang, Micron, Inari Amertron, ESCATEC, dan Pentamaster.',
    relevantDepts=['dept-finance','dept-strategy','dept-legal','dept-operations','dept-risk','dept-procurement'],
    personas=[
      {'name':'Hadar Caspit','role':'Group CFO','roleID':'Direktur Keuangan Grup','acct':'admin@ABSx62256373.onmicrosoft.com','lic':'Microsoft 365 Copilot','color':'#1E40AF'},
      {'name':'Sasha Ouellet','role':'Group Chief of Staff','roleID':'Kepala Staf Grup','acct':'SashaO@ABSx62256373.OnMicrosoft.com','lic':'Free \u2014 no Microsoft 365 Copilot license','color':'#7C3AED'},
      {'name':'Mod Admin','role':'Group Strategy Director','roleID':'Direktur Strategi Grup','acct':'admin@ABSx62256373.onmicrosoft.com','lic':'Microsoft 365 Copilot','color':'#059669'},
      {'name':'Daichi Maruyama','role':'Group Sustainability & Risk Director','roleID':'Direktur Keberlanjutan & Risiko Grup','acct':'admin@ABSx62256373.onmicrosoft.com','lic':'Microsoft 365 Copilot','color':'#DC2626'}
    ],
    storyboard=[
      {'ex':1,'title':'Research & Brief','titleID':'Riset & Pengarahan','minutes':18,'mode':'Show & Tell + Hands-on',
       'summary':'Frame the US BIS export-control update situation and pull peer playbooks before the regulator clock starts ticking.',
       'summaryID':'Bingkai situasi US BIS export-control update dan tarik playbook peer sebelum clock regulator mulai berdetak.',
       'tasks':[
         {'verb':'Frame the morning question and lock the day priorities','verbID':'Susun pertanyaan pagi dan kunci prioritas hari ini','toolId':T_CHAT,'mode':'Show & Tell'},
         {'verb':'Run an outside-in peer scan and pull proven plays','verbID':'Lakukan pemindaian peer dari luar dan tarik praktik terbaik','toolId':T_RESEARCHER,'mode':'Show & Tell'},
         {'verb':'Generate a board-ready brief straight from chat','verbID':'Hasilkan brief siap-Direksi langsung dari chat','toolId':T_WORD_AGT,'mode':'Hands-on'}]},
      {'ex':2,'title':'Analyse & Decide','titleID':'Analisis & Putuskan','minutes':18,'mode':'Hands-on',
       'summary':'Quantify US BIS export-control update financial and operational impact; build an AC dashboard.',
       'summaryID':'Kuantifikasi dampak finansial dan operasional US BIS export-control update; bangun dashboard KA.',
       'tasks':[
         {'verb':'Crunch the numbers and surface the biggest gaps','verbID':'Olah angka dan ungkap celah terbesar','toolId':T_ANALYST,'mode':'Hands-on'},
         {'verb':'Build a single-pane operating dashboard','verbID':'Bangun dashboard operasi satu-halaman','toolId':T_EXCEL,'mode':'Hands-on'},
         {'verb':'Spin up a recurring tracker workbook from chat','verbID':'Buat workbook tracker berulang dari chat','toolId':T_XL_AGT,'mode':'Hands-on'}]},
      {'ex':3,'title':'Communicate & Coordinate','titleID':'Komunikasi & Koordinasi','minutes':18,'mode':'Hands-on',
       'summary':'Brief operating heads, capture the BIS Export-Control War Room recap, and assemble the AC deck and regulator response.',
       'summaryID':'Brief kepala operasi, capture recap BIS Export-Control War Room, dan rakit deck KA serta respons regulator.',
       'tasks':[
         {'verb':'Draft the stakeholder alignment email','verbID':'Draf email penyelarasan stakeholder','toolId':T_OUTLOOK,'mode':'Hands-on'},
         {'verb':'Recap the meeting and turn it into minutes','verbID':'Recap rapat dan ubah ke notulen','toolId':T_TEAMS,'mode':'Hands-on'},
         {'verb':'Generate a board-ready deck from chat','verbID':'Hasilkan deck siap-Direksi dari chat','toolId':T_PPT_AGT,'mode':'Hands-on'},
         {'verb':'Delegate a 5-task parallel sprint','verbID':'Delegasikan 5-tugas paralel ke Cowork','toolId':T_COWORK,'mode':'Show & Tell'}]},
      {'ex':4,'title':'Build & Scale','titleID':'Bangun & Skala','minutes':15,'mode':'Show & Tell',
       'summary':'Wrap the US BIS export-control update playbook into a reusable agent for the Zava Electronics MY operating team.',
       'summaryID':'Bungkus playbook US BIS export-control update ke dalam agent reusable untuk tim operasi Zava Electronics MY.',
       'tasks':[
         {'verb':'Pull every source into one synthesis notebook','verbID':'Tarik semua sumber ke satu notebook sintesis','toolId':T_NOTEBOOK,'mode':'Show & Tell'},
         {'verb':'Wrap the daily workflow into a reusable agent','verbID':'Bungkus alur kerja harian jadi agen yang dapat dipakai ulang','toolId':T_BUILDER,'mode':'Show & Tell'}]}
    ],
    geo='MY'
))


# ╔══════════════════════════════════════════════════════════════════════╗
# ║  7.  RARE-EARTH & METALS                                        ║
# ╚══════════════════════════════════════════════════════════════════════╝
INDUSTRIES_10.append(ind(
    'rare-earth', 'sec-mining', 'Rare-Earth & Metals', '⛏️', '#B45309', '#78350F',
    'Zava Rare Earth',
    'JAEC environmental approval renewal + China REE export curb — Bursa update in 14 days.',
    "Zava Rare Earth operates an integrated heavy rare-earth concentrate plant in Pahang and a downstream separation facility in Gebeng producing neodymium, dysprosium, and terbium oxides for global EV magnet and wind-turbine customers. The Atomic Energy Licensing Board (AELB) environmental-approval renewal is due in 90 days; civil-society stakeholders have raised TENORM-residue concerns. China's MOFCOM has tightened REE export licensing in parallel, lifting global pricing 28% in 4 weeks. Bursa Malaysia expects an operational update in 14 days. The Group CFO needs the JAEC/AELB technical narrative, civil-society engagement plan, customer pricing pass-through analysis, and Bursa disclosure all coordinated. Real customer reference frame: this group operates similarly to Lynas Malaysia and MMC Corp Mining.",
    ['RE_01_AELB_Compliance_Tracker.xlsx', 'RE_02_TENORM_Residue_Inventory.xlsx', 'RE_03_Civil_Society_Engagement.docx', 'RE_04_Customer_Pricing_Model.xlsx', 'RE_05_Bursa_Operational_Update.docx'],
    [
      tool(T_CHAT, FREE_LIC, FREE_ACCT, [
        {'instr':'', 'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. Zava Rare Earth operates an integrated heavy rare-earth concentrate plant in Pahang and a downstream separation facility in Gebeng producing neodymium, dysprosium, and terbium oxides for global EV mag... Here is exactly what I need from you. Frame the AELB renewal + China REE export curb situation in plain English for the Group CEO. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. my notes from the morning crisis call. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. 1-page note with sections — Headline, What Happened, Stakeholder Position, Top 5 Questions the Board Will Ask, 3 Decisions the CEO Must Take in 48 Hours. Tone: calm, precise, no industry jargon. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'},
        {'instr':'', 'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. Audience is internal ExCo + key external stakeholders. Here is exactly what I need from you. 90-second verbal opening for the Zava Rare Earth stakeholder briefing. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. published facts only. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. Open with acknowledgement, explain the response programme, signal credible recovery, end with 3 commitments. Avoid speculative language. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'},
        {'instr':'', 'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. regulator clock active. Here is exactly what I need from you. Build the stakeholder communication map for the AELB renewal + China REE export curb. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. known stakeholders. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. RAG table — Red same-day, Amber 24h, Green monitor. Columns: Audience, Channel, Owner, Message Theme, Timing, Risk if Mishandled. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'}
      ], DESC_CHAT,
      promptsID=[
        {'instr':'', 'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. Zava Rare Earth mengoperasikan pabrik konsentrat heavy rare-earth terintegrasi di Pahang dan fasilitas separation hilir di Gebeng yang memproduksi neodymium, dysprosium, dan terbium oxides untuk custo... Berikut yang saya butuhkan dari Anda secara persis. Bingkai situasi AELB renewal + China REE export curb dalam bahasa sederhana untuk Direktur Utama Grup. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. catatan saya dari rapat krisis pagi. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. nota 1 halaman dengan bagian — Headline, Apa yang Terjadi, Posisi Pemangku Kepentingan, 5 Pertanyaan Direksi, 3 Keputusan Direktur Utama dalam 48 Jam. Nada: tenang, presisi, hindari jargon industri. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'},
        {'instr':'', 'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. Audiens ExCo internal + pemangku kepentingan eksternal kunci. Berikut yang saya butuhkan dari Anda secara persis. Pembukaan lisan 90 detik untuk briefing pemangku kepentingan Zava Rare Earth. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. hanya fakta yang sudah dipublikasi. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. Buka dengan pengakuan, jelaskan program respons, beri sinyal pemulihan kredibel, akhiri dengan 3 komitmen. Hindari bahasa spekulatif. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'},
        {'instr':'', 'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. clock regulator aktif. Berikut yang saya butuhkan dari Anda secara persis. Bangun peta komunikasi pemangku kepentingan untuk AELB renewal + China REE export curb. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. pemangku kepentingan yang dikenal. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. tabel RAG — Merah hari ini juga, Kuning 24 jam, Hijau pantau. Kolom: Audiens, Channel, Pemilik, Tema Pesan, Timing, Risiko bila Keliru. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'}
      ],
      persona=['Sasha Ouellet','Mod Admin','Hadar Caspit'],
      personaID=['Sasha Ouellet','Mod Admin','Hadar Caspit']),

      tool(T_RESEARCHER, M365_LIC, M365_ACCT, [
        {'instr':'Open `m365.cloud.microsoft/chat` > Agents > **Researcher** > **Critique Mode**. Paste the prompt below.',
         'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. Zava Rare Earth must respond to its regulator imminently. Here is exactly what I need from you. Benchmark how peers (Lynas Malaysia, MMC Corp Mining, Iluka Resources, Northern Minerals) handled comparable AELB renewal + China REE export curb events between 2020 and 2025. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. peer disclosures, regulator filings, industry press. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. For each peer, identify trigger, response timeline, programme adopted, share-price recovery 12 months later. Critique each source. Cite all with publication date. Output as comparison table. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'},
        {'instr':'Open `m365.cloud.microsoft/chat` > Agents > **Researcher** > **Model Council**. Paste the prompt below.',
         'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. must protect regulator standing AND customer trust AND financial position concurrently. Here is exactly what I need from you. 3 most defensible response playbooks for Zava Rare Earth hit by AELB renewal + China REE export curb. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. Researcher Model Council — convene parallel reports from GPT and Claude. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. Surface dissent, mark majority and minority views. Comparison table: Playbook, Council Verdict, Dissenting View, ASEAN Precedent, Implementation Risk. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'}
      ], DESC_RESEARCHER,
      promptsID=[
        {'instr':'Buka `m365.cloud.microsoft/chat` > Agents > **Researcher** > **Critique Mode**. Tempel prompt.',
         'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. Zava Rare Earth harus respons ke regulator segera. Berikut yang saya butuhkan dari Anda secara persis. Benchmark bagaimana peer (Lynas Malaysia, MMC Corp Mining, Iluka Resources, Northern Minerals) menangani peristiwa AELB renewal + China REE export curb sebanding antara 2020 hingga 2025. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. pengungkapan peer, filing regulator, pers industri. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. Untuk tiap peer identifikasi pemicu, timeline respons, program yang diadopsi, pemulihan harga saham 12 bulan kemudian. Kritisi tiap sumber. Cantumkan kutipan lengkap dengan tanggal. Hasilkan tabel perbandingan. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'},
        {'instr':'Buka `m365.cloud.microsoft/chat` > Agents > **Researcher** > **Model Council**. Tempel prompt.',
         'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. harus melindungi posisi regulator DAN kepercayaan customer DAN posisi finansial sekaligus. Berikut yang saya butuhkan dari Anda secara persis. 3 playbook respons paling defensible untuk Zava Rare Earth yang terkena AELB renewal + China REE export curb. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. Model Council — gelar laporan paralel dari GPT dan Claude. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. Sorot perbedaan pendapat, tandai mayoritas dan minoritas. Tabel perbandingan: Playbook, Putusan Council, Pandangan Minoritas, Preseden ASEAN, Risiko Implementasi. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'}
      ],
      persona=['Mod Admin','Mod Admin'],
      personaID=['Mod Admin','Mod Admin']),

      tool(T_ANALYST, M365_LIC, M365_ACCT, [
        {'instr':'Open `m365.cloud.microsoft/chat` > Agents > **Analyst**. Upload /RE_01_AELB_Compliance_Tracker.xlsx AND /RE_04_Customer_Pricing_Model.xlsx. Paste the prompt below.',
         'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. Group ExCo needs an evidence-based view in 48 hours. Here is exactly what I need from you. Quantify the AELB renewal + China REE export curb financial and operational impact. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. the 2 uploaded files. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. (1) RAG bar chart of at-risk items by severity; (2) waterfall of MYR EBITDA impact; (3) tracker by stakeholder/segment, flag worst <10% headroom as Red. Output a Board-ready RAG dashboard. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'}
      ], DESC_ANALYST,
      promptsID=[
        {'instr':'Buka `m365.cloud.microsoft/chat` > Agents > **Analyst**. Unggah /RE_01_AELB_Compliance_Tracker.xlsx DAN /RE_04_Customer_Pricing_Model.xlsx. Tempel prompt.',
         'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. ExCo Grup butuh pandangan berbasis bukti dalam 48 jam. Berikut yang saya butuhkan dari Anda secara persis. Kuantifikasi dampak finansial dan operasional dari AELB renewal + China REE export curb. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. 2 file yang diunggah. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. (1) Bar chart RAG item at-risk berdasarkan severity; (2) waterfall dampak EBITDA RM; (3) tracker per stakeholder/segmen, tandai headroom terburuk <10% Merah. Hasilkan dashboard RAG siap-Direksi. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'}
      ],
      persona=['Hadar Caspit'],
      personaID=['Hadar Caspit']),

      tool(T_EXCEL, M365_LIC, M365_ACCT, [
        {'instr':'Open `/RE_01_AELB_Compliance_Tracker.xlsx` in Excel for the Web. Open the **Copilot pane**. Paste the prompt below.',
         'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. Audit Committee meets in the next 14 days. Here is exactly what I need from you. Build a single Audit-Committee-ready dashboard sheet. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. combine all relevant tabs. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. New sheet "AC Dashboard" with KPI tiles, bar chart by severity, sparkline column. RAG conditional formatting. Do not modify source tabs. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'}
      ], '',
      promptsID=[
        {'instr':'Buka `/RE_01_AELB_Compliance_Tracker.xlsx` di Excel for the Web. Buka **Copilot pane**. Tempel prompt.',
         'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. Komite Audit rapat dalam 14 hari ke depan. Berikut yang saya butuhkan dari Anda secara persis. Bangun satu sheet dashboard siap-Komite Audit. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. gabungkan semua tab yang relevan. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. Sheet baru "AC Dashboard" dengan KPI tile, bar chart per severity, kolom sparkline. Format kondisional RAG. Jangan modifikasi tab sumber. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'}
      ],
      persona=['Hadar Caspit'],
      personaID=['Hadar Caspit']),

      tool(T_WORD, M365_LIC, M365_ACCT, [
        {'instr':'Open a new blank Word doc in Word for the Web. Open the **Copilot pane**. Reference /RE_03_Civil_Society_Engagement.docx and /RE_05_Bursa_Operational_Update.docx using `/`. Paste the prompt below.',
         'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. AELB renewal + China REE export curb active. Here is exactly what I need from you. Draft the regulator-grade response brief (4 pages). Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. the referenced docs + my notes. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. Sections — Material Facts, Current Status, Programme, Financial Impact Range, Forward-Looking Statements with explicit risk language. Tone: factual, regulator-grade, no speculation. Cite source files at the end of each section. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'}
      ], DESC_WORD,
      promptsID=[
        {'instr':'Buka dokumen Word baru kosong di Word for the Web. Buka **Copilot pane**. Referensikan /RE_03_Civil_Society_Engagement.docx dan /RE_05_Bursa_Operational_Update.docx menggunakan `/`. Tempel prompt.',
         'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. AELB renewal + China REE export curb aktif. Berikut yang saya butuhkan dari Anda secara persis. Susun brief respons regulator-grade (4 halaman). Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. dokumen yang direferensikan + catatan saya. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. Bagian — Fakta Material, Status Saat Ini, Program, Rentang Dampak Finansial, Pernyataan Forward-Looking dengan bahasa risiko eksplisit. Nada: faktual, regulator-grade, tanpa spekulasi. Kutip file sumber di akhir tiap bagian. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'}
      ],
      persona=['Hadar Caspit'],
      personaID=['Hadar Caspit']),

      tool(T_PPT, M365_LIC, M365_ACCT, [
        {'instr':'Open a new PowerPoint deck in PowerPoint for the Web. Open the **Copilot pane**. Paste the prompt below.',
         'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. AC in 14 days. Here is exactly what I need from you. 8-slide Audit Committee deck on AELB renewal + China REE export curb. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. my brief draft and dashboard. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. Cover; Situation; Status (RAG); Programme (2 slides); Financial Impact; Stakeholder Map; Decisions Requested. Brand colours #B45309 + #0F1C3F, 1 chart per slide. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'}
      ], DESC_PPT,
      promptsID=[
        {'instr':'Buka deck PowerPoint baru di PowerPoint for the Web. Buka **Copilot pane**. Tempel prompt.',
         'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. KA dalam 14 hari. Berikut yang saya butuhkan dari Anda secara persis. Deck 8 slide Komite Audit tentang AELB renewal + China REE export curb. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. draf brief dan dashboard saya. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. Cover; Situasi; Status (RAG); Program (2 slide); Dampak Finansial; Peta Pemangku Kepentingan; Keputusan yang Diminta. Warna brand #B45309 + #0F1C3F, 1 chart per slide. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'}
      ],
      persona=['Sasha Ouellet'],
      personaID=['Sasha Ouellet']),

      tool(T_OUTLOOK, M365_LIC, M365_ACCT, [
        {'instr':'Open Outlook on the Web. Open the email thread "AELB renewal + China REE export curb — Group CFO follow-up". Click the **Copilot icon**. Paste the prompt below.',
         'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. AELB renewal + China REE export curb active. Here is exactly what I need from you. Draft a single email to the Zava Rare Earth ExCo and the relevant operating heads. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. the email thread above and the response programme. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. Subject line, 4 short paragraphs covering — situation, the 3 actions each operating head must complete in 72 hours, the regulator-engagement workstream, the AC date. Tone: firm, supportive, accountable. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'}
      ], DESC_OUTLOOK,
      promptsID=[
        {'instr':'Buka Outlook on the Web. Buka thread email "AELB renewal + China REE export curb — tindak lanjut Direktur Keuangan Grup". Klik **ikon Copilot**. Tempel prompt.',
         'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. AELB renewal + China REE export curb aktif. Berikut yang saya butuhkan dari Anda secara persis. Susun satu email ke ExCo Zava Rare Earth dan kepala operasi yang relevan. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. thread di atas dan program respons. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. Baris subjek, 4 paragraf pendek — situasi, 3 aksi per kepala operasi dalam 72 jam, workstream engagement regulator, tanggal KA. Nada: tegas, suportif, akuntabel. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'}
      ],
      persona=['Hadar Caspit'],
      personaID=['Hadar Caspit']),

      tool(T_TEAMS, M365_LIC, M365_ACCT, 
        [
          {'instr':"**(1) In Teams**, open **Calendar** → click the past meeting **\"New Software Implementation\"**. On the Recap page, walk the audience through the **AI Notes** (auto-summary), the **Custom summary** (Copilot's per-attendee view), and the **Audio recap** (chapter markers with speaker timings). **(2) In Word for the Web**, open a **new blank document**. Type a minutes template at the top — five empty headings: Date and Attendees · Agenda Items · Decisions Taken · Action Items · Risks and Open Questions. **(3) Click the Copilot icon** in the Word ribbon and paste the prompt below — Copilot in Word will reference the meeting recap by name with `/` and fill the template.", 'prompt':"Create meeting minutes for the Teams meeting /New Software Implementation. Use the empty template already on this page and fill each heading from the meeting recap. Sections: (1) Date and Attendees; (2) Agenda Items; (3) Decisions Taken; (4) Action Items with Owner and Due Date; (5) Risks and Open Questions. Quote attendee statements verbatim where the wording matters. Tag any decision that is on the critical path as Critical Path. Save the file as Minutes_New_Software_Implementation.docx in OneDrive."},
          {'instr':'**(1) In Teams**, open **Calendar** → click the past meeting **"Marketing Campaign Performance Review"**. On the Recap page, walk through the **AI Notes**, the **Custom summary**, and the **Audio recap** chapters. **(2) In Word for the Web**, open a **new blank document**. Type a campaign-review minutes template at the top — six empty headings: Date and Attendees · Campaign KPIs Reviewed · Decisions Taken · Action Items · Budget Reallocations · Next Review Date. **(3) Click the Copilot icon** in the Word ribbon and paste the prompt below.', 'prompt':"Create meeting minutes for the Teams meeting /Marketing Campaign Performance Review. Use the empty campaign-review template already on this page. Sections: (1) Date and Attendees; (2) Campaign KPIs Reviewed; (3) Decisions Taken; (4) Action Items with Owner and Due Date; (5) Budget Reallocations Approved; (6) Next Review Date. Quote attendee statements verbatim where the wording matters. Highlight any KPI that missed target by more than 10% in amber. Save the file as Minutes_Marketing_Campaign_Review.docx in OneDrive."},
          {'instr':'**(1) In Teams**, open **Calendar** → click the past meeting **"Negotiating Marketing Contract"**. On the Recap page, walk through the **AI Notes**, the **Custom summary**, and the **Audio recap**. **(2) In Word for the Web**, open a **new blank document**. Type a vendor-negotiation minutes template at the top — seven empty headings: Vendor and Owner · Commercial Terms Discussed · Concessions Offered · Concessions Accepted · Open Items · Approval Thresholds · Next Steps. **(3) Click the Copilot icon** in the Word ribbon and paste the prompt below — then forward the result to Procurement, Legal, and the Group CFO.', 'prompt':"Create meeting minutes for the Teams meeting /Negotiating Marketing Contract. Use the empty vendor-negotiation template already on this page. Sections: (1) Vendor and Owner; (2) Commercial Terms Discussed; (3) Concessions Offered; (4) Concessions Accepted; (5) Open Items; (6) Approval Thresholds (CFO / Board); (7) Next Steps with Owner and Due Date. Highlight any term requiring CFO sign-off in amber and any term requiring Board sign-off in red. Save the file as Minutes_Marketing_Contract_Negotiation.docx in OneDrive and email the link to Procurement, Legal, and the Group CFO."}
        ], DESC_TEAMS,
        promptsID=[
          {'instr':'**(1) Di Teams**, buka **Calendar** → klik rapat **"New Software Implementation"**. Di halaman Recap, jelaskan ke peserta tentang **AI Notes** (ringkasan otomatis), **Custom summary** (tampilan per-peserta dari Copilot), dan **Audio recap** (penanda bab dengan timing pembicara). **(2) Di Word for the Web**, buka **dokumen kosong baru**. Ketik kerangka notulen di bagian atas — lima heading kosong: Tanggal dan Peserta · Agenda · Keputusan · Action Items · Risiko dan Pertanyaan Terbuka. **(3) Klik ikon Copilot** di ribbon Word lalu tempelkan prompt di bawah — Copilot in Word akan merujuk recap rapat dengan `/` dan mengisi template.', 'prompt':"Susun notulen rapat untuk rapat Teams /New Software Implementation. Gunakan template kosong yang sudah ada di halaman ini dan isi tiap heading dari recap rapat. Bagian: (1) Tanggal dan Peserta; (2) Agenda; (3) Keputusan; (4) Action Items dengan Owner dan Due Date; (5) Risiko dan Pertanyaan Terbuka. Kutip pernyataan peserta apa adanya bila kata-katanya penting. Tandai keputusan di jalur kritis sebagai Critical Path. Simpan file sebagai Minutes_New_Software_Implementation.docx di OneDrive."},
          {'instr':'**(1) Di Teams**, buka **Calendar** → klik rapat **"Marketing Campaign Performance Review"**. Di halaman Recap, jelaskan **AI Notes**, **Custom summary**, dan **Audio recap**. **(2) Di Word for the Web**, buka dokumen kosong baru. Ketik kerangka notulen tinjauan kampanye — enam heading kosong: Tanggal dan Peserta · KPI Kampanye yang Dikaji · Keputusan · Action Items · Realokasi Anggaran · Jadwal Tinjauan Berikutnya. **(3) Klik ikon Copilot** di ribbon Word lalu tempelkan prompt di bawah.', 'prompt':"Susun notulen rapat untuk rapat Teams /Marketing Campaign Performance Review. Gunakan template kosong tinjauan kampanye yang sudah ada. Bagian: (1) Tanggal dan Peserta; (2) KPI Kampanye yang Dikaji; (3) Keputusan; (4) Action Items dengan Owner dan Due Date; (5) Realokasi Anggaran yang Disetujui; (6) Jadwal Tinjauan Berikutnya. Kutip pernyataan peserta apa adanya. Tandai KPI yang meleset >10% dengan amber. Simpan sebagai Minutes_Marketing_Campaign_Review.docx di OneDrive."},
          {'instr':'**(1) Di Teams**, buka **Calendar** → klik rapat **"Negotiating Marketing Contract"**. Di halaman Recap, jelaskan **AI Notes**, **Custom summary**, dan **Audio recap**. **(2) Di Word for the Web**, buka dokumen kosong baru. Ketik kerangka notulen negosiasi vendor — tujuh heading kosong: Vendor dan Owner · Term Komersial · Konsesi yang Ditawarkan · Konsesi yang Diterima · Item Terbuka · Threshold Persetujuan · Langkah Berikutnya. **(3) Klik ikon Copilot** di ribbon Word lalu tempelkan prompt di bawah — kemudian teruskan hasilnya ke Procurement, Legal, dan Direktur Keuangan Grup.', 'prompt':"Susun notulen rapat untuk rapat Teams /Negotiating Marketing Contract. Gunakan template kosong negosiasi vendor yang sudah ada. Bagian: (1) Vendor dan Owner; (2) Term Komersial; (3) Konsesi yang Ditawarkan; (4) Konsesi yang Diterima; (5) Item Terbuka; (6) Threshold Persetujuan (CFO / Direksi); (7) Langkah Berikutnya dengan Owner dan Due Date. Tandai term yang memerlukan persetujuan CFO dengan amber dan persetujuan Direksi dengan merah. Simpan sebagai Minutes_Marketing_Contract_Negotiation.docx di OneDrive lalu email link-nya ke Procurement, Legal, dan Direktur Keuangan Grup."}
        ],
        promptsBM=[
          {'instr':'**(1) Di Teams**, buka **Calendar** → klik mesyuarat **"New Software Implementation"**. Pada halaman Recap, terangkan kepada hadirin tentang **AI Notes** (ringkasan automatik), **Custom summary** (paparan per-hadirin dari Copilot), dan **Audio recap** (penanda bab dengan masa pembicara). **(2) Di Word for the Web**, buka **dokumen kosong baharu**. Taip rangka minit di bahagian atas — lima tajuk kosong: Tarikh dan Hadirin · Agenda · Keputusan · Tindakan · Risiko dan Soalan Terbuka. **(3) Klik ikon Copilot** di ribbon Word dan tampal prompt di bawah — Copilot in Word akan merujuk recap mesyuarat dengan `/` dan mengisi templat.', 'prompt':"Hasilkan minit mesyuarat untuk mesyuarat Teams /New Software Implementation. Gunakan templat kosong yang sudah ada di halaman ini dan isi setiap tajuk daripada recap mesyuarat. Bahagian: (1) Tarikh dan Hadirin; (2) Agenda; (3) Keputusan; (4) Tindakan dengan Pemilik dan Tarikh; (5) Risiko dan Soalan Terbuka. Petik kenyataan hadirin sebagaimana asal di mana perkataannya penting. Tandakan sebarang keputusan di laluan kritikal sebagai Critical Path. Simpan fail sebagai Minutes_New_Software_Implementation.docx di OneDrive."},
          {'instr':'**(1) Di Teams**, buka **Calendar** → klik mesyuarat **"Marketing Campaign Performance Review"**. Pada halaman Recap, terangkan **AI Notes**, **Custom summary**, dan **Audio recap**. **(2) Di Word for the Web**, buka dokumen kosong baharu. Taip rangka minit ulasan kempen — enam tajuk kosong: Tarikh dan Hadirin · KPI Kempen yang Diulas · Keputusan · Tindakan · Pelarasan Bajet · Tarikh Ulasan Berikutnya. **(3) Klik ikon Copilot** di ribbon Word dan tampal prompt di bawah.', 'prompt':"Hasilkan minit mesyuarat untuk mesyuarat Teams /Marketing Campaign Performance Review. Gunakan templat kosong ulasan kempen yang sudah ada. Bahagian: (1) Tarikh dan Hadirin; (2) KPI Kempen yang Diulas; (3) Keputusan; (4) Tindakan dengan Pemilik dan Tarikh; (5) Pelarasan Bajet yang Diluluskan; (6) Tarikh Ulasan Berikutnya. Petik kenyataan hadirin sebagaimana asal. Tandakan KPI yang tersasar >10% dengan amber. Simpan sebagai Minutes_Marketing_Campaign_Review.docx di OneDrive."},
          {'instr':'**(1) Di Teams**, buka **Calendar** → klik mesyuarat **"Negotiating Marketing Contract"**. Pada halaman Recap, terangkan **AI Notes**, **Custom summary**, dan **Audio recap**. **(2) Di Word for the Web**, buka dokumen kosong baharu. Taip rangka minit perundingan vendor — tujuh tajuk kosong: Vendor dan Pemilik · Terma Komersial · Konsesi Ditawarkan · Konsesi Diterima · Item Terbuka · Ambang Kelulusan · Langkah Seterusnya. **(3) Klik ikon Copilot** di ribbon Word dan tampal prompt di bawah — kemudian majukan hasilnya kepada Procurement, Legal dan Pengarah Kewangan Kumpulan.', 'prompt':"Hasilkan minit mesyuarat untuk mesyuarat Teams /Negotiating Marketing Contract. Gunakan templat kosong perundingan vendor yang sudah ada. Bahagian: (1) Vendor dan Pemilik; (2) Terma Komersial; (3) Konsesi Ditawarkan; (4) Konsesi Diterima; (5) Item Terbuka; (6) Ambang Kelulusan (CFO / Lembaga); (7) Langkah Seterusnya dengan Pemilik dan Tarikh. Tandakan terma yang memerlukan kelulusan CFO dengan amber dan Lembaga dengan merah. Simpan sebagai Minutes_Marketing_Contract_Negotiation.docx di OneDrive dan e-mel pautan kepada Procurement, Legal dan Pengarah Kewangan Kumpulan."}
        ],
        persona=['Sasha Ouellet', 'Sasha Ouellet', 'Sasha Ouellet'],
        personaID=['Sasha Ouellet', 'Sasha Ouellet', 'Sasha Ouellet']
      ),

      tool(T_NOTEBOOK, M365_LIC, M365_ACCT, [
        {'instr':'All sources are loaded. Type the prompt below in the notebook chat.',
         'prompt':'Synthesise across all sources to produce a 10-bullet Audit Committee narrative. Cover: AELB renewal + China REE export curb status, programme, financial impact, stakeholder map, decisions requested. Cite the source file at the end of every bullet.'},
        {'instr':'Click **Quick Create** > **Audio Overview** to generate a 6-minute briefing podcast.',
         'prompt':'Quick Create: Audio Overview, 6 minutes, formal narration tone, focused on the AC narrative above. Listeners are the Zava Rare Earth operating heads preparing for tomorrow morning huddles.'}
      ], DESC_NOTEBOOK,
      promptsID=[
        {'instr':'Semua sumber sudah dimuat. Ketik prompt di bawah pada chat notebook.',
         'prompt':'Sintesakan dari semua sumber untuk menghasilkan narasi Komite Audit 10-bullet. Cakup: status AELB renewal + China REE export curb, program, dampak finansial, peta pemangku kepentingan, keputusan yang diminta. Kutip file sumber di akhir tiap bullet.'},
        {'instr':'Klik **Quick Create** > **Audio Overview** untuk menghasilkan podcast briefing 6 menit.',
         'prompt':'Quick Create: Audio Overview, 6 menit, gaya narasi formal, fokus pada narasi KA di atas. Pendengar adalah kepala operasi Zava Rare Earth yang menyiapkan huddle pagi besok.'}
      ],
      persona=['Mod Admin','Mod Admin'],
      personaID=['Mod Admin','Mod Admin'],
      notebookMeta={
        'sources':['/RE_01_AELB_Compliance_Tracker.xlsx', '/RE_02_TENORM_Residue_Inventory.xlsx', '/RE_03_Civil_Society_Engagement.docx', '/RE_04_Customer_Pricing_Model.xlsx', '/RE_05_Bursa_Operational_Update.docx'],
        'instructions':'You are the Group CFO of Zava Rare Earth preparing an Audit Committee pack on AELB renewal + China REE export curb. Always cite the source file and tab/section. Tone: precise, regulator-grade, no speculation. Use MYR for the Group totals (1 MYR ≈ 3,580 IDR).',
        'instructionsID':'Anda adalah Direktur Keuangan Grup Zava Rare Earth yang menyiapkan paket Komite Audit untuk AELB renewal + China REE export curb. Selalu kutip file sumber dan tab/bagian. Nada: presisi, regulator-grade, tanpa spekulasi. Gunakan MYR untuk total Grup (1 MYR ≈ 3.580 IDR).'
      }),

      tool(T_COWORK, FRONTIER_LIC, M365_ACCT, [
        {'instr':'Open `m365.cloud.microsoft` > Agents > **Cowork**. Paste the single prompt below — Cowork delegates 5 parallel sub-tasks. Frontier required.',
         'prompt':'Cowork — AELB + China REE 14-Day Sprint. Run these in parallel: (1) 📝 Draft Word — regulator response brief 4 pages, source /RE_01_AELB_Compliance_Tracker.xlsx, /RE_02_TENORM_Residue_Inventory.xlsx, /RE_03_Civil_Society_Engagement.docx, /RE_04_Customer_Pricing_Model.xlsx, /RE_05_Bursa_Operational_Update.docx. (2) 📝 Draft Word — internal ExCo briefing memo 2 pages, same sources. (3) ✉️ Send email to Zava Rare Earth ExCo and operating heads with the 3 actions in 72h. (4) 📅 Schedule 90-min AC Pre-Read tomorrow 8am MYT. (5) 💬 Post Teams message to #group-exco with one-line headline + dashboard link. Use these named recipients consistently across the email task and the Teams meeting task — Hadar (Group CFO), Sasha (Group Chief of Staff), Daichi (Head of Investor Relations), Sonia (Head of Strategy), Will (Head of Risk) and Omar (Head of Procurement) — and adapt the precise distribution per sub-task to keep each communication focused on the right audience.'}
      ], DESC_COWORK,
      promptsID=[
        {'instr':'Buka `m365.cloud.microsoft` > Agents > **Cowork**. Tempel prompt tunggal — Cowork mendelegasikan 5 sub-tugas paralel. Frontier diperlukan.',
         'prompt':'Cowork — AELB + China REE 14-Day Sprint. Jalankan paralel: (1) 📝 Susun Word — brief respons regulator 4 halaman, sumber /RE_01_AELB_Compliance_Tracker.xlsx, /RE_02_TENORM_Residue_Inventory.xlsx, /RE_03_Civil_Society_Engagement.docx, /RE_04_Customer_Pricing_Model.xlsx, /RE_05_Bursa_Operational_Update.docx. (2) 📝 Susun Word — memo briefing ExCo internal 2 halaman, sumber sama. (3) ✉️ Kirim email ke ExCo Zava Rare Earth dan kepala operasi dengan 3 aksi dalam 72 jam. (4) 📅 Jadwalkan AC Pre-Read 90 menit besok 08:00 WIB. (5) 💬 Posting pesan Teams di #group-exco dengan headline satu baris + tautan dashboard. Use these named recipients consistently across the email task and the Teams meeting task — Hadar (Group CFO), Sasha (Group Chief of Staff), Daichi (Head of Investor Relations), Sonia (Head of Strategy), Will (Head of Risk) and Omar (Head of Procurement) — and adapt the precise distribution per sub-task to keep each communication focused on the right audience.'}
      ],
      persona=['Mod Admin'],
      personaID=['Mod Admin']),

      tool(T_WORD_AGT, ANY_LIC, ANY_ACCT, [
        {'instr':'Open `m365.cloud.microsoft/chat` → Agents tab → **Word Agent**. Paste the prompt below — the agent returns a fully drafted .docx.',
         'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. AELB renewal + China REE export curb. Here is exactly what I need from you. Generate a 4-page CFO Crisis Brief in Word. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. /RE_01_AELB_Compliance_Tracker.xlsx AND /RE_04_Customer_Pricing_Model.xlsx. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. Sections — Executive Summary 5 bullets; Current Status; Programme; Financial Impact; Stakeholder Map; Decisions requested. Tone: precise, regulator-grade. Save as AELB_Bursa_Brief.docx. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'}
      ], DESC_WORD_AGT,
      promptsID=[
        {'instr':'Buka `m365.cloud.microsoft/chat` → tab Agents → **Word Agent**. Tempel prompt — agent mengembalikan .docx yang sudah didraf penuh.',
         'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. AELB renewal + China REE export curb. Berikut yang saya butuhkan dari Anda secara persis. Hasilkan Brief Krisis Direktur Keuangan 4 halaman dalam Word. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. /RE_01_AELB_Compliance_Tracker.xlsx DAN /RE_04_Customer_Pricing_Model.xlsx. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. Bagian — Ringkasan Eksekutif 5 bullet; Status Saat Ini; Program; Dampak Finansial; Peta Pemangku Kepentingan; Keputusan yang diminta. Nada: presisi, regulator-grade. Simpan sebagai Brief_AELB_Bursa.docx. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'}
      ],
      persona=['Sasha Ouellet'],
      personaID=['Sasha Ouellet']),

      tool(T_PPT_AGT, ANY_LIC, ANY_ACCT, [
        {'instr':'Open `m365.cloud.microsoft/chat` → Agents tab → **PowerPoint Agent**. Paste the prompt below.',
         'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. AC in 14 days. Here is exactly what I need from you. 8-slide Audit Committee deck on AELB renewal + China REE export curb. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. /AELB_Bursa_Brief.docx and /RE_01_AELB_Compliance_Tracker.xlsx. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. Cover; Situation; Status RAG; Programme (2); Financial Impact; Stakeholder Map; Decisions. Brand #B45309 + #0F1C3F, 1 chart/slide. Save as AELB_AC_Deck.pptx. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'}
      ], DESC_PPT_AGT,
      promptsID=[
        {'instr':'Buka `m365.cloud.microsoft/chat` → tab Agents → **PowerPoint Agent**. Tempel prompt.',
         'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. KA dalam 14 hari. Berikut yang saya butuhkan dari Anda secara persis. Deck 8 slide Komite Audit tentang AELB renewal + China REE export curb. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. /Brief_AELB_Bursa.docx dan /RE_01_AELB_Compliance_Tracker.xlsx. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. Cover; Situasi; Status RAG; Program (2); Dampak Finansial; Peta Pemangku Kepentingan; Keputusan. Brand #B45309 + #0F1C3F, 1 chart/slide. Simpan sebagai Deck_KA_AELB.pptx. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'}
      ],
      persona=['Sasha Ouellet'],
      personaID=['Sasha Ouellet']),

      tool(T_XL_AGT, ANY_LIC, ANY_ACCT, [
        {'instr':'Open `m365.cloud.microsoft/chat` → Agents tab → **Excel Agent**. Paste the prompt below.',
         'prompt':'I am working under a tight deadline and the work product needs to be airtight, so please be thorough rather than terse. Operating tracker for the Group COO. Here is exactly what I need from you. Build a AELB renewal + China REE export curb response control tracker workbook. Ground every part of your answer in the inputs that follow, and walk through them methodically rather than skimming. schema only. When you reply, organise the output as described below so I can lift it straight into my deliverable without reformatting. Sheet 1 Issue Log, Sheet 2 Programme Milestones, Sheet 3 Cost Tracker, Sheet 4 Dashboard with KPI tiles + RAG conditional formatting. Save as AELB_Compliance_Tracker.xlsx. Be specific, attach a citation or sheet/tab/cell reference to every quantitative claim, and if anything is missing or contradictory call it out explicitly with the question I should ask next so nothing slips before the deadline.'}
      ], DESC_XL_AGT,
      promptsID=[
        {'instr':'Buka `m365.cloud.microsoft/chat` → tab Agents → **Excel Agent**. Tempel prompt.',
         'prompt':'Saya sedang mengerjakan ini dengan tenggat yang ketat dan hasil akhirnya harus rapi, jadi mohon jawab dengan tuntas, jangan ringkas. tracker operasi untuk Direktur Operasional Grup. Berikut yang saya butuhkan dari Anda secara persis. Bangun workbook tracker kendali respons AELB renewal + China REE export curb. Grounding setiap bagian jawaban Anda pada masukan berikut, telaah satu per satu, jangan dilewati. hanya skema. Saat menjawab, susun keluaran sesuai format di bawah ini agar dapat langsung saya gunakan di deliverable tanpa perlu format ulang. Sheet 1 Log Isu, Sheet 2 Milestone Program, Sheet 3 Tracker Biaya, Sheet 4 Dashboard dengan KPI tile + format kondisional RAG. Simpan sebagai Tracker_Kepatuhan_AELB.xlsx. Tegas, cantumkan kutipan atau referensi sheet/tab/cell untuk setiap angka, dan bila ada yang kurang atau bertentangan, sebutkan secara eksplisit beserta pertanyaan tindak lanjut yang harus saya ajukan agar tidak ada yang terlewat sebelum tenggat.'}
      ],
      persona=['Hadar Caspit'],
      personaID=['Hadar Caspit']),

      tool_builder(M365_LIC, M365_ACCT,
        agents=[
        {
          'icon': '🪨',
          'label': 'Resource Block Geology',
          'name': 'Zava Rare-Earth — Resource Block & Geology Coach',
          'desc': 'Tracks Rare-Earth & Metals resource-block grade, drill-hole results, and reserve-recovery factor.',
          'instructions': 'You are the Zava Rare-Earth & Metals Resource Block Geology Coach. You support the Chief Geologist. Scan drill-hole data (RE_01_AELB_Compliance_Tracker.xlsx) and the resource model (RE_02_TENORM_Residue_Inventory.xlsx) for grade variability, reserve-recovery factor, and block-prioritisation. Recommend drill-program changes per finding.',
          'knowledge': [
            {'file':'RE_01_AELB_Compliance_Tracker.xlsx', 'note':'Drill-hole register and assay data.'},
            {'file':'RE_02_TENORM_Residue_Inventory.xlsx', 'note':'Resource model and reserve estimate.'},
            {'file':'RE_04_Customer_Pricing_Model.xlsx', 'note':'Mining plan and pit-sequence.'}
          ],
          'knowledgeNote': 'Test: "Which resource blocks at Rare-Earth & Metals are showing the largest reserve-grade variance?"',
          'queries': [
            'Top 5 blocks by grade variance — recommended drill program.',
            'Which blocks have priority for next-pit sequencing? Recommend mining plan update.',
            'Draft the quarterly Geology Steering Committee paper.'
          ],
        },
        {
          'icon': '📦',
          'label': 'Export Compliance',
          'name': 'Zava Rare-Earth — Critical-Minerals Export Compliance',
          'desc': 'Manages Rare-Earth & Metals critical-minerals export licensing, downstream-processing compliance, and offtake KYC.',
          'instructions': 'You are the Zava Rare-Earth & Metals Critical-Minerals Export Compliance agent. Manage export licensing, downstream-processing compliance, and offtake KYC grounded on the regulatory file (RE_03_Civil_Society_Engagement.docx) and the offtake register (RE_05_Bursa_Operational_Update.docx). Quote every clause.',
          'knowledge': [
            {'file':'RE_03_Civil_Society_Engagement.docx', 'note':'Export licensing dossier.'},
            {'file':'RE_05_Bursa_Operational_Update.docx', 'note':'Offtake counterparty register.'}
          ],
          'knowledgeNote': 'Test: "Which Rare-Earth & Metals offtake counterparties have an open KYC gap?"',
          'queries': [
            "List open KYC gaps for the next quarter's scheduled offtakes.",
            'Which export licences are within 60 days of expiry? Tabulate and trigger renewal.',
            "Draft the response letter to the regulator's latest export-permit query."
          ],
        },
        {
          'icon': '🛡️',
          'label': 'Strategic Mineral Liaison',
          'name': 'Zava Rare-Earth — Strategic-Mineral Government Liaison',
          'desc': 'Manages stakeholder coordination with MITI / Kemenperin, defence agencies, and ESG financiers for Rare-Earth & Metals.',
          'instructions': 'You are the Zava Rare-Earth & Metals Strategic-Mineral Government Liaison. Manage briefings to MITI / Kemenperin / Ministry of Defence / ESG financiers grounded on the briefing-note file (RE_04_Customer_Pricing_Model.xlsx). Tone is sovereignty-aware, conservative.',
          'knowledge': [
            {'file':'RE_04_Customer_Pricing_Model.xlsx', 'note':'Government briefing-note archive.'}
          ],
          'knowledgeNote': 'Test: "Draft talking points for the next MITI ministerial briefing for Rare-Earth & Metals."',
          'queries': [
            'Build briefing pack for next ministerial visit.',
            'Which stakeholder concerns require a holding line? Build a Q&A pack.',
            'Draft the strategic-minerals position paper for the inter-ministerial committee.'
          ],
        }
      ],
        agentsID=[
        {
          'icon': '🪨',
          'label': 'Resource Block Geology',
          'name': 'Zava Rare-Earth — Resource Block & Geology Pelatih',
          'desc': 'Memantau Rare-Earth & Metals resource-block grade, drill-hole results, and reserve-recovery factor.',
          'instructions': 'Anda adalah Zava Rare-Earth & Metals Resource Block Geology Pelatih. Anda mendukung the Chief Geologist. Scan drill-hole data (RE_01_AELB_Compliance_Tracker.xlsx) and the resource model (RE_02_TENORM_Residue_Inventory.xlsx) for grade variability, reserve-recovery factor, and block-prioritisation. Rekomendasikan drill-program changes per finding.',
          'knowledge': [
            {'file':'RE_01_AELB_Compliance_Tracker.xlsx', 'note':'Drill-hole register and assay data.'},
            {'file':'RE_02_TENORM_Residue_Inventory.xlsx', 'note':'Resource model and reserve estimate.'},
            {'file':'RE_04_Customer_Pricing_Model.xlsx', 'note':'Mining plan and pit-sequence.'}
          ],
          'knowledgeNote': 'Test: "Yang mana resource blocks at Rare-Earth & Metals are showing terbesar reserve-grade variance?"',
          'queries': [
            '5 teratas blocks by grade variance — recommended drill program.',
            'Yang mana blocks have priority for next-pit sequencing? Rekomendasikan mining plan update.',
            'Susun the kuartalan Geology Komite Pengarah paper.'
          ],
        },
        {
          'icon': '📦',
          'label': 'Export Compliance',
          'name': 'Zava Rare-Earth — Critical-Minerals Export Compliance',
          'desc': 'Manages Rare-Earth & Metals critical-minerals export licensing, downstream-processing compliance, and offtake KYC.',
          'instructions': 'Anda adalah Zava Rare-Earth & Metals Critical-Minerals Export Compliance agen. Manage export licensing, downstream-processing compliance, and offtake KYC grounded on the regulatory file (RE_03_Civil_Society_Engagement.docx) and the offtake register (RE_05_Bursa_Operational_Update.docx). Quote every clause.',
          'knowledge': [
            {'file':'RE_03_Civil_Society_Engagement.docx', 'note':'Export licensing dossier.'},
            {'file':'RE_05_Bursa_Operational_Update.docx', 'note':'Offtake counterparty register.'}
          ],
          'knowledgeNote': 'Test: "Yang mana Rare-Earth & Metals offtake counterparties have an open KYC gap?"',
          'queries': [
            "List open KYC gaps for berikutnya quarter's scheduled offtakes.",
            'Yang mana export licences are within 60 days of expiry? Tabulasikan and trigger renewal.',
            "Susun the response letter to the regulator's latest export-permit query."
          ],
        },
        {
          'icon': '🛡️',
          'label': 'Strategic Mineral Penghubung',
          'name': 'Zava Rare-Earth — Strategic-Mineral Government Penghubung',
          'desc': 'Manages stakeholder coordination with MITI / Kemenperin, defence agencies, and ESG financiers for Rare-Earth & Metals.',
          'instructions': 'Anda adalah Zava Rare-Earth & Metals Strategic-Mineral Government Penghubung. Manage briefings to MITI / Kemenperin / Ministry of Defence / ESG financiers grounded on the briefing-note file (RE_04_Customer_Pricing_Model.xlsx). Tone is sovereignty-aware, conservative.',
          'knowledge': [
            {'file':'RE_04_Customer_Pricing_Model.xlsx', 'note':'Government briefing-note archive.'}
          ],
          'knowledgeNote': 'Test: "Susun talking points for berikutnya MITI ministerial briefing for Rare-Earth & Metals."',
          'queries': [
            'Bangun briefing pack for next ministerial visit.',
            'Yang mana stakeholder concerns require a holding line? Bangun a Q&A pack.',
            'Susun the strategic-minerals position paper for the inter-ministerial committee.'
          ],
        }
      ],
        persona=['Mod Admin', 'Mod Admin', 'Mod Admin'],
        personaID=['Mod Admin', 'Mod Admin', 'Mod Admin']
      ),
    ],
    companyID='Zava Rare Earth',
    taglineID='Pembaruan persetujuan lingkungan JAEC + curb ekspor REE Tiongkok — update Bursa dalam 14 hari.',
    scenarioID='Zava Rare Earth mengoperasikan pabrik konsentrat heavy rare-earth terintegrasi di Pahang dan fasilitas separation hilir di Gebeng yang memproduksi neodymium, dysprosium, dan terbium oxides untuk customer magnet EV dan turbin angin global. Pembaruan persetujuan lingkungan Atomic Energy Licensing Board (AELB) jatuh tempo dalam 90 hari; pemangku kepentingan masyarakat sipil mengangkat kekhawatiran residu TENORM. MOFCOM Tiongkok memperketat lisensi ekspor REE secara paralel, mendorong pricing global naik 28% dalam 4 minggu. Bursa Malaysia mengharapkan update operasional dalam 14 hari. Direktur Keuangan Grup butuh narasi teknis JAEC/AELB, rencana engagement masyarakat sipil, analisis pricing pass-through customer, dan pengungkapan Bursa semuanya terkoordinasi. Frame customer riil: grup ini beroperasi serupa dengan Lynas Malaysia dan MMC Corp Mining.',
    relevantDepts=['dept-finance','dept-strategy','dept-esg','dept-legal','dept-operations','dept-risk','dept-corpsec'],
    personas=[
      {'name':'Hadar Caspit','role':'Group CFO','roleID':'Direktur Keuangan Grup','acct':'admin@ABSx62256373.onmicrosoft.com','lic':'Microsoft 365 Copilot','color':'#1E40AF'},
      {'name':'Sasha Ouellet','role':'Group Chief of Staff','roleID':'Kepala Staf Grup','acct':'SashaO@ABSx62256373.OnMicrosoft.com','lic':'Free \u2014 no Microsoft 365 Copilot license','color':'#7C3AED'},
      {'name':'Mod Admin','role':'Group Strategy Director','roleID':'Direktur Strategi Grup','acct':'admin@ABSx62256373.onmicrosoft.com','lic':'Microsoft 365 Copilot','color':'#059669'},
      {'name':'Daichi Maruyama','role':'Group Sustainability & Risk Director','roleID':'Direktur Keberlanjutan & Risiko Grup','acct':'admin@ABSx62256373.onmicrosoft.com','lic':'Microsoft 365 Copilot','color':'#DC2626'}
    ],
    storyboard=[
      {'ex':1,'title':'Research & Brief','titleID':'Riset & Pengarahan','minutes':18,'mode':'Show & Tell + Hands-on',
       'summary':'Frame the AELB renewal + China REE export curb situation and pull peer playbooks before the regulator clock starts ticking.',
       'summaryID':'Bingkai situasi AELB renewal + China REE export curb dan tarik playbook peer sebelum clock regulator mulai berdetak.',
       'tasks':[
         {'verb':'Frame the morning question and lock the day priorities','verbID':'Susun pertanyaan pagi dan kunci prioritas hari ini','toolId':T_CHAT,'mode':'Show & Tell'},
         {'verb':'Run an outside-in peer scan and pull proven plays','verbID':'Lakukan pemindaian peer dari luar dan tarik praktik terbaik','toolId':T_RESEARCHER,'mode':'Show & Tell'},
         {'verb':'Generate a board-ready brief straight from chat','verbID':'Hasilkan brief siap-Direksi langsung dari chat','toolId':T_WORD_AGT,'mode':'Hands-on'}]},
      {'ex':2,'title':'Analyse & Decide','titleID':'Analisis & Putuskan','minutes':18,'mode':'Hands-on',
       'summary':'Quantify AELB renewal + China REE export curb financial and operational impact; build an AC dashboard.',
       'summaryID':'Kuantifikasi dampak finansial dan operasional AELB renewal + China REE export curb; bangun dashboard KA.',
       'tasks':[
         {'verb':'Crunch the numbers and surface the biggest gaps','verbID':'Olah angka dan ungkap celah terbesar','toolId':T_ANALYST,'mode':'Hands-on'},
         {'verb':'Build a single-pane operating dashboard','verbID':'Bangun dashboard operasi satu-halaman','toolId':T_EXCEL,'mode':'Hands-on'},
         {'verb':'Spin up a recurring tracker workbook from chat','verbID':'Buat workbook tracker berulang dari chat','toolId':T_XL_AGT,'mode':'Hands-on'}]},
      {'ex':3,'title':'Communicate & Coordinate','titleID':'Komunikasi & Koordinasi','minutes':18,'mode':'Hands-on',
       'summary':'Brief operating heads, capture the AELB Renewal War Room recap, and assemble the AC deck and regulator response.',
       'summaryID':'Brief kepala operasi, capture recap AELB Renewal War Room, dan rakit deck KA serta respons regulator.',
       'tasks':[
         {'verb':'Draft the stakeholder alignment email','verbID':'Draf email penyelarasan stakeholder','toolId':T_OUTLOOK,'mode':'Hands-on'},
         {'verb':'Recap the meeting and turn it into minutes','verbID':'Recap rapat dan ubah ke notulen','toolId':T_TEAMS,'mode':'Hands-on'},
         {'verb':'Generate a board-ready deck from chat','verbID':'Hasilkan deck siap-Direksi dari chat','toolId':T_PPT_AGT,'mode':'Hands-on'},
         {'verb':'Delegate a 5-task parallel sprint','verbID':'Delegasikan 5-tugas paralel ke Cowork','toolId':T_COWORK,'mode':'Show & Tell'}]},
      {'ex':4,'title':'Build & Scale','titleID':'Bangun & Skala','minutes':15,'mode':'Show & Tell',
       'summary':'Wrap the AELB renewal + China REE export curb playbook into a reusable agent for the Zava Rare Earth operating team.',
       'summaryID':'Bungkus playbook AELB renewal + China REE export curb ke dalam agent reusable untuk tim operasi Zava Rare Earth.',
       'tasks':[
         {'verb':'Pull every source into one synthesis notebook','verbID':'Tarik semua sumber ke satu notebook sintesis','toolId':T_NOTEBOOK,'mode':'Show & Tell'},
         {'verb':'Wrap the daily workflow into a reusable agent','verbID':'Bungkus alur kerja harian jadi agen yang dapat dipakai ulang','toolId':T_BUILDER,'mode':'Show & Tell'}]}
    ],
    geo='MY'
))
