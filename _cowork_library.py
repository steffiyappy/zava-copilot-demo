# -*- coding: utf-8 -*-
"""
Cowork Library catalog — Contoso C-Suite Immersion format MERGED with
everythingischr0me cowork-prompts format.

Each card carries:
- title, dept_tag, industry_tag (optional), complexity
- apps[]            — Apps Involved badges (Word/Excel/PPT/Outlook/Teams/Forms)
- desc              — 1-2 line description
- skills[]          — what is being demonstrated (the user asked for "skills")
- instructions[]    — step-by-step setup (where to click, what to attach)
- sample_files[]    — list of (filename, ext) tuples (pdf/xlsx/docx/png)
- prompts[]         — list of {label, text}; supports multi-step P1/P2/etc
- expected[]        — Expected Outcome bullets
- watch[]           — WHAT TO WATCH bullets (green callout)
- honest            — HONEST FRAMING paragraph (amber callout)
- tips[]            — Tips & Variations bullets

The catalog is consumed by build_master.py via get_library_for_entry(entry_id)
which returns 4-5 fully-resolved cards per entry.
"""

# ───────────────────────────────────────────────────────────────────────
# Use case catalog
# ───────────────────────────────────────────────────────────────────────

USE_CASES = {}

# ── UNIVERSAL ───────────────────────────────────────────────────────────
USE_CASES['uc-board-pack'] = {
    'title': 'Board Pack Sprint',
    'dept_tag': 'Corporate Secretarial',
    'complexity': 'intermediate',
    'apps': ['Word', 'PowerPoint', 'Outlook', 'Teams'],
    'desc': 'Turn a folder of board papers into a chairman briefing, a slide deck, an email pack to directors, and a Teams discussion thread — in one Cowork run.',
    'skills': [
        'Multi-source synthesis across financial pack, risk update, strategy memo, and audit minutes',
        'Parallel deliverable generation (Word brief + PPT deck + Outlook email + Teams thread)',
        'Tone calibration for board audience (concise, decision-oriented)',
    ],
    'instructions': [
        'Open Microsoft 365 Copilot → left nav → Agents → Cowork (Frontier Program required)',
        'Click 📎 Knowledge → attach the 4 sample files listed below',
        'Paste Prompt 1 — Cowork runs the parallel fan-out',
        'Review the 4 deliverables before forwarding to the Chair',
    ],
    'sample_files': [
        ('BRD_Q4_Financial_Pack.xlsx', 'xlsx'),
        ('BRD_Risk_Quarterly_Update.docx', 'docx'),
        ('BRD_Strategy_Memo.docx', 'docx'),
        ('BRD_Audit_Cmte_Minutes.docx', 'docx'),
    ],
    'prompts': [{
        'label': 'Fan out the board pack',
        'text': (
            "Using the 4 board papers attached, prepare the next Board meeting pack for [BOARD-DATE]. In parallel, do all 5:\n"
            "1) Draft a 3-page Chairman briefing in Word — top 5 decisions needed, key risks, ESG hot spots.\n"
            "2) Build a 10-slide deck in PowerPoint — Slide 1 cover, Slides 2-4 financials, Slide 5 risk dashboard, Slides 6-8 strategy progress, Slide 9 ESG/regulatory, Slide 10 decision summary.\n"
            "3) Draft an email in Outlook to the 8 named directors — Hadar (Chair Audit), Sasha (Chair Risk), Daichi (Chair Nomination), and the 5 INEDs — with the pack attached and pre-read instructions.\n"
            "4) Draft a Teams message to the Board WhatsApp-equivalent channel — 2 lines summary + the 2 critical decisions.\n"
            "5) Block 90 minutes on the calendar — title: Board Meeting [BOARD-DATE], attendees the 8 directors + Group CFO + Group CoS.\n"
            "Cite the specific paper and section for every number."
        )
    }],
    'expected': [
        'Chairman briefing (3 pages, Word)',
        '10-slide board deck (PowerPoint)',
        'Outlook email draft with pack attached',
        'Teams summary message',
        '90-min calendar invite',
    ],
    'watch': [
        'Every figure cites its source paper and section — auditable trail',
        'Each deliverable adapts tone for its audience (Chair memo vs WhatsApp blast)',
        'Decisions surfaced separately from updates — board focus stays sharp',
    ],
    'honest': 'Cowork drafts. The Chair and CoS still hand-review every line — board papers are legal record. The Teams message must be cleared by Comms before going live.',
    'tips': [
        'Swap the 4 source files for your real quarter\'s board pack to scale to other meetings',
        'Add a 6th task — generate a 30-second audio summary for the Chair\'s morning commute',
        'Re-run with persona switched to "Group Chief of Staff" voice for a CoS-led variant',
    ],
}

