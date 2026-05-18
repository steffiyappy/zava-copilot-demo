"""
cowork_customer_runbooks.py

Injects the KLK Cowork Runbook (10 UCs) + KIBB BRC runbook (6 prompts) +
KIBB Cowork page UCs (15 cards) into the matching Zava hub entries' Cowork
tool blocks. Each UC's prompt chain is extended with one additional
**HTML artifact prompt** so Cowork produces a self-contained interactive
HTML deliverable (dashboard / kanban / heatmap / pipeline timeline) tailored
to that UC. Sample files referenced by the UC are also appended to the
target entry's `files[]` list so they show up in the demo's Files tab.

Constraints (user feedback):
- DO NOT create actual HTML files inside the hub repo. The HTML artifact
  is what Cowork generates when the user runs the prompt during the demo.
- Files[] gets the filename strings appended (dedup) so the demo lists them.
- All prompts go into the Cowork tool block (T_COWORK = FRONTIER license).
- APPEND only — never rewrite existing prompts. Idempotent via 60-char
  prefix check.
"""
import json
from pathlib import Path

_RUNBOOK_JSON = Path(__file__).parent / 'tools' / '_customer_runbooks.json'

# ── Routing ──────────────────────────────────────────────────────────────
KLK_ROUTING = {
    'rb-1':  'industrial-manufacturing',
    'rb-2':  'dept-strategy',
    'rb-3':  'property-development',
    'rb-4':  'dept-finance',
    'rb-5':  'dept-procurement',
    'rb-6':  'dept-risk',
    'rb-7':  'dept-hr',
    'rb-8':  'dept-investor-relations',
    'rb-9':  'dept-esg',
    'rb-10': 'diversified-conglomerate',
}

KIBB_BRC_TARGET = 'investment-banking'

KIBB_COWORK_ROUTING = {
    'credit-underwriting-pack':     'investment-banking',
    'investment-council':           'investment-banking',
    'ubo-kyc':                      'dept-legal',
    'bank-statement-extraction':    'dept-operations',
    'financial-spreading':          'dept-risk',
    'cashflow-model-app':           'dept-strategy',
    'underwriting-decision-engine': 'dept-risk',
    'it-governance':                'dept-it-digital',
    'rfp-scoring':                  'dept-procurement',
    'contract-renewal':             'dept-legal',
    'onboarding-bundle':            'dept-hr',
    'perf-review-prep':             'dept-hr',
    'account-brief':                'dept-marketing',
    'incident-postmortem':          'dept-it-digital',
    'campaign-launch':              'dept-marketing',
}

# ── HTML artifact archetype per UC ───────────────────────────────────────
# Picks the visualisation pattern that best fits the UC's deliverable.
KLK_HTML_ARCHETYPE = {
    'rb-1':  ('heatmap',  'Multi-site KPI heatmap — sites × metrics (throughput, yield, OEE, downtime, safety, ESG) with Red/Amber/Green cells and a click-to-drill side panel showing the underlying numbers from the spreading sheet.'),
    'rb-2':  ('dashboard', 'Interactive Capex Scenario App — sliders for capex amount, discount rate, ramp-up profile, FX, and commodity price; live NPV/IRR/Payback/Sensitivity widgets; tornado chart for top-5 sensitivities; toggle Frankfurt vs Detroit vs Combined.'),
    'rb-3':  ('pipeline',  'Riverside Phase 3 development timeline — phase lanes (land bank → entitlements → design → presales → construction → handover) with milestone markers, RAG status pills, council-of-agents verdict per lane, and an "open issues" badge per milestone.'),
    'rb-4':  ('dashboard', 'Bank Statement Extraction QA dashboard — file-source ribbon (text PDF / scanned PDF / mobile screenshot), extraction accuracy meter, LOW-CONFIDENCE row count by month, currency mix donut, and a sortable transactions table with confidence flags.'),
    'rb-5':  ('heatmap',   'UBO + Sanctions risk grid — suppliers (rows) × risk dimensions (UBO opacity, sanctions adjacency, PEP exposure, country risk, beneficial-owner change velocity) with Red/Amber/Green cells, a side panel showing recursive research citations.'),
    'rb-6':  ('dashboard', 'Counterparty exposure dashboard — facility list with exposure bars, headroom % gauges, PD/LGD/EAD ribbons, watchlist toggle, citation chips linking back to the source Underwriting Memo paragraph (Cite-Don\'t-Fabricate guardrail).'),
    'rb-7':  ('kanban',    'Top-50 Talent Review kanban — 5 lanes (High Performance / High Potential / Retention Risk / DEI Spotlight / Succession Ready); each card shows name role, last-cycle rating, retention RAG, council verdict, and a click-to-expand citation panel.'),
    'rb-8':  ('heatmap',   'Quarterly Results parity heatmap — divisions × line items (Revenue, COGS, EBITDA, Capex, Working Capital, Free Cash Flow) with QoQ variance colour-coding and a parity-check ribbon at the top (Balance Sheet, P&L, Cashflow tied).'),
    'rb-9':  ('dashboard', 'CDP-ready GHG dashboard — Scope 1/2/3 stacked bars per site, intensity per unit-output line, methodology pill (location-based vs market-based), inventory-boundary toggle, and a "ready-to-submit" CDP completeness checklist sidebar.'),
    'rb-10': ('dashboard', 'Group P&L Interactive Strategy App — sliders for FX, commodity prices, divestment scenarios, capex pace; live Group P&L, Divisional EBITDA waterfall, free-cash-flow projection, and a "what would change my mind" scenario stack.'),
}

