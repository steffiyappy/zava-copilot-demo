# -*- coding: utf-8 -*-
"""Customer-source Cowork use cases merged from steffiyappy.github.io
KIBB / KLK / Aster immersion pages. Each card distils one headline
multi-step Cowork demo from the original customer site into the
Universal card schema."""

CARDS = {}

# ── KIBB :: Board Risk Committee Pre-Read Pack ────────────────────────────
CARDS['uc-ib-brc-prep'] = {
    'title': 'Board Risk Committee Pre-Read Pack',
    'dept_tag': 'Risk & Compliance',
    'industry_tag': 'Investment Banking',
    'complexity': 'advanced',
    'apps': ['Excel', 'Word', 'Outlook', 'Teams', 'Researcher'],
    'desc': 'One Cowork delegation that analyses segment P&L + vendor contract + BRC transcript + outsourcing policy, drafts the BRC pre-brief, writes the CFO covering email, and proposes 3 calendar slots — pausing for approval before sending.',
    'skills': [
        'Multi-source cross-reference (segment P&L × vendor clauses × prior BRC actions × policy pillars)',
        'RAG heat map construction from policy thresholds (10% MATERIAL / 5% CRITICAL)',
        'Approval-gated communication (Cowork pauses before sending email + calendar invite)',
    ],
    'instructions': [
        'Open Microsoft 365 Copilot Cowork (Frontier required)',
        'Click 📎 Knowledge → attach IB_07 Segment P&L, IB_08 Vendor Contract, IB_09 BRC Transcript, IB_10 Outsourcing Policy',
        'Paste the 4-step prompt as ONE single message',
        'Review the plan Cowork proposes — approve each step before it sends the email or proposes calendar slots',
    ],
    'sample_files': [
        ('IB_07_Segment_PnL.xlsx', 'xlsx'),
        ('IB_08_Vendor_Contract.docx', 'docx'),
        ('IB_09_BoardRisk_Transcript.docx', 'docx'),
        ('IB_10_Outsourcing_Policy.docx', 'docx'),
    ],
    'prompts': [{
        'label': 'BRC pre-brief 4-step fan-out',
        'text': (
            "Cowork: The Board Risk Committee meets in 5 working days and I need the pre-brief pack ready 48 hours before. "
            "Use `/` to reference /IB_07_Segment_PnL.xlsx, /IB_08_Vendor_Contract.docx, "
            "/IB_09_BoardRisk_Transcript.docx and /IB_10_Outsourcing_Policy.docx, and complete all four steps below "
            "in one delegation.\n\n"
            "STEP 1 — Analyse the inputs: from /IB_07 (Monthly_PnL + Segment_Revenue + Segment_KPIs tabs) rank every "
            "segment by Q1 contribution margin against the 10% MATERIAL / 5% CRITICAL thresholds in /IB_10; "
            "cross-reference every vendor-related clause in /IB_08 against the 7 outsourcing governance pillars in /IB_10 "
            "and Red/Amber/Green rate each; reconcile this against the open items raised in /IB_09 to find duplicates "
            "and orphans. Produce a single 1-page RAG snapshot the BRC chair can read in 90 seconds.\n\n"
            "STEP 2 — Draft the Word memo: write a 3-page BRC pre-brief titled 'Q3 Segment Performance + Vendor "
            "Governance Briefing' structured as Executive Summary (3 bullets), Segment Performance Heat Map (RAG table "
            "by segment + Q1 contribution margin), Vendor Governance Gaps (table of clause + policy section + RAG + "
            "60-day remediation owner), BRC Open-Items Tracker Update (Closed / In-Flight / Open with owner + due date), "
            "Decision Asks (3 binary decisions the BRC must take), and an appendix of director Q&A.\n\n"
            "STEP 3 — Draft the email from the Group CFO to the BRC Chair (Will, Head of Risk; cc Hadar, Group CFO and "
            "the Head of Internal Audit) attaching the memo, summarising the 3 binary decisions, and anticipating the 2 "
            "questions the Chair is most likely to push back on with a proposed response for each.\n\n"
            "STEP 4 — Find a 75-minute calendar slot in the 48 hours leading up to the BRC where Will (Head of Risk), "
            "Hadar (Group CFO), Sasha (Group Chief of Staff) and the Head of Internal Audit are all free in MYT business "
            "hours, and propose three candidate slots ranked best-to-worst with one-line rationale per slot.\n\n"
            "Show me the full plan first and pause for my approval before sending the email or sending the calendar invite."
        )
    }],
    'expected': [
        '1-page RAG snapshot (segments × vendor clauses × open items)',
        '3-page BRC pre-brief memo (Word)',
        'CFO covering email draft to BRC Chair + cc list',
        '3 candidate 75-min calendar slots, ranked',
        'Director Q&A bank appended to the memo',
    ],
    'watch': [
        'Every red / amber rating cites the underlying policy clause inline',
        'Cowork PAUSES before sending the email — it shows the draft + recipient list for approval',
        'Calendar slot picker checks 4 attendees\' free/busy across MYT business hours',
    ],
    'honest': 'Researcher-grade synthesis but the CFO must hand-review every red rating before forwarding — BRC papers are legal record. The email and calendar invite must be approved explicitly; Cowork will not send either without your green light.',
    'tips': [
        'Swap Q3 for whichever quarter you are presenting — the structure works identically',
        'For an audit-committee variant, replace /IB_10 Outsourcing Policy with the Group Internal Audit charter',
        'Add a STEP 5: post a 2-line summary to the BRC Teams channel after the email is sent',
    ],
}

