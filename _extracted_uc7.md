Agent completed. agent_id: parse-sites-1-4, agent_type: research, status: completed, description: Extract UC prompts from 4 demo HTML files, elapsed: 204s, total_turns: 0, duration: 204s

I now have all the data needed. I cannot write to files per my operating constraints — but here is the **complete, verbatim-accurate, copy-paste-ready markdown** that would go into `_extracted_uc7.md`, followed by an extraction summary. Every prompt is preserved exactly as it appears in the HTML source.

---

## ✅ COMPLETE EXTRACTED CONTENT — `_extracted_uc7.md`

*(Copy everything below the horizontal rule into the file)*

---

```markdown
# UC7 Extraction — Zava Copilot Demo Sites
> Source: 4× M365 Copilot GM Immersion HTML demo files  
> Extracted: verbatim from HTML source (`<div class="prompt">` blocks)  
> Purpose: Power Platform demo hub integration

---

## SITE 1 · Contoso Lifestyle Retail

**File:** `01_lifestyle_retail.html`  
**Site title:** Contoso Lifestyle Retail · M365 Copilot Executive Workshop  
**Industry:** Lifestyle & Sports Retail  
**Persona:** Pak Andi Wijaya — General Manager · Retail Operations, Contoso Lifestyle Retail

---

### UC7 — Exercise 7 (Bonus) · New-Store Go / No-Go Decision Pack

**Full heading (verbatim):**
> Exercise 7 (Bonus) · New-Store Go / No-Go Decision Pack  
> *Copilot Chat + Researcher · Industry power move*

**Context blurb (verbatim):**
> The single decision your GM grinds through every month — done in 15 minutes.  
> A mall developer just offered Contoso Retail a 450 sqm anchor unit at a new lifestyle mall in Surabaya. The Operating Committee meets in 4 days. The GM has done this 30 times — but it always takes a week of analyst work.

**Tool(s):** Copilot Chat + Researcher (M365 Copilot Chat or Researcher for deeper option)

**Files referenced in UC7:**
- `01 Contoso_Market_Brief.xlsx` — peer benchmark (referenced as `/01 Contoso_Market_Brief.xlsx`)
- `02 Contoso_KPI_Dashboard.xlsx` — same-store performance data (referenced as `/02 Contoso_KPI_Dashboard.xlsx`)

**Why this matters (verbatim bullet points):**
- Catchment fit · brand-mix recommendation · expected SSS · CapEx · payback · risks
- Replaces a 5-day analyst cycle with one Copilot Chat session
- Output is a 1-page GM decision pack, not a 40-page deck

**Task label:** Task 7 · 🚀 Industry-specific GM power move  
**Sub-heading:** One prompt, one decision pack, fully grounded

#### VERBATIM PROMPT — UC7 Site 1

```
Berperan sebagai retail strategy analyst untuk General Manager · Retail Operations dari Contoso Lifestyle Retail.

Skenario: developer mall menawarkan kita anchor unit (450 sqm, Ground Floor) di mall lifestyle baru yang akan dibuka Q4 2026 di Surabaya Barat — catchment ~1,2 juta middle-class dalam radius 5km, proyeksi footfall mall 800k/bulan saat matang. Lease: IDR 18 miliar selama 5 tahun. Estimasi CapEx fit-out: IDR 12 miliar.

Gunakan peer benchmark dari /01 Contoso_Market_Brief.xlsx dan performa same-store kita dari /02 Contoso_KPI_Dashboard.xlsx.

Buat decision pack 1 halaman untuk GM dengan:
1. Catchment & competition fit (vs overlap Tunjungan + Pakuwon Surabaya)
2. Brand mix yang direkomendasikan untuk format ini (4-5 brand dari portfolio kita)
3. Forecast SSS Tahun 1 / Tahun 2 / Tahun 3 dengan asumsi yang jelas
4. Total CapEx + IRR + simple payback
5. Top 3 risiko & satu mitigasi masing-masing
6. Rekomendasi GM yang tegas: GO / NO-GO / CONDITIONAL — dengan syarat spesifik

