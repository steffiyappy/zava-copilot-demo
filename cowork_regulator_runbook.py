"""
cowork_regulator_runbook.py

Injects 9 multi-step Cowork use cases into existing Zava hub entries —
financial-regulator (industry) plus department spill (dept-legal,
dept-hr, dept-investor-relations, dept-marketing, dept-procurement,
dept-finance, dept-strategy, dept-risk, dept-corpsec).

These use cases were inspired by real capital-markets regulator demo
sessions but are written generically against the Zava conglomerate's
own regulator-affiliate and cross-functional departments. No external
customer identity is used. All file names use Zava-internal prefixes
(REG_/HR_/IE_/LEG_/PRC_/AUD_).

Each use case follows the same shape:
  - 5-6 base prompt steps (extract → check → draft → fan-out)
  - + 1 HTML artifact step (dashboard / kanban / heatmap / pipeline)
  - License: T_COWORK = FRONTIER
  - Sample files declared in card['files'] are appended to entry.files[]

Idempotent via 60-char prompt-prefix check.
"""

# ── Use case catalog ─────────────────────────────────────────────────────
REGULATOR_USE_CASES = [
    # ────────────────────────────────────────────────────────────────────
    {
        'slug': 'reg-ipo-prospectus-compliance',
        'title': 'IPO Prospectus Compliance Review',
        'business_group': 'Issuer Review · Equities',
        'apps': ['Researcher', 'Excel', 'Word', 'Outlook', 'Planner'],
        'complexity': 'Advanced',
        'files': [
            'REG_IPO_Prospectus_Sample.pdf',
            'REG_Issuer_Intake_Template.xlsx',
            'REG_Issuer_Compliance_Checklist.xlsx',
            'REG_Equities_Submission_Guidelines.docx',
        ],
        'steps': [
            {
                'label': 'Extract issuer profile + financials from prospectus PDF',
                'text': (
                    "I am a regulator officer in the Equities Issuer-Review unit. I have "
                    "uploaded an IPO prospectus PDF (REG_IPO_Prospectus_Sample.pdf) and the "
                    "standard issuer intake template (REG_Issuer_Intake_Template.xlsx). "
                    "From the prospectus, extract the following into the template's INPUT tab: "
                    "(1) Issuer profile — legal name, incorporation date, principal activities, "
                    "registered office, group structure. "
                    "(2) Use of proceeds — table with each tranche, amount in MYR, intended "
                    "use, timeline. "
                    "(3) Financial highlights — last 3 years Revenue, EBITDA, PAT, Total "
                    "Assets, Net Debt, ROE. "
                    "(4) Risk factors — top 10 ranked by materiality. "
                    "(5) Promoter and substantial shareholders — name, holding %, lock-in "
                    "period. "
                    "Preserve sign conventions and currency. If any required field is not "
                    "discoverable in the prospectus, write 'NOT FOUND IN PROSPECTUS' and flag "
                    "in a sheet called 'Gaps'. Save as "
                    "'Issuer_Intake_[ISSUER]_[DATE].xlsx' to /IssuerReview/Equities/[YYYY-MM]/."
                ),
            },
            {
                'label': 'Run automated Completeness Filter against the checklist',
                'text': (
                    "Building on the populated intake template from Step 1, now run an "
                    "automated Completeness Filter against REG_Issuer_Compliance_Checklist.xlsx "
                    "(tab 'EQUITY_LBR_R3'). "
                    "For each checklist line item, mark Pass / Fail / N/A based on whether the "
                    "prospectus disclosure meets the rule. For every Fail, cite the specific "
                    "page and clause in the prospectus that was inadequate, and quote the "
                    "checklist rule reference. Tabulate as 'Completeness_Filter' sheet in the "
                    "same workbook. Generate a one-line summary at the top: "
                    "'X of Y items Pass; Z items Fail (see rows highlighted red); W items N/A.'"
                ),
            },
            {
                'label': 'Compliance Check on key narrative (Risk Factors, Use of Proceeds)',
                'text': (
                    "Now run a Compliance Check on the Key Narrative sections — Risk Factors, "
                    "Use of Proceeds, Director Statements, Audit Committee Statement — against "
                    "REG_Equities_Submission_Guidelines.docx. "
                    "For each section, do all 3: "
                    "(a) Identify any boilerplate / non-substantive language that fails the "
                    "'clear and specific' standard in the guidelines. "
                    "(b) Flag any inconsistencies between sections (e.g. risk factor on FX not "
                    "matched by FX hedging policy disclosure). "
                    "(c) Suggest a one-line query the issuer must address before submission "
                    "is accepted. Output as a 'Narrative_Check' sheet with columns Section, "
                    "Page, Finding, Severity (Red/Amber/Green), Suggested Query."
                ),
            },
            {
                'label': 'Draft Smart Query Letter + circulate to issuer + log in Planner',
                'text': (
                    "Building on the Completeness Filter + Narrative Check, now do all 4 in "
                    "one Cowork run: "
                    "1) Draft a Smart Query Letter in Word, addressed to the issuer's "
                    "Reporting Accountant (CC: Principal Adviser). Group queries by section, "
                    "cite the exact rule reference for each, and propose a 14-day response "
                    "deadline. Tone: regulatory-formal, never speculative. "
                    "2) Draft a one-page internal cover note to the Head of Issuer-Review "
                    "summarising the verdict (Accept / Refer for Query / Refer for Rejection), "
                    "the 3 biggest gaps, and the recommended action. "
                    "3) Draft an Outlook email to the case officer with the query letter + "
                    "cover note attached, asking for sign-off. "
                    "4) Create a Planner task: 'Issuer response — [ISSUER NAME]' with the "
                    "14-day deadline, assigned to the case officer, with the query letter "
                    "linked. Tag #IPO #IssuerReview #ActiveCase."
                ),
            },
            {
                'label': 'Schedule Teams review meeting with reporting accountant',
                'text': (
                    "Schedule a 60-minute Teams meeting for [DATE+5 business days at 10am] "
                    "titled 'IPO Query Clarification — [ISSUER]'. Invite the issuer's "
                    "Reporting Accountant, Principal Adviser, the case officer and the Head "
                    "of Issuer-Review. In the meeting body include the query letter as a link, "
                    "the 3 priority items for discussion, and a one-line meeting purpose. "
                    "Also send a Teams chat reminder to the case officer at T-24h with a "
                    "summary of the 3 priority items."
                ),
            },
        ],
        'watch': (
            "Completeness Filter catches the rule-letter compliance gaps; the Narrative "
            "Check catches the rule-spirit gaps that boilerplate language hides. Always cite "
            "the page + clause; never paraphrase the rule."
        ),
        'honest': (
            "The Completeness Filter is rule-letter; the case officer must still apply "
            "judgment on materiality, market context and issuer history. The Smart Query "
            "Letter is a draft — the Head of Issuer-Review signs the final letter."
        ),
        'html_archetype': 'heatmap',
        'html_brief': (
            "IPO Compliance Heatmap — Prospectus sections (rows) × Compliance dimensions "
            "(Completeness, Narrative Clarity, Consistency, Rule Reference) with Red/Amber/"
            "Green cells; click a cell to open a drawer with the underlying finding text "
            "and the page reference. Includes a sticky verdict ribbon at top "
            "(Accept / Refer for Query / Refer for Rejection)."
        ),
    },

    # ────────────────────────────────────────────────────────────────────
    {
        'slug': 'reg-complaint-triage',
        'title': 'Anti-Scam Complaint Triage End-to-End',
        'business_group': 'Compliance · Anti-Scam Unit',
        'apps': ['Researcher', 'Excel', 'Word', 'Outlook', 'Teams', 'Planner'],
        'complexity': 'Intermediate',
        'files': [
            'REG_AntiScam_Complaint_Sample.pdf',
            'REG_AntiScam_Complaint_Register.xlsx',
            'REG_Broker_FundManager_Database.xlsx',
            'REG_AntiScam_Email_Reply_Library.docx',
        ],
        'steps': [
            {
                'label': 'Summarise voluminous complainant documents',
                'text': (
                    "I am an officer in the Anti-Scam Unit. I have a complaint package "
                    "(REG_AntiScam_Complaint_Sample.pdf — 47 pages mixing typed letter, "
                    "screenshots of WhatsApp chats, scanned bank statements, and a CSV of "
                    "transactions). "
                    "Read all attachments and produce a structured complaint summary in a "
                    "table with columns: Complainant, Date Received, Alleged Scheme Type "
                    "(boiler-room / clone-firm / unregulated DeFi / Ponzi / other), Suspect "
                    "Entities Named, Suspect Individuals Named, Money Trail (MYR amounts "
                    "and channels), Loss Amount in MYR, Supporting Evidence (1-line per "
                    "exhibit), Red-flag Indicators. "
                    "Translate anything not in English. Where a name is partially obscured, "
                    "mark '** PARTIAL ID' so the officer can ask for clarification."
                ),
            },
            {
                'label': 'Cross-reference suspect entities with broker/fund manager database',
                'text': (
                    "Using the suspect entities and individuals from Step 1, cross-reference "
                    "with REG_Broker_FundManager_Database.xlsx (tabs: Licensed_Entities, "
                    "Licensed_Individuals, Watchlist, Past_Complaints). For each match, "
                    "produce a row showing: Suspect Name, Match Type (Exact / Fuzzy / Alias / "
                    "Clone-firm), Database Reference, Current Licence Status (Active / "
                    "Suspended / Revoked / Never-Licensed), Prior Complaint Count (last 12 "
                    "months), and Risk Verdict (Confirm scam / Likely scam / Refer for "
                    "investigation / Insufficient info). Cite the exact database tab + row "
                    "for every claim — do not fabricate."
                ),
            },
            {
                'label': 'Draft curated complaint response email (EN) + translate to BM',
                'text': (
                    "Building on the summary + cross-reference, draft a curated complaint "
                    "response email to the complainant in English. Pick the closest matching "
                    "template from REG_AntiScam_Email_Reply_Library.docx (templates T01-T08). "
                    "The reply must: (a) acknowledge receipt, (b) state the case has been "
                    "opened with reference AS-[YYYY]-[NNNN], (c) explain the next 14 days "
                    "of investigation in plain language, (d) provide 3 protective actions the "
                    "complainant should take immediately (no fund transfers, secure accounts, "
                    "report to bank), (e) close with a clear next-contact date. Tone: "
                    "empathetic but precise, never promise outcomes. "
                    "Then translate the entire reply into Bahasa Malaysia (formal register), "
                    "preserving meaning and tone. Save both as 'AntiScam_Reply_[REF]_EN.docx' "
                    "and 'AntiScam_Reply_[REF]_BM.docx'."
                ),
            },
            {
                'label': 'Update complaint register + Planner + escalate Red verdicts',
                'text': (
                    "Now do all 4 in one Cowork run: "
                    "1) Add a new row to REG_AntiScam_Complaint_Register.xlsx with: "
                    "Reference, Date, Complainant (Initials only — PII), Alleged Scheme, "
                    "Suspect Entities, Loss MYR, Verdict, Assigned Officer, Next-Action Date, "
                    "Status (Open). "
                    "2) Create a Planner task 'Anti-Scam investigation — [REF]' assigned to "
                    "the duty officer with the 14-day next-action deadline. "
                    "3) If the Verdict from Step 2 was 'Confirm scam' or 'Likely scam' on a "
                    "Watchlist or unlicensed entity, also draft an escalation email to "
                    "Enforcement with the summary + cross-reference attached and a request "
                    "to consider a public warning. "
                    "4) If the suspect entity matches a Licensed_Entities row, draft a "
                    "second escalation email to the Supervision desk of that licensee."
                ),
            },
            {
                'label': 'Compile weekly Anti-Scam management snapshot',
                'text': (
                    "Compile a Friday-EOD weekly Anti-Scam snapshot in Word + a Teams "
                    "message in the Anti-Scam channel. Cover: complaints opened this week "
                    "(count + breakdown by scheme), complaints closed (count + outcome "
                    "distribution), top 5 loss amounts, top 3 most-named suspect entities, "
                    "watchlist additions proposed, and a 1-line management ask if any. "
                    "Pull data from REG_AntiScam_Complaint_Register.xlsx (this week's rows "
                    "only). Keep the Teams post to 6 lines max."
                ),
            },
        ],
        'watch': (
            "The cross-reference step is what makes this valuable — never accept a name "
            "as 'unlicensed' unless the database scan confirms it. Always cite the database "
            "tab + row."
        ),
        'honest': (
            "Auto-translation between EN/BM is good but legal-grade letters still need "
            "officer review. Public warnings are an Enforcement decision, not an Anti-Scam "
            "Unit decision — this runbook only escalates."
        ),
        'html_archetype': 'kanban',
        'html_brief': (
            "Complaint Pipeline kanban — 5 lanes (New / Triage / Investigate / Refer to "
            "Enforcement / Closed) with cards showing reference, complainant initials, "
            "scheme type, loss amount, days-open badge, and verdict pill. Click a card to "
            "drawer-open the full complaint summary + cross-reference matches."
        ),
    },

    # ────────────────────────────────────────────────────────────────────
    {
        'slug': 'reg-workforce-scenario',
        'title': 'Workforce Scenario & Capacity Impact Analysis',
        'business_group': 'Corporate Resources · HR & Knowledge Management',
        'apps': ['Excel', 'Word', 'PowerPoint', 'Outlook', 'Teams'],
        'complexity': 'Advanced',
        'files': [
            'HR_Workforce_FY2026.xlsx',
            'HR_Strategic_Priorities_2030.docx',
            'HR_Outsourcing_and_Contract_Staff.xlsx',
            'HR_Skill_Gap_Survey_2025.xlsx',
        ],
        'steps': [
            {
                'label': 'Build current workforce baseline (FTE, skills, location)',
                'text': (
                    "I am the Head of Corporate Resources at the Group. From "
                    "HR_Workforce_FY2026.xlsx (tabs: Headcount, Skills_Matrix, "
                    "Tenure_Distribution, Salary_Band), produce a baseline summary table "
                    "with columns: Business Group, Total FTE, Approved Headcount, Vacancy %, "
                    "Median Tenure (yrs), Skill Coverage % (against required skills in the "
                    "BG), and Watch Flags (e.g. >20% vacancy, key-person risk, >40% "
                    "near-retirement). Mark each BG Green/Amber/Red. Use only the numbers "
                    "in the workbook; do not fabricate."
                ),
            },
            {
                'label': 'Compare 4 workforce scenarios for FY27-FY30',
                'text': (
                    "Now build 4 forward scenarios for FY27-FY30 capacity planning: "
                    "(A) Status Quo — natural attrition + replacement only, "
                    "(B) Strategic Build — fill all priority skill gaps from "
                    "HR_Skill_Gap_Survey_2025.xlsx and HR_Strategic_Priorities_2030.docx, "
                    "(C) Lean & Outsource — convert 25% of routine roles to contract staff "
                    "(reference HR_Outsourcing_and_Contract_Staff.xlsx), "
                    "(D) Hybrid — strategic build for critical BGs and lean+outsource for "
                    "support BGs. "
                    "For each scenario, model: total FTE FY30, total salary cost FY30, skill "
                    "coverage % FY30, capacity-vs-2030-strategy gap, key risk. Present as a "
                    "side-by-side comparison table."
                ),
            },
            {
                'label': 'Quantify capacity-vs-strategy gap per BG',
                'text': (
                    "For Scenario D (Hybrid) — which is the management preferred direction — "
                    "now drill down per BG: for each BG, compare FY30 planned FTE + skill "
                    "mix vs the BG's 2030 strategic mandate (in "
                    "HR_Strategic_Priorities_2030.docx). Identify any BG where the gap is "
                    ">15% in FTE or >25% in critical-skill coverage. Tabulate as: BG, "
                    "Strategic Mandate (1 line), Capacity Gap, Skill Gap, Recommended "
                    "Mitigation (recruit / upskill / outsource / re-scope mandate). "
                    "Mark Red where the gap exceeds 25%."
                ),
            },
            {
                'label': 'Draft executive memo + Board paper appendix',
                'text': (
                    "Now do all 3 in one Cowork run: "
                    "1) Draft a 3-page Workforce Strategy executive memo in Word, addressed "
                    "to the Group CEO and copying the Chief HR Officer. Open with the "
                    "headline verdict, follow with the 4 scenarios compared, the "
                    "recommendation (Scenario D Hybrid) with rationale, and the 3 most "
                    "material capacity gaps that must be addressed within 12 months. Tone: "
                    "precise, decision-oriented. "
                    "2) Build a 8-slide PowerPoint Board paper appendix — Slide 1 cover, "
                    "Slide 2 baseline, Slides 3-6 the 4 scenarios, Slide 7 recommendation, "
                    "Slide 8 12-month implementation plan. Use the Group corporate template. "
                    "3) Draft an Outlook email to the CEO with both attached, asking for a "
                    "15-min review slot in the next CEO catch-up."
                ),
            },
            {
                'label': 'Schedule cross-BG workshop + invite Heads of BG',
                'text': (
                    "Schedule a 90-minute Teams workshop titled 'FY27-FY30 Workforce Strategy "
                    "Consultation' for [DATE+10 business days at 2pm]. Invite the Heads of "
                    "all critical BGs plus the CHRO. In the invite body include: the headline "
                    "recommendation, the 3 BGs with the largest capacity gaps, and 4 pre-"
                    "read questions. Attach the Board paper appendix from Step 4. Send a "
                    "follow-up Teams reminder 24h before with the 3 priority discussion "
                    "questions."
                ),
            },
        ],
        'watch': (
            "Scenario D Hybrid is the model recommendation but the workshop discussion may "
            "shift mandates per BG. Re-run the scenario after the workshop with revised "
            "inputs before submitting to Board."
        ),
        'honest': (
            "Skill coverage % is only as good as the input survey; refresh the underlying "
            "Skill_Gap_Survey before any final commitment. Outsourcing ratios assume "
            "current procurement panel rates — re-check with Procurement."
        ),
        'html_archetype': 'dashboard',
        'html_brief': (
            "Interactive Workforce Scenario App — left panel has sliders for FY27-FY30 "
            "(headcount delta per BG, attrition rate, salary inflation, outsource ratio, "
            "training spend). Right panel shows live KPI tiles (Total FTE, Total Cost, "
            "Skill Coverage %, Gap-to-Strategy %) and a per-BG heatmap underneath. "
            "Includes a 'Save Scenario' button that emits a JSON blob to paste into Excel."
        ),
    },

    # ────────────────────────────────────────────────────────────────────
    {
        'slug': 'reg-investor-education-audit',
        'title': 'Investor Education Campaign Effectiveness Audit',
        'business_group': 'Consumer & Investor Office · Investor Education',
        'apps': ['Excel', 'Word', 'PowerPoint', 'Outlook', 'Teams', 'Planner'],
        'complexity': 'Intermediate',
        'files': [
            'IE_Campaign_Metrics_Q1.xlsx',
            'IE_Budget_vs_Actual.xlsx',
            'IE_Event_Attendance_Register.xlsx',
            'IE_Bilingual_Content_Library.docx',
        ],
        'steps': [
            {
                'label': 'Aggregate engagement data across channels',
                'text': (
                    "I am the Head of Investor Education at the Consumer & Investor Office. "
                    "From IE_Campaign_Metrics_Q1.xlsx (tabs: Website, Social_Media, Events, "
                    "Webinar) and IE_Event_Attendance_Register.xlsx, build a Q1 engagement "
                    "scorecard. Columns: Campaign Name, Channel Mix (icons), Reach, Engaged "
                    "Audience (defined as 30s+ watch / 60s+ read), Conversion (sign-ups / "
                    "quiz completions / scam-quiz pass rate), Cost-per-Engaged-Audience "
                    "(MYR), and Owner BG. Calculate utilisation rates automatically. Mark "
                    "Red if Cost-per-Engaged > median × 1.5."
                ),
            },
            {
                'label': 'Cross-check vs budget vs actual',
                'text': (
                    "Now cross-reference with IE_Budget_vs_Actual.xlsx (tab: Q1_Tracker). "
                    "For each campaign, produce a row showing: Budgeted Cost, Actual Cost, "
                    "Variance %, Engagement KPI Met (Y/N — defined as Engaged Audience >= "
                    "80% of plan), and Verdict (Continue / Reduce / Stop / Scale). Cite the "
                    "specific KPI target from the budget tab — do not invent the target. "
                    "Total the budget vs actual at bottom with a single-line headline."
                ),
            },
            {
                'label': 'Generate bilingual EN-BM performance report',
                'text': (
                    "Draft a 4-page Investor Education Quarterly Performance Report in Word. "
                    "Sections: Executive Summary (3 bullets), Campaign Scorecard (insert the "
                    "Step 1 table), Budget vs Actual (Step 2 table), Top 3 Wins, Top 3 "
                    "Learnings, Q2 Plan Adjustments. Pull tone and bilingual phrasing from "
                    "IE_Bilingual_Content_Library.docx. After drafting in English, produce a "
                    "fully translated Bahasa Malaysia version (same structure, matching "
                    "numbering, same tables). Save both as 'IE_Q1_Report_EN.docx' and "
                    "'IE_Q1_Report_BM.docx'."
                ),
            },
            {
                'label': 'Build dashboard slide + send to management',
                'text': (
                    "Now do all 3 in one Cowork run: "
                    "1) Build 1 PowerPoint slide titled 'Q1 Investor Education Performance' "
                    "with: a 2x2 quadrant (Reach × Cost-per-Engaged) plotting each campaign, "
                    "the top-line YoY engagement comparison, and the 3 Q2 actions. Use the "
                    "Group corporate template. "
                    "2) Draft an Outlook email to the Chief Consumer & Investor Officer with "
                    "the EN + BM reports + slide attached, requesting endorsement for the "
                    "Q2 plan. "
                    "3) Schedule a 30-min Teams 'IE Quarterly Review' meeting for "
                    "[DATE+3 business days at 11am] with the Chief Officer, the IE team lead, "
                    "and the Comms lead. Include the slide as a meeting pre-read."
                ),
            },
            {
                'label': 'Update central IE database + Planner tasks for Q2',
                'text': (
                    "Update the central IE database (use the Q1 Tracker tab in "
                    "IE_Campaign_Metrics_Q1.xlsx as canonical) with the verdicts from "
                    "Step 2. Then create 3-5 Planner tasks for Q2: one per 'Continue' or "
                    "'Scale' campaign with the next milestone + owner + deadline. Tag each "
                    "task #IE #Q2 and link the campaign verdict back to the database row."
                ),
            },
        ],
        'watch': (
            "Engagement-rate calculation must use a consistent definition across channels "
            "or comparisons are misleading. The bilingual draft must be reviewed by the "
            "Comms lead before publication — translation alone is not enough."
        ),
        'honest': (
            "Quiz pass rate is a proxy for understanding, not behaviour change. Long-term "
            "behaviour metrics (e.g. drop in scam complaint volume) live in the Anti-Scam "
            "Unit's data, not IE's, and should be paired with this report."
        ),
        'html_archetype': 'dashboard',
        'html_brief': (
            "IE Campaign Multi-Channel Dashboard — header KPI tiles (Total Reach, Engaged "
            "Audience, Cost-per-Engaged, YoY Growth %), middle 2x2 quadrant of campaigns "
            "(Reach × Cost-per-Engaged), per-channel performance bars (Website/Social/"
            "Events/Webinar), and a bottom bilingual EN/BM toggle that swaps all labels."
        ),
    },

    # ────────────────────────────────────────────────────────────────────
    {
        'slug': 'reg-contract-review',
        'title': 'Contract Review & Risk Annotation',
        'business_group': 'Legal · Advisory',
        'apps': ['Researcher', 'Word', 'Excel', 'Outlook', 'Teams'],
        'complexity': 'Advanced',
        'files': [
            'LEG_Vendor_Contract_Draft.docx',
            'LEG_Clause_Library_Favourable.xlsx',
            'LEG_Court_Case_Precedents.xlsx',
            'LEG_Standard_Terms_Schedule.docx',
        ],
        'steps': [
            {
                'label': 'Grammar + inconsistency sweep',
                'text': (
                    "I am Group Advisory counsel. Read LEG_Vendor_Contract_Draft.docx "
                    "end-to-end. Produce 3 outputs in one table: "
                    "(a) Grammar/typo list — page, line, error, suggested correction. "
                    "(b) Definitional inconsistencies — capitalised terms used but not "
                    "defined, defined terms not used, or terms defined differently across "
                    "clauses. "
                    "(c) Cross-reference errors — clauses referencing non-existent clause "
                    "numbers or schedules. "
                    "Do not propose substantive redlines yet — that is Step 3. Save as "
                    "'Contract_GrammarCheck.xlsx'."
                ),
            },
            {
                'label': 'Identify clauses NOT favourable to the Group',
                'text': (
                    "Cross-reference every clause in LEG_Vendor_Contract_Draft.docx against "
                    "LEG_Clause_Library_Favourable.xlsx (tabs: Liability_Caps, "
                    "Indemnity_Standard, Termination_Rights, IP_Ownership, Data_Protection, "
                    "Dispute_Resolution, Audit_Rights, SLA_Penalties). For each contract "
                    "clause, mark Favourable / Neutral / Unfavourable to the Group, and cite "
                    "the library row that defines the Group-preferred position. For every "
                    "Unfavourable clause, draft a one-paragraph redline that restores the "
                    "Group position. Tabulate as Clause #, Page, Current Text (truncated), "
                    "Verdict, Library Reference, Proposed Redline."
                ),
            },
            {
                'label': 'Research market precedents + court cases',
                'text': (
                    "For the top 5 Unfavourable clauses from Step 2, research precedents "
                    "using LEG_Court_Case_Precedents.xlsx (tab: Recent_Cases — 2020 onwards) "
                    "and Researcher web grounding for any post-cutoff cases. For each "
                    "clause, produce a brief: Case Name, Year, Court, Outcome, Why It "
                    "Strengthens (or Weakens) the Group redline. Cite the exact case "
                    "reference. If Researcher finds a post-2025 case that materially changes "
                    "the position, flag with 'NEW: ' prefix."
                ),
            },
            {
                'label': 'Draft advisory memo + redlined contract + escalation email',
                'text': (
                    "Now do all 4 in one Cowork run: "
                    "1) Draft an Advisory Memo in Word to the Head of Legal: open with "
                    "the verdict (Sign as-is / Sign with caveats / Renegotiate before sign), "
                    "follow with the top 5 unfavourable clauses, the precedent support, and "
                    "the recommended fallback positions. Tone: counsel-formal, never "
                    "speculative. "
                    "2) Produce a redlined version of the contract — track-changes with the "
                    "proposed redlines from Step 2 inserted, comments referencing the "
                    "library row and case precedent. "
                    "3) Draft an Outlook email to the Head of Legal with both attached, "
                    "asking for sign-off before circulating to counterparty. "
                    "4) Draft a brief Outlook email to the counterparty's counsel (in "
                    "draft-only state — DO NOT send) opening the negotiation."
                ),
            },
            {
                'label': 'Schedule counterparty negotiation Teams call',
                'text': (
                    "Schedule a 60-minute Teams call titled 'Contract Negotiation — "
                    "[VENDOR NAME]' for [DATE+7 business days at 3pm]. Invite the Head of "
                    "Legal, Group Advisory counsel and the counterparty's counsel. Body of "
                    "invite: 'Discussion items: (1) Clause [X] indemnity scope, (2) Clause "
                    "[Y] termination, (3) Clause [Z] IP ownership, (4) Open Q&A.' Send a "
                    "Teams reminder 24h before with the redlined contract as a link."
                ),
            },
        ],
        'watch': (
            "The library + precedent grounding is what makes this defensible. Never propose "
            "a redline without citing the Group-preferred position from the library."
        ),
        'honest': (
            "Researcher precedent search must be cross-checked by the counsel of record. "
            "Court case applicability depends on jurisdiction and current rules of court — "
            "verify before relying."
        ),
        'html_archetype': 'heatmap',
        'html_brief': (
            "Contract Risk Heatmap — clauses (rows) × risk dimensions (Favourability, "
            "Precedent Support, Ambiguity, Enforceability, Counterparty Push-back Risk) "
            "with Red/Amber/Green cells. Click a cell to drawer-open the current clause "
            "text + proposed redline + cited precedent."
        ),
    },

    # ────────────────────────────────────────────────────────────────────
    {
        'slug': 'reg-tax-application',
        'title': 'Tax Application Processing (SFO / VC PE / Private Credit)',
        'business_group': 'Markets Development · Investment Management Division',
        'apps': ['Researcher', 'Excel', 'Word', 'Outlook', 'Planner'],
        'complexity': 'Intermediate',
        'files': [
            'REG_IMD_SFO_Application_Sample.pdf',
            'REG_IMD_VCPE_Application_Sample.pdf',
            'REG_PrivateCredit_Application_Sample.pdf',
            'REG_IMD_Eligibility_Rule_Matrix.xlsx',
            'REG_IMD_Application_Tracker.xlsx',
        ],
        'steps': [
            {
                'label': 'Triage application emails by type',
                'text': (
                    "I am a regulator officer in the Investment Management Division. I have "
                    "3 application packages in my inbox: REG_IMD_SFO_Application_Sample.pdf "
                    "(Single Family Office), REG_IMD_VCPE_Application_Sample.pdf (Venture "
                    "Capital / Private Equity), and REG_PrivateCredit_Application_Sample.pdf "
                    "(private credit from non-bank institutions). "
                    "For each, extract the triage header into a table: Application Type, "
                    "Applicant Legal Name, Date Received, Lead Officer Suggested, Document "
                    "Completeness Quick-Check (1 line), and Priority (Standard / Expedited / "
                    "Refer). Auto-suggest the lead officer based on application type and "
                    "current workload — rotate by next-available officer."
                ),
            },
            {
                'label': 'Extract structured fields into IMD intake template',
                'text': (
                    "For each of the 3 applications, extract the regulated fields into the "
                    "IMD standard intake spreadsheet — use REG_IMD_Application_Tracker.xlsx "
                    "(tabs: SFO_Intake, VCPE_Intake, PrivateCredit_Intake). Required fields "
                    "per type are listed in the tracker headers. "
                    "Key common fields: Applicant name, Jurisdiction, Beneficial Owners "
                    "(natural persons + holding %), Source of Funds attestation, Fund Size, "
                    "Investment Mandate (1-line), Compliance Officer, Auditor, Tax Adviser. "
                    "For SFO add: Family Member List, Wealth Source (Inherited / Earned / "
                    "Business Exit / Mixed), Generations Covered. "
                    "For VC PE add: Fund Strategy (Seed / Growth / Buyout), GP / LP "
                    "Structure, LP Concentration %. "
                    "For Private Credit add: Lending Strategy, Geographies, Borrower "
                    "Profile, Sectors. "
                    "Where a field is not discoverable, mark 'NOT FOUND' and flag in the "
                    "Gaps column."
                ),
            },
            {
                'label': 'Run eligibility check against IMD rule matrix',
                'text': (
                    "Run an eligibility check for each of the 3 applications against "
                    "REG_IMD_Eligibility_Rule_Matrix.xlsx (tabs: SFO_Rules, VCPE_Rules, "
                    "PrivateCredit_Rules). For each rule, mark Pass / Fail / "
                    "Insufficient_Info / N/A and cite the section of the application that "
                    "supports the verdict. Where Fail, draft a clarification query the "
                    "applicant must address. Tabulate as Rule #, Rule Description, Verdict, "
                    "Citation, Query (if Fail). At the bottom, write a single-line headline: "
                    "'X of Y rules Pass; Z items require clarification.'"
                ),
            },
            {
                'label': 'Draft assessment memo + clarification queries + send to applicants',
                'text': (
                    "Now do all 4 in one Cowork run for each of the 3 applications: "
                    "1) Draft a 1-page Assessment Memo in Word to the IMD lead officer "
                    "summarising the verdict (Approve / Refer for Clarification / Refer for "
                    "Decline), the 3 most material findings, and the recommended action. "
                    "2) Draft a Clarification Query Letter to the applicant in Word, "
                    "grouping queries by rule. Tone: regulatory-formal. Cite each rule. "
                    "3) Draft an Outlook email to the applicant's principal adviser with "
                    "the query letter attached and a 21-day deadline. "
                    "4) Create a Planner task 'IMD case clarification — [APPLICANT]' "
                    "assigned to the lead officer with the 21-day deadline."
                ),
            },
            {
                'label': 'Update IMD Application Tracker + weekly snapshot',
                'text': (
                    "Update REG_IMD_Application_Tracker.xlsx with new rows for the 3 cases "
                    "(Status: 'Pending Clarification', Lead Officer assigned, Next-Action "
                    "Date set 21 days out). Also compile a Friday weekly snapshot for the "
                    "Head of Markets Development in Teams: applications opened this week "
                    "(count by type), applications closed (count by outcome), median "
                    "days-to-clarification, and a 1-line management ask if any."
                ),
            },
        ],
        'watch': (
            "The rule-matrix check is rule-letter; final approval still rests on management "
            "judgment, especially for novel structures (e.g. multi-jurisdiction SFO with "
            "PEPs, or hybrid private credit vehicles)."
        ),
        'honest': (
            "Beneficial owner extraction from a corporate chart is best-effort — for any "
            "case with >3 ownership layers, request a re-confirmed UBO declaration before "
            "advancing to approval."
        ),
        'html_archetype': 'kanban',
        'html_brief': (
            "IMD Application Kanban — 5 lanes (New / Extracted / Eligibility Reviewed / "
            "Pending Clarification / Decision). Each card shows applicant initials, type "
            "pill (SFO/VCPE/PrivateCredit), lead officer, days-open, eligibility-pass %. "
            "Click to drawer-open the assessment memo + clarification queries."
        ),
    },

    # ────────────────────────────────────────────────────────────────────
    {
        'slug': 'reg-policy-paper',
        'title': 'Policy Paper Drafting & Industry Guidance Mode',
        'business_group': 'Markets Development · Securities & Derivatives Policy',
        'apps': ['Researcher', 'Word', 'PowerPoint', 'Outlook', 'Teams'],
        'complexity': 'Advanced',
        'files': [
            'REG_Policy_Existing_Library.xlsx',
            'REG_Policy_Peer_Regulator_Scan.xlsx',
            'REG_Policy_Industry_Consultation_Notes.docx',
            'REG_Policy_Standard_Template.docx',
        ],
        'steps': [
            {
                'label': 'Research peer-regulator policy moves (deep)',
                'text': (
                    "I am a Securities & Derivatives Policy officer drafting a new policy "
                    "on [TOPIC e.g. tokenised securities / private market access for retail "
                    "/ sustainable finance disclosure]. "
                    "Using Researcher with deep web grounding, scan the last 24 months of "
                    "policy publications, consultations and enforcement actions from peer "
                    "regulators: MAS (Singapore), SFC (Hong Kong), ASIC (Australia), FCA "
                    "(UK), SEC (US). For each peer regulator, produce: Latest Position "
                    "(1-line), Source (URL or document ref), Key Implementation Date, "
                    "Notable Divergence from the regulator's current position (in "
                    "REG_Policy_Existing_Library.xlsx). Tabulate. Cite every claim."
                ),
            },
            {
                'label': 'Synthesise shifts and risks',
                'text': (
                    "From Step 1 research, synthesise: (a) the 3 most material policy shifts "
                    "happening among peer regulators in the last 24 months; (b) the 3 "
                    "biggest divergences from the current local position; (c) the 3 risks "
                    "to market integrity / investor protection / market development if the "
                    "local position remains unchanged. Reference "
                    "REG_Policy_Industry_Consultation_Notes.docx for any prior industry "
                    "feedback on these areas."
                ),
            },
            {
                'label': 'Draft new policy paper (EN) using standard template',
                'text': (
                    "Using REG_Policy_Standard_Template.docx, draft the new policy paper in "
                    "English. Sections: Executive Summary, Background, Peer Regulator "
                    "Landscape (insert Step 1 table), Risk Analysis (insert Step 2 "
                    "synthesis), Proposed Position (3-5 detailed proposals), "
                    "Implementation Plan (12-24 months), Industry Consultation Plan, "
                    "Appendix A — Comparative Matrix. Tone: regulator-formal. "
                    "Quote existing policy clauses verbatim where amended; mark additions "
                    "in **bold** and deletions in ~~strikethrough~~."
                ),
            },
            {
                'label': 'Generate bilingual EN-BM industry guidance FAQ',
                'text': (
                    "From the Proposed Position section in Step 3, generate a public "
                    "industry guidance FAQ in EN: 10 anticipated industry questions with "
                    "regulator-grade answers. Then translate the entire FAQ into Bahasa "
                    "Malaysia (formal register). Save as 'Policy_FAQ_EN.docx' and "
                    "'Policy_FAQ_BM.docx'. Add a header note: 'This guidance is "
                    "non-binding; the operative position is set out in the policy paper.'"
                ),
            },
            {
                'label': 'Build consultation deck + schedule industry session',
                'text': (
                    "Now do all 3 in one Cowork run: "
                    "1) Build a 12-slide PowerPoint consultation deck — Slide 1 cover, "
                    "Slides 2-3 problem statement + peer landscape, Slides 4-6 proposed "
                    "position, Slides 7-8 implementation roadmap, Slide 9 FAQ teaser, "
                    "Slide 10 consultation questions for industry, Slide 11 next steps, "
                    "Slide 12 contact. Use the corporate template. "
                    "2) Schedule a 2-hour Teams 'Industry Consultation — [TOPIC]' session "
                    "for [DATE+30 calendar days at 10am]. Invite the national stock "
                    "exchange operator, fund managers' association, accounting institute, "
                    "public accountants association and the 5 largest licensed "
                    "intermediaries. Attach the policy paper + FAQ + deck. "
                    "3) Draft an Outlook email to the Head of Markets Development with the "
                    "package attached, asking for endorsement before circulation."
                ),
            },
        ],
        'watch': (
            "Peer-regulator scan must cite source URLs and dates — never paraphrase a "
            "regulatory position. Industry consultation is consultative not delegative — "
            "the policy decision still rests with the regulator."
        ),
        'honest': (
            "Researcher grounding is broad but not exhaustive; final policy paper must be "
            "fact-checked by the policy legal officer of record. Translation must be "
            "reviewed by a bilingual senior officer."
        ),
        'html_archetype': 'dashboard',
        'html_brief': (
            "Policy Comparative Dashboard — top KPI ribbon (Peer Regulators Scanned, "
            "Material Shifts Identified, Divergences, Risks), middle comparative table "
            "with local position vs MAS vs SFC vs ASIC vs FCA vs SEC across 6 dimensions, "
            "side panel of links to source documents. Toggle EN/BM for label translation."
        ),
    },

    # ────────────────────────────────────────────────────────────────────
    {
        'slug': 'reg-procurement-benchmarking',
        'title': 'Procurement Commercial Benchmarking',
        'business_group': 'Corporate Resources · Procurement',
        'apps': ['Researcher', 'Excel', 'Word', 'PowerPoint', 'Outlook', 'Teams'],
        'complexity': 'Intermediate',
        'files': [
            'PRC_Vendor_Responses.xlsx',
            'PRC_RFP_Requirements.docx',
            'PRC_Past_Contracts.xlsx',
            'PRC_Industry_Benchmark.xlsx',
        ],
        'steps': [
            {
                'label': 'Compare vendor responses across cost + capability + risk',
                'text': (
                    "I am a procurement officer at the Group. I have 5 vendor responses to "
                    "the [SERVICE] RFP, listed in PRC_Vendor_Responses.xlsx (tabs: "
                    "Vendor_A through Vendor_E). Cross-reference each response against "
                    "PRC_RFP_Requirements.docx and produce a side-by-side comparison table "
                    "with columns: Vendor, Headline Price (MYR), Per-Unit Rate, Capability "
                    "Score (0-10 against 8 RFP capability requirements), Track Record Score "
                    "(0-10 against past projects of similar scale), Risk Score (0-10 — "
                    "lower is better), Local Content %, ESG / Sustainability Rating. Mark "
                    "the best score per row in green."
                ),
            },
            {
                'label': 'Cross-reference vs industry benchmark + past contracts',
                'text': (
                    "Now cross-reference each vendor's pricing against "
                    "PRC_Industry_Benchmark.xlsx (tab: Last_24_Months) and against "
                    "PRC_Past_Contracts.xlsx (tab: Similar_Scope). For each vendor, "
                    "produce: Headline Price vs Industry Median % (±deviation), Headline "
                    "Price vs Past Contracts %, and a 1-line verdict (Aggressive / Market / "
                    "Premium / Outlier). Mark Outlier with Red — these need extra scrutiny. "
                    "Cite the benchmark source for every claim."
                ),
            },
            {
                'label': 'Generate Scoring Matrix + Recommendation',
                'text': (
                    "Build a weighted Scoring Matrix combining Steps 1 + 2: Capability 30%, "
                    "Price 30%, Track Record 15%, Risk 15%, Local Content 5%, ESG 5%. "
                    "Compute the weighted score per vendor. Rank highest to lowest. Produce "
                    "a 1-paragraph recommendation: which vendor to award, why, and what "
                    "specific terms (price adjustment / SLA tightening / risk mitigation "
                    "clause) the Procurement officer should secure before signing. Highlight "
                    "any vendor that scores top-2 but has an Outlier price tag from Step 2 — "
                    "those need price renegotiation."
                ),
            },
            {
                'label': 'Draft IC paper + recommendation memo + commercial response',
                'text': (
                    "Now do all 4 in one Cowork run: "
                    "1) Draft a 3-page IC (Investment Committee) Paper in Word, addressed to "
                    "the Procurement Committee. Sections: Executive Summary, RFP Background, "
                    "Vendor Comparison (insert Step 1 table), Benchmark Position (insert "
                    "Step 2 table), Scoring Matrix (insert Step 3 table), Recommendation, "
                    "Risks + Mitigations. Tone: committee-formal. "
                    "2) Build a 6-slide PowerPoint summary for the Procurement Committee "
                    "meeting — Slide 1 cover, Slides 2-3 vendor comparison + benchmark, "
                    "Slide 4 scoring + ranking, Slide 5 recommendation, Slide 6 risks + "
                    "mitigations. "
                    "3) Draft an Outlook email to the Procurement Committee with both "
                    "attached, requesting endorsement at the next meeting. "
                    "4) Draft a Commercial Response in Word to the recommended vendor, "
                    "opening the negotiation with the specific terms identified in Step 3 "
                    "(price adjustment / SLA / risk mitigation). DRAFT only — do not send."
                ),
            },
            {
                'label': 'Schedule vendor presentation Teams session + IC review',
                'text': (
                    "Now schedule 2 meetings: "
                    "(a) Teams session 'Vendor Best-and-Final Presentation — [VENDOR]' for "
                    "[DATE+5 business days at 2pm], 90 min, with the recommended vendor, "
                    "the Procurement officer, the technical lead and the Head of "
                    "Procurement. Attach the IC paper as pre-read. "
                    "(b) Teams session 'Procurement Committee Review' for [DATE+10 business "
                    "days at 10am], 60 min, with the full IC. Attach the IC paper + deck + "
                    "vendor's post-presentation revised quotation."
                ),
            },
        ],
        'watch': (
            "Outlier pricing must be explained — either an aggressive market entry by the "
            "vendor or a misunderstanding of scope. The cross-reference vs past contracts "
            "is what catches 'lowball-then-reprice' tactics."
        ),
        'honest': (
            "Weighted scoring is a decision aid, not a decision. The Procurement Committee "
            "must apply judgment on strategic vendor dependency, geographic concentration "
            "and prior dispute history."
        ),
        'html_archetype': 'heatmap',
        'html_brief': (
            "Vendor Scoring Heatmap — vendors (rows) × scoring dimensions (Capability, "
            "Price, Track Record, Risk, Local Content, ESG) with Red/Amber/Green cells. "
            "Top of the heatmap shows the weighted total score per vendor as horizontal "
            "bars. Click a cell to drawer-open the underlying RFP response excerpt + "
            "benchmark comparison."
        ),
    },

    # ────────────────────────────────────────────────────────────────────
    {
        'slug': 'reg-internal-audit-pack',
        'title': 'Internal Audit Pack & Findings Tracker',
        'business_group': 'Office of Internal Audit',
        'apps': ['Researcher', 'Excel', 'Word', 'PowerPoint', 'Outlook', 'Planner'],
        'complexity': 'Advanced',
        'files': [
            'AUD_Working_Papers.xlsx',
            'AUD_Risk_Universe.xlsx',
            'AUD_Auditee_Walkthrough.docx',
            'AUD_Findings_Tracker.xlsx',
        ],
        'steps': [
            {
                'label': 'Aggregate working papers + risk-rate findings',
                'text': (
                    "I am a Group Internal Audit officer wrapping up the audit of [BG / "
                    "Process]. I have working papers in AUD_Working_Papers.xlsx "
                    "(tabs: Testing_Sample, Exceptions, Management_Letter_Points) and the "
                    "auditee walkthrough notes in AUD_Auditee_Walkthrough.docx. "
                    "Aggregate all findings into a single Findings Table with columns: "
                    "Finding #, Description (1 line), Root Cause Category (Control "
                    "Deficiency / Policy Gap / Operational / Technology / People), "
                    "Affected BG, Severity (Critical / High / Medium / Low) per "
                    "AUD_Risk_Universe.xlsx severity rubric, Recommended Action (1 line). "
                    "Sort by Severity descending."
                ),
            },
            {
                'label': 'Cross-reference vs Risk Universe',
                'text': (
                    "Cross-reference each finding from Step 1 against AUD_Risk_Universe.xlsx "
                    "(tab: Top_Risks). For each finding, identify which Top Risk(s) it "
                    "pertains to, and whether the residual risk rating should be revised "
                    "upward, downward, or held. Produce a side panel summarising the impact "
                    "of this audit on the overall Risk Universe (which Top Risks are now "
                    "Red, Amber or Green)."
                ),
            },
            {
                'label': 'Draft management letter + agree response',
                'text': (
                    "Draft the Audit Management Letter in Word, addressed to the Head of "
                    "[BG / Process]. Sections: Scope, Approach, Findings Table (insert Step "
                    "1 table — Critical & High only in body; Medium & Low in appendix), "
                    "Risk Universe Impact (Step 2 summary), Management Response section "
                    "(blank rows for auditee to fill, with a 1-line prompt for each "
                    "finding). Tone: audit-formal. Send DRAFT to the auditee for response "
                    "before finalising."
                ),
            },
            {
                'label': 'Build Audit Committee deck + send to AC Chair',
                'text': (
                    "Now do all 3 in one Cowork run: "
                    "1) Build a 10-slide PowerPoint deck for the next Audit Committee — "
                    "Slide 1 cover, Slide 2 scope + approach, Slide 3 headline verdict, "
                    "Slides 4-6 Critical & High findings (one slide per finding with "
                    "root-cause + recommended action + management response), Slide 7 Risk "
                    "Universe impact, Slide 8 thematic observations across audits, Slide 9 "
                    "audit-plan progress vs annual plan, Slide 10 management asks. Use the "
                    "Group corporate template. "
                    "2) Draft an Outlook email to the AC Chair with the deck + management "
                    "letter attached, asking for any pre-meeting questions before the "
                    "scheduled AC. "
                    "3) Schedule a 15-min Teams pre-meeting with the AC Chair for [DATE+2 "
                    "business days at 9am] to walk through the headline verdict."
                ),
            },
            {
                'label': 'Update Findings Tracker + Planner actions for auditee',
                'text': (
                    "Update AUD_Findings_Tracker.xlsx with all findings from Step 1 "
                    "(Status: Open, Severity, Owner = Head of [BG/Process], Target Close "
                    "Date = 90 days for Critical / 180 days for High / Next-Cycle for "
                    "Medium & Low). Then create Planner tasks (one per Critical & High "
                    "finding) assigned to the auditee owner with the Target Close Date as "
                    "the Planner due date and a link back to the finding row in the tracker."
                ),
            },
        ],
        'watch': (
            "Root cause categorisation drives the recommendation; never let a finding sit "
            "as 'control deficiency' if the underlying issue is 'policy gap' or 'technology "
            "limit' — the remediation is different."
        ),
        'honest': (
            "Severity rating is rubric-based but judgment-driven. Critical findings need "
            "the Head of Internal Audit's sign-off before the management letter goes out — "
            "this runbook drafts; it does not approve."
        ),
        'html_archetype': 'dashboard',
        'html_brief': (
            "Audit Findings Dashboard — header KPI tiles (Total Findings, Critical Open, "
            "Median Days to Close, Audits Completed YTD), middle Findings Table sortable "
            "by Severity / BG / Status, side panel Risk Universe Impact with Red/Amber/"
            "Green Top Risks. Filterable by BG / Audit Cycle / Owner."
        ),
    },
]


