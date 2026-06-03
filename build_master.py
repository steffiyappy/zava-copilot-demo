
import sys, json
sys.path.insert(0, '.')
from util import *
from ind_batch1 import INDUSTRIES_1
from ind_batch2 import INDUSTRIES_2
from ind_batch3 import INDUSTRIES_3
from ind_batch4 import INDUSTRIES_4
from ind_batch5 import INDUSTRIES_5
from ind_batch6 import INDUSTRIES_6
from ind_batch7 import INDUSTRIES_7
from ind_batch8 import INDUSTRIES_8
from ind_batch9 import INDUSTRIES_9
from ind_batch10 import INDUSTRIES_10
from ind_batch11 import INDUSTRIES_11
from ind_batch12 import INDUSTRIES_12
from ind_batch13 import INDUSTRIES_13
from dept_data  import DEPARTMENTS
from dept_data2 import DEPARTMENTS_2
from dept_data3 import DEPARTMENTS_3
from dept_data4 import DEPARTMENTS_4
from dept_data5 import DEPARTMENTS_5

all_industries = (INDUSTRIES_1 + INDUSTRIES_2 + INDUSTRIES_3 + INDUSTRIES_4 +
                  INDUSTRIES_5 + INDUSTRIES_6 + INDUSTRIES_7 + INDUSTRIES_8 +
                  INDUSTRIES_9 + INDUSTRIES_10 + INDUSTRIES_11 + INDUSTRIES_12 +
                  INDUSTRIES_13)
all_departments = DEPARTMENTS + DEPARTMENTS_2 + DEPARTMENTS_3 + DEPARTMENTS_4 + DEPARTMENTS_5

print(f"Industries: {len(all_industries)}, Departments: {len(all_departments)}")

WHATS_NEW = [
    {
        "id": "wn-researcher",
        "title": "🔍 Researcher \u2014 Critique + Model Council",
        "badge": "New rollout (May 2026)",
        "summary": "Two demo modes inside Researcher: (1) Critique Mode self-critiques every source and flags claims it cannot verify; (2) Model Council convenes GPT and Claude each return a full independent report, then a synthesis cover letter highlights where they agree, where they differ, and any unique findings.",
        "tip": "m365.cloud.microsoft/chat > Agents > Researcher > switch the mode pill at the top to 'Critique' or 'Model Council'.",
        "license": "Microsoft 365 Copilot",
        "link": "https://techcommunity.microsoft.com/blog/microsoft365copilotblog/introducing-multi-model-intelligence-in-researcher/4506011"
    },
    {
        "id": "wn-cowork",
        "title": "🤝 Cowork Frontier — refreshed (May 2026)",
        "badge": "Frontier Program",
        "summary": "Cowork is now an autonomous agent that you describe in plain language (16,000 chars + voice input). It runs end-to-end and shows every step. NEW: ⏰ run prompts on a schedule for recurring tasks; 🔍 search across the org for files/people/info; 🔬 deep research across multiple sources; 📊 daily briefings + meeting intelligence summaries; 📁 browse & manage OneDrive + SharePoint inline; ⏯️ Pause/Resume/Cancel any time; ✅ Approve / Approve & Remember / Reject for medium and high risk actions. Side panel shows Progress / Input folder / Output folder / Skills / Schedule / Permissions.",
        "tip": "m365.cloud.microsoft > left nav > Agents > Cowork (Frontier). Try: hold the mic icon, dictate \u201cprep me for tomorrow\u2019s board meeting\u201d, then schedule it to repeat every Monday at 6am.",
        "license": "Microsoft 365 Copilot + Frontier Program",
        "link": "https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-cowork-frontier"
    },
    {
        "id": "wn-scout",
        "title": "🧭 Microsoft Scout — desktop AI app (NEW)",
        "badge": "Frontier preview (June 2026)",
        "summary": "A separate desktop AI application that goes beyond Copilot Chat. Scout has direct access to your local file system, can run shell commands with permission tiers, controls a real browser via Playwright, and reaches into your M365 data. Capabilities: 📁 file system + Word/Excel/PowerPoint skills; \ud83d\udda5\ufe0f shell commands (build/test/git) with sensitive-path guards; \ud83c\udf10 browser automation for portal tasks; \ud83d\udce7 M365 access via WorkIQ; \ud83e\udd16 sub-agents (Explore/Task/Code review/Research/General-purpose); \u2764\ufe0f Heartbeat mode (recurring background prompt every 15min/30min/1h/2h, work hours only); \ud83d\udd04 Automations (schedule- or condition-triggered); \ud83d\udd10 granular Permissions UI.",
        "tip": "Install the Scout desktop app, enrol in Frontier, then try Heartbeat: every 30 min during work hours, sweep email + Teams + OneDrive for new high-risk items and post to a private channel.",
        "license": "Microsoft 365 Copilot + Frontier Program",
        "link": "https://learn.microsoft.com/en-us/microsoft-scout/use-microsoft-scout"
    },
    {
        "id": "wn-sharepoint-ai",
        "title": "🌐 AI in SharePoint — Floating Button (NEW)",
        "badge": "Public Preview (April 2026)",
        "summary": "Microsoft 365 Copilot capabilities now live inside SharePoint pages, libraries, and sites. The Floating Button (bottom-right) surfaces context-sensitive actions based on your role + page + selection. Capabilities: \ud83d\udcc4 Work with files \u2014 Ask, Summarize, Compare files, Audio Overview, Generate FAQ; \ud83d\uddc2\ufe0f Organize libraries \u2014 Autofill columns, Automate workflows / set up rules, Create views; \ud83c\udfa8 Pages and sites \u2014 Improve your SharePoint site (broken links / outdated pages / content gaps), Create Page / Section / FAQ Webpart, Refine pages with Design Ideas, Write/Rewrite. Roles: Site Manager / Content Manager / Content Creator / Content Consumer.",
        "tip": "Open any SharePoint document library, select 2 files, click the Floating Button > Compare files. Or open a long PDF and try Generate Audio Overview.",
        "license": "Microsoft 365 Copilot",
        "link": "https://support.microsoft.com/en-us/topic/ai-in-sharepoint-an-overview-c0b1efc3-81d0-4981-8be9-7ba3a75fae15"
    },
    {
        "id": "wn-doc-agents",
        "title": "📝🎯📊 Word / PPT / Excel Agents \u2014 dual tier",
        "badge": "Free Chat tier + Microsoft 365 Copilot",
        "summary": "Type ONE prompt in m365.cloud.microsoft/chat and Copilot returns a fully drafted .docx / .pptx / .xlsx without you opening Word/PPT/Excel first. Now available in BOTH the free Copilot Chat tier (Sasha account) and with an Microsoft 365 Copilot license (MOD Admin account).",
        "tip": "Try in the free tier: 'Build a 5-slide investor narrative deck for the Zava FY2025 Q4 results...'",
        "license": "Either Free Copilot Chat (no extra license) OR Microsoft 365 Copilot license",
        "link": "https://techcommunity.microsoft.com/blog/microsoft365copilotblog/copilot-in-word-new-capabilities-for-document-workflows/4508974"
    },
    {
        "id": "wn-builder",
        "title": "🏗 Agent Builder \u2014 dual tier",
        "badge": "Free Chat tier + Microsoft 365 Copilot",
        "summary": "Create custom agents inside Copilot Chat \u2014 NOT Copilot Studio. Describe \u2192 Configure (knowledge, instructions, starter prompts) \u2192 Test \u2192 Create + share. Now usable in both the free Copilot Chat tier and with an Microsoft 365 Copilot license.",
        "tip": "m365.cloud.microsoft/chat > Agents > + Create an agent. Try building a 'Group CFO Briefing Bot' grounded in your finance reference files.",
        "license": "Either Free Copilot Chat (no extra license) OR Microsoft 365 Copilot license",
        "link": "https://techcommunity.microsoft.com/blog/microsoft365copilotblog/whats-new-in-microsoft-365-copilot--april-2026/4510935"
    },
    {
        "id": "wn-notebook",
        "title": "📓 Copilot Notebook — 5 sources + Quick Create + Mind Maps (refreshed)",
        "badge": "Generally Available + Frontier preview",
        "summary": "Add up to 5 source files (Word/Excel/PDF/PPT) AND now reference SharePoint sites, OneNote notebooks, and external web links as live sources. Set a persistent Instructions field once, run multiple prompts. Quick Create now produces: 📄 full Word documents, 📊 PowerPoint presentations, 🎧 Audio Overviews (podcast-style), and a custom Page. \ud83e\udde0 Interactive Mind Maps (Frontier preview) let you click any node to drill into the underlying source. \ud83d\udc65 Share notebooks with a Microsoft 365 Group for team co-grounding.",
        "tip": "m365.cloud.microsoft/chat > Notebook > + New Notebook. After grounding 5 files, try Quick Create > Audio Overview for a 12-minute commute briefing, then click Mind Map and drill into the riskiest concept node.",
        "license": "Microsoft 365 Copilot",
        "link": "https://techcommunity.microsoft.com/blog/microsoft365copilotblog/whats-new-in-microsoft-365-copilot--april-2026/4510935"
    },
    {
        "id": "wn-federated",
        "title": "🔌 Federated Copilot Connectors",
        "badge": "May 2026 rollout",
        "summary": "Copilot can now query external systems-of-record from inside Chat: Moody's (credit ratings), HubSpot (CRM), LSEG (market data), Notion (knowledge base) and ServiceNow. Useful for IR/credit prompts that need real-time market or counterparty data.",
        "tip": "Try in Researcher: 'Pull LSEG 5-year CDS spreads for Zava Group's top-3 lender peers and Moody's latest rating action notes.'",
        "license": "Microsoft 365 Copilot",
        "link": "https://techcommunity.microsoft.com/blog/microsoft365copilotblog/federated-copilot-connectors---bringing-real-time-enterprise-data-within-microso/4515993"
    },
    {
        "id": "wn-word-legal",
        "title": "⚖️ Word Legal Agent (Frontier)",
        "badge": "Frontier Program",
        "summary": "Specialised Word agent for contract / litigation / compliance work \u2014 redlines clauses against a playbook, highlights deviations from precedent, and proposes alternate language grounded in the firm's contract corpus.",
        "tip": "Open a contract .docx in Word for the Web > Copilot pane > switch to 'Legal Agent'. Ask: 'Redline this MSA against our Tier-1 vendor playbook and flag any indemnity carve-outs.'",
        "license": "Microsoft 365 Copilot + Frontier Program",
        "link": "https://techcommunity.microsoft.com/blog/microsoft365copilotblog/word-legal-agent-in-frontier/4516218"
    },
    {
        "id": "wn-models",
        "title": "🧠 Frontier Model Picker",
        "badge": "May 2026 rollout",
        "summary": "Switch the underlying frontier model for any chat or agent: GPT Instant, GPT and Claude, ChatGPT Images 2.0. Use Thinking models for board-grade reasoning; Instant for fast triage.",
        "tip": "In any Copilot Chat thread, click the model pill at the top \u2014 try 'GPT' for the Strategy/Risk briefs; 'Claude' for nuanced legal/policy drafting.",
        "license": "Microsoft 365 Copilot",
        "link": "https://techcommunity.microsoft.com/blog/microsoft365copilotblog/available-today-anthropic-claude-opus-4-7-in-microsoft-365-copilot/4511666"
    },
    {
        "id": "wn-excel-plan-python",
        "title": "📈 Excel \u2014 Plan mode + Python",
        "badge": "May 2026 rollout",
        "summary": "Plan mode lets Copilot in Excel outline a step-by-step approach BEFORE making any change \u2014 review and adjust before edits land. Python in Excel runs advanced data techniques (forecasts, regressions, custom visualisations) directly inside the Edit-with-Copilot flow without leaving the workbook.",
        "tip": "In Excel for the Web > Copilot pane, click the menu above the prompt box and pick 'Plan'. Or simply add 'use Python' to your prompt to invoke Python automatically.",
        "license": "Microsoft 365 Copilot",
        "link": "https://techcommunity.microsoft.com/blog/microsoft365copilotblog/what%E2%80%99s-new-in-microsoft-365-copilot--april-2026/4510935"
    },
    {
        "id": "wn-ppt-web-images",
        "title": "🌐 PowerPoint \u2014 web grounding + image picker",
        "badge": "April 2026",
        "summary": "Add a public webpage URL as a deck reference and Copilot pulls in current external context to build the outline. Choose the image model (GPT-Image, Flux, or Auto) when generating or editing visuals \u2014 align with quality, style, and governance expectations.",
        "tip": "In PPT for the Web > Copilot pane > add a web reference URL (e.g. a Bursa Malaysia listing or BNM circular page). When generating an image, click the gear and pick the model.",
        "license": "Microsoft 365 Copilot",
        "link": "https://techcommunity.microsoft.com/blog/microsoft365copilotblog/what%E2%80%99s-new-in-microsoft-365-copilot--april-2026/4510935"
    },
    {
        "id": "wn-outlook-canvas",
        "title": "\u270d\ufe0f Outlook \u2014 first draft in canvas",
        "badge": "March 2026 (new Outlook)",
        "summary": "Copilot now writes the email directly in place and asks clarifying questions about goal, audience, and tone, then iterates with the user in the same canvas. No copy-paste, no formatting surprises \u2014 every change is visible in Outlook as the message is refined.",
        "tip": "In new Outlook on the Web, open Compose > Copilot. After the first draft lands, answer Copilot\u2019s clarifying questions and watch the email update in place.",
        "license": "Microsoft 365 Copilot",
        "link": "https://techcommunity.microsoft.com/blog/microsoft365copilotblog/what%E2%80%99s-new-in-microsoft-365-copilot--april-2026/4510935"
    },
    {
        "id": "wn-teams-call-interpret",
        "title": "📞 Teams \u2014 Call Delegation + Interpretation",
        "badge": "April-May 2026",
        "summary": "Copilot Call Delegation: Copilot answers incoming Teams calls on the user\u2019s behalf, gathers context from the caller, and books follow-ups via Microsoft Bookings. Consecutive Interpretation: turn-based translation between two languages with Interpreter on the meeting stage \u2014 ideal for ASEAN cross-border meetings.",
        "tip": "Teams > Settings > Calls > enable Copilot Call Delegation. For meetings, Interpreter on stage supports both real-time simultaneous and turn-based consecutive interpretation.",
        "license": "Microsoft 365 Copilot",
        "link": "https://techcommunity.microsoft.com/blog/microsoft365copilotblog/what%E2%80%99s-new-in-microsoft-365-copilot--april-2026/4510935"
    },
    {
        "id": "wn-notebook-mindmap",
        "title": "🧠 Notebook \u2014 Mind Maps + PPT/Word generation",
        "badge": "May 2026 (Frontier preview)",
        "summary": "Copilot Notebook can now generate full Word documents and PowerPoint decks directly from notebook content. Mind Maps give an interactive grounded view of relationships across all sources \u2014 click a node to drill in. SharePoint sites, OneNote notebooks, and external web URLs all qualify as sources.",
        "tip": "After grounding the notebook, click Quick Create > Mind Map for an executive overview, or > Word document / PowerPoint presentation to draft a deliverable preloaded with visuals.",
        "license": "Microsoft 365 Copilot",
        "link": "https://techcommunity.microsoft.com/blog/microsoft365copilotblog/what%E2%80%99s-new-in-microsoft-365-copilot--april-2026/4510935"
    },
    {
        "id": "wn-agent-store",
        "title": "🏪 Agent Builder \u2014 submit to Agent Store",
        "badge": "May 2026 rollout",
        "summary": "Agent Builder now supports submitting agents for admin review and approval. Approved agents land in the \u201cBuilt by your org\u201d section of the Agent Store where the whole organisation can discover and install them \u2014 the right balance of citizen-developer scale and IT admin control.",
        "tip": "After Test, click Submit for review (next to Create + share). Once your IT admin approves, the agent appears in the org\u2019s Agent Store automatically.",
        "license": "Microsoft 365 Copilot",
        "link": "https://techcommunity.microsoft.com/blog/microsoft365copilotblog/what%E2%80%99s-new-in-microsoft-365-copilot--april-2026/4510935"
    }
]

