# -*- coding: utf-8 -*-
# Industries batch 12 — Compact 14-tool entries (modeled on ind_batch10 verbosity)
#   1. Aviation — Airlines               (Zava Air)
#   2. Education                         (Zava Education Holdings)
#   3. Utilities — Power Generation      (Zava Power)
#   4. Property Development              (Zava Property)
#   5. E-commerce / Super-app            (Zava Connect)
#   6. Maritime — Shipping & Ports       (Zava Maritime)
import sys; sys.path.insert(0, '.')
from util import *

INDUSTRIES_12 = []

# ╔══════════════════════════════════════════════════════════════════════╗
# ║  1.  AVIATION — AIRLINES  (Zava Air)                                 ║
# ╚══════════════════════════════════════════════════════════════════════╝
INDUSTRIES_12.append(ind(
    'aviation-airlines', 'sec-aviation', 'Aviation — Airlines', '✈️', '#0EA5E9', '#0284C7',
    'Zava Air',
    'Jet fuel hedge unwind MYR 180M + ASEAN open-skies route disruption + cabin crew dispute pre-Hari Raya — Group ExCo in 10 days.',
    "Zava Air is an ASEAN full-service + low-cost carrier group with hubs at KLIA (Malaysia) and CGK Jakarta (Indonesia), operating 78 narrowbody and 14 widebody aircraft across 64 destinations. Three pressures converge: (1) the jet-fuel hedge book unwinds in Q1 with a forecast MYR 180M loss as Brent backwardation pushed realised vs hedged divergence to USD 22/bbl; (2) the new ASEAN open-skies allocation has handed slots on the KUL-CGK, KUL-SIN and KUL-HKT trunk routes to AirAsia, Citilink and Scoot — yield erosion of 8-12% projected on 14 routes; (3) the cabin-crew union has tabled a dispute over rostering and Hari Raya peak pay 18 days before the festive season, creating an industrial-action risk on the 12 highest-yield days of the year. The Group MD needs an ExCo pack in 10 days covering the fuel-hedge cash burn, a network-restructuring response, a CAAM/DGCA/MAVCOM regulator pack, and the cabin-crew negotiation brief. Real customer reference frame: this group operates similarly to **AirAsia**, **Malaysia Airlines (MAS)**, **Firefly**, **Garuda Indonesia**, **Lion Air**, **Citilink**, **Batik Air**, **Super Air Jet**, and **Scoot** — with regulators including **CAAM** (Civil Aviation Authority of Malaysia), **DGCA Indonesia**, **MAVCOM** and **IATA** active concurrently.",
    ['AIR_01_Fuel_Hedge_Unwind_Model.xlsx','AIR_02_Route_Profitability_Tracker.xlsx','AIR_03_Cabin_Crew_Negotiation_Brief.docx','AIR_04_CAAM_DGCA_Compliance_Pack.docx','AIR_05_Network_Restructuring_Playbook.docx'],
    [
      tool(T_CHAT, FREE_LIC, FREE_ACCT, [
        {'instr':'', 'prompt':'Goal: Frame the converging fuel hedge unwind + open-skies route disruption + cabin-crew dispute in plain English for the Group MD. Context: Zava Air faces MYR 180M hedge loss, 14 trunk routes losing yield 8-12% to AirAsia/Citilink/Scoot, and a cabin-crew union dispute 18 days before Hari Raya peak. Source: my notes from the morning Network Operations call. Expectation: 1-page note with sections — Headline; What Happened; Stakeholder Position (CAAM, DGCA, MAVCOM, IATA, union, top 3 corporate accounts); Top 5 Questions the ExCo Will Ask; 3 Decisions the Group MD Must Take in 48 Hours. Tone: calm, precise, no aviation jargon.'},
        {'instr':'', 'prompt':'Goal: Build a stakeholder communication map for the 3 converging pressures with Hari Raya 18 days away. Context: cabin-crew union, CAAM, DGCA, MAVCOM, IATA, top 5 corporate travel accounts, KLIA + CGK ground-handling partners, 4 fuel-hedge counterparty banks. Source: known stakeholders. Expectation: RAG table — Red same-day, Amber 24-72h, Green monitor. Columns: Audience, Channel, Owner, Message Theme, Timing, Risk if Mishandled.'}
      ], DESC_CHAT,
      promptsID=[
        {'instr':'', 'prompt':'Tujuan: Bingkai konvergensi kerugian unwind hedge bahan bakar + disrupsi rute open-skies + sengketa awak kabin dalam bahasa sederhana untuk Direktur Pelaksana Grup. Konteks: Zava Air menghadapi kerugian hedge Rp 644 miliar (RM 180 juta), 14 rute trunk kehilangan yield 8-12% ke AirAsia/Citilink/Scoot, dan sengketa serikat awak kabin 18 hari sebelum puncak Hari Raya. Sumber: catatan saya dari rapat Network Operations pagi. Ekspektasi: nota 1 halaman dengan bagian — Headline; Apa yang Terjadi; Posisi Pemangku Kepentingan (CAAM, DGCA, MAVCOM, IATA, serikat, 3 akun korporat teratas); 5 Pertanyaan Top dari ExCo; 3 Keputusan Direktur Pelaksana Grup dalam 48 Jam. Nada: tenang, presisi, hindari jargon penerbangan.'},
        {'instr':'', 'prompt':'Tujuan: Bangun peta komunikasi pemangku kepentingan untuk 3 tekanan yang bertemu menjelang Hari Raya 18 hari lagi. Konteks: serikat awak kabin, CAAM, DGCA, MAVCOM, IATA, 5 akun travel korporat teratas, mitra ground-handling KLIA + CGK, 4 bank counterparty hedge bahan bakar. Sumber: pemangku kepentingan yang dikenal. Ekspektasi: tabel RAG — Merah hari ini juga, Kuning 24-72 jam, Hijau pantau. Kolom: Audiens, Channel, Pemilik, Tema Pesan, Timing, Risiko bila Keliru.'}
      ],
      persona=['Sasha Ouellet','Hadar Caspit'],
      personaID=['Sasha Ouellet','Hadar Caspit']),

      tool(T_RESEARCHER, M365_LIC, M365_ACCT, [
        {'instr':'Open `m365.cloud.microsoft/chat` > Agents > **Researcher** > **Critique Mode**. Paste the prompt below.',
         'prompt':'Goal: Benchmark how ASEAN airline peers handled simultaneous fuel-hedge unwind, trunk-route yield erosion from open-skies, and cabin-crew industrial action between 2019 and 2025. Context: Zava Air must respond to CAAM, DGCA, MAVCOM and IATA on parallel tracks before Hari Raya peak. Source: peer disclosures (Bursa Malaysia / IDX / SGX), CAPA Centre for Aviation, IATA monthly briefings. Real peers: AirAsia, Malaysia Airlines (MAS), Garuda Indonesia, Lion Air, Citilink, Batik Air, Scoot, Firefly. Expectation: For each peer, identify trigger event, response timeline (90 days), programme adopted (hedge restructuring, route cull, crew settlement), and outcome 12 months later (load factor, yield, EBITDA margin). Critique each source. Cite all with publication date. Output as a comparison table.'},
        {'instr':'Open `m365.cloud.microsoft/chat` > Agents > **Researcher** > **Model Council**. Paste the prompt below.',
         'prompt':'Goal: 3 most defensible response playbooks for an ASEAN carrier hit simultaneously by hedge unwind + open-skies trunk-route erosion + crew dispute in festive peak. Context: Zava Air must protect KLIA + CGK hub credibility, CAAM/DGCA confidence, and labour relations concurrently. Source: Researcher Model Council — convene parallel reports from GPT-5.5 Thinking and Claude Opus 4.7. Expectation: Surface dissent across the council, mark majority and minority views. Comparison table: Playbook, Council Verdict, Dissenting View, ASEAN Precedent (cite specific peer year), Implementation Risk.'}
      ], DESC_RESEARCHER,
      promptsID=[
        {'instr':'Buka `m365.cloud.microsoft/chat` > Agents > **Researcher** > **Critique Mode**. Tempel prompt.',
         'prompt':'Tujuan: Benchmark bagaimana peer maskapai ASEAN menangani unwind hedge bahan bakar, erosi yield rute trunk dari open-skies, dan aksi industrial awak kabin secara bersamaan antara 2019 hingga 2025. Konteks: Zava Air harus merespons CAAM, DGCA, MAVCOM dan IATA di jalur paralel sebelum puncak Hari Raya. Sumber: pengungkapan peer (Bursa Malaysia / BEI / SGX), CAPA Centre for Aviation, briefing bulanan IATA. Peer riil: AirAsia, Malaysia Airlines (MAS), Garuda Indonesia, Lion Air, Citilink, Batik Air, Scoot, Firefly. Ekspektasi: Untuk tiap peer identifikasi peristiwa pemicu, timeline respons (90 hari), program (restrukturisasi hedge, cull rute, penyelesaian awak), dan hasil 12 bulan kemudian (load factor, yield, marjin EBITDA). Kritisi tiap sumber. Cantumkan kutipan lengkap dengan tanggal. Hasilkan tabel perbandingan.'},
        {'instr':'Buka `m365.cloud.microsoft/chat` > Agents > **Researcher** > **Model Council**. Tempel prompt.',
         'prompt':'Tujuan: 3 playbook respons paling defensible untuk maskapai ASEAN yang terkena unwind hedge + erosi rute trunk open-skies + sengketa awak di puncak festive secara bersamaan. Konteks: Zava Air harus melindungi kredibilitas hub KLIA + CGK, kepercayaan CAAM/DGCA, dan hubungan industrial sekaligus. Sumber: Model Council — gelar laporan paralel dari GPT-5.5 Thinking dan Claude Opus 4.7. Ekspektasi: Sorot perbedaan pendapat lintas council, tandai pandangan mayoritas dan minoritas. Tabel perbandingan: Playbook, Putusan Council, Pandangan Minoritas, Preseden ASEAN (kutip peer spesifik dengan tahun), Risiko Implementasi.'}
      ],
      persona=['Mod Admin','Mod Admin'],
      personaID=['Mod Admin','Mod Admin']),

      tool(T_ANALYST, M365_LIC, M365_ACCT, [
        {'instr':'Open `m365.cloud.microsoft/chat` > Agents > **Analyst**. Upload /AIR_01_Fuel_Hedge_Unwind_Model.xlsx AND /AIR_02_Route_Profitability_Tracker.xlsx. Paste the prompt below.',
         'prompt':'Goal: Quantify the combined impact of the Q1 fuel-hedge unwind and the 14-route open-skies yield erosion on FY2026 EBITDA. Context: ExCo needs an evidence-based view in 48 hours. Source: the 2 uploaded files — hedge schedule by tranche + realised vs hedged Brent; route P&L by city-pair with load factor, yield per ASK, CASK ex-fuel. Expectation: (1) RAG bar chart of the 14 disrupted routes ranked by FY2026 EBITDA contribution; (2) waterfall of Group EBITDA bridge — Baseline → Hedge unwind loss → Open-skies yield erosion → Network restructuring upside → Recovered EBITDA; (3) sensitivity table on Brent (USD 70/85/100) showing hedge-cash-burn band per scenario. Output an ExCo-ready RAG dashboard.'}
      ], DESC_ANALYST,
      promptsID=[
        {'instr':'Buka `m365.cloud.microsoft/chat` > Agents > **Analyst**. Unggah /AIR_01_Fuel_Hedge_Unwind_Model.xlsx DAN /AIR_02_Route_Profitability_Tracker.xlsx. Tempel prompt.',
         'prompt':'Tujuan: Kuantifikasi dampak gabungan unwind hedge bahan bakar Q1 dan erosi yield 14 rute open-skies terhadap EBITDA FY2026. Konteks: ExCo butuh pandangan berbasis bukti dalam 48 jam. Sumber: 2 file yang diunggah — jadwal hedge per tranche + Brent realisasi vs hedged; P&L rute per city-pair dengan load factor, yield per ASK, CASK ex-fuel. Ekspektasi: (1) Bar chart RAG 14 rute terdisrupsi diurutkan berdasar kontribusi EBITDA FY2026; (2) waterfall bridge EBITDA Grup — Baseline → kerugian unwind hedge → erosi yield open-skies → upside restrukturisasi jaringan → EBITDA pulih; (3) tabel sensitivitas Brent (USD 70/85/100) menampilkan band cash-burn hedge per skenario. Hasilkan dashboard RAG siap-ExCo.'}
      ],
      persona=['Hadar Caspit'],
      personaID=['Hadar Caspit']),

      tool(T_EXCEL, M365_LIC, M365_ACCT, [
        {'instr':'Open `/AIR_02_Route_Profitability_Tracker.xlsx` in Excel for the Web. Open the **Copilot pane**. Paste the prompt below.',
         'prompt':'Goal: Build a single ExCo-ready dashboard sheet combining route P&L, fuel-hedge exposure and Hari Raya peak load forecasts. Context: ExCo meets in 10 days; Hari Raya peak in 18 days. Source: combine all relevant tabs — Route PnL, Load Factor, Yield, Fuel Burn. Expectation: New sheet "ExCo Dashboard" with KPI tiles for Hedge Loss MYR M, Yield Erosion %, Load Factor Forecast Hari Raya, Routes at Risk; horizontal bar chart of routes ranked worst to best on EBITDA; line chart of yield trajectory across 3 scenarios; RAG conditional formatting; sparkline column. Do not modify source tabs.'}
      ], '',
      promptsID=[
        {'instr':'Buka `/AIR_02_Route_Profitability_Tracker.xlsx` di Excel for the Web. Buka **Copilot pane**. Tempel prompt.',
         'prompt':'Tujuan: Bangun satu sheet dashboard siap-ExCo yang menggabungkan P&L rute, eksposur hedge bahan bakar dan forecast load puncak Hari Raya. Konteks: ExCo bertemu 10 hari; puncak Hari Raya 18 hari. Sumber: gabungkan tab Route PnL, Load Factor, Yield, Fuel Burn. Ekspektasi: Sheet baru "Dashboard ExCo" dengan KPI tile untuk Kerugian Hedge Rp Miliar, Erosi Yield %, Forecast Load Factor Hari Raya, Rute Berisiko; bar chart horizontal rute diurutkan terburuk ke terbaik berdasar EBITDA; line chart trajectory yield lintas 3 skenario; format kondisional RAG; kolom sparkline. Jangan modifikasi tab sumber.'}
      ],
      persona=['Hadar Caspit'],
      personaID=['Hadar Caspit']),

      tool(T_WORD, M365_LIC, M365_ACCT, [
        {'instr':'Open a new blank Word doc in Word for the Web. Open the **Copilot pane**. Reference /AIR_03_Cabin_Crew_Negotiation_Brief.docx and /AIR_05_Network_Restructuring_Playbook.docx using `/`. Paste the prompt below.',
         'prompt':'Goal: Draft the 4-page ExCo paper "Q1 Fuel Hedge, Open-Skies Response & Cabin-Crew Settlement — Group ExCo Pack". Context: ExCo in 10 days; Hari Raya peak in 18 days. Source: the two referenced docs + the fuel-hedge variance numbers I will paste. Expectation: Sections — (1) Executive summary in 5 bullets; (2) Fuel-hedge unwind bridge in plain language; (3) Open-skies route restructuring response; (4) Cabin-crew negotiation status and settlement envelope; (5) CAAM/DGCA/MAVCOM regulator engagement; (6) Decisions requested. Tone: precise, ExCo-ready, no speculation. Cite source files at the end of every section.'}
      ], DESC_WORD,
      promptsID=[
        {'instr':'Buka dokumen Word baru kosong di Word for the Web. Buka **Copilot pane**. Referensikan /AIR_03_Cabin_Crew_Negotiation_Brief.docx dan /AIR_05_Network_Restructuring_Playbook.docx menggunakan `/`. Tempel prompt.',
         'prompt':'Tujuan: Susun paper ExCo 4 halaman "Hedge Bahan Bakar Q1, Respons Open-Skies & Penyelesaian Awak Kabin — Pack ExCo Grup". Konteks: ExCo dalam 10 hari; puncak Hari Raya dalam 18 hari. Sumber: dua dokumen yang direferensikan + angka selisih hedge bahan bakar yang akan saya tempelkan. Ekspektasi: Bagian — (1) Ringkasan eksekutif 5 bullet; (2) Bridge unwind hedge bahasa sederhana; (3) Respons restrukturisasi rute open-skies; (4) Status negosiasi awak kabin dan envelope penyelesaian; (5) Engagement regulator CAAM/DGCA/MAVCOM; (6) Keputusan yang diminta. Nada: presisi, siap-ExCo, tanpa spekulasi. Kutip file sumber di akhir tiap bagian.'}
      ],
      persona=['Hadar Caspit'],
      personaID=['Hadar Caspit']),

      tool(T_PPT, M365_LIC, M365_ACCT, [
        {'instr':'Open a new PowerPoint deck in PowerPoint for the Web. Open the **Copilot pane**. Paste the prompt below.',
         'prompt':'Goal: 9-slide ExCo deck on fuel hedge unwind + open-skies disruption + cabin-crew dispute. Context: ExCo in 10 days. Source: my Word brief and route dashboard. Expectation: (1) Cover; (2) Situation — three converging pressures; (3) Stakeholder Map RAG (CAAM, DGCA, MAVCOM, IATA, union, corporate accounts); (4) Fuel-Hedge Cash Burn waterfall; (5) Open-Skies Network Restructuring; (6) Cabin-Crew Negotiation Settlement Envelope; (7) Hari Raya Peak Operations Plan; (8) Regulator Engagement; (9) Decisions Requested. Brand colours #0EA5E9 + #0284C7, 18pt min body text, 1 chart per slide.'}
      ], DESC_PPT,
      promptsID=[
        {'instr':'Buka deck PowerPoint baru di PowerPoint for the Web. Buka **Copilot pane**. Tempel prompt.',
         'prompt':'Tujuan: Deck 9 slide ExCo tentang unwind hedge bahan bakar + disrupsi open-skies + sengketa awak kabin. Konteks: ExCo dalam 10 hari. Sumber: brief Word dan dashboard rute saya. Ekspektasi: (1) Cover; (2) Situasi — tiga tekanan yang bertemu; (3) Peta Pemangku Kepentingan RAG (CAAM, DGCA, MAVCOM, IATA, serikat, akun korporat); (4) Waterfall Cash Burn Hedge Bahan Bakar; (5) Restrukturisasi Jaringan Open-Skies; (6) Envelope Penyelesaian Negosiasi Awak Kabin; (7) Rencana Operasi Puncak Hari Raya; (8) Engagement Regulator; (9) Keputusan yang Diminta. Warna brand #0EA5E9 + #0284C7, font tubuh min 18pt, 1 chart per slide.'}
      ],
      persona=['Sasha Ouellet'],
      personaID=['Sasha Ouellet']),

      tool(T_OUTLOOK, M365_LIC, M365_ACCT, [
        {'instr':'Open Outlook on the Web. Open the email thread "Fuel hedge unwind + open-skies route response — Group MD follow-up". Click the **Copilot icon**. Paste the prompt below.',
         'prompt':'Goal: Draft a single email to the Zava Air ExCo and the Network, Commercial and Cabin Services heads. Context: fuel hedge unwind, open-skies disruption and cabin-crew dispute active 18 days before Hari Raya. Source: the email thread above. Expectation: Subject line, 4 short paragraphs covering the situation, the 3 actions each functional head must complete in 72 hours (Network: route-cull options; Commercial: corporate-account retention; Cabin Services: settlement envelope), the regulator engagement track, and the ExCo date. Tone: firm, supportive, accountable.'}
      ], DESC_OUTLOOK,
      promptsID=[
        {'instr':'Buka Outlook on the Web. Buka thread email "Unwind hedge bahan bakar + respons rute open-skies — tindak lanjut Direktur Pelaksana Grup". Klik **ikon Copilot**. Tempel prompt.',
         'prompt':'Tujuan: Susun satu email ke ExCo Zava Air dan kepala Network, Commercial dan Cabin Services. Konteks: unwind hedge bahan bakar, disrupsi open-skies dan sengketa awak kabin aktif 18 hari sebelum Hari Raya. Sumber: thread email di atas. Ekspektasi: Baris subjek, 4 paragraf pendek mencakup situasi, 3 aksi per kepala fungsi dalam 72 jam (Network: opsi cull rute; Commercial: retensi akun korporat; Cabin Services: envelope penyelesaian), jalur engagement regulator, dan tanggal ExCo. Nada: tegas, suportif, akuntabel.'}
      ],
      persona=['Hadar Caspit'],
      personaID=['Hadar Caspit']),

      tool(T_TEAMS, M365_LIC, M365_ACCT, [
        {'instr':'**(1) In Teams**, open **Calendar** → click the past meeting **"Fuel Hedge Unwind Crisis Review"**. On the Recap page, walk through **AI Notes**, **Custom summary** (Speaker template), and **Audio recap**. **(2) In Word for the Web**, open a new blank document and type the minutes template (Date · Decisions · Actions · Risks · Open Questions). **(3) Click the Copilot icon** in Word and paste the prompt below — Copilot in Word references the recap with `/`.',
         'prompt':'Create meeting minutes for the Teams meeting /Fuel Hedge Unwind Crisis Review. Use the template on this page. Sections: (1) Date and Attendees; (2) Decisions Taken; (3) Action Items with Owner and Due Date; (4) Risks Raised; (5) Open Questions. Quote Treasury and Network heads verbatim where wording matters. Flag any decision linked to the Hari Raya peak operations as Critical Path. Save as Minutes_Fuel_Hedge_Crisis_Review.docx.'}
      ], '',
      promptsID=[
        {'instr':'**(1) Di Teams**, buka **Calendar** → klik rapat lampau **"Review Krisis Unwind Hedge Bahan Bakar"**. Pada halaman Recap, tampilkan **AI Notes**, **Custom summary** (template Speaker), dan **Audio recap**. **(2) Di Word for the Web**, buka dokumen baru kosong dan ketik template notulen (Tanggal · Keputusan · Action · Risiko · Pertanyaan Terbuka). **(3) Klik ikon Copilot** di Word dan tempel prompt — Copilot in Word mereferensikan recap dengan `/`.',
         'prompt':'Buat notulen rapat untuk rapat Teams /Review Krisis Unwind Hedge Bahan Bakar. Gunakan template di halaman ini. Bagian: (1) Tanggal dan Peserta; (2) Keputusan; (3) Action dengan Pemilik dan Tenggat; (4) Risiko; (5) Pertanyaan Terbuka. Kutip kepala Treasury dan Network secara harfiah jika redaksinya penting. Tandai keputusan terkait operasi puncak Hari Raya sebagai Critical Path. Simpan sebagai Notulen_Review_Krisis_Hedge_Bahan_Bakar.docx.'}
      ],
      persona=['Sasha Ouellet'],
      personaID=['Sasha Ouellet']),

      tool(T_NOTEBOOK, M365_LIC, M365_ACCT, [
        {'instr':'All sources are loaded in the notebook. The Instructions field is set. Type the prompt below in the notebook chat.',
         'prompt':'Synthesise across all sources to produce a 10-bullet ExCo narrative. Cover: fuel-hedge unwind cash burn; open-skies route response; cabin-crew settlement envelope; Hari Raya peak operations plan; CAAM/DGCA/MAVCOM regulator status; financial impact bridge; corporate-account retention; risk register; decisions requested. Cite the source file (and tab/section) at the end of every bullet.'}
      ], DESC_NOTEBOOK,
      promptsID=[
        {'instr':'Semua sumber sudah dimuat di notebook. Field Instructions sudah diset. Ketik prompt di bawah pada chat notebook.',
         'prompt':'Sintesakan dari semua sumber untuk menghasilkan narasi ExCo 10-bullet. Cakup: cash burn unwind hedge bahan bakar; respons rute open-skies; envelope penyelesaian awak kabin; rencana operasi puncak Hari Raya; status regulator CAAM/DGCA/MAVCOM; bridge dampak finansial; retensi akun korporat; register risiko; keputusan yang diminta. Kutip file sumber (dan tab/bagian) di akhir tiap bullet.'}
      ],
      persona=['Mod Admin'],
      personaID=['Mod Admin'],
      notebookMeta={
        'sources':['/AIR_01_Fuel_Hedge_Unwind_Model.xlsx','/AIR_02_Route_Profitability_Tracker.xlsx','/AIR_05_Network_Restructuring_Playbook.docx'],
        'instructions':'You are the Group MD of Zava Air preparing an ExCo pack on converging fuel-hedge unwind, open-skies route disruption and cabin-crew dispute 18 days before Hari Raya. Always cite the source file and tab/section. Tone: precise, ExCo-ready, no speculation. Use MYR for Group totals (1 MYR ≈ 3,580 IDR). Reference real ASEAN peers (AirAsia, MAS, Garuda, Lion Air, Citilink, Scoot, Batik Air) where benchmark precedent strengthens the argument.',
        'instructionsID':'Anda adalah Direktur Pelaksana Grup Zava Air yang menyiapkan paket ExCo tentang konvergensi unwind hedge bahan bakar, disrupsi rute open-skies dan sengketa awak kabin 18 hari sebelum Hari Raya. Selalu kutip file sumber dan tab/bagian. Nada: presisi, siap-ExCo, tanpa spekulasi. Gunakan RM untuk total Grup (1 RM ≈ 3.580 Rp). Referensikan peer ASEAN riil (AirAsia, MAS, Garuda, Lion Air, Citilink, Scoot, Batik Air) bila preseden benchmark memperkuat argumen.'
      }),

      tool(T_COWORK, FRONTIER_LIC, M365_ACCT, [
        {'instr':'Open `m365.cloud.microsoft` > left nav > **Agents** > **Cowork**. Paste the single prompt below — Cowork delegates 5 parallel sub-tasks. Frontier required.',
         'prompt':'Cowork — Hari Raya 18-Day Sprint. Run these in parallel: (1) 📝 Draft Word — Fuel Hedge Unwind Brief 4 pages, sources /AIR_01_Fuel_Hedge_Unwind_Model.xlsx and /AIR_05_Network_Restructuring_Playbook.docx. (2) 📝 Draft Word — Cabin Crew Settlement Talking Points 2 pages, source /AIR_03_Cabin_Crew_Negotiation_Brief.docx. (3) ✉️ Send email to Zava Air ExCo and the Network/Commercial/Cabin Services heads with 3 actions in 72 hours. (4) 📅 Schedule 90-min Group ExCo Pre-Read tomorrow 8am MYT titled "Hari Raya Peak Operations Alignment". (5) 💬 Post Teams message to #zava-air-exco with one-line headline + dashboard link.'}
      ], DESC_COWORK,
      promptsID=[
        {'instr':'Buka `m365.cloud.microsoft` > nav kiri > **Agents** > **Cowork**. Tempel prompt tunggal — Cowork mendelegasikan 5 sub-tugas paralel. Frontier diperlukan.',
         'prompt':'Cowork — Sprint 18 Hari Hari Raya. Jalankan paralel: (1) 📝 Susun Word — Brief Unwind Hedge Bahan Bakar 4 halaman, sumber /AIR_01_Fuel_Hedge_Unwind_Model.xlsx dan /AIR_05_Network_Restructuring_Playbook.docx. (2) 📝 Susun Word — Talking Points Penyelesaian Awak Kabin 2 halaman, sumber /AIR_03_Cabin_Crew_Negotiation_Brief.docx. (3) ✉️ Kirim email ke ExCo Zava Air dan kepala Network/Commercial/Cabin Services dengan 3 aksi dalam 72 jam. (4) 📅 Jadwalkan Pre-Read ExCo Grup 90 menit besok 08:00 WIB berjudul "Penyelarasan Operasi Puncak Hari Raya". (5) 💬 Posting pesan Teams di #zava-air-exco dengan headline satu baris + tautan dashboard.'}
      ],
      persona=['Mod Admin'],
      personaID=['Mod Admin']),

      tool(T_WORD_AGT, ANY_LIC, ANY_ACCT, [
        {'instr':'Open `m365.cloud.microsoft/chat` → Agents tab → **Word Agent**. Paste the prompt below — the agent returns a fully drafted .docx.',
         'prompt':'Goal: Generate a 4-page Group MD Crisis Brief in Word. Context: fuel hedge unwind MYR 180M, open-skies route disruption, cabin-crew dispute 18 days before Hari Raya. Source: /AIR_01_Fuel_Hedge_Unwind_Model.xlsx AND /AIR_02_Route_Profitability_Tracker.xlsx. Expectation: Sections — Executive Summary 5 bullets; Current Status of all 3 workstreams; Programme; Financial Impact; Stakeholder Map (CAAM / DGCA / MAVCOM / IATA / Union / Corporate Accounts); Decisions Requested. Tone: precise, ExCo-ready. Save as Zava_Air_Crisis_Brief.docx.'}
      ], DESC_WORD_AGT,
      promptsID=[
        {'instr':'Buka `m365.cloud.microsoft/chat` → tab Agents → **Word Agent**. Tempel prompt — agent mengembalikan .docx yang sudah didraf penuh.',
         'prompt':'Tujuan: Hasilkan Brief Krisis Direktur Pelaksana Grup 4 halaman dalam Word. Konteks: unwind hedge bahan bakar Rp 644 miliar, disrupsi rute open-skies, sengketa awak kabin 18 hari sebelum Hari Raya. Sumber: /AIR_01_Fuel_Hedge_Unwind_Model.xlsx DAN /AIR_02_Route_Profitability_Tracker.xlsx. Ekspektasi: Bagian — Ringkasan Eksekutif 5 bullet; Status Saat Ini ketiga workstream; Program; Dampak Finansial; Peta Pemangku Kepentingan (CAAM / DGCA / MAVCOM / IATA / Serikat / Akun Korporat); Keputusan yang Diminta. Nada: presisi, siap-ExCo. Simpan sebagai Brief_Krisis_Zava_Air.docx.'}
      ],
      persona=['Sasha Ouellet'],
      personaID=['Sasha Ouellet']),

      tool(T_PPT_AGT, ANY_LIC, ANY_ACCT, [
        {'instr':'Open `m365.cloud.microsoft/chat` → Agents tab → **PowerPoint Agent**. Paste the prompt below.',
         'prompt':'Goal: 9-slide Group ExCo deck on fuel hedge unwind + open-skies disruption + cabin-crew dispute. Context: ExCo in 10 days, Hari Raya in 18 days. Source: /Zava_Air_Crisis_Brief.docx and /AIR_02_Route_Profitability_Tracker.xlsx. Expectation: Cover; Situation; Stakeholder Map RAG; Fuel-Hedge Cash Burn waterfall; Open-Skies Restructuring; Cabin-Crew Settlement; Hari Raya Operations Plan; Regulator Engagement; Decisions. Brand #0EA5E9 + #0284C7, 18pt min body, 1 chart/slide. Save as Zava_Air_ExCo_Deck.pptx.'}
      ], DESC_PPT_AGT,
      promptsID=[
        {'instr':'Buka `m365.cloud.microsoft/chat` → tab Agents → **PowerPoint Agent**. Tempel prompt.',
         'prompt':'Tujuan: Deck 9 slide ExCo Grup tentang unwind hedge bahan bakar + disrupsi open-skies + sengketa awak kabin. Konteks: ExCo dalam 10 hari, Hari Raya dalam 18 hari. Sumber: /Brief_Krisis_Zava_Air.docx dan /AIR_02_Route_Profitability_Tracker.xlsx. Ekspektasi: Cover; Situasi; Peta Pemangku Kepentingan RAG; Waterfall Cash Burn Hedge Bahan Bakar; Restrukturisasi Open-Skies; Penyelesaian Awak Kabin; Rencana Operasi Hari Raya; Engagement Regulator; Keputusan. Brand #0EA5E9 + #0284C7, font tubuh min 18pt, 1 chart/slide. Simpan sebagai Deck_ExCo_Zava_Air.pptx.'}
      ],
      persona=['Sasha Ouellet'],
      personaID=['Sasha Ouellet']),

      tool(T_XL_AGT, ANY_LIC, ANY_ACCT, [
        {'instr':'Open `m365.cloud.microsoft/chat` → Agents tab → **Excel Agent**. Paste the prompt below.',
         'prompt':'Goal: Build a fuel hedge + route profitability + Hari Raya peak load tracker workbook. Context: operating tracker for the Group COO. Source: schema only. Expectation: Sheet 1 Hedge Tranches (realised vs hedged Brent, MTM, cash burn); Sheet 2 Route P&L Watchlist (14 disrupted trunk routes); Sheet 3 Hari Raya Peak Load Forecast (12 highest-yield days); Sheet 4 Dashboard with KPI tiles + RAG conditional formatting. Save as Zava_Air_Operations_Tracker.xlsx.'}
      ], DESC_XL_AGT,
      promptsID=[
        {'instr':'Buka `m365.cloud.microsoft/chat` → tab Agents → **Excel Agent**. Tempel prompt.',
         'prompt':'Tujuan: Bangun workbook tracker hedge bahan bakar + profitabilitas rute + load puncak Hari Raya. Konteks: tracker operasi untuk Direktur Operasional Grup. Sumber: hanya skema. Ekspektasi: Sheet 1 Hedge Tranches (Brent realisasi vs hedged, MTM, cash burn); Sheet 2 Watchlist P&L Rute (14 rute trunk terdisrupsi); Sheet 3 Forecast Load Puncak Hari Raya (12 hari yield tertinggi); Sheet 4 Dashboard dengan KPI tile + format kondisional RAG. Simpan sebagai Tracker_Operasi_Zava_Air.xlsx.'}
      ],
      persona=['Hadar Caspit'],
      personaID=['Hadar Caspit']),

      tool(T_BUILDER, ANY_LIC, ANY_ACCT, [
        {'instr':'Open `m365.cloud.microsoft/chat` > Agents > **+ Create an agent**. Pick ONE of the 3 agents below. Paste the chosen description into the **Describe** field.',
         'prompt':'**Option A — Zava Air Fuel Hedge Watch.** Build an agent for the Group CFO and Treasury team to track and explain hedge unwind cash burn daily. Ground every answer on /AIR_01_Fuel_Hedge_Unwind_Model.xlsx and the Group hedge policy. Always cite file and tab. Classify hedge cover as Adequate / Watch / Insufficient. Tone: precise, treasury-grade, conservative. Starter prompts: (1) What is today rolling 30-day hedge cash burn; (2) Which tranches are at most risk; (3) Should we extend hedges into FY2026 H1; (4) Build a weekly Treasury hedge dashboard; (5) Summarise the H2 fuel-cost bridge in 60 seconds.'},
        {'instr':'**Option B — alternative agent.** Same Create-an-agent flow with a different specialisation.',
         'prompt':'**Option B — Zava Air Network Response Agent.** Build an agent for the Network and Commercial heads to manage the open-skies route response over 60 days. Ground every answer on /AIR_02_Route_Profitability_Tracker.xlsx and /AIR_05_Network_Restructuring_Playbook.docx. Always cite file and section. Classify each disrupted route as Defend / Reduce Frequency / Exit. Tone: factual, commercial-grade. Starter prompts: (1) Which 5 routes are losing the most yield; (2) Draft the corporate-account retention pitch for the top 3 accounts; (3) Build a weekly route-restructuring dashboard; (4) What is the 90-day plan for KUL-CGK and KUL-SIN; (5) Summarise the network response for the ExCo.'},
        {'instr':'**Option C — alternative agent.** Same flow.',
         'prompt':'**Option C — Zava Air Cabin Crew Settlement Agent.** Build an agent for the Cabin Services and HR teams to manage cabin-crew negotiation correspondence and Hari Raya rostering. Ground every answer on /AIR_03_Cabin_Crew_Negotiation_Brief.docx. Always cite section. Classify each open issue as Closed / In Negotiation / Awaiting Internal Sign-Off. Tone: factual, employee-relations grade, no admission of unproven claims. Starter prompts: (1) What is the current settlement envelope; (2) Draft a holding line for the 12 Hari Raya peak days; (3) What are the next 3 negotiation milestones; (4) Build a weekly negotiation status dashboard; (5) Summarise the union position for the ExCo.'},
        {'instr':'**Test.** After the agent is created, click into it and use the right test pane to validate grounding, citations, scope.',
         'prompt':'Give me the 60-second version of the fuel hedge unwind + open-skies disruption + cabin-crew dispute, the worst 3 issues, the response programme, and the decisions I must take to the ExCo in 10 days. Cite the file and tab/section for every paragraph.'},
        {'instr':'**Share.** Click the agent → **Share** → add recipients with **Use** access.',
         'prompt':'Share with the Zava Air ExCo (Group MD, Group CFO, COO, Network Director, Commercial Director, Cabin Services Director, HR Director, Treasurer) — Use access. Send notification: "This agent is now in your M365 Copilot chat — ground every fuel-hedge / open-skies / cabin-crew question through it for the next 90 days."'}
      ], DESC_BUILDER,
      promptsID=[
        {'instr':'Buka `m365.cloud.microsoft/chat` > Agents > **+ Create an agent**. Pilih SATU dari 3 agent. Tempel deskripsi ke field **Describe**.',
         'prompt':'**Opsi A — Zava Air Fuel Hedge Watch.** Bangun agent untuk Direktur Keuangan Grup dan tim Treasury untuk melacak dan menjelaskan cash burn unwind hedge harian. Dasarkan pada /AIR_01_Fuel_Hedge_Unwind_Model.xlsx dan policy hedge Grup. Selalu kutip file dan tab. Klasifikasikan cover hedge sebagai Adequate / Watch / Insufficient. Nada: presisi, treasury-grade, konservatif. Starter prompt: (1) Cash burn hedge rolling 30-hari hari ini; (2) Tranche mana paling berisiko; (3) Haruskah kami perpanjang hedge ke H1 FY2026; (4) Bangun dashboard hedge Treasury mingguan; (5) Rangkum bridge biaya bahan bakar H2 dalam 60 detik.'},
        {'instr':'**Opsi B — agent alternatif.** Alur Create-an-agent sama dengan spesialisasi berbeda.',
         'prompt':'**Opsi B — Zava Air Network Response Agent.** Bangun agent untuk kepala Network dan Commercial untuk mengelola respons rute open-skies selama 60 hari. Dasarkan pada /AIR_02_Route_Profitability_Tracker.xlsx dan /AIR_05_Network_Restructuring_Playbook.docx. Selalu kutip file dan bagian. Klasifikasikan tiap rute terdisrupsi sebagai Pertahankan / Kurangi Frekuensi / Keluar. Nada: faktual, commercial-grade. Starter prompt: (1) 5 rute mana yang kehilangan yield terbanyak; (2) Susun pitch retensi akun korporat untuk 3 akun teratas; (3) Bangun dashboard restrukturisasi rute mingguan; (4) Rencana 90 hari untuk KUL-CGK dan KUL-SIN; (5) Rangkum respons jaringan untuk ExCo.'},
        {'instr':'**Opsi C — agent alternatif.** Alur sama.',
         'prompt':'**Opsi C — Zava Air Cabin Crew Settlement Agent.** Bangun agent untuk tim Cabin Services dan HR untuk mengelola korespondensi negosiasi awak kabin dan rostering Hari Raya. Dasarkan pada /AIR_03_Cabin_Crew_Negotiation_Brief.docx. Selalu kutip bagian. Klasifikasikan tiap isu terbuka sebagai Closed / In Negotiation / Awaiting Internal Sign-Off. Nada: faktual, employee-relations grade, tidak mengakui klaim yang belum terbukti. Starter prompt: (1) Envelope penyelesaian saat ini; (2) Susun holding line untuk 12 hari puncak Hari Raya; (3) 3 milestone negosiasi berikutnya; (4) Bangun dashboard status negosiasi mingguan; (5) Rangkum posisi serikat untuk ExCo.'},
        {'instr':'**Uji.** Validasi grounding, kutipan, cakupan.',
         'prompt':'Berikan versi 60 detik dari unwind hedge bahan bakar + disrupsi open-skies + sengketa awak kabin, 3 isu terburuk, program respons, dan keputusan yang harus saya bawa ke ExCo dalam 10 hari. Kutip file dan tab/bagian untuk tiap paragraf.'},
        {'instr':'**Bagikan.** Klik agent → **Share** → tambahkan penerima dengan akses **Use**.',
         'prompt':'Bagikan ke ExCo Zava Air (Direktur Pelaksana Grup, Direktur Keuangan Grup, COO, Direktur Network, Direktur Commercial, Direktur Cabin Services, Direktur HR, Treasurer) — akses Use. Kirim notifikasi: "Agent ini sekarang ada di M365 Copilot chat Anda — dasarkan tiap pertanyaan hedge bahan bakar / open-skies / awak kabin melalui agent ini selama 90 hari ke depan."'}
      ],
      persona=['Mod Admin','Mod Admin','Mod Admin','Sasha Ouellet','Sasha Ouellet'],
      personaID=['Mod Admin','Mod Admin','Mod Admin','Sasha Ouellet','Sasha Ouellet']),
    ],
    companyID='Zava Air',
    taglineID='Unwind hedge bahan bakar Rp 644 miliar + disrupsi rute open-skies ASEAN + sengketa awak kabin pra-Hari Raya — ExCo Grup dalam 10 hari.',
    scenarioID="Zava Air adalah grup maskapai full-service + low-cost ASEAN dengan hub di KLIA (Malaysia) dan CGK Jakarta (Indonesia), mengoperasikan 78 narrowbody dan 14 widebody di 64 destinasi. Tiga tekanan bertemu: (1) hedge bahan bakar Q1 di-unwind dengan forecast kerugian Rp 644 miliar (RM 180 juta) saat backwardation Brent mendorong divergensi realisasi vs hedged ke USD 22/bbl; (2) alokasi open-skies ASEAN baru menyerahkan slot di rute trunk KUL-CGK, KUL-SIN dan KUL-HKT ke AirAsia, Citilink dan Scoot — erosi yield 8-12% diproyeksikan di 14 rute; (3) serikat awak kabin mengajukan sengketa rostering dan bayaran puncak Hari Raya 18 hari sebelum festive, menciptakan risiko aksi industrial pada 12 hari yield tertinggi tahun ini. Direktur Pelaksana Grup butuh paket ExCo dalam 10 hari mencakup cash burn hedge bahan bakar, respons restrukturisasi jaringan, paket regulator CAAM/DGCA/MAVCOM, dan brief negosiasi awak kabin. Frame customer riil: grup ini beroperasi serupa dengan **AirAsia**, **Malaysia Airlines (MAS)**, **Firefly**, **Garuda Indonesia**, **Lion Air**, **Citilink**, **Batik Air**, **Super Air Jet**, dan **Scoot** — dengan regulator termasuk **CAAM**, **DGCA Indonesia**, **MAVCOM** dan **IATA** aktif bersamaan.",
    relevantDepts=['dept-finance','dept-strategy','dept-operations','dept-hr-talent','dept-risk','dept-legal'],
    personas=[
      {'name':'Sasha Ouellet','role':'Group MD - Network Planning','roleID':'Direktur Utama - Perencanaan Jaringan','acct':FREE_ACCT,'lic':FREE_LIC,'color':'#0EA5E9'},
      {'name':'Mod Admin','role':'Group Strategy Director','roleID':'Direktur Strategi Grup','acct':M365_ACCT,'lic':M365_LIC,'color':'#059669'},
      {'name':'Hadar Caspit','role':'Group CFO','roleID':'Direktur Keuangan Grup','acct':M365_ACCT,'lic':M365_LIC,'color':'#1E40AF'},
      {'name':'Daichi Kimura','role':'Cabin Services & Labour Relations Director','roleID':'Direktur Cabin Services & Hubungan Kerja','acct':M365_ACCT,'lic':M365_LIC,'color':'#DC2626'}
    ],
    storyboard=[
      {'ex':1,'title':'Research & Brief','titleID':'Riset & Pengarahan','minutes':18,'mode':'Show & Tell + Hands-on',
       'summary':'Frame the converging fuel-hedge, open-skies and cabin-crew situation and pull peer playbooks before the Hari Raya clock runs out.',
       'summaryID':'Bingkai situasi konvergensi hedge bahan bakar, open-skies dan awak kabin dan tarik playbook peer sebelum clock Hari Raya habis.',
       'tasks':[
         {'verb':'Frame the morning question and lock the day priorities','verbID':'Susun pertanyaan pagi dan kunci prioritas hari ini','toolId':T_CHAT,'mode':'Show & Tell'},
         {'verb':'Run an outside-in peer scan and pull proven plays','verbID':'Lakukan pemindaian peer dari luar dan tarik praktik terbaik','toolId':T_RESEARCHER,'mode':'Show & Tell'},
         {'verb':'Generate a board-ready brief straight from chat','verbID':'Hasilkan brief siap-Direksi langsung dari chat','toolId':T_WORD_AGT,'mode':'Hands-on'}]},
      {'ex':2,'title':'Analyse & Decide','titleID':'Analisis & Putuskan','minutes':18,'mode':'Hands-on',
       'summary':'Quantify the fuel-hedge + route P&L + Hari Raya peak load combined impact; build an ExCo dashboard.',
       'summaryID':'Kuantifikasi dampak gabungan hedge bahan bakar + P&L rute + load puncak Hari Raya; bangun dashboard ExCo.',
       'tasks':[
         {'verb':'Crunch the numbers and surface the biggest gaps','verbID':'Olah angka dan ungkap celah terbesar','toolId':T_ANALYST,'mode':'Hands-on'},
         {'verb':'Build a single-pane operating dashboard','verbID':'Bangun dashboard operasi satu-halaman','toolId':T_EXCEL,'mode':'Hands-on'},
         {'verb':'Spin up a recurring tracker workbook from chat','verbID':'Buat workbook tracker berulang dari chat','toolId':T_XL_AGT,'mode':'Hands-on'}]},
      {'ex':3,'title':'Communicate & Coordinate','titleID':'Komunikasi & Koordinasi','minutes':18,'mode':'Hands-on',
       'summary':'Brief functional heads, capture the Fuel Hedge Crisis Review recap, and assemble the ExCo deck and Cabin Services brief.',
       'summaryID':'Brief kepala fungsi, capture recap Review Krisis Hedge Bahan Bakar, dan rakit deck ExCo serta brief Cabin Services.',
       'tasks':[
         {'verb':'Draft the stakeholder alignment email','verbID':'Draf email penyelarasan stakeholder','toolId':T_OUTLOOK,'mode':'Hands-on'},
         {'verb':'Recap the meeting and turn it into minutes','verbID':'Recap rapat dan ubah ke notulen','toolId':T_TEAMS,'mode':'Hands-on'},
         {'verb':'Generate a board-ready deck from chat','verbID':'Hasilkan deck siap-Direksi dari chat','toolId':T_PPT_AGT,'mode':'Hands-on'},
         {'verb':'Delegate a 5-task parallel sprint','verbID':'Delegasikan 5-tugas paralel ke Cowork','toolId':T_COWORK,'mode':'Show & Tell'}]},
      {'ex':4,'title':'Build & Scale','titleID':'Bangun & Skala','minutes':15,'mode':'Show & Tell',
       'summary':'Wrap the fuel-hedge + network + cabin-crew playbook into a reusable agent for the Zava Air operating team.',
       'summaryID':'Bungkus playbook hedge bahan bakar + jaringan + awak kabin ke dalam agent reusable untuk tim operasi Zava Air.',
       'tasks':[
         {'verb':'Pull every source into one synthesis notebook','verbID':'Tarik semua sumber ke satu notebook sintesis','toolId':T_NOTEBOOK,'mode':'Show & Tell'},
         {'verb':'Wrap the daily workflow into a reusable agent','verbID':'Bungkus alur kerja harian jadi agen yang dapat dipakai ulang','toolId':T_BUILDER,'mode':'Show & Tell'}]}
    ],
    geo='MY+ID'
))

