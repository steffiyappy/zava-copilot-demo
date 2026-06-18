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