SECTORS = [
    {"id": "sec-general",    "label": "⭐ Start Here",     "industries": ["general"]},
    {"id": "sec-banking",    "label": "Banking",           "industries": ["commercial-banking","islamic-banking","investment-banking","mortgage-finance"]},
    {"id": "sec-insurance",  "label": "Insurance",         "industries": ["general-insurance","life-insurance","takaful"]},
    {"id": "sec-fintech",    "label": "Fintech",           "industries": ["fintech-payments","cross-border-remittance"]},
    {"id": "sec-healthcare", "label": "Healthcare",        "industries": ["hospital-network","pharmaceutical"]},
    {"id": "sec-og",         "label": "Oil & Gas",         "industries": ["og-upstream","og-downstream"]},
    {"id": "sec-energy",     "label": "Energy",            "industries": ["renewable-energy"]},
    {"id": "sec-mfg",        "label": "Manufacturing",     "industries": ["industrial-manufacturing","rubber-gloves","semiconductor","automotive","auto-tyres","construction"]},
    {"id": "sec-food",       "label": "Food & FMCG",       "industries": ["food-fmcg"]},
    {"id": "sec-agri",       "label": "Agriculture",       "industries": ["plantation"]},
    {"id": "sec-bpo",        "label": "BPO & Tech",        "industries": ["bpo-services"]},
    {"id": "sec-telco",      "label": "Telco",             "industries": ["telco"]},
    {"id": "sec-congl",      "label": "Conglomerate",      "industries": ["diversified-conglomerate"]},
    {"id": "sec-govt",       "label": "Government",        "industries": ["government-agency","financial-regulator"]},
    {"id": "sec-glc",        "label": "GLC",               "industries": ["glc-investment"]},
    {"id": "sec-re",         "label": "Real Estate",       "industries": ["property-reit"]},
    {"id": "sec-logistics",  "label": "Logistics",         "industries": ["logistics-3pl"]},
    {"id": "sec-aviation",   "label": "Aviation",          "industries": ["aviation-airports","aviation-airlines"]},
    {"id": "sec-mining",     "label": "Mining",            "industries": ["coal-mining","rare-earth"]},
    {"id": "sec-retail",     "label": "Retail",            "industries": ["retail-grocery"]},
    {"id": "sec-hospitality","label": "Hospitality",       "industries": ["hotel-resort"]},
    {"id": "sec-media",      "label": "Media",             "industries": ["media-entertainment"]},
    {"id": "sec-edu",        "label": "Education",         "industries": ["education"]},
    {"id": "sec-utilities",  "label": "Utilities",         "industries": ["power-utilities"]},
    {"id": "sec-prop-dev",   "label": "Property Development","industries": ["property-development"]},
    {"id": "sec-tech",       "label": "Tech & Digital",    "industries": ["ecommerce-superapp"]},
    {"id": "sec-maritime",   "label": "Maritime & Shipping","industries": ["maritime-shipping"]},
    {"id": "sec-distribution","label": "Industrial Distribution","industries": ["electrical-distribution"]},
]

def esc_val(s):
    """Escape for JS single-quoted strings."""
    if not isinstance(s, str):
        return s
    return s.replace('\\', '\\\\').replace("'", "\\'").replace('\n', ' ').replace('\r', '')

def js_val(v, indent=0):
    """Convert Python value to JS literal."""
    pad = '  ' * indent
    if v is None:
        return 'null'
    if isinstance(v, bool):
        return 'true' if v else 'false'
    if isinstance(v, (int, float)):
        return str(v)
    if isinstance(v, str):
        return "'" + esc_val(v) + "'"
    if isinstance(v, (list, tuple)):
        if not v:
            return '[]'
        items = [pad + '  ' + js_val(item, indent+1) for item in v]
        return '[\n' + ',\n'.join(items) + '\n' + pad + ']'
    if isinstance(v, dict):
        if not v:
            return '{}'
        pairs = []
        for k, dv in v.items():
            pairs.append(pad + '  ' + k + ': ' + js_val(dv, indent+1))
        return '{\n' + ',\n'.join(pairs) + '\n' + pad + '}'
    return "'" + esc_val(str(v)) + "'"

# ── Native BM/IDEN translation merge ────────────────────────────────────────
# Loaded from translations.py (auto-authored). Adds *BM and *IDEN fields to
# each industry/department so the JS render path can prefer native text over
# the runtime phrase translator when locale is MY_BM or ID_EN.
try:
    from translations import TRANSLATIONS as _TRANS
    _trans_count = 0
    for entry in all_industries + all_departments:
        eid = entry.get('id') if isinstance(entry, dict) else None
        if not eid:
            continue
        trans = _TRANS.get(eid)
        if not trans:
            continue
        bm = trans.get('BM') or {}
        iden = trans.get('IDEN') or {}
        if bm.get('company'):  entry['companyBM']  = bm['company']
        if bm.get('tagline'):  entry['taglineBM']  = bm['tagline']
        if bm.get('scenario'): entry['scenarioBM'] = bm['scenario']
        if iden.get('company'):  entry['companyIDEN']  = iden['company']
        if iden.get('tagline'):  entry['taglineIDEN']  = iden['tagline']
        if iden.get('scenario'): entry['scenarioIDEN'] = iden['scenario']
        sb = entry.get('storyboard') or []
        sb_bm = bm.get('storyboard') or []
        sb_iden = iden.get('storyboard') or []
        for i, phase in enumerate(sb):
            if not isinstance(phase, dict):
                continue
            if i < len(sb_bm):
                if sb_bm[i].get('title'):   phase['titleBM']   = sb_bm[i]['title']
                if sb_bm[i].get('summary'): phase['summaryBM'] = sb_bm[i]['summary']
            if i < len(sb_iden):
                if sb_iden[i].get('title'):   phase['titleIDEN']   = sb_iden[i]['title']
                if sb_iden[i].get('summary'): phase['summaryIDEN'] = sb_iden[i]['summary']
        _trans_count += 1
    print(f"Native translations merged into {_trans_count} entries")
except ImportError:
    print("(translations.py not found; building without native translations)")
except Exception as _e:
    print(f"(translations merge skipped due to error: {_e})")

# ── Subsidiaries map merge ─────────────────────────────────────────────────
# Attaches a `subsidiaries` array on each industry record from the customer
# accounts list. Surfaces real ASEAN subsidiaries on the entry hero (chip
# strip) and feeds the search haystack so demoers can search by subsidiary
# name and land on the matching industry.
try:
    from subsidiaries_map import SUBSIDIARIES_MAP as _SUBS
    _subs_count = 0
    for entry in all_industries:
        eid = entry.get('id') if isinstance(entry, dict) else None
        if not eid:
            continue
        subs = _SUBS.get(eid)
        if subs:
            entry['subsidiaries'] = list(subs)
            _subs_count += 1
    print(f"Subsidiaries mapped onto {_subs_count} industries")
except ImportError:
    print("(subsidiaries_map.py not found; building without subsidiary chips)")
except Exception as _e:
    print(f"(subsidiaries merge skipped due to error: {_e})")

# ── ID -> BM auto-fill ─────────────────────────────────────────────────────
# Most promptsBM arrays are empty (~93%) so MY_BM users were seeing English
# fallback for the bulk of prompt blocks while a handful of tools had hand-
# authored BM — producing the dreaded "half English half BM" mix. We now fill
# every empty promptsBM by cloning promptsID and running it through the
# ID→BM token swap table (Ketik→Taip, Akun→Akaun, Kantor→Pejabat, Kolom→Lajur,
# Tabel→Jadual, Bisa→Boleh, etc.). BM and ID are ~80% mutually intelligible so
# this gives MY_BM users a consistent Bahasa Malaysia experience instead of
# locale-mixing.
try:
    from id_to_bm_swaps import fill_missing_bm_from_id
    _bm_filled = fill_missing_bm_from_id(all_industries)
    _bm_filled += fill_missing_bm_from_id(all_departments)
    print(f"BM prompts auto-filled from ID for {_bm_filled} tool blocks")
except ImportError:
    print("(id_to_bm_swaps.py not found; BM prompts left as-is)")
except Exception as _e:
    print(f"(BM auto-fill skipped due to error: {_e})")

# ── Cowork: expand each entry's Cowork block with 3 more delegation scenarios ──
# User feedback: "I need more use cases for all... like the everythingischr0me
# github site". We append 3 cross-cutting Cowork scenarios (Investor Day Sprint,
# Lender Outreach Cycle, Regulator Submission Sprint) to every entry's Cowork
# tool block. Each scenario delegates 5 parallel actions (Word doc + email +
# Teams meeting + Teams post + tracker update) using the standardised named-
# recipients (Hadar/Sasha/Daichi/Sonia/Will/Omar) for persona consistency.
# The BM auto-fill above already ran; we wire in BM via the same path AFTER
# this expansion step so the new ID variants get token-swapped into BM too.
try:
    from cowork_more_scenarios import expand_cowork_prompts
    _cw_added_ind  = expand_cowork_prompts(all_industries)
    _cw_added_dept = expand_cowork_prompts(all_departments)
    print(f"Cowork extra scenarios appended to {_cw_added_ind + _cw_added_dept} entries")
    # Re-run BM auto-fill so the newly appended ID scenarios populate BM too.
    try:
        from id_to_bm_swaps import fill_missing_bm_from_id as _refill
        _bm_more = _refill(all_industries) + _refill(all_departments)
        if _bm_more:
            print(f"BM auto-fill (post-Cowork): {_bm_more} more tool blocks filled")
    except Exception:
        pass
except ImportError:
    print("(cowork_more_scenarios.py not found; Cowork left as-is)")
except Exception as _e:
    print(f"(Cowork expansion skipped due to error: {_e})")

# ── Cowork: append HTML-artifact deliverable prompt to each entry ──────────
# User feedback: "Cowork is also able to produce HTML dashboards, charts, or
# even kanban boards. Can you add those across the industries and departments
# as an additional task under a use case?" We append ONE archetype-routed
# HTML-artifact prompt (Dashboard / Kanban / Heatmap / Pipeline-Timeline) to
# every entry's Cowork tool block. The HTML render runs in parallel with the
# usual 4 Cowork sub-tasks (Word memo + email + Teams meeting + tracker
# update). Wired here so the subsequent approval-gate + recipient-
# diversification passes also touch the new prompt.
try:
    from cowork_html_artifacts import append_html_artifact_prompts
    _html_ind  = append_html_artifact_prompts(all_industries)
    _html_dept = append_html_artifact_prompts(all_departments)
    print(f"Cowork HTML artifact prompts appended to {_html_ind + _html_dept} entries")
    try:
        from id_to_bm_swaps import fill_missing_bm_from_id as _refill_html
        _bm_more = _refill_html(all_industries) + _refill_html(all_departments)
        if _bm_more:
            print(f"BM auto-fill (post-HTML-artifact): {_bm_more} more tool blocks filled")
    except Exception:
        pass
