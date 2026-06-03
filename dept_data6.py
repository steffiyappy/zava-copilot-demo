# -*- coding: utf-8 -*-
# Executives & Business Leaders department — Zava Conglomerate.
# Inspired by https://www.microsoft.com/en-us/microsoft-365-copilot/copilot-for-business-leaders
# but rewritten for the Zava Group CEO + Group ExCo context (Bank, Plantations,
# Energy, Pharma, Consumer divisions across MY + ID).
import sys; sys.path.insert(0, '.')
from util import *

_FILES = [
    'EXEC_01_Group_ExCo_Pack_Q4FY26.pptx',
    'EXEC_02_Group_KPI_Dashboard_FY26.xlsx',
    'EXEC_03_Five_Division_Scorecard.xlsx',
    'EXEC_04_CEO_Daily_Briefing_Template.docx',
    'EXEC_05_Capital_Allocation_FY27.xlsx',
    'EXEC_06_Strategy_Refresh_Memo.docx',
    'EXEC_07_Town_Hall_Script_Q4.docx',
    'EXEC_08_Risk_Heatmap_Group.xlsx',
    'EXEC_09_M_and_A_Pipeline.xlsx',
    'EXEC_10_Investor_Day_Narrative.docx',
]

_PERSONA = 'Mod Admin'  # Group CEO / ExCo Chair persona for the demo
_PERSONAS = [{'name': 'Mod Admin', 'title': 'Group CEO / ExCo Chair'},
             {'name': 'Hadar Caspit', 'title': 'Group CFO'},
             {'name': 'Sasha Ouellet', 'title': 'Group Chief of Staff'}]

