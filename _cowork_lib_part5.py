# -*- coding: utf-8 -*-
"""Department-specific Cowork use cases + remaining sector (Property Development).
12 dept cards + 1 leftover sector card."""

CARDS = {}

CARDS['uc-propdev-launch'] = {
    'title': 'Multi-Tower Launch Campaign Pack',
    'dept_tag': 'Sales & Marketing',
    'industry_tag': 'Property Development',
    'complexity': 'intermediate',
    'apps': ['Excel', 'PowerPoint', 'Word', 'Outlook', 'Teams'],
    'desc': 'Phase launch of 3 towers — Cowork builds the pricing ladder, campaign brief, agent pack and approval brief.',
    'skills': [
        'Phase-by-phase pricing ladder',
        'Agent / channel commission economics',
        'Approval-paper construction (lender + Board)',
    ],
    'instructions': [
        'Open Microsoft 365 Copilot Cowork',
        'Attach the 3 source files',
        'Paste the prompt',
    ],
    'sample_files': [
        ('PD_Project_Feasibility.xlsx', 'xlsx'),
        ('PD_Comparable_Launches.xlsx', 'xlsx'),
        ('PD_Sales_Pipeline.xlsx', 'xlsx'),
    ],
    'prompts': [{
        'label': 'Tower launch pack',
        'text': (
            "Using the 3 attached files, build the [PROJECT] phase-1 launch pack. In parallel:\n"
            "1) Excel — pricing ladder per tower per unit type per floor band with absorption assumption.\n"
            "2) PowerPoint — 10-slide Sales Committee deck.\n"
            "3) Word — agent campaign brief with commission ladder + sales-event calendar.\n"
            "4) Outlook — top-30 agent letters introducing the launch with priority allocation.\n"
            "5) Word — Board / lender approval paper covering financial assumptions + risk.\n"
            "Cite the file + tab for every number. Flag any tower whose breakeven absorption is below 65% in 12 months."
        )
    }],
    'expected': [
        'Pricing ladder',
        'Sales Committee deck',
        'Agent campaign brief',
        '30 agent letters',
        'Board / lender paper',
    ],
    'watch': [
        'Low-absorption towers surfaced',
        'Commission ladder competitive',
    ],
    'honest': 'Launch pricing is market-sensitive — Cowork synthesises; the Head of Sales calibrates against the comp set in the last 60 days.',
    'tips': [
        'Variation: add a phasing alternative (defer Tower 3)',
        'Variation: produce a buyer-facing FAQ document',
    ],
}


# ── Contoso Property Group demo — distinctive Township GM use cases ────

CARDS['uc-property-township-ops-review'] = {
    'title': 'Township Operations Quarterly Review — Sales + Build + Customer + Land Bank',
    'dept_tag': 'Township Operations',
    'industry_tag': 'Property Development',
    'complexity': 'advanced',
    'apps': ['Excel', 'PowerPoint', 'Word', 'Outlook', 'Teams', 'Cowork'],
    'desc': 'GM Township Operations runs the quarter-close across four dimensions in one Cowork pass — sales velocity, construction progress, customer NPS, land bank monetisation — producing a live HTML KPI dashboard, an 8-slide Township Ops Committee deck, a 1-page GM memo, and personalised mail-merged letters to 14 Township Managers.',
    'skills': [
        'Multi-dimensional KPI synthesis across sales / build / customer / land bank in a single quarterly view',
        'Live HTML dashboard generation with green/amber/red indicators per township',
        'Personalised mail merge — same operating themes, different township figures and asks per Township Manager',
        'BCG/McKinsey-style narrative pyramid for the Ops Committee deck',
    ],
    'instructions': [
        'Open Microsoft 365 Copilot Cowork → model picker → Sonnet+Opus Advisor',
        'Attach the 4 township source files listed below',
        'Paste Prompt 1 — Cowork fans out the 5 deliverables in parallel',
        'Open the generated dashboard.html in your browser; review the deck and letters',
    ],
    'sample_files': [
        ('PD_Township_Sales_Velocity.xlsx', 'xlsx'),
        ('PD_Construction_Progress_Tracker.xlsx', 'xlsx'),
        ('PD_Customer_NPS_VP_Defects.xlsx', 'xlsx'),
        ('PD_Land_Bank_Register.xlsx', 'xlsx'),
    ],
    'prompts': [{
        'label': 'Quarterly Township Ops review fan-out',
        'text': (
            "Using the 4 attached township files for [QUARTER] FY[YY], in parallel, do all 5:\n"
            "1) Build a live HTML KPI dashboard — one row per township, columns for GDV Launched vs Target, Sales Take-up % in 90 days, Construction Progress vs Schedule, NPS, Unsold Inventory %, Land Bank Acres, GreenRE Status. Use green/amber/red indicators. Brand: deep teal #0E7C66 + warm gold #D4A017 on white. Save to OneDrive as /Township Ops/Q[QUARTER]_Dashboard.html.\n"
            "2) Build an 8-slide deck in PowerPoint for the Township Ops Committee using our brand template — Slide 1 cover, Slide 2 group dashboard, Slides 3-5 three priority townships (one per slide), Slide 6 land bank update, Slide 7 risks (OPR sensitivity, KPKT/EIA permits, contractor labour), Slide 8 decisions needed.\n"
            "3) Draft a 1-page GM memo in Word for the COO — Three Township Priorities: move the unsold inventory at Iskandar Phase 3; deliver VP on schedule at Hilltop Block C; monetise the Greater Klang Valley parcel. Quantify each.\n"
            "4) Personalised mail merge — one Outlook letter per Township Manager (14 total), each with that township's specific sales gap, construction milestones at risk, customer-NPS hot spots, and the 2 specific asks for the next 30 days.\n"
            "5) Draft a Teams post to #township-ops — 3 lines summary plus the dashboard link plus the 3 priorities.\n"
            "Cite the source file + sheet + row for every figure. Flag any township with NPS below 40 or take-up below 50% at 90 days as RED."
        )
    }],
    'expected': [
        'Live HTML Township KPI dashboard (branded)',
        '8-slide Township Ops Committee deck',
        '1-page GM memo with 3 priorities quantified',
        '14 personalised Township Manager letters (mail merge)',
        'Teams #township-ops summary post',
    ],
    'watch': [
        'One Cowork run covers all 4 dimensions — no copy-paste between sales, build, customer, land bank',
        'Letters differ by township figures despite sharing themes — true personalisation, not bulk send',
        'Red flags surface to the GM memo automatically — no manual highlight needed',
    ],
    'honest': 'Cowork synthesises and renders. The GM still walks each township figure before the Ops Committee — and bumiputera-quota or KPKT/EIA approval timing requires the local Township Manager to confirm. Pricing or rebate decisions go through the Pricing Committee, not the dashboard.',
    'tips': [
        'Re-run weekly with the same prompt — change [QUARTER] tag to keep a rolling dashboard',
        'Add a 6th task — generate a 60-second voice brief for the GM\'s morning commute (Imagen 2 not needed, audio only)',
        'For listed REITs, swap "Township Ops Committee" for "Asset Management Committee" and the deck pivots automatically',
    ],
}

CARDS['uc-property-land-bank'] = {
    'title': 'Land Bank Monetisation Decision Pack — JV / In-House / Divest per Parcel',
    'dept_tag': 'Strategy & Land',
    'industry_tag': 'Property Development',
    'complexity': 'advanced',
    'apps': ['Excel', 'PowerPoint', 'Word', 'Cowork'],
    'desc': 'For each of 6 strategic parcels, Cowork builds the JV vs in-house vs divest decision pack — IRR, GDV potential, masterplan options, GreenRE pipeline pathway, and a board-paper recommendation per parcel.',
    'skills': [
        'Per-parcel IRR and GDV modelling across 3 monetisation pathways (in-house build / JV / outright divest)',
        'Masterplan option evaluation (mixed-use industrial pivot vs residential vs commercial)',
        'GreenRE / GBI certification pathway selection per parcel',
        'Board-paper drafting with quantified recommendation per parcel',
    ],
    'instructions': [
        'Open Cowork',
        'Attach the land bank register + comparable land sales + feasibility models',
        'Paste the prompt — Cowork builds one decision pack per parcel in parallel',
    ],
    'sample_files': [
        ('PD_Land_Bank_Register.xlsx', 'xlsx'),
        ('PD_Comparable_Land_Sales.xlsx', 'xlsx'),
        ('PD_Feasibility_Models.xlsx', 'xlsx'),
        ('PD_GreenRE_GBI_Pipeline.xlsx', 'xlsx'),
    ],
    'prompts': [{
        'label': 'Land bank monetisation decision pack',
        'text': (
            "Using the 4 attached files, build the Land Bank Monetisation Decision Pack for the next Land & Strategy Committee. For each of our 6 strategic parcels (Klang Valley x3, Iskandar x2, Penang x1), in parallel:\n"
            "1) Excel — three-scenario IRR & GDV table per parcel: (a) in-house masterplan & build, (b) JV with a strategic partner (60:40), (c) outright land sale. Include sensitivities on launch year, take-up, and OPR.\n"
            "2) PowerPoint — 1 slide per parcel (6 slides plus a 1-slide cover + 1-slide group recommendation = 8 slides total). Each parcel slide: acreage, indicative GDV, 3-scenario IRR side by side, GreenRE pathway, recommended strategy.\n"
            "3) Word — Board paper (4 pages): executive summary; per-parcel rationale; group portfolio implications (RM 24B remaining GDV, 18-year pipeline at current launch run-rate); risks (cycle timing, partner-selection risk, holding cost); recommendation per parcel with approval ask.\n"
            "4) Excel — a simple ranked table (one row per parcel) with columns: recommended strategy, expected IRR, GDV unlocked, decision urgency (this quarter / this half / next year).\n"
            "Cite the comparable-sale or feasibility row driving each number. Flag any parcel whose in-house IRR is below our 15% hurdle as JV-or-divest preferred."
        )
    }],
    'expected': [
        'Three-scenario IRR & GDV Excel per parcel',
        '8-slide Land & Strategy Committee deck',
        '4-page Board paper with per-parcel recommendation',
        'Ranked decision table',
    ],
    'watch': [
        'Each parcel gets all 3 scenarios — no premature JV recommendation without the divest comparator',
        'GreenRE pathway baked into the masterplan, not retrofitted',
        'Sub-hurdle IRR parcels flagged for JV/divest automatically',
    ],
    'honest': 'IRR depends on launch-year assumptions Cowork cannot independently verify — Strategy & Land owns the assumption set. JV partner selection is a separate workstream involving Legal, Investments, and the GLC sponsor. The Board ultimately decides; Cowork prepares the pack.',
    'tips': [
        'Re-run when OPR moves more than 50 bps — sensitivity table updates auto',
        'Add a 5th deliverable — a draft non-binding term sheet for the JV pathway per parcel',
        'For divestment pathway, add a 6th deliverable — a teaser pack for potential buyers',
    ],
}


# ── Contoso Life Assurance demo — distinctive Operations use cases ─────

CARDS['uc-life-claims-tat-benchmark'] = {
    'title': 'Claims TAT Benchmark Pull + Ops Weekly Briefing',
    'dept_tag': 'Operations',
    'industry_tag': 'Life Insurance',
    'complexity': 'beginner',
    'apps': ['Cowork', 'Word', 'Outlook'],
    'desc': 'Operations team pulls global claims Turn-Around-Time and straight-through-processing benchmarks from Swiss Re, McKinsey, LIMRA, Deloitte, and the regulator in one Cowork run — turning them into a 1-page Ops briefing, a list of 3 open questions for the Claims team, and a draft email to the Head of Claims.',
    'skills': [
        'GCSE-framework prompting — Goal, Context, Source, Expectation explicit in every prompt',
        'Authoritative-source-only research (Swiss Re, McKinsey, LIMRA, Deloitte, OJK)',
        'Synthesis into Ops-team daily briefing format',
        'Open-question generation to drive the next Claims team conversation',
    ],
    'instructions': [
        'Open Cowork → model picker → Auto (or Sonnet+Opus Advisor for higher synthesis quality)',
        'Toggle Researcher tool on — public web research is essential here',
        'Paste Prompt 1 (or use the GCSE colour-coded variant)',
        'Forward the resulting briefing to the Claims team via the Outlook draft',
    ],
    'sample_files': [],
    'prompts': [{
        'label': 'Pull claims TAT benchmarks + Ops briefing',
        'text': (
            "I work in the Operations team at a life insurance company. In parallel, do all 4:\n"
            "1) Researcher — give me a brief summary of global benchmarks for life insurance claims Turn-Around-Time (TAT) and adoption rates for straight-through processing (STP) over the last 12 months. Cite 3-5 authoritative sources (Swiss Re, McKinsey, LIMRA, Deloitte, OJK or the local regulator). Maximum 8 bullets.\n"
            "2) Word — turn the findings into a 1-page Operations briefing with three sections: Where the industry is (benchmarks), Where we sit (placeholder for our actual figures), 3 open questions for the Claims team next week.\n"
            "3) Outlook — draft an email to the Head of Claims forwarding the briefing, with the 3 open questions in the body and a calendar invite for a 30-minute review meeting.\n"
            "4) End the briefing with a sources & retrieval-timestamp footer.\n"
            "Public sources only. No real customer or policy data. If a benchmark is older than 12 months, label it as such."
        )
    }],
    'expected': [
        '1-page Operations briefing (Word)',
        '3 open questions for the Claims team',
        'Outlook draft to Head of Claims with 30-min meeting invite',
        'Sources & retrieval-timestamp footer (auditable)',
    ],
    'watch': [
        'Cowork explicitly cites Swiss Re / McKinsey / LIMRA / Deloitte / regulator — not generic blog posts',
        'Briefing distinguishes industry benchmark from our actual figures — analyst discipline preserved',
        'Open questions are answerable in a 30-min meeting — not vague',
    ],
    'honest': 'Researcher pulls public-source benchmarks; it cannot read your tenant\'s internal Claims dashboard unless you attach the file or enable local browser use. Re-run quarterly — benchmarks drift. Any claim about our own TAT must be verified by Claims Ops before the briefing goes upstream.',
    'tips': [
        'Re-run with "Takaful claims" instead for the Tabarru-fund variant',
        'Add a 5th task — generate a 1-slide visual of the benchmark gap using Copilot Create',
        'For ID variant, add Asosiasi Asuransi Jiwa Indonesia (AAJI) and Bank Indonesia data as sources',
        'Use the GCSE colour toggle when teaching this prompt to new joiners',
    ],
}

