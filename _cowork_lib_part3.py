# -*- coding: utf-8 -*-
"""Energy + Manufacturing + Agriculture + Construction Cowork use cases."""

CARDS = {}

CARDS['uc-og-upstream-lifting'] = {
    'title': 'Monthly Lifting Programme Optimisation',
    'dept_tag': 'Production Operations',
    'industry_tag': 'O&G Upstream',
    'complexity': 'advanced',
    'apps': ['Excel', 'PowerPoint', 'Outlook', 'Teams'],
    'desc': 'Field production forecasts, vessel availability, buyer nominations, and pipeline capacity converge into the optimised lifting schedule with shipping economics.',
    'skills': [
        'Multi-constraint scheduling (vessel × buyer × pipeline × price window)',
        'Shipping freight + demurrage economics with sensitivity',
        'Buyer-priority negotiation framing with explicit trade-offs',
    ],
    'instructions': [
        'Open Cowork',
        'Attach the 4 source files',
        'Paste the prompt',
    ],
    'sample_files': [
        ('OGU_Field_Production_Forecast.xlsx', 'xlsx'),
        ('OGU_Vessel_Availability.xlsx', 'xlsx'),
        ('OGU_Buyer_Nominations.xlsx', 'xlsx'),
        ('OGU_Pipeline_Capacity_Schedule.xlsx', 'xlsx'),
    ],
    'prompts': [{
        'label': 'Lifting programme',
        'text': (
            "Using the 4 attached files, build the [MONTH] lifting programme for [FIELD]. In parallel:\n"
            "1) Optimise the schedule in Excel — assign each cargo to vessel + buyer + lifting window, honouring pipeline capacity and price-window preferences.\n"
            "2) Compute shipping economics per cargo — freight, demurrage, port fees + sensitivity if shipped within +/- 3 days.\n"
            "3) Build a 6-slide deck for the Production Committee — schedule + economics + risks.\n"
            "4) Draft buyer-facing nomination response emails — accepted / partial / deferred + rationale.\n"
            "5) Draft a Teams message to the Marine Operations team — sailing dates, ETA windows, key contacts.\n"
            "Cite the source file + cell for every constraint. Flag any forecast vs vessel slot conflict."
        )
    }],
    'expected': [
        'Optimised lifting schedule',
        'Shipping economics with sensitivity',
        '6-slide Production Committee deck',
        'Buyer nomination responses',
        'Marine Ops Teams briefing',
    ],
    'watch': [
        'Conflicts surfaced before they hit the operations team',
        'Buyer trade-offs explicit — no silent prioritisation',
        'Demurrage cost auto-included — not an afterthought',
    ],
    'honest': 'Cowork optimises against the inputs. The Production Manager and Trader still sign off. Vessel availability is operationally fluid — confirm with Marine Ops in real time. Buyer relationships have a political dimension Cowork cannot weight.',
    'tips': [
        'For LNG, add the cargo cooling + boil-off overlay',
        'For condensate, add the API gravity + sulphur premium/discount',
        'Re-run weekly during peak refining maintenance season',
    ],
}

CARDS['uc-og-hse-pmortem'] = {
    'title': 'HSE Incident — Regulator-Grade Postmortem',
    'dept_tag': 'HSE',
    'industry_tag': 'O&G',
    'complexity': 'advanced',
    'apps': ['Word', 'Excel', 'PowerPoint', 'Outlook'],
    'desc': 'A LOPC / near-miss / process safety incident gets the bow-tie analysis, regulator notification, executive briefing, and lessons-learned campaign in one Cowork run.',
    'skills': [
        'Bow-tie diagram description (threats, top event, consequences, barriers)',
        'Regulator-grade chronology with no speculation',
        'Cross-asset lessons-learned campaign assembly',
    ],
    'instructions': [
        'Open Cowork',
        'Attach the 4 incident artefacts',
        'Paste the prompt',
    ],
    'sample_files': [
        ('HSE_Incident_Wartime_Log.docx', 'docx'),
        ('HSE_DCS_Trip_Sequence.xlsx', 'xlsx'),
        ('HSE_Witness_Statements.docx', 'docx'),
        ('HSE_Asset_Bowtie_Library.docx', 'docx'),
    ],
    'prompts': [{
        'label': 'Process-safety postmortem',
        'text': (
            "Using the 4 attached files for incident [INC-ID] at [ASSET], in parallel:\n"
            "1) Reconstruct the chronology in Word — minute-by-minute from DCS trip sequence + war-room log + witness statements. No speculation.\n"
            "2) Build the bow-tie analysis — threats, top event, consequences, barrier failures (preventive + mitigative).\n"
            "3) Draft the regulator notification letter — formal tone, factual chronology, no admission of liability without legal sign-off.\n"
            "4) Build a 10-slide Group Executive briefing in PowerPoint — what happened, why, immediate containment, lasting fix.\n"
            "5) Draft the cross-asset lessons-learned campaign — Outlook email to all asset managers + Teams safety-share post + 1-page leaflet for shift-handover boards.\n"
            "Cite the artefact + timestamp for every claim. Mark any inference as inference, not fact."
        )
    }],
    'expected': [
        'Minute-by-minute chronology',
        'Bow-tie analysis',
        'Regulator notification letter',
        '10-slide Exec briefing',
        'Cross-asset lessons campaign',
    ],
    'watch': [
        'Inference distinguished from fact — regulator-grade discipline',
        'Bow-tie surfaces barrier failures, not just causes',
        'Cross-asset campaign prevents the same incident at a sister site',
    ],
    'honest': 'Cowork structures the response. Legal MUST review the regulator letter. Independent investigation may be statutory — Cowork output does not replace it. The bow-tie is starter-grade; HSE engineers refine.',
    'tips': [
        'For DOSH / MIGAS / SKK Migas variants, swap the notification template',
        'Add a 6th task — Insurer notification letter for the property + business-interruption claim',
        'For offshore assets, add the MAIB / NOPSEMA notification overlay',
    ],
}

