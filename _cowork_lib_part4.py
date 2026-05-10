# -*- coding: utf-8 -*-
"""Remaining sectors — BPO, Telco, Conglomerate, Govt, GLC, Property, Logistics,
Aviation, Mining, Retail, Hospitality, Media, Education, Utilities, E-commerce,
Maritime. ~17 cards."""

CARDS = {}

CARDS['uc-bpo-sla-brief'] = {
    'title': 'Multi-Client SLA Recovery Brief',
    'dept_tag': 'Service Delivery',
    'industry_tag': 'BPO Services',
    'complexity': 'intermediate',
    'apps': ['Excel', 'PowerPoint', 'Outlook', 'Teams'],
    'desc': 'Five client portfolios slipping AHT, FCR and CSAT — Cowork builds the recovery storyline and client-facing deck.',
    'skills': [
        'Multi-client SLA scorecard reconciliation',
        'Root-cause splitting (volume / staffing / quality / tech)',
        'Differentiated client tone (commercial vs apologetic vs upbeat)',
    ],
    'instructions': [
        'Open Microsoft 365 Copilot Cowork',
        'Attach the 3 BPO source files',
        'Paste the prompt',
    ],
    'sample_files': [
        ('BPO_Client_SLA_Scorecard.xlsx', 'xlsx'),
        ('BPO_Workforce_Schedule.xlsx', 'xlsx'),
        ('BPO_Quality_Audit_Findings.docx', 'docx'),
    ],
    'prompts': [{
        'label': 'SLA recovery sprint',
        'text': (
            "Using the 3 attached files, build the [QUARTER] SLA recovery sprint across the top 5 clients. In parallel:\n"
            "1) Excel — score each client RAG across AHT / FCR / CSAT / Adherence + sparkline 13-week trend.\n"
            "2) PowerPoint — 8-slide deck: red clients first, root-cause split, recovery commitments.\n"
            "3) Outlook — one tailored email per client (commercial tone for red, partnership for amber, thank-you for green).\n"
            "4) Teams — message to operations leads with concrete staffing + training actions per client.\n"
            "5) Excel — staffing reforecast tab showing reallocation of agents across queues.\n"
            "Cite the file + tab + row for every number. Flag any client whose contract carries penalty clauses."
        )
    }],
    'expected': [
        'Client SLA scorecard',
        'Recovery deck',
        '5 client emails tone-matched',
        'Ops Teams brief',
        'Staffing reforecast',
    ],
    'watch': [
        'Tone shifts per client — not a copy-paste',
        'Penalty-clause clients flagged with urgency',
    ],
    'honest': 'Cowork will draft tone — you still need to sign off the commercial language with the Client Services Director before any client sees it.',
    'tips': [
        'Variation: add a single board-level slide ranking clients by retention risk',
        'Variation: ask Cowork to draft talking points for the QBR call',
    ],
}

CARDS['uc-telco-outage'] = {
    'title': 'Major Network Outage Post-Mortem',
    'dept_tag': 'Network Operations',
    'industry_tag': 'Telco',
    'complexity': 'advanced',
    'apps': ['Word', 'PowerPoint', 'Excel', 'Outlook', 'Teams'],
    'desc': 'Region-wide outage hit prepaid + enterprise customers. Cowork drives the regulator, enterprise customer and board narrative streams in parallel.',
    'skills': [
        'MCMC / regulator submission tone with timeline precision',
        'Enterprise SLA credit calculation + client-by-client breakdown',
        'Multi-audience message control (regulator / enterprise / consumer / board)',
    ],
    'instructions': [
        'Open Cowork',
        'Attach the 4 source files',
        'Paste the prompt',
    ],
    'sample_files': [
        ('TELCO_Outage_Timeline.docx', 'docx'),
        ('TELCO_Impacted_Cells_NMS.xlsx', 'xlsx'),
        ('TELCO_Enterprise_SLA_Master.xlsx', 'xlsx'),
        ('TELCO_Network_KPIs_Last30d.xlsx', 'xlsx'),
    ],
    'prompts': [{
        'label': 'Post-mortem fan-out',
        'text': (
            "Using the 4 attached files, build the post-outage response for the [DATE] [REGION] event. In parallel:\n"
            "1) Word — regulator notification per MCMC SP-Tx (or equivalent) format: timeline, root cause, customers affected, restoration steps, prevention.\n"
            "2) Excel — enterprise SLA credit calc per affected customer with cap + cumulative-event check.\n"
            "3) PowerPoint — 10-slide board deck: 30-second exec summary, impact, response, financial, prevention roadmap.\n"
            "4) Outlook — 5 enterprise customer emails (top revenue): apology + credit + dedicated AM contact.\n"
            "5) Teams — message to Customer Operations: scripted holding line + escalation path for next 72h.\n"
            "Cite the file + tab + row for every claim. Flag any customer whose contract triggers automatic termination right."
        )
    }],
    'expected': [
        'Regulator filing',
        'SLA credit register',
        'Board deck',
        'Top-5 customer letters',
        'Customer Ops playbook',
    ],
    'watch': [
        'Regulator timeline precise to the minute',
        'Termination-right customers flagged',
    ],
    'honest': 'Regulator filing is heavily templated — Cowork drafts the narrative but the precise clause references must be checked by Regulatory Affairs.',
    'tips': [
        'Variation: add SMS holding-message text in 3 languages',
        'Variation: ask for press-statement bullets if media is calling',
    ],
}