Tandai setiap asumsi [ASSUMPTION:...]. Tidak boleh ada angka karangan. Format: Word doc 1 halaman.
```

**Expected output (verbatim):**
> The artefact: A 1-page Word decision pack the GM tables at the next OpCo.

**GM call-to-action (verbatim):**
> For the GM in the room: this is the use case worth piloting first. It maps 1:1 to the most expensive analyst hours your team spends every quarter — and Copilot does it in minutes, grounded on your own files.

**Prompt count (UC7):** 1 main prompt  
**Sub-tasks within prompt:** 6 numbered deliverable sections

---

## SITE 2 · Contoso Geothermal

**File:** `02_geothermal.html`  
**Site title:** Contoso Geothermal · M365 Copilot Executive Workshop  
**Industry:** Geothermal Power Generation  
**Persona:** Pak Hendra Setiawan — General Manager · Plant Operations, Contoso Geothermal

---

### UC7 — Exercise 7 (Bonus) · PPA Quarterly Compliance & Steam-Decline Mitigation Briefing

**Full heading (verbatim):**
> Exercise 7 (Bonus) · PPA Quarterly Compliance & Steam-Decline Mitigation Briefing  
> *Copilot Chat + Word Copilot · Industry power move*

**Context blurb (verbatim):**
> The single decision your GM grinds through every month — done in 15 minutes.  
> The quarterly PPA review with PLN is in 5 days. The GM needs the compliance letter, regulator Q&A pack, and a Board one-pager on the steam-decline mitigation case — usually a week of work for the Reliability and Regulatory teams.

**Tool(s):** Copilot Chat + Word Copilot (M365 Copilot Chat or Researcher for deeper option)

**Files referenced in UC7:**
- `02 Contoso_KPI_Dashboard.xlsx` — Plant Availability %, Net Generation GWh, Forced Outage Rate %, Specific Steam Use, TRIR (referenced as `/02 Contoso_KPI_Dashboard.xlsx`)
- `05 Contoso_Strategic_Memo.docx` — steam-decline context (referenced as `/05 Contoso_Strategic_Memo.docx`)

**Why this matters (verbatim bullet points):**
- Drafts the PLN compliance letter (availability, generation, force majeure, remediation)
- Builds the regulator Q&A pack — likely questions + answers grounded on our KPIs
- Frames the steam-decline mitigation CapEx as a 1-page Board investment case

**Task label:** Task 7 · 🚀 Industry-specific GM power move  
**Sub-heading:** One prompt, one decision pack, fully grounded

#### VERBATIM PROMPT — UC7 Site 2

```
Berperan sebagai Plant Reliability lead yang mendukung General Manager · Plant Operations dari Contoso Geothermal.

Kita ada quarterly PPA review dengan PLN dalam 5 hari. Gunakan /02 Contoso_KPI_Dashboard.xlsx (Plant Availability %, Net Generation GWh, Forced Outage Rate %, Specific Steam Use, TRIR) dan /05 Contoso_Strategic_Memo.docx (konteks steam-decline).

Hasilkan tiga artefak:

1. SURAT KEPATUHAN PPA KUARTAL PLN (Word doc, ~1,5 halaman):
 - Availability plant per plant vs MW kontrak PPA
 - Net generation vs nominated profile
 - Kejadian force-majeure dan dampaknya (sebutkan spesifik Wayang Windu / Salak / Darajat)
 - Rencana remediasi untuk underperformance
 - Tone: faktual, regulatory, tanpa bahasa marketing

2. PAKET Q&A REGULATOR (Word doc):
 - 10 pertanyaan yang kemungkinan ditanyakan PLN, dengan jawaban kita
 - Kelompokkan: availability, safety, ESG / Scope 1/2, kontrak, komitmen ke depan

3. ONE-PAGER BOARD — KASUS MITIGASI STEAM-DECLINE (Word doc, 1 halaman):
 - Masalah dalam 3 baris
 - Tiga opsi (do nothing / mid-life workover / make-up well baru) dengan biaya & MW recovery
 - Opsi rekomendasi dengan payback dan IRR
 - Keputusan yang diminta dari Board

