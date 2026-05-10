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