except ImportError:
    print("(cowork_html_artifacts.py not found; HTML artifact prompts skipped)")
except Exception as _e:
    print(f"(Cowork HTML artifact append skipped due to error: {_e})")

# ── Customer Cowork Runbooks: KLK (10 UCs) + KIBB (BRC, 6 steps) ─────────
# User flagged: "the cowork from KIBB and KLK customer pages — runbook prompts
# need to be in the main hub industries/depts". Routes each customer UC to one
# matching Zava entry's Cowork tool block, appending the multi-step prompts.
try:
    from cowork_customer_runbooks import inject_customer_runbooks
    _all_for_rb = list(all_industries) + list(all_departments)
    _rb_result = inject_customer_runbooks(_all_for_rb)
    print(f"Cowork customer-runbook prompts: {_rb_result['prompts']} prompts + {_rb_result['files']} sample files appended across {_rb_result['entries']} entries (KLK 10 UCs + KIBB BRC + KIBB Cowork 15 UCs, each with HTML artifact step)")
    try:
        from id_to_bm_swaps import fill_missing_bm_from_id as _refill_rb
        _bm_more_rb = _refill_rb(all_industries) + _refill_rb(all_departments)
        if _bm_more_rb:
            print(f"BM auto-fill (post-customer-runbook): {_bm_more_rb} more tool blocks filled")
    except Exception:
        pass
except ImportError:
    print("(cowork_customer_runbooks.py not found; KLK/KIBB runbook merge skipped)")
except Exception as _e:
    print(f"(Cowork customer-runbook merge skipped due to error: {_e})")

# ── Regulator + cross-dept Cowork Runbooks (9 UCs) ───────────────────────
# Adds IPO Prospectus Compliance, Anti-Scam Complaint Triage, Workforce
# Scenario, IE Campaign Audit, Contract Review, Tax Application, Policy
# Paper, Procurement Benchmarking, Internal Audit Pack — each with an HTML
# artifact step — onto financial-regulator + relevant dept entries.
try:
    from cowork_regulator_runbook import inject_regulator_runbook
    _all_for_reg = list(all_industries) + list(all_departments)
    _reg_result = inject_regulator_runbook(_all_for_reg)
    print(f"Cowork regulator+dept runbook: {_reg_result['prompts']} prompts + {_reg_result['files']} sample files appended across {_reg_result['entries']} entries (9 UCs incl HTML artifact step each)")
    try:
        from id_to_bm_swaps import fill_missing_bm_from_id as _refill_reg
        _bm_more_reg = _refill_reg(all_industries) + _refill_reg(all_departments)
        if _bm_more_reg:
            print(f"BM auto-fill (post-regulator-runbook): {_bm_more_reg} more tool blocks filled")
    except Exception:
        pass
except ImportError:
    print("(cowork_regulator_runbook.py not found; regulator runbook skipped)")
except Exception as _e:
    print(f"(Cowork regulator runbook skipped due to error: {_e})")

# ── Reverse mirror + canonical override: build relevantIndustries on every department ──
# Each industry declares 3-5 dept ids in relevantDepts (kept narrow so industry
# pages stay visually neat with 3-5 dept pills). Reverse-mirror that graph to
# get a base set of relevantIndustries[] per department.
#
# Then augment: in a conglomerate, EVERY group function (Finance, Strategy,
# Risk, Operations, Legal, HR, Procurement, IR, CorpSec, IT/Digital, ESG,
# Marketing) genuinely interfaces with EVERY operating arm. So we override the
# reverse-mirror with a canonical "all operating arms apply to me" list per
# dept. 'general' is excluded everywhere because it is the umbrella entry.
# 'government-agency' and 'financial-regulator' are excluded from depts where
# they don't naturally apply (IR, CorpSec, Marketing — public-sector entities
# don't have private-listed-entity boards or brand-marketing functions).
try:
    _rev = {}
    for entry in all_industries:
        if not isinstance(entry, dict):
            continue
        eid = entry.get('id')
        for did in (entry.get('relevantDepts') or []):
            _rev.setdefault(did, []).append(eid)

    _all_ind_ids = [e.get('id') for e in all_industries if isinstance(e, dict) and e.get('id')]
    _operating_arms = [iid for iid in _all_ind_ids if iid != 'general']
    _commercial_only = [iid for iid in _operating_arms if iid not in ('government-agency', 'financial-regulator')]

    DEPT_RELEVANT_INDUSTRIES = {
        'dept-finance':             _operating_arms,
        'dept-strategy':            _operating_arms,
        'dept-risk':                _operating_arms,
        'dept-operations':          _operating_arms,
        'dept-legal':               _operating_arms,
        'dept-hr':                  _operating_arms,
        'dept-procurement':         _operating_arms,
        'dept-it-digital':          _operating_arms,
        'dept-esg':                 _operating_arms,
        'dept-investor-relations':  _commercial_only,
        'dept-corpsec':             _commercial_only,
        'dept-marketing':           _commercial_only,
    }

    _mirrored = 0
    for dept in all_departments:
        if not isinstance(dept, dict):
            continue
        did = dept.get('id')
        # Start from reverse-mirror (preserves any explicitly declared links)
        base = _rev.get(did) or []
        # Union with canonical list (every dept sees every operating arm)
        canonical = DEPT_RELEVANT_INDUSTRIES.get(did) or []
        merged = list(dict.fromkeys([*base, *canonical]))
        if merged:
            dept['relevantIndustries'] = merged
            _mirrored += 1
    print(f"Reverse mirror + canonical override: relevantIndustries set on {_mirrored} departments")
except Exception as _e:
    print(f"(reverse mirror skipped due to error: {_e})")

# ── Notebook Demo Guide: surface canonical /00_Copilot_Notebook_Demo_Guide.docx
# as a presenter-only companion (NOT a Notebook source).
# User feedback: "the guide should actually be the guide showing on the page...
# they are not supposed to add that source into the notebook. doesn't make sense."
# So: we expose the guide via meta['guide'] which the renderer paints as a
# separate "📘 Demo guide" callout above the source-pills row, with copy that
# explicitly says "Do NOT add to the Notebook — open this on your screen."
# It stays in the entry-level files list so the file is still downloadable.
_NB_GUIDE = '/00_Copilot_Notebook_Demo_Guide.docx'
def _prepend_nb_guide(entries):
    n = 0
    for e in entries:
        for tool in e.get('prompts') or []:
            if 'Copilot Notebook' not in (tool.get('tool') or ''):
                continue
            meta = tool.get('notebookMeta')
            if not meta:
                meta = {'sources': [], 'instructions': '', 'instructionsID': ''}
                tool['notebookMeta'] = meta
            # Strip the guide if it leaked into a previous build's sources array
            srcs = [s for s in (meta.get('sources') or []) if s != _NB_GUIDE]
            meta['sources'] = srcs
            # Surface the guide as a separate companion field (rendered as a
            # presenter-only callout above the sources row).
            if meta.get('guide') != _NB_GUIDE:
                meta['guide'] = _NB_GUIDE
                n += 1
        # Keep the guide on the entry-level files list so it's still discoverable
        # via the file-pill row at the top of the entry detail panel.
        files = list(e.get('files') or [])
        if _NB_GUIDE not in files:
            files.insert(0, _NB_GUIDE)
            e['files'] = files
    return n
try:
    _nb_added = _prepend_nb_guide(all_industries) + _prepend_nb_guide(all_departments)
    print(f"Notebook Demo Guide prepended on {_nb_added} Notebook blocks")
except Exception as _e:
    print(f"(Notebook Demo Guide prepend skipped due to error: {_e})")

# ── Notebook unique scenarios: kill war-room boilerplate ──
# User feedback: "why all the notebooks are war room? why no unique scenario one."
# 22/55 entries shipped with one of three generic openers:
#   "Use ALL uploaded sources as the only source of truth..." (x11)
#   "You are my executive war-room analyst..."                (x8)
#   "Act as my board-ready synthesis partner..."              (x3)
# 25/55 used "war-room" generically. Result: notebooks felt copy-paste.
#
# Fix: detect generic openers and rewrite with industry-anchored persona +
# real regulator + signature crisis tied to the entry's tagline.
import re as _nb_re
_NB_GENERIC_RX = _nb_re.compile(
    r"^(use all uploaded sources|you are my executive war-room analyst\.|"
    r"act as my board-ready synthesis partner|you are my (portfolio|network|commercial|content) war-room analyst|"
    r"you are my executive readiness analyst)",
    _nb_re.IGNORECASE,
)
# Indonesian generic openers (mirror of the EN templates above)
_NB_GENERIC_RX_ID = _nb_re.compile(
    r"^(gunakan seluruh sumber|anda adalah analis war-room eksekutif saya\.|"
    r"bertindak sebagai mitra sintesis|anda adalah analis (portfolio|jaringan|komersial|konten) war-room|"
    r"anda adalah analis kesiapan eksekutif)",
    _nb_re.IGNORECASE,
)

def _nb_archetype(eid):
    e = (eid or '').lower()
    if _nb_re.search(r'^dept-finance', e): return 'dept-fin'
    if _nb_re.search(r'^dept-hr', e):       return 'dept-hr'
    if _nb_re.search(r'^dept-legal', e):    return 'dept-legal'
    if _nb_re.search(r'^dept-risk', e):     return 'dept-risk'
    if _nb_re.search(r'^dept-strategy', e): return 'dept-strat'
    if _nb_re.search(r'^dept-mark',  e):    return 'dept-mkt'
    if _nb_re.search(r'^dept-esg',  e):     return 'dept-esg'
    if _nb_re.search(r'^dept-operation', e): return 'dept-ops'
    if _nb_re.search(r'^dept-corpsec', e):  return 'dept-corpsec'
    if _nb_re.search(r'^dept-investor', e): return 'dept-ir'
    if _nb_re.search(r'^dept-procurement',e): return 'dept-proc'
    if _nb_re.search(r'^dept-it', e):       return 'dept-it'
    if _nb_re.search(r'bank|finance|treasury|mortgage|remitt|glc-investment', e): return 'bank'
    if _nb_re.search(r'islamic', e):                  return 'islamic'
    if _nb_re.search(r'fintech|payment',  e):         return 'fintech'
    if _nb_re.search(r'insurance|takaful',  e):       return 'insur'
    if _nb_re.search(r'hospital|pharma|health|rubber-glove', e): return 'hc'
    if _nb_re.search(r'og-up|og-down|coal|mining|rare-earth|renewable|power|util', e): return 'energy'
    if _nb_re.search(r'manuf|automotive|auto-tyre|semicon|food-fmcg', e): return 'mfg'
    if _nb_re.search(r'plantation|agri', e):          return 'agri'
    if _nb_re.search(r'retail|grocery|qsr|fashion|apparel|ecomm|super-app|mall', e): return 'retail'
    if _nb_re.search(r'hotel|tourism|airline|aviation|cruise|leisure|entertain|gaming|media|broadcast|hospital(?!ity)|hospitality', e): return 'hosp'
    if _nb_re.search(r'telco|telecom|broadband|tower|isp|tech|software|cloud|data-center|saas|platform|digital|bpo', e): return 'tech'
    if _nb_re.search(r'maritim|shipping|port|logistic|rail|express|courier|cold-chain|transport|trucking|terminal', e): return 'trans'
    if _nb_re.search(r'gov|public|regulator|sovereign', e): return 'pub'
    if _nb_re.search(r'property|construction|reit', e): return 'prop'
    if _nb_re.search(r'education|university', e): return 'edu'
    if _nb_re.search(r'diversified|conglomerate|general', e): return 'congl'
    return 'congl'