CARDS['uc-cong-capalloc'] = {
    'title': 'Annual Capital Allocation Council',
    'dept_tag': 'Group Strategy',
    'industry_tag': 'Diversified Conglomerate',
    'complexity': 'advanced',
    'apps': ['Excel', 'PowerPoint', 'Word', 'Teams'],
    'desc': 'Eight subsidiaries fight for limited group capex. Cowork builds the council pack, ranking matrix and division-by-division letters.',
    'skills': [
        'Cross-divisional ROIC + payback ranking',
        'Capital-rationing trade-off articulation',
        'Differentiated subsidiary CEO messaging',
    ],
    'instructions': [
        'Open Cowork',
        'Attach the 3 source files',
        'Paste the prompt',
    ],
    'sample_files': [
        ('GRP_Capex_Pipeline_Master.xlsx', 'xlsx'),
        ('GRP_Division_5yr_Plans.docx', 'docx'),
        ('GRP_Capital_Allocation_Policy.docx', 'docx'),
    ],
    'prompts': [{
        'label': 'Capex council pack',
        'text': (
            "Using the 3 attached files, build the [YEAR] Capital Allocation Council pack. In parallel:\n"
            "1) Excel — ranking matrix scoring all 30+ projects on ROIC / payback / strategic-fit / risk + recommended portfolio under the [LIMIT] envelope.\n"
            "2) PowerPoint — 12-slide council deck: envelope, ranking, portfolio recommendation, deferred list, sensitivity.\n"
            "3) Word — 8 division-CEO letters: 4 winners (approval + conditions), 4 deferred (rationale + revisit gate).\n"
            "4) Teams — message to division CFO chat with the spreadsheet and key page references.\n"
            "5) Word — Board-paper executive summary (2 pages) for the next Board meeting.\n"
            "Cite the file + tab for every project. Flag any project that the Capital Allocation Policy says requires Board (not Council) approval."
        )
    }],
    'expected': [
        'Project ranking matrix',
        'Council deck',
        '8 division-CEO letters',
        'Division CFO Teams brief',
        'Board paper exec summary',
    ],
    'watch': [
        'Deferred letters preserve the relationship',
        'Board-vs-Council policy threshold respected',
    ],
    'honest': 'Capital allocation is partly political — Cowork ranks on the criteria you give it; the Group CFO still needs to overlay strategic intent.',
    'tips': [
        'Variation: add a sensitivity tab on +/- 200bps WACC',
        'Variation: include an ESG / climate-transition lens as a scoring column',
    ],
}

CARDS['uc-govt-parlq'] = {
    'title': 'Parliamentary Question Briefing Sprint',
    'dept_tag': 'Policy Coordination',
    'industry_tag': 'Government Agency',
    'complexity': 'intermediate',
    'apps': ['Word', 'Excel', 'Outlook', 'Teams'],
    'desc': 'Twelve parliamentary questions land overnight. Cowork drafts the minister-ready answer pack, supporting numbers and clearance chain.',
    'skills': [
        'PQ-style answer drafting (concise, defensible, on-record)',
        'Number-to-narrative reconciliation against published reports',
        'Multi-department clearance chain orchestration',
    ],
    'instructions': [
        'Open Cowork',
        'Attach the 3 source files',
        'Paste the prompt',
    ],
    'sample_files': [
        ('GOV_PQ_Tracker.xlsx', 'xlsx'),
        ('GOV_Programme_Performance.xlsx', 'xlsx'),
        ('GOV_Strategic_Plan.docx', 'docx'),
    ],
    'prompts': [{
        'label': 'PQ brief pack',
        'text': (
            "Using the 3 attached files, build the [SITTING DATE] PQ brief pack. In parallel:\n"
            "1) Word — minister-ready answer for each of the 12 questions in standard PQ format (200-300 words, defensible facts).\n"
            "2) Excel — supporting-number table cross-referenced to the Programme Performance workbook (cite tab + row).\n"
            "3) Word — annex of background notes per question for follow-up supplementaries.\n"
            "4) Outlook — clearance email to relevant DG + Deputy Sec for sign-off, one per question with the answer attached.\n"
            "5) Teams — message to the Minister's Office secretariat summarising the pack.\n"
            "Flag any question that needs cross-ministry input — name the ministry and the missing data point."
        )
    }],
    'expected': [
        '12 minister-ready answers',
        'Supporting-number table',
        'Background annex',
        '12 clearance emails',
        "Minister's Office summary",
    ],
    'watch': [
        'Defensible numbers only — every figure cited',
        'Cross-ministry gaps flagged early',
    ],
    'honest': 'PQ answers carry political weight — Cowork drafts; the SecGen reviews. Treat all output as draft until cleared.',
    'tips': [
        'Variation: prepare suggested supplementary-question responses',
        'Variation: add a one-page top-line for the Minister to memorise',
    ],
}

CARDS['uc-reg-supervisory'] = {
    'title': 'Onsite Supervisory Examination Prep',
    'dept_tag': 'Supervision',
    'industry_tag': 'Financial Regulator',
    'complexity': 'advanced',
    'apps': ['Word', 'Excel', 'Outlook', 'Teams'],
    'desc': 'Onsite exam at a regulated bank in 2 weeks. Cowork builds the exam scope, request list, internal briefing and team logistics.',
    'skills': [
        'Risk-based exam scoping (where to look hardest)',
        'Standard information-request templating',
        'Cross-functional exam team coordination',
    ],
    'instructions': [
        'Open Cowork',
        'Attach the 3 source files',
        'Paste the prompt',
    ],
    'sample_files': [
        ('REG_Entity_Risk_Profile.docx', 'docx'),
        ('REG_Prior_Exam_Findings.docx', 'docx'),
        ('REG_Thematic_Risk_Priorities.docx', 'docx'),
    ],
    'prompts': [{
        'label': 'Exam launch pack',
        'text': (
            "Using the 3 attached files, build the launch pack for the upcoming onsite at [BANK]. In parallel:\n"
            "1) Word — exam scoping memo: risk-based focus areas, sample sizes, expected duration, team composition.\n"
            "2) Excel — information request list (30-50 items) by topic / format / due date.\n"
            "3) Word — internal pre-exam briefing pack for the exam team (entity profile, prior issues, watch-areas).\n"
            "4) Outlook — opening letter to the bank's CEO + Compliance Head transmitting the request list.\n"
            "5) Teams — exam team logistics post (location, hours, escalation contacts).\n"
            "Cite the source document + section for every focus area. Flag any prior finding that has not been satisfactorily closed."
        )
    }],
    'expected': [
        'Exam scoping memo',
        'Information request list',
        'Internal briefing pack',
        'CEO transmittal letter',
        'Team logistics brief',
    ],
    'watch': [
        'Unclosed prior findings explicitly flagged',
        'Sample sizes proportionate to risk',
    ],
    'honest': 'Exam scope is a judgement call — Cowork structures the inputs; the Director of Supervision decides what to prioritise.',
    'tips': [
        'Variation: prepare a 10-question opening interview script for the CEO meeting',
        'Variation: add a horizon-scan note linking entity risks to ongoing thematic reviews',
    ],
}

