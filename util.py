FREE_ACCT = 'Sasha Ouellet \u2014 SashaO@ABSx62256373.OnMicrosoft.com'
M365_ACCT = 'MOD Administrator \u2014 admin@ABSx62256373.onmicrosoft.com'
FREE_LIC = 'Free \u2014 no M365 Copilot license needed'
M365_LIC = 'M365 Copilot'
FRONTIER_LIC = 'M365 Copilot + Frontier Program'

T_CHAT = '💬 Microsoft 365 Copilot Chat'
T_RESEARCHER = '🔍 Researcher'
T_ANALYST = '📊 Analyst'
T_EXCEL = '📊 Copilot in Excel'
T_WORD = '📝 Copilot in Word'
T_PPT = '🎯 Copilot in PowerPoint'
T_OUTLOOK = '📧 Copilot in Outlook'
T_TEAMS = '🎙 Copilot in Teams (Recap → Word minutes)'
T_NOTEBOOK = '📓 Copilot Notebook'
T_COWORK = '🤝 Cowork (Frontier)'
T_WORD_AGT = '📝 Word Agent (Generate document)'
T_PPT_AGT = '🎯 PowerPoint Agent (Generate deck)'
T_XL_AGT = '📊 Excel Agent (Generate workbook)'
T_BUILDER = '🏗 Agent Builder (M365 Copilot Chat)'

DESC_CHAT = 'Microsoft 365 Copilot Chat at m365.cloud.microsoft/chat \u2014 secure, work-grounded chat. Type a prompt and reference files with /file. Available to anyone with an M365 account at no extra cost (Free tier) and supercharged with M365 Copilot license (work-grounded answers, agents, summaries across mailbox/files/meetings).'
DESC_RESEARCHER = 'Reasoning agent in Microsoft 365 Copilot Chat \u2014 access via m365.cloud.microsoft/chat > Agents > Researcher. Two demo modes to highlight: (1) \ud83d\udd0d Critique Mode \u2014 Researcher self-critiques every source, verifying claims against the originals before including them in the report. (2) \u2696\ufe0f Model Council \u2014 Researcher orchestrates multiple frontier reasoning models (GPT-5, Claude, Gemini, etc.) to debate the brief, surface dissent, and synthesise a balanced answer. Grounded in live web + your tenant data with citations. Requires M365 Copilot license.'
DESC_ANALYST = 'Reasoning agent in Microsoft 365 Copilot Chat \u2014 access via m365.cloud.microsoft/chat > Agents > Analyst. Upload an Excel/CSV or /reference a tenant file. Analyst writes Python under the hood, builds charts and dashboards, runs forecasts/regressions, and explains the result \u2014 no formula writing required. Show off chart + dashboard generation in the demo.'
DESC_EXCEL = 'Copilot inside Excel for the Web. Open a workbook > Copilot pane on the right. Two demo angles: (1) inline \"Edit with Copilot\" agent mode that performs multi-step actions across the workbook \u2014 add columns, build pivot tables, build dashboards, conditional formatting; (2) ask grounded questions about the data. Requires M365 Copilot license.'
DESC_WORD = 'Copilot inside Word for the Web. Open a .docx > Copilot pane. Two demo angles: (1) inline \"Edit with Copilot\" agent mode that rewrites, restructures or expands sections of the document in one instruction \u2014 great for board minutes/briefs; (2) draft new sections grounded in /reference files. Requires M365 Copilot license.'
DESC_PPT = 'Copilot inside PowerPoint for the Web. Open a .pptx > Copilot pane. Two demo angles: (1) inline \"Edit with Copilot\" agent mode that restyles/restructures the deck, generates speaker notes, swaps imagery; (2) generate new slides grounded in /reference files. Requires M365 Copilot license.'
DESC_OUTLOOK = 'Copilot inside Outlook on the Web. Two demo angles: (1) summarise long threads + draft replies grounded in tenant context; (2) coach my writing for tone, clarity and stakeholder fit. Requires M365 Copilot license.'
DESC_TEAMS = 'For this demo we use Copilot grounded in the Teams Recap on the demo tenant for one of four meetings: "New Software Implementation", "Potential Merger", "Negotiating Marketing Contract", or "Marketing Campaign Performance Review". Workflow: Open the meeting in your Teams calendar > the Recap page opens with AI Notes, chapters, transcript and action items > click the Copilot icon in the top right of the Recap page > Copilot opens grounded in the meeting transcript > type your minutes prompt > copy the structured output into a new Word document (or open M365 Copilot Chat with a /transcript reference and ask Copilot to produce a .docx). Note: Teams Recap has no Export to Word button \u2014 the workflow is Copilot pane > copy/paste OR M365 Copilot Chat. Requires M365 Copilot license + Teams Premium for full Recap features.'
DESC_NOTEBOOK = 'Microsoft 365 Copilot Notebook \u2014 access via m365.cloud.microsoft/chat > Notebook tab > + New Notebook. Add up to 5 source files (Word/Excel/PDF/PPT) at creation, then set the Instructions field once. Best for synthesising insights across multiple documents at once \u2014 ask several prompts against the same notebook without re-uploading.'
DESC_COWORK = 'Cowork is the autonomous agent in M365 Copilot \u2014 access via m365.cloud.microsoft > left nav > Agents > Cowork. ONE prompt that delegates 5 parallel tasks: draft a Word doc, draft a second Word doc, send an email, schedule a calendar meeting, and post a Teams message \u2014 Cowork executes them all and reports back. Requires M365 Copilot + Frontier Program enrollment.'
DESC_WORD_AGT = 'Word Agent in M365 Copilot Chat \u2014 do NOT open Word first. From m365.cloud.microsoft/chat type a prompt with /reference files context describing the document you want, and Copilot returns a fully drafted .docx you can open in Word. Great for: board minutes, briefing memos, policy drafts, status reports. Requires M365 Copilot license.'
DESC_PPT_AGT = 'PowerPoint Agent in M365 Copilot Chat \u2014 do NOT open PowerPoint first. From m365.cloud.microsoft/chat type a prompt with /reference files context describing the deck you want (theme, audience, slide list), and Copilot returns a complete .pptx you can open in PowerPoint. Great for: Board decks, IR decks, town hall decks. Requires M365 Copilot license.'
DESC_XL_AGT = 'Excel Agent in M365 Copilot Chat \u2014 do NOT open Excel first. From m365.cloud.microsoft/chat type a prompt with /reference files context describing the workbook you want (sheets, columns, charts, conditional formatting), and Copilot returns a fully built .xlsx you can open in Excel. Great for: KPI dashboards, division comparisons, scenario models. Requires M365 Copilot license.'
DESC_BUILDER = 'Agent Builder is INSIDE Microsoft 365 Copilot Chat \u2014 NOT Copilot Studio. Access via m365.cloud.microsoft/chat > Agents > + Create an agent (or sidebar Build). Walkthrough: (1) Describe \u2014 type what your agent should do in plain language; (2) Configure \u2014 add instructions, knowledge (SharePoint URLs / uploaded files), starter prompts; (3) Test in the right pane; (4) Create + share to colleagues. No coding, no environment setup, no licence beyond M365 Copilot.'


