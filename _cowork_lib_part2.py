# -*- coding: utf-8 -*-
"""Banking + Insurance + Fintech use cases for the Cowork Library."""

CARDS = {}

CARDS['uc-bank-credit-council'] = {
    'title': 'Credit Council — Investment Memo with 5-Role Analysis',
    'dept_tag': 'Credit & Risk',
    'industry_tag': 'Banking',
    'complexity': 'advanced',
    'apps': ['Word', 'Excel', 'PowerPoint', 'Outlook', 'Teams'],
    'desc': 'A multi-role council (Fundamental Analyst, Macro Strategist, Risk Officer, Stress Tester, Compliance) builds an audit-ready credit memo for a corporate loan — with traceable dissent and citations.',
    'skills': [
        'Multi-role council prompt — 5 distinct analytical voices in one run',
        'Cross-source synthesis: financials + policy + macro outlook + peer credits',
        'Recommendation table with explicit dissent + assumptions + traceability',
    ],
    'instructions': [
        'Open Microsoft 365 Copilot → Agents → Cowork',
        'Click 📎 Knowledge → attach the 4 sample files',
        'Paste Prompt 1 — Cowork runs the 5-role council. Wait for the long interim report.',
        'Paste Prompt 2 — Cowork assembles the deliverables in parallel',
    ],
    'sample_files': [
        ('BNK_Borrower_Financial_Statements_3yr.xlsx', 'xlsx'),
        ('BNK_BNM_Credit_Policy_Manual.docx', 'docx'),
        ('BNK_Industry_Outlook_Report.pdf', 'pdf'),
        ('BNK_Peer_Credit_Benchmarks.xlsx', 'xlsx'),
    ],
    'prompts': [
        {
            'label': 'Run the 5-role council',
            'text': (
                "You are acting as a council of AI agents to help a Bank assess investment merits in lending to [BORROWER]. Your goal is to analysis and recommend if [BORROWER] is worth investing in.\n\n"
                "For each of the following roles, use Researcher Agent to assume the respective role, capturing dissent, and producing audit-ready decision packs in a LONG interim report.\n\n"
                "Finally analyse all the relevant data to make recommendations, evidence, assumptions, and dissenting views, with traceability. Capture all internal deliberations.\n\n"
                "Roles:\n\n"
                "1. Fundamental Analyst. You perform deep fundamental analysis (financials, business model, unit economics, moat, management quality, comparables). Your internal outputs are underwriting notes, valuation ranges, sensitivity table, quality-of-earnings.\n\n"
                "2. Macro Strategist. You test macro regime fit: growth/inflation, policy path, rates/FX, liquidity conditions, cross-asset correlation. Your internal outputs are macro scenario maps, regime risks, hedging implications, correlation surprises.\n\n"
                "3. Risk Officer. You provide independent risk view across market risk (VaR/ES), credit risk, liquidity risk, concentration, tail risk. Your internal outputs are risk register, key limits breached, proposed risk mitigations, risk-adjusted return commentary.\n\n"
                "4. Stress tester. You run structured scenarios (base/bull/bear + bespoke shocks) and identifies non-linear losses and second-order effects. Your internal outputs are stress results narrative, kill-switch thresholds, scenario tree, early warning indicators.\n\n"
                "5. Compliance & Policy Agent. Your job is to checks investment permissibility: mandate constraints, restricted lists, suitability, product governance, conduct and disclosure obligations. Your internal outputs are Permitted / Not permitted / Permitted with conditions, required disclosures, required approvals."
            )
        },
        {
            'label': 'Assemble the underwriting pack',
            'text': (
                "Using the 5-role council output, in parallel produce all 5 deliverables:\n"
                "1) Underwriting memo in Word — Cover (1 page) + sections A-I:\n"
                "   A. Executive Summary (Credit View — max 1 page)\n"
                "   B. Financial Performance Analysis\n"
                "   C. Balance Sheet & Liquidity Assessment\n"
                "   D. Cash Flow Adequacy Review\n"
                "   E. Leverage & Coverage Metrics Table (multi-year)\n"
                "   F. Accounting & Disclosure Risk Commentary\n"
                "   G. Debt Servicing Capacity Assessment\n"
                "   H. Key Credit Risks & Red Flags\n"
                "   I. Required Follow-Up Items for Credit Approval\n"
                "2) Recommendation table in Excel — Approve / Approve with conditions / Decline + rationale + 5 covenants proposed.\n"
                "3) 8-slide deck in PowerPoint — for the Credit Committee meeting.\n"
                "4) Draft email in Outlook to the Chief Credit Officer + RM + Compliance — with the pack attached.\n"
                "5) Draft a Teams message to the Credit Risk channel — 3 lines summary + the recommendation.\n"
                "Cite statement sections or note numbers when highlighting findings.\n"
                "Do not fabricate financial metrics if not derivable from provided documents.\n"
                "Maintain professional tone suitable for internal underwriting memo."
            )
        }
    ],
    'expected': [
        'Underwriting memo (Word, 9 sections)',
        'Recommendation + covenants table (Excel)',
        '8-slide credit committee deck',
        'Email to CCO + RM + Compliance',
        'Teams summary to Credit Risk channel',
    ],
    'watch': [
        '5 distinct voices visible in the interim report — not a single bland synthesis',
        'Dissenting views captured separately — no false consensus',
        'Every claim cites the statement section or note number — auditable',
        'Compliance verdict explicit: Permitted / Not / Permitted-with-conditions',
    ],
    'honest': 'Cowork drafts. Human credit officer still owns the final decision and the BNM policy interpretation. The macro scenarios are starter-grade — your Market Risk team must validate before binding. Do not bypass the credit committee.',
    'tips': [
        'Swap BNM for OJK / MAS / BOT to localise for ID / SG / TH variants',
        'Add a 6th role (ESG Analyst) for sustainability-linked loans',
        'Re-run with a "Decline" bias prompt to stress-test the upside-only view',
    ],
}