CARDS['uc-glc-dividend'] = {
    'title': 'GLC Dividend Stewardship Pack',
    'dept_tag': 'Portfolio Management',
    'industry_tag': 'GLC Investment',
    'complexity': 'intermediate',
    'apps': ['Excel', 'PowerPoint', 'Word', 'Outlook', 'Teams'],
    'desc': 'Sovereign-fund GLC reviews 12 listed investees for dividend stewardship. Cowork builds the model, voting recommendations and engagement letters.',
    'skills': [
        'Investee dividend / cashflow / payout analysis',
        'Stewardship voting recommendation drafting',
        'Differentiated investee engagement tone (over / under-paying)',
    ],
    'instructions': [
        'Open Cowork',
        'Attach the 3 source files',
        'Paste the prompt',
    ],
    'sample_files': [
        ('GLC_Portfolio_Master.xlsx', 'xlsx'),
        ('GLC_Investee_Annual_Reports.docx', 'docx'),
        ('GLC_Stewardship_Code.docx', 'docx'),
    ],
    'prompts': [{
        'label': 'Stewardship review',
        'text': (
            "Using the 3 attached files, build the [YEAR] dividend stewardship review for the top 12 investees. In parallel:\n"
            "1) Excel — dividend / FCF / payout-ratio model with 3-year trend + peer benchmark per investee.\n"
            "2) PowerPoint — 14-slide Investment Committee deck: portfolio yield, outliers, voting recommendations.\n"
            "3) Word — voting recommendation memos (AGM agenda items) per investee.\n"
            "4) Outlook — 6 chair-to-chair letters: 3 to over-payers (sustainability concern), 3 to under-payers (capital efficiency challenge).\n"
            "5) Teams — analyst team brief on the engagement schedule for the next quarter.\n"
            "Cite the file + tab + row for every figure. Flag any investee whose payout breaches the Stewardship Code thresholds."
        )
    }],
    'expected': [
        'Dividend / payout model',
        'IC deck',
        '12 voting memos',
        '6 chair-to-chair letters',
        'Analyst engagement schedule',
    ],
    'watch': [
        'Tone shifts between over- and under-payers',
        'Stewardship Code breaches flagged',
    ],
    'honest': 'Stewardship is reputational — Cowork drafts; the Head of Stewardship signs off every letter and recommendation.',
    'tips': [
        'Variation: add ESG-payout overlay (climate-CapEx need vs dividend)',
        'Variation: include peer benchmark percentile per investee',
    ],
}

CARDS['uc-reit-renewal'] = {
    'title': 'Major Tenant Renewal Negotiation Pack',
    'dept_tag': 'Asset Management',
    'industry_tag': 'Property REIT',
    'complexity': 'intermediate',
    'apps': ['Excel', 'Word', 'PowerPoint', 'Outlook', 'Teams'],
    'desc': 'Anchor tenant renewal at 12 months out. Cowork builds the rent benchmark, offer pack, fallback scenarios and unitholder narrative.',
    'skills': [
        'Comparable-rent analysis + concession economics',
        'Multi-scenario offer construction (best / target / walk-away)',
        'Unitholder communication on lease risk',
    ],
    'instructions': [
        'Open Cowork',
        'Attach the 4 source files',
        'Paste the prompt',
    ],
    'sample_files': [
        ('REIT_Tenant_Master.xlsx', 'xlsx'),
        ('REIT_Comparable_Leases.xlsx', 'xlsx'),
        ('REIT_Asset_Performance.xlsx', 'xlsx'),
        ('REIT_Lease_Renewal_Policy.docx', 'docx'),
    ],
    'prompts': [{
        'label': 'Tenant renewal pack',
        'text': (
            "Using the 4 attached files, build the renewal pack for [TENANT] at [ASSET]. In parallel:\n"
            "1) Excel — comparable-rent analysis vs 8 peer locations + 3 scenarios (best / target / walk-away) with NPV.\n"
            "2) Word — offer letter v1 (target case) ready to send to the tenant.\n"
            "3) PowerPoint — 6-slide Investment Committee paper recommending the strategy.\n"
            "4) Outlook — internal alignment email to Leasing, Legal, Finance with action items.\n"
            "5) Word — draft unitholder note (only used if the lease lapses) explaining the asset re-tenanting plan.\n"
            "Cite the file + tab for every comparable. Flag any clause where the existing lease has an unusual option / break."
        )
    }],
    'expected': [
        'Rent comparable model',
        'Offer letter v1',
        'IC paper',
        'Internal alignment email',
        'Unitholder contingency note',
    ],
    'watch': [
        'Walk-away math defensible',
        'Unusual lease clauses surfaced',
    ],
    'honest': 'Comparable rents are an art — Cowork synthesises; the Head of Leasing applies market judgement before any offer leaves the building.',
    'tips': [
        'Variation: add WALE impact pre- and post-renewal across the portfolio',
        'Variation: ask for a 2-minute board talking-points version',
    ],
}

