Agent completed. agent_id: demo-extract, agent_type: research, status: completed, description: Extracting use cases from 5 demo sites, elapsed: 799s, total_turns: 0, duration: 788s

Continuing from Task 1.3 of Site 5:

---

```markdown
Ubah poin-poin dampak di atas menjadi talking points 60 detik untuk briefing lisan kepada Direktur Operasi. Sertakan 3 pertanyaan yang kemungkinan akan diajukan Direktur, dengan jawaban 1 kalimat untuk masing-masing.
```

- **Expected output:** Web-sourced regulatory brief citing JDIH/Hukumonline; 5-point impact summary; 60-second director talking points with Q&A

---

#### UC2: Legal Memo (Paid M365 Copilot)
- **Tool:** Copilot Chat (Work mode) + Word Copilot (in-app)
- **Persona:** Ratna Sari
- **Files:** 01_Contoso_Minerals_Mining_Regulation_Brief.docx, 02_Contoso_Minerals_Legal_Knowledge_Base.docx, 02_Contoso_Minerals_Legal_Memo_Template.docx

**Prompts:**

1. (Task 2.1 — Ground Copilot on Legal KB)
```
/01_Contoso_Minerals_Mining_Regulation_Brief.docx /02_Contoso_Minerals_Legal_Knowledge_Base.docx — Berdasarkan kedua dokumen ini, identifikasi 3 isu hukum paling kritis yang dihadapi anak usaha batubara Contoso Minerals di bawah Permen ESDM No. 7 Tahun 2026. Untuk setiap isu, sebutkan: (a) pasal spesifik yang terdampak, (b) referensi SOP atau kebijakan internal kita, dan (c) yurisprudensi Mahkamah Agung relevan dari Legal Knowledge Base.
```

2. (Task 2.2 — Draft full Legal Memo in Word)
```
Gunakan struktur template Legal Memo dalam dokumen ini, dan hasil analisis dari Copilot Chat tadi, untuk menyusun Legal Memo lengkap yang ditujukan kepada Direktur Utama PT Contoso Minerals (Persero). Isi seluruh 6 bagian:
I.   Latar Belakang
II.  Pertanyaan Hukum
III. Analisis Hukum (IRAC)
IV.  Kesimpulan
V.   Rekomendasi & Mitigasi Risiko
VI.  Limitasi & Disclaimer

Gunakan bahasa hukum Indonesia yang formal. Referensikan Permen ESDM 7/2026, UU 3/2020 (Minerba), PP 96/2021, PP 25/2024, serta Putusan MA No. 2447 K/Pdt/2021 bila relevan. Maksimum 1,5 halaman.
```

3. (Task 2.3 — Add risk register to memo)
```
Tambahkan tabel risk register pada Bagian V dengan kolom: Risk ID | Deskripsi Risiko | Severity (Tinggi/Sedang/Rendah) | Owner | Mitigasi | Tenggat. Sertakan minimal 6 risiko yang secara spesifik terkait dengan tenggat fasilitas gasifikasi batubara batubara, opsi tolling batubara, top-up reklamasi, pemicu MAC, pelaporan divestasi, serta kenaikan royalti.
```

- **Expected output:** Full 6-section IRAC Legal Memo addressed to Direktur Utama; 6-row risk register table

---

#### UC3: NDA Red-Flag Review (Paid M365 Copilot)
- **Tool:** Copilot Chat (Work mode) + Word Copilot + Outlook Copilot (Draft with Copilot)
- **Persona:** Ratna Sari
- **Files:** 03_Contoso_Minerals_NDA_Draft.docx, 03_Contoso_Minerals_MA_Playbook.docx

**Prompts:**

1. (Task 3.1 — Red-flag scan across two documents)
```
/03_Contoso_Minerals_NDA_Draft.docx /03_Contoso_Minerals_MA_Playbook.docx — Bandingkan NDA counterparty dengan M&A Playbook v4.0 kita. Daftarkan setiap klausul yang melanggar standar kita. Untuk setiap pelanggaran, hasilkan satu baris tabel: Klausul # | Isu | Alasan melanggar Playbook | Usulan mark-up (1–2 kalimat).
```