CARDS['uc-bank-statement-extract'] = {
    'title': 'Bank Statements Extraction → Reconciliation-Ready Workbook',
    'dept_tag': 'Operations',
    'industry_tag': 'Banking',
    'complexity': 'intermediate',
    'apps': ['Excel'],
    'desc': 'Mixed-format bank statements (PDF, image, scanned) become a clean Excel workbook split by month, sorted chronologically, with multi-line transactions captured intact.',
    'skills': [
        'Multi-format ingestion (PDF text + scanned image + mobile photo) into one schema',
        'OCR-aware extraction with low-confidence row flagging',
        'Auto-split-by-month + within-sheet chronological sort',
    ],
    'instructions': [
        'Open Cowork',
        'Attach the 3 sample statements (or your own real ones)',
        'Paste the prompt — Cowork extracts, standardises, splits, sorts',
        'Re-open the resulting workbook and spot-check the flagged low-confidence rows',
    ],
    'sample_files': [
        ('DBS_Sample_E-Stmt.png', 'png'),
        ('CIMB_Sample_E-Stmt.pdf', 'pdf'),
        ('UOB_Sample_E-Stmt.pdf', 'pdf'),
    ],
    'prompts': [{
        'label': 'Extract → standardise → split by month',
        'text': (
            "Extract the contents from the bank statements into an Excel file with the following columns:\n"
            "Page No, Bank, Transaction Date, Description, Debit, Credit, Running Balance, Currency.\n\n"
            "Standardize on yyyy-MMM-dd as the date format.\n\n"
            "Capture multi-line transaction details.\n\n"
            "Ignore all text that are not part of a transaction.\n\n"
            "Don't perform any translation.\n\n"
            "Split the transactions by month into different worksheets and for each worksheet, sort the transactions so that it is chronologically ascending."
        )
    }],
    'expected': [
        'One workbook with one sheet per month, sorted ascending',
        'Multi-line transaction descriptions preserved',
        'Low-confidence OCR rows flagged for review',
    ],
    'watch': [
        'Three different formats — PDF, image, scanned — all land in the same standardised schema',
        'Multi-line descriptions stay intact; bank-side header noise (logos, marketing, addresses) is filtered out',
        'Date normalisation to yyyy-MMM-dd makes downstream reconciliation trivial',
        'One worksheet per month, sorted ascending — the workbook is reconciliation-ready, not just an extract',
    ],
    'honest': 'OCR quality on scanned or low-resolution images can produce edge-case errors on amounts and dates — Cowork flags any low-confidence rows rather than silently committing them. Bank-specific layouts evolve; new statement templates may need a sample run before production use.',
    'tips': [
        'Add a 4th column "Category" + a tag list to auto-classify spend',
        'For corporate KYC, chain into the UBO use case (uc-bank-ubo-kyc) — same source statements feed the diagram',
        'Run a parity report against the printed running balance to catch any missed transaction',
    ],
}

CARDS['uc-bank-ubo-kyc'] = {
    'title': 'Ultimate Beneficial Ownership Diagram for KYC',
    'dept_tag': 'Compliance',
    'industry_tag': 'Banking',
    'complexity': 'advanced',
    'apps': ['Word'],
    'desc': 'Corporate shareholder registers recursively flatten to a UBO diagram + PDF — every individual shareholder named, with each chain traceable through nominees and holdcos.',
    'skills': [
        'Recursive shareholder graph walk to identify the ultimate natural-person owners',
        'Chain tracing through nominee, holding, and SPV layers',
        'PDF artefact generation for KYC file submission',
    ],
    'instructions': [
        'Open Cowork',
        'Attach the corporate registry extract + annual return',
        'Paste the prompt — Cowork builds the UBO diagram and exports as PDF',
    ],
    'sample_files': [
        ('KYC_Corporate_Registry_Extract.pdf', 'pdf'),
        ('KYC_Annual_Return_AR.pdf', 'pdf'),
    ],
    'prompts': [{
        'label': 'Recursive UBO discovery',
        'text': (
            "Create a Ultimate Beneficiary Ownership diagram for [COMPANY-NAME].\n"
            "Recursively identify the UBO of each identified shareholder until the individual shareholders.\n"
            "Convert this into a pdf for KYC purpose."
        )
    }],
    'expected': [
        'UBO diagram with every natural-person owner identified',
        'Chain trace through each holding layer',
        'PDF ready to drop into the KYC file',
    ],
    'watch': [
        'Every chain traced down to natural persons — no stopping at a holdco',
        'Nominee structures called out separately',
        'PDF formatted for direct upload to the KYC system',
    ],
    'honest': 'Cowork works from the documents you supply. If the registry only goes one layer deep, the UBO output reflects that limitation — chase the underlying registry from each holdco jurisdiction before signing off. Sanctions screening must still be run independently.',
    'tips': [
        'Run alongside the Bank Statements Extraction use case to build the full KYC + transaction file in one session',
        'For ID variant, ingest AHU registry extract; for MY use SSM',
        'Add a "PEP flag" task that highlights any named individual against a politically-exposed-persons list',
    ],
}