CARDS['uc-log-capacity'] = {
    'title': 'Peak-Season Capacity Reallocation Sprint',
    'dept_tag': 'Operations',
    'industry_tag': 'Logistics & 3PL',
    'complexity': 'intermediate',
    'apps': ['Excel', 'PowerPoint', 'Outlook', 'Teams'],
    'desc': 'Six weeks to peak. Cowork rebalances DC capacity, line-haul, and customer SLAs into a single executable plan.',
    'skills': [
        'Network capacity vs demand reconciliation',
        'Customer SLA prioritisation under capacity stress',
        'Cross-functional peak readiness coordination',
    ],
    'instructions': [
        'Open Cowork',
        'Attach the 3 source files',
        'Paste the prompt',
    ],
    'sample_files': [
        ('LOG_Network_Capacity.xlsx', 'xlsx'),
        ('LOG_Customer_Volume_Forecast.xlsx', 'xlsx'),
        ('LOG_SLA_Master.xlsx', 'xlsx'),
    ],
    'prompts': [{
        'label': 'Peak readiness',
        'text': (
            "Using the 3 attached files, build the peak-season plan for [PEAK PERIOD]. In parallel:\n"
            "1) Excel — capacity vs demand heat-map per DC + line-haul lane (red / amber / green by week).\n"
            "2) Excel — customer prioritisation tier with SLA caps under capacity stress.\n"
            "3) PowerPoint — 10-slide operations deck: scenario, levers, residual risk.\n"
            "4) Outlook — pre-peak commitment letters to top-10 customers (tone matched to tier).\n"
            "5) Teams — ops Teams channel announcement with shift schedule + escalation matrix.\n"
            "Cite the file + tab for every capacity number. Flag any customer whose contract has hard-floor commitments we cannot meet."
        )
    }],
    'expected': [
        'Capacity vs demand heat-map',
        'Customer tier list',
        'Ops deck',
        'Top-10 customer letters',
        'Ops channel announcement',
    ],
    'watch': [
        'Hard-floor breaches surfaced',
        'Customer tier explicit, not implicit',
    ],
    'honest': 'Capacity numbers are a forecast — Cowork rebalances based on the data given; the network manager has the local nuance.',
    'tips': [
        'Variation: add a temporary-capacity option (3PL flex + overtime) costing',
        'Variation: include a customer-by-customer post-peak debrief template',
    ],
}

CARDS['uc-avi-airport-slot'] = {
    'title': 'Slot Coordination Conference Pack',
    'dept_tag': 'Airline Operations',
    'industry_tag': 'Aviation Airports',
    'complexity': 'advanced',
    'apps': ['Excel', 'PowerPoint', 'Word', 'Outlook', 'Teams'],
    'desc': 'IATA slot conference preparation — Cowork builds the demand-vs-capacity case, airline-by-airline negotiation plan and concession positioning.',
    'skills': [
        'Hourly slot demand vs declared capacity analysis',
        'Multi-airline negotiation pack construction',
        'Concessions / regulator framing for slot decisions',
    ],
    'instructions': [
        'Open Cowork',
        'Attach the 3 source files',
        'Paste the prompt',
    ],
    'sample_files': [
        ('AVI_Slot_Request_Master.xlsx', 'xlsx'),
        ('AVI_Declared_Capacity.xlsx', 'xlsx'),
        ('AVI_Slot_Policy.docx', 'docx'),
    ],
    'prompts': [{
        'label': 'Slot conference pack',
        'text': (
            "Using the 3 attached files, build the [SEASON] slot conference pack. In parallel:\n"
            "1) Excel — hour-by-hour demand vs declared capacity per runway + terminal.\n"
            "2) PowerPoint — 12-slide deck: capacity, demand, congestion windows, slot-allocation principles, expected push-back.\n"
            "3) Word — negotiation briefs for top 5 airlines (slot reduction asks + concessions).\n"
            "4) Outlook — coordinator letters to airlines + regulator notification of the conference position.\n"
            "5) Teams — Network Planning Teams brief: who is leading each negotiation thread.\n"
            "Cite the file + tab for every slot number. Flag any window where capacity is below historical demand for 2+ consecutive seasons."
        )
    }],
    'expected': [
        'Demand vs capacity grid',
        'Conference deck',
        '5 airline negotiation briefs',
        'Coordinator letters',
        'Network team brief',
    ],
    'watch': [
        'Repeat-congestion windows flagged',
        'Concessions explicit, not hidden',
    ],
    'honest': 'Slot allocation is regulated — Cowork builds the case; the Slot Coordinator (legally independent) makes the final allocation.',
    'tips': [
        'Variation: add a sensitivity if a new runway opens mid-season',
        'Variation: ask for an environmental noise-quota overlay',
    ],
}

