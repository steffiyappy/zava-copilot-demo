# Phase B — Industry batch 4: Oil & Gas Downstream, Renewable Energy, Industrial Manufacturing
# Bilingual (English + Bahasa Indonesia), 14 tools per industry, FRONTIER_LIC for cowork,
# multi-tab Excel workbooks, agent-builder finale, 4 personas, 12-task storyboard.
import sys
sys.path.insert(0, '.')
import _builder_catalog as _bcat
from util import (T_CHAT, T_RESEARCHER, T_ANALYST, T_EXCEL, T_WORD, T_PPT, T_OUTLOOK,
                  T_TEAMS, T_NOTEBOOK, T_COWORK, T_WORD_AGT, T_PPT_AGT, T_XL_AGT, T_BUILDER,
                  tool_builder,
                  DESC_CHAT, DESC_RESEARCHER, DESC_ANALYST, DESC_EXCEL, DESC_WORD, DESC_PPT,
                  DESC_OUTLOOK, DESC_TEAMS, DESC_NOTEBOOK, DESC_COWORK, DESC_WORD_AGT,
                  DESC_PPT_AGT, DESC_XL_AGT, DESC_BUILDER,
                  FREE_LIC, FREE_ACCT, M365_LIC, M365_ACCT, ANY_LIC, ANY_ACCT, FRONTIER_LIC,
                  tool, ind)

# ───────────────────────── INDUSTRY CONTEXTS ─────────────────────────
OG = {
    'id': 'og-downstream', 'sector': 'og-energy',
    'name': 'Oil & Gas Downstream', 'icon': '🏭',
    'color': '#BF360C', 'accent': '#D84315',
    'co': 'Zava Oil Downstream Malaysia', 'co_id': 'Zava Oil Downstream Indonesia',
    'tagline': 'FY2025 refining margin compressed to USD 5.1/bbl with major turnaround in 16 weeks — Board reset Tuesday.',
    'taglineID': 'Margin refining FY2025 turun ke USD 5,1/bbl dengan turnaround besar dalam 16 minggu — reset Direksi hari Selasa.',
    'scenario': "Zava Oil Downstream Malaysia is a Malaysian downstream refiner listed on Bursa Malaysia with about 3,400 employees, a 165 kbpd coastal refinery, and integrated marketing, trading and HSE divisions supplying transport fuels and petrochemical feedstock into Malaysia and selected Indonesian counterparties through a Pertamina-affiliated joint venture. FY2025 gross refining margin compressed to USD 5.1/bbl from a USD 7.4/bbl budget, the conversion units have lost 6 percentage points of utilisation after repeated reliability interruptions, middle-distillate yield is running below plan, and a major turnaround on Crude Distillation Unit 2 is now less than 16 weeks away. Three Tier 2 process-safety events in Q4 have triggered DOSH formal correspondence, the Department of Environment has flagged flaring variance, and the trading book carries USD 38 M of mark-to-market loss on sour-crude hedges. BPH Migas in Indonesia and Kementerian ESDM are simultaneously requesting transparency on volumes, pricing and HSE performance ahead of the next licence review. The Group CEO has called a Board reset on Tuesday and needs a defensible margin recovery, turnaround readiness, HSE remediation and regulator narrative — fast.",
    'scenarioID': 'Zava Oil Downstream Indonesia adalah anak usaha hilir migas BUMN yang tercatat di Bursa Efek Indonesia dengan sekitar 4.200 karyawan, satu kilang pesisir berkapasitas 165 kbpd, serta divisi pemasaran, trading dan HSE terintegrasi yang memasok bahan bakar transportasi dan feedstock petrokimia ke Indonesia dan beberapa mitra Malaysia. Margin refining FY2025 meleset menjadi USD 5,1/bbl dari RKAP USD 7,4/bbl, unit konversi kehilangan 6 poin persentase utilisasi akibat gangguan keandalan berulang, yield distilat tengah berada di bawah rencana, dan turnaround besar pada Crude Distillation Unit 2 kurang dari 16 minggu lagi. Tiga insiden process safety Tier 2 di Q4 telah memicu surat resmi dari Kementerian ESDM, KLHK menyoroti selisih flaring, dan buku trading membukukan kerugian mark-to-market sebesar Rp 600 miliar atas hedge minyak mentah sour. BPH Migas meminta transparansi atas volume, harga dan kinerja HSE menjelang tinjauan izin berikutnya. Direktur Utama menggelar reset Direksi hari Selasa dan membutuhkan narasi pemulihan margin, kesiapan turnaround, remediasi HSE dan regulator yang dapat dipertahankan — secara cepat.',
    'files': ['OGD_01_Refinery_Operations.xlsx', 'OGD_02_Environmental_Compliance.docx',
              'OGD_03_Refinery_Maintenance_Plan.docx', 'OGD_04_Trading_Position_Book.xlsx',
              'OGD_05_HSE_Incident_Register.xlsx', 'OGD_06_BPH_Migas_Submission.docx'],
    'f_xlsx_ops': 'OGD_01_Refinery_Operations.xlsx',
    'f_docx_env': 'OGD_02_Environmental_Compliance.docx',
    'f_docx_maint': 'OGD_03_Refinery_Maintenance_Plan.docx',
    'f_xlsx_trade': 'OGD_04_Trading_Position_Book.xlsx',
    'f_xlsx_hse': 'OGD_05_HSE_Incident_Register.xlsx',
    'f_docx_reg': 'OGD_06_BPH_Migas_Submission.docx',
    'tabs1': 'Throughput Dashboard, Margin Bridge, Yield Profile, Energy Balance and Reliability Index tabs',
    'kpi_phrase_en': 'the USD 5.1/bbl margin compression, the conversion-unit reliability gap and the 16-week turnaround window',
    'kpi_phrase_id': 'kompresi margin USD 5,1/bbl, gap keandalan unit konversi dan jendela turnaround 16 minggu',
    'crisis_short_en': 'the FY2025 refining margin miss and turnaround readiness',
    'crisis_short_id': 'selisih margin refining FY2025 dan kesiapan turnaround',
    'event_en': 'Board reset on Tuesday', 'event_id': 'reset Direksi hari Selasa',
    'regulators_en': 'BPH Migas, Kementerian ESDM, DOSH, Department of Environment, Bursa Malaysia, OJK and BEI',
    'regulators_id': 'BPH Migas, Kementerian ESDM, KLHK, DOSH, BEI dan OJK',
    'agent_name': 'Bumi Seri Refining War Room',
    'agent_name_id': 'War Room Pertamina Hilir Nusantara',
    'recovery_focus_en': 'margin recovery, turnaround readiness and HSE remediation',
    'recovery_focus_id': 'pemulihan margin, kesiapan turnaround dan remediasi HSE',
    'topic_short_en': 'refining margin recovery and turnaround readiness',
    'topic_short_id': 'pemulihan margin refining dan kesiapan turnaround',
    'ana_timeline_event_en': 'reliability interruptions and HSE deviations',
    'ana_timeline_event_id': 'gangguan keandalan dan deviasi HSE',
    'xl_heatmap_metric_en': 'energy intensity (EII) and conversion-unit utilisation',
    'xl_heatmap_metric_id': 'energy intensity (EII) dan utilisasi unit konversi',
    'xl_exposure_lens_en': 'hedged crude positions by counterparty, currency and tenor',
    'xl_exposure_lens_id': 'posisi crude yang dihedge berdasarkan counterparty, mata uang dan tenor',
    'ppt_scenario_label_en': "'Refining Margin Bridge' slide with three columns — base case, accelerated turnaround, deferred turnaround",
    'ppt_scenario_label_id': "slide 'Jembatan Margin Refining' dengan tiga kolom — base case, turnaround dipercepat, turnaround ditunda",
    'roles_en': {'cfo': 'Group CFO', 'ceo': 'Group CEO', 'cos': 'Chief of Staff to the CEO',
                 'coo': 'COO Refining & Marketing', 'hsa': 'Head of HSE'},
    'roles_id': {'cfo': 'Direktur Keuangan', 'ceo': 'Direktur Utama', 'cos': 'Kepala Staf Direktur Utama',
                 'coo': 'Direktur Operasi Refining & Marketing', 'hsa': 'Kepala HSE'},
    'relevantDepts': ['dept-operations', 'dept-finance', 'dept-risk', 'dept-esg'],
}

