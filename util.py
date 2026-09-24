FREE_ACCT = 'Sasha Ouellet \u2014 SashaO@ABSx62256373.OnMicrosoft.com'
M365_ACCT = 'MOD Administrator \u2014 admin@ABSx62256373.onmicrosoft.com'
ANY_ACCT = 'Free: Sasha Ouellet \u2014 SashaO@ABSx62256373.OnMicrosoft.com  \u2022  M365: MOD Administrator \u2014 admin@ABSx62256373.onmicrosoft.com'
FREE_LIC = 'Free \u2014 no Microsoft 365 Copilot license needed'
M365_LIC = 'Microsoft 365 Copilot'
ANY_LIC = 'Either Free Copilot Chat (no extra license) OR Microsoft 365 Copilot license'
FRONTIER_LIC = 'Microsoft 365 Copilot + Frontier Program'

# Labels below stay stable for the build steps that match on them. copilot_refresh.py
# renames them in the generated data (for example Cowork (Frontier) -> Copilot Cowork).
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
T_BUILDER = '🏗 Agent Builder (Microsoft 365 Copilot Chat)'
T_BUILDER_FREE = '🆓 Agent Builder (Free Copilot Chat — public URL knowledge)'
T_SCOUT = '🧭 Microsoft Scout (Frontier preview)'
T_SHAREPOINT = '🌐 AI in SharePoint'
T_CREATE = '🎨 Copilot Create (image · poster · infographic · video)'