USE_CASES['uc-town-hall'] = {
    'title': 'Town Hall Comms Drill',
    'dept_tag': 'HR & Comms',
    'complexity': 'basic',
    'apps': ['Word', 'PowerPoint', 'Outlook', 'Teams', 'Forms'],
    'desc': 'Turn the CEO\'s rough script + a quarter of HR results into a polished town hall — speech, slides, employee email, Teams promo, and a feedback Form.',
    'skills': [
        'Tone-shifting from boardroom (financials) to all-employee (inclusive, plain English)',
        'Multi-channel campaign assembly (slides + email + chat + survey)',
        'Q&A anticipation from prior pulse-survey data',
    ],
    'instructions': [
        'Open Cowork from the Agents menu',
        'Attach the 4 source files (script outline, HR scorecard, prior Q&A, pulse-survey results)',
        'Paste the prompt — Cowork generates the full campaign in parallel',
        'Hand the deliverables to Internal Comms for sign-off before publishing',
    ],
    'sample_files': [
        ('TH_CEO_Script_Outline.docx', 'docx'),
        ('TH_HR_Quarterly_Scorecard.xlsx', 'xlsx'),
        ('TH_Prior_Town_Hall_QA.docx', 'docx'),
        ('TH_Pulse_Survey_Results.xlsx', 'xlsx'),
    ],
    'prompts': [{
        'label': 'Build the town hall campaign',
        'text': (
            "Using the 4 attached files, prepare the Q[N] FY[YEAR] all-employee town hall. In parallel, do all 5:\n"
            "1) Polish the CEO speech in Word — 12 minutes spoken, 5 sections (Wins / Challenges / Customer Voice / People / Ask).\n"
            "2) Build a 15-slide deck in PowerPoint — image-first, big numbers, no jargon, one decision per slide.\n"
            "3) Draft the all-staff email in Outlook from the CEO — RSVP link + 2-line teaser + dial-in details.\n"
            "4) Draft a Teams post for the Company-wide channel — 2 lines + GIF prompt + RSVP.\n"
            "5) Build a Microsoft Forms survey — 6 questions (3 multiple-choice on key initiatives, 2 free-text on biggest worry/biggest hope, 1 NPS).\n"
            "Anticipate 8 likely Q&A items from the pulse-survey themes and append as speaker notes in the deck."
        )
    }],
    'expected': [
        'Polished CEO speech (12-min, Word)',
        '15-slide town hall deck',
        'Outlook all-staff email',
        'Teams company-wide post',
        'Microsoft Forms feedback survey',
    ],
    'watch': [
        'Tone shifts from numbers-dense (board) to story-led (employees) — same data, different voice',
        'Q&A speaker notes prep the CEO for the toughest questions in advance',
        'Forms survey wired to capture sentiment for the next quarter\'s baseline',
    ],
    'honest': 'Cowork sets the structure; the CEO\'s personality still has to come through in the final edit. Sensitive items (layoffs, pay) must be drafted by HR not Cowork — the model has no context on confidential decisions.',
    'tips': [
        'Re-run with the CHRO as the speaker — voice and Q&A library auto-adjust',
        'For ID entities, generate the BI variant simultaneously by adding "Output in Bahasa Indonesia"',
        'Add a 6th task — extract the top 3 themes from the prior Q&A and pre-empt them in the speech',
    ],
}

USE_CASES['uc-incident-pmortem'] = {
    'title': 'Major Incident Postmortem',
    'dept_tag': 'IT & Operations',
    'complexity': 'intermediate',
    'apps': ['Word', 'Excel', 'Outlook', 'Teams'],
    'desc': 'War-room logs, monitoring graphs, customer complaint emails, and the on-call rota become a postmortem doc, root-cause table, customer apology, and regulator-grade timeline.',
    'skills': [
        'Timeline reconstruction from mixed log + email + chat sources',
        'Five-whys root cause analysis in tabular form',
        'Parallel comms drafting (customer apology + internal lessons + regulator notification)',
    ],
    'instructions': [
        'Open Cowork',
        'Attach the 4 incident artefacts',
        'Paste the prompt — Cowork builds the postmortem and the comms in one pass',
        'Hand to the Incident Manager for the SEV-1 review meeting',
    ],
    'sample_files': [
        ('INC_Wartime_Channel_Log.docx', 'docx'),
        ('INC_Monitoring_Metrics.xlsx', 'xlsx'),
        ('INC_Customer_Complaint_Emails.docx', 'docx'),
        ('INC_OnCall_Rota.xlsx', 'xlsx'),
    ],
    'prompts': [{
        'label': 'Build the postmortem pack',
        'text': (
            "Using the 4 attached files for incident [INC-ID] on [INC-DATE], in parallel, do all 5:\n"
            "1) Draft a 5-page postmortem in Word — Timeline (minute-by-minute), Impact (customers affected, revenue at risk, SLA breach), Root cause (5-whys table), Fixes deployed, Prevention plan.\n"
            "2) Build a root-cause table in Excel — Symptom / Direct cause / Contributing factor / Systemic cause / Owner / Due date / Status.\n"
            "3) Draft a customer apology email in Outlook from the COO — empathetic tone, what we did wrong, what we are fixing, goodwill gesture.\n"
            "4) Draft a Teams message to the All-Engineering channel — 2 lines + link to the postmortem + 3 lessons for next time.\n"
            "5) Draft a regulator notification letter in Word — formal tone, factual chronology, no speculation, ready for legal review.\n"
            "Mark every claim with the source artefact + line number from the log."
        )
    }],
    'expected': [
        '5-page postmortem document',
        'Root-cause analysis table (Excel)',
        'Customer apology email draft',
        'All-engineering Teams lessons post',
        'Regulator notification letter',
    ],
    'watch': [
        'Timeline reconstructed from war-room chat + monitoring + emails — no single source missed',
        'Root cause drilled to systemic level — not stopping at the surface symptom',
        'Each comms adapted: customer = empathy, engineers = lessons, regulator = facts',
    ],
    'honest': 'Cowork drafts. Legal MUST review the regulator letter before sending. The customer apology may need executive sign-off depending on goodwill amount. The five-whys is starter logic — engineers still own the systemic conclusion.',
    'tips': [
        'Re-run with persona "CISO" for security incidents instead of availability',
        'Add a 6th task — generate the SEV-1 review meeting agenda + 30-min calendar invite',
        'For sector-regulated entities (banking, healthcare, telco) feed in the relevant regulatory clauses for tone',
    ],
}


