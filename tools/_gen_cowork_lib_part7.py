"""Generate _cowork_lib_part7.py — Cowork Library cards for the customer
runbook UCs (KLK + KIBB Cowork + Regulator). Run once; output is the
hand-edited target file.

Strategy: each runbook UC becomes ONE Cowork Library card with a single
"fan-out" prompt that concatenates all the runbook steps into a single
Cowork delegation (mirroring uc-ib-brc-prep's STEP 1 / STEP 2 / ... pattern).
"""
import json
import sys
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# ── Load KLK + KIBB runbook JSON ─────────────────────────────────────────
with open(ROOT / 'tools' / '_customer_runbooks.json', 'r', encoding='utf-8') as f:
    RB = json.load(f)

# ── Load regulator runbook module ────────────────────────────────────────
sys.path.insert(0, str(ROOT))
from cowork_regulator_runbook import REGULATOR_USE_CASES, PRIMARY_ROUTING, SECONDARY_ROUTING

# ── Helpers ──────────────────────────────────────────────────────────────
def py_repr(s):
    return repr(s)

def emit_files_tuples(file_list):
    out = []
    for f in file_list:
        if not f or not isinstance(f, str):
            continue
        ext = f.rsplit('.', 1)[-1].lower() if '.' in f else 'docx'
        out.append((f, ext))
    return out

def list_str(items, indent=8):
    pad = ' ' * indent
    if not items:
        return '[]'
    parts = ['[']
    for it in items:
        parts.append(f"{pad}{py_repr(it)},")
    parts.append(' ' * (indent - 4) + ']')
    return '\n'.join(parts)

def sample_files_str(tuples, indent=8):
    pad = ' ' * indent
    if not tuples:
        return '[]'
    parts = ['[']
    for f, ext in tuples:
        parts.append(f"{pad}({py_repr(f)}, {py_repr(ext)}),")
    parts.append(' ' * (indent - 4) + ']')
    return '\n'.join(parts)

def prompts_str(prompts, indent=8):
    pad = ' ' * indent
    if not prompts:
        return '[]'
    parts = ['[']
    for p in prompts:
        parts.append(pad + '{')
        parts.append(pad + "    'label': " + py_repr(p['label']) + ',')
        parts.append(pad + "    'text': (")
        # split text into reasonable chunks
        text = p['text']
        # emit as a single string literal
        parts.append(pad + '        ' + py_repr(text))
        parts.append(pad + "    ),")
        parts.append(pad + '},')
    parts.append(' ' * (indent - 4) + ']')
    return '\n'.join(parts)


def render_card(card_id: str, c: dict) -> str:
    """Render one card to a Python dict literal in the file."""
    out = []
    out.append(f"CARDS[{py_repr(card_id)}] = {{")
    out.append(f"    'title': {py_repr(c['title'])},")
    out.append(f"    'dept_tag': {py_repr(c['dept_tag'])},")
    out.append(f"    'industry_tag': {py_repr(c['industry_tag'])},")
    out.append(f"    'complexity': {py_repr(c['complexity'])},")
    out.append(f"    'apps': {list_str(c['apps'], indent=8)},")
    out.append(f"    'desc': {py_repr(c['desc'])},")
    out.append(f"    'skills': {list_str(c['skills'], indent=8)},")
    out.append(f"    'instructions': {list_str(c['instructions'], indent=8)},")
    out.append(f"    'sample_files': {sample_files_str(c['sample_files'], indent=8)},")
    out.append(f"    'prompts': {prompts_str(c['prompts'], indent=8)},")
    out.append(f"    'expected': {list_str(c['expected'], indent=8)},")
    out.append(f"    'watch': {list_str(c['watch'], indent=8)},")
    out.append(f"    'honest': {py_repr(c['honest'])},")
    out.append(f"    'tips': {list_str(c['tips'], indent=8)},")
    out.append("}")
    return '\n'.join(out)