DESC_CHAT = 'Microsoft Copilot Chat at m365.cloud.microsoft/chat (the new name for Microsoft 365 Copilot Chat, August 2026): secure chat for work. Type a prompt and reference files with /file. Web and work chat are now one experience: the Work IQ button at the top left turns work data on or off (GA 25 Aug 2026). Available to anyone with a Microsoft 365 work account at no extra cost. Copilot Chat in Outlook can also use your inbox, calendar and meetings without a Microsoft 365 Copilot license (GA 1 Jul 2026). A Microsoft 365 Copilot license adds work-grounded answers across mailbox, files and meetings in every app, plus Researcher, Analyst and the Word, Excel and PowerPoint agents.'
DESC_RESEARCHER = 'Reasoning agent in Microsoft 365 Copilot Chat — access via m365.cloud.microsoft/chat > Agents > Researcher. Two demo modes to highlight: (1) 🔍 Critique Mode — Researcher self-critiques every source, verifying claims against the originals before including them in the report. (2) ⚖️ Model Council — Researcher orchestrates multiple frontier reasoning models (GPT-5.5 Thinking and Claude Opus 4.7) to debate the brief, surface dissent, and synthesise a balanced answer. Grounded in live web + your tenant data with citations — and now optionally federated connectors (Moody’s, LSEG, HubSpot, Notion, ServiceNow) for real-time external data. NEW (GA 25 Aug 2026): a model selector lets you choose which supported model runs the report. Requires Microsoft 365 Copilot license.'
DESC_ANALYST = 'Reasoning agent in Microsoft 365 Copilot Chat \u2014 access via m365.cloud.microsoft/chat > Agents > Analyst. Upload an Excel/CSV or /reference a tenant file. Analyst writes Python under the hood, builds charts and dashboards, runs forecasts/regressions, and explains the result \u2014 no formula writing required. Show off chart + dashboard generation in the demo.'
DESC_EXCEL = 'Copilot in Excel on the web, Windows and Mac. Open a workbook > Copilot pane on the right. Demo angles: (1) inline "Edit with Copilot" agent mode that performs multi-step actions across the workbook: add columns, build pivot tables, dashboards, conditional formatting; (2) 📈 Plan with Copilot (generally available): Copilot proposes a step-by-step plan BEFORE it changes the workbook, so users can review and adjust first; (3) 🐍 Python in Edit with Copilot (GA 25 Aug 2026): Copilot runs Python in Excel for forecasts, regressions, simulations and custom charts, and writes the results into the workbook; (4) newer skills: brand kit (July 2026), @theme-design, Power BI grounding and change history (August 2026). Requires Microsoft 365 Copilot license.'
DESC_WORD = 'Copilot inside Word for the Web. Open a .docx > Copilot pane. Three demo angles: (1) inline "Edit with Copilot" agent mode that rewrites, restructures or expands sections of the document in one instruction — great for board minutes/briefs; (2) draft new sections grounded in /reference files; (3) 🧠 model picker — switch between GPT and Claude for the same editing workflow when teams prefer specific model behaviours. Claude Sonnet 5 is now the default model for higher-reasoning tasks in Word for the web (Aug 2026). Requires Microsoft 365 Copilot license.'
DESC_PPT = 'Copilot in PowerPoint. Open a .pptx > Copilot pane. Demo angles: (1) inline "Edit with Copilot" agent mode that restyles or restructures the deck, generates speaker notes and swaps imagery; (2) build a deck from Work IQ, a Teams meeting or chat, an email or an existing deck (GA July to August 2026); (3) 🎨 Brand Kit (GA 14 Sep 2026): approved templates, imagery, icons and fonts, with a stricter brand mode that keeps Copilot on approved layouts; (4) prebuilt skills such as @Review Presentation, @Prepare for Questions and @Visualize Slide (GA 14 Sep 2026); (5) 🌐 public web grounding: add a webpage URL as a reference for current external context. Requires Microsoft 365 Copilot license.'
DESC_OUTLOOK = 'Copilot in Outlook. Demo angles: (1) summarise long threads and draft replies grounded in tenant context; (2) Get Coaching now opens in Copilot chat, where you choose which suggestions to apply and Copilot updates the draft in place (GA 11 Aug 2026); (3) ✍️ first draft in canvas (new Outlook): Copilot writes the email in place, asks about goal, audience and tone, then iterates without copy-paste; (4) Schedule with Copilot in classic Outlook finds times, books rooms, drafts agendas and sends invites (GA Aug 2026). Copilot Chat in Outlook can use the inbox, calendar and meetings without a Microsoft 365 Copilot license (GA 1 Jul 2026). Schedule with Copilot and meeting prep need the license.'
DESC_TEAMS = 'For this demo we use Copilot grounded in the Teams Recap on the demo tenant for one of four meetings: "New Software Implementation", "Potential Merger", "Negotiating Marketing Contract", or "Marketing Campaign Performance Review". Workflow: Open the meeting in your Teams calendar > the Recap page opens with AI Notes, chapters, transcript and action items > click the Copilot icon in the top right of the Recap page > Copilot opens grounded in the meeting transcript > type your minutes prompt > copy the structured output into a new Word document (or open Microsoft 365 Copilot Chat with a /transcript reference and ask Copilot to produce a .docx). Note: Teams Recap has no Export to Word button — the workflow is Copilot pane > copy/paste OR Microsoft 365 Copilot Chat. Newer additions: 🗂️ the Meeting recaps app with 30 days of recaps, filters and audio recaps (July 2026) and 🌐 a translation button for recaps (August 2026). Also from April to May 2026: 📞 Copilot Call Delegation — Copilot can answer incoming Teams calls on the user’s behalf, gather context from callers, and book follow-up appointments via Microsoft Bookings; 🗣️ Consecutive Interpretation — turn-based translation between two languages with Interpreter on the meeting stage, ideal for ASEAN cross-border meetings. Requires Microsoft 365 Copilot license + Teams Premium for full Recap features.'
DESC_NOTEBOOK = 'Copilot Notebooks: open Notebooks in the Microsoft Copilot app (m365.cloud.microsoft/chat) or in OneNote, where both views stay in sync (August 2026). Add source files at creation, then set the Instructions field once. Sources can include Word, Excel, PDF and PowerPoint files, Outlook emails and Teams meetings with transcript, notes and chat (GA 25 Aug 2026), plus Markdown, plain text and rich text files. Best for synthesising insights across many sources: ask several prompts against the same notebook without re-uploading. Generally available since 1 Jul 2026 on Windows and the web: 📄 Quick create for Word, PowerPoint and Excel files, and 🧠 Mind maps (click a node to drill in). Also available: 🔗 SharePoint sites and OneNote pages as sources, 🌐 web links, 🎧 Audio Overviews and 👥 sharing with a Microsoft 365 Group. Requires Microsoft 365 Copilot license.'
DESC_COWORK = 'Copilot Cowork is the autonomous agent in Microsoft Copilot, generally available since 16 Jun 2026. Open Microsoft Copilot (m365.cloud.microsoft or copilot.cloud.microsoft) and select Cowork in the toggle next to Chat; Cowork also works in Outlook, Teams and the Copilot desktop and mobile apps. Describe what you need in natural language (up to 250,000 characters, voice input supported); Cowork carries out the work end to end and shows each step. Capabilities: ✉️ send, reply and forward emails with attachments; 🗓️ schedule meetings and manage the calendar; 📝 create and edit Word, Excel, PowerPoint and PDF files; 💬 post in Teams channels and chats; 🔍 search the organisation for files, people and information; 📁 browse and manage OneDrive and SharePoint; 🔬 deep research across sources; 🖼️ create and edit images with ChatGPT Images 2.0; 🌐 local browser use in Microsoft Edge (GA since August 2026); 📊 Power BI reports and semantic models; ⏰ Automations: scheduled prompts and event-driven tasks that run when a matching email or Teams message arrives. Choose from Anthropic and OpenAI models or leave the picker on Auto, and set an effort level from Light to Max (Medium is the default). Cowork asks before sensitive actions: approve once, skip similar prompts for the rest of the session, or cancel. Created files appear in the side panel for preview and download. Requires a Microsoft 365 Copilot license, with Cowork and usage-based billing in Copilot Credits turned on by an admin. Only the App skill and choosing GPT 5.5 still need the Frontier Program.'

