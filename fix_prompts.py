"""
Strip "Open/Upload X. Ask Copilot:" wrapper patterns from all batch files.
Transforms prompts to be directly pasteable (IHH/Contoso HR immersion format).
"""
import re, sys, os

def fix_wrappers(text):
    # Analyst: "Upload X.xlsx to Analyst. [Then ]ask: " or "Upload X.xlsx. Ask Analyst: "
    text = re.sub(r'Upload [A-Za-z0-9_\-\. /]+\.xlsx to Analyst\. (?:Then )?[Aa]sk:\s*', '', text)
    text = re.sub(r'Upload [A-Za-z0-9_\-\. /]+\.xlsx\. Ask Analyst:\s*', '', text)
    text = re.sub(r'Upload [A-Za-z0-9_\-\. /]+\.xlsx and ask:\s*', '', text)
    text = re.sub(r'Upload [A-Za-z0-9_\-\. /]+\.xlsx\. Ask:\s*', '', text)
    text = re.sub(r'Upload [A-Za-z0-9_\-\. /]+\.xlsx\. Then ask:\s*', '', text)

    # Excel: "Open X.xlsx and navigate to the Y sheet. Ask Copilot: " → "Using the Y tab in this workbook,"
    text = re.sub(
        r'Open [A-Za-z0-9_\-\. /]+\.xlsx and navigate to the ([A-Za-z0-9 _\-]+) sheet\. Ask Copilot:\s*',
        r'Using the \1 tab in this workbook, ', text)
    # "Open X.xlsx. Navigate to the Y sheet. Ask Copilot: "
    text = re.sub(
        r'Open [A-Za-z0-9_\-\. /]+\.xlsx\. Navigate to the ([A-Za-z0-9 _\-]+) sheet\. Ask Copilot:\s*',
        r'Using the \1 tab in this workbook, ', text)
    # "Open X.xlsx. Navigate to the Y tab. Ask Copilot: "
    text = re.sub(
        r'Open [A-Za-z0-9_\-\. /]+\.xlsx\. Navigate to the ([A-Za-z0-9 _\-]+) tab\. Ask Copilot:\s*',
        r'Using the \1 tab in this workbook, ', text)

    # "Open X.xlsx. Ask Copilot: " or "Open X.xlsx, ask Copilot: "
    text = re.sub(r'Open [A-Za-z0-9_\-\. /]+\.xlsx[,\.]? [Aa]sk Copilot:\s*', '', text)

    # "Open X.docx. Ask Copilot: "
    text = re.sub(r'Open [A-Za-z0-9_\-\. /]+\.docx[,\.]? [Aa]sk Copilot:\s*', '', text)

    # "Open Email_XX.docx and review the thread. Open Outlook and ask Copilot: "
    text = re.sub(
        r'Open [A-Za-z0-9_\-\. /]+\.docx(?: and review the thread)?\.? Open Outlook and ask Copilot:\s*',
        '', text)

    # "In the same workbook/document, ask Copilot: " → "Using this workbook/document,"
    text = re.sub(r'In the same workbook, ask Copilot:\s*', 'Using this workbook, ', text)
    text = re.sub(r'In the same document, ask Copilot:\s*', 'Using this document, ', text)
    text = re.sub(r'In the same document, ask Copilot to\s*', 'Using this document, ', text)

    # "Ask Copilot in Word/Excel/PPT/Outlook/Teams: "
    text = re.sub(r'Ask Copilot in (?:Word|Excel|PowerPoint|Outlook|Teams):\s*', '', text)

    # "Open an existing recorded Teams meeting recap. Ask Copilot: "
    text = re.sub(r'Open an existing recorded Teams meeting recap\. Ask Copilot:\s*', '', text)
    # "In the same recap/meeting recap, ask Copilot: "
    text = re.sub(r'In the same (?:meeting )?recap, ask Copilot:\s*', '', text)

    # Generic catch-all: "Ask Copilot: " or "ask Copilot: " at start of a prompt string segment
    text = re.sub(r'Ask Copilot:\s*', '', text)
    text = re.sub(r'ask Copilot:\s*', '', text)

    return text


files = [f for f in os.listdir('.') if
         (f.startswith('ind_batch') or f.startswith('dept_data')) and f.endswith('.py')]
files.sort()

total_changes = 0
for fname in files:
    with open(fname, 'r', encoding='utf-8') as f:
        original = f.read()
    fixed = fix_wrappers(original)
    changes = sum(1 for a, b in zip(original.split('\n'), fixed.split('\n')) if a != b)
    if fixed != original:
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(fixed)
        total_changes += changes
        print(f"  Fixed {fname}: ~{changes} lines changed")
    else:
        print(f"  No changes: {fname}")

print(f"\nTotal lines changed: {total_changes}")