2. (Task 3.2 — Generate mark-up in Word)
```
Tulis ulang Klausul 3 (Jangka Waktu), 5 (Ganti Rugi/Indemnity), 6 (Hukum yang Berlaku & Penyelesaian Sengketa), 7 (Eksklusivitas), dan 9 (Pengalihan) dari NDA ini agar sepenuhnya patuh pada M&A Playbook v4.0 Contoso Minerals. Tampilkan klausul baru dalam gaya mark-up — penambahan dicetak tebal, penghapusan dicoret. Bagian lain dokumen tetap utuh. Sesuaikan dengan gaya bahasa hukum yang sudah dipakai di dokumen.
```

3. (Task 3.3 — Draft negotiation cover email in Outlook)
```
Susun email pengantar yang sopan namun tegas kepada Pacific Resources Holdings Pte. Ltd. (perihal: Tanggapan atas Draft NDA — PT Contoso Minerals × Pacific Resources). Rangkum 5 amandemen utama kita terhadap NDA mereka. Untuk setiap amandemen, berikan justifikasi 1 baris dengan referensi hukum Indonesia bila relevan (KUHPerdata Pasal 1247–1248 tentang ganti rugi; POJK 17/2020 tentang transaksi material; UU PT 40/2007). Usulkan call 30 menit dalam 5 hari kerja. Tanda tangan: Ratna Sari, VP Corporate Legal, PT Contoso Minerals (Persero). Sediakan versi Bahasa Indonesia dan English dalam satu email (BI di atas, English di bawah).
```