DESC_SCOUT = 'Microsoft Scout — a desktop AI application (Frontier preview, June 2026) that goes beyond Copilot Chat. Scout acts on your local files, runs shell commands with permission tiers (auto-approve / prompt / deny), controls a browser, and works with your Microsoft 365 data through direct API tools and WorkIQ. Key capabilities: \ud83d\udcc1 file system (create/edit/search files in your workspace with the Word/Excel/PowerPoint/Web Artifacts skills); \ud83d\udda5️ shell commands for builds/tests/git/gh/curl with sensitive-path guards; \ud83c\udf10 browser automation for portal tasks (Azure portal cost checks, Loop edits, web research, screenshots); \ud83d\udce7 M365 access — read/send email, schedule meetings, post Teams, browse OneDrive, run WorkIQ across email+calendar+Teams+docs; \ud83e\udd16 sub-agents (Explore / Task / Code review / Research / General-purpose) for parallel investigation; ❤️ Heartbeat mode — background recurring prompts on a schedule (every 15 min/30 min/1 hr/2 hr, work hours/days, separate restrictive permissions when you’re not present); \ud83d\udd04 Automations — schedule- or condition-triggered tasks with one-shot or recurring runs, importable from GitHub; \ud83d\udd10 Permissions UI — granular allow/deny lists, sensitive paths, auto-approve toggles. Requires Frontier Program enrollment, a Microsoft 365 Copilot license and a GitHub Copilot Business or Enterprise license; runs on Windows 11 or macOS 12 or later after an admin completes setup. Currently a preview feature — may change as Microsoft iterates.'