CARDS['uc-bank-bnm-returns'] = {
    'title': 'BNM Quarterly Returns Pack',
    'dept_tag': 'Regulatory Reporting',
    'industry_tag': 'Banking',
    'complexity': 'advanced',
    'apps': ['Excel', 'Word', 'Outlook', 'Teams'],
    'desc': 'Loan book, deposit book, complaints register, and capital position assemble into the four BNM quarterly returns plus the explanatory letter to the BNM JPAB officer.',
    'skills': [
        'Multi-source roll-up into regulator-template schemas',
        'Variance commentary auto-generated against prior quarter + against peer benchmarks',
        'Formal regulator-grade letter drafting',
    ],
    'instructions': [
        'Open Cowork',
        'Attach the 4 source books',
        'Paste the prompt — Cowork generates the 4 returns + the cover letter in parallel',
    ],
    'sample_files': [
        ('BNM_Loan_Book_Quarter_End.xlsx', 'xlsx'),
        ('BNM_Deposit_Book_Quarter_End.xlsx', 'xlsx'),
        ('BNM_Complaints_Register.xlsx', 'xlsx'),
        ('BNM_Capital_Position_QnQ.xlsx', 'xlsx'),
    ],
    'prompts': [{
        'label': 'Quarterly returns pack',
        'text': (
            "Using the 4 source books, build the Q[N] BNM submission. In parallel:\n"
            "1) Populate the BNM 1/M return (loan classification, NPL, impairments) — match the template tab-for-tab.\n"
            "2) Populate the BNM Cap1 return (capital adequacy, RWA, Tier 1/Tier 2).\n"
            "3) Populate the Consumer Complaints return — by product, by resolution status, by aging bucket.\n"
            "4) Populate the Liquidity Coverage Ratio + Net Stable Funding Ratio returns.\n"
            "5) Draft the cover letter to the JPAB officer — formal Bahasa Malaysia option + English version, explain any Q-on-Q variance > 10%.\n"
            "Cite the source workbook + cell range for every figure. Flag any inconsistency between books."
        )
    }],
    'expected': [
        'BNM 1/M return populated',
        'BNM Cap1 return populated',
        'Complaints return populated',
        'LCR + NSFR returns populated',
        'Cover letter to JPAB officer (EN + BM)',
    ],
    'watch': [
        'Tab-for-tab match to the BNM template — no schema drift',
        'Q-on-Q variance > 10% triggers auto-narrative — never silent',
        'Cover letter has both BM and EN ready for the bilingual submission',
    ],
    'honest': 'Cowork fills the templates. The Head of Regulatory Reporting still signs off. BNM template changes mid-year — check the latest circular before final submission. Reconciliation back to GL is the human reviewer\'s job.',
    'tips': [
        'For Indonesia, swap to OJK SLIK + COREP equivalents',
        'For Singapore, swap to MAS NSCC + LCR returns',
        'Add a 6th task — generate the Audit Committee briefing slide that explains the variances to non-technical directors',
    ],
}

CARDS['uc-islamic-shariah-audit'] = {
    'title': 'Shariah Audit Findings — Recovery Programme',
    'dept_tag': 'Shariah Compliance',
    'industry_tag': 'Islamic Banking',
    'complexity': 'advanced',
    'apps': ['Word', 'Excel', 'Outlook', 'Teams'],
    'desc': 'Shariah Committee findings, product-level non-compliance log, and the Shariah governance framework drive a 30/60/90 recovery plan, board memo, and committee briefing.',
    'skills': [
        'Shariah-rules ingestion (Murabaha, Ijarah, Mudarabah, Wakalah) + non-compliance mapping',
        'Recovery plan with explicit charity-purification calculation for any tainted income',
        'Multi-stakeholder comms — Shariah Committee, Board Risk, and the BNM Shariah Department',
    ],
    'instructions': [
        'Open Cowork',
        'Attach the 4 Shariah artefacts',
        'Paste the prompt — Cowork builds the recovery and the comms in parallel',
    ],
    'sample_files': [
        ('SHC_Audit_Findings_FY.docx', 'docx'),
        ('SHC_Non_Compliance_Log.xlsx', 'xlsx'),
        ('SHC_Governance_Framework.docx', 'docx'),
        ('SHC_Charity_Purification_Calc.xlsx', 'xlsx'),
    ],
    'prompts': [{
        'label': 'Shariah recovery pack',
        'text': (
            "Using the 4 attached Shariah artefacts, prepare the recovery programme for the [PRODUCT] non-compliance findings. In parallel:\n"
            "1) Draft a 5-page Recovery Programme in Word — 30/60/90 day actions, owners, KPIs, escalation triggers.\n"
            "2) Build a Findings Tracker in Excel — Finding / Severity / Sharia rule breached / Root cause / Remediation / Owner / Due date / Status.\n"
            "3) Calculate charity-purification amount for any tainted income — itemised by product, with the Shariah ruling cited.\n"
            "4) Draft the Shariah Committee briefing memo — formal tone, Quranic and Hadith citations where the framework references them.\n"
            "5) Draft an email + Teams message to the Head of Shariah Compliance + Board Risk Chair + BNM Shariah Department contact.\n"
            "Cite the specific Shariah Standard (Murabaha-1, Ijarah-3 etc.) for every recommendation."
        )
    }],
    'expected': [
        '30/60/90 Recovery Programme (Word)',
        'Findings tracker (Excel)',
        'Charity-purification calculation',
        'Shariah Committee briefing memo',
        'Stakeholder email + Teams message',
    ],
    'watch': [
        'Every action ties to a named Shariah Standard — auditable',
        'Charity-purification calculation explicit per product — no rolled-up averages',
        'Tone of the Shariah Committee memo distinct from the Board Risk memo',
    ],
    'honest': 'Cowork structures the response. The Shariah Committee makes the final ruling. Charity-purification amounts must be verified by the Shariah Auditor before disbursement. Some rulings are jurisdiction-specific — Malaysia BNM differs from Indonesia DSN-MUI.',
    'tips': [
        'For Indonesia Islamic banking, swap to DSN-MUI fatwa references',
        'Add a 6th task — public disclosure draft (annual report Shariah review section)',
        'Re-run with persona "Shariah Committee Chair" voice for the committee paper',
    ],
}