Tandai setiap asumsi [ASSUMPTION:...]. Jangan mengada-ada angka KPI — pakai apa yang ada di workbook.
```

**Expected output (verbatim):**
> The artefact: Three Board-ready Word documents, generated in 10 minutes.

**GM call-to-action (verbatim):**
> For the GM in the room: this is the use case worth piloting first. It maps 1:1 to the most expensive analyst hours your team spends every quarter — and Copilot does it in minutes, grounded on your own files.

**Prompt count (UC7):** 1 main prompt  
**Sub-tasks within prompt:** 3 numbered artefacts, each with sub-bullets

---

## SITE 3 · Contoso Pizza Co

**File:** `03_pizza.html`  
**Site title:** Contoso Pizza Co · M365 Copilot Executive Workshop  
**Industry:** Quick-Service Restaurant (QSR)  
**Persona:** Bu Lisa Hartono — General Manager · Operations & Marketing, Contoso Pizza Co

---

### UC7 — Exercise 7 (Bonus) · Lebaran 2026 Promo Launch in 30 Minutes

**Full heading (verbatim):**
> Exercise 7 (Bonus) · Lebaran 2026 Promo Launch in 30 Minutes  
> *Copilot Chat + PowerPoint Copilot · Industry power move*

**Context blurb (verbatim):**
> The single decision your GM grinds through every month — done in 15 minutes.  
> Marketing has 4 weeks until Lebaran. Last year's promo data is messy across emails and folders. The GM wants a launch-ready promo design — menu, price ladder, aggregator copy, outlet briefing pack — by tomorrow morning.

**Tool(s):** Copilot Chat + PowerPoint Copilot (M365 Copilot Chat or Researcher for deeper option)

**Files referenced in UC7:**
- `02 Contoso_KPI_Dashboard.xlsx` — AOV per outlet, food cost %, delivery mix %, CSAT (referenced as `/02 Contoso_KPI_Dashboard.xlsx`)
- `05 Contoso_Strategic_Memo.docx` — context (referenced as `/05 Contoso_Strategic_Memo.docx`)

**Why this matters (verbatim bullet points):**
- Generates the menu mix, price ladder, and food-cost guardrail in one prompt
- Drafts GoFood / GrabFood listing copy + Instagram caption variants
- Produces the outlet briefing pack with operational checklist + cannibalisation forecast

**Task label:** Task 7 · 🚀 Industry-specific GM power move  
**Sub-heading:** One prompt, one decision pack, fully grounded

#### VERBATIM PROMPT — UC7 Site 3

```
Berperan sebagai Marketing & Ops planner untuk General Manager · Operations & Marketing dari Contoso Pizza Co.

Lebaran 2026 tinggal 4 minggu lagi. Gunakan /02 Contoso_KPI_Dashboard.xlsx (AOV per outlet, food cost %, delivery mix %, CSAT) dan /05 Contoso_Strategic_Memo.docx untuk konteks.

Hasilkan promo pack siap launch:

1. DESAIN PROMO
 - 3 bundle promo (keluarga / berdua / solo) dengan menu, target AOV, food-cost %, marjin kotor
 - Price ladder vs menu saat ini — sebutkan risiko cannibalisation
 - Durasi & wave roll-out (Jakarta dulu, lalu kota sekunder)

2. CHANNEL COPY
 - GoFood listing title + description (maks 90 karakter title, 220 karakter desc)
 - GrabFood listing title + description
 - Caption Instagram × 3 varian (hangat/jenaka/Hari-Raya yang santun)
 - Copy push notification untuk app

3. PAKET BRIEFING OUTLET
 - Checklist operasional 1 halaman (prep · staffing · POS · stock-up bahan)
 - Talking points untuk briefing tim outlet
 - Rencana sampling quality-control

4. TABEL FORECAST CANNIBALISATION
 - Outlet per outlet: ekspektasi lift vs cannibalisation menu reguler, dampak AOV bersih

5. SCORECARD LAUNCH
 - 5 KPI untuk dipantau 7 hari pertama, dengan threshold merah/amber/hijau

