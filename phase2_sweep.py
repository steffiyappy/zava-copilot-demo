"""Phase 2 mechanical sweep across all 4 dept_data*.py files.

Standardises personas to the 4-cast (Hadar Caspit / Sasha Ouellet / Mod Admin / Daichi Maruyama),
renames Legal & Corporate Secretarial split, and reports stats.

Persona protagonist mapping per plan.md:
- dept-hr        -> Sasha Ouellet  (Group CoS, talent + culture)
- dept-finance   -> Hadar Caspit   (Group CFO)
- dept-legal     -> Hadar Caspit   (CFO sponsors legal escalations)
- dept-risk      -> Hadar Caspit   (CFO chairs Group Risk Committee)
- dept-strategy  -> Mod Admin      (Strategy Director)
- dept-marketing -> Sasha Ouellet  (CoS owns comms)
- dept-esg       -> Daichi Maruyama (IR owns ESG narrative for investors)
- dept-operations-> Mod Admin      (Strategy Director runs ops transformation)
- dept-board     -> Sasha Ouellet  (CoS = Board secretariat = Corp Sec)
"""
import re
from pathlib import Path

PROTAGONIST = {
    'dept-hr': 'Sasha Ouellet',
    'dept-finance': 'Hadar Caspit',
    'dept-legal': 'Hadar Caspit',
    'dept-risk': 'Hadar Caspit',
    'dept-strategy': 'Mod Admin',
    'dept-marketing': 'Sasha Ouellet',
    'dept-esg': 'Daichi Maruyama',
    'dept-operations': 'Mod Admin',
    'dept-board': 'Sasha Ouellet',
}

DEPT_HEADER_RX = re.compile(
    r"""(?:id\s*=\s*'(dept-[a-z]+)'      # dict-form: id='dept-xxx'
        |ind\(\s*'(dept-[a-z]+)'        # call-form: ind('dept-xxx'
        |'(dept-[a-z]+)'\s*,\s*'department'  # multi-line: 'dept-xxx', 'department'
        )""",
    re.VERBOSE,
)

PERSONA_ARRAY_RX = re.compile(
    r"(persona(?:ID)?\s*=\s*\[)([^\[\]]*)(\])",
    re.MULTILINE,
)

ROOT = Path(r"C:\Users\peiyiyap\zava-copilot-demo")
DEPT_FILES = ['dept_data.py', 'dept_data2.py', 'dept_data3.py', 'dept_data4.py']


def find_dept_spans(text):
    """Return list of (dept_id, start_offset). End of each span = start of next or EOF."""
    spans = []
    for m in DEPT_HEADER_RX.finditer(text):
        dept_id = m.group(1) or m.group(2) or m.group(3)
        spans.append((dept_id, m.start()))
    return spans


def rewrite_personas_in_block(block, protagonist):
    """Replace each item in persona=[...] / personaID=[...] arrays with `protagonist`."""
    def _sub(m):
        prefix, body, suffix = m.group(1), m.group(2), m.group(3)
        # Count items by counting commas + 1 (handle empty list)
        body_stripped = body.strip()
        if not body_stripped:
            return m.group(0)
        items = [x.strip() for x in body.split(',') if x.strip()]
        new_body = ','.join(f"'{protagonist}'" for _ in items)
        return f"{prefix}{new_body}{suffix}"

    return PERSONA_ARRAY_RX.sub(_sub, block)


def process_file(path: Path):
    text = path.read_text(encoding='utf-8')
    spans = find_dept_spans(text)
    if not spans:
        return text, 0, 0

    # Build new text by processing each dept block
    new_parts = []
    last_end = 0
    arrays_changed = 0
    items_changed = 0

    for i, (dept_id, start) in enumerate(spans):
        # text before this dept (preserved)
        new_parts.append(text[last_end:start])
        end = spans[i + 1][1] if i + 1 < len(spans) else len(text)
        block = text[start:end]
        protagonist = PROTAGONIST.get(dept_id)
        if protagonist:
            # count arrays for stats
            arr_matches = list(PERSONA_ARRAY_RX.finditer(block))
            arrays_changed += len(arr_matches)
            for am in arr_matches:
                items_changed += len([x for x in am.group(2).split(',') if x.strip()])
            block = rewrite_personas_in_block(block, protagonist)
        new_parts.append(block)
        last_end = end

    new_parts.append(text[last_end:])
    return ''.join(new_parts), arrays_changed, items_changed


def main():
    print('=== Phase 2 Pass A: persona standardisation ===\n')
    total_arrays = 0
    total_items = 0
    for fname in DEPT_FILES:
        p = ROOT / fname
        new_text, arrays, items = process_file(p)
        if arrays:
            p.write_text(new_text, encoding='utf-8')
            print(f"{fname:18s} -> rewrote {arrays:3d} persona arrays, {items:3d} name slots")
        else:
            print(f"{fname:18s} -> no dept blocks found / no changes")
        total_arrays += arrays
        total_items += items

    print(f"\nTOTAL: {total_arrays} arrays, {total_items} persona names standardised")
    print("\n=== Pass B: split Legal & CorpSec, rename dept-board -> dept-corpsec ===\n")

    # Pass B-1: rename dept-legal label (drop CorpSec)
    p_legal = ROOT / 'dept_data2.py'
    legal_text = p_legal.read_text(encoding='utf-8')
    OLD_LEGAL_HEADER = "ind('dept-legal','department','⚖️ Legal & Corporate Secretarial','⚖️','#4A148C','#6A1B9A',"
    NEW_LEGAL_HEADER = "ind('dept-legal','department','⚖️ Legal','⚖️','#4A148C','#6A1B9A',"
    if OLD_LEGAL_HEADER in legal_text:
        legal_text = legal_text.replace(OLD_LEGAL_HEADER, NEW_LEGAL_HEADER)
        p_legal.write_text(legal_text, encoding='utf-8')
        print("dept_data2.py     -> dept-legal renamed to '⚖️ Legal' (CorpSec dropped from label)")
    else:
        print("dept_data2.py     -> dept-legal header already updated or not found (skipped)")

    # Pass B-2: rename dept-board -> dept-corpsec, label '📜 Corporate Secretarial'
    p_board = ROOT / 'dept_data4.py'
    board_text = p_board.read_text(encoding='utf-8')
    OLD_BOARD_HEADER = "    'dept-board', 'department', '🏛 Board & Executive Office', '🏛', '#1A237E', '#283593',"
    NEW_BOARD_HEADER = "    'dept-corpsec', 'department', '📜 Corporate Secretarial', '📜', '#1A237E', '#283593',"
    if OLD_BOARD_HEADER in board_text:
        board_text = board_text.replace(OLD_BOARD_HEADER, NEW_BOARD_HEADER)
        # also flip 'Zava Board' to 'Zava Corporate Secretariat'
        board_text = board_text.replace("'Zava Board',", "'Zava Corporate Secretariat',", 1)
        p_board.write_text(board_text, encoding='utf-8')
        print("dept_data4.py     -> dept-board renamed to dept-corpsec '📜 Corporate Secretarial'")
    else:
        print("dept_data4.py     -> dept-board header already updated or not found (skipped)")


if __name__ == '__main__':
    main()