DEPARTMENTS_6 = [
  ind(
    'dept-executives', 'department', '👔 Executives & Business Leaders', '👔', '#1A237E', '#283593',
    'Zava Group ExCo',
    'The Group CEO walks into Monday with 5 divisions, 7 regulators, 12,000 employees, an investor day in 6 weeks, and 38 minutes between meetings to make every decision count.',
    "The Group CEO at Zava Conglomerate runs five operating divisions (Bank, Plantations, Energy, Pharma, Consumer) across Malaysia and Indonesia, with combined FY2026 revenue of MYR 28.4B, EBITDA margin of 19.7%, and 12,400 employees. The Group ExCo meets every Monday 8am to align on the week's top three decisions; the agenda routinely runs over because each division leader arrives with their own data, their own format, and their own narrative. Six weeks out from Investor Day, the CEO needs to sharpen the equity story (capital allocation, ESG progress, AI-driven productivity), pre-empt the 12 toughest analyst questions, and deliver a town hall to all 12,400 employees that lands across MY and ID without sounding corporate. Between meetings the CEO has 30-40 minute windows to read papers, approve decisions, draft messages, and prepare for the next room. The ask is straightforward: show how Microsoft 365 Copilot — across Chat, Researcher, Analyst, Word, Excel, PowerPoint, Outlook, Teams, Notebook, Cowork, Scout, AI in SharePoint, and Create — can give back 5-7 hours every week and let the CEO show up sharper in every conversation.",
    _FILES,
    [
      tool(T_CHAT, M365_LIC, M365_ACCT, [
        {'instr':'Open `m365.cloud.microsoft/chat`. /reference EXEC_01_Group_ExCo_Pack_Q4FY26.pptx + EXEC_02_Group_KPI_Dashboard_FY26.xlsx. Ground in the most recent ExCo pack and the live KPI dashboard.', 'prompt':"I'm walking into the Monday Group ExCo at 8am. Give me a 1-page CEO brief grounded in the attached ExCo pack and KPI dashboard: (1) the THREE decisions that must come out of this meeting; (2) for each decision, the data point, the trade-off, and the recommendation; (3) the FIVE questions I should ask each division leader before they finish presenting; (4) the ONE sentence I should open the meeting with. Plain English, no jargon. Output as a Markdown table I can paste into OneNote."},
        {'instr':'Open `m365.cloud.microsoft/chat`. /reference the last 30 days of email + Teams chats with the 5 division CEOs.', 'prompt':"Across my email and Teams chats with the 5 division CEOs over the last 30 days, what are they NOT telling me? Surface (a) topics raised more than once and never resolved; (b) topics where I gave a directive and there's no follow-up; (c) tonal shifts (frustration, hesitation, over-confidence) that suggest something below the surface. Cite the message, the date, and the person. Rank by how likely each is to surface at Investor Day."},
        {'instr':'Open `m365.cloud.microsoft/chat` > Agents > **Researcher** is fine OR plain Chat. Ground in the attached Investor Day narrative draft.', 'prompt':"Read the attached Investor Day narrative draft (EXEC_10_Investor_Day_Narrative.docx). Pretend you are (1) a sceptical sell-side analyst at CIMB, (2) a long-only ESG-focused fund manager from Singapore, (3) a Bursa Malaysia retail investor, and (4) a competitor's strategy head. From each perspective, list the 3 most pointed questions you would ask the Group CEO and the answer that would actually satisfy you. End with the FIVE narrative gaps the CEO should close before going on stage."},
        {'instr':'Open `m365.cloud.microsoft/chat`. /reference the last 14 days of board papers + ExCo minutes + the Strategy Refresh Memo.', 'prompt':"Build me a personal CEO dashboard for this week. Sections: (1) Top 3 risks across the 5 divisions — likelihood × impact × time-to-act; (2) Top 3 opportunities I should personally accelerate; (3) Top 3 people decisions waiting on me; (4) Top 3 commitments I made in the last 14 days that I have NOT yet closed out. Each item: 1-line description, due date, owner. End with the ONE thing I should drop from my calendar to make space."}
      ],
        DESC_CHAT,
        persona=[_PERSONA, _PERSONA, _PERSONA, _PERSONA]),

      tool(T_RESEARCHER, M365_LIC, M365_ACCT, [
        {'instr':'Open `m365.cloud.microsoft/chat` > Agents > **Researcher** > **Critique Mode**. Researcher will self-critique each source and verify claims against the originals.', 'prompt':"Research how 5 Asia-Pacific diversified conglomerates (e.g. CK Hutchison, Reliance, Genting, Astra International, Berjaya Corporation) have communicated AI-driven productivity gains to investors between 2024 and 2026. For each: (a) the metric they disclosed, (b) the methodology, (c) how the share price reacted in the 30 days post-disclosure, (d) which claims were challenged by analysts. Self-critique every source — flag any claim you cannot independently verify. Cite publication date for everything. Conclude with the 3 disclosure patterns that survived analyst scrutiny and the 3 that didn't."},
        {'instr':'Open `m365.cloud.microsoft/chat` > Agents > **Researcher** > **Model Council**. GPT-5.5 Thinking and Claude Opus 4.7 will debate the brief.', 'prompt':"Council brief: Should Zava Conglomerate split off its Pharma division via an IPO in FY2027, or retain it inside the group? Frame as a structured debate. Have one model argue the IPO case (capital release, focused management, valuation re-rating) and the other argue retention (synergies with Bank lending and Consumer distribution, ESG halo, dividend stability). Surface where the models DISAGREE most strongly, summarise the majority view, and flag the dissenting view clearly. End with the 4 conditions that would tip the decision either way."}
      ],
        DESC_RESEARCHER,
        persona=[_PERSONA, _PERSONA]),

      tool(T_ANALYST, M365_LIC, M365_ACCT, [
        {'instr':'', 'prompt':"Upload EXEC_03_Five_Division_Scorecard.xlsx to Analyst. Across all 5 divisions and across Revenue, EBITDA margin, ROIC, ESG score, and Customer NPS, build a single 5x5 RAG heatmap that shows where each division stands vs FY2026 target. Then run a 12-month rolling-trend regression for each division and tell me which division is most likely to MISS its FY2026 EBITDA guidance and by how much. Output: heatmap chart + ranked list with confidence bands."},
        {'instr':'', 'prompt':"Upload EXEC_05_Capital_Allocation_FY27.xlsx to Analyst. The CEO has MYR 2.8B of free capital to allocate across (a) Bank Tier-2 capital top-up, (b) Plantations replanting in Sabah, (c) Energy LSS5 solar bid in Malaysia + IPP bid in Java, (d) Pharma capacity expansion for biosimilars, (e) Consumer e-commerce platform. Run a Monte Carlo on each option using the IRR ranges in the workbook. Show which 3 options Pareto-dominate the others and where the CEO faces a real trade-off. Output: scenario fan chart + recommendation with sensitivity table."}
      ],
        DESC_ANALYST,
        persona=[_PERSONA, _PERSONA]),

      tool(T_EXCEL, M365_LIC, M365_ACCT, [
        {'instr':'Open EXEC_02_Group_KPI_Dashboard_FY26.xlsx in Excel for the Web. Open the Copilot pane > use **Edit with Copilot** (agent mode).', 'prompt':"Across the Revenue, Margin, ROIC, Cash, and Headcount tabs, build a new sheet called 'CEO 1-Pager'. Show 5 KPI tiles at the top (Group revenue YTD vs target, Group EBITDA margin vs target, Group ROIC vs cost of capital, Group net cash, Group headcount vs plan). Below the tiles, build a 5-row × 4-column small-multiples chart matrix — one row per division, columns for Revenue trend / Margin trend / ROIC trend / NPS trend. Apply RAG conditional formatting (red < -10% to target, amber -10% to -2%, green > -2%). Bold the cells where the variance is worsening for 2 or more consecutive quarters. The CEO presents this to Bursa-watching analysts in 90 minutes."},
        {'instr':'Open EXEC_05_Capital_Allocation_FY27.xlsx. Open the Copilot pane > click the menu above the prompt box > pick **Plan** mode.', 'prompt':"Plan mode: outline the steps you will take to build a capital allocation waterfall from FY2026 closing cash to FY2027 free capital, then to the 5 candidate uses, then to FY2027 closing cash. List each step as a numbered plan I can review/approve before edits land. After approval, execute, and on a second sheet 'Advanced' **use Python** to run a 5-year IRR sensitivity and plot a tornado chart of the top 5 IRR drivers."}
      ],
        DESC_EXCEL,
        persona=[_PERSONA, _PERSONA]),

      tool(T_WORD, M365_LIC, M365_ACCT, [
        {'instr':'Open EXEC_06_Strategy_Refresh_Memo.docx in Word for the Web. Open the Copilot pane > **Edit with Copilot** (agent mode).', 'prompt':"This is a 14-page strategy refresh memo. Restructure it into a 3-page CEO version: (1) the strategic question; (2) the 3 strategic moves we are committing to (with the trade-off explicit for each); (3) the 5 metrics we will track and the leading indicators that tell us we're on or off track. Cut the 'history of the company' opener. Keep one chart and one quote. Tone: confident but humble, no consultant-ese. Add inline comments wherever I should personally double-check the numbers."},
        {'instr':'Open EXEC_07_Town_Hall_Script_Q4.docx in Word. Open the Copilot pane.', 'prompt':"Rewrite this town hall script for an audience of 12,400 employees across Malaysia and Indonesia, half of whom are on the shop floor (plantation workers, plant operators, branch staff). Make it readable in 8 minutes. Cut all corporate-speak. Use 3 specific stories from the last quarter — one each from Plantations Sabah, Energy Pengerang, and Consumer Bandung. End with a clear ask of every employee. Generate two language variants — English and Bahasa Malaysia — using the model picker (try GPT first, then Claude, and tell me which version lands better)."}
      ],
        DESC_WORD,
        persona=[_PERSONA, _PERSONA]),

      tool(T_PPT, M365_LIC, M365_ACCT, [
        {'instr':'Open EXEC_01_Group_ExCo_Pack_Q4FY26.pptx in PowerPoint for the Web. Open the Copilot pane > **Edit with Copilot** (agent mode).', 'prompt':"Strip this 64-slide ExCo pack down to a 12-slide CEO read-out. Slide order: (1) one-page summary, (2) 5-division scorecard, (3-7) one slide per division — one chart, one decision, one ask, (8) capital allocation snapshot, (9) ESG progress, (10) people / talent, (11) risks, (12) the THREE asks of ExCo. Generate speaker notes for each slide in plain English. Use the **public web grounding** feature to pull a single relevant industry data point per division slide from the latest analyst notes (cite the source on each slide footer)."}
      ],
        DESC_PPT,
        persona=[_PERSONA]),

      tool(T_OUTLOOK, M365_LIC, M365_ACCT, [
        {'instr':'Open Outlook on the Web. Pick a multi-thread conversation (e.g. the Investor Day prep thread).', 'prompt':"Summarise this thread in 5 bullets: (1) the question the thread is trying to answer, (2) the consensus view, (3) the dissenting view and who holds it, (4) the 3 unresolved items, (5) the next step I should take TODAY. Then draft a reply I can send to the thread that closes 2 of the 3 unresolved items and asks for input on the third. Use the **first draft in canvas** feature so Copilot drafts the email IN PLACE and asks me clarifying questions on tone before sending."}
      ],
        DESC_OUTLOOK,
        persona=[_PERSONA]),

      tool(T_TEAMS, M365_LIC, M365_ACCT, [
        {'instr':'Open the Teams meeting recap for the most recent Group ExCo (or the IR prep meeting). Click the Copilot icon top-right of the recap page.', 'prompt':"From this ExCo meeting recap, generate a CEO-ready 1-page minutes document I can paste into Word: (1) decisions made, (2) decisions DEFERRED and why, (3) actions with owner + due date, (4) dissenting views captured (name + view), (5) the 3 most quotable lines from the discussion that I might want to repeat in the town hall. Then draft a follow-up Teams chat to the 5 division CEOs with the 3 commitments I made in the meeting and the deadlines."}
      ],
        DESC_TEAMS,
        persona=[_PERSONA]),

      tool(T_NOTEBOOK, M365_LIC, M365_ACCT, [
        {'instr':"Open `m365.cloud.microsoft/chat` > **Notebook** tab > **+ New Notebook**. Name it 'CEO Investor Day Briefing'. Add 5 sources: EXEC_10_Investor_Day_Narrative.docx, EXEC_02_Group_KPI_Dashboard_FY26.xlsx, EXEC_05_Capital_Allocation_FY27.xlsx, EXEC_06_Strategy_Refresh_Memo.docx, EXEC_08_Risk_Heatmap_Group.xlsx. Set the Instructions field once: 'You are my Investor Day prep partner. Ground every answer in the 5 sources. Be specific, cite the source, flag where the sources disagree.' Also use **Quick Create** to generate the **Audio Overview** (a 12-minute podcast-style executive summary) and the **Mind Map** of the equity story.", 'prompt':"Across all 5 sources, prep me for Investor Day. (1) The 12 toughest analyst questions I should expect, with my best answer + the back-up data point on each. (2) Where the sources disagree on the FY2027 outlook — flag every contradiction. (3) The 5 numbers I MUST land verbally without notes. (4) The 3 places where the narrative is weak and could be challenged. After answering, generate the Audio Overview AND the Mind Map and tell me which sections of the narrative are most under-supported by the source data."}
      ],
        DESC_NOTEBOOK,
        persona=[_PERSONA],
        notebookMeta={
          'sources': ['EXEC_10_Investor_Day_Narrative.docx','EXEC_02_Group_KPI_Dashboard_FY26.xlsx','EXEC_05_Capital_Allocation_FY27.xlsx','EXEC_06_Strategy_Refresh_Memo.docx','EXEC_08_Risk_Heatmap_Group.xlsx'],
          'instructions': 'You are my Investor Day prep partner. Ground every answer in the 5 sources. Be specific, cite the source, flag where the sources disagree. Use plain English. The reader is the Group CEO of a 5-division ASEAN conglomerate.',
          'name': 'CEO Investor Day Briefing'
        }),

      tool(T_COWORK, FRONTIER_LIC, M365_ACCT, [
        {'instr':"Open `m365.cloud.microsoft` > Agents > **Cowork (Frontier)**. Describe the task in plain language. Cowork will run end-to-end and surface every step (Thinking → Skill → Step-by-step → Streaming → Cards). Approve / Approve & Remember / Reject for medium-risk steps.", 'prompt':"My Investor Day is in 6 weeks. (1) Search OneDrive + SharePoint for every document tagged 'Investor Day FY26' OR 'Strategy Refresh' from the last 90 days. (2) Read them all and produce ONE consolidated 5-page brief in Word, saved to my OneDrive 'Investor Day' folder. (3) Schedule a 60-min prep meeting with Hadar Caspit (CFO), Daichi Maruyama (Head of IR), Sasha Ouellet (CoS) within the next 5 working days. (4) Send a Teams message to the 5 division CEOs asking for their division 1-pager by COB Friday — use a polite but firm tone. (5) Set up a recurring **schedule**: every Monday 7am produce a 1-page CEO daily briefing (top 3 risks, top 3 opportunities, top 3 people decisions) and email it to me before my 8am ExCo. Show me each step before you act on the email/calendar/Teams items."}
      ],
        DESC_COWORK,
        persona=[_PERSONA]),

      tool(T_SCOUT, M365_LIC, M365_ACCT, [
        {'instr':"Open Microsoft Scout (Frontier preview, desktop app). Connect to your local 'Zava CEO' workspace folder. Enable **Heartbeat mode** with restrictive permissions for after-hours runs.", 'prompt':"(1) Skill: file system + WorkIQ. Across my local 'Zava CEO' folder AND my M365 mail/calendar/Teams, build a single 'CEO Weekly Pulse' markdown file that lists: top 5 emails I haven't replied to that are >48h old; top 5 Teams threads where I'm @-mentioned and unread; top 5 calendar conflicts in the next 14 days; top 3 OneDrive files shared with me that I haven't opened. (2) Skill: browser via Playwright. Visit Bursa Malaysia announcements + IDX disclosures + Bank Negara press for the last 7 days, screenshot any item mentioning Zava or the 5 divisions. (3) Skill: shell + sub-agents. Spawn an Explore sub-agent to scan my 'Investor Day' folder for inconsistent numbers across drafts and produce a reconciliation table. (4) Heartbeat: re-run the CEO Weekly Pulse every Monday 6am, save the file with the date, email me a 3-bullet diff vs last week."}
      ],
        DESC_SCOUT,
        persona=[_PERSONA]),

      tool(T_SHAREPOINT, M365_LIC, M365_ACCT, [
        {'instr':"Navigate to the SharePoint site **'Zava Group ExCo'**. Use the Floating Button bottom-right. Role: Site Manager.", 'prompt':"(1) Ask a Question about Content: 'Across all documents tagged Q4FY26, summarise the 3 risks our division CEOs raised most often and where they conflict with the Risk Heatmap.' (2) Generate Audio Overview on EXEC_10_Investor_Day_Narrative.docx — 8-minute version for my driver-time. (3) Compare files: EXEC_06_Strategy_Refresh_Memo.docx vs the previous version 6 months ago — surface what changed in tone and what changed in commitment. (4) Improve the SharePoint site: scan for broken links, retire pages older than 18 months that haven't been opened in the last 90 days, fill content gaps where division pages have no FY26 strategy section. (5) Create a new FAQ webpart on the homepage answering the 12 questions employees ask the CEO most often (use AI to draft from past town hall Q&A transcripts). (6) Create autofill columns on the 'Board Papers' library to auto-classify each paper by Decision / Information / Approval."}
      ],
        DESC_SHAREPOINT,
        persona=[_PERSONA]),

      tool(T_CREATE, M365_LIC, M365_ACCT, [
        {'instr':"Open the M365 Copilot app > **Create** tab > **Image**.", 'prompt':"Create a 16:9 hero image for the Zava Group Investor Day stage backdrop. Show an abstract aerial-view composition — a Malaysian palm plantation transitioning into a Jakarta city skyline transitioning into a solar farm — sunrise lighting, warm tones, navy + amber palette, no text, no logos, no real public figures. Use **Flux** model. Square crop also for the Investor Day hold-card."},
        {'instr':"Open Create > **Poster**.", 'prompt':"A3 portrait poster for the Group CEO town hall. Headline: 'One Zava. Five Engines. One Promise.' Body: 'A new chapter starts together — Q4 FY2026 town hall, Friday 4pm MYT / 3pm WIB.' CTA: 'Join in person at HQ KL or live-stream from your office.' Brand kit: Zava navy + amber. Visual: subtle gradient, abstract icons of the 5 divisions arranged in a circle. No real people."},
        {'instr':"Open Create > **Infographic**.", 'prompt':"One-page vertical infographic for Investor Day handout. 5 sections: (1) Headline KPI — MYR 28.4B FY26 revenue; (2) 3 strategic priorities for FY27 (Productivity, Decarbonisation, Digital); (3) 5-division portfolio mix (donut + 1-line caption per slice); (4) ESG progress bars vs targets; (5) Capital allocation pie for FY27. Footer: 'Zava Conglomerate · Investor Day FY27 · Confidential.'"},
        {'instr':"Open Create > **Video**.", 'prompt':"A 30-second internal comms video to open the Q4 FY26 all-hands. Aspect 16:9. Voiceover: English (US). Music: 'Corporate — Optimistic'. Structure: (0–6s) cold open with the line 'In one quarter, here's what we built together'; (6–22s) 4 quick scenes — KL HQ, Sabah plantation, Pengerang energy plant, Bandung consumer hub — each 4 seconds with 1 caption; (22–28s) the CEO asks 'What will we build next?'; (28–30s) Zava logo card. Captions on for accessibility. Generate a Bahasa Malaysia voiceover variant for the MY all-hands and a Bahasa Indonesia variant for the ID all-hands."}
      ],
        DESC_CREATE,
        persona=[_PERSONA, _PERSONA, _PERSONA, _PERSONA]),
    ],
    personas=_PERSONAS,
    storyboard=[
      {
        'ex': 1, 'title': 'Frame the FY27 Strategic Question', 'titleID': 'Bingkai Pertanyaan Strategis FY27',
        'minutes': 18, 'mode': 'Show & Tell + Hands-on',
        'summary': 'Frame the MYR 2.8B FY27 free-capital choice and the 5-division portfolio question that the ExCo must answer before Investor Day; pull deep ASEAN-conglomerate benchmarks (Sime Darby, Astra International, Ayala, Genting) and governance precedents to anchor management credibility.',
        'summaryID': 'Bingkai pilihan modal-bebas FY27 senilai Rp 9,8 triliun dan pertanyaan portofolio 5 divisi yang harus dijawab ExCo sebelum Investor Day; tarik benchmark konglomerat ASEAN (Sime Darby, Astra, Ayala, Genting) dan preseden tata kelola untuk menopang kredibilitas manajemen.',
        'tasks': [
          {'n':'01','tool':'chat','verb':'1-page ExCo briefing on the FY27 capital choice','verbID':'Briefing ExCo 1 halaman atas pilihan modal FY27','mode':'show','label':'Copilot Chat'},
          {'n':'02','tool':'researcher','verb':'Critique ASEAN-conglomerate capital-allocation precedents','verbID':'Kritik preseden alokasi modal konglomerat ASEAN','mode':'show','label':'Critique'},
          {'n':'03','tool':'researcher','verb':'Multi-model debate on the 5-division portfolio question','verbID':'Debat multi-model atas pertanyaan portofolio 5 divisi','mode':'show','label':'Model Council'}
        ]
      },
      {
        'ex': 2, 'title': 'Quantify the Five-Division Outlook', 'titleID': 'Kuantifikasi Outlook 5 Divisi',
        'minutes': 22, 'mode': 'Hands-on',
        'summary': 'Refresh the 5-division scorecard, build the FY27 capital-allocation Monte Carlo (5 candidate uses × IRR Low/Mid/High), and synthesise the ExCo pack, KPI dashboard and risk heatmap into one decision narrative inside Notebook.',
        'summaryID': 'Refresh scorecard 5 divisi, bangun Monte Carlo alokasi modal FY27 (5 opsi × IRR Low/Mid/High), dan sintesakan ExCo pack, dashboard KPI dan risk heatmap menjadi satu narasi keputusan di Notebook.',
        'tasks': [
          {'n':'04','tool':'analyst','verb':'Variance + Monte Carlo capital-allocation analysis','verbID':'Analisis selisih + Monte Carlo alokasi modal','mode':'hands','label':'Analyst'},
          {'n':'05','tool':'excel','verb':'5-division scorecard refresh + capital-allocation ranking sheet','verbID':'Refresh scorecard 5 divisi + sheet ranking alokasi modal','mode':'hands','label':'Copilot in Excel'},
          {'n':'06','tool':'notebook','verb':'Cross-file ExCo synthesis (10 EXEC sources)','verbID':'Sintesa ExCo lintas-file (10 sumber EXEC)','mode':'hands','label':'Copilot Notebook'}
        ]
      },
      {
        'ex': 3, 'title': 'Communicate the Equity Story', 'titleID': 'Komunikasikan Equity Story',
        'minutes': 22, 'mode': 'Hands-on',
        'summary': 'Condense the 14-page Strategy Refresh memo to a 3-page board read, build the 12-slide ExCo + Investor Day deck in PowerPoint, and align the Q4 stakeholder email pack across board, regulator, employees and analysts in Outlook.',
        'summaryID': 'Padatkan memo Strategy Refresh 14 halaman menjadi 3 halaman untuk dewan, bangun deck ExCo + Investor Day 12 slide di PowerPoint, dan rapikan paket email Q4 untuk dewan, regulator, karyawan dan analis di Outlook.',
        'tasks': [
          {'n':'07','tool':'word','verb':'Strategy Refresh memo — 14p → 3p board read','verbID':'Memo Strategy Refresh — 14h → 3h untuk dewan','mode':'hands','label':'Copilot in Word'},
          {'n':'08','tool':'ppt','verb':'12-slide ExCo + Investor Day deck','verbID':'Deck ExCo + Investor Day 12 slide','mode':'hands','label':'Copilot in PowerPoint'},
          {'n':'09','tool':'outlook','verb':'Q4 stakeholder email pack (board / regulator / staff / analysts)','verbID':'Paket email Q4 (dewan / regulator / staf / analis)','mode':'hands','label':'Copilot in Outlook'}
        ]
      },
      {
        'ex': 4, 'title': 'Coordinate & Scale Decisions', 'titleID': 'Koordinasikan & Skalakan Keputusan',
        'minutes': 18, 'mode': 'Show & Tell',
        'summary': 'Convert the Q4 ExCo Teams Recap into formal minutes, delegate the parallel Investor Day prep package to Cowork (research, deck, FAQ, briefing notes), and stand up the Zava ExCo Heartbeat Agent in Microsoft 365 Copilot Chat to monitor 5-division KPIs and Group risks daily.',
        'summaryID': 'Konversi Teams Recap ExCo Q4 menjadi notulen formal, delegasikan paket prep Investor Day paralel ke Cowork (riset, deck, FAQ, briefing notes), dan bangun Zava ExCo Heartbeat Agent di Microsoft 365 Copilot Chat untuk memantau KPI 5 divisi dan risiko Group setiap hari.',
        'tasks': [
          {'n':'10','tool':'teams','verb':'ExCo Recap → Word minutes + decisions log','verbID':'Recap ExCo → Notulen Word + log keputusan','mode':'show','label':'Copilot in Teams'},
          {'n':'11','tool':'cowork','verb':'Autonomous Investor Day prep package','verbID':'Paket prep Investor Day otonom','mode':'show','label':'Cowork (Frontier)'},
          {'n':'12','tool':'builder','verb':'Zava ExCo Heartbeat Agent in Copilot Chat','verbID':'Zava ExCo Heartbeat Agent di Copilot Chat','mode':'show','label':'Agent Builder'}
        ]
      }
    ],
    geo='MY'
  ),
]

print(f"Departments 6 written: {len(DEPARTMENTS_6)} entries")