DESC_SHAREPOINT = 'AI in SharePoint — Microsoft 365 Copilot capabilities built directly into SharePoint to make your files, pages, and sites Copilot-ready. Several features are now generally available, including planning and building solutions from the Build node of the SharePoint start page and the floating Copilot button in the OneDrive and SharePoint file previewer (29 Jul 2026); personal skills in SharePoint are in public preview (August 2026). Access: the Floating Button in the bottom-right corner of any supported SharePoint page or library surfaces context-sensitive actions based on your role (Site Manager / Content Manager / Content Creator / Content Consumer), location (page or library), and selection (file or folder). Also reachable via the Agents coin in the suite navigation and the AI actions button on selected files. Capabilities by category: \ud83d\udcc4 Work with files — Ask a Question about Content, Summarize this file, Compare files, Generate Audio Overview, Generate FAQ from File; \ud83d\uddc2️ Organize libraries — Create autofill columns (AI fills based on file content), Automate workflows / set up rules, Create views; \ud83c\udfa8 Pages and sites — Improve your SharePoint site with AI (fix broken links, retire outdated pages, fill content gaps), Create Page / Section / FAQ Webpart with AI, Refine pages with Design Ideas, Write and Rewrite with AI. Note: not available on SharePoint Home, Viva Connections, or SharePoint sites within Teams. Requires Microsoft 365 Copilot license.'

DESC_CREATE = 'Copilot Create — a tab in the Microsoft Copilot app (m365.cloud.microsoft) where users generate visual assets from natural-language prompts. Capabilities: \ud83d\uddbc️ Image — generate or edit images; bring text + style direction; request square/landscape/portrait; iterate by referring to the previous image. \ud83d\udcdc Poster — produce one-page posters for events, awareness campaigns, regulator deadlines, all-hands; pick layouts (grid, focal, split); supply headline + body + CTA. \ud83d\udcca Infographic — multi-section data visualisation; supply data points + theme; Copilot picks layout and icons. \ud83c\udfac Video — short-form video (15s–60s) for internal comms or social; add voiceover, background music and transitions. Also: stickers, social posts (LinkedIn/X), branded templates, brand-kit colour and font controls. Output downloads as PNG/JPG/MP4 or saves to OneDrive. Image generation is also available in Copilot Chat without the add-on license; applying the organisation brand kit to visuals needs a Microsoft 365 Copilot license (GA 1 Jul 2026), and Copilot can build a brand kit from brand guidelines (GA 15 Jul 2026). Image generation respects the Microsoft Responsible AI policy (no real public figures, no copyrighted styles).'
DESC_WORD_AGT = 'Word Agent in Microsoft Copilot Chat. Open m365.cloud.microsoft/chat, then choose Word from the Tools menu or All Agents in the left pane, or @mention it in the prompt (July 2026). Describe what you want: Copilot generates a complete .docx preview in chat, asks clarifying questions on tone, length and audience, then saves the file to OneDrive. A premium capability: it needs a paid Microsoft 365 Copilot license, and an admin must allow Anthropic models or the agent is hidden. It grounds in your files, emails, meetings and sites through Work IQ. Great for: board minutes, briefing memos, policy drafts, status reports, employee onboarding guides.'
DESC_PPT_AGT = 'PowerPoint Agent in Microsoft Copilot Chat. Open m365.cloud.microsoft/chat, then choose PowerPoint from the Tools menu or All Agents in the left pane, or @mention it in the prompt (July 2026). Describe what you want: Copilot generates a complete .pptx preview in chat, asks clarifying questions on slide count, audience and theme, then saves the file to OneDrive. A premium capability: it needs a paid Microsoft 365 Copilot license, and an admin must allow Anthropic models or the agent is hidden. It grounds in your files, emails, meetings and sites through Work IQ. Great for: Board decks, IR decks, town hall decks, marketing strategy presentations.'
DESC_XL_AGT = 'Excel Agent in Microsoft Copilot Chat. Open m365.cloud.microsoft/chat, then choose Excel from the Tools menu or All Agents in the left pane, or @mention it in the prompt (July 2026). Describe what you want: Copilot generates a complete .xlsx preview in chat, asks clarifying questions on sheets, columns, charts, formulas and formatting, then saves the file to OneDrive. A premium capability: it needs a paid Microsoft 365 Copilot license, and an admin must allow Anthropic models or the agent is hidden. It grounds in your files, emails, meetings and sites through Work IQ. Great for: KPI dashboards, division comparisons, budget trackers, scenario models, summary reports from existing data.'
DESC_BUILDER = 'Agent Builder is INSIDE Microsoft Copilot Chat, NOT Copilot Studio. Select New agent in the left pane of Copilot Chat on the web or in Teams (not on mobile). Walkthrough: (1) Describe: type what your agent should do in plain language; (2) Configure: add instructions, knowledge (SharePoint sites and files, one SharePoint list of up to 20,000 items, OneDrive files, Teams chats, email, meetings, people, OneNote pages, Copilot connectors or uploaded files) and starter prompts; (3) Test in the right pane; (4) Create and share with colleagues, OR submit to the Agent Store: after admin approval it appears under Built by your org (GA 15 Jul 2026). No coding, no environment setup. Works on BOTH the free Copilot Chat account (Sasha) and a Microsoft 365 Copilot license (MOD Admin); the knowledge you can add depends on the license.'
DESC_BUILDER_FREE = 'Free-tier Agent Builder inside Microsoft Copilot Chat: the same 4-step flow (Describe, Configure, Test, Create) on a free Copilot Chat account with no paid license. Knowledge without a license: web search, scoped web search of up to 4 public sites and OneNote pages, plus the code interpreter and image generator capabilities. SharePoint, OneDrive, Copilot connectors and uploaded files need a license or metered billing, so test before the demo. Ideal for citizen-developer agents that summarise regulator microsites, peer investor-relations pages, public sustainability reports and industry research portals, at zero extra cost. Submit to the Agent Store for org-wide discovery after admin approval (GA 15 Jul 2026).'


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
         personaID=None, promptsBM=None, notebookMeta=None):
    """Define a tool block with EN/ID/BM prompt arrays.

    `prompts`/`promptsID`/`promptsBM` items can be plain strings (legacy, treated as
    pure prompt body with empty instructions) OR dicts of shape
    {'instr': '<setup steps>', 'prompt': '<copyable prompt body>'}.

    `notebookMeta` (Notebook tool only) carries the sources list + Instructions field
    that the renderer surfaces as a separate visual block above the numbered prompts.
    Shape: {'sources':['/file1.xlsx', ...], 'instructions':'...', 'instructionsID':'...', 'instructionsBM':'...'}.
    """
    p_en = _norm_prompts(prompts)
    p_id = _norm_prompts(promptsID)
    p_bm = _norm_prompts(promptsBM)
    per = list(persona or [])
    per_id = list(personaID or [])
    # Defensive: pad persona arrays to match the longer of EN/ID prompt counts. If
    # the per-array is empty, default to 'Hadar Caspit' (Group CFO archetype, one
    # of the 4 approved personas). If it has at least one entry, repeat the last.
    target = max(len(p_en), len(p_id))
    if target > 0:
        default = 'Hadar Caspit'
        if not per:
            per = [default] * target
        elif len(per) < target:
            per = per + [per[-1]] * (target - len(per))
        if not per_id:
            per_id = [default] * target
        elif len(per_id) < target:
            per_id = per_id + [per_id[-1]] * (target - len(per_id))
    return {
        'tool': name, 'license': lic, 'account': acct, 'desc': desc,
        'prompts':   p_en,
        'promptsID': p_id,
        'promptsBM': p_bm,
        'persona': per,
        'personaID': per_id,
        'notebookMeta': notebookMeta or None,
    }


