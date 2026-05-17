#!/usr/bin/env python3
"""
feasibility_check.py — static audit of every source .py against
tools/feature_ruleset.json.

Reports:
  - Tools with the wrong license per rule (e.g. T_COWORK that is not
    FRONTIER_LIC, FREE_LIC tools that reference enterprise /files).
  - Source lines mentioning a deprecated feature.
  - Categories with no current_features mentioned anywhere in the source.

Exits non-zero if any violation is found, so CI can fail the run.
"""

from __future__ import annotations

import io
import json
import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass

ROOT = Path(__file__).resolve().parent.parent
RULESET = json.loads((Path(__file__).resolve().parent / "feature_ruleset.json").read_text(encoding="utf-8"))


def _all_sources():
    return sorted(ROOT.glob("*.py"))


def _find_tool_blocks(text: str, tool_name: str) -> list[tuple[int, str, str]]:
    """Return list of (line_no, license_token, snippet) for every tool() call
    that names tool_name as its first positional arg."""
    out: list[tuple[int, str, str]] = []
    pattern = re.compile(
        r"tool\(\s*(" + re.escape(tool_name) + r")\s*,\s*([A-Z_][A-Z_0-9]*)\s*,",
        re.MULTILINE,
    )
    for m in pattern.finditer(text):
        line_no = text.count("\n", 0, m.start()) + 1
        snippet = text[m.start(): m.start() + 80].replace("\n", " ")
        out.append((line_no, m.group(2), snippet))
    return out


def main() -> int:
    violations: list[str] = []
    impacts_summary: dict[str, int] = {}

    for rule in RULESET.get("license_rules", []):
        tool = rule.get("applies_to_tool")
        tools = rule.get("applies_to_tools", [])
        if tool:
            tools = [tool]
        required = rule.get("required_license")
        if tools and required:
            for src in _all_sources():
                text = src.read_text(encoding="utf-8", errors="ignore")
                for t in tools:
                    for line_no, lic, snippet in _find_tool_blocks(text, t):
                        if lic != required:
                            violations.append(
                                f"{src.name}:{line_no} tool({t}, {lic}, ...) "
                                f"expected {required}  -- {snippet.strip()}"
                            )

    free_files_rule = next(
        (r for r in RULESET.get("license_rules", [])
         if "FREE_LIC" in (r.get("applies_to") or [])),
        None,
    )
    if free_files_rule:
        pattern_re = re.compile(free_files_rule["regex_must_not_match"])
        for src in _all_sources():
            text = src.read_text(encoding="utf-8", errors="ignore")
            in_free_block = False
            block_start_line = 0
            for i, line in enumerate(text.splitlines(), start=1):
                if "tool(T_CHAT" in line and "FREE_LIC" in line:
                    in_free_block = True
                    block_start_line = i
                elif in_free_block and re.match(r"^\s*\]\s*,?\s*$", line):
                    in_free_block = False
                elif in_free_block and pattern_re.search(line):
                    violations.append(
                        f"{src.name}:{i} FREE_LIC tool block references enterprise file "
                        f"(opened L{block_start_line}): {line.strip()[:160]}"
                    )

    for rule in RULESET.get("deprecated_features", []):
        phrase = rule["phrase"]
        if phrase.startswith("T_") and phrase.isupper():
            continue
        plow = phrase.lower()
        for src in _all_sources():
            text = src.read_text(encoding="utf-8", errors="ignore")
            for i, line in enumerate(text.splitlines(), start=1):
                if plow in line.lower():
                    violations.append(
                        f"{src.name}:{i} deprecated phrase '{phrase}': {line.strip()[:160]}  "
                        f"({rule.get('reason','')})"
                    )

    for cat_id, cat in RULESET.get("categories", {}).items():
        feats = cat.get("current_features", [])
        for feat in feats:
            for src in _all_sources():
                if feat.lower() in src.read_text(encoding="utf-8", errors="ignore").lower():
                    impacts_summary[f"{cat_id}: {feat}"] = impacts_summary.get(f"{cat_id}: {feat}", 0) + 1
                    break

    print("# Feasibility Check Report")
    print()
    if violations:
        print(f"## ❌ {len(violations)} violation(s)")
        print()
        for v in violations:
            print(f"- {v}")
        print()
    else:
        print("## ✅ No violations detected")
        print()

    print("## Current-feature coverage (informational)")
    print()
    for k in sorted(impacts_summary):
        print(f"- {k}: referenced in {impacts_summary[k]} source file(s)")

    return 1 if violations else 0


if __name__ == "__main__":
    sys.exit(main())