# ── GA June 2026 capability cards ──────────────────────────────────────
# Three cards showcasing capabilities that shipped with the Cowork GA
# release: Imagen 2 image generation + brand templates + model picker,
# local browser use in Microsoft Edge, and the unified Customize page
# for skills and plugins.

USE_CASES['uc-ga-visual-launch'] = {
    'title': 'Visual Launch Pack — Imagen 2 + Brand Templates',
    'dept_tag': 'Marketing & Communications',
    'complexity': 'beginner',
    'apps': ['Word', 'PowerPoint', 'Outlook', 'Teams', 'Cowork'],
    'desc': 'A product brief, a press release, and a brand kit become a hero image (Imagen 2), a fully branded 6-slide deck, an internal launch email, and 3 social posts — in one Cowork run with the model picker on Sonnet+Opus Advisor.',
    'skills': [
        'In-chat image generation with Imagen 2 saved straight to OneDrive',
        'Brand template auto-applied to every PowerPoint slide (fonts, colours, logo, layout)',
        'Model picker — Sonnet+Opus Advisor pairing for tone + structure quality on launch copy',
        'Parallel deliverable fan-out (image + deck + email + social) from a single prompt',
    ],
    'instructions': [
        'Open Microsoft 365 Copilot → left nav → Agents → Cowork',
        'Top-right model picker → choose Sonnet+Opus Advisor (or Auto for production)',
        'Click 📎 Knowledge → attach the 3 sample files listed below',
        'Paste Prompt 1 — Cowork generates the hero image, applies the brand template, drafts the comms',
        'Hero image lands in OneDrive → /Cowork Outputs/Images/ and is embedded in the deck',
    ],
    'sample_files': [
        ('LAUNCH_Product_Brief.docx', 'docx'),
        ('LAUNCH_Press_Release_Draft.docx', 'docx'),
        ('LAUNCH_Brand_Kit.pdf', 'pdf'),
    ],
    'prompts': [{
        'label': 'Generate the visual launch pack',
        'text': (
            "Using the 3 attached files for product launch [PRODUCT-NAME] on [LAUNCH-DATE], in parallel, do all 5:\n"
            "1) Generate a hero image with Imagen 2 — modern, hopeful, no people, brand colours from the Brand Kit, 16:9, suitable for slide 1 cover and LinkedIn header. Save to OneDrive and embed in the deck.\n"
            "2) Build a 6-slide deck in PowerPoint using our brand template — Slide 1 cover with hero image, Slide 2 the problem we solve, Slide 3 the product (3 key features), Slide 4 customer proof, Slide 5 pricing & availability, Slide 6 call-to-action. Apply the brand template — fonts, colours, logo, master layouts.\n"
            "3) Draft an internal launch email in Outlook from the GM Marketing — what is launching, why now, the 3 things every employee should say if asked.\n"
            "4) Draft 3 LinkedIn posts (different tones — bold, customer-quote, behind-the-scenes), each under 220 characters with 3 hashtags.\n"
            "5) Draft a Teams message to the #all-company channel — 2 lines plus a link to the deck plus the hero image inline.\n"
            "Cite the Brief or Press Release for every product claim. Flag any line that needs Legal review."
        )
    }],
    'expected': [
        'Hero image (PNG, 16:9, brand-coloured, in OneDrive)',
        '6-slide branded launch deck (PowerPoint with template applied)',
        'Internal launch email draft (Outlook)',
        '3 LinkedIn post drafts',
        'Teams #all-company announcement',
    ],
    'watch': [
        'The PPT picks up your brand template automatically — colours, fonts and logo match',
        'The hero image saves to OneDrive AND embeds in the deck — no copy-paste',
        'Sonnet+Opus Advisor improves launch-copy quality versus a single-model run',
    ],
    'honest': 'Cowork drafts and generates the image. Brand-Comms still owns final approval — Imagen 2 sometimes drifts off your exact palette, and Legal must sign off any pricing or competitive claim. The image generation is governed by your tenant\'s admin settings for AI image content.',
    'tips': [
        'Switch the model picker to Auto when the workflow is in production — it picks the right model per sub-task automatically',
        'Re-run with "vertical product photo, mobile portrait" for a separate Instagram-ready asset',
        'Add a 6th task — generate a 30-second voiceover script for a TikTok / Reels teaser',
        'If your tenant has the brand template gallery configured, name it explicitly: "Use the Corporate-2026 template"',
    ],
}

