
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
        "title": "📈 Excel \u2014 Plan mode + Python",
        "badge": "May 2026 rollout",
        "summary": "Plan mode lets Copilot in Excel outline a step-by-step approach BEFORE making any change \u2014 review and adjust before edits land. Python in Excel runs advanced data techniques (forecasts, regressions, custom visualisations) directly inside the Edit-with-Copilot flow without leaving the workbook.",
        "tip": "In Excel for the Web > Copilot pane, click the menu above the prompt box and pick 'Plan'. Or simply add 'use Python' to your prompt to invoke Python automatically.",
        "license": "M365_LIC",
        "link": "https://techcommunity.microsoft.com/blog/microsoft365copilotblog/what%E2%80%99s-new-in-microsoft-365-copilot--april-2026/4510935"
    },
    {
        "id": "wn-ppt-web-images",
        "title": "🌐 PowerPoint \u2014 web grounding + image picker",
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
        "title": "📞 Teams \u2014 Call Delegation + Interpretation",
        "badge": "April-May 2026",
        "summary": "Copilot Call Delegation: Copilot answers incoming Teams calls on the user\u2019s behalf, gathers context from the caller, and books follow-ups via Microsoft Bookings. Consecutive Interpretation: turn-based translation between two languages with Interpreter on the meeting stage \u2014 ideal for ASEAN cross-border meetings.",
        "tip": "Teams > Settings > Calls > enable Copilot Call Delegation. For meetings, Interpreter on stage supports both real-time simultaneous and turn-based consecutive interpretation.",
        "license": "M365_LIC",
        "link": "https://techcommunity.microsoft.com/blog/microsoft365copilotblog/what%E2%80%99s-new-in-microsoft-365-copilot--april-2026/4510935"
    },
    {
        "id": "wn-notebook-mindmap",
        "title": "🧠 Notebook \u2014 Mind Maps + PPT/Word generation",
        "badge": "May 2026 (Frontier preview)",
        "summary": "Copilot Notebook can now generate full Word documents and PowerPoint decks directly from notebook content. Mind Maps give an interactive grounded view of relationships across all sources \u2014 click a node to drill in. SharePoint sites, OneNote notebooks, and external web URLs all qualify as sources.",
        "tip": "After grounding the notebook, click Quick Create > Mind Map for an executive overview, or > Word document / PowerPoint presentation to draft a deliverable preloaded with visuals.",
        "license": "M365_LIC",
        "link": "https://techcommunity.microsoft.com/blog/microsoft365copilotblog/what%E2%80%99s-new-in-microsoft-365-copilot--april-2026/4510935"
    },
    {
        "id": "wn-agent-store",
        "title": "🏪 Agent Builder \u2014 submit to Agent Store",
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

# ── Notebook Demo Guide: prepend canonical /00_Copilot_Notebook_Demo_Guide.docx ──
# User feedback: "do not have generic copilot notebook... make sure you put instructions
# like this: [📝 00_Copilot_Notebook_Demo_Guide.docx] and also their sample prompts."
# We add a single canonical demo guide doc as the FIRST source on EVERY Notebook
# block across all 55 entries so presenters always have the run-sheet alongside
# the entry-specific data files.
_NB_GUIDE = '/00_Copilot_Notebook_Demo_Guide.docx'
def _prepend_nb_guide(entries):
    n = 0
    for e in entries:
        # Each entry has a `prompts` array of tool dicts (NOT 'sections')
        for tool in e.get('prompts') or []:
            if 'Copilot Notebook' not in (tool.get('tool') or ''):
                continue
            meta = tool.get('notebookMeta')
            if not meta:
                meta = {'sources': [], 'instructions': '', 'instructionsID': ''}
                tool['notebookMeta'] = meta
            srcs = list(meta.get('sources') or [])
            if _NB_GUIDE not in srcs:
                srcs.insert(0, _NB_GUIDE)
                meta['sources'] = srcs
                n += 1
        # Also surface the file in the entry-level files list
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
