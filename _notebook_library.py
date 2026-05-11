"""Notebook Library — per-entry Copilot Notebook use cases.

Each card models a 5-source Notebook setup with a specific business decision
flow. Cards are DIFFERENT per archetype (RFP synthesis for procurement,
clinical case prep for healthcare, regulatory cross-ref for banking, etc.).

Shape:
{
  'title': 'Persona — RFP Synthesis',
  'archetype': 'procurement_rfp',     # category tag
  'complexity': 'intermediate',
  'sources': [('file.docx','docx'), ...],   # 5 files
  'instructions': 'You are reviewing RFP submissions ...',
  'desc': 'Compare 4 vendor RFP responses against a scoring rubric ...',
  'prompts': [
    {'label':'Prompt 1 — Scorecard sweep','text':'...'},
    {'label':'Prompt 2 — Risk surfacing','text':'...'},
    {'label':'Prompt 3 — Negotiation playbook','text':'...'}
  ],
  'expected': ['...'],
  'watch': ['...'],   # green callout
  'honest': '...',     # amber callout
  'tips': ['...']
}

Cards are keyed by id (e.g. 'nb-rfp-procurement') and mapped to entries via
ENTRY_NB_USE_CASES below. Most entries get 2-3 cards.
"""

# ════════════════════════════════════════════════════════════════════════════
# UNIVERSAL CARDS — relevant to any entry, used as fallback/cross-pollination
# ════════════════════════════════════════════════════════════════════════════