CARDS['uc-ib-pitchbook'] = {
    'title': 'M&A Pitchbook Sprint',
    'dept_tag': 'Investment Banking',
    'industry_tag': 'Investment Banking',
    'complexity': 'advanced',
    'apps': ['PowerPoint', 'Excel', 'Word', 'Outlook'],
    'desc': 'Target financials, comparable transactions, sector outlook, and management bios become a 40-slide buy-side pitchbook, supporting valuation workbook, and personalised CEO outreach emails.',
    'skills': [
        'Comparable-transactions analysis with multiple valuation methods (DCF, comps, precedent)',
        'Strategic rationale synthesis from sector trends + acquirer capability gaps',
        'Personalised CEO outreach with non-template tone calibration',
    ],
    'instructions': [
        'Open Cowork',
        'Attach the 4 deal artefacts',
        'Paste the prompt — Cowork builds the pitchbook + workbook + outreach',
    ],
    'sample_files': [
        ('IB_Target_3yr_Financials.xlsx', 'xlsx'),
        ('IB_Comparable_Transactions.xlsx', 'xlsx'),
        ('IB_Sector_Outlook_Report.pdf', 'pdf'),
        ('IB_Management_Bios.docx', 'docx'),
    ],
    'prompts': [{
        'label': 'Pitchbook sprint',
        'text': (
            "Using the 4 attached files, build a buy-side pitchbook for [ACQUIRER] to consider acquiring [TARGET]. In parallel:\n"
            "1) Build a 40-slide deck in PowerPoint — Cover / Executive Summary / Strategic Rationale (5) / Target Profile (8) / Financial Analysis (8) / Valuation (DCF + Comps + Precedent — 10) / Synergies (3) / Integration Roadmap (3) / Risks (2) / Process & Timeline (1).\n"
            "2) Build a valuation workbook in Excel — DCF (10-year, WACC sensitivity 6-12%), Comparable Companies (10 peers), Precedent Transactions (15 deals), Football Field summary.\n"
            "3) Draft a 1-page Executive Summary for the [ACQUIRER] CEO in Word.\n"
            "4) Draft a personalised outreach email to the [TARGET] CEO — non-template tone, references the management bios.\n"
            "5) Draft an internal Teams message to the deal team — kickoff agenda for the buy-side mandate.\n"
            "Avoid template language. Every valuation number cites its source sheet + cell."
        )
    }],
    'expected': [
        '40-slide pitchbook',
        'Valuation workbook with DCF + Comps + Precedent',
        '1-page CEO Exec Summary',
        'Personalised target CEO outreach',
        'Deal team kickoff Teams message',
    ],
    'watch': [
        'Three valuation methods reconcile via a football field — no single magic number',
        'CEO outreach reads as written by a Director, not a template',
        'Strategic rationale tied to the acquirer\'s actual capability gaps',
    ],
    'honest': 'Cowork structures the pitch. The MD still finalises the price range and the strategic narrative. Comparable transactions must be verified against Mergermarket / S&P Capital IQ — Cowork has no live deal database. Confidentiality marking goes on every page by a human.',
    'tips': [
        'Re-run as sell-side mandate by reversing the rationale direction',
        'Add a 6th task — pre-mortem the deal: 5 reasons it falls apart',
        'For cross-border, add an FX hedge sheet to the workbook',
    ],
}

CARDS['uc-mortgage-loss-mit'] = {
    'title': 'Mortgage Loss Mitigation Triage',
    'dept_tag': 'Collections & Recovery',
    'industry_tag': 'Mortgage Finance',
    'complexity': 'intermediate',
    'apps': ['Excel', 'Outlook', 'Word', 'Teams'],
    'desc': 'A book of 30-90 day past-due mortgage loans gets segmented by hardship type, with restructure options modelled per loan and personalised borrower outreach drafted at scale.',
    'skills': [
        'Hardship-type segmentation (job loss, medical, divorce, business slowdown)',
        'Per-loan affordability re-test with multiple restructure options modelled',
        'Personalised borrower outreach at scale — different tone per segment',
    ],
    'instructions': [
        'Open Cowork',
        'Attach the loan book + collections notes + restructure rate card',
        'Paste the prompt — Cowork segments, models, drafts in parallel',
    ],
    'sample_files': [
        ('MTG_Past_Due_30_90.xlsx', 'xlsx'),
        ('MTG_Collections_Notes.xlsx', 'xlsx'),
        ('MTG_Restructure_Rate_Card.xlsx', 'xlsx'),
        ('MTG_Borrower_Contact_Master.xlsx', 'xlsx'),
    ],
    'prompts': [{
        'label': 'Triage + restructure + outreach',
        'text': (
            "Using the 4 attached files, work the [N] past-due mortgage loans. In parallel:\n"
            "1) Segment the book in Excel — Hardship type (job loss / medical / divorce / business slowdown / other) × LTV bucket × Days past due.\n"
            "2) For each loan, model 3 restructure options in Excel — Term extension / Step rate / Interest-only period. Show monthly payment under each + NPV impact to the bank.\n"
            "3) Draft personalised SMS + Outlook email per segment — empathetic for medical/divorce, firm for opportunistic-default profiles.\n"
            "4) Draft a Teams message to the Collections team — daily target dashboard + escalation rules.\n"
            "5) Build a Manager briefing in Word — top 20 by NPV-at-risk + recommended treatment for each.\n"
            "Cite the loan ID for every recommendation."
        )
    }],
    'expected': [
        'Segmented book (Excel)',
        'Per-loan restructure options + NPV impact',
        'Personalised outreach drafts (SMS + email)',
        'Team daily dashboard (Teams)',
        'Top-20 manager briefing (Word)',
    ],
    'watch': [
        'Hardship segmentation drives differentiated tone — not one bland letter',
        'NPV impact transparent — relationship managers see the cost of each option',
        'Top-20 by NPV-at-risk gets manager attention first',
    ],
    'honest': 'Cowork drafts. Collections managers approve every restructure individually — automated approval is not permitted under BNM Responsible Financing. Genuine hardship cases must speak to a human counsellor before any commitment.',
    'tips': [
        'Add a 6th task — generate AKPK referral letters for the irrecoverable cases',
        'Re-run for credit cards / personal loans by swapping the product master',
        'For ID variant, add BPR-rural-bank coordination flag',
    ],
}

