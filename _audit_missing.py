#!/usr/bin/env python
"""Audit: how many Cowork Library sample_files + Notebook Library sources
reference files that don't exist on disk?"""
import re, os, sys, json
from pathlib import Path

data = open('data.js', 'r', encoding='utf-8').read()

# Existing files in files/
existing = {f.name for f in Path('files').iterdir() if f.is_file()}
print(f"files/ has {len(existing)} files")

# Find all sample_files references in coworkLibrary blocks.
# After our build_master fix, tuples render as ['filename.xlsx', 'xlsx'].
# Extract every quoted filename ending in .xlsx/.docx/.pdf/.pptx/.png inside sample_files: [ ... ] arrays.

def extract_files(field_name):
    out = []
    for m in re.finditer(r"\b" + field_name + r"\s*:\s*\[([^\]]+?)\]", data, re.S):
        block = m.group(1)
        for f in re.findall(r"'([^']+\.(?:xlsx|docx|pdf|pptx|png))'", block):
            out.append(f)
    return out

cw_files = extract_files('sample_files')
nb_files = extract_files('sources')

cw_unique = {f.lstrip('/') for f in cw_files}
nb_unique = {f.lstrip('/') for f in nb_files}
print(f"Cowork sample_files: {len(cw_files)} refs, {len(cw_unique)} unique")
print(f"Notebook sources:    {len(nb_files)} refs, {len(nb_unique)} unique")

cw_missing = sorted(cw_unique - existing)
nb_missing = sorted(nb_unique - existing)

print(f"\nCowork files missing: {len(cw_missing)}")
for f in cw_missing[:30]:
    print(f"  - {f}")
if len(cw_missing) > 30:
    print(f"  ... +{len(cw_missing)-30} more")

print(f"\nNotebook sources missing: {len(nb_missing)}")
for f in nb_missing[:30]:
    print(f"  - {f}")
if len(nb_missing) > 30:
    print(f"  ... +{len(nb_missing)-30} more")