USE_CASES['uc-ga-browser-research'] = {
    'title': 'Local Browser Research — Live Web + Internal Sources',
    'dept_tag': 'Strategy & Research',
    'complexity': 'intermediate',
    'apps': ['Edge', 'Word', 'Excel', 'Cowork'],
    'desc': 'Cowork drives Microsoft Edge on your device using your existing sign-ins — pulling fresh competitor pricing, regulator filings, and an internal SharePoint dashboard into a one-page Word memo + Excel comparison table, with every cell citing its URL or document path.',
    'skills': [
        'Local browser use — Cowork operates Microsoft Edge with your authenticated sessions (SharePoint, OneDrive, paywalled news, regulator portals)',
        'Live multi-source synthesis — public web + internal authoritative sources in one run',
        'Cell-level URL citation in Excel — every datapoint traceable for audit',
        'Tone-aware Word memo (one page, decision-oriented)',
    ],
    'instructions': [
        'Open Cowork → top-right model picker → Auto',
        'Confirm browser permission when prompted — Cowork uses YOUR Edge session and YOUR sign-ins (tenant-policy permitting)',
        'Paste Prompt 1 — list the 3 to 5 competitors and the internal SharePoint dashboard URL',
        'Watch the browser window — Cowork narrates each page it visits',
        'Review the Word memo and Excel table when the run completes',
    ],
    'sample_files': [],
    'prompts': [{
        'label': 'Run the competitive scan',
        'text': (
            "Using local browser, do live research for the [PRODUCT-CATEGORY] competitive scan I need before Friday's strategy session. In parallel, do all 4:\n"
            "1) Visit these competitor public pricing pages — [COMP-1 URL], [COMP-2 URL], [COMP-3 URL] — and extract: list price, billing model, free tier, enterprise option, last updated date.\n"
            "2) Visit the regulator portal at [REGULATOR-URL] and pull the latest 2 filings or product approvals for this category in the last 90 days.\n"
            "3) Open the internal SharePoint dashboard at [INTERNAL-DASHBOARD-URL] (use my SSO sign-in) and pull our own current pricing, win-rate, and gross-margin for the category.\n"
            "4) Build an Excel comparison table — one row per company (us + 3 competitors), columns for each data point, every cell with a hyperlinked source.\n"
            "5) Draft a 1-page Word memo for the strategy lead — top 3 takeaways, 2 risks, 1 recommended price action. End with a citation list (URL + retrieval timestamp for each public source, document path + page for each internal source).\n"
            "If a page is paywalled or login-gated and you cannot read it with my session, list it under 'Could not access' with the reason."
        )
    }],
    'expected': [
        '1-page Word strategy memo with citations',
        'Excel comparison table with hyperlinked source per cell',
        '"Could not access" list for any gated pages (transparent audit trail)',
    ],
    'watch': [
        'Cowork browses with your sign-in — pulls SharePoint dashboards that public-web scrapers cannot',
        'Every datapoint hyperlinks back to the source page — no opaque "AI said so"',
        'Browser-use respects your tenant\'s data-loss policies; gated content surfaces a friction note instead of fabricating',
    ],
    'honest': 'Cowork operates YOUR browser session, so any site you cannot reach manually, Cowork cannot reach either. Competitor pricing can change between Cowork\'s retrieval and your meeting — re-run on the morning of the decision. Local browser use is governed by your admin\'s Cowork browser-use policies in the Microsoft 365 admin center; some tenants restrict which domains Cowork may visit.',
    'tips': [
        'Pin this prompt — re-run weekly to keep a living competitive baseline',
        'Add a 6th task — generate a 5-slide deck of the table for the strategy session',
        'For regulator-only research, swap step 3 for a second regulator portal in another jurisdiction',
        'If your admin has disabled local browser use, swap to the Researcher tool which uses public web only',
    ],
}