CARDS['uc-og-downstream-margin'] = {
    'title': 'Refining Margin Daily Brief',
    'dept_tag': 'Trading',
    'industry_tag': 'O&G Downstream',
    'complexity': 'intermediate',
    'apps': ['Excel', 'PowerPoint', 'Teams'],
    'desc': 'Crude slate, yields, product prices, freight, and inventory drive the daily refining margin brief — with sensitivity to crude switching and product mix changes.',
    'skills': [
        'GRM (Gross Refining Margin) decomposition by product',
        'Crude-switch sensitivity (Tapis vs Murban vs Arab Light)',
        'Trading-floor briefing tone (concise, actionable)',
    ],
    'instructions': [
        'Open Cowork',
        'Attach the 4 daily data files',
        'Paste the prompt',
    ],
    'sample_files': [
        ('REF_Crude_Slate_T0.xlsx', 'xlsx'),
        ('REF_Yield_Pattern.xlsx', 'xlsx'),
        ('REF_Product_Prices_T0.xlsx', 'xlsx'),
        ('REF_Inventory_Position.xlsx', 'xlsx'),
    ],
    'prompts': [{
        'label': 'Daily margin brief',
        'text': (
            "Using the 4 attached files, build the daily refining margin brief for [REFINERY]. In parallel:\n"
            "1) Compute GRM in USD/bbl in Excel — decomposed by product (gasoline / diesel / jet / fuel oil).\n"
            "2) Run a crude-switch sensitivity — Tapis vs Murban vs Arab Light at current freight differentials.\n"
            "3) Build a 4-slide trading-floor briefing — yesterday GRM, today GRM, drivers, recommended action.\n"
            "4) Draft a Teams message to the Trading Desk — buy/hold/sell on each product + crude switch trigger.\n"
            "5) Build an alert list — any product where inventory > 30 days cover + price falling.\n"
            "Cite the cell range for every figure. Use USD/bbl consistently."
        )
    }],
    'expected': [
        'GRM with product decomposition',
        'Crude-switch sensitivity',
        '4-slide briefing',
        'Trading Desk action message',
        'Inventory alert list',
    ],
    'watch': [
        'GRM decomposed — not a single bland number',
        'Crude switch quantified — actionable for the buyer',
        'Inventory alert prevents margin trap on stale stock',
    ],
    'honest': 'Cowork models. Trading decisions still need the Chief Trader sign-off. Live prices have a lag; final RFQ confirms. Crude switching has commercial-contract constraints Cowork cannot see.',
    'tips': [
        'Add bunker-fuel + LNG variants for integrated downstream players',
        'Re-run as monthly cracking-margin review for the Refinery Committee',
        'Add freight-route alternatives (Suez vs Cape) for crude logistics',
    ],
}

