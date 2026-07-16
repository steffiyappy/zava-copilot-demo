# -*- coding: utf-8 -*-
"""
Scout Library catalog — Contoso C-Suite Immersion format MERGED with
Microsoft Scout Frontier-preview desktop AI use-case cards.

Each card carries:
- title, dept_tag, industry_tag (optional), complexity
- apps[]            — Apps Involved badges (Word/Excel/PowerPoint/Browser/WorkIQ)
- desc              — 1-2 line description
- skills[]          — what is being demonstrated (the user asked for "skills")
- instructions[]    — step-by-step setup (where to click, what to attach)
- sample_files[]    — list of (filename, ext) tuples (pdf/xlsx/docx/png)
- prompts[]         — list of {label, text}; supports multi-step P1/P2/etc
- expected[]        — Expected Outcome bullets
- watch[]           — WHAT TO WATCH bullets (green callout)
- honest            — HONEST FRAMING paragraph (amber callout)
- tips[]            — Tips & Variations bullets

The catalog is consumed by build_master.py via get_scout_library_for_entry(entry_id).
"""

# ───────────────────────────────────────────────────────────────────────
# Use case catalog
# ───────────────────────────────────────────────────────────────────────

USE_CASES = {}

USE_CASES['uc-scout-heartbeat'] = {
    'title': 'Heartbeat — Daily Group Briefing & Risk Sweep',
    'dept_tag': 'Risk',
    'complexity': 'advanced',
    'apps': ['WorkIQ', 'Teams', 'OneDrive', 'Shell'],
    'desc': 'Run Scout heartbeat every 30 minutes to scan M365 risk signals, update a workspace brief, and post a safe Teams update.',
    'skills': [
        'Heartbeat mode with work-days and work-hours configuration',
        'WorkIQ cross-service sweep across email, Teams, calendar, and OneDrive',
        'Workspace file write-back plus Teams posting under restrictive permissions',
    ],
    'instructions': [
        'Open Microsoft Scout desktop app → Heartbeat panel → toggle Heartbeat on',
        'Set interval to 30 min, work days Monday-Friday, work hours 08:30-18:30 Malaysia time',
        'Set permissions: M365 read-only, Teams post allowed only to the nominated channel, outbound email denied',
        'Create or select workspace folder Scout_Group_Briefing and paste the prompt below',
    ],
    'sample_files': [
        ('Scout_Group_Risk_Register.xlsx', 'xlsx'),
        ('Group_ExCo_Watchlist.docx', 'docx'),
        ('Heartbeat_Log_Template.md', 'md'),
    ],
    'prompts': [{
        'label': 'Configure the recurring heartbeat',
        'text': (
            "Heartbeat task for Hadar. Every 30 minutes, use WorkIQ and m365_* read tools to scan email, Teams, calendar, and OneDrive for high-risk ExCo, regulator, customer, liquidity, cyber, legal, or MYR/IDR exposure items above MYR 5m or IDR 20bn.\n"
            "Write an append-only update to ./Scout_Group_Briefing/Daily_Risk_Sweep.md with timestamp, source links, risk rating, owner, and suggested next step. If any item is RED, draft a generic Teams channel post for #group-risk-watch that says only the category, owner, and link to the workspace file. Do not send email. Do not expose private customer data in Teams. Skip any action that requires prompt approval."
        )
    }],
    'expected': [
        'Daily_Risk_Sweep.md updated every heartbeat cycle with auditable source links',
        'Red-risk Teams post draft or post in the approved channel only',
        'Heartbeat activity log showing skipped actions where permissions were too broad',
    ],
    'watch': [
        'Scout runs in the background without a chat prompt — regular Copilot Chat cannot do this',
        'WorkIQ connects email + Teams + documents instead of relying on one uploaded file',
    ],
    'honest': 'Heartbeat is a monitoring assistant, not an incident commander. It can miss nuance, so Hadar or Sasha still owns escalation. Keep outbound email denied until Legal and Comms approve the operating model.',
    'tips': [
        'Use a 15-minute interval for crisis war rooms and 2-hour interval for BAU risk sweeps',
        'Add a deny-list for M&A, HR investigation, and named sensitive folders',
    ],
}

