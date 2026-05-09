"""Phase 3 Pass A: persona standardisation across all 28 industries (ind_batch1-9.py).

Rules applied:
1. "Hadar — <suffix>"     -> "Hadar Caspit"        (strip role suffix)
2. "Sasha — <suffix>"     -> "Sasha Ouellet"
3. "Daichi — <suffix>"    -> "Daichi Maruyama"
4. "Mod Admin — <suffix>" -> "Mod Admin"
5. Any other ad-hoc name  -> "Hadar Caspit"        (default protagonist)

This implements user feedback #12 ("remove the you are 'what name', title... just say you are a persona instead of putting the name") and standardises to the 4-cast across the whole app.
"""
import re
from pathlib import Path

ROOT = Path(r"C:\Users\peiyiyap\zava-copilot-demo")
FILES = [f'ind_batch{i}.py' for i in range(1, 10)]

STANDARD = {'Sasha Ouellet', 'Hadar Caspit', 'Mod Admin', 'Daichi Maruyama'}

DASH_RX = re.compile(r"^(Hadar|Sasha|Daichi|Mod Admin)\s*[—–-].*$")

def normalise(name: str) -> str:
    n = name.strip()
    if n in STANDARD:
        return n
    m = DASH_RX.match(n)
    if m:
        return {
            'Hadar': 'Hadar Caspit',
            'Sasha': 'Sasha Ouellet',
            'Daichi': 'Daichi Maruyama',
            'Mod Admin': 'Mod Admin',
        }[m.group(1)]
    # Ad-hoc name -> default to Hadar Caspit (Group CFO is the most common protagonist
    # across financial/strategic prompts, and user can refine per industry later)
    return 'Hadar Caspit'


PERSONA_ARRAY_RX = re.compile(
    r"(persona(?:ID)?\s*=\s*\[)([^\[\]]*)(\])",
    re.MULTILINE,
)


def rewrite_text(text):
    arrays_changed = 0
    items_changed = 0

    def _sub(m):
        nonlocal arrays_changed, items_changed
        prefix, body, suffix = m.group(1), m.group(2), m.group(3)
        if not body.strip():
            return m.group(0)
        items = [x.strip() for x in body.split(',')]
        items = [x for x in items if x]
        # Strip surrounding quotes from each item
        new_items = []
        any_changed = False
        for it in items:
            inner = it.strip("'\"")
            new = normalise(inner)
            if new != inner:
                any_changed = True
                items_changed += 1
            new_items.append(f"'{new}'")
        if any_changed:
            arrays_changed += 1
        return f"{prefix}{','.join(new_items)}{suffix}"

    new_text = PERSONA_ARRAY_RX.sub(_sub, text)
    return new_text, arrays_changed, items_changed


def main():
    print('=== Phase 3 Pass A: persona standardisation across 28 industries ===\n')
    grand_arr = 0
    grand_items = 0
    for fname in FILES:
        p = ROOT / fname
        text = p.read_text(encoding='utf-8')
        new_text, arr, items = rewrite_text(text)
        if items:
            p.write_text(new_text, encoding='utf-8')
            print(f"{fname:18s} -> {arr:3d} arrays modified, {items:3d} name slots normalised")
        else:
            print(f"{fname:18s} -> already standardised")
        grand_arr += arr
        grand_items += items
    print(f"\nTOTAL: {grand_arr} arrays modified, {grand_items} persona names normalised")


if __name__ == '__main__':
    main()