# INDUSTRIES_12.append(... aviation-airlines ...)

# ╔══════════════════════════════════════════════════════════════════════╗
# ║  2.  EDUCATION  (Zava Education Holdings)                            ║
# ╚══════════════════════════════════════════════════════════════════════╝
INDUSTRIES_12.append(ind(
    'education', 'sec-edu', 'Education', '🎓', '#7C3AED', '#5B21B6',
    'Zava Education Holdings',
    'Intl student visa squeeze MYR 92M + new competitor private uni + MQA accreditation review delay — Group ExCo in 14 days.',
    "Zava Education Holdings is an ASEAN-listed private education group operating a private university (12,400 students), a foundation/A-level college (4,200 students) and a B2B/B2C e-learning platform with 180,000 active learners across Malaysia and Indonesia. Three pressures hit the January 2026 intake: (1) a tightening of international-student visa quotas by Jabatan Imigresen Malaysia and additional Kemendikbudristek scrutiny on Indonesian intake puts MYR 92M of Group revenue at risk; (2) a new competitor private university backed by a regional sovereign fund has launched 6 mid-tier programmes (Computing, Business, Engineering, Hospitality, Communication, Allied Health) with aggressive scholarship pricing — the early-admission funnel for 4 of our flagship programmes shows a 23% YoY drop; (3) the Malaysian Qualifications Agency (MQA) has flagged 3 of our programmes for accreditation review extension — a 90-day delay would force deferral of the January intake for those cohorts. The Group CEO needs an ExCo pack in 14 days covering programme P&L, the international-student pipeline recovery, MQA accreditation defence, competitor programme map, and the FY2026 intake recovery playbook. Real customer reference frame: this group operates similarly to **Sunway Education Group**, **Taylor's Education Group**, **INTI International University**, **KDU University College**, **APU (Asia Pacific University)**, **Universitas Pelita Harapan (UPH)** (Lippo), **BINUS University**, **Sampoerna University**, and **Universitas Ciputra** — with regulators including **MQA** (Malaysian Qualifications Agency), **JPT** (Jabatan Pendidikan Tinggi), **Kementerian Pendidikan Tinggi MY**, **Kemendikbudristek ID**, and **BAN-PT** active concurrently.",
    ['EDU_01_Programme_PnL.xlsx','EDU_02_Intl_Student_Pipeline.xlsx','EDU_03_MQA_Accreditation_Brief.docx','EDU_04_Competitor_Programme_Map.docx','EDU_05_FY2026_Intake_Recovery_Playbook.docx'],
    [
      tool(T_CHAT, FREE_LIC, FREE_ACCT, [
        {'instr':'', 'prompt':'Goal: Frame the international-student visa squeeze + new competitor private uni + MQA accreditation delay in plain English for the Group CEO. Context: Zava Education Holdings runs a private uni, a foundation/A-level college and an e-learning platform; January intake at risk; MYR 92M revenue exposure. Source: my notes from the morning Admissions and Quality Assurance call. Expectation: 1-page note with sections — Headline; What Happened; Stakeholder Position (MQA, JPT, Kementerian Pendidikan Tinggi MY, Kemendikbudristek ID, BAN-PT, partner university overseas, Indonesian study agents); Top 5 Questions the ExCo Will Ask; 3 Decisions the Group CEO Must Take in 48 Hours. Tone: calm, precise, no education-sector jargon.'},
        {'instr':'', 'prompt':'Goal: Build the stakeholder communication map for the 3 converging pressures with January intake 8 weeks away. Context: MQA, JPT, Kemendikbudristek ID, BAN-PT, top 10 study agents in Indonesia, top 3 partner universities for credit transfer, Bumi-quota review committee, and the 4 flagship-programme deans. Source: known stakeholders. Expectation: RAG table — Red same-day, Amber 24-72h, Green monitor. Columns: Audience, Channel, Owner, Message Theme, Timing, Risk if Mishandled.'}
      ], DESC_CHAT,
      promptsID=[
        {'instr':'', 'prompt':'Tujuan: Bingkai squeeze visa mahasiswa internasional + universitas swasta kompetitor baru + delay review akreditasi MQA dalam bahasa sederhana untuk CEO Grup. Konteks: Zava Education Holdings menjalankan universitas swasta, college foundation/A-level dan platform e-learning; intake Januari berisiko; eksposur revenue Rp 329 miliar (RM 92 juta). Sumber: catatan saya dari rapat Admissions dan Quality Assurance pagi. Ekspektasi: nota 1 halaman dengan bagian — Headline; Apa yang Terjadi; Posisi Pemangku Kepentingan (MQA, JPT, Kementerian Pendidikan Tinggi MY, Kemendikbudristek ID, BAN-PT, universitas mitra luar negeri, agen studi Indonesia); 5 Pertanyaan Top dari ExCo; 3 Keputusan CEO Grup dalam 48 Jam. Nada: tenang, presisi, hindari jargon sektor pendidikan.'},
        {'instr':'', 'prompt':'Tujuan: Bangun peta komunikasi pemangku kepentingan untuk 3 tekanan yang bertemu dengan intake Januari 8 minggu lagi. Konteks: MQA, JPT, Kemendikbudristek ID, BAN-PT, 10 agen studi teratas di Indonesia, 3 universitas mitra teratas untuk credit transfer, komite review kuota Bumi, dan 4 dekan program flagship. Sumber: pemangku kepentingan yang dikenal. Ekspektasi: tabel RAG — Merah hari ini juga, Kuning 24-72 jam, Hijau pantau. Kolom: Audiens, Channel, Pemilik, Tema Pesan, Timing, Risiko bila Keliru.'}
      ],
      persona=['Sasha Ouellet','Hadar Caspit'],
      personaID=['Sasha Ouellet','Hadar Caspit']),

      tool(T_RESEARCHER, M365_LIC, M365_ACCT, [
        {'instr':'Open `m365.cloud.microsoft/chat` > Agents > **Researcher** > **Critique Mode**. Paste the prompt below.',
         'prompt':'Goal: Benchmark how ASEAN private-education peers handled simultaneous international-student visa squeezes, mid-tier competitor entry and MQA/BAN-PT accreditation review extensions between 2019 and 2025. Context: Zava Education Holdings must respond before the January intake. Source: peer disclosures (Bursa Malaysia / IDX), MQA notices, BAN-PT accreditation registers, MIDA and Kemendikbudristek statements. Real peers: Sunway Education, Taylor Education, INTI International, KDU, APU, UPH (Lippo), BINUS, Sampoerna University, Universitas Ciputra. Expectation: For each peer, identify trigger event, response timeline, programme adopted (intake recovery, scholarship rebalance, accreditation defence), and outcome 12 months later (intake numbers, programme P&L, accreditation status). Critique each source. Cite all with publication date. Output as a comparison table.'},
        {'instr':'Open `m365.cloud.microsoft/chat` > Agents > **Researcher** > **Model Council**. Paste the prompt below.',
         'prompt':'Goal: 3 most defensible response playbooks for an ASEAN private-education group hit simultaneously by visa squeeze + competitor entry + accreditation delay. Context: Zava Education must protect MQA confidence, partner-university relationships, and Indonesian agent network concurrently. Source: Researcher Model Council — convene parallel reports from GPT-5.5 Thinking and Claude Opus 4.7. Expectation: Surface dissent across the council, mark majority and minority views. Comparison table: Playbook, Council Verdict, Dissenting View, ASEAN Precedent (cite specific peer year), Implementation Risk.'}
      ], DESC_RESEARCHER,
      promptsID=[
        {'instr':'Buka `m365.cloud.microsoft/chat` > Agents > **Researcher** > **Critique Mode**. Tempel prompt.',
         'prompt':'Tujuan: Benchmark bagaimana peer pendidikan swasta ASEAN menangani squeeze visa mahasiswa internasional, masuknya kompetitor mid-tier dan perpanjangan review akreditasi MQA/BAN-PT secara bersamaan antara 2019 hingga 2025. Konteks: Zava Education Holdings harus merespons sebelum intake Januari. Sumber: pengungkapan peer (Bursa Malaysia / BEI), notis MQA, register akreditasi BAN-PT, pernyataan MIDA dan Kemendikbudristek. Peer riil: Sunway Education, Taylor Education, INTI International, KDU, APU, UPH (Lippo), BINUS, Sampoerna University, Universitas Ciputra. Ekspektasi: Untuk tiap peer identifikasi peristiwa pemicu, timeline respons, program (pemulihan intake, rebalance beasiswa, pertahanan akreditasi), dan hasil 12 bulan kemudian (angka intake, P&L program, status akreditasi). Kritisi tiap sumber. Cantumkan kutipan lengkap dengan tanggal. Hasilkan tabel perbandingan.'},
        {'instr':'Buka `m365.cloud.microsoft/chat` > Agents > **Researcher** > **Model Council**. Tempel prompt.',
         'prompt':'Tujuan: 3 playbook respons paling defensible untuk grup pendidikan swasta ASEAN yang terkena squeeze visa + masuk kompetitor + delay akreditasi secara bersamaan. Konteks: Zava Education harus melindungi kepercayaan MQA, hubungan universitas mitra, dan jaringan agen Indonesia sekaligus. Sumber: Model Council — gelar laporan paralel dari GPT-5.5 Thinking dan Claude Opus 4.7. Ekspektasi: Sorot perbedaan pendapat lintas council, tandai pandangan mayoritas dan minoritas. Tabel perbandingan: Playbook, Putusan Council, Pandangan Minoritas, Preseden ASEAN (kutip peer spesifik dengan tahun), Risiko Implementasi.'}
      ],
      persona=['Mod Admin','Mod Admin'],
      personaID=['Mod Admin','Mod Admin']),

      tool(T_ANALYST, M365_LIC, M365_ACCT, [
        {'instr':'Open `m365.cloud.microsoft/chat` > Agents > **Analyst**. Upload /EDU_01_Programme_PnL.xlsx AND /EDU_02_Intl_Student_Pipeline.xlsx. Paste the prompt below.',
         'prompt':'Goal: Quantify the combined impact of the international-student visa squeeze and competitor programme cannibalisation on FY2026 programme P&L. Context: ExCo needs an evidence-based view in 48 hours. Source: the 2 uploaded files — programme P&L by faculty + intake forecast vs prior year; international-student pipeline by source country and study agent. Expectation: (1) RAG bar chart of programmes ranked by FY2026 EBITDA contribution at risk; (2) waterfall of Group EBITDA bridge — Baseline → Visa squeeze revenue loss → Competitor cannibalisation → Scholarship rebalance upside → Recovered EBITDA; (3) sensitivity table on intake recovery (60% / 75% / 90% of prior intake) showing programme-level P&L per scenario. Output an ExCo-ready RAG dashboard.'}
      ], DESC_ANALYST,
      promptsID=[
        {'instr':'Buka `m365.cloud.microsoft/chat` > Agents > **Analyst**. Unggah /EDU_01_Programme_PnL.xlsx DAN /EDU_02_Intl_Student_Pipeline.xlsx. Tempel prompt.',
         'prompt':'Tujuan: Kuantifikasi dampak gabungan squeeze visa mahasiswa internasional dan kanibalisasi program kompetitor terhadap P&L program FY2026. Konteks: ExCo butuh pandangan berbasis bukti dalam 48 jam. Sumber: 2 file yang diunggah — P&L program per fakultas + forecast intake vs tahun sebelumnya; pipeline mahasiswa internasional per negara sumber dan agen studi. Ekspektasi: (1) Bar chart RAG program diurutkan berdasar kontribusi EBITDA FY2026 berisiko; (2) waterfall bridge EBITDA Grup — Baseline → kehilangan revenue squeeze visa → kanibalisasi kompetitor → upside rebalance beasiswa → EBITDA pulih; (3) tabel sensitivitas pemulihan intake (60% / 75% / 90% dari intake sebelumnya) menampilkan P&L tingkat program per skenario. Hasilkan dashboard RAG siap-ExCo.'}
      ],
      persona=['Hadar Caspit'],
      personaID=['Hadar Caspit']),

      tool(T_EXCEL, M365_LIC, M365_ACCT, [
        {'instr':'Open `/EDU_01_Programme_PnL.xlsx` in Excel for the Web. Open the **Copilot pane**. Paste the prompt below.',
         'prompt':'Goal: Build a single ExCo-ready dashboard sheet combining programme P&L, international-student pipeline and competitor positioning. Context: ExCo meets in 14 days; January intake in 8 weeks. Source: combine all relevant tabs — Programme PnL, Intake Pipeline, Scholarship Spend, Faculty Cost. Expectation: New sheet "ExCo Dashboard" with KPI tiles for Revenue at Risk MYR M, Intake Forecast vs Prior Year, Programmes Under MQA Review, Competitor Programmes Live; horizontal bar of programmes ranked worst to best on EBITDA; line chart of pipeline trajectory across 3 scenarios; RAG conditional formatting; sparkline column. Do not modify source tabs.'}
      ], '',
      promptsID=[
        {'instr':'Buka `/EDU_01_Programme_PnL.xlsx` di Excel for the Web. Buka **Copilot pane**. Tempel prompt.',
         'prompt':'Tujuan: Bangun satu sheet dashboard siap-ExCo yang menggabungkan P&L program, pipeline mahasiswa internasional dan positioning kompetitor. Konteks: ExCo bertemu 14 hari; intake Januari 8 minggu lagi. Sumber: gabungkan tab Programme PnL, Intake Pipeline, Scholarship Spend, Faculty Cost. Ekspektasi: Sheet baru "Dashboard ExCo" dengan KPI tile untuk Revenue Berisiko Rp Miliar, Forecast Intake vs Tahun Sebelumnya, Program di Bawah Review MQA, Program Kompetitor Live; bar horizontal program diurutkan terburuk ke terbaik berdasar EBITDA; line chart trajectory pipeline lintas 3 skenario; format kondisional RAG; kolom sparkline. Jangan modifikasi tab sumber.'}
      ],
      persona=['Hadar Caspit'],
      personaID=['Hadar Caspit']),

      tool(T_WORD, M365_LIC, M365_ACCT, [
        {'instr':'Open a new blank Word doc in Word for the Web. Open the **Copilot pane**. Reference /EDU_03_MQA_Accreditation_Brief.docx and /EDU_05_FY2026_Intake_Recovery_Playbook.docx using `/`. Paste the prompt below.',
         'prompt':'Goal: Draft the 4-page ExCo paper "January 2026 Intake Recovery, MQA Accreditation Defence & Competitor Response — ExCo Pack". Context: ExCo in 14 days. Source: the two referenced docs + the intake-pipeline numbers I will paste. Expectation: Sections — (1) Executive summary in 5 bullets; (2) International-student pipeline status by source country; (3) MQA accreditation review and defence programme; (4) Competitor programme map and counter-positioning; (5) Programme P&L recovery levers; (6) Decisions requested. Tone: precise, ExCo-ready, no speculation. Cite source files at the end of every section.'}
      ], DESC_WORD,
      promptsID=[
        {'instr':'Buka dokumen Word baru kosong di Word for the Web. Buka **Copilot pane**. Referensikan /EDU_03_MQA_Accreditation_Brief.docx dan /EDU_05_FY2026_Intake_Recovery_Playbook.docx menggunakan `/`. Tempel prompt.',
         'prompt':'Tujuan: Susun paper ExCo 4 halaman "Pemulihan Intake Januari 2026, Pertahanan Akreditasi MQA & Respons Kompetitor — Pack ExCo". Konteks: ExCo dalam 14 hari. Sumber: dua dokumen yang direferensikan + angka pipeline intake yang akan saya tempelkan. Ekspektasi: Bagian — (1) Ringkasan eksekutif 5 bullet; (2) Status pipeline mahasiswa internasional per negara sumber; (3) Review akreditasi MQA dan program pertahanan; (4) Peta program kompetitor dan counter-positioning; (5) Lever pemulihan P&L program; (6) Keputusan yang diminta. Nada: presisi, siap-ExCo, tanpa spekulasi. Kutip file sumber di akhir tiap bagian.'}
      ],
      persona=['Hadar Caspit'],
      personaID=['Hadar Caspit']),

      tool(T_PPT, M365_LIC, M365_ACCT, [
        {'instr':'Open a new PowerPoint deck in PowerPoint for the Web. Open the **Copilot pane**. Paste the prompt below.',
         'prompt':'Goal: 9-slide ExCo deck on January intake recovery + MQA accreditation defence + competitor response. Context: ExCo in 14 days. Source: my Word brief and dashboard. Expectation: (1) Cover; (2) Situation — three converging pressures; (3) Stakeholder Map RAG (MQA, JPT, Kemendikbudristek, BAN-PT, partner universities, study agents); (4) International-Student Pipeline Recovery; (5) MQA Accreditation Defence Programme; (6) Competitor Programme Map; (7) Programme P&L Recovery Bridge; (8) FY2026 Intake Playbook; (9) Decisions Requested. Brand colours #7C3AED + #5B21B6, 18pt min body text, 1 chart per slide.'}
      ], DESC_PPT,
      promptsID=[
        {'instr':'Buka deck PowerPoint baru di PowerPoint for the Web. Buka **Copilot pane**. Tempel prompt.',
         'prompt':'Tujuan: Deck 9 slide ExCo tentang pemulihan intake Januari + pertahanan akreditasi MQA + respons kompetitor. Konteks: ExCo dalam 14 hari. Sumber: brief Word dan dashboard saya. Ekspektasi: (1) Cover; (2) Situasi — tiga tekanan yang bertemu; (3) Peta Pemangku Kepentingan RAG (MQA, JPT, Kemendikbudristek, BAN-PT, universitas mitra, agen studi); (4) Pemulihan Pipeline Mahasiswa Internasional; (5) Program Pertahanan Akreditasi MQA; (6) Peta Program Kompetitor; (7) Bridge Pemulihan P&L Program; (8) Playbook Intake FY2026; (9) Keputusan yang Diminta. Warna brand #7C3AED + #5B21B6, font tubuh min 18pt, 1 chart per slide.'}
      ],
      persona=['Sasha Ouellet'],
      personaID=['Sasha Ouellet']),

      tool(T_OUTLOOK, M365_LIC, M365_ACCT, [
        {'instr':'Open Outlook on the Web. Open the email thread "January intake recovery + MQA accreditation review — Group CEO follow-up". Click the **Copilot icon**. Paste the prompt below.',
         'prompt':'Goal: Draft a single email to the Zava Education ExCo and the 4 flagship-programme deans plus the Admissions Director. Context: visa squeeze, MQA review and competitor entry active 8 weeks before January intake. Source: the email thread above. Expectation: Subject line, 4 short paragraphs covering the situation, the 3 actions each dean and the Admissions Director must complete in 72 hours (programme defence narrative; agent-network briefing; scholarship rebalance proposal), the MQA engagement track, and the ExCo date. Tone: firm, supportive, accountable.'}
      ], DESC_OUTLOOK,
      promptsID=[
        {'instr':'Buka Outlook on the Web. Buka thread email "Pemulihan intake Januari + review akreditasi MQA — tindak lanjut CEO Grup". Klik **ikon Copilot**. Tempel prompt.',
         'prompt':'Tujuan: Susun satu email ke ExCo Zava Education dan 4 dekan program flagship plus Direktur Admissions. Konteks: squeeze visa, review MQA dan masuk kompetitor aktif 8 minggu sebelum intake Januari. Sumber: thread email di atas. Ekspektasi: Baris subjek, 4 paragraf pendek mencakup situasi, 3 aksi per dekan dan Direktur Admissions dalam 72 jam (naratif pertahanan program; briefing jaringan agen; usulan rebalance beasiswa), jalur engagement MQA, dan tanggal ExCo. Nada: tegas, suportif, akuntabel.'}
      ],
      persona=['Hadar Caspit'],
      personaID=['Hadar Caspit']),

      tool(T_TEAMS, M365_LIC, M365_ACCT, [
        {'instr':'**(1) In Teams**, open **Calendar** → click the past meeting **"MQA Accreditation Review Briefing"**. On the Recap page, walk through **AI Notes**, **Custom summary** (Speaker template), and **Audio recap**. **(2) In Word for the Web**, open a new blank document and type the minutes template (Date · Decisions · Actions · Risks · Open Questions). **(3) Click the Copilot icon** in Word and paste the prompt below — Copilot in Word references the recap with `/`.',
         'prompt':'Create meeting minutes for the Teams meeting /MQA Accreditation Review Briefing. Use the template on this page. Sections: (1) Date and Attendees; (2) Decisions Taken; (3) Action Items with Owner and Due Date; (4) Risks Raised; (5) Open Questions. Quote MQA reviewers and the Quality Assurance Director verbatim where wording matters. Flag any decision linked to the January intake deferral as Critical Path. Save as Minutes_MQA_Accreditation_Review.docx.'}
      ], '',
      promptsID=[
        {'instr':'**(1) Di Teams**, buka **Calendar** → klik rapat lampau **"Briefing Review Akreditasi MQA"**. Pada halaman Recap, tampilkan **AI Notes**, **Custom summary** (template Speaker), dan **Audio recap**. **(2) Di Word for the Web**, buka dokumen baru kosong dan ketik template notulen (Tanggal · Keputusan · Action · Risiko · Pertanyaan Terbuka). **(3) Klik ikon Copilot** di Word dan tempel prompt — Copilot in Word mereferensikan recap dengan `/`.',
         'prompt':'Buat notulen rapat untuk rapat Teams /Briefing Review Akreditasi MQA. Gunakan template di halaman ini. Bagian: (1) Tanggal dan Peserta; (2) Keputusan; (3) Action dengan Pemilik dan Tenggat; (4) Risiko; (5) Pertanyaan Terbuka. Kutip reviewer MQA dan Direktur Quality Assurance secara harfiah jika redaksinya penting. Tandai keputusan terkait deferral intake Januari sebagai Critical Path. Simpan sebagai Notulen_Review_Akreditasi_MQA.docx.'}
      ],
      persona=['Sasha Ouellet'],
      personaID=['Sasha Ouellet']),

      tool(T_NOTEBOOK, M365_LIC, M365_ACCT, [
        {'instr':'All sources are loaded in the notebook. The Instructions field is set. Type the prompt below in the notebook chat.',
         'prompt':'Synthesise across all sources to produce a 10-bullet ExCo narrative. Cover: international-student pipeline status by source country; MQA accreditation defence programme; competitor programme map; programme P&L recovery levers; scholarship rebalance proposal; agent-network engagement; financial impact bridge; risk register; FY2026 intake playbook; decisions requested. Cite the source file (and tab/section) at the end of every bullet.'}
      ], DESC_NOTEBOOK,
      promptsID=[
        {'instr':'Semua sumber sudah dimuat di notebook. Field Instructions sudah diset. Ketik prompt di bawah pada chat notebook.',
         'prompt':'Sintesakan dari semua sumber untuk menghasilkan narasi ExCo 10-bullet. Cakup: status pipeline mahasiswa internasional per negara sumber; program pertahanan akreditasi MQA; peta program kompetitor; lever pemulihan P&L program; usulan rebalance beasiswa; engagement jaringan agen; bridge dampak finansial; register risiko; playbook intake FY2026; keputusan yang diminta. Kutip file sumber (dan tab/bagian) di akhir tiap bullet.'}
      ],
      persona=['Mod Admin'],
      personaID=['Mod Admin'],
      notebookMeta={
        'sources':['/EDU_01_Programme_PnL.xlsx','/EDU_02_Intl_Student_Pipeline.xlsx','/EDU_05_FY2026_Intake_Recovery_Playbook.docx'],
        'instructions':'You are the Group CEO of Zava Education Holdings preparing an ExCo pack on converging international-student visa squeeze, new competitor private uni and MQA accreditation review delay 8 weeks before the January 2026 intake. Always cite the source file and tab/section. Tone: precise, ExCo-ready, no speculation about MQA or Kemendikbudristek intentions beyond what they have communicated in writing. Use MYR for Group totals (1 MYR ≈ 3,580 IDR). Reference real ASEAN peers (Sunway Education, Taylor Education, INTI, KDU, APU, UPH, BINUS, Sampoerna University) where benchmark precedent strengthens the argument.',
        'instructionsID':'Anda adalah CEO Grup Zava Education Holdings yang menyiapkan paket ExCo tentang konvergensi squeeze visa mahasiswa internasional, universitas swasta kompetitor baru dan delay review akreditasi MQA 8 minggu sebelum intake Januari 2026. Selalu kutip file sumber dan tab/bagian. Nada: presisi, siap-ExCo, tanpa spekulasi tentang niat MQA atau Kemendikbudristek di luar yang sudah disampaikan tertulis. Gunakan RM untuk total Grup (1 RM ≈ 3.580 Rp). Referensikan peer ASEAN riil (Sunway Education, Taylor Education, INTI, KDU, APU, UPH, BINUS, Sampoerna University) bila preseden benchmark memperkuat argumen.'
      }),

      tool(T_COWORK, FRONTIER_LIC, M365_ACCT, [
        {'instr':'Open `m365.cloud.microsoft` > left nav > **Agents** > **Cowork**. Paste the single prompt below — Cowork delegates 5 parallel sub-tasks. Frontier required.',
         'prompt':'Cowork — January Intake 8-Week Sprint. Run these in parallel: (1) 📝 Draft Word — January Intake Recovery Brief 4 pages, sources /EDU_01_Programme_PnL.xlsx and /EDU_02_Intl_Student_Pipeline.xlsx. (2) 📝 Draft Word — MQA Accreditation Defence Talking Points 2 pages, source /EDU_03_MQA_Accreditation_Brief.docx. (3) ✉️ Send email to Zava Education ExCo and the 4 flagship-programme deans with 3 actions in 72 hours. (4) 📅 Schedule 90-min ExCo Pre-Read tomorrow 8am MYT titled "January Intake Recovery Alignment". (5) 💬 Post Teams message to #zava-education-exco with one-line headline + dashboard link.'}
      ], DESC_COWORK,
      promptsID=[
        {'instr':'Buka `m365.cloud.microsoft` > nav kiri > **Agents** > **Cowork**. Tempel prompt tunggal — Cowork mendelegasikan 5 sub-tugas paralel. Frontier diperlukan.',
         'prompt':'Cowork — Sprint 8 Minggu Intake Januari. Jalankan paralel: (1) 📝 Susun Word — Brief Pemulihan Intake Januari 4 halaman, sumber /EDU_01_Programme_PnL.xlsx dan /EDU_02_Intl_Student_Pipeline.xlsx. (2) 📝 Susun Word — Talking Points Pertahanan Akreditasi MQA 2 halaman, sumber /EDU_03_MQA_Accreditation_Brief.docx. (3) ✉️ Kirim email ke ExCo Zava Education dan 4 dekan program flagship dengan 3 aksi dalam 72 jam. (4) 📅 Jadwalkan Pre-Read ExCo 90 menit besok 08:00 WIB berjudul "Penyelarasan Pemulihan Intake Januari". (5) 💬 Posting pesan Teams di #zava-education-exco dengan headline satu baris + tautan dashboard.'}
      ],
      persona=['Mod Admin'],
      personaID=['Mod Admin']),

      tool(T_WORD_AGT, ANY_LIC, ANY_ACCT, [
        {'instr':'Open `m365.cloud.microsoft/chat` → Agents tab → **Word Agent**. Paste the prompt below — the agent returns a fully drafted .docx.',
         'prompt':'Goal: Generate a 4-page Group CEO Crisis Brief in Word. Context: international-student visa squeeze MYR 92M, new competitor private uni, MQA accreditation review delay, January intake at risk. Source: /EDU_01_Programme_PnL.xlsx AND /EDU_02_Intl_Student_Pipeline.xlsx. Expectation: Sections — Executive Summary 5 bullets; Current Status of all 3 workstreams; Programme; Financial Impact; Stakeholder Map (MQA / JPT / Kemendikbudristek / BAN-PT / partner universities / study agents); Decisions Requested. Tone: precise, ExCo-ready. Save as Zava_Education_Crisis_Brief.docx.'}
      ], DESC_WORD_AGT,
      promptsID=[
        {'instr':'Buka `m365.cloud.microsoft/chat` → tab Agents → **Word Agent**. Tempel prompt — agent mengembalikan .docx yang sudah didraf penuh.',
         'prompt':'Tujuan: Hasilkan Brief Krisis CEO Grup 4 halaman dalam Word. Konteks: squeeze visa mahasiswa internasional Rp 329 miliar, universitas swasta kompetitor baru, delay review akreditasi MQA, intake Januari berisiko. Sumber: /EDU_01_Programme_PnL.xlsx DAN /EDU_02_Intl_Student_Pipeline.xlsx. Ekspektasi: Bagian — Ringkasan Eksekutif 5 bullet; Status Saat Ini ketiga workstream; Program; Dampak Finansial; Peta Pemangku Kepentingan (MQA / JPT / Kemendikbudristek / BAN-PT / universitas mitra / agen studi); Keputusan yang Diminta. Nada: presisi, siap-ExCo. Simpan sebagai Brief_Krisis_Zava_Education.docx.'}
      ],
      persona=['Sasha Ouellet'],
      personaID=['Sasha Ouellet']),

      tool(T_PPT_AGT, ANY_LIC, ANY_ACCT, [
        {'instr':'Open `m365.cloud.microsoft/chat` → Agents tab → **PowerPoint Agent**. Paste the prompt below.',
         'prompt':'Goal: 9-slide ExCo deck on January intake recovery + MQA accreditation defence + competitor response. Context: ExCo in 14 days. Source: /Zava_Education_Crisis_Brief.docx and /EDU_02_Intl_Student_Pipeline.xlsx. Expectation: Cover; Situation; Stakeholder Map RAG; Pipeline Recovery; MQA Defence; Competitor Map; Programme P&L Bridge; FY2026 Playbook; Decisions. Brand #7C3AED + #5B21B6, 18pt min body, 1 chart/slide. Save as Zava_Education_ExCo_Deck.pptx.'}
      ], DESC_PPT_AGT,
      promptsID=[
        {'instr':'Buka `m365.cloud.microsoft/chat` → tab Agents → **PowerPoint Agent**. Tempel prompt.',
         'prompt':'Tujuan: Deck 9 slide ExCo tentang pemulihan intake Januari + pertahanan akreditasi MQA + respons kompetitor. Konteks: ExCo dalam 14 hari. Sumber: /Brief_Krisis_Zava_Education.docx dan /EDU_02_Intl_Student_Pipeline.xlsx. Ekspektasi: Cover; Situasi; Peta Pemangku Kepentingan RAG; Pemulihan Pipeline; Pertahanan MQA; Peta Kompetitor; Bridge P&L Program; Playbook FY2026; Keputusan. Brand #7C3AED + #5B21B6, font tubuh min 18pt, 1 chart/slide. Simpan sebagai Deck_ExCo_Zava_Education.pptx.'}
      ],
      persona=['Sasha Ouellet'],
      personaID=['Sasha Ouellet']),

      tool(T_XL_AGT, ANY_LIC, ANY_ACCT, [
        {'instr':'Open `m365.cloud.microsoft/chat` → Agents tab → **Excel Agent**. Paste the prompt below.',
         'prompt':'Goal: Build a programme P&L + intake pipeline + MQA accreditation tracker workbook. Context: operating tracker for the Group CEO. Source: schema only. Expectation: Sheet 1 Programme PnL (12 flagship programmes Q-on-Q); Sheet 2 Intake Pipeline (by source country and study agent); Sheet 3 MQA Accreditation Watchlist (3 programmes under review); Sheet 4 Dashboard with KPI tiles + RAG conditional formatting. Save as Zava_Education_Operations_Tracker.xlsx.'}
      ], DESC_XL_AGT,
      promptsID=[
        {'instr':'Buka `m365.cloud.microsoft/chat` → tab Agents → **Excel Agent**. Tempel prompt.',
         'prompt':'Tujuan: Bangun workbook tracker P&L program + pipeline intake + akreditasi MQA. Konteks: tracker operasi untuk CEO Grup. Sumber: hanya skema. Ekspektasi: Sheet 1 P&L Program (12 program flagship Q-on-Q); Sheet 2 Pipeline Intake (per negara sumber dan agen studi); Sheet 3 Watchlist Akreditasi MQA (3 program di bawah review); Sheet 4 Dashboard dengan KPI tile + format kondisional RAG. Simpan sebagai Tracker_Operasi_Zava_Education.xlsx.'}
      ],
      persona=['Hadar Caspit'],
      personaID=['Hadar Caspit']),

      tool(T_BUILDER, ANY_LIC, ANY_ACCT, [
        {'instr':'Open `m365.cloud.microsoft/chat` > Agents > **+ Create an agent**. Pick ONE of the 3 agents below. Paste the chosen description into the **Describe** field.',
         'prompt':'**Option A — Zava Education Intake Watch.** Build an agent for the Group CEO and Admissions team to track and explain intake pipeline daily. Ground every answer on /EDU_02_Intl_Student_Pipeline.xlsx and the agent-network playbook. Always cite file and tab. Classify pipeline as On-Track / Watch / Behind. Tone: precise, education-grade. Starter prompts: (1) What is the rolling intake forecast vs prior year; (2) Which source countries are slipping the most; (3) Build a weekly Admissions dashboard; (4) Draft a study-agent briefing memo; (5) Summarise the intake recovery story for the ExCo.'},
        {'instr':'**Option B — alternative agent.** Same Create-an-agent flow with a different specialisation.',
         'prompt':'**Option B — Zava Education MQA Accreditation Agent.** Build an agent for the Quality Assurance Director and the 3 programme deans whose programmes are under MQA review. Ground every answer on /EDU_03_MQA_Accreditation_Brief.docx. Always cite section. Classify each open MQA finding as Closed / In Progress / Awaiting Internal Sign-Off. Tone: factual, regulator-facing, no admission of unproven causation. Starter prompts: (1) What MQA findings are still open; (2) Draft a holding line for MQA; (3) What are the next 3 milestones; (4) Build a weekly accreditation status dashboard; (5) Summarise the MQA position for the ExCo.'},
        {'instr':'**Option C — alternative agent.** Same flow.',
         'prompt':'**Option C — Zava Education Competitor Watch Agent.** Build an agent for the Strategy and Marketing teams to track the new competitor private uni weekly. Ground every answer on /EDU_04_Competitor_Programme_Map.docx and /EDU_01_Programme_PnL.xlsx. Always cite file and section. Classify each competitor programme as Watch / Defend / Reposition. Tone: factual, marketing-grade. Starter prompts: (1) Which competitor programmes pose the biggest threat; (2) Draft a counter-positioning narrative; (3) Build a weekly competitor watch dashboard; (4) What is the scholarship-rebalance proposal; (5) Summarise the competitor map for the ExCo.'},
        {'instr':'**Test.** After the agent is created, click into it and use the right test pane to validate grounding, citations, scope.',
         'prompt':'Give me the 60-second version of the international-student visa squeeze + new competitor private uni + MQA accreditation review, the worst 3 issues, the response programme, and the decisions I must take to the ExCo in 14 days. Cite the file and tab/section for every paragraph.'},
        {'instr':'**Share.** Click the agent → **Share** → add recipients with **Use** access.',
         'prompt':'Share with the Zava Education ExCo (Group CEO, Group CFO, COO, Quality Assurance Director, Admissions Director, the 4 flagship-programme deans, Marketing Director) — Use access. Send notification: "This agent is now in your M365 Copilot chat — ground every January-intake / MQA / competitor question through it for the next 90 days."'}
      ], DESC_BUILDER,
      promptsID=[
        {'instr':'Buka `m365.cloud.microsoft/chat` > Agents > **+ Create an agent**. Pilih SATU dari 3 agent. Tempel deskripsi ke field **Describe**.',
         'prompt':'**Opsi A — Zava Education Intake Watch.** Bangun agent untuk CEO Grup dan tim Admissions untuk melacak dan menjelaskan pipeline intake harian. Dasarkan pada /EDU_02_Intl_Student_Pipeline.xlsx dan playbook jaringan agen. Selalu kutip file dan tab. Klasifikasikan pipeline sebagai On-Track / Watch / Behind. Nada: presisi, education-grade. Starter prompt: (1) Forecast intake rolling vs tahun sebelumnya; (2) Negara sumber mana yang paling slip; (3) Bangun dashboard Admissions mingguan; (4) Susun memo briefing agen studi; (5) Rangkum cerita pemulihan intake untuk ExCo.'},
        {'instr':'**Opsi B — agent alternatif.** Alur Create-an-agent sama dengan spesialisasi berbeda.',
         'prompt':'**Opsi B — Zava Education MQA Accreditation Agent.** Bangun agent untuk Direktur Quality Assurance dan 3 dekan program yang programnya di bawah review MQA. Dasarkan pada /EDU_03_MQA_Accreditation_Brief.docx. Selalu kutip bagian. Klasifikasikan tiap temuan MQA terbuka sebagai Closed / In Progress / Awaiting Internal Sign-Off. Nada: faktual, regulator-facing, tanpa pengakuan kausalitas yang belum terbukti. Starter prompt: (1) Temuan MQA mana yang masih terbuka; (2) Susun holding line untuk MQA; (3) 3 milestone berikutnya; (4) Bangun dashboard status akreditasi mingguan; (5) Rangkum posisi MQA untuk ExCo.'},
        {'instr':'**Opsi C — agent alternatif.** Alur sama.',
         'prompt':'**Opsi C — Zava Education Competitor Watch Agent.** Bangun agent untuk tim Strategi dan Marketing untuk melacak universitas swasta kompetitor baru mingguan. Dasarkan pada /EDU_04_Competitor_Programme_Map.docx dan /EDU_01_Programme_PnL.xlsx. Selalu kutip file dan bagian. Klasifikasikan tiap program kompetitor sebagai Watch / Defend / Reposition. Nada: faktual, marketing-grade. Starter prompt: (1) Program kompetitor mana yang paling mengancam; (2) Susun naratif counter-positioning; (3) Bangun dashboard watch kompetitor mingguan; (4) Usulan rebalance beasiswa; (5) Rangkum peta kompetitor untuk ExCo.'},
        {'instr':'**Uji.** Validasi grounding, kutipan, cakupan.',
         'prompt':'Berikan versi 60 detik dari squeeze visa mahasiswa internasional + universitas swasta kompetitor baru + review akreditasi MQA, 3 isu terburuk, program respons, dan keputusan yang harus saya bawa ke ExCo dalam 14 hari. Kutip file dan tab/bagian untuk tiap paragraf.'},
        {'instr':'**Bagikan.** Klik agent → **Share** → tambahkan penerima dengan akses **Use**.',
         'prompt':'Bagikan ke ExCo Zava Education (CEO Grup, Direktur Keuangan Grup, COO, Direktur Quality Assurance, Direktur Admissions, 4 dekan program flagship, Direktur Marketing) — akses Use. Kirim notifikasi: "Agent ini sekarang ada di M365 Copilot chat Anda — dasarkan tiap pertanyaan intake Januari / MQA / kompetitor melalui agent ini selama 90 hari ke depan."'}
      ],
      persona=['Mod Admin','Mod Admin','Mod Admin','Sasha Ouellet','Sasha Ouellet'],
      personaID=['Mod Admin','Mod Admin','Mod Admin','Sasha Ouellet','Sasha Ouellet']),
    ],
    companyID='Zava Education Holdings',
    taglineID='Squeeze visa mahasiswa internasional Rp 329 miliar + universitas swasta kompetitor baru + delay review akreditasi MQA — ExCo Grup dalam 14 hari.',
    scenarioID="Zava Education Holdings adalah grup pendidikan swasta tercatat di bursa ASEAN yang mengoperasikan universitas swasta (12.400 mahasiswa), college foundation/A-level (4.200 mahasiswa) dan platform e-learning B2B/B2C dengan 180.000 pembelajar aktif di Malaysia dan Indonesia. Tiga tekanan menghantam intake Januari 2026: (1) pengetatan kuota visa mahasiswa internasional oleh Jabatan Imigresen Malaysia dan scrutiny tambahan Kemendikbudristek atas intake Indonesia menempatkan Rp 329 miliar (RM 92 juta) revenue Grup pada risiko; (2) universitas swasta kompetitor baru yang didukung sovereign fund regional meluncurkan 6 program mid-tier (Computing, Business, Engineering, Hospitality, Communication, Allied Health) dengan harga beasiswa agresif — funnel early-admission untuk 4 program flagship kami menunjukkan penurunan 23% YoY; (3) Malaysian Qualifications Agency (MQA) menandai 3 program kami untuk perpanjangan review akreditasi — delay 90 hari akan memaksa deferral intake Januari untuk kohort tersebut. CEO Grup butuh paket ExCo dalam 14 hari mencakup P&L program, pemulihan pipeline mahasiswa internasional, pertahanan akreditasi MQA, peta program kompetitor, dan playbook pemulihan intake FY2026. Frame customer riil: grup ini beroperasi serupa dengan **Sunway Education Group**, **Taylor's Education Group**, **INTI International University**, **KDU University College**, **APU**, **Universitas Pelita Harapan (UPH)**, **BINUS University**, **Sampoerna University**, dan **Universitas Ciputra** — dengan regulator termasuk **MQA**, **JPT**, **Kementerian Pendidikan Tinggi MY**, **Kemendikbudristek ID**, dan **BAN-PT** aktif bersamaan.",
    relevantDepts=['dept-finance','dept-strategy','dept-operations','dept-marketing','dept-legal','dept-hr-talent'],
    personas=[
      {'name':'Sasha Ouellet','role':'Group CEO - Education','roleID':'CEO Grup - Pendidikan','acct':FREE_ACCT,'lic':FREE_LIC,'color':'#7C3AED'},
      {'name':'Mod Admin','role':'Group Quality Assurance Director','roleID':'Direktur Quality Assurance Grup','acct':M365_ACCT,'lic':M365_LIC,'color':'#059669'},
      {'name':'Hadar Caspit','role':'Group CFO','roleID':'Direktur Keuangan Grup','acct':M365_ACCT,'lic':M365_LIC,'color':'#1E40AF'},
      {'name':'Daichi Kimura','role':'Admissions & Agent Network Director','roleID':'Direktur Admissions & Jaringan Agen','acct':M365_ACCT,'lic':M365_LIC,'color':'#DC2626'}
    ],
    storyboard=[
      {'ex':1,'title':'Research & Brief','titleID':'Riset & Pengarahan','minutes':18,'mode':'Show & Tell + Hands-on',
       'summary':'Frame the visa squeeze + competitor entry + MQA delay before the January intake clock runs out.',
       'summaryID':'Bingkai squeeze visa + masuk kompetitor + delay MQA sebelum clock intake Januari habis.',
       'tasks':[
         {'verb':'Frame the morning question and lock the day priorities','verbID':'Susun pertanyaan pagi dan kunci prioritas hari ini','toolId':T_CHAT,'mode':'Show & Tell'},
         {'verb':'Run an outside-in peer scan and pull proven plays','verbID':'Lakukan pemindaian peer dari luar dan tarik praktik terbaik','toolId':T_RESEARCHER,'mode':'Show & Tell'},
         {'verb':'Generate a board-ready brief straight from chat','verbID':'Hasilkan brief siap-Direksi langsung dari chat','toolId':T_WORD_AGT,'mode':'Hands-on'}]},
      {'ex':2,'title':'Analyse & Decide','titleID':'Analisis & Putuskan','minutes':18,'mode':'Hands-on',
       'summary':'Quantify the programme P&L + pipeline + competitor combined impact; build an ExCo dashboard.',
       'summaryID':'Kuantifikasi dampak gabungan P&L program + pipeline + kompetitor; bangun dashboard ExCo.',
       'tasks':[
         {'verb':'Crunch the numbers and surface the biggest gaps','verbID':'Olah angka dan ungkap celah terbesar','toolId':T_ANALYST,'mode':'Hands-on'},
         {'verb':'Build a single-pane operating dashboard','verbID':'Bangun dashboard operasi satu-halaman','toolId':T_EXCEL,'mode':'Hands-on'},
         {'verb':'Spin up a recurring tracker workbook from chat','verbID':'Buat workbook tracker berulang dari chat','toolId':T_XL_AGT,'mode':'Hands-on'}]},
      {'ex':3,'title':'Communicate & Coordinate','titleID':'Komunikasi & Koordinasi','minutes':18,'mode':'Hands-on',
       'summary':'Brief deans and Admissions, capture the MQA Review recap, and assemble the ExCo deck.',
       'summaryID':'Brief dekan dan Admissions, capture recap Review MQA, dan rakit deck ExCo.',
       'tasks':[
         {'verb':'Draft the stakeholder alignment email','verbID':'Draf email penyelarasan stakeholder','toolId':T_OUTLOOK,'mode':'Hands-on'},
         {'verb':'Recap the meeting and turn it into minutes','verbID':'Recap rapat dan ubah ke notulen','toolId':T_TEAMS,'mode':'Hands-on'},
         {'verb':'Generate a board-ready deck from chat','verbID':'Hasilkan deck siap-Direksi dari chat','toolId':T_PPT_AGT,'mode':'Hands-on'},
         {'verb':'Delegate a 5-task parallel sprint','verbID':'Delegasikan 5-tugas paralel ke Cowork','toolId':T_COWORK,'mode':'Show & Tell'}]},
      {'ex':4,'title':'Build & Scale','titleID':'Bangun & Skala','minutes':15,'mode':'Show & Tell',
       'summary':'Wrap the intake + MQA + competitor playbook into a reusable agent for the Zava Education operating team.',
       'summaryID':'Bungkus playbook intake + MQA + kompetitor ke dalam agent reusable untuk tim operasi Zava Education.',
       'tasks':[
         {'verb':'Pull every source into one synthesis notebook','verbID':'Tarik semua sumber ke satu notebook sintesis','toolId':T_NOTEBOOK,'mode':'Show & Tell'},
         {'verb':'Wrap the daily workflow into a reusable agent','verbID':'Bungkus alur kerja harian jadi agen yang dapat dipakai ulang','toolId':T_BUILDER,'mode':'Show & Tell'}]}
    ],
    geo='MY+ID'
))

