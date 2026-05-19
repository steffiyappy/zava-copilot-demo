"""_cowork_lib_html_inject.py

Append ONE HTML artifact prompt to every USE_CASES card in the Cowork Library
that does not already have one. The prompt asks Cowork to produce a
SELF-CONTAINED interactive HTML deliverable — dashboard / kanban / heatmap /
timeline / matrix — best matching the card's archetype, with comprehensive
filter + slice-and-dice controls.

Imported and invoked by _cowork_library.py once USE_CASES is fully merged
(after parts 2-7). Idempotent via the marker string ZAVA_HTML_ART_LIB_v1.

Result: every card on the standalone 🤝 Cowork sidebar tab carries an extra
prompt at the end called "Build interactive HTML artifact (filters + drill-
down)" that the presenter can fire as the final step of the runbook.
"""
import re

_MARK = 'ZAVA_HTML_ART_LIB_v1'  # idempotency phrase appears in the prompt text

# ── Keywords -> archetype mapping ──────────────────────────────────────
_KW = [
    # (regex, archetype)
    (re.compile(r'\b(kanban|onboarding|launch|campaign|outage|incident|postmortem|recall|response|recovery|sprint|stand[- ]?up|playbook|workflow)\b', re.I), 'KANBAN'),
    (re.compile(r'\b(heatmap|risk appetite|risk register|esg|control|materiality|compliance check|audit pack|findings)\b', re.I), 'HEATMAP'),
    (re.compile(r'\b(pipeline|timeline|gantt|funnel|stage|milestone|RFP|scor(ing|ecard)|application processing|tax application|prospectus|policy paper)\b', re.I), 'PIPELINE'),
    (re.compile(r'\b(matrix|score ?card|kyc|ubo|sanction|beneficial owner|decision engine|underwriting)\b', re.I), 'MATRIX'),
    # default -> DASHBOARD
]


def _archetype_for(card):
    """Pick an HTML archetype from card title + dept_tag + first prompt label."""
    blob = ' '.join([
        str(card.get('title') or ''),
        str(card.get('dept_tag') or ''),
        str(card.get('industry_tag') or ''),
        ' '.join(str(p.get('label') or '') for p in (card.get('prompts') or [])[:2] if isinstance(p, dict)),
    ])
    for pat, arch in _KW:
        if pat.search(blob):
            return arch
    return 'DASHBOARD'


# ── Archetype prompt templates ─────────────────────────────────────────
# Each template uses {TITLE} / {ENTITY} / {FILES} placeholders.
_DASHBOARD = (
    'Cowork: produce a SELF-CONTAINED interactive HTML executive dashboard '
    'titled "{TITLE}" using {FILES} as the source of truth. Output ONE .html '
    'file (inline CSS + inline JS, ABSOLUTELY NO external CDN) so it opens '
    'cleanly offline. The dashboard must be COMPREHENSIVE and let the user '
    'slice-and-dice every dimension. Required structure:\n'
    '• TOP FILTER BAR (sticky) — multi-select chips for the 3 most important '
    'dimensions (e.g. business unit, region, status, owner); free-text search '
    'box; date-range picker (last 30d / quarter / FY / custom); reset button. '
    'All filters apply instantly to every panel below — no refresh.\n'
    '• KPI STRIP — 6 KPI cards with current value, period delta vs prior, '
    'colour coded vs target threshold, and an inline 12-period sparkline '
    'drawn on Canvas.\n'
    '• MAIN GRID — 2×2 panels: trend line chart, top-N bar chart, distribution '
    'pie/donut, and a heat-strip showing concentration; each panel reacts '
    'to filter bar selections.\n'
    '• DRILL-DOWN TABLE — sortable + searchable table of every underlying row '
    'with column-show/hide toggles; click a row to open a side-panel with '
    'full record detail + linked source files. Includes an "Export CSV of '
    'current view" button that respects active filters.\n'
    '• ALERTS PANEL — auto-flag anomalies / threshold breaches with one-line '
    'narratives.\n'
    '• Theme: Zava navy (#1F2D55) header, light/dark toggle in the top-right, '
    'sans-serif typography, mobile-responsive.\n'
    'Save the file as "{TITLE} — Dashboard.html" to my OneDrive > Zava '
    'Dashboards folder once Cowork has my approval.'
)