USE_CASES['uc-ga-custom-skill'] = {
    'title': 'Custom Skill — Guided Skill Builder on the Customize Page',
    'dept_tag': 'Productivity & Automation',
    'complexity': 'beginner',
    'apps': ['Cowork', 'OneDrive', 'Word'],
    'desc': 'A repeat task — say, the Monday weekly status digest — becomes a reusable Cowork skill, authored through the guided skill builder on the unified Customize page, so the team triggers the workflow with two clicks instead of re-pasting the prompt.',
    'skills': [
        'Customize page — unified home for plugins and skills (GA, June 2026)',
        'Guided skill builder — Cowork interviews you and writes the skill prompt for you',
        'Skill sharing — publish to your team so the same prompt runs the same way',
        'Markdown-native skill files in OneDrive — version-controlled and editable',
    ],
    'instructions': [
        'Open Cowork → top nav → Customize → Skills tab',
        'Click ➕ Add → Create new (guided)',
        'Answer Cowork\'s questions in chat — what triggers the skill, what inputs it needs, what outputs you expect',
        'Save the generated skill — Cowork stores it as a Markdown file in your OneDrive Cowork Skills folder',
        'Trigger the skill by name in any future Cowork run — or share it with your team via the Customize page',
    ],
    'sample_files': [],
    'prompts': [{
        'label': 'Build a Weekly Status Digest skill (guided)',
        'text': (
            "I want a reusable skill called 'Weekly Status Digest' that I run every Monday morning.\n\n"
            "When triggered, the skill should:\n"
            "1) Read my Sent emails from Friday last week to Sunday this week, and read my Teams chat messages from the same window.\n"
            "2) Pull the calendar events from last week and extract any commitments I made (look for phrases like 'I will', 'by Friday', 'next week we').\n"
            "3) Generate a 1-page Word digest with 3 sections — What got shipped, What slipped, Commitments for the coming week.\n"
            "4) Save the Word doc to my OneDrive at /Weekly Digests/ with filename YYYY-MM-DD-Status.docx.\n"
            "5) Draft an Outlook email to my manager with the digest attached and a 4-line summary in the body.\n\n"
            "Walk me through naming, scoping, and saving this skill — then save it to my Cowork Skills folder and make it shareable with my direct team."
        )
    }],
    'expected': [
        'A named, reusable Cowork skill saved in OneDrive (Markdown)',
        'A test run that produces the first weekly digest end-to-end',
        'A team-shareable skill listed on the Customize → Skills tab',
    ],
    'watch': [
        'Cowork drafts the skill prompt from your conversational description — you don\'t hand-write the syntax',
        'The skill file is plain Markdown in OneDrive — auditable, editable, version-controllable',
        'Future runs trigger with a short skill name — no copy-paste of the long prompt every Monday',
    ],
    'honest': 'Cowork can author up to 50 custom skills per tenant (April 2026 limit, may rise). The skill triggers on demand, not on a schedule — pair it with a Power Automate weekly cron if you want hands-off Monday morning delivery. Skills shared with the team carry your prompt verbatim — review any sensitive language before sharing.',
    'tips': [
        'Use this same pattern for a Monthly Board Pack skill, a Quarterly OKR Review skill, or a Friday Wrap skill',
        'Combine with the plugin catalog — install the Jira or ServiceNow plugin first so the skill can pull tickets too',
        'When the GA model picker is on Auto, the skill chooses the right model per sub-task automatically — no maintenance',
        'Edit the Markdown file directly in OneDrive when the workflow changes — no rebuild needed',
    ],
}


# ── MERGE PARTS 2-5 ────────────────────────────────────────────────────
try:
    from _cowork_lib_part2 import CARDS as _P2
    USE_CASES.update(_P2)
except Exception:
    pass
try:
    from _cowork_lib_part3 import CARDS as _P3
    USE_CASES.update(_P3)
except Exception:
    pass
try:
    from _cowork_lib_part4 import CARDS as _P4
    USE_CASES.update(_P4)
except Exception:
    pass
try:
    from _cowork_lib_part5 import CARDS as _P5
    USE_CASES.update(_P5)
except Exception:
    pass
try:
    from _cowork_lib_part6 import CARDS as _P6
    USE_CASES.update(_P6)
except Exception:
    pass
try:
    from _cowork_lib_part7 import CARDS as _P7
    USE_CASES.update(_P7)
except Exception:
    pass

# Append a comprehensive interactive-HTML-artifact prompt to every card
# (dashboard / kanban / heatmap / pipeline / matrix archetype, chosen by
# title + dept_tag). Idempotent. Skips cards whose prompts already mention
# an HTML deliverable.
try:
    from _cowork_lib_html_inject import inject_html_prompts as _inject_html_prompts
    _added_html, _skipped_html = _inject_html_prompts(USE_CASES)
except Exception as _e:
    _added_html, _skipped_html = 0, 0


UNIVERSAL_USE_CASES = ['uc-board-pack', 'uc-town-hall', 'uc-incident-pmortem', 'uc-ga-visual-launch', 'uc-ga-browser-research', 'uc-ga-custom-skill']