CARDS['uc-genins-cat-claim'] = {
    'title': 'Catastrophic Event Claims Surge',
    'dept_tag': 'Claims Operations',
    'industry_tag': 'General Insurance',
    'complexity': 'advanced',
    'apps': ['Excel', 'Word', 'Outlook', 'Teams'],
    'desc': 'After a flood / earthquake / typhoon, a surge of claims gets triaged by severity, fast-tracked for vulnerable customers, and reinsurance recoveries pre-modelled.',
    'skills': [
        'Geospatial claims clustering using policyholder postcodes vs hazard map',
        'Fast-track triage for vulnerable customers (elderly, low cover, sole earner)',
        'Reinsurance treaty matching + recovery estimate',
    ],
    'instructions': [
        'Open Cowork',
        'Attach the open claims + policyholder master + hazard map + reinsurance treaty schedule',
        'Paste the prompt — Cowork triages, escalates, models in parallel',
    ],
    'sample_files': [
        ('GENINS_Open_Claims_T0_to_T7.xlsx', 'xlsx'),
        ('GENINS_Policyholder_Master.xlsx', 'xlsx'),
        ('GENINS_Hazard_Map_Affected_Postcodes.xlsx', 'xlsx'),
        ('GENINS_Reinsurance_Treaty_Schedule.xlsx', 'xlsx'),
    ],
    'prompts': [{
        'label': 'Triage the surge',
        'text': (
            "Using the 4 attached files for the [EVENT-NAME] catastrophic event, in parallel:\n"
            "1) Cluster the [N] open claims by affected postcode and severity in Excel — High / Medium / Low.\n"
            "2) Fast-track the vulnerable-customer queue in a separate Excel sheet — elderly (>65), low cover (<MYR 50k), sole-earner households.\n"
            "3) Match each claim against the reinsurance treaty schedule — estimate recovery per claim and total event recovery.\n"
            "4) Draft an empathetic email + SMS template per severity band in Outlook — vulnerable cohort gets the fast-track number.\n"
            "5) Draft a Daily Catastrophe Bulletin in Word for the COO — claims received / approved / paid / reserve set + reinsurance recovery progress.\n"
            "Flag any claim where the policyholder appears in the hazard zone but has not filed a claim — proactive outreach list."
        )
    }],
    'expected': [
        'Geographic + severity claims cluster',
        'Vulnerable-customer fast-track queue',
        'Reinsurance recovery estimate',
        'Empathetic outreach templates',
        'Daily COO bulletin',
    ],
    'watch': [
        'Vulnerable customer fast-track is automatic — not a manual scan',
        'Reinsurance recovery modelled per claim, not just at event level',
        'Proactive outreach to silent policyholders surfaces under-reporting',
    ],
    'honest': 'Cowork triages and drafts. Final claim acceptance still needs an adjuster. Treaty interpretation has nuance — Reinsurance team must validate before booking recoveries. Counsel may be needed for any liability-coded claims.',
    'tips': [
        'For ID variant, plug in BMKG hazard data for floods/earthquakes',
        'Add a 6th task — drone-imagery review queue prioritisation',
        'Re-run for motor surge events (multi-vehicle pileups) with different cohort logic',
    ],
}