_KANBAN = (
    'Cowork: produce a SELF-CONTAINED interactive HTML kanban board titled '
    '"{TITLE}" using {FILES} as the source of items. Output ONE .html file '
    '(inline CSS + JS, NO external CDN). Make it COMPREHENSIVE and fully '
    'slice-able. Required structure:\n'
    '• TOP FILTER BAR — multi-select chips for owner, team, priority, status '
    'and tag; free-text search across card title + description; date-range '
    'picker on due-date; reset button. Filters apply live to all columns.\n'
    '• 5 COLUMNS: Backlog · To Do · In Progress · Blocked · Done. Each '
    'column header shows the live count plus the count of overdue items.\n'
    '• CARDS — title, owner avatar, due date (red if overdue), priority chip, '
    'tags. Click a card to open a right-hand details panel with full '
    'description, linked source files, recent activity log, and an inline '
    'comment box.\n'
    '• DRAG TO RE-COLUMN (HTML5 drag-and-drop) — moving a card updates an '
    'in-memory state and triggers a "save changes" button at the top.\n'
    '• SWIMLANES TOGGLE — group by team / priority / tag on demand.\n'
    '• SUMMARY STRIP — totals per column, % done, blocked count, overdue '
    'count, and a "what changed since yesterday" mini-feed.\n'
    '• EXPORT CSV of current filtered view.\n'
    '• Theme: Zava navy header, light/dark toggle.\n'
    'Save the file as "{TITLE} — Kanban.html" to my OneDrive once approved.'
)

_HEATMAP = (
    'Cowork: produce a SELF-CONTAINED interactive HTML risk / compliance / '
    'ESG heatmap titled "{TITLE}" using {FILES} as the source data. Output '
    'ONE .html file (inline CSS + JS, NO external CDN). Required structure:\n'
    '• TOP FILTER BAR — multi-select chips for business unit, risk category, '
    'owner, residual band; date-range on last-reviewed; free-text search; '
    'reset button. Filters update both the matrix and the lists below.\n'
    '• 5×5 PROBABILITY × IMPACT MATRIX — colour-coded cells (green 1-2 / '
    'amber 3-4 / red 5), each cell shows the count of items landing in it. '
    'Click a cell to open a side panel listing every issue in that cell with '
    'owner, mitigation status, due date, and a link to the source file.\n'
    '• DUAL STRIPS BELOW THE MATRIX — "Top 10 Inherent" and "Top 10 '
    'Residual"; each row is sortable and clickable, opens the same side '
    'panel.\n'
    '• HEAT-TIMELINE — bottom strip of last 12 monthly snapshots showing the '
    'count of red-cell items per month so the audience sees the trend.\n'
    '• DRILL-DOWN TABLE — sortable + searchable table of every item with '
    'column-show/hide toggles. Export CSV button respects filters.\n'
    '• Theme: Zava navy header, light/dark toggle, mobile-responsive.\n'
    'Save as "{TITLE} — Heatmap.html" to my OneDrive once approved.'
)

_PIPELINE = (
    'Cowork: produce a SELF-CONTAINED interactive HTML pipeline / timeline '
    'view titled "{TITLE}" using {FILES} as the source of items. Output ONE '
    '.html file (inline CSS + JS, NO external CDN). Required structure:\n'
    '• TOP FILTER BAR — multi-select chips for stage, owner, priority, '
    'team / sector; date-range slider on expected close / submission date; '
    'free-text search; reset button. Filters apply live across all views.\n'
    '• STAGE FUNNEL — horizontal funnel showing count + total value at each '
    'stage; click a stage to filter the timeline + table below.\n'
    '• GANTT-STYLE TIMELINE — horizontal bars per item across a 12-month '
    'X-axis with milestones plotted as diamonds; colour by owner or stage; '
    'today line drawn in red; hover a bar to see KPI tooltip; click to open '
    'side-panel with full item detail + linked source files.\n'
    '• KPI STRIP — 5 cards: count by stage, weighted value, average cycle '
    'time, slipping count, won/lost ratio.\n'
    '• DRILL-DOWN TABLE at bottom — sortable, searchable, column toggles, '
    'CSV export of filtered view.\n'
    '• Theme: Zava navy header, light/dark toggle.\n'
    'Save as "{TITLE} — Pipeline.html" to my OneDrive once approved.'
)