KIBB_BRC_HTML_ARCHETYPE = (
    'dashboard',
    'BRC Pack interactive dashboard — segment P&L bars, vendor governance RAG matrix, top-10 risk register grid, decision-tracker timeline, and a "directors will ask" Q&A panel sourced from the BRC pack with citation chips back to the underlying memo paragraphs.',
)

KIBB_CARD_HTML_ARCHETYPE = {
    'credit-underwriting-pack':     ('dashboard', 'Credit Underwriting Pack dashboard — borrower profile, exposure timeline, PD/LGD/EAD ribbon, covenant matrix, and a Cite-Don\'t-Fabricate citation tray that links every red rating back to the source memo paragraph.'),
    'investment-council':           ('pipeline',  'Investment Council timeline — lens lanes (Land Bank / Macro / Construction Risk / Stress Test / Compliance), each lane shows the council-agent verdict, the highest-conviction concern, and a recommendation pill.'),
    'ubo-kyc':                      ('heatmap',   'UBO + KYC risk heatmap — ownership chain rows × diligence dimensions (UBO opacity, sanctions, PEP, country risk, source-of-funds clarity) with RAG cells and a click-to-open citation drawer.'),
    'bank-statement-extraction':    ('dashboard', 'Bank Statement Extraction dashboard — file-source ribbon, extraction-accuracy meter, LOW-CONFIDENCE row count, currency mix donut, sortable transaction table with confidence flags.'),
    'financial-spreading':          ('dashboard', 'Financial Spreading dashboard — 3-year line trends, balance-sheet parity ribbon (Total Assets = Liabilities + Equity tick), Unmapped-Lines panel, and a coverage % gauge per statement section.'),
    'cashflow-model-app':           ('dashboard', 'Cashflow Model Interactive App — sliders for revenue ramp, gross margin, capex, working-capital days, FX; live free-cashflow projection, DSCR/ICR gauges, downside/base/upside scenario toggle.'),
    'underwriting-decision-engine': ('dashboard', 'Underwriting Decision Engine — borrower input form (top), live PD/LGD/EAD calculation, decision pill (Approve / Refer / Decline) with citation back to policy clause, and an "explain my decision" trace panel.'),
    'it-governance':                ('heatmap',   'IT Governance compliance heatmap — controls (rows) × frameworks (RMiT / BNM / ISO27001 / PDPA) with RAG cells and click-to-drill into the source clause + gap-list panel.'),
    'rfp-scoring':                  ('heatmap',   'RFP Scoring matrix — bidders (rows) × scoring dimensions (Technical, Commercial, Risk, ESG, Local Content, Track Record) with RAG cells, total-score ribbon, and a recommendation drawer feeding the IC paper.'),
    'contract-renewal':             ('pipeline',  'Contract Renewal pipeline — renewal lanes by month, each card shows counterparty, value, key-clause-changes RAG, renewal-deadline countdown, and a "recommend renegotiate / let-lapse / extend" pill.'),
    'onboarding-bundle':            ('kanban',    'New Joiner onboarding kanban — Day-0 / Week-1 / Day-30 / Day-60 / Day-90 lanes with task cards (kit, accesses, training, stakeholders, first deliverable); each card carries owner and status pill.'),
    'perf-review-prep':             ('kanban',    'Performance Review kanban — Strengths / Achievements / Development Areas / Stretch Goals / Calibration Notes lanes; each card cites the underlying evidence file and tags the competency framework.'),
    'account-brief':                ('dashboard', 'Account-Based Selling Brief dashboard — buyer-map graph (decision makers, influencers, blockers), opportunity stack with deal-value bars, recent-news ribbon, and a "next-best-action" tray.'),
    'incident-postmortem':          ('pipeline',  'Major Incident Postmortem timeline — detect / triage / mitigate / restore / learn lanes with timestamp markers, MTTD/MTTR meters, top-3 contributing factors, and a remediation-tracker card per action.'),
    'campaign-launch':              ('kanban',    'Campaign Launch kanban — Creative / Content / Channels / Targeting / Measurement lanes with task cards, owner avatars, due-date pills, and a launch-readiness % gauge in the header.'),
}