CARDS['uc-renewable-ppa'] = {
    'title': 'PPA / Tariff Bid Pack',
    'dept_tag': 'Commercial',
    'industry_tag': 'Renewable Energy',
    'complexity': 'advanced',
    'apps': ['Excel', 'Word', 'PowerPoint'],
    'desc': 'Resource assessment, LCOE build-up, offtake market analysis, and EPC quotes converge into a tariff bid pack with legal annex and investor IC paper.',
    'skills': [
        'LCOE modelling with capacity factor + degradation + tax-equity inputs',
        'Bid-strategy framing — under-bid risk vs win probability',
        'Investor IC paper for project finance lender + sponsor approval',
    ],
    'instructions': [
        'Open Cowork',
        'Attach the 4 source files',
        'Paste the prompt',
    ],
    'sample_files': [
        ('REN_Resource_Assessment.xlsx', 'xlsx'),
        ('REN_LCOE_Model.xlsx', 'xlsx'),
        ('REN_Offtake_Market_Analysis.docx', 'docx'),
        ('REN_EPC_Quote_Summary.xlsx', 'xlsx'),
    ],
    'prompts': [{
        'label': 'PPA bid pack',
        'text': (
            "Using the 4 attached files, build the bid pack for the [PROJECT] PPA tender. In parallel:\n"
            "1) Refresh the LCOE model in Excel — capacity factor / degradation / OPEX / financing / tax incentives. Show breakeven tariff per scenario (Base / Conservative / Stretch).\n"
            "2) Build the bid strategy in PowerPoint — recommended bid + win probability + IRR under each scenario.\n"
            "3) Draft the technical proposal in Word — Resource / Technology / Plant configuration / Schedule / O&M plan.\n"
            "4) Draft the legal annex pointer document — which clauses we want amended in the standard PPA template.\n"
            "5) Build the Investor IC paper — for the project finance lender + the sponsor approval committee.\n"
            "Cite the model sheet + assumption for every number."
        )
    }],
    'expected': [
        'Refreshed LCOE',
        'Bid strategy with IRR + win probability',
        'Technical proposal',
        'PPA legal annex',
        'Investor IC paper',
    ],
    'watch': [
        'Win probability quantified — not "we will win"',
        'Conservative scenario stress-tests the worst case',
        'Legal annex flags non-negotiable clauses upfront',
    ],
    'honest': 'Cowork models. The Bid Manager and CFO sign off. Resource assessment is the upstream input — model results are only as good as the wind/solar resource report. Lender due diligence will re-do the LCOE independently.',
    'tips': [
        'For corporate PPAs, swap to a private offtaker template',
        'Add a 6th task — environmental + social due diligence summary (IFC PS / Equator Principles)',
        'For battery storage, add the cycle-degradation + market-price overlay',
    ],
}

CARDS['uc-mfg-recall'] = {
    'title': 'Quality Batch Recall Decision Brief',
    'dept_tag': 'Quality',
    'industry_tag': 'Industrial Manufacturing',
    'complexity': 'advanced',
    'apps': ['Word', 'Excel', 'Outlook', 'Teams'],
    'desc': 'A failed QA result triggers a structured recall decision — affected batches, customer exposure, regulatory obligation, financial impact, and the trigger comms — in one pass.',
    'skills': [
        'Batch genealogy tracing (lot → shipment → customer)',
        'Regulatory obligation mapping per market',
        'Recall vs retain decision framing with quantified downside',
    ],
    'instructions': [
        'Open Cowork',
        'Attach the QA result + batch master + customer shipment log + recall SOP',
        'Paste the prompt',
    ],
    'sample_files': [
        ('QA_Failed_Test_Result.pdf', 'pdf'),
        ('QA_Batch_Genealogy.xlsx', 'xlsx'),
        ('QA_Customer_Shipment_Log.xlsx', 'xlsx'),
        ('QA_Recall_SOP.docx', 'docx'),
    ],
    'prompts': [{
        'label': 'Recall decision brief',
        'text': (
            "Using the 4 attached files for failed batch [BATCH-ID], in parallel:\n"
            "1) Trace the batch genealogy in Excel — affected lots / shipments / customers / countries / volumes.\n"
            "2) Map regulatory obligations per destination market — Notify / Recall / Public-warning / No-action thresholds.\n"
            "3) Quantify the financial impact in Excel — replacement cost / freight / customer goodwill / liability exposure under each option (Recall all / Partial / Retain-with-monitoring).\n"
            "4) Draft a 3-page decision brief in Word for the Quality Director — recommended option + rationale + risks.\n"
            "5) Draft trigger comms — customer notification email, regulator pre-notification letter, factory-floor Teams message.\n"
            "Cite the batch ID + shipment reference for every claim. Flag any retained risk explicitly."
        )
    }],
    'expected': [
        'Batch genealogy',
        'Per-market obligation map',
        'Financial impact by option',
        'Decision brief',
        'Trigger comms',
    ],
    'watch': [
        'Per-market obligation explicit — no missed jurisdiction',
        'Retain-vs-recall trade-off quantified — not gut feel',
        'Comms drafted before the decision lands — no panic delay',
    ],
    'honest': 'Cowork structures. Quality Director and CEO own the final decision. Some markets require regulator pre-notification within hours — check live timelines. Counsel must review every external comms.',
    'tips': [
        'For food / pharma, add the consumer-safety threshold overlay',
        'For automotive, add the NHTSA / regulator severity classification',
        'For electronics, add the field-failure rate + warranty cost overlay',
    ],
}

