"""
cowork_customer_runbooks.py

Injects the KLK Cowork Runbook (10 UCs, 26 prompts) + KIBB BRC Exercise
runbook (6 prompts) + KIBB Cowork page UCs (15 cards, 16 prompts) into
the matching Zava hub entries' Cowork tool blocks.

User feedback: "Did you see the KIBB page? and the KLK page? on the cowork
runbook? You need to put those into the main hub in either the industries
and/or the departments."  And later: "The KIBB runbook was so comprehensive"
— pointing out the dedicated KIBB Cowork page (15 UC cards, IDs cw-uc-*)
that I missed in the first pass.

Approach:
- Read tools/_customer_runbooks.json (produced by tools/_extract_runbook.py).
- For each runbook UC, route to the matching Zava entry (industry or dept)
  by curated mapping. Append each prompt as a new entry in the Cowork tool
  block's prompts[] array.
- Each prompt's `instr` field carries:
  "Cowork Runbook · {UC Title} · Step N of M" prefix
  + pattern/category/apps pills (from customer page)
  + sample file list (step 1 only)
  + honest-framing callout (final step only)

License: T_COWORK = FRONTIER (unchanged).
Idempotent: skip prompts whose first 60 chars already appear in the entry.
"""
import json
from pathlib import Path

_RUNBOOK_JSON = Path(__file__).parent / 'tools' / '_customer_runbooks.json'

# ── Routing: KLK runbook UC id -> Zava entry id ────────────────────────────
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

# ── Routing: KIBB Cowork page card slug -> Zava entry id ───────────────────
# All 15 cards live in the investment-bank persona but each maps to a
# different department in Zava. Spread them across the matching dept hubs
# (some also onto investment-banking itself).
KIBB_COWORK_ROUTING = {
    'credit-underwriting-pack':     'investment-banking',   # UC01 risk-credit
    'investment-council':           'investment-banking',   # UC02 risk-credit (CIB-style)
    'ubo-kyc':                      'dept-legal',           # UC03 legal-compliance
    'bank-statement-extraction':    'dept-operations',      # UC04 operations
    'financial-spreading':          'dept-risk',            # UC05 risk-credit
    'cashflow-model-app':           'dept-strategy',        # UC06 strategy (2 prompts)
    'underwriting-decision-engine': 'dept-risk',            # UC07 risk-credit
    'it-governance':                'dept-it-digital',      # UC08 it
    'rfp-scoring':                  'dept-procurement',     # UC09 procurement
    'contract-renewal':             'dept-legal',           # UC10 legal-compliance
    'onboarding-bundle':            'dept-hr',              # UC11 hr
    'perf-review-prep':             'dept-hr',              # UC12 hr
    'account-brief':                'dept-marketing',       # UC13 sales-marketing (Zava has no dept-sales)
    'incident-postmortem':          'dept-it-digital',      # UC14 it
    'campaign-launch':              'dept-marketing',       # UC15 sales-marketing
}


# ── Helpers ─────────────────────────────────────────────────────────────────
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
    total = len(uc['prompts'])
    return [{'instr': _format_instr_klk(uc, i, total), 'prompt': p['text']}
            for i, p in enumerate(uc['prompts'])]


def _format_kibb_brc_prompts(items):
    titles_by_id = {
        'p2-1': ('BRC Prep · Step 1 of 6', 'Research – Vendor governance scan'),
        'p2-2': ('BRC Prep · Step 2 of 6', 'Draft – Risk briefing memo'),
        'p2-3': ('BRC Prep · Step 3 of 6', 'Draft – Board circular'),
        'p3-1': ('BRC Build · Step 4 of 6', 'Brief – CFO talking points'),
        'p3-2': ('BRC Build · Step 5 of 6', 'Build – Board Risk Committee deck'),
        'p3-3': ('BRC Build · Step 6 of 6', 'Wrap – Post-meeting actions email'),
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
    return out


def _format_kibb_card_prompts(card: dict):
    """Format a single KIBB Cowork page card into 1+ T_COWORK prompts."""
    title = card.get('title', '')
    desc = card.get('description', '')
    apps = ' · '.join(card.get('apps', []) or [])
    files = card.get('files', []) or []
    complexity = card.get('complexity', '')
    watch = card.get('watch', '')
    honest = card.get('honest', '')
    prompts = card.get('prompts', []) or []
    total = len(prompts)

    out = []
    for i, p in enumerate(prompts):
        label = p.get('label', '') or f'Step {i+1}'
        step = f"Step {i+1} of {total}" if total > 1 else "Single-step run"
        instr = (f"**Cowork Runbook · {title} · {step}** ({label}). "
                 f"Pattern: {desc[:160]}{'...' if len(desc) > 160 else ''} "
                 f"Apps: {apps}. Complexity: {complexity}.")
        if i == 0 and files:
            flist = ', '.join(files[:6])
            instr += f" Sample source files (attach via 📎 Knowledge): {flist}."
        if i == 0 and watch:
            instr += f" **What to watch:** {watch}"
        if i == total - 1 and honest:
            instr += f" **Honest framing:** {honest}"
        out.append({'instr': instr, 'prompt': p['text']})
    return out


def _append_to_cowork(entry, new_prompts):
    """Append prompts to entry's Cowork tool block; idempotent by 60-char prefix.
    Returns the number actually appended."""
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


# ── Main API ────────────────────────────────────────────────────────────────
def inject_customer_runbooks(all_entries):
    """Mutates entries in place; returns (n_entries_touched, n_prompts_added)."""
    rb = _load_runbooks()
    if not rb:
        return 0, 0

    by_id = {e.get('id'): e for e in all_entries if e.get('id')}

    n_entries = 0
    n_prompts = 0
    touched_eids = set()

    # 1) KLK 10 UCs
    klk = {uc['id']: uc for uc in rb.get('klk_runbook', [])}
    for rb_id, target_eid in KLK_ROUTING.items():
        uc = klk.get(rb_id)
        if not uc:
            continue
        entry = by_id.get(target_eid)
        if not entry:
            continue
        added = _append_to_cowork(entry, _format_klk_prompts(uc))
        if added:
            n_prompts += added
            touched_eids.add(target_eid)

    # 2) KIBB BRC (Exercises 2+3) -> investment-banking
    kibb_brc = rb.get('kibb_brc_runbook', [])
    if kibb_brc:
        entry = by_id.get(KIBB_BRC_TARGET)
        if entry:
            added = _append_to_cowork(entry, _format_kibb_brc_prompts(kibb_brc))
            if added:
                n_prompts += added
                touched_eids.add(KIBB_BRC_TARGET)

    # 3) KIBB Cowork page cards (15 UCs, 16 prompts) -> per-dept routing
    cards_by_slug = {c['slug']: c for c in rb.get('kibb_cowork_cards', [])}
    for slug, target_eid in KIBB_COWORK_ROUTING.items():
        card = cards_by_slug.get(slug)
        if not card:
            continue
        entry = by_id.get(target_eid)
        if not entry:
            continue
        added = _append_to_cowork(entry, _format_kibb_card_prompts(card))
        if added:
            n_prompts += added
            touched_eids.add(target_eid)

    return len(touched_eids), n_prompts