def esc(s):
    s = str(s)
    s = s.replace('\\', '\\\\')
    s = s.replace("'", "\\'")
    s = s.replace('\n', ' ')
    s = s.replace('\r', '')
    return s


def _norm_prompt(p):
    """Normalise a single prompt entry to {instr, prompt} dict shape.

    Accepts: a plain string (legacy)  OR  a dict {instr, prompt} (new shape).
    Returns: {'instr': '<str>', 'prompt': '<str>'}.
    """
    if isinstance(p, dict):
        return {'instr': p.get('instr', '') or '', 'prompt': p.get('prompt', '') or ''}
    return {'instr': '', 'prompt': str(p)}


def _norm_prompts(prompts):
    if not prompts:
        return []
    return [_norm_prompt(p) for p in prompts]


def tool(name, lic, acct, prompts, desc='', promptsID=None, persona=None,
         personaID=None, promptsBM=None):
    """Define a tool block with EN/ID/BM prompt arrays.

    `prompts`/`promptsID`/`promptsBM` items can be plain strings (legacy, treated as
    pure prompt body with empty instructions) OR dicts of shape
    {'instr': '<setup steps>', 'prompt': '<copyable prompt body>'}.
    """
    return {
        'tool': name, 'license': lic, 'account': acct, 'desc': desc,
        'prompts':   _norm_prompts(prompts),
        'promptsID': _norm_prompts(promptsID),
        'promptsBM': _norm_prompts(promptsBM),
        'persona': persona or [],
        'personaID': personaID or [],
    }


def ind(id, sectorId, name, icon, color, accent, company, tagline, scenario, files, tools,
        companyID='', taglineID='', scenarioID='', subsector='',
        relevantDepts=None, storyboard=None, personas=None, geo='MY'):
    return {
        'id': id, 'sectorId': sectorId, 'subsector': subsector,
        'name': name, 'icon': icon, 'color': color, 'accent': accent,
        'company': company, 'tagline': tagline, 'scenario': scenario,
        'companyID': companyID, 'taglineID': taglineID, 'scenarioID': scenarioID,
        'files': files, 'prompts': tools,
        'relevantDepts': relevantDepts or [],
        'storyboard': storyboard or [],
        'personas': personas or [],
        'geo': geo,
    }