# Per-archetype: (persona-role, regulator/governance-anchor, signature-deliverable, framing-rule, language-ID-translation-of-rule)
_NB_TEMPLATES = {
    'bank':    ('Group CFO and Group Treasurer war-room analyst', 'BNM (MY) / OJK (ID) / MAS (SG) prudential and SCM disclosure', 'next Board-Risk briefing pack', 'Classify every credit and treasury recommendation as Red / Amber / Green and cite the file + tab.', 'Klasifikasikan setiap rekomendasi kredit dan treasury sebagai Merah / Kuning / Hijau dan kutip file + tab.'),
    'islamic': ('Shariah Committee secretariat analyst', 'IFSA + AAOIFI Shariah governance', 'next Shariah Committee meeting pack', 'Anchor every recommendation in the relevant Shariah resolution and cite the file + section.', 'Anchor setiap rekomendasi pada resolusi Shariah yang relevan dan kutip file + bagian.'),
    'fintech': ('Group CRO and Compliance Lead briefing analyst', 'BNM e-money / OJK PUJK / MAS PSA licensing', 'next Risk Committee deep-dive', 'Tag each recommendation as Red / Amber / Green for fraud, AML/CFT, and operational risk and cite the file + section.', 'Tag setiap rekomendasi sebagai Merah / Kuning / Hijau untuk fraud, APU/PPT, dan risiko operasional dan kutip file + bagian.'),
    'insur':   ('Chief Actuary and Group CFO briefing analyst', 'BNM RBC / OJK SLOJK / MAS RBC2 solvency framework', 'next Capital and Risk Committee pack', 'Tie every figure to the loss ratio, expense ratio or combined ratio it impacts and cite the source file.', 'Kaitkan setiap angka dengan loss ratio, expense ratio atau combined ratio yang dipengaruhi dan kutip file sumber.'),
    'hc':      ('Medical Director and Chief Nurse case-conference analyst', 'PDPA (MY) / UU PDP (ID) / PDPA (SG) and MOH clinical-governance standards', 'next Medical Advisory Committee meeting', 'De-identify all patient detail (use case IDs) and tag each finding as Clinical-Quality / Patient-Safety / Compliance and cite the source file.', 'De-identifikasi semua detail pasien (gunakan case ID) dan tag setiap temuan sebagai Clinical-Quality / Patient-Safety / Compliance dan kutip file sumber.'),
    'energy':  ('HSSE Director and Operations VP incident-review analyst', 'DOSH (MY) / KemenESDM (ID) / MOM (SG) HSE reporting and Bursa / IDX disclosure', 'next Operating Committee HSE review', 'Tag each item as Process-Safety / People-Safety / Environment / Commercial and cite the source file + tab.', 'Tag setiap item sebagai Process-Safety / People-Safety / Environment / Commercial dan kutip file + tab sumber.'),
    'mfg':     ('Plant Manager and QA Director quality-review analyst', 'Customer Quality Agreement and ISO 9001 / IATF 16949 batch-traceability', 'next Quality Council and Customer Recovery review', 'For every recommendation tag the affected SKU / batch / lot and cite the source file + tab.', 'Untuk setiap rekomendasi tag SKU / batch / lot yang terdampak dan kutip file + tab sumber.'),
    'agri':    ('Sustainability Manager and Estate GM analyst', 'RSPO / ISPO / MSPO / NDPE certification audit', 'next Sustainability Committee + Buyer audit close-out', 'Tag every finding by estate / mill / smallholder block, classify as Compliant / Watchlist / Non-conformance and cite the source file.', 'Tag setiap temuan berdasarkan estate / mill / blok smallholder, klasifikasikan sebagai Compliant / Watchlist / Non-conformance dan kutip file sumber.'),
    'retail':  ('Category Manager and Store Operations VP huddle analyst', 'Category Performance Review + Loyalty Privacy policy', 'next weekly Trade Huddle + Category Council', 'Tag every recommendation by category / SKU / store cluster and cite the source file + tab.', 'Tag setiap rekomendasi berdasarkan kategori / SKU / klaster gerai dan kutip file + tab sumber.'),
    'hosp':    ('General Manager and Director of Operations property-review analyst', 'Brand Standard audit + Guest Privacy policy', 'next property leadership huddle + brand audit close-out', 'Tag every issue by property / department / shift, classify as Guest-Impact / Revenue-Impact / Compliance and cite the source file.', 'Tag setiap masalah berdasarkan properti / departemen / shift, klasifikasikan sebagai Guest-Impact / Revenue-Impact / Compliance dan kutip file sumber.'),
    'tech':    ('SVP Product and SVP Engineering operating-review analyst', 'SLA + DPA contractual obligations and tenant-side DLP', 'next Operating Review + SLA breach customer notification', 'Anchor every recommendation in the SLA metric or DPA clause it impacts and cite the source file + tab.', 'Anchor setiap rekomendasi pada metrik SLA atau klausul DPA yang dipengaruhi dan kutip file + tab sumber.'),
    'trans':   ('Port Captain and Operations Director incident-review analyst', 'IMO / port-state authority and customs-broker compliance', 'next Operations Committee + customer hold-note review', 'Tag every action by vessel / voyage / port-call and classify as Schedule / Cargo / Compliance / Customer and cite the source file.', 'Tag setiap aksi berdasarkan kapal / voyage / port-call dan klasifikasikan sebagai Schedule / Cargo / Compliance / Customer dan kutip file sumber.'),
    'pub':     ('Permanent Secretary and Communications Director citizen-engagement analyst', 'BPK / AGD / National Audit Department audit-trail standard', 'next Inter-Ministry Steering Committee + DPR / Parliament hearing prep', 'Tag every recommendation by ministry / agency / programme and classify as Service-Delivery / Compliance / Reputation and cite the source file.', 'Tag setiap rekomendasi berdasarkan kementerian / lembaga / program dan klasifikasikan sebagai Service-Delivery / Compliance / Reputation dan kutip file sumber.'),
    'prop':    ('Project Director and Asset Management VP development-review analyst', 'Sales & Purchase Agreement + REIT trustee disclosure', 'next Project Steering Committee + REIT-trustee briefing', 'Tag every issue by project phase / asset / tenant and classify as Schedule / Cost / Quality / Compliance and cite the source file.', 'Tag setiap masalah berdasarkan fase proyek / aset / tenant dan klasifikasikan sebagai Schedule / Cost / Quality / Compliance dan kutip file sumber.'),
    'edu':     ('Vice-Chancellor and Registrar academic-quality analyst', 'MQA / Kemdikbud / SkillsFuture academic-quality audit', 'next Senate / Academic Council meeting', 'Tag every issue by faculty / programme / cohort and classify as Academic-Quality / Compliance / Student-Experience and cite the source file.', 'Tag setiap masalah berdasarkan fakultas / program / cohort dan klasifikasikan sebagai Academic-Quality / Compliance / Student-Experience dan kutip file sumber.'),
    'congl':   ('Group CFO and Chief of Staff Board-pack analyst', 'Bursa / IDX dual-listing disclosure and SCM / OJK enquiries', 'next emergency Board review', 'Classify every divisional recommendation as Red / Amber / Green and cite the source file + tab.', 'Klasifikasikan setiap rekomendasi divisional sebagai Merah / Kuning / Hijau dan kutip file + tab sumber.'),
    # Departments
    'dept-fin':     ('Group CFO and Head of FP&A briefing analyst', 'Group Finance close calendar + variance protocol', 'next Group CFO briefing + Audit Committee deep-dive', 'Tag every variance by division / cost line and classify as Volume / Price / FX / Other and cite the source file.', 'Tag setiap selisih berdasarkan divisi / lini biaya dan klasifikasikan sebagai Volume / Price / FX / Other dan kutip file sumber.'),
    'dept-hr':      ('Group CHRO and Head of Talent talent-review analyst', 'PDPA (MY) / UU PDP (ID) employee-data protection', 'next Talent Council + Group ExCo people-update', 'Tag every action by population / job-family / location and classify as Talent / Comp / ER / Compliance and cite the source file.', 'Tag setiap aksi berdasarkan populasi / job-family / lokasi dan klasifikasikan sebagai Talent / Comp / ER / Compliance dan kutip file sumber.'),
    'dept-legal':   ('Group General Counsel and Head of Litigation matter-review analyst', 'Privilege protocol + matter-management standard', 'next Group Legal Council + risk-committee escalation', 'Tag every matter as Privileged / Open / Closed and classify exposure as Material / Notable / Routine and cite the source file.', 'Tag setiap matter sebagai Privileged / Open / Closed dan klasifikasikan eksposur sebagai Material / Notable / Routine dan kutip file sumber.'),
    'dept-risk':    ('Group CRO and Head of ORM enterprise-risk analyst', 'Group Risk Appetite Statement + Bank Negara / OJK / MAS supervisory expectations', 'next Risk Management Committee deep-dive', 'Map every recommendation to the relevant risk-appetite metric and tag as Red / Amber / Green vs threshold and cite the source file.', 'Petakan setiap rekomendasi ke metrik risk-appetite yang relevan dan tag sebagai Merah / Kuning / Hijau vs threshold dan kutip file sumber.'),
    'dept-strat':   ('Group Chief of Staff and Head of Strategy strategy-review analyst', 'Group Strategy Framework + 5-Year Plan governance', 'next Strategy Council + Board strategy day', 'Map every recommendation to the strategic pillar it serves and classify as Build / Buy / Partner / Stop and cite the source file.', 'Petakan setiap rekomendasi ke pilar strategis yang dilayani dan klasifikasikan sebagai Build / Buy / Partner / Stop dan kutip file sumber.'),
    'dept-mkt':     ('Group CMO and Head of Brand campaign-review analyst', 'Brand Guidelines + Group Communications policy', 'next Marketing Council + brand-equity tracker review', 'Tag every campaign by audience / channel / phase and classify as On-Track / At-Risk / Re-Plan and cite the source file.', 'Tag setiap kampanye berdasarkan audience / channel / fase dan klasifikasikan sebagai On-Track / At-Risk / Re-Plan dan kutip file sumber.'),
    'dept-esg':     ('Group Chief Sustainability Officer and ESG Lead disclosure analyst', 'GRI + IFRS S1/S2 + Bursa / IDX sustainability reporting standards', 'next Sustainability Committee + investor ESG roadshow', 'Tag every disclosure by E / S / G pillar and classify materiality as Material / Notable / Watchlist and cite the source file.', 'Tag setiap disclosure berdasarkan pilar E / S / G dan klasifikasikan materialitas sebagai Material / Notable / Watchlist dan kutip file sumber.'),
    'dept-ops':     ('COO and Head of Operations excellence-review analyst', 'Operating Model design + KPI dictionary', 'next Operating Committee + functional QBR', 'Tag every initiative by function / site / programme and classify as Run / Change / Transform and cite the source file.', 'Tag setiap inisiatif berdasarkan fungsi / lokasi / program dan klasifikasikan sebagai Run / Change / Transform dan kutip file sumber.'),
    'dept-corpsec': ('Company Secretary and Head of Governance Board-prep analyst', 'Bursa / IDX listing rules + Companies Act minute-keeping standard', 'next Board / committee meeting pack', 'Classify every Board paper as Decision / Discussion / Information and cite the source file + section.', 'Klasifikasikan setiap Board paper sebagai Decision / Discussion / Information dan kutip file + bagian sumber.'),
    'dept-ir':      ('Head of Investor Relations and Group CFO disclosure analyst', 'Bursa / IDX continuing-disclosure rules + Reg-FD-equivalent fairness', 'next quarterly results call + investor-day prep', 'Pre-empt every analyst concern by mapping it to a published disclosure and tag as On-Message / Risk / Off-Limits and cite the source file.', 'Antisipasi setiap kekhawatiran analis dengan memetakannya ke disclosure yang dipublikasikan dan tag sebagai On-Message / Risk / Off-Limits dan kutip file sumber.'),
    'dept-proc':    ('Chief Procurement Officer and Head of Supplier Risk savings-review analyst', 'Group Procurement policy + supplier code of conduct', 'next Procurement Council + savings-tracker close-out', 'Tag every saving by category / supplier and classify as Realised / Run-Rate / At-Risk and cite the source file.', 'Tag setiap saving berdasarkan kategori / supplier dan klasifikasikan sebagai Realised / Run-Rate / At-Risk dan kutip file sumber.'),
    'dept-it':      ('Group CIO and Head of Cyber operating-review analyst', 'ISO 27001 + Group cyber-resilience framework', 'next Technology Council + Cyber sub-committee', 'Tag every issue by service / domain / stage and classify as Run / Change / Cyber / Compliance and cite the source file.', 'Tag setiap masalah berdasarkan service / domain / tahap dan klasifikasikan sebagai Run / Change / Cyber / Compliance dan kutip file sumber.'),
}

