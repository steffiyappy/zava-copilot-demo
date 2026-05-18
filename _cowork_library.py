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


UNIVERSAL_USE_CASES = ['uc-board-pack', 'uc-town-hall', 'uc-incident-pmortem']


# Per-entry mapping: each entry gets 4-5 cards.
# Pattern: 2-3 entry-specific + 1-2 universal (rotated to vary).
ENTRY_USE_CASES = {
    # ── Industries ──
    'general':                  ['uc-board-pack', 'uc-town-hall', 'uc-incident-pmortem', 'uc-fin-monthend'],
    'commercial-banking':       ['uc-bank-credit-council', 'uc-bank-statement-extract', 'uc-bank-ubo-kyc', 'uc-bank-bnm-returns', 'uc-board-pack'],
    'islamic-banking':          ['uc-islamic-shariah-audit', 'uc-bank-credit-council', 'uc-bank-bnm-returns', 'uc-board-pack'],
    'investment-banking':       ['uc-ib-brc-prep', 'uc-ib-pitchbook', 'uc-bank-credit-council', 'uc-board-pack', 'uc-incident-pmortem'],
    'mortgage-finance':         ['uc-mortgage-loss-mit', 'uc-bank-statement-extract', 'uc-bank-bnm-returns', 'uc-board-pack'],
    'general-insurance':        ['uc-genins-cat-claim', 'uc-board-pack', 'uc-incident-pmortem', 'uc-fin-monthend'],
    'life-insurance':           ['uc-lifeins-persistency', 'uc-board-pack', 'uc-fin-monthend', 'uc-town-hall'],
    'takaful':                  ['uc-takaful-tabarru', 'uc-islamic-shariah-audit', 'uc-board-pack', 'uc-fin-monthend'],
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
    'food-fmcg':                ['uc-food-promo', 'uc-board-pack', 'uc-town-hall', 'uc-marketing-campaign'],
    'plantation':               ['uc-klk-q1-ops-review', 'uc-plantation-rspo', 'uc-esg-disclosure', 'uc-board-pack', 'uc-incident-pmortem'],
    'bpo-services':             ['uc-bpo-sla-brief', 'uc-board-pack', 'uc-town-hall', 'uc-it-incident'],
    'telco':                    ['uc-telco-outage', 'uc-it-incident', 'uc-board-pack', 'uc-incident-pmortem'],
    'diversified-conglomerate': ['uc-klk-q1-ops-review', 'uc-cong-capalloc', 'uc-board-pack', 'uc-strat-marketscan', 'uc-fin-monthend'],
    'government-agency':        ['uc-govt-parlq', 'uc-board-pack', 'uc-town-hall', 'uc-it-incident'],
    'financial-regulator':      ['uc-reg-supervisory', 'uc-board-pack', 'uc-incident-pmortem', 'uc-town-hall'],
    'glc-investment':           ['uc-glc-dividend', 'uc-board-pack', 'uc-strat-marketscan', 'uc-fin-monthend'],
    'property-reit':            ['uc-reit-renewal', 'uc-board-pack', 'uc-fin-monthend', 'uc-ir-invday'],
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
    'property-development':     ['uc-propdev-launch', 'uc-construction-vo', 'uc-board-pack', 'uc-marketing-campaign'],
    'ecommerce-superapp':       ['uc-ecomm-surge', 'uc-it-incident', 'uc-incident-pmortem', 'uc-board-pack'],
    'maritime-shipping':        ['uc-maritime-port', 'uc-board-pack', 'uc-incident-pmortem', 'uc-fin-monthend'],

    # ── Departments ──
    'dept-finance':             ['uc-fin-monthend', 'uc-board-pack', 'uc-cong-capalloc', 'uc-incident-pmortem'],
    'dept-hr':                  ['uc-hr-perfreview', 'uc-hr-onboarding', 'uc-town-hall', 'uc-board-pack'],
    'dept-legal':               ['uc-legal-contract', 'uc-board-pack', 'uc-incident-pmortem', 'uc-it-incident'],
    'dept-risk':                ['uc-ib-brc-prep', 'uc-risk-appetite', 'uc-board-pack', 'uc-incident-pmortem', 'uc-fintech-fraud'],
    'dept-strategy':            ['uc-klk-q1-ops-review', 'uc-strat-marketscan', 'uc-cong-capalloc', 'uc-board-pack', 'uc-town-hall'],
    'dept-marketing':           ['uc-marketing-campaign', 'uc-media-campaign', 'uc-board-pack', 'uc-town-hall'],
    'dept-esg':                 ['uc-aster-esg-workflow', 'uc-esg-disclosure', 'uc-plantation-rspo', 'uc-board-pack', 'uc-renewable-ppa'],
    'dept-operations':          ['uc-ops-sop', 'uc-board-pack', 'uc-incident-pmortem', 'uc-it-incident'],
    'dept-corpsec':             ['uc-corpsec-agm', 'uc-board-pack', 'uc-town-hall', 'uc-glc-dividend'],
    'dept-investor-relations':  ['uc-ir-invday', 'uc-board-pack', 'uc-glc-dividend', 'uc-fin-monthend'],
    'dept-procurement':         ['uc-proc-rfp', 'uc-board-pack', 'uc-incident-pmortem', 'uc-cong-capalloc'],
    'dept-it-digital':          ['uc-it-incident', 'uc-incident-pmortem', 'uc-board-pack', 'uc-ops-sop'],
}


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