CARDS['uc-mfg-oee'] = {
    'title': 'OEE Variance & Recovery Plan',
    'dept_tag': 'Operations',
    'industry_tag': 'Manufacturing',
    'complexity': 'intermediate',
    'apps': ['Excel', 'PowerPoint', 'Teams'],
    'desc': 'Line-level OEE drop into the three buckets (Availability / Performance / Quality) gets root-caused and a 30-day recovery plan with named owners and a daily standup pack.',
    'skills': [
        'OEE decomposition across the 3 dimensions',
        'Pareto + 5-why for top losses',
        'Daily standup pack with KPI traffic lights',
    ],
    'instructions': [
        'Open Cowork',
        'Attach the OEE log + downtime codes + first-pass yield + shift handover notes',
        'Paste the prompt',
    ],
    'sample_files': [
        ('OEE_30D_Log_Line5.xlsx', 'xlsx'),
        ('OEE_Downtime_Code_Master.xlsx', 'xlsx'),
        ('OEE_First_Pass_Yield.xlsx', 'xlsx'),
        ('OEE_Shift_Handover_Notes.docx', 'docx'),
    ],
    'prompts': [{
        'label': 'OEE recovery plan',
        'text': (
            "Using the 4 attached files for Line [LINE-ID], in parallel:\n"
            "1) Decompose OEE in Excel — Availability × Performance × Quality + show the 30-day trend.\n"
            "2) Pareto the top 5 downtime drivers + 5-why each.\n"
            "3) Build a 30-day recovery plan in Excel — Action / Owner / Expected lift / Due date / Status.\n"
            "4) Build a 5-slide daily standup pack in PowerPoint — yesterday actual vs target, today plan, blockers.\n"
            "5) Draft a Teams message to the Line Lead + Production Manager + Quality Manager — what changes Monday morning.\n"
            "Cite the log timestamp + downtime code for every claim."
        )
    }],
    'expected': [
        'OEE decomposition with trend',
        'Pareto + 5-why',
        '30-day recovery plan',
        'Daily standup pack',
        'Line-lead Teams message',
    ],
    'watch': [
        'OEE split into the 3 buckets — not a single rolled-up number',
        'Each action has an expected lift quantified',
        '5-why drills past the surface code',
    ],
    'honest': 'Cowork structures. Operators on the line still own the standup. Some downtime codes get over-coded (e.g. "machine fault" used for any unscheduled stop) — clean the code data before relying on Pareto.',
    'tips': [
        'For multi-line plants, re-run per line then aggregate',
        'Add a 6th task — Capex business case for the top remediation (if it needs investment)',
        'Re-run as monthly Plant Manager review',
    ],
}

CARDS['uc-rubber-fda510k'] = {
    'title': 'US FDA 510(k) Refresh Submission',
    'dept_tag': 'Regulatory Affairs',
    'industry_tag': 'Rubber Gloves',
    'complexity': 'advanced',
    'apps': ['Word', 'Excel'],
    'desc': 'A formulation tweak triggers an FDA 510(k) substantial-equivalence refresh — predicate device mapping, performance data, biocompatibility, and the cover letter assembled in one Cowork run.',
    'skills': [
        'Predicate-device mapping for substantial-equivalence claim',
        'Performance testing summary against ASTM standards',
        'Biocompatibility evidence package per ISO 10993',
    ],
    'instructions': [
        'Open Cowork',
        'Attach the change-control + predicate-device dossier + test data + biocompatibility report',
        'Paste the prompt',
    ],
    'sample_files': [
        ('GLV_Change_Control.docx', 'docx'),
        ('GLV_Predicate_Device_Dossier.pdf', 'pdf'),
        ('GLV_ASTM_Test_Data.xlsx', 'xlsx'),
        ('GLV_ISO10993_Biocompat_Report.pdf', 'pdf'),
    ],
    'prompts': [{
        'label': '510(k) refresh pack',
        'text': (
            "Using the 4 attached files for the [PRODUCT] formulation refresh, in parallel:\n"
            "1) Draft the 510(k) cover letter + indications-for-use form in Word.\n"
            "2) Build the substantial-equivalence table in Excel — Predicate vs Subject device × Indications / Materials / Design / Performance / Biocompatibility.\n"
            "3) Summarise the ASTM performance data tables — D6319 / D3578 / D5151 results with pass-fail call-outs.\n"
            "4) Summarise the ISO 10993 biocompatibility evidence with explicit endpoint coverage.\n"
            "5) Build the internal Q&A document — top 6 likely FDA queries + responses.\n"
            "Cite the predicate K-number for every equivalence claim. Mark any non-equivalence point in red."
        )
    }],
    'expected': [
        'Cover letter + IFU form',
        'Substantial-equivalence table',
        'ASTM performance summary',
        'ISO 10993 evidence summary',
        'Anticipated Q&A',
    ],
    'watch': [
        'Non-equivalence flagged in red — reviewer-ready honesty',
        'Predicate K-number cited for every claim',
        'ASTM endpoints called by clause, not summarised away',
    ],
    'honest': 'Cowork drafts. The Regulatory Affairs Director + Notified Body equivalent + FDA reviewer all have a say. ASTM tests must come from accredited labs — Cowork cannot generate test data. Predicate selection has strategic implications and is the RA team\'s judgement.',
    'tips': [
        'For EU, swap to MDR Technical Documentation structure',
        'For surgical gloves, add the sterility validation overlay (ISO 11135 / 11137)',
        'Add a 6th task — Marketing claims review (FTC alignment in the US)',
    ],
}