# Use-case taxonomy: one of 13 canonical notebook events, picked by keyword
# matching the entry's tagline + scenario. Mirrors Microsoft's published
# Notebook patterns (Persol = RFP scoring; AECOM = bid pursuit; PWC = audit
# response; Sanofi = clinical case; Pfizer = regulator submission; etc.) —
# every notebook becomes a "single grounded source" for ONE specific event.
# (event_name_EN, deliverable_EN, framing_EN, event_name_ID, deliverable_ID, framing_ID)
_NB_USECASES = {
    'rfp':       ('RFP scoring marathon', 'RFP scoring memo + supplier short-list',
                  'For every shortlisted supplier output a Strengths / Risks / Conditions block tied to the scoring rubric.',
                  'maraton penilaian RFP', 'memo penilaian RFP + shortlist supplier',
                  'Untuk setiap supplier shortlist keluarkan blok Kekuatan / Risiko / Syarat yang terikat ke rubrik penilaian.'),
    'ma':        ('M&A target due-diligence', 'diligence findings memo + go/no-go recommendation',
                  'For every red flag produce an Action / Owner / Pre-close-condition entry with valuation impact.',
                  'due-diligence target M&A', 'memo temuan due-diligence + rekomendasi go/no-go',
                  'Untuk setiap red flag hasilkan entry Aksi / Pemilik / Syarat-Pra-Closing dengan dampak valuasi.'),
    'lender':    ('lender refinancing & covenant engagement', 'lender pack: covenant cure plan + refi options',
                  'Tag every covenant by Headroom / Breach-Risk / Cure-Path and bring the Information Memorandum thread.',
                  'engagement refinancing & covenant lender', 'lender pack: rencana cure covenant + opsi refinancing',
                  'Tag setiap covenant berdasarkan Headroom / Breach-Risk / Cure-Path dan bawa benang IM.'),
    'regulator': ('regulator submission cycle', 'regulator response submission with full audit trail',
                  'Number every regulator query and cite the source file + paragraph that answers it.',
                  'siklus submisi regulator', 'submisi tanggapan regulator dengan jejak audit lengkap',
                  'Beri nomor pada setiap pertanyaan regulator dan kutip file sumber + paragraf yang menjawabnya.'),
    'audit':     ('Bursa / SCM / OJK enquiry response', 'audit-response binder + management letter',
                  'Tag every finding as Material / Notable / Watch and cite the file + section that supports the position.',
                  'tanggapan enquiry Bursa / SCM / OJK', 'binder tanggapan audit + management letter',
                  'Tag setiap temuan sebagai Material / Notable / Watch dan kutip file + bagian yang mendukung posisi.'),
    'recall':    ('customer recall & quality crisis', 'customer recovery memo + recall-scope decision',
                  'For every affected SKU / batch / lot tag as Recall-In-Field / Recall-In-Stock / Hold with recovery cost.',
                  'recall pelanggan & krisis kualitas', 'memo recovery pelanggan + keputusan scope recall',
                  'Untuk setiap SKU / batch / lot terdampak tag sebagai Recall-In-Field / Recall-In-Stock / Hold dengan biaya recovery.'),
    'earnings':  ('pre-results blackout window', 'results-day pack: Q&A bank + IR script + Board paper',
                  'Pre-empt every analyst concern by mapping to a published disclosure and tag On-Message / Risk / Off-Limits.',
                  'window blackout pra-hasil', 'pack hari hasil: bank Q&A + skrip IR + Board paper',
                  'Antisipasi setiap kekhawatiran analis dengan memetakan ke disclosure terpublikasi dan tag On-Message / Risk / Off-Limits.'),
    'board':     ('emergency Board variance review', 'Board paper + variance bridge + recovery programme',
                  'Classify every divisional recommendation as Red / Amber / Green and tie to the EBITDA bridge component it serves.',
                  'review variance Board darurat', 'Board paper + bridge variance + program recovery',
                  'Klasifikasikan setiap rekomendasi divisional sebagai Merah / Kuning / Hijau dan kaitkan ke komponen EBITDA bridge yang dilayani.'),
    'clinical':  ('clinical case-conference / M&M review', 'case-conference brief + clinical-quality recommendations',
                  'De-identify all patient detail (use case IDs) and tag every finding as Clinical-Quality / Patient-Safety / Compliance.',
                  'review konferensi kasus klinis / M&M', 'brief konferensi kasus + rekomendasi clinical-quality',
                  'De-identifikasi semua detail pasien (gunakan case ID) dan tag setiap temuan sebagai Clinical-Quality / Patient-Safety / Compliance.'),
    'customer':  ('major-account recovery / churn save', 'customer recovery memo + remediation plan',
                  'For every named account tag as Save / Right-Size / Exit and cite the contract clause that backs the position.',
                  'recovery major-account / churn save', 'memo recovery pelanggan + rencana remediasi',
                  'Untuk setiap akun bernama tag sebagai Save / Right-Size / Exit dan kutip klausul kontrak yang mendukung posisi.'),
    'incident':  ('incident / outage post-mortem', 'incident root-cause memo + customer-impact note',
                  'Tag each finding as Process / People / Tech / Comms with named owner and time-to-cure.',
                  'post-mortem insiden / outage', 'memo root-cause insiden + catatan dampak-pelanggan',
                  'Tag setiap temuan sebagai Process / People / Tech / Comms dengan pemilik bernama dan time-to-cure.'),
    'esg':       ('ESG / sustainability disclosure cycle', 'sustainability statement + materiality matrix update',
                  'Tag every disclosure by E / S / G pillar and classify materiality as Material / Notable / Watchlist.',
                  'siklus disclosure ESG / sustainability', 'statement sustainability + update materiality matrix',
                  'Tag setiap disclosure berdasarkan pilar E / S / G dan klasifikasikan materialitas sebagai Material / Notable / Watchlist.'),
    'strategy':  ('5-year plan refresh', '5-year plan paper + capital-allocation case',
                  'Map every initiative to a strategic pillar and classify as Build / Buy / Partner / Stop with NPV anchor.',
                  'refresh rencana 5-tahun', 'paper rencana 5-tahun + case alokasi modal',
                  'Petakan setiap inisiatif ke pilar strategis dan klasifikasikan sebagai Build / Buy / Partner / Stop dengan anchor NPV.'),
}

# Per-archetype short-list of plausible use-cases — ordered by how natural
# each event is for that industry. Detector picks the FIRST keyword match
# inside this short-list, so a hospital can never land on RFP scoring even
# if the scenario happens to contain "tender" anywhere.
_NB_ARCHETYPE_USECASES = {
    'bank':         ['lender', 'regulator', 'earnings', 'audit'],
    'islamic':      ['regulator', 'lender', 'audit'],
    'fintech':      ['regulator', 'incident', 'audit'],
    'insur':        ['regulator', 'recall', 'audit', 'earnings'],
    'hc':           ['clinical', 'regulator', 'recall'],
    'energy':       ['incident', 'regulator', 'recall', 'esg'],
    'mfg':          ['recall', 'audit', 'incident', 'customer'],
    'agri':         ['esg', 'audit', 'regulator'],
    'retail':       ['customer', 'recall', 'incident'],
    'hosp':         ['customer', 'incident', 'audit'],
    'tech':         ['incident', 'customer', 'regulator'],
    'trans':        ['incident', 'audit', 'regulator', 'customer'],
    'pub':          ['regulator', 'audit', 'esg'],
    'prop':         ['lender', 'regulator', 'audit'],
    'edu':          ['audit', 'regulator', 'strategy'],
    'congl':        ['board', 'ma', 'lender', 'strategy'],
    'dept-fin':     ['lender', 'audit', 'board', 'earnings'],
    'dept-hr':      ['strategy', 'audit', 'incident'],
    'dept-legal':   ['regulator', 'audit', 'ma'],
    'dept-risk':    ['incident', 'audit', 'regulator'],
    'dept-strat':   ['ma', 'strategy', 'board'],
    'dept-mkt':     ['customer', 'strategy'],
    'dept-esg':     ['esg', 'audit'],
    'dept-ops':     ['incident', 'strategy', 'recall'],
    'dept-corpsec': ['board', 'regulator', 'audit'],
    'dept-ir':      ['earnings', 'regulator'],
    'dept-proc':    ['rfp', 'customer', 'audit'],
    'dept-it':      ['incident', 'audit'],
}

# Use-case lane — what review/handoff each event delivers into. Lets us pair
# archetype "named roles" with a use-case-aware "lane" so the language stays
# coherent ("Medical Director, leading the M&M case-conference" — not
# "Medical Director...case-conference analyst...for the RFP scoring marathon").
# Lanes are short noun phrases, EN+ID, dropped into "leading the {lane}".
_NB_USECASE_LANE = {
    'rfp':       ('RFP scoring marathon',                 'maraton penilaian RFP'),
    'ma':        ('M&A target due-diligence',             'due-diligence target M&A'),
    'lender':    ('lender refinancing & covenant cure',   'cure refinancing & covenant lender'),
    'regulator': ('regulator submission cycle',           'siklus submisi regulator'),
    'audit':     ('Bursa / SCM / OJK enquiry response',   'tanggapan enquiry Bursa / SCM / OJK'),
    'recall':    ('customer recall & quality crisis',     'recall pelanggan & krisis kualitas'),
    'earnings':  ('pre-results blackout package',         'paket blackout pra-hasil'),
    'clinical':  ('clinical M&M / case-conference review','review M&M klinis / konferensi kasus'),
    'customer':  ('major-account recovery campaign',      'kampanye recovery major-account'),
    'incident':  ('incident / outage post-mortem',        'post-mortem insiden / outage'),
    'esg':       ('ESG / sustainability disclosure cycle','siklus disclosure ESG / sustainability'),
    'strategy':  ('5-year plan refresh',                  'refresh rencana 5-tahun'),
    'board':     ('emergency Board variance review',      'review variance Board darurat'),
}

# Use-case keyword detector. Reuses regex in _NB_USECASES, narrowed to the
# archetype's short-list at decision time so out-of-domain matches are blocked.
_NB_USECASE_PATTERNS = [
    ('rfp',       r'\brfp\b|\btender\b|supplier panel|sourcing event|reverse auction|panel of suppliers|panel award'),
    ('ma',        r'\bm&a\b|\bm and a\b|acquisition|target screen|due[- ]?diligence|integration program|carve[- ]?out|merger|takeover|bidder'),
    ('lender',    r'lender|covenant|refinanc|maturity wall|debt stack|sukuk|credit facility|syndicat|bond tap|coupon|holding line'),
    ('regulator', r'regulator|bnm|ojk|mas|scm|bursa enquiry|idx enquiry|enforcement notice|supervisory|clarification letter|show[- ]cause|moh|kkm|kemenkes|jci'),
    ('audit',     r'\baudit\b|disclosure breach|continuing disclosure|internal audit|external audit|management letter|qualified opinion'),
    ('recall',    r'recall|product safety|defect|batch hold|quality issue|complaint surge|lot rejection|customer hold'),
    ('earnings',  r'earnings|results call|investor day|blackout|guidance|consensus|preliminary results|analyst day|results pack'),
    ('clinical',  r'clinical|patient case|m&m|morbidity|adverse event|case conference|sentinel event|near miss|jci|bed occupancy|infection|safety event'),
    ('customer',  r'churn|\bnps\b|customer recovery|major account|key account|sla breach|claim|hold note|stop[- ]work|trade huddle|sss\b|same-store'),
    ('incident',  r'incident|outage|breach|leak|spill|fire|blast|cyber attack|ransomware|data leak|near[- ]miss'),
    ('esg',       r'esg|sustainability report|tcfd|gri|ifrs s\d|net[- ]zero|emissions disclosure|csrd|rspo|ispo|ndpe|nikkanjo|carbon|deforestation'),
    ('strategy',  r'strategy refresh|5[- ]year plan|operating model|transformation programme|portfolio reshape'),
    ('board',     r'board[- ]pack|emergency board|variance|adverse|missed.*ebitda|board paper|board[- ]risk'),
]
_NB_PATTERN_MAP = {k: _nb_re.compile(p, _nb_re.IGNORECASE) for k, p in _NB_USECASE_PATTERNS}

def _nb_usecase(entry):
    arche = _nb_archetype(entry.get('id'))
    allowed = _NB_ARCHETYPE_USECASES.get(arche) or ['board']
    text = ' '.join([
        str(entry.get('tagline') or ''),
        str(entry.get('scenario') or ''),
        str(entry.get('name') or ''),
        str(entry.get('id') or ''),
    ]).lower()
    # Prefer specificity inside the archetype's allowed set
    for tag in allowed:
        rx = _NB_PATTERN_MAP.get(tag)
        if rx and rx.search(text):
            return tag
    # No keyword hit — first item in archetype short-list is the natural default
    return allowed[0]

def _nb_first_sentence(s):
    if not s: return ''
    s = str(s).strip()
    m = _nb_re.search(r'(.+?[\.!\?])(\s|$)', s)
    return (m.group(1) if m else s[:160]).strip()

def _nb_named_files(meta, max_files=3):
    src = meta.get('sources') or []
    names = []
    for s in src:
        if not isinstance(s, dict): continue
        nm = s.get('name') or s.get('label') or ''
        if not nm: continue
        if 'Copilot_Notebook_Demo_Guide' in nm or 'Copilot Notebook Demo Guide' in nm:
            continue
        names.append(nm)
        if len(names) >= max_files:
            break
    return names

# Per-archetype "named roles" (short noun phrase, no "...analyst" suffix).
# Format: (named_roles_EN, regulator_EN_or_governance_anchor)
_NB_ROLES = {
    'bank':         ('Group CFO and Group Treasurer',                     'BNM (MY) / OJK (ID) / MAS (SG) prudential and SCM disclosure'),
    'islamic':      ('Shariah Committee secretariat',                     'IFSA + AAOIFI Shariah governance'),
    'fintech':      ('Group CRO and Compliance Lead',                     'BNM e-money / OJK PUJK / MAS PSA licensing'),
    'insur':        ('Chief Actuary and Group CFO',                       'BNM RBC / OJK SLOJK / MAS RBC2 solvency framework'),
    'hc':           ('Medical Director and Chief Nurse',                  'PDPA (MY) / UU PDP (ID) and MOH clinical-governance standards'),
    'energy':       ('HSSE Director and Operations VP',                   'DOSH (MY) / KemenESDM (ID) / MOM (SG) HSE reporting and Bursa / IDX disclosure'),
    'mfg':          ('Plant Manager and QA Director',                     'Customer Quality Agreement and ISO 9001 / IATF 16949 batch-traceability'),
    'agri':         ('Sustainability Manager and Estate GM',              'RSPO / ISPO / MSPO / NDPE certification audit'),
    'retail':       ('Category Manager and Store Operations VP',          'Category Performance Review + Loyalty Privacy policy'),
    'hosp':         ('General Manager and Director of Operations',        'Brand Standard audit + Guest Privacy policy'),
    'tech':         ('SVP Product and SVP Engineering',                   'SLA + DPA contractual obligations and tenant-side DLP'),
    'trans':        ('Port Captain and Operations Director',              'IMO / port-state authority and customs-broker compliance'),
    'pub':          ('Permanent Secretary and Communications Director',   'BPK / AGD / National Audit Department audit-trail standard'),
    'prop':         ('Project Director and Asset Management VP',          'Sales & Purchase Agreement + REIT trustee disclosure'),
    'edu':          ('Vice-Chancellor and Registrar',                     'MQA / Kemdikbud / SkillsFuture academic-quality audit'),
    'congl':        ('Group CFO and Chief of Staff',                      'Bursa / IDX dual-listing disclosure and SCM / OJK enquiries'),
    'dept-fin':     ('Group CFO and Head of FP&A',                        'Group Finance close calendar + variance protocol'),
    'dept-hr':      ('Group CHRO and Head of Talent',                     'PDPA (MY) / UU PDP (ID) employee-data protection'),
    'dept-legal':   ('Group General Counsel and Head of Litigation',      'privilege protocol + matter-management standard'),
    'dept-risk':    ('Group CRO and Head of ORM',                         'Group Risk Appetite Statement + BNM / OJK / MAS supervisory expectations'),
    'dept-strat':   ('Group Chief of Staff and Head of Strategy',         'Group Strategy Framework + 5-Year Plan governance'),
    'dept-mkt':     ('Group CMO and Head of Brand',                       'Brand Guidelines + Group Communications policy'),
    'dept-esg':     ('Group Chief Sustainability Officer and ESG Lead',   'GRI + IFRS S1/S2 + Bursa / IDX sustainability reporting standards'),
    'dept-ops':     ('COO and Head of Operations',                        'Operating Model design + KPI dictionary'),
    'dept-corpsec': ('Company Secretary and Head of Governance',          'Bursa / IDX listing rules + Companies Act minute-keeping standard'),
    'dept-ir':      ('Head of Investor Relations and Group CFO',          'Bursa / IDX continuing-disclosure rules + Reg-FD-equivalent fairness'),
    'dept-proc':    ('Chief Procurement Officer and Head of Supplier Risk','Group Procurement policy + supplier code of conduct'),
    'dept-it':      ('Group CIO and Head of Cyber',                       'ISO 27001 + Group cyber-resilience framework'),
}