CARDS['uc-life-corporate-renewal'] = {
    'title': 'Corporate Health Benefits Renewal Kick-off Pack',
    'dept_tag': 'Corporate Accounts',
    'industry_tag': 'Life Insurance',
    'complexity': 'intermediate',
    'apps': ['Excel', 'PowerPoint', 'Word', 'Outlook', 'Cowork'],
    'desc': 'For a 25,000-employee corporate account renewing the 2027 policy year, Cowork builds the renewal kick-off pack — utilisation analysis, benefit-adjustment recommendations, wellness programme options, 24h-onboarding commitment letter, and a partnership-grade invitation email to the corporate HR lead.',
    'skills': [
        'Corporate account renewal economics (utilisation, loss ratio, benefit calibration)',
        'B2B partnership-grade email drafting (collaborative tone, not transactional)',
        'Wellness programme option scoping with measurable adoption KPIs',
        'Multi-deliverable kick-off pack from one Cowork run',
    ],
    'instructions': [
        'Open Cowork → model picker → Sonnet+Opus Advisor (B2B copy benefits from advisor pairing)',
        'Attach the 3 source files listed below',
        'Paste the prompt — Cowork prepares the full kick-off pack',
        'Send the Outlook invitation; bring the deck to the kick-off',
    ],
    'sample_files': [
        ('LIFE_Corporate_Utilisation_2026.xlsx', 'xlsx'),
        ('LIFE_Wellness_Programme_Catalogue.docx', 'docx'),
        ('LIFE_Service_Commitments_SLA.docx', 'docx'),
    ],
    'prompts': [{
        'label': 'Build the corporate renewal kick-off pack',
        'text': (
            "I am a Senior Manager in the Operations team at Contoso Life Assurance, preparing the 2027 corporate health benefits renewal kick-off for [CORPORATE-CLIENT] (25,000 employees). The kick-off meeting is on [KICK-OFF-DATE]. In parallel, do all 5:\n"
            "1) Excel — analyse 2026 utilisation: claims frequency, average claim cost, top 5 claim categories, loss ratio, high-cost-claimant cohort (top 5%). Output a 1-tab summary with current vs prior year and a recommended-action column per category.\n"
            "2) Word — recommendation memo (2 pages): 3 benefit-adjustment options for 2027 (no change with re-pricing / structural redesign / wellness-weighted hybrid). Quantify expected loss-ratio impact per option.\n"
            "3) PowerPoint — 8-slide kick-off deck: Slide 1 cover, Slide 2 partnership recap, Slides 3-4 2026 utilisation story, Slide 5 the 3 benefit options, Slide 6 wellness programme menu, Slide 7 our 24-hour onboarding commitment for new joiners, Slide 8 next steps & timeline.\n"
            "4) Outlook — partnership-grade invitation email to the Head of HR. Professional collaborative tone. Cover: (a) 2026 utilisation results and benefit-adjustment recommendations, (b) new wellness programme options, (c) 24h onboarding commitment. End with a request to confirm attendance 7 days before the kick-off.\n"
            "5) Word — 1-page service-commitment letter signed by the GM Corporate Accounts, restating the 24-hour onboarding SLA, the dedicated relationship-manager line, and the quarterly business-review cadence.\n"
            "All five deliverables in EN and BI. No real customer or policy data — use placeholder figures grounded in the attached utilisation pattern."
        )
    }],
    'expected': [
        '1-tab utilisation summary (Excel)',
        '2-page 3-option recommendation memo (Word)',
        '8-slide kick-off deck (PowerPoint)',
        'Partnership-grade invitation email (Outlook)',
        '1-page service-commitment letter (Word)',
    ],
    'watch': [
        'Tone is partnership-grade, not transactional — collaborative language throughout',
        'Each benefit-adjustment option carries a quantified loss-ratio impact, not just descriptive copy',
        'EN + BI side-by-side so the corporate HR lead can pick their preferred language',
    ],
    'honest': 'Final pricing for the 2027 renewal goes through the Product Pricing Committee and the Appointed Actuary — Cowork drafts; Pricing decides. The service-commitment letter is contractual once signed — Legal must review before the GM signs. Wellness programme options should be calibrated against the broker/consultant\'s benchmark before the kick-off.',
    'tips': [
        'Re-run with the corporate client\'s industry context as additional Source (e.g. high-shift-work for manufacturing changes the wellness mix)',
        'Add a 6th deliverable — a 2-minute video script for the GM\'s pre-meeting message to the HR lead',
        'Pin this as a custom skill on the Customize page so every Account Manager can trigger the same flow',
    ],
}


# ── Contoso Property Group demo — additional distinctive use cases ─────

CARDS['uc-property-strategic-landscape'] = {
    'title': 'Property Sector Landscape Scan — Researcher Critique + Model Council',
    'dept_tag': 'Strategy & Land',
    'industry_tag': 'Property Development',
    'complexity': 'intermediate',
    'apps': ['Cowork', 'Word'],
    'desc': 'GM-level sector intelligence on the Integrated Township & Property Development landscape in Malaysia — first Researcher Critique (Auto) for the default scan, then Model Council (multiple models in parallel) when the decision is too important for one model, then a 1-page GM strategy brief.',
    'skills': [
        'Researcher Critique mode — Auto picks the right model and shows its reasoning critique',
        'Model Council mode — 3-4 frontier models answer the same question in parallel; Cowork reconciles disagreements',
        'Sector intelligence specific to Malaysian property (OPR, KPKT, EIA, bumiputera quota, GreenRE, MM2H, EPF withdrawal scheme)',
        'Distilling council debate into a 1-page GM brief with explicit areas of consensus and disagreement',
    ],
    'instructions': [
        'Open Cowork → Researcher tool → Mode: Critique (Auto)',
        'Paste Prompt 1 for the default landscape scan',
        'When Critique flags an answer-confidence below 80%, switch to Mode: Model Council and paste Prompt 2',
        'Paste Prompt 3 to convert the council output into a 1-page Word brief for the GM',
    ],
    'sample_files': [],
    'prompts': [
        {
            'label': '1. Critique (Auto) — default landscape scan',
            'text': (
                "Researcher Critique mode. Scan the Integrated Township & Property Development landscape in Malaysia for the last 12 months. Cover:\n"
                "1) Headwinds (OPR trajectory, household-debt-to-GDP, contractor labour supply, KPKT/EIA permit timelines, GreenRE/GBI cost premium).\n"
                "2) Tailwinds (MM2H scheme, EPF withdrawal flexibility, Johor-Singapore Special Economic Zone, ETR / data-centre catchment).\n"
                "3) The top 5 listed Malaysian township developers' Q reported take-up, GDV launched, and unsold inventory.\n"
                "4) Two regulator moves to watch (Ministry of Housing / Bank Negara) in the next 12 months.\n"
                "Output: maximum 12 bullets, each bullet citing one authoritative source with retrieval timestamp. End with 3 open questions for the Strategy team's Friday session."
            )
        },
        {
            'label': '2. Model Council — stress-test the strategic question',
            'text': (
                "Switch to Model Council. The question: 'Given the current OPR trajectory and unsold-inventory levels, should Contoso Property Group accelerate Phase 4 launches at Iskandar, hold for 6 months, or pivot Phase 4 to mixed-use industrial?'\n"
                "Run the question across all available council models in parallel. Report:\n"
                "- Each model's recommended action and its top 2 reasons\n"
                "- Where the council agrees (consensus)\n"
                "- Where the council disagrees (disagreement axis — what would change the answer)\n"
                "- The deciding question the GM should answer before choosing\n"
                "Format as a 2-column reconciliation table plus a 3-bullet executive note."
            )
        },
        {
            'label': '3. 1-page GM strategy brief in Word',
            'text': (
                "Convert the council output into a 1-page Word brief for the GM. Sections: (1) The strategic question; (2) Council consensus in 3 bullets; (3) Council disagreement axis in 2 bullets; (4) Recommended decision with the supporting model rationale; (5) The deciding question the GM still owns. Brand tone: deep teal, professional, no marketing fluff. End with a source footer (each citation hyperlinked)."
            )
        },
    ],
    'expected': [
        'Researcher Critique landscape scan (12 bullets, sources)',
        'Model Council reconciliation table',
        '1-page GM strategy brief (Word)',
    ],
    'watch': [
        'Critique mode shows the model\'s own confidence — surfaces when to escalate to Council',
        'Council reveals model disagreement honestly — no false consensus',
        'The GM brief preserves disagreement instead of hiding it under a single recommendation',
    ],
    'honest': 'Researcher pulls public data; private competitor data (e.g. unannounced launch pricing) is out of scope. The Council disagreement is signal, not noise — if 3 models out of 4 disagree, the right answer is probably to gather more data before deciding.',
    'tips': [
        'Re-run the Council monthly — the disagreement axis shifts as conditions move',
        'For REITs, swap the question to "Acquire / hold / divest the [ASSET] in this cap-rate environment?"',
        'Add a 4th prompt that drafts the Friday session agenda using the 3 open questions',
    ],
}

CARDS['uc-property-gm-strategy-deck'] = {
    'title': 'GM Strategy Deck — BCG/McKinsey Tightening for Township Ops Committee',
    'dept_tag': 'Township Operations',
    'industry_tag': 'Property Development',
    'complexity': 'intermediate',
    'apps': ['PowerPoint', 'Cowork'],
    'desc': 'Two-pass deck workflow — first Cowork drafts an 8-slide GM strategy deck for the Township Ops Committee from the strategic landscape brief; then a McKinsey-style tightening pass rewrites every slide to one-pyramid-per-slide with quantified asks.',
    'skills': [
        'Pyramid Principle deck structure (situation, complication, resolution per slide)',
        'McKinsey tightening prompt — every slide must have a quantified ask or be cut',
        'Brand template auto-application (deep teal + warm gold)',
        'GM persona calibration (concise, decision-oriented, not training-deck dense)',
    ],
    'instructions': [
        'Open Cowork → attach the GM strategy brief (output from the landscape-scan card)',
        'Paste Prompt 1 — Cowork drafts the 8-slide deck applying your brand template',
        'Paste Prompt 2 — McKinsey tightening pass; the deck shrinks and sharpens',
        'Open the deck in PowerPoint, accept the tightened slides',
    ],
    'sample_files': [
        ('PD_GM_Strategy_Brief.docx', 'docx'),
    ],
    'prompts': [
        {
            'label': '1. Draft an 8-slide GM strategy deck',
            'text': (
                "Using the attached GM strategy brief, draft an 8-slide deck in PowerPoint for the next Township Operations Committee. Apply our brand template (deep teal #0E7C66, warm gold #D4A017). Structure:\n"
                "Slide 1 — Cover: 'Township Strategy Refresh · Q[QUARTER] FY[YY]'\n"
                "Slide 2 — Where we are: 3 numbers on group performance (GDV launched, take-up %, NPS)\n"
                "Slide 3 — Sector headwinds (OPR, contractor labour, KPKT timelines) — top 3 with quantified exposure\n"
                "Slide 4 — Sector tailwinds (MM2H, JS-SEZ, data-centre catchment) — top 3 with quantified upside\n"
                "Slide 5 — Three township priorities (Iskandar inventory, Hilltop VP, Klang Valley land bank)\n"
                "Slide 6 — Land bank monetisation pathway: in-house / JV / divest by parcel\n"
                "Slide 7 — GreenRE pipeline — pricing premium and the certification roadmap\n"
                "Slide 8 — Decisions needed at Township Ops Committee with owners and dates\n"
                "Every slide carries a top-of-slide title that IS the slide's argument (not just the topic)."
            )
        },
        {
            'label': '2. McKinsey-style tightening review',
            'text': (
                "Tighten the deck McKinsey-style. For every slide:\n"
                "- Rewrite the title so it states the slide's argument in one sentence (not the topic)\n"
                "- Remove any bullet that does not carry a number or a date\n"
                "- Surface the quantified ask of the slide (decision, approval, resource) at the bottom right\n"
                "- If a slide has no ask, propose deleting it and tell me why\n"
                "Output: the revised deck plus a 1-paragraph rationale for any deleted or merged slides."
            )
        },
    ],
    'expected': [
        '8-slide branded GM strategy deck (PowerPoint)',
        'McKinsey-tightened version with action-titled slides',
        'Rationale paragraph for any cuts or merges',
    ],
    'watch': [
        'Slide titles state the argument, not the topic — pyramid principle in action',
        'Every slide has a quantified ask — no decoration slides survive',
        'Brand template applied automatically — no manual reformatting',
    ],
    'honest': 'Cowork drafts and tightens. The GM still walks every slide before the Committee — pyramid titles can be over-confident if the underlying data is shaky. Sensitive numbers (e.g. unannounced pricing) need Pricing Committee clearance before any slide leaves the GM.',
    'tips': [
        'Re-run the tightening prompt twice — second pass usually cuts another 2 slides',
        'Add a 3rd prompt: "Generate the speaker notes the GM would actually say"',
        'For asset-management committees (REIT), swap "township priorities" for "asset priorities"',
    ],
}