# ── Helpers ──────────────────────────────────────────────────────────────
def _is_cowork(name: str) -> bool:
    return 'Cowork' in (name or '')


def _find_cowork_block(entry: dict):
    for tb in entry.get('prompts') or []:
        if _is_cowork(tb.get('tool', '')):
            return tb
    return None


def _load_runbooks():
    if not _RUNBOOK_JSON.exists():
        return None
    with open(_RUNBOOK_JSON, 'r', encoding='utf-8') as f:
        return json.load(f)


def _html_artifact_prompt(uc_title: str, archetype: str, brief: str,
                          context_files: list, deliverable_note: str = '') -> dict:
    """Build a single Cowork prompt that asks for a self-contained interactive
    HTML deliverable tailored to the UC. Each prompt also tells Cowork to fan
    out 4 parallel deliverables (Word memo + Outlook email + Teams meeting +
    tracker update) so the cowork pattern is preserved."""
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

    instr = (f"**Cowork Runbook · {uc_title} · HTML Artifact Step** "
             f"({archetype.title()}). Pattern: Model → Interactive App. "
             f"Apps: Cowork · Word · Outlook · Teams · Tracker. "
             f"Produces a **{archetype_label}** plus 4 parallel side-deliverables. "
             f"**Honest framing:** The HTML is for review and demo; for production "
             f"use, hand the data over to your BI team. {deliverable_note}").strip()

    prompt = (
        f"Building on the {uc_title} runbook output above, now produce a "
        f"**SELF-CONTAINED interactive HTML** artifact for executive review.{files_clause}\n\n"
        f"The HTML must be a single .html file with inline CSS and inline JavaScript "
        f"— NO external CDN, NO external image, NO web fonts. It must open and "
        f"function fully offline. Use a clean executive aesthetic (slate text, "
        f"off-white background, accent colour from the source brand).\n\n"
        f"**The {archetype_label} should be:** {brief}\n\n"
        f"In parallel, also do all of these in one Cowork run:\n"
        f"1) Save the HTML as '{uc_title.replace(' ', '_').replace('/', '_')}.html' "
        f"to /Cowork/Artifacts/[YYYY-MM]/.\n"
        f"2) Draft a 1-page Word memo summarising what the HTML shows, the top-3 "
        f"insights an executive should read first, and the recommended next step.\n"
        f"3) Draft an Outlook email to the executive sponsor with the HTML attached, "
        f"a 4-bullet TL;DR in the body, and a request to confirm by [DATE].\n"
        f"4) Schedule a 30-minute Teams review meeting for [DATE+2 business days] "
        f"with the sponsor + 2 named deputies; include the HTML link in the invite.\n"
        f"5) Update the tracker workbook with a new row: date, UC, artifact link, "
        f"owner, review status (Pending), and target close date."
    )
    return {'instr': instr, 'prompt': prompt}