_MATRIX = (
    'Cowork: produce a SELF-CONTAINED interactive HTML decision / scoring '
    'matrix titled "{TITLE}" using {FILES} as the source data. Output ONE '
    '.html file (inline CSS + JS, NO external CDN). Required structure:\n'
    '• TOP FILTER BAR — multi-select chips for entity type, category, '
    'analyst / owner, decision band; free-text search; reset button.\n'
    '• MAIN MATRIX — rows = items being evaluated, columns = criteria. Each '
    'cell shows the score (1-5) colour-coded; click a cell to open a side-'
    'panel with the rationale, source file reference, and audit trail.\n'
    '• AGGREGATE COLUMN on the right — weighted score, recommended band '
    '(GO / HOLD / NO-GO), and a confidence badge.\n'
    '• RADAR CHART panel — top 3 ranked items rendered on Canvas so the '
    'audience can compare strengths visually; selectable from a dropdown.\n'
    '• AUDIT STRIP — last reviewer, last change, citations count; click to '
    'expand into the full audit log.\n'
    '• SORTABLE TABLE below the matrix mirrors the same data with column '
    'show/hide toggles and CSV export of the current filtered view.\n'
    '• Theme: Zava navy header, light/dark toggle, mobile responsive.\n'
    'Save as "{TITLE} — Scoring Matrix.html" to my OneDrive once approved.'
)

_TEMPLATES = {
    'DASHBOARD': ('Build interactive HTML dashboard (filters + drill-down)', _DASHBOARD),
    'KANBAN':    ('Build interactive HTML kanban board (filters + drag)', _KANBAN),
    'HEATMAP':   ('Build interactive HTML risk/ESG heatmap (filters + drill-down)', _HEATMAP),
    'PIPELINE':  ('Build interactive HTML pipeline timeline (filters + drill-down)', _PIPELINE),
    'MATRIX':    ('Build interactive HTML scoring matrix (filters + drill-down)', _MATRIX),
}

# ── HTML hint detector (skip cards that already have one) ──────────────
_HTML_HINT = re.compile(
    r'\b(self[- ]contained html|html dashboard|html kanban|html heatmap|html '
    r'pipeline|html matrix|html timeline|html artifact|html artefact|'
    r'interactive html|inline css \+ inline js)\b', re.IGNORECASE)


def _file_list_for(card):
    """Return a comma-joined list of sample_files names for the {FILES} slot."""
    sf = card.get('sample_files') or []
    names = []
    for item in sf[:5]:
        if isinstance(item, (list, tuple)) and item:
            names.append(item[0])
        elif isinstance(item, dict):
            names.append(item.get('name') or item.get('n') or '')
        elif isinstance(item, str):
            names.append(item)
    names = [n for n in names if n]
    if not names:
        return 'the source files attached to this Cowork session'
    if len(names) == 1:
        return names[0]
    return ', '.join(names[:-1]) + ' and ' + names[-1]


def _entity_for(card):
    return card.get('industry_tag') or card.get('dept_tag') or 'Zava Conglomerate'


def inject_html_prompts(use_cases):
    """Walk USE_CASES dict, append HTML artifact prompt to each card lacking one.

    Returns (n_added, n_skipped_already).
    """
    added = 0; skipped = 0
    for cid, card in use_cases.items():
        if not isinstance(card, dict):
            continue
        prompts = card.get('prompts')
        if not isinstance(prompts, list):
            prompts = []
            card['prompts'] = prompts
        # Skip if any existing prompt already references HTML artifact creation
        combined = ' '.join(p.get('text', '') + ' ' + p.get('label', '')
                            for p in prompts if isinstance(p, dict))
        if _HTML_HINT.search(combined) or _MARK in combined:
            skipped += 1
            continue
        arch = _archetype_for(card)
        label, body_tmpl = _TEMPLATES[arch]
        title = card.get('title') or cid
        files = _file_list_for(card)
        entity = _entity_for(card)
        body = body_tmpl.format(TITLE=title, ENTITY=entity, FILES=files)
        # Embed the idempotency marker as an HTML comment-like tail (invisible
        # in chat-rendered prompts but detectable for re-runs).
        body = body + f'\n\n<!-- {_MARK} -->'
        prompts.append({
            'label': label,
            'text': body,
        })
        added += 1
    return added, skipped