CARDS['uc-property-create-infographic'] = {
    'title': 'Township Snapshot Infographic — Copilot Create on Brand',
    'dept_tag': 'Sales & Marketing',
    'industry_tag': 'Property Development',
    'complexity': 'beginner',
    'apps': ['Copilot Create', 'PowerPoint', 'Outlook'],
    'desc': 'A one-page A4 infographic poster for the Township Ops Committee — four variants from one Copilot Create session: Township Snapshot · Land-Bank Map · Customer VP Journey · GreenRE Pipeline. Deep teal + warm gold brand, fills the full A4 page (no empty bottom), Refine-without-restarting follow-ups for trim.',
    'skills': [
        'Copilot Create with brand colour discipline (specific hex codes)',
        'Composing a full-A4 vertical infographic in one prompt (no empty bottom)',
        'Refine-without-restarting — Edit follow-ups instead of new Create runs',
        'Brand-aligned thin-outline-icon style (no clip-art, no stock photos)',
    ],
    'instructions': [
        'Open Microsoft 365 Copilot Chat → Create in left sidebar (or type /create)',
        'Paste Prompt 1 — get 4 design variants',
        'Pick your favourite → click Edit',
        'Paste any of the Refine follow-ups to trim or extend',
        'Download as PNG or PDF and drop into Outlook, Teams or PowerPoint',
    ],
    'sample_files': [],
    'prompts': [
        {
            'label': '1. Township Snapshot · Q[QUARTER] FY[YY]',
            'text': (
                "Make a clean, premium one-page infographic poster called 'Township Snapshot — Sales, Build, Customer · Q[QUARTER] FY[YY]'. Use our brand colours deep teal (#0E7C66) and warm gold (#D4A017) on white, with a small dark-grey for headings — a confident, property-developer feel. Vertical A4, fill the entire page top to bottom — NO empty space at the bottom.\n\n"
                "At the top, a big bold title: 'TOWNSHIP SNAPSHOT · Q[QUARTER] FY[YY]'. Underneath: 'Sales velocity · Construction · Land bank · Customer · For the Township Operations Committee'.\n\n"
                "Then a row of 4 big-number boxes: 'RM 480M' GDV Launched YTD (target RM 520M); '68%' Group Sales Take-up in 90 days (target 75%); '92%' Construction Progress vs Schedule; '48' Customer NPS (target 55).\n\n"
                "Then a section called 'THE THREE TOWNSHIP PRIORITIES' with 3 numbered cards side by side: (1) Move the unsold inventory (price-realignment at Iskandar Phase 3; bumiputera-quota release; sales-gallery activation; rebate package). (2) Deliver VP on schedule (main-contractor catch-up at Hilltop Block C; CONQUAS audit; KPKT VP certification; defects-liability handover). (3) Monetise the land bank (Greater Klang Valley JV vs in-house; GreenRE/GBI roll-out; mixed-use industrial pivot; refreshed masterplan).\n\n"
                "Then a 'Township Compare' table (5 rows × 3 columns: Take-up %, GDV Launched, Unsold Inventory %, Construction Progress, NPS for the 3 priority townships, green/amber/red indicators).\n\n"
                "Then a 'Risks we're managing' row of 3 icons: OPR sensitivity, KPKT/EIA permits, contractor labour supply.\n\n"
                "Bottom: a teal-gold ribbon footer with the recommendation and today's date.\n\n"
                "Style: clean modern sans-serif, thin outline icons (house, crane, map-pin, leaf), NO clip-art, NO stock photos. Fill the entire A4 page."
            )
        },
        {
            'label': '2. Refine — fill empty space',
            'text': "There is empty space at the bottom of the page. Please fill it by extending the sections, or add a footer ribbon in our brand colour with a one-sentence recommendation for the GM and the company name 'Contoso Property Group' on the left."
        },
        {
            'label': '3. Refine — icon style',
            'text': "Replace all the icons with simple, thin outline icons in our brand colour. No emojis, no stock photos."
        },
        {
            'label': '4. Alternate angles (pick one)',
            'text': "Generate three alternate one-page A4 infographic variants in the same teal-gold style: (a) 'Where We Hold Land — Klang Valley & Iskandar Bank · FY[YY]' with a stylised Peninsular Malaysia map, 6 parcel pins, and a Parcel Strategy table. (b) 'From Sale to Keys — Your Township Journey' with a 5-step VP timeline and a Service Standards table. (c) 'GreenRE & GBI Pipeline · FY[YY]' with three pillars (energy, water, materials) and a Pipeline Status table."
        },
    ],
    'expected': [
        '1 polished A4 infographic poster (PNG or PDF), brand-aligned',
        '3 alternate angle variants on demand',
        'Refined version (full-bleed, brand icons) on follow-up',
    ],
    'watch': [
        'Create respects exact brand hex codes when you specify them',
        'Refine works in plain English — no design-tool skills needed',
        'Enterprise Data Protection keeps the design inside your tenant',
    ],
    'honest': 'Copilot Create is great for the first 80%. Final pixel polish (legal disclaimers, exact logo position, accessibility colour contrast) may still need the design team. For external customer-facing pieces, get Brand and Comms sign-off before posting.',
    'tips': [
        'Save the prompt as a reusable skill on the Customize page so any team member can re-run',
        'For Mandarin / BM / BI variants, just add "Translate the title and labels into [LANGUAGE]"',
        'For mobile/social, ask "Make a vertical 9:16 version for Instagram Stories" as a refine follow-up',
    ],
}

CARDS['uc-property-opr-shock'] = {
    'title': 'OPR-Shock Pricing & Take-Up Response Pack — the Industry Power Move',
    'dept_tag': 'Strategy & Sales',
    'industry_tag': 'Property Development',
    'complexity': 'advanced',
    'apps': ['Excel', 'PowerPoint', 'Word', 'Outlook', 'Cowork'],
    'desc': 'When Bank Negara moves the OPR, Cowork rebuilds the entire pricing and take-up response pack in one prompt: home-loan affordability impact per unit type, township-by-township take-up sensitivity, pricing-ladder recalibration options, lender talking points, and a sales-gallery script for the next 30 days.',
    'skills': [
        'OPR-to-monthly-instalment translation per unit type and loan tenure',
        'Take-up sensitivity modelling per township × unit type × price band',
        'Pricing-ladder recalibration (price-hold + rebate / price-cut / tenure-extension / lender-rate-buydown)',
        'Cross-channel comms cascade (Lender Relations · Sales Galleries · External Comms)',
    ],
    'instructions': [
        'Open Cowork → model picker → Sonnet+Opus Advisor (financial reasoning benefits from the pairing)',
        'Attach the 4 source files',
        'Paste the prompt — Cowork builds the full response pack in parallel',
        'Hand to the GM and the Head of Sales within the same hour as the OPR move',
    ],
    'sample_files': [
        ('PD_Township_Pricing_Ladder.xlsx', 'xlsx'),
        ('PD_Take_Up_Sensitivity_Model.xlsx', 'xlsx'),
        ('PD_Lender_Panel_Rate_Sheet.xlsx', 'xlsx'),
        ('PD_Sales_Gallery_Activity_Tracker.xlsx', 'xlsx'),
    ],
    'prompts': [{
        'label': 'OPR-Shock response pack',
        'text': (
            "Bank Negara has just moved the OPR by [BPS] basis points to [NEW-RATE]%. Using the 4 attached files, in parallel, do all 6:\n"
            "1) Excel — affordability impact: for each of our 12 unit-type × price-band combinations, recompute the monthly instalment at the new OPR for 30-yr and 35-yr tenures, and show the % change vs the prior OPR. Flag rows where the instalment crosses the typical bank DSR ceiling for that band.\n"
            "2) Excel — take-up sensitivity: per township × unit type, model the expected 90-day take-up % at the new affordability level using the historical elasticity in the sensitivity model. Show base case, optimistic (+10%), pessimistic (-10%).\n"
            "3) Word — pricing-ladder recalibration memo (3 pages): 4 options — (a) price-hold with rebate package, (b) selective 1-3% price cut at sub-DSR-ceiling units, (c) tenure-extension push with lender partners, (d) lender-rate-buydown subsidy. Quantify expected take-up lift, GDV impact, and gross-margin impact per option. Recommend one.\n"
            "4) Excel — lender talking points: per panel lender, the rate sheet impact and the conversation we want our Lender Relations team to have. Output as a 1-row-per-lender brief.\n"
            "5) Word — sales-gallery script for the next 30 days: 5 customer-conversation playbooks (first-time buyer, upgrader, investor, MM2H buyer, EPF withdrawal buyer) addressing the OPR move and our response.\n"
            "6) Outlook — draft an email cascade: (a) to the Group CEO with the 1-pager recommendation, (b) to each Township GM with that township's specific take-up exposure, (c) to the Head of Lender Relations with the bank-by-bank action list.\n"
            "Cite the source file + sheet + row for every figure. Every recommendation carries the GDV and gross-margin impact attached."
        )
    }],
    'expected': [
        'Affordability impact table (Excel)',
        'Take-up sensitivity table per township (Excel)',
        '3-page pricing-ladder recalibration memo (Word)',
        'Lender-by-lender talking points (Excel)',
        'Sales-gallery 30-day script (Word, 5 playbooks)',
        '3-direction Outlook email cascade',
    ],
    'watch': [
        'Affordability impact translates rate moves into the instalment number buyers actually see',
        'Sensitivity ranges are explicit (base / optimistic / pessimistic) — no false precision',
        'Email cascade is differentiated by audience — CEO sees the recommendation, Township GMs see their own exposure',
    ],
    'honest': 'Elasticities are historical — actual buyer behaviour in a shock may differ. The recommendation is one informed view; the Pricing Committee owns the decision. Any lender-rate-buydown subsidy needs Treasury + Lender Relations sign-off before sales-gallery teams quote it.',
    'tips': [
        'Pin this prompt as a custom skill so the Strategy team can re-run within minutes of any OPR move',
        'Run a "what-if BNM cuts 25bps" version in parallel — quantifies the upside lever',
        'For Singapore / Indonesia operations, swap BNM for MAS / Bank Indonesia and the model still works',
    ],
}


# ── Contoso Life Assurance demo — additional distinctive use cases ─────

CARDS['uc-life-pitch-brief'] = {
    'title': 'Corporate Health Benefits Pitch Brief — Prospect-Facing',
    'dept_tag': 'Corporate Sales',
    'industry_tag': 'Life Insurance',
    'complexity': 'intermediate',
    'apps': ['Cowork', 'Word', 'PowerPoint'],
    'desc': 'For a corporate prospect (not yet a client), Copilot Chat scans public industry sources and produces a one-page pitch brief grounded in current employer benefit trends — wellness, mental health, family coverage, claims TAT — plus a 1-slide pitch hook and 3 conversation openers.',
    'skills': [
        'Public-source-only research (suitable for prospect-facing material)',
        'Employer-benefit-trend distillation (wellness, mental health, family coverage)',
        'Pitch-brief structure (hook, evidence, our differentiation, call-to-action)',
        'Conversation-opener generation calibrated to the prospect\'s industry',
    ],
    'instructions': [
        'Open Cowork → Researcher tool on',
        'Paste Prompt 1 — public-source pitch brief',
        'Paste Prompt 2 — 1-slide pitch hook as a PowerPoint single-slide ready to share',
        'Bring the brief and the slide to the prospect meeting',
    ],
    'sample_files': [],
    'prompts': [
        {
            'label': '1. One-page corporate pitch brief',
            'text': (
                "I am a Senior Manager at Contoso Life Assurance pitching corporate health benefits to a corporate prospect: [PROSPECT-NAME], a [INDUSTRY] company with [N-EMPLOYEES] employees in [COUNTRY]. Using public industry sources only (Swiss Re, McKinsey, LIMRA, Deloitte, Mercer, AAJI/LIAM benchmarks, regulator), produce a one-page pitch brief in Word:\n"
                "(1) Hook — what's changing in corporate health benefits in [INDUSTRY] this year (3 bullets);\n"
                "(2) Evidence — 3-5 datapoints from cited sources on wellness, mental health, family coverage, claims TAT;\n"
                "(3) Our differentiation — 3 things Contoso Life Assurance does that the prospect should hear about (placeholder our team will tailor);\n"
                "(4) Call-to-action — propose a 45-min benefits-design workshop in 3 weeks;\n"
                "(5) Source footer with hyperlinks and retrieval timestamps.\n"
                "Public sources only. No real customer or policy data. Professional collaborative tone, EN and BI."
            )
        },
        {
            'label': '2. 1-slide pitch hook',
            'text': (
                "Convert the pitch-brief Hook section into a single PowerPoint slide ready to share: title states the change in one sentence; 3 evidence bullets with source labels; bottom-right call-to-action 'Let's run a 45-min benefits-design workshop in 3 weeks'. Apply our brand template if available."
            )
        },
        {
            'label': '3. Three conversation openers',
            'text': (
                "Generate 3 conversation openers for the prospect's HR lead based on the brief. Each opener: 1 sentence asking about their current pain point, 1 sentence offering our perspective, 1 invitation to go deeper. Keep them human, not salesy."
            )
        },
    ],
    'expected': [
        '1-page corporate pitch brief (Word, EN + BI)',
        '1-slide pitch hook (PowerPoint, branded)',
        '3 conversation openers',
    ],
    'watch': [
        'Public sources only — pitch brief is safe to share externally',
        'Hook frames the change, not the product — earns the prospect\'s attention',
        'Conversation openers ask before they sell — relationship-first',
    ],
    'honest': 'Public-source pitch material is appropriate for first contact; once the prospect engages, switch to confidential materials with proper data clearance. Any claim about our differentiation is a placeholder — Corporate Sales and Marketing tailor with verified, signed-off product positioning.',
    'tips': [
        'Pin as a custom skill for every Account Manager — same flow, different prospect',
        'Add a 4th prompt — draft the outreach LinkedIn DM in the prospect HR lead\'s voice',
        'For ID variant, weight sources toward AAJI, OJK, and Mercer Indonesia benchmarks',
    ],
}

CARDS['uc-life-empathetic-claim-reply'] = {
    'title': 'Empathetic Reply to a Delayed Death Claim',
    'dept_tag': 'Claims & Customer Service',
    'industry_tag': 'Life Insurance',
    'complexity': 'beginner',
    'apps': ['Cowork', 'Outlook', 'Word'],
    'desc': 'For a bereaved beneficiary whose death claim has been delayed, Cowork drafts a deeply empathetic reply — acknowledges the loss, owns the delay, explains the next 3 steps with named owner and timeline, offers a named contact, and ends with a sincere apology. Tone calibrated for grief, not procedure.',
    'skills': [
        'Empathy-first drafting (grief-appropriate tone, no corporate hedging)',
        'Owning a service failure without making excuses',
        'Clear next-steps commitment with named owner + timeline',
        'Plain Bahasa Indonesia / Bahasa Malaysia variant for bereaved family\'s preferred language',
    ],
    'instructions': [
        'Open Cowork',
        'Paste the prompt with the case-specific context filled in (no PII)',
        'Review the draft sentence-by-sentence — empathy cannot be skipped',
        'Send via the Claims case file, not the generic Ops inbox',
    ],
    'sample_files': [],
    'prompts': [{
        'label': 'Empathetic claim-delay reply',
        'text': (
            "Draft a deeply empathetic email reply to Mr/Mrs [BENEFICIARY-FAMILY-NAME] (relationship to insured: [RELATIONSHIP]) whose death claim for the late [INSURED-NAME] (policy [POLICY-NUMBER-PLACEHOLDER], date of claim submission [SUBMISSION-DATE], number of days outstanding [DAYS]) has been delayed due to [REASON: e.g. medical-records verification pending from the hospital].\n\n"
            "The email must:\n"
            "(1) Open by acknowledging the family's loss — by name, in one sentence, no corporate filler;\n"
            "(2) Own the delay — name it, do not minimise it;\n"
            "(3) Explain the next 3 steps with a named owner (Claims Officer's name as placeholder) and a specific timeline for each;\n"
            "(4) Offer a direct named contact (Claims Officer name + direct phone) for any question, available [HOURS];\n"
            "(5) Close with a sincere apology in the writer's own voice — not a template phrase.\n\n"
            "Produce two versions side-by-side: English and Bahasa Indonesia. Tone must be calibrated for grief, not procedure — no jargon, no defensive language, no 'we apologise for any inconvenience caused'.\n"
            "Also draft a 2-line internal Teams handover note to the Claims Officer with the case status and the commitment we just made on email."
        )
    }],
    'expected': [
        'Empathetic email reply in EN',
        'Bahasa Indonesia version side-by-side',
        '2-line Teams handover note to Claims Officer',
    ],
    'watch': [
        'Email opens by name and acknowledges loss before anything else',
        'Delay is owned, not euphemised — no "challenges in processing"',
        'Each next step has an owner and a date — accountability is visible',
    ],
    'honest': 'Empathy cannot be outsourced. Cowork drafts a starting point; the Claims Officer reads every line aloud before sending and edits anything that sounds template-like. Any commitment of timeline must be one the team will actually meet — never promise dates you cannot keep to a grieving family.',
    'tips': [
        'For Takaful claims, add Tabarru-fund context if relevant to the family',
        'Save as a custom skill so every Claims Officer can produce a humane first draft within minutes',
        'Pair with a follow-up reminder skill — Outlook prompts the officer 3 days later to confirm closure',
        'Always have a supervisor review before the email goes out — empathy reviewed, not assumed',
    ],
}