# ── Routing ──────────────────────────────────────────────────────────────
# Primary target: regulator UCs land on financial-regulator (existing industry entry)
# Department-specific UCs land on their natural dept entry as primary instead.

PRIMARY_ROUTING = {
    'reg-ipo-prospectus-compliance':   'financial-regulator',
    'reg-complaint-triage':            'financial-regulator',
    'reg-workforce-scenario':          'dept-hr',
    'reg-investor-education-audit':    'dept-marketing',
    'reg-contract-review':             'dept-legal',
    'reg-tax-application':             'financial-regulator',
    'reg-policy-paper':                'financial-regulator',
    'reg-procurement-benchmarking':    'dept-procurement',
    'reg-internal-audit-pack':         'dept-corpsec',
}

# Secondary spill — each UC also lands on a relevant peer entry
SECONDARY_ROUTING = {
    'reg-ipo-prospectus-compliance':   'investment-banking',
    'reg-complaint-triage':            'dept-legal',
    'reg-workforce-scenario':          'diversified-conglomerate',
    'reg-investor-education-audit':    'dept-investor-relations',
    'reg-contract-review':             'dept-procurement',
    'reg-tax-application':             'dept-finance',
    'reg-policy-paper':                'dept-strategy',
    'reg-procurement-benchmarking':    'dept-finance',
    'reg-internal-audit-pack':         'dept-risk',
}