# ── Build KLK cards from runbook JSON ────────────────────────────────────
KLK_META = {
    'rb-1':  {'dept_tag': 'Operations & Manufacturing', 'industry_tag': 'Industrial Manufacturing',
              'complexity': 'advanced'},
    'rb-2':  {'dept_tag': 'Strategy & Operations', 'industry_tag': 'Industrial Manufacturing',
              'complexity': 'advanced'},
    'rb-3':  {'dept_tag': 'Strategy & Operations', 'industry_tag': 'Property Development',
              'complexity': 'advanced'},
    'rb-4':  {'dept_tag': 'Finance', 'industry_tag': 'Conglomerate',
              'complexity': 'intermediate'},
    'rb-5':  {'dept_tag': 'Procurement & Risk', 'industry_tag': 'Conglomerate',
              'complexity': 'advanced'},
    'rb-6':  {'dept_tag': 'Risk & Credit', 'industry_tag': 'Conglomerate',
              'complexity': 'advanced'},
    'rb-7':  {'dept_tag': 'HR & Talent', 'industry_tag': 'Conglomerate',
              'complexity': 'advanced'},
    'rb-8':  {'dept_tag': 'Investor Relations', 'industry_tag': 'Conglomerate',
              'complexity': 'advanced'},
    'rb-9':  {'dept_tag': 'Sustainability', 'industry_tag': 'Conglomerate',
              'complexity': 'advanced'},
    'rb-10': {'dept_tag': 'Strategy & Operations', 'industry_tag': 'Conglomerate',
              'complexity': 'advanced'},
}

# id -> (slug, html_archetype label hint for desc)
KLK_SLUG = {
    'rb-1':  ('klk-site-spreading', 'multi-site KPI heatmap'),
    'rb-2':  ('klk-capex-scenario', 'interactive Capex scenario app'),
    'rb-3':  ('klk-investment-council', 'Riverside Phase 3 timeline'),
    'rb-4':  ('klk-bank-statement', 'extraction QA dashboard'),
    'rb-5':  ('klk-ubo-sanctions', 'UBO risk grid'),
    'rb-6':  ('klk-counterparty-memo', 'counterparty exposure dashboard'),
    'rb-7':  ('klk-talent-council', 'Top-50 talent kanban'),
    'rb-8':  ('klk-quarterly-spread', 'QoQ parity heatmap'),
    'rb-9':  ('klk-ghg-cdp', 'CDP-ready GHG dashboard'),
    'rb-10': ('klk-group-pnl-app', 'interactive Group P&L strategy app'),
}


def build_klk_card(uc: dict) -> tuple:
    """Build (card_id, card_dict) for one KLK UC."""
    meta = KLK_META[uc['id']]
    slug, html_brief = KLK_SLUG[uc['id']]
    card_id = f"uc-{slug}"

    # Combine all sub-prompts into one fan-out
    steps = uc.get('prompts', [])
    if len(steps) == 1:
        prompt_text = steps[0].get('text', '')
        label = steps[0].get('title', 'Run the runbook')
    else:
        parts = []
        for i, s in enumerate(steps, 1):
            t = s.get('title', f'Step {i}')
            parts.append(f"STEP {i} — {t}.\n\n{s.get('text', '')}")
        prompt_text = '\n\n'.join(parts)
        label = f"{uc['title']} — {len(steps)}-step fan-out"

    apps_str = uc.get('apps', '') or ''
    apps_list = [a.strip() for a in apps_str.replace('Apps · ', '').split(' · ') if a.strip()]
    if not apps_list:
        apps_list = ['Word', 'Excel', 'Outlook', 'Teams']

    files = uc.get('files', []) or []

    card = {
        'title': uc['title'],
        'dept_tag': meta['dept_tag'],
        'industry_tag': meta['industry_tag'],
        'complexity': meta['complexity'],
        'apps': apps_list,
        'desc': (
            f"KLK demo runbook — {uc['title']}. "
            f"One Cowork delegation that fans out across {len(steps)} steps and ends in an "
            f"interactive {html_brief}."
        ),
        'skills': [
            'Multi-step Cowork delegation with cross-deliverable consistency',
            'Source-of-truth file attached via 📎 Knowledge with `/` references',
            'Pause-before-action choreography on outbound communications',
        ],
        'instructions': [
            'Open Microsoft 365 Copilot Cowork (Frontier required)',
            'Click 📎 Knowledge → attach the sample files listed below',
            'Paste the fan-out prompt — Cowork plans first, executes each step in parallel where safe',
            'Review every deliverable before forwarding; approve any external send explicitly',
        ],
        'sample_files': emit_files_tuples(files[:6]),
        'prompts': [{'label': label, 'text': prompt_text}],
        'expected': [
            f"Outputs across {', '.join(apps_list[:5])}",
            'Source-cited tables and references',
            'Approval-gated email / Teams / calendar invites',
            'Self-contained HTML artifact as the final summary',
        ],
        'watch': [
            'Every number cites the source file + tab/section',
            'Cowork pauses before sending external comms',
            'Cross-app consistency: same KPI value renders identically across all outputs',
        ],
        'honest': (
            uc.get('honest', '') or
            'Cowork drafts everything. The accountable owner must hand-review before forwarding.'
        ),
        'tips': [
            'Swap the sample files for your live ones — the runbook scales identically',
            'For a smaller demo, run only steps 1-2 and skip the HTML artifact step',
            'Add a parallel Teams message to the relevant working group at the end',
        ],
    }
    return card_id, card