# INDUSTRIES_12.append(... education ...)

# ╔══════════════════════════════════════════════════════════════════════╗
# ║  3.  UTILITIES — POWER GENERATION  (Zava Power)                      ║
# ╚══════════════════════════════════════════════════════════════════════╝
INDUSTRIES_12.append(ind(
    'power-utilities', 'sec-utilities', 'Utilities — Power Generation', '⚡', '#FACC15', '#CA8A04',
    'Zava Power',
    'PPA renewal at lower tariff threatens MYR 240M EBITDA + coal-to-renewables 2030 deadline + grid availability liquidated damages — Board in 21 days.',
    "Zava Power is an ASEAN independent power producer with a 4.2 GW gross portfolio across coal-fired, combined-cycle gas, large-scale solar, hydro and on-grid wind across Malaysia and Indonesia. The group operates under long-dated Power Purchase Agreements (PPAs) with TNB (Malaysia) and PLN Nusantara Power (Indonesia) as primary off-takers. Three pressures converge: (1) the largest coal-fired PPA (1,200 MW) is up for renewal in 14 months at a tariff structure that, under the regulator-imposed levelised cost framework, threatens MYR 240M of FY2027 EBITDA; (2) the Energy Commission Malaysia (Suruhanjaya Tenaga / ST) has codified a coal-to-renewables transition deadline by 2030, requiring MYR 2.1B of capex re-prioritisation across the BESS, large-scale solar and on-grid wind pipelines; (3) two grid-availability events at the Pasir Gudang and Cilegon plants triggered liquidated-damages claims from off-takers totalling MYR 38M YTD with a further MYR 22M contingent. The Group MD needs a Board pack in 21 days covering the PPA renewal model, the plant-availability remediation programme, the coal-to-renewables capex schedule, the ST/MEMR/PLN regulator pack, and the off-taker negotiation brief. Real customer reference frame: this group operates similarly to **TNB**, **YTL Power International**, **Petronas Gas**, **Mega First Corp (MFCB)**, **Cypark Resources**, **Indonesia Power**, **PLN Nusantara Power**, **Cikarang Listrindo**, **Adaro Power**, and **Medco Power** — with regulators including **Energy Commission Malaysia (ST)**, **MEMR (Kementerian ESDM)**, **PLN** (off-taker), and **KeTSA** active concurrently.",
    ['POW_01_PPA_Renewal_Model.xlsx','POW_02_Plant_Availability_Tracker.xlsx','POW_03_Coal_to_Renewables_Capex.xlsx','POW_04_ST_MEMR_Compliance_Pack.docx','POW_05_Off_Taker_Negotiation_Brief.docx'],
    [
      tool(T_CHAT, FREE_LIC, FREE_ACCT, [
        {'instr':'', 'prompt':'Goal: Frame the converging PPA renewal + coal-to-renewables 2030 deadline + grid-availability LD claims situation in plain English for the Group MD. Context: Zava Power runs 4.2 GW across coal, gas, solar, hydro and wind in MY+ID; PPA renewal in 14 months threatens MYR 240M EBITDA; LD claims MYR 38M YTD + MYR 22M contingent. Source: my notes from the morning Asset Operations call. Expectation: 1-page note with sections — Headline; What Happened; Stakeholder Position (ST, MEMR, KeTSA, TNB, PLN, MTN bondholders, lender consortium); Top 5 Questions the Board Will Ask; 3 Decisions the Group MD Must Take in 48 Hours. Tone: calm, precise, no power-sector jargon.'},
        {'instr':'', 'prompt':'Goal: Build the stakeholder communication map for the 3 converging pressures with Board in 21 days and PPA renewal in 14 months. Context: ST, MEMR, KeTSA, TNB, PLN Nusantara Power, lender consortium, MTN bondholders, the 5 plant General Managers, and the EPC partners on the BESS and solar pipeline. Source: known stakeholders. Expectation: RAG table — Red same-day, Amber 24-72h, Green monitor. Columns: Audience, Channel, Owner, Message Theme, Timing, Risk if Mishandled.'}
      ], DESC_CHAT,
      promptsID=[
        {'instr':'', 'prompt':'Tujuan: Bingkai konvergensi pembaruan PPA + deadline transisi batu bara ke energi terbarukan 2030 + klaim LD ketersediaan grid dalam bahasa sederhana untuk Direktur Pelaksana Grup. Konteks: Zava Power menjalankan 4,2 GW di batu bara, gas, surya, hidro dan angin di MY+ID; pembaruan PPA dalam 14 bulan mengancam EBITDA Rp 859 miliar (RM 240 juta); klaim LD Rp 136 miliar YTD + Rp 79 miliar kontinjen. Sumber: catatan saya dari rapat Asset Operations pagi. Ekspektasi: nota 1 halaman dengan bagian — Headline; Apa yang Terjadi; Posisi Pemangku Kepentingan (ST, MEMR, KeTSA, TNB, PLN, pemegang MTN, konsorsium pemberi pinjaman); 5 Pertanyaan Top dari Direksi; 3 Keputusan Direktur Pelaksana Grup dalam 48 Jam. Nada: tenang, presisi, hindari jargon sektor listrik.'},
        {'instr':'', 'prompt':'Tujuan: Bangun peta komunikasi pemangku kepentingan untuk 3 tekanan yang bertemu dengan Direksi 21 hari dan pembaruan PPA 14 bulan. Konteks: ST, MEMR, KeTSA, TNB, PLN Nusantara Power, konsorsium pemberi pinjaman, pemegang MTN, 5 General Manager pembangkit, dan mitra EPC pipeline BESS dan surya. Sumber: pemangku kepentingan yang dikenal. Ekspektasi: tabel RAG — Merah hari ini juga, Kuning 24-72 jam, Hijau pantau. Kolom: Audiens, Channel, Pemilik, Tema Pesan, Timing, Risiko bila Keliru.'}
      ],
      persona=['Sasha Ouellet','Hadar Caspit'],
      personaID=['Sasha Ouellet','Hadar Caspit']),

      tool(T_RESEARCHER, M365_LIC, M365_ACCT, [
        {'instr':'Open `m365.cloud.microsoft/chat` > Agents > **Researcher** > **Critique Mode**. Paste the prompt below.',
         'prompt':'Goal: Benchmark how ASEAN IPP peers handled simultaneous PPA-renewal-at-lower-tariff, coal-to-renewables transition mandates and grid-availability LD events between 2019 and 2025. Context: Zava Power must respond to ST, MEMR and PLN on parallel tracks. Source: peer disclosures (Bursa Malaysia / IDX), ST tariff registers, MEMR press releases, PLN annual reports. Real peers: TNB, YTL Power International, Petronas Gas, MFCB, Cypark Resources, Indonesia Power, PLN Nusantara Power, Cikarang Listrindo, Adaro Power, Medco Power. Expectation: For each peer, identify trigger event, response timeline, programme adopted (capex re-prioritisation, plant remediation, off-taker negotiation), and outcome 12-24 months later (tariff outcome, EBITDA impact, regulator stance). Critique each source. Cite all with publication date. Output as a comparison table.'},
        {'instr':'Open `m365.cloud.microsoft/chat` > Agents > **Researcher** > **Model Council**. Paste the prompt below.',
         'prompt':'Goal: 3 most defensible response playbooks for an ASEAN IPP hit simultaneously by PPA renewal + coal transition + LD claims. Context: Zava Power must protect ST/MEMR confidence, off-taker relationships and lender ratings concurrently. Source: Researcher Model Council — convene parallel reports from GPT-5.5 Thinking and Claude Opus 4.7. Expectation: Surface dissent across the council, mark majority and minority views. Comparison table: Playbook, Council Verdict, Dissenting View, ASEAN Precedent (cite specific peer year), Implementation Risk.'}
      ], DESC_RESEARCHER,
      promptsID=[
        {'instr':'Buka `m365.cloud.microsoft/chat` > Agents > **Researcher** > **Critique Mode**. Tempel prompt.',
         'prompt':'Tujuan: Benchmark bagaimana peer IPP ASEAN menangani pembaruan PPA pada tarif lebih rendah, mandat transisi batu bara ke energi terbarukan dan kejadian LD ketersediaan grid secara bersamaan antara 2019 hingga 2025. Konteks: Zava Power harus merespons ST, MEMR dan PLN di jalur paralel. Sumber: pengungkapan peer (Bursa Malaysia / BEI), register tarif ST, siaran pers MEMR, laporan tahunan PLN. Peer riil: TNB, YTL Power International, Petronas Gas, MFCB, Cypark Resources, Indonesia Power, PLN Nusantara Power, Cikarang Listrindo, Adaro Power, Medco Power. Ekspektasi: Untuk tiap peer identifikasi peristiwa pemicu, timeline respons, program (re-prioritisasi capex, remediasi pembangkit, negosiasi off-taker), dan hasil 12-24 bulan kemudian (hasil tarif, dampak EBITDA, sikap regulator). Kritisi tiap sumber. Cantumkan kutipan lengkap dengan tanggal. Hasilkan tabel perbandingan.'},
        {'instr':'Buka `m365.cloud.microsoft/chat` > Agents > **Researcher** > **Model Council**. Tempel prompt.',
         'prompt':'Tujuan: 3 playbook respons paling defensible untuk IPP ASEAN yang terkena pembaruan PPA + transisi batu bara + klaim LD secara bersamaan. Konteks: Zava Power harus melindungi kepercayaan ST/MEMR, hubungan off-taker dan rating pemberi pinjaman sekaligus. Sumber: Model Council — gelar laporan paralel dari GPT-5.5 Thinking dan Claude Opus 4.7. Ekspektasi: Sorot perbedaan pendapat lintas council, tandai pandangan mayoritas dan minoritas. Tabel perbandingan: Playbook, Putusan Council, Pandangan Minoritas, Preseden ASEAN (kutip peer spesifik dengan tahun), Risiko Implementasi.'}
      ],
      persona=['Mod Admin','Mod Admin'],
      personaID=['Mod Admin','Mod Admin']),

      tool(T_ANALYST, M365_LIC, M365_ACCT, [
        {'instr':'Open `m365.cloud.microsoft/chat` > Agents > **Analyst**. Upload /POW_01_PPA_Renewal_Model.xlsx AND /POW_02_Plant_Availability_Tracker.xlsx. Paste the prompt below.',
         'prompt':'Goal: Quantify the combined impact of the PPA renewal and grid-availability LD claims on FY2027 EBITDA. Context: Board needs an evidence-based view in 48 hours. Source: the 2 uploaded files — PPA tariff scenarios across base/stretch/regulator-aligned + plant availability events with LD exposure. Expectation: (1) RAG bar chart of plants ranked by FY2027 EBITDA contribution at risk; (2) waterfall of Group EBITDA bridge — Baseline → PPA tariff erosion → LD claims → Coal-to-renewables capex drag → Renewables ramp upside → Recovered EBITDA; (3) sensitivity table on PPA renewal tariff (-15% / -10% / -5%) showing EBITDA per scenario. Output a Board-ready RAG dashboard.'}
      ], DESC_ANALYST,
      promptsID=[
        {'instr':'Buka `m365.cloud.microsoft/chat` > Agents > **Analyst**. Unggah /POW_01_PPA_Renewal_Model.xlsx DAN /POW_02_Plant_Availability_Tracker.xlsx. Tempel prompt.',
         'prompt':'Tujuan: Kuantifikasi dampak gabungan pembaruan PPA dan klaim LD ketersediaan grid terhadap EBITDA FY2027. Konteks: Direksi butuh pandangan berbasis bukti dalam 48 jam. Sumber: 2 file yang diunggah — skenario tarif PPA lintas base/stretch/selaras-regulator + peristiwa ketersediaan pembangkit dengan eksposur LD. Ekspektasi: (1) Bar chart RAG pembangkit diurutkan berdasar kontribusi EBITDA FY2027 berisiko; (2) waterfall bridge EBITDA Grup — Baseline → erosi tarif PPA → klaim LD → drag capex transisi batu bara → upside ramp renewables → EBITDA pulih; (3) tabel sensitivitas tarif pembaruan PPA (-15% / -10% / -5%) menampilkan EBITDA per skenario. Hasilkan dashboard RAG siap-Direksi.'}
      ],
      persona=['Hadar Caspit'],
      personaID=['Hadar Caspit']),

      tool(T_EXCEL, M365_LIC, M365_ACCT, [
        {'instr':'Open `/POW_01_PPA_Renewal_Model.xlsx` in Excel for the Web. Open the **Copilot pane**. Paste the prompt below.',
         'prompt':'Goal: Build a single Board-ready dashboard sheet combining PPA tariff scenarios, plant availability and coal-to-renewables capex schedule. Context: Board meets in 21 days. Source: combine all relevant tabs — Tariff Scenarios, Plant Availability, Capex Schedule, LD Claims. Expectation: New sheet "Board Dashboard" with KPI tiles for EBITDA at Risk MYR M, Plant Availability %, Coal-to-Renewables Capex Required MYR B, LD Claims YTD; horizontal bar of plants ranked worst to best on EBITDA contribution; line chart of EBITDA trajectory across 3 PPA scenarios; RAG conditional formatting; sparkline column. Do not modify source tabs.'}
      ], '',
      promptsID=[
        {'instr':'Buka `/POW_01_PPA_Renewal_Model.xlsx` di Excel for the Web. Buka **Copilot pane**. Tempel prompt.',
         'prompt':'Tujuan: Bangun satu sheet dashboard siap-Direksi yang menggabungkan skenario tarif PPA, ketersediaan pembangkit dan jadwal capex transisi batu bara ke energi terbarukan. Konteks: Direksi bertemu 21 hari. Sumber: gabungkan tab Tariff Scenarios, Plant Availability, Capex Schedule, LD Claims. Ekspektasi: Sheet baru "Dashboard Direksi" dengan KPI tile untuk EBITDA Berisiko Rp Miliar, Ketersediaan Pembangkit %, Capex Transisi Batu Bara Rp Triliun, Klaim LD YTD; bar horizontal pembangkit diurutkan terburuk ke terbaik berdasar kontribusi EBITDA; line chart trajectory EBITDA lintas 3 skenario PPA; format kondisional RAG; kolom sparkline. Jangan modifikasi tab sumber.'}
      ],
      persona=['Hadar Caspit'],
      personaID=['Hadar Caspit']),

      tool(T_WORD, M365_LIC, M365_ACCT, [
        {'instr':'Open a new blank Word doc in Word for the Web. Open the **Copilot pane**. Reference /POW_04_ST_MEMR_Compliance_Pack.docx and /POW_05_Off_Taker_Negotiation_Brief.docx using `/`. Paste the prompt below.',
         'prompt':'Goal: Draft the 4-page Board paper "PPA Renewal Defence, Coal-to-Renewables Transition & Off-Taker Negotiation — Board Pack". Context: Board in 21 days. Source: the two referenced docs + the PPA scenario numbers I will paste. Expectation: Sections — (1) Executive summary in 5 bullets; (2) PPA renewal defence and tariff scenarios; (3) Plant availability remediation programme; (4) Coal-to-renewables capex re-prioritisation; (5) ST/MEMR/PLN regulator engagement; (6) Decisions requested. Tone: precise, Board-ready, no speculation. Cite source files at the end of every section.'}
      ], DESC_WORD,
      promptsID=[
        {'instr':'Buka dokumen Word baru kosong di Word for the Web. Buka **Copilot pane**. Referensikan /POW_04_ST_MEMR_Compliance_Pack.docx dan /POW_05_Off_Taker_Negotiation_Brief.docx menggunakan `/`. Tempel prompt.',
         'prompt':'Tujuan: Susun paper Direksi 4 halaman "Pertahanan Pembaruan PPA, Transisi Batu Bara ke Energi Terbarukan & Negosiasi Off-Taker — Pack Direksi". Konteks: Direksi dalam 21 hari. Sumber: dua dokumen yang direferensikan + angka skenario PPA yang akan saya tempelkan. Ekspektasi: Bagian — (1) Ringkasan eksekutif 5 bullet; (2) Pertahanan pembaruan PPA dan skenario tarif; (3) Program remediasi ketersediaan pembangkit; (4) Re-prioritisasi capex transisi batu bara ke energi terbarukan; (5) Engagement regulator ST/MEMR/PLN; (6) Keputusan yang diminta. Nada: presisi, siap-Direksi, tanpa spekulasi. Kutip file sumber di akhir tiap bagian.'}
      ],
      persona=['Hadar Caspit'],
      personaID=['Hadar Caspit']),

      tool(T_PPT, M365_LIC, M365_ACCT, [
        {'instr':'Open a new PowerPoint deck in PowerPoint for the Web. Open the **Copilot pane**. Paste the prompt below.',
         'prompt':'Goal: 9-slide Board deck on PPA renewal + coal-to-renewables transition + grid LD claims. Context: Board in 21 days. Source: my Word brief and dashboard. Expectation: (1) Cover; (2) Situation — three converging pressures; (3) Stakeholder Map RAG (ST, MEMR, KeTSA, TNB, PLN, lenders, bondholders); (4) PPA Renewal Tariff Scenarios; (5) Plant Availability Remediation; (6) Coal-to-Renewables Capex Schedule; (7) EBITDA Bridge waterfall; (8) Off-Taker Negotiation Programme; (9) Decisions Requested. Brand colours #FACC15 + #CA8A04, 18pt min body text, 1 chart per slide.'}
      ], DESC_PPT,
      promptsID=[
        {'instr':'Buka deck PowerPoint baru di PowerPoint for the Web. Buka **Copilot pane**. Tempel prompt.',
         'prompt':'Tujuan: Deck 9 slide Direksi tentang pembaruan PPA + transisi batu bara ke energi terbarukan + klaim LD grid. Konteks: Direksi dalam 21 hari. Sumber: brief Word dan dashboard saya. Ekspektasi: (1) Cover; (2) Situasi — tiga tekanan yang bertemu; (3) Peta Pemangku Kepentingan RAG (ST, MEMR, KeTSA, TNB, PLN, pemberi pinjaman, pemegang obligasi); (4) Skenario Tarif Pembaruan PPA; (5) Remediasi Ketersediaan Pembangkit; (6) Jadwal Capex Transisi Batu Bara ke Energi Terbarukan; (7) Waterfall Bridge EBITDA; (8) Program Negosiasi Off-Taker; (9) Keputusan yang Diminta. Warna brand #FACC15 + #CA8A04, font tubuh min 18pt, 1 chart per slide.'}
      ],
      persona=['Sasha Ouellet'],
      personaID=['Sasha Ouellet']),

      tool(T_OUTLOOK, M365_LIC, M365_ACCT, [
        {'instr':'Open Outlook on the Web. Open the email thread "PPA renewal + plant availability remediation — Group MD follow-up". Click the **Copilot icon**. Paste the prompt below.',
         'prompt':'Goal: Draft a single email to the Zava Power ExCo, the 5 plant General Managers, and the Treasury and Regulatory Affairs heads. Context: PPA renewal, coal-to-renewables transition and grid LD claims active. Source: the email thread above. Expectation: Subject line, 4 short paragraphs covering the situation, the 3 actions each plant GM must complete in 72 hours (availability remediation; LD-claim documentation; ST/MEMR briefing inputs), the off-taker engagement track, and the Board date. Tone: firm, supportive, accountable.'}
      ], DESC_OUTLOOK,
      promptsID=[
        {'instr':'Buka Outlook on the Web. Buka thread email "Pembaruan PPA + remediasi ketersediaan pembangkit — tindak lanjut Direktur Pelaksana Grup". Klik **ikon Copilot**. Tempel prompt.',
         'prompt':'Tujuan: Susun satu email ke ExCo Zava Power, 5 General Manager pembangkit, dan kepala Treasury dan Regulatory Affairs. Konteks: pembaruan PPA, transisi batu bara ke energi terbarukan dan klaim LD grid aktif. Sumber: thread email di atas. Ekspektasi: Baris subjek, 4 paragraf pendek mencakup situasi, 3 aksi per GM pembangkit dalam 72 jam (remediasi ketersediaan; dokumentasi klaim LD; input briefing ST/MEMR), jalur engagement off-taker, dan tanggal Direksi. Nada: tegas, suportif, akuntabel.'}
      ],
      persona=['Hadar Caspit'],
      personaID=['Hadar Caspit']),

      tool(T_TEAMS, M365_LIC, M365_ACCT, [
        {'instr':'**(1) In Teams**, open **Calendar** → click the past meeting **"PPA Renewal Strategy Workshop"**. On the Recap page, walk through **AI Notes**, **Custom summary** (Speaker template), and **Audio recap**. **(2) In Word for the Web**, open a new blank document and type the minutes template (Date · Decisions · Actions · Risks · Open Questions). **(3) Click the Copilot icon** in Word and paste the prompt below — Copilot in Word references the recap with `/`.',
         'prompt':'Create meeting minutes for the Teams meeting /PPA Renewal Strategy Workshop. Use the template on this page. Sections: (1) Date and Attendees; (2) Decisions Taken; (3) Action Items with Owner and Due Date; (4) Risks Raised; (5) Open Questions. Quote the Group CFO and Regulatory Affairs head verbatim where wording matters. Flag any decision linked to the coal-to-renewables 2030 deadline as Critical Path. Save as Minutes_PPA_Renewal_Workshop.docx.'}
      ], '',
      promptsID=[
        {'instr':'**(1) Di Teams**, buka **Calendar** → klik rapat lampau **"Workshop Strategi Pembaruan PPA"**. Pada halaman Recap, tampilkan **AI Notes**, **Custom summary** (template Speaker), dan **Audio recap**. **(2) Di Word for the Web**, buka dokumen baru kosong dan ketik template notulen (Tanggal · Keputusan · Action · Risiko · Pertanyaan Terbuka). **(3) Klik ikon Copilot** di Word dan tempel prompt — Copilot in Word mereferensikan recap dengan `/`.',
         'prompt':'Buat notulen rapat untuk rapat Teams /Workshop Strategi Pembaruan PPA. Gunakan template di halaman ini. Bagian: (1) Tanggal dan Peserta; (2) Keputusan; (3) Action dengan Pemilik dan Tenggat; (4) Risiko; (5) Pertanyaan Terbuka. Kutip Direktur Keuangan Grup dan kepala Regulatory Affairs secara harfiah jika redaksinya penting. Tandai keputusan terkait deadline transisi batu bara ke energi terbarukan 2030 sebagai Critical Path. Simpan sebagai Notulen_Workshop_Pembaruan_PPA.docx.'}
      ],
      persona=['Sasha Ouellet'],
      personaID=['Sasha Ouellet']),

      tool(T_NOTEBOOK, M365_LIC, M365_ACCT, [
        {'instr':'All sources are loaded in the notebook. The Instructions field is set. Type the prompt below in the notebook chat.',
         'prompt':'Synthesise across all sources to produce a 10-bullet Board narrative. Cover: PPA renewal tariff scenarios; plant availability remediation; coal-to-renewables capex schedule; LD claims status; ST/MEMR/PLN regulator engagement; off-taker negotiation envelope; financial impact bridge; lender and bondholder posture; risk register; decisions requested. Cite the source file (and tab/section) at the end of every bullet.'}
      ], DESC_NOTEBOOK,
      promptsID=[
        {'instr':'Semua sumber sudah dimuat di notebook. Field Instructions sudah diset. Ketik prompt di bawah pada chat notebook.',
         'prompt':'Sintesakan dari semua sumber untuk menghasilkan narasi Direksi 10-bullet. Cakup: skenario tarif pembaruan PPA; remediasi ketersediaan pembangkit; jadwal capex transisi batu bara ke energi terbarukan; status klaim LD; engagement regulator ST/MEMR/PLN; envelope negosiasi off-taker; bridge dampak finansial; postur pemberi pinjaman dan pemegang obligasi; register risiko; keputusan yang diminta. Kutip file sumber (dan tab/bagian) di akhir tiap bullet.'}
      ],
      persona=['Mod Admin'],
      personaID=['Mod Admin'],
      notebookMeta={
        'sources':['/POW_01_PPA_Renewal_Model.xlsx','/POW_02_Plant_Availability_Tracker.xlsx','/POW_03_Coal_to_Renewables_Capex.xlsx'],
        'instructions':'You are the Group MD of Zava Power preparing a Board pack on converging PPA renewal, coal-to-renewables 2030 transition and grid-availability LD claims. Always cite the source file and tab/section. Tone: precise, Board-ready, no speculation about ST or MEMR intentions beyond what they have communicated in writing. Use MYR for Group totals (1 MYR ≈ 3,580 IDR). Reference real ASEAN peers (TNB, YTL Power, Petronas Gas, MFCB, Cypark, Indonesia Power, PLN Nusantara Power, Cikarang Listrindo, Adaro Power, Medco Power) where benchmark precedent strengthens the argument.',
        'instructionsID':'Anda adalah Direktur Pelaksana Grup Zava Power yang menyiapkan paket Direksi tentang konvergensi pembaruan PPA, transisi batu bara ke energi terbarukan 2030 dan klaim LD ketersediaan grid. Selalu kutip file sumber dan tab/bagian. Nada: presisi, siap-Direksi, tanpa spekulasi tentang niat ST atau MEMR di luar yang sudah disampaikan tertulis. Gunakan RM untuk total Grup (1 RM ≈ 3.580 Rp). Referensikan peer ASEAN riil (TNB, YTL Power, Petronas Gas, MFCB, Cypark, Indonesia Power, PLN Nusantara Power, Cikarang Listrindo, Adaro Power, Medco Power) bila preseden benchmark memperkuat argumen.'
      }),

      tool(T_COWORK, FRONTIER_LIC, M365_ACCT, [
        {'instr':'Open `m365.cloud.microsoft` > left nav > **Agents** > **Cowork**. Paste the single prompt below — Cowork delegates 5 parallel sub-tasks. Frontier required.',
         'prompt':'Cowork — PPA Renewal 21-Day Sprint. Run these in parallel: (1) 📝 Draft Word — PPA Renewal Defence Brief 4 pages, sources /POW_01_PPA_Renewal_Model.xlsx and /POW_05_Off_Taker_Negotiation_Brief.docx. (2) 📝 Draft Word — ST/MEMR Compliance Talking Points 2 pages, source /POW_04_ST_MEMR_Compliance_Pack.docx. (3) ✉️ Send email to Zava Power ExCo, the 5 plant GMs and Regulatory Affairs head with 3 actions in 72 hours. (4) 📅 Schedule 90-min Board Pre-Read tomorrow 8am MYT titled "PPA Renewal & 2030 Transition Alignment". (5) 💬 Post Teams message to #zava-power-exco with one-line headline + dashboard link.'}
      ], DESC_COWORK,
      promptsID=[
        {'instr':'Buka `m365.cloud.microsoft` > nav kiri > **Agents** > **Cowork**. Tempel prompt tunggal — Cowork mendelegasikan 5 sub-tugas paralel. Frontier diperlukan.',
         'prompt':'Cowork — Sprint 21 Hari Pembaruan PPA. Jalankan paralel: (1) 📝 Susun Word — Brief Pertahanan Pembaruan PPA 4 halaman, sumber /POW_01_PPA_Renewal_Model.xlsx dan /POW_05_Off_Taker_Negotiation_Brief.docx. (2) 📝 Susun Word — Talking Points Kepatuhan ST/MEMR 2 halaman, sumber /POW_04_ST_MEMR_Compliance_Pack.docx. (3) ✉️ Kirim email ke ExCo Zava Power, 5 GM pembangkit dan kepala Regulatory Affairs dengan 3 aksi dalam 72 jam. (4) 📅 Jadwalkan Pre-Read Direksi 90 menit besok 08:00 WIB berjudul "Penyelarasan Pembaruan PPA & Transisi 2030". (5) 💬 Posting pesan Teams di #zava-power-exco dengan headline satu baris + tautan dashboard.'}
      ],
      persona=['Mod Admin'],
      personaID=['Mod Admin']),

      tool(T_WORD_AGT, ANY_LIC, ANY_ACCT, [
        {'instr':'Open `m365.cloud.microsoft/chat` → Agents tab → **Word Agent**. Paste the prompt below — the agent returns a fully drafted .docx.',
         'prompt':'Goal: Generate a 4-page Group MD Crisis Brief in Word. Context: PPA renewal threatens MYR 240M EBITDA, coal-to-renewables 2030 deadline, grid LD claims MYR 38M YTD. Source: /POW_01_PPA_Renewal_Model.xlsx AND /POW_02_Plant_Availability_Tracker.xlsx. Expectation: Sections — Executive Summary 5 bullets; Current Status of all 3 workstreams; Programme; Financial Impact; Stakeholder Map (ST / MEMR / KeTSA / TNB / PLN / lenders / bondholders); Decisions Requested. Tone: precise, Board-ready. Save as Zava_Power_Crisis_Brief.docx.'}
      ], DESC_WORD_AGT,
      promptsID=[
        {'instr':'Buka `m365.cloud.microsoft/chat` → tab Agents → **Word Agent**. Tempel prompt — agent mengembalikan .docx yang sudah didraf penuh.',
         'prompt':'Tujuan: Hasilkan Brief Krisis Direktur Pelaksana Grup 4 halaman dalam Word. Konteks: pembaruan PPA mengancam EBITDA Rp 859 miliar, deadline transisi batu bara ke energi terbarukan 2030, klaim LD grid Rp 136 miliar YTD. Sumber: /POW_01_PPA_Renewal_Model.xlsx DAN /POW_02_Plant_Availability_Tracker.xlsx. Ekspektasi: Bagian — Ringkasan Eksekutif 5 bullet; Status Saat Ini ketiga workstream; Program; Dampak Finansial; Peta Pemangku Kepentingan (ST / MEMR / KeTSA / TNB / PLN / pemberi pinjaman / pemegang obligasi); Keputusan yang Diminta. Nada: presisi, siap-Direksi. Simpan sebagai Brief_Krisis_Zava_Power.docx.'}
      ],
      persona=['Sasha Ouellet'],
      personaID=['Sasha Ouellet']),

      tool(T_PPT_AGT, ANY_LIC, ANY_ACCT, [
        {'instr':'Open `m365.cloud.microsoft/chat` → Agents tab → **PowerPoint Agent**. Paste the prompt below.',
         'prompt':'Goal: 9-slide Board deck on PPA renewal + coal-to-renewables transition + grid LD claims. Context: Board in 21 days. Source: /Zava_Power_Crisis_Brief.docx and /POW_01_PPA_Renewal_Model.xlsx. Expectation: Cover; Situation; Stakeholder Map RAG; PPA Tariff Scenarios; Plant Availability Remediation; Coal-to-Renewables Capex; EBITDA Bridge; Off-Taker Negotiation; Decisions. Brand #FACC15 + #CA8A04, 18pt min body, 1 chart/slide. Save as Zava_Power_Board_Deck.pptx.'}
      ], DESC_PPT_AGT,
      promptsID=[
        {'instr':'Buka `m365.cloud.microsoft/chat` → tab Agents → **PowerPoint Agent**. Tempel prompt.',
         'prompt':'Tujuan: Deck 9 slide Direksi tentang pembaruan PPA + transisi batu bara ke energi terbarukan + klaim LD grid. Konteks: Direksi dalam 21 hari. Sumber: /Brief_Krisis_Zava_Power.docx dan /POW_01_PPA_Renewal_Model.xlsx. Ekspektasi: Cover; Situasi; Peta Pemangku Kepentingan RAG; Skenario Tarif PPA; Remediasi Ketersediaan Pembangkit; Capex Transisi Batu Bara ke Energi Terbarukan; Bridge EBITDA; Negosiasi Off-Taker; Keputusan. Brand #FACC15 + #CA8A04, font tubuh min 18pt, 1 chart/slide. Simpan sebagai Deck_Direksi_Zava_Power.pptx.'}
      ],
      persona=['Sasha Ouellet'],
      personaID=['Sasha Ouellet']),

      tool(T_XL_AGT, ANY_LIC, ANY_ACCT, [
        {'instr':'Open `m365.cloud.microsoft/chat` → Agents tab → **Excel Agent**. Paste the prompt below.',
         'prompt':'Goal: Build a PPA renewal + plant availability + capex schedule tracker workbook. Context: operating tracker for the Group COO. Source: schema only. Expectation: Sheet 1 PPA Tariff Scenarios (Base / Stretch / Regulator-aligned); Sheet 2 Plant Availability Watchlist (5 plants with LD exposure); Sheet 3 Coal-to-Renewables Capex Schedule; Sheet 4 Dashboard with KPI tiles + RAG conditional formatting. Save as Zava_Power_Operations_Tracker.xlsx.'}
      ], DESC_XL_AGT,
      promptsID=[
        {'instr':'Buka `m365.cloud.microsoft/chat` → tab Agents → **Excel Agent**. Tempel prompt.',
         'prompt':'Tujuan: Bangun workbook tracker pembaruan PPA + ketersediaan pembangkit + jadwal capex. Konteks: tracker operasi untuk Direktur Operasional Grup. Sumber: hanya skema. Ekspektasi: Sheet 1 Skenario Tarif PPA (Base / Stretch / Selaras-Regulator); Sheet 2 Watchlist Ketersediaan Pembangkit (5 pembangkit dengan eksposur LD); Sheet 3 Jadwal Capex Transisi Batu Bara ke Energi Terbarukan; Sheet 4 Dashboard dengan KPI tile + format kondisional RAG. Simpan sebagai Tracker_Operasi_Zava_Power.xlsx.'}
      ],
      persona=['Hadar Caspit'],
      personaID=['Hadar Caspit']),

      tool(T_BUILDER, ANY_LIC, ANY_ACCT, [
        {'instr':'Open `m365.cloud.microsoft/chat` > Agents > **+ Create an agent**. Pick ONE of the 3 agents below. Paste the chosen description into the **Describe** field.',
         'prompt':'**Option A — Zava Power PPA Renewal Watch.** Build an agent for the Group CFO and Regulatory Affairs head to track PPA renewal scenarios daily. Ground every answer on /POW_01_PPA_Renewal_Model.xlsx and the off-taker correspondence. Always cite file and tab. Classify each scenario as Defendable / Watch / At Risk. Tone: precise, regulator-grade. Starter prompts: (1) What is the latest tariff sensitivity; (2) Which assumptions are most fragile; (3) Build a weekly PPA dashboard; (4) Draft the off-taker counter-proposal; (5) Summarise for the Board.'},
        {'instr':'**Option B — alternative agent.** Same Create-an-agent flow with a different specialisation.',
         'prompt':'**Option B — Zava Power Plant Availability Agent.** Build an agent for the COO and the 5 plant General Managers to manage availability remediation and LD-claim documentation. Ground every answer on /POW_02_Plant_Availability_Tracker.xlsx. Always cite section. Classify each event as Closed / In Progress / Awaiting Internal Sign-Off. Tone: factual, ops-grade. Starter prompts: (1) What plants are below 92% availability; (2) Draft an LD-claim narrative; (3) What are the next 3 remediation milestones; (4) Build a weekly availability dashboard; (5) Summarise for the COO.'},
        {'instr':'**Option C — alternative agent.** Same flow.',
         'prompt':'**Option C — Zava Power Coal-to-Renewables Agent.** Build an agent for the Strategy and Capex Programme teams to track the 2030 transition pipeline. Ground every answer on /POW_03_Coal_to_Renewables_Capex.xlsx. Always cite file and section. Classify each project as On-Track / Watch / Slipping. Tone: factual, capex-grade. Starter prompts: (1) Which BESS / solar / wind projects are slipping; (2) Draft an EPC partner status memo; (3) Build a monthly transition dashboard; (4) What is the FY2027 capex envelope; (5) Summarise for the Board.'},
        {'instr':'**Test.** After the agent is created, click into it and use the right test pane to validate grounding, citations, scope.',
         'prompt':'Give me the 60-second version of the PPA renewal + coal-to-renewables 2030 + grid LD claims situation, the worst 3 issues, the response programme, and the decisions I must take to the Board in 21 days. Cite the file and tab/section for every paragraph.'},
        {'instr':'**Share.** Click the agent → **Share** → add recipients with **Use** access.',
         'prompt':'Share with the Zava Power ExCo (Group MD, Group CFO, COO, Regulatory Affairs head, Treasury head, the 5 plant GMs) — Use access. Send notification: "This agent is now in your M365 Copilot chat — ground every PPA / availability / coal-to-renewables question through it for the next 90 days."'}
      ], DESC_BUILDER,
      promptsID=[
        {'instr':'Buka `m365.cloud.microsoft/chat` > Agents > **+ Create an agent**. Pilih SATU dari 3 agent. Tempel deskripsi ke field **Describe**.',
         'prompt':'**Opsi A — Zava Power PPA Renewal Watch.** Bangun agent untuk Direktur Keuangan Grup dan kepala Regulatory Affairs untuk melacak skenario pembaruan PPA harian. Dasarkan pada /POW_01_PPA_Renewal_Model.xlsx dan korespondensi off-taker. Selalu kutip file dan tab. Klasifikasikan tiap skenario sebagai Defendable / Watch / At Risk. Nada: presisi, regulator-grade. Starter prompt: (1) Sensitivitas tarif terbaru; (2) Asumsi mana paling rapuh; (3) Bangun dashboard PPA mingguan; (4) Susun counter-proposal off-taker; (5) Rangkum untuk Direksi.'},
        {'instr':'**Opsi B — agent alternatif.** Alur Create-an-agent sama dengan spesialisasi berbeda.',
         'prompt':'**Opsi B — Zava Power Plant Availability Agent.** Bangun agent untuk COO dan 5 General Manager pembangkit untuk mengelola remediasi ketersediaan dan dokumentasi klaim LD. Dasarkan pada /POW_02_Plant_Availability_Tracker.xlsx. Selalu kutip bagian. Klasifikasikan tiap kejadian sebagai Closed / In Progress / Awaiting Internal Sign-Off. Nada: faktual, ops-grade. Starter prompt: (1) Pembangkit mana di bawah 92% ketersediaan; (2) Susun naratif klaim LD; (3) 3 milestone remediasi berikutnya; (4) Bangun dashboard ketersediaan mingguan; (5) Rangkum untuk COO.'},
        {'instr':'**Opsi C — agent alternatif.** Alur sama.',
         'prompt':'**Opsi C — Zava Power Coal-to-Renewables Agent.** Bangun agent untuk tim Strategi dan Program Capex untuk melacak pipeline transisi 2030. Dasarkan pada /POW_03_Coal_to_Renewables_Capex.xlsx. Selalu kutip file dan bagian. Klasifikasikan tiap proyek sebagai On-Track / Watch / Slipping. Nada: faktual, capex-grade. Starter prompt: (1) Proyek BESS / surya / angin mana yang slip; (2) Susun memo status mitra EPC; (3) Bangun dashboard transisi bulanan; (4) Envelope capex FY2027; (5) Rangkum untuk Direksi.'},
        {'instr':'**Uji.** Validasi grounding, kutipan, cakupan.',
         'prompt':'Berikan versi 60 detik dari pembaruan PPA + transisi batu bara ke energi terbarukan 2030 + klaim LD grid, 3 isu terburuk, program respons, dan keputusan yang harus saya bawa ke Direksi dalam 21 hari. Kutip file dan tab/bagian untuk tiap paragraf.'},
        {'instr':'**Bagikan.** Klik agent → **Share** → tambahkan penerima dengan akses **Use**.',
         'prompt':'Bagikan ke ExCo Zava Power (Direktur Pelaksana Grup, Direktur Keuangan Grup, COO, kepala Regulatory Affairs, kepala Treasury, 5 GM pembangkit) — akses Use. Kirim notifikasi: "Agent ini sekarang ada di M365 Copilot chat Anda — dasarkan tiap pertanyaan PPA / ketersediaan / transisi batu bara ke energi terbarukan melalui agent ini selama 90 hari ke depan."'}
      ],
      persona=['Mod Admin','Mod Admin','Mod Admin','Sasha Ouellet','Sasha Ouellet'],
      personaID=['Mod Admin','Mod Admin','Mod Admin','Sasha Ouellet','Sasha Ouellet']),
    ],
    companyID='Zava Power',
    taglineID='Pembaruan PPA pada tarif lebih rendah mengancam EBITDA Rp 859 miliar + deadline transisi batu bara ke energi terbarukan 2030 + LD ketersediaan grid — Direksi dalam 21 hari.',
    scenarioID="Zava Power adalah produsen listrik independen ASEAN dengan portfolio gross 4,2 GW di pembangkit batu bara, combined-cycle gas, surya skala besar, hidro dan angin on-grid di Malaysia dan Indonesia. Grup beroperasi di bawah PPA jangka panjang dengan TNB (Malaysia) dan PLN Nusantara Power (Indonesia) sebagai off-taker utama. Tiga tekanan bertemu: (1) PPA pembangkit batu bara terbesar (1.200 MW) jatuh tempo pembaruan dalam 14 bulan pada struktur tarif yang, di bawah framework levelised cost yang diimposisi regulator, mengancam EBITDA FY2027 sebesar Rp 859 miliar (RM 240 juta); (2) Energy Commission Malaysia (Suruhanjaya Tenaga / ST) telah mengkodifikasi deadline transisi batu bara ke energi terbarukan pada 2030, menuntut re-prioritisasi capex Rp 7,5 triliun (RM 2,1 miliar) lintas pipeline BESS, surya skala besar dan angin on-grid; (3) dua kejadian ketersediaan grid di pembangkit Pasir Gudang dan Cilegon memicu klaim liquidated damages dari off-taker total Rp 136 miliar YTD dengan tambahan Rp 79 miliar kontinjen. Direktur Pelaksana Grup butuh paket Direksi dalam 21 hari mencakup model pembaruan PPA, program remediasi ketersediaan pembangkit, jadwal capex transisi batu bara ke energi terbarukan, paket regulator ST/MEMR/PLN, dan brief negosiasi off-taker. Frame customer riil: grup ini beroperasi serupa dengan **TNB**, **YTL Power International**, **Petronas Gas**, **Mega First Corp (MFCB)**, **Cypark Resources**, **Indonesia Power**, **PLN Nusantara Power**, **Cikarang Listrindo**, **Adaro Power**, dan **Medco Power** — dengan regulator termasuk **Energy Commission Malaysia (ST)**, **MEMR (Kementerian ESDM)**, **PLN** (off-taker), dan **KeTSA** aktif bersamaan.",
    relevantDepts=['dept-finance','dept-strategy','dept-operations','dept-risk','dept-legal','dept-procurement'],
    personas=[
      {'name':'Sasha Ouellet','role':'Group MD - Power Generation','roleID':'Direktur Utama - Pembangkit Listrik','acct':FREE_ACCT,'lic':FREE_LIC,'color':'#FACC15'},
      {'name':'Mod Admin','role':'Group Strategy & Capex Director','roleID':'Direktur Strategi & Capex Grup','acct':M365_ACCT,'lic':M365_LIC,'color':'#059669'},
      {'name':'Hadar Caspit','role':'Group CFO','roleID':'Direktur Keuangan Grup','acct':M365_ACCT,'lic':M365_LIC,'color':'#1E40AF'},
      {'name':'Daichi Kimura','role':'Regulatory Affairs & Off-Taker Director','roleID':'Direktur Regulatory Affairs & Off-Taker','acct':M365_ACCT,'lic':M365_LIC,'color':'#DC2626'}
    ],
    storyboard=[
      {'ex':1,'title':'Research & Brief','titleID':'Riset & Pengarahan','minutes':18,'mode':'Show & Tell + Hands-on',
       'summary':'Frame the PPA renewal + 2030 transition + LD claims situation and pull peer playbooks before the regulator clock starts ticking.',
       'summaryID':'Bingkai situasi pembaruan PPA + transisi 2030 + klaim LD dan tarik playbook peer sebelum clock regulator berdetak.',
       'tasks':[
         {'verb':'Frame the morning question and lock the day priorities','verbID':'Susun pertanyaan pagi dan kunci prioritas hari ini','toolId':T_CHAT,'mode':'Show & Tell'},
         {'verb':'Run an outside-in peer scan and pull proven plays','verbID':'Lakukan pemindaian peer dari luar dan tarik praktik terbaik','toolId':T_RESEARCHER,'mode':'Show & Tell'},
         {'verb':'Generate a board-ready brief straight from chat','verbID':'Hasilkan brief siap-Direksi langsung dari chat','toolId':T_WORD_AGT,'mode':'Hands-on'}]},
      {'ex':2,'title':'Analyse & Decide','titleID':'Analisis & Putuskan','minutes':18,'mode':'Hands-on',
       'summary':'Quantify the PPA + availability + capex combined impact; build a Board dashboard.',
       'summaryID':'Kuantifikasi dampak gabungan PPA + ketersediaan + capex; bangun dashboard Direksi.',
       'tasks':[
         {'verb':'Crunch the numbers and surface the biggest gaps','verbID':'Olah angka dan ungkap celah terbesar','toolId':T_ANALYST,'mode':'Hands-on'},
         {'verb':'Build a single-pane operating dashboard','verbID':'Bangun dashboard operasi satu-halaman','toolId':T_EXCEL,'mode':'Hands-on'},
         {'verb':'Spin up a recurring tracker workbook from chat','verbID':'Buat workbook tracker berulang dari chat','toolId':T_XL_AGT,'mode':'Hands-on'}]},
      {'ex':3,'title':'Communicate & Coordinate','titleID':'Komunikasi & Koordinasi','minutes':18,'mode':'Hands-on',
       'summary':'Brief plant GMs and Regulatory Affairs, capture the PPA workshop recap, and assemble the Board deck.',
       'summaryID':'Brief GM pembangkit dan Regulatory Affairs, capture recap workshop PPA, dan rakit deck Direksi.',
       'tasks':[
         {'verb':'Draft the stakeholder alignment email','verbID':'Draf email penyelarasan stakeholder','toolId':T_OUTLOOK,'mode':'Hands-on'},
         {'verb':'Recap the meeting and turn it into minutes','verbID':'Recap rapat dan ubah ke notulen','toolId':T_TEAMS,'mode':'Hands-on'},
         {'verb':'Generate a board-ready deck from chat','verbID':'Hasilkan deck siap-Direksi dari chat','toolId':T_PPT_AGT,'mode':'Hands-on'},
         {'verb':'Delegate a 5-task parallel sprint','verbID':'Delegasikan 5-tugas paralel ke Cowork','toolId':T_COWORK,'mode':'Show & Tell'}]},
      {'ex':4,'title':'Build & Scale','titleID':'Bangun & Skala','minutes':15,'mode':'Show & Tell',
       'summary':'Wrap the PPA + availability + capex playbook into a reusable agent for the Zava Power operating team.',
       'summaryID':'Bungkus playbook PPA + ketersediaan + capex ke dalam agent reusable untuk tim operasi Zava Power.',
       'tasks':[
         {'verb':'Pull every source into one synthesis notebook','verbID':'Tarik semua sumber ke satu notebook sintesis','toolId':T_NOTEBOOK,'mode':'Show & Tell'},
         {'verb':'Wrap the daily workflow into a reusable agent','verbID':'Bungkus alur kerja harian jadi agen yang dapat dipakai ulang','toolId':T_BUILDER,'mode':'Show & Tell'}]}
    ],
    geo='MY+ID'
))