- **Expected output:** Red-flag table (clause # | issue | playbook violation | proposed mark-up); marked-up NDA clauses 3/5/6/7/9; bilingual negotiation cover email as Outlook draft

---

#### UC4: Litigation Analytics (Paid M365 Copilot)
- **Tool:** Excel Copilot (Edit mode + Plan mode) + Analyst Agent
- **Persona:** Ratna Sari
- **Files:** 04_Contoso_Minerals_Litigation_Cases.xlsx (50 cases, 6 subsidiaries)

**Prompts:**

1. (Task 4.1 — Profile dataset with Edit mode)
```
Profilkan sheet Litigation_Cases. Tambahkan sheet baru bernama "Summary" yang berisi: total kasus, ongoing vs closed, breakdown per Anak_Holding, breakdown per Case_Type, total exposure klaim (IDR Bn), total settlement dibayarkan (IDR Bn), dan win rate keseluruhan. Gunakan header yang rapi dan terapkan conditional formatting (hijau ≥ 60%, kuning 40–60%, merah < 40%) pada kolom win rate.
```

2. (Task 4.2 — Multi-step analytics plan with Plan mode)
```
Susun dan eksekusi workflow analitik berikut, dan konfirmasi dengan saya sebelum menjalankan setiap langkah:
1) Hitung rata-rata durasi (hari) per Case_Type dan per Forum_Level.
2) Identifikasi 5 kasus ongoing high-value teratas berdasarkan Claim_Amount_IDR_Bn.
3) Hitung win/loss rate per Anak_Holding (Menang / total closed).
4) Tandai setiap kasus dengan Duration_Days > 730 sebagai "Aging" di kolom baru.
5) Sisipkan bar chart total exposure (jumlah Claim_Amount_IDR_Bn) per Province.
```

3. (Task 4.3 — Root cause analysis with Analyst Agent)
```
Dengan menggunakan dataset litigasi, identifikasi 3 akar penyebab teratas yang memicu exposure finansial tertinggi di seluruh 6 Anak Holding. Untuk setiap akar penyebab, hitung: total claim amount, rata-rata durasi, dan rasio menang/kalah. Kemudian rekomendasikan 2 tindakan hukum preventif per akar penyebab, dengan landasan regulasi Indonesia (sitasi UU/PP/Permen).
```

- **Expected output:** Summary sheet with win-rate RAG formatting; analytics plan executed step-by-step; root-cause analysis with 6 preventive legal actions

---

#### UC5: Cowork Finale — Executive Legal Dashboard (Paid M365 Copilot)
- **Tool:** Teams Recap → Word Copilot (Task 5.1); Cowork + Researcher + Analyst Agent (Task 5.2); PowerPoint Copilot (Task 5.3)
- **Persona:** Ratna Sari
- **Files:** 05_Contoso_Minerals_Legal_Sync_Transcript.docx + all earlier files (01–04)

**Prompts:**

1. (Task 5.1 — Turn meeting transcript into formal minutes in Word)
```
Ubah rekaman rapat menjadi notulen formal: Teams Recap melakukan auto-transcribe, lalu Word mengubahnya ke template notulen profesional. Buat "Notulen Rapat Mingguan Divisi Corporate Legal" dengan: Kop Rapat, Peserta, Agenda, Ringkasan Diskusi per Topik, Keputusan, dan tabel Action Items (PIC | Tindakan | Tenggat | Status).
```

2. (Task 5.2 — Build HTML Executive Legal Dashboard via Cowork — ONE master prompt)
```
Buatkan saya "Executive Legal Dashboard" untuk Direktur Utama PT Contoso Minerals (Persero). Susun rencana langkah-langkahnya, konfirmasi dengan saya sebelum setiap langkah, lalu eksekusi:

1) Gunakan Researcher untuk menarik status terbaru Permen ESDM No. 7 Tahun 2026 dan setiap surat edaran atau keputusan dirjen terkait.
2) Gunakan Analyst agent pada /04_Contoso_Minerals_Litigation_Cases.xlsx untuk menghitung: total exposure (IDR Bn), win rate keseluruhan, 5 kasus ongoing high-value teratas, breakdown per Case_Type, dan tren 12 bulan kasus baru.
3) Dari notulen yang dihasilkan di Task 5.1 (atau langsung dari /05_Contoso_Minerals_Legal_Sync_Transcript.docx) ekstrak 7 action items terbuka beserta owner dan deadline.
4) Hasilkan satu halaman HTML self-contained berjudul "Contoso Minerals — Executive Legal Dashboard — Mei 2026". Sertakan: 4 KPI tile di atas (Total Exposure, Win Rate, Ongoing Cases, Open Actions), tabel Top-5 ongoing cases, bar chart exposure per Case_Type, panel Regulatory Watchlist dengan status Permen ESDM 7/2026, serta daftar Open Action Items. Gunakan tema korporat navy gelap + putih, font Inter/Segoe UI. Inline seluruh CSS dan SVG chart — tanpa dependensi eksternal.
5) Simpan HTML sebagai ContosoMinerals_Legal_Dashboard.html di OneDrive saya.
```

3. (Task 5.3 — Board-ready 5-slide deck from memo + dashboard)
```
Buat presentasi board-ready 5 slide berjudul "Update Hukum & Risiko — Mei 2026" untuk Direktur Utama PT Contoso Minerals (Persero), bersumber dari Legal Memo tentang Permen ESDM 7/2026 dan temuan Executive Legal Dashboard. Slide: (1) Cover dengan tanggal dan "Confidential — Board Use Only", (2) Permen ESDM 7/2026 — 3 perubahan utama dan status kepatuhan kita, (3) 5 litigasi ongoing high-value teratas dengan exposure dan forum, (4) Risiko terbesar dan usulan mitigasinya, (5) Asks dan keputusan yang dibutuhkan dari BOD. Tampilan korporat — navy + putih, Segoe UI. Tambahkan speaker notes ringkas berbahasa Indonesia di setiap slide.
```

- **Expected output:** Formal meeting minutes (notulen) from Teams transcript; self-contained HTML Executive Legal Dashboard; 5-slide board deck with speaker notes

---

#### UC6 (Bonus): Agent Builder — "Contoso Legal Counsel" Agent
- **Tool:** M365 Copilot Agent Builder (NOT Copilot Studio)
- **Persona:** Ratna Sari
- **Files:** 02_Contoso_Minerals_Legal_Knowledge_Base.docx, 02_Contoso_Minerals_Legal_Memo_Template.docx, 03_Contoso_Minerals_MA_Playbook.docx, 04_Contoso_Minerals_Litigation_Cases.xlsx

**Prompts:**

1. (Task 6.1 — Create agent via natural language description)
```
Create a new agent called "Contoso Legal Counsel".

Description: Internal legal assistant for the Corporate Legal Division of PT Contoso Minerals (Persero), grounded on Indonesian mining regulation and our internal Legal Knowledge Base.

Instructions:
- Always answer in Bahasa Indonesia unless the question is in English.
- Cite the specific UU, PP, Permen ESDM, POJK, KUHPerdata article, or Putusan Mahkamah Agung when giving legal answers.
- Use the IRAC structure (Issue–Rule–Application–Conclusion) for any legal opinion.
- If the question requires updated regulation outside the attached knowledge base, say so and recommend escalation to the VP Corporate Legal.
- Never give definitive advice on litigation strategy without flagging that internal counsel review is required.

Tone: Professional, precise, formal Indonesian legal register.
```

2. (Task 6.2 — Attach Legal Knowledge Base; no prompt — UI action to add 4 files to Knowledge tab)
> *UI step: add /02_Contoso_Minerals_Legal_Knowledge_Base.docx, /02_Contoso_Minerals_Legal_Memo_Template.docx, /03_Contoso_Minerals_MA_Playbook.docx, /04_Contoso_Minerals_Litigation_Cases.xlsx via Knowledge tab. Turn "Always cite sources" ON.*

3. (Task 6.3a — Test prompt 1)
```
Apa kewajiban divestasi saham bagi pemegang IUPK PMA berdasarkan SOP internal kita dan PP 96/2021?
```

4. (Task 6.3b — Test prompt 2)
```
Klausul apa yang termasuk auto-reject pada review NDA berdasarkan M&A Playbook v4.0? Berikan minimal 5 contoh dengan alasannya.
```

5. (Task 6.3c — Test prompt 3)
```
Berapa total exposure litigasi grup untuk kasus jenis Sengketa Pertanahan? Sebutkan top 3 kasus tertinggi beserta Anak Holding-nya, status, dan claim amount.
```

- **Expected output:** Published "Contoso Legal Counsel" agent grounded on 4 internal documents; every answer cites specific file and clause; shareable with Corporate Legal Division team in M365 Copilot

---
---

## Mapping Recommendations

### Key to Zava industry/dept IDs used below
- Industries: `retail`, `fmcg`, `hospitality-tourism`, `power-utility`, `mining-resources`, `construction-engineering`, `government-public-sector`
- Departments: `dept-strategy`, `dept-operations`, `dept-marketing`, `dept-hr`, `dept-finance`, `dept-legal`, `dept-executives`, `dept-risk-compliance`, `dept-corporate-affairs`

---

### Site 1 — Contoso Lifestyle Retail

| Use Case | Best-fit Industry | Best-fit Dept | Likely Duplicate of existing theme? | Justification |
|----------|------------------|---------------|--------------------------------------|---------------|
| UC1: Market Intelligence (Researcher) | `retail` | `dept-strategy` | **Partial duplicate** — sector scan / competitor benchmarking is a common Researcher demo | Identical structure to any "scan your industry" Researcher prompt; differentiated only by the peer list (MAP, Erajaya etc.) and Indonesian retail KPIs |
| UC2: Branded Infographic (Copilot Create) | `retail` | `dept-marketing` | **Low duplicate risk** — Copilot Create / Designer demos are rare in most demo libraries | ESG/brand one-pager for board is a strong visual showcase; retail colour palette and Indonesian market context makes it uniquely usable |
| UC3: PPT Draft & Digest | `retail` | `dept-executives` | **Likely duplicate** — BCG/McKinsey-style deck drafting is a canonical Copilot PPT demo | Action-title methodology and the Digest sub-task are high-value but the core prompt structure appears in many exec immersion kits |
| UC4: Excel Power Hour (Insights/Edit/Plan/Analyst) | `retail` | `dept-finance` | **Partial duplicate** — Excel KPI analysis exists but Edit + Plan modes are newer and less common | KPIs (SSSG, basket size, inventory turn, gross margin) are retail-specific; four-flavour structure (Insights / Edit / Plan / Analyst) is differentiated from simple pivot demos |
| UC5: Outlook + 5-min Exec Moments | `retail` | `dept-executives` | **Likely duplicate** — thread catch-up, draft reply, Teams recap are the most-used Copilot exec demos | Almost identical across all 4 GM sites; best absorbed once into `dept-executives` as a general exec productivity module |
| UC6.1: Cowork Personalised Cascade (14 letters) | `retail` | `dept-hr` | **Low duplicate** — Cowork-driven personalised mail merge (not Word Mailings) is a distinctive capability | Performance-band differentiation (Top Quartile / On Track / Watch) and Outlook-draft-only safeguard are strong differentiators from classic mail merge demos |
| UC6.2: Cowork CV Screening (SharePoint folder) | `retail` | `dept-hr` | **Low duplicate** — SharePoint-folder grounding for bulk CV screening is relatively rare | Scoring rubric (multi-store P&L, visual merchandising, shrinkage control, POS analytics, luxury brand) is retail-specific; the SharePoint-folder-at-scale capability is a strong hook |
| UC6.3: Cowork HTML Dashboard | `retail` | `dept-operations` | **Partial duplicate** — KPI dashboard via Cowork appears in some demo kits | The "5 outputs, 1 prompt" structure (analysis → Word → email → calendar → HTML) is the headline finale; HTML inline CSS dashboard output is distinctive |
| UC7: New-Store Go/No-Go Decision Pack | `retail` | `dept-strategy` | **No duplicate** — location investment decision with IRR/payback is highly industry-specific | Catchment analysis, cannibalization risk vs existing stores, brand-mix recommendation for new format — unique to retail expansion use case; high CFO/strategy relevance |

---

### Site 2 — Contoso Geothermal

| Use Case | Best-fit Industry | Best-fit Dept | Likely Duplicate? | Justification |
|----------|------------------|---------------|-------------------|---------------|
| UC1: Market Intelligence (Researcher) | `power-utility` | `dept-strategy` | **Partial duplicate** | Same Researcher template; differentiated by geothermal-specific peers (Star Energy, Pertamina Geothermal, Sarulla) and PPA/availability/ESG context |
| UC2: ESG / Board One-Pager (Copilot Create) | `power-utility` | `dept-corporate-affairs` | **Low duplicate** | ESG infographic for quarterly board pack is highly relevant for utilities and energy companies; teal brand palette and energy-transition framing distinguish it |
| UC3: PPT Draft & Digest | `power-utility` | `dept-executives` | **Likely duplicate** | Same BCG/McKinsey PPT structure; KPIs are geothermal-specific (Plant Availability, Net Generation GWh, Forced Outage Rate, Specific Steam Use) |
| UC4: Excel Power Hour | `power-utility` | `dept-operations` | **Partial duplicate** | Plant KPIs (availability %, GWh, FOR, t/MWh) and site names (Wayang Windu, Salak, Darajat) make this genuinely distinct from retail/F&B KPI demos |
| UC5: Outlook + 5-min Exec Moments | `power-utility` | `dept-executives` | **Likely duplicate** | Core prompts identical to Site 1; only persona name differs |
| UC6.1: Cowork Safety & Reliability Cascade | `power-utility` | `dept-hr` | **Low duplicate** | Safety-reminder + KPI-status + one-focus-area per recipient is operationally specific to a plant environment; HSE context differentiates from retail cascade |
| UC6.2: Cowork CV Screening | `power-utility` | `dept-hr` | **Low duplicate** | Scoring rubric (steam-turbine maintenance, vibration analysis, DCS Honeywell, API 610) is highly technical; same SharePoint-at-scale capability story |
| UC6.3: Cowork HTML Dashboard | `power-utility` | `dept-operations` | **Partial duplicate** | Dashboard title ("Plant Reliability & PPA Performance Dashboard") and KPI set are plant-specific; same 5-output Cowork structure |
| UC7: PPA Compliance + Steam-Decline Briefing | `power-utility` | `dept-operations` | **No duplicate** | Three simultaneous artefacts (PLN compliance letter, regulator Q&A pack, Board steam-decline CapEx case) — unique to geothermal PPA regulatory context; highest value add for power-utility industry in the Zava library |

---

### Site 3 — Contoso Pizza Co

| Use Case | Best-fit Industry | Best-fit Dept | Likely Duplicate? | Justification |
|----------|------------------|---------------|-------------------|---------------|
| UC1: Market Intelligence (Researcher) | `hospitality-tourism` or `fmcg` | `dept-strategy` | **Partial duplicate** | QSR peers (PHI, Domino's, McD, KFC) and delivery-economics angle make it distinct from generic sector scans |
| UC2: Campaign Infographic (Copilot Create) | `hospitality-tourism` | `dept-marketing` | **Low duplicate** | Campaign/promo infographic angle (vs ESG or board) is more marketing-forward; red brand palette and QSR delivery-economics framing |
| UC3: PPT Draft & Digest | `hospitality-tourism` | `dept-executives` | **Likely duplicate** | Same BCG/McKinsey template; KPIs are QSR-specific (SSSG, Avg Ticket, Delivery Mix, Food Cost) |
| UC4: Excel Power Hour | `hospitality-tourism` | `dept-finance` | **Partial duplicate** | Food Cost % and Delivery Mix % as KPIs are QSR-specific; useful for `fmcg` and `retail` too |
| UC5: Outlook + 5-min Exec Moments | `hospitality-tourism` | `dept-executives` | **Likely duplicate** | Identical to Sites 1 & 2; persona is Bu Lisa Hartono |
| UC6.1: Cowork Pre-Lebaran Cascade | `hospitality-tourism` | `dept-hr` | **Low duplicate** | Pre-Lebaran campaign context and outlet-delivery-mix tuning make this distinctly F&B/QSR; tone guidance (not tone-deaf to Muslim audience) is a useful cultural prompt |
| UC6.2: Cowork CV Screening | `hospitality-tourism` | `dept-hr` | **Low duplicate** | Scoring rubric (multi-outlet P&L, food-cost control, GoFood/GrabFood mix, ServSafe HACCP) is QSR-specific |
| UC6.3: Cowork HTML Dashboard | `hospitality-tourism` | `dept-operations` | **Partial duplicate** | "Outlet Performance & Delivery Mix Dashboard" — delivery-mix RAG at outlet level is useful for `fmcg` and `ecommerce-marketplace` too |
| UC7: Lebaran 2026 Promo Launch Pack | `hospitality-tourism` | `dept-marketing` | **No duplicate** — highest uniqueness score of any use case across all 5 sites | Bundle design + GoFood/GrabFood listing copy + Instagram captions + outlet ops checklist + cannibalisation forecast + 7-day launch scorecard — end-to-end campaign execution in one prompt; no analogue in standard Copilot demo libraries |

---

### Site 4 — Contoso Mining Services

| Use Case | Best-fit Industry | Best-fit Dept | Likely Duplicate? | Justification |
|----------|------------------|---------------|-------------------|---------------|
| UC1: Market Intelligence (Researcher) | `mining-resources` | `dept-strategy` | **Partial duplicate** | Mining-services peers (Petrosea, BUMA, Pamapersada, Thiess) and EPC angle give strong industry specificity |
| UC2: Tender Capability One-Pager (Copilot Create) | `mining-resources` | `dept-sales` | **Low duplicate** | "Tender capability one-pager" framing for EPC bids is functionally closer to `dept-sales` / BD than to marketing; low-carbon mining services narrative is timely |
| UC3: PPT Draft & Digest | `mining-resources` | `dept-executives` | **Likely duplicate** | Same BCG/McKinsey template; KPIs (Overburden Mbcm, Equipment Availability, Strip Ratio, Fuel Burn L/bcm) are mining-specific and genuinely distinct |
| UC4: Excel Power Hour | `mining-resources` | `dept-operations` | **Partial duplicate** | Mining KPIs (bcm, strip ratio, OEE, fuel burn) are operationally specific; useful for `construction-engineering` too |
| UC5: Outlook + 5-min Exec Moments | `mining-resources` | `dept-executives` | **Likely duplicate** | Identical core prompts; persona is Pak Surya Wibawa |
| UC6.1: Cowork Monthly Site Cascade | `mining-resources` | `dept-hr` | **Low duplicate** | "Production tonnes, equipment availability, HSE focus, one 30-day ask per site" — HSE-safety focus is specific to mining; useful for `construction-engineering` and `oil-gas-upstream` too |
| UC6.2: Cowork CV Screening | `mining-resources` | `dept-hr` | **Low duplicate** | Scoring rubric (open-pit, Komatsu/CAT fleet, blast design, geotech, drill & blast) is highly technical and sector-specific |
| UC6.3: Cowork HTML Dashboard | `mining-resources` | `dept-operations` | **Partial duplicate** | "Project Performance & HSE Dashboard" — HSE + production KPI combo at site level is distinct from retail/food dashboards |
| UC7: EPC Bid Response Pack | `mining-resources` or `construction-engineering` | `dept-strategy` | **No duplicate** — highest strategic value for B2B industries | Win-themes analysis + bid executive summary + compliance matrix + project risk register from a 240-page RFP — no equivalent in standard Copilot demo libraries; directly maps to the most expensive BD hours in EPC/contracting firms; also relevant for `construction-engineering`, `transportation-logistics` |

---

### Site 5 — Contoso Minerals Legal Copilot

| Use Case | Best-fit Industry | Best-fit Dept | Likely Duplicate? | Justification |
|----------|------------------|---------------|-------------------|---------------|
| UC1: Regulatory Research (Free Copilot Chat) | `mining-resources` | `dept-legal` | **Low duplicate** | Indonesian mining regulation (Permen ESDM, UU Minerba, JDIH, Hukumonline) is highly specific; the Free vs Paid tier distinction is a useful onboarding demo |
| UC2: Legal Memo (IRAC, grounded on internal KB) | `mining-resources` | `dept-legal` | **No duplicate** | IRAC-structured legal memo with internal KB grounding + Putusan MA citations is the most legally rigorous use case across all 5 sites; highly reusable for `government-public-sector`, `oil-gas-upstream`, `plantation-agribusiness` |
| UC3: NDA Red-Flag Review + Negotiation Email | `mining-resources` | `dept-legal` | **Low duplicate** | Cross-document comparison (counterparty NDA vs internal playbook) producing a compliance table + tracked-changes mark-up + bilingual email is a standout legal workflow; reusable across any M&A-active industry (`commercial-banking`, `asset-management`, `sovereign-wealth`, `fintech`) |
| UC4: Litigation Analytics (Excel Edit + Plan + Analyst) | `mining-resources` | `dept-risk-compliance` | **Low duplicate** | 50-case dataset with win-rate RAG, aging flags, bar chart by province, root-cause analysis — most data-intensive legal use case in the library; reusable for `insurance`, `financial-services-other`, `regulator` |
| UC5: Cowork — Executive Legal Dashboard | `mining-resources` | `dept-legal` | **No duplicate** — most technically ambitious use case across all 5 sites | Chains Researcher + Analyst Agent + Teams Recap + Cowork + PPT Copilot in a single orchestrated session; HTML dashboard output for Direktur Utama is a compelling C-suite showcase; no analogue found in standard demo libraries |
| UC6: Agent Builder — "Contoso Legal Counsel" | `mining-resources` | `dept-legal` | **No duplicate** | No-code agent grounded on internal legal KB with IRAC instructions, citation requirements, and escalation logic — directly demonstrates M365 Copilot Agent Builder capability without Copilot Studio; highly transferable to any regulated industry (`regulator`, `central-bank`, `takaful-islamic`, `government-public-sector`) |

---

### Cross-site consolidation notes

1. **Exercises 5.1 / 5.3 are 100% identical across Sites 1–4** (Outlook thread catch-up and Teams recap). These should be ingested once into a `dept-executives` general module rather than duplicated 4 times.

2. **Exercise 3.1b (McKinsey critique pass) and 4.2 (Edit mode diff) are 100% identical across Sites 1–4.** Ingest once; tag by industry for persona swapping.

3. **Exercise 6.3 (Cowork HTML dashboard) differs only in brand colour and KPI names across Sites 1–4.** Treat as one parameterised template with 4 industry variants.

4. **The 4 GM-Immersion sites (1–4) collectively give you strong coverage of:** `retail`, `hospitality-tourism`, `fmcg`, `power-utility`, `mining-resources`, `construction-engineering` — with `dept-strategy`, `dept-operations`, `dept-hr`, `dept-marketing`, `dept-executives`, `dept-finance` all represented.

5. **Site 5 is the only site covering `dept-legal` and `dept-risk-compliance`** — it should be treated as a standalone module and tagged for `mining-resources` primary, with secondary tags for any regulated industry needing legal workflow demos.

6. **Highest-uniqueness use cases (no likely duplicates, highest ingestion priority):**
   - Site 1 UC7: New-Store Go/No-Go Decision Pack
   - Site 2 UC7: PPA Compliance + Steam-Decline Board Brief
   - Site 3 UC7: Lebaran 2026 Promo Launch Pack (campaign execution end-to-end)
   - Site 4 UC7: EPC Bid Response (win-themes + compliance matrix + risk register)
   - Site 5 UC2: IRAC Legal Memo grounded on internal KB
   - Site 5 UC3: NDA Red-Flag Review with bilingual negotiation email
   - Site 5 UC5: Cowork Executive Legal Dashboard (Researcher + Analyst + Cowork chain)
   - Site 5 UC6: Agent Builder "Contoso Legal Counsel" (no-code, no Copilot Studio)
```

---

> **Note on file saving:** My tools do not include file-write capability, so I cannot save directly to `C:\Users\peiyiyap\zava-copilot-demo\_extracted_use_cases.md`. Please copy everything between the triple-backtick fences above and save it to that path. The content is complete and ready to paste — all verbatim prompts are included for all 5 sites.

**Summary of what was extracted:**
- **Sites 1–4** share an identical 7-exercise GM Immersion template; the unique content is in Exercise 1 (industry/peer benchmarks), Exercise 3 (deck title + KPI names), Exercise 4 (KPI set), and Exercise 7 (industry-specific bonus)
- **Site 5** is entirely distinct — a 6-exercise Legal Immersion covering regulatory research, IRAC memo drafting, NDA red-flag review, litigation analytics, Cowork HTML dashboard, and Agent Builder
- **Total unique prompts extracted: 87** across all 5 sites (including bonus/refinement variants)
- **Highest-value novel use cases** for the Zava library: UC7 from each of Sites 1–4 (all industry-specific power moves), plus UC2/3/5/6 from Site 5 (legal workflows with no existing analogue in standard demo libraries)