Tandai setiap asumsi [ASSUMPTION:...]. Tone: percaya diri, food-first, tidak boleh rasis atau tone-deaf terhadap audiens Muslim Indonesia.
```

**Expected output (verbatim):**
> The artefact: A launch-ready Lebaran promo pack — menu, copy, briefing, scorecard.

**GM call-to-action (verbatim):**
> For the GM in the room: this is the use case worth piloting first. It maps 1:1 to the most expensive analyst hours your team spends every quarter — and Copilot does it in minutes, grounded on your own files.

**Prompt count (UC7):** 1 main prompt  
**Sub-tasks within prompt:** 5 numbered sections, each with sub-bullets

---

## SITE 4 · Contoso Mining Services

**File:** `04_mining_services.html`  
**Site title:** Contoso Mining Services · M365 Copilot Executive Workshop  
**Industry:** Mining Services & EPC  
**Persona:** Pak Surya Wibawa — General Manager · Operations, Contoso Mining Services

---

### UC7 — Exercise 7 (Bonus) · EPC Bid Response — Win-Themes & Compliance Matrix

**Full heading (verbatim):**
> Exercise 7 (Bonus) · EPC Bid Response — Win-Themes & Compliance Matrix  
> *Copilot Chat + Word + Researcher · Industry power move*

**Context blurb (verbatim):**
> The single decision your GM grinds through every month — done in 15 minutes.  
> A gold mining client has just released a 240-page EPC RFP, with response due in 14 days. The GM wants the win-themes, executive summary, and compliance matrix started this afternoon — usually 2 weeks of proposal-team work.

**Tool(s):** Copilot Chat + Word + Researcher (M365 Copilot Chat or Researcher for deeper option)

**Files referenced in UC7:**
- `01 Contoso_Market_Brief.xlsx` — peer benchmark vs Pamapersada, BUMA, Thiess (referenced as `/01 Contoso_Market_Brief.xlsx`)
- `05 Contoso_Strategic_Memo.docx` — capability narrative (referenced as `/05 Contoso_Strategic_Memo.docx`)

**Why this matters (verbatim bullet points):**
- Researcher scans the RFP + our last 3 wins for the highest-impact win-themes
- Drafts the bid executive summary tuned to the client's language
- Generates the compliance matrix starter (every "shall" mapped to our response)
- Builds a project-specific risk register and pricing-strategy memo

**Task label:** Task 7 · 🚀 Industry-specific GM power move  
**Sub-heading:** One prompt, one decision pack, fully grounded

#### VERBATIM PROMPT — UC7 Site 4

```
Berperan sebagai Bid Manager yang mendukung General Manager · Operations dari Contoso Mining Services.

Kita menanggapi RFP EPC 240 halaman dari klien gold mining untuk paket open-pit overburden + ore-haul, durasi 36 bulan, armada ~120 unit, lokasi Kalimantan Timur. Submission dalam 14 hari.

Gunakan /01 Contoso_Market_Brief.xlsx (peer benchmark vs Pamapersada, BUMA, Thiess) dan /05 Contoso_Strategic_Memo.docx (narasi kapabilitas kita).

Hasilkan empat artefak:

1. WIN-THEMES (1 halaman)
 - Prioritas yang disebut klien (safety, cost, schedule, ESG) — diranking
 - 3 win-theme kita yang paling berdampak dengan bukti spesifik (project / KPI)
 - 2 kelemahan kompetitor yang bisa kita highlight (secara faktual)

2. BID EXECUTIVE SUMMARY (Word doc, 2 halaman)
 - Opening kuat yang merujuk pada bahasa klien sendiri
 - Mengapa kita (3 alasan, anchored ke bukti)
 - Pendekatan schedule & mobilisasi
 - Komitmen Safety & ESG
 - Pricing positioning (tanpa angka — itu terpisah)
 - Closing call-to-action

3. COMPLIANCE MATRIX STARTER (tabel)
 - Tarik setiap requirement bernomor dari spec RFP
 - Map ke: Compliant / Compliant-with-comment / Non-compliant
 - Pre-fill respon standar kita di mana sudah ada
 - Tandai 5 item paling kontensius untuk legal review

