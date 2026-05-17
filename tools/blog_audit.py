#!/usr/bin/env python3
"""
blog_audit.py — daily holistic Microsoft 365 Copilot blog auditor.

Workflow
--------
1. Fetch the official Microsoft 365 Copilot blog RSS feed (configurable).
2. Compare each post's GUID against tools/blog_audit_state.json — anything new
   is a candidate update for the hub.
3. Classify each new post against tools/feature_ruleset.json categories
   (researcher, analyst, excel, word, ppt, outlook, teams, notebook, cowork,
   agent_builder, agents_doc, pages).
4. Generate proposed actions:
   - A new WHATS_NEW banner entry in build_master.py for the most relevant posts
   - A "feasibility impact report" naming every existing prompt/file that
     references the affected feature and may need a refresh
5. If --apply is passed, edit build_master.py in place to add the new banner
   entries and update tools/blog_audit_state.json. Otherwise, dry-run only:
   write proposals to tools/proposals/<run-id>/ for human review.

The companion GitHub Action (.github/workflows/blog-audit.yml) calls this
script daily, then opens a draft PR with the proposed changes so a human can
review descriptions, prompts, files, and feasibility together before merge.
"""

from __future__ import annotations

import argparse
import datetime as _dt
import hashlib
import html
import json
import os
import re
import sys
import urllib.request
import urllib.error
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass

ROOT = Path(__file__).resolve().parent.parent
TOOLS = ROOT / "tools"
STATE_PATH = TOOLS / "blog_audit_state.json"
RULESET_PATH = TOOLS / "feature_ruleset.json"
BUILD_MASTER = ROOT / "build_master.py"
DEFAULT_FEED = "https://www.microsoft.com/en-us/microsoft-365/blog/feed/"


def _load_json(p: Path) -> dict:
    if not p.exists():
        return {}
    return json.loads(p.read_text(encoding="utf-8"))