# ── Helpers ──────────────────────────────────────────────────────────────
def _is_cowork(name: str) -> bool:
    return 'Cowork' in (name or '')


def _find_cowork_block(entry: dict):
    for tb in entry.get('prompts') or []:
        if _is_cowork(tb.get('tool', '')):
            return tb
    return None


def _html_artifact_prompt(uc_title: str, archetype: str, brief: str,
                          context_files: list, step_label: str) -> dict:
    archetype_label = {
        'dashboard': 'interactive HTML dashboard',
        'kanban':    'interactive HTML kanban board',
        'heatmap':   'interactive HTML heatmap grid',
        'pipeline':  'interactive HTML pipeline timeline',
    }.get(archetype, 'interactive HTML artifact')

    files_clause = ''
    if context_files:
        flist = ', '.join(context_files[:6])
        files_clause = f' Use the data from the attached files: {flist}.'

    instr = (f"**Cowork Runbook · {uc_title} · {step_label}** "
             f"({archetype.title()}). Pattern: Model → Interactive App. "
             f"Apps: Cowork · Word · Outlook · Teams · Tracker. "
             f"Produces a **{archetype_label}** plus 4 parallel side-deliverables. "
             f"**Honest framing:** The HTML is for executive review and demo; for "
             f"production use, hand the data over to your BI team.")

    safe_name = uc_title.replace(' ', '_').replace('/', '_')
    prompt = (
        f"Building on the {uc_title} runbook output above, now produce a "
        f"**SELF-CONTAINED interactive HTML** artifact for executive review.{files_clause}\n\n"
        f"The HTML must be a single .html file with inline CSS and inline JavaScript "
        f"— NO external CDN, NO external image, NO web fonts. It must open and "
        f"function fully offline. Use the Group corporate aesthetic (slate text, "
        f"off-white background, brand accent colour).\n\n"
        f"**The {archetype_label} should be:** {brief}\n\n"
        f"In parallel, also do all of these in one Cowork run:\n"
        f"1) Save the HTML as '{safe_name}.html' to /Cowork/Artifacts/[YYYY-MM]/.\n"
        f"2) Draft a 1-page Word memo summarising what the HTML shows, the top-3 "
        f"insights an executive should read first, and the recommended next step.\n"
        f"3) Draft an Outlook email to the executive sponsor with the HTML attached, "
        f"a 4-bullet TL;DR in the body, and a request to confirm by [DATE].\n"
        f"4) Schedule a 30-minute Teams review meeting for [DATE+2 business days] "
        f"with the sponsor + 2 named deputies; include the HTML link in the invite.\n"
        f"5) Update the case tracker workbook with a new row: date, UC, artifact link, "
        f"owner, review status (Pending), and target close date."
    )
    return {'instr': instr, 'prompt': prompt}