CARDS['uc-semicon-capacity'] = {
    'title': 'Fab Capacity Re-allocation',
    'dept_tag': 'Manufacturing Strategy',
    'industry_tag': 'Semiconductor',
    'complexity': 'advanced',
    'apps': ['Excel', 'PowerPoint', 'Outlook', 'Teams'],
    'desc': 'Backlog by customer × node × wafer, plus equipment utilisation and competing capex plans, drive a capacity-reallocation decision with customer-by-customer comms.',
    'skills': [
        'Backlog ageing × customer importance scoring',
        'Equipment-bottleneck identification',
        'Customer-by-customer commercial impact framing',
    ],
    'instructions': [
        'Open Cowork',
        'Attach the backlog + equipment util + customer master + capex schedule',
        'Paste the prompt',
    ],
    'sample_files': [
        ('SC_Backlog_By_Customer_Node.xlsx', 'xlsx'),
        ('SC_Equipment_Utilization.xlsx', 'xlsx'),
        ('SC_Customer_Master_Strategic_Tier.xlsx', 'xlsx'),
        ('SC_Capex_Schedule.xlsx', 'xlsx'),
    ],
    'prompts': [{
        'label': 'Capacity re-allocation',
        'text': (
            "Using the 4 attached files, build the [QUARTER] fab capacity re-allocation plan. In parallel:\n"
            "1) Compute backlog ageing in Excel — by customer × node × wafer start week.\n"
            "2) Identify the top 3 equipment bottlenecks — propose move work / pull in capex / qualify alternative tool.\n"
            "3) Score customers — Strategic tier × volume × margin × multi-year commitment. Recommend who gets priority slots.\n"
            "4) Draft customer-specific commercial comms in Outlook — Tier 1 get prioritised slots + apology for any push-out; Tier 3 get a deferred quote.\n"
            "5) Draft an internal Teams message to the Account Managers — what to expect, who escalates how.\n"
            "Cite the bottleneck + customer ID for every recommendation."
        )
    }],
    'expected': [
        'Backlog ageing',
        'Bottleneck remediation',
        'Customer prioritisation table',
        'Tier-1 customer comms',
        'Account Manager briefing',
    ],
    'watch': [
        'Customer tiering explicit — no silent re-prioritisation',
        'Capex pull-in evaluated against bottleneck — not capex-for-capex',
        'Tier 1 customer comms drafted before they hear from Sales',
    ],
    'honest': 'Cowork models. The CCO and CTO sign off — re-allocation has long-tail customer-relationship cost. Strategic tier is qualitative — refresh it before relying. Yield assumptions are the engineering team\'s.',
    'tips': [
        'For OSAT (assembly + test), add the package-mix re-allocation overlay',
        'For foundry, add the design-rule lock-in risk per customer',
        'Re-run when major customer changes its forecast > 20%',
    ],
}

