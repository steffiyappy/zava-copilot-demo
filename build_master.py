
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
from dept_data  import DEPARTMENTS
from dept_data2 import DEPARTMENTS_2
from dept_data3 import DEPARTMENTS_3
from dept_data4 import DEPARTMENTS_4
from dept_data5 import DEPARTMENTS_5

all_industries = (INDUSTRIES_1 + INDUSTRIES_2 + INDUSTRIES_3 + INDUSTRIES_4 +
                  INDUSTRIES_5 + INDUSTRIES_6 + INDUSTRIES_7 + INDUSTRIES_8 +
                  INDUSTRIES_9 + INDUSTRIES_10 + INDUSTRIES_11 + INDUSTRIES_12)
all_departments = DEPARTMENTS + DEPARTMENTS_2 + DEPARTMENTS_3 + DEPARTMENTS_4 + DEPARTMENTS_5

print(f"Industries: {len(all_industries)}, Departments: {len(all_departments)}")

WHATS_NEW = [
    {
        "id": "wn-researcher",
        "title": "🔍 Researcher \u2014 Critique + Model Council",
        "badge": "New rollout (May 2026)",
        "summary": "Two demo modes inside Researcher: (1) Critique Mode self-critiques every source and flags claims it cannot verify; (2) Model Council convenes GPT and Claude each return a full independent report, then a synthesis cover letter highlights where they agree, where they differ, and any unique findings.",
        "tip": "m365.cloud.microsoft/chat > Agents > Researcher > switch the mode pill at the top to 'Critique' or 'Model Council'.",
        "license": "M365_LIC",
        "link": "https://techcommunity.microsoft.com/blog/microsoft365copilotblog/introducing-multi-model-intelligence-in-researcher/4506011"
    },
    {
        "id": "wn-cowork",
        "title": "🤝 Cowork (Frontier)",
        "badge": "Frontier Program",
        "summary": "ONE prompt that delegates 5 parallel tasks: draft a Word doc, draft a second Word doc, send an email, schedule a calendar meeting, post a Teams message \u2014 Cowork executes them all in parallel and reports back with a single status panel.",
        "tip": "m365.cloud.microsoft > left nav > Agents > Cowork. Requires Frontier program enrollment.",
        "license": "FRONTIER_LIC",
        "link": "https://techcommunity.microsoft.com/blog/microsoft365copilotblog/cowork-in-progress/4511672"
    },
    {
        "id": "wn-doc-agents",
        "title": "📝🎯📊 Word / PPT / Excel Agents \u2014 dual tier",
        "badge": "Free Chat tier + Microsoft 365 Copilot",
        "summary": "Type ONE prompt in m365.cloud.microsoft/chat and Copilot returns a fully drafted .docx / .pptx / .xlsx without you opening Word/PPT/Excel first. Now available in BOTH the free Copilot Chat tier (Sasha account) and with an Microsoft 365 Copilot license (MOD Admin account).",
        "tip": "Try in the free tier: 'Build a 5-slide investor narrative deck for the Zava FY2025 Q4 results...'",
        "license": "ANY_LIC",
        "link": "https://techcommunity.microsoft.com/blog/microsoft365copilotblog/copilot-in-word-new-capabilities-for-document-workflows/4508974"
    },
    {
        "id": "wn-builder",
        "title": "🏗 Agent Builder \u2014 dual tier",
        "badge": "Free Chat tier + Microsoft 365 Copilot",
        "summary": "Create custom agents inside Copilot Chat \u2014 NOT Copilot Studio. Describe \u2192 Configure (knowledge, instructions, starter prompts) \u2192 Test \u2192 Create + share. Now usable in both the free Copilot Chat tier and with an Microsoft 365 Copilot license.",
        "tip": "m365.cloud.microsoft/chat > Agents > + Create an agent. Try building a 'Group CFO Briefing Bot' grounded in your finance reference files.",
        "license": "ANY_LIC",
        "link": "https://techcommunity.microsoft.com/blog/microsoft365copilotblog/whats-new-in-microsoft-365-copilot--april-2026/4510935"
    },
    {
        "id": "wn-notebook",
        "title": "📓 Copilot Notebook \u2014 5 sources + Quick Create",
        "badge": "Generally Available",
        "summary": "Add up to 5 source files (Word/Excel/PDF/PPT) at notebook creation, set a persistent Instructions field, then run multiple prompts against the same notebook without re-uploading. Quick Create now produces Pages, Audio Overviews, and presentations from any notebook.",
        "tip": "m365.cloud.microsoft/chat > Notebook tab > + New Notebook. After grounding, click Quick Create > Audio Overview for a podcast-style executive summary.",
        "license": "M365_LIC",
        "link": "https://techcommunity.microsoft.com/blog/microsoft365copilotblog/whats-new-in-microsoft-365-copilot--april-2026/4510935"
    },
    {
        "id": "wn-federated",
        "title": "🔌 Federated Copilot Connectors",
        "badge": "May 2026 rollout",
        "summary": "Copilot can now query external systems-of-record from inside Chat: Moody's (credit ratings), HubSpot (CRM), LSEG (market data), Notion (knowledge base) and ServiceNow. Useful for IR/credit prompts that need real-time market or counterparty data.",
        "tip": "Try in Researcher: 'Pull LSEG 5-year CDS spreads for Zava Group's top-3 lender peers and Moody's latest rating action notes.'",
        "license": "M365_LIC",
        "link": "https://techcommunity.microsoft.com/blog/microsoft365copilotblog/federated-copilot-connectors---bringing-real-time-enterprise-data-within-microso/4515993"
    },
    {
        "id": "wn-word-legal",
        "title": "⚖️ Word Legal Agent (Frontier)",
        "badge": "Frontier Program",
        "summary": "Specialised Word agent for contract / litigation / compliance work \u2014 redlines clauses against a playbook, highlights deviations from precedent, and proposes alternate language grounded in the firm's contract corpus.",
        "tip": "Open a contract .docx in Word for the Web > Copilot pane > switch to 'Legal Agent'. Ask: 'Redline this MSA against our Tier-1 vendor playbook and flag any indemnity carve-outs.'",
        "license": "FRONTIER_LIC",
        "link": "https://techcommunity.microsoft.com/blog/microsoft365copilotblog/word-legal-agent-in-frontier/4516218"
    },
    {
        "id": "wn-models",
        "title": "🧠 Frontier Model Picker",
        "badge": "May 2026 rollout",
        "summary": "Switch the underlying frontier model for any chat or agent: GPT Instant, GPT and Claude, ChatGPT Images 2.0. Use Thinking models for board-grade reasoning; Instant for fast triage.",
        "tip": "In any Copilot Chat thread, click the model pill at the top \u2014 try 'GPT' for the Strategy/Risk briefs; 'Claude' for nuanced legal/policy drafting.",
        "license": "M365_LIC",
        "link": "https://techcommunity.microsoft.com/blog/microsoft365copilotblog/available-today-anthropic-claude-opus-4-7-in-microsoft-365-copilot/4511666"
    },
    {
        "id": "wn-excel-plan-python",
        "title": "\ud83d\udcc8 Excel \u2014 Plan mode + Python",
        "badge": "May 2026 rollout",
        "summary": "Plan mode lets Copilot in Excel outline a step-by-step approach BEFORE making any change \u2014 review and adjust before edits land. Python in Excel runs advanced data techniques (forecasts, regressions, custom visualisations) directly inside the Edit-with-Copilot flow without leaving the workbook.",
        "tip": "In Excel for the Web > Copilot pane, click the menu above the prompt box and pick 'Plan'. Or simply add 'use Python' to your prompt to invoke Python automatically.",
        "license": "M365_LIC",
        "link": "https://techcommunity.microsoft.com/blog/microsoft365copilotblog/what%E2%80%99s-new-in-microsoft-365-copilot--april-2026/4510935"
    },
    {
        "id": "wn-ppt-web-images",
        "title": "\ud83c\udf10 PowerPoint \u2014 web grounding + image picker",
        "badge": "April 2026",
        "summary": "Add a public webpage URL as a deck reference and Copilot pulls in current external context to build the outline. Choose the image model (GPT-Image, Flux, or Auto) when generating or editing visuals \u2014 align with quality, style, and governance expectations.",
        "tip": "In PPT for the Web > Copilot pane > add a web reference URL (e.g. a Bursa Malaysia listing or BNM circular page). When generating an image, click the gear and pick the model.",
        "license": "M365_LIC",
        "link": "https://techcommunity.microsoft.com/blog/microsoft365copilotblog/what%E2%80%99s-new-in-microsoft-365-copilot--april-2026/4510935"
    },
    {
        "id": "wn-outlook-canvas",
        "title": "\u270d\ufe0f Outlook \u2014 first draft in canvas",
        "badge": "March 2026 (new Outlook)",
        "summary": "Copilot now writes the email directly in place and asks clarifying questions about goal, audience, and tone, then iterates with the user in the same canvas. No copy-paste, no formatting surprises \u2014 every change is visible in Outlook as the message is refined.",
        "tip": "In new Outlook on the Web, open Compose > Copilot. After the first draft lands, answer Copilot\u2019s clarifying questions and watch the email update in place.",
        "license": "M365_LIC",
        "link": "https://techcommunity.microsoft.com/blog/microsoft365copilotblog/what%E2%80%99s-new-in-microsoft-365-copilot--april-2026/4510935"
    },
    {
        "id": "wn-teams-call-interpret",
        "title": "\ud83d\udcde Teams \u2014 Call Delegation + Interpretation",
        "badge": "April-May 2026",
        "summary": "Copilot Call Delegation: Copilot answers incoming Teams calls on the user\u2019s behalf, gathers context from the caller, and books follow-ups via Microsoft Bookings. Consecutive Interpretation: turn-based translation between two languages with Interpreter on the meeting stage \u2014 ideal for ASEAN cross-border meetings.",
        "tip": "Teams > Settings > Calls > enable Copilot Call Delegation. For meetings, Interpreter on stage supports both real-time simultaneous and turn-based consecutive interpretation.",
        "license": "M365_LIC",
        "link": "https://techcommunity.microsoft.com/blog/microsoft365copilotblog/what%E2%80%99s-new-in-microsoft-365-copilot--april-2026/4510935"
    },
    {
        "id": "wn-notebook-mindmap",
        "title": "\ud83e\udde0 Notebook \u2014 Mind Maps + PPT/Word generation",
        "badge": "May 2026 (Frontier preview)",
        "summary": "Copilot Notebook can now generate full Word documents and PowerPoint decks directly from notebook content. Mind Maps give an interactive grounded view of relationships across all sources \u2014 click a node to drill in. SharePoint sites, OneNote notebooks, and external web URLs all qualify as sources.",
        "tip": "After grounding the notebook, click Quick Create > Mind Map for an executive overview, or > Word document / PowerPoint presentation to draft a deliverable preloaded with visuals.",
        "license": "M365_LIC",
        "link": "https://techcommunity.microsoft.com/blog/microsoft365copilotblog/what%E2%80%99s-new-in-microsoft-365-copilot--april-2026/4510935"
    },
    {
        "id": "wn-agent-store",
        "title": "\ud83c\udfea Agent Builder \u2014 submit to Agent Store",
        "badge": "May 2026 rollout",
        "summary": "Agent Builder now supports submitting agents for admin review and approval. Approved agents land in the \u201cBuilt by your org\u201d section of the Agent Store where the whole organisation can discover and install them \u2014 the right balance of citizen-developer scale and IT admin control.",
        "tip": "After Test, click Submit for review (next to Create + share). Once your IT admin approves, the agent appears in the org\u2019s Agent Store automatically.",
        "license": "M365_LIC",
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
    if isinstance(v, list):
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