# ── KLK :: Q1 Group Operations Review — 6-Deliverable Parallel ───────────
CARDS['uc-klk-q1-ops-review'] = {
    'title': 'Q1 Group Operations Review — 6-Deliverable Parallel',
    'dept_tag': 'Strategy & Operations',
    'industry_tag': 'Conglomerate',
    'complexity': 'advanced',
    'apps': ['Word', 'Excel', 'PowerPoint', 'Outlook', 'Teams', 'Researcher'],
    'desc': 'The Quarterly Board Operations Review is Friday — one Cowork delegation reads the Q1 Group Operations Report and fans out 6 board-grade deliverables: executive summary, variance workbook, board deck, Chair email, exec WhatsApp summary, 90-minute calendar block.',
    'skills': [
        'Single-source fan-out across 6 deliverable types in parallel',
        'Voice-shifting from board-grade prose (Word) to 2-line WhatsApp summary (Teams)',
        'Cross-deliverable consistency: same KPIs cited identically in Word memo, Excel, PPT, email, and Teams',
    ],
    'instructions': [
        'Open Microsoft 365 Copilot Cowork (Frontier required)',
        'Click 📎 Knowledge → attach the Q1 Group Operations Report (and the prior-quarter pack for comparison)',
        'Paste the 6-task prompt as ONE single message',
        'Cowork plans first, then executes each task — review every deliverable before forwarding',
    ],
    'sample_files': [
        ('KLK_Q1_Group_Operations_Report.xlsx', 'xlsx'),
        ('KLK_Q1_Prior_Quarter_Pack.docx', 'docx'),
        ('KLK_Board_Audit_Cmte_Minutes.docx', 'docx'),
    ],
    'prompts': [{
        'label': 'Q1 Group Ops Review fan-out',
        'text': (
            "I am Siew Ling, Group COO at Zava Conglomerate. The Quarterly Board Operations Review is on Friday. Using "
            "the attached Q1 Group Operations Report as the source of truth, prepare these SIX deliverables in parallel:\n\n"
            "1. WORD — 'Q1 2026 Operations Executive Summary' — one page, board-grade. Structure: Headline (3 lines), "
            "Top 5 KPIs vs target with RAG, 3 recovery levers we are pulling, 3 open decisions the Board must take. "
            "Tone: confident, factual, no jargon.\n\n"
            "2. EXCEL — 'Q1 Variance Workbook' with 3 sheets. Sheet 1 = group-level revenue / EBITDA / OEE vs target "
            "with %% delta. Sheet 2 = same metrics drilled by division. Sheet 3 = 'Watch List' — every metric breaching "
            "5%% adverse variance, with proposed owner + 30-day action.\n\n"
            "3. POWERPOINT — 12-slide Board Operations Review deck. Slide 1 cover. Slides 2-3 group KPIs. Slides 4-7 "
            "division-by-division drilldown. Slide 8 recovery levers. Slide 9 risks. Slide 10 decisions for the Board. "
            "Slides 11-12 appendix.\n\n"
            "4. OUTLOOK — confidential email from the Group COO to the Board Chair attaching the 3 documents above, "
            "with a 4-bullet executive summary in the body anticipating the 3 questions the Chair is most likely to ask.\n\n"
            "5. TEAMS — 2-line summary I can paste into the Board WhatsApp-equivalent channel — first line = headline "
            "delta, second line = the one decision the Board must take.\n\n"
            "6. CALENDAR — block 90 minutes on Friday morning titled 'Board Operations Review — Q1 2026' with the "
            "Board Chair, Group CEO, Group CFO, Group CoS and all division MDs.\n\n"
            "Cite the source file and tab for every figure. Show me the plan first and pause for my approval before "
            "sending the email or sending the calendar invite."
        )
    }],
    'expected': [
        '1-page Executive Summary (Word)',
        '3-sheet Variance Workbook (Excel)',
        '12-slide Board Operations Review deck (PowerPoint)',
        'CFO covering email draft to Board Chair (Outlook)',
        '2-line Teams summary for Board chat',
        '90-min Friday calendar block, all attendees verified free',
    ],
    'watch': [
        'Same KPI figure appears identically across all 6 deliverables — no drift',
        'Voice shifts from formal Word memo to terse 2-line Teams blast — same data',
        'Cowork pauses before sending the email AND before scheduling the calendar invite',
    ],
    'honest': 'Cowork drafts everything. The Group COO must hand-review the deck before forwarding — board papers are legal record. The Teams message must be cleared by Group Comms before going live. Approve each external communication explicitly before Cowork sends.',
    'tips': [
        'Swap Q1 for whichever quarter is current — the structure works identically across the year',
        'For monthly reviews, drop the PowerPoint and email tasks — keep Word + Excel + Teams summary',
        'Add a 7th task: prep a 90-second voice memo for the Chair\'s morning commute',
    ],
}