CARDS['uc-avi-airline-irrops'] = {
    'title': 'IROPS (Irregular Ops) Response Pack',
    'dept_tag': 'Operations Control',
    'industry_tag': 'Aviation Airlines',
    'complexity': 'advanced',
    'apps': ['Excel', 'Word', 'PowerPoint', 'Outlook', 'Teams'],
    'desc': 'Weather event grounded the network for 18 hours. Cowork drives passenger comms, crew/fleet recovery and regulator filings in parallel.',
    'skills': [
        'Passenger compensation calc (EC 261 / IATA 824 / local equivalents)',
        'Crew duty-time reconciliation under recovery',
        'Multi-regulator notification with consistent narrative',
    ],
    'instructions': [
        'Open Cowork',
        'Attach the 4 source files',
        'Paste the prompt',
    ],
    'sample_files': [
        ('AIR_Cancelled_Flights.xlsx', 'xlsx'),
        ('AIR_Passenger_Manifest.xlsx', 'xlsx'),
        ('AIR_Crew_Duty_Roster.xlsx', 'xlsx'),
        ('AIR_IROPS_Playbook.docx', 'docx'),
    ],
    'prompts': [{
        'label': 'IROPS response',
        'text': (
            "Using the 4 attached files, build the response to the [DATE] [REGION] IROPS event. In parallel:\n"
            "1) Excel — passenger compensation per flight per cabin with rule-applied lookup (EC 261 / equivalent).\n"
            "2) Word — multi-language passenger letter templates (apology / rebooking options / compensation rights).\n"
            "3) PowerPoint — 8-slide ExCo brief: timeline, network impact, customer cost, recovery curve.\n"
            "4) Outlook — emails to top corporate clients (5 highest yield) with dedicated rebooking line.\n"
            "5) Teams — Ops Control announcement: crew duty trade-offs and aircraft repositioning plan.\n"
            "Cite the file + tab for every flight + rule. Flag any crew pairing that exceeds duty-time without waiver."
        )
    }],
    'expected': [
        'Compensation calc per flight',
        'Multi-language pax letters',
        'ExCo brief',
        '5 corporate client emails',
        'Crew + fleet recovery brief',
    ],
    'watch': [
        'Duty-time exceedances surfaced',
        'Compensation rule applied consistently per route',
    ],
    'honest': 'Compensation rules vary by jurisdiction — Cowork applies the rule you give it; Legal must confirm cross-border edge cases.',
    'tips': [
        'Variation: prep a 2-paragraph holding press statement',
        'Variation: build a 24h / 48h / 72h recovery KPI dashboard',
    ],
}

CARDS['uc-coal-volume'] = {
    'title': 'Quarterly Sales-Volume Commitment Pack',
    'dept_tag': 'Sales & Marketing',
    'industry_tag': 'Coal Mining',
    'complexity': 'intermediate',
    'apps': ['Excel', 'PowerPoint', 'Word', 'Outlook', 'Teams'],
    'desc': 'Mine output guidance + buyer take-or-pay obligations. Cowork builds the commitment ladder and buyer letters.',
    'skills': [
        'Mine production forecast vs offtake reconciliation',
        'Take-or-pay shortfall economics',
        'Buyer-by-buyer commitment framing',
    ],
    'instructions': [
        'Open Cowork',
        'Attach the 3 source files',
        'Paste the prompt',
    ],
    'sample_files': [
        ('COAL_Mine_Production_Plan.xlsx', 'xlsx'),
        ('COAL_Offtake_Contracts.xlsx', 'xlsx'),
        ('COAL_Stockpile_Status.xlsx', 'xlsx'),
    ],
    'prompts': [{
        'label': 'Sales commitment pack',
        'text': (
            "Using the 3 attached files, build the [QUARTER] sales commitment pack. In parallel:\n"
            "1) Excel — supply ladder: mine production + stockpile draw + railed coal vs offtake commitments by buyer.\n"
            "2) PowerPoint — 8-slide Sales Committee deck: surplus / deficit by month + buyer.\n"
            "3) Word — buyer letters: 4 confirmation letters, 2 reallocation requests, 1 shortfall + indemnity note.\n"
            "4) Outlook — internal Operations + Logistics alignment email with railing schedule.\n"
            "5) Teams — Investor Relations brief: production guidance impact for the quarterly call.\n"
            "Cite the file + tab + row for every tonnage. Flag any buyer whose take-or-pay penalty exceeds the spot uplift."
        )
    }],
    'expected': [
        'Supply ladder',
        'Sales Committee deck',
        '7 buyer letters',
        'Operations alignment email',
        'IR brief',
    ],
    'watch': [
        'Take-or-pay penalty math defensible',
        'Spot uplift / penalty trade-off explicit',
    ],
    'honest': 'Production forecasts shift with geology — Cowork reconciles; the Mine Manager owns the volume number.',
    'tips': [
        'Variation: add Newcastle benchmark price sensitivity per offtake',
        'Variation: produce a one-pager for the Group CFO',
    ],
}

CARDS['uc-rare-earth-export'] = {
    'title': 'Critical-Mineral Export Licence Pack',
    'dept_tag': 'Trade Compliance',
    'industry_tag': 'Rare Earth',
    'complexity': 'advanced',
    'apps': ['Word', 'Excel', 'PowerPoint', 'Outlook', 'Teams'],
    'desc': 'Export licence renewal for critical minerals — Cowork builds the application, end-use checks and government engagement plan.',
    'skills': [
        'End-use due-diligence narrative construction',
        'Critical-mineral export-control rule mapping',
        'Government engagement positioning',
    ],
    'instructions': [
        'Open Cowork',
        'Attach the 3 source files',
        'Paste the prompt',
    ],
    'sample_files': [
        ('RE_Export_Application_Form.docx', 'docx'),
        ('RE_Customer_DueDiligence.xlsx', 'xlsx'),
        ('RE_Production_Inventory.xlsx', 'xlsx'),
    ],
    'prompts': [{
        'label': 'Export licence pack',
        'text': (
            "Using the 3 attached files, build the [YEAR] export licence renewal pack. In parallel:\n"
            "1) Word — completed licence application with full end-use narrative per shipment.\n"
            "2) Excel — customer + end-use due-diligence matrix (red / amber / green) with documentary evidence.\n"
            "3) PowerPoint — 8-slide deck for the inter-ministerial review meeting.\n"
            "4) Outlook — covering letter to the regulator + parallel briefing email to the line ministry.\n"
            "5) Teams — internal Compliance + Sales brief on what is in / out of scope of the renewed licence.\n"
            "Cite the file + tab for every customer / volume / end-use. Flag any customer who has appeared on a sanctions-screening hit since the last cycle."
        )
    }],
    'expected': [
        'Completed application',
        'Customer DD matrix',
        'Inter-ministerial deck',
        'Regulator + ministry letters',
        'Internal scope brief',
    ],
    'watch': [
        'Sanctions hits surfaced',
        'End-use narrative concrete per shipment',
    ],
    'honest': 'Export control is highly political — Cowork drafts; Trade Compliance Director and external counsel must review before any filing.',
    'tips': [
        'Variation: build a horizon-scan slide of pending export-control changes',
        'Variation: prep talking-points for the line minister briefing',
    ],
}