CARDS['uc-auto-recall'] = {
    'title': 'Vehicle Model Recall Customer Comms',
    'dept_tag': 'Customer Experience',
    'industry_tag': 'Automotive',
    'complexity': 'advanced',
    'apps': ['Word', 'Excel', 'Outlook', 'Teams'],
    'desc': 'A model recall (safety / emission / software) gets the customer-by-customer outreach, dealer briefing, regulator notification, and inventory hold orchestrated in one pass.',
    'skills': [
        'VIN-level affected-vehicle list with owner contact',
        'Dealer briefing pack with parts + bay-time allocation',
        'Regulator notification per market + customer comms hierarchy',
    ],
    'instructions': [
        'Open Cowork',
        'Attach the affected-VIN list, dealer master, parts availability, regulator template',
        'Paste the prompt',
    ],
    'sample_files': [
        ('AUTO_Affected_VIN_List.xlsx', 'xlsx'),
        ('AUTO_Dealer_Master.xlsx', 'xlsx'),
        ('AUTO_Parts_Inventory_Forecast.xlsx', 'xlsx'),
        ('AUTO_Recall_Notice_Template.docx', 'docx'),
    ],
    'prompts': [{
        'label': 'Recall customer comms orchestration',
        'text': (
            "Using the 4 attached files for the [MODEL-YEAR] recall, in parallel:\n"
            "1) Build the customer outreach plan in Excel — affected VINs by region + assigned dealer + parts availability week + booking priority.\n"
            "2) Draft customer-facing recall notice in Outlook — empathetic tone, what to do, free service, loaner if needed.\n"
            "3) Build a dealer briefing pack in Word — symptom, fix, parts, bay time, customer-handling script.\n"
            "4) Draft regulator notifications per market — JPJ Malaysia + Kemenhub Indonesia + LTA Singapore.\n"
            "5) Draft a Teams message to the National Sales Manager + Dealer Network Manager — daily milestone reporting cadence.\n"
            "Cite the VIN sample for every region. Sequence outreach so parts arrive before customers call."
        )
    }],
    'expected': [
        'Customer outreach plan',
        'Customer recall notice',
        'Dealer briefing pack',
        'Per-market regulator notifications',
        'Sales-network Teams briefing',
    ],
    'watch': [
        'Outreach sequenced to parts availability — no booking with no parts',
        'Per-market notification — no missed jurisdiction',
        'Dealer script ensures consistent customer handling',
    ],
    'honest': 'Cowork drafts. Legal and Comms must review every external letter. Regulator timelines differ per market — confirm. Loaner-car economics + free-service cost need Finance sign-off.',
    'tips': [
        'For EVs, add the OTA software fix track in parallel with the mechanical fix',
        'For commercial vehicles, add fleet-customer escalation paths',
        'Re-run as a proactive Service Action campaign for non-safety items',
    ],
}

CARDS['uc-auto-tyres-compound'] = {
    'title': 'Tyre Compound Recipe Trial Report',
    'dept_tag': 'R&D',
    'industry_tag': 'Auto / Tyres',
    'complexity': 'intermediate',
    'apps': ['Excel', 'Word', 'PowerPoint'],
    'desc': 'A new rubber compound trial — rolling resistance, wet grip, wear, durability — gets the structured trial report, internal IP memo, and customer marketing brief.',
    'skills': [
        'Trial data normalisation across 12 KPIs',
        'Statistical-significance check on improvements',
        'IP-claim drafting for the patent attorney',
    ],
    'instructions': [
        'Open Cowork',
        'Attach the trial data, prior generation baseline, customer-spec target, patent landscape memo',
        'Paste the prompt',
    ],
    'sample_files': [
        ('TYR_Trial_Data_Run_42.xlsx', 'xlsx'),
        ('TYR_Prior_Gen_Baseline.xlsx', 'xlsx'),
        ('TYR_Customer_Spec_Target.docx', 'docx'),
        ('TYR_Patent_Landscape_Memo.docx', 'docx'),
    ],
    'prompts': [{
        'label': 'Compound trial pack',
        'text': (
            "Using the 4 attached files for compound trial [RUN-ID], in parallel:\n"
            "1) Normalise the trial data in Excel — 12 KPIs × New compound vs Prior gen vs Customer target.\n"
            "2) Statistical significance check — confidence interval per KPI improvement.\n"
            "3) Draft the trial report in Word — Hypothesis / Method / Results / Discussion / Recommendation.\n"
            "4) Build a 6-slide customer marketing brief — what gets better, by how much, for whom.\n"
            "5) Draft the IP claim memo for the patent attorney — novel features + closest prior art + recommended claim language.\n"
            "Cite the trial run + KPI cell for every claim. Mark any KPI where improvement is below statistical significance threshold."
        )
    }],
    'expected': [
        'Normalised trial data',
        'Statistical significance check',
        'Trial report',
        'Customer marketing brief',
        'IP claim memo',
    ],
    'watch': [
        'Significance threshold respected — no hyping noise',
        'Customer target sits next to actual delta — no over-promise',
        'Patent-attorney brief prevents amateur claim language',
    ],
    'honest': 'Cowork structures. R&D Director signs off. Significance check assumes the trial design is sound — DoE choice still the engineer\'s. Patent attorney does the final claim language.',
    'tips': [
        'For OE customer trials, add the homologation-process tracker',
        'For after-market launches, add the channel-marketing campaign plan',
        'Re-run as a competitive-benchmarking report by adding competitor data',
    ],
}

