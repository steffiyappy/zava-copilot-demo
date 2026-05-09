
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
from dept_data  import DEPARTMENTS
from dept_data2 import DEPARTMENTS_2
from dept_data3 import DEPARTMENTS_3
from dept_data4 import DEPARTMENTS_4

all_industries = (INDUSTRIES_1 + INDUSTRIES_2 + INDUSTRIES_3 + INDUSTRIES_4 +
                  INDUSTRIES_5 + INDUSTRIES_6 + INDUSTRIES_7 + INDUSTRIES_8 +
                  INDUSTRIES_9 + INDUSTRIES_10)
all_departments = DEPARTMENTS + DEPARTMENTS_2 + DEPARTMENTS_3 + DEPARTMENTS_4

print(f"Industries: {len(all_industries)}, Departments: {len(all_departments)}")

WHATS_NEW = [
    {
        "id": "wn-researcher",
        "title": "🔍 Researcher \u2014 Critique + Model Council",
        "badge": "New rollout (May 2026)",
        "summary": "Two demo modes inside Researcher: (1) Critique Mode self-critiques every source and flags claims it cannot verify; (2) Model Council convenes GPT-5.5 Thinking + Claude Opus 4.7 + Claude Sonnet 4.7 each return a full independent report, then a synthesis cover letter highlights where they agree, where they differ, and any unique findings.",
        "tip": "m365.cloud.microsoft/chat > Agents > Researcher > switch the mode pill at the top to 'Critique' or 'Model Council'.",
        "license": "M365_LIC"
    },
    {
        "id": "wn-cowork",
        "title": "🤝 Cowork (Frontier)",
        "badge": "Frontier Program",
        "summary": "ONE prompt that delegates 5 parallel tasks: draft a Word doc, draft a second Word doc, send an email, schedule a calendar meeting, post a Teams message \u2014 Cowork executes them all in parallel and reports back with a single status panel.",
        "tip": "m365.cloud.microsoft > left nav > Agents > Cowork. Requires Frontier program enrollment.",
        "license": "FRONTIER_LIC"
    },
    {
        "id": "wn-doc-agents",
        "title": "📝🎯📊 Word / PPT / Excel Agents \u2014 dual tier",
        "badge": "Free Chat tier + M365 Copilot",
        "summary": "Type ONE prompt in m365.cloud.microsoft/chat and Copilot returns a fully drafted .docx / .pptx / .xlsx without you opening Word/PPT/Excel first. Now available in BOTH the free Copilot Chat tier (Sasha account) and with an M365 Copilot license (MOD Admin account).",
        "tip": "Try in the free tier: 'Build a 5-slide investor narrative deck for the Zava FY2025 Q4 results...'",
        "license": "ANY_LIC"
    },
    {
        "id": "wn-builder",
        "title": "🏗 Agent Builder \u2014 dual tier",
        "badge": "Free Chat tier + M365 Copilot",
        "summary": "Create custom agents inside Copilot Chat \u2014 NOT Copilot Studio. Describe \u2192 Configure (knowledge, instructions, starter prompts) \u2192 Test \u2192 Create + share. Now usable in both the free Copilot Chat tier and with an M365 Copilot license.",
        "tip": "m365.cloud.microsoft/chat > Agents > + Create an agent. Try building a 'Group CFO Briefing Bot' grounded in your finance reference files.",
        "license": "ANY_LIC"
    },
    {
        "id": "wn-notebook",
        "title": "📓 Copilot Notebook \u2014 5 sources + Quick Create",
        "badge": "Generally Available",
        "summary": "Add up to 5 source files (Word/Excel/PDF/PPT) at notebook creation, set a persistent Instructions field, then run multiple prompts against the same notebook without re-uploading. Quick Create now produces Pages, Audio Overviews, and presentations from any notebook.",
        "tip": "m365.cloud.microsoft/chat > Notebook tab > + New Notebook. After grounding, click Quick Create > Audio Overview for a podcast-style executive summary.",
        "license": "M365_LIC"
    },
    {
        "id": "wn-federated",
        "title": "🔌 Federated Copilot Connectors",
        "badge": "May 2026 rollout",
        "summary": "Copilot can now query external systems-of-record from inside Chat: Moody's (credit ratings), HubSpot (CRM), LSEG (market data), Notion (knowledge base) and ServiceNow. Useful for IR/credit prompts that need real-time market or counterparty data.",
        "tip": "Try in Researcher: 'Pull LSEG 5-year CDS spreads for Zava Group's top-3 lender peers and Moody's latest rating action notes.'",
        "license": "M365_LIC"
    },
    {
        "id": "wn-word-legal",
        "title": "⚖️ Word Legal Agent (Frontier)",
        "badge": "Frontier Program",
        "summary": "Specialised Word agent for contract / litigation / compliance work \u2014 redlines clauses against a playbook, highlights deviations from precedent, and proposes alternate language grounded in the firm's contract corpus.",
        "tip": "Open a contract .docx in Word for the Web > Copilot pane > switch to 'Legal Agent'. Ask: 'Redline this MSA against our Tier-1 vendor playbook and flag any indemnity carve-outs.'",
        "license": "FRONTIER_LIC"
    },
    {
        "id": "wn-models",
        "title": "🧠 Frontier Model Picker",
        "badge": "May 2026 rollout",
        "summary": "Switch the underlying frontier model for any chat or agent: GPT-5.5 Instant, GPT-5.5 Thinking, Claude Opus 4.7, Claude Sonnet 4.7, ChatGPT Images 2.0. Use Thinking models for board-grade reasoning; Instant for fast triage.",
        "tip": "In any Copilot Chat thread, click the model pill at the top \u2014 try 'GPT-5.5 Thinking' for the Strategy/Risk briefs; 'Claude Opus 4.7' for nuanced legal/policy drafting.",
        "license": "M365_LIC"
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
    {"id": "sec-mfg",        "label": "Manufacturing",     "industries": ["industrial-manufacturing","rubber-gloves","semiconductor","auto-tyres","construction"]},
    {"id": "sec-food",       "label": "Food & FMCG",       "industries": ["food-fmcg"]},
    {"id": "sec-agri",       "label": "Agriculture",       "industries": ["plantation"]},
    {"id": "sec-bpo",        "label": "BPO & Tech",        "industries": ["bpo-services"]},
    {"id": "sec-telco",      "label": "Telco",             "industries": ["telco"]},
    {"id": "sec-congl",      "label": "Conglomerate",      "industries": ["diversified-conglomerate"]},
    {"id": "sec-govt",       "label": "Government",        "industries": ["government-agency","financial-regulator"]},
    {"id": "sec-glc",        "label": "GLC",               "industries": ["glc-investment"]},
    {"id": "sec-re",         "label": "Real Estate",       "industries": ["property-reit"]},
    {"id": "sec-logistics",  "label": "Logistics",         "industries": ["logistics-3pl"]},
    {"id": "sec-aviation",   "label": "Aviation",          "industries": ["aviation-airports"]},
    {"id": "sec-mining",     "label": "Mining",            "industries": ["coal-mining","rare-earth"]},
    {"id": "sec-retail",     "label": "Retail",            "industries": ["retail-grocery"]},
    {"id": "sec-hospitality","label": "Hospitality",       "industries": ["hotel-resort"]},
    {"id": "sec-media",      "label": "Media",             "industries": ["media-entertainment"]},
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