# Per-use-case framing (deliverable + Tag/RAG rule), EN + ID
_NB_FRAMING = {
    'rfp':       ('RFP scoring memo + supplier short-list',
                  'For every shortlisted supplier emit a Strengths / Risks / Conditions block tied to the scoring rubric.',
                  'memo penilaian RFP + shortlist supplier',
                  'Untuk setiap supplier shortlist keluarkan blok Kekuatan / Risiko / Syarat yang terikat ke rubrik penilaian.'),
    'ma':        ('diligence findings memo + go/no-go recommendation',
                  'For every red flag produce an Action / Owner / Pre-close-condition entry with valuation impact.',
                  'memo temuan due-diligence + rekomendasi go/no-go',
                  'Untuk setiap red flag hasilkan entry Aksi / Pemilik / Syarat-Pra-Closing dengan dampak valuasi.'),
    'lender':    ('lender pack: covenant cure plan + refi options',
                  'Tag every covenant by Headroom / Breach-Risk / Cure-Path and bring the IM thread.',
                  'lender pack: rencana cure covenant + opsi refinancing',
                  'Tag setiap covenant berdasarkan Headroom / Breach-Risk / Cure-Path dan bawa benang IM.'),
    'regulator': ('regulator response submission with full audit trail',
                  'Number every regulator query and cite the source file + paragraph that answers it.',
                  'submisi tanggapan regulator dengan jejak audit lengkap',
                  'Beri nomor pada setiap pertanyaan regulator dan kutip file sumber + paragraf yang menjawabnya.'),
    'audit':     ('audit-response binder + management letter',
                  'Tag every finding as Material / Notable / Watch and cite the file + section that supports the position.',
                  'binder tanggapan audit + management letter',
                  'Tag setiap temuan sebagai Material / Notable / Watch dan kutip file + bagian yang mendukung posisi.'),
    'recall':    ('customer recovery memo + recall-scope decision',
                  'For every affected SKU / batch / lot tag as Recall-In-Field / Recall-In-Stock / Hold with recovery cost.',
                  'memo recovery pelanggan + keputusan scope recall',
                  'Untuk setiap SKU / batch / lot terdampak tag sebagai Recall-In-Field / Recall-In-Stock / Hold dengan biaya recovery.'),
    'earnings':  ('results-day pack: Q&A bank + IR script + Board paper',
                  'Pre-empt every analyst concern by mapping to a published disclosure and tag On-Message / Risk / Off-Limits.',
                  'pack hari hasil: bank Q&A + skrip IR + Board paper',
                  'Antisipasi setiap kekhawatiran analis dengan memetakan ke disclosure terpublikasi dan tag On-Message / Risk / Off-Limits.'),
    'clinical':  ('case-conference brief + clinical-quality recommendations',
                  'De-identify all patient detail (use case IDs) and tag every finding as Clinical-Quality / Patient-Safety / Compliance.',
                  'brief konferensi kasus + rekomendasi clinical-quality',
                  'De-identifikasi semua detail pasien (gunakan case ID) dan tag setiap temuan sebagai Clinical-Quality / Patient-Safety / Compliance.'),
    'customer':  ('customer recovery memo + remediation plan',
                  'For every named account tag as Save / Right-Size / Exit and cite the contract clause that backs the position.',
                  'memo recovery pelanggan + rencana remediasi',
                  'Untuk setiap akun bernama tag sebagai Save / Right-Size / Exit dan kutip klausul kontrak yang mendukung posisi.'),
    'incident':  ('incident root-cause memo + customer-impact note',
                  'Tag each finding as Process / People / Tech / Comms with named owner and time-to-cure.',
                  'memo root-cause insiden + catatan dampak-pelanggan',
                  'Tag setiap temuan sebagai Process / People / Tech / Comms dengan pemilik bernama dan time-to-cure.'),
    'esg':       ('sustainability statement + materiality matrix update',
                  'Tag every disclosure by E / S / G pillar and classify materiality as Material / Notable / Watchlist.',
                  'statement sustainability + update materiality matrix',
                  'Tag setiap disclosure berdasarkan pilar E / S / G dan klasifikasikan materialitas sebagai Material / Notable / Watchlist.'),
    'strategy':  ('5-year plan paper + capital-allocation case',
                  'Map every initiative to a strategic pillar and classify as Build / Buy / Partner / Stop with NPV anchor.',
                  'paper rencana 5-tahun + case alokasi modal',
                  'Petakan setiap inisiatif ke pilar strategis dan klasifikasikan sebagai Build / Buy / Partner / Stop dengan anchor NPV.'),
    'board':     ('Board paper + variance bridge + recovery programme',
                  'Classify every divisional recommendation as Red / Amber / Green and tie to the EBITDA bridge component.',
                  'Board paper + bridge variance + program recovery',
                  'Klasifikasikan setiap rekomendasi divisional sebagai Merah / Kuning / Hijau dan kaitkan ke komponen EBITDA bridge.'),
}

def _build_nb_instructions(entry, meta):
    arche = _nb_archetype(entry.get('id'))
    use_tag = _nb_usecase(entry)
    roles_en, regulator = _NB_ROLES.get(arche, _NB_ROLES['congl'])
    lane_en, lane_id = _NB_USECASE_LANE[use_tag]
    deliv_en, frame_en, deliv_id, frame_id = _NB_FRAMING[use_tag]
    company = entry.get('company') or entry.get('name') or 'Zava'
    company_id = entry.get('companyID') or company
    burning = _nb_first_sentence(entry.get('tagline') or '')
    burning_id = _nb_first_sentence(entry.get('taglineID') or burning)
    n_src = len(meta.get('sources') or []) or 5
    files = _nb_named_files(meta, 3)
    files_phrase_en = ''
    files_phrase_id = ''
    if files:
        names_inline = ', '.join(f"`{f}`" for f in files)
        files_phrase_en = f"Named anchor files for this cycle: {names_inline}. "
        files_phrase_id = f"File anchor bernama untuk siklus ini: {names_inline}. "
    # Lead with the entry-unique tagline so each instruction's first chars are
    # different on the rendered page. Then event + persona + governance.
    en = (
        f"Trigger: \"{burning}\". "
        f"This notebook is the {company} grounded source for the {lane_en} — "
        f"the {roles_en} convene the workstream. "
        f"{files_phrase_en}"
        f"Synthesise across ALL {n_src} sources. Use {regulator} as the governance reference. "
        f"Every answer must cite the source file by name and the tab / section. "
        f"Frame the output for the {deliv_en}. {frame_en} "
        f"Tone: precise, evidence-only, never speculative."
    )
    idn = (
        f"Pemicu: \"{burning_id}\". "
        f"Notebook ini adalah sumber tertanam {company_id} untuk {lane_id} — "
        f"{roles_en} memimpin workstream. "
        f"{files_phrase_id}"
        f"Sintesakan SEMUA {n_src} sumber. Gunakan {regulator} sebagai referensi tata kelola. "
        f"Setiap jawaban harus mengutip file sumber berdasarkan nama dan tab / bagian. "
        f"Bingkai output untuk {deliv_id}. {frame_id} "
        f"Nada: presisi, hanya berdasarkan bukti, tidak pernah spekulatif."
    )
    return en, idn, use_tag

def _uniquify_nb_instructions(entries):
    """Rewrite EVERY notebookMeta instruction so each entry is anchored to its
    own unique business event AND its own tagline. The instruction LEADS with
    the entry-specific tagline so first-glance uniqueness is visible.
    """
    rewritten = 0
    bucket_counts = {}
    for e in entries:
        for tool in e.get('prompts') or []:
            if 'Copilot Notebook' not in (tool.get('tool') or ''):
                continue
            meta = tool.get('notebookMeta') or {}
            if not meta:
                continue
            en_new, id_new, use_tag = _build_nb_instructions(e, meta)
            meta['instructions'] = en_new
            meta['instructionsID'] = id_new
            tool['notebookMeta'] = meta
            rewritten += 1
            bucket_counts[use_tag] = bucket_counts.get(use_tag, 0) + 1
    return rewritten, bucket_counts

try:
    _nb_uniq_i, _nb_buckets_i = _uniquify_nb_instructions(all_industries)
    _nb_uniq_d, _nb_buckets_d = _uniquify_nb_instructions(all_departments)
    _nb_total = _nb_uniq_i + _nb_uniq_d
    _nb_combined = {}
    for _b in (_nb_buckets_i, _nb_buckets_d):
        for _k, _v in _b.items():
            _nb_combined[_k] = _nb_combined.get(_k, 0) + _v
    print(f"Notebook unique scenarios — rewrote {_nb_total} notebookMeta blocks")
    print(f"  Use-case distribution: " + ", ".join(f"{k}={v}" for k, v in sorted(_nb_combined.items(), key=lambda x: -x[1])))
except Exception as _e:
    print(f"(Notebook uniquify skipped due to error: {_e})")


# ── Cowork approval gate: append a human-approval sentence to every cowork prompt ──
# Per Aaron Yue / OneDrive File Intelligence canonical pattern, every Cowork prompt
# that may send/post external content must end with a human approval gate so the
# delegation pauses for review before changing state.
_AG_EN = ' Wait for my approval before sending anything externally or posting to channels.'
_AG_ID = ' Tunggu persetujuan saya sebelum mengirim apa pun secara eksternal atau memposting ke channel.'
_AG_BM = ' Tunggu kelulusan saya sebelum menghantar apa-apa secara luaran atau menyiarkan di saluran.'
_AG_KEYS_EN = ['confirm each task','my approval','approval before','wait for me','wait for my','wait for approval','wait until','before sending','await sign','await my','before externalising','review with me','before externally','do not send','no external comm','hold for review']
_AG_KEYS_ID = ['konfirmasi','persetujuan saya','tunggu persetujuan','sebelum mengirim','jangan kirim','jangan post','tahan dulu','sebelum eksternal','sebelum menyiarkan','konfirmasikan']
_AG_KEYS_BM = ['kelulusan saya','tunggu kelulusan','sebelum menghantar','jangan hantar','sebelum siar','luluskan dahulu','sebelum luaran','sahkan dahulu']
def _has_gate(text, lang):
    if not text: return True
    low = text.lower()
    if lang == 'EN': return any(k in low for k in _AG_KEYS_EN)
    if lang == 'ID': return any(k in low for k in _AG_KEYS_ID)
    if lang == 'BM': return any(k in low for k in _AG_KEYS_BM)
    return True
def _normalize_cowork(entries):
    fixed = 0
    for e in entries:
        for tool in e.get('prompts') or []:
            if 'Cowork' not in (tool.get('tool') or ''):
                continue
            for arr_key, lang, gate in [('prompts','EN',_AG_EN),('promptsID','ID',_AG_ID),('promptsBM','BM',_AG_BM)]:
                arr = tool.get(arr_key) or []
                for p in arr:
                    if not isinstance(p, dict): continue
                    body = p.get('prompt') or ''
                    if body and not _has_gate(body, lang):
                        p['prompt'] = body.rstrip() + gate
                        fixed += 1
    return fixed
try:
    _gate_fixed = _normalize_cowork(all_industries) + _normalize_cowork(all_departments)
    print(f"Cowork approval gate appended to {_gate_fixed} prompts")
except Exception as _e:
    print(f"(Cowork approval gate normalise skipped due to error: {_e})")

# ── Cowork recipient diversification ─────────────────────────────────────
# User feedback: "the cowork one... why all so similar prompts one... each
# and everyone in the industries and departments"
# Diagnosis: every Cowork prompt (220+ across 55 entries) carried the SAME
# 6-name appendix (Hadar / Sasha / Daichi / Sonia / Will / Omar). At a
# glance every Cowork block looked identical even though the 5-action
# bodies are unique.
# Fix: build-time replacement of the generic appendix with an entry-
# archetype-specific 6-person cast (Banking gets BNM/CFO/Treasurer/Wholesale-
# Risk casting; Healthcare gets Medical-Director/Chief-Nurse/Pharmacy/Quality;
# Manufacturing gets Plant-Manager/QA/Customer-Recovery/S&OP; etc.). Each
# cast keeps 1-2 of the 4 canonical Hadar/Sasha/Daichi/Mod-Admin personas
# for persona consistency. Defined in cowork_recipient_casts.py.
try:
    from cowork_recipient_casts import diversify_cowork_recipients as _divcw
    _divcw_fixed = _divcw(all_industries) + _divcw(all_departments)
    print(f"Cowork recipients diversified on {_divcw_fixed} prompts")
except Exception as _e:
    print(f"(Cowork recipient diversify skipped due to error: {_e})")

