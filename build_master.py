
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
from dept_data  import DEPARTMENTS
from dept_data2 import DEPARTMENTS_2
from dept_data3 import DEPARTMENTS_3
from dept_data4 import DEPARTMENTS_4

all_industries = (INDUSTRIES_1 + INDUSTRIES_2 + INDUSTRIES_3 + INDUSTRIES_4 +
                  INDUSTRIES_5 + INDUSTRIES_6 + INDUSTRIES_7 + INDUSTRIES_8 + INDUSTRIES_9)
all_departments = DEPARTMENTS + DEPARTMENTS_2 + DEPARTMENTS_3 + DEPARTMENTS_4

print(f"Industries: {len(all_industries)}, Departments: {len(all_departments)}")

WHATS_NEW = [
    {
        "id": "wn-researcher",
        "title": "🔍 Researcher",
        "badge": "New in M365 Copilot",
        "summary": "Deep web + work graph synthesis. Ask Copilot to research any topic — competitors, regulations, market trends — and it grounds its answer in live web data and your org files.",
        "tip": "Try: 'Research the top 5 ESG regulations impacting ASEAN palm oil exporters in 2025.'",
        "license": "M365_LIC"
    },
    {
        "id": "wn-analyst",
        "title": "📊 Analyst",
        "badge": "New in M365 Copilot",
        "summary": "Upload Excel/CSV files and Copilot runs Python code to generate charts, regressions, waterfall analysis, and scenario models — right in your browser.",
        "tip": "Try: Upload any Zava Excel file and ask 'Create a waterfall chart showing EBITDA bridge by division.'",
        "license": "M365_LIC"
    },
    {
        "id": "wn-cowork",
        "title": "🤝 Cowork (Frontier)",
        "badge": "Frontier Program",
        "summary": "Autonomous multi-step agent at m365.cloud.microsoft > Agents > Cowork. Cowork can search the web, draft documents, send emails (with your confirmation), and manage calendars — end-to-end workflows.",
        "tip": "Start Cowork at m365.cloud.microsoft, click Agents, then Cowork. Requires Frontier program enrollment.",
        "license": "FRONTIER_LIC"
    },
    {
        "id": "wn-notebook",
        "title": "📓 Copilot Notebook",
        "badge": "Available Now",
        "summary": "Multi-document synthesis hub. Paste or upload multiple documents, set a persistent Instruction, then ask questions across all of them — perfect for M&A due diligence, policy review, and report compilation.",
        "tip": "Try: Upload all 4 M&A target files + the evaluation framework, then ask Copilot to rank targets.",
        "license": "M365_LIC"
    },
    {
        "id": "wn-agents",
        "title": "🏗 Agent Builder",
        "badge": "Copilot Studio",
        "summary": "Build custom Copilot agents trained on your own documents and policies — no code required. Deploy to Teams, SharePoint, or as a standalone chat agent for your employees.",
        "tip": "Go to copilotstudio.microsoft.com > Create > New Agent. Upload your policy documents and publish to Teams.",
        "license": "M365_LIC"
    }
]

SECTORS = [
    {"id": "sec-general",    "label": "⭐ Start Here",     "industries": ["general"]},
    {"id": "sec-banking",    "label": "Banking",           "industries": ["commercial-banking","islamic-banking","investment-banking"]},
    {"id": "sec-insurance",  "label": "Insurance",         "industries": ["general-insurance","life-insurance","takaful"]},
    {"id": "sec-fintech",    "label": "Fintech",           "industries": ["fintech-payments"]},
    {"id": "sec-healthcare", "label": "Healthcare",        "industries": ["hospital-network","pharmaceutical"]},
    {"id": "sec-og",         "label": "Oil & Gas",         "industries": ["og-upstream","og-downstream"]},
    {"id": "sec-energy",     "label": "Energy",            "industries": ["renewable-energy"]},
    {"id": "sec-mfg",        "label": "Manufacturing",     "industries": ["industrial-manufacturing","construction"]},
    {"id": "sec-agri",       "label": "Agriculture",       "industries": ["plantation"]},
    {"id": "sec-bpo",        "label": "BPO & Tech",        "industries": ["bpo-services"]},
    {"id": "sec-telco",      "label": "Telco",             "industries": ["telco"]},
    {"id": "sec-congl",      "label": "Conglomerate",      "industries": ["diversified-conglomerate"]},
    {"id": "sec-govt",       "label": "Government",        "industries": ["government-agency","financial-regulator"]},
    {"id": "sec-glc",        "label": "GLC",               "industries": ["glc-investment"]},
    {"id": "sec-re",         "label": "Real Estate",       "industries": ["property-reit"]},
    {"id": "sec-logistics",  "label": "Logistics",         "industries": ["logistics-3pl"]},
    {"id": "sec-aviation",   "label": "Aviation",          "industries": ["aviation-airports"]},
    {"id": "sec-mining",     "label": "Mining",            "industries": ["coal-mining"]},
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