def _format_uc_prompts(uc: dict):
    """Turn a UC into a list of {'instr', 'prompt'} dicts including the HTML step."""
    base_steps = uc['steps']
    total = len(base_steps) + 1  # +1 HTML artifact
    out = []
    for i, step in enumerate(base_steps):
        step_label = f"Step {i+1} of {total}"
        instr = (f"**Cowork Runbook · {uc['title']} · {step_label}** "
                 f"({step['label']}). Pattern: Multi-step Operational Workflow. "
                 f"Business Group: {uc.get('business_group', '')}. "
                 f"Apps: {' · '.join(uc.get('apps', []) or [])}. "
                 f"Complexity: {uc.get('complexity', '')}.")
        if i == 0 and uc.get('files'):
            flist = ', '.join(uc['files'][:6])
            instr += f" Sample source files (attach via 📎 Knowledge): {flist}."
        if i == 0 and uc.get('watch'):
            instr += f" **What to watch:** {uc['watch']}"
        if i == len(base_steps) - 1 and uc.get('honest'):
            instr += f" **Honest framing:** {uc['honest']}"
        out.append({'instr': instr, 'prompt': step['text']})

    # Append the HTML artifact step
    html_step_label = f"Step {total} of {total}"
    out.append(_html_artifact_prompt(
        uc['title'],
        uc.get('html_archetype', 'dashboard'),
        uc.get('html_brief', f"Executive dashboard for {uc['title']}."),
        uc.get('files', []),
        html_step_label,
    ))
    return out