CARDS['uc-construction-vo'] = {
    'title': 'Variation Order Claim Defence Pack',
    'dept_tag': 'Commercial',
    'industry_tag': 'Construction',
    'complexity': 'advanced',
    'apps': ['Word', 'Excel', 'Outlook'],
    'desc': 'A contractor variation claim → defence pack assembling the contract, drawings, RFIs, and prior correspondence into a clause-by-clause rebuttal and counter-offer.',
    'skills': [
        'FIDIC / PWD-203 / JKR clause mapping',
        'Drawing-version forensics to test "instructed vs not instructed"',
        'Counter-offer numeric build with delay damages',
    ],
    'instructions': [
        'Open Cowork',
        'Attach the contract, claim submission, drawings register, RFI log',
        'Paste the prompt',
    ],
    'sample_files': [
        ('CON_Contract_FIDIC_Yellow.pdf', 'pdf'),
        ('CON_Variation_Claim_Submitted.pdf', 'pdf'),
        ('CON_Drawing_Register.xlsx', 'xlsx'),
        ('CON_RFI_Log.xlsx', 'xlsx'),
    ],
    'prompts': [{
        'label': 'VO defence pack',
        'text': (
            "Using the 4 attached files for variation claim [VO-ID], in parallel:\n"
            "1) Build the clause-by-clause rebuttal in Word — each contractor claim point + relevant FIDIC clause + our position + evidence reference.\n"
            "2) Map drawing versions in Excel — when was each version issued, did it reach the contractor, did it instruct the variation.\n"
            "3) RFI cross-check — did the contractor raise an RFI before doing the work, or after.\n"
            "4) Build the counter-offer in Excel — what we accept (with rationale), what we reject, delay-damages we counterclaim.\n"
            "5) Draft the response letter to the contractor + email to the project owner + internal Teams message.\n"
            "Cite contract clause + drawing version + RFI number for every rebuttal."
        )
    }],
    'expected': [
        'Clause-by-clause rebuttal',
        'Drawing-version forensics',
        'RFI cross-check',
        'Counter-offer with delay damages',
        'Response correspondence',
    ],
    'watch': [
        'Every rebuttal cites a clause + evidence — not subjective',
        'RFI cross-check separates instructed from opportunistic claims',
        'Counter-offer leaves room for negotiation without admitting liability',
    ],
    'honest': 'Cowork structures. Project Director + General Counsel sign off. FIDIC interpretation is contested — adjudicator may rule differently. Document discoverable; keep tone professional.',
    'tips': [
        'For PWD / JKR contracts, swap the clause map',
        'Add a 6th task — adjudicator pack assembly in case of dispute escalation',
        'Re-run quarterly across the project portfolio to spot claim patterns',
    ],
}

