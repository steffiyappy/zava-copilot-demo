# tools/ — M365 Copilot Blog Holistic Audit

The hub data in this repo (`data.js`, `hub.html`) is generated from Python
source files (`build_master.py`, `gen_hub.py`, `ind_batch*.py`, `dept_data*.py`).
Microsoft ships Copilot capability changes on a fast cadence via the **M365
Copilot blog**. This folder contains the scheduler that keeps the demo hub
*holistically* in sync with those changes: descriptions, prompts, sample
files, license tiers, and feasibility — not just banner copy.

## Files

| File | Purpose |
|---|---|
| `blog_audit.py` | Fetches the M365 Copilot blog RSS feed, classifies new posts against the ruleset, proposes a `WHATS_NEW` banner addition, and writes a feasibility-impact report. With `--apply`, it edits `build_master.py` and updates the state file. |
| `feasibility_check.py` | Static validator. Walks every `.py` source and confirms tool license assignments match `feature_ruleset.json`, plus flags any deprecated phrases (e.g. `Gemini`, `o3`, removed tool constants). |
| `feature_ruleset.json` | Authoritative catalog of categories (researcher / excel / cowork / ...) with their keywords, required license, and currently-shipping features. **Update this file when Microsoft ships or retires a feature.** |
| `blog_audit_state.json` | Persisted state: last-seen blog post GUIDs. Edited automatically by `blog_audit.py --apply`. |
| `proposals/<run-id>/` | One folder per audit run. Contains `summary.json` (structured) and `report.md` (human-readable). |

## How it runs

The companion workflow is `.github/workflows/blog-audit.yml`:

- **Daily cron at 06:15 UTC** (~14:15 SGT/MYT). Runs `python tools/blog_audit.py --apply`.
- **Manual trigger** via `workflow_dispatch` with an `apply` boolean.

When new blog posts are detected, the workflow:

1. Inserts one banner entry per new post (up to a cap of 3 per run) into the
   `WHATS_NEW` list in `build_master.py`.
2. Records the post GUID in `blog_audit_state.json` so the next run skips it.
3. Runs `feasibility_check.py` to confirm nothing in the source files
   currently violates the latest license rules.
4. Re-runs `build_master.py` + `gen_hub.py` to regenerate `data.js` and
   `hub.html`.
5. Opens a **draft PR** titled `chore(blog-audit): proposed M365 Copilot hub
   updates`. The PR is intentionally a draft so a human reviewer can:
   - Rephrase the auto-generated banner copy.
   - Decide which existing prompts / sample files need to be updated to
     mention the new feature (or remove a deprecated one).
   - Adjust `feature_ruleset.json` if the new post changes license tiering
     or introduces a brand-new category.
   - Mark the PR ready-for-review and merge.

The workflow never force-merges. The reviewer always has the final say.

## Local usage

Dry run (no changes written):
```
python tools/blog_audit.py
```

Apply mode (edits `build_master.py` and `tools/blog_audit_state.json`):
```
python tools/blog_audit.py --apply
python build_master.py
python gen_hub.py
```

Run the standalone feasibility check:
```
python tools/feasibility_check.py
```

Returns exit code 0 if clean, non-zero if any violation is found.

## Updating the ruleset

When you read a new M365 Copilot blog post and want the audit to pick up the
new capability, edit `tools/feature_ruleset.json`:

- Add new keywords to an existing category's `keywords` array (so future
  posts get classified into it).
- Add new shipping features under `current_features` so
  `feasibility_check.py` can confirm they appear in the hub source.
- If Microsoft deprecates a feature, add it to `deprecated_features` with a
  short reason — the next run flags any source line still referencing it.

## Why a draft PR (not auto-merge)?

Description rewrites, new prompts, and sample-file updates require domain
judgement. The scheduler does the boring discovery + categorisation work; a
human reviewer does the substantive editing. This keeps the hub realistic
and technically feasible without surprise destructive auto-changes.