def _append_to_cowork(entry, new_prompts):
    tb = _find_cowork_block(entry)
    if not tb:
        return 0
    existing = tb.get('prompts') or []
    existing_starts = {(p.get('prompt') or '')[:60] for p in existing if isinstance(p, dict)}
    to_add = [p for p in new_prompts if (p['prompt'][:60] not in existing_starts)]
    if not to_add:
        return 0
    tb['prompts'] = list(existing) + to_add
    existing_id = tb.get('promptsID') or []
    tb['promptsID'] = list(existing_id) + [dict(p) for p in to_add]
    return len(to_add)


def _augment_files(entry, file_list):
    if not file_list:
        return 0
    cur = entry.get('files') or []
    cur_set = set(cur)
    added = 0
    for f in file_list:
        f = f.strip()
        if not f or f in cur_set:
            continue
        cur.append(f)
        cur_set.add(f)
        added += 1
    if added:
        entry['files'] = cur
    return added


# ── Main API ─────────────────────────────────────────────────────────────
def inject_regulator_runbook(all_entries):
    """Inject all 9 use cases into their primary + secondary target entries.
    Returns dict {entries, prompts, files}."""
    by_id = {e.get('id'): e for e in all_entries if e.get('id')}

    touched = set()
    n_prompts = 0
    n_files = 0

    for uc in REGULATOR_USE_CASES:
        prompts = _format_uc_prompts(uc)
        files = uc.get('files', [])

        # Primary
        primary_eid = PRIMARY_ROUTING.get(uc['slug'])
        if primary_eid:
            primary = by_id.get(primary_eid)
            if primary:
                n_prompts += _append_to_cowork(primary, prompts)
                n_files += _augment_files(primary, files)
                touched.add(primary_eid)

        # Secondary spill
        sec_eid = SECONDARY_ROUTING.get(uc['slug'])
        if sec_eid and sec_eid != primary_eid:
            sec = by_id.get(sec_eid)
            if sec:
                n_prompts += _append_to_cowork(sec, prompts)
                n_files += _augment_files(sec, files)
                touched.add(sec_eid)

    return {'entries': len(touched), 'prompts': n_prompts, 'files': n_files}


def get_all_sample_files():
    """Return flat list of all sample file names referenced by UCs."""
    out = []
    for uc in REGULATOR_USE_CASES:
        out.extend(uc.get('files', []))
    return sorted(set(out))