def _format_instr_klk(uc: dict, prompt_idx: int, total_steps: int) -> str:
    parts = []
    step = f"Step {prompt_idx+1} of {total_steps}"
    parts.append(f"**Cowork Runbook · {uc['title']} · {step}** "
                 f"({uc['prompts'][prompt_idx]['title']}). "
                 f"Pattern: {uc.get('pattern', '').replace('Pattern · ', '')}. "
                 f"Category: {uc.get('category', '')}. "
                 f"Apps: {uc.get('apps', '').replace('Apps · ', '')}.")
    if prompt_idx == 0 and uc.get('files'):
        flist = ', '.join(uc['files'][:6])
        parts.append(f"Sample source files (attach via 📎 Knowledge): {flist}.")
    if prompt_idx == total_steps - 1 and uc.get('honest'):
        honest = uc['honest']
        if honest.lower().startswith('honest framing'):
            honest = honest[len('Honest framing'):].strip()
        parts.append(f"**Honest framing:** {honest}")
    return ' '.join(parts)


def _format_klk_prompts(uc: dict):
    """KLK UC steps -> Cowork prompts; final extra step = UC-tailored HTML artifact."""
    base_steps = len(uc['prompts'])
    total = base_steps + 1  # +1 for the HTML artifact step
    out = []
    for i, p in enumerate(uc['prompts']):
        # Adjust the step count so 'Step N of total' references the new total
        instr = _format_instr_klk(uc, i, base_steps)
        # Rewrite the "Step X of Y" to use the expanded total
        instr = instr.replace(f"Step {i+1} of {base_steps}", f"Step {i+1} of {total}")
        out.append({'instr': instr, 'prompt': p['text']})
    # Append the HTML artifact step
    archetype, brief = KLK_HTML_ARCHETYPE.get(uc['id'], ('dashboard', 'Executive summary dashboard for this UC.'))
    html_p = _html_artifact_prompt(
        uc['title'], archetype, brief,
        uc.get('files', []),
        deliverable_note=f"This is Step {total} of {total}.",
    )
    out.append(html_p)
    return out


def _format_kibb_brc_prompts(items):
    titles_by_id = {
        'p2-1': ('BRC Prep · Step 1 of 7', 'Research – Vendor governance scan'),
        'p2-2': ('BRC Prep · Step 2 of 7', 'Draft – Risk briefing memo'),
        'p2-3': ('BRC Prep · Step 3 of 7', 'Draft – Board circular'),
        'p3-1': ('BRC Build · Step 4 of 7', 'Brief – CFO talking points'),
        'p3-2': ('BRC Build · Step 5 of 7', 'Build – Board Risk Committee deck'),
        'p3-3': ('BRC Build · Step 6 of 7', 'Wrap – Post-meeting actions email'),
    }
    out = []
    for it in items:
        pid = it.get('id')
        step_label, step_title = titles_by_id.get(pid, (pid, ''))
        instr = (f"**Cowork Runbook · Board Risk Committee End-to-End · {step_label}** "
                 f"({step_title}). Pattern: Structured Pack with Citations. "
                 f"Category: Investment Banking · Group CFO. "
                 f"Apps: Researcher · Word · PowerPoint · Outlook.")
        if pid == 'p2-1':
            instr += (" Sample source files (attach via 📎 Knowledge): "
                      "IB_07_Segment_PnL.xlsx, IB_08_Vendor_Contract.docx, "
                      "IB_09_BoardRisk_Transcript.docx, IB_10_Outsourcing_Policy.docx.")
        if pid == 'p3-3':
            instr += (" **Honest framing:** Researcher-grade synthesis but the "
                      "Group CFO must hand-review every red rating before the BRC "
                      "pack leaves the building — BRC papers are legal record.")
        out.append({'instr': instr, 'prompt': it['text']})
    # Final Step 7: HTML artifact
    archetype, brief = KIBB_BRC_HTML_ARCHETYPE
    out.append(_html_artifact_prompt(
        'Board Risk Committee End-to-End', archetype, brief,
        ['IB_07_Segment_PnL.xlsx', 'IB_08_Vendor_Contract.docx',
         'IB_09_BoardRisk_Transcript.docx', 'IB_10_Outsourcing_Policy.docx'],
        deliverable_note='This is Step 7 of 7.',
    ))
    return out