USE_CASES['uc-scout-bulk-files'] = {
    'title': 'Bulk File-System Processing — 200 Contracts in One Run',
    'dept_tag': 'Legal',
    'complexity': 'advanced',
    'apps': ['Word', 'Excel', 'PowerPoint', 'File System'],
    'desc': 'Point Scout at a OneDrive workspace containing 200 contracts, extract obligations into a master workbook, create one-page Word summaries, and build a counterparty tiering deck.',
    'skills': [
        'File-system read/write/search across a workspace folder tree',
        'Word, Excel, and PowerPoint skills in one desktop run',
        'Shell command inventory for filenames, page counts, duplicate detection, and CSV validation',
    ],
    'instructions': [
        'Sync the contract room to a local OneDrive workspace folder and open that folder in Scout',
        'Set file system access to allow the workspace only; shell prompt-mode for commands that write files',
        'Attach the counterparty register and folder index, then paste the prompt',
        'Review exception rows before sending summaries to Legal or Procurement',
    ],
    'sample_files': [
        ('Contracts_Folder_Index.csv', 'csv'),
        ('Group_Counterparty_Master.xlsx', 'xlsx'),
        ('Contract_Tiering_Template.pptx', 'pptx'),
        ('Sample_Supply_Agreement_MY_2026.docx', 'docx'),
    ],
    'prompts': [{
        'label': 'Process the contract room',
        'text': (
            "In this Scout workspace, browser access is not needed. Use file-system search and safe shell commands to inventory ./Contracts_200_Run. For each DOCX or PDF contract, extract counterparty, entity, country, MYR or IDR value, expiry date, auto-renewal clause, termination notice, data/privacy clause, anti-bribery clause, and unusual obligations.\n"
            "Create ./outputs/Group_Contract_Master.xlsx with one row per contract and an Exceptions tab. Create a one-page Word summary per contract under ./outputs/summaries using the naming pattern Summary_[counterparty]_[expiry].docx. Then build ./outputs/Contract_Tiering_ExCo.pptx with Tier 1/Tier 2/Tier 3 segmentation, top 20 expiry risks, and Sasha's recommended approval queue. Cite source file and page for each extracted fact."
        )
    }],
    'expected': [
        'Master xlsx with 200 rows, exceptions tab, formulas, filters, and risk tiers',
        'One-page Word summary per contract in the workspace output folder',
        'PowerPoint tiering deck for ExCo or Procurement Council',
    ],
    'watch': [
        'Scout reads and writes hundreds of local workspace files, not just attached documents',
        'Shell commands accelerate inventory and QA while permission tiers control writes',
    ],
    'honest': 'Contract extraction is a first-pass workbench; Legal must verify key clauses and scanned-PDF OCR quality.',
    'tips': [
        'Swap contracts for leases, supplier MSAs, bancassurance agreements, or hospital panel contracts',
        'Add a shell validation step to compare workbook row count against the source folder count',
    ],
}