CARDS['uc-life-plain-language-clause'] = {
    'title': 'Translate Policy Clause into Plain Bahasa Indonesia / Bahasa Malaysia',
    'dept_tag': 'Legal & Customer Education',
    'industry_tag': 'Life Insurance',
    'complexity': 'beginner',
    'apps': ['Cowork', 'Word'],
    'desc': 'A dense English policy clause (exclusions, waiting periods, free-look, suicide clauses, reinstatement) becomes a plain-language Bahasa Indonesia / Bahasa Malaysia version a non-expert can understand — with a 3-bullet "what this means for you", a 1-sentence "what is NOT covered", and a footer pointing to the binding original text.',
    'skills': [
        'Translation of insurance-technical English into plain BI / BM (not literal — concept-faithful)',
        'Consumer-friendly framing ("what this means for you" reframing)',
        'Explicit disclosure of exclusions in customer\'s language',
        'Footer pattern that preserves the binding original — regulator-safe',
    ],
    'instructions': [
        'Open Cowork',
        'Paste the source English clause (no PII; use template clauses for first pass)',
        'Paste Prompt 1 — Cowork produces the plain BI / BM version',
        'Run Prompt 2 to validate the translation by back-translating into English',
        'Run Prompt 3 to produce a 1-page customer letter format',
    ],
    'sample_files': [],
    'prompts': [
        {
            'label': '1. Translate clause into plain BI / BM',
            'text': (
                "Translate the following insurance policy clause into plain Bahasa Indonesia and plain Bahasa Malaysia (side-by-side). Target reader: a working adult with SPM / SMA-level education who is buying their first life insurance policy.\n\n"
                "[ENGLISH CLAUSE — paste full clause here, e.g. an Exclusions clause or a Free-Look Period clause]\n\n"
                "Output structure:\n"
                "(1) Plain BI version (max 120 words, sentences max 18 words, no insurance jargon)\n"
                "(2) Plain BM version (same constraints)\n"
                "(3) 'Apa artinya untuk Anda' / 'Apa maksudnya untuk anda' — 3 bullets translating into customer impact\n"
                "(4) 'Yang TIDAK ditanggung' / 'Yang TIDAK dilindungi' — 1 sentence flagging the most-misunderstood exclusion\n"
                "(5) Footer: 'Versi resmi yang mengikat secara hukum adalah teks Bahasa Inggris di [POLICY DOCUMENT SECTION]. Jika ada perbedaan interpretasi, teks asli yang berlaku.' / 'Versi rasmi yang mengikat dari segi undang-undang adalah teks Bahasa Inggeris di [SEKSYEN DOKUMEN POLISI]. Jika terdapat perbezaan tafsiran, teks asal yang terpakai.'\n"
                "Do NOT modify the legal meaning of the clause — translate, don't reinterpret. If a concept has no clean BI / BM equivalent, keep the English term in brackets after the BI / BM phrase."
            )
        },
        {
            'label': '2. Back-translate to validate',
            'text': "Now back-translate the plain BI version into English. Compare it to the original English clause and flag any change in meaning, omission, or addition. If any change is material, rewrite the BI version."
        },
        {
            'label': '3. Customer letter format',
            'text': "Format the plain BI / BM version as a 1-page customer letter on Contoso Life Assurance letterhead, opening with the customer's name, followed by the plain-language clause, the 'Apa artinya untuk Anda' section, the 'Yang TIDAK ditanggung' line, and a sign-off from the Customer Relationship Manager. Ready to send."
        },
    ],
    'expected': [
        'Plain BI version (≤ 120 words, ≤ 18-word sentences)',
        'Plain BM version side-by-side',
        '"What this means for you" 3 bullets',
        '"What is NOT covered" 1 sentence',
        'Back-translation validation report',
        '1-page customer letter format',
    ],
    'watch': [
        'Plain version preserves legal meaning — back-translation flags any drift',
        'Footer preserves binding original — regulator-safe translation',
        'Most-misunderstood exclusion called out explicitly — proactive consumer protection',
    ],
    'honest': 'The plain version is a customer-education aid, not the contract. The binding text remains the original. Legal must review any plain-language version sent to customers, and the binding-original footer is non-negotiable. For Takaful contracts, the Shariah Committee may also need to review the plain-language framing.',
    'tips': [
        'Pin as a custom skill — every product-launch clause gets a same-day plain version',
        'Run a "Mandarin / Tamil" variant for Malaysian segments',
        'Pair with the empathetic-reply skill for a complete customer-education + customer-care workflow',
    ],
}

CARDS['uc-life-ops-agent'] = {
    'title': 'No-Code Cowork Agent — Monthly Ops Review Workflow Packaged',
    'dept_tag': 'Operations',
    'industry_tag': 'Life Insurance',
    'complexity': 'intermediate',
    'apps': ['Cowork', 'Customize Page', 'OneDrive', 'Excel', 'Word', 'PowerPoint'],
    'desc': 'The monthly Ops Review workflow — pull TAT and STP figures, regenerate the operations dashboard, draft the Ops memo, prepare the slide pack, draft the Outlook agenda — gets packaged as a single named Cowork skill on the Customize page that the whole Ops team can trigger every month.',
    'skills': [
        'Guided skill builder on the Customize page (conversational authoring)',
        'Multi-source data pull (Excel claims log + Outlook commitments + SharePoint dashboard)',
        'Reusable team-shareable skill stored as Markdown in OneDrive',
        'Plugin-aware skill — uses installed plugins (e.g. ServiceNow for incidents) when present',
    ],
    'instructions': [
        'Open Cowork → top nav → Customize → Skills tab',
        'Click ➕ Add → Create new (guided)',
        'Paste Prompt 1 — Cowork interviews you about the workflow',
        'Save the skill — Cowork stores Markdown in /Cowork Skills/Ops/',
        'Share with the Ops team via the Customize page',
        'Every team member triggers by name: "Run Monthly Ops Review for [MONTH]"',
    ],
    'sample_files': [],
    'prompts': [
        {
            'label': '1. Author the skill (guided)',
            'text': (
                "I want to create a reusable Cowork skill called 'Monthly Ops Review' that the whole Operations team triggers every month.\n\n"
                "When triggered for a given month, the skill should:\n"
                "(1) Pull the claims TAT and STP figures from the Ops Claims Log Excel in our OneDrive 'Ops Monthly' folder;\n"
                "(2) Compare against the trailing-3-month average and against the latest industry benchmark (use the Researcher tool with our standard public sources: Swiss Re, McKinsey, LIMRA, AAJI / LIAM, regulator);\n"
                "(3) Regenerate the operations HTML dashboard with the new figures — green/amber/red on every KPI vs target;\n"
                "(4) Draft a 1-page Ops Memo (Word) for the COO with 3 bullets on what improved, 3 bullets on what slipped, 1 commitment for next month;\n"
                "(5) Draft a 6-slide pack (PowerPoint) for the monthly Ops Review meeting;\n"
                "(6) Draft an Outlook agenda email to the Ops Review attendees with the dashboard link and the pack attached.\n\n"
                "Walk me through naming, scoping, and saving this skill. Save it to /Cowork Skills/Ops/Monthly-Ops-Review.md and make it shareable with the Operations team only. The skill should accept one input parameter: [MONTH-AND-YEAR]."
            )
        },
        {
            'label': '2. Test run',
            'text': "Run the Monthly Ops Review skill for [PAST-MONTH] as a test, using last month's actual data, so I can verify each output before publishing the skill to the team."
        },
        {
            'label': '3. Iterate on the skill',
            'text': "Update the Monthly Ops Review skill: add a 7th deliverable — a 60-second voice brief for the COO's morning commute summarising the 3 'what slipped' bullets. Save the updated skill."
        },
    ],
    'expected': [
        'Named, reusable Cowork skill in OneDrive (Markdown)',
        'Team-shareable skill on the Customize > Skills tab',
        'Test-run that produces the first dashboard + memo + pack + email',
        'Iteration that adds the voice-brief 7th deliverable',
    ],
    'watch': [
        'Skill is conversation-authored — no syntax to learn',
        'Markdown file is editable directly in OneDrive when the workflow shifts',
        'Trigger by short name every month — no copy-paste of the long prompt',
        'Plugins (Jira, ServiceNow, Salesforce) integrate automatically if installed on the tenant',
    ],
    'honest': 'Skills run on demand. For fully hands-off Monday-morning delivery, pair with Power Automate to trigger the skill on a schedule. Shared skills carry the author\'s prompt verbatim — review for sensitive language before sharing with the broader team. The Researcher pull uses public sources; private competitor data remains out of scope.',
    'tips': [
        'Same pattern works for Weekly Claims Stand-up, Quarterly Persistency Review, Annual AAJI / LIAM Submission Pack',
        'Combine with the corporate-renewal skill — chain them for an end-of-quarter B2B refresh',
        'Use the model picker inside the skill: set it to Auto for production, Sonnet+Opus Advisor for the first time it runs after a process change',
    ],
}


# ── Contoso Beverages & Dairy demo — distinctive Beverage GM use cases ─

CARDS['uc-bev-strategic-landscape'] = {
    'title': 'Beverage & Dairy Sector Landscape — Researcher Critique + Model Council',
    'dept_tag': 'Strategy & Trade',
    'industry_tag': 'Food & FMCG',
    'complexity': 'intermediate',
    'apps': ['Cowork', 'Word'],
    'desc': 'Head of Department · Operations & Trade gets the Beverage & Dairy Manufacturing landscape in Malaysia in one Cowork run — Researcher Critique (Auto) for the default scan, Model Council when the call is too important for one model, then a 1-page HOD brief reconciling consensus and disagreement.',
    'skills': [
        'Researcher Critique mode — Auto picks the right model and shows its reasoning critique',
        'Model Council mode — frontier models answer in parallel; Cowork reconciles disagreements',
        'Sector intelligence specific to Malaysian beverage/dairy (SSB sugar tax, MyNutri front-of-pack labelling, SST, JAKIM halal, MOH, MOF, glass/PET supply, sugar tariff)',
        'Distilling council debate into a 1-page HOD brief with consensus + disagreement axis',
    ],
    'instructions': [
        'Open Cowork → Researcher tool → Mode: Critique (Auto)',
        'Paste Prompt 1 for the default landscape scan',
        'When Critique flags answer-confidence below 80%, switch to Mode: Model Council and paste Prompt 2',
        'Paste Prompt 3 to convert the council output into a 1-page Word brief for the HOD',
    ],
    'sample_files': [],
    'prompts': [
        {
            'label': '1. Critique (Auto) — default sector scan',
            'text': (
                "Researcher Critique mode. Scan the Beverage & Dairy Manufacturing landscape in Malaysia for the last 12 months. Cover:\n"
                "1) Regulatory shifts (SSB sugar-tax tier signals from MOF, MyNutri front-of-pack labelling enforcement by MOH, MS1500 / JAKIM halal certification cycle, SST treatment).\n"
                "2) Input-cost moves (raw sugar tariff, milk powder, glass and PET packaging, freight to ASEAN/GCC).\n"
                "3) Demand and channel (modern trade vs general trade share shift, foodservice recovery, e-commerce direct-to-consumer beverages, low/zero-sugar adoption).\n"
                "4) Top 5 listed Malaysian beverage/dairy manufacturers' Q reported volume, share, and gross-margin moves.\n"
                "5) Export tailwinds (ASEAN halal corridor, GCC halal demand, free-trade-agreement coverage).\n"
                "Output: maximum 14 bullets, each citing one authoritative source with retrieval timestamp. Use precise Malaysian FMCG/regulatory language (SSB, SST, MyNutri, JAKIM, MOH, MOF, Customs). End with 3 open questions for the HOD's Friday Trade & Strategy session."
            )
        },
        {
            'label': '2. Model Council — stress-test the strategic question',
            'text': (
                "Switch to Model Council. The question: 'Given the FY27 SSB tariff step signal and the rising sugar-tariff floor, should Contoso Beverages & Dairy accelerate the low/zero-sugar reformulation across the affected portfolio in the next 12 months, hold and pass-through pricing, or pivot the affected SKUs into the GCC halal-export channel?'\n"
                "Run the question across all available council models in parallel. Report:\n"
                "- Each model's recommended action and its top 2 reasons\n"
                "- Where the council agrees (consensus)\n"
                "- Where the council disagrees (disagreement axis — what would change the answer)\n"
                "- The deciding question the HOD should answer before choosing\n"
                "Format as a 2-column reconciliation table plus a 3-bullet executive note."
            )
        },
        {
            'label': '3. 1-page HOD brief in Word',
            'text': (
                "Convert the council output into a 1-page Word brief for the Head of Department · Operations & Trade. Sections: (1) The strategic question; (2) Council consensus in 3 bullets; (3) Council disagreement axis in 2 bullets; (4) Recommended decision with supporting rationale and the [ASSUMPTION:...] tag on every assumption; (5) The deciding question the HOD still owns. Tone: precise FMCG language, no marketing fluff. End with a source footer (hyperlinked) and 'Do not invent anything — use [PLACEHOLDER] for anything not in source'."
            )
        },
    ],
    'expected': [
        'Researcher Critique sector scan (14 bullets, sources)',
        'Model Council reconciliation table',
        '1-page HOD strategy brief (Word)',
    ],
    'watch': [
        'Critique mode shows model self-confidence — flags when to escalate to Council',
        'Council reveals model disagreement honestly — no false consensus',
        'Brief preserves disagreement instead of hiding it under a single recommendation',
        'Every assumption tagged [ASSUMPTION:...] so the HOD knows what is grounded vs inferred',
    ],
    'honest': 'Researcher pulls public data; competitor confidential pricing or unannounced launches stay out of scope. Council disagreement is signal — when 3 models out of 4 disagree, the right answer is usually to gather more data before deciding. The HOD owns the call; Cowork prepares the brief.',
    'tips': [
        'Re-run quarterly — the SSB and halal landscape shifts on every Budget announcement',
        'Add a 4th prompt that drafts the Friday Trade & Strategy session agenda from the 3 open questions',
        'For dairy specifically, weight sources toward DVS, MoA, and the Dairy Industry Association',
    ],
}