def _norm_agents(arr):
    """Normalise an agents list into the IHH-style shape.

    Each agent is a dict with these fields (any missing default to empty):
      icon          short emoji or symbol shown on the picker card
      label         display label for picker card and step header
      name          string the user types into the Agent Builder Name field
      desc          string the user types into the Description field
      instructions  multi-paragraph system prompt for the Instructions field
      knowledge     list of {'file': '/PATH.xlsx', 'note': 'short hint'}
      knowledgeNote optional callout under the knowledge list (e.g. test tip)
      queries       list of 3 short test-query strings for the Test step

    Performs a deep copy so callers passing the same source list to both
    agentsID and agentsBM (build_master.py uses `agentsBM=agents_id` to seed
    BM with BI text for dialect-cleanup) end up with INDEPENDENT objects —
    otherwise fix_bm and fix_bi mutate shared knowledge[i].note dicts and
    one fixer overwrites the other (e.g. 'Bea Cukai' -> 'Bea Pajak' bleed).
    """
    import copy
    if not arr:
        return []
    out = []
    for a in arr:
        if not isinstance(a, dict):
            continue
        out.append({
            'icon':         a.get('icon', '🤖'),
            'label':        a.get('label', a.get('name', '')),
            'name':         a.get('name', ''),
            'desc':         a.get('desc', ''),
            'instructions': a.get('instructions', ''),
            'knowledge':    copy.deepcopy(a.get('knowledge', []) or []),
            'knowledgeNote': a.get('knowledgeNote', ''),
            'queries':      copy.deepcopy(a.get('queries', []) or []),
        })
    return out


