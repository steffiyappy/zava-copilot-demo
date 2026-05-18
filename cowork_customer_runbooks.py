"""
cowork_customer_runbooks.py

Injects the KLK Cowork Runbook (10 UCs, ~26 prompts) and KIBB BRC runbook
(Exercises 2 + 3, 6 prompts) into the matching Zava hub entries' Cowork
tool blocks.

User feedback: "Did you see the KIBB page? and the KLK page? on the cowork
runbook? You need to put those into the main hub in either the industries
and/or the departments."

Approach:
- Read tools/_customer_runbooks.json (produced by tools/_extract_runbook.py).
- For each KLK UC, route to the matching Zava entry (industry or dept) via
  CATEGORY_MAP. Append each prompt as a new entry in the Cowork tool block's
  prompts[] array. Use the original UC title + prompt-step title as the
  instruction text, prefixed with "Runbook · UC{n} · Step P{m}" so the user
  can see which customer-runbook step they're running.
- For KIBB BRC, append Exercises 2 + 3 to the investment-banking entry's
  Cowork block.

Routing decisions (one UC -> 1-2 entries to avoid duplication):
  rb-1 Site Spreading + Parity Check  -> industrial-manufacturing
  rb-2 Capex Model -> Interactive App -> dept-strategy
  rb-3 Investment Council Riverside   -> property-development
  rb-4 Bank Statement Extraction      -> dept-finance
  rb-5 Recursive UBO + Sanctions      -> dept-procurement
  rb-6 Counterparty Underwriting Memo -> dept-risk
  rb-7 Top-50 Talent Review Council   -> dept-hr
  rb-8 Quarterly Results Spreading    -> dept-investor-relations
  rb-9 Multi-Site GHG Standardisation -> dept-esg
  rb-10 Group P&L Interactive App     -> diversified-conglomerate

  KIBB BRC ex2 + ex3 -> investment-banking

Wired into build_master.py AFTER cowork_html_artifacts and BEFORE the
approval-gate + recipient-diversification passes so those passes process
the new prompts.

License: T_COWORK = FRONTIER (unchanged).
Persona arrays auto-padded by util.tool() (commit 79fa5f8).
Idempotency via unique customer-runbook UC titles + step numbers.
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

KIBB_TARGET = 'investment-banking'


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


def _format_instr(uc: dict, prompt_idx: int, total_steps: int) -> str:
    """Build the instruction text shown above the prompt."""
    parts = []
    # Step header
    step = f"Step {prompt_idx+1} of {total_steps}"
    parts.append(f"**Cowork Runbook · {uc['title']} · {step}** "
                 f"({uc['prompts'][prompt_idx]['title']}). "
                 f"Pattern: {uc.get('pattern', '').replace('Pattern · ', '')}. "
                 f"Category: {uc.get('category', '')}. "
                 f"Apps: {uc.get('apps', '').replace('Apps · ', '')}.")
    # Add sample files reference on first step only
    if prompt_idx == 0 and uc.get('files'):
        flist = ', '.join(uc['files'][:6])
        parts.append(f"Sample source files (attach via 📎 Knowledge): {flist}.")
    # Add honest framing on the last step
    if prompt_idx == total_steps - 1 and uc.get('honest'):
        # honest may have prefix "Honest framing" — strip
        honest = uc['honest']
        if honest.lower().startswith('honest framing'):
            honest = honest[len('Honest framing'):].strip()
        parts.append(f"**Honest framing:** {honest}")
    return ' '.join(parts)


def _format_klk_prompts(uc: dict):
    """Turn a KLK UC into a list of {'instr', 'prompt'} dicts."""
    total = len(uc['prompts'])
    out = []
    for i, p in enumerate(uc['prompts']):
        out.append({
            'instr': _format_instr(uc, i, total),
            'prompt': p['text'],
        })
    return out


def _format_kibb_prompts(items):
    """Group KIBB Ex2 + Ex3 into Cowork prompts.

    Ex2 = BRC pack preparation (research + draft memo + draft circular)
    Ex3 = BRC pack build (deck + Q&A + briefing email)
    """
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
                      "Group CFO must hand-review every red rating before the BRC pack "
                      "leaves the building — BRC papers are legal record.")
        out.append({'instr': instr, 'prompt': it['text']})
    return out


# ── Main API ────────────────────────────────────────────────────────────────
def inject_customer_runbooks(all_entries):
    """all_entries: a single flat list of entries (industries + departments).

    Walks each entry; if its id matches a routing target, finds the Cowork
    tool block and appends the runbook prompts. Mutates in place; returns
    (n_entries_touched, n_prompts_added).
    """
    rb = _load_runbooks()
    if not rb:
        return 0, 0

    # Build entry-id -> entry lookup
    by_id = {e.get('id'): e for e in all_entries if e.get('id')}

    n_entries = 0
    n_prompts = 0

    # KLK: route 10 UCs
    klk = {uc['id']: uc for uc in rb.get('klk_runbook', [])}
    for rb_id, target_eid in KLK_ROUTING.items():
        uc = klk.get(rb_id)
        if not uc:
            continue
        entry = by_id.get(target_eid)
        if not entry:
            continue
        tb = _find_cowork_block(entry)
        if not tb:
            continue
        new_prompts = _format_klk_prompts(uc)

        existing = tb.get('prompts') or []
        # Idempotency: skip if any new prompt's first 60 chars already present
        existing_starts = {(p.get('prompt') or '')[:60] for p in existing if isinstance(p, dict)}
        to_add = [p for p in new_prompts
                  if (p['prompt'][:60] not in existing_starts)]
        if not to_add:
            continue

        tb['prompts'] = list(existing) + to_add
        # Mirror to promptsID — best-effort: clone EN (ID auto-fill happens downstream via id_to_bm_swaps)
        existing_id = tb.get('promptsID') or []
        tb['promptsID'] = list(existing_id) + [dict(p) for p in to_add]

        n_entries += 1
        n_prompts += len(to_add)

    # KIBB: route 6 prompts to investment-banking
    kibb_items = rb.get('kibb_brc_runbook', [])
    if kibb_items:
        entry = by_id.get(KIBB_TARGET)
        if entry:
            tb = _find_cowork_block(entry)
            if tb:
                new_prompts = _format_kibb_prompts(kibb_items)
                existing = tb.get('prompts') or []
                existing_starts = {(p.get('prompt') or '')[:60] for p in existing if isinstance(p, dict)}
                to_add = [p for p in new_prompts
                          if (p['prompt'][:60] not in existing_starts)]
                if to_add:
                    tb['prompts'] = list(existing) + to_add
                    existing_id = tb.get('promptsID') or []
                    tb['promptsID'] = list(existing_id) + [dict(p) for p in to_add]
                    n_entries += 1
                    n_prompts += len(to_add)

    return n_entries, n_prompts