# ── Aster :: ESG Committee Full Reporting Workflow ─────────────────────────
CARDS['uc-aster-esg-workflow'] = {
    'title': 'ESG Committee Full Reporting Workflow',
    'dept_tag': 'Sustainability',
    'industry_tag': 'Chemicals & Energy',
    'complexity': 'intermediate',
    'apps': ['Excel', 'Word', 'PowerPoint', 'Outlook', 'Teams'],
    'desc': 'The headline Aster Cowork demo — one prompt that reads ESG performance data from Excel, drafts the Committee Pack Word memo, builds the committee deck, drafts the Committee Chair email, and schedules the meeting. Cowork pauses before sending the email and creating the invite.',
    'skills': [
        'ESG metric synthesis across Scope 1 / 2 / 3 with materiality framing',
        'Audience switching — board-grade Word memo to skim-friendly 8-slide deck',
        'Pause-before-action choreography — review draft email + draft invite before they send',
    ],
    'instructions': [
        'Open Microsoft 365 Copilot Cowork (Frontier required)',
        'Click 📎 Knowledge → attach the ESG Performance workbook (12-month log) and the prior-quarter Committee pack',
        'Paste the 5-task prompt as ONE single message',
        'Cowork will plan first — review the plan, then approve each step. It will pause before sending the email and scheduling the invite.',
    ],
    'sample_files': [
        ('OGD_06_ESG_Performance.xlsx', 'xlsx'),
        ('OGD_07_Prior_Quarter_ESG_Pack.docx', 'docx'),
        ('OGD_08_Materiality_Assessment.docx', 'docx'),
    ],
    'prompts': [{
        'label': 'ESG Committee fan-out',
        'text': (
            "Cowork: The ESG Committee meets in 10 working days. Using `/` to reference /OGD_06_ESG_Performance.xlsx, "
            "/OGD_07_Prior_Quarter_ESG_Pack.docx and /OGD_08_Materiality_Assessment.docx, please complete the FIVE steps "
            "below in one delegation.\n\n"
            "STEP 1 — Excel analysis: from /OGD_06 (12-month log of Scope 1/2/3 emissions, water withdrawal, hazardous "
            "waste, lost-time incidents, community grievances) build a 1-sheet 'Committee Snapshot' tab. Columns: KPI, "
            "Current Quarter, Prior Quarter, YoY %%, Materiality Tag (from /OGD_08), RAG vs Group target. Highlight any "
            "KPI breaching its materiality threshold.\n\n"
            "STEP 2 — Word pack: draft a 4-page 'ESG Committee Pack — Q[N] FY26' document. Structure: Executive "
            "Summary (3 bullets), Quarter-on-quarter KPI Trend Table (from STEP 1), Material Issues Update (top 3 "
            "issues from /OGD_08 with status), Regulatory / Disclosure Watch (Bursa SR, IFRS S1/S2, GRI, CDP), and "
            "Decisions Required (2-3 binary decisions for the Committee).\n\n"
            "STEP 3 — PowerPoint: 8-slide ESG Committee deck. Slide 1 cover. Slide 2 KPI snapshot. Slides 3-5 material "
            "issues drilldown. Slide 6 disclosure roadmap. Slide 7 decisions. Slide 8 appendix.\n\n"
            "STEP 4 — Outlook email from the Group Sustainability Director to the ESG Committee Chair (cc Group CFO and "
            "Group CoS) attaching the 3 deliverables, with a 4-bullet body anticipating the 2 questions the Chair will "
            "ask hardest. Pause before sending.\n\n"
            "STEP 5 — Calendar invite: schedule a 60-minute ESG Committee meeting at a slot in the next 10 working days "
            "when the Chair, Group CFO, Group Sustainability Director, and 3 INED members are all free. Propose 3 candidate "
            "slots ranked best-to-worst. Pause before sending the invite.\n\n"
            "Show me the full plan first. Cite source tab/section for every figure. Flag any KPI with no source data as "
            "[VERIFY] so the Sustainability Manager can manually sign off."
        )
    }],
    'expected': [
        '1-sheet Committee Snapshot tab (Excel)',
        '4-page ESG Committee Pack (Word)',
        '8-slide ESG Committee deck (PowerPoint)',
        'Draft email from Sustainability Director to Committee Chair (Outlook)',
        '60-min calendar invite candidates, ranked',
    ],
    'watch': [
        'Every KPI cell is cited back to the Excel tab + row — auditable',
        '[VERIFY] tags clearly mark anything without a source for manual sign-off',
        'Cowork PAUSES before the email and before the calendar invite — you approve both explicitly',
    ],
    'honest': 'Cowork drafts. The Sustainability Manager must verify every figure before Board submission — ESG disclosures carry SC/Bursa penalty exposure under IFRS S1/S2 and the Group SR framework. Approve the email and invite explicitly. Do not let Cowork send anything without your green light.',
    'tips': [
        'Run this monthly with /OGD_06 refreshed — same structure, smaller scope',
        'Swap /OGD_08 Materiality Assessment for /OGD_09 Climate Risk Register to flip the lens to TCFD/IFRS S2',
        'Add a 6th step: draft a 1-page external press note for sustainability@zavaeng.com to be ready post-Committee',
    ],
}