# Per-entry mapping: each entry gets 4-5 cards.
# Pattern: 2-3 entry-specific + 1-2 universal (rotated to vary).
ENTRY_USE_CASES = {
    # ── Industries ──
    'general':                  ['uc-board-pack', 'uc-town-hall', 'uc-incident-pmortem', 'uc-fin-monthend'],
    'commercial-banking':       ['uc-bank-credit-council', 'uc-bank-statement-extract', 'uc-bank-ubo-kyc', 'uc-bank-bnm-returns', 'uc-board-pack'],
    'islamic-banking':          ['uc-islamic-shariah-audit', 'uc-bank-credit-council', 'uc-bank-bnm-returns', 'uc-board-pack'],
    'investment-banking':       ['uc-ib-brc-prep', 'uc-ib-pitchbook', 'uc-bank-credit-council', 'uc-board-pack', 'uc-incident-pmortem'],
    'mortgage-finance':         ['uc-property-opr-shock', 'uc-mortgage-loss-mit', 'uc-bank-statement-extract', 'uc-bank-bnm-returns', 'uc-board-pack'],
    'general-insurance':        ['uc-life-empathetic-claim-reply', 'uc-life-plain-language-clause', 'uc-genins-cat-claim', 'uc-board-pack', 'uc-incident-pmortem', 'uc-fin-monthend'],
    'life-insurance':           ['uc-life-claims-tat-benchmark', 'uc-life-corporate-renewal', 'uc-life-pitch-brief', 'uc-life-empathetic-claim-reply', 'uc-life-plain-language-clause', 'uc-life-ops-agent', 'uc-lifeins-persistency', 'uc-board-pack', 'uc-fin-monthend', 'uc-town-hall'],
    'takaful':                  ['uc-life-empathetic-claim-reply', 'uc-life-plain-language-clause', 'uc-takaful-tabarru', 'uc-islamic-shariah-audit', 'uc-board-pack', 'uc-fin-monthend'],
    'fintech-payments':         ['uc-fintech-fraud', 'uc-it-incident', 'uc-incident-pmortem', 'uc-board-pack'],
    'cross-border-remittance':  ['uc-remit-corridor', 'uc-bank-ubo-kyc', 'uc-it-incident', 'uc-board-pack'],
    'hospital-network':         ['uc-hospital-caseconf', 'uc-board-pack', 'uc-it-incident', 'uc-town-hall'],
    'pharmaceutical':           ['uc-pharma-regsubmission', 'uc-board-pack', 'uc-incident-pmortem', 'uc-fin-monthend'],
    'og-upstream':              ['uc-og-upstream-lifting', 'uc-og-hse-pmortem', 'uc-board-pack', 'uc-incident-pmortem'],
    'og-downstream':            ['uc-aster-esg-workflow', 'uc-og-downstream-margin', 'uc-og-hse-pmortem', 'uc-board-pack', 'uc-fin-monthend'],
    'renewable-energy':         ['uc-renewable-ppa', 'uc-board-pack', 'uc-incident-pmortem', 'uc-esg-disclosure'],
    'industrial-manufacturing': ['uc-mfg-oee', 'uc-mfg-recall', 'uc-board-pack', 'uc-incident-pmortem'],
    'rubber-gloves':            ['uc-rubber-fda510k', 'uc-mfg-oee', 'uc-board-pack', 'uc-incident-pmortem'],
    'semiconductor':            ['uc-semicon-capacity', 'uc-mfg-oee', 'uc-board-pack', 'uc-incident-pmortem'],
    'automotive':               ['uc-auto-recall', 'uc-mfg-oee', 'uc-board-pack', 'uc-incident-pmortem'],
    'auto-tyres':               ['uc-auto-tyres-compound', 'uc-mfg-oee', 'uc-board-pack', 'uc-incident-pmortem'],
    'construction':             ['uc-construction-vo', 'uc-board-pack', 'uc-incident-pmortem', 'uc-fin-monthend'],
    'food-fmcg':                ['uc-bev-strategic-landscape', 'uc-bev-create-infographic', 'uc-bev-ssb-tax-shock', 'uc-food-promo', 'uc-board-pack', 'uc-town-hall', 'uc-marketing-campaign'],
    'plantation':               ['uc-klk-q1-ops-review', 'uc-plantation-rspo', 'uc-esg-disclosure', 'uc-board-pack', 'uc-incident-pmortem'],
    'bpo-services':             ['uc-bpo-sla-brief', 'uc-board-pack', 'uc-town-hall', 'uc-it-incident'],
    'telco':                    ['uc-telco-outage', 'uc-it-incident', 'uc-board-pack', 'uc-incident-pmortem'],
    'diversified-conglomerate': ['uc-klk-q1-ops-review', 'uc-cong-capalloc', 'uc-board-pack', 'uc-strat-marketscan', 'uc-fin-monthend'],
    'government-agency':        ['uc-govt-parlq', 'uc-board-pack', 'uc-town-hall', 'uc-it-incident'],
    'financial-regulator':      ['uc-reg-supervisory', 'uc-board-pack', 'uc-incident-pmortem', 'uc-town-hall'],
    'glc-investment':           ['uc-glc-dividend', 'uc-board-pack', 'uc-strat-marketscan', 'uc-fin-monthend'],
    'property-reit':            ['uc-property-township-ops-review', 'uc-property-strategic-landscape', 'uc-property-gm-strategy-deck', 'uc-reit-renewal', 'uc-board-pack', 'uc-fin-monthend', 'uc-ir-invday'],
    'logistics-3pl':            ['uc-log-capacity', 'uc-board-pack', 'uc-incident-pmortem', 'uc-it-incident'],
    'aviation-airports':        ['uc-avi-airport-slot', 'uc-board-pack', 'uc-incident-pmortem', 'uc-it-incident'],
    'aviation-airlines':        ['uc-avi-airline-irrops', 'uc-board-pack', 'uc-incident-pmortem', 'uc-town-hall'],
    'coal-mining':              ['uc-coal-volume', 'uc-board-pack', 'uc-incident-pmortem', 'uc-esg-disclosure'],
    'rare-earth':               ['uc-rare-earth-export', 'uc-board-pack', 'uc-incident-pmortem', 'uc-esg-disclosure'],
    'retail-grocery':           ['uc-retail-store-pnl', 'uc-board-pack', 'uc-marketing-campaign', 'uc-town-hall'],
    'hotel-resort':             ['uc-hotel-surge', 'uc-board-pack', 'uc-marketing-campaign', 'uc-town-hall'],
    'media-entertainment':      ['uc-media-campaign', 'uc-marketing-campaign', 'uc-board-pack', 'uc-town-hall'],
    'education':                ['uc-edu-cohort', 'uc-board-pack', 'uc-town-hall', 'uc-hr-perfreview'],
    'power-utilities':          ['uc-util-outage', 'uc-incident-pmortem', 'uc-it-incident', 'uc-board-pack'],
    'property-development':     ['uc-property-township-ops-review', 'uc-property-land-bank', 'uc-property-strategic-landscape', 'uc-property-gm-strategy-deck', 'uc-property-create-infographic', 'uc-property-opr-shock', 'uc-propdev-launch', 'uc-construction-vo', 'uc-board-pack', 'uc-marketing-campaign'],
    'ecommerce-superapp':       ['uc-ecomm-surge', 'uc-it-incident', 'uc-incident-pmortem', 'uc-board-pack'],
    'maritime-shipping':        ['uc-maritime-port', 'uc-board-pack', 'uc-incident-pmortem', 'uc-fin-monthend'],

    # ── Departments ──
    'dept-finance':             ['uc-fin-monthend', 'uc-board-pack', 'uc-cong-capalloc', 'uc-incident-pmortem'],
    'dept-hr':                  ['uc-hr-perfreview', 'uc-hr-onboarding', 'uc-town-hall', 'uc-board-pack'],
    'dept-legal':               ['uc-life-plain-language-clause', 'uc-legal-contract', 'uc-board-pack', 'uc-incident-pmortem', 'uc-it-incident'],
    'dept-risk':                ['uc-bev-ssb-tax-shock', 'uc-property-opr-shock', 'uc-ib-brc-prep', 'uc-risk-appetite', 'uc-board-pack', 'uc-incident-pmortem', 'uc-fintech-fraud'],
    'dept-strategy':            ['uc-bev-strategic-landscape', 'uc-bev-ssb-tax-shock', 'uc-property-land-bank', 'uc-property-strategic-landscape', 'uc-property-gm-strategy-deck', 'uc-klk-q1-ops-review', 'uc-strat-marketscan', 'uc-cong-capalloc', 'uc-board-pack', 'uc-town-hall'],
    'dept-marketing':           ['uc-bev-create-infographic', 'uc-life-corporate-renewal', 'uc-life-pitch-brief', 'uc-property-create-infographic', 'uc-marketing-campaign', 'uc-media-campaign', 'uc-board-pack', 'uc-town-hall'],
    'dept-esg':                 ['uc-aster-esg-workflow', 'uc-esg-disclosure', 'uc-plantation-rspo', 'uc-board-pack', 'uc-renewable-ppa'],
    'dept-operations':          ['uc-life-claims-tat-benchmark', 'uc-life-empathetic-claim-reply', 'uc-life-ops-agent', 'uc-property-township-ops-review', 'uc-ops-sop', 'uc-board-pack', 'uc-incident-pmortem', 'uc-it-incident'],
    'dept-corpsec':             ['uc-corpsec-agm', 'uc-board-pack', 'uc-town-hall', 'uc-glc-dividend'],
    'dept-investor-relations':  ['uc-ir-invday', 'uc-board-pack', 'uc-glc-dividend', 'uc-fin-monthend'],
    'dept-procurement':         ['uc-proc-rfp', 'uc-board-pack', 'uc-incident-pmortem', 'uc-cong-capalloc'],
    'dept-it-digital':          ['uc-it-incident', 'uc-incident-pmortem', 'uc-board-pack', 'uc-ops-sop'],
}