RE = {
    'id': 'renewable-energy', 'sector': 'og-energy',
    'name': 'Renewable Energy', 'icon': '☀️',
    'color': '#F9A825', 'accent': '#F57F17',
    'co': 'Zava Renewables Malaysia', 'co_id': 'Zava Renewables Indonesia',
    'tagline': 'Curtailment at 8.6%, O&M cost up 14% and a MYR 1.4B refinancing window — Board pipeline review Thursday.',
    'taglineID': 'Curtailment 8,6%, biaya O&M naik 14% dan jendela refinancing Rp 4,8 triliun — tinjauan pipeline Direksi hari Kamis.',
    'scenario': "Zava Renewables Malaysia is a Malaysian renewable energy IPP listed on Bursa Malaysia with about 1,900 employees and 1.4 GW of operating solar and wind capacity, plus a cross-border project development pipeline of 850 MW with an Indonesian affiliate listed on IDX. Operating data shows utility-scale Solar Generation and Wind Farm Output close to nameplate, but the Grid Curtailment Tracker reveals curtailment has reached 8.6% at two sites because of TNB transmission constraints and PLN dispatch limits in Sumatra. PPA Revenue Tracker shows revenue leakage of about MYR 41 M over the last four quarters, while O&M Cost Summary has risen 14% year on year due to inverter replacements, blade inspections and imported spare parts. The 850 MW Indonesian pipeline depends on PLN PPA renegotiation, Renewable Portfolio Standard alignment and KLHK environmental permits, and a MYR 1.4B refinancing window opens in 14 weeks. Suruhanjaya Tenaga and Kementerian ESDM are both watching dispatch performance, and the Board wants clearer evidence that the asset management plan and the ESG disclosures can withstand lender scrutiny. The Group CEO has called a Board pipeline review on Thursday and needs a defensible recovery plan on curtailment, O&M cost, project finance and regulator engagement — fast.",
    'scenarioID': 'Zava Renewables Indonesia adalah IPP energi terbarukan Indonesia yang tercatat di Bursa Efek Indonesia dengan sekitar 2.300 karyawan dan kapasitas operasi solar dan angin sebesar 1,4 GW, ditambah pipeline pengembangan proyek lintas-batas 850 MW dengan mitra Malaysia. Data operasi menunjukkan Solar Generation dan Wind Farm Output utility-scale mendekati nameplate, namun Grid Curtailment Tracker menampakkan curtailment mencapai 8,6% di dua lokasi akibat keterbatasan dispatch PLN di Sumatra dan kendala transmisi TNB. PPA Revenue Tracker memperlihatkan kebocoran pendapatan sekitar Rp 145 miliar selama empat kuartal terakhir, sementara O&M Cost Summary naik 14% tahun-ke-tahun karena penggantian inverter, inspeksi blade dan suku cadang impor. Pipeline 850 MW bergantung pada renegosiasi PPA PLN, keselarasan Renewable Portfolio Standard dan izin lingkungan KLHK, sedangkan jendela refinancing sebesar Rp 4,8 triliun terbuka dalam 14 minggu. Kementerian ESDM dan Suruhanjaya Tenaga sama-sama memantau kinerja dispatch, dan Direksi ingin bukti lebih jelas bahwa rencana asset management dan pengungkapan ESG tahan terhadap penelitian kreditor. Direktur Utama menggelar tinjauan pipeline Direksi hari Kamis dan membutuhkan rencana pemulihan curtailment, biaya O&M, project finance dan engagement regulator yang dapat dipertahankan — secara cepat.',
    'files': ['RE_01_Plant_Performance.xlsx', 'RE_02_ESG_Reporting_Framework.docx',
              'RE_03_Asset_Management_Plan.docx', 'RE_04_PPA_Contract_Tracker.xlsx',
              'RE_05_Project_Pipeline_Finance.xlsx', 'RE_06_PLN_Dispatch_Compliance.docx'],
    'f_xlsx_ops': 'RE_01_Plant_Performance.xlsx',
    'f_docx_env': 'RE_02_ESG_Reporting_Framework.docx',
    'f_docx_maint': 'RE_03_Asset_Management_Plan.docx',
    'f_xlsx_trade': 'RE_04_PPA_Contract_Tracker.xlsx',
    'f_xlsx_hse': 'RE_05_Project_Pipeline_Finance.xlsx',
    'f_docx_reg': 'RE_06_PLN_Dispatch_Compliance.docx',
    'tabs1': 'Solar Generation, Wind Farm Output, Grid Curtailment Tracker, PPA Revenue Tracker and O&M Cost Summary tabs',
    'kpi_phrase_en': 'the 8.6% grid curtailment, the 14% O&M cost rise and the MYR 1.4B refinancing window',
    'kpi_phrase_id': 'curtailment 8,6%, kenaikan biaya O&M 14% dan jendela refinancing Rp 4,8 triliun',
    'crisis_short_en': 'curtailment, O&M cost rise and the refinancing window',
    'crisis_short_id': 'curtailment, kenaikan biaya O&M dan jendela refinancing',
    'event_en': 'Board pipeline review on Thursday', 'event_id': 'tinjauan pipeline Direksi hari Kamis',
    'regulators_en': 'Suruhanjaya Tenaga, Kementerian ESDM, KLHK, PLN, TNB, Bursa Malaysia and BEI',
    'regulators_id': 'PLN, Kementerian ESDM, KLHK, BEI dan OJK',
    'agent_name': 'Suria Angin Renewables War Room',
    'agent_name_id': 'War Room Energi Hijau Nusantara',
    'recovery_focus_en': 'curtailment recovery, O&M cost discipline, project finance readiness and regulator engagement',
    'recovery_focus_id': 'pemulihan curtailment, disiplin biaya O&M, kesiapan project finance dan engagement regulator',
    'topic_short_en': 'curtailment recovery and project finance readiness',
    'topic_short_id': 'pemulihan curtailment dan kesiapan project finance',
    'ana_timeline_event_en': 'curtailment incidents and PPA dispatch breaches',
    'ana_timeline_event_id': 'insiden curtailment dan pelanggaran dispatch PPA',
    'xl_heatmap_metric_en': 'capacity factor and PPA-availability ratio',
    'xl_heatmap_metric_id': 'capacity factor dan rasio ketersediaan PPA',
    'xl_exposure_lens_en': 'off-taker credit exposure and curtailment compensation by site',
    'xl_exposure_lens_id': 'eksposur kredit off-taker dan kompensasi curtailment per lokasi',
    'ppt_scenario_label_en': "'PPA Cashflow Bridge' slide with three columns — base case, accelerated build-out, deferred build-out",
    'ppt_scenario_label_id': "slide 'Jembatan Cashflow PPA' dengan tiga kolom — base case, build-out dipercepat, build-out ditunda",
    'roles_en': {'cfo': 'Group CFO', 'ceo': 'Group CEO', 'cos': 'Chief of Staff to the CEO',
                 'coo': 'Chief Project Officer', 'hsa': 'Head of ESG'},
    'roles_id': {'cfo': 'Direktur Keuangan', 'ceo': 'Direktur Utama', 'cos': 'Kepala Staf Direktur Utama',
                 'coo': 'Direktur Proyek', 'hsa': 'Kepala ESG'},
    'relevantDepts': ['dept-operations', 'dept-finance', 'dept-esg', 'dept-strategy'],
}

MFG = {
    'id': 'industrial-manufacturing', 'sector': 'manufacturing',
    'name': 'Industrial Manufacturing', 'icon': '⚙️',
    'color': '#263238', 'accent': '#37474F',
    'co': 'Zava Manufacturing Malaysia', 'co_id': 'Zava Manufacturing Indonesia',
    'tagline': 'Network OEE stuck at 68%, rejects at 4.9% and OTIF at 91% — Board operations reset Wednesday.',
    'taglineID': 'OEE jaringan tertahan 68%, reject rate 4,9% dan OTIF 91% — reset operasi Direksi hari Rabu.',
    'scenario': "Zava Manufacturing Malaysia is a Malaysian precision component and sub-assembly manufacturer listed on Bursa Malaysia with about 5,800 employees across plants in Nilai and Batu Kawan supplying automotive, electronics and industrial OEM customers, and an Indonesian affiliate listed on IDX serving regional Tier 1 customers. The Line OEE Dashboard shows network OEE stuck at 68% against a 75% recovery target, Quality Reject Log shows defect rate at 4.9% with rework concentrated on two high-volume customer programmes, Production Plan vs Actual shows chronic shortfalls on weekend shifts, and Raw Material Cost Tracker captures continuing volatility in resin, copper and imported machining consumables. Customer Order Fulfillment has slipped to 91% OTIF, raising the risk of supplier penalties and allocation losses on the next sourcing round with three Tier 1 OEM customers. Supply Chain Performance shows two single-source components with 9-week lead times, and a key Japanese customer audit is scheduled in 5 weeks. Kementerian Perindustrian incentive reporting, BKPM investment review, SNI quality certification and DOSH workplace safety discipline all intersect with the operating reset described in the lean manufacturing guide and the controls documented in the quality management system. The Group CEO has called a Board operations reset on Wednesday and needs a defensible recovery on OEE, quality, OTIF and supply chain — fast.",
    'scenarioID': 'Zava Manufacturing Indonesia adalah produsen komponen presisi dan sub-assembly Indonesia yang tercatat di Bursa Efek Indonesia dengan sekitar 6.500 karyawan di pabrik Karawang dan Cikarang yang memasok pelanggan OEM otomotif, elektronik dan industri, serta mitra Malaysia yang melayani pelanggan Tier 1 regional. Line OEE Dashboard menampakkan OEE jaringan tertahan 68% terhadap target pemulihan 75%, Quality Reject Log menunjukkan reject rate 4,9% dengan rework terkonsentrasi pada dua program pelanggan volume tinggi, Production Plan vs Actual menampilkan kekurangan kronis pada shift akhir pekan, dan Raw Material Cost Tracker mencatat volatilitas berlanjut pada resin, tembaga dan consumable mesin impor. Customer Order Fulfillment turun ke 91% OTIF, meningkatkan risiko penalti supplier dan kehilangan alokasi pada putaran sourcing berikutnya dengan tiga pelanggan OEM Tier 1. Supply Chain Performance menunjukkan dua komponen single-source dengan lead time 9 minggu, dan audit pelanggan Jepang utama dijadwalkan 5 minggu lagi. Pelaporan insentif Kementerian Perindustrian, tinjauan investasi BKPM, sertifikasi mutu SNI dan disiplin keselamatan kerja DOSH semuanya berpotongan dengan reset operasi yang dijelaskan dalam panduan lean manufacturing dan kontrol yang didokumentasikan dalam quality management system. Direktur Utama menggelar reset operasi Direksi hari Rabu dan membutuhkan pemulihan OEE, mutu, OTIF dan rantai pasok yang dapat dipertahankan — secara cepat.',
    'files': ['MFG_01_Production_Metrics.xlsx', 'MFG_02_Quality_Management_System.docx',
              'MFG_03_Lean_Manufacturing_Guide.docx', 'MFG_04_Supply_Chain_Performance.xlsx',
              'MFG_05_Customer_OTIF_Tracker.xlsx', 'MFG_06_SNI_Quality_Submission.docx'],
    'f_xlsx_ops': 'MFG_01_Production_Metrics.xlsx',
    'f_docx_env': 'MFG_02_Quality_Management_System.docx',
    'f_docx_maint': 'MFG_03_Lean_Manufacturing_Guide.docx',
    'f_xlsx_trade': 'MFG_04_Supply_Chain_Performance.xlsx',
    'f_xlsx_hse': 'MFG_05_Customer_OTIF_Tracker.xlsx',
    'f_docx_reg': 'MFG_06_SNI_Quality_Submission.docx',
    'tabs1': 'Line OEE Dashboard, Quality Reject Log, Production Plan vs Actual, Raw Material Cost Tracker and Customer Order Fulfillment tabs',
    'kpi_phrase_en': 'the 68% network OEE, the 4.9% reject rate and the 91% OTIF slippage',
    'kpi_phrase_id': 'OEE jaringan 68%, reject rate 4,9% dan slippage OTIF 91%',
    'crisis_short_en': 'OEE recovery, quality, OTIF and supply chain',
    'crisis_short_id': 'pemulihan OEE, mutu, OTIF dan rantai pasok',
    'event_en': 'Board operations reset on Wednesday', 'event_id': 'reset operasi Direksi hari Rabu',
    'regulators_en': 'Kementerian Perindustrian, BKPM, SNI, DOSH, Bursa Malaysia and BEI',
    'regulators_id': 'Kementerian Perindustrian, BKPM, SNI, DOSH, BEI dan OJK',
    'agent_name': 'Maju Teknika Operations War Room',
    'agent_name_id': 'War Room Operasi Astra Industri Mandiri',
    'recovery_focus_en': 'OEE recovery, quality discipline, OTIF protection and supply-chain de-risking',
    'recovery_focus_id': 'pemulihan OEE, disiplin mutu, perlindungan OTIF dan de-risking rantai pasok',
    'topic_short_en': 'OEE recovery and OTIF protection',
    'topic_short_id': 'pemulihan OEE dan perlindungan OTIF',
    'ana_timeline_event_en': 'OEE breaks, line-changeover misses and customer-OTIF slips',
    'ana_timeline_event_id': 'gangguan OEE, kegagalan changeover line dan slippage OTIF pelanggan',
    'xl_heatmap_metric_en': 'OEE and customer-OTIF score',
    'xl_heatmap_metric_id': 'OEE dan skor OTIF pelanggan',
    'xl_exposure_lens_en': 'customer-concentration and single-source supplier exposure',
    'xl_exposure_lens_id': 'konsentrasi pelanggan dan eksposur supplier single-source',
    'ppt_scenario_label_en': "'Order-Book Bridge' slide with three columns — base case, accelerated mix-shift, deferred capex",
    'ppt_scenario_label_id': "slide 'Jembatan Order Book' dengan tiga kolom — base case, mix-shift dipercepat, capex ditunda",
    'roles_en': {'cfo': 'Group CFO', 'ceo': 'Group CEO', 'cos': 'Chief of Staff to the CEO',
                 'coo': 'COO', 'hsa': 'Head of Supply Chain'},
    'roles_id': {'cfo': 'Direktur Keuangan', 'ceo': 'Direktur Utama', 'cos': 'Kepala Staf Direktur Utama',
                 'coo': 'Direktur Operasi', 'hsa': 'Kepala Rantai Pasok'},
    'relevantDepts': ['dept-operations', 'dept-finance', 'dept-strategy', 'dept-risk'],
}