CARDS['uc-retail-store-pnl'] = {
    'title': 'Underperforming-Store Action Sprint',
    'dept_tag': 'Store Operations',
    'industry_tag': 'Retail Grocery',
    'complexity': 'intermediate',
    'apps': ['Excel', 'PowerPoint', 'Word', 'Outlook', 'Teams'],
    'desc': 'Twenty-five stores below P&L threshold. Cowork builds the diagnosis, store-by-store action plan and field-team brief.',
    'skills': [
        'Store-level P&L pattern recognition',
        'Differentiated action plan (price / shrink / labour / range)',
        'Field-team communication tone (motivate, not blame)',
    ],
    'instructions': [
        'Open Cowork',
        'Attach the 3 source files',
        'Paste the prompt',
    ],
    'sample_files': [
        ('RTL_Store_PnL.xlsx', 'xlsx'),
        ('RTL_Shrink_by_Category.xlsx', 'xlsx'),
        ('RTL_Catchment_Demographics.xlsx', 'xlsx'),
    ],
    'prompts': [{
        'label': 'Store action sprint',
        'text': (
            "Using the 3 attached files, build the action sprint for the bottom 25 stores. In parallel:\n"
            "1) Excel — diagnosis grid: each store tagged by primary issue (margin / shrink / labour / range / catchment).\n"
            "2) PowerPoint — 10-slide ops deck for the regional GMs.\n"
            "3) Word — 25 one-page store action plans (90-day commitments).\n"
            "4) Outlook — 25 store-manager emails (motivational tone, specific asks, support offered).\n"
            "5) Teams — regional ops chat brief with the consolidated tracker.\n"
            "Cite the file + tab + row for every metric. Flag any store whose catchment is structurally declining (close / convert decision needed)."
        )
    }],
    'expected': [
        'Diagnosis grid',
        'Ops deck',
        '25 store action plans',
        '25 store-manager emails',
        'Regional ops Teams brief',
    ],
    'watch': [
        'Structural-decline stores surfaced (not just operational)',
        'Tone supportive, not blame',
    ],
    'honest': 'Store P&L diagnosis is iterative — Cowork tags by pattern; the area manager refines the action plan with on-the-ground context.',
    'tips': [
        'Variation: add a competitor-opening overlay per store',
        'Variation: build a 30/60/90 review cadence calendar',
    ],
}

CARDS['uc-hotel-surge'] = {
    'title': 'Mega-Event Surge Revenue Sprint',
    'dept_tag': 'Revenue Management',
    'industry_tag': 'Hotel & Resort',
    'complexity': 'intermediate',
    'apps': ['Excel', 'PowerPoint', 'Word', 'Outlook', 'Teams'],
    'desc': 'Major event in the city in 90 days. Cowork builds the surge pricing model, channel mix and corporate / group strategy.',
    'skills': [
        'Event-driven demand modelling + price ladder',
        'Channel-mix optimisation (OTA / direct / corporate / group)',
        'Service-readiness coordination',
    ],
    'instructions': [
        'Open Cowork',
        'Attach the 3 source files',
        'Paste the prompt',
    ],
    'sample_files': [
        ('HOTEL_Booking_Pace.xlsx', 'xlsx'),
        ('HOTEL_Comp_Set_Rates.xlsx', 'xlsx'),
        ('HOTEL_Channel_Performance.xlsx', 'xlsx'),
    ],
    'prompts': [{
        'label': 'Event surge plan',
        'text': (
            "Using the 3 attached files, build the [EVENT] surge plan. In parallel:\n"
            "1) Excel — price ladder per room type per day with comp-set anchor.\n"
            "2) Excel — channel-mix optimisation under the surge cap (OTA / direct / corporate / group).\n"
            "3) PowerPoint — 8-slide commercial team brief.\n"
            "4) Outlook — outreach letters to top-20 corporate accounts (early-bird offer) + 10 group bookers.\n"
            "5) Teams — Front Office + F&B + Housekeeping readiness brief.\n"
            "Cite the file + tab for every rate / pace number. Flag any night where the comp set is undercutting our rack rate by >15%."
        )
    }],
    'expected': [
        'Price ladder',
        'Channel optimisation',
        'Commercial brief',
        '30 outreach letters',
        'Hotel readiness brief',
    ],
    'watch': [
        'Comp-set gaps surfaced',
        'Service readiness not just price',
    ],
    'honest': 'Surge pricing is a brand decision — Cowork recommends; GM signs off on what the brand will tolerate.',
    'tips': [
        'Variation: add a length-of-stay restriction sensitivity',
        'Variation: prep loyalty-member exclusivity offers',
    ],
}