# ── Customer-runbook Cowork cards (KLK / KIBB / Regulator) ────────────────
# Prepended to each routed entry so the runbook UCs surface on the
# standalone 🤝 Cowork sidebar tab too (in addition to each entry's own
# M365 Copilot Tools → Cowork sub-tab which already carries the prompts).
_RUNBOOK_ENTRY_CARDS = {
    # KLK (per cowork_customer_runbooks.KLK_ROUTING)
    'industrial-manufacturing': ['uc-klk-site-spreading'],
    'property-development':     ['uc-klk-investment-council'],
    'diversified-conglomerate': ['uc-klk-group-pnl-app', 'uc-reg-workforce-scenario'],

    # KIBB Cowork cards (per KIBB_COWORK_ROUTING) + KLK + Regulator that route to depts
    'investment-banking':       ['uc-kibb-credit-underwriting-pack', 'uc-kibb-investment-council', 'uc-reg-ipo-prospectus-compliance'],
    'financial-regulator':      ['uc-reg-ipo-prospectus-compliance', 'uc-reg-complaint-triage', 'uc-reg-tax-application', 'uc-reg-policy-paper'],

    # Departments
    'dept-finance':             ['uc-klk-bank-statement', 'uc-reg-tax-application', 'uc-reg-procurement-benchmarking'],
    'dept-hr':                  ['uc-klk-talent-council', 'uc-kibb-onboarding-bundle', 'uc-kibb-perf-review-prep', 'uc-reg-workforce-scenario'],
    'dept-legal':               ['uc-kibb-ubo-kyc', 'uc-kibb-contract-renewal', 'uc-reg-complaint-triage', 'uc-reg-contract-review'],
    'dept-risk':                ['uc-klk-counterparty-memo', 'uc-kibb-financial-spreading', 'uc-kibb-underwriting-decision-engine', 'uc-reg-internal-audit-pack'],
    'dept-strategy':            ['uc-klk-capex-scenario', 'uc-kibb-cashflow-model-app', 'uc-reg-policy-paper'],
    'dept-marketing':           ['uc-kibb-account-brief', 'uc-kibb-campaign-launch', 'uc-reg-investor-education-audit'],
    'dept-esg':                 ['uc-klk-ghg-cdp'],
    'dept-operations':          ['uc-kibb-bank-statement-extraction'],
    'dept-corpsec':             ['uc-reg-internal-audit-pack'],
    'dept-investor-relations':  ['uc-klk-quarterly-spread', 'uc-reg-investor-education-audit'],
    'dept-procurement':         ['uc-klk-ubo-sanctions', 'uc-kibb-rfp-scoring', 'uc-reg-contract-review', 'uc-reg-procurement-benchmarking'],
    'dept-it-digital':          ['uc-kibb-it-governance', 'uc-kibb-incident-postmortem'],
}