CARDS['uc-bev-create-infographic'] = {
    'title': 'Beverage Infographic Kit — Brand Portfolio, SSB Snapshot, Halal-Export',
    'dept_tag': 'Brand & Trade Marketing',
    'industry_tag': 'Food & FMCG',
    'complexity': 'beginner',
    'apps': ['Copilot Create', 'PowerPoint', 'Outlook'],
    'desc': 'Three on-brand A4 infographic posters from one Copilot Create session: (1) Brand Portfolio One-Pager for the trade review, (2) Sugar-Tax (SSB) & Compliance Snapshot for the HOD pre-read, (3) ASEAN & GCC Halal-Export Launch Plan for the Export Committee. Beverage corporate palette, thin outline icons, full-bleed A4.',
    'skills': [
        'Copilot Create with FMCG brand colour discipline (specific hex codes)',
        'Composing a full-A4 vertical infographic in one prompt (no empty bottom)',
        'Producing 3 thematically different posters from related prompts in one session',
        'Brand-aligned thin-outline-icon style (no clip-art, no stock photos of bottles or people)',
    ],
    'instructions': [
        'Open Microsoft 365 Copilot Chat → Create in left sidebar (or /create)',
        'Paste Prompt 1 for the Brand Portfolio one-pager — 4 variants generated',
        'Paste Prompt 2 for the SSB Compliance Snapshot',
        'Paste Prompt 3 for the Halal-Export Launch Plan',
        'Use Refine follow-ups to tighten any variant; download as PNG or PDF',
    ],
    'sample_files': [],
    'prompts': [
        {
            'label': '1. Brand Portfolio One-Pager',
            'text': (
                "Make a clean, premium one-page A4 infographic poster called 'Brand Portfolio · FY[YY]' for Contoso Beverages & Dairy. Use brand colours deep aqua (#0891B2) and warm cream (#FDE68A) on white, with a small dark slate for headings. Vertical A4, fill the entire page — no empty space at the bottom.\n\n"
                "Top: big bold title 'BRAND PORTFOLIO · FY[YY]'. Underneath: 'Beverages · Dairy · Functional · For the Trade & Brand Committee'.\n\n"
                "Then 4 big-number boxes: [PLACEHOLDER]M litres total volume YTD; [PLACEHOLDER]% modern-trade share; [PLACEHOLDER]% low/zero-sugar contribution; [PLACEHOLDER] active SKUs.\n\n"
                "Then a section called 'THE PORTFOLIO IN THREE TIERS' with 3 cards: (1) HERO BRANDS — flagship Cola / Dairy / Functional, role: scale + cash flow; (2) GROWTH BETS — low/zero-sugar, premium dairy, plant-based; (3) WATCH LIST — small / declining SKUs under rationalisation review.\n\n"
                "Then a 'Brand Compare' table (4 rows × 3 columns) — Hero / Growth / Watch with columns Volume share, Revenue share, Gross-margin band.\n\n"
                "'Risks we're managing' row of 3 icons: SSB sugar-tax exposure, raw-sugar tariff, glass/PET supply.\n\n"
                "Bottom: cream-aqua ribbon footer with a one-line recommendation and today's date.\n\n"
                "Style: clean modern sans-serif, thin outline icons (bottle, leaf, factory, scale), NO clip-art, NO stock photos. Fill the entire A4 page."
            )
        },
        {
            'label': '2. SSB Sugar-Tax & Compliance Snapshot',
            'text': (
                "Make a serious one-page A4 infographic poster called 'SSB & COMPLIANCE SNAPSHOT · FY[YY]' for Contoso Beverages & Dairy. Same brand palette. Vertical A4, fill the entire page.\n\n"
                "Top: 'SSB & COMPLIANCE SNAPSHOT'. Underneath: 'Sugar-Sweetened Beverage tier · MyNutri labelling · JAKIM halal · For the HOD pre-read'.\n\n"
                "4 big-number boxes: [PLACEHOLDER] SKUs in the SSB-affected band; RM [PLACEHOLDER]M annual SSB tariff at current threshold; [PLACEHOLDER]% portfolio already compliant with the proposed FY27 threshold; [PLACEHOLDER] days to MyNutri labelling cut-over.\n\n"
                "Section 'WHAT'S MOVING' with 3 cards: (1) MOF — FY27 SSB step signal (threshold tightening from 5g/100ml to 4g/100ml, tariff lift from RM 0.50/L to RM 0.65/L); (2) MOH — MyNutri front-of-pack labelling enforcement timeline; (3) JAKIM — halal certification cycle for the affected reformulated SKUs.\n\n"
                "'Compliance Compare' table (5 SKUs × 3 columns: current sugar g/100ml, proposed reformulated level, certification status).\n\n"
                "'Risks' icons row: reformulation timeline slip, consumer-acceptance on taste, trade cut-over logistics, credit-note treatment for in-trade stock.\n\n"
                "Bottom: ribbon footer 'OWNER: HOD Operations & Trade · REVIEW: monthly'.\n\n"
                "Style: clean modern sans-serif, thin outline icons (label, scale, factory, calendar). Fill the entire A4 page."
            )
        },
        {
            'label': '3. ASEAN & GCC Halal-Export Launch Plan',
            'text': (
                "Make a clean one-page A4 infographic poster called 'ASEAN & GCC HALAL-EXPORT LAUNCH PLAN · FY[YY]' for Contoso Beverages & Dairy. Same brand palette plus a small halal green accent. Vertical A4, fill the entire page.\n\n"
                "Top: 'HALAL-EXPORT LAUNCH · FY[YY]'. Underneath: 'ASEAN corridor · GCC priority markets · For the Export Committee'.\n\n"
                "4 big-number boxes: [PLACEHOLDER] export-ready SKUs; [PLACEHOLDER] target markets; RM [PLACEHOLDER]M Year-1 revenue target; [PLACEHOLDER]% gross-margin uplift vs domestic baseline.\n\n"
                "Section 'THREE-COUNTRY ROLLOUT' with 3 cards: (1) Indonesia + Vietnam (ASEAN-MAFTA / RCEP corridor, registration via BPOM and Vietnam MOH, distributor playbook); (2) UAE + Saudi Arabia (ESMA labelling, SFDA registration, FOB Jebel Ali logistics); (3) Future wave — Bangladesh, Pakistan, Egypt.\n\n"
                "'Launch Compare' table (3 markets × 4 columns: regulator, registration lead time, distributor partner status, Year-1 revenue target).\n\n"
                "'Risks' icons row: registration timeline, freight cost volatility, distributor capability, halal recertification.\n\n"
                "Bottom: ribbon footer 'COMMITMENT: 3 markets live by end of FY27 · REVIEW: monthly'.\n\n"
                "Style: clean modern sans-serif, thin outline icons (globe, ship, certificate, handshake). Fill the entire A4 page."
            )
        },
        {
            'label': '4. Refine — fill empty space + brand icons',
            'text': "If any of the three has empty space at the bottom, extend the sections or add a footer ribbon with the company name 'Contoso Beverages & Dairy' on the left and today's date on the right. Replace any non-brand icons with thin outline icons in our brand colour. Remove any emoji or stock photo of bottles, glasses, or people."
        },
    ],
    'expected': [
        '3 polished A4 infographic posters (PNG or PDF), brand-aligned',
        'Refined full-bleed brand-icon versions on follow-up',
        'Ready to drop into Outlook, Teams or PowerPoint',
    ],
    'watch': [
        'Create respects exact brand hex codes when you specify them',
        '3 thematically different posters from one Create session — Brand / Compliance / Export',
        'Refine follow-ups work in plain English — no design tools needed',
        'Enterprise Data Protection keeps the design inside your tenant',
    ],
    'honest': 'Copilot Create is great for the first 80%. Final pixel polish (legal disclaimers, exact logo position, accessibility colour contrast, halal logo placement) usually needs the design team. For external customer or regulator-facing pieces, Brand, Comms, Legal and Halal Compliance must sign off before posting.',
    'tips': [
        'Save each prompt as a reusable skill on the Customize page — every campaign refresh re-runs in seconds',
        'For Mandarin / BM / BI / Arabic variants, add "Translate the title and labels into [LANGUAGE]" as a refine follow-up',
        'For social, ask "Make a vertical 9:16 version for Instagram Stories" as a refine',
    ],
}

CARDS['uc-bev-ssb-tax-shock'] = {
    'title': 'FY27 SSB Sugar-Tax Step Response Pack — the Industry Power Move',
    'dept_tag': 'Strategy & Trade',
    'industry_tag': 'Food & FMCG',
    'complexity': 'advanced',
    'apps': ['Excel', 'Word', 'Outlook', 'Cowork'],
    'desc': 'When the Ministry of Finance signals the FY27 SSB tariff step, Cowork rebuilds the country response pack in one prompt: pricing scenarios with SKU sensitivity, SKU-by-SKU reformulation roadmap, distributor cut-over letter, and a 1-page CEO pre-read — fully grounded in the source KPI dashboard and strategic memo.',
    'skills': [
        'SSB threshold and tariff translation into per-SKU gross-profit impact',
        'Three-scenario pricing modelling (Hold price / Partial pass-through / Reformulate-and-relaunch)',
        'SKU-by-SKU reformulation roadmap with MyNutri labelling and consumer-acceptance test plan',
        'Distributor cut-over communication grounded on the new price ladder and credit-note treatment',
        'Source-grounded discipline — every assumption tagged [ASSUMPTION:...], every unknown tagged [VERIFY]',
    ],
    'instructions': [
        'Open Microsoft 365 Copilot Chat (or Researcher for deeper sources) → Cowork',
        'Reference the relevant source files with / (KPI dashboard + strategic memo)',
        'Paste the prompt — Cowork builds the 4 artefacts in parallel',
        'Pre-read each artefact before forwarding; CEO pre-read goes through HOD first',
    ],
    'sample_files': [
        ('BEV_KPI_Dashboard.xlsx', 'xlsx'),
        ('BEV_Strategic_Memo.docx', 'docx'),
    ],
    'prompts': [{
        'label': 'FY27 SSB tariff step response pack',
        'text': (
            "Act as Country Strategy lead supporting Head of Department · Operations & Trade at Contoso Beverages & Dairy. The FY27 SSB (Sugar-Sweetened Beverage) tariff step has just been signalled — assume the threshold tightens from 5g/100ml to 4g/100ml and the tariff lifts from RM 0.50/litre to RM 0.65/litre, effective the next fiscal year. Use /BEV_KPI_Dashboard.xlsx (volumes, share, current price ladder by SKU and region) and /BEV_Strategic_Memo.docx (low/zero-sugar reformulation stance).\n\n"
            "Produce four artefacts in parallel:\n\n"
            "1. PRICING SCENARIOS (Excel-style table) — three scenarios (Hold price / Partial pass-through / Reformulate-and-relaunch) with modelled volume sensitivity, share impact, and gross-profit impact for each affected SKU. Show the recommended scenario per SKU.\n\n"
            "2. SKU-BY-SKU REFORMULATION ROADMAP (Word, 1 page) — recommended new sugar level per SKU, MyNutri label impact, consumer-acceptance test plan (sample size, duration, decision gate), and trade cut-over date.\n\n"
            "3. DISTRIBUTOR LETTER (Word, 0.5 page) — clear, respectful, signed by Head of Department · Operations & Trade, explaining the new price ladder, cut-over logistics, MyNutri label change, and credit-note treatment for in-trade stock. Same letter in Bahasa Malaysia side-by-side.\n\n"
            "4. CEO PRE-READ (Word, 1 page) — what we are doing, why, expected P&L impact, the 3 risks we are watching (consumer-acceptance, distributor cut-over, halal recertification timeline), and 2 open questions for the Group Board.\n\n"
            "Use precise Malaysian FMCG / regulatory language (SSB, SST, JAKIM halal, MyNutri front-of-pack labelling, MOH, MOF, Customs). Flag every assumption with [ASSUMPTION:...]. Do not invent KPI numbers — pull them from the source file or mark [VERIFY]. End with the assumptions list and one open question."
        )
    }],
    'expected': [
        '3-scenario pricing impact table (Excel)',
        'SKU-by-SKU reformulation roadmap (Word, 1 page)',
        'Distributor cut-over letter EN + BM (Word, 0.5 page)',
        'CEO pre-read (Word, 1 page)',
        'Assumptions + open-question footer',
    ],
    'watch': [
        'Three scenarios shown side-by-side — no premature recommendation without the alternatives',
        'Every figure traceable to the source file + sheet + row — no invented KPIs',
        'Assumptions explicitly tagged — HOD knows what is grounded vs inferred',
        'Distributor letter in EN + BM — partner reads it in their preferred language',
    ],
    'honest': 'Volume elasticities are historical — actual consumer reaction to a sugar-tax step may differ. The recommendation is one informed view; the Pricing & Trade Committee owns the decision. Reformulation timelines depend on R&D, halal recertification, and consumer-acceptance test results — flag any cut-over date as provisional until those gates pass. CEO pre-read goes through HOD review before reaching the CEO.',
    'tips': [
        'Pin this prompt as a custom skill — Trade Strategy can re-run within minutes of any Budget speech',
        'Run a parallel "what if MoF goes 3g/100ml" version as a sensitivity stress test',
        'For Indonesia operations, swap MOF/MOH for Kemenkeu/BPOM and the model still works',
        'Pair with the halal-export infographic — pivot the affected SKUs into GCC if the domestic margin compresses too far',
    ],
}


# ── Contoso Coal & Resources demo — mining M&A meeting-minutes flow ─