USE_CASES = {

# ────────────────────────────────────────────────────────────────────────────
# Procurement / RFP archetype
# ────────────────────────────────────────────────────────────────────────────
'nb-rfp-procurement': {
    'title': 'RFP Vendor Synthesis',
    'archetype': 'procurement_rfp',
    'complexity': 'intermediate',
    'sources': [
        ('Vendor_A_RFP_Response.pdf','pdf'),
        ('Vendor_B_RFP_Response.pdf','pdf'),
        ('Vendor_C_RFP_Response.pdf','pdf'),
        ('Vendor_D_RFP_Response.pdf','pdf'),
        ('Scoring_Rubric_and_Requirements.xlsx','xlsx'),
    ],
    'instructions': ('You are evaluating 4 vendor RFP responses against the '
        'scoring rubric. Cite every claim back to the vendor name + RFP section. '
        'Flag where vendors are silent on a mandatory requirement. Stay '
        'evidence-bound — do not infer beyond what is in the responses.'),
    'desc': ('Load 4 vendor RFP responses and the scoring rubric. Use Notebook '
        'to score, surface risks, and draft the recommendation memo without '
        'context-switching between PDFs.'),
    'prompts': [
        {'label':'Prompt 1 — Scorecard sweep','text':(
            'Score all 4 vendors against the rubric in /Scoring_Rubric_and_Requirements.xlsx. '
            'For each criterion give: vendor name, score 1-5 with the exact RFP section it '
            'came from, and a one-line justification. End with a weighted summary table '
            'using the rubric weights. Flag any criterion where a vendor is silent.')},
        {'label':'Prompt 2 — Risk surfacing','text':(
            'List the 5 biggest commercial, technical and compliance risks across the 4 '
            'responses. For each: (1) the risk in one sentence, (2) which vendor it applies '
            'to, (3) the exact RFP section, (4) Red/Amber/Green severity, (5) the '
            'clarification question to send to the vendor.')},
        {'label':'Prompt 3 — Negotiation playbook','text':(
            'Draft a 1-page negotiation playbook for the shortlist (top 2 vendors). For each '
            'shortlist vendor list: their commercial gaps, their compliance gaps, the 3 '
            'concessions to request, and the BATNA if they refuse. Cite RFP section for every '
            'claim.')},
    ],
    'expected': [
        'A defensible scorecard with line-by-line citations.',
        'A ranked risk register pointing to exact RFP sections.',
        'A negotiation playbook the buyer can hand to Procurement.',
    ],
    'watch': [
        'Numbers in the scorecard match the rubric weights in the Excel file.',
        'Every score cites a specific RFP section (page or heading).',
        'Silent / non-responsive criteria are flagged, not invented.',
    ],
    'honest': ('Copilot Notebook does not negotiate for you and cannot read between the lines '
        'of a vendor pitch. The 1-page playbook is a starting draft — Procurement still owns '
        'the conversation and the final BATNA.'),
    'tips': [
        'Add the contract template as a 6th source if you also need redline language.',
        'For follow-up clarifications, ask Copilot to draft the email back to each vendor.',
        'Re-run the scorecard prompt after any clarification to see the score shift.',
    ],
},

# ────────────────────────────────────────────────────────────────────────────
# Clinical / case-conference archetype
# ────────────────────────────────────────────────────────────────────────────
'nb-clinical-case': {
    'title': 'Clinical Case Conference Prep',
    'archetype': 'clinical_case',
    'complexity': 'advanced',
    'sources': [
        ('Patient_History_Summary.docx','docx'),
        ('Imaging_Report_MRI.pdf','pdf'),
        ('Lab_Results_Panel.xlsx','xlsx'),
        ('Clinical_Guidelines_Pathway.pdf','pdf'),
        ('Multidisciplinary_Team_Notes.docx','docx'),
    ],
    'instructions': ('You are preparing the multidisciplinary case-conference brief. '
        'Cite every clinical observation to its source file and date. Flag any contradiction '
        'between imaging, labs, and the guidelines. Do NOT recommend treatment beyond what '
        'the guidelines authorise — surface options for the clinical team to decide.'),
    'desc': ('Build a tight 1-page case conference brief that pulls patient history, imaging, '
        'labs and the pathway guidelines into one workspace so the MDT can decide quickly.'),
    'prompts': [
        {'label':'Prompt 1 — Case snapshot','text':(
            'Produce a 1-page case snapshot: (1) presenting complaint and timeline from '
            '/Patient_History_Summary.docx; (2) imaging findings from /Imaging_Report_MRI.pdf '
            'with exact phrases quoted; (3) abnormal lab values flagged red/amber from '
            '/Lab_Results_Panel.xlsx; (4) where the picture aligns or diverges from the '
            'pathway in /Clinical_Guidelines_Pathway.pdf. Cite every claim.')},
        {'label':'Prompt 2 — Decision options','text':(
            'List the 3-4 treatment options consistent with /Clinical_Guidelines_Pathway.pdf '
            'for this case. For each: indications met, contraindications present, key risks, '
            'and the unresolved question for the MDT. Do not recommend one option — surface '
            'the decision for clinicians.')},
        {'label':'Prompt 3 — Outstanding gaps','text':(
            'List every clinical question that is currently unanswered by the 5 sources — '
            'tests not done, history fields blank, missing consent. For each: the gap, the '
            'team member who should close it, and the urgency before the MDT meets.')},
    ],
    'expected': [
        'Concise case snapshot with quotes and lab flags.',
        'Guideline-anchored option set the MDT can debate.',
        'A pre-meeting checklist of evidence gaps to close.',
    ],
    'watch': [
        'Imaging phrases are quoted verbatim, not paraphrased.',
        'Lab thresholds match the panel reference ranges in the file.',
        'Treatment options ALL trace back to the pathway document.',
    ],
    'honest': ('This is clinician-assist tooling. Copilot Notebook does not replace clinical '
        'judgement, does not prescribe, and does not handle PHI outside the M365 tenant. '
        'Treat the snapshot as a pre-read, not a clinical decision.'),
    'tips': [
        'Add the patient consent record as a 6th source if discussing trial enrolment.',
        'For pre-MDT distribution, ask Copilot to generate the slide pack via Quick Create.',
        'Re-run prompt 3 after the MDT meets to track which gaps closed.',
    ],
},

# ────────────────────────────────────────────────────────────────────────────
# Regulatory cross-ref archetype (banking / GLC / regulated industries)
# ────────────────────────────────────────────────────────────────────────────
'nb-regulator-crossref': {
    'title': 'Regulator Cross-Reference Pack',
    'archetype': 'regulator_crossref',
    'complexity': 'advanced',
    'sources': [
        ('Regulator_Circular_2026.pdf','pdf'),
        ('Internal_Policy_Manual.docx','docx'),
        ('Audit_Findings_Last_Cycle.xlsx','xlsx'),
        ('Compliance_Register_Live.xlsx','xlsx'),
        ('Board_Risk_Appetite_Statement.docx','docx'),
    ],
    'instructions': ('You are mapping the latest regulator circular against internal policy, '
        'last cycle audit findings, the live compliance register, and Board risk appetite. '
        'Cite every requirement to its source. Flag where internal policy is silent on a new '
        'regulator obligation. Do not invent controls that the policy does not establish.'),
    'desc': ('Bridge a new regulator circular into the operating environment — what is '
        'already covered, what is not, and which audit findings now repeat.'),
    'prompts': [
        {'label':'Prompt 1 — Obligation map','text':(
            'Extract every regulator obligation from /Regulator_Circular_2026.pdf as a numbered '
            'list. For each obligation: the exact paragraph reference, whether '
            '/Internal_Policy_Manual.docx already covers it (cite section), and the gap '
            'severity Red/Amber/Green.')},
        {'label':'Prompt 2 — Repeat findings','text':(
            'Cross-reference /Audit_Findings_Last_Cycle.xlsx against the new obligations. '
            'Identify which open or closed findings will REPEAT under the new circular if no '
            'action is taken. Quote the finding ID and the obligation paragraph.')},
        {'label':'Prompt 3 — Appetite breach risk','text':(
            'Compare the new obligations against /Board_Risk_Appetite_Statement.docx. List '
            'any obligation where compliance would push us above the stated risk appetite '
            'limits. For each: the obligation, the appetite metric breached, and the option '
            'to bring back to Board.')},
    ],
    'expected': [
        'Numbered obligation map with policy gap severity.',
        'List of audit findings at risk of repeating.',
        'Appetite-breach risks surfaced for Board attention.',
    ],
    'watch': [
        'Every obligation cites a paragraph reference in the circular.',
        'Policy-gap calls are anchored to a policy section, not inferred.',
        'Repeat-finding list reuses the exact finding IDs.',
    ],
    'honest': ('Notebook reads what you give it. If a key policy is missing from the 5 sources, '
        'gaps may look bigger than they are. Validate with Compliance before commitments.'),
    'tips': [
        'Swap source #5 to the previous regulator circular to spot regulatory drift.',
        'Use Quick Create > Pages to export the obligation map for circulation.',
        'Re-run Prompt 1 once internal policy is updated to confirm gaps are closed.',
    ],
},

# ────────────────────────────────────────────────────────────────────────────
# M&A due diligence archetype
# ────────────────────────────────────────────────────────────────────────────
'nb-ma-due-diligence': {
    'title': 'M&A Target Due Diligence',
    'archetype': 'ma_diligence',
    'complexity': 'advanced',
    'sources': [
        ('Target_Financials_3Y.xlsx','xlsx'),
        ('Target_Cap_Table.xlsx','xlsx'),
        ('Material_Contracts_Index.pdf','pdf'),
        ('Litigation_Register.xlsx','xlsx'),
        ('Management_Presentation.pdf','pdf'),
    ],
    'instructions': ('You are the deal-team analyst preparing the IC pre-read. Cite every '
        'number to file + tab/page. Highlight where management commentary contradicts the '
        'numbers. Flag any contract or litigation item that could materially shift '
        'enterprise value. Stay evidence-bound.'),
    'desc': ('Compress 3 years of financials, the cap table, key contracts, litigation, and '
        'management deck into a 1-page IC pre-read with quotable line items.'),
    'prompts': [
        {'label':'Prompt 1 — Financial spine','text':(
            'Build the 3-year financial spine from /Target_Financials_3Y.xlsx: revenue, gross '
            'margin, EBITDA, FCF, working capital. Show CAGR and trend. Quote any unusual '
            'one-off and cross-check against /Management_Presentation.pdf — flag any '
            'inconsistency.')},
        {'label':'Prompt 2 — Risk register','text':(
            'Combine /Material_Contracts_Index.pdf and /Litigation_Register.xlsx into one '
            'risk register. For each: item, counterparty, value impact, expiry/trigger date, '
            'mitigation option. Sort by EV impact.')},
        {'label':'Prompt 3 — IC question pack','text':(
            'Produce the 10 sharpest IC questions to ask management before signing. Each '
            'question must cite which source raises it (financial line / contract / case). '
            'Group by Commercial, Legal, Financial, People.')},
    ],
    'expected': [
        'Defensible 3-year financial summary with reconciled commentary.',
        'EV-ranked risk register from contracts + litigation.',
        '10 sharp, evidence-anchored questions for management.',
    ],
    'watch': [
        'Every financial number traces to a cell reference.',
        'Inconsistencies are NAMED (number vs management quote).',
        'IC questions cite a specific source, not generic concerns.',
    ],
    'honest': ('Diligence depth is limited by what you upload. Notebook will not catch a '
        'risk in a document you did not give it. Quality of the IC pre-read scales with the '
        'completeness of the data room extract you load.'),
    'tips': [
        'Add the LOI as a 6th source for terms alignment checks.',
        'Run prompt 2 separately for each contract category if the index is huge.',
        'Use Quick Create > Audio Overview for the IC chair to listen on the road.',
    ],
},

# ────────────────────────────────────────────────────────────────────────────
# Board pre-read synthesis archetype
# ────────────────────────────────────────────────────────────────────────────
'nb-board-prereread': {
    'title': 'Board Pre-Read Synthesis',
    'archetype': 'board_prereread',
    'complexity': 'intermediate',
    'sources': [
        ('CEO_Report.docx','docx'),
        ('CFO_Financial_Pack.xlsx','xlsx'),
        ('Risk_Heatmap.xlsx','xlsx'),
        ('Strategy_Update_Deck.pdf','pdf'),
        ('Previous_Board_Minutes.docx','docx'),
    ],
    'instructions': ('You are compressing 5 Board documents into a tight pre-read. Cite '
        'every claim. Flag where the CEO narrative diverges from the CFO numbers or the '
        'risk heatmap. Carry forward unresolved actions from the previous minutes.'),
    'desc': ('Turn a 200-page Board pack into a 1-page pre-read that surfaces the 5 things '
        'each director MUST read before the meeting.'),
    'prompts': [
        {'label':'Prompt 1 — The 5 things','text':(
            'From all 5 sources, distil the 5 items each Director must read before the '
            'meeting. For each: a 2-sentence summary, the source citation, and the Board '
            'decision required (Note / Approve / Decide).')},
        {'label':'Prompt 2 — Narrative vs numbers','text':(
            'Compare /CEO_Report.docx narrative against /CFO_Financial_Pack.xlsx and '
            '/Risk_Heatmap.xlsx. List every place the story and the numbers diverge — quote '
            'both. End with the single sharpest question to put to the CEO in the meeting.')},
        {'label':'Prompt 3 — Action carry-forward','text':(
            'From /Previous_Board_Minutes.docx, list every action that remains open. For '
            'each: owner, due date, current status from the latest sources, and the line '
            'to push in this meeting.')},
    ],
    'expected': [
        'A 5-item Board pre-read with decision tags.',
        'A narrative-vs-numbers reconciliation with a sharp question.',
        'A clean action carry-forward list with status updates.',
    ],
    'watch': [
        'The 5 items each cite a different source where possible.',
        'Divergences quote both the CEO line AND the contradicting number.',
        'Open actions reuse the exact action IDs from the minutes.',
    ],
    'honest': ('This compresses what is in the pack. If a director needs context not in '
        'the 5 sources (e.g. analyst notes, industry context), add them as additional '
        'sources or pair Notebook with Researcher.'),
    'tips': [
        'Add a 6th source = analyst report for external context.',
        'Use Quick Create > Pages to publish the pre-read to a Loop component.',
        'Re-run prompt 3 right after the meeting to refresh status.',
    ],
},

# ────────────────────────────────────────────────────────────────────────────
# Customer renewal book archetype (sales / commercial)
# ────────────────────────────────────────────────────────────────────────────
'nb-renewal-book': {
    'title': 'Customer Renewal Book',
    'archetype': 'renewal_book',
    'complexity': 'intermediate',
    'sources': [
        ('Account_Plan.docx','docx'),
        ('Usage_Telemetry_Last_12M.xlsx','xlsx'),
        ('Support_Tickets_Log.xlsx','xlsx'),
        ('Renewal_Contract_Draft.pdf','pdf'),
        ('Competitor_Win_Loss_Notes.docx','docx'),
    ],
    'instructions': ('You are preparing the renewal book for the account team. Cite every '
        'figure to the source. Flag any divergence between what the account plan claims and '
        'what the telemetry / tickets show. Stay evidence-bound — do not project numbers.'),
    'desc': ('Build a renewal book that prices the relationship honestly using telemetry, '
        'support load and competitive context — not the account plan optimism.'),
    'prompts': [
        {'label':'Prompt 1 — Health snapshot','text':(
            'Produce a 1-page health snapshot from /Usage_Telemetry_Last_12M.xlsx and '
            '/Support_Tickets_Log.xlsx: active users trend, feature adoption, ticket volume '
            'by severity, time-to-resolution. Flag any metric that contradicts '
            '/Account_Plan.docx with a quote.')},
        {'label':'Prompt 2 — Renewal levers','text':(
            'From /Renewal_Contract_Draft.pdf and the health snapshot, list the 5 commercial '
            'levers (uplift, term, modules, support tier, payment terms). For each: current '
            'baseline, proposed change, the evidence that justifies it, and the customer '
            'objection to expect.')},
        {'label':'Prompt 3 — Competitive defence','text':(
            'From /Competitor_Win_Loss_Notes.docx, list the 3 competitor plays we should '
            'expect in this renewal. For each: the play, which capability gap they will '
            'exploit, and our 2-line counter-message rooted in our telemetry.')},
    ],
    'expected': [
        'Health snapshot grounded in telemetry not narrative.',
        '5 commercial levers each backed by evidence.',
        'Competitive defence pack with concrete counter-messages.',
    ],
    'watch': [
        'Health metrics come from the spreadsheet, not the account plan.',
        'Each lever cites a number / clause / behaviour.',
        'Competitive plays cite the win/loss note that anticipates them.',
    ],
    'honest': ('Renewal pricing is a commercial conversation. Notebook surfaces the '
        'evidence — the account team still owns the discount call and the relationship '
        'dynamics.'),
    'tips': [
        'Add the previous renewal contract as a 6th source for delta tracking.',
        'Re-run prompt 1 quarterly as part of QBR prep.',
        'Use Quick Create > PowerPoint to generate the executive readout.',
    ],
},

# ────────────────────────────────────────────────────────────────────────────
# Incident post-mortem archetype
# ────────────────────────────────────────────────────────────────────────────
'nb-incident-pmortem': {
    'title': 'Incident Post-Mortem',
    'archetype': 'incident_pmortem',
    'complexity': 'intermediate',
    'sources': [
        ('Incident_Timeline.docx','docx'),
        ('Pager_Alerts_Log.xlsx','xlsx'),
        ('Customer_Comms_Sent.docx','docx'),
        ('System_Architecture_Diagram.pdf','pdf'),
        ('Past_Similar_Incidents.xlsx','xlsx'),
    ],
    'instructions': ('You are producing a blameless post-mortem. Cite every event to a '
        'timestamp + source. Focus on systems and processes, not individuals. Flag where '
        'this incident matches a past one in the register. Stay evidence-bound.'),
    'desc': ('Turn an incident response into a blameless post-mortem and action register '
        'that closes the loop instead of repeating the same failure.'),
    'prompts': [
        {'label':'Prompt 1 — Sequenced timeline','text':(
            'Reconstruct the incident as a strictly time-stamped event log combining '
            '/Incident_Timeline.docx and /Pager_Alerts_Log.xlsx. For each event: the '
            'timestamp, the trigger, the responder action, and the system state. Highlight '
            'the 3 longest gaps between detection and response.')},
        {'label':'Prompt 2 — Contributing causes','text':(
            'Identify the 5 contributing causes (technical, process, communication) using '
            '/System_Architecture_Diagram.pdf for the technical layer and '
            '/Customer_Comms_Sent.docx for the comms layer. For each: cause, evidence '
            'citation, and the safeguard absent.')},
        {'label':'Prompt 3 — Repeat-risk + actions','text':(
            'Compare against /Past_Similar_Incidents.xlsx — list any prior incident this '
            'repeats. Then produce 5 prevention actions, each with: owner role, due date, '
            'and the leading-indicator metric to watch.')},
    ],
    'expected': [
        'A defensible timeline with response-gap analysis.',
        'A contributing-causes list anchored to systems and comms.',
        'A repeat-risk audit + actionable prevention register.',
    ],
    'watch': [
        'Every event has a real timestamp from the log.',
        'Causes cite architecture or comms evidence, not opinion.',
        'Actions reuse owner roles, not named individuals.',
    ],
    'honest': ('A post-mortem is only useful if the actions ship. Notebook produces the '
        'register — the engineering org still needs to track closure.'),
    'tips': [
        'Add monitoring-config snapshots as a 6th source for tooling gaps.',
        'Use Quick Create > Audio Overview for the all-hands walkthrough.',
        'Re-run prompt 3 monthly to track action burndown.',
    ],
},

# ────────────────────────────────────────────────────────────────────────────
# Capex business case archetype (infra / energy / manufacturing)
# ────────────────────────────────────────────────────────────────────────────
'nb-capex-business-case': {
    'title': 'Capex Business Case',
    'archetype': 'capex_case',
    'complexity': 'advanced',
    'sources': [
        ('Capex_Model_Base.xlsx','xlsx'),
        ('Sensitivity_Scenarios.xlsx','xlsx'),
        ('Permit_and_EIA_Status.pdf','pdf'),
        ('Procurement_Quotes.pdf','pdf'),
        ('Strategic_Rationale_Memo.docx','docx'),
    ],
    'instructions': ('You are stress-testing a capex business case for the Investment '
        'Committee. Cite every number to file + tab. Surface where the strategic memo '
        'over-claims relative to the model. Flag any permit / quote risk that could push '
        'timeline.'),
    'desc': ('Pressure-test a capex submission before it reaches the IC — numbers, '
        'sensitivities, permits and procurement integrity.'),
    'prompts': [
        {'label':'Prompt 1 — Returns reconciled','text':(
            'From /Capex_Model_Base.xlsx extract IRR, NPV, payback, and key revenue / opex '
            'drivers. Reconcile against the claims in /Strategic_Rationale_Memo.docx — '
            'quote any over-claim with the contradicting cell reference.')},
        {'label':'Prompt 2 — Stress envelope','text':(
            'From /Sensitivity_Scenarios.xlsx identify the 3 scenarios where IRR drops '
            'below hurdle. For each: the trigger variables, the size of move required, and '
            'the early-warning indicator we should monitor.')},
        {'label':'Prompt 3 — Execution risk','text':(
            'Combine /Permit_and_EIA_Status.pdf and /Procurement_Quotes.pdf into an '
            'execution risk register. List any permit pending, quote expiring, or vendor '
            'concentration that could push timeline or cost.')},
    ],
    'expected': [
        'A reconciled returns picture that flags memo over-claims.',
        'A stress envelope with named monitoring indicators.',
        'A timeline / cost execution risk register.',
    ],
    'watch': [
        'Returns numbers all trace to specific cells.',
        'Over-claim flags quote both sides verbatim.',
        'Permit / quote risks cite expiry dates explicitly.',
    ],
    'honest': ('Notebook tests the case you uploaded. If your model is wrong upstream of '
        'the cells, Notebook will not catch that — pair it with Finance for the underlying '
        'methodology review.'),
    'tips': [
        'Add the Board capex policy as a 6th source to check against threshold rules.',
        'Re-run prompt 2 with a new sensitivity tab when assumptions update.',
        'Use Quick Create > PowerPoint for the IC chair walkthrough.',
    ],
},

# ────────────────────────────────────────────────────────────────────────────
# Marketing campaign retro archetype
# ────────────────────────────────────────────────────────────────────────────
'nb-campaign-retro': {
    'title': 'Marketing Campaign Retro',
    'archetype': 'campaign_retro',
    'complexity': 'basic',
    'sources': [
        ('Campaign_Brief.docx','docx'),
        ('Channel_Spend_Performance.xlsx','xlsx'),
        ('Creative_Asset_Library.pdf','pdf'),
        ('Survey_and_Sentiment_Pulse.xlsx','xlsx'),
        ('Sales_Pipeline_Influence.xlsx','xlsx'),
    ],
    'instructions': ('You are running the campaign retro for the next planning cycle. '
        'Cite spend, performance, sentiment and pipeline numbers to file + tab. Flag where '
        'the brief targets and the outcomes diverged. Stay evidence-bound.'),
    'desc': ('Turn a quarter of campaign data into a retro that is brutally honest about '
        'what worked and what to stop funding.'),
    'prompts': [
        {'label':'Prompt 1 — Brief vs outcome','text':(
            'Compare /Campaign_Brief.docx KPI targets against actuals in '
            '/Channel_Spend_Performance.xlsx and /Sales_Pipeline_Influence.xlsx. Produce a '
            'target-vs-actual table by KPI. Flag any miss > 10% in amber.')},
        {'label':'Prompt 2 — Spend efficiency','text':(
            'From /Channel_Spend_Performance.xlsx compute cost-per-MQL, cost-per-SQL, ROAS '
            'per channel. Rank channels and call out the 2 to defund next quarter with the '
            'numeric justification.')},
        {'label':'Prompt 3 — Brand pulse','text':(
            'From /Survey_and_Sentiment_Pulse.xlsx surface the 3 sharpest themes that '
            'shifted during the campaign. Quote real survey verbatims for each. Map to the '
            'creative asset in /Creative_Asset_Library.pdf that drove the shift.')},
    ],
    'expected': [
        'A target-vs-actual scoreboard with amber misses flagged.',
        'A defensible channel rationalisation recommendation.',
        'A brand pulse anchored to specific creatives.',
    ],
    'watch': [
        'Misses are FLAGGED, not explained away.',
        'Channel rankings cite the exact cost/return cells.',
        'Verbatims are quoted, not paraphrased.',
    ],
    'honest': ('Attribution is messy. Notebook reports what the pipeline file says — if '
        'attribution methodology is broken upstream, the channel ranking will be too. '
        'Treat it as a directional input, not the final budget call.'),
    'tips': [
        'Add the next-quarter media plan as a 6th source to draft adjustments inline.',
        'Use Quick Create > Pages to publish the retro to a Loop component.',
        'Re-run prompt 2 weekly during in-flight campaigns to catch drift early.',
    ],
},

# ────────────────────────────────────────────────────────────────────────────
# Tax / treasury close archetype
# ────────────────────────────────────────────────────────────────────────────
'nb-tax-treasury-close': {
    'title': 'Tax & Treasury Close-Pack',
    'archetype': 'tax_treasury_close',
    'complexity': 'advanced',
    'sources': [
        ('Tax_Position_Summary.xlsx','xlsx'),
        ('Transfer_Pricing_Documentation.pdf','pdf'),
        ('Treasury_Cash_Positions.xlsx','xlsx'),
        ('FX_Hedging_Register.xlsx','xlsx'),
        ('Auditor_Open_Queries.docx','docx'),
    ],
    'instructions': ('You are preparing the month-end close-pack on tax and treasury. '
        'Cite every number to file + tab. Flag any open auditor query that ties to a tax '
        'position or hedge. Stay evidence-bound — do not opine on tax positions, surface '
        'them.'),
    'desc': ('Combine tax, transfer pricing, treasury and FX into a single close-pack the '
        'CFO can sign off without chasing 5 spreadsheets.'),
    'prompts': [
        {'label':'Prompt 1 — Tax + TP position','text':(
            'Summarise /Tax_Position_Summary.xlsx and cross-check against '
            '/Transfer_Pricing_Documentation.pdf. List every entity with an open tax position, '
            'the documentation status, and any margin that breaches benchmark.')},
        {'label':'Prompt 2 — Cash + FX','text':(
            'From /Treasury_Cash_Positions.xlsx and /FX_Hedging_Register.xlsx produce a '
            'currency-bucket cash view, the hedge coverage ratio per currency, and any '
            'unhedged exposure above the policy limit.')},
        {'label':'Prompt 3 — Auditor query map','text':(
            'For each open query in /Auditor_Open_Queries.docx, identify which source file '
            'and tab/section answers it. List any query that the 5 sources cannot answer.')},
    ],
    'expected': [
        'A tax + transfer pricing scoreboard with documentation status.',
        'A treasury cash + FX hedge view with policy breach flags.',
        'An auditor query map showing which queries can be cleared today.',
    ],
    'watch': [
        'Entity-level numbers cite the entity tab in the workbook.',
        'Hedge coverage ratio uses the exact policy threshold.',
        'Queries are marked "answerable" or "evidence gap", not both.',
    ],
    'honest': ('Tax and treasury require human judgement. Notebook organises the evidence '
        'and surfaces gaps — it does not opine on accepted positions or hedge accounting '
        'treatment. Sign-off remains with the CFO and Tax.'),
    'tips': [
        'Add the loan covenant pack as a 6th source for covenant headroom views.',
        'Re-run prompt 3 each Friday to track auditor query burn-down.',
        'Use Quick Create > PowerPoint for the Audit Committee report.',
    ],
},

# ────────────────────────────────────────────────────────────────────────────
# Operations turnaround archetype (logistics / manufacturing / supply chain)
# ────────────────────────────────────────────────────────────────────────────
'nb-ops-turnaround': {
    'title': 'Operations Turnaround Pack',
    'archetype': 'ops_turnaround',
    'complexity': 'intermediate',
    'sources': [
        ('Site_Performance_Dashboard.xlsx','xlsx'),
        ('Root_Cause_Investigations.docx','docx'),
        ('Capex_and_Maintenance_Plan.xlsx','xlsx'),
        ('Supplier_Performance_Scorecard.xlsx','xlsx'),
        ('Worker_Safety_Incidents.xlsx','xlsx'),
    ],
    'instructions': ('You are building a 90-day turnaround pack for an underperforming '
        'operation. Cite every performance number to file + tab. Tie root causes to '
        'evidence. Stay evidence-bound — surface options, do not commit budget.'),
    'desc': ('Combine performance, root cause, maintenance plan, supplier and safety data '
        'into a 90-day operations turnaround pack.'),
    'prompts': [
        {'label':'Prompt 1 — Performance baseline','text':(
            'From /Site_Performance_Dashboard.xlsx establish the 4 KPIs that matter most, '
            'their trend, and the gap to target. Cross-reference '
            '/Worker_Safety_Incidents.xlsx to flag any KPI movement that came at safety '
            'cost.')},
        {'label':'Prompt 2 — Root cause + supplier link','text':(
            'For each root cause in /Root_Cause_Investigations.docx, identify whether '
            '/Supplier_Performance_Scorecard.xlsx shows a supplier behind it. List '
            'cause → supplier mapping with evidence cell references.')},
        {'label':'Prompt 3 — 90-day plan','text':(
            'From /Capex_and_Maintenance_Plan.xlsx build a 90-day calendar by week of '
            'maintenance + capex actions that target the 4 KPIs. Each line: action, owner '
            'role, week, KPI moved, and the leading indicator to monitor.')},
    ],
    'expected': [
        'A baseline + gap KPI view linked to safety implications.',
        'A root-cause map that names supplier contributors.',
        'A 90-day execution calendar tied to KPI movement.',
    ],
    'watch': [
        'Trend numbers cite specific dashboard cells.',
        'Safety / KPI trade-off flags are surfaced, not buried.',
        'Calendar items each have a leading-indicator metric.',
    ],
    'honest': ('Turnarounds need on-the-ground execution. Notebook organises the diagnosis '
        'and the plan; it does not run the meetings or hold the owners accountable. Pair '
        'with a weekly Cowork status sync.'),
    'tips': [
        'Add the union / workforce engagement notes as a 6th source for change-management.',
        'Re-run prompt 3 every fortnight to refresh the calendar.',
        'Use Quick Create > Audio Overview for the night-shift handover.',
    ],
},

# ────────────────────────────────────────────────────────────────────────────
# ESG / sustainability disclosure archetype
# ────────────────────────────────────────────────────────────────────────────
'nb-esg-disclosure': {
    'title': 'ESG Disclosure Drafting',
    'archetype': 'esg_disclosure',
    'complexity': 'intermediate',
    'sources': [
        ('Emissions_Inventory.xlsx','xlsx'),
        ('Sustainability_Strategy.docx','docx'),
        ('Audit_Assurance_Findings.docx','docx'),
        ('Disclosure_Framework_Mapping.xlsx','xlsx'),
        ('Prior_Year_Disclosure.pdf','pdf'),
    ],
    'instructions': ('You are drafting the ESG disclosure narrative for sign-off. Cite '
        'every emissions or target number to the source. Flag any gap between the strategy '
        'commitment and the inventory. Stay evidence-bound — do not invent reductions.'),
    'desc': ('Anchor the ESG disclosure draft in actual inventory data and prior assurance '
        'findings — not aspirational language.'),
    'prompts': [
        {'label':'Prompt 1 — Inventory vs target','text':(
            'From /Emissions_Inventory.xlsx and /Sustainability_Strategy.docx produce a '
            'target-vs-actual emissions table by scope (1/2/3). Flag the largest variance '
            'and quote the strategy commitment.')},
        {'label':'Prompt 2 — Framework mapping','text':(
            'From /Disclosure_Framework_Mapping.xlsx list every required disclosure '
            'datapoint. For each: status (covered / partial / gap), source file that '
            'covers it, and the writing owner.')},
        {'label':'Prompt 3 — Year-on-year delta','text':(
            'Compare against /Prior_Year_Disclosure.pdf. List every material change in '
            'narrative, metric, or methodology. Quote prior wording where it has shifted '
            'and flag for legal review.')},
    ],
    'expected': [
        'A scope-by-scope target gap table.',
        'A framework coverage matrix with owners.',
        'A YoY change log ready for legal/assurance review.',
    ],
    'watch': [
        'Variances are NUMBERED and SIGNED (over/under target).',
        'Coverage statuses are pinned to specific framework rows.',
        'Wording deltas are quoted (old vs new).',
    ],
    'honest': ('ESG disclosures are scrutinised. Notebook anchors the drafting in your '
        'inventory but does not replace external assurance or legal review. Push every '
        'material change through the assurance partner.'),
    'tips': [
        'Add the assurance partner instruction letter as a 6th source.',
        'Re-run prompt 2 weekly during disclosure prep to track gap closure.',
        'Use Quick Create > Pages to publish a draft for collaborators.',
    ],
},

# ────────────────────────────────────────────────────────────────────────────
# Employee onboarding / handbook archetype (HR)
# ────────────────────────────────────────────────────────────────────────────
'nb-hr-onboarding-pack': {
    'title': 'HR Onboarding Knowledge Pack',
    'archetype': 'hr_onboarding',
    'complexity': 'basic',
    'sources': [
        ('Employee_Handbook.pdf','pdf'),
        ('Benefits_Guide.pdf','pdf'),
        ('Role_Specific_Onboarding_Plan.docx','docx'),
        ('Compliance_Training_Catalog.xlsx','xlsx'),
        ('Buddy_Programme_Notes.docx','docx'),
    ],
    'instructions': ('You are the new joiner. Cite every answer to file + section so the '
        'joiner can verify in the original document. Flag any policy that has prerequisites '
        '(form, training, signature). Stay evidence-bound — do not paraphrase policy.'),
    'desc': ('A self-service knowledge pack a new joiner can use in week one to answer '
        '90% of their questions without booking time with HR.'),
    'prompts': [
        {'label':'Prompt 1 — First-week checklist','text':(
            'From /Role_Specific_Onboarding_Plan.docx and /Compliance_Training_Catalog.xlsx '
            'build a numbered first-week checklist. For each item: action, who owns it, '
            'deadline, and where to find it (system / form / person).')},
        {'label':'Prompt 2 — Benefits Q&A','text':(
            'From /Benefits_Guide.pdf answer the 10 most common benefit questions (leave, '
            'medical, dental, retirement, parental, allowances). Quote the exact policy '
            'language and the page reference.')},
        {'label':'Prompt 3 — Buddy match brief','text':(
            'From /Buddy_Programme_Notes.docx draft the conversation guide the joiner can '
            'use in their first buddy session: 5 questions to ask, 3 things to share about '
            'themselves, and what to expect from the programme.')},
    ],
    'expected': [
        'A clean first-week checklist with owners and deadlines.',
        'A benefits Q&A grounded in actual policy wording.',
        'A buddy conversation guide that makes the first session productive.',
    ],
    'watch': [
        'Checklist items reference the policy or system that hosts the action.',
        'Benefit answers are QUOTED not paraphrased.',
        'Buddy guide uses programme language consistently.',
    ],
    'honest': ('Policy can change. Notebook reflects the documents you load — if HR has '
        'updated a policy and the new version is not in the notebook, the answer will be '
        'stale. Encourage joiners to verify with HR for anything time-sensitive.'),
    'tips': [
        'Add the org chart as a 6th source for "who does what" questions.',
        'Re-publish the notebook each cohort with refreshed sources.',
        'Use Quick Create > Audio Overview for a walking-commute first-week briefing.',
    ],
},

}