USE_CASES['uc-scout-browser-portal'] = {
    'title': 'Browser Automation — Regulator Portal Sweep',
    'dept_tag': 'Corporate Secretarial',
    'complexity': 'intermediate',
    'apps': ['Browser', 'Word', 'WorkIQ', 'OneDrive'],
    'desc': 'Use Scout Playwright browser control to download regulator circulars and assemble a board-ready brief.',
    'skills': [
        'Playwright browser navigate, click, fill, download, and screenshot actions',
        'Prompt-mode browser permissions with deny-list for internal portals',
        'Word brief generation with source URLs, screenshots, and regulator citations',
    ],
    'instructions': [
        'Open Scout → Settings → Permissions → Browser Control: Prompt; deny-list internal finance, HR, and production admin portals',
        'Create workspace folder Regulator_Portal_Sweep_2026',
        'Use a public regulator source such as BNM, OJK, Bursa Malaysia, MAS, or SC Malaysia',
        'Paste the prompt and approve only public-site navigation and downloads',
    ],
    'sample_files': [
        ('BNM_Circulars_2026.pdf', 'pdf'),
        ('OJK_Regulatory_Watchlist.xlsx', 'xlsx'),
        ('Regulator_Brief_Template.docx', 'docx'),
    ],
    'prompts': [{
        'label': 'Sweep public regulator portals',
        'text': (
            "Use Scout browser automation in prompt mode. Navigate only to public regulator portals: BNM, OJK, Bursa Malaysia, SC Malaysia, and MAS. Find the latest 10 circulars or consultation papers relevant to banking, payments, insurance, AML, cyber resilience, market conduct, or disclosures. Download PDFs to ./Regulator_Portal_Sweep_2026/downloads and take a screenshot of the listing page for each source.\n"
            "Summarise each document in 200 words: what changed, affected entities, effective date, MYR/IDR penalty or capital impact if stated, and actions for Mod Admin, Sasha, and the Company Secretary. Assemble ./Regulator_Portal_Sweep_2026/ASEAN_Regulatory_Brief.docx with a table, source URLs, and an appendix of screenshots. Do not log into internal portals."
        )
    }],
    'expected': [
        'Downloaded latest circular PDFs and screenshots in the workspace',
        'Word brief with 10 summaries, action owners, and source URLs',
        'Exception log for inaccessible pages or duplicate circulars',
    ],
    'watch': [
        'Scout controls a real browser: navigate, click, download, screenshot',
        'Prompt-mode approvals make the demo safe and visible to compliance audiences',
    ],
    'honest': 'Use public portals or approved sandboxes. Scout must not bypass controls; Legal and Compliance still interpret obligations.',
    'tips': [
        'For Bursa announcements, add issuer filters and export market-sensitive items separately',
        'For OJK, ask for bilingual Bahasa Indonesia and English output',
    ],
}

USE_CASES['uc-scout-subagents'] = {
    'title': 'Sub-Agent Fan-Out — Strategic Diligence in Parallel',
    'dept_tag': 'Strategy',
    'complexity': 'advanced',
    'apps': ['Word', 'Excel', 'PowerPoint', 'Research Agents'],
    'desc': 'One Scout prompt launches sub-agents for M&A diligence, then synthesises a brief, xlsx, and speaker-note deck.',
    'skills': [
        'Sub-agent fan-out using Research, Code review, Explore, and General-purpose agents',
        'Parallel diligence across market, financial, technology, ESG, and regulatory workstreams',
        'Synthesis of background-agent outputs into executive-ready files',
    ],
    'instructions': [
        'Open Scout in the M&A workspace with target profile, NDA-safe public sources, and internal thesis notes',
        'Enable web research and workspace file access; keep shell in prompt mode',
        'Paste the prompt and watch the sub-agent activity panel as agents run independently',
        'Ask Scout to reconcile conflicts between agents before finalising the pack',
    ],
    'sample_files': [
        ('TargetCo_Public_Profile.docx', 'docx'),
        ('SEA_Market_Size_Assumptions.xlsx', 'xlsx'),
        ('Diligence_Question_Bank.xlsx', 'xlsx'),
        ('IC_Memo_Template.pptx', 'pptx'),
    ],
    'prompts': [{
        'label': 'Fan out strategic diligence',
        'text': (
            "For Hadar and the Group Strategy team, run a Scout sub-agent fan-out on TargetCo. Launch five background agents: Research for market/news/regulatory signals with citations; Explore for internal synergy files and prior board references; Explore for competitor and customer concentration analysis; Explore for ESG/labour/supply-chain red flags; Code review for the target's public GitHub/mobile app or technology diligence notes where available.\n"
            "When all agents return, synthesise a 6-page Word investment brief, a Diligence_Findings.xlsx with source, confidence, MYR synergy range, and owner, and a 12-slide IC deck with speaker notes for Sasha and Daichi. Highlight contradictions between agents instead of hiding them."
        )
    }],
    'expected': [
        'Five parallel sub-agent workstreams with separate logs and citations',
        'Word investment brief with risks, synergies, and open diligence questions',
        'Excel finding register and PowerPoint IC deck with speaker notes',
    ],
    'watch': [
        'The main Scout session delegates to isolated sub-agents instead of doing one serial search',
        'Contradictions and confidence levels are preserved for Investment Committee challenge',
    ],
    'honest': 'Sub-agents accelerate triage; formal due diligence, valuation, and legal reliance remain human-owned.',
    'tips': [
        'Replace TargetCo with a hospital chain, payments fintech, plantation miller, or logistics 3PL',
        'Use one General-purpose agent to build a synergy model while Research agents gather citations',
    ],
}