# ── W/P/X Agent consistency: ensure every Word / PowerPoint / Excel Agent block
# carries TWO prompts (matching the General reference). Where an entry shipped
# only one prompt, append a second "follow-up executive summary" deliverable
# using the canonical "Stay in chat. Type the next prompt." instr. ──
_W_LABEL = '\U0001F4DD Word Agent (Generate document)'
_P_LABEL = '\U0001F3AF PowerPoint Agent (Generate deck)'
_X_LABEL = '\U0001F4CA Excel Agent (Generate workbook)'
_STAY_EN = "Stay in `m365.cloud.microsoft/chat`. Type the next prompt."
_STAY_ID = "Tetap di `m365.cloud.microsoft/chat`. Ketik prompt berikut."
_STAY_BM = "Kekal di `m365.cloud.microsoft/chat`. Taip prompt seterusnya."
_FU_WORD = {
    'EN': "Generate a follow-up 1-page executive summary `.docx` named ExecSummary_{eid}.docx that condenses the deliverable above into a five-bullet headline, a RAG status box, and a decisions-required block. Cite the same source files as the previous prompt. Tone: tight, audience CEO and Chair.",
    'ID': "Hasilkan ringkasan eksekutif satu halaman lanjutan dalam bentuk `.docx` bernama Ringkasan_Eksekutif_{eid}.docx yang merangkum deliverable di atas menjadi headline lima bullet, kotak status RAG, dan blok keputusan yang diperlukan. Kutip file sumber yang sama dengan prompt sebelumnya. Nada padat, audiens Direktur Utama dan Komisaris Utama.",
    'BM': "Hasilkan ringkasan eksekutif satu muka surat susulan dalam bentuk `.docx` bernama Ringkasan_Eksekutif_{eid}.docx yang merumuskan deliverable di atas menjadi tajuk utama lima poin, kotak status RAG, dan blok keputusan diperlukan. Petik fail sumber yang sama seperti prompt sebelumnya. Nada padat, audiens CEO dan Pengerusi.",
}
_FU_PPT = {
    'EN': "Generate a follow-up 5-slide town-hall pre-read `.pptx` named TownHall_PreRead_{eid}.pptx covering the same theme but pitched to mid-management. Slides: (1) Title and Disclaimer; (2) Why we are doing this; (3) What changes for you; (4) What we ask of you; (5) Q&A. Cite the same source files as the previous prompt. Use the same brand colours.",
    'ID': "Hasilkan deck pra-baca town-hall 5 slide lanjutan `.pptx` bernama PreRead_TownHall_{eid}.pptx mencakup tema yang sama tetapi ditujukan untuk middle-management. Slide: (1) Judul dan Disclaimer; (2) Mengapa kami melakukan ini; (3) Apa yang berubah untuk Anda; (4) Apa yang kami minta dari Anda; (5) Q&A. Kutip file sumber yang sama dengan prompt sebelumnya. Gunakan warna brand yang sama.",
    'BM': "Hasilkan deck pra-baca town-hall 5 slaid susulan `.pptx` bernama PreRead_TownHall_{eid}.pptx merangkumi tema yang sama tetapi disasarkan kepada pengurusan pertengahan. Slaid: (1) Tajuk dan Disclaimer; (2) Mengapa kami melakukan ini; (3) Apa yang berubah untuk anda; (4) Apa yang kami minta dari anda; (5) Q&A. Petik fail sumber yang sama seperti prompt sebelumnya. Guna warna jenama yang sama.",
}
_FU_XLS = {
    'EN': "Generate a follow-up 1-page scorecard `.xlsx` named Scorecard_{eid}.xlsx with one sheet 'Exec View' carrying KPI tiles for the top 6 metrics from the workbook above (Target / Actual / Variance / RAG status). Apply conditional formatting on the Variance column (Red < -10%, Amber -5% to -10%, Green > -5%). Cite the same source files as the previous prompt.",
    'ID': "Hasilkan scorecard satu halaman lanjutan `.xlsx` bernama Scorecard_{eid}.xlsx dengan satu sheet 'Exec View' berisi tile KPI untuk 6 metrik teratas dari workbook di atas (Target / Aktual / Selisih / Status RAG). Terapkan format kondisional pada kolom Selisih (Merah < -10%, Kuning -5% sampai -10%, Hijau > -5%). Kutip file sumber yang sama dengan prompt sebelumnya.",
    'BM': "Hasilkan scorecard satu muka surat susulan `.xlsx` bernama Scorecard_{eid}.xlsx dengan satu helaian 'Exec View' membawa tile KPI untuk 6 metrik teratas dari workbook di atas (Sasaran / Sebenar / Varians / Status RAG). Gunakan format bersyarat pada lajur Varians (Merah < -10%, Kuning -5% hingga -10%, Hijau > -5%). Petik fail sumber yang sama seperti prompt sebelumnya.",
}
def _normalize_wxp_agent(entries):
    fixed = 0
    stay_fixed = 0
    for e in entries:
        eid = (e.get('id') or 'entry').replace('-', '_')
        for tool in e.get('prompts') or []:
            label = tool.get('tool') or ''
            if label == _W_LABEL:
                tmpl = _FU_WORD
            elif label == _P_LABEL:
                tmpl = _FU_PPT
            elif label == _X_LABEL:
                tmpl = _FU_XLS
            else:
                continue
            for arr_key, lang, stay in [
                ('prompts',   'EN', _STAY_EN),
                ('promptsID', 'ID', _STAY_ID),
                ('promptsBM', 'BM', _STAY_BM),
            ]:
                arr = tool.get(arr_key)
                if arr is None:
                    continue
                if len(arr) == 0:
                    continue
                if len(arr) < 2:
                    tool[arr_key] = list(arr) + [{
                        'instr': stay,
                        'prompt': tmpl[lang].format(eid=eid),
                    }]
                    fixed += 1
                    continue
                # Force canonical "Stay in chat" instr on every prompt at index >= 1
                arr2 = list(arr)
                for j in range(1, len(arr2)):
                    p = arr2[j]
                    if not isinstance(p, dict):
                        continue
                    cur_instr = (p.get('instr') or '').lower()
                    has_stay = ('stay in `m365' in cur_instr) or ('tetap di `m365' in cur_instr) or ('kekal di `m365' in cur_instr)
                    if not has_stay:
                        p['instr'] = stay
                        stay_fixed += 1
                tool[arr_key] = arr2
    return fixed, stay_fixed
try:
    _wxp_a, _wxp_b = 0, 0
    for _coll in (all_industries, all_departments):
        _a, _b = _normalize_wxp_agent(_coll)
        _wxp_a += _a; _wxp_b += _b
    print(f"W/P/X Agent 2nd-prompt appended on {_wxp_a} arrays")
    print(f"W/P/X Agent 2nd-instr forced to 'Stay in chat' on {_wxp_b} prompts")
except Exception as _e:
    print(f"(W/P/X Agent normaliser skipped due to error: {_e})")

# ── Free-tier Agent Builder injection ──────────────────────────────────────
# After every paid (T_BUILDER) block, append a parallel free-tier (T_BUILDER_FREE)
# block whose knowledge is PUBLIC URLs only (regulator microsites, association
# pages, statistics offices). Free Copilot Chat cannot resolve enterprise file
# paths, so this gives demoers an authentic "build the same kind of agent on
# the free tier" path with unique, industry-specific public sources.
try:
    from _builder_free_catalog import render_agents_free, render_agents_free_id
    def _inject_builder_free(entries):
        n = 0
        for e in entries:
            if not isinstance(e, dict):
                continue
            eid = e.get('id') or ''
            ename = e.get('name') or eid
            prompts_arr = e.get('prompts') or []
            # Skip if already injected
            if any((t.get('tool') == T_BUILDER_FREE) for t in prompts_arr if isinstance(t, dict)):
                continue
            # Find paid builder block index — anchor the free block right after it.
            paid_idx = -1
            for i, t in enumerate(prompts_arr):
                if isinstance(t, dict) and t.get('tool') == T_BUILDER and t.get('isBuilder3'):
                    paid_idx = i
                    break
            if paid_idx < 0:
                continue
            agents_en = render_agents_free(eid, ename) or []
            agents_id = render_agents_free_id(eid, ename) or []
            free_block = tool_builder_free(
                FREE_ACCT,
                agents_en,
                desc=DESC_BUILDER_FREE,
                agentsID=agents_id,
                agentsBM=agents_id,  # BM falls back to ID phrasing (Bahasa overlap)
            )
            new_arr = list(prompts_arr)
            new_arr.insert(paid_idx + 1, free_block)
            e['prompts'] = new_arr
            n += 1
        return n
    _bf_added = _inject_builder_free(all_industries) + _inject_builder_free(all_departments)
    print(f"Free-tier Agent Builder injected on {_bf_added} entries")
except Exception as _e:
    print(f"(Free-tier Agent Builder injection skipped due to error: {_e})")

# ── Cowork Library: attach per-entry catalog of 4-5 unique Cowork use cases ──
# Source: _cowork_library.py (combines parts 2-5). Card schema includes title,
# dept_tag, industry_tag, complexity, apps, desc, skills, instructions,
# sample_files, prompts (P1/P2), expected, watch, honest, tips. Renderer in
# gen_hub.py turns each card into an expandable cw-card with WHAT TO WATCH /
# HONEST FRAMING callouts.
try:
    from _cowork_library import get_library_for_entry as _get_cwlib
    def _inject_cwlib(entries):
        n = 0
        for e in entries:
            if not isinstance(e, dict):
                continue
            eid = e.get('id') or ''
            cards = _get_cwlib(eid)
            if cards:
                e['coworkLibrary'] = cards
                n += 1
        return n
    _cwlib_added = _inject_cwlib(all_industries) + _inject_cwlib(all_departments)
    print(f"Cowork Library attached to {_cwlib_added} entries")
except Exception as _e:
    print(f"(Cowork Library injection skipped due to error: {_e})")

# ── Notebook Library injection: attach a per-entry notebookLibrary[] of
# 2-3 unique Copilot Notebook use-case cards (different archetypes per
# industry / department) so the audience sees concrete bespoke scenarios,
# not just the standardised 12-prompt demo guide flow.
try:
    from _notebook_library import get_nb_library_for_entry as _get_nblib
    def _inject_nblib(entries):
        n = 0
        for e in entries:
            if not isinstance(e, dict):
                continue
            eid = e.get('id') or ''
            ename = e.get('name') or e.get('label') or ''
            personas = e.get('personas') or []
            pname = ''
            if personas and isinstance(personas[0], dict):
                pname = personas[0].get('name') or ''
            cards = _get_nblib(eid, entry_name=ename, persona_name=pname)
            if cards:
                e['notebookLibrary'] = cards
                n += 1
        return n
    _nblib_added = _inject_nblib(all_industries) + _inject_nblib(all_departments)
    print(f"Notebook Library attached to {_nblib_added} entries")
except Exception as _e:
    print(f"(Notebook Library injection skipped due to error: {_e})")

# ── Scout Library injection ──────────────────────────────────────────────
try:
    from _scout_library import get_scout_library_for_entry as _get_scoutlib
    def _inject_scoutlib(entries):
        n = 0
        for e in entries:
            if not isinstance(e, dict):
                continue
            eid = e.get('id') or ''
            ename = e.get('name') or e.get('label') or ''
            personas = e.get('personas') or []
            pname = ''
            if personas and isinstance(personas[0], dict):
                pname = personas[0].get('name') or ''
            cards = _get_scoutlib(eid, entry_name=ename, persona_name=pname)
            if cards:
                e['scoutLibrary'] = cards
                n += 1
        return n
    _sclib_added = _inject_scoutlib(all_industries) + _inject_scoutlib(all_departments)
    print(f"Scout Library attached to {_sclib_added} entries")
except Exception as _e:
    print(f"(Scout Library injection skipped due to error: {_e})")

# ── SharePoint AI Library injection ──────────────────────────────────────
try:
    from _sharepoint_library import get_sp_library_for_entry as _get_splib
    def _inject_splib(entries):
        n = 0
        for e in entries:
            if not isinstance(e, dict):
                continue
            eid = e.get('id') or ''
            ename = e.get('name') or e.get('label') or ''
            personas = e.get('personas') or []
            pname = ''
            if personas and isinstance(personas[0], dict):
                pname = personas[0].get('name') or ''
            cards = _get_splib(eid, entry_name=ename, persona_name=pname)
            if cards:
                e['sharepointLibrary'] = cards
                n += 1
        return n
    _splib_added = _inject_splib(all_industries) + _inject_splib(all_departments)
    print(f"SharePoint AI Library attached to {_splib_added} entries")
except Exception as _e:
    print(f"(SharePoint AI Library injection skipped due to error: {_e})")