4. RISK REGISTER (top 10)
 - Operasional, komersial, HSE, regulatori, cuaca/musim
 - Untuk masing-masing: probabilitas, dampak, mitigasi, owner

Tandai setiap asumsi [ASSUMPTION:...]. Gunakan terminologi mining-services yang presisi (Mbcm, strip ratio, OEE, TKDN, TRIR). Jangan mengada-ada riwayat project.
```

**Expected output (verbatim):**
> The artefact: Four bid-ready artefacts — win-themes, exec summary, compliance matrix, risk register.

**GM call-to-action (verbatim):**
> For the GM in the room: this is the use case worth piloting first. It maps 1:1 to the most expensive analyst hours your team spends every quarter — and Copilot does it in minutes, grounded on your own files.

**Prompt count (UC7):** 1 main prompt  
**Sub-tasks within prompt:** 4 numbered artefacts, each with sub-bullets

---

## Files Inventory — All 4 Sites

All 4 sites share the same 6-file structure. Files differ only in industry-specific content within the same filename schema.

### Shared File Schema (all sites)

| # | Filename | Type | Used in | Description (site-specific content) |
|---|----------|------|---------|--------------------------------------|
| 01 | `01 Contoso_Market_Brief.xlsx` | Excel | Ex 1 (optional), UC7 | Peer benchmark, market sizing 2024–28, SWOT |
| 02 | `02 Contoso_KPI_Dashboard.xlsx` | Excel | Ex 3, Ex 4, Ex 6, UC7 | 12 months of KPIs, targets vs actual, open issues |
| 03 | `03 Contoso_Mail_Merge_Recipients.xlsx` | Excel | Ex 6.1 | 14 recipients for Cowork-driven personalised letters |
| 04 | `04 Contoso_Brand_Guidelines.docx` | Word | Ex 5.2, Ex 6.1 | Brand tone, GM communications template, press release structure |
| 05 | `05 Contoso_Strategic_Memo.docx` | Word | Ex 3, Ex 5.4, UC7 | Strategic memo — grounds PowerPoint draft + Word doc Q&A demo |
| 06 | `samples/CVs/` (12 × .docx) | Word ×12 | Ex 6.2 | 12 candidate CVs for role-specific position |

---

### Site-Specific File Descriptions

#### Site 1 — Contoso Lifestyle Retail

| # | Filename | Site-specific description |
|---|----------|--------------------------|
| 02 | `02 Contoso_KPI_Dashboard.xlsx` | 12 months of KPIs across Plaza Indonesia, Pondok Indah Mall, Pakuwon Surabaya and more, targets vs actual, open issues |
| 03 | `03 Contoso_Mail_Merge_Recipients.xlsx` | 14 Store Managers for Cowork-driven personalised letters (name, location, role, email, performance band, key highlight) |
| 06 | `samples/CVs/` | 12 candidate CVs for the Area Retail Manager (5+ stores) role — upload as a SharePoint folder |

#### Site 2 — Contoso Geothermal

| # | Filename | Site-specific description |
|---|----------|--------------------------|
| 02 | `02 Contoso_KPI_Dashboard.xlsx` | 12 months of KPIs across Wayang Windu Unit 1, Wayang Windu Unit 2, Salak Unit 4 and more, targets vs actual, open issues |
| 03 | `03 Contoso_Mail_Merge_Recipients.xlsx` | 14 Plant Managers & Shift Supervisors for Cowork-driven personalised letters (name, location, role, email, performance band, key highlight) |
| 06 | `samples/CVs/` | 12 candidate CVs for the Geothermal Reliability Engineer role — upload as a SharePoint folder |

#### Site 3 — Contoso Pizza Co

| # | Filename | Site-specific description |
|---|----------|--------------------------|
| 02 | `02 Contoso_KPI_Dashboard.xlsx` | 12 months of KPIs across PHD Kemang, PHD Kelapa Gading, PHR Tunjungan and more, targets vs actual, open issues |
| 03 | `03 Contoso_Mail_Merge_Recipients.xlsx` | 14 Area & Outlet Managers for Cowork-driven personalised letters (name, location, role, email, performance band, key highlight) |
| 06 | `samples/CVs/` | 12 candidate CVs for the QSR Area Operations Manager (10+ outlets) role — upload as a SharePoint folder |

#### Site 4 — Contoso Mining Services

| # | Filename | Site-specific description |
|---|----------|--------------------------|
| 02 | `02 Contoso_KPI_Dashboard.xlsx` | 12 months of KPIs across Tabang Coal Site, Gunung Bayan Site, Martabe Gold EPC and more, targets vs actual, open issues |
| 03 | `03 Contoso_Mail_Merge_Recipients.xlsx` | 14 Project Managers & Site Superintendents for Cowork-driven personalised letters (name, location, role, email, performance band, key highlight) |
| 06 | `samples/CVs/` | 12 candidate CVs for the Mining Project Superintendent role — upload as a SharePoint folder |

---

### Complete Flat File List (all unique filenames across 4 sites)

```
01 Contoso_Market_Brief.xlsx
02 Contoso_KPI_Dashboard.xlsx
03 Contoso_Mail_Merge_Recipients.xlsx
04 Contoso_Brand_Guidelines.docx
05 Contoso_Strategic_Memo.docx
samples/CVs/CV_01.docx  [× 12 per site, filenames as CV_*.docx]
```

> **Note:** All 4 sites use the same filenames. Each site's `samples/` folder contains industry-specific data inside those files. The `CVs/` folder contains 12 × `CV_*.docx` files per site.

---

*End of extraction — generated from verbatim HTML source parsing*  
*Session ID referenced in all 4 files: `112e253a-7fd6-48b4-80b3-e89c7d7914fd`*
```