CARDS['uc-lifeins-persistency'] = {
    'title': 'Persistency Drop Drill-Down',
    'dept_tag': 'Actuarial',
    'industry_tag': 'Life Insurance',
    'complexity': 'intermediate',
    'apps': ['Excel', 'PowerPoint', 'Word', 'Teams'],
    'desc': 'Why is 13M-persistency falling? Five years of policy data + agent activity + competitor pricing + customer complaints triangulate the answer with a board-ready remediation plan.',
    'skills': [
        'Cohort analysis by issue year × channel × product',
        'Cause attribution (price / agent churn / customer service / competitor)',
        'Remediation plan with quantified expected lift per intervention',
    ],
    'instructions': [
        'Open Cowork',
        'Attach the 4 source datasets',
        'Paste the prompt — Cowork drills + recommends + drafts in parallel',
    ],
    'sample_files': [
        ('LIFE_Policy_Master_5yr.xlsx', 'xlsx'),
        ('LIFE_Agent_Activity_Score.xlsx', 'xlsx'),
        ('LIFE_Competitor_Pricing.xlsx', 'xlsx'),
        ('LIFE_Customer_Complaint_NLP_Tags.xlsx', 'xlsx'),
    ],
    'prompts': [{
        'label': 'Persistency drill + remediation',
        'text': (
            "Using the 4 attached datasets, analyse why 13-month persistency has dropped from [X]% to [Y]%. In parallel:\n"
            "1) Cohort analysis in Excel — issue year × channel (agency / bancassurance / direct) × product line × persistency.\n"
            "2) Cause attribution — quantify the contribution of price, agent churn, customer service, competitor offering. Show effect sizes.\n"
            "3) Build a 12-slide deck in PowerPoint for the Board Risk Committee — the story, the data, the remediation.\n"
            "4) Draft a 2-page memo to the CEO in Word — top 3 recommendations + expected persistency lift per intervention.\n"
            "5) Draft a Teams message to the Heads of Agency + Banca + Direct — what changes in each channel.\n"
            "Cite the dataset + sheet + filter for every claim. No correlation-equals-causation conclusions — distinguish hypothesis from finding."
        )
    }],
    'expected': [
        'Cohort analysis grid',
        'Cause attribution with effect sizes',
        '12-slide Risk Committee deck',
        '2-page CEO memo',
        'Channel-head Teams message',
    ],
    'watch': [
        'Hypothesis vs finding distinguished — actuarial discipline',
        'Each intervention quantified — not generic "improve service"',
        'Channel-head messages differentiated — same data, channel-specific actions',
    ],
    'honest': 'Cowork builds the story. The Appointed Actuary signs off on any persistency assumption that flows into reserves. Lapse-supported product economics are complex — re-pricing decisions go through the Product Committee, not the model.',
    'tips': [
        'Add Takaful variant — overlay the Tabarru fund impact',
        'Re-run focused on a single product (e.g. ILP) to localise the diagnosis',
        'For ID variant, add OJK persistency benchmarks',
    ],
}

CARDS['uc-takaful-tabarru'] = {
    'title': 'Takaful Tabarru Fund Solvency Brief',
    'dept_tag': 'Takaful Operations',
    'industry_tag': 'Takaful',
    'complexity': 'intermediate',
    'apps': ['Excel', 'Word', 'PowerPoint'],
    'desc': 'Quarter-end Tabarru fund position, with surplus distribution plan, Shariah Committee briefing, and customer-facing surplus statement — generated in one pass.',
    'skills': [
        'Tabarru fund mechanics — contribution, claims, surplus, wakalah fee',
        'Surplus distribution policy application across cohorts',
        'Shariah-compliant customer communication',
    ],
    'instructions': [
        'Open Cowork',
        'Attach the Tabarru fund position, claims register, surplus policy, and prior-period statement',
        'Paste the prompt',
    ],
    'sample_files': [
        ('TKF_Tabarru_Position_QE.xlsx', 'xlsx'),
        ('TKF_Claims_Register_Q.xlsx', 'xlsx'),
        ('TKF_Surplus_Distribution_Policy.docx', 'docx'),
        ('TKF_Prior_Period_Statement.pdf', 'pdf'),
    ],
    'prompts': [{
        'label': 'Tabarru surplus brief',
        'text': (
            "Using the 4 attached files, prepare the Q[N] Tabarru fund brief. In parallel:\n"
            "1) Update the Tabarru position in Excel — Opening / Contributions / Claims / Wakalah fee / Investment income / Closing.\n"
            "2) Calculate the surplus available for distribution + apply the surplus distribution policy across cohorts.\n"
            "3) Draft a 3-page Shariah Committee briefing in Word — fund mechanics, surplus calculation, distribution rationale, Shariah ruling references.\n"
            "4) Build a 5-slide deck for the Board Audit Committee — fund health + surplus story.\n"
            "5) Draft the customer-facing surplus statement template — eligible cohorts get their pro-rata share, ineligible cohorts get a plain-English explanation of why.\n"
            "Cite the Shariah ruling and the policy clause for every number."
        )
    }],
    'expected': [
        'Tabarru fund roll-forward',
        'Surplus distribution calculation',
        'Shariah Committee briefing',
        'Audit Committee deck',
        'Customer surplus statement template',
    ],
    'watch': [
        'Wakalah fee separated from surplus — Shariah-correct treatment',
        'Ineligible cohorts get a plain-English "why not" — not silent omission',
        'Every figure ties to a Shariah ruling or a policy clause',
    ],
    'honest': 'Cowork applies the policy. The Appointed Actuary still confirms the surplus calculation; the Shariah Committee still rules on any edge case. Customer-facing statements must be approved by Comms + Compliance before mailing.',
    'tips': [
        'For Family Takaful add the participant-account split',
        'For Investment-Linked Takaful add the unit-fund overlay',
        'Re-run quarterly via Cowork scheduled refresh once policies are stable',
    ],
}