# Merge runbook cards into ENTRY_USE_CASES (prepend; preserve existing entries)
for _eid, _new_cids in _RUNBOOK_ENTRY_CARDS.items():
    _existing = ENTRY_USE_CASES.get(_eid, list(UNIVERSAL_USE_CASES))
    _merged = list(_new_cids) + [c for c in _existing if c not in _new_cids]
    ENTRY_USE_CASES[_eid] = _merged


# ── GA June 2026 — surface the 3 new-capability cards on every entry ──
# Append (not prepend) so each entry's own domain-specific cards stay on
# top of the sidebar; the GA cards anchor the bottom as a cross-cutting
# capability showcase available regardless of industry/department.
_GA_JUN2026_APPEND = ['uc-ga-visual-launch', 'uc-ga-browser-research', 'uc-ga-custom-skill']
for _eid in list(ENTRY_USE_CASES.keys()):
    _existing = ENTRY_USE_CASES[_eid]
    ENTRY_USE_CASES[_eid] = list(_existing) + [c for c in _GA_JUN2026_APPEND if c not in _existing]


def get_library_for_entry(entry_id):
    """Return list of 4-5 resolved card dicts for the given entry id.

    Each card is a dict carrying:
      title, dept_tag, industry_tag, complexity, apps, desc,
      skills, instructions, sample_files, prompts, expected, watch, honest, tips,
      and the auto-injected 'id' field.

    Falls back to the 3 universal cards if entry_id is unknown.
    """
    card_ids = ENTRY_USE_CASES.get(entry_id) or UNIVERSAL_USE_CASES
    out = []
    for cid in card_ids:
        c = USE_CASES.get(cid)
        if not c:
            continue
        card = dict(c)
        card['id'] = cid
        out.append(card)
    return out


# Optional self-check when run directly
if __name__ == '__main__':
    print('USE_CASES catalog size:', len(USE_CASES))
    print('ENTRY_USE_CASES mapped entries:', len(ENTRY_USE_CASES))
    missing = []
    for eid, cids in ENTRY_USE_CASES.items():
        for cid in cids:
            if cid not in USE_CASES:
                missing.append((eid, cid))
    if missing:
        print('MISSING:', missing)
    else:
        print('All entry mappings resolve.')
    # Per-entry preview
    for eid in list(ENTRY_USE_CASES.keys())[:3]:
        cards = get_library_for_entry(eid)
        print(f'\n{eid} -> {len(cards)} cards:')
        for c in cards:
            print(f"  - {c['id']}: {c['title']}")
