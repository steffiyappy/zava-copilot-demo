# -*- coding: utf-8 -*-
# Industries batch 11 — Automotive vehicle distribution & dealership network
# (Distinct from auto-tyres in batch 10 which is component manufacturing.)
import sys; sys.path.insert(0, '.')
from util import *

INDUSTRIES_11 = []

# ╔══════════════════════════════════════════════════════════════════════╗
# ║  AUTOMOTIVE — Vehicle Distribution & Dealership Network              ║
# ╚══════════════════════════════════════════════════════════════════════╝
INDUSTRIES_11.append(ind(
    'automotive', 'sec-mfg', 'Automotive Distribution & Dealerships', '🚗', '#1F2937', '#0F172A',
    'Zava Motors',
    'Toyota EV-mix shortfall + Honda principal renegotiation + 8 underperforming dealers — Group ExCo in 14 days.',
    "Zava Motors is the Group's automotive distribution and dealership platform with sole-distributor rights for Toyota and Honda passenger vehicles in Malaysia, an authorised Hyundai 3S network in Indonesia, and a newly signed BYD electrified brand partnership (BEV + PHEV). The group operates 92 sales-and-service outlets across both countries (54 in Malaysia, 38 in Indonesia), assembles select CKD models at the Pekan and Bekasi plants, and runs a captive auto-financing arm. Three converging pressures hit at once: (1) Toyota Motor Asia Pacific's 2027 BEV-mix target requires 30% electrified sales but Zava Motors is at 4.1% YTD, with FY2026 capex re-prioritisation needed across the BYD rollout vs the Honda hybrid line; (2) Honda Motor Co. has opened a principal-margin renegotiation seeking to cut ATPM/distributor margin by 150 bps, threatening MYR 84M of FY2026 EBITDA; (3) 8 of the 92 dealers are operating below break-even for 4 consecutive quarters — same-store sales down 11% YoY, F&I attach rate at 38% vs a 55% benchmark. The Group MD needs a Group-ExCo-ready pack in 14 days covering EV-mix recovery scenarios, principal-renegotiation defence, dealer-rationalisation plan, and the MITI Energy-Efficient Vehicle (EEV) / Indonesian Kementerian Perindustrian PPnBM-policy briefing notes. Real customer reference frame: this group operates similarly to **UMW Holdings** (UMW Toyota Motor + Perodua), **Sime Darby Motors** (BMW/Hyundai/Ford/Porsche distribution), **DRB-HICOM** (Honda Malaysia + Proton/Geely), **Bermaz Auto** (Mazda), **MBM Resources** (Perodua dealer + Hino), **Astra International** (Toyota/Daihatsu/Isuzu/BMW + Astra Honda Motor 2-wheel), and **Indomobil Sukses Internasional** (Suzuki/Nissan/Volvo).",
    ['AUTOM_01_EV_Mix_and_Capex_Model.xlsx', 'AUTOM_02_Dealer_PnL_Tracker.xlsx', 'AUTOM_03_Principal_Margin_Renegotiation_Brief.docx', 'AUTOM_04_MITI_EEV_BKPM_PPnBM_Briefing_Pack.docx', 'AUTOM_05_Dealer_Rationalisation_Playbook.docx'],
    [
      tool(T_CHAT, FREE_LIC, FREE_ACCT, [
        {'instr':'', 'prompt':'Goal: Frame the Toyota EV-mix shortfall + Honda principal renegotiation + 8 underperforming dealers situation in plain English for the Group MD. Context: Zava Motors holds Toyota and Honda sole-distributor rights in Malaysia, a Hyundai 3S network in Indonesia, and a new BYD partnership across 92 outlets. EV-mix is at 4.1% vs the Toyota 2027 30% target, Honda is seeking a 150 bps margin cut worth MYR 84M, and 8 dealers have been below break-even for 4 quarters. Source: my notes from the morning principal call. Expectation: 1-page note with sections — Headline, What Happened, Stakeholder Position (Toyota Motor Asia Pacific, Honda Motor Co., dealer principals, MITI, BKPM), Top 5 Questions the Group ExCo Will Ask, 3 Decisions the Group MD Must Take in 48 Hours. Tone: calm, precise, no industry jargon.'},
        {'instr':'', 'prompt':'Goal: 90-second verbal opening for the Zava Motors Group ExCo briefing. Context: Audience is the Group MD, Group CFO, COO, the Toyota and Honda principal liaison heads, and the dealer-network director. Source: published facts only — no speculation about Toyota or Honda intentions beyond what they have communicated in writing. Expectation: Open with acknowledgement of the converging pressures, explain the response programme, signal credible recovery on EV-mix and dealer P&L, end with 3 commitments. Avoid forward-looking statements that could embarrass the Toyota or Honda principal relationships.'},
        {'instr':'', 'prompt':'Goal: Build the stakeholder communication map for the EV-mix shortfall + principal renegotiation + dealer rationalisation programme. Context: Toyota Motor Asia Pacific quarterly review in 14 days, Honda margin-cut response due in 21 days, MITI EEV briefing in 14 days, BKPM Indonesia briefing in 21 days, dealer principals waiting on rationalisation decision. Source: known stakeholders. Expectation: RAG table — Red same-day, Amber 24-72h, Green monitor. Columns: Audience, Channel, Owner, Message Theme, Timing, Risk if Mishandled.'}
      ], DESC_CHAT,
      promptsID=[
        {'instr':'', 'prompt':'Tujuan: Bingkai situasi shortfall EV-mix Toyota + renegosiasi prinsipal Honda + 8 dealer underperform dalam bahasa sederhana untuk Direktur Pelaksana Grup. Konteks: Zava Motors memegang hak sole-distributor Toyota dan Honda di Malaysia, jaringan 3S Hyundai di Indonesia, dan kemitraan BYD baru di 92 outlet. EV-mix 4,1% terhadap target 30% Toyota 2027, Honda meminta potongan margin 150 bps senilai Rp 300 miliar, 8 dealer di bawah break-even selama 4 kuartal. Sumber: catatan saya dari rapat prinsipal pagi. Ekspektasi: nota 1 halaman dengan bagian — Headline, Apa yang Terjadi, Posisi Pemangku Kepentingan (Toyota Motor Asia Pacific, Honda Motor Co., prinsipal dealer, Kemenperin, BKPM, MITI), 5 Pertanyaan Top dari ExCo Grup, 3 Keputusan Direktur Pelaksana Grup dalam 48 Jam. Nada: tenang, presisi, hindari jargon industri.'},
        {'instr':'', 'prompt':'Tujuan: Pembukaan lisan 90 detik untuk briefing ExCo Grup Zava Motors. Konteks: Audiens adalah Direktur Pelaksana Grup, Direktur Keuangan Grup, COO, kepala liaison prinsipal Toyota dan Honda, dan direktur jaringan dealer. Sumber: hanya fakta yang sudah diungkapkan — tidak ada spekulasi tentang niat Toyota atau Honda di luar yang sudah disampaikan tertulis. Ekspektasi: Buka dengan pengakuan tekanan yang bertemu, jelaskan program respons, beri sinyal pemulihan kredibel atas EV-mix dan P&L dealer, akhiri dengan 3 komitmen. Hindari pernyataan forward-looking yang dapat membahayakan hubungan prinsipal Toyota atau Honda.'},
        {'instr':'', 'prompt':'Tujuan: Bangun peta komunikasi pemangku kepentingan untuk program shortfall EV-mix + renegosiasi prinsipal + rasionalisasi dealer. Konteks: review kuartalan Toyota Motor Asia Pacific dalam 14 hari, respons potongan margin Honda dalam 21 hari, briefing EEV MITI dalam 14 hari, briefing BKPM Indonesia dalam 21 hari, prinsipal dealer menunggu keputusan rasionalisasi. Sumber: pemangku kepentingan yang dikenal. Ekspektasi: tabel RAG — Merah hari ini juga, Kuning 24-72 jam, Hijau pantau. Kolom: Audiens, Channel, Pemilik, Tema Pesan, Timing, Risiko bila Keliru.'}
      ],
      persona=['Sasha Ouellet','Mod Admin','Hadar Caspit'],
      personaID=['Sasha Ouellet','Mod Admin','Hadar Caspit']),

      tool(T_RESEARCHER, M365_LIC, M365_ACCT, [
        {'instr':'Open `m365.cloud.microsoft/chat` > Agents > **Researcher** > **Critique Mode**. Paste the prompt below.',
         'prompt':'Goal: Benchmark how peers (UMW Holdings, Sime Darby Motors, DRB-HICOM, Bermaz Auto, MBM Resources, Astra International, Indomobil Sukses Internasional) handled comparable BEV-transition pressure, principal-margin renegotiation, and dealer-network rationalisation events between 2022 and 2025. Context: Zava Motors must respond to Toyota Motor Asia Pacific and Honda Motor Co. on parallel tracks while honouring MITI EEV and BKPM Indonesia commitments. Source: peer disclosures (Bursa Malaysia / IDX), MITI/MIDA/Kementerian Perindustrian press releases, Malaysian Automotive Association (MAA) and Gaikindo Indonesia statistics. Expectation: For each peer, identify trigger event, response timeline, programme adopted (capex re-prioritisation, dealer cull, EV partnership), and outcome 12 months later (sales mix, EBITDA margin, principal relationship status). Critique each source. Cite all with publication date. Output as a comparison table.'},
        {'instr':'Open `m365.cloud.microsoft/chat` > Agents > **Researcher** > **Model Council**. Paste the prompt below.',
         'prompt':'Goal: 3 most defensible response playbooks for Zava Motors hit by simultaneous Toyota EV-mix shortfall + Honda margin renegotiation + dealer rationalisation. Context: must protect Toyota and Honda principal relationships AND BYD partnership AND dealer-principal trust AND financial position concurrently. Source: Researcher Model Council — convene parallel reports from GPT-5.5 Thinking and Claude Opus 4.7. Expectation: Surface dissent across the council, mark majority and minority views. Comparison table: Playbook, Council Verdict, Dissenting View, ASEAN Precedent (cite specific peer transaction year), Implementation Risk.'}
      ], DESC_RESEARCHER,
      promptsID=[
        {'instr':'Buka `m365.cloud.microsoft/chat` > Agents > **Researcher** > **Critique Mode**. Tempel prompt.',
         'prompt':'Tujuan: Benchmark bagaimana peer (UMW Holdings, Sime Darby Motors, DRB-HICOM, Bermaz Auto, MBM Resources, Astra International, Indomobil Sukses Internasional) menangani peristiwa serupa transisi BEV, renegosiasi margin prinsipal, dan rasionalisasi jaringan dealer antara 2022 hingga 2025. Konteks: Zava Motors harus merespons Toyota Motor Asia Pacific dan Honda Motor Co. di jalur paralel sambil menghormati komitmen EEV MITI dan BKPM Indonesia. Sumber: pengungkapan peer (Bursa Malaysia / BEI), siaran pers MITI/MIDA/Kementerian Perindustrian, statistik MAA dan Gaikindo. Ekspektasi: Untuk tiap peer identifikasi peristiwa pemicu, timeline respons, program yang diadopsi (re-prioritisasi capex, cull dealer, kemitraan EV), dan hasil 12 bulan kemudian (mix penjualan, marjin EBITDA, status hubungan prinsipal). Kritisi tiap sumber. Cantumkan kutipan lengkap dengan tanggal. Hasilkan tabel perbandingan.'},
        {'instr':'Buka `m365.cloud.microsoft/chat` > Agents > **Researcher** > **Model Council**. Tempel prompt.',
         'prompt':'Tujuan: 3 playbook respons paling defensible untuk Zava Motors yang menghadapi shortfall EV-mix Toyota + renegosiasi margin Honda + rasionalisasi dealer secara bersamaan. Konteks: harus melindungi hubungan prinsipal Toyota dan Honda DAN kemitraan BYD DAN kepercayaan prinsipal dealer DAN posisi finansial sekaligus. Sumber: Model Council — gelar laporan paralel dari GPT-5.5 Thinking dan Claude Opus 4.7. Ekspektasi: Sorot perbedaan pendapat lintas council, tandai pandangan mayoritas dan minoritas. Tabel perbandingan: Playbook, Putusan Council, Pandangan Minoritas, Preseden ASEAN (kutip transaksi peer spesifik dengan tahun), Risiko Implementasi.'}
      ],
      persona=['Mod Admin','Mod Admin'],
      personaID=['Mod Admin','Mod Admin']),

      tool(T_ANALYST, M365_LIC, M365_ACCT, [
        {'instr':'Open `m365.cloud.microsoft/chat` > Agents > **Analyst**. Upload /AUTOM_01_EV_Mix_and_Capex_Model.xlsx AND /AUTOM_02_Dealer_PnL_Tracker.xlsx. Paste the prompt below.',
         'prompt':'Goal: Quantify the combined impact of Toyota EV-mix shortfall + Honda margin renegotiation + dealer-rationalisation programme on FY2026 and FY2027 EBITDA. Context: Group ExCo needs an evidence-based view in 48 hours covering all three workstreams. Source: the 2 uploaded files — EV mix scenarios across BYD ramp + Toyota hybrid + Honda PHEV; dealer P&L by outlet with same-store-sales, F&I attach rate, and parts-revenue. Expectation: (1) RAG bar chart of the 8 underperforming dealers ranked by FY2026 EBITDA contribution; (2) waterfall of Group EBITDA bridge — Baseline → Honda margin cut → EV-mix capex drag → Dealer rationalisation savings → BYD ramp upside → Recovered EBITDA; (3) sensitivity table on EV-mix achievement (15% / 22% / 30% by FY2027) showing the Toyota principal-relationship risk band per scenario. Output a Group-ExCo-ready RAG dashboard.'}
      ], DESC_ANALYST,
      promptsID=[
        {'instr':'Buka `m365.cloud.microsoft/chat` > Agents > **Analyst**. Unggah /AUTOM_01_EV_Mix_and_Capex_Model.xlsx DAN /AUTOM_02_Dealer_PnL_Tracker.xlsx. Tempel prompt.',
         'prompt':'Tujuan: Kuantifikasi dampak gabungan shortfall EV-mix Toyota + renegosiasi margin Honda + program rasionalisasi dealer terhadap EBITDA FY2026 dan FY2027. Konteks: ExCo Grup butuh pandangan berbasis bukti dalam 48 jam mencakup ketiga workstream. Sumber: 2 file yang diunggah — skenario mix EV lintas ramp BYD + hybrid Toyota + PHEV Honda; P&L dealer per outlet dengan same-store-sales, attach rate F&I, dan revenue parts. Ekspektasi: (1) Bar chart RAG 8 dealer underperform diurutkan berdasarkan kontribusi EBITDA FY2026; (2) waterfall bridge EBITDA Grup — Baseline → potongan margin Honda → drag capex EV-mix → penghematan rasionalisasi dealer → upside ramp BYD → EBITDA pulih; (3) tabel sensitivitas pencapaian EV-mix (15% / 22% / 30% pada FY2027) menampilkan band risiko hubungan prinsipal Toyota per skenario. Hasilkan dashboard RAG siap-ExCo Grup.'}
      ],
      persona=['Hadar Caspit'],
      personaID=['Hadar Caspit']),

      tool(T_EXCEL, M365_LIC, M365_ACCT, [
        {'instr':'Open `/AUTOM_01_EV_Mix_and_Capex_Model.xlsx` in Excel for the Web. Open the **Copilot pane**. Paste the prompt below.',
         'prompt':'Goal: Build a single Group-ExCo-ready dashboard sheet that combines the EV-mix recovery scenarios with the Honda margin defence and the dealer-rationalisation savings. Context: Group ExCo meets in 14 days, the Toyota principal review is on day 14, the Honda response is due on day 21. Source: combine all relevant tabs in this workbook — Vehicle Sales Mix, Capex Schedule, Dealer Network, Principal Margin Schedule. Expectation: New sheet "ExCo Dashboard" with KPI tiles for FY2026 EV-mix %, Honda EBITDA at risk MYR, Dealer Network EBITDA, BYD Pipeline; bar chart of dealers ranked worst to best on EBITDA contribution; line chart of EV-mix trajectory across 3 scenarios (Base / Stretch / Toyota-aligned); RAG conditional formatting; sparkline column. Do not modify source tabs.'}
      ], '',
      promptsID=[
        {'instr':'Buka `/AUTOM_01_EV_Mix_and_Capex_Model.xlsx` di Excel for the Web. Buka **Copilot pane**. Tempel prompt.',
         'prompt':'Tujuan: Bangun satu sheet dashboard siap-ExCo Grup yang menggabungkan skenario pemulihan EV-mix dengan pertahanan margin Honda dan penghematan rasionalisasi dealer. Konteks: ExCo Grup bertemu 14 hari, review prinsipal Toyota pada hari 14, respons Honda pada hari 21. Sumber: gabungkan semua tab terkait — Vehicle Sales Mix, Capex Schedule, Dealer Network, Principal Margin Schedule. Ekspektasi: Sheet baru "Dashboard ExCo" dengan KPI tile untuk EV-mix % FY2026, EBITDA Honda Berisiko Rp, EBITDA Jaringan Dealer, Pipeline BYD; bar chart dealer diurutkan terburuk ke terbaik berdasar kontribusi EBITDA; line chart trajectory EV-mix lintas 3 skenario (Base / Stretch / Selaras-Toyota); format kondisional RAG; kolom sparkline. Jangan modifikasi tab sumber.'}
      ],
      persona=['Hadar Caspit'],
      personaID=['Hadar Caspit']),

      tool(T_WORD, M365_LIC, M365_ACCT, [
        {'instr':'Open a new blank Word doc in Word for the Web. Open the **Copilot pane**. Reference /AUTOM_03_Principal_Margin_Renegotiation_Brief.docx and /AUTOM_05_Dealer_Rationalisation_Playbook.docx using `/`. Paste the prompt below.',
         'prompt':'Goal: Draft the principal-grade response brief to Honda Motor Co. on the proposed 150 bps margin cut (4 pages). Context: Honda margin renegotiation is active and a written response is due in 21 days. Source: the two referenced docs + the Group CFO\'s notes. Expectation: Sections — Material Facts (volume, mix, working-capital cycle, after-sales captive ratio); Current Status of the Honda relationship; Counter-proposal Programme (joint EV-line capex commitment, parts-localisation, after-sales co-investment); Financial Impact Range; Forward-Looking Statements with explicit risk language tying the response to MITI EEV and Kementerian Perindustrian PPnBM commitments. Tone: factual, principal-grade, no speculation. Cite source files at the end of each section.'}
      ], DESC_WORD,
      promptsID=[
        {'instr':'Buka dokumen Word baru kosong di Word for the Web. Buka **Copilot pane**. Referensikan /AUTOM_03_Principal_Margin_Renegotiation_Brief.docx dan /AUTOM_05_Dealer_Rationalisation_Playbook.docx menggunakan `/`. Tempel prompt.',
         'prompt':'Tujuan: Susun brief respons principal-grade ke Honda Motor Co. tentang usulan potongan margin 150 bps (4 halaman). Konteks: renegosiasi margin Honda aktif dan respons tertulis jatuh tempo dalam 21 hari. Sumber: dua dokumen yang direferensikan + catatan Direktur Keuangan Grup. Ekspektasi: Bagian — Fakta Material (volume, mix, siklus modal kerja, rasio captive after-sales); Status Saat Ini hubungan Honda; Program Counter-proposal (komitmen capex jalur EV bersama, lokalisasi parts, ko-investasi after-sales); Rentang Dampak Finansial; Pernyataan Forward-Looking dengan bahasa risiko eksplisit yang mengikat respons pada komitmen EEV MITI dan PPnBM Kementerian Perindustrian. Nada: faktual, principal-grade, tanpa spekulasi. Kutip file sumber di akhir tiap bagian.'}
      ],
      persona=['Hadar Caspit'],
      personaID=['Hadar Caspit']),

      tool(T_PPT, M365_LIC, M365_ACCT, [
        {'instr':'Open a new PowerPoint deck in PowerPoint for the Web. Open the **Copilot pane**. Paste the prompt below.',
         'prompt':'Goal: 9-slide Group ExCo deck on Toyota EV-mix shortfall + Honda margin renegotiation + dealer rationalisation. Context: Group ExCo in 14 days. Source: my brief draft and dashboard. Expectation: (1) Cover; (2) Situation — three converging pressures; (3) Stakeholder Map RAG (Toyota, Honda, BYD, dealers, MITI, BKPM); (4) Toyota EV-Mix Recovery Programme (BYD ramp + hybrid mix); (5) Honda Margin Defence Counter-proposal; (6) Dealer Rationalisation — 8 below break-even (chart); (7) Financial Impact Bridge waterfall; (8) MITI EEV / BKPM PPnBM Briefing Lines; (9) Decisions Requested. Brand colours #1F2937 + #0F172A, 1 chart per slide.'}
      ], DESC_PPT,
      promptsID=[
        {'instr':'Buka deck PowerPoint baru di PowerPoint for the Web. Buka **Copilot pane**. Tempel prompt.',
         'prompt':'Tujuan: Deck 9 slide ExCo Grup tentang shortfall EV-mix Toyota + renegosiasi margin Honda + rasionalisasi dealer. Konteks: ExCo Grup dalam 14 hari. Sumber: draf brief dan dashboard saya. Ekspektasi: (1) Cover; (2) Situasi — tiga tekanan yang bertemu; (3) Peta Pemangku Kepentingan RAG (Toyota, Honda, BYD, dealer, MITI, BKPM); (4) Program Pemulihan EV-Mix Toyota (ramp BYD + mix hybrid); (5) Counter-proposal Pertahanan Margin Honda; (6) Rasionalisasi Dealer — 8 di bawah break-even (chart); (7) Waterfall Bridge Dampak Finansial; (8) Briefing EEV MITI / PPnBM BKPM; (9) Keputusan yang Diminta. Warna brand #1F2937 + #0F172A, 1 chart per slide.'}
      ],
      persona=['Sasha Ouellet'],
      personaID=['Sasha Ouellet']),

      tool(T_OUTLOOK, M365_LIC, M365_ACCT, [
        {'instr':'Open Outlook on the Web. Open the email thread "Toyota TMAP Q4 review + Honda margin response — Group MD follow-up". Click the **Copilot icon**. Paste the prompt below.',
         'prompt':'Goal: Draft a single email to the Zava Motors ExCo and the brand-principal liaison heads. Context: Toyota EV-mix shortfall + Honda margin renegotiation + dealer rationalisation programme active. Source: the email thread above and the response programme. Expectation: Subject line, 4 short paragraphs covering — situation, the 3 actions each principal-liaison head must complete in 72 hours (Toyota EV-mix narrative refresh; Honda counter-proposal pre-read; dealer-rationalisation comms freeze), the MITI/BKPM regulator-engagement workstream, the Group ExCo date. Tone: firm, supportive, accountable.'}
      ], DESC_OUTLOOK,
      promptsID=[
        {'instr':'Buka Outlook on the Web. Buka thread email "Review TMAP Q4 Toyota + respons margin Honda — tindak lanjut Direktur Pelaksana Grup". Klik **ikon Copilot**. Tempel prompt.',
         'prompt':'Tujuan: Susun satu email ke ExCo Zava Motors dan kepala liaison prinsipal merek. Konteks: program shortfall EV-mix Toyota + renegosiasi margin Honda + rasionalisasi dealer aktif. Sumber: thread email di atas dan program respons. Ekspektasi: Baris subjek, 4 paragraf pendek — situasi, 3 aksi per kepala liaison prinsipal dalam 72 jam (refresh naratif EV-mix Toyota; pre-read counter-proposal Honda; freeze komunikasi rasionalisasi dealer), workstream engagement regulator MITI/BKPM, tanggal ExCo Grup. Nada: tegas, suportif, akuntabel.'}
      ],
      persona=['Hadar Caspit'],
      personaID=['Hadar Caspit']),

      tool(T_TEAMS, M365_LIC, M365_ACCT, [
        {'instr':'**(1) In Teams**, open **Calendar** → click the past meeting **"Toyota TMAP Q4 EV-Mix Review"**. On the Recap page, walk the audience through **AI Notes**, **Custom summary** (Speaker summary template), and **Audio recap**. **(2) In Word for the Web**, open a new blank document and type the minutes template (Date · Decisions · Actions · Risks). **(3) Click the Copilot icon** in Word and paste the prompt below — Copilot in Word references the recap with `/`.',
         'prompt':'Create meeting minutes for the Teams meeting /Toyota TMAP Q4 EV-Mix Review. Use the template on this page. Sections: (1) Date and Attendees; (2) Decisions Taken; (3) Action Items with Owner and Due Date; (4) Risks Raised; (5) Open Questions. Quote Toyota Motor Asia Pacific representatives verbatim where wording matters. Flag any decision linked to the FY2026 BYD ramp or Honda counter-proposal as Critical Path. Save as Minutes_Toyota_TMAP_Q4_Review.docx.'}
      ], '',
      promptsID=[
        {'instr':'**(1) Di Teams**, buka **Calendar** → klik rapat lampau **"Review EV-Mix Q4 Toyota TMAP"**. Pada halaman Recap, tampilkan **AI Notes**, **Custom summary** (template Speaker summary), dan **Audio recap**. **(2) Di Word for the Web**, buka dokumen baru kosong dan ketik template notulen (Tanggal · Keputusan · Action · Risiko). **(3) Klik ikon Copilot** di Word dan tempel prompt — Copilot in Word mereferensikan recap dengan `/`.',
         'prompt':'Buat notulen rapat untuk rapat Teams /Review EV-Mix Q4 Toyota TMAP. Gunakan template di halaman ini. Bagian: (1) Tanggal dan Peserta; (2) Keputusan; (3) Action dengan Pemilik dan Tenggat; (4) Risiko; (5) Pertanyaan Terbuka. Kutip perwakilan Toyota Motor Asia Pacific secara harfiah jika redaksinya penting. Tandai keputusan terkait ramp BYD FY2026 atau counter-proposal Honda sebagai Critical Path. Simpan sebagai Notulen_Review_TMAP_Q4_Toyota.docx.'}
      ],
      persona=['Sasha Ouellet'],
      personaID=['Sasha Ouellet']),

      tool(T_NOTEBOOK, M365_LIC, M365_ACCT, [
        {'instr':'All sources are loaded. Type the prompt below in the notebook chat.',
         'prompt':'Synthesise across all sources to produce a 12-bullet Group ExCo narrative. Cover: Toyota EV-mix shortfall status and recovery programme; Honda margin renegotiation defence; dealer rationalisation 8 underperformers; BYD partnership ramp; MITI EEV briefing lines; Kementerian Perindustrian PPnBM briefing lines; financial impact bridge; principal-relationship risk register; decisions requested. Cite the source file at the end of every bullet.'},
        {'instr':'Click **Quick Create** > **Audio Overview** to generate a 7-minute briefing podcast.',
         'prompt':'Quick Create: Audio Overview, 7 minutes, formal narration tone, focused on the Group ExCo narrative above. Listeners are the Zava Motors regional dealer-network heads preparing for tomorrow morning huddles.'}
      ], DESC_NOTEBOOK,
      promptsID=[
        {'instr':'Semua sumber sudah dimuat. Ketik prompt di bawah pada chat notebook.',
         'prompt':'Sintesakan dari semua sumber untuk menghasilkan narasi ExCo Grup 12-bullet. Cakup: status shortfall EV-mix Toyota dan program pemulihan; pertahanan renegosiasi margin Honda; rasionalisasi 8 dealer underperform; ramp kemitraan BYD; briefing EEV MITI; briefing PPnBM Kementerian Perindustrian; bridge dampak finansial; register risiko hubungan prinsipal; keputusan yang diminta. Kutip file sumber di akhir tiap bullet.'},
        {'instr':'Klik **Quick Create** > **Audio Overview** untuk menghasilkan podcast briefing 7 menit.',
         'prompt':'Quick Create: Audio Overview, 7 menit, gaya narasi formal, fokus pada narasi ExCo Grup di atas. Pendengar adalah kepala jaringan dealer regional Zava Motors yang menyiapkan huddle pagi besok.'}
      ],
      persona=['Mod Admin','Mod Admin'],
      personaID=['Mod Admin','Mod Admin'],
      notebookMeta={
        'sources':['/AUTOM_01_EV_Mix_and_Capex_Model.xlsx', '/AUTOM_02_Dealer_PnL_Tracker.xlsx', '/AUTOM_03_Principal_Margin_Renegotiation_Brief.docx', '/AUTOM_04_MITI_EEV_BKPM_PPnBM_Briefing_Pack.docx', '/AUTOM_05_Dealer_Rationalisation_Playbook.docx'],
        'instructions':'You are the Group MD of Zava Motors preparing a Group ExCo pack on the converging Toyota EV-mix shortfall, Honda margin renegotiation, and dealer rationalisation. Always cite the source file and tab/section. Tone: precise, principal-grade, no speculation about Toyota or Honda intentions beyond what they have communicated in writing. Use MYR for the Group totals (1 MYR ≈ 3,580 IDR). Reference real Malaysian peers (UMW Holdings, Sime Darby Motors, DRB-HICOM, Bermaz Auto, MBM Resources) and Indonesian peers (Astra International, Indomobil) where benchmark precedent strengthens the argument.',
        'instructionsID':'Anda adalah Direktur Pelaksana Grup Zava Motors yang menyiapkan paket ExCo Grup tentang konvergensi shortfall EV-mix Toyota, renegosiasi margin Honda, dan rasionalisasi dealer. Selalu kutip file sumber dan tab/bagian. Nada: presisi, principal-grade, tanpa spekulasi tentang niat Toyota atau Honda di luar yang sudah disampaikan tertulis. Gunakan RM untuk total Grup (1 RM ≈ 3.580 Rp). Referensikan peer Malaysia riil (UMW Holdings, Sime Darby Motors, DRB-HICOM, Bermaz Auto, MBM Resources) dan peer Indonesia (Astra International, Indomobil) bila preseden benchmark memperkuat argumen.'
      }),

      tool(T_COWORK, FRONTIER_LIC, M365_ACCT, [
        {'instr':'Open `m365.cloud.microsoft` > Agents > **Cowork**. Paste the single prompt below — Cowork delegates 5 parallel sub-tasks. Frontier required.',
         'prompt':'Cowork — Toyota+Honda+Dealers 14-Day Sprint. Run these in parallel: (1) 📝 Draft Word — Honda counter-proposal brief 4 pages, source /AUTOM_01_EV_Mix_and_Capex_Model.xlsx, /AUTOM_02_Dealer_PnL_Tracker.xlsx, /AUTOM_03_Principal_Margin_Renegotiation_Brief.docx, /AUTOM_05_Dealer_Rationalisation_Playbook.docx. (2) 📝 Draft Word — Toyota TMAP Q4 EV-mix recovery narrative 2 pages, sources same. (3) ✉️ Send email to Zava Motors ExCo and brand-principal liaison heads with the 3 actions in 72h. (4) 📅 Schedule 90-min Group ExCo Pre-Read tomorrow 8am MYT. (5) 💬 Post Teams message to #zava-motors-exco with one-line headline + dashboard link.'}
      ], DESC_COWORK,
      promptsID=[
        {'instr':'Buka `m365.cloud.microsoft` > Agents > **Cowork**. Tempel prompt tunggal — Cowork mendelegasikan 5 sub-tugas paralel. Frontier diperlukan.',
         'prompt':'Cowork — Sprint 14 Hari Toyota+Honda+Dealer. Jalankan paralel: (1) 📝 Susun Word — brief counter-proposal Honda 4 halaman, sumber /AUTOM_01_EV_Mix_and_Capex_Model.xlsx, /AUTOM_02_Dealer_PnL_Tracker.xlsx, /AUTOM_03_Principal_Margin_Renegotiation_Brief.docx, /AUTOM_05_Dealer_Rationalisation_Playbook.docx. (2) 📝 Susun Word — naratif pemulihan EV-mix Toyota TMAP Q4 2 halaman, sumber sama. (3) ✉️ Kirim email ke ExCo Zava Motors dan kepala liaison prinsipal merek dengan 3 aksi dalam 72 jam. (4) 📅 Jadwalkan Pre-Read ExCo Grup 90 menit besok 08:00 WIB. (5) 💬 Posting pesan Teams di #zava-motors-exco dengan headline satu baris + tautan dashboard.'}
      ],
      persona=['Mod Admin'],
      personaID=['Mod Admin']),

      tool(T_WORD_AGT, ANY_LIC, ANY_ACCT, [
        {'instr':'Open `m365.cloud.microsoft/chat` → Agents tab → **Word Agent**. Paste the prompt below — the agent returns a fully drafted .docx.',
         'prompt':'Goal: Generate a 4-page Group MD Crisis Brief in Word. Context: Toyota EV-mix shortfall + Honda margin renegotiation + dealer rationalisation. Source: /AUTOM_01_EV_Mix_and_Capex_Model.xlsx AND /AUTOM_02_Dealer_PnL_Tracker.xlsx. Expectation: Sections — Executive Summary 5 bullets; Current Status of all 3 workstreams; Programme; Financial Impact; Stakeholder Map (Toyota / Honda / BYD / Dealers / MITI / BKPM); Decisions requested. Tone: precise, principal-grade. Save as Toyota_Honda_Dealer_Brief.docx.'}
      ], DESC_WORD_AGT,
      promptsID=[
        {'instr':'Buka `m365.cloud.microsoft/chat` → tab Agents → **Word Agent**. Tempel prompt — agent mengembalikan .docx yang sudah didraf penuh.',
         'prompt':'Tujuan: Hasilkan Brief Krisis Direktur Pelaksana Grup 4 halaman dalam Word. Konteks: shortfall EV-mix Toyota + renegosiasi margin Honda + rasionalisasi dealer. Sumber: /AUTOM_01_EV_Mix_and_Capex_Model.xlsx DAN /AUTOM_02_Dealer_PnL_Tracker.xlsx. Ekspektasi: Bagian — Ringkasan Eksekutif 5 bullet; Status Saat Ini ketiga workstream; Program; Dampak Finansial; Peta Pemangku Kepentingan (Toyota / Honda / BYD / Dealer / MITI / BKPM); Keputusan yang diminta. Nada: presisi, principal-grade. Simpan sebagai Brief_Toyota_Honda_Dealer.docx.'}
      ],
      persona=['Sasha Ouellet'],
      personaID=['Sasha Ouellet']),

      tool(T_PPT_AGT, ANY_LIC, ANY_ACCT, [
        {'instr':'Open `m365.cloud.microsoft/chat` → Agents tab → **PowerPoint Agent**. Paste the prompt below.',
         'prompt':'Goal: 9-slide Group ExCo deck on Toyota EV-mix shortfall + Honda margin renegotiation + dealer rationalisation. Context: Group ExCo in 14 days. Source: /Toyota_Honda_Dealer_Brief.docx and /AUTOM_01_EV_Mix_and_Capex_Model.xlsx. Expectation: Cover; Situation; Stakeholder Map RAG; Toyota EV-Mix Programme; Honda Counter-proposal; Dealer Rationalisation; Financial Bridge waterfall; MITI EEV / BKPM PPnBM Lines; Decisions. Brand #1F2937 + #0F172A, 1 chart/slide. Save as Toyota_Honda_Dealer_ExCo_Deck.pptx.'}
      ], DESC_PPT_AGT,
      promptsID=[
        {'instr':'Buka `m365.cloud.microsoft/chat` → tab Agents → **PowerPoint Agent**. Tempel prompt.',
         'prompt':'Tujuan: Deck 9 slide ExCo Grup tentang shortfall EV-mix Toyota + renegosiasi margin Honda + rasionalisasi dealer. Konteks: ExCo Grup dalam 14 hari. Sumber: /Brief_Toyota_Honda_Dealer.docx dan /AUTOM_01_EV_Mix_and_Capex_Model.xlsx. Ekspektasi: Cover; Situasi; Peta Pemangku Kepentingan RAG; Program EV-Mix Toyota; Counter-proposal Honda; Rasionalisasi Dealer; Waterfall Finansial; Briefing EEV MITI / PPnBM BKPM; Keputusan. Brand #1F2937 + #0F172A, 1 chart/slide. Simpan sebagai Deck_ExCo_Toyota_Honda_Dealer.pptx.'}
      ],
      persona=['Sasha Ouellet'],
      personaID=['Sasha Ouellet']),

      tool(T_XL_AGT, ANY_LIC, ANY_ACCT, [
        {'instr':'Open `m365.cloud.microsoft/chat` → Agents tab → **Excel Agent**. Paste the prompt below.',
         'prompt':'Goal: Build a Toyota EV-mix + Honda margin + dealer rationalisation response control tracker workbook. Context: Operating tracker for the Group COO. Source: schema only. Expectation: Sheet 1 EV-Mix Programme Milestones (BYD ramp + Toyota hybrid + Honda PHEV); Sheet 2 Honda Counter-proposal Tracker; Sheet 3 Dealer P&L Watchlist (8 underperformers); Sheet 4 Dashboard with KPI tiles + RAG conditional formatting. Save as Toyota_Honda_Dealer_Tracker.xlsx.'}
      ], DESC_XL_AGT,
      promptsID=[
        {'instr':'Buka `m365.cloud.microsoft/chat` → tab Agents → **Excel Agent**. Tempel prompt.',
         'prompt':'Tujuan: Bangun workbook tracker kendali respons EV-mix Toyota + margin Honda + rasionalisasi dealer. Konteks: tracker operasi untuk Direktur Operasional Grup. Sumber: hanya skema. Ekspektasi: Sheet 1 Milestone Program EV-Mix (ramp BYD + hybrid Toyota + PHEV Honda); Sheet 2 Tracker Counter-proposal Honda; Sheet 3 Watchlist P&L Dealer (8 underperform); Sheet 4 Dashboard dengan KPI tile + format kondisional RAG. Simpan sebagai Tracker_Toyota_Honda_Dealer.xlsx.'}
      ],
      persona=['Hadar Caspit'],
      personaID=['Hadar Caspit']),

      tool(T_BUILDER, ANY_LIC, ANY_ACCT, [
        {'instr':'Open `m365.cloud.microsoft/chat` > Agents > **+ Create an agent**. Pick ONE of the 3 agents below. Paste the chosen description into the **Describe** field.',
         'prompt':'**Option A — Zava Motors EV-Mix Agent.** Build an agent for the Group COO and the brand-principal liaison heads to drive the Toyota EV-mix recovery programme to closure. Ground every answer on /AUTOM_01_EV_Mix_and_Capex_Model.xlsx and the Toyota TMAP correspondence. Always cite file and section. Classify each milestone as Closed / On-Track / Delayed. Tone: precise, principal-grade. Starter prompts: (1) Which BYD ramp milestones are at risk of slipping; (2) What is the day-by-day plan for the Toyota Q4 review; (3) Draft the Toyota TMAP narrative; (4) Build a daily ops dashboard; (5) Summarise progress for the Group ExCo.'},
        {'instr':'**Option B — alternative agent.** Same flow, different specialisation.',
         'prompt':'**Option B — Zava Motors Honda Liaison Agent.** Build an agent for the Group CFO and the Honda liaison head to handle Honda margin renegotiation correspondence over 30 days. Ground every answer on /AUTOM_03_Principal_Margin_Renegotiation_Brief.docx and /AUTOM_05_Dealer_Rationalisation_Playbook.docx. Always cite section. Filter every answer through Bursa Malaysia continuous-disclosure rules. Tone: factual, conservative, not forward-looking unless source already disclosed. Starter prompts: (1) Draft 200-word Honda counter-proposal answer; (2) Holding line for media if Honda response leaks; (3) Recovery roadmap summary; (4) 60-second EBITDA-bridge talking points; (5) Build IR Q&A pack on Honda margin defence.'},
        {'instr':'**Option C — alternative agent.** Same flow.',
         'prompt':'**Option C — Zava Motors Dealer Network Agent.** Build an agent for the Group COO / Dealer Network team to handle the dealer-rationalisation programme. Ground every answer on /AUTOM_02_Dealer_PnL_Tracker.xlsx, /AUTOM_05_Dealer_Rationalisation_Playbook.docx. Always cite section. Classify each dealer as Retain / Restructure / Exit. Tone: factual, no admission of unproven facts about dealer principal performance. Starter prompts: (1) Status of the 8 underperforming dealers; (2) Draft principal-conversation prep notes; (3) Build a weekly dashboard; (4) Summarise dealer-rationalisation timeline; (5) Give me the 60-second update.'},
        {'instr':'**Test.** Validate grounding, citations, GCSE framework, and scope.',
         'prompt':'Give me the 60-second version of the Toyota EV-mix shortfall + Honda margin renegotiation + 8 underperforming dealer situation, the 3 worst issues, the response programme, and the decisions I must take to the Group ExCo in 14 days. Cite the file and section for every paragraph. Use the GCSE framework where relevant.'},
        {'instr':'**Share.** Click the agent → **Share** → add recipients with **Use** access.',
         'prompt':'Share with the Zava Motors ExCo (Group MD, CFO, COO, Dealer Network Director, Toyota liaison head, Honda liaison head, Hyundai liaison head, BYD liaison head) — Use access. Send notification: "This agent is now in your M365 Copilot chat — ground every Toyota / Honda / dealer-rationalisation question through it for the next 90 days."'}
      ], DESC_BUILDER,
      promptsID=[
        {'instr':'Buka `m365.cloud.microsoft/chat` > Agents > **+ Create an agent**. Pilih SATU dari 3 agent. Tempel deskripsi ke field **Describe**.',
         'prompt':'**Opsi A — Zava Motors EV-Mix Agent.** Bangun agent untuk Direktur Operasional Grup dan kepala liaison prinsipal merek untuk mendorong program pemulihan EV-mix Toyota hingga ditutup. Dasarkan pada /AUTOM_01_EV_Mix_and_Capex_Model.xlsx dan korespondensi Toyota TMAP. Selalu kutip file dan bagian. Klasifikasikan tiap milestone sebagai Closed / On-Track / Delayed. Nada: presisi, principal-grade. Starter prompt: (1) Milestone ramp BYD mana yang berisiko slip; (2) Apa rencana harian untuk review Q4 Toyota; (3) Susun naratif Toyota TMAP; (4) Bangun dashboard ops harian; (5) Rangkum progress untuk ExCo Grup.'},
        {'instr':'**Opsi B — agent alternatif.** Alur sama, spesialisasi berbeda.',
         'prompt':'**Opsi B — Zava Motors Honda Liaison Agent.** Bangun agent untuk Direktur Keuangan Grup dan kepala liaison Honda untuk menangani korespondensi renegosiasi margin Honda selama 30 hari. Dasarkan pada /AUTOM_03_Principal_Margin_Renegotiation_Brief.docx dan /AUTOM_05_Dealer_Rationalisation_Playbook.docx. Selalu kutip bagian. Saring tiap jawaban melalui aturan continuous-disclosure Bursa Malaysia. Nada: faktual, konservatif, tidak forward-looking kecuali sumber sudah mengungkap. Starter prompt: (1) Susun jawaban counter-proposal Honda 200 kata; (2) Holding line untuk media bila respons Honda bocor; (3) Rangkum roadmap pemulihan; (4) Talking points bridge EBITDA 60 detik; (5) Bangun pack Q&A IR pertahanan margin Honda.'},
        {'instr':'**Opsi C — agent alternatif.** Alur sama.',
         'prompt':'**Opsi C — Zava Motors Dealer Network Agent.** Bangun agent untuk Direktur Operasional Grup / tim Jaringan Dealer untuk menangani program rasionalisasi dealer. Dasarkan pada /AUTOM_02_Dealer_PnL_Tracker.xlsx, /AUTOM_05_Dealer_Rationalisation_Playbook.docx. Selalu kutip bagian. Klasifikasikan tiap dealer sebagai Pertahankan / Restrukturisasi / Keluar. Nada: faktual, tidak mengakui fakta yang belum terbukti tentang kinerja prinsipal dealer. Starter prompt: (1) Status 8 dealer underperform; (2) Susun catatan persiapan percakapan prinsipal; (3) Bangun dashboard mingguan; (4) Rangkum timeline rasionalisasi dealer; (5) Berikan update 60 detik.'},
        {'instr':'**Uji.** Validasi grounding, kutipan, framework GCSE, dan cakupan.',
         'prompt':'Berikan versi 60 detik dari situasi shortfall EV-mix Toyota + renegosiasi margin Honda + 8 dealer underperform, 3 isu terburuk, program respons, dan keputusan yang harus saya bawa ke ExCo Grup dalam 14 hari. Kutip file dan bagian untuk tiap paragraf. Gunakan framework GCSE bila relevan.'},
        {'instr':'**Bagikan.** Klik agent → **Share** → tambahkan penerima dengan akses **Use**.',
         'prompt':'Bagikan ke ExCo Zava Motors (Direktur Pelaksana Grup, Direktur Keuangan, Direktur Operasional, Direktur Jaringan Dealer, kepala liaison Toyota, kepala liaison Honda, kepala liaison Hyundai, kepala liaison BYD) — akses Use. Kirim notifikasi: "Agent ini sekarang ada di M365 Copilot chat Anda — dasarkan tiap pertanyaan Toyota / Honda / rasionalisasi dealer melalui agent ini selama 90 hari ke depan."'}
      ],
      persona=['Mod Admin','Mod Admin','Mod Admin','Sasha Ouellet','Sasha Ouellet'],
      personaID=['Mod Admin','Mod Admin','Mod Admin','Sasha Ouellet','Sasha Ouellet']),
    ],
    companyID='Zava Motors',
    taglineID='Shortfall EV-mix Toyota + renegosiasi prinsipal Honda + 8 dealer underperform — ExCo Grup dalam 14 hari.',
    scenarioID="Zava Motors adalah platform distribusi otomotif dan dealership Grup dengan hak sole-distributor Toyota dan Honda untuk kendaraan penumpang di Malaysia, jaringan 3S Hyundai resmi di Indonesia, dan kemitraan merek elektrifikasi BYD yang baru ditandatangani (BEV + PHEV). Grup mengoperasikan 92 outlet sales-and-service di kedua negara (54 di Malaysia, 38 di Indonesia), merakit model CKD pilihan di pabrik Pekan dan Bekasi, dan menjalankan unit auto-financing captive. Tiga tekanan bertemu sekaligus: (1) target mix BEV 2027 Toyota Motor Asia Pacific menuntut 30% penjualan elektrifikasi tetapi Zava Motors di 4,1% YTD, dengan re-prioritisasi capex FY2026 dibutuhkan antara peluncuran BYD vs lini hybrid Honda; (2) Honda Motor Co. membuka renegosiasi margin prinsipal yang meminta potongan margin ATPM/distributor 150 bps, mengancam EBITDA FY2026 sebesar Rp 300 miliar; (3) 8 dari 92 dealer beroperasi di bawah break-even selama 4 kuartal berturut — same-store sales turun 11% YoY, attach rate F&I di 38% terhadap benchmark 55%. Direktur Pelaksana Grup butuh pack siap-ExCo Grup dalam 14 hari mencakup skenario pemulihan EV-mix, pertahanan renegosiasi prinsipal, rencana rasionalisasi dealer, dan catatan briefing kebijakan EEV MITI / PPnBM Kementerian Perindustrian. Frame customer riil: grup ini beroperasi serupa dengan **UMW Holdings** (UMW Toyota Motor + Perodua), **Sime Darby Motors** (distribusi BMW/Hyundai/Ford/Porsche), **DRB-HICOM** (Honda Malaysia + Proton/Geely), **Bermaz Auto** (Mazda), **MBM Resources** (dealer Perodua + Hino), **Astra International** (Toyota/Daihatsu/Isuzu/BMW + Astra Honda Motor 2-wheel), dan **Indomobil Sukses Internasional** (Suzuki/Nissan/Volvo).",
    relevantDepts=['dept-finance','dept-strategy','dept-operations','dept-procurement','dept-risk','dept-legal','dept-investor-relations'],
    personas=[
      {'name':'Hadar Caspit','role':'Group CFO','roleID':'Direktur Keuangan Grup','acct':'admin@ABSx62256373.onmicrosoft.com','lic':'M365 Copilot','color':'#1E40AF'},
      {'name':'Sasha Ouellet','role':'Group Chief of Staff','roleID':'Kepala Staf Grup','acct':'SashaO@ABSx62256373.OnMicrosoft.com','lic':'Free \u2014 no M365 Copilot license','color':'#7C3AED'},
      {'name':'Mod Admin','role':'Group Strategy Director','roleID':'Direktur Strategi Grup','acct':'admin@ABSx62256373.onmicrosoft.com','lic':'M365 Copilot','color':'#059669'},
      {'name':'Daichi Maruyama','role':'Group Sustainability & Risk Director','roleID':'Direktur Keberlanjutan & Risiko Grup','acct':'admin@ABSx62256373.onmicrosoft.com','lic':'M365 Copilot','color':'#DC2626'}
    ],
    storyboard=[
      {'ex':1,'title':'Research & Brief','titleID':'Riset & Pengarahan','minutes':18,'mode':'Show & Tell + Hands-on',
       'summary':'Frame the Toyota EV-mix shortfall + Honda margin renegotiation + dealer rationalisation situation and pull peer playbooks before the principal clock starts ticking.',
       'summaryID':'Bingkai situasi shortfall EV-mix Toyota + renegosiasi margin Honda + rasionalisasi dealer dan tarik playbook peer sebelum clock prinsipal mulai berdetak.',
       'tasks':[
         {'verb':'Frame','toolId':T_CHAT,'mode':'Show & Tell'},
         {'verb':'Benchmark','toolId':T_RESEARCHER,'mode':'Show & Tell'},
         {'verb':'Draft brief','toolId':T_WORD_AGT,'mode':'Hands-on'}]},
      {'ex':2,'title':'Analyse & Decide','titleID':'Analisis & Putuskan','minutes':18,'mode':'Hands-on',
       'summary':'Quantify the Toyota EV-mix + Honda margin + dealer P&L combined impact; build a Group-ExCo dashboard.',
       'summaryID':'Kuantifikasi dampak gabungan EV-mix Toyota + margin Honda + P&L dealer; bangun dashboard ExCo Grup.',
       'tasks':[
         {'verb':'Crunch','toolId':T_ANALYST,'mode':'Hands-on'},
         {'verb':'Dashboard','toolId':T_EXCEL,'mode':'Hands-on'},
         {'verb':'Tracker','toolId':T_XL_AGT,'mode':'Hands-on'}]},
      {'ex':3,'title':'Communicate & Coordinate','titleID':'Komunikasi & Koordinasi','minutes':18,'mode':'Hands-on',
       'summary':'Brief brand-principal liaison heads, capture the Toyota TMAP Q4 review recap, and assemble the ExCo deck and Honda counter-proposal.',
       'summaryID':'Brief kepala liaison prinsipal merek, capture recap review TMAP Q4 Toyota, dan rakit deck ExCo serta counter-proposal Honda.',
       'tasks':[
         {'verb':'Email','toolId':T_OUTLOOK,'mode':'Hands-on'},
         {'verb':'Recap','toolId':T_TEAMS,'mode':'Hands-on'},
         {'verb':'Deck','toolId':T_PPT_AGT,'mode':'Hands-on'},
         {'verb':'Sprint','toolId':T_COWORK,'mode':'Show & Tell'}]},
      {'ex':4,'title':'Build & Scale','titleID':'Bangun & Skala','minutes':15,'mode':'Show & Tell',
       'summary':'Wrap the Toyota EV-mix + Honda margin + dealer rationalisation playbook into a reusable agent for the Zava Motors operating team.',
       'summaryID':'Bungkus playbook EV-mix Toyota + margin Honda + rasionalisasi dealer ke dalam agent reusable untuk tim operasi Zava Motors.',
       'tasks':[
         {'verb':'Notebook','toolId':T_NOTEBOOK,'mode':'Show & Tell'},
         {'verb':'Agent','toolId':T_BUILDER,'mode':'Show & Tell'}]}
    ],
    geo='MY+ID'
))

print(f"Industries batch 11 written: {len(INDUSTRIES_11)} entries")