# ── Build KIBB Cowork-card cards ─────────────────────────────────────────
KIBB_META = {
    'credit-underwriting-pack':     {'dept_tag': 'Risk & Credit', 'industry_tag': 'Investment Banking', 'complexity': 'advanced'},
    'investment-council':           {'dept_tag': 'Investment Banking', 'industry_tag': 'Investment Banking', 'complexity': 'advanced'},
    'ubo-kyc':                      {'dept_tag': 'Legal & Compliance', 'industry_tag': 'Investment Banking', 'complexity': 'intermediate'},
    'bank-statement-extraction':    {'dept_tag': 'Operations', 'industry_tag': 'Investment Banking', 'complexity': 'intermediate'},
    'financial-spreading':          {'dept_tag': 'Risk & Credit', 'industry_tag': 'Investment Banking', 'complexity': 'advanced'},
    'cashflow-model-app':           {'dept_tag': 'Strategy & Operations', 'industry_tag': 'Investment Banking', 'complexity': 'advanced'},
    'underwriting-decision-engine': {'dept_tag': 'Risk & Credit', 'industry_tag': 'Investment Banking', 'complexity': 'advanced'},
    'it-governance':                {'dept_tag': 'IT & Digital', 'industry_tag': 'Investment Banking', 'complexity': 'intermediate'},
    'rfp-scoring':                  {'dept_tag': 'Procurement', 'industry_tag': 'Conglomerate', 'complexity': 'intermediate'},
    'contract-renewal':             {'dept_tag': 'Legal & Compliance', 'industry_tag': 'Conglomerate', 'complexity': 'intermediate'},
    'onboarding-bundle':            {'dept_tag': 'HR & Talent', 'industry_tag': 'Conglomerate', 'complexity': 'basic'},
    'perf-review-prep':             {'dept_tag': 'HR & Talent', 'industry_tag': 'Conglomerate', 'complexity': 'intermediate'},
    'account-brief':                {'dept_tag': 'Marketing & Sales', 'industry_tag': 'Conglomerate', 'complexity': 'intermediate'},
    'incident-postmortem':          {'dept_tag': 'IT & Digital', 'industry_tag': 'Investment Banking', 'complexity': 'intermediate'},
    'campaign-launch':              {'dept_tag': 'Marketing & Sales', 'industry_tag': 'Conglomerate', 'complexity': 'intermediate'},
}