def _format_kibb_card_prompts(card: dict):
    title = card.get('title', '')
    desc = card.get('description', '')
    apps = ' · '.join(card.get('apps', []) or [])
    files = card.get('files', []) or []
    complexity = card.get('complexity', '')
    watch = card.get('watch', '')
    honest = card.get('honest', '')
    base_prompts = card.get('prompts', []) or []
    base_steps = len(base_prompts)
    total = base_steps + 1  # +1 for HTML artifact

    out = []
    for i, p in enumerate(base_prompts):
        label = p.get('label', '') or f'Step {i+1}'
        step = f"Step {i+1} of {total}"
        instr = (f"**Cowork Runbook · {title} · {step}** ({label}). "
                 f"Pattern: {desc[:160]}{'...' if len(desc) > 160 else ''} "
                 f"Apps: {apps}. Complexity: {complexity}.")
        if i == 0 and files:
            flist = ', '.join(files[:6])
            instr += f" Sample source files (attach via 📎 Knowledge): {flist}."
        if i == 0 and watch:
            instr += f" **What to watch:** {watch}"
        if i == base_steps - 1 and honest:
            instr += f" **Honest framing:** {honest}"
        out.append({'instr': instr, 'prompt': p['text']})
    # Append HTML artifact step
    archetype, brief = KIBB_CARD_HTML_ARCHETYPE.get(card.get('slug', ''),
                                                    ('dashboard', f'Executive summary dashboard for {title}.'))
    out.append(_html_artifact_prompt(
        title, archetype, brief, files,
        deliverable_note=f"This is Step {total} of {total}.",
    ))
    return out


def _append_to_cowork(entry, new_prompts):
    """Append prompts to entry's Cowork tool block; idempotent by 60-char prefix.
    Also clones EN -> promptsID so ID locale carries the new content; downstream
    id_to_bm_swaps then auto-fills BM. Returns count actually appended."""
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
    """Append the runbook's sample file names to the entry's files[] array,
    deduplicated. Mutates entry['files'] in place. Returns count of new files
    added."""
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
def inject_customer_runbooks(all_entries):
    """Mutates entries in place; returns dict with prompt + file counts."""
    rb = _load_runbooks()
    if not rb:
        return {'entries': 0, 'prompts': 0, 'files': 0}

    by_id = {e.get('id'): e for e in all_entries if e.get('id')}

    touched = set()
    n_prompts = 0
    n_files = 0

    # 1) KLK 10 UCs
    klk = {uc['id']: uc for uc in rb.get('klk_runbook', [])}
    for rb_id, target_eid in KLK_ROUTING.items():
        uc = klk.get(rb_id)
        if not uc:
            continue
        entry = by_id.get(target_eid)
        if not entry:
            continue
        n_prompts += _append_to_cowork(entry, _format_klk_prompts(uc))
        n_files += _augment_files(entry, uc.get('files', []))
        if entry:
            touched.add(target_eid)

    # 2) KIBB BRC -> investment-banking
    kibb_brc = rb.get('kibb_brc_runbook', [])
    if kibb_brc:
        entry = by_id.get(KIBB_BRC_TARGET)
        if entry:
            n_prompts += _append_to_cowork(entry, _format_kibb_brc_prompts(kibb_brc))
            n_files += _augment_files(entry, [
                'IB_07_Segment_PnL.xlsx', 'IB_08_Vendor_Contract.docx',
                'IB_09_BoardRisk_Transcript.docx', 'IB_10_Outsourcing_Policy.docx',
            ])
            touched.add(KIBB_BRC_TARGET)

    # 3) KIBB Cowork cards (15 UCs)
    cards_by_slug = {c['slug']: c for c in rb.get('kibb_cowork_cards', [])}
    for slug, target_eid in KIBB_COWORK_ROUTING.items():
        card = cards_by_slug.get(slug)
        if not card:
            continue
        entry = by_id.get(target_eid)
        if not entry:
            continue
        n_prompts += _append_to_cowork(entry, _format_kibb_card_prompts(card))
        n_files += _augment_files(entry, card.get('files', []))
        touched.add(target_eid)

    return {'entries': len(touched), 'prompts': n_prompts, 'files': n_files}