CARDS['uc-coal-merger-recap'] = {
    'title': 'Mining M&A — Teams Merger Recap to Word Minutes',
    'dept_tag': 'Strategy & M&A',
    'industry_tag': 'Mining',
    'complexity': 'intermediate',
    'apps': ['Teams', 'Word', 'Cowork'],
    'desc': 'The GM missed the Potential Merger session. Teams Copilot summarises the meeting with owners and decisions; a reusable Word minutes template is generated once; then the transcript auto-fills the template — a defensible board-ready set of merger-committee minutes in minutes, not hours.',
    'skills': [
        'Teams recap from an audio meeting (Potential Merger scenario)',
        'Creating a reusable corporate meeting-minutes template (Word)',
        'Auto-filling the template from the merger transcript with owners, decisions, next steps',
        'Mining M&A discipline — decisions traceable, assumptions tagged, no invented commitments',
    ],
    'instructions': [
        'Teams → open the recorded Potential Merger meeting → Copilot pane → paste Prompt 1',
        'Word → New blank doc → Copilot compose → paste Prompt 2 to build the template once',
        'Word → open the template → Copilot pane → paste Prompt 3 with the transcript reference',
    ],
    'sample_files': [
        ('Coal_Merger_Transcript.docx', 'docx'),
    ],
    'prompts': [
        {
            'label': '1. Teams — recap the Potential Merger meeting',
            'text': (
                "Summarise the Potential Merger meeting for the GM who missed it. Structure:\n"
                "(1) Meeting context — who convened, who joined, what was the agenda\n"
                "(2) The proposed transaction in 3 bullets — target, rationale, indicative deal shape\n"
                "(3) Key decisions taken and by whom\n"
                "(4) Open questions and who owns each one\n"
                "(5) Next steps with owner and date\n"
                "Include quotations only where they are decisions or commitments. Do not invent numbers. Flag any commercial figure as [VERIFY] if not explicitly said. Use precise mining M&A language (target, EV, EBITDA, reserves, resources, JORC, permits, royalty, PROPER, IUP, ESDM). End with a 3-bullet 'what the GM needs to decide this week'."
            )
        },
        {
            'label': '2. Word — create the reusable minutes template',
            'text': (
                "Create a corporate meeting-minutes template for Contoso Coal & Resources' Merger & Acquisition Committee. Use a clean corporate style with dark slate headings on white. Include:\n"
                "- Header block: meeting title, date, time, location, chair, secretary, attendees, apologies\n"
                "- Section 1: Confirmation of the last minutes\n"
                "- Section 2: Matters arising\n"
                "- Section 3: Agenda items (repeatable block with: Item, Discussion summary, Decision, Owner, Due date)\n"
                "- Section 4: Risks & mitigants (table: Risk, Likelihood, Impact, Owner, Mitigation)\n"
                "- Section 5: Actions register (table: Action, Owner, Due, Status)\n"
                "- Section 6: Next meeting\n"
                "- Footer: 'Confidential — MAC members only'\n"
                "Leave [PLACEHOLDER] tokens on every field so the template is reusable. Save as MAC_Minutes_Template.docx."
            )
        },
        {
            'label': '3. Word — auto-fill the template from the transcript',
            'text': (
                "Using the transcript in /Coal_Merger_Transcript.docx, fill the MAC_Minutes_Template.docx. Rules: (1) Fill every field the transcript supports; leave [VERIFY] where the transcript is ambiguous. (2) In the Decision column, quote the decision-maker verbatim. (3) Do not invent owners — if unclear, write [VERIFY: owner]. (4) Preserve the exact monetary and reserve figures the transcript used; if none were quoted, write [VERIFY]. (5) End the doc with an 'Assumptions & open items' section listing every [VERIFY] token and one open question for the GM."
            )
        },
    ],
    'expected': [
        'Teams recap with decisions, owners, next steps',
        'Reusable MAC minutes template (Word)',
        'Filled MAC minutes with [VERIFY] tokens for anything not evidenced',
    ],
    'watch': [
        'Recap distinguishes decisions from discussion — no false consensus',
        'Template is reusable — the next MAC meeting reuses the same shape',
        '[VERIFY] tokens are honest — the GM sees what still needs confirming',
    ],
    'honest': 'Teams Copilot works on what the transcript actually says. If someone spoke off-mic or the discussion happened in a side channel, it will not appear. The MAC chair should always spot-check decisions and owners before circulating. Do not treat the auto-filled minutes as the official minutes until the chair signs off.',
    'tips': [
        'Save the template in a shared M&A SharePoint library so every MAC meeting reuses it',
        'Pair with the Analyst Agent to run the CFO / GM / Legal lens on any decision that has a financial impact',
        'For sensitive deals, run the recap on a dedicated MAC Teams channel with membership tightly scoped',
    ],
}


# ── Contoso General Assurance Indonesia demo — Insurance PMO + BPR ─

CARDS['uc-cga-raid-heatmap'] = {
    'title': 'Insurance PMO — RAID Heatmap + PivotTable in One Prompt',
    'dept_tag': 'PMO / Transformation',
    'industry_tag': 'General Insurance',
    'complexity': 'intermediate',
    'apps': ['Excel', 'Cowork'],
    'desc': 'The PMO Lead consolidates a live RAID log into an executive dashboard for the weekly CTO review in one Copilot in Excel prompt: summary counts, Owner × Severity PivotTable, conditional-formatting heatmap, top-5 critical items, and an overdue-item formula — each formula annotated in plain English.',
    'skills': [
        'Excel Copilot pane — one prompt, multiple artefacts on a new sheet',
        'Preserving the raw sheet untouched (audit-safe transformation)',
        'PivotTable + conditional formatting heatmap generated declaratively',
        'Plain-English formula annotation so PMs without Excel skills can maintain it',
    ],
    'instructions': [
        'Open the RAID log workbook',
        'Copilot pane → paste the prompt',
        'Review each formula and the plain-English annotation before circulating',
    ],
    'sample_files': [
        ('CGA_RAID_Log.xlsx', 'xlsx'),
    ],
    'prompts': [{
        'label': 'RAID_Dashboard in one prompt',
        'text': (
            "Consolidate this RAID log into an executive dashboard on a new sheet called RAID_Dashboard. I am the PMO Lead at Contoso General Assurance Indonesia; this will be reviewed weekly by the CTO. Use only the active workbook /CGA_RAID_Log.xlsx. Preserve the raw sheet untouched. On RAID_Dashboard produce:\n"
            "(1) a summary table counting items by category (Risk, Assumption, Issue, Dependency) and by severity (High, Medium, Low)\n"
            "(2) a PivotTable with Owner as rows and Severity as columns\n"
            "(3) heatmap conditional formatting on the PivotTable — red for High, amber for Medium, green for Low\n"
            "(4) a top-5 critical items list ranked by severity then status\n"
            "(5) a formula that flags any item overdue by more than 14 days\n"
            "Explain each formula in one line of plain English next to it. English. Do not invent values — use only what is in the sheet."
        )
    }],
    'expected': [
        'RAID_Dashboard sheet with 5 artefacts',
        'Raw sheet untouched',
        'Every formula annotated in plain English',
    ],
    'watch': [
        'One prompt produces multiple artefacts (summary, PivotTable, heatmap, top 5, overdue flag)',
        'Copilot preserves the audit trail — raw data untouched, new sheet is transparent',
        'Formula annotations let a non-technical PM maintain the dashboard',
    ],
    'honest': 'Copilot depends on clean column names and consistent status values in the raw sheet. If your RAID log has free-text severity ("Very high", "Med", "med-high") the counts will be off — normalise the raw sheet first. The dashboard is a snapshot: schedule the refresh weekly and treat any manual edits on the dashboard as temporary.',
    'tips': [
        'Add a 6th ask: "generate a 200-word Teams post summarising the top 3 risks" to reuse the dashboard for weekly comms',
        'Pin the prompt as a reusable skill on the Customize page — every project reuses the same shape',
        'For programme-level rollup, run once per project and stitch the outputs together in a portfolio workbook',
    ],
}

CARDS['uc-cga-multi-lob-claims-tat'] = {
    'title': 'Multi-LOB Claims TAT — the Insurance BPR Power Move',
    'dept_tag': 'Operations / BPR',
    'industry_tag': 'General Insurance',
    'complexity': 'advanced',
    'apps': ['Analyst Agent', 'Excel', 'Cowork'],
    'desc': "The Head of Operations diagnoses claims TAT loss across three lines of business (Motor, Property, Marine Cargo) and proposes a per-LOB automation portfolio for the board — in one Analyst-agent prompt grounded on the adjuster survey. Python-quality profiling, per-LOB bottleneck ranking, satisfaction correlation, chart, 6-initiative portfolio, and a CEO paragraph.",
    'skills': [
        'Analyst agent — Python-grade data analysis without writing code',
        'Multi-LOB analysis (Motor, Property, Marine Cargo) with correlation and ranking',
        'To-be automation portfolio with expected TAT reduction, complexity, and dependency',
        'Ground-only discipline — no fabricated values; missing data flagged',
    ],
    'instructions': [
        'Copilot Chat → Switch agent → Analyst',
        'Attach /CGA_ClaimsOperationsSurvey.xlsx',
        'Paste the prompt',
        'Review the CEO paragraph with the transformation lead before forwarding',
    ],
    'sample_files': [
        ('CGA_ClaimsOperationsSurvey.xlsx', 'xlsx'),
    ],
    'prompts': [{
        'label': 'Multi-LOB claims TAT diagnosis + automation portfolio',
        'text': (
            "Analyse the attached multi-LOB adjuster survey and produce a data-driven bottleneck diagnosis with a per-LOB automation portfolio.\n\n"
            "I am the Head of Operations at Contoso General Assurance Indonesia. The Board wants a business case for a claims transformation this quarter. Use only the 40 rows in /CGA_ClaimsOperationsSurvey.xlsx which cover three lines of business (Motor, Property, Marine Cargo) across Jakarta, Surabaya, Medan, Bandung and Semarang. Do not fabricate values; if data is missing, say so.\n\n"
            "Deliverables in order:\n"
            "(1) Python-quality data profile of the sheet (row count, column types, missing-value pattern)\n"
            "(2) top 5 bottlenecks ranked by TAT loss in days per claim and total FTE hours, quantified per LOB (Motor vs Property vs Marine Cargo)\n"
            "(3) correlation between adjuster satisfaction and bottleneck category, per LOB\n"
            "(4) a chart showing average TAT per bottleneck category, grouped by LOB\n"
            "(5) proposed to-be automation portfolio of 6 initiatives (2 per LOB) with expected TAT reduction per LOB, complexity 1 to 5, and dependency on existing systems\n"
            "(6) one paragraph summary for the CEO covering all three LOBs\n\n"
            "English, tables and one chart, no opinions without a data citation."
        )
    }],
    'expected': [
        'Per-LOB bottleneck ranking with quantified TAT loss',
        'Adjuster-satisfaction correlation per LOB',
        'Chart: TAT per bottleneck category grouped by LOB',
        '6-initiative automation portfolio with dependency map',
        'CEO paragraph',
    ],
    'watch': [
        'Analyst runs Python-grade analysis but you do not write Python',
        'Every insight is data-cited; opinions without citation are not allowed',
        'Missing data is flagged, not fabricated',
        'Automation portfolio explicitly maps to complexity + dependency — implementation-ready',
    ],
    'honest': 'A 40-row survey is a starting point, not the whole truth. The bottleneck ranking will be directionally right but the automation portfolio must be validated with a wider sample and with the adjuster union / staff council before board sign-off. The CEO paragraph should always be reviewed by the Head of Operations personally — do not forward Analyst output unedited.',
    'tips': [
        'Re-run per quarter with a fresh survey to trend the TAT loss over time',
        'Pair with the autonomous weekly RAID digest — the portfolio becomes the transformation programme',
        'For OJK submissions, extract the LOB-level TAT numbers into the RBC / statutory return template',
    ],
}

CARDS['uc-cga-autonomous-raid-digest'] = {
    'title': 'Cowork Frontier — Autonomous Weekly RAID Digest',
    'dept_tag': 'PMO / Transformation',
    'industry_tag': 'General Insurance',
    'complexity': 'advanced',
    'apps': ['Cowork', 'Outlook', 'Teams'],
    'desc': 'The PMO Lead sets up a Cowork Frontier scheduled task: every Friday at 16:00 Jakarta, Cowork reads the shared PMO folder, refreshes the RAID dashboard, flags new High-severity items and overdue items, drafts a 200-word sponsor Teams post, and drafts a CTO email with the top-3 decisions — held for the PMO Lead to approve before send.',
    'skills': [
        'Cowork Frontier scheduled task (weekly, timezone-aware)',
        'Multi-artefact autonomous run (refresh + flag + draft Teams + draft email)',
        'Approve-before-send gate — no autonomous outbound',
        'Portfolio-level view spanning 5 concurrent transformation projects',
    ],
    'instructions': [
        'Copilot Cowork (Frontier) → Set as scheduled task → Weekly',
        'Time: Friday 16:00 Jakarta',
        'Paste the prompt',
        'Confirm the folder read-scope + the approval gate before saving the task',
    ],
    'sample_files': [],
    'prompts': [{
        'label': 'Autonomous weekly RAID digest',
        'text': (
            "Run a weekly autonomous RAID digest for the CGA Indonesia transformation portfolio (Motor & Property Claims Platform Modernisation, Marine Cargo Digital Onboarding, Bancassurance Distribution Integration, Sharia Product Launch, Auto Manufacturer Partnership API) every Friday at 16:00 Jakarta time.\n\n"
            "I am the PMO Lead at Contoso General Assurance Indonesia. The CTO and sponsors want a consistent Friday inbox drop that summarises the week without me having to build it.\n\n"
            "Read the shared PMO folder in OneDrive weekly. Include: the latest RAID log, the latest steering brief, and any status reports uploaded in the last 7 days.\n\n"
            "Every Friday:\n"
            "(1) refresh the RAID_Dashboard sheet\n"
            "(2) flag any new High-severity item, any item overdue by more than 14 days, and any owner with more than 3 open items\n"
            "(3) draft a 200-word Teams post for the sponsor channel\n"
            "(4) draft an email to the CTO with the top-3 decisions needed next week and a link to the dashboard\n\n"
            "Send only after I approve. English, calm and factual."
        )
    }],
    'expected': [
        'Weekly refreshed RAID_Dashboard',
        'Draft Teams post (200 words) — held for approval',
        'Draft CTO email with top-3 decisions — held for approval',
        'Zero autonomous outbound without PMO Lead sign-off',
    ],
    'watch': [
        'Cowork Frontier runs on schedule without a human trigger',
        'Approval gate is explicit — nothing leaves without the PMO Lead pressing Send',
        'Read-scope is fenced to the PMO folder — no over-reach into unrelated content',
        'Portfolio-level rollup (5 projects) in a single weekly artefact',
    ],
    'honest': 'Frontier scheduled tasks are powerful — the discipline is in the fence. Keep the read-scope tight (this specific folder only), keep the send-scope gated (approve before send), and audit the task log weekly. If the CTO ever complains about a noisy inbox, tighten the "top-3 decisions" ask to "top-1 decision + 2 FYIs".',
    'tips': [
        'Version-control the prompt — treat the scheduled task like production code',
        'Add a monthly variant that rolls up the four weekly digests into a Steering Committee pre-read',
        'Pair with the multi-LOB claims TAT card — the transformation programme becomes the source of truth for the digest',
    ],
}