def build_kibb_card(c: dict) -> tuple:
    slug = c['slug']
    meta = KIBB_META.get(slug, {'dept_tag': 'Operations', 'industry_tag': 'Investment Banking', 'complexity': 'intermediate'})
    card_id = f"uc-kibb-{slug}"

    base_prompts = c.get('prompts', []) or []
    if len(base_prompts) == 1:
        prompt_text = base_prompts[0].get('text', '')
        label = base_prompts[0].get('label', c['title'])
    else:
        parts = []
        for i, p in enumerate(base_prompts, 1):
            lbl = p.get('label', f'Step {i}')
            parts.append(f"STEP {i} — {lbl}.\n\n{p.get('text', '')}")
        prompt_text = '\n\n'.join(parts)
        label = f"{c['title']} — {len(base_prompts)}-step fan-out"

    apps = c.get('apps', []) or ['Word', 'Excel', 'Outlook', 'Teams']
    files = c.get('files', []) or []

    desc = c.get('description', '') or f"KIBB demo runbook — {c['title']}."
    if len(desc) > 220:
        desc = desc[:217].rstrip() + '...'

    card = {
        'title': c['title'],
        'dept_tag': meta['dept_tag'],
        'industry_tag': meta['industry_tag'],
        'complexity': meta['complexity'],
        'apps': apps,
        'desc': desc,
        'skills': [
            'Cowork multi-step delegation from a small file pack',
            'Cite-don\'t-fabricate guardrail with file+section references',
            'Audience-shifted outputs (memo + dashboard + email + Teams)',
        ],
        'instructions': [
            'Open Microsoft 365 Copilot Cowork (Frontier required)',
            'Click 📎 Knowledge → attach the sample files listed below',
            'Paste the fan-out prompt as ONE single message',
            'Approve each step before Cowork sends any external comms',
        ],
        'sample_files': emit_files_tuples(files[:6]),
        'prompts': [{'label': label, 'text': prompt_text}],
        'expected': [
            f"Outputs across {', '.join(apps[:5])}",
            'Source-cited tables / models / draft memos',
            'Approval-gated outbound communications',
            'Final HTML artifact summarising the run',
        ],
        'watch': [
            c.get('watch', '') or 'Every number cites the source file and section',
            'Cowork pauses before any external send',
            'Cross-deliverable consistency on KPI values',
        ],
        'honest': (
            c.get('honest', '') or
            'Cowork drafts; the accountable owner must hand-review before forwarding.'
        ),
        'tips': [
            'Swap sample files for your real pack — the runbook scales identically',
            'For a tighter demo run only the first 2-3 steps',
            'Add a Teams summary message at the end for the working group',
        ],
    }
    return card_id, card


# ── Build Regulator cards ────────────────────────────────────────────────
REG_META = {
    'reg-ipo-prospectus-compliance':   {'dept_tag': 'Risk & Compliance',     'industry_tag': 'Financial Regulator'},
    'reg-complaint-triage':            {'dept_tag': 'Legal & Compliance',    'industry_tag': 'Financial Regulator'},
    'reg-workforce-scenario':          {'dept_tag': 'HR & Talent',           'industry_tag': 'Conglomerate'},
    'reg-investor-education-audit':    {'dept_tag': 'Marketing & Sales',     'industry_tag': 'Financial Regulator'},
    'reg-contract-review':             {'dept_tag': 'Legal & Compliance',    'industry_tag': 'Conglomerate'},
    'reg-tax-application':             {'dept_tag': 'Finance',               'industry_tag': 'Financial Regulator'},
    'reg-policy-paper':                {'dept_tag': 'Strategy & Operations', 'industry_tag': 'Financial Regulator'},
    'reg-procurement-benchmarking':    {'dept_tag': 'Procurement',           'industry_tag': 'Conglomerate'},
    'reg-internal-audit-pack':         {'dept_tag': 'Corporate Secretarial', 'industry_tag': 'Conglomerate'},
}