USE_CASES['uc-scout-automation-monthly'] = {
    'title': 'Automation — Monthly Close Pack',
    'dept_tag': 'Finance',
    'complexity': 'advanced',
    'apps': ['Excel', 'PowerPoint', 'Outlook', 'Automation'],
    'desc': 'Schedule Scout for the 1st monthly at 7am to prepare variance workbooks, decks, and a CFO email draft.',
    'skills': [
        'Schedule-triggered recurring automation independent of an active chat',
        'Excel skill for GL extracts, budget variance, and workbook formatting',
        'PowerPoint and Outlook output with permission-aware send/draft behaviour',
    ],
    'instructions': [
        'Open Scout → Automations → New automation',
        'Name it Group Monthly Close Pack; trigger type Schedule; schedule 1st day monthly at 07:00',
        'Set file access to the Finance_Close workspace; Outlook send requires approval or draft-only',
        'Paste the automation prompt and importable GitHub definition if your environment uses automation-as-code',
    ],
    'sample_files': [
        ('GL_Extract_MY_ID_SG_2026M06.xlsx', 'xlsx'),
        ('Budget_Forecast_Bridge.xlsx', 'xlsx'),
        ('Monthly_Close_Deck_Template.pptx', 'pptx'),
        ('CFO_Email_Template.docx', 'docx'),
    ],
    'prompts': [{
        'label': 'Schedule monthly finance automation',
        'text': (
            "Create a recurring Scout automation for the 1st of every month at 07:00. In ./Finance_Close/[YYYY-MM], locate the latest GL extracts for Malaysia, Indonesia, and Singapore, then use the Excel skill to produce Group_Monthly_Variance_Pack.xlsx with tabs P&L, Cash, and Working Capital. Compare actuals vs budget and prior month, flag MYR variances over 3% or MYR 2m, and IDR variances over IDR 10bn.\n"
            "Generate a 6-slide PowerPoint monthly review deck for the Group CFO: Executive summary, revenue bridge, cost bridge, cash/working capital, entity exceptions, decisions needed. Draft an Outlook email to Group CFO and Finance LT with links to the files. If send approval is not available, save as draft only and log the run history."
        )
    }],
    'expected': [
        'Recurring Scout automation visible in Automations history',
        'Three-tab variance workbook with formulas, thresholds, and exception comments',
        'Six-slide monthly review deck plus CFO email draft or approved send',
    ],
    'watch': [
        'Automations are saved tasks with schedule or condition triggers, not ad-hoc prompts',
        'Scout can run the same close workflow every month and write back to folders',
    ],
    'honest': 'Finance automation needs clean GL extracts; the CFO still reviews, and material variances must tie to ledgers.',
    'tips': [
        'Change the trigger to condition-based: run when all entity GL extracts arrive',
        'Add a shell validation that compares workbook checksums and row counts to last month',
    ],
}