CARDS['uc-plantation-rspo'] = {
    'title': 'RSPO Estate Audit Recovery',
    'dept_tag': 'Sustainability',
    'industry_tag': 'Plantation',
    'complexity': 'advanced',
    'apps': ['Word', 'Excel', 'Outlook', 'Teams'],
    'desc': 'RSPO audit non-conformities trigger a 90-day recovery programme — estate-level action plans, buyer notifications, and Board briefing in one Cowork run.',
    'skills': [
        'P&C non-conformity mapping (Major / Minor)',
        'Estate-level corrective action ownership',
        'Buyer disclosure under their sustainability policy',
    ],
    'instructions': [
        'Open Cowork',
        'Attach the audit findings, certification manual, estate SOP, buyer contracts',
        'Paste the prompt',
    ],
    'sample_files': [
        ('PLT_Audit_NCRs.pdf', 'pdf'),
        ('PLT_MSPO_RSPO_Manual.docx', 'docx'),
        ('PLT_Estate_SOP_Master.docx', 'docx'),
        ('PLT_Buyer_Contracts_Sustainability_Clauses.xlsx', 'xlsx'),
    ],
    'prompts': [{
        'label': 'RSPO recovery pack',
        'text': (
            "Using the 4 attached files, prepare the 90-day RSPO recovery programme. In parallel:\n"
            "1) Map each non-conformity in Excel — Severity / Estate affected / P&C clause / Root cause / Corrective action / Owner / Due / Buyer impact.\n"
            "2) Build a 90-day weekly calendar in Word — week-by-week milestone with the responsible estate manager.\n"
            "3) Draft buyer notification letters in Outlook — what we found, what we are doing, when we will be re-audit-ready, supply-continuity assurance.\n"
            "4) Build a 6-slide Board Risk Committee briefing in PowerPoint.\n"
            "5) Draft a Teams message to the Heads of Estate Operations — week-1 actions per estate.\n"
            "Cite the P&C clause + estate code for every entry. Highlight obligations that contradict a current SOP."
        )
    }],
    'expected': [
        'Non-conformity matrix',
        '90-day weekly recovery calendar',
        'Buyer notification letters',
        'Board Risk briefing',
        'Estate-ops Teams message',
    ],
    'watch': [
        'Each NCR maps to a named P&C clause + estate — auditable',
        'SOP-vs-obligation contradictions surfaced — fix the SOP, not just the symptom',
        'Buyer notifications protect supply continuity while disclosing honestly',
    ],
    'honest': 'Cowork structures. Group Sustainability Director and the certification body still own the verification. Estate-level reality (smallholder dependencies, FFB supply) limits some corrective actions — engage suppliers before promising the date.',
    'tips': [
        'For Indonesia, layer ISPO on top of RSPO',
        'For Malaysia, layer MSPO on top of RSPO',
        'Add a 6th task — smallholder communication brief (Bahasa Malaysia + Bahasa Indonesia)',
    ],
}

CARDS['uc-food-promo'] = {
    'title': 'Festive Promo Campaign Pack',
    'dept_tag': 'Marketing',
    'industry_tag': 'Food & FMCG',
    'complexity': 'intermediate',
    'apps': ['Word', 'Excel', 'PowerPoint', 'Outlook'],
    'desc': 'Hari Raya / Lebaran / Deepavali campaign assembly — creative brief, channel-by-channel placement, BTL retailer pack, and finance approval memo.',
    'skills': [
        'Multi-channel campaign assembly (ATL + BTL + digital + retailer)',
        'SKU-by-SKU promo economics (margin sacrifice vs volume lift)',
        'Cultural-tone calibration for festive season',
    ],
    'instructions': [
        'Open Cowork',
        'Attach the brand strategy, retailer master, SKU master, prior campaign learnings',
        'Paste the prompt',
    ],
    'sample_files': [
        ('FMCG_Brand_Strategy.docx', 'docx'),
        ('FMCG_Retailer_Master.xlsx', 'xlsx'),
        ('FMCG_SKU_Master_Pricing.xlsx', 'xlsx'),
        ('FMCG_Prior_Campaign_Learnings.docx', 'docx'),
    ],
    'prompts': [{
        'label': 'Festive campaign pack',
        'text': (
            "Using the 4 attached files, build the [FESTIVE] campaign. In parallel:\n"
            "1) Draft the creative brief in Word — Big idea / Cultural insight / Key visual concepts / Tagline (EN + BM + BI variants).\n"
            "2) Build the channel plan in Excel — ATL (TV / OOH) × BTL (in-store) × Digital (social / search) × Retailer-specific tactics. Show spend mix + expected GRP.\n"
            "3) Compute SKU-level promo economics — margin sacrifice / expected volume lift / net contribution per retailer.\n"
            "4) Build a 10-slide Finance Committee approval deck.\n"
            "5) Draft retailer BTL packs + Outlook emails to Key Account Managers + Teams brief to Trade Marketing.\n"
            "Cite the SKU + retailer for every economic claim. Flag any SKU below 5% net contribution post-promo."
        )
    }],
    'expected': [
        'Creative brief',
        'Channel plan with spend mix',
        'SKU-level promo economics',
        'Finance Committee deck',
        'Retailer BTL pack',
    ],
    'watch': [
        'Multi-language taglines drafted, not translated word-for-word',
        'SKU contribution explicit — no margin destruction in the name of share',
        'Festive cultural sensitivity baked in — not bolted on',
    ],
    'honest': 'Cowork structures. The CMO and Brand Director sign off. Cultural lines benefit from local agency review — Cowork drafts a starting point. Promo regulations differ by market (BNM advertising codes, KPDN consumer-protection rules).',
    'tips': [
        'For HoReCa-focused brands, add the on-trade execution overlay',
        'For multi-brand portfolios, run a portfolio-level competition analysis first',
        'Add a 6th task — agency RFP scoring if a new creative agency is in the running',
    ],
}