def _save_json(p: Path, data: dict) -> None:
    p.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def _fetch_feed(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "zava-blog-audit/1.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def _parse_rss(xml_bytes: bytes) -> list[dict]:
    """Parse RSS 2.0 OR Atom feed; return list of normalised entries."""
    root = ET.fromstring(xml_bytes)
    ns = {"atom": "http://www.w3.org/2005/Atom"}
    entries: list[dict] = []

    rss_items = root.findall(".//item")
    if rss_items:
        for it in rss_items:
            title = (it.findtext("title") or "").strip()
            link = (it.findtext("link") or "").strip()
            desc = (it.findtext("description") or "").strip()
            guid = (it.findtext("guid") or link or title).strip()
            pub = (it.findtext("pubDate") or "").strip()
            entries.append({
                "title": title, "link": link, "summary": desc,
                "guid": guid, "pub_date": pub,
            })
        return entries

    for it in root.findall("atom:entry", ns):
        title = (it.findtext("atom:title", default="", namespaces=ns) or "").strip()
        link_el = it.find("atom:link", ns)
        link = link_el.get("href") if link_el is not None else ""
        summary = (it.findtext("atom:summary", default="", namespaces=ns) or "").strip()
        guid = (it.findtext("atom:id", default=link or title, namespaces=ns) or "").strip()
        pub = (it.findtext("atom:updated", default="", namespaces=ns) or "").strip()
        entries.append({
            "title": title, "link": link, "summary": summary,
            "guid": guid, "pub_date": pub,
        })
    return entries


def _strip_html(s: str) -> str:
    s = re.sub(r"<[^>]+>", " ", s)
    return html.unescape(re.sub(r"\s+", " ", s)).strip()


def _classify(entry: dict, ruleset: dict) -> list[str]:
    """Return list of category-ids the entry matches, in declaration order."""
    blob = (entry["title"] + " " + _strip_html(entry["summary"])).lower()
    hits: list[str] = []
    for cat_id, cat in ruleset.get("categories", {}).items():
        for kw in cat.get("keywords", []):
            if kw.lower() in blob:
                hits.append(cat_id)
                break
    return hits


def _propose_whats_new(entry: dict, categories: list[str], ruleset: dict) -> dict:
    """Build a WHATS_NEW dict matching the build_master.py schema."""
    cat = ruleset["categories"][categories[0]] if categories else {"label": "Copilot update"}
    label = cat.get("label", "Copilot update")
    summary_clean = _strip_html(entry["summary"])
    if len(summary_clean) > 380:
        summary_clean = summary_clean[:377].rstrip() + "..."
    digest = hashlib.sha1(entry["guid"].encode("utf-8")).hexdigest()[:8]
    return {
        "id": f"wn-auto-{digest}",
        "title": f"📰 {label} — {entry['title']}",
        "badge": entry["pub_date"][:16] if entry["pub_date"] else "Recent",
        "summary": summary_clean,
        "tip": f"Read the announcement: {entry['link']}",
        "license": cat.get("license_required", "Microsoft 365 Copilot"),
        "link": entry["link"],
    }


def _scan_feasibility(categories_seen: set[str], ruleset: dict) -> list[dict]:
    """Walk every .py source under ROOT and surface lines mentioning the
    affected feature keywords. Returns a sorted impact list."""
    feature_kws: dict[str, list[str]] = {}
    for cat_id in categories_seen:
        cat = ruleset["categories"].get(cat_id, {})
        feature_kws[cat_id] = [k.lower() for k in cat.get("keywords", []) + cat.get("current_features", [])]

    impacts: list[dict] = []
    for py in sorted(ROOT.glob("*.py")):
        try:
            text = py.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        for i, line in enumerate(text.splitlines(), start=1):
            low = line.lower()
            for cat_id, kws in feature_kws.items():
                if any(k in low for k in kws):
                    snippet = line.strip()
                    if len(snippet) > 240:
                        snippet = snippet[:237] + "..."
                    impacts.append({
                        "file": py.name,
                        "line": i,
                        "category": cat_id,
                        "snippet": snippet,
                    })
                    break

    for rule in ruleset.get("deprecated_features", []):
        phrase = rule["phrase"].lower()
        for py in sorted(ROOT.glob("*.py")):
            try:
                text = py.read_text(encoding="utf-8", errors="ignore")
            except OSError:
                continue
            for i, line in enumerate(text.splitlines(), start=1):
                if phrase in line.lower():
                    impacts.append({
                        "file": py.name,
                        "line": i,
                        "category": f"deprecated:{rule['phrase']}",
                        "snippet": (line.strip()[:237] + "...") if len(line.strip()) > 240 else line.strip(),
                    })
    return impacts


def _apply_whats_new(banner: dict) -> bool:
    """Insert banner dict into the WHATS_NEW list in build_master.py.

    Returns True if applied, False if banner['id'] already present.
    """
    text = BUILD_MASTER.read_text(encoding="utf-8")
    if f'"id": "{banner["id"]}"' in text:
        return False
    closing = re.search(r"\n(\s*)\}\s*\n\]\s*\n\s*\n\s*SECTORS", text)
    if not closing:
        raise RuntimeError("Could not locate WHATS_NEW closing in build_master.py")
    indent = closing.group(1) or "    "
    new_entry = "    {\n"
    for k in ("id", "title", "badge", "summary", "tip", "license", "link"):
        v = json.dumps(banner[k], ensure_ascii=False)
        new_entry += f'        "{k}": {v},\n'
    new_entry = new_entry.rstrip(",\n") + "\n    }"
    insertion = ",\n" + new_entry
    insert_at = closing.start() + 1
    new_text = text[:insert_at] + indent + "}" + insertion + text[insert_at + len(indent) + 1:]
    BUILD_MASTER.write_text(new_text, encoding="utf-8")
    return True


def _write_proposals(run_id: str, summary: dict) -> Path:
    out_dir = TOOLS / "proposals" / run_id
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "summary.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    md = ["# M365 Copilot Blog Audit", "", f"Run id: `{run_id}`", ""]
    if not summary["new_posts"]:
        md.append("No new posts since last run.")
    else:
        md.append(f"## {len(summary['new_posts'])} new post(s) detected")
        md.append("")
        for p in summary["new_posts"]:
            cats = ", ".join(p["categories"]) or "(uncategorised)"
            md.append(f"### {p['title']}")
            md.append(f"- Pub date: {p['pub_date']}")
            md.append(f"- Link: {p['link']}")
            md.append(f"- Categories: **{cats}**")
            if p.get("proposed_banner"):
                md.append("- Proposed WHATS_NEW banner id: " + p["proposed_banner"]["id"])
            md.append("")
        md.append("## Feasibility impact")
        md.append("")
        if summary["impacts"]:
            md.append(f"{len(summary['impacts'])} source lines reference affected features (review whether description / prompt / file needs refresh):")
            md.append("")
            by_file: dict[str, list[dict]] = {}
            for imp in summary["impacts"]:
                by_file.setdefault(imp["file"], []).append(imp)
            for f, lst in sorted(by_file.items()):
                md.append(f"- **{f}** — {len(lst)} reference(s)")
        else:
            md.append("No existing source lines reference the affected features.")
    (out_dir / "report.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    return out_dir


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Microsoft 365 Copilot blog holistic auditor")
    ap.add_argument("--feed", default=DEFAULT_FEED, help="RSS/Atom feed URL")
    ap.add_argument("--apply", action="store_true",
                    help="Apply proposed banner additions to build_master.py + update state")
    ap.add_argument("--max-posts", type=int, default=8,
                    help="Maximum new posts to surface per run (default 8)")
    ap.add_argument("--limit-banners", type=int, default=3,
                    help="At most N proposed banner additions per run (default 3)")
    args = ap.parse_args(argv)

    state = _load_json(STATE_PATH)
    ruleset = _load_json(RULESET_PATH)
    seen = set(state.get("seen_guids") or [])

    try:
        raw = _fetch_feed(args.feed)
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as e:
        print(f"ERROR: failed to fetch feed: {e}", file=sys.stderr)
        return 2

    entries = _parse_rss(raw)
    new_entries = [e for e in entries if e["guid"] and e["guid"] not in seen][: args.max_posts]

    summary = {
        "run_at_utc": _dt.datetime.now(_dt.timezone.utc).isoformat(timespec="seconds"),
        "feed": args.feed,
        "feed_entry_count": len(entries),
        "new_post_count": len(new_entries),
        "new_posts": [],
        "impacts": [],
    }

    categories_seen: set[str] = set()
    banner_proposals: list[dict] = []
    for ent in new_entries:
        cats = _classify(ent, ruleset)
        categories_seen.update(cats)
        proposed = None
        if cats and len(banner_proposals) < args.limit_banners:
            proposed = _propose_whats_new(ent, cats, ruleset)
            banner_proposals.append(proposed)
        summary["new_posts"].append({
            "title": ent["title"],
            "link": ent["link"],
            "pub_date": ent["pub_date"],
            "guid": ent["guid"],
            "categories": cats,
            "proposed_banner": proposed,
        })

    summary["impacts"] = _scan_feasibility(categories_seen, ruleset)

    run_id = _dt.datetime.now(_dt.timezone.utc).strftime("%Y%m%d-%H%M%S")
    out_dir = _write_proposals(run_id, summary)
    print(f"Proposals written to: {out_dir}")

    if args.apply and banner_proposals:
        applied = 0
        for b in banner_proposals:
            if _apply_whats_new(b):
                applied += 1
        for ent in new_entries:
            seen.add(ent["guid"])
        state["seen_guids"] = sorted(seen)[-500:]
        if new_entries:
            state["last_seen_guid"] = new_entries[0]["guid"]
            state["last_seen_pub_date_utc"] = new_entries[0]["pub_date"]
        state["last_run_utc"] = summary["run_at_utc"]
        _save_json(STATE_PATH, state)
        print(f"Applied {applied} new banner(s); state updated.")
    elif args.apply:
        state["last_run_utc"] = summary["run_at_utc"]
        _save_json(STATE_PATH, state)
        print("No banner candidates; state timestamp updated.")
    else:
        print(f"Dry run: detected {len(new_entries)} new post(s), "
              f"{len(banner_proposals)} banner candidate(s), "
              f"{len(summary['impacts'])} feasibility hit(s).")

    return 0


if __name__ == "__main__":
    sys.exit(main())