# ---------------- DEPARTMENT-SPECIFIC CARDS ----------------

CARDS['uc-fin-monthend'] = {
    'title': 'Month-End Close Acceleration',
    'dept_tag': 'Finance',
    'industry_tag': None,
    'complexity': 'intermediate',
    'apps': ['Excel', 'PowerPoint', 'Word', 'Outlook', 'Teams'],
    'desc': 'Group close compressed by 2 days — Cowork orchestrates intercompany, accruals, flux narrative and Audit Committee pack.',
    'skills': [
        'Intercompany reconciliation + cut-off',
        'Variance flux narrative drafting',
        'Audit-Committee-ready storytelling',
    ],
    'instructions': [
        'Open Cowork',
        'Attach the 3 source files',
        'Paste the prompt',
    ],
    'sample_files': [
        ('FIN_Trial_Balance.xlsx', 'xlsx'),
        ('FIN_Intercompany_Schedule.xlsx', 'xlsx'),
        ('FIN_Accounting_Policy.docx', 'docx'),
    ],
    'prompts': [{
        'label': 'Month-end sprint',
        'text': (
            "Using the 3 attached files, build the [MONTH-END] close sprint. In parallel:\n"
            "1) Excel — intercompany match grid with break list + proposed JE clearances.\n"
            "2) Excel — flux table P&L line vs budget vs prior with auto-generated explanation column.\n"
            "3) PowerPoint — 8-slide CFO / Audit Committee deck.\n"
            "4) Word — narrative commentary memo cross-referencing every flux > [THRESHOLD].\n"
            "5) Outlook — division CFO emails for outstanding sign-offs with action items.\n"
            "Cite the file + tab + row for every figure. Flag any policy departure (revenue recognition / capitalisation / lease)."
        )
    }],
    'expected': [
        'Intercompany match grid',
        'Flux table',
        'CFO / AC deck',
        'Narrative memo',
        'Division CFO emails',
    ],
    'watch': [
        'Policy departures surfaced',
        'Flux explanations specific, not generic',
    ],
    'honest': 'Cowork drafts the narrative — the Group Controller reviews every line that ties to a JE before close is signed off.',
    'tips': [
        'Variation: add a quarterly Audit-Committee-only flux deck',
        'Variation: build a close-day status tracker shared in Teams',
    ],
}

CARDS['uc-hr-perfreview'] = {
    'title': 'Annual Performance Review Calibration',
    'dept_tag': 'Human Resources',
    'industry_tag': None,
    'complexity': 'intermediate',
    'apps': ['Excel', 'PowerPoint', 'Word', 'Outlook', 'Teams'],
    'desc': 'Group-wide calibration cycle — Cowork builds the distribution analysis, manager calibration pack and manager-to-employee letters.',
    'skills': [
        'Performance distribution analysis vs guidance curve',
        'Manager calibration framing',
        'Differentiated employee-letter tone (exceed / meet / improve)',
    ],
    'instructions': [
        'Open Cowork',
        'Attach the 3 source files',
        'Paste the prompt',
    ],
    'sample_files': [
        ('HR_Performance_Ratings.xlsx', 'xlsx'),
        ('HR_Compensation_Ranges.xlsx', 'xlsx'),
        ('HR_Performance_Policy.docx', 'docx'),
    ],
    'prompts': [{
        'label': 'Calibration sprint',
        'text': (
            "Using the 3 attached files, build the [YEAR] calibration sprint. In parallel:\n"
            "1) Excel — rating distribution per business unit vs guidance + outlier report.\n"
            "2) PowerPoint — 10-slide ExCo calibration deck.\n"
            "3) Word — manager calibration brief (per business unit) for the review meeting.\n"
            "4) Outlook — manager-to-employee letter templates: 3 tones (exceed / meet / improve).\n"
            "5) Teams — HR Business Partner brief on common calibration pushbacks and how to handle.\n"
            "Cite the file + tab for every distribution number. Flag any unit whose top-rating quota exceeds policy."
        )
    }],
    'expected': [
        'Distribution analysis',
        'ExCo calibration deck',
        'Per-BU manager briefs',
        '3 employee-letter templates',
        'HRBP brief',
    ],
    'watch': [
        'Top-rating quota breaches surfaced',
        'Tone differentiated, not generic',
    ],
    'honest': 'Calibration is about people — Cowork structures the data; HRBPs run the nuanced conversation with managers.',
    'tips': [
        'Variation: add a gender / diversity-lens distribution check',
        'Variation: prep talent-review (9-box) input from the same data',
    ],
}

CARDS['uc-hr-onboarding'] = {
    'title': 'Senior Hire Onboarding Pack',
    'dept_tag': 'Human Resources',
    'industry_tag': None,
    'complexity': 'basic',
    'apps': ['Word', 'PowerPoint', 'Outlook', 'Teams'],
    'desc': 'Senior leadership hire — Cowork builds the 30-60-90 plan, stakeholder map, induction calendar and welcome comms.',
    'skills': [
        '30-60-90 onboarding plan construction',
        'Stakeholder mapping for new joiner',
        'Welcome / induction tone shaping',
    ],
    'instructions': [
        'Open Cowork',
        'Attach the 3 source files',
        'Paste the prompt',
    ],
    'sample_files': [
        ('HR_Role_JD.docx', 'docx'),
        ('HR_Org_Chart.docx', 'docx'),
        ('HR_Onboarding_Playbook.docx', 'docx'),
    ],
    'prompts': [{
        'label': 'Onboarding pack',
        'text': (
            "Using the 3 attached files, build the onboarding pack for [NAME] joining as [ROLE]. In parallel:\n"
            "1) Word — 30-60-90 plan with concrete deliverables and stakeholders to meet.\n"
            "2) PowerPoint — 6-slide induction deck (org / strategy / team / role / norms).\n"
            "3) Outlook — welcome email from the line manager + introductions to the top 12 stakeholders.\n"
            "4) Word — week-1 calendar template (induction sessions + meet-and-greet schedule).\n"
            "5) Teams — internal announcement post for the team channel.\n"
            "Cite the playbook section for every onboarding step. Flag any compliance / certification step that must clear in week 1."
        )
    }],
    'expected': [
        '30-60-90 plan',
        'Induction deck',
        'Welcome + intro emails',
        'Week-1 calendar',
        'Team announcement',
    ],
    'watch': [
        'Compliance gates surfaced',
        'Stakeholder list realistic, not bloated',
    ],
    'honest': 'Onboarding is relational — Cowork structures the calendar; the line manager owns the human side.',
    'tips': [
        'Variation: prep a 100-day check-in survey',
        'Variation: include a buddy / mentor pairing suggestion',
    ],
}

CARDS['uc-legal-contract'] = {
    'title': 'Major Contract Review Sprint',
    'dept_tag': 'Legal',
    'industry_tag': None,
    'complexity': 'advanced',
    'apps': ['Word', 'Excel', 'Outlook', 'Teams'],
    'desc': 'Strategic supplier contract — Cowork builds the risk matrix, redline brief and negotiation playbook.',
    'skills': [
        'Risk-clause identification + risk-rating',
        'Redline drafting with rationale',
        'Negotiation playbook with fallback positions',
    ],
    'instructions': [
        'Open Cowork',
        'Attach the 3 source files',
        'Paste the prompt',
    ],
    'sample_files': [
        ('LEG_Draft_Contract.docx', 'docx'),
        ('LEG_Internal_Standards.docx', 'docx'),
        ('LEG_Prior_Disputes_Register.xlsx', 'xlsx'),
    ],
    'prompts': [{
        'label': 'Contract review',
        'text': (
            "Using the 3 attached files, review the [CONTRACT] draft. In parallel:\n"
            "1) Word — redlined version with clause-by-clause issue notes.\n"
            "2) Excel — risk matrix (each clause × likelihood × impact × proposed treatment).\n"
            "3) Word — negotiation playbook with target / fallback / walk-away positions per clause.\n"
            "4) Outlook — covering note to the GC + business sponsor summarising top 5 risks.\n"
            "5) Teams — Legal Ops brief on the redline submission timeline.\n"
            "Cite the Internal Standards document section for every divergence. Flag any clause that has triggered a prior dispute."
        )
    }],
    'expected': [
        'Redlined contract',
        'Risk matrix',
        'Negotiation playbook',
        'GC / sponsor covering note',
        'Legal Ops brief',
    ],
    'watch': [
        'Dispute-history flags surfaced',
        'Walk-away clauses identified',
    ],
    'honest': 'Cowork accelerates the first pass — the Senior Counsel owns final position on every contentious clause.',
    'tips': [
        'Variation: add a sanctions / export-control screen overlay',
        'Variation: prep a one-page deal-breaker summary for the sponsor',
    ],
}

CARDS['uc-risk-appetite'] = {
    'title': 'Annual Risk Appetite Refresh',
    'dept_tag': 'Risk',
    'industry_tag': None,
    'complexity': 'advanced',
    'apps': ['Excel', 'PowerPoint', 'Word', 'Outlook', 'Teams'],
    'desc': 'Group Risk Appetite Statement refresh — Cowork builds the back-test, top-down vs bottom-up reconciliation and Board paper.',
    'skills': [
        'Risk-appetite metric back-testing',
        'Top-down / bottom-up reconciliation',
        'Board paper construction (concise + defensible)',
    ],
    'instructions': [
        'Open Cowork',
        'Attach the 3 source files',
        'Paste the prompt',
    ],
    'sample_files': [
        ('RSK_Current_RAS.docx', 'docx'),
        ('RSK_Metric_History.xlsx', 'xlsx'),
        ('RSK_Top_Risks_Register.xlsx', 'xlsx'),
    ],
    'prompts': [{
        'label': 'RAS refresh pack',
        'text': (
            "Using the 3 attached files, build the [YEAR] Risk Appetite refresh pack. In parallel:\n"
            "1) Excel — 24-month back-test of every appetite metric vs actual.\n"
            "2) Excel — top-down / bottom-up appetite reconciliation by business unit.\n"
            "3) PowerPoint — 12-slide Risk Committee deck.\n"
            "4) Word — Board paper recommending the refreshed statement with rationale per change.\n"
            "5) Outlook — division Risk Officer alignment emails with the BU-level proposed numbers.\n"
            "Cite the file + tab for every metric. Flag any metric that was breached more than 2 months in the last 12."
        )
    }],
    'expected': [
        'Metric back-test',
        'Top-down / bottom-up recon',
        'Risk Committee deck',
        'Board paper',
        'Division Risk Officer emails',
    ],
    'watch': [
        'Breached metrics flagged',
        'Bottom-up consistency tested, not assumed',
    ],
    'honest': 'Risk appetite is a Board decision — Cowork builds the case; the CRO defends the statement at the Risk Committee.',
    'tips': [
        'Variation: add a stress overlay on a single severe scenario',
        'Variation: prep a simplified one-page version for managers',
    ],
}

CARDS['uc-strat-marketscan'] = {
    'title': 'Strategic Market Scan Pack',
    'dept_tag': 'Strategy',
    'industry_tag': None,
    'complexity': 'intermediate',
    'apps': ['Word', 'PowerPoint', 'Excel', 'Outlook', 'Teams'],
    'desc': 'Quarterly strategic scan — Cowork builds the macro / competitor / regulatory / technology view and strategic implications brief.',
    'skills': [
        'Multi-lens market scan structuring',
        'Strategic-implication framing',
        'Differentiated stakeholder briefing',
    ],
    'instructions': [
        'Open Cowork',
        'Attach the 3 source files',
        'Paste the prompt',
    ],
    'sample_files': [
        ('STR_Macro_Inputs.docx', 'docx'),
        ('STR_Competitor_Tracker.xlsx', 'xlsx'),
        ('STR_Strategic_Plan.docx', 'docx'),
    ],
    'prompts': [{
        'label': 'Market scan pack',
        'text': (
            "Using the 3 attached files, build the [QUARTER] strategic scan. In parallel:\n"
            "1) Word — 4-lens scan: macro / competitor / regulatory / technology with key moves.\n"
            "2) PowerPoint — 12-slide ExCo deck.\n"
            "3) Excel — competitor move tracker updated with the new quarter's data.\n"
            "4) Outlook — Division CEO emails highlighting moves most relevant to their P&L.\n"
            "5) Teams — Strategy team brief on follow-up workstreams.\n"
            "Cite the source document + section for every claim. Flag any move that contradicts the assumptions in the current Strategic Plan."
        )
    }],
    'expected': [
        '4-lens scan',
        'ExCo deck',
        'Updated tracker',
        'Division CEO emails',
        'Strategy team brief',
    ],
    'watch': [
        'Plan-contradicting moves surfaced',
        'BU relevance differentiated, not generic',
    ],
    'honest': 'Cowork synthesises what is on the page — the Head of Strategy must add the unwritten signals from market conversations.',
    'tips': [
        'Variation: add a 12-quarter trend view on the top 3 competitors',
        'Variation: prep a Board horizon-scan version (annual)',
    ],
}