CARDS['uc-media-campaign'] = {
    'title': 'Tentpole Campaign Launch Pack',
    'dept_tag': 'Content Marketing',
    'industry_tag': 'Media & Entertainment',
    'complexity': 'intermediate',
    'apps': ['Word', 'PowerPoint', 'Excel', 'Outlook', 'Teams'],
    'desc': 'Major content launch — Cowork builds the campaign plan, partner pack, talent brief and editorial calendar.',
    'skills': [
        'Multi-channel campaign architecture',
        'Talent + partner brief differentiation',
        'Editorial calendar orchestration',
    ],
    'instructions': [
        'Open Cowork',
        'Attach the 3 source files',
        'Paste the prompt',
    ],
    'sample_files': [
        ('MEDIA_Campaign_Brief.docx', 'docx'),
        ('MEDIA_Channel_Performance.xlsx', 'xlsx'),
        ('MEDIA_Brand_Guidelines.docx', 'docx'),
    ],
    'prompts': [{
        'label': 'Campaign launch pack',
        'text': (
            "Using the 3 attached files, build the [TITLE] launch pack. In parallel:\n"
            "1) Word — master campaign narrative (positioning, audience, pillars, KPIs).\n"
            "2) PowerPoint — 12-slide partner pack for distribution + media partners.\n"
            "3) Excel — editorial calendar across owned / earned / paid channels with deliverables + owner + due date.\n"
            "4) Outlook — talent briefs (3 leads) with do / don't messaging.\n"
            "5) Teams — internal launch-week brief to Content + PR + Trade Marketing.\n"
            "Cite the source document + section for every brand-rule reference. Flag any channel under-delivering 30 days pre-launch."
        )
    }],
    'expected': [
        'Campaign narrative',
        'Partner pack',
        'Editorial calendar',
        '3 talent briefs',
        'Internal launch brief',
    ],
    'watch': [
        'Brand-rule references explicit',
        'Talent dos/donts unambiguous',
    ],
    'honest': 'Campaign tone is craft work — Cowork structures; Creative Director shapes the language.',
    'tips': [
        'Variation: add a crisis playbook (in case talent issue)',
        'Variation: include a post-launch 30-day measurement deck template',
    ],
}

CARDS['uc-edu-cohort'] = {
    'title': 'Cohort Outcome Review + Intervention',
    'dept_tag': 'Academic Affairs',
    'industry_tag': 'Education',
    'complexity': 'intermediate',
    'apps': ['Excel', 'PowerPoint', 'Word', 'Outlook', 'Teams'],
    'desc': 'Mid-year cohort review — Cowork builds the at-risk list, intervention plan and parent / faculty comms.',
    'skills': [
        'At-risk learner identification (academic + attendance + wellbeing)',
        'Differentiated intervention design',
        'Parent / faculty communication tone',
    ],
    'instructions': [
        'Open Cowork',
        'Attach the 3 source files',
        'Paste the prompt',
    ],
    'sample_files': [
        ('EDU_Cohort_Performance.xlsx', 'xlsx'),
        ('EDU_Attendance_Wellbeing.xlsx', 'xlsx'),
        ('EDU_Intervention_Playbook.docx', 'docx'),
    ],
    'prompts': [{
        'label': 'Cohort intervention',
        'text': (
            "Using the 3 attached files, build the mid-year cohort review for [PROGRAMME]. In parallel:\n"
            "1) Excel — at-risk list ranked by composite (academic + attendance + wellbeing) with intervention tag.\n"
            "2) PowerPoint — 10-slide Faculty Council deck: cohort health, interventions, resource ask.\n"
            "3) Word — 15 parent / guardian letters (tone tiered: caring, escalation, urgent).\n"
            "4) Outlook — programme leader emails to module owners with module-level concerns.\n"
            "5) Teams — student-support team brief with the action register.\n"
            "Cite the file + tab + row for every concern. Flag any learner whose wellbeing flags require safeguarding referral."
        )
    }],
    'expected': [
        'At-risk register',
        'Faculty Council deck',
        '15 parent letters',
        'Module-owner emails',
        'Support team brief',
    ],
    'watch': [
        'Safeguarding flags surfaced separately',
        'Tone tiered per risk level',
    ],
    'honest': 'Learner intervention is sensitive — Cowork drafts; programme leader applies pastoral judgement before any parent contact.',
    'tips': [
        'Variation: add a peer-mentor pairing recommendation',
        'Variation: prep a 30-day follow-up review template',
    ],
}

CARDS['uc-util-outage'] = {
    'title': 'Substation Outage Response Pack',
    'dept_tag': 'Grid Operations',
    'industry_tag': 'Power Utilities',
    'complexity': 'advanced',
    'apps': ['Word', 'Excel', 'PowerPoint', 'Outlook', 'Teams'],
    'desc': 'Major substation outage affected 280,000 customers and a steel mill. Cowork drives regulator, large-customer and field-crew streams in parallel.',
    'skills': [
        'Outage-impact reconstruction (CMI, SAIDI/SAIFI impact)',
        'Large industrial customer compensation drafting',
        'Regulator outage report compliance',
    ],
    'instructions': [
        'Open Cowork',
        'Attach the 3 source files',
        'Paste the prompt',
    ],
    'sample_files': [
        ('UTIL_Outage_Telemetry.xlsx', 'xlsx'),
        ('UTIL_Customer_Connections.xlsx', 'xlsx'),
        ('UTIL_Outage_Reporting_Manual.docx', 'docx'),
    ],
    'prompts': [{
        'label': 'Outage response',
        'text': (
            "Using the 3 attached files, build the [DATE] [SUBSTATION] outage response. In parallel:\n"
            "1) Word — regulator outage report per Service Code format: cause, customers affected, CMI, restoration steps.\n"
            "2) Excel — large-customer impact ledger with compensation calc per tariff class.\n"
            "3) PowerPoint — 8-slide board-level outage brief: cause, financial impact, prevention roadmap.\n"
            "4) Outlook — letters to 5 industrial customers + 2 hospitals with apology and compensation note.\n"
            "5) Teams — field-crew Teams channel summary: lessons learned + crew commendation.\n"
            "Cite the file + tab for every customer / CMI figure. Flag any customer with a guaranteed-service plan triggering automatic credit."
        )
    }],
    'expected': [
        'Regulator outage report',
        'Customer impact ledger',
        'Board brief',
        '7 customer letters',
        'Field-crew Teams summary',
    ],
    'watch': [
        'Automatic-credit triggers surfaced',
        'CMI math matches telemetry',
    ],
    'honest': 'Outage reporting is regulator-defined — Cowork drafts to the manual; Compliance must confirm classification before filing.',
    'tips': [
        'Variation: add a SAIDI / SAIFI rolling impact view',
        'Variation: produce a public-information short statement',
    ],
}