# ════════════════════════════════════════════════════════════════════════════
# Universal cards available to any entry as fallback.
# ════════════════════════════════════════════════════════════════════════════
UNIVERSAL_USE_CASES = ['nb-board-prereread', 'nb-incident-pmortem']

# ════════════════════════════════════════════════════════════════════════════
# Per-entry mapping. 2-3 cards per entry — entry-specific archetypes
# preferred, universals as the second slot.
# ════════════════════════════════════════════════════════════════════════════
ENTRY_NB_USE_CASES = {
    # General / cross-cutting
    'general': ['nb-board-prereread', 'nb-campaign-retro', 'nb-incident-pmortem'],

    # Banking / FSI
    'commercial-banking':   ['nb-regulator-crossref', 'nb-renewal-book', 'nb-board-prereread'],
    'islamic-banking':      ['nb-regulator-crossref', 'nb-board-prereread'],
    'investment-banking':   ['nb-ma-due-diligence', 'nb-board-prereread'],
    'private-banking':      ['nb-renewal-book', 'nb-regulator-crossref'],
    'insurance':            ['nb-regulator-crossref', 'nb-renewal-book'],
    'takaful':              ['nb-regulator-crossref', 'nb-board-prereread'],
    'asset-management':     ['nb-ma-due-diligence', 'nb-regulator-crossref'],
    'fintech':              ['nb-regulator-crossref', 'nb-renewal-book'],

    # Healthcare
    'hospital':             ['nb-clinical-case', 'nb-board-prereread'],
    'pharma':               ['nb-clinical-case', 'nb-regulator-crossref'],
    'medical-devices':      ['nb-regulator-crossref', 'nb-rfp-procurement'],
    'health-insurance':     ['nb-renewal-book', 'nb-regulator-crossref'],

    # Energy / utilities
    'oil-gas':              ['nb-capex-business-case', 'nb-ops-turnaround'],
    'utilities':            ['nb-capex-business-case', 'nb-ops-turnaround'],
    'renewables':           ['nb-capex-business-case', 'nb-esg-disclosure'],
    'mining':               ['nb-ops-turnaround', 'nb-esg-disclosure'],
    'coal':                 ['nb-ops-turnaround', 'nb-esg-disclosure'],
    'rare-earth':           ['nb-capex-business-case', 'nb-esg-disclosure'],

    # Manufacturing / industrial
    'manufacturing':        ['nb-ops-turnaround', 'nb-rfp-procurement'],
    'automotive':           ['nb-ops-turnaround', 'nb-rfp-procurement'],
    'electronics':          ['nb-ops-turnaround', 'nb-rfp-procurement'],
    'chemicals':            ['nb-ops-turnaround', 'nb-esg-disclosure'],
    'fmcg':                 ['nb-campaign-retro', 'nb-ops-turnaround'],
    'food-bev':             ['nb-campaign-retro', 'nb-ops-turnaround'],

    # Agriculture / plantation
    'plantation':           ['nb-esg-disclosure', 'nb-ops-turnaround', 'nb-board-prereread'],
    'agriculture':          ['nb-ops-turnaround', 'nb-esg-disclosure'],

    # Services / BPO / Telco
    'bpo-services':         ['nb-renewal-book', 'nb-rfp-procurement'],
    'telco':                ['nb-regulator-crossref', 'nb-capex-business-case'],
    'media':                ['nb-campaign-retro', 'nb-renewal-book'],

    # Real estate / hospitality / property
    'reit':                 ['nb-board-prereread', 'nb-renewal-book'],
    'hotel':                ['nb-renewal-book', 'nb-campaign-retro'],
    'property-development': ['nb-capex-business-case', 'nb-board-prereread'],

    # Logistics / aviation / maritime
    'logistics':            ['nb-ops-turnaround', 'nb-rfp-procurement'],
    'aviation-airline':     ['nb-ops-turnaround', 'nb-renewal-book'],
    'aviation-airport':     ['nb-capex-business-case', 'nb-ops-turnaround'],
    'maritime':             ['nb-ops-turnaround', 'nb-regulator-crossref'],

    # Government / GLC / regulators
    'government':           ['nb-board-prereread', 'nb-rfp-procurement'],
    'regulator':            ['nb-regulator-crossref', 'nb-board-prereread'],
    'glc':                  ['nb-board-prereread', 'nb-regulator-crossref'],

    # Conglomerate
    'conglomerate':         ['nb-ma-due-diligence', 'nb-board-prereread'],

    # Retail / e-commerce
    'retail':               ['nb-campaign-retro', 'nb-renewal-book'],
    'ecommerce':            ['nb-campaign-retro', 'nb-ops-turnaround'],

    # Education
    'education':            ['nb-board-prereread', 'nb-hr-onboarding-pack'],

    # Departments — 2 cards each
    'dept-finance':         ['nb-tax-treasury-close', 'nb-board-prereread'],
    'dept-hr':              ['nb-hr-onboarding-pack', 'nb-board-prereread'],
    'dept-legal':           ['nb-regulator-crossref', 'nb-ma-due-diligence'],
    'dept-risk':            ['nb-regulator-crossref', 'nb-incident-pmortem'],
    'dept-strategy':        ['nb-ma-due-diligence', 'nb-board-prereread'],
    'dept-marketing':       ['nb-campaign-retro', 'nb-renewal-book'],
    'dept-esg':             ['nb-esg-disclosure', 'nb-board-prereread'],
    'dept-operations':      ['nb-ops-turnaround', 'nb-rfp-procurement'],
    'dept-corpsec':         ['nb-board-prereread', 'nb-regulator-crossref'],
    'dept-investor-rel':    ['nb-board-prereread', 'nb-renewal-book'],
    'dept-procurement':     ['nb-rfp-procurement', 'nb-renewal-book'],
    'dept-it':              ['nb-incident-pmortem', 'nb-rfp-procurement'],
}


def get_nb_library_for_entry(entry_id):
    """Return list of card dicts for a given entry id; falls back to
    universal cards when the entry is unmapped or maps to a missing card."""
    ids = ENTRY_NB_USE_CASES.get(entry_id, UNIVERSAL_USE_CASES)
    out = []
    for cid in ids:
        c = USE_CASES.get(cid)
        if not c:
            continue
        item = dict(c)
        item['id'] = cid
        out.append(item)
    if not out:
        for cid in UNIVERSAL_USE_CASES:
            c = USE_CASES.get(cid)
            if c:
                item = dict(c)
                item['id'] = cid
                out.append(item)
    return out


if __name__ == '__main__':
    print(f"Notebook Library: {len(USE_CASES)} unique cards")
    missing = 0
    for eid in ENTRY_NB_USE_CASES:
        cards = get_nb_library_for_entry(eid)
        if not cards:
            print(f"  ✗ {eid}: NO CARDS")
            missing += 1
        else:
            print(f"  ✓ {eid}: {len(cards)} cards -> {[c['id'] for c in cards]}")
    print(f"\n{len(ENTRY_NB_USE_CASES)} entries mapped, {missing} missing.")