USE_CASES['uc-scout-loop-collab'] = {
    'title': 'Loop Page Co-Authoring — Live Strategy Doc',
    'dept_tag': 'Strategy',
    'complexity': 'intermediate',
    'apps': ['Browser', 'Loop', 'WorkIQ', 'Word'],
    'desc': 'Scout browser-opens Loop, drafts FY27 strategy content, and refreshes its own section every 4 hours.',
    'skills': [
        'Loop integration through Scout browser/Playwright skill',
        'WorkIQ refresh from email, Teams threads, meetings, and documents',
        'Recurring update pattern with clear ownership boundaries on a co-authored page',
    ],
    'instructions': [
        'Open Scout and sign into Microsoft 365 in the controlled browser session',
        'Set Browser Control to prompt mode and allow the specific Loop page URL',
        'Create a Loop section labelled Scout Draft - Strategy Signals',
        'Run the prompt once, then convert the refresh instruction to a heartbeat or automation every 4 hours',
    ],
    'sample_files': [
        ('FY27_Strategy_Themes.docx', 'docx'),
        ('Strategy_KPI_Baseline.xlsx', 'xlsx'),
        ('Loop_Strategy_Page_Screenshot.png', 'png'),
    ],
    'prompts': [{
        'label': 'Co-author and refresh the Loop page',
        'text': (
            "Use Scout browser control to open the approved Loop page [LOOP-URL]. In the section named Scout Draft - Strategy Signals, write the current draft of the FY27 strategy paper for Mod Admin and Hadar: 5 strategic choices, ASEAN market shifts, digital productivity bets, talent implications, ESG/regulatory watch, and unresolved decisions.\n"
            "Use WorkIQ to refresh only this Scout-owned section from new email threads, Teams discussions, meeting notes, and OneDrive strategy files from the last 4 hours. Add timestamped bullets and source links. Do not edit sections owned by Sasha, Daichi, HR, Legal, or Investor Relations. Also export a Word snapshot to ./Strategy_Loop_Snapshots/FY27_Strategy_Scout_Snapshot.docx."
        )
    }],
    'expected': [
        'Loop page section updated through controlled browser automation',
        'Timestamped strategy-signal bullets sourced from recent M365 activity',
        'Word snapshot saved to the workspace for review and archival',
    ],
    'watch': [
        'Scout uses browser actions to work in Loop, which standard chat cannot directly co-author',
        'The prompt scopes Scout to its own section to avoid overwriting colleagues',
    ],
    'honest': 'Live co-authoring is visible. Keep ownership rules explicit and browser approvals on.',
    'tips': [
        'Use heartbeat for 4-hour refresh during strategy offsites',
        'Add a nightly automation to export Loop snapshots for records management',
    ],
}

UNIVERSAL_USE_CASES = ['uc-scout-heartbeat', 'uc-scout-bulk-files', 'uc-scout-browser-portal']