CARDS['uc-fintech-fraud'] = {
    'title': 'Real-Time Fraud Hotspot Brief',
    'dept_tag': 'Fraud Risk',
    'industry_tag': 'Fintech & Payments',
    'complexity': 'advanced',
    'apps': ['Excel', 'PowerPoint', 'Teams', 'Outlook'],
    'desc': 'Yesterday\'s transaction stream, fraud alerts, chargeback records, and merchant master converge into a hotspot heatmap, control recommendations, and merchant-bank dual outreach.',
    'skills': [
        'Fraud-pattern clustering across merchant × geo × time × method',
        'Loss vs control-cost trade-off — recommend tighten / loosen per cohort',
        'Dual-track comms — protect customers without tipping off the fraud ring',
    ],
    'instructions': [
        'Open Cowork',
        'Attach the 4 source datasets',
        'Paste the prompt — Cowork builds the heatmap + recommendations + outreach',
    ],
    'sample_files': [
        ('PAY_T_minus_1_Transactions.xlsx', 'xlsx'),
        ('PAY_Fraud_Alert_Log.xlsx', 'xlsx'),
        ('PAY_Chargeback_Register_30D.xlsx', 'xlsx'),
        ('PAY_Merchant_Master.xlsx', 'xlsx'),
    ],
    'prompts': [{
        'label': 'Fraud hotspot brief',
        'text': (
            "Using the 4 attached datasets, in parallel:\n"
            "1) Cluster T-1 fraud signals in Excel — merchant × geo × method × time-of-day. Highlight the top 10 hotspots.\n"
            "2) For each hotspot, recommend control action — block / step-up auth / hold for review / monitor. Quantify expected loss avoided vs control cost.\n"
            "3) Build a 5-slide CEO briefing in PowerPoint — yesterday, what we did, what we recommend.\n"
            "4) Draft an Outlook email to the affected merchants — coded language that does not reveal the fraud pattern.\n"
            "5) Draft a Teams message to the Fraud Ops shift — action list for next 4 hours.\n"
            "Cite the alert ID + chargeback reference for every recommendation. Do NOT name the suspected fraud rings in any external comms."
        )
    }],
    'expected': [
        'Hotspot heatmap',
        'Control recommendations with cost-benefit',
        '5-slide CEO briefing',
        'Coded merchant outreach',
        'Fraud Ops shift Teams message',
    ],
    'watch': [
        'External comms never reveal the pattern — fraud ring stays uninformed',
        'Control recommendations are quantified — not generic "tighten rules"',
        'CEO briefing answers "what is the loss today, what is the loss tomorrow if we do nothing"',
    ],
    'honest': 'Cowork drafts. Real-time blocking decisions still pass through the Fraud Risk Manager. Pattern attribution can be wrong — control actions on first-time merchant signals should err on the side of step-up, not outright block.',
    'tips': [
        'For card-present add the EMV chip data overlay',
        'For wallet topup add the source-of-funds check trigger',
        'Re-run hourly via Cowork scheduled refresh during high-risk windows (paydays, festive periods)',
    ],
}

CARDS['uc-remit-corridor'] = {
    'title': 'FX Corridor Pricing Refresh',
    'dept_tag': 'Treasury',
    'industry_tag': 'Cross-Border Remittance',
    'complexity': 'intermediate',
    'apps': ['Excel', 'PowerPoint', 'Teams'],
    'desc': 'Volumes, competitor pricing, FX cost, and customer complaint themes per corridor decide where to widen the spread, where to narrow, and where to defend share.',
    'skills': [
        'Margin sensitivity simulation per corridor',
        'Competitor spread benchmarking from public-rate scrapes',
        'Volume-vs-margin trade-off framing for product committee',
    ],
    'instructions': [
        'Open Cowork',
        'Attach the 4 source files',
        'Paste the prompt',
    ],
    'sample_files': [
        ('REM_Corridor_Volume_90D.xlsx', 'xlsx'),
        ('REM_Competitor_Live_Rates.xlsx', 'xlsx'),
        ('REM_FX_Cost_Sheet.xlsx', 'xlsx'),
        ('REM_Customer_NPS_Themes.xlsx', 'xlsx'),
    ],
    'prompts': [{
        'label': 'Corridor margin refresh',
        'text': (
            "Using the 4 attached files, in parallel:\n"
            "1) Build the corridor margin grid in Excel — 12 corridors × Spread / Volume / Margin / Customer NPS.\n"
            "2) Simulate +/- 10/25/50 bp spread changes per corridor — show volume elasticity and total margin impact.\n"
            "3) Build a 6-slide Product Committee deck — recommended action per corridor (widen / narrow / hold / promo).\n"
            "4) Draft a Teams message to the Heads of Corridor Operations — what changes when, with what comms.\n"
            "5) Build a customer-comms calendar — which corridors get a promo headline, which get silent.\n"
            "Cite the volume cell + competitor scrape for every claim."
        )
    }],
    'expected': [
        'Corridor margin grid',
        'Spread-change simulation',
        '6-slide Product Committee deck',
        'Corridor-ops Teams message',
        'Customer-comms calendar',
    ],
    'watch': [
        'Volume elasticity simulated, not guessed',
        'Each corridor gets a distinct action — no one-size-fits-all',
        'Customer NPS overlay prevents margin-chasing that breaks loyalty',
    ],
    'honest': 'Cowork models. The Treasurer signs off on the spread move. Live-rate scrapes have a 5-15 minute lag — final decisions confirmed against your real-time RFQ feed. Promo headlines must clear Compliance for any APR-disclosure rules in the destination corridor.',
    'tips': [
        'Add Bahasa Malaysia + Bahasa Indonesia variants for the customer comms',
        'For digital wallets, add the wallet-load fee component',
        'Re-run when a new BNM / OJK / MAS notice changes the disclosure rules',
    ],
}