INDUSTRIES_4 = []  # populated below by _build()


# ───────────────────────── PERSONAS HELPER ─────────────────────────
def _personas(c):
    re_id = c['roles_id']
    re_en = c['roles_en']
    return [
        {'id': 'hadar-caspit', 'name': 'Hadar Caspit',
         'role': re_en['cfo'], 'roleID': re_id['cfo'],
         'license': 'Microsoft 365 Copilot', 'licenseID': 'Microsoft 365 Copilot',
         'account': 'admin@ABSx62256373.onmicrosoft.com',
         'color': '#1E40AF', 'avatar': 'HC',
         'leads': ['T_RESEARCHER', 'T_ANALYST', 'T_EXCEL', 'T_NOTEBOOK'],
         'leadsID': ['T_RESEARCHER', 'T_ANALYST', 'T_EXCEL', 'T_NOTEBOOK']},
        {'id': 'mod-admin', 'name': 'Mod Admin',
         'role': re_en['coo'], 'roleID': re_id['coo'],
         'license': 'Microsoft 365 Copilot', 'licenseID': 'Microsoft 365 Copilot',
         'account': 'admin@ABSx62256373.onmicrosoft.com',
         'color': '#059669', 'avatar': 'MA',
         'leads': ['T_TEAMS', 'T_OUTLOOK', 'T_COWORK'],
         'leadsID': ['T_TEAMS', 'T_OUTLOOK', 'T_COWORK']},
        {'id': 'sasha-ouellet', 'name': 'Sasha Ouellet',
         'role': re_en['cos'], 'roleID': re_id['cos'],
         'license': 'Free — no Microsoft 365 Copilot license needed',
         'licenseID': 'Bebas — tanpa lisensi Microsoft 365 Copilot',
         'account': 'SashaO@ABSx62256373.OnMicrosoft.com',
         'color': '#7C3AED', 'avatar': 'SO',
         'leads': ['T_CHAT', 'T_RESEARCHER'],
         'leadsID': ['T_CHAT', 'T_RESEARCHER']},
        {'id': 'daichi-maruyama', 'name': 'Daichi Maruyama',
         'role': re_en['hsa'], 'roleID': re_id['hsa'],
         'license': 'Microsoft 365 Copilot', 'licenseID': 'Microsoft 365 Copilot',
         'account': 'admin@ABSx62256373.onmicrosoft.com',
         'color': '#DC2626', 'avatar': 'DM',
         'leads': ['T_WORD', 'T_PPT', 'T_WORD_AGT', 'T_PPT_AGT', 'T_XL_AGT', 'T_BUILDER'],
         'leadsID': ['T_WORD', 'T_PPT', 'T_WORD_AGT', 'T_PPT_AGT', 'T_XL_AGT', 'T_BUILDER']},
    ]