def build_reg_card(uc: dict) -> tuple:
    slug = uc['slug']
    meta = REG_META[slug]
    card_id = f"uc-{slug}"

    steps = uc.get('steps', [])
    if len(steps) == 1:
        prompt_text = steps[0].get('text', '')
        label = steps[0].get('label', uc['title'])
    else:
        parts = []
        for i, s in enumerate(steps, 1):
            lbl = s.get('label', f'Step {i}')
            parts.append(f"STEP {i} — {lbl}.\n\n{s.get('text', '')}")
        prompt_text = '\n\n'.join(parts)
        label = f"{uc['title']} — {len(steps)}-step fan-out"

    apps = uc.get('apps', []) or ['Word', 'Excel', 'Outlook', 'Teams']
    files = uc.get('files', []) or []

    card = {
        'title': uc['title'],
        'dept_tag': meta['dept_tag'],
        'industry_tag': meta['industry_tag'],
        'complexity': 'advanced',
        'apps': apps,
        'desc': (
            f"Regulator + cross-dept Cowork runbook — {uc['title']}. "
            f"One delegation that fans out across {len(steps)} steps and ends in an interactive "
            f"{uc.get('html_archetype', 'dashboard')} artifact."
        ),
        'skills': [
            'Multi-step regulatory or cross-functional workflow in one Cowork run',
            'Cite-don\'t-fabricate guardrail with rule + page references',
            'Approval-gated outbound communications',
        ],
        'instructions': [
            'Open Microsoft 365 Copilot Cowork (Frontier required)',
            'Click 📎 Knowledge → attach the sample files listed below',
            'Paste the fan-out prompt as ONE single message',
            'Approve every external send (email / Teams / calendar)',
        ],
        'sample_files': emit_files_tuples(files[:6]),
        'prompts': [{'label': label, 'text': prompt_text}],
        'expected': [
            f"Outputs across {', '.join(apps[:5])}",
            'Citations back to the source rule, page, or table',
            'Approval-gated outbound communications',
            'HTML artifact (dashboard / kanban / heatmap)',
        ],
        'watch': [
            uc.get('watch', '') or 'Every finding cites the underlying rule or evidence',
            'Cowork pauses before sending external comms',
            'Cross-deliverable consistency on key numbers and ratings',
        ],
        'honest': (
            uc.get('honest', '') or
            'Cowork drafts; the accountable officer must hand-review before forwarding. Regulatory outputs are legal record.'
        ),
        'tips': [
            'Swap sample files for the live submission pack — the runbook scales identically',
            'For a tighter demo run only the first 2-3 steps',
            'Add a Teams summary message at the end for the case team',
        ],
    }
    return card_id, card


# ── Emit file ─────────────────────────────────────────────────────────────
def main():
    out_path = ROOT / '_cowork_lib_part7.py'
    lines = [
        '# -*- coding: utf-8 -*-',
        '"""Cowork Library cards distilled from the KLK / KIBB / Regulator customer',
        'runbook UCs. Auto-generated by tools/_gen_cowork_lib_part7.py — re-run when',
        'the underlying runbook JSON or regulator module changes."""',
        '',
        'CARDS = {}',
        '',
    ]

    # KLK
    lines.append('# ── KLK runbook UCs (10) ─────────────────────────────────────────────────')
    for uc in RB.get('klk_runbook', []):
        cid, card = build_klk_card(uc)
        lines.append('')
        lines.append(render_card(cid, card))

    # KIBB
    lines.append('')
    lines.append('# ── KIBB Cowork page UCs (15) ────────────────────────────────────────────')
    for c in RB.get('kibb_cowork_cards', []):
        cid, card = build_kibb_card(c)
        lines.append('')
        lines.append(render_card(cid, card))

    # Regulator
    lines.append('')
    lines.append('# ── Regulator + cross-dept UCs (9) ───────────────────────────────────────')
    for uc in REGULATOR_USE_CASES:
        cid, card = build_reg_card(uc)
        lines.append('')
        lines.append(render_card(cid, card))

    text = '\n'.join(lines) + '\n'
    out_path.write_text(text, encoding='utf-8')
    print(f"Wrote {out_path} ({len(text):,} chars)")


if __name__ == '__main__':
    main()