---

## 📊 Extraction Summary

| # | Site | UC7 Heading | Persona | Tools | Files in UC7 | Prompt Count | Sub-tasks |
|---|------|-------------|---------|-------|-------------|-------------|-----------|
| 1 | Contoso Lifestyle Retail | New-Store Go / No-Go Decision Pack | Pak Andi Wijaya | Copilot Chat + Researcher | 2 (.xlsx ×2) | 1 | 6 |
| 2 | Contoso Geothermal | PPA Quarterly Compliance & Steam-Decline Mitigation Briefing | Pak Hendra Setiawan | Copilot Chat + Word Copilot | 2 (.xlsx + .docx) | 1 | 3 artefacts |
| 3 | Contoso Pizza Co | Lebaran 2026 Promo Launch in 30 Minutes | Bu Lisa Hartono | Copilot Chat + PowerPoint Copilot | 2 (.xlsx + .docx) | 1 | 5 sections |
| 4 | Contoso Mining Services | EPC Bid Response — Win-Themes & Compliance Matrix | Pak Surya Wibawa | Copilot Chat + Word + Researcher | 2 (.xlsx + .docx) | 1 | 4 artefacts |

**Files inventory total:** 6 unique filenames × 4 sites = 24 file slots (all shared schema, site-specific data inside). Every site contains: `01 Contoso_Market_Brief.xlsx`, `02 Contoso_KPI_Dashboard.xlsx`, `03 Contoso_Mail_Merge_Recipients.xlsx`, `04 Contoso_Brand_Guidelines.docx`, `05 Contoso_Strategic_Memo.docx`, `samples/CVs/` (12 × `.docx`).

**Notes for the integrating agent:**
- All 4 UC7 prompts are **single prompts** (not multi-turn sequences) — the entire scenario is in one paste block
- Each prompt uses `/filename` reference syntax for file grounding (e.g. `/02 Contoso_KPI_Dashboard.xlsx`)
- All prompts contain `Tandai setiap asumsi [ASSUMPTION:...]` as a hallucination guard
- Bahasa Indonesia is preserved verbatim throughout — do **not** translate
- The `<button class="copy">` elements in source are UI artefacts and are NOT part of the prompt text (excluded above)
- Site 2 (Geothermal) is the only UC7 that produces **3 Word documents** — the others produce a single pack/artefact
- Site 4 (Mining) is the most complex UC7 — 4 artefacts including a compliance matrix table and risk register