# INDUSTRIES_12.append(... power-utilities ...)

# ╔══════════════════════════════════════════════════════════════════════╗
# ║  4.  PROPERTY DEVELOPMENT  (Zava Property)                           ║
# ╚══════════════════════════════════════════════════════════════════════╝
INDUSTRIES_12.append(ind(
    'property-development', 'sec-re', 'Property Development', '🏗️', '#A16207', '#854D0E',
    'Zava Property',
    'MYR 1.4B unsold inventory + Bumi-quota conversion overdue at 5 townships + MTN bond redemption test in 18 months — Board in 14 days.',
    "Zava Property is an ASEAN-listed property developer with residential, integrated-township and industrial-park operations across Malaysia (Klang Valley, Iskandar Johor, Penang) and Indonesia (Greater Jakarta, Bandung, Surabaya). The group has 18,400 active build-out units across 14 active townships and 4 industrial parks. Three pressures converge: (1) MYR 1.4B of unsold completed inventory has accumulated over 24 months, generating MYR 280M of annual holding cost (interest + assessment + utilities + property tax); (2) the Bumi-quota conversion programme (Bumiputera reserved units that have not been taken up) is overdue at 5 townships — the State Authority approval window for conversion under KPKT guidelines closes in 90 days for 3 of those townships; (3) the MYR 1.8B MTN bond redemption test falls in 18 months and credit-watch agencies have downgraded the outlook on the back of the inventory drag and a slowing primary launch take-up rate. The Group MD needs a Board pack in 14 days covering the unsold inventory tracker, township P&L model, Bumi-quota conversion brief, bond redemption stress test, and the FY2026 launch cadence playbook. Real customer reference frame: this group operates similarly to **Sime Darby Property**, **Mah Sing Group**, **Eco World Development**, **IOI Properties**, **Sunway Property**, **S P Setia**, **Sinar Mas Land**, **Lippo Karawaci**, **Ciputra Development**, **Pakuwon Jati**, **Summarecon Agung**, and **Agung Podomoro Land** — with regulators including **REHDA**, **KPKT** (Kementerian Perumahan & Kerajaan Tempatan), **BPN** (Indonesia Land Office), **Kementerian PUPR**, and **OJK** active concurrently.",
    ['PROP_01_Unsold_Inventory_Tracker.xlsx','PROP_02_Township_PnL_Model.xlsx','PROP_03_Bumi_Quota_Conversion_Brief.docx','PROP_04_Bond_Redemption_Stress_Test.xlsx','PROP_05_Launch_Cadence_FY2026_Playbook.docx'],
    [
      tool(T_CHAT, FREE_LIC, FREE_ACCT, [
        {'instr':'', 'prompt':'Goal: Frame the unsold inventory + Bumi-quota conversion + MTN bond redemption test situation in plain English for the Group MD. Context: Zava Property has MYR 1.4B unsold completed inventory, MYR 280M annual holding cost, Bumi-quota conversion overdue at 5 townships with 90-day window for 3 of them, and MTN bond redemption test in 18 months with credit-watch downgrade. Source: my notes from the morning Sales and Treasury call. Expectation: 1-page note with sections — Headline; What Happened; Stakeholder Position (KPKT, State Authority Bumi committee, REHDA, BPN, OJK, MTN trustee, the 4 lender consortium banks, primary buyers); Top 5 Questions the Board Will Ask; 3 Decisions the Group MD Must Take in 48 Hours. Tone: calm, precise, no property-sector jargon.'},
        {'instr':'', 'prompt':'Goal: Build the stakeholder communication map for the 3 converging pressures with Board in 14 days and Bumi conversion window closing in 90 days. Context: KPKT, State Authority Bumi committee, REHDA, BPN, Kementerian PUPR, OJK, MTN trustee, lender consortium, top 3 institutional investors, and the 14 township GMs. Source: known stakeholders. Expectation: RAG table — Red same-day, Amber 24-72h, Green monitor. Columns: Audience, Channel, Owner, Message Theme, Timing, Risk if Mishandled.'}
      ], DESC_CHAT,
      promptsID=[
        {'instr':'', 'prompt':'Tujuan: Bingkai situasi inventory belum terjual + konversi kuota Bumi + uji redemption obligasi MTN dalam bahasa sederhana untuk Direktur Pelaksana Grup. Konteks: Zava Property memiliki Rp 5,0 triliun (RM 1,4 miliar) inventory selesai belum terjual, biaya holding tahunan Rp 1,0 triliun (RM 280 juta), konversi kuota Bumi overdue di 5 township dengan jendela 90 hari untuk 3 di antaranya, dan uji redemption MTN dalam 18 bulan dengan downgrade credit-watch. Sumber: catatan saya dari rapat Sales dan Treasury pagi. Ekspektasi: nota 1 halaman dengan bagian — Headline; Apa yang Terjadi; Posisi Pemangku Kepentingan (KPKT, komite Bumi State Authority, REHDA, BPN, OJK, trustee MTN, konsorsium 4 bank pemberi pinjaman, pembeli primer); 5 Pertanyaan Top dari Direksi; 3 Keputusan Direktur Pelaksana Grup dalam 48 Jam. Nada: tenang, presisi, hindari jargon sektor properti.'},
        {'instr':'', 'prompt':'Tujuan: Bangun peta komunikasi pemangku kepentingan untuk 3 tekanan yang bertemu dengan Direksi 14 hari dan jendela konversi Bumi tutup dalam 90 hari. Konteks: KPKT, komite Bumi State Authority, REHDA, BPN, Kementerian PUPR, OJK, trustee MTN, konsorsium pemberi pinjaman, 3 investor institusional teratas, dan 14 GM township. Sumber: pemangku kepentingan yang dikenal. Ekspektasi: tabel RAG — Merah hari ini juga, Kuning 24-72 jam, Hijau pantau. Kolom: Audiens, Channel, Pemilik, Tema Pesan, Timing, Risiko bila Keliru.'}
      ],
      persona=['Sasha Ouellet','Hadar Caspit'],
      personaID=['Sasha Ouellet','Hadar Caspit']),

      tool(T_RESEARCHER, M365_LIC, M365_ACCT, [
        {'instr':'Open `m365.cloud.microsoft/chat` > Agents > **Researcher** > **Critique Mode**. Paste the prompt below.',
         'prompt':'Goal: Benchmark how ASEAN listed property developers handled simultaneous unsold-inventory drag, Bumi/State land-quota conversion programmes and MTN-bond-redemption stress between 2019 and 2025. Context: Zava Property must respond to KPKT, State Authority Bumi committee, MTN trustee and credit-watch agencies on parallel tracks. Source: peer disclosures (Bursa Malaysia / IDX), REHDA quarterly briefings, KPKT registers, BPN announcements. Real peers: Sime Darby Property, Mah Sing, Eco World, IOI Properties, Sunway Property, S P Setia, Sinar Mas Land, Lippo Karawaci, Ciputra Development, Pakuwon Jati, Summarecon Agung, Agung Podomoro. Expectation: For each peer, identify trigger event, response timeline, programme adopted (inventory disposal, launch deferral, Bumi-quota conversion, refinancing), and outcome 12-24 months later (inventory days, take-up rate, credit rating). Critique each source. Cite all with publication date. Output as a comparison table.'},
        {'instr':'Open `m365.cloud.microsoft/chat` > Agents > **Researcher** > **Model Council**. Paste the prompt below.',
         'prompt':'Goal: 3 most defensible response playbooks for an ASEAN listed property developer hit simultaneously by inventory drag + Bumi conversion deadline + MTN bond redemption stress. Context: Zava Property must protect KPKT and State Authority confidence, MTN trustee and lender ratings, and primary-buyer trust concurrently. Source: Researcher Model Council — convene parallel reports from GPT-5.5 Thinking and Claude Opus 4.7. Expectation: Surface dissent across the council, mark majority and minority views. Comparison table: Playbook, Council Verdict, Dissenting View, ASEAN Precedent (cite specific peer year), Implementation Risk.'}
      ], DESC_RESEARCHER,
      promptsID=[
        {'instr':'Buka `m365.cloud.microsoft/chat` > Agents > **Researcher** > **Critique Mode**. Tempel prompt.',
         'prompt':'Tujuan: Benchmark bagaimana developer properti tercatat ASEAN menangani drag inventory belum terjual, program konversi kuota tanah Bumi/State dan stres redemption obligasi MTN secara bersamaan antara 2019 hingga 2025. Konteks: Zava Property harus merespons KPKT, komite Bumi State Authority, trustee MTN dan agen credit-watch di jalur paralel. Sumber: pengungkapan peer (Bursa Malaysia / BEI), briefing kuartalan REHDA, register KPKT, pengumuman BPN. Peer riil: Sime Darby Property, Mah Sing, Eco World, IOI Properties, Sunway Property, S P Setia, Sinar Mas Land, Lippo Karawaci, Ciputra Development, Pakuwon Jati, Summarecon Agung, Agung Podomoro. Ekspektasi: Untuk tiap peer identifikasi peristiwa pemicu, timeline respons, program (disposal inventory, deferral peluncuran, konversi kuota Bumi, refinancing), dan hasil 12-24 bulan kemudian (hari inventory, take-up rate, rating kredit). Kritisi tiap sumber. Cantumkan kutipan lengkap dengan tanggal. Hasilkan tabel perbandingan.'},
        {'instr':'Buka `m365.cloud.microsoft/chat` > Agents > **Researcher** > **Model Council**. Tempel prompt.',
         'prompt':'Tujuan: 3 playbook respons paling defensible untuk developer properti tercatat ASEAN yang terkena drag inventory + deadline konversi Bumi + stres redemption obligasi MTN secara bersamaan. Konteks: Zava Property harus melindungi kepercayaan KPKT dan State Authority, rating trustee MTN dan pemberi pinjaman, serta kepercayaan pembeli primer sekaligus. Sumber: Model Council — gelar laporan paralel dari GPT-5.5 Thinking dan Claude Opus 4.7. Ekspektasi: Sorot perbedaan pendapat lintas council, tandai pandangan mayoritas dan minoritas. Tabel perbandingan: Playbook, Putusan Council, Pandangan Minoritas, Preseden ASEAN (kutip peer spesifik dengan tahun), Risiko Implementasi.'}
      ],
      persona=['Mod Admin','Mod Admin'],
      personaID=['Mod Admin','Mod Admin']),

      tool(T_ANALYST, M365_LIC, M365_ACCT, [
        {'instr':'Open `m365.cloud.microsoft/chat` > Agents > **Analyst**. Upload /PROP_01_Unsold_Inventory_Tracker.xlsx AND /PROP_04_Bond_Redemption_Stress_Test.xlsx. Paste the prompt below.',
         'prompt':'Goal: Quantify the combined impact of unsold inventory drag and the MTN bond redemption test on FY2027 cash flow and credit metrics. Context: Board needs an evidence-based view in 48 hours. Source: the 2 uploaded files — unsold inventory by township + ageing buckets; bond redemption stress test under base/stretch/downside scenarios. Expectation: (1) RAG bar chart of townships ranked by unsold-inventory holding cost; (2) waterfall of operating cash bridge — Baseline → Holding cost drag → Bumi-conversion cash unlock → Inventory disposal proceeds → Refinancing requirement → Net cash position; (3) sensitivity table on take-up rate (45% / 60% / 75% of launch) showing covenant headroom per scenario. Output a Board-ready RAG dashboard.'}
      ], DESC_ANALYST,
      promptsID=[
        {'instr':'Buka `m365.cloud.microsoft/chat` > Agents > **Analyst**. Unggah /PROP_01_Unsold_Inventory_Tracker.xlsx DAN /PROP_04_Bond_Redemption_Stress_Test.xlsx. Tempel prompt.',
         'prompt':'Tujuan: Kuantifikasi dampak gabungan drag inventory belum terjual dan uji redemption obligasi MTN terhadap arus kas FY2027 dan metrik kredit. Konteks: Direksi butuh pandangan berbasis bukti dalam 48 jam. Sumber: 2 file yang diunggah — inventory belum terjual per township + bucket ageing; uji stres redemption obligasi di bawah skenario base/stretch/downside. Ekspektasi: (1) Bar chart RAG township diurutkan berdasar biaya holding inventory belum terjual; (2) waterfall bridge kas operasi — Baseline → drag biaya holding → unlock kas konversi Bumi → proceed disposal inventory → kebutuhan refinancing → posisi kas neto; (3) tabel sensitivitas take-up rate (45% / 60% / 75% peluncuran) menampilkan headroom covenant per skenario. Hasilkan dashboard RAG siap-Direksi.'}
      ],
      persona=['Hadar Caspit'],
      personaID=['Hadar Caspit']),

      tool(T_EXCEL, M365_LIC, M365_ACCT, [
        {'instr':'Open `/PROP_02_Township_PnL_Model.xlsx` in Excel for the Web. Open the **Copilot pane**. Paste the prompt below.',
         'prompt':'Goal: Build a single Board-ready dashboard sheet combining township P&L, unsold inventory ageing and Bumi-quota conversion status. Context: Board meets in 14 days. Source: combine all relevant tabs — Township PnL, Unsold Ageing, Bumi Quota Status, Launch Cadence. Expectation: New sheet "Board Dashboard" with KPI tiles for Unsold Inventory MYR M, Annual Holding Cost MYR M, Townships with Bumi Conversion Overdue, Covenant Headroom; horizontal bar of townships ranked worst to best on EBITDA; line chart of unsold ageing trajectory; RAG conditional formatting; sparkline column. Do not modify source tabs.'}
      ], '',
      promptsID=[
        {'instr':'Buka `/PROP_02_Township_PnL_Model.xlsx` di Excel for the Web. Buka **Copilot pane**. Tempel prompt.',
         'prompt':'Tujuan: Bangun satu sheet dashboard siap-Direksi yang menggabungkan P&L township, ageing inventory belum terjual dan status konversi kuota Bumi. Konteks: Direksi bertemu 14 hari. Sumber: gabungkan tab Township PnL, Unsold Ageing, Bumi Quota Status, Launch Cadence. Ekspektasi: Sheet baru "Dashboard Direksi" dengan KPI tile untuk Inventory Belum Terjual Rp Miliar, Biaya Holding Tahunan Rp Miliar, Township dengan Konversi Bumi Overdue, Headroom Covenant; bar horizontal township diurutkan terburuk ke terbaik berdasar EBITDA; line chart trajectory ageing belum terjual; format kondisional RAG; kolom sparkline. Jangan modifikasi tab sumber.'}
      ],
      persona=['Hadar Caspit'],
      personaID=['Hadar Caspit']),

      tool(T_WORD, M365_LIC, M365_ACCT, [
        {'instr':'Open a new blank Word doc in Word for the Web. Open the **Copilot pane**. Reference /PROP_03_Bumi_Quota_Conversion_Brief.docx and /PROP_05_Launch_Cadence_FY2026_Playbook.docx using `/`. Paste the prompt below.',
         'prompt':'Goal: Draft the 4-page Board paper "Unsold Inventory Action, Bumi Conversion & MTN Bond Strategy — Board Pack". Context: Board in 14 days. Source: the two referenced docs + the inventory and bond stress numbers I will paste. Expectation: Sections — (1) Executive summary in 5 bullets; (2) Unsold inventory disposal programme; (3) Bumi-quota conversion path with the 90-day window for 3 townships; (4) MTN bond redemption strategy and refinancing options; (5) FY2026 launch cadence proposal; (6) Decisions requested. Tone: precise, Board-ready, no speculation. Cite source files at the end of every section.'}
      ], DESC_WORD,
      promptsID=[
        {'instr':'Buka dokumen Word baru kosong di Word for the Web. Buka **Copilot pane**. Referensikan /PROP_03_Bumi_Quota_Conversion_Brief.docx dan /PROP_05_Launch_Cadence_FY2026_Playbook.docx menggunakan `/`. Tempel prompt.',
         'prompt':'Tujuan: Susun paper Direksi 4 halaman "Aksi Inventory Belum Terjual, Konversi Bumi & Strategi Obligasi MTN — Pack Direksi". Konteks: Direksi dalam 14 hari. Sumber: dua dokumen yang direferensikan + angka inventory dan stres obligasi yang akan saya tempelkan. Ekspektasi: Bagian — (1) Ringkasan eksekutif 5 bullet; (2) Program disposal inventory belum terjual; (3) Jalur konversi kuota Bumi dengan jendela 90 hari untuk 3 township; (4) Strategi redemption obligasi MTN dan opsi refinancing; (5) Usulan cadence peluncuran FY2026; (6) Keputusan yang diminta. Nada: presisi, siap-Direksi, tanpa spekulasi. Kutip file sumber di akhir tiap bagian.'}
      ],
      persona=['Hadar Caspit'],
      personaID=['Hadar Caspit']),

      tool(T_PPT, M365_LIC, M365_ACCT, [
        {'instr':'Open a new PowerPoint deck in PowerPoint for the Web. Open the **Copilot pane**. Paste the prompt below.',
         'prompt':'Goal: 9-slide Board deck on unsold inventory + Bumi-quota conversion + MTN bond redemption. Context: Board in 14 days. Source: my Word brief and dashboard. Expectation: (1) Cover; (2) Situation — three converging pressures; (3) Stakeholder Map RAG (KPKT, State Authority, REHDA, BPN, OJK, MTN trustee, lenders); (4) Unsold Inventory Disposal Programme; (5) Bumi-Quota Conversion Plan; (6) MTN Bond Redemption Strategy; (7) Operating Cash Bridge waterfall; (8) FY2026 Launch Cadence; (9) Decisions Requested. Brand colours #A16207 + #854D0E, 18pt min body text, 1 chart per slide.'}
      ], DESC_PPT,
      promptsID=[
        {'instr':'Buka deck PowerPoint baru di PowerPoint for the Web. Buka **Copilot pane**. Tempel prompt.',
         'prompt':'Tujuan: Deck 9 slide Direksi tentang inventory belum terjual + konversi kuota Bumi + redemption obligasi MTN. Konteks: Direksi dalam 14 hari. Sumber: brief Word dan dashboard saya. Ekspektasi: (1) Cover; (2) Situasi — tiga tekanan yang bertemu; (3) Peta Pemangku Kepentingan RAG (KPKT, State Authority, REHDA, BPN, OJK, trustee MTN, pemberi pinjaman); (4) Program Disposal Inventory Belum Terjual; (5) Rencana Konversi Kuota Bumi; (6) Strategi Redemption Obligasi MTN; (7) Waterfall Bridge Kas Operasi; (8) Cadence Peluncuran FY2026; (9) Keputusan yang Diminta. Warna brand #A16207 + #854D0E, font tubuh min 18pt, 1 chart per slide.'}
      ],
      persona=['Sasha Ouellet'],
      personaID=['Sasha Ouellet']),

      tool(T_OUTLOOK, M365_LIC, M365_ACCT, [
        {'instr':'Open Outlook on the Web. Open the email thread "Unsold inventory + Bumi conversion + MTN bond — Group MD follow-up". Click the **Copilot icon**. Paste the prompt below.',
         'prompt':'Goal: Draft a single email to the Zava Property ExCo, the 14 township GMs and the Treasury and Legal heads. Context: unsold inventory, Bumi conversion deadline and MTN bond redemption stress active. Source: the email thread above. Expectation: Subject line, 4 short paragraphs covering the situation, the 3 actions each township GM and Treasury head must complete in 72 hours (inventory disposal proposal; Bumi conversion submission; refinancing options pre-read), the regulator engagement track, and the Board date. Tone: firm, supportive, accountable.'}
      ], DESC_OUTLOOK,
      promptsID=[
        {'instr':'Buka Outlook on the Web. Buka thread email "Inventory belum terjual + konversi Bumi + obligasi MTN — tindak lanjut Direktur Pelaksana Grup". Klik **ikon Copilot**. Tempel prompt.',
         'prompt':'Tujuan: Susun satu email ke ExCo Zava Property, 14 GM township dan kepala Treasury dan Legal. Konteks: inventory belum terjual, deadline konversi Bumi dan stres redemption obligasi MTN aktif. Sumber: thread email di atas. Ekspektasi: Baris subjek, 4 paragraf pendek mencakup situasi, 3 aksi per GM township dan kepala Treasury dalam 72 jam (usulan disposal inventory; submission konversi Bumi; pre-read opsi refinancing), jalur engagement regulator, dan tanggal Direksi. Nada: tegas, suportif, akuntabel.'}
      ],
      persona=['Hadar Caspit'],
      personaID=['Hadar Caspit']),

      tool(T_TEAMS, M365_LIC, M365_ACCT, [
        {'instr':'**(1) In Teams**, open **Calendar** → click the past meeting **"Unsold Inventory Disposal Workshop"**. On the Recap page, walk through **AI Notes**, **Custom summary** (Speaker template), and **Audio recap**. **(2) In Word for the Web**, open a new blank document and type the minutes template (Date · Decisions · Actions · Risks · Open Questions). **(3) Click the Copilot icon** in Word and paste the prompt below — Copilot in Word references the recap with `/`.',
         'prompt':'Create meeting minutes for the Teams meeting /Unsold Inventory Disposal Workshop. Use the template on this page. Sections: (1) Date and Attendees; (2) Decisions Taken; (3) Action Items with Owner and Due Date; (4) Risks Raised; (5) Open Questions. Quote the Group CFO and Treasury head verbatim where wording matters. Flag any decision linked to the MTN bond redemption test as Critical Path. Save as Minutes_Unsold_Inventory_Workshop.docx.'}
      ], '',
      promptsID=[
        {'instr':'**(1) Di Teams**, buka **Calendar** → klik rapat lampau **"Workshop Disposal Inventory Belum Terjual"**. Pada halaman Recap, tampilkan **AI Notes**, **Custom summary** (template Speaker), dan **Audio recap**. **(2) Di Word for the Web**, buka dokumen baru kosong dan ketik template notulen (Tanggal · Keputusan · Action · Risiko · Pertanyaan Terbuka). **(3) Klik ikon Copilot** di Word dan tempel prompt — Copilot in Word mereferensikan recap dengan `/`.',
         'prompt':'Buat notulen rapat untuk rapat Teams /Workshop Disposal Inventory Belum Terjual. Gunakan template di halaman ini. Bagian: (1) Tanggal dan Peserta; (2) Keputusan; (3) Action dengan Pemilik dan Tenggat; (4) Risiko; (5) Pertanyaan Terbuka. Kutip Direktur Keuangan Grup dan kepala Treasury secara harfiah jika redaksinya penting. Tandai keputusan terkait uji redemption obligasi MTN sebagai Critical Path. Simpan sebagai Notulen_Workshop_Inventory_Belum_Terjual.docx.'}
      ],
      persona=['Sasha Ouellet'],
      personaID=['Sasha Ouellet']),

      tool(T_NOTEBOOK, M365_LIC, M365_ACCT, [
        {'instr':'All sources are loaded in the notebook. The Instructions field is set. Type the prompt below in the notebook chat.',
         'prompt':'Synthesise across all sources to produce a 10-bullet Board narrative. Cover: unsold inventory disposal programme; Bumi-quota conversion 90-day window; MTN bond redemption test status; township P&L recovery; refinancing options; FY2026 launch cadence; KPKT/BPN/OJK regulator engagement; covenant headroom; risk register; decisions requested. Cite the source file (and tab/section) at the end of every bullet.'}
      ], DESC_NOTEBOOK,
      promptsID=[
        {'instr':'Semua sumber sudah dimuat di notebook. Field Instructions sudah diset. Ketik prompt di bawah pada chat notebook.',
         'prompt':'Sintesakan dari semua sumber untuk menghasilkan narasi Direksi 10-bullet. Cakup: program disposal inventory belum terjual; jendela 90 hari konversi kuota Bumi; status uji redemption obligasi MTN; pemulihan P&L township; opsi refinancing; cadence peluncuran FY2026; engagement regulator KPKT/BPN/OJK; headroom covenant; register risiko; keputusan yang diminta. Kutip file sumber (dan tab/bagian) di akhir tiap bullet.'}
      ],
      persona=['Mod Admin'],
      personaID=['Mod Admin'],
      notebookMeta={
        'sources':['/PROP_01_Unsold_Inventory_Tracker.xlsx','/PROP_02_Township_PnL_Model.xlsx','/PROP_04_Bond_Redemption_Stress_Test.xlsx'],
        'instructions':'You are the Group MD of Zava Property preparing a Board pack on converging unsold inventory, Bumi-quota conversion deadline and MTN bond redemption test. Always cite the source file and tab/section. Tone: precise, Board-ready, no speculation about KPKT or OJK intentions beyond what they have communicated in writing. Use MYR for Group totals (1 MYR ≈ 3,580 IDR). Reference real ASEAN peers (Sime Darby Property, Mah Sing, Eco World, IOI Properties, Sunway Property, S P Setia, Sinar Mas Land, Lippo Karawaci, Ciputra Development, Pakuwon Jati, Summarecon Agung, Agung Podomoro) where benchmark precedent strengthens the argument.',
        'instructionsID':'Anda adalah Direktur Pelaksana Grup Zava Property yang menyiapkan paket Direksi tentang konvergensi inventory belum terjual, deadline konversi kuota Bumi dan uji redemption obligasi MTN. Selalu kutip file sumber dan tab/bagian. Nada: presisi, siap-Direksi, tanpa spekulasi tentang niat KPKT atau OJK di luar yang sudah disampaikan tertulis. Gunakan RM untuk total Grup (1 RM ≈ 3.580 Rp). Referensikan peer ASEAN riil (Sime Darby Property, Mah Sing, Eco World, IOI Properties, Sunway Property, S P Setia, Sinar Mas Land, Lippo Karawaci, Ciputra Development, Pakuwon Jati, Summarecon Agung, Agung Podomoro) bila preseden benchmark memperkuat argumen.'
      }),

      tool(T_COWORK, FRONTIER_LIC, M365_ACCT, [
        {'instr':'Open `m365.cloud.microsoft` > left nav > **Agents** > **Cowork**. Paste the single prompt below — Cowork delegates 5 parallel sub-tasks. Frontier required.',
         'prompt':'Cowork — Property 14-Day Sprint. Run these in parallel: (1) 📝 Draft Word — Unsold Inventory Disposal Brief 4 pages, sources /PROP_01_Unsold_Inventory_Tracker.xlsx and /PROP_05_Launch_Cadence_FY2026_Playbook.docx. (2) 📝 Draft Word — Bumi Conversion Submission Talking Points 2 pages, source /PROP_03_Bumi_Quota_Conversion_Brief.docx. (3) ✉️ Send email to Zava Property ExCo, 14 township GMs, Treasury and Legal heads with 3 actions in 72 hours. (4) 📅 Schedule 90-min Board Pre-Read tomorrow 8am MYT titled "Inventory & MTN Bond Alignment". (5) 💬 Post Teams message to #zava-property-exco with one-line headline + dashboard link.'}
      ], DESC_COWORK,
      promptsID=[
        {'instr':'Buka `m365.cloud.microsoft` > nav kiri > **Agents** > **Cowork**. Tempel prompt tunggal — Cowork mendelegasikan 5 sub-tugas paralel. Frontier diperlukan.',
         'prompt':'Cowork — Sprint 14 Hari Property. Jalankan paralel: (1) 📝 Susun Word — Brief Disposal Inventory Belum Terjual 4 halaman, sumber /PROP_01_Unsold_Inventory_Tracker.xlsx dan /PROP_05_Launch_Cadence_FY2026_Playbook.docx. (2) 📝 Susun Word — Talking Points Submission Konversi Bumi 2 halaman, sumber /PROP_03_Bumi_Quota_Conversion_Brief.docx. (3) ✉️ Kirim email ke ExCo Zava Property, 14 GM township, kepala Treasury dan Legal dengan 3 aksi dalam 72 jam. (4) 📅 Jadwalkan Pre-Read Direksi 90 menit besok 08:00 WIB berjudul "Penyelarasan Inventory & Obligasi MTN". (5) 💬 Posting pesan Teams di #zava-property-exco dengan headline satu baris + tautan dashboard.'}
      ],
      persona=['Mod Admin'],
      personaID=['Mod Admin']),

      tool(T_WORD_AGT, ANY_LIC, ANY_ACCT, [
        {'instr':'Open `m365.cloud.microsoft/chat` → Agents tab → **Word Agent**. Paste the prompt below — the agent returns a fully drafted .docx.',
         'prompt':'Goal: Generate a 4-page Group MD Crisis Brief in Word. Context: MYR 1.4B unsold inventory + MYR 280M annual holding cost; Bumi-quota conversion overdue at 5 townships; MTN bond redemption test in 18 months. Source: /PROP_01_Unsold_Inventory_Tracker.xlsx AND /PROP_04_Bond_Redemption_Stress_Test.xlsx. Expectation: Sections — Executive Summary 5 bullets; Current Status of all 3 workstreams; Programme; Financial Impact; Stakeholder Map (KPKT / State Authority / REHDA / BPN / OJK / MTN trustee / lenders); Decisions Requested. Tone: precise, Board-ready. Save as Zava_Property_Crisis_Brief.docx.'}
      ], DESC_WORD_AGT,
      promptsID=[
        {'instr':'Buka `m365.cloud.microsoft/chat` → tab Agents → **Word Agent**. Tempel prompt — agent mengembalikan .docx yang sudah didraf penuh.',
         'prompt':'Tujuan: Hasilkan Brief Krisis Direktur Pelaksana Grup 4 halaman dalam Word. Konteks: Rp 5,0 triliun inventory belum terjual + Rp 1,0 triliun biaya holding tahunan; konversi kuota Bumi overdue di 5 township; uji redemption obligasi MTN dalam 18 bulan. Sumber: /PROP_01_Unsold_Inventory_Tracker.xlsx DAN /PROP_04_Bond_Redemption_Stress_Test.xlsx. Ekspektasi: Bagian — Ringkasan Eksekutif 5 bullet; Status Saat Ini ketiga workstream; Program; Dampak Finansial; Peta Pemangku Kepentingan (KPKT / State Authority / REHDA / BPN / OJK / trustee MTN / pemberi pinjaman); Keputusan yang Diminta. Nada: presisi, siap-Direksi. Simpan sebagai Brief_Krisis_Zava_Property.docx.'}
      ],
      persona=['Sasha Ouellet'],
      personaID=['Sasha Ouellet']),

      tool(T_PPT_AGT, ANY_LIC, ANY_ACCT, [
        {'instr':'Open `m365.cloud.microsoft/chat` → Agents tab → **PowerPoint Agent**. Paste the prompt below.',
         'prompt':'Goal: 9-slide Board deck on unsold inventory + Bumi conversion + MTN bond redemption. Context: Board in 14 days. Source: /Zava_Property_Crisis_Brief.docx and /PROP_01_Unsold_Inventory_Tracker.xlsx. Expectation: Cover; Situation; Stakeholder Map RAG; Unsold Disposal; Bumi Conversion; MTN Bond Strategy; Operating Cash Bridge; FY2026 Launch Cadence; Decisions. Brand #A16207 + #854D0E, 18pt min body, 1 chart/slide. Save as Zava_Property_Board_Deck.pptx.'}
      ], DESC_PPT_AGT,
      promptsID=[
        {'instr':'Buka `m365.cloud.microsoft/chat` → tab Agents → **PowerPoint Agent**. Tempel prompt.',
         'prompt':'Tujuan: Deck 9 slide Direksi tentang inventory belum terjual + konversi Bumi + redemption obligasi MTN. Konteks: Direksi dalam 14 hari. Sumber: /Brief_Krisis_Zava_Property.docx dan /PROP_01_Unsold_Inventory_Tracker.xlsx. Ekspektasi: Cover; Situasi; Peta Pemangku Kepentingan RAG; Disposal Belum Terjual; Konversi Bumi; Strategi Obligasi MTN; Bridge Kas Operasi; Cadence Peluncuran FY2026; Keputusan. Brand #A16207 + #854D0E, font tubuh min 18pt, 1 chart/slide. Simpan sebagai Deck_Direksi_Zava_Property.pptx.'}
      ],
      persona=['Sasha Ouellet'],
      personaID=['Sasha Ouellet']),

      tool(T_XL_AGT, ANY_LIC, ANY_ACCT, [
        {'instr':'Open `m365.cloud.microsoft/chat` → Agents tab → **Excel Agent**. Paste the prompt below.',
         'prompt':'Goal: Build an unsold inventory + township P&L + bond redemption tracker workbook. Context: operating tracker for the Group COO and Treasury. Source: schema only. Expectation: Sheet 1 Unsold Inventory Ageing (by township and unit type with holding cost); Sheet 2 Township P&L Watchlist (14 active townships); Sheet 3 MTN Bond Redemption Stress Test (Base / Stretch / Downside); Sheet 4 Dashboard with KPI tiles + RAG conditional formatting. Save as Zava_Property_Operations_Tracker.xlsx.'}
      ], DESC_XL_AGT,
      promptsID=[
        {'instr':'Buka `m365.cloud.microsoft/chat` → tab Agents → **Excel Agent**. Tempel prompt.',
         'prompt':'Tujuan: Bangun workbook tracker inventory belum terjual + P&L township + redemption obligasi. Konteks: tracker operasi untuk Direktur Operasional Grup dan Treasury. Sumber: hanya skema. Ekspektasi: Sheet 1 Ageing Inventory Belum Terjual (per township dan tipe unit dengan biaya holding); Sheet 2 Watchlist P&L Township (14 township aktif); Sheet 3 Uji Stres Redemption Obligasi MTN (Base / Stretch / Downside); Sheet 4 Dashboard dengan KPI tile + format kondisional RAG. Simpan sebagai Tracker_Operasi_Zava_Property.xlsx.'}
      ],
      persona=['Hadar Caspit'],
      personaID=['Hadar Caspit']),

      tool(T_BUILDER, ANY_LIC, ANY_ACCT, [
        {'instr':'Open `m365.cloud.microsoft/chat` > Agents > **+ Create an agent**. Pick ONE of the 3 agents below. Paste the chosen description into the **Describe** field.',
         'prompt':'**Option A — Zava Property Inventory Watch.** Build an agent for the Group COO and the 14 township GMs to track and explain unsold inventory ageing weekly. Ground every answer on /PROP_01_Unsold_Inventory_Tracker.xlsx and the disposal playbook. Always cite file and tab. Classify each township as On-Track / Watch / Slipping. Tone: precise, sales-grade. Starter prompts: (1) Which townships have the worst ageing; (2) Draft a disposal incentive proposal; (3) Build a weekly inventory dashboard; (4) What is the FY2026 disposal target; (5) Summarise for the COO.'},
        {'instr':'**Option B — alternative agent.** Same Create-an-agent flow with a different specialisation.',
         'prompt':'**Option B — Zava Property Bumi Conversion Agent.** Build an agent for the Legal and Township Liaison teams to manage Bumi-quota conversion submissions to the State Authority. Ground every answer on /PROP_03_Bumi_Quota_Conversion_Brief.docx. Always cite section. Classify each submission as Approved / In Progress / Awaiting State Authority. Tone: factual, regulator-facing, no admission of unproven facts. Starter prompts: (1) Which 3 townships have the 90-day window closing; (2) Draft a State Authority submission narrative; (3) What are the next 3 milestones; (4) Build a weekly conversion dashboard; (5) Summarise the conversion programme.'},
        {'instr':'**Option C — alternative agent.** Same flow.',
         'prompt':'**Option C — Zava Property MTN Bond Redemption Agent.** Build an agent for the Group CFO and Treasury to manage the MTN bond redemption stress test and refinancing options. Ground every answer on /PROP_04_Bond_Redemption_Stress_Test.xlsx. Always cite file and section. Classify covenant headroom as Adequate / Watch / Insufficient. Tone: precise, treasury-grade, conservative. Starter prompts: (1) What is the rolling covenant headroom; (2) Draft the refinancing option memo; (3) Build a weekly Treasury dashboard; (4) What is the FY2027 redemption strategy; (5) Summarise for the Board.'},
        {'instr':'**Test.** After the agent is created, click into it and use the right test pane to validate grounding, citations, scope.',
         'prompt':'Give me the 60-second version of the unsold inventory + Bumi conversion + MTN bond redemption situation, the worst 3 issues, the response programme, and the decisions I must take to the Board in 14 days. Cite the file and tab/section for every paragraph.'},
        {'instr':'**Share.** Click the agent → **Share** → add recipients with **Use** access.',
         'prompt':'Share with the Zava Property ExCo (Group MD, Group CFO, COO, Treasury head, Legal head, Township Liaison head, the 14 township GMs) — Use access. Send notification: "This agent is now in your M365 Copilot chat — ground every inventory / Bumi / MTN-bond question through it for the next 90 days."'}
      ], DESC_BUILDER,
      promptsID=[
        {'instr':'Buka `m365.cloud.microsoft/chat` > Agents > **+ Create an agent**. Pilih SATU dari 3 agent. Tempel deskripsi ke field **Describe**.',
         'prompt':'**Opsi A — Zava Property Inventory Watch.** Bangun agent untuk Direktur Operasional Grup dan 14 GM township untuk melacak dan menjelaskan ageing inventory belum terjual mingguan. Dasarkan pada /PROP_01_Unsold_Inventory_Tracker.xlsx dan playbook disposal. Selalu kutip file dan tab. Klasifikasikan tiap township sebagai On-Track / Watch / Slipping. Nada: presisi, sales-grade. Starter prompt: (1) Township mana yang ageing terburuk; (2) Susun usulan insentif disposal; (3) Bangun dashboard inventory mingguan; (4) Target disposal FY2026; (5) Rangkum untuk COO.'},
        {'instr':'**Opsi B — agent alternatif.** Alur Create-an-agent sama dengan spesialisasi berbeda.',
         'prompt':'**Opsi B — Zava Property Bumi Conversion Agent.** Bangun agent untuk tim Legal dan Township Liaison untuk mengelola submission konversi kuota Bumi ke State Authority. Dasarkan pada /PROP_03_Bumi_Quota_Conversion_Brief.docx. Selalu kutip bagian. Klasifikasikan tiap submission sebagai Approved / In Progress / Awaiting State Authority. Nada: faktual, regulator-facing, tanpa pengakuan fakta yang belum terbukti. Starter prompt: (1) 3 township mana yang jendela 90-hari nya tutup; (2) Susun naratif submission State Authority; (3) 3 milestone berikutnya; (4) Bangun dashboard konversi mingguan; (5) Rangkum program konversi.'},
        {'instr':'**Opsi C — agent alternatif.** Alur sama.',
         'prompt':'**Opsi C — Zava Property MTN Bond Redemption Agent.** Bangun agent untuk Direktur Keuangan Grup dan Treasury untuk mengelola uji stres redemption obligasi MTN dan opsi refinancing. Dasarkan pada /PROP_04_Bond_Redemption_Stress_Test.xlsx. Selalu kutip file dan bagian. Klasifikasikan headroom covenant sebagai Adequate / Watch / Insufficient. Nada: presisi, treasury-grade, konservatif. Starter prompt: (1) Headroom covenant rolling; (2) Susun memo opsi refinancing; (3) Bangun dashboard Treasury mingguan; (4) Strategi redemption FY2027; (5) Rangkum untuk Direksi.'},
        {'instr':'**Uji.** Validasi grounding, kutipan, cakupan.',
         'prompt':'Berikan versi 60 detik dari inventory belum terjual + konversi Bumi + redemption obligasi MTN, 3 isu terburuk, program respons, dan keputusan yang harus saya bawa ke Direksi dalam 14 hari. Kutip file dan tab/bagian untuk tiap paragraf.'},
        {'instr':'**Bagikan.** Klik agent → **Share** → tambahkan penerima dengan akses **Use**.',
         'prompt':'Bagikan ke ExCo Zava Property (Direktur Pelaksana Grup, Direktur Keuangan Grup, COO, kepala Treasury, kepala Legal, kepala Township Liaison, 14 GM township) — akses Use. Kirim notifikasi: "Agent ini sekarang ada di M365 Copilot chat Anda — dasarkan tiap pertanyaan inventory / Bumi / obligasi MTN melalui agent ini selama 90 hari ke depan."'}
      ],
      persona=['Mod Admin','Mod Admin','Mod Admin','Sasha Ouellet','Sasha Ouellet'],
      personaID=['Mod Admin','Mod Admin','Mod Admin','Sasha Ouellet','Sasha Ouellet']),
    ],
    companyID='Zava Property',
    taglineID='Inventory belum terjual Rp 5,0 triliun + konversi kuota Bumi overdue di 5 township + uji redemption obligasi MTN dalam 18 bulan — Direksi dalam 14 hari.',
    scenarioID="Zava Property adalah developer properti tercatat di bursa ASEAN dengan operasi residensial, township terintegrasi dan kawasan industri di Malaysia (Klang Valley, Iskandar Johor, Penang) dan Indonesia (Jabodetabek, Bandung, Surabaya). Grup memiliki 18.400 unit build-out aktif di 14 township aktif dan 4 kawasan industri. Tiga tekanan bertemu: (1) Rp 5,0 triliun (RM 1,4 miliar) inventory selesai belum terjual telah terakumulasi selama 24 bulan, menghasilkan biaya holding tahunan Rp 1,0 triliun (RM 280 juta) (bunga + assessment + utilitas + pajak properti); (2) program konversi kuota Bumi (unit yang diperuntukkan Bumiputera namun tidak diambil) overdue di 5 township — jendela persetujuan State Authority untuk konversi di bawah pedoman KPKT tutup dalam 90 hari untuk 3 township tersebut; (3) uji redemption obligasi MTN Rp 6,4 triliun (RM 1,8 miliar) jatuh tempo dalam 18 bulan dan agen credit-watch telah menurunkan outlook karena drag inventory dan take-up rate peluncuran primer yang melambat. Direktur Pelaksana Grup butuh paket Direksi dalam 14 hari mencakup tracker inventory belum terjual, model P&L township, brief konversi kuota Bumi, uji stres redemption obligasi, dan playbook cadence peluncuran FY2026. Frame customer riil: grup ini beroperasi serupa dengan **Sime Darby Property**, **Mah Sing Group**, **Eco World Development**, **IOI Properties**, **Sunway Property**, **S P Setia**, **Sinar Mas Land**, **Lippo Karawaci**, **Ciputra Development**, **Pakuwon Jati**, **Summarecon Agung**, dan **Agung Podomoro Land** — dengan regulator termasuk **REHDA**, **KPKT**, **BPN**, **Kementerian PUPR**, dan **OJK** aktif bersamaan.",
    relevantDepts=['dept-finance','dept-strategy','dept-operations','dept-legal','dept-risk','dept-marketing'],
    personas=[
      {'name':'Sasha Ouellet','role':'Group MD - Property Development','roleID':'Direktur Utama - Pengembangan Properti','acct':FREE_ACCT,'lic':FREE_LIC,'color':'#A16207'},
      {'name':'Mod Admin','role':'Group Strategy Director','roleID':'Direktur Strategi Grup','acct':M365_ACCT,'lic':M365_LIC,'color':'#059669'},
      {'name':'Hadar Caspit','role':'Group CFO & Treasurer','roleID':'Direktur Keuangan & Treasurer Grup','acct':M365_ACCT,'lic':M365_LIC,'color':'#1E40AF'},
      {'name':'Daichi Kimura','role':'Township Liaison & Legal Director','roleID':'Direktur Township Liaison & Legal','acct':M365_ACCT,'lic':M365_LIC,'color':'#DC2626'}
    ],
    storyboard=[
      {'ex':1,'title':'Research & Brief','titleID':'Riset & Pengarahan','minutes':18,'mode':'Show & Tell + Hands-on',
       'summary':'Frame the inventory + Bumi + MTN bond situation and pull peer playbooks before the redemption clock starts ticking.',
       'summaryID':'Bingkai situasi inventory + Bumi + obligasi MTN dan tarik playbook peer sebelum clock redemption berdetak.',
       'tasks':[
         {'verb':'Frame the morning question and lock the day priorities','verbID':'Susun pertanyaan pagi dan kunci prioritas hari ini','toolId':T_CHAT,'mode':'Show & Tell'},
         {'verb':'Run an outside-in peer scan and pull proven plays','verbID':'Lakukan pemindaian peer dari luar dan tarik praktik terbaik','toolId':T_RESEARCHER,'mode':'Show & Tell'},
         {'verb':'Generate a board-ready brief straight from chat','verbID':'Hasilkan brief siap-Direksi langsung dari chat','toolId':T_WORD_AGT,'mode':'Hands-on'}]},
      {'ex':2,'title':'Analyse & Decide','titleID':'Analisis & Putuskan','minutes':18,'mode':'Hands-on',
       'summary':'Quantify the inventory + township P&L + bond stress combined impact; build a Board dashboard.',
       'summaryID':'Kuantifikasi dampak gabungan inventory + P&L township + stres obligasi; bangun dashboard Direksi.',
       'tasks':[
         {'verb':'Crunch the numbers and surface the biggest gaps','verbID':'Olah angka dan ungkap celah terbesar','toolId':T_ANALYST,'mode':'Hands-on'},
         {'verb':'Build a single-pane operating dashboard','verbID':'Bangun dashboard operasi satu-halaman','toolId':T_EXCEL,'mode':'Hands-on'},
         {'verb':'Spin up a recurring tracker workbook from chat','verbID':'Buat workbook tracker berulang dari chat','toolId':T_XL_AGT,'mode':'Hands-on'}]},
      {'ex':3,'title':'Communicate & Coordinate','titleID':'Komunikasi & Koordinasi','minutes':18,'mode':'Hands-on',
       'summary':'Brief township GMs and Treasury, capture the Inventory Workshop recap, and assemble the Board deck.',
       'summaryID':'Brief GM township dan Treasury, capture recap Workshop Inventory, dan rakit deck Direksi.',
       'tasks':[
         {'verb':'Draft the stakeholder alignment email','verbID':'Draf email penyelarasan stakeholder','toolId':T_OUTLOOK,'mode':'Hands-on'},
         {'verb':'Recap the meeting and turn it into minutes','verbID':'Recap rapat dan ubah ke notulen','toolId':T_TEAMS,'mode':'Hands-on'},
         {'verb':'Generate a board-ready deck from chat','verbID':'Hasilkan deck siap-Direksi dari chat','toolId':T_PPT_AGT,'mode':'Hands-on'},
         {'verb':'Delegate a 5-task parallel sprint','verbID':'Delegasikan 5-tugas paralel ke Cowork','toolId':T_COWORK,'mode':'Show & Tell'}]},
      {'ex':4,'title':'Build & Scale','titleID':'Bangun & Skala','minutes':15,'mode':'Show & Tell',
       'summary':'Wrap the inventory + Bumi + MTN bond playbook into a reusable agent for the Zava Property operating team.',
       'summaryID':'Bungkus playbook inventory + Bumi + obligasi MTN ke dalam agent reusable untuk tim operasi Zava Property.',
       'tasks':[
         {'verb':'Pull every source into one synthesis notebook','verbID':'Tarik semua sumber ke satu notebook sintesis','toolId':T_NOTEBOOK,'mode':'Show & Tell'},
         {'verb':'Wrap the daily workflow into a reusable agent','verbID':'Bungkus alur kerja harian jadi agen yang dapat dipakai ulang','toolId':T_BUILDER,'mode':'Show & Tell'}]}
    ],
    geo='MY+ID'
))

# INDUSTRIES_12.append(... property-development ...)
# INDUSTRIES_12.append(... ecommerce-superapp ...)
# INDUSTRIES_12.append(... maritime-shipping ...)

print(f"Industries batch 12 written: {len(INDUSTRIES_12)} entries")