CARDS['uc-hospital-caseconf'] = {
    'title': 'Case Conference Prep — Multi-Disciplinary Team',
    'dept_tag': 'Clinical Operations',
    'industry_tag': 'Healthcare',
    'complexity': 'intermediate',
    'apps': ['Word', 'Teams', 'PowerPoint'],
    'desc': 'The day before a tumour board / MDT case conference, EMR notes, latest scans, pathology, and prior MDT minutes assemble into a structured patient brief plus the chair agenda.',
    'skills': [
        'Clinical-record synthesis — EMR + imaging + pathology + prior MDT',
        'Structured patient brief in SOAP-or-equivalent format',
        'Chair-agenda assembly with time-boxed slots',
    ],
    'instructions': [
        'Open Cowork',
        'Attach the patient pack (de-identified for demo)',
        'Paste the prompt',
        'PHI controls: do NOT use real patient data in demo runs — use the synthetic pack',
    ],
    'sample_files': [
        ('HC_Patient_EMR_Excerpt.docx', 'docx'),
        ('HC_Latest_Scan_Report.pdf', 'pdf'),
        ('HC_Pathology_Report.pdf', 'pdf'),
        ('HC_Prior_MDT_Minutes.docx', 'docx'),
    ],
    'prompts': [{
        'label': 'MDT case brief',
        'text': (
            "Using the 4 attached patient artefacts, prepare the tomorrow MDT brief for Patient [PT-ID]. In parallel:\n"
            "1) Build a 1-page patient brief in Word — Presenting / History / Examinations / Imaging / Pathology / Current Plan / Open questions for the MDT.\n"
            "2) Build 3 slides in PowerPoint — Slide 1 patient summary, Slide 2 imaging + pathology side-by-side, Slide 3 the 3 decisions sought.\n"
            "3) Draft the MDT chair agenda — 8 patients × 6 minutes each + 12 minutes group items.\n"
            "4) Draft a Teams message to the MDT roster — case order, who presents, who decides.\n"
            "5) Build a follow-up tracker in Excel — for each decision, owner + due date + escalation rule.\n"
            "Cite the EMR section / scan date / path report ID for every clinical claim. Flag any data point older than 30 days as stale."
        )
    }],
    'expected': [
        '1-page patient brief',
        '3-slide case deck',
        'MDT chair agenda (8 patients)',
        'MDT roster Teams message',
        'Follow-up tracker',
    ],
    'watch': [
        'Stale data (>30 days) auto-flagged — clinician knows to refresh',
        'Decisions sought are explicit — MDT does not drift into discussion-only',
        'Follow-up tracker prevents decisions from getting lost between MDTs',
    ],
    'honest': 'Cowork synthesises the record. Clinical decisions remain the MDT\'s. PHI / PDPA / HIPAA: never use real patient data without proper anonymisation pipelines + a hospital DPO sign-off — Cowork in M365 sits in the M365 tenant boundary, follow your institution\'s data policy.',
    'tips': [
        'Re-run as a Morbidity & Mortality conference prep with M&M-specific structure',
        'For oncology, add the most recent staging + treatment-line history',
        'Add a 6th task — generate the post-MDT decision letter to the referring physician',
    ],
}

CARDS['uc-pharma-regsubmission'] = {
    'title': 'Variation Submission Pack — DCA / BPOM',
    'dept_tag': 'Regulatory Affairs',
    'industry_tag': 'Pharmaceutical',
    'complexity': 'advanced',
    'apps': ['Word', 'Excel', 'Outlook'],
    'desc': 'A manufacturing change → regulatory variation submission (DCA Malaysia, BPOM Indonesia) — CTD module assembly, change-control rationale, response template for likely queries.',
    'skills': [
        'CTD module structure (Module 1-5) auto-mapping',
        'Change-control rationale drafting with regulatory references',
        'Q&A template anticipating reviewer queries',
    ],
    'instructions': [
        'Open Cowork',
        'Attach the change-control package, prior approved dossier extract, regulator guideline',
        'Paste the prompt',
    ],
    'sample_files': [
        ('PHA_Change_Control_Package.docx', 'docx'),
        ('PHA_Prior_Approved_Dossier_Excerpt.pdf', 'pdf'),
        ('PHA_DCA_BPOM_Variation_Guideline.pdf', 'pdf'),
        ('PHA_Stability_Data_Tables.xlsx', 'xlsx'),
    ],
    'prompts': [{
        'label': 'Variation submission pack',
        'text': (
            "Using the 4 attached files, prepare the [PRODUCT] variation submission to [DCA / BPOM]. In parallel:\n"
            "1) Draft the Module 1 cover letter and forms in Word.\n"
            "2) Draft the Module 3 quality variation rationale — reference the change against the prior approved dossier + the guideline clause.\n"
            "3) Summarise the stability data in Excel — Time-point / Storage condition / Assay / Impurity / Conclusion.\n"
            "4) Draft an internal Q&A document anticipating the 8 most likely reviewer queries with proposed responses.\n"
            "5) Draft an Outlook email + Teams message to the QA Director + Plant Manager + Marketing Authorisation Holder — submission status and next-action owners.\n"
            "Cite the dossier section + guideline clause for every claim. Mark anything outside the prior approved dossier in red."
        )
    }],
    'expected': [
        'Module 1 cover + forms',
        'Module 3 quality rationale',
        'Stability data summary',
        'Anticipated Q&A document',
        'Internal stakeholder briefing',
    ],
    'watch': [
        'Anything outside the prior approved dossier flagged in red — reviewer-ready transparency',
        'Stability data tabulated against guideline storage conditions — auditable',
        'Q&A prep prevents response cycles that delay approval',
    ],
    'honest': 'Cowork drafts. The Qualified Person and Regulatory Affairs Director sign off before submission. DCA and BPOM templates evolve — check the latest circular. Cross-border variation harmonisation (ASEAN ACTR) is not automatic and must be validated per country.',
    'tips': [
        'For ASEAN harmonised variations, re-run with the ACTR Common Technical Document headers',
        'Add a 6th task — generate the Marketing Authorisation Holder internal note + Board notification',
        'For combination products, add the device-side change-control overlay',
    ],
}