def _write_storyboard(f, sb, indent='      '):
    f.write(f"{indent}storyboard: [\n")
    for si, s in enumerate(sb):
        sl = si == len(sb) - 1
        f.write(f"{indent}  {{\n")
        f.write(f"{indent}    ex: {s.get('ex', si+1)},\n")
        f.write(f"{indent}    title: '{esc(s.get('title',''))}',\n")
        if s.get('titleID'):
            f.write(f"{indent}    titleID: '{esc(s['titleID'])}',\n")
        f.write(f"{indent}    minutes: {s.get('minutes', 15)},\n")
        f.write(f"{indent}    mode: '{esc(s.get('mode',''))}',\n")
        if s.get('summary'):
            f.write(f"{indent}    summary: '{esc(s['summary'])}',\n")
        if s.get('summaryID'):
            f.write(f"{indent}    summaryID: '{esc(s['summaryID'])}',\n")
        tasks = s.get('tasks', [])
        f.write(f"{indent}    tasks: [\n")
        for ti, t in enumerate(tasks):
            tl = ti == len(tasks) - 1
            f.write(f"{indent}      {{")
            f.write(f"n: '{esc(t.get('n',''))}', ")
            f.write(f"tool: '{esc(t.get('tool',''))}', ")
            f.write(f"verb: '{esc(t.get('verb',''))}', ")
            if t.get('verbID'):
                f.write(f"verbID: '{esc(t['verbID'])}', ")
            f.write(f"mode: '{esc(t.get('mode','show'))}'")
            if t.get('label'):
                f.write(f", label: '{esc(t['label'])}'")
            f.write("}" + ('' if tl else ',') + "\n")
        f.write(f"{indent}    ]\n")
        f.write(f"{indent}  }}" + ('' if sl else ',') + "\n")
    f.write(f"{indent}],\n")


def _write_personas(f, ps, indent='      '):
    f.write(f"{indent}personas: [\n")
    for pi, p in enumerate(ps):
        pl = pi == len(ps) - 1
        f.write(f"{indent}  {{")
        f.write(f"name: '{esc(p.get('name',''))}', ")
        f.write(f"role: '{esc(p.get('role',''))}', ")
        if p.get('roleID'):
            f.write(f"roleID: '{esc(p['roleID'])}', ")
        f.write(f"acct: '{esc(p.get('acct',''))}', ")
        f.write(f"lic: '{esc(p.get('lic',''))}'")
        if p.get('color'):
            f.write(f", color: '{esc(p['color'])}'")
        f.write("}" + ('' if pl else ',') + "\n")
    f.write(f"{indent}],\n")


def _write_prompt_array(f, arr, key, indent='          '):
    f.write(f"{indent}{key}: [\n")
    for pi, p in enumerate(arr):
        pl = pi == len(arr) - 1
        f.write(f"{indent}  {{instr: '{esc(p.get('instr',''))}', prompt: '{esc(p.get('prompt',''))}'}}"
                + ('' if pl else ',') + "\n")
    f.write(f"{indent}]")


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
    f.write(f"      geo: '{esc(e.get('geo','MY'))}',\n")
    f.write(f"      company: '{esc(e['company'])}',\n")
    f.write(f"      tagline: '{esc(e['tagline'])}',\n")
    if e.get('companyID'):
        f.write(f"      companyID: '{esc(e['companyID'])}',\n")
    if e.get('taglineID'):
        f.write(f"      taglineID: '{esc(e['taglineID'])}',\n")
    f.write(f"      scenario: '{esc(e['scenario'])}',\n")
    if e.get('scenarioID'):
        f.write(f"      scenarioID: '{esc(e['scenarioID'])}',\n")
    files_js = ', '.join(f"'{esc(x)}'" for x in e.get('files', []))
    f.write(f"      files: [{files_js}],\n")
    if e.get('relevantDepts'):
        rd = ', '.join(f"'{esc(x)}'" for x in e['relevantDepts'])
        f.write(f"      relevantDepts: [{rd}],\n")
    if e.get('personas'):
        _write_personas(f, e['personas'])
    if e.get('storyboard'):
        _write_storyboard(f, e['storyboard'])
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
        # prompts array (always present, dict shape)
        _write_prompt_array(f, t.get('prompts', []), 'prompts')
        if t.get('promptsID'):
            f.write(",\n")
            _write_prompt_array(f, t['promptsID'], 'promptsID')
        if t.get('promptsBM'):
            f.write(",\n")
            _write_prompt_array(f, t['promptsBM'], 'promptsBM')
        if t.get('persona'):
            f.write(",\n")
            ppl = t['persona']
            pers = ', '.join(f"'{esc(x)}'" for x in ppl)
            f.write(f"          persona: [{pers}]")
        if t.get('personaID'):
            f.write(",\n")
            ppl = t['personaID']
            pers = ', '.join(f"'{esc(x)}'" for x in ppl)
            f.write(f"          personaID: [{pers}]")
        f.write("\n")
        f.write(f"        }}" + ('' if tl else ',') + "\n")
    f.write(f"      ]\n")
    f.write(f"    }}" + ('' if is_last else ',') + "\n")