# Per-entry mapping.
ENTRY_USE_CASES = {
    'general': ['uc-scout-heartbeat', 'uc-scout-subagents', 'uc-scout-loop-collab'],
    'banking': ['uc-scout-heartbeat', 'uc-scout-browser-portal', 'uc-scout-automation-monthly'],
    'asset-management': ['uc-scout-subagents', 'uc-scout-browser-portal', 'uc-scout-loop-collab'],
    'takaful': ['uc-scout-browser-portal', 'uc-scout-bulk-files', 'uc-scout-heartbeat'],
    'insurance': ['uc-scout-bulk-files', 'uc-scout-browser-portal', 'uc-scout-heartbeat'],
    'investment-banking': ['uc-scout-subagents', 'uc-scout-heartbeat', 'uc-scout-browser-portal'],
    'mortgage-finance': ['uc-scout-bulk-files', 'uc-scout-automation-monthly', 'uc-scout-browser-portal'],
    'cross-border-remittance': ['uc-scout-browser-portal', 'uc-scout-heartbeat', 'uc-scout-subagents'],
    'fintech-payments': ['uc-scout-browser-portal', 'uc-scout-heartbeat', 'uc-scout-subagents'],
    'oil-gas-upstream': ['uc-scout-bulk-files', 'uc-scout-subagents', 'uc-scout-heartbeat'],
    'oil-gas-downstream': ['uc-scout-automation-monthly', 'uc-scout-bulk-files', 'uc-scout-heartbeat'],
    'renewable-energy': ['uc-scout-bulk-files', 'uc-scout-subagents', 'uc-scout-loop-collab'],
    'power-utilities': ['uc-scout-heartbeat', 'uc-scout-bulk-files', 'uc-scout-automation-monthly'],
    'mining-coal': ['uc-scout-bulk-files', 'uc-scout-heartbeat', 'uc-scout-browser-portal'],
    'rare-earth': ['uc-scout-browser-portal', 'uc-scout-bulk-files', 'uc-scout-subagents'],
    'plantation': ['uc-scout-bulk-files', 'uc-scout-automation-monthly', 'uc-scout-loop-collab'],
    'food-fmcg': ['uc-scout-automation-monthly', 'uc-scout-bulk-files', 'uc-scout-subagents'],
    'cosmetics': ['uc-scout-automation-monthly', 'uc-scout-bulk-files', 'uc-scout-subagents'],
    'rubber-gloves': ['uc-scout-browser-portal', 'uc-scout-bulk-files', 'uc-scout-heartbeat'],
    'retail-grocery': ['uc-scout-automation-monthly', 'uc-scout-bulk-files', 'uc-scout-loop-collab'],
    'hospitality-hotel': ['uc-scout-automation-monthly', 'uc-scout-browser-portal', 'uc-scout-loop-collab'],
    'hospital-network': ['uc-scout-bulk-files', 'uc-scout-browser-portal', 'uc-scout-heartbeat'],
    'healthcare': ['uc-scout-bulk-files', 'uc-scout-browser-portal', 'uc-scout-heartbeat'],
    'pharmaceutical': ['uc-scout-browser-portal', 'uc-scout-bulk-files', 'uc-scout-subagents'],
    'telco': ['uc-scout-subagents', 'uc-scout-heartbeat', 'uc-scout-automation-monthly'],
    'ecommerce-superapp': ['uc-scout-automation-monthly', 'uc-scout-subagents', 'uc-scout-heartbeat'],
    'education': ['uc-scout-loop-collab', 'uc-scout-bulk-files', 'uc-scout-subagents'],
    'transportation-logistics': ['uc-scout-bulk-files', 'uc-scout-heartbeat', 'uc-scout-automation-monthly'],
    'logistics-3pl': ['uc-scout-bulk-files', 'uc-scout-heartbeat', 'uc-scout-automation-monthly'],
    'aviation-airports': ['uc-scout-heartbeat', 'uc-scout-browser-portal', 'uc-scout-automation-monthly'],
    'aviation-airlines': ['uc-scout-heartbeat', 'uc-scout-browser-portal', 'uc-scout-loop-collab'],
    'maritime-shipping': ['uc-scout-bulk-files', 'uc-scout-browser-portal', 'uc-scout-heartbeat'],
    'automotive': ['uc-scout-bulk-files', 'uc-scout-subagents', 'uc-scout-automation-monthly'],
    'auto-tyres': ['uc-scout-bulk-files', 'uc-scout-automation-monthly', 'uc-scout-subagents'],
    'semiconductor': ['uc-scout-subagents', 'uc-scout-bulk-files', 'uc-scout-heartbeat'],
    'industrial-manufacturing': ['uc-scout-bulk-files', 'uc-scout-automation-monthly', 'uc-scout-subagents'],
    'property-development': ['uc-scout-bulk-files', 'uc-scout-loop-collab', 'uc-scout-subagents'],
    'property-reit': ['uc-scout-automation-monthly', 'uc-scout-bulk-files', 'uc-scout-loop-collab'],
    'construction': ['uc-scout-bulk-files', 'uc-scout-browser-portal', 'uc-scout-heartbeat'],
    'government-agency': ['uc-scout-bulk-files', 'uc-scout-browser-portal', 'uc-scout-loop-collab'],
    'financial-regulator': ['uc-scout-browser-portal', 'uc-scout-heartbeat', 'uc-scout-subagents'],
    'glc-investment': ['uc-scout-automation-monthly', 'uc-scout-subagents', 'uc-scout-loop-collab'],
    'diversified-conglomerate': ['uc-scout-automation-monthly', 'uc-scout-subagents', 'uc-scout-heartbeat'],
    'bpo-services': ['uc-scout-heartbeat', 'uc-scout-bulk-files', 'uc-scout-automation-monthly'],


    'dept-finance': ['uc-scout-heartbeat', 'uc-scout-automation-monthly', 'uc-scout-bulk-files'],
    'dept-investor-relations': ['uc-scout-loop-collab', 'uc-scout-subagents', 'uc-scout-automation-monthly'],
    'dept-strategy': ['uc-scout-subagents', 'uc-scout-loop-collab', 'uc-scout-heartbeat'],
    'dept-esg': ['uc-scout-browser-portal', 'uc-scout-loop-collab', 'uc-scout-subagents'],
    'dept-risk': ['uc-scout-heartbeat', 'uc-scout-browser-portal', 'uc-scout-subagents'],
    'dept-legal': ['uc-scout-bulk-files', 'uc-scout-browser-portal', 'uc-scout-heartbeat'],
    'dept-corpsec': ['uc-scout-browser-portal', 'uc-scout-loop-collab', 'uc-scout-bulk-files'],
    'dept-procurement': ['uc-scout-bulk-files', 'uc-scout-automation-monthly', 'uc-scout-subagents'],
    'dept-operations': ['uc-scout-heartbeat', 'uc-scout-bulk-files', 'uc-scout-automation-monthly'],
    'dept-it-digital': ['uc-scout-heartbeat', 'uc-scout-subagents', 'uc-scout-browser-portal'],
    'dept-hr': ['uc-scout-loop-collab', 'uc-scout-bulk-files', 'uc-scout-heartbeat'],
    'dept-marketing': ['uc-scout-subagents', 'uc-scout-loop-collab', 'uc-scout-automation-monthly'],
    'dept-executives': ['uc-scout-subagents', 'uc-scout-heartbeat', 'uc-scout-automation-monthly'],
}


def get_scout_library_for_entry(entry_id, entry_name='', persona_name=''):
    """Return list of 2-3 Scout use-case cards for the entry."""
    # Aliases: actual entry IDs in ind_data*.py don't always match the keys in
    # ENTRY_USE_CASES above (which were authored before the entries were renamed).
    # Map them so every entry resolves to a use-case set.
    _ALIASES = {
        'commercial-banking': 'banking',
        'islamic-banking': 'banking',
        'general-insurance': 'insurance',
        'life-insurance': 'insurance',
        'og-upstream': 'oil-gas-upstream',
        'og-downstream': 'oil-gas-downstream',
        'coal-mining': 'mining-coal',
        'hotel-resort': 'hospitality-hotel',
        'media-entertainment': 'ecommerce-superapp',
        'electrical-distribution': 'industrial-manufacturing',
    }
    eid = _ALIASES.get(entry_id, entry_id)
    card_ids = ENTRY_USE_CASES.get(eid, [])
    cards = []
    for cid in card_ids:
        if cid in USE_CASES:
            card = dict(USE_CASES[cid])  # shallow copy
            card['id'] = cid
            cards.append(card)
    return cards