CARDS['uc-ecomm-surge'] = {
    'title': 'Mega-Sale Day Readiness Sprint',
    'dept_tag': 'Marketplace Operations',
    'industry_tag': 'E-commerce / Super-app',
    'complexity': 'intermediate',
    'apps': ['Excel', 'PowerPoint', 'Word', 'Outlook', 'Teams'],
    'desc': '11.11 / Mega-sale day prep — Cowork builds the demand model, seller readiness pack, payments and fulfilment readiness, and customer-support surge plan.',
    'skills': [
        'Mega-sale demand modelling per category',
        'Seller / fulfilment / payments / CS surge readiness',
        'Top-seller account-management framing',
    ],
    'instructions': [
        'Open Cowork',
        'Attach the 4 source files',
        'Paste the prompt',
    ],
    'sample_files': [
        ('ECOM_Last_Sale_Postmortem.docx', 'docx'),
        ('ECOM_Seller_Performance.xlsx', 'xlsx'),
        ('ECOM_Payment_Channel_Health.xlsx', 'xlsx'),
        ('ECOM_CS_Volumes.xlsx', 'xlsx'),
    ],
    'prompts': [{
        'label': 'Mega-sale readiness',
        'text': (
            "Using the 4 attached files, build the [SALE DATE] readiness pack. In parallel:\n"
            "1) Excel — demand forecast per category vs last year + capacity per fulfilment node.\n"
            "2) PowerPoint — 12-slide ExCo readiness deck.\n"
            "3) Word — top-50 seller account briefs (assortment + price commitment + safety stock).\n"
            "4) Outlook — payments PSP letters + bank letters confirming surge headroom.\n"
            "5) Teams — Customer Support surge plan (shift, scripts, escalation matrix).\n"
            "Cite the file + tab for every number. Flag any category whose top seller is operating below 90% on-time fulfilment in the last 8 weeks."
        )
    }],
    'expected': [
        'Category demand model',
        'ExCo readiness deck',
        '50 seller briefs',
        'PSP / bank letters',
        'CS surge plan',
    ],
    'watch': [
        'Under-performing top sellers surfaced',
        'Payment / fulfilment / CS all covered, not just demand',
    ],
    'honest': 'Mega-sale is system-level — Cowork orchestrates the streams; each domain owner (Logistics / Payments / CS) signs off the readiness gate.',
    'tips': [
        'Variation: include a stress-test on 1.5x demand peak',
        'Variation: prep a real-time war-room dashboard spec',
    ],
}

CARDS['uc-maritime-port'] = {
    'title': 'Port Call Optimisation Pack',
    'dept_tag': 'Fleet Operations',
    'industry_tag': 'Maritime & Shipping',
    'complexity': 'intermediate',
    'apps': ['Excel', 'PowerPoint', 'Word', 'Outlook', 'Teams'],
    'desc': 'Multiple port calls colliding. Cowork builds the optimised schedule, port-by-port agents brief and demurrage / bunker economics.',
    'skills': [
        'Multi-port schedule optimisation',
        'Demurrage / bunker economics under reschedule',
        'Port agent coordination',
    ],
    'instructions': [
        'Open Cowork',
        'Attach the 3 source files',
        'Paste the prompt',
    ],
    'sample_files': [
        ('SHIP_Fleet_Schedule.xlsx', 'xlsx'),
        ('SHIP_Port_Berth_Availability.xlsx', 'xlsx'),
        ('SHIP_Cargo_Manifests.xlsx', 'xlsx'),
    ],
    'prompts': [{
        'label': 'Port call optimisation',
        'text': (
            "Using the 3 attached files, build the [PERIOD] port call optimisation. In parallel:\n"
            "1) Excel — optimised schedule across the fleet honouring berth availability + tide / draft windows.\n"
            "2) Excel — bunker + demurrage economics under the new schedule with sensitivity to a 12h delay.\n"
            "3) PowerPoint — 6-slide Commercial team brief.\n"
            "4) Outlook — port agent letters per port with the revised ETA + berth ask.\n"
            "5) Teams — Master Mariner brief on bunker / supply implications.\n"
            "Cite the file + tab for every schedule constraint. Flag any tide / draft window we are at risk of missing."
        )
    }],
    'expected': [
        'Optimised schedule',
        'Bunker / demurrage model',
        'Commercial brief',
        'Port-agent letters',
        'Master Mariner brief',
    ],
    'watch': [
        'Tide / draft risks surfaced',
        'Demurrage / bunker trade-off explicit',
    ],
    'honest': 'Port slot availability moves hourly — Cowork builds from the data given; Operations Centre confirms before any port agent is told.',
    'tips': [
        'Variation: add a CII / IMO compliance overlay',
        'Variation: produce a charterer-comms version focused on cargo ETA',
    ],
}