def tool_builder(lic, acct, agents, desc='', agentsID=None, agentsBM=None,
                 persona=None, personaID=None, personaBM=None):
    """IHH-style Agent Builder block — 3 agent use-cases the demoer picks from.

    `agents` (and optional `agentsID`, `agentsBM`) is a list of 3 agent dicts —
    see `_norm_agents` for the shape.  The renderer detects the `isBuilder3`
    flag and emits a 3-card picker plus the IHH 4-step layout (Configure →
    Connect knowledge → Test → Share).
    """
    return {
        'tool': T_BUILDER,
        'license': lic,
        'account': acct,
        'desc': desc or DESC_BUILDER,
        'isBuilder3': True,
        'builderTier': 'premium',
        'prompts':   [],
        'promptsID': [],
        'promptsBM': [],
        'agents':   _norm_agents(agents),
        'agentsID': _norm_agents(agentsID),
        'agentsBM': _norm_agents(agentsBM),
        'persona':   persona or [],
        'personaID': personaID or [],
        'personaBM': personaBM or [],
        'notebookMeta': None,
    }


def tool_builder_free(acct, agents, desc='', agentsID=None, agentsBM=None,
                      persona=None, personaID=None, personaBM=None):
    """Free-tier Agent Builder block — 3 agent use-cases that use PUBLIC URL knowledge only.

    Same shape as `tool_builder` but pinned to FREE_LIC + the T_BUILDER_FREE
    tool label so the renderer routes it to the Copilot Chat tab and surfaces
    the free-tier UI copy (URL knowledge, no file uploads). Agent dicts here
    must use 'knowledge' entries shaped {'url': 'https://…', 'note': '…'}
    instead of {'file': '…', 'note': '…'}.
    """
    return {
        'tool': T_BUILDER_FREE,
        'license': FREE_LIC,
        'account': acct,
        'desc': desc or DESC_BUILDER_FREE,
        'isBuilder3': True,
        'builderTier': 'free',
        'prompts':   [],
        'promptsID': [],
        'promptsBM': [],
        'agents':   _norm_agents(agents),
        'agentsID': _norm_agents(agentsID),
        'agentsBM': _norm_agents(agentsBM),
        'persona':   persona or [],
        'personaID': personaID or [],
        'personaBM': personaBM or [],
        'notebookMeta': None,
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
        nm = t.get('notebookMeta')
        if nm:
            f.write(",\n")
            f.write(f"          notebookMeta: {{")
            srcs = nm.get('sources') or []
            if srcs:
                src_js = ', '.join(f"'{esc(x)}'" for x in srcs)
                f.write(f"sources: [{src_js}], ")
            if nm.get('instructions'):
                f.write(f"instructions: '{esc(nm['instructions'])}', ")
            if nm.get('instructionsID'):
                f.write(f"instructionsID: '{esc(nm['instructionsID'])}', ")
            if nm.get('instructionsBM'):
                f.write(f"instructionsBM: '{esc(nm['instructionsBM'])}', ")
            f.write("}")
        f.write("\n")
        f.write(f"        }}" + ('' if tl else ',') + "\n")
    f.write(f"      ]\n")
    f.write(f"    }}" + ('' if is_last else ',') + "\n")