# ───────────────────────── STORYBOARD HELPER ─────────────────────────
def _storyboard(c):
    re_en = c['roles_en']
    re_id = c['roles_id']
    return [
        {'id': 'ex1', 'title': 'Exercise 1 — Diagnose & Brief',
         'titleID': 'Latihan 1 — Diagnosa & Pengarahan',
         'objective': f"Frame the {c['crisis_short_en']} so the {re_en['ceo']} and Board can see exactly where {c['name'].lower()} performance has slipped.",
         'objectiveID': f"Bingkai {c['crisis_short_id']} agar {re_id['ceo']} dan Direksi dapat melihat dengan tepat di mana kinerja {c['name'].lower()} meleset.",
         'tasks': [
             {'tool': 'T_CHAT', 'persona': 'Sasha Ouellet',
              'verb': f"Scope the {c['agent_name']} brief on the open web",
              'verbID': f"Susun ringkasan {c['agent_name_id']} di web terbuka",
              'desc': f"Sasha ({re_en['cos']}, Free license) opens m365.cloud.microsoft/chat in Edge to scope the {c['agent_name']} brief without grounding on tenant data.",
              'descID': f"Sasha ({re_id['cos']}, lisensi Bebas) membuka m365.cloud.microsoft/chat di Edge untuk menyusun ringkasan {c['agent_name_id']} tanpa grounding pada data tenant."},
             {'tool': 'T_RESEARCHER', 'persona': 'Hadar Caspit',
              'verb': f"Run Researcher in Critique Mode on the FY2025 narrative",
              'verbID': f"Jalankan Researcher Critique Mode pada narasi FY2025",
              'desc': f"Hadar ({re_en['cfo']}) runs Researcher in Critique Mode against the FY2025 narrative on {c['kpi_phrase_en']}.",
              'descID': f"Hadar ({re_id['cfo']}) menjalankan Researcher dalam Critique Mode terhadap narasi FY2025 mengenai {c['kpi_phrase_id']}."},
             {'tool': 'T_RESEARCHER', 'persona': 'Hadar Caspit',
              'verb': f"Run Researcher in Model Council Mode to compare Asia-Pacific peers",
              'verbID': f"Jalankan Researcher Model Council Mode untuk membandingkan peer Asia-Pasifik",
              'desc': f"Hadar reruns Researcher in Model Council Mode to compare Asia-Pacific peer responses on {c['topic_short_en']}.",
              'descID': f"Hadar menjalankan ulang Researcher dalam Model Council Mode untuk membandingkan respons peer Asia-Pasifik mengenai {c['topic_short_id']}."},
         ]},
        {'id': 'ex2', 'title': 'Exercise 2 — Quantify',
         'titleID': 'Latihan 2 — Kuantifikasi',
         'objective': f"Quantify the operating gap so the {re_en['cfo']} can present a defensible bridge for the {c['event_en']}.",
         'objectiveID': f"Kuantifikasi gap operasi agar {re_id['cfo']} dapat menyajikan bridge yang dapat dipertahankan untuk {c['event_id']}.",
         'tasks': [
             {'tool': 'T_ANALYST', 'persona': 'Hadar Caspit',
              'verb': f"Use Analyst on the ops and trade workbooks to isolate KPI drivers",
              'verbID': f"Gunakan Analyst pada workbook operasi dan trade untuk mengisolasi pendorong KPI",
              'desc': f"Hadar uses Analyst in Copilot Chat against {c['f_xlsx_ops']} and {c['f_xlsx_trade']} to isolate the drivers behind {c['kpi_phrase_en']}.",
              'descID': f"Hadar menggunakan Analyst di Copilot Chat terhadap {c['f_xlsx_ops']} dan {c['f_xlsx_trade']} untuk mengisolasi pendorong di balik {c['kpi_phrase_id']}."},
             {'tool': 'T_EXCEL', 'persona': 'Hadar Caspit',
              'verb': f"Refresh the operations dashboard tabs in Excel",
              'verbID': f"Segarkan tab dashboard operasi di Excel",
              'desc': f"Hadar opens {c['f_xlsx_ops']} in Excel desktop and asks Copilot to refresh the {c['tabs1']}.",
              'descID': f"Hadar membuka {c['f_xlsx_ops']} di Excel desktop dan meminta Copilot menyegarkan tab {c['tabs1']}."},
             {'tool': 'T_NOTEBOOK', 'persona': 'Hadar Caspit',
              'verb': f"Pin the four working files into a Copilot Notebook and ask for an audio overview",
              'verbID': f"Sematkan empat file kerja ke Copilot Notebook dan minta audio overview",
              'desc': f"Hadar pins the four working files into a Copilot Notebook and asks for an audio overview on {c['topic_short_en']}.",
              'descID': f"Hadar menyematkan empat file kerja ke dalam Copilot Notebook dan meminta audio overview mengenai {c['topic_short_id']}."},
         ]},
        {'id': 'ex3', 'title': 'Exercise 3 — Communicate',
         'titleID': 'Latihan 3 — Komunikasi',
         'objective': f"Translate the operating gap into Word, PowerPoint and Outlook artefacts the Board, regulators and lenders can act on.",
         'objectiveID': f"Terjemahkan gap operasi menjadi artefak Word, PowerPoint dan Outlook yang dapat ditindaklanjuti Direksi, regulator dan kreditor.",
         'tasks': [
             {'tool': 'T_WORD', 'persona': 'Daichi Maruyama',
              'verb': f"Draft the regulator-facing remediation memo in Word",
              'verbID': f"Susun memo remediasi untuk regulator di Word",
              'desc': f"Daichi ({re_en['hsa']}) opens {c['f_docx_env']} in Word desktop and asks Copilot to draft the regulator-facing remediation memo.",
              'descID': f"Daichi ({re_id['hsa']}) membuka {c['f_docx_env']} di Word desktop dan meminta Copilot menyusun memo remediasi untuk regulator."},
             {'tool': 'T_PPT', 'persona': 'Daichi Maruyama',
              'verb': f"Convert the Word memo into a 10-slide Board pack",
              'verbID': f"Ubah memo Word menjadi paket Direksi 10 slide",
              'desc': f"Daichi opens PowerPoint and asks Copilot to convert the Word remediation memo into a 10-slide Board pack covering {c['recovery_focus_en']}.",
              'descID': f"Daichi membuka PowerPoint dan meminta Copilot mengubah memo remediasi Word menjadi paket Direksi 10 slide yang mencakup {c['recovery_focus_id']}."},
             {'tool': 'T_OUTLOOK', 'persona': 'Mod Admin',
              'verb': f"Draft the CEO's Outlook brief to regulators",
              'verbID': f"Susun brief Outlook Direktur Utama kepada regulator",
              'desc': f"Mod ({re_en['coo']}) drafts the {re_en['ceo']}'s Outlook brief to {c['regulators_en']} contacts using the Word memo and PowerPoint pack as grounding.",
              'descID': f"Mod ({re_id['coo']}) menyusun brief Outlook {re_id['ceo']} kepada kontak {c['regulators_id']} dengan grounding pada memo Word dan paket PowerPoint."},
         ]},
        {'id': 'ex4', 'title': 'Exercise 4 — Coordinate & Scale',
         'titleID': 'Latihan 4 — Koordinasi & Skalakan',
         'objective': f"Coordinate the executive response in Teams, run a parallel Copilot agent and stand up the {c['agent_name']} so {c['recovery_focus_en']} stays on track.",
         'objectiveID': f"Koordinasikan respons eksekutif di Teams, jalankan agen Copilot paralel dan bangun {c['agent_name_id']} agar {c['recovery_focus_id']} tetap on-track.",
         'tasks': [
             {'tool': 'T_TEAMS', 'persona': 'Mod Admin',
              'verb': f"Extract decisions and risks from last week's Teams meeting recaps",
              'verbID': f"Ekstrak keputusan dan risiko dari recap rapat Teams minggu lalu",
              'desc': f"Mod opens the recap of last week's New Software Implementation, Marketing Campaign Performance Review and Negotiating Marketing Contract meetings in Teams calendar and uses Copilot to extract decisions and risks affecting {c['crisis_short_en']}.",
              'descID': f"Mod membuka recap rapat New Software Implementation, Marketing Campaign Performance Review dan Negotiating Marketing Contract minggu lalu di kalender Teams dan menggunakan Copilot untuk mengekstrak keputusan dan risiko yang memengaruhi {c['crisis_short_id']}."},
             {'tool': 'T_COWORK', 'persona': 'Mod Admin',
              'verb': f"Delegate five parallel tasks to Copilot Coworker (Frontier)",
              'verbID': f"Delegasikan lima tugas paralel ke Copilot Coworker (Frontier)",
              'desc': f"Mod runs Copilot in Coworker (Frontier) mode to draft two Word documents, one Outlook email, schedule one Teams meeting and post one Teams chat in parallel — all aligned to {c['recovery_focus_en']}.",
              'descID': f"Mod menjalankan Copilot dalam mode Coworker (Frontier) untuk menyusun dua dokumen Word, satu email Outlook, menjadwalkan satu rapat Teams dan memposting satu chat Teams secara paralel — seluruhnya selaras dengan {c['recovery_focus_id']}."},
             {'tool': 'T_BUILDER', 'persona': 'Daichi Maruyama',
              'verb': f"Build the {c['agent_name']} end-to-end from m365.cloud.microsoft/chat",
              'verbID': f"Bangun {c['agent_name_id']} end-to-end dari m365.cloud.microsoft/chat",
              'desc': f"Daichi opens m365.cloud.microsoft/chat and pastes the {c['agent_name']} description into Copilot so the agent is built end-to-end without leaving chat.",
              'descID': f"Daichi membuka m365.cloud.microsoft/chat dan menempelkan deskripsi {c['agent_name_id']} ke Copilot agar agen dibangun end-to-end tanpa meninggalkan chat."},
         ]},
    ]