# ── Scout + SharePoint AI prompt-block injection ─────────────────────────
# Surface the per-entry scoutLibrary / sharepointLibrary cards inside the main
# detail-view prompts list, between the existing Notebook and Chat blocks. Each
# library card already has industry/department-tailored instructions, prompts,
# sample_files and personas, so we reformat one tool() block per entry from
# those cards (no new content authoring). Idempotent: skips if T_SCOUT or
# T_SHAREPOINT block already exists for that entry.
try:
    from util import T_SCOUT, T_SHAREPOINT, T_NOTEBOOK, T_CHAT, M365_LIC, M365_ACCT, DESC_SCOUT, DESC_SHAREPOINT, tool

    def _card_to_prompt_entries(cards, kind):
        """Convert library cards to {instr, prompt} entries. kind='scout'|'sp'."""
        out = []
        for c in (cards or []):
            if not isinstance(c, dict):
                continue
            title = c.get('title') or ''
            instructions = c.get('instructions') or []
            sample_files = c.get('sample_files') or []
            prompts = c.get('prompts') or []
            if not prompts:
                continue
            instr_lines = []
            if title:
                instr_lines.append(f"**Use case:** {title}")
            if kind == 'scout':
                instr_lines.append("**(1) Open Microsoft Scout** desktop app (Frontier preview).")
            else:
                instr_lines.append("**(1) Open SharePoint** → navigate to the relevant site or library.")
            for j, step in enumerate(instructions, start=2):
                instr_lines.append(f"**({j})** {step}")
            if sample_files:
                fnames = ", ".join(f if isinstance(f, str) else (f[0] if isinstance(f, (list, tuple)) and f else '') for f in sample_files)
                if fnames:
                    instr_lines.append(f"**Reference files:** {fnames}")
            instr_text = " ".join(instr_lines)
            for p in prompts:
                if not isinstance(p, dict):
                    continue
                ptext = p.get('text') or ''
                if not ptext:
                    continue
                lbl = p.get('label')
                this_instr = instr_text if not out else (f"**Same Scout session.** {lbl}" if (kind == 'scout' and lbl) else (f"**Same SharePoint flow.** {lbl}" if lbl else ("**Stay in Scout.**" if kind == 'scout' else "**Stay in SharePoint.**")))
                out.append({'instr': this_instr, 'prompt': ptext})
        return out

    def _entry_persona(e):
        personas = e.get('personas') or []
        if personas and isinstance(personas[0], dict):
            return personas[0].get('name') or 'Hadar Caspit'
        return 'Hadar Caspit'

    def _inject_scout_prompts(entries):
        n = 0
        for e in entries:
            if not isinstance(e, dict):
                continue
            cards = e.get('scoutLibrary') or []
            if not cards:
                continue
            prompts_arr = e.get('prompts') or []
            if any(isinstance(t, dict) and t.get('tool') == T_SCOUT for t in prompts_arr):
                continue
            entries_list = _card_to_prompt_entries(cards, 'scout')
            if not entries_list:
                continue
            persona_name = _entry_persona(e)
            block = tool(
                T_SCOUT, M365_LIC, M365_ACCT,
                entries_list,
                desc=DESC_SCOUT,
                promptsID=entries_list,
                promptsBM=entries_list,
                persona=[persona_name] * len(entries_list),
                personaID=[persona_name] * len(entries_list),
            )
            # Insert after T_NOTEBOOK if present, else before T_CHAT, else at end.
            insert_at = len(prompts_arr)
            for i, t in enumerate(prompts_arr):
                if isinstance(t, dict) and t.get('tool') == T_NOTEBOOK:
                    insert_at = i + 1
                    break
            else:
                for i, t in enumerate(prompts_arr):
                    if isinstance(t, dict) and t.get('tool') == T_CHAT:
                        insert_at = i
                        break
            new_arr = list(prompts_arr)
            new_arr.insert(insert_at, block)
            e['prompts'] = new_arr
            n += 1
        return n

    def _inject_sharepoint_prompts(entries):
        n = 0
        for e in entries:
            if not isinstance(e, dict):
                continue
            cards = e.get('sharepointLibrary') or []
            if not cards:
                continue
            prompts_arr = e.get('prompts') or []
            if any(isinstance(t, dict) and t.get('tool') == T_SHAREPOINT for t in prompts_arr):
                continue
            entries_list = _card_to_prompt_entries(cards, 'sp')
            if not entries_list:
                continue
            persona_name = _entry_persona(e)
            block = tool(
                T_SHAREPOINT, M365_LIC, M365_ACCT,
                entries_list,
                desc=DESC_SHAREPOINT,
                promptsID=entries_list,
                promptsBM=entries_list,
                persona=[persona_name] * len(entries_list),
                personaID=[persona_name] * len(entries_list),
            )
            # Insert after T_SCOUT if present (so order is Notebook → Scout → SP),
            # else after T_NOTEBOOK, else before T_CHAT, else at end.
            insert_at = len(prompts_arr)
            anchor_found = False
            for i, t in enumerate(prompts_arr):
                if isinstance(t, dict) and t.get('tool') == T_SCOUT:
                    insert_at = i + 1
                    anchor_found = True
                    break
            if not anchor_found:
                for i, t in enumerate(prompts_arr):
                    if isinstance(t, dict) and t.get('tool') == T_NOTEBOOK:
                        insert_at = i + 1
                        anchor_found = True
                        break
            if not anchor_found:
                for i, t in enumerate(prompts_arr):
                    if isinstance(t, dict) and t.get('tool') == T_CHAT:
                        insert_at = i
                        break
            new_arr = list(prompts_arr)
            new_arr.insert(insert_at, block)
            e['prompts'] = new_arr
            n += 1
        return n

    _scp_added = _inject_scout_prompts(all_industries) + _inject_scout_prompts(all_departments)
    _spp_added = _inject_sharepoint_prompts(all_industries) + _inject_sharepoint_prompts(all_departments)
    print(f"Scout prompt block injected on {_scp_added} entries")
    print(f"SharePoint AI prompt block injected on {_spp_added} entries")
except Exception as _e:
    import traceback as _tb
    print(f"(Scout / SharePoint AI prompt injection skipped due to error: {_e})")

# ── Wire Scout/SP sample_files into entry.files (so they appear in the
#    📁 Reference Files panel and get bundled into entry-<id>.zip) ─────────
try:
    def _merge_sample_files(entries):
        n = 0
        for e in entries:
            if not isinstance(e, dict):
                continue
            files = list(e.get('files') or [])
            existing = set(files)
            added = 0
            for libkey in ('scoutLibrary', 'sharepointLibrary'):
                for c in (e.get(libkey) or []):
                    if not isinstance(c, dict):
                        continue
                    for sf in (c.get('sample_files') or []):
                        fname = sf if isinstance(sf, str) else (sf[0] if isinstance(sf, (list, tuple)) and sf else '')
                        if fname and fname not in existing:
                            files.append(fname)
                            existing.add(fname)
                            added += 1
            if added:
                e['files'] = files
                n += 1
        return n
    _sf_added = _merge_sample_files(all_industries) + _merge_sample_files(all_departments)
    print(f"Scout/SP sample_files merged into entry.files on {_sf_added} entries")
except Exception as _e:
    print(f"(sample_files merge skipped due to error: {_e})")

# ── Copilot Create prompt-block injection ────────────────────────────────
# User asked for a few Copilot Create prompts under each industry/department's
# Chat tab — covering image, poster, infographic, video. Tailored to the
# entry name and sector. Lives in m365.cloud.microsoft > Create. M365 Copilot
# license. Folded into the Chat tab via the _isChatTab classifier in gen_hub.
try:
    from util import T_CREATE, DESC_CREATE, T_CHAT, M365_LIC, M365_ACCT, tool

    def _create_prompts_for_entry(e):
        """Return 4 instr/prompt entries (image, poster, infographic, video)."""
        ename = (e.get('name') or e.get('label') or 'Zava Conglomerate').strip()
        sector = (e.get('sector') or e.get('subSector') or '').strip()
        scope = ename + (f" ({sector})" if sector else '')
        out = []
        # 1. Image — hero/banner
        out.append({
            'instr': "**Open the Microsoft 365 Copilot app** \u2192 left nav > **Create** > **Image**. "
                     "Pick **landscape 16:9**. Choose model **Flux** or **GPT-Image** (try both). "
                     f"Give Copilot a reference image of the Zava brand mark (optional) for style consistency. Iterate by referring to the previous image (\u201cSame style, change the foreground to \u2026\u201d).",
            'prompt': f"Create a clean, modern hero banner image for **{scope}** at Zava Conglomerate. "
                      f"Show a confident professional team in a {sector or 'corporate'} setting (Southeast Asia context \u2014 Kuala Lumpur or Jakarta skyline blurred behind), wearing smart business attire. "
                      "Lighting: warm morning sun. Mood: trustworthy, forward-looking. "
                      "Brand palette: deep navy + amber accents. No text on the image, no logos, no real public figures. "
                      "Composition: rule of thirds, plenty of negative space on the right for headline overlay. 16:9 widescreen."
        })
        # 2. Poster — event / awareness
        out.append({
            'instr': "**Open Copilot \u2192 Create \u2192 Poster**. Choose layout **Focal** (one big visual + headline). "
                     f"Set the brand kit to Zava Conglomerate (navy #0F172A + amber #F59E0B). Output: PNG A3 portrait. "
                     "Iterate the headline with Copilot before exporting.",
            'prompt': f"Design an internal awareness poster for **{scope}** at Zava Conglomerate. "
                      "Headline: \u201cReady. Resilient. Responsible.\u201d Body: a 2-line teaser explaining the initiative in plain language for all employees across our Bank, Plantations, Energy, Pharma, and Consumer divisions. "
                      "Include a clear call-to-action (\u201cJoin the briefing on Friday 3pm \u2014 Teams link in your inbox\u201d). "
                      "Visual: abstract gradient (navy \u2192 teal) with a subtle grid texture and one bold icon related to the topic. A3 portrait. Brand-kit colours only."
        })
        # 3. Infographic — data viz
        out.append({
            'instr': "**Open Copilot \u2192 Create \u2192 Infographic**. Pick layout **Vertical \u2014 5 sections**. "
                     "Paste the data points below into the brief. Refine each section heading with Copilot before export. PNG long-portrait.",
            'prompt': f"Create a one-page infographic summarising the **FY2026 outlook for {scope}**. "
                      "Five vertical sections: (1) Headline KPI \u2014 1 big number with caption; (2) 3 strategic priorities for the year (icons + 1-line caption each); "
                      "(3) Risk heat-map \u2014 5 risks rated low/med/high with colour dots; (4) Targets vs FY2025 actuals \u2014 simple bar comparison; "
                      "(5) Next milestones \u2014 timeline with 4 dated checkpoints. Brand: Zava navy + amber. Footer: \u201cZava Conglomerate \u2022 Confidential \u2022 Internal use only\u201d."
        })
        # 4. Video — short comms clip
        out.append({
            'instr': "**Open Copilot \u2192 Create \u2192 Video**. Length **30 seconds**. Voiceover: **English (US)** "
                     "(or set to **Bahasa Malaysia / Bahasa Indonesia** if your audience is local). "
                     "Background music: **Corporate \u2014 Optimistic**. Aspect ratio: **16:9** for Teams Town Hall, or **9:16** for Viva Engage / mobile. "
                     "Iterate the script with Copilot before generating; review every clip in preview before export.",
            'prompt': f"Generate a 30-second internal comms video introducing **{scope}** at Zava Conglomerate. "
                      "Structure: (0\u20135s) cold open with the headline question; (5\u201320s) three quick scenes \u2014 office in KL, plantation in Sabah, energy plant in Pengerang \u2014 each 4\u20135 seconds with a one-line caption; "
                      "(20\u201325s) the leader (no real person \u2014 generic professional avatar) delivers the call-to-action; (25\u201330s) closing card with Zava logo placeholder + URL placeholder. "
                      "Voiceover tone: warm, confident, conversational. End with \u201cTogether, that\u2019s how Zava grows.\u201d Captions on screen for accessibility."
        })
        return out

    def _inject_create_prompts(entries):
        n = 0
        for e in entries:
            if not isinstance(e, dict):
                continue
            prompts_arr = e.get('prompts') or []
            if any(isinstance(t, dict) and t.get('tool') == T_CREATE for t in prompts_arr):
                continue
            entries_list = _create_prompts_for_entry(e)
            if not entries_list:
                continue
            persona_name = (lambda: ((e.get('personas') or [{}])[0].get('name') if (e.get('personas') and isinstance(e.get('personas')[0], dict)) else 'Sasha Ouellet'))() or 'Sasha Ouellet'
            block = tool(
                T_CREATE, M365_LIC, M365_ACCT,
                entries_list,
                desc=DESC_CREATE,
                promptsID=entries_list,
                promptsBM=entries_list,
                persona=[persona_name] * len(entries_list),
                personaID=[persona_name] * len(entries_list),
            )
            # Insert immediately AFTER the T_CHAT block (so it sits on the Chat
            # detail tab just below the chat prompts). If no T_CHAT, append.
            insert_at = len(prompts_arr)
            for i, t in enumerate(prompts_arr):
                if isinstance(t, dict) and t.get('tool') == T_CHAT:
                    insert_at = i + 1
                    break
            new_arr = list(prompts_arr)
            new_arr.insert(insert_at, block)
            e['prompts'] = new_arr
            n += 1
        return n

    _cr_added = _inject_create_prompts(all_industries) + _inject_create_prompts(all_departments)
    print(f"Copilot Create prompt block injected on {_cr_added} entries")
except Exception as _e:
    import traceback as _tb
    print(f"(Copilot Create prompt injection skipped due to error: {_e})")
    _tb.print_exc()

lines = ['window.HUB_DATA = {']
lines.append('  whatsNew: ' + js_val(WHATS_NEW, 1) + ',')
lines.append('  sectors: ' + js_val(SECTORS, 1) + ',')
lines.append('  industries: ' + js_val(all_industries, 1) + ',')
lines.append('  departments: ' + js_val(all_departments, 1))
lines.append('};')

output = '\n'.join(lines)

with open('data.js', 'w', encoding='utf-8', errors='replace') as f:
    f.write(output)

import os
size = os.path.getsize('data.js')
print(f"data.js written: {size:,} bytes ({size//1024} KB)")
