
FREE_ACCT = 'Sasha Ouellet \u2014 SashaO@ABSx62256373.OnMicrosoft.com'
M365_ACCT = 'MOD Administrator \u2014 admin@ABSx62256373.onmicrosoft.com'
FREE_LIC = 'Free \u2014 no M365 Copilot license needed'
M365_LIC = 'M365 Copilot'
FRONTIER_LIC = 'M365 Copilot + Frontier Program'

T_CHAT = '🤖 Copilot Chat (Basic)'
T_RESEARCHER = '🔍 Researcher'
T_ANALYST = '📊 Analyst'
T_EXCEL = '📊 Copilot in Excel'
T_WORD = '📝 Copilot in Word'
T_PPT = '🎯 Copilot in PowerPoint'
T_OUTLOOK = '📧 Copilot in Outlook'
T_TEAMS = '🎙 Copilot in Teams'
T_NOTEBOOK = '📓 Copilot Notebook'
T_COWORK = '🤝 Cowork (Frontier)'
T_EDIT_COPILOT = '✏️ Edit with Copilot'
T_WORD_AGT = '🤖 Word Agent'
T_PPT_AGT = '🤖 PowerPoint Agent'
T_XL_AGT = '🤖 Excel Agent'
T_BUILDER = '🏗 Agent Builder (Copilot Studio)'

DESC_RESEARCHER = 'Access via Microsoft 365 Copilot Chat > Agents > Researcher. Researcher automatically critiques every source — verifying claims against the original before including them in the report. Grounds answers in live web sources and your organisation\'s data with full citations. Faster and more reliable than manual research.'
DESC_EDIT_COPILOT = 'Edit with Copilot is an agentic mode in Word, Excel, and PowerPoint (web) that executes multi-step editing tasks across your entire document in one instruction — reformatting, restructuring, building formulas, generating new sections. Access: open any Office file in browser > Copilot pane > Edit with Copilot. Requires M365 Copilot licence.'
DESC_ANALYST = 'Access via Microsoft 365 Copilot Chat > click Agents > Analyst. Upload an Excel or CSV file. Analyst runs Python-style analysis, builds charts, and interprets results without you writing a single formula.'
DESC_TEAMS = 'Use your OWN existing recorded Teams meetings. Open a meeting recap in Teams > Recap tab. Copilot generates summaries, action items, and follow-up drafts grounded in the actual transcript.'
DESC_NOTEBOOK = 'Access via copilot.microsoft.com > Notebook tab. Upload up to 5 files and set a system instruction. Best for synthesising insights across multiple documents simultaneously.'
DESC_COWORK = 'Cowork is an autonomous agent that takes actions across Microsoft 365 on your behalf \u2014 sending emails, scheduling meetings, creating documents, posting in Teams, and scheduling recurring tasks. Access: m365.cloud.microsoft > left nav > Agents > Cowork. Requires Frontier program enrollment.'
DESC_WORD_AGT = 'Create a declarative agent scoped to a Word document. Open the .docx in Word for Web > Copilot pane > + New Agent > name it, write a description, set the document as knowledge source > Share. Colleagues chat with it in Teams or M365 Copilot.'
DESC_PPT_AGT = 'Create a declarative agent scoped to a PowerPoint presentation. Great for strategy decks or Board presentations many people need to reference. Same setup as Word Agent but using a .pptx file.'
DESC_XL_AGT = 'Create a declarative agent scoped to an Excel workbook. Colleagues ask data questions in plain English without opening Excel. Open .xlsx in Excel for Web > Copilot pane > + New Agent > set workbook as knowledge source > share.'
DESC_BUILDER = 'Build a custom declarative agent in Copilot Studio \u2014 no coding required. Access: copilotstudio.microsoft.com > Create > New Agent. Add name, description, knowledge sources (SharePoint URLs or uploaded files), topics/actions. Publish to Teams in under 10 minutes.'

def esc(s):
    s = str(s)
    s = s.replace('\\', '\\\\')
    s = s.replace("'", "\\'")
    s = s.replace('\n', ' ')
    s = s.replace('\r', '')
    return s

def tool(name, lic, acct, prompts, desc=''):
    return {'tool': name, 'license': lic, 'account': acct, 'desc': desc, 'prompts': prompts}

def ind(id, sectorId, name, icon, color, accent, company, tagline, scenario, files, tools,
        companyID='', taglineID='', subsector=''):
    return {
        'id': id, 'sectorId': sectorId, 'subsector': subsector,
        'name': name, 'icon': icon, 'color': color, 'accent': accent,
        'company': company, 'tagline': tagline, 'scenario': scenario,
        'companyID': companyID, 'taglineID': taglineID,
        'files': files, 'prompts': tools
    }

def write_entry(f, entry, is_last):
    e = entry
    f.write("    {\n")
    f.write(f"      id: '{esc(e['id'])}',\n")
    f.write(f"      sectorId: '{esc(e.get('sectorId',''))}',\n")
    if e.get('subsector'):
        f.write(f"      subsector: '{esc(e['subsector'])}',\n")
    f.write(f"      name: '{esc(e['name'])}',\n")
    f.write(f"      icon: '{e['icon']}',\n")
    f.write(f"      color: '{e['color']}',\n")
    f.write(f"      accent: '{e['accent']}',\n")
    f.write(f"      company: '{esc(e['company'])}',\n")
    f.write(f"      tagline: '{esc(e['tagline'])}',\n")
    if e.get('companyID'):
        f.write(f"      companyID: '{esc(e['companyID'])}',\n")
    if e.get('taglineID'):
        f.write(f"      taglineID: '{esc(e['taglineID'])}',\n")
    f.write(f"      scenario: '{esc(e['scenario'])}',\n")
    files_js = ', '.join(f"'{esc(x)}'" for x in e.get('files', []))
    f.write(f"      files: [{files_js}],\n")
    f.write(f"      prompts: [\n")
    tools = e.get('prompts', [])
    for ti, t in enumerate(tools):
        tl = ti == len(tools) - 1
        f.write(f"        {{\n")
        f.write(f"          tool: '{esc(t['tool'])}',\n")
        f.write(f"          license: '{esc(t.get('license',''))}',\n")
        f.write(f"          account: '{esc(t.get('account',''))}',\n")
        if t.get('desc'):
            f.write(f"          desc: '{esc(t['desc'])}',\n")
        f.write(f"          prompts: [\n")
        ps = t.get('prompts', [])
        for pi, p in enumerate(ps):
            pl = pi == len(ps) - 1
            f.write(f"            '{esc(p)}'" + ('' if pl else ',') + "\n")
        f.write(f"          ]\n")
        f.write(f"        }}" + ('' if tl else ',') + "\n")
    f.write(f"      ]\n")
    f.write(f"    }}" + ('' if is_last else ',') + "\n")