# ───────────────────────── _BUILD: emits one ind() per industry ─────────────────────────
def _build(c):
    re_en = c['roles_en']
    re_id = c['roles_id']
    files = c['files']

    # 1. T_CHAT — 3 prompts each
    chat_en = [
        f"You are advising the {re_en['cfo']} of {c['co']}. Summarise in 6 bullets the FY2025 operating gap implied by {c['kpi_phrase_en']}, and flag the three risks {re_en['ceo']} must address before {c['event_en']}.",
        f"From the perspective of the {re_en['cos']}, draft 8 questions {re_en['ceo']} should put to {re_en['coo']} and {re_en['hsa']} on {c['recovery_focus_en']}, ranked by urgency.",
        f"Compare two scenarios for {c['co']} over the next 12 months — (a) accelerated remediation on {c['topic_short_en']} or (b) staged remediation. Output a 2-column table with capex, regulator exposure and Board defensibility.",
    ]
    chat_id = [
        f"Anda menasihati {re_id['cfo']} {c['co_id']}. Ringkas dalam 6 bullet selisih operasi FY2025 yang tersirat dari {c['kpi_phrase_id']}, dan tandai tiga risiko yang harus ditangani {re_id['ceo']} sebelum {c['event_id']}.",
        f"Dari sudut pandang {re_id['cos']}, susun 8 pertanyaan yang harus diajukan {re_id['ceo']} kepada {re_id['coo']} dan {re_id['hsa']} mengenai {c['recovery_focus_id']}, diurutkan berdasarkan urgensi.",
        f"Bandingkan dua skenario untuk {c['co_id']} dalam 12 bulan ke depan — (a) remediasi dipercepat pada {c['topic_short_id']} atau (b) remediasi bertahap. Keluarkan tabel 2 kolom dengan capex, eksposur regulator dan ketahanan terhadap Direksi.",
    ]
    chat_personas = ['Sasha Ouellet', 'Sasha Ouellet', 'Sasha Ouellet']
    t1 = tool(T_CHAT, FREE_LIC, FREE_ACCT, chat_en, DESC_CHAT,
              promptsID=chat_id, persona=chat_personas, personaID=chat_personas)

    # 2. T_RESEARCHER — 2 prompts (Critique + Model Council)
    res_en = [
        f"🔍 CRITIQUE MODE. You are a sceptical Asia-Pacific analyst reading the FY2025 board narrative for {c['co']}. Stress-test the claims around {c['kpi_phrase_en']}. Identify the three weakest assumptions, name the missing benchmarks, and propose a defensible counter-narrative for {re_en['ceo']} to use at the {c['event_en']}.",
        f"⚖️ MODEL COUNCIL MODE. Convene a panel of three peer companies in {c['name']} across Asia-Pacific. For each peer, summarise how they responded to a similar {c['crisis_short_en']} situation, what worked, what failed, and what {c['co']} should adopt or avoid.",
    ]
    res_id = [
        f"🔍 MODE CRITIQUE. Anda adalah analis Asia-Pasifik yang skeptis membaca narasi Direksi FY2025 untuk {c['co_id']}. Uji-tekan klaim seputar {c['kpi_phrase_id']}. Identifikasi tiga asumsi terlemah, sebutkan benchmark yang hilang, dan ajukan narasi tandingan yang dapat dipertahankan untuk digunakan {re_id['ceo']} pada {c['event_id']}.",
        f"⚖️ MODE MODEL COUNCIL. Kumpulkan panel tiga perusahaan peer di {c['name']} di Asia-Pasifik. Untuk setiap peer, ringkas bagaimana mereka merespons situasi {c['crisis_short_id']} serupa, apa yang berhasil, apa yang gagal, dan apa yang harus diadopsi atau dihindari {c['co_id']}.",
    ]
    res_personas = ['Hadar Caspit', 'Hadar Caspit']
    t2 = tool(T_RESEARCHER, M365_LIC, M365_ACCT, res_en, DESC_RESEARCHER,
              promptsID=res_id, persona=res_personas, personaID=res_personas)

    # 3. T_ANALYST — 3 prompts
    ana_en = [
        f"From Copilot Chat with /file {files[0]} and /file {files[3]}, run Analyst to isolate the top five drivers behind {c['kpi_phrase_en']}. Output a ranked table with driver, magnitude, and proposed owner.",
        f"From Copilot Chat with /file {files[0]} and /file {files[4]}, ask Analyst to build a weekly timeline of {c['ana_timeline_event_en']} that explain the FY2025 deterioration, and tag each event as recoverable, structural or external.",
        f"From Copilot Chat with /file {files[3]} and /file {files[4]}, ask Analyst to model the financial impact of three recovery levers on {c['recovery_focus_en']} and rank them by NPV.",
    ]
    ana_id = [
        f"Dari Copilot Chat dengan /file {files[0]} dan /file {files[3]}, jalankan Analyst untuk mengisolasi lima pendorong utama di balik {c['kpi_phrase_id']}. Keluarkan tabel berperingkat dengan pendorong, besaran, dan pemilik yang diusulkan.",
        f"Dari Copilot Chat dengan /file {files[0]} dan /file {files[4]}, minta Analyst membangun timeline mingguan {c['ana_timeline_event_id']} yang menjelaskan kemerosotan FY2025, dan tandai setiap kejadian sebagai dapat dipulihkan, struktural atau eksternal.",
        f"Dari Copilot Chat dengan /file {files[3]} dan /file {files[4]}, minta Analyst memodelkan dampak finansial tiga lever pemulihan pada {c['recovery_focus_id']} dan urutkan berdasarkan NPV.",
    ]
    ana_personas = ['Hadar Caspit', 'Hadar Caspit', 'Hadar Caspit']
    t3 = tool(T_ANALYST, M365_LIC, M365_ACCT, ana_en, DESC_ANALYST,
              promptsID=ana_id, persona=ana_personas, personaID=ana_personas)

    # 4. T_EXCEL — 3 prompts (multi-tab dashboard)
    xl_en = [
        f"Open {files[0]} in Excel desktop. Ask Copilot to refresh the {c['tabs1']}, then add a new Executive Summary tab that calls out the worst-performing line, the best-performing line, and the FY2025 selisih against budget.",
        f"In {files[0]}, ask Copilot to build a conditional-formatting heatmap on the operating tabs tracking {c['xl_heatmap_metric_en']}, so any week breaching the FY2025 target is flagged red, and any week beating the prior 8-week average is flagged green.",
        f"In {files[3]}, ask Copilot to summarise {c['xl_exposure_lens_en']}, and to draft a 5-bullet narrative the {re_en['cfo']} can paste into the Board pack.",
    ]
    xl_id = [
        f"Buka {files[0]} di Excel desktop. Minta Copilot menyegarkan tab {c['tabs1']}, lalu tambahkan tab Executive Summary baru yang menonjolkan line dengan kinerja terburuk, terbaik, dan selisih FY2025 terhadap RKAP.",
        f"Di {files[0]}, minta Copilot membangun heatmap conditional-formatting pada tab operasi yang memantau {c['xl_heatmap_metric_id']}, sehingga setiap minggu yang melanggar target FY2025 ditandai merah, dan setiap minggu yang melampaui rata-rata 8 minggu sebelumnya ditandai hijau.",
        f"Di {files[3]}, minta Copilot meringkas {c['xl_exposure_lens_id']}, dan menyusun narasi 5 bullet yang dapat ditempelkan {re_id['cfo']} ke paket Direksi.",
    ]
    xl_personas = ['Hadar Caspit', 'Hadar Caspit', 'Hadar Caspit']
    t4 = tool(T_EXCEL, M365_LIC, M365_ACCT, xl_en, DESC_EXCEL,
              promptsID=xl_id, persona=xl_personas, personaID=xl_personas)

    # 5. T_WORD — 3 prompts
    w_en = [
        f"Open {files[1]} in Word desktop. Ask Copilot to draft a 3-page regulator-facing remediation memo aligned with {c['regulators_en']}, opening with the FY2025 selisih, then root cause, then committed actions and milestones.",
        f"In {files[1]}, ask Copilot to add a section on {c['recovery_focus_en']} with a 12-week milestone table, and rewrite the executive summary in plain Bahasa-friendly English suitable for both Board and regulator audiences.",
        f"In {files[2]}, ask Copilot to refresh the maintenance/asset narrative against the FY2025 operating gap and produce a 1-page CEO talking-point appendix that ties to {c['kpi_phrase_en']}.",
    ]
    w_id = [
        f"Buka {files[1]} di Word desktop. Minta Copilot menyusun memo remediasi 3 halaman untuk regulator yang selaras dengan {c['regulators_id']}, dibuka dengan selisih FY2025, lalu akar masalah, kemudian tindakan dan milestone yang dikomitmenkan.",
        f"Di {files[1]}, minta Copilot menambahkan bagian tentang {c['recovery_focus_id']} dengan tabel milestone 12 minggu, dan menulis ulang executive summary dalam Bahasa Indonesia yang ramah baik untuk Direksi maupun regulator.",
        f"Di {files[2]}, minta Copilot menyegarkan narasi maintenance/aset terhadap gap operasi FY2025 dan menghasilkan apendiks talking-point 1 halaman untuk Direktur Utama yang terkait dengan {c['kpi_phrase_id']}.",
    ]
    w_personas = ['Daichi Maruyama', 'Daichi Maruyama', 'Daichi Maruyama']
    t5 = tool(T_WORD, M365_LIC, M365_ACCT, w_en, DESC_WORD,
              promptsID=w_id, persona=w_personas, personaID=w_personas)

    # 6. T_PPT — 3 prompts
    p_en = [
        f"Open PowerPoint and create a new deck. Ask Copilot to convert {files[1]} into a 10-slide Board pack covering the FY2025 selisih, {c['recovery_focus_en']}, regulator engagement and {c['event_en']} ask.",
        f"In the same deck, ask Copilot to add a {c['ppt_scenario_label_en']}, populated from {files[0]} and {files[3]}.",
        f"In the same deck, ask Copilot to redesign the title slide with the executive headline 'FY2025 reset for {c['co']}' and apply a consistent corporate look across all slides.",
    ]
    p_id = [
        f"Buka PowerPoint dan buat deck baru. Minta Copilot mengubah {files[1]} menjadi paket Direksi 10 slide yang mencakup selisih FY2025, {c['recovery_focus_id']}, engagement regulator dan permintaan {c['event_id']}.",
        f"Pada deck yang sama, minta Copilot menambahkan {c['ppt_scenario_label_id']}, diisi dari {files[0]} dan {files[3]}.",
        f"Pada deck yang sama, minta Copilot mendesain ulang slide judul dengan headline eksekutif 'Reset FY2025 untuk {c['co_id']}' dan menerapkan tampilan korporat yang konsisten di seluruh slide.",
    ]
    p_personas = ['Daichi Maruyama', 'Daichi Maruyama', 'Daichi Maruyama']
    t6 = tool(T_PPT, M365_LIC, M365_ACCT, p_en, DESC_PPT,
              promptsID=p_id, persona=p_personas, personaID=p_personas)

    # 7. T_OUTLOOK — 3 prompts
    o_en = [
        f"Open Outlook web. Ask Copilot to draft an email from the {re_en['ceo']} of {c['co']} to {c['regulators_en']} contacts, opening with acknowledgement of the FY2025 selisih, then committed remediation, grounded on {files[1]} and {files[5]}.",
        f"In Outlook, ask Copilot to summarise the unread thread on {c['crisis_short_en']} and propose a draft reply that defers the regulator meeting by one week without weakening the {c['co']} position.",
        f"In Outlook, ask Copilot to write a short internal note from the {re_en['cfo']} to executive leadership setting context for {c['event_en']} and listing the three pre-reads.",
    ]
    o_id = [
        f"Buka Outlook web. Minta Copilot menyusun email dari {re_id['ceo']} {c['co_id']} kepada kontak {c['regulators_id']}, dibuka dengan pengakuan atas selisih FY2025, lalu remediasi yang dikomitmenkan, berdasarkan {files[1]} dan {files[5]}.",
        f"Di Outlook, minta Copilot meringkas thread yang belum dibaca tentang {c['crisis_short_id']} dan mengusulkan draft balasan yang menunda rapat regulator selama satu minggu tanpa memperlemah posisi {c['co_id']}.",
        f"Di Outlook, minta Copilot menulis nota internal singkat dari {re_id['cfo']} kepada direksi eksekutif untuk memberi konteks {c['event_id']} dan mencantumkan tiga pre-read.",
    ]
    o_personas = ['Mod Admin', 'Mod Admin', 'Mod Admin']
    t7 = tool(T_OUTLOOK, M365_LIC, M365_ACCT, o_en, DESC_OUTLOOK,
              promptsID=o_id, persona=o_personas, personaID=o_personas)

    # 8. T_TEAMS — 3 prompts (3 of 4 fixed titles, no "Export")
    tm_en = [
        f"Open the New Software Implementation meeting in Teams calendar — Recap opens. Click the Copilot icon at top right — the Copilot pane opens grounded in the transcript. Type: \"List the three decisions and two risks from this meeting that affect {c['crisis_short_en']}, and the owners.\" Copy the result into the Word remediation memo.",
        f"Open the Marketing Campaign Performance Review meeting in Teams calendar — Recap opens. Click the Copilot icon at top right — the Copilot pane opens grounded in the transcript. Type: \"Summarise the customer signals and competitor moves that change the {c['recovery_focus_en']} priorities.\" Copy the result into the Outlook brief to {re_en['ceo']}.",
        f"Open the Negotiating Marketing Contract meeting in Teams calendar — Recap opens. Click the Copilot icon at top right — the Copilot pane opens grounded in the transcript. Type: \"Identify the contractual concessions discussed and how they shift exposure relative to {c['kpi_phrase_en']}.\" Copy the result into the Word memo annex.",
    ]
    tm_id = [
        f"Buka rapat New Software Implementation di kalender Teams — Recap terbuka. Klik ikon Copilot di kanan atas — pane Copilot terbuka dengan grounding pada transkrip. Ketik: \"Sebutkan tiga keputusan dan dua risiko dari rapat ini yang memengaruhi {c['crisis_short_id']}, beserta pemiliknya.\" Salin hasilnya ke memo remediasi Word.",
        f"Buka rapat Marketing Campaign Performance Review di kalender Teams — Recap terbuka. Klik ikon Copilot di kanan atas — pane Copilot terbuka dengan grounding pada transkrip. Ketik: \"Ringkas sinyal pelanggan dan pergerakan kompetitor yang mengubah prioritas {c['recovery_focus_id']}.\" Salin hasilnya ke brief Outlook untuk {re_id['ceo']}.",
        f"Buka rapat Negotiating Marketing Contract di kalender Teams — Recap terbuka. Klik ikon Copilot di kanan atas — pane Copilot terbuka dengan grounding pada transkrip. Ketik: \"Identifikasi konsesi kontrak yang dibahas dan bagaimana hal itu menggeser eksposur relatif terhadap {c['kpi_phrase_id']}.\" Salin hasilnya ke lampiran memo Word.",
    ]
    tm_personas = ['Mod Admin', 'Mod Admin', 'Mod Admin']
    t8 = tool(T_TEAMS, M365_LIC, M365_ACCT, 
      [
        {'instr':"**(1) In Teams**, open **Calendar** → click the past meeting **\"New Software Implementation\"**. On the Recap page, walk the audience through the **AI Notes** (auto-summary), the **Custom summary** (Copilot's per-attendee view), and the **Audio recap** (chapter markers with speaker timings). **(2) In Word for the Web**, open a **new blank document**. Type a minutes template at the top — five empty headings: Date and Attendees · Agenda Items · Decisions Taken · Action Items · Risks and Open Questions. **(3) Click the Copilot icon** in the Word ribbon and paste the prompt below — Copilot in Word will reference the meeting recap by name with `/` and fill the template.", 'prompt':"Create meeting minutes for the Teams meeting /New Software Implementation. Use the empty template already on this page and fill each heading from the meeting recap. Sections: (1) Date and Attendees; (2) Agenda Items; (3) Decisions Taken; (4) Action Items with Owner and Due Date; (5) Risks and Open Questions. Quote attendee statements verbatim where the wording matters. Tag any decision that is on the critical path as Critical Path."},
        {'instr':'**(1) In Teams**, open **Calendar** → click the past meeting **"Marketing Campaign Performance Review"**. On the Recap page, walk through the **AI Notes**, the **Custom summary**, and the **Audio recap** chapters. **(2) In Word for the Web**, open a **new blank document**. Type a campaign-review minutes template at the top — six empty headings: Date and Attendees · Campaign KPIs Reviewed · Decisions Taken · Action Items · Budget Reallocations · Next Review Date. **(3) Click the Copilot icon** in the Word ribbon and paste the prompt below.', 'prompt':"Create meeting minutes for the Teams meeting /Marketing Campaign Performance Review. Use the empty campaign-review template already on this page. Sections: (1) Date and Attendees; (2) Campaign KPIs Reviewed; (3) Decisions Taken; (4) Action Items with Owner and Due Date; (5) Budget Reallocations Approved; (6) Next Review Date. Quote attendee statements verbatim where the wording matters. Highlight any KPI that missed target by more than 10% in amber."},
        {'instr':'**(1) In Teams**, open **Calendar** → click the past meeting **"Negotiating Marketing Contract"**. On the Recap page, walk through the **AI Notes**, the **Custom summary**, and the **Audio recap**. **(2) In Word for the Web**, open a **new blank document**. Type a vendor-negotiation minutes template at the top — seven empty headings: Vendor and Owner · Commercial Terms Discussed · Concessions Offered · Concessions Accepted · Open Items · Approval Thresholds · Next Steps. **(3) Click the Copilot icon** in the Word ribbon and paste the prompt below — then forward the result to Procurement, Legal, and the Group CFO.', 'prompt':"Create meeting minutes for the Teams meeting /Negotiating Marketing Contract. Use the empty vendor-negotiation template already on this page. Sections: (1) Vendor and Owner; (2) Commercial Terms Discussed; (3) Concessions Offered; (4) Concessions Accepted; (5) Open Items; (6) Approval Thresholds (CFO / Board); (7) Next Steps with Owner and Due Date. Highlight any term requiring CFO sign-off in amber and any term requiring Board sign-off in red.. Email the link to Procurement, Legal, and the Group CFO."}
      ], DESC_TEAMS,
      promptsID=[
        {'instr':'**(1) Di Teams**, buka **Calendar** → klik rapat **"New Software Implementation"**. Di halaman Recap, jelaskan ke peserta tentang **AI Notes** (ringkasan otomatis), **Custom summary** (tampilan per-peserta dari Copilot), dan **Audio recap** (penanda bab dengan timing pembicara). **(2) Di Word for the Web**, buka **dokumen kosong baru**. Ketik kerangka notulen di bagian atas — lima heading kosong: Tanggal dan Peserta · Agenda · Keputusan · Action Items · Risiko dan Pertanyaan Terbuka. **(3) Klik ikon Copilot** di ribbon Word lalu tempelkan prompt di bawah — Copilot in Word akan merujuk recap rapat dengan `/` dan mengisi template.', 'prompt':"Susun notulen rapat untuk rapat Teams /New Software Implementation. Gunakan template kosong yang sudah ada di halaman ini dan isi tiap heading dari recap rapat. Bagian: (1) Tanggal dan Peserta; (2) Agenda; (3) Keputusan; (4) Action Items dengan Owner dan Due Date; (5) Risiko dan Pertanyaan Terbuka. Kutip pernyataan peserta apa adanya bila kata-katanya penting. Tandai keputusan di jalur kritis sebagai Critical Path."},
        {'instr':'**(1) Di Teams**, buka **Calendar** → klik rapat **"Marketing Campaign Performance Review"**. Di halaman Recap, jelaskan **AI Notes**, **Custom summary**, dan **Audio recap**. **(2) Di Word for the Web**, buka dokumen kosong baru. Ketik kerangka notulen tinjauan kampanye — enam heading kosong: Tanggal dan Peserta · KPI Kampanye yang Dikaji · Keputusan · Action Items · Realokasi Anggaran · Jadwal Tinjauan Berikutnya. **(3) Klik ikon Copilot** di ribbon Word lalu tempelkan prompt di bawah.', 'prompt':"Susun notulen rapat untuk rapat Teams /Marketing Campaign Performance Review. Gunakan template kosong tinjauan kampanye yang sudah ada. Bagian: (1) Tanggal dan Peserta; (2) KPI Kampanye yang Dikaji; (3) Keputusan; (4) Action Items dengan Owner dan Due Date; (5) Realokasi Anggaran yang Disetujui; (6) Jadwal Tinjauan Berikutnya. Kutip pernyataan peserta apa adanya. Tandai KPI yang meleset >10% dengan amber."},
        {'instr':'**(1) Di Teams**, buka **Calendar** → klik rapat **"Negotiating Marketing Contract"**. Di halaman Recap, jelaskan **AI Notes**, **Custom summary**, dan **Audio recap**. **(2) Di Word for the Web**, buka dokumen kosong baru. Ketik kerangka notulen negosiasi vendor — tujuh heading kosong: Vendor dan Owner · Term Komersial · Konsesi yang Ditawarkan · Konsesi yang Diterima · Item Terbuka · Threshold Persetujuan · Langkah Berikutnya. **(3) Klik ikon Copilot** di ribbon Word lalu tempelkan prompt di bawah — kemudian teruskan hasilnya ke Procurement, Legal, dan Direktur Keuangan Grup.', 'prompt':"Susun notulen rapat untuk rapat Teams /Negotiating Marketing Contract. Gunakan template kosong negosiasi vendor yang sudah ada. Bagian: (1) Vendor dan Owner; (2) Term Komersial; (3) Konsesi yang Ditawarkan; (4) Konsesi yang Diterima; (5) Item Terbuka; (6) Threshold Persetujuan (CFO / Direksi); (7) Langkah Berikutnya dengan Owner dan Due Date. Tandai term yang memerlukan persetujuan CFO dengan amber dan persetujuan Direksi dengan merah.. Lalu email link-nya ke Procurement, Legal, dan Direktur Keuangan Grup."}
      ],
      promptsBM=[
        {'instr':'**(1) Di Teams**, buka **Calendar** → klik mesyuarat **"New Software Implementation"**. Pada halaman Recap, terangkan kepada hadirin tentang **AI Notes** (ringkasan automatik), **Custom summary** (paparan per-hadirin dari Copilot), dan **Audio recap** (penanda bab dengan masa pembicara). **(2) Di Word for the Web**, buka **dokumen kosong baharu**. Taip rangka minit di bahagian atas — lima tajuk kosong: Tarikh dan Hadirin · Agenda · Keputusan · Tindakan · Risiko dan Soalan Terbuka. **(3) Klik ikon Copilot** di ribbon Word dan tampal prompt di bawah — Copilot in Word akan merujuk recap mesyuarat dengan `/` dan mengisi templat.', 'prompt':"Hasilkan minit mesyuarat untuk mesyuarat Teams /New Software Implementation. Gunakan templat kosong yang sudah ada di halaman ini dan isi setiap tajuk daripada recap mesyuarat. Bahagian: (1) Tarikh dan Hadirin; (2) Agenda; (3) Keputusan; (4) Tindakan dengan Pemilik dan Tarikh; (5) Risiko dan Soalan Terbuka. Petik kenyataan hadirin sebagaimana asal di mana perkataannya penting. Tandakan sebarang keputusan di laluan kritikal sebagai Critical Path."},
        {'instr':'**(1) Di Teams**, buka **Calendar** → klik mesyuarat **"Marketing Campaign Performance Review"**. Pada halaman Recap, terangkan **AI Notes**, **Custom summary**, dan **Audio recap**. **(2) Di Word for the Web**, buka dokumen kosong baharu. Taip rangka minit ulasan kempen — enam tajuk kosong: Tarikh dan Hadirin · KPI Kempen yang Diulas · Keputusan · Tindakan · Pelarasan Bajet · Tarikh Ulasan Berikutnya. **(3) Klik ikon Copilot** di ribbon Word dan tampal prompt di bawah.', 'prompt':"Hasilkan minit mesyuarat untuk mesyuarat Teams /Marketing Campaign Performance Review. Gunakan templat kosong ulasan kempen yang sudah ada. Bahagian: (1) Tarikh dan Hadirin; (2) KPI Kempen yang Diulas; (3) Keputusan; (4) Tindakan dengan Pemilik dan Tarikh; (5) Pelarasan Bajet yang Diluluskan; (6) Tarikh Ulasan Berikutnya. Petik kenyataan hadirin sebagaimana asal. Tandakan KPI yang tersasar >10% dengan amber."},
        {'instr':'**(1) Di Teams**, buka **Calendar** → klik mesyuarat **"Negotiating Marketing Contract"**. Pada halaman Recap, terangkan **AI Notes**, **Custom summary**, dan **Audio recap**. **(2) Di Word for the Web**, buka dokumen kosong baharu. Taip rangka minit perundingan vendor — tujuh tajuk kosong: Vendor dan Pemilik · Terma Komersial · Konsesi Ditawarkan · Konsesi Diterima · Item Terbuka · Ambang Kelulusan · Langkah Seterusnya. **(3) Klik ikon Copilot** di ribbon Word dan tampal prompt di bawah — kemudian majukan hasilnya kepada Procurement, Legal dan Pengarah Kewangan Kumpulan.', 'prompt':"Hasilkan minit mesyuarat untuk mesyuarat Teams /Negotiating Marketing Contract. Gunakan templat kosong perundingan vendor yang sudah ada. Bahagian: (1) Vendor dan Pemilik; (2) Terma Komersial; (3) Konsesi Ditawarkan; (4) Konsesi Diterima; (5) Item Terbuka; (6) Ambang Kelulusan (CFO / Lembaga); (7) Langkah Seterusnya dengan Pemilik dan Tarikh. Tandakan terma yang memerlukan kelulusan CFO dengan amber dan Lembaga dengan merah.. Kemudian e-mel pautan kepada Procurement, Legal dan Pengarah Kewangan Kumpulan."}
      ],
      persona=tm_personas,
      personaID=tm_personas
    )

    # 9. T_NOTEBOOK — 3 prompts
    nb_en = [
        f"Create a new Copilot Notebook called '{c['agent_name']} Workbench'. Pin {files[0]}, {files[1]}, {files[3]} and {files[4]} as sources. Ask Copilot for a 6-bullet executive briefing on {c['kpi_phrase_en']}.",
        f"In the same Notebook, ask Copilot to generate a 12-minute audio overview that {re_en['ceo']} can listen to before {c['event_en']}, structured by FY2025 selisih, root cause, recovery and regulator narrative.",
        f"In the same Notebook, ask Copilot to surface contradictions across the four pinned sources and list the five biggest reconciliation items the {re_en['cfo']} must close before {c['event_en']}.",
    ]
    nb_id = [
        f"Buat Copilot Notebook baru bernama '{c['agent_name_id']} Workbench'. Sematkan {files[0]}, {files[1]}, {files[3]} dan {files[4]} sebagai sumber. Minta Copilot membuat briefing eksekutif 6 bullet mengenai {c['kpi_phrase_id']}.",
        f"Pada Notebook yang sama, minta Copilot menghasilkan audio overview 12 menit yang dapat didengarkan {re_id['ceo']} sebelum {c['event_id']}, terstruktur berdasarkan selisih FY2025, akar masalah, pemulihan dan narasi regulator.",
        f"Pada Notebook yang sama, minta Copilot memunculkan kontradiksi di antara empat sumber yang disematkan dan mencantumkan lima item rekonsiliasi terbesar yang harus diselesaikan {re_id['cfo']} sebelum {c['event_id']}.",
    ]
    nb_personas = ['Hadar Caspit', 'Hadar Caspit', 'Hadar Caspit']
    t9 = tool(T_NOTEBOOK, M365_LIC, M365_ACCT, nb_en, DESC_NOTEBOOK,
              promptsID=nb_id, persona=nb_personas, personaID=nb_personas)

    # 10. T_COWORK — 2 prompts (each fans out to 5 parallel sub-tasks), FRONTIER_LIC + M365_ACCT
    cw_en = [
        f"From Copilot Chat, run Coworker mode in parallel: (1) draft a Word remediation memo for {c['regulators_en']} grounded on {files[1]} and {files[5]}; (2) draft a second Word brief for the {re_en['ceo']} grounded on {files[2]}; (3) send an Outlook email to {re_en['cfo']} attaching both Word drafts; (4) schedule a Teams meeting titled 'FY2025 reset — {c['co']}' for the executive team within the next 5 business days; (5) post a Teams chat to the {c['recovery_focus_en']} group summarising all four artefacts. Use these named recipients consistently across the email task and the Teams meeting task — Hadar (Group CFO), Sasha (Group Chief of Staff), Daichi (Head of Investor Relations), Sonia (Head of Strategy), Will (Head of Risk) and Omar (Head of Procurement) — and adapt the precise distribution per sub-task to keep each communication focused on the right audience.",
        f"From Copilot Chat, run Coworker mode in parallel for the {c['event_en']} prep: (1) draft a Word executive summary tying {c['kpi_phrase_en']} to {c['recovery_focus_en']}; (2) draft a second Word annex on regulator engagement with {c['regulators_en']}; (3) send an Outlook email to {re_en['hsa']} requesting HSE/operational sign-off; (4) schedule a Teams meeting titled 'Pre-Board war room' for {re_en['coo']} and {re_en['hsa']}; (5) post a Teams chat to executive leadership confirming the four artefacts are ready. Use these named recipients consistently across the email task and the Teams meeting task — Hadar (Group CFO), Sasha (Group Chief of Staff), Daichi (Head of Investor Relations), Sonia (Head of Strategy), Will (Head of Risk) and Omar (Head of Procurement) — and adapt the precise distribution per sub-task to keep each communication focused on the right audience.",
    ]
    cw_id = [
        f"Dari Copilot Chat, jalankan mode Coworker secara paralel: (1) susun memo remediasi Word untuk {c['regulators_id']} berdasarkan {files[1]} dan {files[5]}; (2) susun brief Word kedua untuk {re_id['ceo']} berdasarkan {files[2]}; (3) kirim email Outlook ke {re_id['cfo']} dengan melampirkan kedua draft Word; (4) jadwalkan rapat Teams berjudul 'Reset FY2025 — {c['co_id']}' untuk tim eksekutif dalam 5 hari kerja ke depan; (5) posting chat Teams ke grup {c['recovery_focus_id']} yang meringkas keempat artefak. Gunakan penerima bernama berikut secara konsisten lintas tugas email dan tugas rapat Teams — Hadar (Direktur Keuangan Grup), Sasha (Kepala Staf Grup), Daichi (Kepala Hubungan Investor), Sonia (Kepala Strategi), Will (Kepala Risiko) dan Omar (Kepala Pengadaan) — dan sesuaikan distribusi tepat per sub-tugas agar tiap komunikasi tetap fokus pada audiens yang tepat.",
        f"Dari Copilot Chat, jalankan mode Coworker secara paralel untuk persiapan {c['event_id']}: (1) susun executive summary Word yang mengaitkan {c['kpi_phrase_id']} dengan {c['recovery_focus_id']}; (2) susun lampiran Word kedua tentang engagement regulator dengan {c['regulators_id']}; (3) kirim email Outlook ke {re_id['hsa']} untuk meminta sign-off HSE/operasi; (4) jadwalkan rapat Teams berjudul 'War room pra-Direksi' untuk {re_id['coo']} dan {re_id['hsa']}; (5) posting chat Teams ke direksi eksekutif yang mengonfirmasi keempat artefak sudah siap. Gunakan penerima bernama berikut secara konsisten lintas tugas email dan tugas rapat Teams — Hadar (Direktur Keuangan Grup), Sasha (Kepala Staf Grup), Daichi (Kepala Hubungan Investor), Sonia (Kepala Strategi), Will (Kepala Risiko) dan Omar (Kepala Pengadaan) — dan sesuaikan distribusi tepat per sub-tugas agar tiap komunikasi tetap fokus pada audiens yang tepat.",
    ]
    cw_personas = ['Mod Admin', 'Mod Admin']
    t10 = tool(T_COWORK, FRONTIER_LIC, M365_ACCT, cw_en, DESC_COWORK,
               promptsID=cw_id, persona=cw_personas, personaID=cw_personas)

    # 11. T_WORD_AGT — 2 prompts 
    wa_en = [
        f"From Microsoft 365 Copilot Chat (m365.cloud.microsoft/chat) — type: \"Draft a 4-page Word memo from the {re_en['cfo']} of {c['co']} to the Board on the FY2025 selisih and {c['recovery_focus_en']}, grounded on /file {files[1]} and /file {files[2]}, and save the file to my OneDrive.\"",
        f"From Microsoft 365 Copilot Chat (m365.cloud.microsoft/chat) — type: \"Draft a 2-page Word talking-point pack for {re_en['ceo']} of {c['co']} ahead of {c['event_en']} grounded on /file {files[5]}, and save the file to my OneDrive.\"",
    ]
    wa_id = [
        f"Dari Microsoft 365 Copilot Chat (m365.cloud.microsoft/chat) — di kotak prompt klik menu Tools (atau Agents) lalu pilih Word — ketik: \"Susun memo Word 4 halaman dari {re_id['cfo']} {c['co_id']} kepada Direksi mengenai selisih FY2025 dan {c['recovery_focus_id']}, berdasarkan /file {files[1]} dan /file {files[2]}, dan simpan file ke OneDrive saya.\"",
        f"Dari Microsoft 365 Copilot Chat (m365.cloud.microsoft/chat) — di kotak prompt klik menu Tools (atau Agents) lalu pilih Word — ketik: \"Susun paket talking-point Word 2 halaman untuk {re_id['ceo']} {c['co_id']} menjelang {c['event_id']} berdasarkan /file {files[5]}, dan simpan file ke OneDrive saya.\"",
    ]
    wa_personas = ['Daichi Maruyama', 'Daichi Maruyama']
    t11 = tool(T_WORD_AGT, ANY_LIC, ANY_ACCT, wa_en, DESC_WORD_AGT,
               promptsID=wa_id, persona=wa_personas, personaID=wa_personas)

    # 12. T_PPT_AGT — 2 prompts 
    pa_en = [
        f"From Microsoft 365 Copilot Chat (m365.cloud.microsoft/chat) — type: \"Build a 12-slide PowerPoint Board pack for {c['co']} on the FY2025 reset, grounded on /file {files[1]} and /file {files[0]}, covering {c['recovery_focus_en']}, and save the file to my OneDrive.\"",
        f"From Microsoft 365 Copilot Chat (m365.cloud.microsoft/chat) — type: \"Build a 6-slide regulator pack for {c['co']} aligned with {c['regulators_en']}, grounded on /file {files[5]} and /file {files[4]}, and save the file to my OneDrive.\"",
    ]
    pa_id = [
        f"Dari Microsoft 365 Copilot Chat (m365.cloud.microsoft/chat) — di kotak prompt klik menu Tools (atau Agents) lalu pilih PowerPoint — ketik: \"Bangun paket Direksi PowerPoint 12 slide untuk {c['co_id']} mengenai reset FY2025, berdasarkan /file {files[1]} dan /file {files[0]}, mencakup {c['recovery_focus_id']}, dan simpan file ke OneDrive saya.\"",
        f"Dari Microsoft 365 Copilot Chat (m365.cloud.microsoft/chat) — di kotak prompt klik menu Tools (atau Agents) lalu pilih PowerPoint — ketik: \"Bangun paket regulator 6 slide untuk {c['co_id']} yang selaras dengan {c['regulators_id']}, berdasarkan /file {files[5]} dan /file {files[4]}, dan simpan file ke OneDrive saya.\"",
    ]
    pa_personas = ['Daichi Maruyama', 'Daichi Maruyama']
    t12 = tool(T_PPT_AGT, ANY_LIC, ANY_ACCT, pa_en, DESC_PPT_AGT,
               promptsID=pa_id, persona=pa_personas, personaID=pa_personas)

    # 13. T_XL_AGT — 2 prompts 
    xa_en = [
        f"From Microsoft 365 Copilot Chat (m365.cloud.microsoft/chat) — type: \"Build a new Excel workbook called 'FY2025 Reset Bridge — {c['co']}' with three tabs: FY2025 Bridge, Recovery Levers, Regulator Asks, grounded on /file {files[0]} and /file {files[3]}, and save the file to my OneDrive.\"",
        f"From Microsoft 365 Copilot Chat (m365.cloud.microsoft/chat) — type: \"Build a new Excel workbook called 'Risk Heatmap — {c['co']}' that ranks the top 15 risks behind {c['kpi_phrase_en']} grounded on /file {files[4]} and /file {files[1]}, and save the file to my OneDrive.\"",
    ]
    xa_id = [
        f"Dari Microsoft 365 Copilot Chat (m365.cloud.microsoft/chat) — di kotak prompt klik menu Tools (atau Agents) lalu pilih Excel — ketik: \"Bangun workbook Excel baru bernama 'Bridge Reset FY2025 — {c['co_id']}' dengan tiga tab: Bridge FY2025, Lever Pemulihan, Permintaan Regulator, berdasarkan /file {files[0]} dan /file {files[3]}, dan simpan file ke OneDrive saya.\"",
        f"Dari Microsoft 365 Copilot Chat (m365.cloud.microsoft/chat) — di kotak prompt klik menu Tools (atau Agents) lalu pilih Excel — ketik: \"Bangun workbook Excel baru bernama 'Risk Heatmap — {c['co_id']}' yang memeringkat 15 risiko teratas di balik {c['kpi_phrase_id']} berdasarkan /file {files[4]} dan /file {files[1]}, dan simpan file ke OneDrive saya.\"",
    ]
    xa_personas = ['Daichi Maruyama', 'Daichi Maruyama']
    t13 = tool(T_XL_AGT, ANY_LIC, ANY_ACCT, xa_en, DESC_XL_AGT,
               promptsID=xa_id, persona=xa_personas, personaID=xa_personas)

    # 14. T_BUILDER — 2 prompts (paste-into-chat agent description with starter prompts)
    b_en = [
        (f"Open m365.cloud.microsoft/chat. Paste this as a single prompt to build the {c['agent_name']} agent end-to-end without leaving chat:\n\n"
         f"\"You are the {c['agent_name']}, a Copilot agent for {c['co']} that monitors {c['recovery_focus_en']}, drafts regulator-ready narrative aligned with {c['regulators_en']}, and surfaces the FY2025 selisih implied by {c['kpi_phrase_en']}. Ground every response on the current state of {files[0]}, {files[1]}, {files[3]}, {files[4]} and {files[5]}. Always show your sources, always quantify in MYR/USD/Rupiah, and always offer the next best action. Starter prompts: "
         f"(1) 'Brief me on this week\'s {c['crisis_short_en']} status'; "
         f"(2) 'Draft the regulator memo to {c['regulators_en']} on {c['recovery_focus_en']}'; "
         f"(3) 'Show me the top five risks behind {c['kpi_phrase_en']}'; "
         f"(4) 'Build the talking points for {re_en['ceo']} ahead of {c['event_en']}'; "
         f"(5) 'List the executive decisions still outstanding from last week\'s Teams meetings'. \""),
        (f"Open m365.cloud.microsoft/chat. Paste this as a single prompt to build the {c['agent_name']} 'Lite' regulator-only variant end-to-end without leaving chat:\n\n"
         f"\"You are the {c['agent_name']} Regulator Lite, a Copilot agent for {c['co']} focused exclusively on {c['regulators_en']} engagement on {c['topic_short_en']}. Ground every response on {files[1]} and {files[5]}. Always quote the relevant clause, always show the date the underlying figure was last refreshed, and always propose a deferral, a concession, or a counter-narrative. Starter prompts: "
         f"(1) 'Summarise outstanding regulator asks'; "
         f"(2) 'Draft a holding reply that buys 7 days'; "
         f"(3) 'Compare our position to the last two enforcement letters'; "
         f"(4) 'Build a 1-page regulator-ready narrative'; "
         f"(5) 'Flag any disclosure gap that triggers a re-filing'. \""),
    ]
    b_id = [
        (f"Buka m365.cloud.microsoft/chat. Tempelkan ini sebagai prompt tunggal untuk membangun agen {c['agent_name_id']} end-to-end tanpa meninggalkan chat:\n\n"
         f"\"Anda adalah {c['agent_name_id']}, agen Copilot untuk {c['co_id']} yang memantau {c['recovery_focus_id']}, menyusun narasi siap-regulator yang selaras dengan {c['regulators_id']}, dan memunculkan selisih FY2025 yang tersirat dari {c['kpi_phrase_id']}. Grounding setiap respons pada kondisi terkini {files[0]}, {files[1]}, {files[3]}, {files[4]} dan {files[5]}. Selalu tampilkan sumber, selalu kuantifikasi dalam MYR/USD/Rupiah, dan selalu tawarkan tindakan berikutnya yang terbaik. Prompt awal: "
         f"(1) 'Beri saya briefing status {c['crisis_short_id']} minggu ini'; "
         f"(2) 'Susun memo regulator kepada {c['regulators_id']} mengenai {c['recovery_focus_id']}'; "
         f"(3) 'Tampilkan lima risiko teratas di balik {c['kpi_phrase_id']}'; "
         f"(4) 'Bangun talking point untuk {re_id['ceo']} menjelang {c['event_id']}'; "
         f"(5) 'Cantumkan keputusan eksekutif yang masih terbuka dari rapat Teams minggu lalu'. \""),
        (f"Buka m365.cloud.microsoft/chat. Tempelkan ini sebagai prompt tunggal untuk membangun varian {c['agent_name_id']} 'Lite' khusus regulator end-to-end tanpa meninggalkan chat:\n\n"
         f"\"Anda adalah {c['agent_name_id']} Regulator Lite, agen Copilot untuk {c['co_id']} yang fokus eksklusif pada engagement {c['regulators_id']} mengenai {c['topic_short_id']}. Grounding setiap respons pada {files[1]} dan {files[5]}. Selalu kutip klausul yang relevan, selalu tampilkan tanggal angka terkait terakhir disegarkan, dan selalu usulkan penundaan, konsesi, atau narasi tandingan. Prompt awal: "
         f"(1) 'Ringkas permintaan regulator yang belum diselesaikan'; "
         f"(2) 'Susun balasan sementara yang memberi waktu 7 hari'; "
         f"(3) 'Bandingkan posisi kita dengan dua surat penegakan terakhir'; "
         f"(4) 'Bangun narasi siap-regulator 1 halaman'; "
         f"(5) 'Tandai setiap celah pengungkapan yang memicu re-filing'. \""),
    ]
    b_personas = ['Daichi Maruyama', 'Daichi Maruyama', 'Daichi Maruyama']
    _en_agents = _bcat.render_agents(c['id'], c['name'], c['files']) or []
    _id_agents = _bcat.render_agents_id(c['id'], c['name'], c['files']) or []
    _en_remap = [{'icon':a['icon'],'label':a['label'],'name':a['name'],'desc':a['description'],
                  'instructions':a['instructions'],'knowledge':a['knowledge'],
                  'knowledgeNote':a['knowledgeTest'],'queries':a['queries']} for a in _en_agents]
    _id_remap = [{'icon':a['icon'],'label':a['label'],'name':a['name'],'desc':a['description'],
                  'instructions':a['instructions'],'knowledge':a['knowledge'],
                  'knowledgeNote':a['knowledgeTest'],'queries':a['queries']} for a in _id_agents]
    t14 = tool_builder(M365_LIC, M365_ACCT,
                       agents=_en_remap, agentsID=_id_remap,
                       persona=b_personas, personaID=b_personas)

    tools = [t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14]

    return ind(c['id'], c['sector'], c['name'], c['icon'], c['color'], c['accent'],
               c['co'], c['tagline'], c['scenario'], c['files'], tools,
               companyID=c['co_id'], taglineID=c['taglineID'], scenarioID=c['scenarioID'],
               subsector='', relevantDepts=c['relevantDepts'],
               storyboard=_storyboard(c), personas=_personas(c))


INDUSTRIES_4 = [_build(OG), _build(RE), _build(MFG)]
print(f"Batch 4 written: {len(INDUSTRIES_4)} entries")
