"""Dump missing Cowork sample_files and Notebook sources to _missing.txt."""
import re
from pathlib import Path

data = open('data.js', 'r', encoding='utf-8').read()
existing = {f.name for f in Path('files').iterdir() if f.is_file()}

def extract_files(field):
    out = []
    for m in re.finditer(r"\b" + field + r"\s*:\s*\[([^\]]+?)\]", data, re.S):
        for f in re.findall(r"'([^']+\.(?:xlsx|docx|pdf|pptx|png))'", m.group(1)):
            out.append(f)
    return out

cw = sorted({f.lstrip('/') for f in extract_files('sample_files')} - existing)
nb = sorted({f.lstrip('/') for f in extract_files('sources')} - existing)

with open('_missing.txt', 'w', encoding='utf-8') as fh:
    fh.write('=== COWORK MISSING (' + str(len(cw)) + ') ===\n')
    for f in cw:
        fh.write(f + '\n')
    fh.write('\n=== NOTEBOOK MISSING (' + str(len(nb)) + ') ===\n')
    for f in nb:
        fh.write(f + '\n')

print(f'Cowork missing: {len(cw)}')
print(f'Notebook missing: {len(nb)}')
print('Wrote _missing.txt')