CARDS['uc-marketing-campaign'] = {
    'title': 'Group Brand Campaign Pack',
    'dept_tag': 'Marketing',
    'industry_tag': None,
    'complexity': 'intermediate',
    'apps': ['Word', 'PowerPoint', 'Excel', 'Outlook', 'Teams'],
    'desc': 'Group umbrella brand campaign — Cowork builds the narrative, channel plan, divisional adaptation pack and agency brief.',
    'skills': [
        'Group brand-narrative articulation',
        'Multi-channel media planning',
        'Divisional adaptation of a single master campaign',
    ],
    'instructions': [
        'Open Cowork',
        'Attach the 3 source files',
        'Paste the prompt',
    ],
    'sample_files': [
        ('MKT_Brand_Strategy.docx', 'docx'),
        ('MKT_Channel_Performance.xlsx', 'xlsx'),
        ('MKT_Divisional_Brands.docx', 'docx'),
    ],
    'prompts': [{
        'label': 'Brand campaign pack',
        'text': (
            "Using the 3 attached files, build the [YEAR] umbrella brand campaign pack. In parallel:\n"
            "1) Word — master campaign narrative + 3 audience-tailored versions.\n"
            "2) Excel — channel + spend plan across 8 channels with KPI per channel.\n"
            "3) PowerPoint — 12-slide divisional adaptation pack (how each division tailors).\n"
            "4) Word — agency brief for the creative production phase.\n"
            "5) Outlook + Teams — Group Comms + Division CMO alignment emails and Teams briefing.\n"
            "Cite the Brand Strategy section for every brand-rule reference. Flag any divisional brand that conflicts with the umbrella narrative."
        )
    }],
    'expected': [
        'Campaign narrative + 3 versions',
        'Channel + spend plan',
        'Divisional adaptation pack',
        'Agency brief',
        'CMO alignment emails',
    ],
    'watch': [
        'Brand-architecture conflicts surfaced',
        'Channel mix proportional to objective',
    ],
    'honest': 'Brand language is craft work — Cowork drafts the structure; the CMO + creative lead refine the words.',
    'tips': [
        'Variation: add a measurement framework (pre/post survey + brand-tracker)',
        'Variation: prep a crisis-comms appendix',
    ],
}

CARDS['uc-esg-disclosure'] = {
    'title': 'Annual ESG Disclosure Pack',
    'dept_tag': 'ESG',
    'industry_tag': None,
    'complexity': 'advanced',
    'apps': ['Word', 'Excel', 'PowerPoint', 'Outlook', 'Teams'],
    'desc': 'IFRS S1 / S2 / GRI / Bursa annual disclosure — Cowork builds the data pack, narrative sections and stakeholder pack.',
    'skills': [
        'Disclosure-standard mapping (IFRS S1/S2, GRI, Bursa)',
        'Climate-scenario narrative drafting',
        'Multi-stakeholder disclosure framing',
    ],
    'instructions': [
        'Open Cowork',
        'Attach the 3 source files',
        'Paste the prompt',
    ],
    'sample_files': [
        ('ESG_Data_Pack.xlsx', 'xlsx'),
        ('ESG_Materiality_Assessment.docx', 'docx'),
        ('ESG_Standards_Mapping.docx', 'docx'),
    ],
    'prompts': [{
        'label': 'Disclosure pack',
        'text': (
            "Using the 3 attached files, build the [YEAR] ESG disclosure pack. In parallel:\n"
            "1) Word — narrative sections per material topic mapped to IFRS S1/S2 / GRI / Bursa requirements.\n"
            "2) Excel — data pack with assurance trail per metric (source / owner / methodology).\n"
            "3) PowerPoint — 14-slide ESG Council pack.\n"
            "4) Word — investor / regulator covering letter.\n"
            "5) Outlook + Teams — division ESG champion alignment emails + Council Teams brief.\n"
            "Cite the file + tab for every metric. Flag any metric where prior-year and current-year data use different methodology."
        )
    }],
    'expected': [
        'Narrative sections',
        'Data pack with assurance trail',
        'ESG Council pack',
        'Stakeholder covering letter',
        'Division champion emails',
    ],
    'watch': [
        'Methodology changes surfaced',
        'Standards mapping explicit per section',
    ],
    'honest': 'ESG disclosure has legal weight — Cowork drafts; external assurance provider tests the data; Group GC signs off the language.',
    'tips': [
        'Variation: add a peer-benchmark slide on top 5 metrics',
        'Variation: prep a simplified version for retail investors',
    ],
}

CARDS['uc-ops-sop'] = {
    'title': 'Cross-BU SOP Harmonisation',
    'dept_tag': 'Operations',
    'industry_tag': None,
    'complexity': 'intermediate',
    'apps': ['Word', 'Excel', 'PowerPoint', 'Outlook', 'Teams'],
    'desc': 'Five BUs run differing variants of the same process — Cowork harmonises into one SOP with BU-specific addenda.',
    'skills': [
        'SOP variation extraction across BUs',
        'Harmonised SOP construction + BU-specific exception annex',
        'Change-management framing for SOP rollout',
    ],
    'instructions': [
        'Open Cowork',
        'Attach the 3 source files',
        'Paste the prompt',
    ],
    'sample_files': [
        ('OPS_BU1_Procedure.docx', 'docx'),
        ('OPS_BU2_Procedure.docx', 'docx'),
        ('OPS_BU3_Procedure.docx', 'docx'),
    ],
    'prompts': [{
        'label': 'SOP harmonisation',
        'text': (
            "Using the 3 attached files (and 2 more I will add), build the harmonised [PROCESS] SOP. In parallel:\n"
            "1) Word — master harmonised SOP with cross-references.\n"
            "2) Excel — variation matrix showing each BU's current step vs harmonised step.\n"
            "3) PowerPoint — 8-slide change-management deck for the rollout.\n"
            "4) Word — BU-specific exception annex (only where exception is justified).\n"
            "5) Outlook + Teams — BU Ops Lead alignment emails + change champion Teams brief.\n"
            "Cite the source procedure document + section for every variation. Flag any BU step that conflicts with policy."
        )
    }],
    'expected': [
        'Master harmonised SOP',
        'Variation matrix',
        'Change-mgmt deck',
        'BU exception annex',
        'BU Ops Lead alignment',
    ],
    'watch': [
        'Policy-conflicts surfaced',
        'Justified exceptions preserved, unjustified ones removed',
    ],
    'honest': 'SOP harmonisation has change-management cost — Cowork structures; the COO must own the rollout politically.',
    'tips': [
        'Variation: add a training calendar appendix',
        'Variation: prep a 90-day post-rollout audit template',
    ],
}

CARDS['uc-corpsec-agm'] = {
    'title': 'AGM Preparation Sprint',
    'dept_tag': 'Corporate Secretarial',
    'industry_tag': None,
    'complexity': 'intermediate',
    'apps': ['Word', 'PowerPoint', 'Excel', 'Outlook', 'Teams'],
    'desc': 'Listed-co AGM in 6 weeks — Cowork builds the notice + circular, voting analysis and shareholder Q&A bank.',
    'skills': [
        'AGM notice + circular drafting',
        'Voting / proxy analysis',
        'Shareholder Q&A anticipation',
    ],
    'instructions': [
        'Open Cowork',
        'Attach the 3 source files',
        'Paste the prompt',
    ],
    'sample_files': [
        ('CSEC_Last_AGM_Minutes.docx', 'docx'),
        ('CSEC_Shareholder_Register.xlsx', 'xlsx'),
        ('CSEC_AGM_Resolutions.docx', 'docx'),
    ],
    'prompts': [{
        'label': 'AGM pack',
        'text': (
            "Using the 3 attached files, build the [YEAR] AGM prep pack. In parallel:\n"
            "1) Word — AGM notice + circular per Listing Rules.\n"
            "2) Excel — voting / proxy analysis vs prior years for each resolution.\n"
            "3) PowerPoint — 12-slide Board pre-AGM briefing.\n"
            "4) Word — shareholder Q&A bank with draft answers (40-60 anticipated questions).\n"
            "5) Outlook + Teams — major-shareholder alignment letters + Investor Relations Teams brief.\n"
            "Cite the source document + section for every resolution. Flag any resolution that requires special-resolution majority and has historically been close."
        )
    }],
    'expected': [
        'Notice + circular',
        'Voting / proxy analysis',
        'Board pre-AGM brief',
        'Shareholder Q&A bank',
        'IR alignment',
    ],
    'watch': [
        'Close-vote resolutions flagged',
        'Special-resolution thresholds confirmed',
    ],
    'honest': 'AGM compliance is regulated — Cowork drafts; the Company Secretary signs every document before lodgement.',
    'tips': [
        'Variation: prep an investor day calendar around the AGM',
        'Variation: produce a meeting-script appendix for the Chairman',
    ],
}

CARDS['uc-ir-invday'] = {
    'title': 'Investor Day Pack',
    'dept_tag': 'Investor Relations',
    'industry_tag': None,
    'complexity': 'advanced',
    'apps': ['PowerPoint', 'Word', 'Excel', 'Outlook', 'Teams'],
    'desc': 'Capital Markets Day — Cowork builds the keynote deck, division break-out packs, sell-side Q&A and investor follow-up plan.',
    'skills': [
        'Capital-markets storytelling (group + division)',
        'Sell-side Q&A anticipation',
        'Differentiated investor follow-up plan',
    ],
    'instructions': [
        'Open Cowork',
        'Attach the 3 source files',
        'Paste the prompt',
    ],
    'sample_files': [
        ('IR_Group_Strategy.docx', 'docx'),
        ('IR_Divisional_Performance.xlsx', 'xlsx'),
        ('IR_Sell_Side_Notes.docx', 'docx'),
    ],
    'prompts': [{
        'label': 'Capital Markets Day pack',
        'text': (
            "Using the 3 attached files, build the [YEAR] Capital Markets Day pack. In parallel:\n"
            "1) PowerPoint — 30-slide keynote (CEO + CFO + 4 division leads).\n"
            "2) PowerPoint — 4 division break-out packs (10 slides each).\n"
            "3) Word — sell-side Q&A bank with 30 anticipated questions and approved answers.\n"
            "4) Excel — investor follow-up plan: top 30 investors with tailored meeting agenda.\n"
            "5) Outlook + Teams — covering invitations + IR team Teams brief for day-of logistics.\n"
            "Cite the file + tab for every guidance / target number. Flag any number that contradicts last quarterly disclosure."
        )
    }],
    'expected': [
        'Keynote deck',
        'Division break-outs',
        'Sell-side Q&A bank',
        'Investor follow-up plan',
        'Team logistics brief',
    ],
    'watch': [
        'Disclosure contradictions surfaced',
        'Division break-outs reinforce, not contradict, group story',
    ],
    'honest': 'Capital-markets numbers are guidance — Cowork drafts; the CFO + Head of IR must align every quoted figure with the most recent disclosure.',
    'tips': [
        'Variation: add a 30-day post-event analyst report tracker',
        'Variation: include sustainability-investor focus version',
    ],
}

CARDS['uc-proc-rfp'] = {
    'title': 'Strategic RFP Evaluation Sprint',
    'dept_tag': 'Procurement',
    'industry_tag': None,
    'complexity': 'advanced',
    'apps': ['Excel', 'PowerPoint', 'Word', 'Outlook', 'Teams'],
    'desc': 'Strategic supplier RFP closing — Cowork builds the technical + commercial evaluation, BAFO brief and award recommendation.',
    'skills': [
        'Multi-criteria RFP scoring (tech + commercial + risk)',
        'BAFO (Best-And-Final-Offer) framing',
        'Award recommendation construction',
    ],
    'instructions': [
        'Open Cowork',
        'Attach the 4 source files',
        'Paste the prompt',
    ],
    'sample_files': [
        ('PROC_Bid_Master.xlsx', 'xlsx'),
        ('PROC_Tech_Evaluation.docx', 'docx'),
        ('PROC_Commercial_Evaluation.xlsx', 'xlsx'),
        ('PROC_Award_Policy.docx', 'docx'),
    ],
    'prompts': [{
        'label': 'RFP evaluation pack',
        'text': (
            "Using the 4 attached files, build the [RFP] evaluation pack. In parallel:\n"
            "1) Excel — composite scoring sheet (tech 50 / commercial 35 / risk 15) with rationale per criterion.\n"
            "2) PowerPoint — 10-slide Tender Committee deck.\n"
            "3) Word — BAFO invitation letters to short-listed bidders.\n"
            "4) Word — award recommendation memo (winner + 2 backups + rationale).\n"
            "5) Outlook + Teams — internal stakeholder alignment emails + Tender Committee Teams brief.\n"
            "Cite the file + tab for every score. Flag any bidder whose price is more than 25% below mean (abnormally low) or fails the financial-health screen."
        )
    }],
    'expected': [
        'Composite scoring sheet',
        'Tender Committee deck',
        'BAFO letters',
        'Award memo',
        'Stakeholder alignment',
    ],
    'watch': [
        'Abnormally low bids flagged',
        'Financial-health screen explicit',
    ],
    'honest': 'Award is a governed decision — Cowork supports; the Tender Committee chair signs the recommendation.',
    'tips': [
        'Variation: add a sustainability / local-content scoring overlay',
        'Variation: prep a post-award supplier-onboarding plan',
    ],
}

CARDS['uc-it-incident'] = {
    'title': 'Cyber Incident Response Pack',
    'dept_tag': 'IT & Digital',
    'industry_tag': None,
    'complexity': 'advanced',
    'apps': ['Word', 'PowerPoint', 'Excel', 'Outlook', 'Teams'],
    'desc': 'Major cyber incident — Cowork drives regulator, customer, board and IT-team streams in parallel under time pressure.',
    'skills': [
        'Incident timeline construction with forensic precision',
        'Multi-jurisdiction notification (PDPA, sectoral regulators)',
        'Multi-audience holding-line maintenance',
    ],
    'instructions': [
        'Open Cowork',
        'Attach the 3 source files',
        'Paste the prompt',
    ],
    'sample_files': [
        ('IT_Incident_Timeline.docx', 'docx'),
        ('IT_Impacted_Systems.xlsx', 'xlsx'),
        ('IT_Incident_Playbook.docx', 'docx'),
    ],
    'prompts': [{
        'label': 'Incident response',
        'text': (
            "Using the 3 attached files, build the response to the [DATE] cyber incident. In parallel:\n"
            "1) Word — regulator notification per PDPA / sectoral rules (one per jurisdiction).\n"
            "2) Excel — affected-customer ledger with notification status + categorical risk tag.\n"
            "3) PowerPoint — 8-slide board / Audit Committee brief.\n"
            "4) Outlook — customer / partner notification letters with controlled tone.\n"
            "5) Teams — IT team coordination brief: who is doing what for the next 72h.\n"
            "Cite the playbook section for every action. Flag any system whose downtime exceeds the regulator-disclosable threshold."
        )
    }],
    'expected': [
        'Regulator notifications',
        'Customer ledger + notifications',
        'Board / AC brief',
        'Customer letters',
        'IT team coordination',
    ],
    'watch': [
        'Disclosable-threshold breaches flagged',
        'Notification timing tracked precisely',
    ],
    'honest': 'Cyber notification is law-bound — Cowork drafts; the CISO + GC + DPO all sign before any external party is notified.',
    'tips': [
        'Variation: add a forensic-evidence preservation checklist',
        'Variation: prep a post-incident lessons-learned template',
    ],
}
