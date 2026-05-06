window.HUB_DATA = {
  whatsNew: [
    {
      id: 'wn-researcher',
      title: '🔍 Researcher',
      badge: 'New in M365 Copilot',
      summary: 'Deep web + work graph synthesis. Ask Copilot to research any topic — competitors, regulations, market trends — and it grounds its answer in live web data and your org files.',
      tip: 'Try: \'Research the top 5 ESG regulations impacting ASEAN palm oil exporters in 2025.\'',
      license: 'M365_LIC'
    },
    {
      id: 'wn-analyst',
      title: '📊 Analyst',
      badge: 'New in M365 Copilot',
      summary: 'Upload Excel/CSV files and Copilot runs Python code to generate charts, regressions, waterfall analysis, and scenario models — right in your browser.',
      tip: 'Try: Upload any Zava Excel file and ask \'Create a waterfall chart showing EBITDA bridge by division.\'',
      license: 'M365_LIC'
    },
    {
      id: 'wn-cowork',
      title: '🤝 Cowork (Frontier)',
      badge: 'Frontier Program',
      summary: 'Autonomous multi-step agent at m365.cloud.microsoft > Agents > Cowork. Cowork can search the web, draft documents, send emails (with your confirmation), and manage calendars — end-to-end workflows.',
      tip: 'Start Cowork at m365.cloud.microsoft, click Agents, then Cowork. Requires Frontier program enrollment.',
      license: 'FRONTIER_LIC'
    },
    {
      id: 'wn-notebook',
      title: '📓 Copilot Notebook',
      badge: 'Available Now',
      summary: 'Multi-document synthesis hub. Paste or upload multiple documents, set a persistent Instruction, then ask questions across all of them — perfect for M&A due diligence, policy review, and report compilation.',
      tip: 'Try: Upload all 4 M&A target files + the evaluation framework, then ask Copilot to rank targets.',
      license: 'M365_LIC'
    },
    {
      id: 'wn-agents',
      title: '🏗 Agent Builder',
      badge: 'Copilot Studio',
      summary: 'Build custom Copilot agents trained on your own documents and policies — no code required. Deploy to Teams, SharePoint, or as a standalone chat agent for your employees.',
      tip: 'Go to copilotstudio.microsoft.com > Create > New Agent. Upload your policy documents and publish to Teams.',
      license: 'M365_LIC'
    }
  ],
  sectors: [
    {
      id: 'sec-banking',
      label: 'Banking',
      industries: [
        'ind-commercial-banking',
        'ind-islamic-banking',
        'ind-investment-banking'
      ]
    },
    {
      id: 'sec-insurance',
      label: 'Insurance',
      industries: [
        'ind-general-insurance',
        'ind-life-insurance',
        'ind-takaful'
      ]
    },
    {
      id: 'sec-fintech',
      label: 'Fintech',
      industries: [
        'ind-fintech'
      ]
    },
    {
      id: 'sec-healthcare',
      label: 'Healthcare',
      industries: [
        'ind-hospital',
        'ind-pharma'
      ]
    },
    {
      id: 'sec-og',
      label: 'Oil & Gas',
      industries: [
        'ind-og-upstream',
        'ind-og-downstream'
      ]
    },
    {
      id: 'sec-energy',
      label: 'Energy',
      industries: [
        'ind-renewable'
      ]
    },
    {
      id: 'sec-mfg',
      label: 'Manufacturing',
      industries: [
        'ind-industrial-mfg',
        'ind-construction'
      ]
    },
    {
      id: 'sec-agri',
      label: 'Agriculture',
      industries: [
        'ind-plantation'
      ]
    },
    {
      id: 'sec-bpo',
      label: 'BPO & Tech',
      industries: [
        'ind-bpo'
      ]
    },
    {
      id: 'sec-telco',
      label: 'Telco',
      industries: [
        'ind-telco'
      ]
    },
    {
      id: 'sec-congl',
      label: 'Conglomerate',
      industries: [
        'ind-conglomerate'
      ]
    },
    {
      id: 'sec-govt',
      label: 'Government',
      industries: [
        'ind-govt',
        'ind-regulator'
      ]
    },
    {
      id: 'sec-glc',
      label: 'GLC',
      industries: [
        'ind-glc'
      ]
    },
    {
      id: 'sec-re',
      label: 'Real Estate',
      industries: [
        'ind-property-reit'
      ]
    },
    {
      id: 'sec-logistics',
      label: 'Logistics',
      industries: [
        'ind-logistics'
      ]
    },
    {
      id: 'sec-aviation',
      label: 'Aviation',
      industries: [
        'ind-aviation'
      ]
    },
    {
      id: 'sec-mining',
      label: 'Mining',
      industries: [
        'ind-coal-mining'
      ]
    },
    {
      id: 'sec-retail',
      label: 'Retail',
      industries: [
        'ind-retail-grocery'
      ]
    },
    {
      id: 'sec-hospitality',
      label: 'Hospitality',
      industries: [
        'ind-hotel'
      ]
    },
    {
      id: 'sec-media',
      label: 'Media',
      industries: [
        'ind-media'
      ]
    },
    {
      id: 'sec-general',
      label: 'General',
      industries: [
        'ind-general'
      ]
    }
  ],
  industries: [
    {
      id: 'general',
      sectorId: 'general',
      subsector: '',
      name: '⭐ General (Any Role)',
      icon: '⭐',
      color: '#FF6B35',
      accent: '#FF8C42',
      company: 'Your Organisation',
      tagline: 'A universal demo set — works for any industry, any role.',
      scenario: 'These scenarios work for any organisation and any seniority level. No prior context needed — just open Copilot and follow the prompts. Perfect as a warm-up before industry-specific demos.',
      files: [
        '01_Zava_Group_Financial_Performance.xlsx',
        '02_Zava_Group_Policy_Handbook.docx',
        '03_Zava_Group_Strategy_Framework.docx'
      ],
      prompts: [
        {
          tool: '🤖 Copilot Chat (Basic)',
          license: 'Free — no M365 Copilot license needed',
          account: 'Sasha Ouellet — SashaO@ABSx62256373.OnMicrosoft.com',
          desc: '',
          prompts: [
            'I have a performance review meeting in two days and I need to articulate the impact of my last six months of work clearly. My key achievements include leading a cross-functional project that cut procurement cycle time by 22%, coaching two junior team members who both received "exceeds expectations" ratings, and resolving a long-standing vendor dispute that had been escalating for months. Draft a concise self-assessment narrative of around 300 words that connects these achievements to the team\'s broader goals, uses active language, and ends with a forward-looking statement about my priorities for the next half-year. Avoid generic phrases like "team player" — keep it specific and confident.',
            'My manager just asked me to prepare a 5-minute briefing for the leadership team on why our department should pilot Microsoft 365 Copilot before the company-wide rollout. I need to make a compelling, evidence-based case without it sounding like a vendor pitch. Draft talking points covering: what Copilot does in plain language, two concrete use cases relevant to a finance or operations team, estimated time savings based on published Microsoft research, and how we would measure success in a 30-day pilot. Keep each talking point under 40 words so I can deliver it naturally without reading from a script.',
            'Explain the difference between Copilot Chat, Microsoft 365 Copilot, and Copilot Studio in plain language — as if you were explaining to a department head who has heard the terms but is confused about what each one does and which licence they need. Use a simple analogy and end with a one-sentence recommendation on which to start with for a team of 50 knowledge workers who primarily use Outlook, Word, and Excel.'
          ]
        },
        {
          tool: '🔍 Researcher',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via Microsoft 365 Copilot Chat (copilot.microsoft.com or Teams) > click Agents > Researcher. Grounds answers in live web sources and your organisation data with full citations.',
          prompts: [
            'Research how Fortune 500 companies are measuring the ROI of Microsoft 365 Copilot deployments in 2025 and 2026. I need specific data points: average hours saved per user per week, cost-per-seat payback periods, and which job functions report the highest productivity gains. Summarise findings in a structured format with source citations so I can use this in an executive briefing next week.',
            'What are the top five AI governance and responsible AI frameworks that enterprises in Southeast Asia are adopting in 2025? For each framework, identify who publishes it, what its core principles are, and whether it has any regulatory backing in Malaysia or Indonesia. Present as a comparison table.'
          ]
        },
        {
          tool: '📊 Analyst',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via Microsoft 365 Copilot Chat > click Agents > Analyst. Upload an Excel or CSV file. Analyst runs Python-style analysis, builds charts, and interprets results without you writing a single formula.',
          prompts: [
            'Upload 01_Zava_Group_Financial_Performance.xlsx to Analyst. Then ask: Analyse the revenue and EBITDA trends across all 11 divisions from FY2022 to FY2025. Which three divisions have shown the steepest decline in EBITDA margin? Calculate the year-on-year change in margin for each and rank them from worst to best. Create a bar chart showing EBITDA margin by division for FY2024 vs FY2025, and flag any division where margin has dropped more than 5 percentage points in a single year.',
            'Upload 01_Zava_Group_Financial_Performance.xlsx and ask: Perform a variance analysis between the FY2025 budget and actuals for each division. Calculate both the absolute variance in MYR millions and the percentage variance. Identify the top three divisions with the largest unfavourable variances and suggest two plausible business reasons for each based on the data patterns visible in the file. Output as a table ranked by absolute variance, largest first.'
          ]
        },
        {
          tool: '📊 Copilot in Excel',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open 01_Zava_Group_Financial_Performance.xlsx. Navigate to the Group Summary sheet. Ask Copilot: Create a formula that calculates the compound annual growth rate (CAGR) of total group revenue from FY2022 to FY2025, then apply the same formula across each division row. Add a conditional formatting rule that highlights any division with a CAGR below 3% in red and above 8% in green.',
            'In the same workbook, ask Copilot: Add a new sheet called "FY2026 Forecast" that projects each division\'s revenue using linear trend extrapolation from the FY2022–FY2025 data. Include a column showing the assumed growth rate and a column showing the 90% confidence interval range. Format all currency cells in MYR millions with 1 decimal place.',
            'Ask Copilot in Excel: Identify any cells in this workbook that contain hard-coded numbers where a formula would be more appropriate, and list them with the sheet name and cell reference. Also flag any formula inconsistencies where a formula in a row differs from the pattern used in adjacent rows.'
          ]
        },
        {
          tool: '📝 Copilot in Word',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open 02_Zava_Group_Policy_Handbook.docx. Ask Copilot: Summarise this policy handbook into a one-page executive briefing covering the five most critical compliance obligations, the three highest-risk policy areas, and the escalation path for a potential breach. Format as a briefing memo addressed to the Group CEO, with a "Key Actions Required" section at the end.',
            'In the same document, ask Copilot: Identify all sections that reference regulatory bodies or government agencies. List each reference with the section number, the regulatory body named, and the specific obligation it relates to. Present as a structured table with three columns: Section | Regulatory Body | Obligation Summary.',
            'Ask Copilot to draft a new section for the policy handbook titled "Artificial Intelligence Acceptable Use Policy" covering: permitted uses of AI tools in the workplace, data classification rules (what can and cannot be uploaded to AI tools), employee responsibilities, and the approval process for deploying AI in a business process. Keep it under 600 words, use the same formal tone as the existing document, and flag where legal review is recommended.'
          ]
        },
        {
          tool: '🎯 Copilot in PowerPoint',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Ask Copilot in PowerPoint: Create a 10-slide presentation titled "Microsoft 365 Copilot — Productivity Unlocked" for a C-suite audience. Include: an executive summary of what Copilot does, a slide on business impact with three metrics (time saved, cost avoidance, employee satisfaction), a demo flow slide showing which tools to show first, a change management slide, and a recommended 90-day rollout roadmap. Use a professional blue and white colour scheme.',
            'Open any existing strategy presentation. Ask Copilot: Redesign this presentation so each slide follows a "Situation — Complication — Resolution" narrative structure. Rewrite the speaker notes for each slide to be a 30-second verbal script. Flag any slide that is currently text-heavy and suggest a chart or visual to replace it.',
            'Ask Copilot: Add a new slide titled "AI Governance Principles" to this presentation. The slide should show five principles as icons with one-line descriptions: Responsible, Secure, Transparent, Inclusive, and Accountable. Use the existing slide template and colour palette.'
          ]
        },
        {
          tool: '📧 Copilot in Outlook',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open Outlook and find the most recent email thread about a project update or budget review. Ask Copilot: Summarise this thread, identify all open action items with the name of the person responsible, and draft a follow-up email to all participants listing the actions, owners, and a proposed deadline of end of this week. Keep the tone professional but direct.',
            'Ask Copilot in Outlook: Draft a meeting request email to three senior stakeholders requesting a 45-minute strategy alignment session. The email should explain the purpose (reviewing Q2 performance against FY2026 targets), the proposed agenda in three bullet points, and ask them to confirm availability for one of three time slots next week. Keep it concise — under 150 words.',
            'Ask Copilot: Coach me on this email before I send it. Check the tone, identify anything that could be misinterpreted, suggest a stronger subject line, and recommend whether I should copy or blind-copy anyone based on the content. Show your suggestions as tracked changes.'
          ]
        },
        {
          tool: '🎙 Copilot in Teams',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Use your OWN existing recorded Teams meetings. Open a meeting recap in Teams > Recap tab. Copilot generates summaries, action items, and follow-up drafts grounded in the actual transcript.',
          prompts: [
            'Open an existing recorded Teams meeting recap. Ask Copilot: Generate a full meeting summary with four sections: Key Decisions Made, Open Action Items (with owner and due date), Topics That Need Follow-Up, and a one-paragraph executive summary I can paste into an email to stakeholders who did not attend.',
            'In the same recap, ask Copilot: Draft a follow-up email to all meeting participants. The email should thank them for attending, list all action items with owners and deadlines, note any decisions that require sign-off from absent stakeholders, and propose a date for the next check-in in two weeks.',
            'Ask Copilot in the Teams recap: Which discussion points from this meeting are still unresolved? For each unresolved item, identify who raised it, what the proposed next step was, and whether a decision was reached or deferred. Present as a table: Topic | Raised By | Status | Next Step.'
          ]
        },
        {
          tool: '📓 Copilot Notebook',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via copilot.microsoft.com > Notebook tab. Upload up to 5 files and set a system instruction. Best for synthesising insights across multiple documents simultaneously.',
          prompts: [
            'Upload 02_Zava_Group_Policy_Handbook.docx and 03_Zava_Group_Strategy_Framework.docx to Copilot Notebook. Set this system instruction: "You are a senior strategy advisor. Answer questions by synthesising insights from both documents — always cite which document your answer draws from." Then ask: Where do the strategic priorities in the strategy framework conflict with or create compliance obligations under the policy handbook? List the top three tensions and suggest how leadership might resolve each.',
            'Upload 01_Zava_Group_Financial_Performance.xlsx and 03_Zava_Group_Strategy_Framework.docx to Notebook. Ask: Based on the actual financial performance data and the stated strategic objectives, which strategic priorities appear to be underfunded given current revenue allocation? Rank by gap size and suggest which two should be accelerated and which one should be deferred.'
          ]
        },
        {
          tool: '🤝 Cowork (Frontier)',
          license: 'M365 Copilot + Frontier Program',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Cowork is an autonomous agent that takes actions across Microsoft 365 on your behalf — sending emails, scheduling meetings, creating documents, posting in Teams, and scheduling recurring tasks. Access: m365.cloud.microsoft > left nav > Agents > Cowork. Requires Frontier program enrollment.',
          prompts: [
            'Do all of the following autonomously: (1) Research the latest Microsoft 365 Copilot adoption statistics and productivity benchmarks published in 2025 or 2026. (2) Draft a two-page Word document titled "Copilot Business Case — Internal Briefing" summarising the research with three key data points, two customer case studies, and a recommended adoption approach. (3) Save the document to my OneDrive. (4) Send an email to my manager with the document attached, subject line "Copilot Business Case — Ready for Review", asking for feedback by end of week. (5) Schedule a 30-minute Teams meeting with my manager for next Tuesday at 10am titled "Copilot Business Case Review".',
            'Do all of the following: (1) Check my calendar for any meetings this week that do not have an agenda attached. (2) For each such meeting, draft a short agenda based on the meeting title and attendees. (3) Send each agenda as a reply to the original meeting invitation. (4) Create a recurring Teams meeting every Monday at 9am titled "Weekly Copilot Adoption Check-In" for the next 8 weeks and invite my manager.'
          ]
        },
        {
          tool: '🤖 Word Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to a Word document. Open the .docx in Word for Web > Copilot pane > + New Agent > name it, write a description, set the document as knowledge source > Share. Colleagues chat with it in Teams or M365 Copilot.',
          prompts: [
            'Open 02_Zava_Group_Policy_Handbook.docx in Word for Web. In the Copilot pane, click + New Agent. Name it "Group Policy Assistant". Description: "Answers employee questions about Zava Group\'s internal policies, compliance obligations, and escalation procedures based on the official policy handbook." Set the document as the knowledge source. Copy the share link and send it to your HR team so employees can chat with it from Teams.',
            'Demo the agent: Open a new Teams chat or M365 Copilot session and ask the Policy Assistant: "What is the escalation process if I suspect a colleague is violating our anti-bribery policy? Who do I contact and what documentation do I need to prepare?" Show how the agent answers with specific references to the policy sections.'
          ]
        },
        {
          tool: '🤖 PowerPoint Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to a PowerPoint presentation. Great for strategy decks or Board presentations many people need to reference. Same setup as Word Agent but using a .pptx file.',
          prompts: [
            'Open 03_Zava_Group_Strategy_Framework.docx or a strategy presentation in PowerPoint for Web. Create a new agent called "Strategy Deck Assistant". Description: "Helps leadership and strategy teams quickly find information from the group strategy framework, including KPIs, initiative owners, and investment priorities." Set the file as knowledge source and share with the strategy team.',
            'Demo query: Ask the Strategy Deck Assistant in Teams: "Which strategic initiative has the highest investment priority for FY2026, and who is the executive sponsor?" Then ask: "What are the three key risks flagged for the ASEAN expansion workstream?" Show how it pulls answers directly from the deck without requiring anyone to open the file.'
          ]
        },
        {
          tool: '🤖 Excel Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to an Excel workbook. Colleagues ask data questions in plain English without opening Excel. Open .xlsx in Excel for Web > Copilot pane > + New Agent > set workbook as knowledge source > share.',
          prompts: [
            'Open 01_Zava_Group_Financial_Performance.xlsx in Excel for Web. In the Copilot pane, click + New Agent. Name it "Group Financials Q&A". Description: "Answers questions about Zava Group\'s divisional revenue, EBITDA, and budget performance using the latest financial data workbook." Set the workbook as knowledge source and share with finance leaders.',
            'Demo query: Ask the Group Financials Q&A agent: "Which three divisions missed their FY2025 EBITDA target and by how much in MYR millions?" Then ask: "What was the group-level revenue growth rate from FY2024 to FY2025?" Show how non-finance colleagues get instant answers without needing to navigate the workbook.'
          ]
        },
        {
          tool: '🏗 Agent Builder (Copilot Studio)',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Build a custom declarative agent in Copilot Studio — no coding required. Access: copilotstudio.microsoft.com > Create > New Agent. Add name, description, knowledge sources (SharePoint URLs or uploaded files), topics/actions. Publish to Teams in under 10 minutes.',
          prompts: [
            'Go to copilotstudio.microsoft.com > Create > New Agent. Name the agent "Zava Knowledge Hub". Description: "A company-wide AI assistant that answers questions about group policies, strategy, and financial performance, drawing from official Zava Group documents." Under Knowledge, upload 01_Zava_Group_Financial_Performance.xlsx, 02_Zava_Group_Policy_Handbook.docx, and 03_Zava_Group_Strategy_Framework.docx. Under Topics, add a welcome topic that greets users and explains what the agent can help with. Click Publish > Microsoft Teams. Within 10 minutes the agent appears in Teams for all authorised users.',
            'Demo the published agent in Teams: Open the Zava Knowledge Hub bot and ask: "What is the group\'s FY2026 revenue target and which divisions are expected to contribute the most growth?" Then ask: "Is there a policy covering the use of AI tools in client-facing communications?" Show how the agent synthesises answers from multiple source documents and cites them.'
          ]
        }
      ]
    },
    {
      id: 'commercial-banking',
      sectorId: 'banking-fs',
      subsector: '',
      name: 'Commercial Banking',
      icon: '🏦',
      color: '#0D47A1',
      accent: '#1976D2',
      company: 'Meridian Bank Berhad',
      tagline: 'NPL at 14.2% — 4x BNM\'s supervisory threshold. Bilateral review in 3 days.',
      scenario: 'Meridian Bank Berhad is Malaysia\'s fifth-largest commercial bank by assets (MYR 68.4B). Personal Financing NPL has climbed for 6 consecutive quarters, reaching 14.2% — four times BNM\'s 3.5% supervisory threshold. The CFO goes into a BNM bilateral review on Tuesday. Provision coverage sits at 68%, well below the internal 80% target.',
      files: [
        'BNK_01_Meridian_Bank.xlsx',
        'BNK_02_Meridian_Bank_Strategy.docx',
        'Email_01_Zava_Bank_NPL_Thread.docx',
        'Email_06_BNM_Regulatory_Correspondence.docx'
      ],
      prompts: [
        {
          tool: '🤖 Copilot Chat (Basic)',
          license: 'Free — no M365 Copilot license needed',
          account: 'Sasha Ouellet — SashaO@ABSx62256373.OnMicrosoft.com',
          desc: '',
          prompts: [
            'I am the CFO of a Malaysian commercial bank. Our Personal Financing NPL ratio has climbed from 8.2% to 14.2% over six quarters and I have a BNM bilateral review in three days. Draft a one-page internal briefing note for my Board Risk Committee explaining the NPL situation in plain language: what drove the deterioration, what remediation actions we have taken so far, and what we expect BNM to ask. Keep the tone calm and factual — this is not a crisis communication, it is a preparatory briefing.',
            'Explain the difference between gross NPL ratio, net NPL ratio, and provision coverage ratio in the context of Malaysian banking regulation. Use simple language suitable for a Board director who has a finance background but is not a banking specialist. Include a worked numerical example using approximate figures.',
            'What are BNM\'s standard remediation requirements when a bank\'s NPL ratio exceeds its supervisory threshold? List the typical regulatory actions BNM may impose, from supervisory letters through to more formal interventions, and indicate the approximate timelines involved.'
          ]
        },
        {
          tool: '🔍 Researcher',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via Microsoft 365 Copilot Chat (copilot.microsoft.com or Teams) > click Agents > Researcher. Grounds answers in live web sources and your organisation data with full citations.',
          prompts: [
            'Research how Malaysian commercial banks have managed NPL surges in the past five years, particularly post-moratorium periods. I need: (1) Industry-average NPL ratios for Malaysian banks in 2023–2025, (2) The three most common remediation strategies banks used successfully, (3) Any BNM guidance circulars on NPL management issued since 2023. Cite all sources so I can share this with our credit risk team.',
            'Research global best practices for bank NPL resolution programmes, particularly in markets with similar profile to Malaysia — emerging markets with retail-heavy loan books. Identify two or three banks that successfully reduced NPL ratios by more than 4 percentage points within 18 months and summarise their approach. Present findings as a structured brief with source links.'
          ]
        },
        {
          tool: '📊 Analyst',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via Microsoft 365 Copilot Chat > click Agents > Analyst. Upload an Excel or CSV file. Analyst runs Python-style analysis, builds charts, and interprets results without you writing a single formula.',
          prompts: [
            'Upload BNK_01_Meridian_Bank.xlsx to Analyst. Ask: Analyse the NPL trend across all loan product segments from Q1 FY2023 to Q4 FY2025. Which three product segments are driving the highest NPL increase in absolute MYR terms? Calculate the required provision top-up to reach 80% provision coverage for each segment and show the cumulative impact on pre-tax profit. Present as a ranked table: Segment | Current NPL (MYR M) | Coverage Gap | Provision Top-Up Required | Pre-Tax Profit Impact.',
            'Upload BNK_01_Meridian_Bank.xlsx. Ask Analyst: Build a scatter plot showing the relationship between loan vintage (year of origination) and default rate across all Personal Financing accounts. Identify whether there is a specific origination cohort that is disproportionately contributing to the NPL problem. If a pattern exists, calculate what percentage of total NPL would be resolved by writing off or restructuring that cohort alone.'
          ]
        },
        {
          tool: '📊 Copilot in Excel',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open BNK_01_Meridian_Bank.xlsx and navigate to the Loan Portfolio sheet. Ask Copilot: Our Personal Financing NPL ratio has climbed from 8.2% in Q1 FY2023 to 14.2% in Q4 FY2025, now 4x BNM\'s supervisory threshold of 3.5%. Analyse the quarterly deterioration trend across all product segments, identify the three sub-segments contributing most to the NPL increase, calculate the additional loan loss provision required to reach 80% provision coverage, and show the resulting impact on pre-tax profit. Present as a 4-column table: Segment | NPL Rate | Provision Shortfall (MYR M) | Recommended Action.',
            'Ask Copilot in Excel: Create a dynamic NPL stress-test model on a new sheet called "Stress Test". Assume three scenarios — Base (NPL stays at 14.2%), Moderate (NPL rises to 18%), Severe (NPL rises to 22%). For each scenario, calculate the required provision, the impact on Tier 1 capital ratio, and the regulatory capital buffer remaining above BNM\'s 10.5% minimum. Flag in red any scenario where the buffer falls below 1%.',
            'Ask Copilot: Add a rolling 4-quarter average NPL ratio column next to each product segment row. Then add conditional formatting to flag any segment where the most recent quarter\'s NPL exceeds the 4Q average by more than 2 percentage points — these are the fast-deteriorating segments that need immediate escalation.',
            'Ask Copilot: Summarise the key risk metrics on the Risk Dashboard sheet into a plain-language paragraph I can paste into the Board pack. Highlight the three metrics that are outside tolerance thresholds and suggest a one-sentence action for each.'
          ]
        },
        {
          tool: '📝 Copilot in Word',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open BNK_02_Meridian_Bank_Strategy.docx. Ask Copilot: Draft a 2-page credit risk remediation plan for BNM submission. Structure it as: (1) Executive Summary — current NPL position and root causes, (2) Remediation Actions — three concrete steps with timelines, (3) Governance — who owns each action and how progress will be reported, (4) Milestones — what BNM should expect to see at 30, 60, and 90 days. Use a formal regulatory tone throughout.',
            'Ask Copilot in Word: Identify all sections in this strategy document that reference credit risk or lending standards. For each section, summarise in one sentence whether the current strategy is consistent with remediation of the NPL problem or whether it may be contributing to it. Present as a gap analysis table.',
            'Ask Copilot: Rewrite the Executive Summary of this document to reflect the current NPL crisis. The new summary should open with the most critical issue, acknowledge the BNM bilateral review, and end with a clear statement of the bank\'s commitment to reaching 80% provision coverage within 6 months. Keep it under 200 words.'
          ]
        },
        {
          tool: '🎯 Copilot in PowerPoint',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Ask Copilot in PowerPoint: Create a 12-slide Board presentation titled "NPL Remediation Programme — Q4 FY2025 Update" for Meridian Bank. Slides should cover: (1) NPL dashboard — current vs threshold, (2) Root cause analysis, (3) Segment breakdown — top 3 contributors, (4) Provision coverage gap analysis, (5) Remediation plan — 3 initiatives, (6) Timeline and milestones, (7) Capital adequacy impact, (8) BNM engagement strategy, (9) Risk appetite reset, (10) Next steps. Use a professional dark-blue colour scheme.',
            'Ask Copilot: For each slide in this presentation, generate speaker notes that are a 45-second verbal script. The CFO delivering this has 20 years of banking experience, so avoid over-explaining basics — focus the notes on pre-empting the questions Board members are most likely to ask.',
            'Ask Copilot: Add a "Key Risks" slide after slide 8 that shows five risks to the remediation plan in a 2×2 risk matrix (likelihood vs impact), with one-line mitigants for each risk.'
          ]
        },
        {
          tool: '📧 Copilot in Outlook',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open Email_06_BNM_Regulatory_Correspondence.docx and review the thread. Open Outlook and ask Copilot: Draft a formal response to BNM\'s latest query. Acknowledge their concerns about the NPL trajectory, outline the three immediate remediation steps we have initiated, confirm the timeline for our next progress report, and request a 30-minute call with the BNM supervision team to discuss the bilateral review agenda. Use the formal salutation style appropriate for BNM correspondence.',
            'Open Email_01_Zava_Bank_NPL_Thread.docx. Ask Copilot in Outlook: Summarise this internal email thread, identify all commitments made by the credit risk team, and draft a follow-up email to the Chief Credit Officer asking for a status update on each commitment before the BNM meeting on Tuesday. List the commitments as numbered bullet points in the email body.',
            'Ask Copilot: Draft an all-staff email from the CEO to branch managers and relationship managers explaining the NPL situation without causing alarm. The email should acknowledge the challenge, explain what the bank is doing about it, and give clear guidance on what relationship managers should and should not say to customers who ask about loan restructuring options. Keep it under 300 words.'
          ]
        },
        {
          tool: '🎙 Copilot in Teams',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Use your OWN existing recorded Teams meetings. Open a meeting recap in Teams > Recap tab. Copilot generates summaries, action items, and follow-up drafts grounded in the actual transcript.',
          prompts: [
            'Open an existing recorded Teams meeting recap from a credit or risk committee meeting. Ask Copilot: Generate a structured recap covering: (1) Key credit risk metrics reviewed, (2) Decisions made on provisioning or remediation, (3) Action items with owners and due dates, (4) Any escalation items that need Board or BNM notification. Format for distribution to the Risk Committee.',
            'In the same meeting recap, ask Copilot: Draft a follow-up email to all Risk Committee members. The email should list all action items with owner names and deadlines, note any decisions that require CFO or Board sign-off, and propose the next Risk Committee meeting date.',
            'Ask Copilot in Teams: Based on this meeting transcript, identify any statements made about NPL targets or remediation timelines that could be interpreted as commitments to BNM. List each statement with the speaker name and timestamp so the legal team can review before the bilateral meeting.'
          ]
        },
        {
          tool: '📓 Copilot Notebook',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via copilot.microsoft.com > Notebook tab. Upload up to 5 files and set a system instruction. Best for synthesising insights across multiple documents simultaneously.',
          prompts: [
            'Upload BNK_01_Meridian_Bank.xlsx, BNK_02_Meridian_Bank_Strategy.docx, and Email_06_BNM_Regulatory_Correspondence.docx to Copilot Notebook. Set this instruction: "You are a senior banking regulator advisor preparing the CFO for a BNM bilateral review." Ask: Based on the NPL data, our strategy document, and the BNM correspondence, what are the five most likely questions BNM will ask on Tuesday? For each question, draft a concise, factually grounded answer the CFO can use.',
            'Upload BNK_01_Meridian_Bank.xlsx and Email_01_Zava_Bank_NPL_Thread.docx. Ask: Cross-reference the NPL figures in the data file against the commitments made in the internal email thread. Are there any discrepancies between what was promised internally and what the data shows has actually happened? List any gaps the CFO should be aware of before the BNM meeting.'
          ]
        },
        {
          tool: '🤝 Cowork (Frontier)',
          license: 'M365 Copilot + Frontier Program',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Cowork is an autonomous agent that takes actions across Microsoft 365 on your behalf — sending emails, scheduling meetings, creating documents, posting in Teams, and scheduling recurring tasks. Access: m365.cloud.microsoft > left nav > Agents > Cowork. Requires Frontier program enrollment.',
          prompts: [
            'Do all of the following: (1) Research the latest BNM guidelines on NPL classification and provisioning requirements published in 2024 or 2025. (2) Draft a 3-page internal compliance brief summarising the key requirements and how Meridian Bank\'s current provisioning compares. (3) Save it as "BNM NPL Compliance Brief - [Today\'s Date]" in OneDrive. (4) Email it to the Chief Risk Officer and Chief Credit Officer with subject "BNM NPL Compliance Brief — Please review before Tuesday" asking for feedback by Monday 5pm. (5) Schedule a 1-hour prep meeting titled "BNM Bilateral Review Prep" for Monday 2pm and invite the CFO, CRO, and CCO.',
            'Do all of the following: (1) Check the calendar for any outstanding action items from the last Risk Committee meeting. (2) For each action item that is overdue, send a polite follow-up email to the owner asking for a status update by end of day. (3) Create a Word document listing all overdue items with owner names and original due dates. (4) Post a summary in the #risk-committee Teams channel: "Reminder: 3 action items from our last meeting are overdue — please update by COB today." (5) Set a recurring weekly reminder in my calendar titled "Risk Action Item Review" every Friday at 4pm for 12 weeks.'
          ]
        },
        {
          tool: '🤖 Word Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to a Word document. Open the .docx in Word for Web > Copilot pane > + New Agent > name it, write a description, set the document as knowledge source > Share. Colleagues chat with it in Teams or M365 Copilot.',
          prompts: [
            'Open BNK_02_Meridian_Bank_Strategy.docx in Word for Web. Create a new agent called "Credit Strategy Assistant" with description: "Answers questions from credit and risk officers about Meridian Bank\'s credit risk strategy, NPL remediation plan, and lending standards." Set the document as knowledge source. Share with the credit risk team and branch network compliance officers.',
            'Demo query: Ask the Credit Strategy Assistant in Teams: "What is the approved remediation approach for Personal Financing accounts that have been in arrears for more than 90 days? What restructuring options am I authorised to offer before escalating to the Credit Committee?" Show how the agent pulls the answer directly from the strategy document.'
          ]
        },
        {
          tool: '🤖 PowerPoint Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to a PowerPoint presentation. Great for strategy decks or Board presentations many people need to reference. Same setup as Word Agent but using a .pptx file.',
          prompts: [
            'Create a PowerPoint presentation summarising the NPL remediation programme slides, then open it in PowerPoint for Web. Create an agent called "NPL Remediation Briefing Bot". Description: "Provides instant answers about Meridian Bank\'s NPL remediation programme, targets, and milestones for board members and senior management." Share with Board members so they can review without needing to open the full deck.',
            'Demo: Ask the agent "What is our target NPL ratio at the end of Q2 FY2026 and what are the three key actions driving that target?" Then ask: "What happens to our Tier 1 capital ratio in the severe stress scenario?" Show how Board members get precise answers without navigating through slides.'
          ]
        },
        {
          tool: '🤖 Excel Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to an Excel workbook. Colleagues ask data questions in plain English without opening Excel. Open .xlsx in Excel for Web > Copilot pane > + New Agent > set workbook as knowledge source > share.',
          prompts: [
            'Open BNK_01_Meridian_Bank.xlsx in Excel for Web. Create an agent called "Meridian Loan Portfolio Q&A". Description: "Answers questions about Meridian Bank\'s loan portfolio, NPL ratios, provision coverage, and segment breakdowns using live workbook data." Share with senior credit officers who need quick data access without navigating the full workbook.',
            'Demo: Ask the agent "What is the current NPL ratio for the SME segment and how does it compare to the industry average?" Then ask: "Which loan product has the highest rate of deterioration over the last four quarters?" Show how credit managers get instant, data-grounded answers.'
          ]
        },
        {
          tool: '🏗 Agent Builder (Copilot Studio)',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Build a custom declarative agent in Copilot Studio — no coding required. Access: copilotstudio.microsoft.com > Create > New Agent. Add name, description, knowledge sources (SharePoint URLs or uploaded files), topics/actions. Publish to Teams in under 10 minutes.',
          prompts: [
            'Go to copilotstudio.microsoft.com > Create > New Agent. Name it "Meridian Credit Risk Assistant". Description: "A regulatory-ready AI assistant for Meridian Bank\'s credit and risk teams — answers questions about NPL positions, remediation plans, BNM requirements, and lending policies using official bank documents." Upload BNK_01_Meridian_Bank.xlsx, BNK_02_Meridian_Bank_Strategy.docx, and Email_06_BNM_Regulatory_Correspondence.docx as knowledge sources. Add a starter topic: "Explain our current NPL situation and remediation plan." Publish to Teams for the Risk and Credit divisions.',
            'Demo the agent in Teams. Ask it: "We have a customer requesting a third loan restructuring on their Personal Financing account. What is our policy and what approval level is required?" Then ask: "What NPL ratio target has the Board approved for end of FY2026 and what are the consequences if we miss it?" Show how the agent gives consistent, document-grounded answers that reduce compliance risk from inconsistent verbal guidance.'
          ]
        }
      ]
    },
    {
      id: 'islamic-banking',
      sectorId: 'banking-fs',
      subsector: '',
      name: 'Islamic Banking',
      icon: '🕌',
      color: '#1A237E',
      accent: '#283593',
      company: 'Al-Amanah Islamic Bank Malaysia',
      tagline: 'MYR 3.5B Sukuk issuance pending — BNM IFSA compliance review in 4 weeks.',
      scenario: 'Al-Amanah Islamic Bank Malaysia (AIBM) has MYR 22.1B in total financing assets. A landmark MYR 3.5B Sukuk Wakalah issuance is pending regulatory approval. The BNM IFSA compliance review is scheduled in 4 weeks and the Shariah Committee has flagged two products for re-structuring. Profit rate risk is rising as OPR hovers at 3.0%.',
      files: [
        'BNK_01_Meridian_Bank.xlsx',
        'BNK_02_Meridian_Bank_Strategy.docx'
      ],
      prompts: [
        {
          tool: '🤖 Copilot Chat (Basic)',
          license: 'Free — no M365 Copilot license needed',
          account: 'Sasha Ouellet — SashaO@ABSx62256373.OnMicrosoft.com',
          desc: '',
          prompts: [
            'Explain the key differences between a conventional bank loan and Islamic financing products such as Murabahah, Ijarah, and Musharakah Mutanaqisah — in plain language suitable for a retail customer who has only ever had a conventional mortgage. Focus on how the profit rate is determined, who owns the asset, and what happens in the event of default.',
            'What are the key disclosure requirements under BNM\'s IFSA 2013 (Islamic Financial Services Act) for a Sukuk Wakalah issuance? List the five most critical compliance obligations and the approval timeline from application to issuance. Include the role of the Shariah Advisory Council in the approval process.',
            'Draft a one-paragraph explanation of profit rate risk in Islamic banking that I can use in our annual report. The paragraph should explain the concept, why it differs from interest rate risk in conventional banking, and how we manage it through our Asset and Liability Management framework. Keep it under 150 words and avoid overly technical language.'
          ]
        },
        {
          tool: '🔍 Researcher',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via Microsoft 365 Copilot Chat (copilot.microsoft.com or Teams) > click Agents > Researcher. Grounds answers in live web sources and your organisation data with full citations.',
          prompts: [
            'Research the global Sukuk market outlook for 2025 and 2026 — specifically for Malaysia. I need: (1) Total Sukuk issuance volumes in Malaysia for 2024 and the forecast for 2025, (2) Demand trends from Middle Eastern and Southeast Asian investors, (3) Any new BNM or SC guidelines affecting Sukuk Wakalah structures issued in the past 12 months. Provide source citations for each data point.',
            'Research how Islamic banks in Malaysia are managing profit rate risk in a rising OPR environment. Identify the top three strategies used by leading Islamic banks (Maybank Islamic, CIMB Islamic, Bank Islam) and compare their approaches. Summarise in a briefing note format suitable for the ALCO (Asset and Liability Committee).'
          ]
        },
        {
          tool: '📊 Analyst',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via Microsoft 365 Copilot Chat > click Agents > Analyst. Upload an Excel or CSV file. Analyst runs Python-style analysis, builds charts, and interprets results without you writing a single formula.',
          prompts: [
            'Upload BNK_01_Meridian_Bank.xlsx. Ask Analyst: Analyse the financing asset breakdown by product type (Murabahah, Ijarah, Musharakah, etc.) and calculate the concentration risk — what percentage of total financing is in the top 3 product categories. Create a pie chart showing product mix and a trend chart showing how the mix has shifted over the past 8 quarters. Flag any product category where growth has exceeded 15% quarter-on-quarter.',
            'Upload BNK_01_Meridian_Bank.xlsx. Ask: Perform a sensitivity analysis on profit income assuming OPR changes of -50bps, flat, +50bps, and +100bps. For each scenario, calculate the impact on Net Financing Income (NFI) in MYR millions and the resulting NFI margin. Present as a 4-scenario sensitivity table with a colour-coded heat map — red for scenarios where NFI margin falls below 2.5%.'
          ]
        },
        {
          tool: '📊 Copilot in Excel',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open BNK_01_Meridian_Bank.xlsx and navigate to the Financing Portfolio sheet. Ask Copilot: Create a Shariah compliance monitoring dashboard on a new sheet called "Shariah Dashboard". It should show: (1) Each product type and its Shariah contract structure, (2) The profit rate benchmark used (COF + spread), (3) Any product where the actual rate charged deviates from the approved structure by more than 10bps — flag these in red.',
            'Ask Copilot: Build a Sukuk issuance impact model on a new sheet. Assume a MYR 3.5B Sukuk Wakalah at 4.2% profit rate for 5 years. Calculate: (1) Annual profit distribution to Sukukholders, (2) Impact on the bank\'s liquidity coverage ratio (LCR), (3) Impact on the net stable funding ratio (NSFR), (4) Breakeven period assuming proceeds are deployed into Murabahah financing at 6.8% profit rate.',
            'Ask Copilot: In the financing data, identify all accounts where the financing-to-value (FTV) ratio has exceeded 90% and the account is classified as Stage 2 under MFRS 9. List them by product type and calculate the expected credit loss (ECL) for each assuming a 35% loss given default (LGD). Present as a table sorted by ECL amount, largest first.'
          ]
        },
        {
          tool: '📝 Copilot in Word',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open BNK_02_Meridian_Bank_Strategy.docx. Ask Copilot: Draft a Shariah compliance remediation memo for the two flagged products. For each product, the memo should include: (1) the Shariah issue identified, (2) the proposed re-structuring to comply with IFSA requirements, (3) the customer impact and communication plan, (4) the timeline for remediation and sign-off by the Shariah Committee. Use a formal regulatory tone.',
            'Ask Copilot in Word: Summarise the BNM IFSA compliance requirements referenced in this strategy document into a checklist format. For each requirement, add a status column (Compliant / Partial / Gap) and a responsible officer column. This checklist will be used by the compliance team to prepare for the upcoming BNM review.',
            'Ask Copilot: Draft a Sukuk Wakalah investor briefing document of approximately 500 words. Cover: the structure of the instrument, profit rate and payment schedule, the underlying Wakalah assets, the risk factors, and the use of proceeds. The audience is institutional investors from the GCC who are familiar with Islamic finance but unfamiliar with Malaysian regulatory requirements.'
          ]
        },
        {
          tool: '🎯 Copilot in PowerPoint',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Ask Copilot in PowerPoint: Create a 10-slide Sukuk Wakalah roadshow presentation for institutional investors. Include slides on: AIBM overview and credit rating, the Sukuk structure diagram, profit rate and tenure, use of proceeds, the Shariah compliance framework, key financial metrics (CAR, NPF ratio, ROAE), risk factors, and a Q&A summary. Use a professional green and gold colour scheme appropriate for an Islamic finance presentation.',
            'Ask Copilot: Add speaker notes to each slide of this investor presentation. The notes should anticipate the three most likely questions from a GCC sovereign wealth fund and provide brief scripted answers the presenter can deliver naturally.',
            'Ask Copilot: Create a 2-slide summary of the BNM IFSA compliance status for use in the Board Shariah Committee meeting. Slide 1: Current compliance status (RAG table by requirement). Slide 2: Remediation plan for the two flagged products with a Gantt-style timeline.'
          ]
        },
        {
          tool: '📧 Copilot in Outlook',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open Email_06_BNM_Regulatory_Correspondence.docx. Ask Copilot in Outlook: Draft a formal response to the BNM IFSA review notice. The letter should: acknowledge receipt of the review schedule, confirm our readiness and the documents we will provide, request clarification on two specific requirements relating to Musharakah profit-sharing ratios, and propose a pre-review meeting with the BNM supervision officer to align on expectations.',
            'Ask Copilot: Draft an email to our Shariah Committee members calling an emergency meeting to address the two flagged products. The email should explain the nature of the Shariah issue without using overly technical language, attach the relevant product term sheets for review, and ask for written confirmation of availability for a 2-hour session this week. Subject line: "Urgent: Shariah Committee Review — Two Product Compliance Issues".',
            'Ask Copilot: Coach me on the tone of the draft email to BNM. Is it too defensive? Too casual? Does it inadvertently admit any non-compliance? Suggest three edits that would make the letter more confident and regulatory-appropriate without being evasive.'
          ]
        },
        {
          tool: '🎙 Copilot in Teams',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Use your OWN existing recorded Teams meetings. Open a meeting recap in Teams > Recap tab. Copilot generates summaries, action items, and follow-up drafts grounded in the actual transcript.',
          prompts: [
            'Open an existing recorded Teams meeting recap from a Shariah Committee or ALCO meeting. Ask Copilot: Identify all Shariah compliance decisions made in this meeting, the rationale provided, and any conditions attached to the approval. Format as a formal Shariah Committee resolution summary suitable for inclusion in the minute book.',
            'Ask Copilot in the recap: Draft follow-up action items for the ALCO based on this meeting. Each action should have a clear owner, a deliverable, and a deadline. Group actions by theme: Profit Rate Risk, Liquidity, Sukuk Issuance, and Shariah Compliance.',
            'Ask Copilot: Were any profit rate assumptions discussed in this meeting that differ from the assumptions in our Board-approved ALCO policy? If so, flag them with the exact quote from the transcript and the page number of the policy they may conflict with.'
          ]
        },
        {
          tool: '📓 Copilot Notebook',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via copilot.microsoft.com > Notebook tab. Upload up to 5 files and set a system instruction. Best for synthesising insights across multiple documents simultaneously.',
          prompts: [
            'Upload BNK_02_Meridian_Bank_Strategy.docx and Email_06_BNM_Regulatory_Correspondence.docx to Copilot Notebook. Set instruction: "You are a Shariah compliance officer preparing for a BNM IFSA review." Ask: What are the five most critical gaps between our strategy document and the BNM IFSA requirements referenced in the regulatory correspondence? For each gap, propose a remediation step and estimate the time required to close it.',
            'Upload BNK_01_Meridian_Bank.xlsx and BNK_02_Meridian_Bank_Strategy.docx. Ask: Based on the financing portfolio data and our stated strategy, which business segments are growing fastest and are they consistent with our Shariah-compliant product strategy? Flag any segment where growth is driven by a product type that the Shariah Committee has flagged for review.'
          ]
        },
        {
          tool: '🤝 Cowork (Frontier)',
          license: 'M365 Copilot + Frontier Program',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Cowork is an autonomous agent that takes actions across Microsoft 365 on your behalf — sending emails, scheduling meetings, creating documents, posting in Teams, and scheduling recurring tasks. Access: m365.cloud.microsoft > left nav > Agents > Cowork. Requires Frontier program enrollment.',
          prompts: [
            'Do all of the following: (1) Research BNM\'s latest IFSA guidelines on Sukuk Wakalah issuance requirements and any updates from the Securities Commission published in 2025. (2) Draft a 2-page compliance readiness checklist for our Sukuk issuance, mapping each requirement to our current status. (3) Save it to OneDrive as "Sukuk IFSA Compliance Checklist - [Today\'s Date]". (4) Email it to the Head of Islamic Finance and the Chief Compliance Officer asking for review and sign-off by Thursday. (5) Schedule a 90-minute "Sukuk Issuance Pre-Approval Review" meeting for Friday morning and invite the CFO, Head of Islamic Finance, and Shariah Committee Chairman.',
            'Do all of the following: (1) Set up a recurring weekly 30-minute Teams meeting titled "Shariah Compliance Monitoring Check-In" every Wednesday at 3pm for the next 12 weeks and invite the Shariah Compliance team. (2) Draft an agenda template for these meetings covering: open issues review, new product pipeline, BNM correspondence updates, and any other business. (3) Post the agenda template in the #shariah-compliance Teams channel with a message: "Agenda template for our weekly check-ins — please use this format going forward." (4) Send each invitee a welcome email explaining the purpose of the check-in series.'
          ]
        },
        {
          tool: '🤖 Word Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to a Word document. Open the .docx in Word for Web > Copilot pane > + New Agent > name it, write a description, set the document as knowledge source > Share. Colleagues chat with it in Teams or M365 Copilot.',
          prompts: [
            'Open BNK_02_Meridian_Bank_Strategy.docx in Word for Web. Create an agent called "AIBM Shariah Policy Bot". Description: "Answers questions from product managers and relationship managers about Al-Amanah Islamic Bank\'s Shariah compliance requirements, approved product structures, and profit rate policies." Set the document as knowledge source and share with the Islamic Banking product team.',
            'Demo: Ask the Shariah Policy Bot: "Is it permissible under our current Shariah framework to offer a hybrid Murabahah-Ijarah product for commercial property financing? What are the structural requirements and who needs to approve it?" Show how the agent gives a policy-grounded answer rather than requiring the team to search through documentation.'
          ]
        },
        {
          tool: '🤖 PowerPoint Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to a PowerPoint presentation. Great for strategy decks or Board presentations many people need to reference. Same setup as Word Agent but using a .pptx file.',
          prompts: [
            'Convert the Sukuk investor presentation into a PowerPoint file and open it in PowerPoint for Web. Create an agent called "Sukuk Investor Q&A Bot". Description: "Answers investor questions about Al-Amanah\'s MYR 3.5B Sukuk Wakalah issuance — structure, profit rate, Shariah compliance, and use of proceeds." Share the agent with the IR team and external investor contacts.',
            'Demo: Ask the agent "What is the profit rate and payment frequency for this Sukuk?" Then ask: "Who is the Shariah advisor for this issuance and what is the fatwa basis for the Wakalah structure?" Show how investor queries are answered instantly without requiring the IR team to dig through the prospectus.'
          ]
        },
        {
          tool: '🤖 Excel Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to an Excel workbook. Colleagues ask data questions in plain English without opening Excel. Open .xlsx in Excel for Web > Copilot pane > + New Agent > set workbook as knowledge source > share.',
          prompts: [
            'Open BNK_01_Meridian_Bank.xlsx in Excel for Web. Create an agent called "AIBM Portfolio Analytics Q&A". Description: "Instant answers on Al-Amanah Islamic Bank\'s financing portfolio — product mix, NPF ratios, profit rate sensitivity, and concentration risk — for ALCO and senior management." Share with ALCO members.',
            'Demo: Ask the agent "What is the current non-performing financing ratio for the Home Financing (Musharakah Mutanaqisah) segment?" Then ask: "If OPR rises by 50bps, what is the projected impact on our Net Financing Income?" Show how ALCO members get data-grounded answers in seconds.'
          ]
        },
        {
          tool: '🏗 Agent Builder (Copilot Studio)',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Build a custom declarative agent in Copilot Studio — no coding required. Access: copilotstudio.microsoft.com > Create > New Agent. Add name, description, knowledge sources (SharePoint URLs or uploaded files), topics/actions. Publish to Teams in under 10 minutes.',
          prompts: [
            'Go to copilotstudio.microsoft.com > Create > New Agent. Name it "AIBM Compliance & Product Assistant". Description: "Helps Islamic banking staff answer Shariah compliance questions, understand approved product structures, and navigate BNM IFSA requirements — grounded in official bank strategy and compliance documents." Upload BNK_02_Meridian_Bank_Strategy.docx and Email_06_BNM_Regulatory_Correspondence.docx. Add topics: "Shariah Product Query", "BNM Requirement Lookup", "Sukuk Issuance FAQ". Publish to Teams for all Islamic Banking staff.',
            'Demo the agent: Ask it "A corporate client wants Islamic financing for a toll road concession. What Shariah-compliant structures can we offer and what is the maximum tenure allowed under our current policy?" Then ask: "What are the BNM disclosure requirements for this type of infrastructure financing?" Show how front-line bankers get consistent, compliant guidance without calling the Shariah department.'
          ]
        }
      ]
    },
    {
      id: 'investment-banking',
      sectorId: 'banking-fs',
      subsector: '',
      name: 'Investment Banking',
      icon: '💹',
      color: '#0D47A1',
      accent: '#1565C0',
      company: 'Kenanga Capital Group',
      tagline: 'MYR 18.4B AUM — 3 IPO mandates in pipeline, ESG fund launch Q2 FY2026.',
      scenario: 'Kenanga Capital Group manages MYR 18.4B in assets under management and has three IPO mandates in the pipeline totalling a combined market cap of MYR 4.2B. An ESG-themed fund is being structured for launch in Q2 FY2026. The Securities Commission quarterly regulatory filing is due in two weeks and the M&A advisory team is evaluating a cross-border acquisition target.',
      files: [
        'GLC_01_Danamas_Capital.xlsx',
        'GLC_02_Danamas_Strategy.docx',
        '04_Zava_MA_Evaluation_Framework.docx'
      ],
      prompts: [
        {
          tool: '🤖 Copilot Chat (Basic)',
          license: 'Free — no M365 Copilot license needed',
          account: 'Sasha Ouellet — SashaO@ABSx62256373.OnMicrosoft.com',
          desc: '',
          prompts: [
            'I am an investment banker preparing a pitch to a tech company that wants to list on Bursa Malaysia. They are profitable but relatively small — MYR 180M revenue, MYR 22M EBITDA — and the founders are worried about whether the IPO window is open. Draft a 5-bullet talking points document I can use to open the pitch meeting. Cover: current Bursa market sentiment for tech listings, typical listing requirements for the ACE Market vs Main Market, the realistic timeline from mandate to listing day, and what we would need from them to start the due diligence process.',
            'Explain what an ESG-themed fund is, how it differs from a conventional equity fund, and what the key regulatory requirements are from the Securities Commission Malaysia for marketing an ESG fund to retail investors. Keep the explanation suitable for a senior client who understands investments but is new to ESG frameworks.',
            'What are the five most important factors that determine the success of an IPO in Malaysia? Rank them in order of importance and explain each in two to three sentences. Include one recent Malaysian IPO example to illustrate each factor.'
          ]
        },
        {
          tool: '🔍 Researcher',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via Microsoft 365 Copilot Chat (copilot.microsoft.com or Teams) > click Agents > Researcher. Grounds answers in live web sources and your organisation data with full citations.',
          prompts: [
            'Research the Malaysian IPO market in 2025 and 2026. I need: (1) Total number of IPOs listed and total funds raised on Bursa Malaysia in 2024 and year-to-date 2025, (2) Sectors with the highest demand from institutional investors, (3) Average price-to-earnings multiples achieved by tech and consumer sector IPOs. Provide source citations and present as an investment research brief.',
            'Research global ESG fund regulations relevant to Malaysian fund managers — specifically SEC, MAS, and Securities Commission Malaysia requirements for ESG disclosure. Identify the three key differences between SC Malaysia\'s ESG framework and the EU SFDR, and explain the implications for a Malaysian fund manager distributing to European institutional investors.'
          ]
        },
        {
          tool: '📊 Analyst',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via Microsoft 365 Copilot Chat > click Agents > Analyst. Upload an Excel or CSV file. Analyst runs Python-style analysis, builds charts, and interprets results without you writing a single formula.',
          prompts: [
            'Upload GLC_01_Danamas_Capital.xlsx. Ask Analyst: Analyse the AUM trend across all fund categories (equity, fixed income, ESG, alternative) over the past 8 quarters. Which categories are growing and which are in outflow? Calculate the net flow rate for each category and identify which fund manager or product has the highest alpha generation. Create a bubble chart showing AUM size vs net flow rate vs alpha.',
            'Upload GLC_01_Danamas_Capital.xlsx. Ask: Perform a peer comparison of Kenanga Capital\'s fee structure against the 4 closest competitors listed in the data. Which fee categories (management fee, performance fee, entry/exit fee) are above or below market median? Show as a heatmap table: Product Category | Our Fee | Market Median | Position (Above/Below/At).'
          ]
        },
        {
          tool: '📊 Copilot in Excel',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open GLC_01_Danamas_Capital.xlsx. Navigate to the IPO Pipeline sheet. Ask Copilot: For each of the three IPO mandates in the pipeline, calculate the estimated deal fee revenue based on the assumed offer price, shares offered, and our advisory fee rate (2.5% of gross proceeds). Show total expected revenue from all three mandates and flag which deal has the highest fee risk if the IPO is withdrawn.',
            'Ask Copilot: Create an ESG fund performance attribution model on a new sheet. The model should break down fund return into: (1) Market beta contribution, (2) ESG factor premium/discount, (3) Stock selection alpha, (4) Sector allocation effect. Use the returns data in the Fund Performance sheet and show monthly attribution for the last 12 months.',
            'Ask Copilot: In the Client AUM sheet, identify the top 20 clients by AUM and calculate the revenue concentration risk — what percentage of total management fee revenue comes from the top 5 clients. Highlight in red any client where a 30% AUM withdrawal would reduce our total fee revenue by more than 5%.'
          ]
        },
        {
          tool: '📝 Copilot in Word',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open GLC_02_Danamas_Strategy.docx. Ask Copilot: Draft an ESG fund prospectus introduction of 400 words for the new fund launching in Q2 FY2026. Cover: the fund\'s ESG investment philosophy, the screening methodology (negative exclusions + ESG scoring), the benchmark index, the target investor profile, and the expected distribution yield. Use language that meets SC Malaysia\'s disclosure standards for ESG funds.',
            'Ask Copilot in Word: Identify all sections in this strategy document related to M&A and corporate advisory. For each section, extract the key strategic rationale and create a one-page M&A pitch template that our advisory team can customise for new mandates. The template should have five sections: Client Situation, Strategic Rationale, Deal Mechanics, Our Credentials, and Proposed Fee Structure.',
            'Ask Copilot: Draft a 300-word "Chairman\'s Letter to Investors" for the annual fund report. The letter should acknowledge market volatility in FY2025, highlight our top-performing fund (the ESG equity fund returned 14.2%), reaffirm our investment philosophy, and outline our key strategic priorities for FY2026 — growing ESG AUM to MYR 2B and launching two new alternative investment products.'
          ]
        },
        {
          tool: '🎯 Copilot in PowerPoint',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Ask Copilot in PowerPoint: Create a 12-slide IPO pitch deck for a Malaysian tech company targeting a Main Market listing at MYR 420M market cap. Include: company overview, financial highlights (Revenue CAGR 28%, EBITDA margin 22%), industry tailwinds, competitive positioning, IPO structure and use of proceeds, valuation methodology (DCF + comparable companies), Bursa listing timeline, risk factors, and why now is the right time to list. Professional blue and silver theme.',
            'Ask Copilot: Generate a 6-slide ESG fund investor update presentation. Slides: (1) Portfolio overview and ESG score distribution, (2) Top 10 holdings with ESG ratings, (3) Carbon footprint vs benchmark, (4) Active ownership highlights — engagements and votes, (5) Performance attribution, (6) Outlook and strategy. Include speaker notes for each slide.',
            'Ask Copilot: Redesign slide 3 of this presentation to replace the text-heavy bullet list with a 2x2 matrix showing deal complexity vs fee potential for our pipeline. Place each of the three IPO mandates in the appropriate quadrant and add a one-line rationale.'
          ]
        },
        {
          tool: '📧 Copilot in Outlook',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Ask Copilot in Outlook: I have a meeting with a sovereign wealth fund potential investor next week about our ESG fund. Draft a pre-meeting email that introduces our ESG fund, attaches a one-pager (note: attach manually), proposes a 45-minute meeting agenda, and requests information on their typical ESG fund allocation size and return expectations. Keep the tone professional but not overly formal — this is a relationship-building email, not a hard sell.',
            'Ask Copilot: Draft the Securities Commission quarterly regulatory filing cover letter. The letter should reference the relevant SC circular, confirm the accuracy of the enclosed statements, note any material changes to the fund strategy or fee structure, and request acknowledgement of receipt. Use the formal tone required for SC correspondence.',
            'Ask Copilot: Summarise my inbox from the past two weeks and flag any emails related to our IPO pipeline mandates. Categorise them as: Urgent (client needs response today), Action Required (needs response this week), and FYI. List each email with sender, subject, and one-line summary.'
          ]
        },
        {
          tool: '🎙 Copilot in Teams',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Use your OWN existing recorded Teams meetings. Open a meeting recap in Teams > Recap tab. Copilot generates summaries, action items, and follow-up drafts grounded in the actual transcript.',
          prompts: [
            'Open an existing recorded Teams meeting recap from a deal team or investment committee meeting. Ask Copilot: Summarise all investment recommendations made, the key rationale for each, any dissenting views, and the final decision. Format as an investment committee minute suitable for regulatory record-keeping.',
            'Ask Copilot in the recap: Identify all client commitments made in this meeting — any promise to deliver a document, update, or recommendation to a client by a specific date. List each commitment with the staff member who made it and the agreed deadline, so I can follow up before end of week.',
            'Ask Copilot: Based on this meeting transcript, draft an action item register for the M&A deal team. Include four columns: Action | Owner | Deadline | Dependencies. Sort by deadline, earliest first.'
          ]
        },
        {
          tool: '📓 Copilot Notebook',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via copilot.microsoft.com > Notebook tab. Upload up to 5 files and set a system instruction. Best for synthesising insights across multiple documents simultaneously.',
          prompts: [
            'Upload GLC_01_Danamas_Capital.xlsx, GLC_02_Danamas_Strategy.docx, and 04_Zava_MA_Evaluation_Framework.docx to Copilot Notebook. Set instruction: "You are a senior M&A advisor preparing a cross-border acquisition recommendation." Ask: Based on the capital position in the data file, the strategic priorities in the strategy document, and the evaluation framework, what is the maximum acquisition size Kenanga Capital could prudently pursue without impairing its capital ratios or fund management licence? What type of acquisition target would best complement the current AUM mix?',
            'Upload GLC_02_Danamas_Strategy.docx and 04_Zava_MA_Evaluation_Framework.docx. Ask: The M&A evaluation framework lists 12 criteria for target assessment. Apply these criteria to a hypothetical acquisition of a Malaysia-based digital wealth management platform with MYR 800M AUM and 45,000 retail clients. Score the target out of 100 and recommend whether to proceed to indicative offer stage.'
          ]
        },
        {
          tool: '🤝 Cowork (Frontier)',
          license: 'M365 Copilot + Frontier Program',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Cowork is an autonomous agent that takes actions across Microsoft 365 on your behalf — sending emails, scheduling meetings, creating documents, posting in Teams, and scheduling recurring tasks. Access: m365.cloud.microsoft > left nav > Agents > Cowork. Requires Frontier program enrollment.',
          prompts: [
            'Do all of the following: (1) Research the top 5 ESG fund managers in Southeast Asia by AUM and their fund performance over the past 3 years. (2) Draft a competitive positioning brief comparing Kenanga Capital\'s ESG fund against these peers — 2 pages, with a summary table showing AUM, returns, expense ratio, and ESG methodology. (3) Save to OneDrive as "ESG Fund Competitive Analysis - [Date]". (4) Email to the Head of Fund Management and CEO asking for review before the investor roadshow next week. (5) Schedule a 60-minute "ESG Fund Investor Roadshow Prep" meeting for Tuesday at 9am.',
            'Do all of the following: (1) Check the Securities Commission Malaysia website for any new circulars or guidelines published in the past 30 days. (2) Identify any that affect our fund management licence or ESG fund offering. (3) Draft a compliance alert memo for the Chief Compliance Officer summarising the new requirements and recommended actions. (4) Post a summary in the #compliance-team Teams channel. (5) Schedule a 45-minute compliance briefing for the fund management team for this Friday.'
          ]
        },
        {
          tool: '🤖 Word Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to a Word document. Open the .docx in Word for Web > Copilot pane > + New Agent > name it, write a description, set the document as knowledge source > Share. Colleagues chat with it in Teams or M365 Copilot.',
          prompts: [
            'Open GLC_02_Danamas_Strategy.docx in Word for Web. Create an agent called "Capital Strategy Q&A Bot". Description: "Answers questions from investment managers and relationship managers about Kenanga Capital\'s investment strategy, ESG fund framework, and M&A evaluation criteria." Share with the investment management and advisory teams.',
            'Demo: Ask the agent "What is the minimum ESG score threshold for a company to be included in our ESG fund portfolio? What happens if a holding\'s score drops below the threshold after inclusion?" Show how the fund management team gets consistent policy answers without calling compliance.'
          ]
        },
        {
          tool: '🤖 PowerPoint Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to a PowerPoint presentation. Great for strategy decks or Board presentations many people need to reference. Same setup as Word Agent but using a .pptx file.',
          prompts: [
            'Create a PowerPoint summary of the IPO pitch deck and open in PowerPoint for Web. Create an agent called "IPO Pitch Deck Q&A". Description: "Answers due diligence questions from potential IPO clients about Kenanga Capital\'s track record, deal process, timeline, and fee structure." Share with the corporate finance team to use in client pitches.',
            'Demo: A client asks the agent "How long does the IPO process typically take from mandate signing to listing day on Bursa Main Market?" Then: "What is your typical underwriting fee structure and are there any performance-linked fee arrangements?" Show how the agent handles common client questions consistently.'
          ]
        },
        {
          tool: '🤖 Excel Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to an Excel workbook. Colleagues ask data questions in plain English without opening Excel. Open .xlsx in Excel for Web > Copilot pane > + New Agent > set workbook as knowledge source > share.',
          prompts: [
            'Open GLC_01_Danamas_Capital.xlsx in Excel for Web. Create an agent called "AUM & Performance Q&A". Description: "Provides instant answers on Kenanga Capital\'s fund AUM, performance data, client concentration, and pipeline deal metrics." Share with senior management and investor relations.',
            'Demo: Ask the agent "What is the total AUM across all equity funds and what was the average return in FY2025?" Then: "Which client accounts for the largest single AUM concentration and what is the revenue exposure if they redeem?" Show how management gets instant portfolio intelligence.'
          ]
        },
        {
          tool: '🏗 Agent Builder (Copilot Studio)',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Build a custom declarative agent in Copilot Studio — no coding required. Access: copilotstudio.microsoft.com > Create > New Agent. Add name, description, knowledge sources (SharePoint URLs or uploaded files), topics/actions. Publish to Teams in under 10 minutes.',
          prompts: [
            'Go to copilotstudio.microsoft.com > Create > New Agent. Name it "Kenanga Investor Intelligence Bot". Description: "An AI assistant for Kenanga Capital\'s client-facing team — answers investor questions about fund performance, ESG methodology, IPO pipeline, and regulatory compliance using official strategy and fund documents." Upload GLC_01_Danamas_Capital.xlsx and GLC_02_Danamas_Strategy.docx. Add topics: "Fund Performance Query", "ESG Methodology", "IPO Services". Publish to Teams for the client advisory team.',
            'Demo in Teams: Ask the bot "An institutional client wants to know how our ESG fund screens for climate risk — can you walk me through our methodology and name two examples of companies we excluded in the last 12 months?" Then: "What is our current track record for IPO mandates — how many have we completed and what was the average first-day trading premium?" Show how the advisory team answers complex client questions confidently and consistently.'
          ]
        }
      ]
    },
    {
      id: 'general-insurance',
      sectorId: 'insurance',
      subsector: '',
      name: 'General Insurance',
      icon: '🛡',
      color: '#1A237E',
      accent: '#283593',
      company: 'Pacific Shield Insurance Berhad',
      tagline: 'Motor combined ratio at 108% — claims leakage and fraud costing MYR 84M annually.',
      scenario: 'Pacific Shield Insurance Berhad is Malaysia\'s fourth-largest general insurer. The motor segment combined ratio has breached 108%, well above the 95% profitability threshold, driven by rising claims frequency and a suspected claims fraud syndicate (Project SWIFT CLAIM). BNM\'s detariffication deadline creates additional pricing pressure.',
      files: [
        'INS_01_Pacific_Shield_Insurance.xlsx',
        'INS_02_Pacific_Shield_Strategy.docx'
      ],
      prompts: [
        {
          tool: '🤖 Copilot Chat (Basic)',
          license: 'Free — no M365 Copilot license needed',
          account: 'Sasha Ouellet — SashaO@ABSx62256373.OnMicrosoft.com',
          desc: '',
          prompts: [
            'I am the Head of Claims at a Malaysian general insurer. Our motor combined ratio has risen to 108% and we suspect a fraud syndicate is inflating repair bills through workshop collusion. Draft a structured fraud investigation brief of approximately 250 words that I can use to brief our investigators. Cover: the suspected fraud pattern, the data signals we should look for in claims records, the legal framework for fraud investigation in Malaysia, and the key questions our investigators should ask suspicious claimants. Keep the tone professional and factual.',
            'Explain the BNM motor detariffication framework in plain language. What does it mean for insurers, what pricing freedoms does it create, and what risks does it introduce if an insurer prices too aggressively in the first year? Limit the explanation to 200 words suitable for a Board Risk Committee briefing.',
            'What are the five key metrics used to assess the profitability of a general insurance portfolio? Define each metric, provide the industry benchmark for Malaysian general insurers, and indicate whether a higher or lower number is desirable for each.'
          ]
        },
        {
          tool: '🔍 Researcher',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via Microsoft 365 Copilot Chat (copilot.microsoft.com or Teams) > click Agents > Researcher. Grounds answers in live web sources and your organisation data with full citations.',
          prompts: [
            'Research insurance fraud detection technology trends in Southeast Asia for 2025 and 2026. I need: (1) The most effective AI and machine learning approaches used by leading insurers to detect motor claims fraud, (2) Two or three vendor solutions deployed in the region with documented fraud reduction results, (3) Any regulatory guidance from BNM or the Malaysia Insurance Institute on fraud analytics. Provide citations.',
            'Research how Malaysian general insurers are responding to BNM motor detariffication. What pricing strategies are the top 5 insurers using? Has the detariffication led to market share shifts? Are there any BNM supervisory concerns about underpricing? Present as a competitive intelligence brief.'
          ]
        },
        {
          tool: '📊 Analyst',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via Microsoft 365 Copilot Chat > click Agents > Analyst. Upload an Excel or CSV file. Analyst runs Python-style analysis, builds charts, and interprets results without you writing a single formula.',
          prompts: [
            'Upload INS_01_Pacific_Shield_Insurance.xlsx to Analyst. Ask: Analyse the motor claims data to identify patterns consistent with fraud. Look for: (1) workshops with unusually high average claim values, (2) policyholders with multiple claims in 12 months, (3) claims submitted within 30 days of policy inception, (4) claims where repair cost exceeds 70% of vehicle value. Create a fraud risk score for each workshop and rank the top 10 highest-risk workshops. Show as a table and a bar chart.',
            'Upload INS_01_Pacific_Shield_Insurance.xlsx. Ask Analyst: Decompose the motor combined ratio of 108% into its component parts: claims frequency, average claims severity, expense ratio, and reinsurance recovery rate. Which component has deteriorated most year-on-year? Show the trend over 8 quarters with a waterfall chart showing how each component has contributed to the combined ratio movement from 95% to 108%.'
          ]
        },
        {
          tool: '📊 Copilot in Excel',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open INS_01_Pacific_Shield_Insurance.xlsx and navigate to the Claims Analysis sheet. Ask Copilot: Create a fraud detection dashboard on a new sheet. For each motor workshop in the data, calculate: (1) Average claim value vs national average, (2) Claims rejection rate, (3) Percentage of claims submitted by the same loss adjuster, (4) Average repair days vs industry benchmark of 12 days. Highlight in red any workshop that triggers 3 or more of these fraud indicators.',
            'Ask Copilot: Build a detariffication pricing model on a new sheet. For each motor risk category (private car, commercial vehicle, motorcycle), calculate the breakeven premium rate that achieves a 95% combined ratio target. Assume: current claims frequency, projected 5% claims inflation, and our current expense ratio of 28%. Show the new premium rate and the percentage change from the current tariff rate.',
            'Ask Copilot: In the Policy Renewal sheet, identify all policies where the renewal date is within the next 30 days, the current premium is below breakeven, and the policyholder has made more than one claim in the past 12 months. These are high-risk renewals we should either reprice or decline. List with policy number, current premium, breakeven premium, and claims history.'
          ]
        },
        {
          tool: '📝 Copilot in Word',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open INS_02_Pacific_Shield_Strategy.docx. Ask Copilot: Draft a 2-page Project SWIFT CLAIM investigation report for the Board Audit Committee. Structure: (1) Background — fraud suspected based on claims data analysis, (2) Evidence Summary — key data signals identified, (3) Top 5 suspicious workshops with supporting data, (4) Recommended Actions — referral to police, claims suspension, blacklisting, (5) Financial Impact — estimated annual claims leakage of MYR 84M. Use a formal, legally cautious tone that avoids prejudging guilt.',
            'Ask Copilot in Word: Identify all sections in this strategy document that reference claims management or fraud prevention. Summarise the current fraud prevention commitments and identify any gaps relative to industry best practice. Create a gap analysis table: Current Practice | Best Practice | Gap | Recommended Action.',
            'Ask Copilot: Draft a customer communication letter that will be sent to policyholders whose claims are being reviewed as part of Project SWIFT CLAIM. The letter must: inform them of the review without alleging fraud, explain that a small delay in claims payment should be expected, provide contact details for queries, and maintain a respectful, non-accusatory tone. Keep it under 250 words.'
          ]
        },
        {
          tool: '🎯 Copilot in PowerPoint',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Ask Copilot in PowerPoint: Create a 10-slide Board presentation on Project SWIFT CLAIM and detariffication strategy. Slides: (1) Executive summary — combined ratio at 108% and key drivers, (2) Fraud analysis — claims leakage breakdown, (3) Top 10 suspicious workshops heat map, (4) Investigation plan and timeline, (5) Detariffication pricing strategy, (6) New premium rates by risk category, (7) Retention vs repricing decision matrix, (8) Financial impact — if fraud reduced by 50% and detariffication implemented, (9) Key risks, (10) Recommended decisions for Board approval. Use navy blue and white colour scheme.',
            'Ask Copilot: Create speaker notes for each slide. The CEO presenting has a habit of going off-topic — the notes should include a bracketed "[STOP HERE]" marker to help her stay on time. Each slide should be 45 seconds maximum.',
            'Ask Copilot: Add an appendix slide with a 2x2 risk matrix showing the four key risks to our detariffication strategy: underprice risk, competitor aggression, BNM supervisory scrutiny, and claims inflation. Place each risk in the appropriate quadrant based on likelihood and impact.'
          ]
        },
        {
          tool: '📧 Copilot in Outlook',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Ask Copilot in Outlook: Draft a formal notification letter to BNM\'s Insurance Supervision Department regarding the suspected claims fraud syndicate. The letter should: explain the nature and scale of the suspected fraud, describe the internal investigation steps taken, request guidance on whether BNM expects a formal regulatory notification, and propose a meeting to discuss. Use the formal tone required for BNM correspondence.',
            'Ask Copilot: Draft an internal email to all claims adjusters and investigators briefing them on Project SWIFT CLAIM. The email should explain the investigation without naming specific workshops yet, instruct adjusters to flag any motor claim over MYR 15,000 for secondary review, and ask them to report any unusual patterns they have observed. Remind them of the strict confidentiality requirement.',
            'Ask Copilot: Summarise the last 10 emails in my inbox related to claims or fraud. Identify any that require a response today, any that contain regulatory communications, and any where a commitment was made that has not yet been fulfilled. Present as a prioritised action list.'
          ]
        },
        {
          tool: '🎙 Copilot in Teams',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Use your OWN existing recorded Teams meetings. Open a meeting recap in Teams > Recap tab. Copilot generates summaries, action items, and follow-up drafts grounded in the actual transcript.',
          prompts: [
            'Open an existing recorded Teams meeting recap from a claims committee or fraud taskforce meeting. Ask Copilot: Summarise all fraud case updates discussed, decisions made on claims suspension or rejection, and any escalation actions agreed. Format as a fraud committee minute.',
            'Ask Copilot in the recap: Draft a follow-up email to the investigation team summarising the actions agreed in this meeting. Include a table: Action | Owner | Deadline | Status (In Progress / Not Started).',
            'Ask Copilot: Were any specific workshop names or policy numbers discussed in this meeting? List them with the context in which they were mentioned so I can update the fraud watch list.'
          ]
        },
        {
          tool: '📓 Copilot Notebook',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via copilot.microsoft.com > Notebook tab. Upload up to 5 files and set a system instruction. Best for synthesising insights across multiple documents simultaneously.',
          prompts: [
            'Upload INS_01_Pacific_Shield_Insurance.xlsx and INS_02_Pacific_Shield_Strategy.docx to Copilot Notebook. Set instruction: "You are a senior insurance executive preparing a combined ratio recovery plan." Ask: Based on the claims data and our strategic priorities, what is a realistic combined ratio target we can achieve in 12 months if we implement both the fraud reduction programme and the detariffication repricing? Show your working and flag the two biggest assumptions in your estimate.',
            'Upload INS_01_Pacific_Shield_Insurance.xlsx and INS_02_Pacific_Shield_Strategy.docx. Ask: The strategy document commits to growing motor insurance market share. The claims data shows motor is deeply unprofitable at 108% CR. Is there a direct tension between these two objectives? How should the Board resolve this tension? Suggest two options with the financial trade-off for each.'
          ]
        },
        {
          tool: '🤝 Cowork (Frontier)',
          license: 'M365 Copilot + Frontier Program',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Cowork is an autonomous agent that takes actions across Microsoft 365 on your behalf — sending emails, scheduling meetings, creating documents, posting in Teams, and scheduling recurring tasks. Access: m365.cloud.microsoft > left nav > Agents > Cowork. Requires Frontier program enrollment.',
          prompts: [
            'Do all of the following: (1) Research the BNM guidelines on insurance fraud reporting obligations and the Malaysia Anti-Corruption Commission (MACC) referral process for insurance fraud syndicates. (2) Draft a 3-page legal and regulatory obligations summary for our General Counsel and Compliance Officer. (3) Save to OneDrive as "SWIFT CLAIM Regulatory Obligations Brief". (4) Email to the General Counsel and Chief Compliance Officer asking for review by Thursday. (5) Schedule a 90-minute "Project SWIFT CLAIM Legal Review" meeting for Friday at 2pm with the General Counsel, CRO, and Head of Claims.',
            'Do all of the following: (1) For each of the top 10 suspicious workshops identified in the fraud analysis, search our claims system emails for any prior complaints or irregularities. (2) Draft a workshop suspension notification letter template. (3) Create a tracking spreadsheet listing all 10 workshops with columns: Workshop Name | Fraud Score | Total Claims Value | Action Status | Date of Suspension Letter. (4) Save the spreadsheet to the Claims Team SharePoint folder. (5) Post in the #claims-fraud-taskforce Teams channel: "Top 10 suspicious workshops identified — suspension letters to be issued this week. See SharePoint for tracker."'
          ]
        },
        {
          tool: '🤖 Word Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to a Word document. Open the .docx in Word for Web > Copilot pane > + New Agent > name it, write a description, set the document as knowledge source > Share. Colleagues chat with it in Teams or M365 Copilot.',
          prompts: [
            'Open INS_02_Pacific_Shield_Strategy.docx in Word for Web. Create an agent called "Claims Policy Assistant". Description: "Answers questions from claims adjusters and investigators about Pacific Shield\'s claims handling procedures, fraud detection protocols, and workshop blacklisting policy." Share with the claims operations team.',
            'Demo: Ask the Claims Policy Assistant "A workshop has submitted three claims in 5 days for the same vehicle, all for different parts. What is our fraud flag threshold and what investigation steps am I required to take before approving any of the three claims?" Show how the agent provides consistent, policy-grounded guidance.'
          ]
        },
        {
          tool: '🤖 PowerPoint Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to a PowerPoint presentation. Great for strategy decks or Board presentations many people need to reference. Same setup as Word Agent but using a .pptx file.',
          prompts: [
            'Create a PowerPoint from the Board fraud presentation and open in PowerPoint for Web. Create an agent called "SWIFT CLAIM Board Briefing Bot". Description: "Answers Board and Audit Committee questions about Project SWIFT CLAIM, fraud data, and the detariffication pricing strategy." Share with Board members ahead of the meeting.',
            'Demo: A Board member asks the agent "What is the estimated annual financial impact if we successfully reduce workshop fraud by 50%?" Then: "What legal risks do we face if we wrongly suspend a legitimate workshop?" Show how Board members get data-grounded answers before the meeting.'
          ]
        },
        {
          tool: '🤖 Excel Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to an Excel workbook. Colleagues ask data questions in plain English without opening Excel. Open .xlsx in Excel for Web > Copilot pane > + New Agent > set workbook as knowledge source > share.',
          prompts: [
            'Open INS_01_Pacific_Shield_Insurance.xlsx in Excel for Web. Create an agent called "Claims Analytics Q&A". Description: "Answers questions about Pacific Shield\'s motor claims data, combined ratio breakdown, fraud indicators, and renewal portfolio — for claims managers and the pricing team." Share with the actuarial and claims leadership.',
            'Demo: Ask the agent "What is the average claim value submitted by the top 3 highest-risk workshops compared to the national average?" Then: "How many policies are up for renewal in the next 30 days where the premium is below our breakeven rate?" Show instant access to critical pricing and claims intelligence.'
          ]
        },
        {
          tool: '🏗 Agent Builder (Copilot Studio)',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Build a custom declarative agent in Copilot Studio — no coding required. Access: copilotstudio.microsoft.com > Create > New Agent. Add name, description, knowledge sources (SharePoint URLs or uploaded files), topics/actions. Publish to Teams in under 10 minutes.',
          prompts: [
            'Go to copilotstudio.microsoft.com > Create > New Agent. Name it "Pacific Shield Claims Intelligence Agent". Description: "An AI assistant for Pacific Shield\'s claims and underwriting teams — answers questions about fraud detection, claims handling policy, combined ratio targets, and detariffication pricing strategy using official strategy and data documents." Upload INS_01_Pacific_Shield_Insurance.xlsx and INS_02_Pacific_Shield_Strategy.docx. Add a starter topic: "Help me assess a potentially fraudulent claim." Publish to Teams for Claims and Underwriting.',
            'Demo the agent in Teams. A claims adjuster asks: "I have a motor claim for MYR 28,000 from a workshop that has submitted 8 claims this month. Three of the claims involve the same loss adjuster. What fraud indicators should I document and what is the escalation path?" Show how the agent provides a structured investigation checklist and escalation guidance grounded in company policy.'
          ]
        }
      ]
    },
    {
      id: 'life-insurance',
      sectorId: 'insurance',
      subsector: '',
      name: 'Life Insurance',
      icon: '💗',
      color: '#283593',
      accent: '#3949AB',
      company: 'Meridian Life Assurance Berhad',
      tagline: 'RBC ratio 182% — agent channel productivity declining 18% as digital disruptors gain share.',
      scenario: 'Meridian Life Assurance Berhad manages MYR 8.4B in life fund assets with an RBC ratio of 182% — comfortable but declining. Agent channel productivity has dropped 18% year-on-year as digital insurtech platforms capture first-time buyers. A new digital distribution initiative is being piloted in Q2 FY2026.',
      files: [
        'INS_01_Pacific_Shield_Insurance.xlsx',
        'INS_02_Pacific_Shield_Strategy.docx'
      ],
      prompts: [
        {
          tool: '🤖 Copilot Chat (Basic)',
          license: 'Free — no M365 Copilot license needed',
          account: 'Sasha Ouellet — SashaO@ABSx62256373.OnMicrosoft.com',
          desc: '',
          prompts: [
            'I am the Chief Distribution Officer of a Malaysian life insurer. Our agent productivity has fallen 18% year-on-year and digital insurtech platforms are capturing the 25–35 age segment. Draft a strategic options paper of 300 words presenting three distinct approaches we could take: (1) defend and enhance the agent channel, (2) launch our own digital platform, (3) partner or acquire an insurtech. For each option, summarise the key advantages, risks, and estimated timeline to see results.',
            'Explain the BNM Risk-Based Capital (RBC) framework for Malaysian life insurers. What does an RBC ratio of 182% indicate, what are the regulatory minimum and supervisory target levels, and what actions would BNM take if the ratio fell below 130%? Keep the explanation suitable for a Board member with a legal background.',
            'What are the five key trends shaping the life insurance industry in Malaysia and Southeast Asia in 2025 and 2026? Focus on customer behaviour, regulation, and technology. Summarise each trend in three sentences.'
          ]
        },
        {
          tool: '🔍 Researcher',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via Microsoft 365 Copilot Chat (copilot.microsoft.com or Teams) > click Agents > Researcher. Grounds answers in live web sources and your organisation data with full citations.',
          prompts: [
            'Research the competitive landscape for digital life insurance distribution in Malaysia. I need: (1) The main insurtech and digital-first life insurance platforms operating in Malaysia and their estimated market share, (2) The customer segments they are targeting, (3) Any BNM licensing requirements for digital insurance distribution. Summarise as a competitive intelligence brief with sources.',
            'Research life insurance product innovation trends in Southeast Asia — specifically investment-linked products (ILPs) and micro-insurance. Which markets are growing fastest and why? What product features are driving take-up among millennial and Gen Z buyers? Cite recent industry reports or research.'
          ]
        },
        {
          tool: '📊 Analyst',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via Microsoft 365 Copilot Chat > click Agents > Analyst. Upload an Excel or CSV file. Analyst runs Python-style analysis, builds charts, and interprets results without you writing a single formula.',
          prompts: [
            'Upload INS_01_Pacific_Shield_Insurance.xlsx. Ask Analyst: Analyse agent productivity data over the past 8 quarters. Calculate new policies per active agent, average premium per policy, and lapse rate by agent tier (Platinum, Gold, Silver, Bronze). Which agent tier has the highest lapse rate and lowest productivity? Create a scatter plot of agent tenure vs productivity score and identify whether newer agents (under 2 years) are performing better or worse than tenured agents.',
            'Upload INS_01_Pacific_Shield_Insurance.xlsx. Ask: Perform a lapse rate cohort analysis — group policyholders by the year they purchased their policy and calculate the cumulative lapse rate at 1 year, 2 years, 3 years, and 5 years. Which vintage has the highest early lapse rate? Show as a cohort table and a line chart.'
          ]
        },
        {
          tool: '📊 Copilot in Excel',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open INS_01_Pacific_Shield_Insurance.xlsx. Navigate to the Agent Performance sheet. Ask Copilot: Create a tier-based productivity dashboard for our 3,200 active agents. For each tier (Platinum, Gold, Silver, Bronze), calculate: (1) Average new annual premium equivalents (APE) per agent, (2) Persistency ratio (13-month), (3) Average income earned. Highlight in red any tier where persistency has dropped below 80%.',
            'Ask Copilot: In the Product Mix sheet, analyse the shift in product mix from FY2022 to FY2025. Has the proportion of ILP (Investment-Linked Plans) vs traditional life products changed? Calculate the revenue impact of this shift given that ILPs have lower margin than whole life products. Show as a stacked bar chart by year.',
            'Ask Copilot: Build a digital channel vs agent channel comparison on a new sheet. Compare: (1) Customer acquisition cost, (2) Average premium size, (3) Lapse rate at 12 months, (4) Cross-sell rate. If the digital channel has a 40% lower customer acquisition cost but 25% higher lapse rate, calculate the 5-year lifetime value difference between the two channels.'
          ]
        },
        {
          tool: '📝 Copilot in Word',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open INS_02_Pacific_Shield_Strategy.docx. Ask Copilot: Draft a 2-page agent productivity recovery plan. Cover: (1) Root causes of the 18% productivity decline (3 key reasons), (2) Three initiatives to reverse the trend — training uplift, digital tools for agents, performance incentive restructuring, (3) KPIs and targets for 12 months, (4) Investment required and expected ROI. Use an executive memo format.',
            'Ask Copilot: Identify all product mentions in this strategy document. For each product, determine whether it is positioned for the agent channel, digital channel, or both. Create a product-channel matrix table showing which products are currently channel-appropriate and which may need repositioning as the digital channel grows.',
            'Ask Copilot: Draft a 400-word internal communication from the CEO to all 3,200 agents explaining the digital initiative. The message should: reassure agents that the digital channel complements rather than replaces them, explain the new digital tools being rolled out to help agents, and invite agents to a town hall session next month. Tone: motivating and honest, not corporate-speak.'
          ]
        },
        {
          tool: '🎯 Copilot in PowerPoint',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Ask Copilot in PowerPoint: Create an 8-slide presentation for the Board on the Digital Distribution Initiative. Include: (1) Problem statement — agent productivity decline and digital competition, (2) Market opportunity — digital life insurance market size, (3) Our proposed digital strategy, (4) Technology platform requirements, (5) Financial projections — APE and margin at Year 1, 2, 3, (6) Risk and mitigation, (7) Change management plan, (8) Decision required. Use a modern teal and white design.',
            'Ask Copilot: Generate a one-slide agent value proposition that clearly explains to our agent force why the digital initiative helps them rather than threatens them. Use three key messages, each with a supporting statistic. Design it as a simple visual slide they can share with their teams.',
            'Ask Copilot: Add a competitive landscape slide showing the digital insurtech players in Malaysia, their estimated market share, and the customer segment each targets. Use a simple 2x2 matrix (digital experience vs price) to position each player.'
          ]
        },
        {
          tool: '📧 Copilot in Outlook',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Ask Copilot in Outlook: Draft an email to BNM\'s Insurance Supervision Department requesting a pre-consultation meeting regarding our digital distribution platform. The email should describe the initiative at a high level, explain how it will comply with BNM\'s digital insurance guidelines, and request a 45-minute meeting to discuss regulatory expectations before we launch the pilot.',
            'Ask Copilot: Draft a recruitment email to three potential digital platform technology partners inviting them to submit a proposal for our digital distribution platform. The email should outline our requirements: policy issuance capability, e-KYC integration, BNM takaful separation compliance, and API-first architecture. Request a proposal within 3 weeks.',
            'Ask Copilot: I have 47 unread emails from my agents in the past week about the digital initiative announcement. Categorise them into: Concerns (worried about job security), Questions (want more information), Positive (supportive), and Suggestions. Draft a single FAQ document that addresses the top 5 concerns and 5 questions raised.'
          ]
        },
        {
          tool: '🎙 Copilot in Teams',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Use your OWN existing recorded Teams meetings. Open a meeting recap in Teams > Recap tab. Copilot generates summaries, action items, and follow-up drafts grounded in the actual transcript.',
          prompts: [
            'Open a recorded Teams meeting recap from an agent or distribution team meeting. Ask Copilot: Identify all concerns raised about the digital initiative, any specific suggestions agents made for improving the agent toolset, and any commitments the management team made in response. Format as a structured feedback summary for the Digital Transformation team.',
            'Ask Copilot in the recap: Draft follow-up actions from this town hall meeting. Group actions into three categories: Immediate (this week), Short-term (this month), and Strategic (this quarter). Assign an owner to each.',
            'Ask Copilot: Based on this meeting, what is the overall sentiment of the agent force toward the digital initiative — positive, neutral, or negative? Identify the three most commonly expressed concerns and the one area where agents expressed the strongest support.'
          ]
        },
        {
          tool: '📓 Copilot Notebook',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via copilot.microsoft.com > Notebook tab. Upload up to 5 files and set a system instruction. Best for synthesising insights across multiple documents simultaneously.',
          prompts: [
            'Upload INS_01_Pacific_Shield_Insurance.xlsx and INS_02_Pacific_Shield_Strategy.docx. Set instruction: "You are the Chief Strategy Officer preparing the digital transformation business case for the Board." Ask: Based on the agent productivity data and our strategic objectives, what is the minimum number of digital policies we need to sell in Year 1 to offset the projected further decline in agent channel APE? What customer segment should we target first and why?',
            'Upload INS_01_Pacific_Shield_Insurance.xlsx and INS_02_Pacific_Shield_Strategy.docx. Ask: Are there any internal contradictions in our current strategy? Specifically, the document commits to growing APE by 12% while agent productivity is declining 18%. Is this growth target realistic without the digital channel? If not, what is a more credible target and what must we execute on to achieve it?'
          ]
        },
        {
          tool: '🤝 Cowork (Frontier)',
          license: 'M365 Copilot + Frontier Program',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Cowork is an autonomous agent that takes actions across Microsoft 365 on your behalf — sending emails, scheduling meetings, creating documents, posting in Teams, and scheduling recurring tasks. Access: m365.cloud.microsoft > left nav > Agents > Cowork. Requires Frontier program enrollment.',
          prompts: [
            'Do all of the following: (1) Research the top 5 insurtech platforms in Southeast Asia that offer white-label digital life insurance distribution and identify which ones have Malaysian regulatory approval. (2) Draft a vendor evaluation brief comparing their capabilities against our requirements. (3) Save to OneDrive as "Digital Distribution Vendor Shortlist". (4) Email to the CTO and CDO asking for input before the vendor RFP closes on Friday. (5) Schedule a 2-hour vendor review meeting for next Wednesday and invite the CTO, CDO, Head of Digital, and Head of Products.',
            'Do all of the following for agent productivity recovery: (1) Review the agent performance data and identify the bottom 20% of agents by APE who have been with the company more than 2 years. (2) Draft personalised coaching emails to each underperforming agent — the email should acknowledge their tenure, offer a 1-on-1 coaching session, and outline the new digital tools available to help them. (3) Schedule individual 30-minute coaching sessions for each agent over the next 4 weeks. (4) Create a tracking sheet in OneDrive with columns: Agent Name | Tier | Current APE | Target APE | Coaching Date | Follow-up Date.'
          ]
        },
        {
          tool: '🤖 Word Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to a Word document. Open the .docx in Word for Web > Copilot pane > + New Agent > name it, write a description, set the document as knowledge source > Share. Colleagues chat with it in Teams or M365 Copilot.',
          prompts: [
            'Open INS_02_Pacific_Shield_Strategy.docx in Word for Web. Create an agent called "Life Insurance Strategy Bot". Description: "Answers questions from agents and managers about Meridian Life\'s product strategy, distribution approach, RBC requirements, and digital initiative. Helps the agent force understand how the strategy affects their role and what tools are available to them." Share with the agent network.',
            'Demo: Ask the Strategy Bot "The digital platform is launching next quarter. Does this mean my territory will be split with digital customers? Will my commissions change for policies purchased online?" Show how the agent gets a clear, consistent answer from the official strategy document rather than rumour.'
          ]
        },
        {
          tool: '🤖 PowerPoint Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to a PowerPoint presentation. Great for strategy decks or Board presentations many people need to reference. Same setup as Word Agent but using a .pptx file.',
          prompts: [
            'Create a PowerPoint from the Digital Distribution Initiative Board presentation. Create an agent called "Digital Initiative Board Q&A". Share with Board members before the meeting so they can review and prepare questions.',
            'Demo: A Board member asks "What is our projected RBC ratio impact if the digital initiative requires MYR 80M of capital investment over 3 years?" Then: "What happens to agent channel productivity projections if we do nothing — what does the 3-year outlook look like without the digital investment?" Show how the agent helps Board members challenge assumptions before the meeting.'
          ]
        },
        {
          tool: '🤖 Excel Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to an Excel workbook. Colleagues ask data questions in plain English without opening Excel. Open .xlsx in Excel for Web > Copilot pane > + New Agent > set workbook as knowledge source > share.',
          prompts: [
            'Open INS_01_Pacific_Shield_Insurance.xlsx in Excel for Web. Create an agent called "Life Portfolio Analytics Q&A". Description: "Instant answers on Meridian Life\'s policy portfolio, agent productivity, lapse rates, product mix, and RBC position — for actuarial, distribution, and senior management teams." Share broadly across the insurance division.',
            'Demo: Ask "What is the current 13-month persistency ratio for Platinum-tier agents and how does it compare to Silver-tier?" Then: "How many policies lapsed in the first 12 months across the investment-linked product range in FY2025?" Show how the actuarial and distribution teams access precise portfolio intelligence instantly.'
          ]
        },
        {
          tool: '🏗 Agent Builder (Copilot Studio)',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Build a custom declarative agent in Copilot Studio — no coding required. Access: copilotstudio.microsoft.com > Create > New Agent. Add name, description, knowledge sources (SharePoint URLs or uploaded files), topics/actions. Publish to Teams in under 10 minutes.',
          prompts: [
            'Go to copilotstudio.microsoft.com > Create > New Agent. Name it "Meridian Life Agent Support Bot". Description: "Supports Meridian Life\'s 3,200 agents with instant answers on products, policy administration, RBC position, commission structures, and the digital transformation initiative — reducing calls to the agency support desk and ensuring agents have consistent, accurate information." Upload INS_02_Pacific_Shield_Strategy.docx. Add topics: "Product Questions", "Commission & Incentives", "Digital Tools", "RBC & Financial Questions". Publish to Teams for all agents.',
            'Demo the agent: An agent asks "I have a client who wants to surrender a 3-year ILP policy. What is the surrender value calculation and are there any early surrender penalties? What alternatives should I discuss before the client decides to surrender?" Show how the agent provides a complete, policy-grounded response that helps the agent retain the client rather than simply processing a surrender.'
          ]
        }
      ]
    },
    {
      id: 'takaful',
      sectorId: 'insurance',
      subsector: '',
      name: 'Takaful',
      icon: '☪',
      color: '#1A237E',
      accent: '#1976D2',
      company: 'Amanah Takaful Group Berhad',
      tagline: 'MYR 4.2B tabarru\' fund — wakalah fee model under BNM IFSA Takaful review.',
      scenario: 'Amanah Takaful Group Berhad manages a MYR 4.2B tabarru\' fund under a wakalah fee model. The BNM IFSA Takaful Operational Framework review is due in 6 weeks. Re-takaful arrangements with Middle East counterparties need renegotiation, and the family takaful segment is facing lapse pressure from new competitors offering lower wakalah fees.',
      files: [
        'INS_01_Pacific_Shield_Insurance.xlsx',
        'INS_02_Pacific_Shield_Strategy.docx'
      ],
      prompts: [
        {
          tool: '🤖 Copilot Chat (Basic)',
          license: 'Free — no M365 Copilot license needed',
          account: 'Sasha Ouellet — SashaO@ABSx62256373.OnMicrosoft.com',
          desc: '',
          prompts: [
            'Explain the difference between the wakalah and mudharabah fee models in takaful in plain language. Which model is more common in Malaysia and why? What are the key considerations a takaful operator must disclose to participants under BNM\'s IFSA Takaful Operational Framework? Keep the explanation under 200 words.',
            'What is the role of a re-takaful arrangement and how does it differ from conventional reinsurance? List three key structuring principles that must be met for a re-takaful arrangement to comply with Shariah requirements, and name two major Middle Eastern re-takaful operators that are active in Southeast Asia.',
            'Draft a simple FAQ for family takaful participants who are asking about lapse consequences. The FAQ should cover: what happens to the tabarru\' fund contribution if they lapse, whether they can reinstate a lapsed certificate, the qard (loan) provision if the fund is insufficient, and the surrender value calculation. Use plain, jargon-free language.'
          ]
        },
        {
          tool: '🔍 Researcher',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via Microsoft 365 Copilot Chat (copilot.microsoft.com or Teams) > click Agents > Researcher. Grounds answers in live web sources and your organisation data with full citations.',
          prompts: [
            'Research the competitive landscape for family takaful in Malaysia — specifically how new digital takaful operators are pricing their wakalah fees versus established operators. I need market data on average wakalah fee rates, the fastest-growing takaful distribution channels, and any BNM statements on competitive pricing in takaful. Provide citations.',
            'Research BNM\'s IFSA Takaful Operational Framework requirements updated since 2023. What are the key changes operators must implement? Specifically, what are the requirements around tabarru\' fund surplus distribution, waqf-linked takaful, and participant disclosure? Present as a compliance checklist.'
          ]
        },
        {
          tool: '📊 Analyst',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via Microsoft 365 Copilot Chat > click Agents > Analyst. Upload an Excel or CSV file. Analyst runs Python-style analysis, builds charts, and interprets results without you writing a single formula.',
          prompts: [
            'Upload INS_01_Pacific_Shield_Insurance.xlsx (use as takaful portfolio proxy). Ask Analyst: Analyse the tabarru\' fund surplus/deficit trend over the past 8 quarters. Is the fund trending toward deficit? Calculate the required additional contribution rate increase to maintain a 15% surplus buffer. Show as a chart and a sensitivity table under three scenarios: claims stay flat, claims rise 10%, claims rise 20%.',
            'Upload INS_01_Pacific_Shield_Insurance.xlsx. Ask: Compare lapse rates across the three main family takaful product categories. Which product has the highest lapse rate and at what certificate duration does lapsing peak? Create a lapse rate heat map by product and certificate age (years 1 through 5).'
          ]
        },
        {
          tool: '📊 Copilot in Excel',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open INS_01_Pacific_Shield_Insurance.xlsx. Navigate to the relevant sheet. Ask Copilot: Build a tabarru\' fund sustainability model on a new sheet. Inputs: current fund balance of MYR 4.2B, annual new contribution inflow, claims outgo, wakalah fee deduction (15% of contributions), and investment income at 4.8% return. Show a 5-year projection under three scenarios: no growth, 5% contribution growth, and 10% lapse increase. Highlight in red any scenario where the fund balance drops below the BNM minimum surplus threshold.',
            'Ask Copilot: Create a wakalah fee benchmarking table comparing Amanah Takaful\'s 15% wakalah fee against the five largest family takaful operators in Malaysia. For each competitor, show the wakalah fee rate, market share, and 5-year lapse rate trend. Source: use data from the portfolio sheet and add competitor data manually where available.',
            'Ask Copilot: In the Re-Takaful Arrangements sheet, identify the three largest re-takaful treaties by ceded premium. For each, calculate the cession ratio, the retention after re-takaful, and the expiry date. Flag any treaty expiring within 6 months that has not been marked as "Renewal In Progress".'
          ]
        },
        {
          tool: '📝 Copilot in Word',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open INS_02_Pacific_Shield_Strategy.docx. Ask Copilot: Draft a 2-page BNM IFSA Takaful Operational Framework compliance readiness assessment. Structure: (1) Key framework requirements, (2) Our current compliance status for each (Compliant / Partial / Gap), (3) Action plan for the 3 gap areas, (4) Timeline to full compliance before the review in 6 weeks. Use a formal regulatory tone.',
            'Ask Copilot: Draft a re-takaful renegotiation brief for the CFO. Cover: the three re-takaful treaties being renegotiated, the current terms, our negotiating objectives (target cession ratio reduction from 40% to 32%, maintain catastrophe cover), the walk-away terms, and a BATNA (Best Alternative to a Negotiated Agreement). Keep it to one page.',
            'Ask Copilot: Write a participant communication explaining the annual tabarru\' fund surplus distribution. The letter should explain how the surplus was calculated, how much each participant will receive based on their contribution, the payment date, and the option to donate their surplus to a waqf fund. Keep it warm and clear, under 300 words.'
          ]
        },
        {
          tool: '🎯 Copilot in PowerPoint',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Ask Copilot in PowerPoint: Create an 8-slide BNM IFSA compliance presentation for the Board Shariah and Audit Committee. Include: (1) IFSA framework overview and key changes, (2) Our compliance status — RAG dashboard, (3) Top 3 gap areas and remediation plan, (4) Re-takaful renegotiation update, (5) Tabarru\' fund sustainability — 5-year projection, (6) Lapse rate concern and retention strategy, (7) Key risks and mitigants, (8) Decisions required. Use a teal and gold Islamic-themed design.',
            'Ask Copilot: Add a one-page Shariah compliance declaration slide that can be included in our annual report. It should confirm that all products and investments comply with the BNM Shariah Advisory Council standards, reference the specific fatwas relied upon, and include a quote from our Shariah Committee Chairman.',
            'Ask Copilot: Create a 3-slide mini-presentation on our lapse reduction strategy for the agency network. Slides: (1) Current lapse rate by product and agent tier, (2) Root causes — top 3 reasons participants lapse, (3) Retention action plan with agent incentives. Keep it simple — this will be shown at a branch level town hall.'
          ]
        },
        {
          tool: '📧 Copilot in Outlook',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Ask Copilot in Outlook: Draft a formal letter to BNM\'s Takaful Supervision Unit ahead of the IFSA review. The letter should: confirm we have received the review schedule, provide a brief self-assessment of our compliance status, note two areas where we are seeking regulatory guidance, and request a pre-review engagement meeting. Use formal BNM correspondence tone.',
            'Ask Copilot: Draft a re-takaful renegotiation invitation letter to our three Middle Eastern re-takaful counterparties. The letter should: acknowledge the expiry of the current treaties, propose a face-to-face negotiation meeting in Kuala Lumpur or Dubai, outline our key negotiating priorities, and suggest three available weeks for the meeting.',
            'Ask Copilot: Summarise the last 3 months of email correspondence with our largest re-takaful counterparty. Identify their key concerns, any commitments we made in writing, and any open items that need to be resolved before treaty renewal.'
          ]
        },
        {
          tool: '🎙 Copilot in Teams',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Use your OWN existing recorded Teams meetings. Open a meeting recap in Teams > Recap tab. Copilot generates summaries, action items, and follow-up drafts grounded in the actual transcript.',
          prompts: [
            'Open an existing recorded Teams meeting recap from a risk or compliance committee. Ask Copilot: Identify all IFSA compliance-related action items discussed. For each, note the owner, the deadline, and whether it was marked as completed or still pending at the time of the meeting.',
            'Ask Copilot: Draft a post-meeting summary for the Re-Takaful Renegotiation Taskforce based on this meeting. Include: key terms agreed, points still in negotiation, the next negotiation round date, and the escalation path if the parties cannot reach agreement on the cession ratio.',
            'Ask Copilot: Were any Shariah compliance concerns raised in this meeting? List each concern with the context and the proposed resolution. Flag any that will require Shariah Committee sign-off before implementation.'
          ]
        },
        {
          tool: '📓 Copilot Notebook',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via copilot.microsoft.com > Notebook tab. Upload up to 5 files and set a system instruction. Best for synthesising insights across multiple documents simultaneously.',
          prompts: [
            'Upload INS_01_Pacific_Shield_Insurance.xlsx and INS_02_Pacific_Shield_Strategy.docx. Set instruction: "You are a takaful expert advising the CEO on BNM IFSA compliance and competitive positioning." Ask: Based on the portfolio data and our strategy, what is the single biggest risk to our tabarru\' fund sustainability over the next 3 years? What one action should the Board approve immediately to address it?',
            'Upload INS_01_Pacific_Shield_Insurance.xlsx and INS_02_Pacific_Shield_Strategy.docx. Ask: Our wakalah fee of 15% is above the market median of 12%. The strategy document commits to growing family takaful market share. Are these two objectives consistent? What would we need to do to reduce the wakalah fee to 12% without impairing profitability, and how long would the transition take?'
          ]
        },
        {
          tool: '🤝 Cowork (Frontier)',
          license: 'M365 Copilot + Frontier Program',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Cowork is an autonomous agent that takes actions across Microsoft 365 on your behalf — sending emails, scheduling meetings, creating documents, posting in Teams, and scheduling recurring tasks. Access: m365.cloud.microsoft > left nav > Agents > Cowork. Requires Frontier program enrollment.',
          prompts: [
            'Do all of the following: (1) Research the latest BNM IFSA Takaful Operational Framework updates and any accompanying guidance notes published since 2024. (2) Summarise the 5 most critical requirements in a compliance action plan document. (3) Save to OneDrive as "IFSA Takaful Compliance Action Plan - [Date]". (4) Email to the Chief Compliance Officer and Head of Shariah Compliance asking for review and sign-off by Wednesday. (5) Schedule a 2-hour IFSA Compliance Readiness Workshop for Thursday with the compliance, product, and operations teams.',
            'Do all of the following for the lapse reduction initiative: (1) Identify all family takaful certificates that have been inactive (no premium payment) for 60–90 days and are at risk of lapsing. (2) Draft a personalised re-engagement message to each participant — the message should remind them of their takaful coverage, explain the lapse consequence, and offer a payment extension. (3) Send the messages via email to all identified participants. (4) Create a tracking log in SharePoint with participant name, certificate number, last payment date, and re-engagement email sent date. (5) Schedule a follow-up check for 2 weeks later to identify who has resumed payment.'
          ]
        },
        {
          tool: '🤖 Word Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to a Word document. Open the .docx in Word for Web > Copilot pane > + New Agent > name it, write a description, set the document as knowledge source > Share. Colleagues chat with it in Teams or M365 Copilot.',
          prompts: [
            'Open INS_02_Pacific_Shield_Strategy.docx in Word for Web. Create an agent called "Takaful Operations Policy Bot". Description: "Answers questions from operations staff, agents, and Shariah compliance teams about Amanah Takaful\'s operational policies, IFSA compliance requirements, and product structures." Share with the takaful operations and compliance teams.',
            'Demo: Ask the agent "A participant wants to increase their tabarru\' contribution mid-term. What is the process, and does it require a new medical underwriting assessment? Is there a minimum increase amount?" Show how the agent gives a policy-accurate response that the operations team can act on confidently.'
          ]
        },
        {
          tool: '🤖 PowerPoint Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to a PowerPoint presentation. Great for strategy decks or Board presentations many people need to reference. Same setup as Word Agent but using a .pptx file.',
          prompts: [
            'Create a PowerPoint from the IFSA Board compliance presentation. Create an agent called "IFSA Compliance Board Bot". Share with Board members and the Shariah Committee.',
            'Demo: A Shariah Committee member asks "What is our current tabarru\' fund surplus ratio and what is the minimum BNM requires before we can distribute surplus to participants?" Show how the agent provides a precise, data-grounded answer based on the presentation content.'
          ]
        },
        {
          tool: '🤖 Excel Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to an Excel workbook. Colleagues ask data questions in plain English without opening Excel. Open .xlsx in Excel for Web > Copilot pane > + New Agent > set workbook as knowledge source > share.',
          prompts: [
            'Open INS_01_Pacific_Shield_Insurance.xlsx in Excel for Web. Create an agent called "Takaful Fund Analytics Q&A". Description: "Answers questions about Amanah Takaful\'s fund performance, lapse rates, re-takaful cession ratios, and wakalah fee benchmarks." Share with actuarial and senior management.',
            'Demo: Ask "What is the current lapse rate for family takaful policies in their second year of contribution?" Then: "If lapse rates increase by 15%, by how much would the tabarru\' fund balance decline in year 1, assuming all other factors remain constant?" Show how management gets scenario intelligence rapidly.'
          ]
        },
        {
          tool: '🏗 Agent Builder (Copilot Studio)',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Build a custom declarative agent in Copilot Studio — no coding required. Access: copilotstudio.microsoft.com > Create > New Agent. Add name, description, knowledge sources (SharePoint URLs or uploaded files), topics/actions. Publish to Teams in under 10 minutes.',
          prompts: [
            'Go to copilotstudio.microsoft.com > Create > New Agent. Name it "Amanah Takaful Participant Assistant". Description: "Helps participants and agents answer questions about family takaful coverage, contributions, tabarru\' fund surplus, lapse consequences, and Shariah compliance — grounded in official takaful documents and policy terms." Upload INS_02_Pacific_Shield_Strategy.docx. Add topics: "Coverage Questions", "Contribution & Payment", "Lapse & Reinstatement", "Surplus Distribution". Publish to Teams and the participant self-service portal.',
            'Demo the agent: A participant asks "I missed two months of contributions due to a medical emergency. Can I reinstate my certificate and what is the grace period? Will my existing coverage remain valid during the reinstatement process?" Show how the agent gives a complete, Shariah-compliant response that helps the participant make an informed decision.'
          ]
        }
      ]
    },
    {
      id: 'hospital-network',
      sectorId: 'healthcare',
      subsector: '',
      name: 'Hospital Network',
      icon: '🏥',
      color: '#1B5E20',
      accent: '#2E7D32',
      company: 'Apex Health Group Berhad',
      tagline: '18.4% nurse attrition + 6-week oncology wait — MYR 2.84B revenue at risk.',
      scenario: 'Apex Health Group Berhad operates 12 hospitals across Malaysia and Indonesia with MYR 2.84B in revenue. Nurse attrition has reached 18.4%, creating ward coverage gaps. Oncology waiting time has stretched to 6 weeks against a 2-week clinical target. A Ministry of Health accreditation review is due in 10 weeks.',
      files: [
        'HC_01_Apex_Health_Group.xlsx',
        'HC_02_Apex_Health_Strategy.docx'
      ],
      prompts: [
        {
          tool: '🤖 Copilot Chat (Basic)',
          license: 'Free — no M365 Copilot license needed',
          account: 'Sasha Ouellet — SashaO@ABSx62256373.OnMicrosoft.com',
          desc: '',
          prompts: [
            'I am the COO of a private hospital group managing 12 hospitals across Malaysia and Indonesia. Nurse attrition has reached 18.4% — nearly double the industry benchmark of 10%. Draft a structured root cause analysis framework I can use to run a half-day workshop with my nursing directors. The framework should identify the five most common reasons nurses leave private hospitals in Southeast Asia, suggest data sources to validate each hypothesis, and propose one intervention per root cause that can be implemented within 60 days without significant capital outlay.',
            'Explain the MOH Malaysia hospital accreditation process — what is the scope of review, what clinical and administrative standards are assessed, and what are the consequences for a private hospital that fails the inspection? I need to brief my Board in 5 minutes, so keep the answer to 150 words.',
            'What are the five most effective evidence-based interventions to reduce oncology waiting times in a private hospital setting? For each intervention, indicate the typical implementation timeline, estimated cost range, and the clinical benefit in terms of waiting time reduction. Focus on approaches that can be implemented with existing technology and staff.'
          ]
        },
        {
          tool: '🔍 Researcher',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via Microsoft 365 Copilot Chat (copilot.microsoft.com or Teams) > click Agents > Researcher. Grounds answers in live web sources and your organisation data with full citations.',
          prompts: [
            'Research nurse retention strategies used by private hospital groups in Southeast Asia that have successfully reduced attrition from above 15% to below 10% within 18 months. I need: (1) The specific interventions used, (2) The cost per FTE of implementing the programme, (3) The return on investment compared to replacement cost. Provide citations from healthcare management journals or industry reports.',
            'Research the regulatory environment for private hospitals in Malaysia — specifically the Private Healthcare Facilities and Services Act (PHFSA) requirements for clinical staffing ratios, patient safety reporting, and data protection for medical records. Summarise the five most critical compliance obligations and recent MOH enforcement actions. Cite sources.'
          ]
        },
        {
          tool: '📊 Analyst',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via Microsoft 365 Copilot Chat > click Agents > Analyst. Upload an Excel or CSV file. Analyst runs Python-style analysis, builds charts, and interprets results without you writing a single formula.',
          prompts: [
            'Upload HC_01_Apex_Health_Group.xlsx to Analyst. Ask: Analyse nurse attrition data by hospital, department, and seniority band (junior 0-3 years, mid 4-7 years, senior 8+ years). Which hospital has the highest attrition? Which seniority band is leaving fastest? Calculate the annual replacement cost per nurse (assume MYR 18,000 in recruitment and training cost per hire) and the total group-level cost of current attrition. Present as a heat map table and a cost waterfall chart.',
            'Upload HC_01_Apex_Health_Group.xlsx. Ask Analyst: Analyse the oncology department waiting time data across all 12 hospitals. Which hospitals have the longest average waiting time for first oncologist consultation? Calculate the revenue at risk — assume each week of excess wait costs 1.4% patient leakage to competitor hospitals and each oncology patient generates MYR 85,000 in average annual revenue. Show as a ranked table and a bar chart.'
          ]
        },
        {
          tool: '📊 Copilot in Excel',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open HC_01_Apex_Health_Group.xlsx. Navigate to the Workforce Planning sheet. Ask Copilot: Create a nurse attrition prediction model. For each hospital, calculate: (1) current attrition rate, (2) projected ward coverage gap if attrition continues at the same rate for 6 more months, (3) the minimum number of new nurse hires required to maintain safe patient-to-nurse ratios. Flag any hospital in red where the coverage gap exceeds 15%.',
            'Ask Copilot: Build an MOH accreditation readiness tracker on a new sheet. List the 20 key accreditation criteria from the strategy document. For each criterion, add columns: Current Status (Compliant/Gap/Unknown), Evidence Required, Responsible Department, and Target Completion Date. Apply conditional formatting: green for Compliant, yellow for In Progress, red for Gap.',
            'Ask Copilot: In the Revenue by Specialty sheet, calculate the revenue contribution of oncology, cardiology, and orthopaedics as a percentage of total group revenue for each of the last 4 years. Show the trend as a stacked area chart. Flag any specialty where revenue share has declined more than 3 percentage points year-on-year.'
          ]
        },
        {
          tool: '📝 Copilot in Word',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open HC_02_Apex_Health_Strategy.docx. Ask Copilot: Draft a nurse retention action plan of 2 pages. Cover: (1) Current attrition rate and financial impact, (2) Three root causes identified from our exit interview data, (3) Five specific retention interventions with timelines and costs, (4) KPIs: target attrition rate of 12% within 6 months, (5) Governance — who is accountable. Write in a formal healthcare management style.',
            'Ask Copilot in Word: Identify all sections in this strategy document that reference clinical quality or patient safety. Summarise each section\'s key commitment in one sentence and create a compliance gap table showing which commitments have measurable KPIs and which do not.',
            'Ask Copilot: Draft a 300-word CEO statement for the group\'s MOH accreditation submission. The statement should demonstrate commitment to patient safety, acknowledge the oncology waiting time challenge and the corrective actions underway, and reaffirm the group\'s investment in clinical excellence and nursing capability.'
          ]
        },
        {
          tool: '🎯 Copilot in PowerPoint',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Ask Copilot in PowerPoint: Create a 10-slide Board presentation titled "Clinical Operations Transformation — FY2026 Priorities". Include: (1) Executive summary — key challenges (attrition, oncology wait, accreditation), (2) Nurse attrition dashboard, (3) Root cause analysis, (4) Retention programme — 5 initiatives, (5) Oncology capacity expansion plan, (6) MOH accreditation readiness — RAG status, (7) Financial impact if we solve vs do nothing, (8) Capital investment required, (9) Risk register, (10) Board decisions required. Use a professional green and white colour scheme.',
            'Ask Copilot: For each slide, write speaker notes that anticipate Board questions. The Chairman has a clinical background, so the notes should go deeper on patient safety implications than on financials.',
            'Ask Copilot: Create a one-slide oncology waiting time comparison chart showing our 6-week average against the 2-week clinical target and the 3.5-week industry benchmark for private hospitals in Malaysia. Add a call-out box showing the estimated annual revenue at risk from patient leakage.'
          ]
        },
        {
          tool: '📧 Copilot in Outlook',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Ask Copilot in Outlook: Draft a letter to the MOH accreditation team requesting a 30-day extension on the submission of our clinical staffing compliance documentation. The letter should acknowledge the reason for the delay (nursing staff restructuring in progress), describe the remediation actions we have taken, and provide a specific new submission date. Use the formal tone required for MOH correspondence.',
            'Ask Copilot: Draft an internal email to all 12 Hospital Directors briefing them on the MOH accreditation review in 10 weeks. The email should: list the 5 highest-risk accreditation criteria based on our gap assessment, assign each Hospital Director specific pre-inspection actions, request confirmation of their hospital\'s readiness status by next Friday, and stress the importance of accurate, consistent documentation.',
            'Ask Copilot: I have received 3 complaints from oncology patients about their waiting time. Draft personalised, empathetic response emails for each patient that: acknowledge the delay without making legal admissions, explain what steps we are taking to reduce waiting times, and offer to personally expedite their case review. Use a warm, caring tone appropriate for clinical communication.'
          ]
        },
        {
          tool: '🎙 Copilot in Teams',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Use your OWN existing recorded Teams meetings. Open a meeting recap in Teams > Recap tab. Copilot generates summaries, action items, and follow-up drafts grounded in the actual transcript.',
          prompts: [
            'Open a recorded Teams meeting recap from a clinical leadership or operations committee meeting. Ask Copilot: Identify all patient safety issues discussed, the corrective actions committed to, and any incidents that require escalation to the MOH or the Medical Advisory Board. Format as a clinical governance meeting summary.',
            'Ask Copilot in the recap: Draft follow-up action items for the nurse retention taskforce. Include: the specific hospital or department where each action applies, the nurse manager responsible, the completion deadline, and the KPI that will confirm the action was effective.',
            'Ask Copilot: Were any specific financial figures discussed in this meeting related to attrition costs or oncology revenue? Extract and list them with context so I can update the financial impact model.'
          ]
        },
        {
          tool: '📓 Copilot Notebook',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via copilot.microsoft.com > Notebook tab. Upload up to 5 files and set a system instruction. Best for synthesising insights across multiple documents simultaneously.',
          prompts: [
            'Upload HC_01_Apex_Health_Group.xlsx and HC_02_Apex_Health_Strategy.docx to Copilot Notebook. Set instruction: "You are a healthcare management consultant. Help the COO prioritise clinical and operational interventions." Ask: Based on the workforce and revenue data and our strategic priorities, which single intervention — nurse retention programme or oncology capacity expansion — will deliver the highest financial return within 12 months? Show the reasoning and key assumptions.',
            'Upload HC_01_Apex_Health_Group.xlsx and HC_02_Apex_Health_Strategy.docx. Ask: The strategy document commits to expanding oncology services to 3 new hospitals. The workforce data shows we already have a nursing shortage in our existing hospitals. Are these two objectives compatible? What workforce plan would be needed before the oncology expansion can proceed safely?'
          ]
        },
        {
          tool: '🤝 Cowork (Frontier)',
          license: 'M365 Copilot + Frontier Program',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Cowork is an autonomous agent that takes actions across Microsoft 365 on your behalf — sending emails, scheduling meetings, creating documents, posting in Teams, and scheduling recurring tasks. Access: m365.cloud.microsoft > left nav > Agents > Cowork. Requires Frontier program enrollment.',
          prompts: [
            'Do all of the following for MOH accreditation prep: (1) Research MOH Malaysia\'s latest PHFSA inspection criteria updated in 2024 or 2025. (2) Draft a 10-point pre-inspection checklist for Hospital Directors covering the highest-risk compliance areas. (3) Save to OneDrive as "MOH Accreditation Pre-Inspection Checklist". (4) Email to all 12 Hospital Directors with subject "Action Required: MOH Accreditation Prep — 10 Weeks to Inspection" asking each to complete the self-assessment and return it within 2 weeks. (5) Schedule a 90-minute Group Clinical Governance Review via Teams for 3 weeks before the inspection date.',
            'Do all of the following for nurse retention: (1) Identify the 3 hospitals with the highest nurse attrition rates from the data. (2) Draft personalised retention initiative proposals for each hospital — customised based on their specific attrition drivers. (3) Email the proposals to each Hospital Director and Nursing Director. (4) Create a retention programme tracker spreadsheet in OneDrive with weekly attrition rate tracking for each hospital. (5) Post in the #clinical-operations Teams channel: "Nurse Retention Programme launched for 3 priority hospitals — see OneDrive for trackers."'
          ]
        },
        {
          tool: '🤖 Word Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to a Word document. Open the .docx in Word for Web > Copilot pane > + New Agent > name it, write a description, set the document as knowledge source > Share. Colleagues chat with it in Teams or M365 Copilot.',
          prompts: [
            'Open HC_02_Apex_Health_Strategy.docx in Word for Web. Create an agent called "Clinical Governance Policy Bot". Description: "Answers questions from Hospital Directors, nursing managers, and clinical staff about Apex Health\'s clinical governance policies, MOH accreditation requirements, staffing ratios, and patient safety protocols." Share with all 12 hospitals.',
            'Demo: A nursing manager asks "What is the minimum nurse-to-patient ratio for a general medical ward during night shift under our current policy? And what is the escalation procedure if we fall below the minimum due to unexpected absenteeism?" Show how the agent provides an immediate, policy-grounded answer.'
          ]
        },
        {
          tool: '🤖 PowerPoint Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to a PowerPoint presentation. Great for strategy decks or Board presentations many people need to reference. Same setup as Word Agent but using a .pptx file.',
          prompts: [
            'Create a PowerPoint from the Board presentation and open in PowerPoint for Web. Create an agent called "Clinical Ops Board Q&A Bot". Share with Board members and the Medical Advisory Board.',
            'Demo: A Board member asks "If we implement all 5 nurse retention initiatives, what is the projected attrition rate at the end of FY2026 and what does that mean for ward coverage at our largest hospital?" Show how Board members get scenario-specific answers before the meeting.'
          ]
        },
        {
          tool: '🤖 Excel Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to an Excel workbook. Colleagues ask data questions in plain English without opening Excel. Open .xlsx in Excel for Web > Copilot pane > + New Agent > set workbook as knowledge source > share.',
          prompts: [
            'Open HC_01_Apex_Health_Group.xlsx in Excel for Web. Create an agent called "Apex Health Operations Q&A". Description: "Instant answers on nurse attrition, oncology waiting times, revenue by specialty, and MOH compliance indicators for COO and Hospital Directors." Share with clinical and operational leadership.',
            'Demo: Ask "Which hospital has the lowest nurse retention rate and what is the current patient-to-nurse ratio in its ICU?" Then: "How much revenue did oncology generate across the group in FY2025 and which hospital contributed the most?" Show how the COO gets rapid operational intelligence.'
          ]
        },
        {
          tool: '🏗 Agent Builder (Copilot Studio)',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Build a custom declarative agent in Copilot Studio — no coding required. Access: copilotstudio.microsoft.com > Create > New Agent. Add name, description, knowledge sources (SharePoint URLs or uploaded files), topics/actions. Publish to Teams in under 10 minutes.',
          prompts: [
            'Go to copilotstudio.microsoft.com > Create > New Agent. Name it "Apex Health Clinical Assistant". Description: "Supports clinical and operations teams across all 12 Apex Health hospitals — answers questions on clinical governance policies, nurse staffing standards, MOH accreditation requirements, and patient safety protocols. Ensures consistent, policy-grounded responses across the hospital network." Upload HC_02_Apex_Health_Strategy.docx. Add topics: "Staffing Standards", "MOH Accreditation", "Patient Safety", "Oncology Protocols". Publish to Teams for all hospital staff.',
            'Demo the agent: A junior doctor asks: "A patient in my oncology clinic has been waiting 8 weeks for their second chemotherapy cycle due to scheduling issues. What is the clinical escalation pathway and am I required to file an incident report? Who do I notify?" Show how the agent gives a clear, policy-grounded escalation guidance that protects both the patient and the clinician.'
          ]
        }
      ]
    },
    {
      id: 'pharmaceutical',
      sectorId: 'healthcare',
      subsector: '',
      name: 'Pharmaceutical',
      icon: '💊',
      color: '#2E7D32',
      accent: '#388E3C',
      company: 'ZavaGen Pharmaceutical (Zava Pharma)',
      tagline: '3 BPOM enforcement notices closed — Sitagliptin 100mg BPfK registration in progress.',
      scenario: 'ZavaGen Pharmaceutical is the pharmaceutical arm of Zava Group, operating plants in Cikarang (Indonesia) and Johor (Malaysia). Three BPOM enforcement notices were received and all closed as of April 2025. BPfK registration for Sitagliptin 100mg is in progress. Four products are in Phase II/III clinical trials. GMP certification renewal is due in 3 months.',
      files: [
        '17_Zava_Pharma_Pipeline.xlsx',
        'Email_11_Sitagliptin_BPOM_Registration.docx'
      ],
      prompts: [
        {
          tool: '🤖 Copilot Chat (Basic)',
          license: 'Free — no M365 Copilot license needed',
          account: 'Sasha Ouellet — SashaO@ABSx62256373.OnMicrosoft.com',
          desc: '',
          prompts: [
            'I am the Head of Regulatory Affairs at a pharmaceutical company with manufacturing plants in Malaysia and Indonesia. We have just closed three BPOM enforcement notices and need to demonstrate to BPOM and our investors that our quality management system is now fully compliant. Draft a 300-word regulatory remediation statement that I can use in investor communications and regulatory correspondence. The statement should acknowledge the issues, explain the root cause at a high level, describe the corrective and preventive actions (CAPAs) implemented, and assert our current compliance status without creating liability.',
            'Explain the difference between BPOM (Indonesia) and BPfK (Malaysia) drug registration processes for a generic pharmaceutical product. What are the key differences in documentation requirements, review timelines, and post-approval obligations? Keep the answer under 250 words and suitable for briefing a CEO who is not a regulatory expert.',
            'What are the GMP (Good Manufacturing Practice) requirements under ASEAN harmonised guidelines for pharmaceutical tablet manufacturing? List the five most critical areas an inspector looks at during a GMP audit and the most common findings that lead to a warning letter or enforcement notice.'
          ]
        },
        {
          tool: '🔍 Researcher',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via Microsoft 365 Copilot Chat (copilot.microsoft.com or Teams) > click Agents > Researcher. Grounds answers in live web sources and your organisation data with full citations.',
          prompts: [
            'Research the market opportunity for Sitagliptin (a DPP-4 inhibitor for Type 2 diabetes) in Malaysia and Indonesia. I need: (1) Market size and growth rate for diabetes medications in both countries, (2) Current competitors and their market share, (3) Any pricing regulations or reimbursement status under MOH Malaysia and BPJS Indonesia. Provide citations.',
            'Research the latest ASEAN GMP guidelines updates and any BPOM enforcement trends in the Indonesian pharmaceutical sector in 2024 and 2025. Are there specific areas where enforcement has been more active? Have any major multinational pharmaceutical companies received enforcement actions? Provide citations.'
          ]
        },
        {
          tool: '📊 Analyst',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via Microsoft 365 Copilot Chat > click Agents > Analyst. Upload an Excel or CSV file. Analyst runs Python-style analysis, builds charts, and interprets results without you writing a single formula.',
          prompts: [
            'Upload 17_Zava_Pharma_Pipeline.xlsx to Analyst. Ask: Analyse the clinical trial pipeline — 4 products in Phase II/III. For each product, show the estimated market size, probability of approval (use industry average Phase II→III success rate of 52% and Phase III→approval rate of 68%), and projected revenue at Year 3 post-launch. Rank the pipeline by expected value (market size × approval probability). Present as a ranked table and a bubble chart.',
            'Upload 17_Zava_Pharma_Pipeline.xlsx. Ask: Build a GMP compliance risk dashboard. For each manufacturing site, show: (1) Last GMP inspection date and outcome, (2) Number of open CAPAs by severity (critical, major, minor), (3) Days until next GMP certification renewal. Highlight in red any site with a critical CAPA open for more than 60 days or a renewal due within 90 days.'
          ]
        },
        {
          tool: '📊 Copilot in Excel',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open 17_Zava_Pharma_Pipeline.xlsx. Navigate to the Pipeline sheet. Ask Copilot: Create a product launch revenue model for Sitagliptin 100mg assuming BPfK approval in Q3 FY2026. Assume: Year 1 market share 3%, Year 2 5%, Year 3 8% of a MYR 420M total addressable market. Calculate annual revenue, gross margin at 62%, and contribution after regulatory and marketing costs. Show as a 5-year P&L projection.',
            'Ask Copilot: In the CAPA Tracker sheet, identify all open CAPAs where the target completion date has passed. For each overdue CAPA, calculate the number of days overdue and flag the severity level. Create a summary showing: Total Open CAPAs | Critical Overdue | Major Overdue | Minor Overdue. This summary should be the first thing a BPOM inspector sees.',
            'Ask Copilot: Build a batch release productivity model on a new sheet. For the Cikarang plant, calculate: (1) Average batch release cycle time (days from manufacturing to QA release), (2) Percentage of batches released within the 14-day SLA, (3) Percentage of batches requiring OOS (Out of Specification) investigation. Flag any trend of increasing OOS rate over the last 6 months.'
          ]
        },
        {
          tool: '📝 Copilot in Word',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open Email_11_Sitagliptin_BPOM_Registration.docx. Ask Copilot: Draft a BPfK drug registration covering letter for Sitagliptin 100mg. The letter should: identify the product and applicant, reference the CTD (Common Technical Document) dossier being submitted, highlight the key data supporting safety and efficacy (Phase III results: HbA1c reduction 0.82%, placebo-adjusted), note the ASEAN harmonised registration pathway being used, and request acknowledgement of receipt. Use the formal BPfK correspondence format.',
            'Ask Copilot in Word: Draft a CAPA summary report for submission to BPOM covering the three enforcement notices now closed. For each notice, provide: (1) The original finding, (2) Root cause identified, (3) CAPA implemented, (4) Evidence of effectiveness, (5) Date of closure. Use the BPOM CAPA report format with numbered sections.',
            'Ask Copilot: Draft a GMP audit readiness checklist in Word format. The checklist should cover the 10 key areas a GMP inspector will review: documentation, personnel training, equipment qualification, environmental monitoring, batch records, QA release procedures, deviation management, CAPA system, product complaints, and change control. For each area, include a self-assessment column and an evidence required column.'
          ]
        },
        {
          tool: '🎯 Copilot in PowerPoint',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Ask Copilot in PowerPoint: Create an 8-slide pharmaceutical pipeline investor update presentation for ZavaGen. Include: (1) Company overview and manufacturing footprint, (2) Regulatory compliance update — 3 BPOM notices closed, (3) Pipeline overview — 4 products in Phase II/III, (4) Sitagliptin 100mg — BPfK registration status and market opportunity, (5) GMP certification renewal plan, (6) Financial projections — pipeline NPV, (7) Partnerships and licensing opportunities, (8) Investment thesis. Use a professional blue and white design.',
            'Ask Copilot: Create a 3-slide GMP remediation update for the ZavaGen Cikarang plant. Slides: (1) Before/after — the 3 BPOM enforcement notices and what we fixed, (2) Current GMP compliance scorecard — 10 key criteria with RAG status, (3) GMP certification renewal plan and timeline. Keep it factual and confidence-building for a regulatory audience.',
            'Ask Copilot: Add a risk matrix slide to the investor presentation showing the top 5 risks to our pipeline — regulatory delay, manufacturing failure, competitor generic launch, IP challenge, and market access — each positioned on a likelihood vs impact matrix with a one-line mitigation.'
          ]
        },
        {
          tool: '📧 Copilot in Outlook',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open Email_11_Sitagliptin_BPOM_Registration.docx. Ask Copilot in Outlook: Draft a follow-up email to our BPfK regulatory contact requesting an update on the Sitagliptin 100mg registration status. The submission has been pending for 4 months. The email should be professional and persistent without being aggressive, reference the submission date and dossier reference number, and ask for an estimated review completion timeline.',
            'Ask Copilot: Draft an email to our GMP consultant requesting a pre-audit inspection simulation for the Cikarang plant ahead of the certification renewal in 3 months. The email should specify the scope of the simulation (all 10 GMP areas), the preferred dates (within the next 4 weeks), and request a quote for the engagement.',
            'Ask Copilot: Summarise the email thread in Email_11_Sitagliptin_BPOM_Registration.docx. What are the key outstanding documentation gaps identified by BPfK? List each gap with the section of the dossier it refers to and the deadline for submission.'
          ]
        },
        {
          tool: '🎙 Copilot in Teams',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Use your OWN existing recorded Teams meetings. Open a meeting recap in Teams > Recap tab. Copilot generates summaries, action items, and follow-up drafts grounded in the actual transcript.',
          prompts: [
            'Open an existing recorded Teams meeting recap from a regulatory affairs or quality management meeting. Ask Copilot: Identify all regulatory submission milestones discussed, the current status of each, and any at-risk items where the deadline may be missed. Format as a regulatory affairs status report.',
            'Ask Copilot in the recap: Draft follow-up actions for the GMP certification renewal project. Include: the specific action, the department responsible, the completion deadline, and the dependency on any other action that must come first. Present as a project task list.',
            'Ask Copilot: Were any batch manufacturing issues or quality failures discussed in this meeting? List each with: the product, the nature of the issue, the investigation status, and whether BPOM or BPfK notification was discussed.'
          ]
        },
        {
          tool: '📓 Copilot Notebook',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via copilot.microsoft.com > Notebook tab. Upload up to 5 files and set a system instruction. Best for synthesising insights across multiple documents simultaneously.',
          prompts: [
            'Upload 17_Zava_Pharma_Pipeline.xlsx and Email_11_Sitagliptin_BPOM_Registration.docx to Copilot Notebook. Set instruction: "You are a pharmaceutical regulatory strategist." Ask: Based on our pipeline data and the Sitagliptin registration status, what is the earliest realistic date we can begin generating revenue from our Phase III pipeline? What are the top 3 risks to that timeline and how should we mitigate them?',
            'Upload 17_Zava_Pharma_Pipeline.xlsx and Email_11_Sitagliptin_BPOM_Registration.docx. Ask: Our pipeline has 4 products in Phase II/III. Given that 3 BPOM enforcement notices were recently closed and our GMP certification is up for renewal, is it realistic to pursue all 4 products simultaneously? Should we prioritise and deprioritise based on regulatory risk, market size, or manufacturing complexity? Recommend a portfolio strategy.'
          ]
        },
        {
          tool: '🤝 Cowork (Frontier)',
          license: 'M365 Copilot + Frontier Program',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Cowork is an autonomous agent that takes actions across Microsoft 365 on your behalf — sending emails, scheduling meetings, creating documents, posting in Teams, and scheduling recurring tasks. Access: m365.cloud.microsoft > left nav > Agents > Cowork. Requires Frontier program enrollment.',
          prompts: [
            'Do all of the following: (1) Research the BPfK review timeline for Type 2 diabetes generic medications and identify if there are expedited review pathways available. (2) Draft a BPfK expedited review application letter for Sitagliptin 100mg, citing the unmet need in the Malaysian diabetes patient population. (3) Save to OneDrive as "Sitagliptin BPfK Expedited Review Application". (4) Email to our Regulatory Affairs Director and General Counsel for review by Wednesday. (5) Schedule a Regulatory Strategy Meeting for Thursday with the Head of Regulatory Affairs, CMO, and CFO.',
            'Do all of the following for GMP certification renewal: (1) Compile a pre-audit checklist of all documentation required for the Cikarang plant GMP renewal. (2) Send a request to each department head (QA, Production, Engineering, Warehouse) asking them to self-assess their readiness against the checklist and respond within 5 business days. (3) Schedule a pre-audit simulation with our external GMP consultant for 6 weeks from today. (4) Create a GMP renewal tracker in SharePoint with a column for each of the 10 audit areas and status (Ready/In Progress/Not Ready). (5) Post in the #quality-operations Teams channel: "GMP certification renewal is in 3 months. Pre-audit simulation scheduled. Please complete your self-assessments by [date]."'
          ]
        },
        {
          tool: '🤖 Word Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to a Word document. Open the .docx in Word for Web > Copilot pane > + New Agent > name it, write a description, set the document as knowledge source > Share. Colleagues chat with it in Teams or M365 Copilot.',
          prompts: [
            'Open Email_11_Sitagliptin_BPOM_Registration.docx in Word for Web. Create an agent called "Regulatory Submission Tracker". Description: "Answers questions from the regulatory affairs team about the status of drug registration submissions, outstanding documentation gaps, and correspondence with BPOM and BPfK. Grounded in official regulatory correspondence files." Share with the regulatory affairs team.',
            'Demo: Ask the Regulatory Tracker "What documentation gaps did BPfK identify in the Sitagliptin 100mg dossier review and have all of them been addressed?" Show how the team gets instant, document-grounded status updates without digging through email threads.'
          ]
        },
        {
          tool: '🤖 PowerPoint Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to a PowerPoint presentation. Great for strategy decks or Board presentations many people need to reference. Same setup as Word Agent but using a .pptx file.',
          prompts: [
            'Create a PowerPoint from the pipeline investor presentation. Create an agent called "ZavaGen Pipeline Investor Q&A". Share with investor relations and institutional investors.',
            'Demo: An investor asks "What is the expected approval date for Sitagliptin 100mg and what is the projected market share in Year 2 post-launch in Malaysia?" Show how the IR team handles investor questions consistently using the agent during roadshows.'
          ]
        },
        {
          tool: '🤖 Excel Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to an Excel workbook. Colleagues ask data questions in plain English without opening Excel. Open .xlsx in Excel for Web > Copilot pane > + New Agent > set workbook as knowledge source > share.',
          prompts: [
            'Open 17_Zava_Pharma_Pipeline.xlsx in Excel for Web. Create an agent called "Pharma Pipeline Analytics Q&A". Description: "Answers questions about ZavaGen\'s product pipeline, GMP compliance status, CAPA tracker, and Sitagliptin registration — for the regulatory affairs, QA, and finance teams." Share broadly.',
            'Demo: Ask "How many open CAPAs are there at the Cikarang plant and how many are critical?" Then: "What is the probability-adjusted NPV of our Phase II pipeline assuming 52% transition success rate?" Show how management gets rapid pipeline intelligence.'
          ]
        },
        {
          tool: '🏗 Agent Builder (Copilot Studio)',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Build a custom declarative agent in Copilot Studio — no coding required. Access: copilotstudio.microsoft.com > Create > New Agent. Add name, description, knowledge sources (SharePoint URLs or uploaded files), topics/actions. Publish to Teams in under 10 minutes.',
          prompts: [
            'Go to copilotstudio.microsoft.com > Create > New Agent. Name it "ZavaGen Regulatory Intelligence Bot". Description: "Supports ZavaGen\'s regulatory affairs and quality teams with instant answers on BPOM and BPfK submission requirements, GMP standards, CAPA management, and pipeline registration status. Grounded in regulatory submissions and quality management documents." Upload 17_Zava_Pharma_Pipeline.xlsx and Email_11_Sitagliptin_BPOM_Registration.docx. Add topics: "BPOM Requirements", "BPfK Submission", "GMP Standards", "CAPA Management". Publish to Teams.',
            'Demo the agent: A QA manager at the Cikarang plant asks: "We have discovered a batch of Sitagliptin tablets where the dissolution rate is 2% below the lower specification limit. What is the OOS investigation procedure, do I need to quarantine the batch, and does this need to be reported to BPOM?" Show how the agent walks the QA manager through the correct procedure step by step.'
          ]
        }
      ]
    },
    {
      id: 'og-upstream',
      sectorId: 'og-energy',
      subsector: '',
      name: 'Oil & Gas — Upstream',
      icon: '⛽',
      color: '#E65100',
      accent: '#F57C00',
      company: 'Nusantara Energy Berhad',
      tagline: 'Tier 1 PSE at Miri field — PETRONAS HSE audit in 6 weeks. 2 offshore spill incidents.',
      scenario: 'Nusantara Energy Berhad is an upstream oil and gas operator with a Tier 1 Process Safety Event (PSE) at its Miri offshore field. Two minor offshore spill incidents were reported to PETRONAS in Q3. The HSE audit is scheduled in 6 weeks. Net Zero 2050 commitments require a 30% GHG reduction plan by Q1 FY2027.',
      files: [
        'OG_01_Nusantara_Energy.xlsx',
        'OG_02_Nusantara_HSE_Report.docx',
        'Email_04_PETRONAS_Meeting_Prep.docx'
      ],
      prompts: [
        {
          tool: '🤖 Copilot Chat (Basic)',
          license: 'Free — no M365 Copilot license needed',
          account: 'Sasha Ouellet — SashaO@ABSx62256373.OnMicrosoft.com',
          desc: '',
          prompts: [
            'I am the Head of HSE at a Malaysian upstream oil and gas company. We have experienced two minor offshore spill incidents this quarter and a Tier 1 Process Safety Event at our Miri field. A PETRONAS HSE audit is in 6 weeks. Draft a 300-word incident investigation brief I can use to brief the PETRONAS audit team. The brief should: describe the nature of the Tier 1 PSE without minimising it, explain the investigation methodology used, summarise the root cause findings, and list the corrective actions implemented. Tone: transparent, professional, and accountability-focused.',
            'Explain the PETRONAS Process Safety Management (PSM) framework for upstream offshore operations. What are the five key elements of the framework, what does a Tier 1 PSE classification mean, and what are the regulatory reporting obligations under the Malaysia Energy Commission (ST) and Department of Environment (DOE) following such an event?',
            'What are the best practices for managing GHG emissions in upstream offshore oil and gas operations? Focus on practical measures that can be implemented within 12–18 months without major capital investment. Include examples of measures used by operators in Southeast Asia and their typical GHG reduction impact in percentage terms.'
          ]
        },
        {
          tool: '🔍 Researcher',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via Microsoft 365 Copilot Chat (copilot.microsoft.com or Teams) > click Agents > Researcher. Grounds answers in live web sources and your organisation data with full citations.',
          prompts: [
            'Research PETRONAS HSE audit requirements and the typical findings that upstream operators receive. I need: (1) The key HSE performance indicators PETRONAS measures during audits, (2) The most common non-conformances issued to upstream operators in Malaysia in 2023–2025, (3) Any PETRONAS HSE circulars or updates issued in the past 12 months. Provide citations.',
            'Research global upstream oil and gas Net Zero 2050 strategies adopted by operators of similar scale to Nusantara Energy (production 50,000–100,000 BOE/day). What are the most cost-effective GHG reduction levers? How are operators in Southeast Asia balancing production growth with decarbonisation commitments? Cite recent industry reports.'
          ]
        },
        {
          tool: '📊 Analyst',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via Microsoft 365 Copilot Chat > click Agents > Analyst. Upload an Excel or CSV file. Analyst runs Python-style analysis, builds charts, and interprets results without you writing a single formula.',
          prompts: [
            'Upload OG_01_Nusantara_Energy.xlsx to Analyst. Ask: Analyse the HSE incident data for the past 3 years. What is the trend in Total Recordable Incident Rate (TRIR), Lost Time Incident Rate (LTIR), and Process Safety Events (PSE) by severity tier? Are incidents concentrated at specific offshore platforms or in specific operations (drilling, production, maintenance)? Create a trend chart and an incident heat map by platform.',
            'Upload OG_01_Nusantara_Energy.xlsx. Ask: Build a GHG emissions analysis. Show Scope 1 and Scope 2 emissions by platform and operating unit for FY2023–FY2025. Calculate the GHG intensity (tCO2e per BOE produced). Identify the 3 highest-emitting platforms and estimate the GHG reduction potential if each implemented the top emission reduction measure appropriate for that platform type. Show as a ranked table with reduction potential in tCO2e and as a percentage of total Scope 1 emissions.'
          ]
        },
        {
          tool: '📊 Copilot in Excel',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open OG_01_Nusantara_Energy.xlsx. Navigate to the HSE KPI sheet. Ask Copilot: Create a PETRONAS HSE audit readiness dashboard on a new sheet. For each of the 12 key HSE performance indicators PETRONAS measures, show: (1) Our current performance, (2) PETRONAS threshold, (3) Status (Above/Below threshold), (4) Trend (Improving/Stable/Deteriorating). Highlight in red any indicator that is below threshold and deteriorating.',
            'Ask Copilot: Build a corrective action plan (CAP) tracker on a new sheet. List all open CAPAs from the Tier 1 PSE investigation and the two spill incidents. For each CAPA, include: Description | Root Cause Category | Priority (Critical/High/Medium) | Owner | Due Date | Status | % Complete. Apply conditional formatting: overdue critical items in red, overdue high items in orange.',
            'Ask Copilot: In the Production Data sheet, calculate the production uptime percentage for each offshore platform over the past 4 quarters. Identify which platforms have experienced the most unplanned shutdowns and whether there is a correlation between unplanned shutdowns and the incidents in the HSE data sheet. Show as a scatter plot.'
          ]
        },
        {
          tool: '📝 Copilot in Word',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open OG_02_Nusantara_HSE_Report.docx. Ask Copilot: Rewrite the Executive Summary of this HSE report to address the PETRONAS audit team directly. The new summary should: acknowledge the Tier 1 PSE transparently, demonstrate that our incident investigation followed PETRONAS PSM guidelines, highlight the 5 most significant corrective actions implemented, and project our target TRIR for the next 12 months. Use a confident but accountable regulatory tone.',
            'Ask Copilot in Word: Create a Net Zero 2050 GHG reduction roadmap section for the annual sustainability report. Cover: (1) Our current Scope 1+2 baseline in tCO2e, (2) 5 key reduction levers — flare reduction, electrification, energy efficiency, methane leak detection, and carbon capture feasibility, (3) 2030 interim target: 30% reduction vs 2020 baseline, (4) Investment required and payback period for each lever. Format as a structured narrative with a table.',
            'Ask Copilot: Draft a PETRONAS pre-audit submission letter. The letter should: confirm our readiness for the scheduled audit, provide a summary of corrective actions since the last audit, highlight our HSE improvement initiatives, and request 30 minutes at the start of the audit for a management presentation. Use the formal correspondence format required for PETRONAS regulatory submissions.'
          ]
        },
        {
          tool: '🎯 Copilot in PowerPoint',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Ask Copilot in PowerPoint: Create a 12-slide PETRONAS HSE audit management presentation. Include: (1) Company overview and operational scope, (2) HSE performance dashboard — 3-year trend, (3) Tier 1 PSE — incident, investigation, root cause, (4) Corrective actions implemented — CAPA tracker summary, (5) Two spill incidents — cause and remediation, (6) HSE management system maturity assessment, (7) Contractor HSE performance, (8) Emergency response readiness, (9) Net Zero 2050 — GHG reduction roadmap, (10) HSE investment plan FY2026, (11) Key risks and mitigants, (12) Our commitment to PETRONAS HSE standards. Use a dark green and white professional colour scheme.',
            'Ask Copilot: For each slide, generate speaker notes that anticipate the PETRONAS audit team\'s follow-up questions. The audit lead is known to probe hard on root cause analysis quality — the notes should show that we have used structured RCA methodology (such as 5-Why or Bowtie).',
            'Ask Copilot: Add a bowtie diagram on slide 3 showing the Tier 1 PSE event — the threat on the left, the top event in the middle, the consequences on the right, with prevention barriers on the left side and recovery barriers on the right. Include which barriers failed and which held.'
          ]
        },
        {
          tool: '📧 Copilot in Outlook',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open Email_04_PETRONAS_Meeting_Prep.docx. Ask Copilot in Outlook: Draft a formal pre-audit meeting request to our PETRONAS account manager. The email should: reference the upcoming HSE audit date, request a 30-minute pre-audit briefing to present our self-assessment and corrective action progress, propose two available dates, and attach the executive summary of our HSE performance report (note: attach separately). Use formal energy industry correspondence tone.',
            'Ask Copilot: Draft an internal email to the Miri Platform management team briefing them on the PETRONAS HSE audit in 6 weeks. The email should: list the 5 areas the audit team will focus on based on our previous audit findings, assign a responsible person for each area, request that all documentation be ready for review 2 weeks before the audit, and remind the team of the confidentiality requirements during the audit.',
            'Ask Copilot: Summarise the email thread in Email_04_PETRONAS_Meeting_Prep.docx. What specific documentation has PETRONAS requested for the audit? List each requested document, the section of the PSM framework it relates to, and whether we currently have the document ready.'
          ]
        },
        {
          tool: '🎙 Copilot in Teams',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Use your OWN existing recorded Teams meetings. Open a meeting recap in Teams > Recap tab. Copilot generates summaries, action items, and follow-up drafts grounded in the actual transcript.',
          prompts: [
            'Open an existing recorded Teams meeting recap from an HSE or operations review meeting. Ask Copilot: Identify all safety-critical action items discussed, the owner of each, and the due date. Flag any action item that is related to the Tier 1 PSE CAPA plan as "Priority". Format as an HSE action register.',
            'Ask Copilot: Draft a post-incident communication for the Miri platform crew following the Tier 1 PSE. The communication should: acknowledge the incident without assigning blame, explain the immediate corrective actions taken to make the platform safe, outline the lessons-learned review process, and thank the crew for their cooperation. Tone: open, safety-first, respectful.',
            'Ask Copilot: Based on this meeting transcript, identify any discussion about GHG or emissions topics. List any emissions reduction targets or milestones mentioned and check whether they are consistent with our stated Net Zero 2050 commitment.'
          ]
        },
        {
          tool: '📓 Copilot Notebook',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via copilot.microsoft.com > Notebook tab. Upload up to 5 files and set a system instruction. Best for synthesising insights across multiple documents simultaneously.',
          prompts: [
            'Upload OG_01_Nusantara_Energy.xlsx, OG_02_Nusantara_HSE_Report.docx, and Email_04_PETRONAS_Meeting_Prep.docx to Copilot Notebook. Set instruction: "You are a senior HSE consultant preparing a company for a PETRONAS regulatory audit." Ask: Based on the HSE performance data, the incident report, and the PETRONAS correspondence, what are the three most likely areas of non-conformance in the upcoming audit? For each, what evidence should we prepare to demonstrate that the corrective action has been effective?',
            'Upload OG_01_Nusantara_Energy.xlsx and OG_02_Nusantara_HSE_Report.docx. Ask: The HSE report commits to a 30% GHG reduction by 2030. Based on the current production data and emissions data, what is the implied annual reduction required? Which single platform — if it implemented all identified GHG reduction measures — would contribute most to achieving the 2030 target? Is the target achievable without reducing production?'
          ]
        },
        {
          tool: '🤝 Cowork (Frontier)',
          license: 'M365 Copilot + Frontier Program',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Cowork is an autonomous agent that takes actions across Microsoft 365 on your behalf — sending emails, scheduling meetings, creating documents, posting in Teams, and scheduling recurring tasks. Access: m365.cloud.microsoft > left nav > Agents > Cowork. Requires Frontier program enrollment.',
          prompts: [
            'Do all of the following for the PETRONAS HSE audit: (1) Research PETRONAS\'s latest Process Safety Management framework and any updated audit criteria published in 2024 or 2025. (2) Draft a self-assessment gap analysis comparing our current practices against the updated criteria. (3) Save to OneDrive as "PETRONAS HSE Audit Self-Assessment - [Date]". (4) Email to the VP HSE and the Miri Platform HSE Manager asking for review and input within 3 days. (5) Schedule a 2-hour "PETRONAS Audit Prep Workshop" for 5 weeks before the audit date and invite all platform HSE leads.',
            'Do all of the following for the Net Zero roadmap: (1) Research the carbon credit market for oil and gas operators in Malaysia and Indonesia — specifically VERRA and Gold Standard certification. (2) Draft a 2-page carbon credit strategy brief covering: voluntary offset opportunities, estimated cost per tCO2e, and whether offsets should be used to bridge the gap in the 2030 target. (3) Save to OneDrive. (4) Email to the Sustainability Director and CFO. (5) Schedule a Carbon Strategy Workshop for the sustainability team.'
          ]
        },
        {
          tool: '🤖 Word Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to a Word document. Open the .docx in Word for Web > Copilot pane > + New Agent > name it, write a description, set the document as knowledge source > Share. Colleagues chat with it in Teams or M365 Copilot.',
          prompts: [
            'Open OG_02_Nusantara_HSE_Report.docx in Word for Web. Create an agent called "HSE Policy & Incident Agent". Description: "Answers questions from operations staff and HSE teams about Nusantara Energy\'s HSE policies, incident investigation procedures, PETRONAS reporting requirements, and corrective action obligations." Share with all platform HSE leads.',
            'Demo: A platform supervisor asks "We have just detected a small oil sheen approximately 20 metres from Platform Miri-A. What is the immediate response procedure, who do I notify in the first hour, and is this reportable to PETRONAS and DOE?" Show how the agent walks the supervisor through the emergency response protocol step by step.'
          ]
        },
        {
          tool: '🤖 PowerPoint Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to a PowerPoint presentation. Great for strategy decks or Board presentations many people need to reference. Same setup as Word Agent but using a .pptx file.',
          prompts: [
            'Create a PowerPoint from the PETRONAS audit management presentation. Create an agent called "PETRONAS Audit Prep Bot". Share with the PETRONAS audit team as a pre-reading tool and with internal leadership.',
            'Demo: The PETRONAS audit lead asks the agent "What corrective action did Nusantara implement following the Tier 1 PSE at Miri, and what evidence is available that the corrective action has been effective?" Show how the agent provides a precise, document-grounded answer that demonstrates accountability.'
          ]
        },
        {
          tool: '🤖 Excel Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to an Excel workbook. Colleagues ask data questions in plain English without opening Excel. Open .xlsx in Excel for Web > Copilot pane > + New Agent > set workbook as knowledge source > share.',
          prompts: [
            'Open OG_01_Nusantara_Energy.xlsx in Excel for Web. Create an agent called "Nusantara HSE & Operations Q&A". Description: "Instant answers on HSE KPIs, incident data, platform uptime, GHG emissions, and CAPA tracker status for the HSE leadership and audit preparation teams." Share with VP HSE and platform managers.',
            'Demo: Ask "What was our Lost Time Incident Rate for FY2025 and how does it compare to the PETRONAS threshold?" Then: "Which platform has the highest Scope 1 GHG emissions intensity and by how much does it exceed the group average?" Show how the HSE team gets rapid data-grounded answers.'
          ]
        },
        {
          tool: '🏗 Agent Builder (Copilot Studio)',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Build a custom declarative agent in Copilot Studio — no coding required. Access: copilotstudio.microsoft.com > Create > New Agent. Add name, description, knowledge sources (SharePoint URLs or uploaded files), topics/actions. Publish to Teams in under 10 minutes.',
          prompts: [
            'Go to copilotstudio.microsoft.com > Create > New Agent. Name it "Nusantara HSE Compliance Assistant". Description: "Supports Nusantara Energy\'s HSE teams with instant answers on incident reporting procedures, PETRONAS PSM requirements, GHG reduction targets, emergency response protocols, and corrective action tracking. Ensures consistent, standard-compliant responses across all offshore platforms." Upload OG_01_Nusantara_Energy.xlsx and OG_02_Nusantara_HSE_Report.docx. Add topics: "Incident Reporting", "PETRONAS PSM", "Emergency Response", "GHG & Sustainability". Publish to Teams for all HSE staff.',
            'Demo the agent: A drilling supervisor asks "We have a well control incident — a kick — on the Miri-B drilling rig. Gas is showing at the shakers. What is the Level 1 emergency response procedure, who is in the Emergency Command Team, and what do I report to PETRONAS and at what point?" Show how the agent gives an immediate, complete emergency response guidance in a high-stakes situation.'
          ]
        }
      ]
    },
    {
      id: 'og-downstream',
      sectorId: 'og-energy',
      subsector: '',
      name: 'Oil & Gas — Downstream',
      icon: '🏭',
      color: '#BF360C',
      accent: '#D84315',
      company: 'HengYuan Refining Sdn Bhd',
      tagline: 'Refinery margin at USD 4.2/bbl — DOSH CIMAH audit in 8 weeks.',
      scenario: 'HengYuan Refining operates Malaysia\'s second-largest crude oil refinery with 156,000 bbl/day capacity. Refinery margins have compressed to USD 4.2/bbl (breakeven at USD 5.8/bbl) driven by MOPS crack spread compression. A DOSH CIMAH (Control of Industrial Major Accident Hazards) audit is scheduled in 8 weeks. A major maintenance turnaround is being planned for Q3.',
      files: [
        'OG_01_Nusantara_Energy.xlsx',
        'OG_02_Nusantara_HSE_Report.docx'
      ],
      prompts: [
        {
          tool: '🤖 Copilot Chat (Basic)',
          license: 'Free — no M365 Copilot license needed',
          account: 'Sasha Ouellet — SashaO@ABSx62256373.OnMicrosoft.com',
          desc: '',
          prompts: [
            'I am the CFO of a Malaysian crude oil refinery. Our refinery margin has compressed to USD 4.2 per barrel — below our breakeven of USD 5.8/bbl — driven by MOPS crack spread compression and rising crude differentials. Draft a 300-word margin recovery briefing for our Board. Cover: the key drivers of margin compression, three operational levers we can pull to improve margin within 90 days (without capital investment), and the crude slate optimisation opportunity given current Middle East vs North African crude price differentials.',
            'Explain the DOSH CIMAH (Control of Industrial Major Accident Hazards) Regulations 1996 for a petroleum refinery in Malaysia. What are the key obligations, the documentation required, and the consequences of a failed CIMAH audit? Keep it under 200 words for a non-technical Board member.',
            'What are the main components of a refinery maintenance turnaround (T/A) and what are the typical cost and production loss risks? Describe the best practices for turnaround planning that minimise production downtime and cost overrun, specifically for a complex refinery in Southeast Asia.'
          ]
        },
        {
          tool: '🔍 Researcher',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via Microsoft 365 Copilot Chat (copilot.microsoft.com or Teams) > click Agents > Researcher. Grounds answers in live web sources and your organisation data with full citations.',
          prompts: [
            'Research the current MOPS (Mean of Platts Singapore) crack spread trends for Asian refineries and the outlook for the next 6 months. What is driving the compression? Which product slates (gasoline, diesel, jet fuel) are most and least affected? Cite recent energy market reports or commodity trading publications.',
            'Research DOSH Malaysia\'s CIMAH enforcement trends for petroleum refineries in 2023–2025. What are the most common audit findings? Have any refineries received improvement orders or stop-work orders? What documentation do DOSH auditors typically request on the first day of inspection? Provide citations.'
          ]
        },
        {
          tool: '📊 Analyst',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via Microsoft 365 Copilot Chat > click Agents > Analyst. Upload an Excel or CSV file. Analyst runs Python-style analysis, builds charts, and interprets results without you writing a single formula.',
          prompts: [
            'Upload OG_01_Nusantara_Energy.xlsx (use as refinery operations proxy). Ask Analyst: Analyse refinery margin data over the past 8 quarters. Decompose the margin into: crude differential, product realisation (by product slate), variable operating cost, and fixed cost per barrel. Which component has deteriorated most? Show as a waterfall chart from peak margin to current margin.',
            'Upload OG_01_Nusantara_Energy.xlsx. Ask: Build a crude slate optimisation analysis. Compare three crude blends available to us — Arab Light, Murban, and Basrah Heavy — showing for each: (1) current spot price vs our long-term contract price, (2) API gravity and sulphur content, (3) estimated product yield by category, (4) net margin contribution per barrel. Recommend the optimal crude slate mix for the next quarter.'
          ]
        },
        {
          tool: '📊 Copilot in Excel',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open OG_01_Nusantara_Energy.xlsx. Navigate to the Refinery Operations sheet. Ask Copilot: Build a margin sensitivity model on a new sheet. Show how the refinery margin changes for every USD 1/bbl move in the MOPS crack spread and every USD 0.50/bbl change in crude differential. Create a 6x6 sensitivity table (crack spread vs crude differential) showing the resulting margin and highlight in green cells above breakeven (USD 5.8/bbl) and red cells below.',
            'Ask Copilot: Create a turnaround planning model on a new sheet. The planned Q3 turnaround will take 28 days and shut down Units 3 and 5. Calculate: (1) Total production loss in barrels assuming 80,000 bbl/day from those units, (2) Revenue loss at current margin of USD 4.2/bbl, (3) Fixed cost absorption loss, (4) Net P&L impact of the turnaround. Compare against the cost of deferring the turnaround by 6 months.',
            'Ask Copilot: In the CIMAH Compliance sheet, identify all major hazard installations (MHIs) that are due for re-inspection within the next 12 months. For each, show the last inspection date, the next due date, the responsible engineer, and whether the pre-inspection documentation is complete. Flag in red any MHI where documentation is incomplete and the inspection is less than 60 days away.'
          ]
        },
        {
          tool: '📝 Copilot in Word',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open OG_02_Nusantara_HSE_Report.docx. Ask Copilot: Draft a DOSH CIMAH pre-audit submission letter. The letter should: confirm our readiness for the scheduled audit, provide a summary of our major hazard risk assessment updates since the last audit, list the key safety-critical equipment that has been tested and certified in the past 12 months, and request 20 minutes for a management presentation at the start of the audit.',
            'Ask Copilot: Create a CIMAH Safety Report executive summary of 500 words. Cover: (1) description of the hazardous substances on site and quantities relative to CIMAH thresholds, (2) the major accident scenarios identified in our HAZOP/QRA, (3) the safety systems in place to prevent and mitigate each scenario, (4) the emergency response plan and last drill date. Use formal regulatory language.',
            'Ask Copilot: Draft the turnaround scope-of-work document for Units 3 and 5. Structure: (1) objective of the turnaround, (2) equipment list for inspection and maintenance, (3) critical path activities, (4) contractor safety requirements, (5) permit-to-work framework during T/A, (6) restoration and recommissioning criteria. Keep it to 3 pages.'
          ]
        },
        {
          tool: '🎯 Copilot in PowerPoint',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Ask Copilot in PowerPoint: Create a 10-slide Board presentation on Refinery Performance and Margin Recovery. Include: (1) Current margin position vs breakeven, (2) Margin decomposition waterfall, (3) MOPS market outlook — 6-month view, (4) Three margin recovery levers with estimated impact, (5) Crude slate optimisation — recommended blend, (6) Q3 turnaround — scope, cost, and margin impact, (7) CIMAH audit readiness — RAG status, (8) Safety performance dashboard, (9) Financial outlook — 12-month margin projection, (10) Board decisions required. Dark red and white colour scheme.',
            'Ask Copilot: Add a one-slide crude slate decision matrix showing the trade-off between three crude options. Display as a spider chart with 5 axes: Margin Contribution | Sulphur Content | Availability Risk | Price Volatility | Refinery Compatibility.',
            'Ask Copilot: Create speaker notes for the CFO for slides 1 through 4. The CFO needs to be able to explain the margin compression to non-technical Board members in under 3 minutes using plain language and one analogy.'
          ]
        },
        {
          tool: '📧 Copilot in Outlook',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Ask Copilot in Outlook: Draft an email to our crude oil trading desk requesting a revised crude supply proposal for Q3. The email should specify: (1) our preferred crude API gravity range (32-38 API), (2) maximum sulphur content (0.5%), (3) required delivery window for the turnaround period, (4) target price differential vs Brent, and (5) request for optionality on volumes given the turnaround timing uncertainty.',
            'Ask Copilot: Draft an internal memo to the operations leadership team briefing them on the DOSH CIMAH audit in 8 weeks. List the 5 areas DOSH will focus on, assign a responsible manager for each area, and set a document readiness deadline of 4 weeks before the audit. Emphasise that DOSH auditors will conduct physical plant walk-rounds and interview operators directly.',
            'Ask Copilot: Draft a letter to DOSH Malaysia confirming our CIMAH Safety Report has been updated and requesting confirmation that the latest version is on file with DOSH. Reference the relevant CIMAH regulation schedule and our establishment registration number.'
          ]
        },
        {
          tool: '🎙 Copilot in Teams',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Use your OWN existing recorded Teams meetings. Open a meeting recap in Teams > Recap tab. Copilot generates summaries, action items, and follow-up drafts grounded in the actual transcript.',
          prompts: [
            'Open an existing recorded Teams meeting recap from a refinery operations or HSE meeting. Ask Copilot: Identify all CIMAH or process safety topics discussed. List each topic with the key point made, any decision taken, and the follow-up action assigned. Format as a process safety meeting minute.',
            'Ask Copilot: Draft follow-up actions from this meeting for the turnaround planning team. Group by workstream: Engineering | HSE | Procurement | Contractor Management | Operations Readiness. Include owner and deadline for each action.',
            'Ask Copilot: Were any near-miss incidents or process deviations mentioned in this meeting? Extract each one with: the unit or equipment involved, the nature of the deviation, and whether a formal incident report was raised.'
          ]
        },
        {
          tool: '📓 Copilot Notebook',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via copilot.microsoft.com > Notebook tab. Upload up to 5 files and set a system instruction. Best for synthesising insights across multiple documents simultaneously.',
          prompts: [
            'Upload OG_01_Nusantara_Energy.xlsx and OG_02_Nusantara_HSE_Report.docx to Copilot Notebook. Set instruction: "You are a refinery CFO preparing a margin recovery and CIMAH audit strategy." Ask: Based on the operations data and the HSE report, what are the top 3 actions that will simultaneously improve refinery margin AND reduce CIMAH compliance risk before the audit in 8 weeks? Show the financial impact and the risk reduction benefit of each.',
            'Upload OG_01_Nusantara_Energy.xlsx and OG_02_Nusantara_HSE_Report.docx. Ask: If we defer the Q3 turnaround to Q1 FY2027 to avoid the production loss during a period of already-compressed margins, what is the increased safety and regulatory risk? What criteria should the Board use to make this deferral decision responsibly?'
          ]
        },
        {
          tool: '🤝 Cowork (Frontier)',
          license: 'M365 Copilot + Frontier Program',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Cowork is an autonomous agent that takes actions across Microsoft 365 on your behalf — sending emails, scheduling meetings, creating documents, posting in Teams, and scheduling recurring tasks. Access: m365.cloud.microsoft > left nav > Agents > Cowork. Requires Frontier program enrollment.',
          prompts: [
            'Do all of the following: (1) Research the latest DOSH CIMAH audit requirements and any guidance notes published since 2023. (2) Draft a CIMAH audit readiness action plan covering the 8 weeks to the audit — with specific weekly milestones. (3) Save to OneDrive as "CIMAH Audit Readiness Plan". (4) Email to the Plant Manager, Process Safety Manager, and Head of HSE asking them to review and confirm ownership of each milestone by Friday. (5) Schedule a weekly "CIMAH Audit Prep" 30-minute check-in every Monday morning for 8 weeks starting next Monday.',
            'Do all of the following for margin recovery: (1) Pull the latest MOPS pricing data from available sources. (2) Calculate the current crack spread for gasoline, diesel, and jet fuel based on available data. (3) Draft a 1-page crude slate recommendation memo for the trading desk showing the recommended crude blend for Q3. (4) Email to the Crude Procurement Manager and CFO. (5) Schedule a Crude Slate Review meeting for this Thursday.'
          ]
        },
        {
          tool: '🤖 Word Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to a Word document. Open the .docx in Word for Web > Copilot pane > + New Agent > name it, write a description, set the document as knowledge source > Share. Colleagues chat with it in Teams or M365 Copilot.',
          prompts: [
            'Open OG_02_Nusantara_HSE_Report.docx in Word for Web. Create an agent called "CIMAH Compliance Assistant". Description: "Answers questions from process engineers, HSE officers, and plant managers about CIMAH obligations, major hazard risk assessments, safety-critical equipment inspection requirements, and audit documentation." Share with all plant HSE and engineering teams.',
            'Demo: A process engineer asks "Unit 3 has a relief valve that was last tested 14 months ago. CIMAH requires annual testing. Is this non-compliant and what is the procedure to bring it into compliance before the DOSH audit in 8 weeks?" Show how the agent provides a precise, policy-grounded compliance answer.'
          ]
        },
        {
          tool: '🤖 PowerPoint Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to a PowerPoint presentation. Great for strategy decks or Board presentations many people need to reference. Same setup as Word Agent but using a .pptx file.',
          prompts: [
            'Create a PowerPoint from the Board presentation and open in PowerPoint for Web. Create an agent called "Refinery Performance Board Bot". Share with Board members.',
            'Demo: A Board member asks "If the MOPS crack spread remains at current levels for the full year, what is our projected full-year EBITDA and do we remain above our debt covenant requirements?" Show how the agent provides a scenario-specific financial answer.'
          ]
        },
        {
          tool: '🤖 Excel Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to an Excel workbook. Colleagues ask data questions in plain English without opening Excel. Open .xlsx in Excel for Web > Copilot pane > + New Agent > set workbook as knowledge source > share.',
          prompts: [
            'Open OG_01_Nusantara_Energy.xlsx in Excel for Web. Create an agent called "Refinery Operations Analytics Q&A". Description: "Answers questions on refinery margin, crude slate, CIMAH compliance status, and turnaround planning for the operations and finance teams." Share with refinery management.',
            'Demo: Ask "What is the current refinery margin and how does it compare to our 3-year average?" Then: "How many safety-critical inspections are overdue across all major hazard installations?" Show how management gets instant operational intelligence.'
          ]
        },
        {
          tool: '🏗 Agent Builder (Copilot Studio)',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Build a custom declarative agent in Copilot Studio — no coding required. Access: copilotstudio.microsoft.com > Create > New Agent. Add name, description, knowledge sources (SharePoint URLs or uploaded files), topics/actions. Publish to Teams in under 10 minutes.',
          prompts: [
            'Go to copilotstudio.microsoft.com > Create > New Agent. Name it "HengYuan Operations Intelligence Bot". Description: "Supports HengYuan\'s plant operations and HSE teams with answers on CIMAH compliance, margin analysis, crude slate decisions, turnaround planning, and DOSH requirements — grounded in official operations and HSE documents." Upload OG_01_Nusantara_Energy.xlsx and OG_02_Nusantara_HSE_Report.docx. Add topics: "CIMAH Compliance", "Margin Analysis", "Turnaround Planning". Publish to Teams for operations and HSE staff.',
            'Demo the agent: A shift supervisor asks "We have detected a gas leak in the Unit 3 heat exchanger area. Concentration is at 15% LEL. What is our emergency response Level 1 procedure, do we isolate the unit, and who do I call first?" Show how the agent provides an immediate, structured emergency response for a high-stakes situation.'
          ]
        }
      ]
    },
    {
      id: 'renewable-energy',
      sectorId: 'og-energy',
      subsector: '',
      name: 'Renewable Energy',
      icon: '☀',
      color: '#F9A825',
      accent: '#F57F17',
      company: 'GreenPower Division (Sarawak Energy)',
      tagline: '480MW solar pipeline + PPA renegotiation with Tenaga — EUETS carbon credit filing due.',
      scenario: 'GreenPower Division manages Sarawak Energy\'s 2.4GW hydro portfolio and a 480MW solar pipeline under development. The power purchase agreement (PPA) with Tenaga Nasional Berhad (TNB) for 800MW is up for renegotiation. Carbon credit generation under Verra VCS is being certified. The Energy Commission (ST) large-scale solar (LSS) bid is due in 6 weeks.',
      files: [
        'OG_01_Nusantara_Energy.xlsx',
        '20_Zava_ESG_Sustainability_Framework.docx'
      ],
      prompts: [
        {
          tool: '🤖 Copilot Chat (Basic)',
          license: 'Free — no M365 Copilot license needed',
          account: 'Sasha Ouellet — SashaO@ABSx62256373.OnMicrosoft.com',
          desc: '',
          prompts: [
            'I lead the commercial team for a renewable energy developer in Malaysia. We have an 800MW hydro PPA with Tenaga that is up for renegotiation. The current tariff is MYR 0.214/kWh on a 25-year contract. Market tariffs for new hydro have risen to MYR 0.26/kWh. Draft a negotiation strategy brief of 250 words covering: our target tariff, our walk-away position, our three strongest negotiating arguments, and the key concessions we should be prepared to offer Tenaga in exchange for a tariff increase.',
            'Explain the Verra VCS (Verified Carbon Standard) certification process for a large hydro project. What are the key steps, the typical timeline from initial project design document (PDD) to first carbon credits issued, and the verification requirements? Focus on Sarawak hydro projects specifically.',
            'What is the Energy Commission Malaysia\'s Large Scale Solar (LSS) bidding framework? What are the eligibility criteria, the maximum capacity per bid, the tariff determination mechanism, and the typical timeline from bid submission to financial close? How competitive has the LSS bidding been in recent rounds?'
          ]
        },
        {
          tool: '🔍 Researcher',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via Microsoft 365 Copilot Chat (copilot.microsoft.com or Teams) > click Agents > Researcher. Grounds answers in live web sources and your organisation data with full citations.',
          prompts: [
            'Research the carbon credit market for renewable energy in Southeast Asia in 2025 and 2026. I need: (1) Current voluntary carbon credit price range for hydro and solar projects, (2) Demand trends from corporate buyers in Malaysia and Singapore, (3) The Bursa Carbon Exchange (BCX) performance since launch. Provide citations.',
            'Research global solar PV cost trends and the competitive landscape for LSS solar bids in Malaysia. What levelised cost of energy (LCOE) are developers achieving? Who are the main EPC contractors active in Malaysian LSS projects and what are typical project timelines? Cite recent energy reports.'
          ]
        },
        {
          tool: '📊 Analyst',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via Microsoft 365 Copilot Chat > click Agents > Analyst. Upload an Excel or CSV file. Analyst runs Python-style analysis, builds charts, and interprets results without you writing a single formula.',
          prompts: [
            'Upload OG_01_Nusantara_Energy.xlsx (use as energy portfolio proxy). Ask Analyst: Analyse the hydro portfolio generation data for the past 4 years. What is the capacity factor trend for each dam? Which dams have the highest variability in generation due to rainfall patterns? Calculate the average annual generation in GWh and the revenue sensitivity to a 10% drop in generation. Show as a trend chart and a sensitivity table.',
            'Upload 20_Zava_ESG_Sustainability_Framework.xlsx. Ask: Build a carbon credit revenue projection for the hydro portfolio. Assume 2.4GW capacity, 45% average capacity factor, grid emission factor of 0.62 tCO2e/MWh. Calculate: (1) Annual carbon credits generated in tCO2e, (2) Revenue at USD 8/tCO2e (current VCS price), (3) Revenue at USD 15/tCO2e (if carbon price rises). Show as a 5-year projection table.'
          ]
        },
        {
          tool: '📊 Copilot in Excel',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open OG_01_Nusantara_Energy.xlsx. Navigate to the Renewable Portfolio sheet. Ask Copilot: Build a PPA renegotiation model on a new sheet. Current PPA: 800MW at MYR 0.214/kWh, 25-year remaining term, 2% annual escalation. Proposed new tariff: MYR 0.248/kWh. Calculate: (1) Annual revenue difference, (2) NPV of the tariff increase over the remaining 25 years at an 8% discount rate, (3) The impact on our DSCR (Debt Service Coverage Ratio). Show as a comparison table: Current PPA vs Proposed PPA.',
            'Ask Copilot: Create a 480MW solar pipeline development tracker on a new sheet. List each solar project with: Project Name | Capacity (MW) | Development Stage | Land Status | Grid Connection Application Status | Expected COD | Estimated Capex (MYR M) | LSS Bid Round. Apply conditional formatting: projects at Financial Close stage in green, at Grid Application stage in yellow, at Land Acquisition stage in orange.',
            'Ask Copilot: Build a carbon credit generation tracker. For each hydro asset in the portfolio, calculate the estimated annual carbon credits based on generation data and the grid emission factor. Show the cumulative carbon credits generated to date and the estimated revenue at current market prices. Add a chart showing annual carbon credit revenue at three price scenarios: USD 8, USD 12, and USD 18/tCO2e.'
          ]
        },
        {
          tool: '📝 Copilot in Word',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open 20_Zava_ESG_Sustainability_Framework.docx. Ask Copilot: Draft a 400-word renewable energy section for our annual sustainability report. Cover: (1) Our renewable energy generation capacity and portfolio overview, (2) Carbon emission avoidance in tCO2e from our hydro and solar assets, (3) Progress on the 480MW solar pipeline, (4) Carbon credit certification update, (5) PPA contribution to Malaysia\'s renewable energy targets under the National Energy Transition Roadmap (NETR). Use an optimistic but factually grounded tone.',
            'Ask Copilot: Draft the PPA renegotiation position paper for the TNB negotiation. Cover: (1) Market context — new hydro tariffs have risen to MYR 0.26/kWh, (2) Our cost structure justification — OPEX has increased 18% since the original PPA, (3) The long-term supply security value we provide TNB, (4) Our proposal — MYR 0.248/kWh with 2.5% escalation, (5) What we can offer TNB in return — extended term optionality, demand response capability. Keep it to 2 pages.',
            'Ask Copilot: Write the LSS bid submission executive summary for our 150MW solar project in Sarawak. Cover: project overview, site location, technology (single-axis tracking monofacial), expected capacity factor 19.2%, proposed tariff MYR 0.198/kWh, EPC contractor, connection point, and environmental impact summary. Format to match the Energy Commission LSS bid template structure.'
          ]
        },
        {
          tool: '🎯 Copilot in PowerPoint',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Ask Copilot in PowerPoint: Create a 10-slide renewable energy investor day presentation. Include: (1) Portfolio overview — 2.4GW hydro + 480MW solar pipeline, (2) Hydro generation performance and revenue, (3) PPA renegotiation — rationale and impact, (4) Solar pipeline — project map and development status, (5) Carbon credit programme — certification update and revenue potential, (6) LSS Round 5 bid — project details, (7) NETR alignment — how our portfolio supports Malaysia\'s 70% renewable target, (8) Financial projections — 5-year revenue and EBITDA, (9) ESG commitment, (10) Investment thesis. Use a green and yellow colour scheme.',
            'Ask Copilot: Create a 2-slide carbon credit explainer for our Board who are unfamiliar with voluntary carbon markets. Slide 1: How carbon credits are generated, verified (Verra VCS), and sold. Slide 2: Our portfolio\'s carbon credit potential — annual tCO2e generated and revenue at three price scenarios. Use simple visuals, no jargon.',
            'Ask Copilot: Add a risk matrix slide showing the top 4 risks to our renewable energy business: hydrology risk (rainfall variability), tariff renegotiation risk, LSS bid failure, and carbon price volatility. Position each on a 3x3 likelihood-impact matrix.'
          ]
        },
        {
          tool: '📧 Copilot in Outlook',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Ask Copilot in Outlook: Draft a formal letter to TNB\'s Power Procurement team requesting a PPA renegotiation meeting. The letter should: reference the existing PPA and its key terms, note that the PPA review clause allows renegotiation at the 10-year mark, outline our position at a high level (seeking a tariff revision to reflect current market rates), and propose a negotiation timeline of 3 months. Use formal utility sector correspondence tone.',
            'Ask Copilot: Draft an email to the Energy Commission Malaysia submitting our intention to bid in the LSS Round 5 tender. The email should confirm our company eligibility, specify the project name and capacity (150MW), attach the pre-qualification documents checklist (note: attach separately), and request confirmation of the submission portal access.',
            'Ask Copilot: Draft an update email to our Verra VCS verifier requesting the status of our carbon credit certification for the Bakun Hydro project. The verification has been pending for 5 months. Ask for an estimated completion date and a list of any outstanding documentation required from our side.'
          ]
        },
        {
          tool: '🎙 Copilot in Teams',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Use your OWN existing recorded Teams meetings. Open a meeting recap in Teams > Recap tab. Copilot generates summaries, action items, and follow-up drafts grounded in the actual transcript.',
          prompts: [
            'Open an existing recorded Teams meeting recap from a project development or commercial meeting. Ask Copilot: Identify all commercial milestones discussed — PPA, LSS bid, carbon credits, and land acquisition. For each, note the current status, the next key milestone, and who is responsible.',
            'Ask Copilot: Draft follow-up actions for the LSS bid preparation team. Assign each action to a workstream: Technical | Commercial | Legal | Environmental | Grid Connection. Include deadline and the person responsible.',
            'Ask Copilot: Were any regulatory risks or delays discussed in this meeting? List each risk with the project it affects, the nature of the risk, and the mitigation discussed.'
          ]
        },
        {
          tool: '📓 Copilot Notebook',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via copilot.microsoft.com > Notebook tab. Upload up to 5 files and set a system instruction. Best for synthesising insights across multiple documents simultaneously.',
          prompts: [
            'Upload OG_01_Nusantara_Energy.xlsx and 20_Zava_ESG_Sustainability_Framework.docx to Copilot Notebook. Set instruction: "You are a renewable energy commercial director." Ask: Based on the portfolio data and our sustainability framework, what is the optimal sequencing of our three commercial priorities — PPA renegotiation, LSS bid, and carbon credit certification — given that we have limited management bandwidth? Which should we focus on first and why?',
            'Upload OG_01_Nusantara_Energy.xlsx and 20_Zava_ESG_Sustainability_Framework.docx. Ask: Our sustainability framework commits to being carbon neutral by 2035. Our current operations generate 480,000 tCO2e/year. Our renewable portfolio avoids an estimated 4.2M tCO2e/year. Does this mean we are already carbon neutral on a portfolio basis? What is the correct way to report this under GHG Protocol accounting standards?'
          ]
        },
        {
          tool: '🤝 Cowork (Frontier)',
          license: 'M365 Copilot + Frontier Program',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Cowork is an autonomous agent that takes actions across Microsoft 365 on your behalf — sending emails, scheduling meetings, creating documents, posting in Teams, and scheduling recurring tasks. Access: m365.cloud.microsoft > left nav > Agents > Cowork. Requires Frontier program enrollment.',
          prompts: [
            'Do all of the following for the LSS bid: (1) Research the Energy Commission Malaysia LSS Round 5 requirements and submission deadline. (2) Draft a bid preparation checklist covering all required documents. (3) Save to OneDrive as "LSS Round 5 Bid Checklist". (4) Email to the Project Director and Head of Business Development asking them to assign responsibility for each checklist item and confirm readiness in 2 weeks. (5) Schedule a weekly LSS Bid Preparation meeting every Tuesday at 9am for 6 weeks.',
            'Do all of the following for the PPA renegotiation: (1) Research recent PPA tariff benchmarks for hydro power in Malaysia and comparable markets. (2) Compile a negotiation brief showing our tariff request (MYR 0.248/kWh) against market benchmarks. (3) Draft a letter to TNB\'s Power Procurement team requesting a renegotiation meeting. (4) Save the letter and brief to OneDrive. (5) Email both documents to our General Counsel and CFO for review before sending to TNB.'
          ]
        },
        {
          tool: '🤖 Word Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to a Word document. Open the .docx in Word for Web > Copilot pane > + New Agent > name it, write a description, set the document as knowledge source > Share. Colleagues chat with it in Teams or M365 Copilot.',
          prompts: [
            'Open 20_Zava_ESG_Sustainability_Framework.docx in Word for Web. Create an agent called "GreenPower ESG Policy Bot". Description: "Answers questions from the project development team about GreenPower\'s sustainability commitments, carbon credit methodology, ESG reporting requirements, and renewable energy targets." Share with the development and sustainability teams.',
            'Demo: A project developer asks "Does our 150MW Sarawak solar project qualify for Verra VCS carbon credit certification? What additionality criteria do we need to meet and what is the typical documentation required for the Project Design Document?" Show how the agent provides a precise, policy-grounded answer.'
          ]
        },
        {
          tool: '🤖 PowerPoint Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to a PowerPoint presentation. Great for strategy decks or Board presentations many people need to reference. Same setup as Word Agent but using a .pptx file.',
          prompts: [
            'Create a PowerPoint from the investor day presentation. Create an agent called "GreenPower Investor Q&A Bot". Share with institutional investors and the IR team.',
            'Demo: An investor asks "What is GreenPower\'s projected EBITDA from the 480MW solar pipeline at full buildout, and what assumptions does that use for tariff and capacity factor?" Show how the agent handles complex investor questions during a roadshow.'
          ]
        },
        {
          tool: '🤖 Excel Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to an Excel workbook. Colleagues ask data questions in plain English without opening Excel. Open .xlsx in Excel for Web > Copilot pane > + New Agent > set workbook as knowledge source > share.',
          prompts: [
            'Open OG_01_Nusantara_Energy.xlsx in Excel for Web. Create an agent called "Renewable Portfolio Analytics Q&A". Description: "Instant answers on GreenPower\'s hydro and solar portfolio — generation, PPA revenue, carbon credits, and project pipeline — for the commercial and finance teams." Share with senior management.',
            'Demo: Ask "What is the capacity factor for our top-performing hydro asset in FY2025?" Then: "At USD 12/tCO2e, what is the annual carbon credit revenue from our full hydro portfolio?" Show how the commercial team gets rapid portfolio intelligence.'
          ]
        },
        {
          tool: '🏗 Agent Builder (Copilot Studio)',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Build a custom declarative agent in Copilot Studio — no coding required. Access: copilotstudio.microsoft.com > Create > New Agent. Add name, description, knowledge sources (SharePoint URLs or uploaded files), topics/actions. Publish to Teams in under 10 minutes.',
          prompts: [
            'Go to copilotstudio.microsoft.com > Create > New Agent. Name it "GreenPower Commercial Intelligence Bot". Description: "Supports GreenPower\'s commercial, project development, and sustainability teams with answers on PPA terms, LSS bid requirements, carbon credit methodology, ESG reporting, and portfolio performance — grounded in official portfolio and sustainability documents." Upload OG_01_Nusantara_Energy.xlsx and 20_Zava_ESG_Sustainability_Framework.docx. Add topics: "PPA & Tariff", "LSS Bid", "Carbon Credits", "ESG Reporting". Publish to Teams.',
            'Demo the agent: A business development manager asks: "We are evaluating a 50MW rooftop solar project for a large industrial client in Penang. Can we structure this as a corporate PPA and how does it interact with our existing LSS licences? Are there any Energy Commission approval requirements?" Show how the agent gives a comprehensive commercial answer that helps the team make the right decision.'
          ]
        }
      ]
    },
    {
      id: 'industrial-manufacturing',
      sectorId: 'manufacturing',
      subsector: '',
      name: 'Industrial Manufacturing',
      icon: '⚙',
      color: '#263238',
      accent: '#37474F',
      company: 'Zava Manufacturing (Nilai Plant)',
      tagline: 'OEE 62% — spindle motor failures, 2,800-unit backlog MYR 14.2M. SIRIM audit in 8 weeks.',
      scenario: 'Zava Manufacturing\'s Nilai plant produces precision industrial components for the automotive and electronics sectors. Overall Equipment Effectiveness (OEE) has dropped from 76% to 62% over 3 quarters, driven by recurring spindle motor failures on 3 of 12 CNC machines. A 2,800-unit production backlog worth MYR 14.2M has accumulated. SIRIM ISO 9001:2015 audit is scheduled in 8 weeks.',
      files: [
        '12_Zava_Manufacturing_KPIs.xlsx',
        '21_Zava_Chemical_Safety_HIRARC.docx'
      ],
      prompts: [
        {
          tool: '🤖 Copilot Chat (Basic)',
          license: 'Free — no M365 Copilot license needed',
          account: 'Sasha Ouellet — SashaO@ABSx62256373.OnMicrosoft.com',
          desc: '',
          prompts: [
            'I am the Plant Manager of a precision manufacturing facility. Three of my 12 CNC machines have recurring spindle motor failures, dragging OEE from 76% to 62% over the past 3 quarters. I have a 2,800-unit backlog worth MYR 14.2M and a SIRIM ISO 9001 audit in 8 weeks. Draft a 300-word operational recovery brief for my Managing Director. Cover: root cause hypothesis for the spindle motor failures, the three immediate actions I am taking to reduce the backlog, and how I will ensure the audit readiness is not compromised by the operational recovery effort.',
            'Explain Overall Equipment Effectiveness (OEE) — how it is calculated, what the three components are (availability, performance, quality), and what a world-class OEE target looks like for a precision manufacturing facility producing automotive and electronics components. Include an example calculation.',
            'What are the most common root causes of CNC spindle motor failures in precision machining environments, and what predictive maintenance approaches are most effective for preventing them? Focus on approaches that can be implemented without replacing the machines entirely.'
          ]
        },
        {
          tool: '🔍 Researcher',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via Microsoft 365 Copilot Chat (copilot.microsoft.com or Teams) > click Agents > Researcher. Grounds answers in live web sources and your organisation data with full citations.',
          prompts: [
            'Research best practices for rapid OEE recovery in precision manufacturing — specifically for facilities producing automotive and electronics components in Southeast Asia. I need: (1) The most effective maintenance strategies (TPM, predictive maintenance, RCM) and their typical OEE improvement impact, (2) Any case studies of Malaysian manufacturers who recovered OEE from below 65% to above 80% within 6 months, (3) SIRIM\'s expectations during an ISO 9001 audit for a facility with known equipment issues. Cite sources.',
            'Research the current state of predictive maintenance technology for CNC machining — specifically spindle health monitoring using vibration analysis and IoT sensors. What are the leading solutions available in Malaysia, typical implementation cost for a 12-machine facility, and the expected reduction in unplanned downtime? Provide citations.'
          ]
        },
        {
          tool: '📊 Analyst',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via Microsoft 365 Copilot Chat > click Agents > Analyst. Upload an Excel or CSV file. Analyst runs Python-style analysis, builds charts, and interprets results without you writing a single formula.',
          prompts: [
            'Upload 12_Zava_Manufacturing_KPIs.xlsx to Analyst. Ask: Analyse OEE data for all 12 CNC machines over the past 12 months. Break down OEE into availability, performance, and quality for each machine. Which 3 machines have the lowest OEE? Is the OEE decline driven primarily by availability loss (breakdowns) or performance loss (speed reduction)? Create a machine-level OEE heat map and a trend chart showing the group OEE from 76% to 62%.',
            'Upload 12_Zava_Manufacturing_KPIs.xlsx. Ask: Analyse the production backlog by customer and product type. Which customer has the largest backlog in units and MYR value? Calculate the financial penalty risk — assume our top 3 automotive customers have SLA penalties of 0.5% of order value per week of delay. Show total penalty exposure at current backlog clearance rate.'
          ]
        },
        {
          tool: '📊 Copilot in Excel',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open 12_Zava_Manufacturing_KPIs.xlsx. Navigate to the Machine Performance sheet. Ask Copilot: Create an OEE recovery simulation model on a new sheet. Show what happens to overall plant OEE if we: (1) Fix the 3 failing spindle motors (assume restores those machines to 82% OEE), (2) Implement 2-shift vs 3-shift production for the backlog clearance, (3) Temporarily defer non-urgent preventive maintenance. Calculate the projected backlog clearance date under each scenario.',
            'Ask Copilot: Build a SIRIM ISO 9001 audit readiness tracker on a new sheet. List the 10 key ISO 9001 clauses most commonly reviewed in a manufacturing audit. For each clause, add: Current Status (Compliant/Partial/Gap) | Evidence on File (Yes/No) | Responsible Person | Action Required Before Audit. Apply colour coding: green = Compliant with evidence, amber = Partial, red = Gap.',
            'Ask Copilot: In the Quality Control sheet, calculate the First Pass Yield (FPY) and scrap rate for each product family over the past 6 months. Has the scrap rate increased since the OEE decline began? If scrap has increased, estimate the additional material cost in MYR. Show as a trend chart with a correlation line.'
          ]
        },
        {
          tool: '📝 Copilot in Word',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open 21_Zava_Chemical_Safety_HIRARC.docx. Ask Copilot: Draft a CNC spindle motor failure root cause analysis report using the 5-Why methodology. The failures occur predominantly after 8–10 hours of continuous operation and are linked to 3 specific machines (CNC-04, CNC-07, CNC-11). Suspected causes include: insufficient coolant flow to the spindle bearing, inadequate preventive maintenance intervals, and substandard replacement parts. Structure the report: Problem Statement | 5-Why Analysis | Root Cause | Corrective Actions | Preventive Actions | Effectiveness Review Date.',
            'Ask Copilot: Write a backlog recovery plan of 2 pages for the Managing Director. Cover: (1) Current backlog — 2,800 units, MYR 14.2M value, (2) Customer impact and penalty risk, (3) Recovery plan — 3-shift production, contract machining outsource for 400 units, spindle motor repair timeline, (4) Expected clearance date — 6 weeks, (5) Communication plan for affected customers. Include a week-by-week recovery milestone table.',
            'Ask Copilot: Draft an ISO 9001 internal audit non-conformance response report. The internal audit found 3 minor non-conformances: (1) calibration records not updated for 2 measurement instruments, (2) operator training records incomplete for 4 new employees, (3) customer complaint response log not updated for 3 complaints. For each non-conformance, write the corrective action and the preventive action in the format required by SIRIM.'
          ]
        },
        {
          tool: '🎯 Copilot in PowerPoint',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Ask Copilot in PowerPoint: Create a 10-slide operations recovery presentation for the Managing Director and key customers. Include: (1) Situation — OEE decline from 76% to 62%, (2) Root cause — spindle motor analysis, (3) Financial impact — backlog value and penalty risk, (4) Recovery plan — timeline and milestones, (5) SIRIM audit readiness — status dashboard, (6) Resource plan — 3-shift operation and outsourcing, (7) Customer impact by account, (8) Communication plan, (9) OEE target trajectory — 62% to 78% in 6 months, (10) Decisions required. Use a professional dark grey and orange colour scheme.',
            'Ask Copilot: Create a customer communication slide showing each affected customer, their backlog in units, the expected delivery date under the recovery plan, and whether we are triggering any SLA penalty clauses. Format as a table with a RAG status column.',
            'Ask Copilot: Add a predictive maintenance roadmap slide showing a phased implementation: Phase 1 — vibration sensors on 3 failing machines (Month 1–2), Phase 2 — IoT dashboard and alerting (Month 3–4), Phase 3 — expand to all 12 machines (Month 5–6). Show estimated cost and OEE improvement for each phase.'
          ]
        },
        {
          tool: '📧 Copilot in Outlook',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Ask Copilot in Outlook: Draft a customer communication email to our top 3 automotive customers who are affected by the production backlog. The email should: acknowledge the delay without going into technical detail about the cause, provide the revised delivery schedule for their specific orders, confirm that no quality compromise has occurred, and offer a goodwill gesture (expedited shipping at our cost). Use a professional, accountable but not grovelling tone.',
            'Ask Copilot: Draft an urgent email to our CNC spindle motor supplier requesting emergency delivery of 3 replacement spindle motor units within 5 business days. The email should cite the criticality of the situation (production backlog, customer SLA risk), reference our existing supply agreement and volume commitment, and ask for a price for expedited delivery. Copy our procurement manager.',
            'Ask Copilot: Draft an internal email to all shift supervisors briefing them on the 3-shift recovery operation starting next Monday. Cover: the shift rotation schedule, the backlog clearance target per shift (160 units), the quality checkpoint requirements, and the escalation procedure if a machine goes down during the recovery period.'
          ]
        },
        {
          tool: '🎙 Copilot in Teams',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Use your OWN existing recorded Teams meetings. Open a meeting recap in Teams > Recap tab. Copilot generates summaries, action items, and follow-up drafts grounded in the actual transcript.',
          prompts: [
            'Open an existing recorded Teams meeting recap from an operations or production review. Ask Copilot: Extract all KPI figures mentioned — OEE, production output, backlog units, scrap rate, and delivery performance. Create a structured operations scorecard from the meeting data.',
            'Ask Copilot: Draft follow-up actions from this production meeting. Prioritise actions into: Critical (affects backlog clearance this week), High (affects SIRIM audit), Medium (process improvement). Assign owner and deadline to each.',
            'Ask Copilot: Were any customer escalations or SLA breaches discussed? List each customer, the SLA metric at risk, the current performance, and the recovery commitment made in the meeting.'
          ]
        },
        {
          tool: '📓 Copilot Notebook',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via copilot.microsoft.com > Notebook tab. Upload up to 5 files and set a system instruction. Best for synthesising insights across multiple documents simultaneously.',
          prompts: [
            'Upload 12_Zava_Manufacturing_KPIs.xlsx and 21_Zava_Chemical_Safety_HIRARC.docx to Copilot Notebook. Set instruction: "You are a manufacturing excellence consultant helping the Plant Manager prioritise recovery actions." Ask: Based on the KPI data and the operational situation, which 3 actions will have the greatest combined impact on OEE recovery and SIRIM audit readiness in the next 8 weeks? Rank them and explain the trade-offs.',
            'Upload 12_Zava_Manufacturing_KPIs.xlsx and 21_Zava_Chemical_Safety_HIRARC.docx. Ask: The safety document commits to specific machine guarding and chemical handling standards. Given that the plant is operating 3 shifts under backlog recovery pressure, what are the 3 highest safety risks that could materialise and what must the Plant Manager do before the extended shift schedule starts?'
          ]
        },
        {
          tool: '🤝 Cowork (Frontier)',
          license: 'M365 Copilot + Frontier Program',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Cowork is an autonomous agent that takes actions across Microsoft 365 on your behalf — sending emails, scheduling meetings, creating documents, posting in Teams, and scheduling recurring tasks. Access: m365.cloud.microsoft > left nav > Agents > Cowork. Requires Frontier program enrollment.',
          prompts: [
            'Do all of the following: (1) Research the best spindle motor suppliers in Malaysia and Singapore who can provide emergency delivery of Fanuc or Siemens spindle motors for CNC machines within 5 business days. (2) Draft an emergency procurement request to the top 2 suppliers with our technical specifications. (3) Email to both suppliers and CC our Procurement Manager asking for quotation within 24 hours. (4) Create a spindle motor replacement tracker in OneDrive showing: Machine ID | Motor Spec | Supplier | Order Date | Expected Delivery | Installation Date | Status. (5) Post an update in the #plant-operations Teams channel: "Emergency spindle motor procurement initiated for CNC-04, CNC-07, CNC-11. Quotations expected within 24 hours."',
            'Do all of the following for SIRIM audit prep: (1) Create an ISO 9001 audit readiness checklist based on the standard\'s 10 key clauses. (2) Email to all 5 department heads (Quality, Production, Maintenance, Logistics, HR) asking them to complete their section of the checklist within 1 week. (3) Schedule a pre-audit internal review meeting for 5 weeks before the SIRIM audit date. (4) Set a calendar reminder for yourself 3 weeks before the audit: "Final document readiness check". (5) Post in the #quality-management Teams channel: "SIRIM ISO 9001 audit is in 8 weeks. Please complete the readiness checklist sent via email within 1 week."'
          ]
        },
        {
          tool: '🤖 Word Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to a Word document. Open the .docx in Word for Web > Copilot pane > + New Agent > name it, write a description, set the document as knowledge source > Share. Colleagues chat with it in Teams or M365 Copilot.',
          prompts: [
            'Open 21_Zava_Chemical_Safety_HIRARC.docx in Word for Web. Create an agent called "Plant Safety & Compliance Bot". Description: "Answers questions from supervisors and operators about Zava Manufacturing\'s safety procedures, chemical handling requirements, machine guarding standards, and ISO 9001 quality requirements." Share with all plant supervisors.',
            'Demo: A production supervisor asks "We need to extend the shift to 12 hours to clear the backlog. What are the HSE requirements for extended shifts — are there additional risk assessment steps required and what welfare facilities must we provide?" Show how the agent provides a policy-grounded answer that protects both productivity and safety.'
          ]
        },
        {
          tool: '🤖 PowerPoint Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to a PowerPoint presentation. Great for strategy decks or Board presentations many people need to reference. Same setup as Word Agent but using a .pptx file.',
          prompts: [
            'Create a PowerPoint from the operations recovery presentation. Create an agent called "Manufacturing Recovery Board Bot". Share with the MD and key customer account managers.',
            'Demo: A customer account manager asks the agent "My customer Toyota is asking for a firm revised delivery date for their 480-unit order. What does the recovery plan show as the expected delivery date and is there any risk to that date?" Show how account managers get a precise, plan-grounded answer.'
          ]
        },
        {
          tool: '🤖 Excel Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to an Excel workbook. Colleagues ask data questions in plain English without opening Excel. Open .xlsx in Excel for Web > Copilot pane > + New Agent > set workbook as knowledge source > share.',
          prompts: [
            'Open 12_Zava_Manufacturing_KPIs.xlsx in Excel for Web. Create an agent called "Nilai Plant Operations Q&A". Description: "Answers questions on OEE by machine, production backlog, scrap rate, delivery performance, and SIRIM audit status for the Plant Manager and operations team." Share with plant leadership.',
            'Demo: Ask "What is the current OEE for CNC-04 and how many units is it producing per shift?" Then: "What is the total backlog for Toyota and when is the expected clearance date at current recovery pace?" Show how the Plant Manager gets instant operational intelligence.'
          ]
        },
        {
          tool: '🏗 Agent Builder (Copilot Studio)',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Build a custom declarative agent in Copilot Studio — no coding required. Access: copilotstudio.microsoft.com > Create > New Agent. Add name, description, knowledge sources (SharePoint URLs or uploaded files), topics/actions. Publish to Teams in under 10 minutes.',
          prompts: [
            'Go to copilotstudio.microsoft.com > Create > New Agent. Name it "Nilai Plant Intelligence Agent". Description: "Supports Zava Manufacturing Nilai plant supervisors and managers with instant answers on OEE performance, production backlog, SIRIM ISO 9001 requirements, machine maintenance procedures, and chemical safety — helping drive the OEE recovery from 62% to 78%." Upload 12_Zava_Manufacturing_KPIs.xlsx and 21_Zava_Chemical_Safety_HIRARC.docx. Add topics: "OEE & Production", "SIRIM Audit", "Machine Maintenance", "Safety". Publish to Teams.',
            'Demo the agent: A shift supervisor asks: "CNC-07 has just triggered a spindle overheat alarm for the third time this shift. We are in the middle of an urgent automotive customer run. Should I stop the machine, reduce speed, or can I continue? What does our maintenance protocol say and do I need to raise a maintenance work order immediately?" Show how the agent gives an operationally-grounded, safety-conscious answer that helps the supervisor make the right call.'
          ]
        }
      ]
    },
    {
      id: 'plantation',
      sectorId: 'plantation',
      subsector: '',
      name: 'Plantation & Agribusiness',
      icon: '🌿',
      color: '#388E3C',
      accent: '#43A047',
      company: 'Zava Agribusiness (Perkebunan Lestari)',
      tagline: 'RSPO suspended 2 mills — EUDR deadline Jan 2026 with 184,200 ha at risk.',
      scenario: 'Zava Agribusiness operates 184,200 hectares of oil palm in Kalimantan and Sabah. Two mills have had RSPO certification suspended following a third-party audit. The EU Deforestation Regulation (EUDR) deadline is January 2026 — all palm oil exported to the EU must be deforestation-free with full geolocation traceability. OER has declined to 19.4% vs the 21.2% industry benchmark.',
      files: [
        '11_Zava_Agribusiness_Plantations.xlsx',
        '22_Zava_Plantation_RSPO_Audit.docx',
        '20_Zava_ESG_Sustainability_Framework.docx',
        'Email_03_Cilegon_EHS_Enforcement.docx'
      ],
      prompts: [
        {
          tool: '🤖 Copilot Chat (Basic)',
          license: 'Free — no M365 Copilot license needed',
          account: 'Sasha Ouellet — SashaO@ABSx62256373.OnMicrosoft.com',
          desc: '',
          prompts: [
            'I am the Sustainability Director of a Malaysian-Indonesian palm oil plantation group. Two of our mills have had RSPO certification suspended and the EU Deforestation Regulation takes effect in January 2026, putting our EU-bound export volumes at risk. Draft a 300-word crisis communications brief for our investors. The brief should: acknowledge the RSPO suspension transparently, explain the remediation steps underway, describe our EUDR compliance programme, and reaffirm our commitment to sustainable palm oil. Tone: honest, accountable, and forward-looking.',
            'Explain the EU Deforestation Regulation (EUDR) requirements for palm oil exporters — specifically what traceability documentation is required, what the "no deforestation after December 31, 2020" cutoff date means in practice, and what the penalties are for non-compliance. Focus on the implications for a plantation with operations in Kalimantan.',
            'What is the RSPO remediation and complaints process? If two mills have had certification suspended, what specific steps must the company take to reinstate certification? What is the typical timeline and what evidence does RSPO require to lift a suspension?'
          ]
        },
        {
          tool: '🔍 Researcher',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via Microsoft 365 Copilot Chat (copilot.microsoft.com or Teams) > click Agents > Researcher. Grounds answers in live web sources and your organisation data with full citations.',
          prompts: [
            'Research the latest EUDR implementation updates — specifically for Indonesian and Malaysian palm oil exporters. I need: (1) The current implementation timeline (is the January 2026 deadline confirmed?), (2) Which EU member states are most actively enforcing, (3) The specific geolocation and due diligence documentation required, (4) Any industry body guidance from MPOB, RSPO, or MSPO on EUDR compliance. Provide citations.',
            'Research oil extraction rate (OER) improvement strategies for tropical oil palm in Southeast Asia. What are the key factors that drive the gap between 19.4% (our current OER) and the 21.2% industry benchmark? What mill process improvements and estate best practices have shown the highest OER improvement impact? Cite recent research or industry case studies.'
          ]
        },
        {
          tool: '📊 Analyst',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via Microsoft 365 Copilot Chat > click Agents > Analyst. Upload an Excel or CSV file. Analyst runs Python-style analysis, builds charts, and interprets results without you writing a single formula.',
          prompts: [
            'Upload 11_Zava_Agribusiness_Plantations.xlsx to Analyst. Ask: Analyse OER trends by mill over the past 8 quarters. Which mills have the lowest OER and what is the variance from the 21.2% industry benchmark? Calculate the revenue impact of the OER gap — if all mills operated at the industry benchmark OER, how much additional CPO would we have produced at current FFB tonnage and what is the MYR revenue impact at MYR 3,800/tonne? Show as a ranked table and a bar chart.',
            'Upload 11_Zava_Agribusiness_Plantations.xlsx and 22_Zava_Plantation_RSPO_Audit.docx. Ask: Cross-reference the EUDR compliance status of each estate block against the December 31, 2020 deforestation cutoff. Which estate blocks show land conversion activity after this date? Calculate the total hectarage at risk and the corresponding export volume that cannot be sold to EU buyers until remediation is complete. Present as a heat map.'
          ]
        },
        {
          tool: '📊 Copilot in Excel',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open 11_Zava_Agribusiness_Plantations.xlsx. Navigate to the Mill Performance sheet. Ask Copilot: Create an EUDR traceability compliance tracker on a new sheet. For each estate block, show: (1) Block ID and hectarage, (2) Geolocation coordinates (latitude/longitude), (3) Land conversion history pre/post December 2020, (4) RSPO certification status, (5) EUDR compliance status (Compliant/At Risk/Non-Compliant). Colour code: green = Compliant, red = Non-Compliant.',
            'Ask Copilot: In the Financial Performance sheet, model the revenue impact of losing EU market access for 12 months. Assume: 35% of CPO exports go to the EU, average EU premium of MYR 180/tonne over non-EU markets, total CPO production of 280,000 tonnes per year. Calculate: (1) Annual EU premium revenue at risk, (2) Revenue loss if EU volumes are diverted to non-EU markets at lower prices, (3) The cost to implement full EUDR compliance (estimate MYR 12M for satellite monitoring and traceability system). Show as a cost-benefit table.',
            'Ask Copilot: Create an OER improvement action plan on a new sheet. For the 5 mills with the lowest OER, identify the 3 most impactful improvement actions for each (based on the audit findings in the strategy data). Calculate the projected OER improvement if all actions are implemented and the resulting additional CPO revenue per mill.'
          ]
        },
        {
          tool: '📝 Copilot in Word',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open 22_Zava_Plantation_RSPO_Audit.docx. Ask Copilot: Draft a 3-page RSPO remediation plan for the two suspended mills. Structure: (1) Summary of audit findings that led to the suspension, (2) Corrective actions for each finding — with responsible person, action description, and completion date, (3) Evidence to be provided to RSPO verifier — list by finding, (4) Stakeholder grievance resolution plan — addressing any community or worker complaints raised in the audit, (5) Timeline to reinstatement — target 4 months. Use formal RSPO reporting language.',
            'Ask Copilot: Draft an EUDR due diligence statement template for use with our EU customers. The statement should: assert that the palm oil in the specified shipment was produced on land not deforested after December 31, 2020, reference the geolocation data supporting this assertion, confirm RSPO or MSPO certification (where applicable), and provide the name and contact of the responsible officer. Format to meet EU regulatory requirements.',
            'Ask Copilot: Draft a letter to our top 3 EU customers (who together represent 28% of our CPO sales) explaining our EUDR compliance programme. The letter should: confirm our commitment to full EUDR compliance by January 2026, describe our traceability system implementation, acknowledge the RSPO suspension and the remediation timeline, and assure them that their supply volumes will not be affected. Keep it professional and confidence-building.'
          ]
        },
        {
          tool: '🎯 Copilot in PowerPoint',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Ask Copilot in PowerPoint: Create a 12-slide sustainability investor briefing presentation. Include: (1) Portfolio overview — 184,200 ha, (2) RSPO suspension — cause, remediation, timeline, (3) EUDR compliance programme — progress dashboard, (4) Traceability system implementation, (5) OER improvement roadmap, (6) ESG rating trajectory, (7) Community and social commitments, (8) Financial impact of EUDR compliance investment, (9) Competitive positioning — sustainability as a market differentiator, (10) Key milestones FY2026, (11) Risks and mitigants, (12) Our Net Zero pathway. Use green and earthy tones.',
            'Ask Copilot: Create a 2-slide RSPO suspension update for the Board. Slide 1: What happened — the audit findings and suspension notice. Slide 2: What we are doing — remediation plan, timeline, and expected reinstatement date. Keep it factual, accountable, and concise.',
            'Ask Copilot: Add a geolocation compliance map slide showing our estate blocks colour-coded by EUDR compliance status (green/amber/red). Include statistics: total compliant hectarage, at-risk hectarage, and non-compliant hectarage.'
          ]
        },
        {
          tool: '📧 Copilot in Outlook',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Ask Copilot in Outlook: Draft a formal response to the RSPO complaints panel regarding the two suspended mills. The letter should: acknowledge the suspension, provide a timeline for remediation, note the corrective actions already completed, and request a re-audit within 4 months. Use formal RSPO correspondence language.',
            'Ask Copilot: Draft an email to the EU customer relations team providing an EUDR compliance update. The email should confirm our traceability system is on track for full deployment by October 2025, attach our current compliance certificate for unaffected estate blocks, and outline the due diligence documentation we will provide with each shipment from November 2025.',
            'Ask Copilot: Summarise the email thread in Email_03_Cilegon_EHS_Enforcement.docx and identify any findings from the enforcement action that also affect our plantation operations. List each relevant finding with the corrective action required and the deadline.'
          ]
        },
        {
          tool: '🎙 Copilot in Teams',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Use your OWN existing recorded Teams meetings. Open a meeting recap in Teams > Recap tab. Copilot generates summaries, action items, and follow-up drafts grounded in the actual transcript.',
          prompts: [
            'Open an existing recorded Teams meeting recap from a sustainability or RSPO compliance meeting. Ask Copilot: Identify all RSPO remediation commitments made, the responsible mill manager for each, and the evidence submission deadline. Format as a formal RSPO remediation action register.',
            'Ask Copilot: Draft a follow-up communication to all mill managers and estate supervisors covering the EUDR traceability requirements. Include a simple checklist of what data each manager must collect and submit monthly to the central traceability system.',
            'Ask Copilot: Were any community or worker grievances mentioned in this meeting? List each with the nature of the grievance, the mill or estate it relates to, and whether it has been formally logged in the RSPO grievance mechanism.'
          ]
        },
        {
          tool: '📓 Copilot Notebook',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via copilot.microsoft.com > Notebook tab. Upload up to 5 files and set a system instruction. Best for synthesising insights across multiple documents simultaneously.',
          prompts: [
            'Upload 11_Zava_Agribusiness_Plantations.xlsx, 22_Zava_Plantation_RSPO_Audit.docx, and 20_Zava_ESG_Sustainability_Framework.docx to Copilot Notebook. Set instruction: "You are an ESG advisor helping the Sustainability Director navigate RSPO and EUDR simultaneously." Ask: Given that we must reinstate RSPO certification for 2 mills AND achieve EUDR compliance by January 2026, what is the optimal sequencing of activities over the next 6 months? Where do the requirements overlap and where do they conflict?',
            'Upload 11_Zava_Agribusiness_Plantations.xlsx and 20_Zava_ESG_Sustainability_Framework.docx. Ask: Our sustainability framework commits to zero deforestation across all new development. The EUDR requires proof of no deforestation after December 2020. Based on the estate data, are there any estates where our current commitments may not meet the EUDR standard? Identify any gaps and recommend how to address them.'
          ]
        },
        {
          tool: '🤝 Cowork (Frontier)',
          license: 'M365 Copilot + Frontier Program',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Cowork is an autonomous agent that takes actions across Microsoft 365 on your behalf — sending emails, scheduling meetings, creating documents, posting in Teams, and scheduling recurring tasks. Access: m365.cloud.microsoft > left nav > Agents > Cowork. Requires Frontier program enrollment.',
          prompts: [
            'Do all of the following for RSPO reinstatement: (1) Research the RSPO remediation process and the typical evidence required to lift a mill certification suspension. (2) Draft a month-by-month remediation plan for both suspended mills covering the next 4 months. (3) Save to OneDrive as "RSPO Reinstatement Plan - [Date]". (4) Email to the VP Sustainability and both Mill Managers asking for review and commitment by Friday. (5) Schedule a bi-weekly RSPO Remediation Check-In via Teams every other Monday starting next week.',
            'Do all of the following for EUDR compliance: (1) Research satellite-based deforestation monitoring solutions suitable for palm oil operations — identify 3 vendors operating in Indonesia/Malaysia with EUDR-compliant outputs. (2) Draft an RFP (Request for Proposal) for a traceability system covering satellite monitoring + supply chain geolocation. (3) Save the RFP to OneDrive. (4) Email the RFP to the 3 vendors and to our Head of IT and Head of Sustainability asking for proposals within 3 weeks. (5) Schedule a Vendor Evaluation Workshop for 4 weeks from today.'
          ]
        },
        {
          tool: '🤖 Word Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to a Word document. Open the .docx in Word for Web > Copilot pane > + New Agent > name it, write a description, set the document as knowledge source > Share. Colleagues chat with it in Teams or M365 Copilot.',
          prompts: [
            'Open 22_Zava_Plantation_RSPO_Audit.docx in Word for Web. Create an agent called "RSPO Compliance Agent". Description: "Answers questions from mill managers and sustainability officers about RSPO certification requirements, audit findings, remediation procedures, and grievance handling — grounded in our official RSPO audit documents." Share with all mill and estate managers.',
            'Demo: A mill manager asks "The RSPO auditor flagged that we do not have documented evidence of our riparian buffer zone maintenance for the past 12 months. What evidence do I need to provide, in what format, and by when to close this non-conformance?" Show how the agent gives a precise, audit-grounded remediation guide.'
          ]
        },
        {
          tool: '🤖 PowerPoint Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to a PowerPoint presentation. Great for strategy decks or Board presentations many people need to reference. Same setup as Word Agent but using a .pptx file.',
          prompts: [
            'Create a PowerPoint from the sustainability investor briefing. Create an agent called "Sustainability Briefing Bot". Share with ESG-focused investors and rating agencies such as MSCI and Sustainalytics.',
            'Demo: An ESG analyst asks "What percentage of your total hectarage is currently EUDR-compliant with full geolocation data submitted, and what is your projected compliance rate by October 2025?" Show how the agent provides a precise, data-grounded answer for ESG due diligence.'
          ]
        },
        {
          tool: '🤖 Excel Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to an Excel workbook. Colleagues ask data questions in plain English without opening Excel. Open .xlsx in Excel for Web > Copilot pane > + New Agent > set workbook as knowledge source > share.',
          prompts: [
            'Open 11_Zava_Agribusiness_Plantations.xlsx in Excel for Web. Create an agent called "Plantation Operations & ESG Q&A". Description: "Instant answers on OER by mill, RSPO certification status, EUDR compliance by estate block, and CPO production for the sustainability and operations teams." Share with senior management and external ESG auditors.',
            'Demo: Ask "What is the total hectarage currently non-compliant with EUDR and what CPO volume does that represent?" Then: "Which mill has the lowest OER this quarter and by how much does it fall short of the industry benchmark?" Show how the sustainability team gets instant data-grounded answers.'
          ]
        },
        {
          tool: '🏗 Agent Builder (Copilot Studio)',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Build a custom declarative agent in Copilot Studio — no coding required. Access: copilotstudio.microsoft.com > Create > New Agent. Add name, description, knowledge sources (SharePoint URLs or uploaded files), topics/actions. Publish to Teams in under 10 minutes.',
          prompts: [
            'Go to copilotstudio.microsoft.com > Create > New Agent. Name it "Perkebunan Lestari Compliance & Ops Agent". Description: "Supports Zava Agribusiness mill managers and sustainability teams with answers on RSPO certification, EUDR traceability requirements, OER improvement, and ESG reporting — ensuring consistent, document-grounded guidance across all 184,200 hectares of operations." Upload 11_Zava_Agribusiness_Plantations.xlsx, 22_Zava_Plantation_RSPO_Audit.docx, and 20_Zava_ESG_Sustainability_Framework.docx. Add topics: "RSPO Compliance", "EUDR Traceability", "OER Improvement", "ESG Reporting". Publish to Teams for all mill and estate managers.',
            'Demo the agent: An estate manager in Kalimantan asks: "A community representative has just filed a land rights grievance claiming that 120 hectares of our Block K-14 was traditionally used for community farming and was converted without free, prior and informed consent (FPIC). What is our RSPO FPIC obligation in this situation, what is the grievance response process, and do I need to immediately suspend operations in that block?" Show how the agent provides a comprehensive, policy-grounded response.'
          ]
        }
      ]
    },
    {
      id: 'bpo-services',
      sectorId: 'technology',
      subsector: '',
      name: 'BPO Services',
      icon: '🖥',
      color: '#01579B',
      accent: '#0277BD',
      company: 'Zava BPO (Bengaluru Centre)',
      tagline: 'Attrition 31.2% — Bank Mandiri renewal MYR 84M at risk. DOCUAI at 99.8% accuracy.',
      scenario: 'Zava BPO\'s Bengaluru Centre houses 3,200 FTE across banking, insurance, and healthcare process outsourcing. Staff attrition has surged to 31.2% (industry benchmark: 22%). The Bank Mandiri BPO contract worth MYR 84M is up for renewal — client satisfaction score is 6.8/10, below the 7.5 renewal threshold. DOCUAI (document processing AI) is performing at 99.8% accuracy.',
      files: [
        '15_Zava_BPO_Operations.xlsx',
        '18_Zava_HR_Analytics.xlsx',
        'Email_13_Bengaluru_Attrition_Crisis.docx',
        'Email_12_BPO_Contract_Pipeline.docx'
      ],
      prompts: [
        {
          tool: '🤖 Copilot Chat (Basic)',
          license: 'Free — no M365 Copilot license needed',
          account: 'Sasha Ouellet — SashaO@ABSx62256373.OnMicrosoft.com',
          desc: '',
          prompts: [
            'I am the MD of a BPO centre in Bengaluru with 3,200 FTE. Attrition has hit 31.2% against an industry benchmark of 22%, and my largest client — Bank Mandiri — has given us a satisfaction score of 6.8/10 against a 7.5 renewal threshold. The MYR 84M contract is up for renewal in 4 months. Draft a 300-word account recovery brief covering: the 3 most likely drivers of the low satisfaction score, the immediate actions I should take to demonstrate commitment to Mandiri before the renewal meeting, and the retention risk if we lose this contract.',
            'What are the most effective strategies to reduce BPO attrition in the Indian IT-BPO sector? Focus on approaches that have been proven to work for 3,000+ FTE operations. Rank the top 5 strategies by speed of impact — I need results within 90 days not 12 months.',
            'Explain how AI-powered document processing (such as OCR + NLP) is changing BPO service delivery. What is a realistic accuracy target for a well-trained model on structured financial documents? How should a BPO operator position AI as a productivity enhancer rather than a threat to its workforce in client conversations?'
          ]
        },
        {
          tool: '🔍 Researcher',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via Microsoft 365 Copilot Chat (copilot.microsoft.com or Teams) > click Agents > Researcher. Grounds answers in live web sources and your organisation data with full citations.',
          prompts: [
            'Research BPO industry attrition benchmarks in Bengaluru specifically for banking and insurance process outsourcing. I need: (1) Average and top-quartile attrition rates for 2024 and 2025, (2) The top 5 reasons BPO employees cite for leaving, (3) The most effective retention bonuses and non-monetary benefits used by leading BPO operators in India. Provide citations.',
            'Research the competitive landscape for banking BPO services in Southeast Asia — specifically for Indonesian bank clients. Who are the top BPO providers competing for Bank Mandiri-scale contracts? What differentiators are most valued by Indonesian banking clients — cost, accuracy, turnaround time, or regulatory compliance expertise? Cite industry sources.'
          ]
        },
        {
          tool: '📊 Analyst',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via Microsoft 365 Copilot Chat > click Agents > Analyst. Upload an Excel or CSV file. Analyst runs Python-style analysis, builds charts, and interprets results without you writing a single formula.',
          prompts: [
            'Upload 18_Zava_HR_Analytics.xlsx to Analyst. Ask: Analyse attrition data for Zava BPO Bengaluru by department, tenure band, and job level. Which department has the highest attrition? Are employees leaving most within the first 6 months (early attrition) or after 12–24 months (mid-tenure)? Calculate the fully-loaded replacement cost per FTE (assume USD 2,800 per hire including training) and the total annual attrition cost. Show as a heat map and cost waterfall.',
            'Upload 15_Zava_BPO_Operations.xlsx to Analyst. Ask: Analyse the Bank Mandiri contract SLA performance over the last 12 months. Which SLA metrics — turnaround time, accuracy, escalation rate, CSAT — are below the contract threshold? Calculate the weighted satisfaction score and identify the 3 metrics most correlated with the low CSAT score of 6.8. Show as a correlation matrix and a trend chart.'
          ]
        },
        {
          tool: '📊 Copilot in Excel',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open 15_Zava_BPO_Operations.xlsx. Navigate to the SLA Performance sheet. Ask Copilot: Build a Bank Mandiri account recovery dashboard on a new sheet. For each of the 8 SLA metrics in the contract, show: (1) Contract threshold, (2) Last 3 months actual performance, (3) Status vs threshold (RAG), (4) Trend (Improving/Stable/Declining). Highlight in red any metric that is below threshold AND declining.',
            'Ask Copilot: Create an attrition cost model on a new sheet. Calculate: (1) Total FTE lost to attrition last 12 months (31.2% of 3,200), (2) Replacement cost per FTE at USD 2,800, (3) Total attrition cost, (4) Productivity loss during new hire ramp-up (assume 60% productivity for first 3 months), (5) Total cost including productivity loss. Compare against the cost of a MYR 2M retention programme. Show the ROI of the retention programme.',
            'Ask Copilot: In the Contract Pipeline sheet, calculate the total contract renewal value at risk in the next 12 months. For each contract marked "At Risk", show the contract value, the renewal probability (based on current CSAT), and the expected value. Rank by expected value at risk and flag any contract where the CSAT score is below the renewal threshold.'
          ]
        },
        {
          tool: '📝 Copilot in Word',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open Email_13_Bengaluru_Attrition_Crisis.docx. Ask Copilot: Draft a comprehensive attrition reduction action plan of 2 pages. Cover: (1) Root cause analysis — 3 key drivers based on exit interview data, (2) Five retention initiatives — retention bonus structure, career pathing programme, flexible work policy, wellness benefits, and manager excellence training, (3) KPIs: target attrition rate of 24% within 6 months, (4) Investment required: MYR 2M, projected ROI through reduced replacement cost and improved client CSAT, (5) Governance: who owns each initiative. Use a business case format.',
            'Open Email_12_BPO_Contract_Pipeline.docx. Ask Copilot: Draft a Bank Mandiri account recovery plan in the format of a client executive briefing. Cover: (1) Current SLA performance — transparent acknowledgement of the 3 metrics below threshold, (2) Root cause — the attrition impact on experienced staff levels, (3) Recovery plan — 6 specific commitments with measurable targets, (4) DOCUAI deployment — how AI will improve accuracy and turnaround for Mandiri processes, (5) Our investment commitment — dedicated Mandiri team ring-fenced from attrition impact. Keep it confident and specific.',
            'Ask Copilot: Write a DOCUAI capability one-pager for the Bank Mandiri renewal meeting. The document should explain in client-friendly language: what DOCUAI does (OCR + NLP for financial document processing), the 99.8% accuracy achievement vs the 98.5% industry benchmark, the turnaround time improvement (from 4 hours to 45 minutes for standard forms), and the integration with Mandiri\'s existing document management system.'
          ]
        },
        {
          tool: '🎯 Copilot in PowerPoint',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Ask Copilot in PowerPoint: Create a 12-slide Bank Mandiri contract renewal presentation. Include: (1) Partnership overview — 5 years, 850 FTE dedicated, (2) Service delivery scorecard — 12-month trend, (3) Transparent acknowledgement of 3 below-threshold metrics, (4) Root cause — attrition impact and what we have done, (5) Recovery plan — 6 commitments with targets, (6) DOCUAI — live demo results for Mandiri process types, (7) New value-add proposition — 3 additional services we can offer, (8) Dedicated Mandiri team structure — ring-fenced, (9) Proposed renewal terms, (10) Investment in Mandiri\'s success — our commitments, (11) Testimonials from other banking BPO clients, (12) Recommended next steps. Use navy blue and white.',
            'Ask Copilot: Create a 2-slide attrition update for the Zava Group Board. Slide 1: The Bengaluru attrition crisis — root causes and financial impact. Slide 2: The retention action plan — 5 initiatives, MYR 2M investment, and projected CSAT recovery impact.',
            'Ask Copilot: Add a DOCUAI impact slide showing a before/after process flow diagram — how Bank Mandiri\'s loan documentation process worked before DOCUAI (4 hours, 3 manual steps, 2.1% error rate) vs after DOCUAI (45 minutes, 1 review step, 0.2% error rate).'
          ]
        },
        {
          tool: '📧 Copilot in Outlook',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open Email_12_BPO_Contract_Pipeline.docx. Ask Copilot in Outlook: Draft a proactive email to Bank Mandiri\'s procurement lead requesting a contract renewal review meeting. The email should: acknowledge that we are aware the CSAT score fell below threshold in Q3, take accountability and briefly describe what we have done to address it, and request a 90-minute business review meeting 6 weeks before the contract expiry. Tone: confident and relationship-focused, not defensive.',
            'Ask Copilot: Draft an internal email to the Bengaluru Centre leadership team briefing them on the Bank Mandiri renewal risk and the recovery plan. Be direct about the stakes: losing this contract will result in 850 role reductions. Ask each department head to submit their specific commitments for the account recovery plan within 3 days.',
            'Open Email_13_Bengaluru_Attrition_Crisis.docx. Ask Copilot: Summarise the key facts and decisions from this email thread. What commitments were made by the Bengaluru HR Director to the Group CEO? List each commitment with the deadline. Draft a status update email from the HR Director to the CEO confirming progress on each commitment.'
          ]
        },
        {
          tool: '🎙 Copilot in Teams',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Use your OWN existing recorded Teams meetings. Open a meeting recap in Teams > Recap tab. Copilot generates summaries, action items, and follow-up drafts grounded in the actual transcript.',
          prompts: [
            'Open an existing recorded Teams meeting recap from an account review or operations meeting. Ask Copilot: Identify all client commitments discussed — specific SLA improvements, process changes, or escalation resolutions. List each with owner and deadline. Flag any commitment made to Bank Mandiri that has a deadline within the next 30 days.',
            'Ask Copilot: Draft follow-up actions for the attrition reduction taskforce based on this meeting. Group by initiative: Retention Bonus | Career Pathing | Manager Training | Wellness | Flexible Work. Include the HR business partner responsible and the target completion date.',
            'Ask Copilot: Based on this meeting, what is the overall tone regarding the Bank Mandiri renewal — confident, uncertain, or at risk? Identify the 3 most important statements made about the renewal and what they imply about the likelihood of securing it.'
          ]
        },
        {
          tool: '📓 Copilot Notebook',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via copilot.microsoft.com > Notebook tab. Upload up to 5 files and set a system instruction. Best for synthesising insights across multiple documents simultaneously.',
          prompts: [
            'Upload 15_Zava_BPO_Operations.xlsx, 18_Zava_HR_Analytics.xlsx, and Email_12_BPO_Contract_Pipeline.docx to Copilot Notebook. Set instruction: "You are a BPO turnaround specialist. The MD needs to retain the Bank Mandiri contract and reduce attrition simultaneously." Ask: Based on all three documents, what is the single most important action the MD should take in the next 2 weeks that will have the greatest positive impact on BOTH the Bank Mandiri renewal AND the attrition crisis?',
            'Upload 15_Zava_BPO_Operations.xlsx and Email_13_Bengaluru_Attrition_Crisis.docx. Ask: The attrition data and the contract pipeline show a direct link — high attrition is leading to experienced staff losses which is driving down CSAT. Quantify this connection: for each 1 percentage point increase in attrition, estimate the impact on the Bank Mandiri CSAT score based on the data patterns. At what attrition rate does CSAT drop below the 7.5 renewal threshold?'
          ]
        },
        {
          tool: '🤝 Cowork (Frontier)',
          license: 'M365 Copilot + Frontier Program',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Cowork is an autonomous agent that takes actions across Microsoft 365 on your behalf — sending emails, scheduling meetings, creating documents, posting in Teams, and scheduling recurring tasks. Access: m365.cloud.microsoft > left nav > Agents > Cowork. Requires Frontier program enrollment.',
          prompts: [
            'Do all of the following: (1) Research Bank Mandiri\'s latest annual report and public statements about their BPO and digital transformation strategy to understand what they value most in a BPO partner. (2) Draft a 2-page Bank Mandiri-specific value proposition document showing how Zava BPO aligns with their strategic priorities. (3) Save to OneDrive as "Bank Mandiri Renewal Value Prop". (4) Email to the Account Director and MD asking for review before the renewal meeting. (5) Schedule a 2-hour "Mandiri Renewal Prep" session for next week with the Account Director, Head of Operations, and DOCUAI Product Lead.',
            'Do all of the following for attrition: (1) Analyse the exit interview data from the past 6 months (from the HR Analytics data) and identify the top 3 reasons for resignation. (2) Draft 3 targeted retention initiatives — one addressing each root cause. (3) Create a retention programme proposal document in Word. (4) Email to the Group HR Director and Bengaluru Centre HR Head for approval. (5) Schedule a town hall meeting for all Bengaluru staff next Friday to announce the retention programme.'
          ]
        },
        {
          tool: '🤖 Word Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to a Word document. Open the .docx in Word for Web > Copilot pane > + New Agent > name it, write a description, set the document as knowledge source > Share. Colleagues chat with it in Teams or M365 Copilot.',
          prompts: [
            'Open Email_12_BPO_Contract_Pipeline.docx in Word for Web. Create an agent called "BPO Contract Intelligence Bot". Description: "Answers questions about Zava BPO\'s contract pipeline, SLA performance, account renewal status, and recovery plans — for the MD and account management team." Share with the account management and commercial teams.',
            'Demo: An account manager asks "What is the current CSAT score for Bank Mandiri and what specific SLA metrics are below the renewal threshold? What commitments have we made in the account recovery plan?" Show how the team gets instant, document-grounded account intelligence.'
          ]
        },
        {
          tool: '🤖 PowerPoint Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to a PowerPoint presentation. Great for strategy decks or Board presentations many people need to reference. Same setup as Word Agent but using a .pptx file.',
          prompts: [
            'Create a PowerPoint from the Bank Mandiri renewal presentation. Create an agent called "Mandiri Renewal Deck Bot". Share with the Bank Mandiri procurement team as a pre-meeting resource and with internal leadership.',
            'Demo: A Mandiri procurement officer asks "What specific accuracy improvement has Zava BPO achieved on our loan documentation process since DOCUAI was deployed, and what is the new turnaround time SLA you are proposing for Year 2?" Show how the agent handles client due diligence questions with specific, documented answers.'
          ]
        },
        {
          tool: '🤖 Excel Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to an Excel workbook. Colleagues ask data questions in plain English without opening Excel. Open .xlsx in Excel for Web > Copilot pane > + New Agent > set workbook as knowledge source > share.',
          prompts: [
            'Open 15_Zava_BPO_Operations.xlsx in Excel for Web. Create an agent called "BPO Operations Analytics Q&A". Description: "Instant answers on SLA performance by client, attrition by department, contract renewal status, and DOCUAI accuracy — for the MD and operations leadership." Share with operations and commercial leadership.',
            'Demo: Ask "What is the current turnaround time SLA performance for Bank Mandiri\'s loan document processing and how does it compare to the contract threshold?" Then: "Which department in the Bengaluru Centre has the highest attrition rate this quarter?" Show how management gets rapid operational intelligence.'
          ]
        },
        {
          tool: '🏗 Agent Builder (Copilot Studio)',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Build a custom declarative agent in Copilot Studio — no coding required. Access: copilotstudio.microsoft.com > Create > New Agent. Add name, description, knowledge sources (SharePoint URLs or uploaded files), topics/actions. Publish to Teams in under 10 minutes.',
          prompts: [
            'Go to copilotstudio.microsoft.com > Create > New Agent. Name it "Zava BPO Client Success Bot". Description: "Supports Zava BPO\'s account management and operations teams with instant answers on SLA commitments, contract terms, DOCUAI capabilities, attrition impact on service delivery, and account recovery plans — helping retain key clients and win renewals." Upload 15_Zava_BPO_Operations.xlsx, 18_Zava_HR_Analytics.xlsx, and Email_12_BPO_Contract_Pipeline.docx. Add topics: "SLA Performance", "Contract Renewal", "DOCUAI Capabilities", "Attrition Impact". Publish to Teams for the account management and operations leadership.',
            'Demo the agent: During the Bank Mandiri renewal negotiation, the client asks: "If your attrition is at 31%, how can you guarantee that the 850-person team we have been working with will remain intact for Year 2 of the contract? What contractual commitment can you give us on staff retention for our account?" Show how the account director uses the agent to pull the specific retention commitment and ring-fencing proposal from the recovery plan in real-time during the negotiation.'
          ]
        }
      ]
    },
    {
      id: 'telco',
      sectorId: 'media-telco',
      subsector: '',
      name: 'Telecommunications',
      icon: '📡',
      color: '#4A148C',
      accent: '#6A1B9A',
      company: 'ClearWave Communications Berhad',
      tagline: '5G at 12.4% vs 20% target — MCMC penalty risk + Nexus Home FMC bundle launch.',
      scenario: 'ClearWave Communications Berhad is Malaysia\'s third-largest telco with 14.8 million subscribers. 5G coverage has reached only 12.4% of the population against MCMC\'s 20% year-end target. An MCMC penalty notice has been issued. The Nexus Home fixed-mobile convergence (FMC) bundle is launching in Q2 FY2026. Postpaid ARPU has declined 8.4% year-on-year.',
      files: [
        'TC_01_ClearWave_Communications.xlsx',
        'TC_02_ClearWave_Strategy.docx'
      ],
      prompts: [
        {
          tool: '🤖 Copilot Chat (Basic)',
          license: 'Free — no M365 Copilot license needed',
          account: 'Sasha Ouellet — SashaO@ABSx62256373.OnMicrosoft.com',
          desc: '',
          prompts: [
            'I am the CTO of a Malaysian telecommunications company. Our 5G rollout is at 12.4% population coverage against MCMC\'s 20% year-end target and we have received a penalty notice. Draft a 300-word 5G acceleration plan brief for my CEO and MCMC that covers: the 3 main obstacles to our rollout (site acquisition, backhaul capacity, power supply to rural sites), the acceleration actions we have taken since the penalty notice, and the revised coverage milestone commitments we can credibly commit to for Q3 and Q4. Tone: transparent, committed, and technically credible.',
            'Explain what a fixed-mobile convergence (FMC) bundle is and why it is strategically important for a telco in 2025–2026. What are the key customer value propositions, the typical bundling models (ARPU lift, churn reduction, net promoter score impact), and the technical infrastructure requirements? Keep the answer under 200 words.',
            'What are the most effective strategies for reversing postpaid ARPU decline in a competitive telco market? Focus on Malaysia specifically — what are the pricing and bundling approaches that have worked for Maxis and Celcom? What role does 5G play in ARPU recovery?'
          ]
        },
        {
          tool: '🔍 Researcher',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via Microsoft 365 Copilot Chat (copilot.microsoft.com or Teams) > click Agents > Researcher. Grounds answers in live web sources and your organisation data with full citations.',
          prompts: [
            'Research MCMC\'s 5G rollout requirements and enforcement framework for Malaysian telecommunications operators. I need: (1) The specific coverage and population penetration milestones MCMC requires, (2) The penalty structure for missing milestones, (3) Any recent MCMC statements about enforcement flexibility or remediation pathways for operators missing targets. Provide citations.',
            'Research global FMC bundle performance data — specifically how bundles of fixed broadband + mobile postpaid + OTT content have affected ARPU, churn rate, and NPS for telcos in comparable markets (Singapore, Australia, UK). What are the 3 most important success factors for a successful FMC launch? Cite industry reports.'
          ]
        },
        {
          tool: '📊 Analyst',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via Microsoft 365 Copilot Chat > click Agents > Analyst. Upload an Excel or CSV file. Analyst runs Python-style analysis, builds charts, and interprets results without you writing a single formula.',
          prompts: [
            'Upload TC_01_ClearWave_Communications.xlsx to Analyst. Ask: Analyse 5G rollout progress by region and state. Which states have the largest gap between actual and target coverage? What is the correlation between 5G coverage and postpaid subscriber growth in those states? Create a map-style table showing: State | 5G Coverage % | Target % | Gap | Postpaid Growth Rate. Highlight in red any state where coverage gap exceeds 10 percentage points.',
            'Upload TC_01_ClearWave_Communications.xlsx. Ask: Analyse ARPU trends for postpaid, prepaid, and home broadband segments over the last 8 quarters. Which segment is declining fastest? Calculate the total ARPU decline impact on annual revenue. Build a churn rate cohort analysis — for the Nexus Home FMC bundle pilot (500 subscribers), what is the 3-month churn rate compared to non-bundle postpaid subscribers? Show as trend charts.'
          ]
        },
        {
          tool: '📊 Copilot in Excel',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open TC_01_ClearWave_Communications.xlsx. Navigate to the 5G Rollout Tracker sheet. Ask Copilot: Build a 5G acceleration model showing the monthly site activation required to reach 20% population coverage by December 31, 2026. Current pace is 80 sites/month. Calculate: (1) Sites needed to close the gap, (2) Monthly activation rate required to reach target by December, (3) Additional capex required vs current budget at MYR 1.8M per site. Flag if the required activation rate exceeds our current deployment team capacity.',
            'Ask Copilot: Create a Nexus Home FMC bundle revenue model on a new sheet. Assume: (1) Target of 180,000 bundle subscribers in Year 1, (2) Bundle ARPU of MYR 158/month vs current postpaid ARPU of MYR 82 and fixed broadband ARPU of MYR 110 separately, (3) Churn rate improvement from 2.1% to 1.4% for bundle subscribers. Calculate: Year 1 incremental revenue, Year 1 churn avoidance revenue, and 3-year NPV of the bundle at 10% discount rate.',
            'Ask Copilot: In the Network Quality sheet, calculate the average 5G download speed (Mbps) and latency (ms) per region. How do our 5G KPIs compare to our stated commitments to MCMC (100 Mbps download, <20ms latency)? Flag any region where we are below commitment and calculate the impact on the MCMC penalty calculation.'
          ]
        },
        {
          tool: '📝 Copilot in Word',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open TC_02_ClearWave_Strategy.docx. Ask Copilot: Draft a formal response to the MCMC penalty notice. The response should: acknowledge the coverage shortfall factually, explain the root causes (site acquisition delays, backhaul supply constraints), present a credible revised milestone commitment for 16% coverage by Q3 and 20% by Q4, note the acceleration investments already committed (MYR 280M additional capex), and request a bilateral meeting to discuss the penalty mitigation framework. Use formal regulatory correspondence tone.',
            'Ask Copilot: Draft the Nexus Home FMC bundle launch go-to-market brief of 2 pages. Cover: (1) Bundle proposition — what is included (postpaid line, home fibre, and 3 OTT subscriptions), (2) Target customer segment — multi-person households currently on separate contracts, (3) Pricing — MYR 158/month vs MYR 192 for equivalent standalone products, (4) Sales channel strategy — direct digital, retail, and retention saves, (5) Key success metrics — 180,000 subscribers Year 1, churn reduction to 1.4%.',
            'Ask Copilot: Summarise the competitive intelligence section of this strategy document. Who are our top 3 competitors, what are their 5G coverage levels and ARPU positions, and where are we competitively advantaged or disadvantaged? Create a simple competitive matrix.'
          ]
        },
        {
          tool: '🎯 Copilot in PowerPoint',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Ask Copilot in PowerPoint: Create a 12-slide Board presentation titled "5G Recovery & FMC Growth Strategy". Include: (1) Current situation — 5G at 12.4%, MCMC penalty, ARPU decline, (2) Root cause analysis — 5G rollout blockers, (3) 5G acceleration plan — monthly milestones and capex, (4) MCMC engagement strategy, (5) FMC bundle — product overview and pricing, (6) FMC revenue model — 3-year projection, (7) Subscriber growth outlook — 5G and FMC impact, (8) Competitive positioning, (9) Network quality dashboard, (10) Financial outlook — ARPU recovery, (11) Risk register, (12) Board decisions required. Purple and white colour scheme.',
            'Ask Copilot: Create a one-slide Nexus Home FMC customer value proposition visual. Show the bundle components as overlapping circles (Venn diagram style): Mobile | Home Broadband | OTT Content. In the overlap area, show the bundle benefits: MYR 34 monthly saving, one bill, shared data pool, priority 5G access.',
            'Ask Copilot: Add a 5G coverage heat map slide showing coverage by state against MCMC target. Use green (at target), amber (within 5%), red (below by more than 5%). Add a timeline showing the monthly activation plan to reach 20% by December.'
          ]
        },
        {
          tool: '📧 Copilot in Outlook',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Ask Copilot in Outlook: Draft a formal response letter to the MCMC penalty notice. Reference the notice number, acknowledge the coverage shortfall, present our revised milestone commitments (16% by Q3, 20% by Q4), outline the MYR 280M acceleration investment, and request a bilateral meeting. Attach the 5G acceleration plan as an annex (note: attach separately). Use the formal regulatory correspondence format.',
            'Ask Copilot: Draft an internal brief email to the 5G Rollout Taskforce with 3 action items: (1) prioritise site acquisition in the 5 most under-covered states, (2) escalate backhaul supply chain constraints to the CEO for resolution, (3) submit revised rollout milestone report to MCMC by Friday. Include the urgency context: penalty risk if we do not demonstrate credible progress.',
            'Ask Copilot: Draft a launch announcement email to our top 500 high-value postpaid customers introducing the Nexus Home FMC bundle. The email should explain the bundle, highlight the MYR 34 monthly saving, include a limited early adopter offer (first 3 months at 50% off), and provide a direct link to upgrade online. Subject line should be compelling and under 10 words.'
          ]
        },
        {
          tool: '🎙 Copilot in Teams',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Use your OWN existing recorded Teams meetings. Open a meeting recap in Teams > Recap tab. Copilot generates summaries, action items, and follow-up drafts grounded in the actual transcript.',
          prompts: [
            'Open an existing recorded Teams meeting recap from a network or commercial operations meeting. Ask Copilot: Identify all 5G rollout milestones discussed, the current completion status of each, and any blockers mentioned. Format as a 5G programme status report.',
            'Ask Copilot: Draft follow-up actions for the Nexus Home FMC launch team. Group by workstream: Product | Marketing | Sales | Network | IT Systems | Customer Care. Include owner and deadline for each action.',
            'Ask Copilot: Based on this meeting, what are the top 3 risks to our MCMC milestone recovery? For each risk, identify who raised it, what mitigation was proposed, and whether a decision was made.'
          ]
        },
        {
          tool: '📓 Copilot Notebook',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via copilot.microsoft.com > Notebook tab. Upload up to 5 files and set a system instruction. Best for synthesising insights across multiple documents simultaneously.',
          prompts: [
            'Upload TC_01_ClearWave_Communications.xlsx, TC_02_ClearWave_Strategy.docx to Copilot Notebook. Set instruction: "You are a telecoms strategy advisor helping the CEO navigate the MCMC penalty and FMC launch simultaneously." Ask: Given constrained management bandwidth and capital, should ClearWave prioritise 5G rollout (to avoid further MCMC penalties) or FMC bundle launch (to arrest ARPU decline)? Make a recommendation with financial reasoning.',
            'Upload TC_01_ClearWave_Communications.xlsx and TC_02_ClearWave_Strategy.docx. Ask: The strategy commits to 20% 5G coverage by year-end and 180,000 FMC subscribers in Year 1. Given the current pace of 80 site activations per month and the FMC marketing investment required, does our current capex budget support both objectives simultaneously? If not, which should we fund first and what is the opportunity cost of delaying the other?'
          ]
        },
        {
          tool: '🤝 Cowork (Frontier)',
          license: 'M365 Copilot + Frontier Program',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Cowork is an autonomous agent that takes actions across Microsoft 365 on your behalf — sending emails, scheduling meetings, creating documents, posting in Teams, and scheduling recurring tasks. Access: m365.cloud.microsoft > left nav > Agents > Cowork. Requires Frontier program enrollment.',
          prompts: [
            'Do all of the following: (1) Research MCMC\'s penalty mitigation framework and any precedents where Malaysian telcos successfully negotiated penalty reductions by presenting credible remediation plans. (2) Draft a penalty mitigation submission to MCMC — 3 pages — presenting our 5G acceleration plan and requesting a 50% penalty reduction. (3) Save to OneDrive as "MCMC Penalty Mitigation Submission". (4) Email to our General Counsel and CEO for sign-off before the MCMC deadline. (5) Schedule a preparation meeting for the bilateral MCMC session.',
            'Do all of the following for the Nexus Home FMC launch: (1) Research competitor FMC bundle pricing in Malaysia — Maxis, Celcom, U Mobile — and compile a pricing comparison. (2) Draft a competitive pricing analysis brief for the CCO. (3) Create a launch countdown tracker in SharePoint with 30-day pre-launch milestones and owners. (4) Email the tracker and pricing brief to the CCO and Head of Products. (5) Schedule a daily FMC Launch War Room call for the 2 weeks before launch.'
          ]
        },
        {
          tool: '🤖 Word Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to a Word document. Open the .docx in Word for Web > Copilot pane > + New Agent > name it, write a description, set the document as knowledge source > Share. Colleagues chat with it in Teams or M365 Copilot.',
          prompts: [
            'Open TC_02_ClearWave_Strategy.docx in Word for Web. Create an agent called "ClearWave Strategy & Regulatory Bot". Description: "Answers questions from the commercial and regulatory teams about ClearWave\'s 5G commitments, MCMC obligations, FMC bundle strategy, and competitive positioning." Share with the strategy, regulatory, and commercial leadership.',
            'Demo: A regulatory affairs manager asks "What is our specific MCMC coverage commitment for Sabah and Sarawak by Q3, and what are the penalty rates if we miss it by 2 percentage points?" Show how the agent provides a precise, strategy-grounded regulatory answer.'
          ]
        },
        {
          tool: '🤖 PowerPoint Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to a PowerPoint presentation. Great for strategy decks or Board presentations many people need to reference. Same setup as Word Agent but using a .pptx file.',
          prompts: [
            'Create a PowerPoint from the Board presentation. Create an agent called "5G & FMC Strategy Board Bot". Share with Board members and institutional investors.',
            'Demo: A Board member asks "If we achieve 20% 5G coverage by December but our FMC bundle only reaches 120,000 subscribers in Year 1, what is the net ARPU impact and do we still meet our FY2026 revenue guidance?" Show how the agent handles complex financial scenario questions.'
          ]
        },
        {
          tool: '🤖 Excel Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to an Excel workbook. Colleagues ask data questions in plain English without opening Excel. Open .xlsx in Excel for Web > Copilot pane > + New Agent > set workbook as knowledge source > share.',
          prompts: [
            'Open TC_01_ClearWave_Communications.xlsx in Excel for Web. Create an agent called "ClearWave Network & Commercial Q&A". Description: "Instant answers on 5G coverage by state, ARPU trends, FMC bundle performance, churn rates, and MCMC compliance status for the CTO, CFO, and CCO." Share with senior leadership.',
            'Demo: Ask "What is the current 5G coverage percentage in Selangor and what is the gap to the MCMC state-level target?" Then: "What is the current postpaid ARPU trend and what is the projected ARPU at Year 1 with full FMC bundle adoption?" Show how leadership gets rapid operational intelligence.'
          ]
        },
        {
          tool: '🏗 Agent Builder (Copilot Studio)',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Build a custom declarative agent in Copilot Studio — no coding required. Access: copilotstudio.microsoft.com > Create > New Agent. Add name, description, knowledge sources (SharePoint URLs or uploaded files), topics/actions. Publish to Teams in under 10 minutes.',
          prompts: [
            'Go to copilotstudio.microsoft.com > Create > New Agent. Name it "ClearWave Commercial Intelligence Agent". Description: "Supports ClearWave\'s commercial, regulatory, and network teams with answers on 5G rollout commitments, MCMC obligations, FMC bundle details, ARPU trends, and competitive intelligence — ensuring consistent, strategy-grounded responses across the organisation." Upload TC_01_ClearWave_Communications.xlsx and TC_02_ClearWave_Strategy.docx. Add topics: "5G & MCMC", "FMC Bundle", "ARPU & Revenue", "Competitive Intelligence". Publish to Teams.',
            'Demo the agent: A retail channel manager asks: "A Maxis customer is in our store comparing the Nexus Home FMC bundle against Maxis ONE. What is our price advantage, what is included in our bundle that Maxis does not offer, and if they mention they get a free upgrade phone with Maxis, what is our counter-offer?" Show how the agent equips frontline staff with the right competitive response in real time.'
          ]
        }
      ]
    },
    {
      id: 'diversified-conglomerate',
      sectorId: 'conglomerate',
      subsector: '',
      name: 'Diversified Conglomerate',
      icon: '🏛',
      color: '#37474F',
      accent: '#455A64',
      company: 'Zava Group Holdings Berhad',
      tagline: 'Coal trading breach USD 22.4M — Board emergency meeting + dual HQ MY+ID restructure.',
      scenario: 'Zava Group Holdings Berhad is a dual-HQ (Kuala Lumpur / Jakarta) ASEAN conglomerate with 11 divisions and MYR 44.8B revenue. A coal trading desk has breached its USD 20M single-counterparty exposure limit by USD 2.4M. An emergency Board meeting has been called. Three divisions are underperforming vs FY2026 targets. Group CFO Hadar Caspit must present to the Board on Monday.',
      files: [
        '01_Zava_Group_Financial_Performance.xlsx',
        '03_Zava_Group_Strategy_Framework.docx',
        'Email_07_Emergency_Board_Meeting.docx',
        'Email_08_Coal_Trading_Breach.docx'
      ],
      prompts: [
        {
          tool: '🤖 Copilot Chat (Basic)',
          license: 'Free — no M365 Copilot license needed',
          account: 'Sasha Ouellet — SashaO@ABSx62256373.OnMicrosoft.com',
          desc: '',
          prompts: [
            'I am the Group CFO of a diversified ASEAN conglomerate. Our coal trading desk has breached its USD 20M single-counterparty exposure limit by USD 2.4M and I have an emergency Board meeting on Monday. Draft a 300-word Board briefing note covering: (1) the nature and scale of the breach, (2) how it occurred — control failure, (3) the immediate remediation steps taken, (4) the financial exposure if the counterparty defaults, (5) the proposed governance enhancement to prevent recurrence. Tone: accountable, factual, and forward-looking. Do not minimise the breach.',
            'Explain what a single-counterparty exposure limit is, why it exists in commodity trading operations, and what the typical regulatory and internal governance consequences are when such a limit is breached. Include what a Board Risk Committee would normally expect in terms of escalation and reporting within the first 48 hours.',
            'What are the 5 most important things a conglomerate Group CEO should do in the first week after discovering a significant internal control breach? Focus on governance, stakeholder communication, and operational actions. Be practical and specific.'
          ]
        },
        {
          tool: '🔍 Researcher',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via Microsoft 365 Copilot Chat (copilot.microsoft.com or Teams) > click Agents > Researcher. Grounds answers in live web sources and your organisation data with full citations.',
          prompts: [
            'Research governance best practices for commodity trading risk management in diversified Asian conglomerates. I need: (1) Typical exposure limit frameworks used by conglomerates with commodity trading arms, (2) How boards of comparable conglomerates (Sime Darby, IOI, IJM) structure their risk oversight, (3) Any regulatory guidance from Bursa Malaysia or the Securities Commission on trading risk governance for listed conglomerates. Provide citations.',
            'Research the current Asian coal market — specifically Indonesian thermal coal pricing, demand trends from China and India, and any regulatory restrictions affecting Malaysian-listed companies\' coal trading activities. I need to brief the Board on whether our coal trading exposure represents a strategic risk beyond the immediate limit breach. Cite sources.'
          ]
        },
        {
          tool: '📊 Analyst',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via Microsoft 365 Copilot Chat > click Agents > Analyst. Upload an Excel or CSV file. Analyst runs Python-style analysis, builds charts, and interprets results without you writing a single formula.',
          prompts: [
            'Upload 01_Zava_Group_Financial_Performance.xlsx to Analyst. Ask: Analyse the performance of all 11 divisions against their FY2026 targets. Identify the 3 underperforming divisions — calculate the revenue variance vs target and the EBITDA margin variance. For each underperformer, show the trend over the past 4 quarters and calculate the full-year impact if the current trend continues. Present as a ranked table and a waterfall chart.',
            'Upload 01_Zava_Group_Financial_Performance.xlsx. Ask: Perform a conglomerate portfolio health assessment. For each division, calculate: (1) Revenue growth rate year-on-year, (2) EBITDA margin trend, (3) Working capital days (if data available), (4) Return on capital employed (ROCE). Rank all 11 divisions from highest to lowest portfolio value contribution. Create a 2x2 matrix: Revenue Growth vs EBITDA Margin — place each division in the appropriate quadrant (Star, Cash Cow, Question Mark, Dog).'
          ]
        },
        {
          tool: '📊 Copilot in Excel',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open 01_Zava_Group_Financial_Performance.xlsx. Navigate to the Trading Risk sheet. Ask Copilot: Build an exposure limit monitoring dashboard on a new sheet. For each trading counterparty, show: (1) Current exposure in USD M, (2) Approved limit in USD M, (3) Utilisation % (exposure/limit), (4) Breach status (OK / Warning >80% / BREACH >100%). Highlight breaches in red, warnings in amber. Add a total group exposure row at the bottom.',
            'Ask Copilot: Create a division performance dashboard on a new sheet. For each of the 11 divisions, show the current FY2026 revenue vs target, EBITDA vs target, and a traffic light status (Green: within 5% of target, Amber: 5–15% below, Red: >15% below). Add a group total row. Sort by largest revenue variance, unfavourable first.',
            'Ask Copilot: In the Group Cashflow sheet, calculate the group-level free cash flow for FY2025 and project FY2026 assuming the 3 underperforming divisions recover to 90% of target. Calculate the impact on group gearing (net debt/EBITDA) under two scenarios: divisions recover vs divisions continue declining. Show side-by-side.'
          ]
        },
        {
          tool: '📝 Copilot in Word',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open Email_08_Coal_Trading_Breach.docx. Ask Copilot: Draft a 2-page Board paper on the coal trading exposure breach. Structure: (1) Executive Summary — breach description, scale, and immediate status, (2) Background — how the breach occurred, (3) Immediate Actions Taken — exposure reduction steps, counterparty engagement, internal escalation, (4) Financial Exposure — worst-case scenario if counterparty defaults, (5) Governance Enhancement Plan — revised limit structure, daily reporting, real-time monitoring system, (6) Decisions Required from Board. Use formal board paper format.',
            'Open Email_07_Emergency_Board_Meeting.docx. Ask Copilot: Draft the emergency Board meeting agenda. The meeting is Monday at 9am. Agenda items: (1) Apologies and quorum, (2) Coal Trading Breach — CFO presentation and Board deliberation, (3) FY2026 Performance Review — 3 underperforming divisions, (4) Group Strategy — any adjustments required, (5) Actions and decisions. Allocate time to each item — total meeting is 3 hours. Include a note on what pre-reading documents should be circulated 24 hours before the meeting.',
            'Open 03_Zava_Group_Strategy_Framework.docx. Ask Copilot: Identify the sections in this strategy document related to risk management and trading. Does the current strategy adequately address commodity trading risk? Highlight any gaps and suggest additions to the risk governance framework that would prevent a recurrence of this type of breach. Create a gap analysis table: Current Policy | Gap | Proposed Enhancement.'
          ]
        },
        {
          tool: '🎯 Copilot in PowerPoint',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Ask Copilot in PowerPoint: Create a 14-slide emergency Board presentation for the Group CFO. Include: (1) Opening — purpose of the emergency meeting, (2) Coal trading breach — facts, scale, and timeline, (3) Root cause — control failure analysis, (4) Immediate actions taken, (5) Financial exposure scenario analysis, (6) Counterparty risk assessment, (7) Governance enhancement plan, (8) FY2026 group performance — 11 divisions dashboard, (9) Top 3 underperforming divisions — root cause and recovery plan, (10) Group cashflow and gearing outlook, (11) Strategic implications — should we divest coal trading?, (12) Regulatory and disclosure obligations, (13) Key risks, (14) Board decisions required. Use a serious dark grey and white colour scheme.',
            'Ask Copilot: For slides 2 through 5 (the breach narrative), generate detailed speaker notes. The CFO presenting is under significant Board pressure. Notes should be factual, accountable, and help the CFO maintain composure when challenged by Board members who may have already heard about the breach from media.',
            'Ask Copilot: Create a risk heat map slide showing the top 10 group-level risks, each positioned on a 5x5 likelihood-impact matrix. Flag the coal trading breach as a new risk. Compare this to the risk register from the previous quarter to show which risks have increased.'
          ]
        },
        {
          tool: '📧 Copilot in Outlook',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open Email_07_Emergency_Board_Meeting.docx. Ask Copilot in Outlook: Draft the emergency Board meeting notice to all 9 Board members. The notice should: confirm Monday 9am (specify location and Teams link), attach the meeting agenda, note that pre-reading documents will be circulated by Sunday 6pm, stress the confidentiality of the breach information, and ask for immediate confirmation of attendance. Subject line: "URGENT: Emergency Board Meeting — Monday 9am".',
            'Open Email_08_Coal_Trading_Breach.docx. Ask Copilot: Draft an internal escalation email from the Group CFO to the Group CEO and Chairman informing them of the breach before the Board meeting. The email should: state the facts of the breach clearly, confirm the immediate containment actions taken, note the regulatory disclosure considerations, and recommend that no external communications be made until after the Board meeting on Monday. Mark as CONFIDENTIAL.',
            'Ask Copilot: Draft the Bursa Malaysia stock exchange announcement regarding the coal trading breach, to be released after the Board meeting. The announcement should: disclose the nature and financial magnitude of the breach, confirm that internal investigations are underway, state that no material impact on group financials is expected, and note the governance enhancements being implemented. Follow the Bursa Main Market disclosure guidelines.'
          ]
        },
        {
          tool: '🎙 Copilot in Teams',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Use your OWN existing recorded Teams meetings. Open a meeting recap in Teams > Recap tab. Copilot generates summaries, action items, and follow-up drafts grounded in the actual transcript.',
          prompts: [
            'Open an existing recorded Teams meeting recap from a group management committee or risk committee meeting. Ask Copilot: Identify all risk-related discussions — any early warning signals about the coal trading exposure, any risk limit updates discussed, and any governance concerns raised. Format as a risk committee minute and flag any discussion point that may be relevant to the current breach investigation.',
            'Ask Copilot: Draft a post-breach communication for all Division MDs via Teams. The message should: acknowledge that they may have heard about the Board emergency meeting, reassure them that this is isolated to the trading desk, provide clear guidance on what they should and should not say to their teams and external stakeholders, and ask them to continue normal operations.',
            'Ask Copilot: Based on this meeting transcript, were there any previous discussions about commodity trading risk that should have prompted earlier escalation of the exposure limit? Extract any relevant statements with timestamps that the risk investigation team should review.'
          ]
        },
        {
          tool: '📓 Copilot Notebook',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via copilot.microsoft.com > Notebook tab. Upload up to 5 files and set a system instruction. Best for synthesising insights across multiple documents simultaneously.',
          prompts: [
            'Upload 01_Zava_Group_Financial_Performance.xlsx, 03_Zava_Group_Strategy_Framework.docx, Email_07_Emergency_Board_Meeting.docx, and Email_08_Coal_Trading_Breach.docx to Copilot Notebook. Set instruction: "You are the Group General Counsel advising the CFO on managing the Board emergency meeting." Ask: Based on all four documents, what are the top 3 legal and regulatory obligations the Board must be advised of at Monday\'s meeting? What decisions must the Board make and what cannot be delegated?',
            'Upload 01_Zava_Group_Financial_Performance.xlsx and 03_Zava_Group_Strategy_Framework.docx. Ask: The group strategy prioritises growing the commodity trading division as a high-margin business. The breach has called this into question. Based on the financial data, is the commodity trading division actually delivering the returns that justify the governance risk? Should the Board consider divesting or scaling back the trading operation? Present a data-based recommendation.'
          ]
        },
        {
          tool: '🤝 Cowork (Frontier)',
          license: 'M365 Copilot + Frontier Program',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Cowork is an autonomous agent that takes actions across Microsoft 365 on your behalf — sending emails, scheduling meetings, creating documents, posting in Teams, and scheduling recurring tasks. Access: m365.cloud.microsoft > left nav > Agents > Cowork. Requires Frontier program enrollment.',
          prompts: [
            'Do all of the following immediately: (1) Research Bursa Malaysia\'s disclosure requirements for material events at listed conglomerates — specifically trading losses and exposure limit breaches. (2) Draft a Bursa announcement for review by the Board — 2 paragraphs, factual and measured. (3) Save to OneDrive as "Bursa Disclosure Draft - CONFIDENTIAL". (4) Email to the General Counsel and CFO marked CONFIDENTIAL asking for review before Monday\'s Board meeting. (5) Schedule a 1-hour pre-Board legal and compliance briefing for Sunday 3pm with the General Counsel, CFO, and Company Secretary.',
            'Do all of the following for the Board meeting: (1) Confirm all 9 Board members\' attendance for Monday 9am and send calendar invites with the Teams link and a reminder. (2) Create a Board pre-reading pack in OneDrive with the 3 documents the CFO has drafted. (3) Set an access permission so only Board members and the Company Secretary can open the folder. (4) Send each Board member a link to the pre-reading pack via email with the instruction to review before Sunday 8pm. (5) Schedule a 15-minute pre-brief call for the Chairman and CEO for Sunday 8pm.'
          ]
        },
        {
          tool: '🤖 Word Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to a Word document. Open the .docx in Word for Web > Copilot pane > + New Agent > name it, write a description, set the document as knowledge source > Share. Colleagues chat with it in Teams or M365 Copilot.',
          prompts: [
            'Open 03_Zava_Group_Strategy_Framework.docx in Word for Web. Create an agent called "Group Strategy & Governance Bot". Description: "Answers questions from Group executives and Division MDs about Zava Group\'s strategic priorities, risk governance framework, performance targets, and corporate governance policies." Share with all Division MDs and the Group management team.',
            'Demo: A Division MD asks "Our EBITDA is tracking 18% below target. The Group strategy says underperforming divisions should submit a turnaround plan by end of Q2. What is the required format of the turnaround plan and who do I submit it to?" Show how the agent provides a governance-grounded, consistent answer to a high-stakes operational question.'
          ]
        },
        {
          tool: '🤖 PowerPoint Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to a PowerPoint presentation. Great for strategy decks or Board presentations many people need to reference. Same setup as Word Agent but using a .pptx file.',
          prompts: [
            'Create a PowerPoint from the Board presentation. Create an agent called "Group Board Pack Bot". Share ONLY with Board members and the Company Secretary.',
            'Demo: A Board member reviewing the pack at 11pm Sunday asks the agent "In the coal trading breach scenario analysis, what is the worst-case financial impact on group EBITDA and does it trigger any debt covenant breaches on our existing revolving credit facility?" Show how the agent gives a precise, scenario-specific answer that prepares the Board member for Monday\'s discussion.'
          ]
        },
        {
          tool: '🤖 Excel Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to an Excel workbook. Colleagues ask data questions in plain English without opening Excel. Open .xlsx in Excel for Web > Copilot pane > + New Agent > set workbook as knowledge source > share.',
          prompts: [
            'Open 01_Zava_Group_Financial_Performance.xlsx in Excel for Web. Create an agent called "Group Financial Performance Q&A". Description: "Answers questions from the Group CFO, CEO, and Board on divisional performance, trading exposure, cashflow, and gearing — providing instant data-grounded intelligence for executive decision-making." Share with the Group C-suite and Board.',
            'Demo: Ask "Which 3 divisions are most below their FY2026 EBITDA target and by how much in absolute MYR terms?" Then: "If the coal trading counterparty defaults on their full exposure, what would be the impact on our group net debt/EBITDA ratio and do we breach the 3.5x covenant?" Show how the CFO gets instant scenario intelligence.'
          ]
        },
        {
          tool: '🏗 Agent Builder (Copilot Studio)',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Build a custom declarative agent in Copilot Studio — no coding required. Access: copilotstudio.microsoft.com > Create > New Agent. Add name, description, knowledge sources (SharePoint URLs or uploaded files), topics/actions. Publish to Teams in under 10 minutes.',
          prompts: [
            'Go to copilotstudio.microsoft.com > Create > New Agent. Name it "Zava Group Executive Intelligence Bot". Description: "Supports Zava Group\'s Board, C-suite, and Division MDs with instant answers on group financial performance, divisional KPIs, risk governance requirements, trading exposure limits, and strategic priorities — grounded in official group financial and strategy documents." Upload 01_Zava_Group_Financial_Performance.xlsx, 03_Zava_Group_Strategy_Framework.docx. Add topics: "Group Performance", "Risk Governance", "Trading Limits", "Strategic Priorities". Publish to Teams for Group executives only (restricted access).',
            'Demo the agent: The Group CEO asks at 7am Monday before the Board meeting: "Give me a 60-second summary of the coal trading situation, the 3 worst-performing divisions, and the key decision the Board needs to make today. Also — are there any regulatory disclosure obligations that must be acted on immediately after the meeting?" Show how the CEO gets an instant, comprehensive executive intelligence briefing before walking into the boardroom.'
          ]
        }
      ]
    },
    {
      id: 'fintech-payments',
      sectorId: 'fintech',
      subsector: '',
      name: 'Fintech & Payments',
      icon: '💳',
      color: '#6A1B9A',
      accent: '#7B1FA2',
      company: 'Tranglo Payments Group',
      tagline: '120+ corridor remittance — BNM e-money licence renewal + fraud detection ML upgrade.',
      scenario: 'Tranglo Payments Group operates cross-border remittance across 120+ corridors serving 8 million active digital wallets. The BNM e-money licence is up for renewal in 3 months. A fraud detection ML model upgrade is underway — current model flags 94% of fraud with a 12% false positive rate. ASEAN Payment Network (APN) integration is in progress.',
      files: [
        '13_Zava_Financial_Services.xlsx',
        'BNK_01_Meridian_Bank.xlsx'
      ],
      prompts: [
        {
          tool: '🤖 Copilot Chat (Basic)',
          license: 'Free — no M365 Copilot license needed',
          account: 'Sasha Ouellet — SashaO@ABSx62256373.OnMicrosoft.com',
          desc: '',
          prompts: [
            'I am the Chief Risk Officer of a Malaysian fintech specialising in cross-border remittance. Our fraud detection model has a 94% detection rate but a 12% false positive rate — meaning 1 in 8 legitimate transactions is incorrectly flagged as fraud, causing customer friction. Draft a 250-word brief for my Board explaining the trade-off between detection rate and false positive rate, why both matter for our business, and the approach we will take to improve both simultaneously in our ML model upgrade.',
            'What are BNM\'s key requirements for e-money licence renewal in Malaysia? What financial, operational, and technical conditions must the licensee meet, and what documentation is typically required 90 days before renewal? Focus on requirements relevant to a cross-border remittance operator with 8 million active wallets.',
            'Explain how the ASEAN Payment Network (APN) initiative works and what it means for cross-border remittance operators in the region. What are the key technical and regulatory requirements for integration? Which corridors will benefit most from APN connectivity in Malaysia, Indonesia, Thailand, and Singapore?'
          ]
        },
        {
          tool: '🔍 Researcher',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via Microsoft 365 Copilot Chat (copilot.microsoft.com or Teams) > click Agents > Researcher. Grounds answers in live web sources and your organisation data with full citations.',
          prompts: [
            'Research the competitive landscape for digital cross-border remittance in Southeast Asia. I need: (1) Market size and growth rate for intra-ASEAN and ASEAN-GCC remittance in 2024–2025, (2) The top 5 competitors (Wise, Western Union, GrabPay, Sea Money, local players) and their key differentiators, (3) The impact of APN on incumbent remittance operators. Provide citations.',
            'Research best practices for fraud detection in digital payments — specifically for cross-border remittance. What ML model architectures are most effective for remittance fraud? How do leading fintechs balance detection rate and false positive rate? Are there regulatory expectations from BNM on fraud detection performance? Cite industry sources.'
          ]
        },
        {
          tool: '📊 Analyst',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via Microsoft 365 Copilot Chat > click Agents > Analyst. Upload an Excel or CSV file. Analyst runs Python-style analysis, builds charts, and interprets results without you writing a single formula.',
          prompts: [
            'Upload 13_Zava_Financial_Services.xlsx to Analyst. Ask: Analyse transaction data by remittance corridor. Which 10 corridors have the highest transaction volume? Which have the highest fraud rate? Is there a correlation between high-volume corridors and high fraud rates? Create a bubble chart: X-axis = transaction volume, Y-axis = fraud rate, bubble size = average transaction value. Identify corridors that are high-volume AND high-fraud (top-right quadrant).',
            'Upload 13_Zava_Financial_Services.xlsx. Ask: Analyse the false positive rate by customer segment (first-time senders, regular senders, high-value senders). Which segment has the highest false positive rate? Calculate the customer dropout rate for transactions incorrectly flagged — if 8% of customers abandon a transaction after a false positive flag, calculate the annual revenue loss from false positives at current transaction volumes and average fee of MYR 18 per transaction.'
          ]
        },
        {
          tool: '📊 Copilot in Excel',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open 13_Zava_Financial_Services.xlsx. Navigate to the Compliance sheet. Ask Copilot: Build a BNM e-money licence renewal readiness checklist on a new sheet. List the 15 key BNM renewal criteria. For each, show: Current Status (Met/Partial/Not Met) | Evidence on File (Yes/No) | Responsible Team | Action Required | Deadline. Apply conditional formatting: green = Met, amber = Partial, red = Not Met.',
            'Ask Copilot: Create a fraud model performance dashboard on a new sheet. Show monthly data for the past 12 months: (1) Detection rate (%), (2) False positive rate (%), (3) Fraud losses prevented (MYR M), (4) Customer complaints due to false positives (count). Add trend lines and flag months where false positive rate exceeded 15%. Calculate the estimated revenue saved by fraud prevention vs the estimated revenue lost due to false positives — show the net benefit.',
            'Ask Copilot: In the Corridor Performance sheet, build a corridor priority matrix. For each of the top 20 corridors, calculate: (1) Annual fee revenue (MYR M), (2) Transaction volume growth rate, (3) Current fraud rate, (4) APN integration status. Rank corridors by a composite score (revenue × growth ÷ fraud rate) to identify which corridors should receive the most investment in fraud detection improvement.'
          ]
        },
        {
          tool: '📝 Copilot in Word',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open BNK_01_Meridian_Bank.xlsx (use as a financial services reference). Ask Copilot: Draft the BNM e-money licence renewal application cover letter. The letter should: reference our existing licence number and expiry date, confirm our continued compliance with the BNM e-money framework, highlight our key operational metrics (8M active wallets, 120+ corridors, 99.97% system uptime), note the ML fraud model upgrade underway, and request a pre-renewal meeting with BNM Supervision. Use formal BNM correspondence format.',
            'Ask Copilot in Word: Draft a fraud risk management policy document of 3 pages. Cover: (1) Fraud risk appetite statement — acceptable detection rate and false positive rate targets, (2) ML model governance — how the model is trained, validated, and monitored, (3) Manual review process for flagged transactions, (4) Customer dispute resolution process for false positives, (5) Regulatory reporting of fraud incidents to BNM. Format as a formal policy document with version control header.',
            'Ask Copilot: Draft an APN integration business case for the CFO. Cover: (1) What APN connectivity means for our corridor economics — expected fee compression and volume increase, (2) Technical integration requirements and estimated cost (MYR 8.5M), (3) Revenue impact — net of fee compression, volume uplift, and new corridors unlocked, (4) Risk: if we do not integrate, we lose access to APN-connected corridors to competitors who do. Recommend: proceed vs defer.'
          ]
        },
        {
          tool: '🎯 Copilot in PowerPoint',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Ask Copilot in PowerPoint: Create a 10-slide investor presentation for Tranglo Payments Group. Include: (1) Business overview — 120+ corridors, 8M wallets, (2) Market opportunity — intra-ASEAN remittance growth, (3) Competitive positioning, (4) Fraud detection — current model and ML upgrade roadmap, (5) BNM licence renewal — compliance status, (6) APN integration — timeline and revenue impact, (7) Financial performance — revenue growth and margin, (8) Technology roadmap, (9) ESG — financial inclusion and migrant worker impact, (10) Investment thesis. Purple and white colour scheme.',
            'Ask Copilot: Create a 2-slide fraud model explainer for a non-technical Board audience. Slide 1: How our ML fraud model works — simple visual with 3 steps (transaction comes in → model scores risk → action taken). Slide 2: Current performance vs target — detection rate and false positive rate shown as gauges, with the improvement target for the upgraded model.',
            'Ask Copilot: Add a corridor map slide showing our 10 highest-revenue corridors as a world map with connecting lines. Label each corridor with the annual transaction volume and the fraud rate. Use different colours to indicate APN-integrated vs non-APN corridors.'
          ]
        },
        {
          tool: '📧 Copilot in Outlook',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Ask Copilot in Outlook: Draft a letter to BNM\'s Payment Systems Policy Department requesting a pre-renewal consultation meeting for our e-money licence renewal. The letter should: introduce the purpose of the meeting, summarise our compliance status, highlight the ML fraud model upgrade as a key enhancement since the last renewal, and request a 45-minute meeting within the next 4 weeks.',
            'Ask Copilot: Draft a customer apology and resolution email for the top 50 customers who were most affected by false positive fraud flags in the past quarter. The email should: acknowledge the inconvenience, explain briefly that our fraud detection system has flagged their transaction incorrectly, confirm the transaction has been approved, and offer a waived fee on their next transaction as a goodwill gesture.',
            'Ask Copilot: Draft an email to our APN integration technology partner requesting a project status update. The integration is now 6 weeks behind the original schedule. The email should ask for: the root cause of the delay, a revised project timeline, and confirmation of the resources assigned to the integration sprint.'
          ]
        },
        {
          tool: '🎙 Copilot in Teams',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Use your OWN existing recorded Teams meetings. Open a meeting recap in Teams > Recap tab. Copilot generates summaries, action items, and follow-up drafts grounded in the actual transcript.',
          prompts: [
            'Open an existing recorded Teams meeting recap from a product or compliance meeting. Ask Copilot: Identify all BNM compliance actions discussed — their status, deadline, and responsible team. Flag any action that is overdue or at risk of missing its deadline before the licence renewal in 3 months.',
            'Ask Copilot: Draft follow-up actions from this meeting for the fraud model upgrade team. Group by workstream: Data Science | Engineering | Compliance | Customer Experience. Include owner and deadline.',
            'Ask Copilot: Based on this meeting, what is the team\'s confidence level that the ML model upgrade will be completed before the BNM renewal inspection? Identify the top 2 technical or resource risks that could delay the upgrade.'
          ]
        },
        {
          tool: '📓 Copilot Notebook',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via copilot.microsoft.com > Notebook tab. Upload up to 5 files and set a system instruction. Best for synthesising insights across multiple documents simultaneously.',
          prompts: [
            'Upload 13_Zava_Financial_Services.xlsx and BNK_01_Meridian_Bank.xlsx to Copilot Notebook. Set instruction: "You are a fintech regulatory advisor preparing Tranglo for BNM e-money licence renewal." Ask: Based on the transaction data and the financial services framework, what are the 3 areas where our current performance is most likely to draw BNM scrutiny during the renewal assessment? For each area, what specific evidence should we prepare?',
            'Upload 13_Zava_Financial_Services.xlsx. Ask: Our current false positive rate of 12% is significantly above the industry best practice of 5–7%. If we reduce it to 7% through the ML upgrade, what is the projected impact on: (1) customer retention rate, (2) annual transaction volume, (3) annual fee revenue? Quantify the business case for the ML upgrade investment.'
          ]
        },
        {
          tool: '🤝 Cowork (Frontier)',
          license: 'M365 Copilot + Frontier Program',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Cowork is an autonomous agent that takes actions across Microsoft 365 on your behalf — sending emails, scheduling meetings, creating documents, posting in Teams, and scheduling recurring tasks. Access: m365.cloud.microsoft > left nav > Agents > Cowork. Requires Frontier program enrollment.',
          prompts: [
            'Do all of the following: (1) Research BNM\'s e-money licence renewal requirements and any updates published in 2024 or 2025. (2) Draft a 90-day countdown renewal action plan with weekly milestones covering all documentation, compliance, and technical requirements. (3) Save to OneDrive as "BNM e-Money Licence Renewal Plan". (4) Email to the Chief Compliance Officer and CTO asking for review and sign-off within 2 days. (5) Schedule a weekly 30-minute "BNM Renewal Check-In" every Monday at 9am for 12 weeks.',
            'Do all of the following for APN integration: (1) Research the technical specification for APN integration published by BNM or the ASEAN payment network. (2) Draft an accelerated integration timeline to make up the 6-week delay. (3) Email to our CTO and the technology partner project manager asking for a recovery plan call this week. (4) Create an integration milestone tracker in SharePoint with weekly check-points. (5) Post in the #product-engineering Teams channel: "APN integration is 6 weeks behind — recovery plan discussion on [date]. All corridor and API team members please attend."'
          ]
        },
        {
          tool: '🤖 Word Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to a Word document. Open the .docx in Word for Web > Copilot pane > + New Agent > name it, write a description, set the document as knowledge source > Share. Colleagues chat with it in Teams or M365 Copilot.',
          prompts: [
            'Open BNK_01_Meridian_Bank.xlsx in Excel for Web. Create a Word document summarising the key BNM compliance requirements for e-money operators and open it in Word for Web. Create an agent called "Tranglo Compliance Policy Bot". Description: "Answers questions from compliance and product teams about BNM e-money framework requirements, fraud reporting obligations, AML/CFT rules for remittance, and licence renewal criteria." Share with the compliance team.',
            'Demo: A compliance analyst asks "A customer has sent 15 transactions over MYR 5,000 to the same overseas beneficiary in one week. Does this trigger our STR (Suspicious Transaction Report) obligation to BNM and what is the 24-hour reporting deadline?" Show how the agent provides a precise, regulatory-grounded AML compliance answer.'
          ]
        },
        {
          tool: '🤖 PowerPoint Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to a PowerPoint presentation. Great for strategy decks or Board presentations many people need to reference. Same setup as Word Agent but using a .pptx file.',
          prompts: [
            'Create a PowerPoint from the investor presentation and open in PowerPoint for Web. Create an agent called "Tranglo Investor Q&A Bot". Share with institutional investors and analyst research teams.',
            'Demo: An analyst asks "What is Tranglo\'s current market share in the Malaysia-Indonesia remittance corridor and what is the projected impact of APN integration on corridor fees?" Show how the agent handles investor research questions with specific data-grounded answers.'
          ]
        },
        {
          tool: '🤖 Excel Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to an Excel workbook. Colleagues ask data questions in plain English without opening Excel. Open .xlsx in Excel for Web > Copilot pane > + New Agent > set workbook as knowledge source > share.',
          prompts: [
            'Open 13_Zava_Financial_Services.xlsx in Excel for Web. Create an agent called "Tranglo Payments Analytics Q&A". Description: "Instant answers on corridor performance, fraud rates, false positive rates, wallet metrics, and BNM compliance status for the CRO, CEO, and product leadership." Share with senior leadership.',
            'Demo: Ask "What is the fraud rate on the Malaysia-Philippines corridor and how does it compare to the group average?" Then: "How many customer transactions were incorrectly flagged as fraud last month and what was the estimated revenue impact?" Show how the CRO gets rapid fraud intelligence.'
          ]
        },
        {
          tool: '🏗 Agent Builder (Copilot Studio)',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Build a custom declarative agent in Copilot Studio — no coding required. Access: copilotstudio.microsoft.com > Create > New Agent. Add name, description, knowledge sources (SharePoint URLs or uploaded files), topics/actions. Publish to Teams in under 10 minutes.',
          prompts: [
            'Go to copilotstudio.microsoft.com > Create > New Agent. Name it "Tranglo Payments Intelligence Agent". Description: "Supports Tranglo\'s compliance, product, and commercial teams with answers on BNM e-money requirements, fraud detection policies, APN integration status, corridor performance, and customer dispute procedures — ensuring regulatory-compliant, consistent responses across the fintech operation." Upload 13_Zava_Financial_Services.xlsx. Add topics: "BNM Compliance", "Fraud Detection", "APN Integration", "Corridor Performance". Publish to Teams.',
            'Demo the agent: A customer success manager gets a call from an angry corporate customer whose payroll remittance to 120 employees in Indonesia was blocked by the fraud model. The manager asks the agent: "A USD 340,000 payroll transfer to Indonesia was flagged and blocked. What is our SLA to resolve a blocked corporate payroll transfer, what information do I need from the customer to manually approve it, and can I override the ML flag?" Show how the agent provides an instant, policy-grounded resolution path.'
          ]
        }
      ]
    },
    {
      id: 'government-agency',
      sectorId: 'government',
      subsector: '',
      name: 'Government Agency',
      icon: '🏛',
      color: '#4E342E',
      accent: '#5D4037',
      company: 'Jabatan Perkhidmatan Awam (JPA) / State Digital Office',
      tagline: 'MyGovID rollout — 2.4M constituent digital interactions, e-service transformation.',
      scenario: 'The Selangor State Digital Office is leading the digital government transformation agenda — migrating 48 government services online, integrating with MyGovID (national digital identity), and reducing counter-based transactions by 60% within 18 months. 2.4 million constituent interactions per year are being transformed through digital channels.',
      files: [
        '03_Zava_Group_Strategy_Framework.docx',
        '02_Zava_Group_Policy_Handbook.docx'
      ],
      prompts: [
        {
          tool: '🤖 Copilot Chat (Basic)',
          license: 'Free — no M365 Copilot license needed',
          account: 'Sasha Ouellet — SashaO@ABSx62256373.OnMicrosoft.com',
          desc: '',
          prompts: [
            'I am leading the digital transformation programme for a Malaysian state government. We are migrating 48 services online and integrating with MyGovID. Constituents are resistant to digital channels — only 34% adoption after 6 months. Draft a 300-word constituent adoption acceleration strategy brief. Cover: the 3 most common barriers to adoption for Malaysian government digital services, three specific interventions that have worked in comparable GovTech programmes (cite examples from Singapore, Estonia, or other advanced digital governments), and the key success metric we should target at the 12-month mark.',
            'Explain how MyGovID works as a national digital identity for Malaysia — what it enables for government service delivery, how it differs from SingPass, and what the key privacy and data security considerations are for state government agencies integrating with it.',
            'What are the 5 most important change management principles for a successful government digital transformation? Focus on the specific challenges of driving change in a public sector environment where civil servants may fear that digitalisation will reduce headcount.'
          ]
        },
        {
          tool: '🔍 Researcher',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via Microsoft 365 Copilot Chat (copilot.microsoft.com or Teams) > click Agents > Researcher. Grounds answers in live web sources and your organisation data with full citations.',
          prompts: [
            'Research successful government digital transformation case studies in Southeast Asia and comparable markets. I need: (1) The top 3 governments that have achieved the highest e-service adoption rates, (2) The specific interventions that drove adoption beyond 60%, (3) How they handled data privacy and cybersecurity concerns with constituents. Provide citations from GovTech publications or government reports.',
            'Research the Malaysia Government digital transformation roadmap — specifically MAMPU\'s guidelines, the MyDigital blueprint, and any Selangor-specific digital government initiatives. What are the performance benchmarks the federal government expects from state agencies? Are there any grant funding programmes for digital government projects? Cite official sources.'
          ]
        },
        {
          tool: '📊 Analyst',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via Microsoft 365 Copilot Chat > click Agents > Analyst. Upload an Excel or CSV file. Analyst runs Python-style analysis, builds charts, and interprets results without you writing a single formula.',
          prompts: [
            'Upload 03_Zava_Group_Strategy_Framework.docx (use as strategy proxy). Ask Analyst: Assume we have a dataset of 2.4 million constituent interactions — 34% digital, 66% counter-based. Analyse the digital adoption rate by service type (business licence, property assessment, civil complaints, permit applications). Which service types have the highest digital adoption? Which have the lowest? Create a bar chart ranked by adoption rate and calculate the revenue/cost saving for each 1% shift from counter to digital (assume MYR 12 cost per counter transaction vs MYR 2 per digital transaction).',
            'Ask Analyst: Build a digital transformation ROI model. Inputs: 2.4M annual interactions, current 34% digital adoption (816,000 digital, 1,584,000 counter), target 80% digital by Month 18. Calculate: (1) Annual cost saving at 80% adoption vs current, (2) Investment required — portal development MYR 4.2M, MyGovID integration MYR 1.8M, digital outreach MYR 0.8M, (3) Payback period in months. Show as a cost-benefit table.'
          ]
        },
        {
          tool: '📊 Copilot in Excel',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open 03_Zava_Group_Strategy_Framework.docx. In Excel, create a new workbook called "Digital Services Migration Tracker.xlsx". Ask Copilot to help structure: Create a sheet with columns: Service Name | Department | Current Mode (Counter/Hybrid/Digital) | MyGovID Integration Required (Y/N) | Development Status | Go-Live Date | Adoption Rate (%) | Monthly Transactions. Populate with 10 sample services. Add conditional formatting: red = not started, amber = in progress, green = live.',
            'Ask Copilot: Build a constituent adoption dashboard. For each of the 10 sample services, create a chart showing: (1) Monthly transaction volume by channel (digital vs counter) for the past 6 months, (2) Digital adoption trend line, (3) Target adoption rate line at 80%. Flag any service where digital adoption is declining despite being live.',
            'Ask Copilot: Create an efficiency savings model. For each service, calculate: (1) Annual counter transactions saved if digital adoption reaches 80%, (2) Cost saving at MYR 10 per counter transaction, (3) Officer hours freed for higher-value work. Sum across all 48 services and show the total annual productivity dividend in MYR and officer hours.'
          ]
        },
        {
          tool: '📝 Copilot in Word',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open 02_Zava_Group_Policy_Handbook.docx. Ask Copilot: Draft a digital government transformation policy for the Selangor State Government. Cover: (1) Vision and mandate — 80% digital adoption within 18 months, (2) Scope — 48 services, (3) MyGovID integration requirements, (4) Data privacy and cybersecurity standards for digital services, (5) Civil servant role in supporting constituent adoption, (6) Performance measurement framework. Keep it to 5 pages, use formal government policy language.',
            'Ask Copilot: Draft a constituent communication guide for the digital migration of 5 high-volume services. For each service, the guide should: explain the new online process in plain language (Bahasa Malaysia and English), list the documents to prepare before logging in, provide the MyGovID registration link, and note the helpline for constituents who need assistance. Format as a simple infographic script.',
            'Ask Copilot: Write a Board paper for the State Exco Committee recommending the approval of MYR 6.8M for the digital services migration programme. Cover: strategic rationale, scope, investment breakdown, ROI and payback period, risks and mitigants, and the decision required. Format as a formal Exco submission paper.'
          ]
        },
        {
          tool: '🎯 Copilot in PowerPoint',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Ask Copilot in PowerPoint: Create a 10-slide presentation for the State Exco Committee on the digital transformation programme. Include: (1) Vision — transforming 2.4M annual constituent interactions, (2) Current state — 34% digital adoption, (3) Target state — 80% digital, 60% counter reduction, (4) Service migration roadmap — 48 services, phased over 18 months, (5) MyGovID integration plan, (6) Cost savings — MYR 18M annual by Year 3, (7) Technology architecture — simple diagram, (8) Change management plan — civil servant and constituent engagement, (9) Budget request — MYR 6.8M, (10) Decision required. Use dark blue and gold Malaysian government colour scheme.',
            'Ask Copilot: Create a one-slide "Before and After" digital journey map showing how a constituent currently obtains a business licence at a counter (7 steps, 45-minute wait, MYR 12 cost) vs the new digital process (4 steps, 10 minutes online, MYR 2 cost). Use a simple flowchart format.',
            'Ask Copilot: Add a constituent testimonial slide with 3 fictional but realistic quotes from different constituent segments — a millennial entrepreneur, a 55-year-old smallholder farmer, and a SME owner — showing their positive experience with the new digital service.'
          ]
        },
        {
          tool: '📧 Copilot in Outlook',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Ask Copilot in Outlook: Draft a letter from the State Digital Director to all 48 department heads whose services are being migrated. The letter should: explain the digital migration mandate, the MyGovID integration requirement, the department\'s responsibilities in the migration project, and the go-live timeline. Ask each department head to nominate a digital champion within 2 weeks. Use formal government correspondence language in Bahasa Malaysia (or bilingual format).',
            'Ask Copilot: Draft a press release announcing the launch of the Selangor Digital Government Portal. The release should: announce the availability of the first 10 digital services, explain the MyGovID login process, note the constituent support channels, and include a quote from the State Exco member for Digital Affairs. Target audience: Malay and English-language media.',
            'Ask Copilot: Draft an email to MAMPU (Malaysia Administrative Modernisation and Management Planning Unit) requesting technical support for the MyGovID API integration. The email should specify our integration requirements, the development timeline, and the number of services being integrated. Request a technical onboarding meeting within 2 weeks.'
          ]
        },
        {
          tool: '🎙 Copilot in Teams',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Use your OWN existing recorded Teams meetings. Open a meeting recap in Teams > Recap tab. Copilot generates summaries, action items, and follow-up drafts grounded in the actual transcript.',
          prompts: [
            'Open an existing recorded Teams meeting recap from a project or digital transformation steering committee. Ask Copilot: Identify all digital service migration milestones discussed, their current status, and any blockers. Format as a programme status update for the Exco Digital Transformation Committee.',
            'Ask Copilot: Draft follow-up actions for the digital transformation team. Group by workstream: Technology | Change Management | Constituent Communications | MyGovID Integration | Training. Include department owner and deadline.',
            'Ask Copilot: Were any constituent complaints or feedback about the digital services discussed? List each with the service type, the nature of the feedback, and whether a resolution was proposed.'
          ]
        },
        {
          tool: '📓 Copilot Notebook',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via copilot.microsoft.com > Notebook tab. Upload up to 5 files and set a system instruction. Best for synthesising insights across multiple documents simultaneously.',
          prompts: [
            'Upload 03_Zava_Group_Strategy_Framework.docx and 02_Zava_Group_Policy_Handbook.docx to Copilot Notebook. Set instruction: "You are a GovTech transformation advisor helping the State Digital Director drive constituent adoption." Ask: Based on the strategic framework and policy requirements, what is the single biggest barrier to digital adoption in a Malaysian state government context and what is the most effective intervention backed by international evidence?',
            'Upload 02_Zava_Group_Policy_Handbook.docx and 03_Zava_Group_Strategy_Framework.docx. Ask: A civil servant has raised concerns that the digital migration will lead to job losses in the counter service teams. Is this concern valid based on comparable government digital transformations? How should the State Digital Director address this concern in a way that is honest, compassionate, and motivating for the civil service?'
          ]
        },
        {
          tool: '🤝 Cowork (Frontier)',
          license: 'M365 Copilot + Frontier Program',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Cowork is an autonomous agent that takes actions across Microsoft 365 on your behalf — sending emails, scheduling meetings, creating documents, posting in Teams, and scheduling recurring tasks. Access: m365.cloud.microsoft > left nav > Agents > Cowork. Requires Frontier program enrollment.',
          prompts: [
            'Do all of the following: (1) Research the top 3 GovTech vendors in Malaysia who have successfully implemented MyGovID integration for state government portals — identify their references and pricing models. (2) Draft a vendor RFP for the digital portal development covering our 10 priority services. (3) Save to OneDrive as "Digital Portal RFP - Selangor SDO". (4) Email the RFP to the 3 shortlisted vendors asking for proposals within 3 weeks. (5) Schedule an RFP briefing session for all 3 vendors for next Thursday.',
            'Do all of the following for the digital adoption campaign: (1) Draft a constituent digital awareness campaign concept for social media, WhatsApp, and community halls targeting 3 segments: youth (18–35), working age (36–54), and senior (55+). (2) Create a campaign calendar showing the 12-week rollout. (3) Draft sample social media posts in Bahasa Malaysia and English for weeks 1 and 2. (4) Email the concept and calendar to the State Communications team for review. (5) Schedule a campaign kickoff meeting for next week.'
          ]
        },
        {
          tool: '🤖 Word Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to a Word document. Open the .docx in Word for Web > Copilot pane > + New Agent > name it, write a description, set the document as knowledge source > Share. Colleagues chat with it in Teams or M365 Copilot.',
          prompts: [
            'Open 02_Zava_Group_Policy_Handbook.docx in Word for Web. Create an agent called "Digital Government Policy Bot". Description: "Answers questions from civil servants and department heads about the digital transformation policy, MyGovID integration requirements, data privacy obligations, and constituent service standards." Share with all 48 department heads.',
            'Demo: A department head asks "My team handles physical land title searches. The new digital portal requires us to process results within 3 working days. Our current process takes 7 days. What process changes are we required to make and is there any budget available for system upgrades to meet the 3-day SLA?" Show how the agent provides a policy-grounded answer that empowers the department head to act.'
          ]
        },
        {
          tool: '🤖 PowerPoint Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to a PowerPoint presentation. Great for strategy decks or Board presentations many people need to reference. Same setup as Word Agent but using a .pptx file.',
          prompts: [
            'Create a PowerPoint from the Exco presentation. Create an agent called "Selangor Digital Transformation Q&A". Share with Exco members and the State Secretary.',
            'Demo: An Exco member asks "If we achieve 80% digital adoption within 18 months, what is the total headcount saving across all 48 services and how will those officers be redeployed rather than retrenched?" Show how the agent gives a data-grounded, politically-sensitive answer.'
          ]
        },
        {
          tool: '🤖 Excel Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to an Excel workbook. Colleagues ask data questions in plain English without opening Excel. Open .xlsx in Excel for Web > Copilot pane > + New Agent > set workbook as knowledge source > share.',
          prompts: [
            'Create a Digital Services Tracker workbook and open in Excel for Web. Create an agent called "Digital Services Programme Q&A". Description: "Answers questions about the Selangor digital government programme — service migration status, adoption rates, cost savings, and MyGovID integration progress — for the State Digital Director and Exco." Share with the State Digital Office.',
            'Demo: Ask "How many of the 48 services are currently live on the digital portal and what is the average adoption rate across live services?" Then: "Which 3 services have the lowest digital adoption and what might be causing it?" Show how the Digital Director gets instant programme intelligence.'
          ]
        },
        {
          tool: '🏗 Agent Builder (Copilot Studio)',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Build a custom declarative agent in Copilot Studio — no coding required. Access: copilotstudio.microsoft.com > Create > New Agent. Add name, description, knowledge sources (SharePoint URLs or uploaded files), topics/actions. Publish to Teams in under 10 minutes.',
          prompts: [
            'Go to copilotstudio.microsoft.com > Create > New Agent. Name it "Selangor Digital Government Assistant". Description: "Helps civil servants, department heads, and the State Digital Office team with answers on digital service requirements, MyGovID integration, constituent FAQ, data privacy obligations, and transformation programme milestones — supporting Malaysia\'s digital government agenda." Upload 02_Zava_Group_Policy_Handbook.docx and 03_Zava_Group_Strategy_Framework.docx. Add topics: "MyGovID Integration", "Digital Service Standards", "Constituent FAQ", "Privacy & Data". Publish to Teams for all state government staff.',
            'Demo the agent: A counter officer who has been redeployed to a digital support role asks: "A constituent is trying to renew their business licence online but keeps getting an error at the payment step after connecting their MyGovID. What are the 3 most common causes of this error and what is the step-by-step resolution I should guide them through over the phone?" Show how the agent empowers redeployed staff to provide excellent digital support.'
          ]
        }
      ]
    },
    {
      id: 'property-reit',
      sectorId: 'property',
      subsector: '',
      name: 'Property & REIT',
      icon: '🏢',
      color: '#1565C0',
      accent: '#1976D2',
      company: 'Zava Properties Berhad',
      tagline: 'MYR 8.2B REIT injection — Shell anchor lease expiry Dec 2026 + Penang MYR 2.1B GDV.',
      scenario: 'Zava Properties Berhad manages a 25-asset commercial, industrial, and hospitality portfolio valued at MYR 8.2B across Malaysia and Indonesia. The group is structuring a REIT IPO in 2026. Menara Zava KL\'s anchor tenant (Shell, 820,000 sq ft) has flagged a potential lease non-renewal in December 2026. A Penang mixed-development with MYR 2.1B GDV has received planning approval.',
      files: [
        '14_Zava_Properties_Portfolio.xlsx',
        '03_Zava_Group_Strategy_Framework.docx'
      ],
      prompts: [
        {
          tool: '🤖 Copilot Chat (Basic)',
          license: 'Free — no M365 Copilot license needed',
          account: 'Sasha Ouellet — SashaO@ABSx62256373.OnMicrosoft.com',
          desc: '',
          prompts: [
            'I am the CFO of a Malaysian property company preparing for a REIT IPO in 2026. Our largest office building (820,000 sq ft, Grade A) has its anchor tenant — a global oil major — expiring in December 2026, 6 months after our planned REIT IPO. This tenant represents 28% of the building\'s rental income. The building\'s REIT valuation will be significantly impacted if the lease is not renewed before IPO. Draft a 250-word strategic brief covering: (1) How tenant departure risk is typically priced in REIT IPO valuations, (2) The negotiation levers I have to incentivise early lease renewal, (3) Whether I should proceed with the REIT IPO before or after the lease renewal decision.',
            'What is a REIT-in-trust structure for Malaysian property assets? Explain: how assets are injected into the REIT, how the IPO price is calculated, what the SC (Securities Commission) and Bursa Malaysia requirements are, and how the parent company benefits financially from the REIT IPO.',
            'What are the current Grade A office market conditions in KL and what is the typical absorption rate for large anchor-tenant vacancies? How long would it realistically take to re-tenant an 820,000 sq ft building if the current anchor leaves?'
          ]
        },
        {
          tool: '🔍 Researcher',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via Microsoft 365 Copilot Chat (copilot.microsoft.com or Teams) > click Agents > Researcher. Grounds answers in live web sources and your organisation data with full citations.',
          prompts: [
            'Research the Malaysian REIT market in 2024–2025. I need: (1) Current REIT yield compression trends in Malaysia, (2) Recent REIT IPOs and their pricing — average premium/discount to NAV, (3) The major institutional investors in Malaysian REITs and their investment criteria, (4) How comparable Malaysian REITs (Sunway REIT, IGB REIT, Pavilion REIT) have handled large tenant vacancies. Cite sources.',
            'Research the Penang property market — specifically the mixed-use development segment. What is the current residential and commercial absorption rate in Georgetown and Batu Kawan? Who are the major developer competitors? What GDV pricing benchmarks apply for a MYR 2.1B mixed-use development? Cite Savills, JLL, or CBRE reports.'
          ]
        },
        {
          tool: '📊 Analyst',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via Microsoft 365 Copilot Chat > click Agents > Analyst. Upload an Excel or CSV file. Analyst runs Python-style analysis, builds charts, and interprets results without you writing a single formula.',
          prompts: [
            'Upload 14_Zava_Properties_Portfolio.xlsx to Analyst. Ask: Analyse the 25-asset portfolio and identify the top 12 REIT-eligible assets. For each, calculate: (1) NPI yield (Net Property Income ÷ Market Value), (2) Weighted average lease expiry (WALE) in years, (3) Occupancy rate. Rank by NPI yield and highlight assets where occupancy is below 80% or WALE is under 2 years — these represent risk factors for the REIT IPO. Create a portfolio heatmap.',
            'Upload 14_Zava_Properties_Portfolio.xlsx. Ask: Model 3 REIT IPO scenarios: (A) Include all 12 REIT-eligible assets at current occupancy, (B) Exclude Menara Zava KL if Shell leaves (worst case), (C) Include Menara Zava KL only if Shell renews. For each scenario, calculate: total portfolio NPI yield, IPO valuation at a 5.5% cap rate, parent company net proceeds after debt transfer, and year-1 distribution per unit (DPU) assuming 90% distribution.'
          ]
        },
        {
          tool: '📊 Copilot in Excel',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open 14_Zava_Properties_Portfolio.xlsx. Navigate to the Asset Register sheet. Ask Copilot: Add a REIT Readiness Assessment column. For each asset, score it against 5 criteria: (1) REIT-eligible (Y/N), (2) Occupancy >85% (Y/N), (3) WALE >3 years (Y/N), (4) NPI yield >5% (Y/N), (5) Lease documentation current (Y/N). Total the score out of 5. Highlight assets scoring 4–5 in green (ready), 3 in amber (conditional), 0–2 in red (not ready).',
            'Ask Copilot: Build a lease expiry schedule on a new sheet. For each REIT-eligible asset, list all major tenants, their current lease expiry, the next rent review date, and the lease area in sq ft. Identify any lease expiring within 18 months — flag as "REIT IPO Risk" if the tenant is >10% of the building NLA. Sort by earliest expiry.',
            'Ask Copilot: In the REIT Injection Analysis sheet, build a sensitivity table showing the REIT IPO valuation under different cap rate assumptions (4.5%, 5.0%, 5.5%, 6.0%, 6.5%) and occupancy assumptions (80%, 85%, 90%, 95%, 100%). Show the IPO market capitalisation and the net proceeds to Zava Properties under each cell of the matrix.'
          ]
        },
        {
          tool: '📝 Copilot in Word',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open 03_Zava_Group_Strategy_Framework.docx. Ask Copilot: Draft a 3-page REIT IPO strategy paper for the Zava Properties Board. Cover: (1) REIT structure and asset injection plan — 12 assets, MYR 8.2B total, (2) IPO timeline — target Q2 2026, key milestones, (3) Shell anchor lease renewal — negotiation strategy and timeline, (4) Pre-IPO asset enhancements — refurbishment and occupancy improvement plans, (5) Expected IPO proceeds and use of funds. Format as a Board strategy paper.',
            'Ask Copilot: Draft a 2-page letter to Shell Malaysia\'s Head of Real Estate requesting an early lease renewal discussion for their Menara Zava KL tenancy. The letter should: acknowledge the December 2026 expiry, express Zava Properties\' strong commitment to the relationship, propose a 5-year renewal with enhanced building management services, and request a meeting within 4 weeks. Professional commercial tone.',
            'Ask Copilot: Write a 1-page Penang development launch press release for the new MYR 2.1B mixed-use development in Georgetown. Announce the planning approval, the project highlights (residential units, retail podium, serviced apartments), the target completion in Q4 2028, and the JV partner. Include a quote from the Zava Properties MD.'
          ]
        },
        {
          tool: '🎯 Copilot in PowerPoint',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Ask Copilot in PowerPoint: Create a 12-slide REIT IPO roadshow presentation. Include: (1) Zava Properties — company overview and portfolio highlights, (2) Malaysian REIT market overview — yield trends and investor appetite, (3) Portfolio snapshot — 12 assets, MYR 8.2B, (4) Asset quality — occupancy, NPI yield, WALE, (5) Top 5 assets deep dive, (6) Shell lease situation — risk and mitigation, (7) IPO structure and asset injection plan, (8) Financial projections — Year 1 and Year 3 DPU, (9) Growth pipeline — Penang GDV 2.1B, (10) ESG positioning, (11) IPO timeline and milestones, (12) Investment thesis. Dark navy and gold colour scheme.',
            'Ask Copilot: Create a one-pager summary slide: "Why Invest in Zava REIT" — 3 key investment highlights, year-1 DPU yield vs Malaysian REIT peer average, portfolio resilience factors, and a high-quality asset photo collage layout.',
            'Ask Copilot: Add an anchor tenant risk slide (slide 6) with a visual showing the 3 scenarios (Shell renews / Shell leaves / partial renewal) and their impact on Year 1 DPU. Show this as a simple scenario table with traffic light status and the DPU range for each.'
          ]
        },
        {
          tool: '📧 Copilot in Outlook',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Ask Copilot in Outlook: Draft an email from the Group CFO to Goldman Sachs and CIMB (the proposed joint lead managers for the REIT IPO) requesting a kick-off meeting. The email should: confirm the target Q2 2026 IPO timeline, request their preliminary views on valuation and investor appetite, and note the Shell lease renewal risk as a key discussion point. Attach the REIT strategy summary.',
            'Ask Copilot: Draft a follow-up email to the SC (Securities Commission) Malaysia acknowledging receipt of the preliminary REIT registration guidance and confirming our intended filing timeline. List the 5 key documents we will submit with the prospectus application and ask for clarity on the minimum unit holder spread requirement.',
            'Ask Copilot: Draft a letter to the Penang State Government acknowledging receipt of the planning approval for the Georgetown mixed-use development. Express gratitude for the expedited approval, confirm the project commencement date, and propose a groundbreaking ceremony at the Governor\'s convenience.'
          ]
        },
        {
          tool: '🎙 Copilot in Teams',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Use your OWN existing recorded Teams meetings. Open a meeting recap in Teams > Recap tab. Copilot generates summaries, action items, and follow-up drafts grounded in the actual transcript.',
          prompts: [
            'Open an existing recorded Teams meeting recap from a property portfolio or asset management review. Ask Copilot: Identify all lease renewal discussions, occupancy concerns, and asset performance issues. Flag any tenant at risk and summarise the actions the asset management team has agreed to take.',
            'Ask Copilot: Draft follow-up actions from the REIT IPO planning meeting. Group by workstream: Legal & Compliance | Valuation | Asset Management | Marketing & Investor Relations | Finance. Include owner and deadline.',
            'Ask Copilot: Were there any discussions about the Penang development project in this meeting? If yes, summarise the planning approval status, JV partner discussions, and financing requirements.'
          ]
        },
        {
          tool: '📓 Copilot Notebook',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via copilot.microsoft.com > Notebook tab. Upload up to 5 files and set a system instruction. Best for synthesising insights across multiple documents simultaneously.',
          prompts: [
            'Upload 14_Zava_Properties_Portfolio.xlsx and 03_Zava_Group_Strategy_Framework.docx to Copilot Notebook. Set instruction: "You are a REIT structuring advisor helping Zava Properties prepare for their 2026 IPO." Ask: Based on the portfolio data and strategy, what is the single biggest risk to the REIT IPO timeline and what concrete action should be taken in the next 30 days to address it?',
            'Upload 14_Zava_Properties_Portfolio.xlsx. Ask: If Shell does not renew and Menara Zava KL drops to 70% occupancy, what is the impact on the REIT\'s projected distribution per unit in Year 1 and Year 2? Is the REIT still investable at a 5.5% yield target? What asset enhancement actions could partially offset the revenue loss within 12 months?'
          ]
        },
        {
          tool: '🤝 Cowork (Frontier)',
          license: 'M365 Copilot + Frontier Program',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Cowork is an autonomous agent that takes actions across Microsoft 365 on your behalf — sending emails, scheduling meetings, creating documents, posting in Teams, and scheduling recurring tasks. Access: m365.cloud.microsoft > left nav > Agents > Cowork. Requires Frontier program enrollment.',
          prompts: [
            'Do all of the following: (1) Research current Grade A office vacancy rates in KL Sentral, KLCC, and Bangsar South as context for the Shell lease negotiation. (2) Draft a 2-page Shell lease renewal proposal offering a 5-year renewal at current rate plus CPI escalation plus MYR 12M building enhancement commitment. (3) Save to OneDrive as "Shell Lease Renewal Proposal". (4) Email to the Chief Leasing Officer and the General Counsel for review before sending to Shell. (5) Schedule a Shell meeting prep call with the leasing team for next Monday.',
            'Do all of the following for the REIT IPO: (1) Research the SC Malaysia\'s most recent guidelines on REIT IPO structuring and the minimum requirements for prospectus filing. (2) Draft a 90-day REIT IPO preparation checklist covering legal, valuation, accounting, and investor roadshow workstreams. (3) Email to the CFO, General Counsel, and Head of Finance for review. (4) Create a REIT IPO project folder in SharePoint with the preparation checklist and the asset injection schedule. (5) Schedule a weekly 1-hour REIT IPO steering committee meeting for 20 weeks starting next Monday.'
          ]
        },
        {
          tool: '🤖 Word Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to a Word document. Open the .docx in Word for Web > Copilot pane > + New Agent > name it, write a description, set the document as knowledge source > Share. Colleagues chat with it in Teams or M365 Copilot.',
          prompts: [
            'Open 03_Zava_Group_Strategy_Framework.docx in Word for Web. Create an agent called "Zava Properties REIT & Strategy Bot". Description: "Answers questions from the Zava Properties team on the REIT IPO strategy, asset injection criteria, lease management requirements, and Penang development milestones." Share with the Properties executive team.',
            'Demo: An asset manager asks "We have a 180,000 sq ft industrial warehouse in Nilai with 100% occupancy but a 3.8% NPI yield. Does it qualify for REIT injection and is the yield high enough for institutional REIT investors?" Show how the agent provides a data-grounded, strategy-aligned answer.'
          ]
        },
        {
          tool: '🤖 PowerPoint Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to a PowerPoint presentation. Great for strategy decks or Board presentations many people need to reference. Same setup as Word Agent but using a .pptx file.',
          prompts: [
            'Create a PowerPoint from the REIT IPO roadshow deck. Create an agent called "Zava REIT IPO Roadshow Q&A Bot". Share with institutional investor relations contacts and joint lead managers.',
            'Demo: An institutional investor asks "What is the Year 1 DPU yield at the indicative IPO price and how does it compare to the average Malaysian REIT peer yield? Also, what is the WALE of the portfolio and which assets carry the highest lease renewal risk?" Show the agent answering a real investor due diligence question.'
          ]
        },
        {
          tool: '🤖 Excel Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to an Excel workbook. Colleagues ask data questions in plain English without opening Excel. Open .xlsx in Excel for Web > Copilot pane > + New Agent > set workbook as knowledge source > share.',
          prompts: [
            'Open 14_Zava_Properties_Portfolio.xlsx in Excel for Web. Create an agent called "Zava Properties Portfolio Q&A". Description: "Instant answers on the 25-asset portfolio — occupancy, NPI yield, WALE, REIT eligibility, and development pipeline — for the CEO, CFO, and asset management team." Share with the Properties executive team.',
            'Demo: Ask "Which assets currently have occupancy below 85% and what is the combined revenue impact of those vacancies?" Then: "What is the total NPI from the 12 REIT-eligible assets and what REIT market cap does that imply at a 5.5% cap rate?" Show the CFO getting instant portfolio intelligence.'
          ]
        },
        {
          tool: '🏗 Agent Builder (Copilot Studio)',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Build a custom declarative agent in Copilot Studio — no coding required. Access: copilotstudio.microsoft.com > Create > New Agent. Add name, description, knowledge sources (SharePoint URLs or uploaded files), topics/actions. Publish to Teams in under 10 minutes.',
          prompts: [
            'Go to copilotstudio.microsoft.com > Create > New Agent. Name it "Zava Properties Intelligence Agent". Description: "Supports the Zava Properties team with instant answers on asset portfolio performance, REIT IPO structuring, tenant management, development project status, and Malaysian property market conditions — helping the team make faster, data-driven asset management decisions." Upload 14_Zava_Properties_Portfolio.xlsx and 03_Zava_Group_Strategy_Framework.docx. Add topics: "REIT IPO", "Portfolio Performance", "Tenant Management", "Development Projects". Publish to Teams.',
            'Demo the agent: The CEO is preparing for a breakfast meeting with a GIC Singapore institutional investor at 7:30am. At 6:45am the CEO asks the agent: "Give me 3 data points about our portfolio quality that will resonate with a Singaporean institutional REIT investor, and tell me the 2 questions they are most likely to ask about our Shell anchor lease risk and how I should answer them." Show how the agent prepares the CEO for a high-stakes investor meeting in under 2 minutes.'
          ]
        }
      ]
    },
    {
      id: 'logistics-3pl',
      sectorId: 'logistics',
      subsector: '',
      name: 'Logistics & 3PL',
      icon: '🚢',
      color: '#00695C',
      accent: '#00796B',
      company: 'Samudera Logistics',
      tagline: '48 vessels, IMO 2030 decarbonisation — biofuel pilot + cold chain expansion.',
      scenario: 'Samudera Logistics operates 48 vessels across ASEAN corridors and manages 340,000 sq ft of bonded warehousing. IMO 2030 carbon intensity regulations require a 40% fuel efficiency improvement. A biofuel blending pilot on 6 vessels launched in Q1 FY2025. Cold chain logistics expansion into 3 new markets is in progress.',
      files: [
        '15_Zava_BPO_Operations.xlsx',
        '20_Zava_ESG_Sustainability_Framework.docx'
      ],
      prompts: [
        {
          tool: '🤖 Copilot Chat (Basic)',
          license: 'Free — no M365 Copilot license needed',
          account: 'Sasha Ouellet — SashaO@ABSx62256373.OnMicrosoft.com',
          desc: '',
          prompts: [
            'I am the Chief Operations Officer of an ASEAN regional shipping and logistics company operating 48 vessels. IMO 2030 regulations require us to cut carbon intensity by 40% vs 2008 baseline within 5 years. We have launched a biofuel blending pilot on 6 vessels at USD 28/MT premium over conventional bunker fuel. Draft a 250-word brief for our Board on: (1) What IMO 2030 and Carbon Intensity Indicator (CII) ratings mean for vessel valuations and charter contracts, (2) Whether biofuel blending at USD 28/MT premium is financially viable at scale, (3) Alternative decarbonisation pathways for ASEAN regional shipping (LNG, methanol, electrification).',
            'Explain what the Carbon Intensity Indicator (CII) rating system is for shipping, how vessels are rated from A to E, and what the consequences are for vessels rated D or E — including potential port restrictions and charter contract penalties.',
            'What is the business case for expanding cold chain logistics in Southeast Asia? What are the key industries driving demand, the infrastructure requirements, and the typical return on investment for a regional 3PL investing MYR 85M in cold storage and refrigerated transport?'
          ]
        },
        {
          tool: '🔍 Researcher',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via Microsoft 365 Copilot Chat (copilot.microsoft.com or Teams) > click Agents > Researcher. Grounds answers in live web sources and your organisation data with full citations.',
          prompts: [
            'Research IMO 2030 decarbonisation requirements for ASEAN shipping operators. I need: (1) The CII rating thresholds and how they change annually, (2) How leading ASEAN shipping companies (MISC, PIL, Wan Hai) are addressing IMO 2030 compliance, (3) The availability and pricing of sustainable marine fuels in ASEAN ports, (4) Any Malaysian government incentives for green shipping. Cite official IMO and industry sources.',
            'Research the ASEAN cold chain logistics market. I need: (1) Market size and growth rate in Malaysia, Indonesia, and Vietnam, (2) Key demand drivers — pharmaceutical, food & beverage, e-commerce, (3) Top 3PL providers and their cold chain capabilities, (4) Investment requirements for cold storage expansion. Cite logistics industry reports.'
          ]
        },
        {
          tool: '📊 Analyst',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via Microsoft 365 Copilot Chat > click Agents > Analyst. Upload an Excel or CSV file. Analyst runs Python-style analysis, builds charts, and interprets results without you writing a single formula.',
          prompts: [
            'Upload 15_Zava_BPO_Operations.xlsx (use as operational data proxy). Ask Analyst: Build a fleet CII rating model. For a fleet of 48 vessels with average age 9 years, calculate the CII rating for each vessel class (container, bulker, tanker) based on current fuel consumption and cargo carried. Project the CII rating trajectory if biofuel blending reduces carbon intensity by 12% per year. Which vessels will reach a D or E rating by 2027 without intervention?',
            'Upload 15_Zava_BPO_Operations.xlsx. Ask: Build a cold chain expansion ROI model. Investment: MYR 85M across 3 markets (Malaysia MYR 45M, Indonesia MYR 28M, Vietnam MYR 12M). Revenue assumptions: Year 1 capacity 40% utilised at MYR 180/pallet/month, Year 3 capacity 75% utilised. Calculate: NPV at 10% discount rate, IRR, and payback period. Show sensitivity to utilisation rate (50%, 65%, 75%, 85%).'
          ]
        },
        {
          tool: '📊 Copilot in Excel',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open 15_Zava_BPO_Operations.xlsx. Navigate to the Operations sheet. Ask Copilot: Create a fleet CII monitoring dashboard on a new sheet. For each of the 48 vessels, show: (1) Vessel name and class, (2) Current fuel consumption (tonnes/nautical mile), (3) CII score (calculated), (4) CII rating (A/B/C/D/E), (5) Biofuel pilot status (Y/N), (6) Next dry dock date. Highlight D-rated vessels in amber and E-rated vessels in red.',
            'Ask Copilot: Build a biofuel blending cost-benefit tracker. For the 6 pilot vessels, show: Monthly biofuel consumption (MT), biofuel premium cost (USD/MT above conventional), total premium cost per month, carbon intensity improvement achieved (%), and CII rating before/after biofuel. Calculate the cost per CII grade improvement point.',
            'Ask Copilot: Create a cold chain expansion project tracker on a new sheet. For each of the 3 markets (Malaysia, Indonesia, Vietnam), show: facility size (sq m), storage capacity (pallets), investment (MYR M), build status (design/construction/commissioning/operational), planned go-live date, pre-committed customers, and projected Year 1 revenue. Add a total row and a portfolio IRR calculation.'
          ]
        },
        {
          tool: '📝 Copilot in Word',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open 20_Zava_ESG_Sustainability_Framework.docx. Ask Copilot: Draft a Green Shipping Strategy section for our ESG report. Cover: (1) Our commitment to IMO 2030 CII targets, (2) Biofuel blending pilot results — 6 vessels, 12 months data, (3) Fleet modernisation plan — 8 vessels to be retired by 2026, replaced with dual-fuel capable vessels, (4) Alternative fuel roadmap — evaluation of LNG, methanol, and green ammonia for ASEAN corridors, (5) Investment plan — USD 240M over 5 years in green fleet. Use GRI 302 (Energy) and GRI 305 (Emissions) reporting standards.',
            'Ask Copilot: Draft a customer presentation script for cold chain expansion. The script is for a 30-minute meeting with a pharmaceutical manufacturer who is evaluating cold chain outsourcing. Cover: (1) Our cold chain capabilities across Malaysia, Indonesia, and Vietnam, (2) Good Distribution Practice (GDP) certification and regulatory compliance, (3) Real-time temperature monitoring and SCADA system, (4) Case study from an existing pharma customer, (5) Pricing structure and SLA commitments. Include suggested responses to 3 likely objections.',
            'Ask Copilot: Draft an urgent response letter to a key customer whose cargo was delayed 72 hours due to a port congestion issue in Surabaya. The letter should: acknowledge the delay and apologise unequivocally, explain the root cause (berth unavailability due to port authority planning issue — not Samudera\'s operational failure), confirm the cargo has now been delivered safely, propose penalty waiver or credit note as goodwill, and outline the contingency routing we have now put in place.'
          ]
        },
        {
          tool: '🎯 Copilot in PowerPoint',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Ask Copilot in PowerPoint: Create a 10-slide investor presentation for Samudera Logistics. Include: (1) Business overview — 48 vessels, ASEAN network, (2) IMO 2030 compliance plan — biofuel pilot results, (3) Fleet CII rating dashboard, (4) Cold chain expansion — MYR 85M investment, 3 markets, (5) Financial performance — revenue and EBITDA, (6) Technology — real-time vessel tracking and cold chain IoT, (7) Sustainability credentials, (8) Growth outlook, (9) Risk factors, (10) Investment thesis. Teal and white colour scheme.',
            'Ask Copilot: Create a 3-slide cold chain pitch deck for pharmaceutical customers. Slide 1: Why outsource cold chain to Samudera — 3 key value propositions. Slide 2: Our cold chain network map across Malaysia, Indonesia, Vietnam. Slide 3: GDP compliance, temperature monitoring, and SLA guarantees.',
            'Ask Copilot: Create a 2-slide CII compliance update for the Board. Slide 1: Current fleet CII rating distribution — how many vessels at A, B, C, D, E. Slide 2: The 3-year plan to bring all vessels to CII C or better — biofuel, fleet retirement, and dual-fuel newbuilds.'
          ]
        },
        {
          tool: '📧 Copilot in Outlook',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Ask Copilot in Outlook: Draft a proposal email to a large FMCG manufacturer offering an integrated end-to-end cold chain solution — refrigerated sea freight from Indonesia to Malaysia, bonded cold storage in Port Klang, and last-mile refrigerated delivery to 12 distribution points. Include: key service specifications, GDP certification, real-time temperature visibility, and indicative pricing at MYR 195/pallet/month.',
            'Ask Copilot: Draft an internal alert to the fleet operations team: a weather system is forecast in the South China Sea over the next 72 hours affecting our 8 vessels on the MY-Vietnam corridor. The alert should: describe the weather situation, state the routing instruction (alternative route via east coast), confirm the customer notification process, and ask vessel masters to confirm receipt.',
            'Ask Copilot: Draft an email to IMO\'s Data Collection System (DCS) reporting team confirming our fleet carbon intensity data submission for FY2024. The email should confirm the 48 vessels covered, the fuel consumption and distance data submitted, and note that 6 vessels on the biofuel pilot have their biodiesel volumes separately identified. Request confirmation of receipt.'
          ]
        },
        {
          tool: '🎙 Copilot in Teams',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Use your OWN existing recorded Teams meetings. Open a meeting recap in Teams > Recap tab. Copilot generates summaries, action items, and follow-up drafts grounded in the actual transcript.',
          prompts: [
            'Open an existing recorded Teams meeting recap from an operations or fleet management meeting. Ask Copilot: Identify all vessel performance issues discussed — CII rating concerns, maintenance alerts, route delays, and customer complaints. Create an action log with owner and deadline.',
            'Ask Copilot: Draft a fleet operations update for the weekly leadership meeting. Structure: (1) Fleet status — vessels operational / off hire / in dry dock, (2) CII compliance — any vessels requiring immediate action, (3) Biofuel pilot update, (4) Cold chain facility status, (5) Top 3 customer issues.',
            'Ask Copilot: From the meeting transcript, what decisions were made about the biofuel pilot expansion from 6 to 15 vessels? What concerns were raised about biofuel supply availability in Indonesian ports?'
          ]
        },
        {
          tool: '📓 Copilot Notebook',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via copilot.microsoft.com > Notebook tab. Upload up to 5 files and set a system instruction. Best for synthesising insights across multiple documents simultaneously.',
          prompts: [
            'Upload 15_Zava_BPO_Operations.xlsx and 20_Zava_ESG_Sustainability_Framework.docx to Copilot Notebook. Set instruction: "You are a sustainability advisor helping Samudera Logistics achieve IMO 2030 compliance." Ask: Based on the operational data and ESG framework, what is the fastest path to CII B rating for the 12 vessels currently rated C/D? Quantify the cost and the timeline for each intervention option.',
            'Upload 20_Zava_ESG_Sustainability_Framework.docx. Ask: Our biofuel blending pilot on 6 vessels has achieved a 9% CII improvement but at a USD 28/MT fuel premium. Customers are pushing back on a proposed 4% surcharge to cover the premium. Draft 3 negotiation arguments I can use with customers to justify the surcharge — using both environmental and commercial angles.'
          ]
        },
        {
          tool: '🤝 Cowork (Frontier)',
          license: 'M365 Copilot + Frontier Program',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Cowork is an autonomous agent that takes actions across Microsoft 365 on your behalf — sending emails, scheduling meetings, creating documents, posting in Teams, and scheduling recurring tasks. Access: m365.cloud.microsoft > left nav > Agents > Cowork. Requires Frontier program enrollment.',
          prompts: [
            'Do all of the following: (1) Research the latest IMO CII rating thresholds for 2025 and 2026 and identify which vessel classes are most affected. (2) Draft an IMO 2030 compliance roadmap for a 48-vessel ASEAN fleet covering biofuel, fleet retirement, and dual-fuel newbuild options. (3) Save to OneDrive as "IMO 2030 Compliance Roadmap". (4) Email to the COO and Head of Fleet Management for review. (5) Schedule a fleet decarbonisation strategy workshop with the ops and sustainability teams.',
            'Do all of the following for cold chain expansion: (1) Research Good Distribution Practice (GDP) certification requirements for cold chain operators in Malaysia, Indonesia, and Vietnam. (2) Draft a GDP certification application timeline and checklist for each market. (3) Email to the cold chain operations manager and the compliance team asking for review. (4) Create a cold chain project folder in SharePoint with the GDP requirements for each market. (5) Schedule weekly project review meetings with the construction and operations teams.'
          ]
        },
        {
          tool: '🤖 Word Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to a Word document. Open the .docx in Word for Web > Copilot pane > + New Agent > name it, write a description, set the document as knowledge source > Share. Colleagues chat with it in Teams or M365 Copilot.',
          prompts: [
            'Open 20_Zava_ESG_Sustainability_Framework.docx in Word for Web. Create an agent called "Samudera Sustainability & Compliance Bot". Description: "Answers fleet managers and operations teams on IMO 2030 CII requirements, biofuel specifications, GDP cold chain regulations, and ESG reporting obligations." Share with the fleet management and operations team.',
            'Demo: A vessel master radios in asking: "We are at 92% of our annual CII allowance with 3 months remaining. What operational measures can I take immediately — speed reduction, fuel change, route optimisation — to keep within the CII C threshold for the year?" Show how the agent provides immediate, practical decarbonisation guidance.'
          ]
        },
        {
          tool: '🤖 PowerPoint Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to a PowerPoint presentation. Great for strategy decks or Board presentations many people need to reference. Same setup as Word Agent but using a .pptx file.',
          prompts: [
            'Create a PowerPoint from the investor presentation. Create an agent called "Samudera Investor Q&A Bot". Share with investor relations contacts.',
            'Demo: An analyst asks "What is your current CII rating distribution across the 48-vessel fleet and how confident are you in achieving all vessels at CII C or better by 2027?" Show the agent providing a fleet-data-grounded compliance outlook.'
          ]
        },
        {
          tool: '🤖 Excel Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to an Excel workbook. Colleagues ask data questions in plain English without opening Excel. Open .xlsx in Excel for Web > Copilot pane > + New Agent > set workbook as knowledge source > share.',
          prompts: [
            'Open 15_Zava_BPO_Operations.xlsx in Excel for Web. Create an agent called "Samudera Fleet & Operations Q&A". Description: "Instant answers on fleet CII ratings, biofuel pilot performance, cold chain utilisation, and customer SLA status for the COO and operations leadership." Share with the operations leadership team.',
            'Demo: Ask "Which vessels are currently at CII D rating and when is their next dry dock scheduled?" Then: "What is the current utilisation rate of our Malaysia cold storage facility and which customer accounts for the largest volume?" Show the COO getting instant operational intelligence.'
          ]
        },
        {
          tool: '🏗 Agent Builder (Copilot Studio)',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Build a custom declarative agent in Copilot Studio — no coding required. Access: copilotstudio.microsoft.com > Create > New Agent. Add name, description, knowledge sources (SharePoint URLs or uploaded files), topics/actions. Publish to Teams in under 10 minutes.',
          prompts: [
            'Go to copilotstudio.microsoft.com > Create > New Agent. Name it "Samudera Logistics Operations Intelligence Agent". Description: "Supports Samudera\'s fleet managers, operations team, and COO with instant answers on IMO 2030 CII compliance, biofuel pilot data, cold chain operations, customer SLA status, and regulatory requirements — enabling faster, smarter logistics decisions across the ASEAN fleet." Upload 15_Zava_BPO_Operations.xlsx and 20_Zava_ESG_Sustainability_Framework.docx. Add topics: "CII Compliance", "Biofuel Operations", "Cold Chain", "Customer SLA". Publish to Teams.',
            'Demo the agent: A customer service manager receives a complaint from a pharmaceutical client: "Our insulin shipment temperature log shows 2 excursions above 8°C lasting 4 hours during transit from Penang to Jakarta. The shipment value is USD 840,000. What is our liability, what GDP investigation is required, and do we need to notify the client\'s quality team immediately?" Show how the agent provides an instant, policy-grounded crisis response path.'
          ]
        }
      ]
    },
    {
      id: 'coal-mining',
      sectorId: 'mining',
      subsector: '',
      name: 'Coal Mining',
      icon: '⛏',
      color: '#424242',
      accent: '#616161',
      company: 'PrimaCal Energy Berhad',
      tagline: 'ESDM royalty audit + EUDR-adjacent ESG risk — coal exit transition plan FY2026.',
      scenario: 'PrimaCal Energy Berhad operates 3 thermal coal concessions in East Kalimantan, Indonesia with 28MT annual production capacity. An ESDM (Indonesian Ministry of Energy) royalty audit is underway covering FY2022–FY2024. ESG pressure from European offtakers is intensifying. The Board has resolved to develop a coal exit and energy transition plan by Q4 FY2025.',
      files: [
        '16_Zava_Trading_Commodities.xlsx',
        '20_Zava_ESG_Sustainability_Framework.docx'
      ],
      prompts: [
        {
          tool: '🤖 Copilot Chat (Basic)',
          license: 'Free — no M365 Copilot license needed',
          account: 'Sasha Ouellet — SashaO@ABSx62256373.OnMicrosoft.com',
          desc: '',
          prompts: [
            'I am the CEO of a Malaysian-listed coal mining company operating in East Kalimantan, Indonesia. Royalty rates from the Indonesian ESDM have increased and a back-audit covering FY2022-FY2024 is underway. Our external auditors estimate additional royalty exposure of USD 18.4M. Draft a 250-word brief for my CFO covering: (1) How coal production royalties in Indonesia are calculated (IUP vs IUPK structure), (2) Typical outcomes of an ESDM back-audit — what can be challenged vs conceded, (3) The accounting treatment for the contingent royalty liability under MFRS 137.',
            'European institutional shareholders are pressuring us to publish a coal exit timeline. The Board is divided — some directors want to continue mining until 2035 to maximise shareholder returns; others want to announce a 2030 exit. Draft a 200-word board memo arguing the case for a 2030 coal exit with a managed transition to thermal energy assets.',
            'What is the current thermal coal market outlook for 2025–2027? Which countries are still buying East Kalimantan coal, what is the current Newcastle benchmark price, and how does Indonesian coal trade policy affect export restrictions?'
          ]
        },
        {
          tool: '🔍 Researcher',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via Microsoft 365 Copilot Chat (copilot.microsoft.com or Teams) > click Agents > Researcher. Grounds answers in live web sources and your organisation data with full citations.',
          prompts: [
            'Research ESG requirements for coal mining companies listed on Bursa Malaysia. I need: (1) Bursa Malaysia\'s sustainability reporting requirements for mining companies, (2) Whether any Malaysian-listed coal companies have published coal exit timelines and what the investor reaction was, (3) How comparable companies (Bumi Resources, Indo Tambangraya Megah) are managing ESG pressure. Cite sources.',
            'Research the energy transition opportunity for coal mine operators in East Kalimantan. What clean energy projects are feasible on coal mining land? Are there any Indonesian government incentives for coal-to-clean-energy transitions? What has been the experience of companies like Adaro in transitioning from coal? Cite industry sources.'
          ]
        },
        {
          tool: '📊 Analyst',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via Microsoft 365 Copilot Chat > click Agents > Analyst. Upload an Excel or CSV file. Analyst runs Python-style analysis, builds charts, and interprets results without you writing a single formula.',
          prompts: [
            'Upload 16_Zava_Trading_Commodities.xlsx to Analyst. Ask: Analyse our coal trading position. Show: (1) Current open positions — size, direction, mark-to-market value, (2) Limit utilisation — any positions approaching or breaching limits, (3) Price sensitivity — if Newcastle benchmark drops USD 20/MT, what is the impact on open position values? (4) Counterparty concentration — what % of our coal offtake is with European buyers who have coal exclusion policies? Create a risk summary dashboard.',
            'Upload 16_Zava_Trading_Commodities.xlsx. Ask: Model the coal exit transition scenarios. Scenario A: Continue mining until 2035. Scenario B: Exit coal by 2030 and redeploy capital into solar assets in East Kalimantan. Scenario C: Exit coal by 2028 through asset sale. For each scenario, estimate: NPV of remaining coal reserves, transition cost, projected shareholder return over 10 years. Which scenario maximises long-term shareholder value?'
          ]
        },
        {
          tool: '📊 Copilot in Excel',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open 16_Zava_Trading_Commodities.xlsx. Navigate to the Open Positions sheet. Ask Copilot: Build a royalty audit exposure calculator on a new sheet. For FY2022, FY2023, and FY2024, calculate: total coal production (MT), royalty rate applied (%), royalty paid (USD M), ESDM\'s claimed royalty rate (higher %), additional royalty under audit (USD M), penalty and interest (8% per year), total exposure per year. Sum to total contingent liability. Apply red formatting if total exposure exceeds USD 15M.',
            'Ask Copilot: Create a coal export revenue sensitivity table. Rows: Newcastle benchmark price (USD 90/MT to USD 180/MT in USD 10 steps). Columns: Production volume (20MT, 24MT, 28MT). Each cell: annual revenue in USD M. Add a breakeven row showing the minimum price to cover all-in cash costs of USD 88/MT. Highlight cells where margin is negative in red, thin margin (<15%) in amber, healthy margin in green.',
            'Ask Copilot: Build an energy transition opportunity dashboard on a new sheet. For each of the 3 concession areas, estimate: (1) Land area available for solar after coal exhaustion (ha), (2) Solar generation potential (MW) at 1.5 MW/ha, (3) Estimated project cost at USD 0.8M/MW, (4) Expected IRR at Indonesian solar feed-in tariff, (5) Earliest development timeline. Calculate total transition portfolio size and aggregate IRR.'
          ]
        },
        {
          tool: '📝 Copilot in Word',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open 20_Zava_ESG_Sustainability_Framework.docx. Ask Copilot: Draft a coal exit and energy transition strategy document for Board approval. Cover: (1) Strategic rationale — ESG pressure, policy risk, capital market access, (2) Exit timeline — coal production to cease by December 2030, (3) Capital redeployment — USD 320M into East Kalimantan solar and geothermal assets 2026–2032, (4) Transition cost and funding plan, (5) Employee transition programme — 4,200 mining workers, (6) Community impact and CSR obligations, (7) Investor communication plan. 10 pages, formal board paper format.',
            'Ask Copilot: Draft the ESDM royalty audit response letter. The letter should: acknowledge the audit findings, dispute 3 specific line items where we believe the royalty calculation methodology is incorrect, propose a joint verification process with independent auditors, and request a 90-day extension to compile the disputed documentation. Use formal Indonesian government correspondence format.',
            'Ask Copilot: Write a 3-page ESG section for our Bursa Malaysia Annual Report. Cover: (1) Our carbon intensity per tonne of coal produced and the year-on-year improvement, (2) Our commitment to the Paris Agreement and the coal exit timeline, (3) Community investment around the 3 mining concessions — schools, healthcare, infrastructure, (4) Mine rehabilitation progress — area rehabilitated in FY2024 vs requirement. Comply with GRI 302, 305, and 413 standards.'
          ]
        },
        {
          tool: '🎯 Copilot in PowerPoint',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Ask Copilot in PowerPoint: Create an 8-slide coal exit and energy transition investor presentation. Include: (1) Why we are transitioning — ESG and capital market rationale, (2) Coal exit timeline — 2030, (3) East Kalimantan solar and geothermal opportunity, (4) Transition investment plan — USD 320M, (5) NPV comparison — coal-to-2035 vs transition scenario, (6) Employee and community transition plan, (7) Near-term (2025–2027) financial performance — coal revenues remain strong, (8) Why this transition creates long-term shareholder value. Dark grey and green colour scheme.',
            'Ask Copilot: Create a 2-slide royalty audit situation update for the Audit Committee. Slide 1: Audit status — 3 disputed line items, total contingent liability USD 18.4M, provision taken in accounts USD 8M, unresolved USD 10.4M. Slide 2: The 3 specific items disputed and the legal arguments for each.',
            'Ask Copilot: Add a slide showing the carbon intensity trend for PrimaCal over the past 5 years vs the Indonesian mining sector benchmark. Show the trajectory to 2030 exit — when does our carbon intensity from operations go to zero?'
          ]
        },
        {
          tool: '📧 Copilot in Outlook',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Ask Copilot in Outlook: Draft a letter from the CEO to our 3 largest European coal offtakers (combined 38% of our annual production). The letter should: proactively disclose our 2030 coal exit timeline, explain the managed transition plan, reassure them of continued supply through 2030, and invite them to explore a long-term energy partnership as we develop solar and geothermal assets. Tone: strategic, transparent, and forward-looking.',
            'Ask Copilot: Draft an internal email from the CFO to the Audit Committee Chairman disclosing the ESDM royalty audit exposure. The email should: state the nature and scale of the contingent liability, the accounting treatment, the legal strategy for disputing 3 items, and the timeline for resolution. Mark as CONFIDENTIAL.',
            'Ask Copilot: Draft a community engagement letter to the village heads (kepala desa) of the 12 communities within 5km of our mining concessions. Inform them of the coal exit plan, the mine rehabilitation commitments, and the energy transition projects that will create new employment opportunities. Use community-appropriate language.'
          ]
        },
        {
          tool: '🎙 Copilot in Teams',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Use your OWN existing recorded Teams meetings. Open a meeting recap in Teams > Recap tab. Copilot generates summaries, action items, and follow-up drafts grounded in the actual transcript.',
          prompts: [
            'Open an existing recorded Teams meeting recap from a management or sustainability committee meeting. Ask Copilot: Identify all ESG-related action items and any discussions about the coal exit strategy or royalty audit. Flag items that are overdue.',
            'Ask Copilot: Draft a management update on the royalty audit status for the weekly operations call. Cover: (1) Audit status, (2) Items disputed and timeline, (3) Provision adequacy, (4) Legal team action items, (5) Next ESDM meeting date.',
            'Ask Copilot: Were there any discussions about employee communication regarding the 2030 coal exit? What concerns were raised by HR and how is the transition programme being designed?'
          ]
        },
        {
          tool: '📓 Copilot Notebook',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via copilot.microsoft.com > Notebook tab. Upload up to 5 files and set a system instruction. Best for synthesising insights across multiple documents simultaneously.',
          prompts: [
            'Upload 16_Zava_Trading_Commodities.xlsx and 20_Zava_ESG_Sustainability_Framework.docx to Copilot Notebook. Set instruction: "You are an ESG advisor helping PrimaCal Energy develop its coal exit strategy." Ask: Based on the trading position data and ESG framework, which ESG commitments are currently incompatible with continued coal mining operations? Identify the specific GRI or TCFD disclosures where our coal operations represent the biggest exposure.',
            'Upload 20_Zava_ESG_Sustainability_Framework.docx. Ask: Our 4,200 mining workers will need retraining and redeployment as we phase out coal operations by 2030. Design a 5-year just transition programme covering: skill assessment, retraining priorities (solar installation, environmental rehabilitation, vocational trades), employment partnerships with renewable energy developers, and the budget required per worker.'
          ]
        },
        {
          tool: '🤝 Cowork (Frontier)',
          license: 'M365 Copilot + Frontier Program',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Cowork is an autonomous agent that takes actions across Microsoft 365 on your behalf — sending emails, scheduling meetings, creating documents, posting in Teams, and scheduling recurring tasks. Access: m365.cloud.microsoft > left nav > Agents > Cowork. Requires Frontier program enrollment.',
          prompts: [
            'Do all of the following: (1) Research the ESDM royalty calculation methodology for Indonesian coal IUP holders and identify any recent court decisions where companies successfully disputed royalty audit findings. (2) Draft a 3-page legal brief summarising our 3 disputed audit items and the strongest arguments for each. (3) Save to OneDrive as "ESDM Royalty Dispute Brief - CONFIDENTIAL". (4) Email to the General Counsel and external counsel with a request for review within 48 hours. (5) Schedule an urgent legal strategy call for tomorrow at 2pm.',
            'Do all of the following for ESG investor communication: (1) Research how other coal companies have managed the investor communication around their coal exit announcements — what language worked, what backfired. (2) Draft a 500-word ESG transition press release announcing our 2030 coal exit and energy transition plan. (3) Save to OneDrive as "PrimaCal Coal Exit Press Release". (4) Email to the CEO, CFO, and Head of IR for review. (5) Schedule an investor call for next month to answer questions about the transition plan.'
          ]
        },
        {
          tool: '🤖 Word Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to a Word document. Open the .docx in Word for Web > Copilot pane > + New Agent > name it, write a description, set the document as knowledge source > Share. Colleagues chat with it in Teams or M365 Copilot.',
          prompts: [
            'Open 20_Zava_ESG_Sustainability_Framework.docx in Word for Web. Create an agent called "PrimaCal ESG & Compliance Bot". Description: "Answers questions from the sustainability, legal, and operations teams about ESG reporting requirements, royalty obligations, mine rehabilitation standards, and energy transition options for East Kalimantan." Share with the ESG and legal teams.',
            'Demo: A sustainability analyst asks "We need to report our Scope 3 emissions for our coal product — the emissions when customers burn the coal. Is Scope 3 Category 11 reporting required under GRI 305 and what data do we need from our customers to calculate it?" Show how the agent provides a technically accurate GRI compliance answer.'
          ]
        },
        {
          tool: '🤖 PowerPoint Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to a PowerPoint presentation. Great for strategy decks or Board presentations many people need to reference. Same setup as Word Agent but using a .pptx file.',
          prompts: [
            'Create a PowerPoint from the transition investor presentation. Create an agent called "PrimaCal Transition Strategy Q&A". Share with institutional investor relations contacts.',
            'Demo: A Scandinavian pension fund analyst asks "What is PrimaCal\'s Scope 1 + Scope 2 carbon intensity per tonne of coal produced and how does this compare to the Indonesian mining sector average? Also, will you commit to interim 2027 emissions reduction targets?" Show the agent providing an ESG data-grounded response.'
          ]
        },
        {
          tool: '🤖 Excel Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to an Excel workbook. Colleagues ask data questions in plain English without opening Excel. Open .xlsx in Excel for Web > Copilot pane > + New Agent > set workbook as knowledge source > share.',
          prompts: [
            'Open 16_Zava_Trading_Commodities.xlsx in Excel for Web. Create an agent called "PrimaCal Commodity & Risk Q&A". Description: "Instant answers on coal trading positions, royalty audit exposure, price sensitivity, and energy transition ROI for the CEO, CFO, and risk team." Share with the executive team.',
            'Demo: Ask "What is our current coal position mark-to-market if Newcastle falls to USD 95/MT?" Then: "What is the royalty audit contingent liability vs what we have provisioned in the accounts?" Show the CFO getting instant risk intelligence.'
          ]
        },
        {
          tool: '🏗 Agent Builder (Copilot Studio)',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Build a custom declarative agent in Copilot Studio — no coding required. Access: copilotstudio.microsoft.com > Create > New Agent. Add name, description, knowledge sources (SharePoint URLs or uploaded files), topics/actions. Publish to Teams in under 10 minutes.',
          prompts: [
            'Go to copilotstudio.microsoft.com > Create > New Agent. Name it "PrimaCal Energy Intelligence Agent". Description: "Supports PrimaCal\'s executive team, legal counsel, and operations managers with instant answers on coal royalty obligations, ESDM regulatory requirements, ESG reporting standards, coal market outlook, and energy transition strategy — helping the company navigate a complex multi-year transformation." Upload 16_Zava_Trading_Commodities.xlsx and 20_Zava_ESG_Sustainability_Framework.docx. Add topics: "Royalty Compliance", "ESG Reporting", "Energy Transition", "Coal Market". Publish to Teams.',
            'Demo the agent: The CEO is travelling to Jakarta for an unplanned meeting with ESDM officials about the royalty audit. On the way to the meeting, the CEO asks the agent: "Give me the 3 key facts I need to defend our royalty calculation methodology to ESDM, and tell me the maximum additional liability we would face if we lose all 3 disputed items. Also — what is our current coal price and how does that affect our ability to settle the audit now vs litigate?" Show how the agent prepares the CEO for a high-stakes regulatory meeting in real time.'
          ]
        }
      ]
    },
    {
      id: 'hotel-resort',
      sectorId: 'hospitality',
      subsector: '',
      name: 'Hotel & Resort',
      icon: '🏨',
      color: '#AD1457',
      accent: '#C2185B',
      company: 'Suria Hotels & Resorts',
      tagline: 'RevPAR MYR 284 — F&B margin recovery + staff turnover 32% reduction programme.',
      scenario: 'Suria Hotels & Resorts operates 14 properties across Malaysia, Indonesia, and Thailand — 4 five-star city hotels, 6 four-star business hotels, and 4 resort properties. RevPAR stands at MYR 284 vs pre-COVID benchmark of MYR 318. F&B margin has slipped to 18.4% from a target of 26%. Staff turnover is 32% — the industry\'s leading challenge post-COVID.',
      files: [
        'HT_01_Suria_Hotels_Resorts.xlsx',
        '18_Zava_HR_Analytics.xlsx'
      ],
      prompts: [
        {
          tool: '🤖 Copilot Chat (Basic)',
          license: 'Free — no M365 Copilot license needed',
          account: 'Sasha Ouellet — SashaO@ABSx62256373.OnMicrosoft.com',
          desc: '',
          prompts: [
            'I am the Chief Commercial Officer of a regional hotel chain with 14 properties in Malaysia, Indonesia, and Thailand. Our RevPAR is MYR 284 vs our pre-COVID benchmark of MYR 318 — a 10.7% gap. Our occupancy has recovered to 74% but our ADR is still 15% below benchmark. Draft a 250-word strategic brief covering: (1) The 3 most effective strategies to close the ADR gap — segmentation, direct booking incentives, and rate parity management, (2) How OTA dependency (currently 58% of room revenue booked through OTAs) is suppressing net ADR, (3) The target direct booking % we should achieve in 12 months to recover MYR 18/RevPAR.',
            'Explain what F&B contribution margin is in hotel operations, what a target margin of 26% implies for menu pricing and cost of goods sold, and what the 3 most common reasons why hotel F&B margins slip from 26% to 18% post-COVID.',
            'What are the best practices for reducing staff turnover in the hospitality industry? We have 32% annual turnover across our 14 properties — above the industry benchmark of 28%. Focus on practical retention strategies that work in Southeast Asian hospitality markets.'
          ]
        },
        {
          tool: '🔍 Researcher',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via Microsoft 365 Copilot Chat (copilot.microsoft.com or Teams) > click Agents > Researcher. Grounds answers in live web sources and your organisation data with full citations.',
          prompts: [
            'Research the hotel and resort market recovery in Malaysia, Indonesia, and Thailand in 2024–2025. I need: (1) Current average occupancy and RevPAR benchmarks by market and hotel class (5-star, 4-star, resort), (2) Key demand drivers — MICE, corporate, leisure, inbound tourism, (3) How leading hotel chains (Marriott, IHG, Shangri-La) are driving ADR recovery. Cite industry sources (STR, JLL, CBRE Hotels).',
            'Research F&B profitability improvement best practices for hotel F&B operations in Southeast Asia. What menu engineering techniques, supplier renegotiation strategies, and upselling training programmes have delivered the best margin improvements? Are there any relevant technology solutions (revenue management, menu analytics) used by leading Asian hotel groups? Cite sources.'
          ]
        },
        {
          tool: '📊 Analyst',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via Microsoft 365 Copilot Chat > click Agents > Analyst. Upload an Excel or CSV file. Analyst runs Python-style analysis, builds charts, and interprets results without you writing a single formula.',
          prompts: [
            'Upload HT_01_Suria_Hotels_Resorts.xlsx to Analyst. Ask: Build a RevPAR recovery dashboard. For each of the 14 properties, show: (1) Current RevPAR vs pre-COVID benchmark, (2) Occupancy rate and ADR, (3) OTA booking mix vs direct channels, (4) Year-on-year RevPAR improvement rate. Identify the 3 properties with the biggest RevPAR gap and the 3 with the fastest recovery rate. Calculate the group-level revenue impact if all properties reach pre-COVID RevPAR by end of FY2026.',
            'Upload 18_Zava_HR_Analytics.xlsx. Ask: Analyse the staff turnover data for the hospitality division. Which properties have turnover above 35%? Which departments are most affected (F&B, Housekeeping, Front Office)? Calculate the annual replacement cost for each property assuming MYR 8,500 recruitment cost per departing employee. Rank properties by total annual turnover cost and identify the 3 highest-cost properties where a retention investment would have the biggest ROI.'
          ]
        },
        {
          tool: '📊 Copilot in Excel',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open HT_01_Suria_Hotels_Resorts.xlsx. Navigate to the Financial Performance sheet. Ask Copilot: Create a F&B margin recovery tracker on a new sheet. For each of the 14 properties, show: (1) Current F&B revenue (MYR M), (2) F&B cost of goods sold (MYR M), (3) Current F&B margin %, (4) Target margin 26%, (5) Gap in percentage points, (6) Revenue required at target margin (MYR M). Calculate the group-level F&B revenue improvement at target margin vs current margin.',
            'Ask Copilot: Build an OTA mix optimisation dashboard. For each property, show: (1) OTA bookings as % of total, (2) Average OTA commission rate (%), (3) Net ADR after OTA commission, (4) Direct booking ADR (no commission), (5) Revenue gain if OTA mix reduces by 10 percentage points. Highlight properties where the OTA commission cost exceeds MYR 2M per year.',
            'Ask Copilot: Create a staff turnover cost model on a new sheet. For each property, input: total headcount, annual turnover %, recruitment cost per hire (MYR 8,500), training cost per new hire (MYR 3,200), and productivity loss during onboarding (estimated as 60% of monthly salary for 60 days). Calculate total annual turnover cost per property and rank from highest to lowest. Show the savings from reducing turnover by 8 percentage points per property.'
          ]
        },
        {
          tool: '📝 Copilot in Word',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open 18_Zava_HR_Analytics.xlsx. Ask Copilot in Word: Draft a hospitality staff retention programme proposal for the HR Committee. Cover: (1) Current turnover situation — 32%, 14 properties, cost impact MYR XX per year, (2) Root cause analysis — exit interview data, (3) 4 retention initiatives with budget and expected impact: (a) Career development programme, (b) Enhanced housing and transport benefits for remote resorts, (c) Performance-based retention bonus (12-month cliff vesting), (d) Salary benchmarking and uplift for critical roles. (4) Implementation timeline and total investment. Format as a formal HR Committee paper.',
            'Ask Copilot: Draft a menu engineering review guide for F&B managers across all 14 properties. The guide should explain: (1) What menu engineering is, (2) The 4 categories (Stars, Ploughhorses, Puzzles, Dogs) and how to classify each menu item, (3) The 5 actions to improve F&B margin (remove dogs, reprice puzzles, promote stars), (4) How to calculate cost per dish and the minimum selling price for 26% margin. Keep language practical — this is for hotel F&B managers, not accountants.',
            'Ask Copilot: Write a guest loyalty programme launch announcement for Suria Hotels — "Suria Privileges" programme. Cover: 3 membership tiers (Suria Silver, Gold, Platinum), points earning rates, tier benefits (room upgrades, F&B discounts, express check-in), partner benefits, and enrollment call-to-action. Format as a press release and as a guest email.'
          ]
        },
        {
          tool: '🎯 Copilot in PowerPoint',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Ask Copilot in PowerPoint: Create a 12-slide performance recovery presentation for the Board. Include: (1) FY2025 snapshot — RevPAR MYR 284, occupancy 74%, F&B margin 18.4%, turnover 32%, (2) RevPAR recovery roadmap — target MYR 318 by FY2027, (3) ADR improvement strategy — direct booking and rate management, (4) OTA mix reduction plan, (5) F&B margin recovery — from 18.4% to 26%, (6) Retention programme — cost and expected impact, (7) Revenue per available employee (RevPAE) improvement, (8) Property-by-property performance league table, (9) Capital investment required, (10) Three-year financial projections, (11) Key risks, (12) Board decisions required. Deep rose and gold colour scheme.',
            'Ask Copilot: Create a 3-slide RevPAR recovery pitch for a hotel owner client who is considering whether to continue with Suria as the operator. Slide 1: Where we are today vs benchmark. Slide 2: The recovery actions we are implementing. Slide 3: The projected RevPAR trajectory with Suria vs without.',
            'Ask Copilot: Create a staff retention infographic slide for the all-staff town hall. Show: 5 retention initiatives, when they launch, and what benefit each brings to frontline hotel employees. Use warm, motivating visuals — this is an internal communication piece.'
          ]
        },
        {
          tool: '📧 Copilot in Outlook',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Ask Copilot in Outlook: Draft an email to all 14 General Managers announcing the F&B margin recovery programme. The email should: state the group target of 26% margin by Q3 FY2025, explain the 4 key actions each property must take (menu engineering review, supplier renegotiation, portion control, upselling training), set the monthly reporting requirement, and ask GMs to nominate their F&B Manager as the property champion. Tone: energetic and performance-focused.',
            'Ask Copilot: Draft an email to our top 3 OTA partners (Booking.com, Expedia, Agoda) proposing a preferred partner programme. The proposal should offer enhanced listing visibility and priority placement in exchange for a reduced commission rate and guaranteed rate parity. Frame as a win-win commercial proposition.',
            'Ask Copilot: Draft a personalised renewal email to our top 500 loyalty programme members who have not stayed in the past 12 months. The email should: acknowledge their last stay, offer a "welcome back" rate (15% below BAR), invite them to the new Suria Privileges programme, and include a direct booking link. Tone: warm, personal, and exclusive.'
          ]
        },
        {
          tool: '🎙 Copilot in Teams',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Use your OWN existing recorded Teams meetings. Open a meeting recap in Teams > Recap tab. Copilot generates summaries, action items, and follow-up drafts grounded in the actual transcript.',
          prompts: [
            'Open an existing recorded Teams meeting recap from a revenue management or GM operations call. Ask Copilot: Identify all RevPAR, occupancy, and ADR discussions. Which properties are behind target? What actions have been committed to by GMs? Create an action tracker.',
            'Ask Copilot: Draft follow-up actions from the F&B margin review meeting. Group by area: Menu Engineering | Supplier Negotiation | Staff Training | Portion Control. Include property owner and deadline.',
            'Ask Copilot: Based on this meeting, which GMs raised the most concern about staff turnover? What specific causes did they identify and what interventions did they request from Group HR?'
          ]
        },
        {
          tool: '📓 Copilot Notebook',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via copilot.microsoft.com > Notebook tab. Upload up to 5 files and set a system instruction. Best for synthesising insights across multiple documents simultaneously.',
          prompts: [
            'Upload HT_01_Suria_Hotels_Resorts.xlsx and 18_Zava_HR_Analytics.xlsx to Copilot Notebook. Set instruction: "You are a hospitality management consultant advising Suria Hotels on RevPAR recovery and operational improvement." Ask: Which 3 properties should receive the most urgent management attention — considering RevPAR gap, F&B margin underperformance, and staff turnover simultaneously? What is the prioritised action plan for each?',
            'Upload HT_01_Suria_Hotels_Resorts.xlsx. Ask: The Bali resort has the highest F&B revenue of all our properties but the lowest F&B margin (14.2%). The GM believes it is because of high food cost from imported ingredients. Design a 90-day F&B margin improvement plan specifically for a Bali resort context — considering local supplier development, menu localisation, and seasonal menu rotation.'
          ]
        },
        {
          tool: '🤝 Cowork (Frontier)',
          license: 'M365 Copilot + Frontier Program',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Cowork is an autonomous agent that takes actions across Microsoft 365 on your behalf — sending emails, scheduling meetings, creating documents, posting in Teams, and scheduling recurring tasks. Access: m365.cloud.microsoft > left nav > Agents > Cowork. Requires Frontier program enrollment.',
          prompts: [
            'Do all of the following: (1) Research RevPAR recovery strategies used by comparable Asian hotel groups post-COVID and identify the 3 most impactful ADR improvement tactics. (2) Draft a direct booking acceleration plan including website, loyalty programme, and CRM outreach components. (3) Save to OneDrive as "Suria Direct Booking Strategy". (4) Email to the Chief Commercial Officer and VP Revenue Management for review. (5) Schedule a cross-property revenue management workshop for next month.',
            'Do all of the following for the retention programme: (1) Research salary benchmarks for hotel department heads and frontline roles in Malaysia, Indonesia, and Thailand — identify where Suria is most underpaying vs market. (2) Draft a 12-month retention programme rollout plan with quarterly milestones. (3) Calculate the total programme investment and ROI from reduced turnover costs. (4) Email to the CHRO asking for an urgent review of salary bands for the 4 most critical roles. (5) Schedule a retention taskforce kickoff meeting with all 14 GMs.'
          ]
        },
        {
          tool: '🤖 Word Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to a Word document. Open the .docx in Word for Web > Copilot pane > + New Agent > name it, write a description, set the document as knowledge source > Share. Colleagues chat with it in Teams or M365 Copilot.',
          prompts: [
            'Open 18_Zava_HR_Analytics.xlsx in Excel for Web. Create a Word summary document on HR policies for hospitality staff and open in Word for Web. Create an agent called "Suria HR & Operations Policy Bot". Description: "Answers questions from hotel GMs and department heads on Suria Hotels HR policies, staff benefits, retention programme details, F&B margin targets, and operational standards." Share with all 14 GMs.',
            'Demo: A Housekeeping Manager at Suria Hotel Bangkok asks "We have 6 housekeeping staff who have been with us for 3+ years. Are they eligible for the new retention bonus and when is the first payment date? Also, what training must they complete to be enrolled in the career development programme?" Show how the agent empowers managers to retain their team with instant policy answers.'
          ]
        },
        {
          tool: '🤖 PowerPoint Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to a PowerPoint presentation. Great for strategy decks or Board presentations many people need to reference. Same setup as Word Agent but using a .pptx file.',
          prompts: [
            'Create a PowerPoint from the Board recovery presentation. Create an agent called "Suria Hotels Performance Q&A Bot". Share with hotel owners and the Board.',
            'Demo: A hotel owner asks "My Penang property has the second-worst RevPAR gap in the portfolio. What specific actions is Suria implementing at my property to close the gap and by when should I expect RevPAR to reach the pre-COVID benchmark?" Show the agent providing a property-specific, data-grounded recovery plan.'
          ]
        },
        {
          tool: '🤖 Excel Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to an Excel workbook. Colleagues ask data questions in plain English without opening Excel. Open .xlsx in Excel for Web > Copilot pane > + New Agent > set workbook as knowledge source > share.',
          prompts: [
            'Open HT_01_Suria_Hotels_Resorts.xlsx in Excel for Web. Create an agent called "Suria Hotels Revenue & Operations Q&A". Description: "Instant answers on RevPAR, occupancy, ADR, F&B margin, and staff turnover across all 14 Suria properties for the CEO, CCO, and property GMs." Share with the revenue and operations leadership.',
            'Demo: Ask "Which 3 properties have the worst F&B margin and by how much are they below the 26% group target?" Then: "What is the total annual turnover cost across all 14 properties and which single property has the highest turnover-related cost?" Show the COO getting instant multi-property intelligence.'
          ]
        },
        {
          tool: '🏗 Agent Builder (Copilot Studio)',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Build a custom declarative agent in Copilot Studio — no coding required. Access: copilotstudio.microsoft.com > Create > New Agent. Add name, description, knowledge sources (SharePoint URLs or uploaded files), topics/actions. Publish to Teams in under 10 minutes.',
          prompts: [
            'Go to copilotstudio.microsoft.com > Create > New Agent. Name it "Suria Hotels Intelligence Agent". Description: "Supports Suria Hotels\' GMs, revenue managers, and Group leadership with instant answers on RevPAR performance, F&B margin improvement, retention programme details, OTA strategy, and operational benchmarks across all 14 properties — enabling faster, smarter hospitality management decisions." Upload HT_01_Suria_Hotels_Resorts.xlsx and 18_Zava_HR_Analytics.xlsx. Add topics: "Revenue Management", "F&B Operations", "Staff Retention", "Direct Booking". Publish to Teams.',
            'Demo the agent: A GM of the KL city hotel is preparing for a difficult owner call at 9am tomorrow. The property\'s RevPAR is MYR 22 below portfolio benchmark. At 8:45am the GM asks the agent: "Give me the 3 specific actions that will have the biggest RevPAR impact at my property in the next 90 days. Also tell me what our F&B margin gap is vs target and the 2 quickest wins to improve it. I need specific numbers, not general advice." Show how the agent empowers the GM to have a confident, data-backed owner conversation.'
          ]
        }
      ]
    },
    {
      id: 'construction',
      sectorId: 'construction',
      subsector: '',
      name: 'Construction',
      icon: '🏗',
      color: '#E65100',
      accent: '#F57C00',
      company: 'NusaBuild Group Berhad',
      tagline: 'LRT 3 delayed 14 weeks — CIDB Green Building certification + ESG tender scoring.',
      scenario: 'NusaBuild Group Berhad is Malaysia\'s 3rd largest civil and building contractor with a RM 8.4B order book. The LRT3 package is 14 weeks behind schedule due to ground condition variations. CIDB Green Building Index (GBI) certification is required for 6 upcoming government tenders. ESG scoring now forms 15% of government tender evaluation.',
      files: [
        '14_Zava_Properties_Portfolio.xlsx',
        '12_Zava_Manufacturing_KPIs.xlsx'
      ],
      prompts: [
        {
          tool: '🤖 Copilot Chat (Basic)',
          license: 'Free — no M365 Copilot license needed',
          account: 'Sasha Ouellet — SashaO@ABSx62256373.OnMicrosoft.com',
          desc: '',
          prompts: [
            'I am the CEO of Malaysia\'s 3rd largest construction company. Our LRT3 extension package is 14 weeks behind schedule due to ground condition variations — specifically, 3 pile cap locations encountered unexpected soft clay 8 metres deeper than the site investigation predicted. The JKR extension of time (EOT) application is in progress. Draft a 250-word brief for my Board explaining: (1) The grounds for a valid EOT claim under PAM 2018 contract, (2) What contractual evidence we need to support the claim, (3) The risk that JKR will grant a lesser EOT and we will face liquidated damages of RM 180,000 per week for the remaining 14 weeks.',
            'What is the CIDB Green Building Index (GBI) in Malaysia? What are the 6 scoring categories, what score is required for GBI certification, and what specific construction practices and materials must be changed to achieve GBI certification vs conventional building?',
            'How is ESG scoring being incorporated into government construction tenders in Malaysia? What types of ESG evidence do JKR and CIDB evaluate, what weight do they carry in the tender score, and which ESG certifications give the most points?'
          ]
        },
        {
          tool: '🔍 Researcher',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via Microsoft 365 Copilot Chat (copilot.microsoft.com or Teams) > click Agents > Researcher. Grounds answers in live web sources and your organisation data with full citations.',
          prompts: [
            'Research the Malaysian construction industry outlook for 2025–2027. I need: (1) Total value of government infrastructure projects in the pipeline, (2) Key competitive dynamics — who are the top contractors and how are they positioned for upcoming tenders, (3) Impact of rising steel, concrete, and labour costs on contractor margins, (4) Government\'s ESG requirements in tender evaluation. Cite official CIDB, JKR, or MITI sources.',
            'Research the LRT and MRT extension projects in Malaysia — current status, contractor packages, any delays or cost overruns reported publicly, and how the government has managed extension of time claims historically. Cite news sources and official project announcements.'
          ]
        },
        {
          tool: '📊 Analyst',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via Microsoft 365 Copilot Chat > click Agents > Analyst. Upload an Excel or CSV file. Analyst runs Python-style analysis, builds charts, and interprets results without you writing a single formula.',
          prompts: [
            'Upload 12_Zava_Manufacturing_KPIs.xlsx (use as project KPI proxy). Ask Analyst: Model the financial impact of the LRT3 delay. Inputs: 14 weeks behind schedule, RM 180,000/week liquidated damages, EOT application filed for 14 weeks (outcome uncertain — 3 scenarios: full grant, 8 weeks granted, 0 weeks granted). For each scenario, calculate: (1) Total LD exposure, (2) Cash flow impact — assuming RM 4.2M per week of construction revenue that is delayed, (3) Impact on contract margin. Show as a scenario table with traffic light status.',
            'Upload 12_Zava_Manufacturing_KPIs.xlsx. Ask: Build a tender pipeline analysis. NusaBuild is targeting 12 government tenders in FY2026 totalling RM 5.8B. ESG scoring is 15% of evaluation. Our current ESG score is estimated at 62 out of 100 vs the estimated winning bid score of 78+. Calculate: if we improve ESG score from 62 to 82 (above winning threshold), what is the increase in probability of winning each tender? What is the expected value of tenders won at each ESG score level?'
          ]
        },
        {
          tool: '📊 Copilot in Excel',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open 12_Zava_Manufacturing_KPIs.xlsx. Navigate to the Capex Tracker sheet (use as project tracker proxy). Ask Copilot: Build a construction project delay dashboard on a new sheet. For each of NusaBuild\'s 8 active projects, show: (1) Project name and client, (2) Contract value (RM M), (3) Planned completion date, (4) Current forecast completion date, (5) Delay (weeks), (6) EOT filed (Y/N), (7) LD rate (RM/week), (8) Current LD exposure (RM M), (9) Status (On Track / Watch / Critical). Sort by LD exposure, highest first.',
            'Ask Copilot: Create a GBI certification gap analysis on a new sheet. For each of the 6 criteria (Energy Efficiency, Indoor Environment Quality, Sustainable Site Planning, Materials & Resources, Water Efficiency, Innovation), show: (1) Current score estimate, (2) Required score for GBI certification, (3) Gap, (4) Specific interventions needed, (5) Cost of intervention (RM M), (6) Timeline to implement.',
            'Ask Copilot: Build a tender ESG scoring improvement tracker. For each of the 12 upcoming tenders, show: (1) Tender name and value (RM M), (2) ESG weight in tender evaluation (%), (3) Our current estimated ESG score, (4) Target ESG score, (5) Improvement actions required, (6) Expected score after improvement, (7) Estimated increase in winning probability.'
          ]
        },
        {
          tool: '📝 Copilot in Word',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Ask Copilot in Word: Draft the Extension of Time (EOT) claim narrative for the LRT3 contract. The narrative should: describe the ground condition variation (soft clay encountered 8m deeper than SI data), provide the 3 pile cap locations affected, calculate the delay to critical path activities, demonstrate that NusaBuild took all reasonable mitigation steps, and quantify the 14-week extension required. Reference the relevant PAM 2018 contract clauses. Attach as supporting narrative to the formal EOT application.',
            'Ask Copilot: Draft a GBI certification action plan document. For each of the 6 GBI scoring categories, provide: current practice at NusaBuild, the change required for GBI certification, responsible department, investment required, and timeline. Set the goal of achieving GBI Silver (minimum 50 points) on all 6 upcoming government tenders. 8 pages, formal document format.',
            'Ask Copilot: Write an ESG performance section for NusaBuild\'s Bursa Malaysia sustainability report. Cover: (1) Green construction certifications obtained FY2024 (list projects), (2) Carbon intensity per RM M of contract value, (3) Construction waste diversion rate (target: 80% diversion from landfill), (4) Worker safety TRIR score and how it compares to CIDB benchmark, (5) Local subcontractor and supplier spend %. Follow GRI 302, 305, 403, and 413 standards.'
          ]
        },
        {
          tool: '🎯 Copilot in PowerPoint',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Ask Copilot in PowerPoint: Create a 10-slide business development presentation for NusaBuild targeting JKR procurement officers. Include: (1) NusaBuild overview — RM 8.4B order book, track record, (2) ESG leadership — GBI certification, carbon intensity reduction, (3) Safety — TRIR of 0.8 vs industry benchmark, (4) LRT3 experience — project management, (5) Digital construction — BIM, digital site monitoring, (6) Local and Bumiputera content, (7) ESG tender scoring credentials, (8) Current project portfolio, (9) Management team, (10) Why NusaBuild. Dark orange and grey colour scheme.',
            'Ask Copilot: Create a 3-slide LRT3 delay briefing for the Board. Slide 1: Delay status — 14 weeks, EOT filed, current LD exposure. Slide 2: Three EOT outcome scenarios and their financial impact. Slide 3: Mitigation actions — acceleration plan, cost absorption vs recovery.',
            'Ask Copilot: Create a 2-slide GBI certification journey slide for a tender submission. Slide 1: Our GBI score vs certification target by category (radar chart). Slide 2: The specific green construction initiatives we are implementing for this tender.'
          ]
        },
        {
          tool: '📧 Copilot in Outlook',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Ask Copilot in Outlook: Draft a letter to JKR\'s Project Director formally submitting the Extension of Time claim for the LRT3 package. The letter should: reference the contract number and package, state the basis of the claim (ground condition variation under Clause 23 of PAM 2018), summarise the delay impact, request 14 weeks EOT, and attach the supporting narrative. Use formal JKR correspondence format.',
            'Ask Copilot: Draft an email to the CIDB GBI certification office requesting a pre-assessment consultation for 6 upcoming NusaBuild projects. The email should: introduce NusaBuild\'s intention to pursue GBI certification, describe the project types (3 government offices, 2 hospitals, 1 university), ask about the pre-assessment process and timeline, and request a meeting within 3 weeks.',
            'Ask Copilot: Draft an internal email from the CEO to all Project Directors announcing the mandatory GBI certification requirement for all new tenders above RM 50M effective from Q3 FY2025. The email should explain why (ESG tender scoring), what is required from each project team, and the training programme being arranged.'
          ]
        },
        {
          tool: '🎙 Copilot in Teams',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Use your OWN existing recorded Teams meetings. Open a meeting recap in Teams > Recap tab. Copilot generates summaries, action items, and follow-up drafts grounded in the actual transcript.',
          prompts: [
            'Open an existing recorded Teams meeting recap from a project or site management meeting. Ask Copilot: Identify all project delay issues discussed, their root cause, and the actions taken. Flag any project with LD risk and note whether an EOT has been filed.',
            'Ask Copilot: Draft follow-up actions from the LRT3 delay review meeting. Group by workstream: EOT Claim | Acceleration Plan | Subcontractor Engagement | Client Communication | Cost Recovery. Include owner and deadline.',
            'Ask Copilot: Were there any discussions about subcontractor performance impacting the LRT3 delay? Identify which subcontractors were mentioned and what contractual actions were proposed against them.'
          ]
        },
        {
          tool: '📓 Copilot Notebook',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via copilot.microsoft.com > Notebook tab. Upload up to 5 files and set a system instruction. Best for synthesising insights across multiple documents simultaneously.',
          prompts: [
            'Upload 14_Zava_Properties_Portfolio.xlsx and 12_Zava_Manufacturing_KPIs.xlsx to Copilot Notebook. Set instruction: "You are a construction contract specialist advising NusaBuild on the LRT3 EOT claim." Ask: Based on the project data and Malaysian construction contract norms (PAM 2018), what is the strongest and weakest element of our EOT claim? What additional evidence should we gather in the next 2 weeks to strengthen the claim?',
            'Upload 12_Zava_Manufacturing_KPIs.xlsx. Ask: NusaBuild is considering an acceleration plan to recover 8 of the 14 delayed weeks. The plan involves adding 2 additional tower crane shifts per day (RM 85,000/week additional cost) and extending working hours to Sundays (15% labour premium). Calculate: (1) Total acceleration cost for 8 weeks, (2) Whether the acceleration saves more in avoided LD than it costs, (3) The break-even point — how many weeks of LD must be avoided to justify the acceleration cost.'
          ]
        },
        {
          tool: '🤝 Cowork (Frontier)',
          license: 'M365 Copilot + Frontier Program',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Cowork is an autonomous agent that takes actions across Microsoft 365 on your behalf — sending emails, scheduling meetings, creating documents, posting in Teams, and scheduling recurring tasks. Access: m365.cloud.microsoft > left nav > Agents > Cowork. Requires Frontier program enrollment.',
          prompts: [
            'Do all of the following: (1) Research PAM 2018 clauses related to ground condition variations and EOT entitlement — provide the specific clause numbers and the key requirements for a valid claim. (2) Draft a 5-page EOT claim narrative for the LRT3 ground condition variation including all required elements under PAM 2018. (3) Save to OneDrive as "LRT3 EOT Claim Narrative - CONFIDENTIAL". (4) Email to the contracts manager and external legal advisor requesting review within 3 days. (5) Schedule an EOT claim strategy meeting with the legal and contracts team for this week.',
            'Do all of the following for the GBI certification programme: (1) Research the specific CIDB GBI assessment criteria and scoring methodology for commercial and government buildings. (2) Identify the top 5 highest-scoring interventions that NusaBuild can implement immediately (before construction start) to maximise our GBI score across all 6 projects. (3) Create a GBI certification project plan covering all 6 tenders with timelines and cost estimates. (4) Email to the Head of Engineering and HSE Manager asking for review. (5) Book a GBI certification workshop for all Project Directors next month.'
          ]
        },
        {
          tool: '🤖 Word Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to a Word document. Open the .docx in Word for Web > Copilot pane > + New Agent > name it, write a description, set the document as knowledge source > Share. Colleagues chat with it in Teams or M365 Copilot.',
          prompts: [
            'Open the GBI certification action plan document in Word for Web. Create an agent called "NusaBuild Green Building & Compliance Bot". Description: "Answers questions from Project Directors and engineers on GBI certification requirements, PAM 2018 contract clauses, ESG tender scoring criteria, and CIDB safety regulations." Share with all Project Directors.',
            'Demo: A site engineer asks "Our hospital project requires GBI Silver. We are currently at 42 points — 8 short of the 50 required. We have budget for 2 more interventions. What are the highest-scoring GBI interventions we can realistically implement on a running hospital construction site within 90 days?" Show the agent providing specific, score-maximising technical guidance.'
          ]
        },
        {
          tool: '🤖 PowerPoint Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to a PowerPoint presentation. Great for strategy decks or Board presentations many people need to reference. Same setup as Word Agent but using a .pptx file.',
          prompts: [
            'Create a PowerPoint from the business development presentation. Create an agent called "NusaBuild Tender Q&A Bot". Share with the business development and tender teams.',
            'Demo: A business development manager is preparing a tender submission and asks "For this JKR government hospital tender, our ESG score is 64 and we estimate the winning threshold is 78. What are the 3 highest-value ESG credentials we can add to our submission that we already have documented?" Show the agent helping win more tenders.'
          ]
        },
        {
          tool: '🤖 Excel Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to an Excel workbook. Colleagues ask data questions in plain English without opening Excel. Open .xlsx in Excel for Web > Copilot pane > + New Agent > set workbook as knowledge source > share.',
          prompts: [
            'Open 12_Zava_Manufacturing_KPIs.xlsx in Excel for Web. Create an agent called "NusaBuild Project Performance Q&A". Description: "Instant answers on project delay status, LD exposure, GBI certification progress, and tender pipeline for the CEO and project directors." Share with the NusaBuild leadership team.',
            'Demo: Ask "What is our total current LD exposure across all 8 active projects and which 2 projects have the highest risk?" Then: "Across our 12 upcoming tenders, what is the total value at risk if our ESG score stays at 62 vs improves to 82?" Show the CEO getting instant project and commercial intelligence.'
          ]
        },
        {
          tool: '🏗 Agent Builder (Copilot Studio)',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Build a custom declarative agent in Copilot Studio — no coding required. Access: copilotstudio.microsoft.com > Create > New Agent. Add name, description, knowledge sources (SharePoint URLs or uploaded files), topics/actions. Publish to Teams in under 10 minutes.',
          prompts: [
            'Go to copilotstudio.microsoft.com > Create > New Agent. Name it "NusaBuild Construction Intelligence Agent". Description: "Supports NusaBuild\'s CEO, project directors, and tender teams with instant answers on project delay status, contract entitlements, GBI certification requirements, ESG tender scoring, and Malaysian construction regulations — enabling faster, smarter project and commercial decisions." Upload 14_Zava_Properties_Portfolio.xlsx and 12_Zava_Manufacturing_KPIs.xlsx. Add topics: "Project Delays & EOT", "GBI Certification", "ESG Tender Scoring", "Contract Management". Publish to Teams.',
            'Demo the agent: The CEO is called into an urgent JKR project review meeting with 15 minutes notice. On the way, the CEO asks the agent: "Give me the LRT3 delay status in 3 sentences, our current LD exposure if EOT is granted for only 8 of 14 weeks, and the 2 strongest contractual arguments for the remaining 6 weeks. Also — are there any other active projects where we have an unacknowledged delay risk that JKR might raise today?" Show how the agent prepares the CEO instantly for a high-pressure government client meeting.'
          ]
        }
      ]
    },
    {
      id: 'aviation-airports',
      sectorId: 'aviation',
      subsector: '',
      name: 'Aviation & Airports',
      icon: '✈️',
      color: '#01579B',
      accent: '#0277BD',
      company: 'MAHB / Airport Operator',
      tagline: '73.4M pax FY2024 — KLIA2 MYR 2.8B expansion + aeronautical charge regulatory review.',
      scenario: 'Malaysia Airports Holdings Berhad (MAHB) manages 39 airports including KLIA. FY2024 passenger throughput was 73.4M — 94% of pre-COVID levels. KLIA2 is undergoing a MYR 2.8B capacity expansion. A regulatory review of aeronautical charges is due by MAVCOM in Q3 FY2025, which will affect airline relationships and airport revenue.',
      files: [
        '01_Zava_Group_Financial_Performance.xlsx',
        '03_Zava_Group_Strategy_Framework.docx'
      ],
      prompts: [
        {
          tool: '🤖 Copilot Chat (Basic)',
          license: 'Free — no M365 Copilot license needed',
          account: 'Sasha Ouellet — SashaO@ABSx62256373.OnMicrosoft.com',
          desc: '',
          prompts: [
            'I am the CFO of a major airport group. Our aeronautical charges — passenger service charges (PSC) and landing fees — are under regulatory review by MAVCOM. Airlines are lobbying for a freeze or reduction. Our airport is investing MYR 2.8B in capacity expansion at Terminal 2. Draft a 250-word submission summary for the MAVCOM regulatory review. Cover: (1) The cost base justifying a CPI+ increase in aeronautical charges, (2) The return on invested capital framework for regulated airport assets and why the MYR 2.8B capex must be reflected in the charge base, (3) The precedent from comparable airport regulatory determinations in Singapore (Changi) or Sydney.',
            'Explain the dual-till vs single-till regulatory model for airports. What is the difference, which model favours the airport vs the airline, and which model does Malaysia use? What would switching from single-till to dual-till mean for MAHB\'s aeronautical revenue?',
            'What are the key performance indicators for an international airport that MAVCOM or comparable regulators typically monitor? How are passenger satisfaction, flight punctuality, terminal cleanliness, and retail revenue used to evaluate an airport\'s operational performance?'
          ]
        },
        {
          tool: '🔍 Researcher',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via Microsoft 365 Copilot Chat (copilot.microsoft.com or Teams) > click Agents > Researcher. Grounds answers in live web sources and your organisation data with full citations.',
          prompts: [
            'Research international airport regulatory frameworks — specifically how aeronautical charges are set for airports of comparable size to KLIA (60–80M passengers per year). I need: (1) How Changi Airport, Dubai International, and Heathrow structure their regulatory charge frameworks, (2) The typical WACC (weighted average cost of capital) used in airport regulatory determinations, (3) How capacity expansion capex is treated in the regulated asset base. Cite regulatory decisions and academic sources.',
            'Research the Malaysia aviation market recovery in 2024–2025. I need: (1) Passenger volume recovery by route type (domestic, ASEAN, international), (2) The top 10 airlines by passenger volume at KLIA and KLIA2, (3) Any new route announcements or airline capacity additions, (4) Budget airline growth vs full service at Malaysian airports. Cite MAVCOM, MAHB, or ACI sources.'
          ]
        },
        {
          tool: '📊 Analyst',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via Microsoft 365 Copilot Chat > click Agents > Analyst. Upload an Excel or CSV file. Analyst runs Python-style analysis, builds charts, and interprets results without you writing a single formula.',
          prompts: [
            'Upload 01_Zava_Group_Financial_Performance.xlsx to Analyst (use as financial data proxy). Ask: Model the KLIA2 expansion financial impact. Investment: MYR 2.8B over 4 years. Capacity expansion: from 45M pax per year to 60M pax. Aeronautical revenue per pax: MYR 52 (current). Calculate: (1) Revenue increase from additional 15M pax capacity at full utilisation, (2) Additional depreciation and financing cost from MYR 2.8B capex, (3) EBITDA impact — net of revenue gain and additional costs, (4) Return on invested capital (ROIC) at 70% and 85% utilisation of new capacity, (5) Payback period.',
            'Upload 01_Zava_Group_Financial_Performance.xlsx. Ask: Build a passenger revenue sensitivity model. X-axis: passenger volume (60M to 85M per year in 5M steps). Y-axis: aeronautical charge per pax (MYR 48, 52, 56, 60, 64 — from regulatory freeze to 23% increase). For each cell, calculate total aeronautical revenue. Highlight the cell matching our current position and the target revenue needed to fund the capex at our WACC of 7.8%.'
          ]
        },
        {
          tool: '📊 Copilot in Excel',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open 01_Zava_Group_Financial_Performance.xlsx. Navigate to the revenue sheet. Ask Copilot: Build an airport revenue dashboard on a new sheet. Show monthly data for the past 12 months: (1) Passenger throughput (M pax), (2) Aeronautical revenue (RM M), (3) Non-aeronautical revenue — retail, F&B, car park (RM M), (4) Revenue per passenger (RM), (5) Passenger service charge collected (RM M). Calculate the non-aeronautical revenue as % of total — the target is 40%.',
            'Ask Copilot: Build a MAVCOM regulatory submission financial model. Show: (1) Our current aeronautical charge per pax (RM 52), (2) Our total regulated cost base for FY2024, (3) The WACC calculation at 7.8%, (4) The revenue requirement to cover all costs and earn the WACC return, (5) The required charge per pax to meet the revenue requirement. Compare to the airline lobby position (freeze at RM 52) and our proposal (increase to RM 64). Show the gap.',
            'Ask Copilot: Create an airline performance scorecard on a new sheet. For the top 20 airlines at KLIA/KLIA2, show: (1) Annual passenger volume, (2) On-time performance rate (%), (3) Average load factor (%), (4) Net PSC collected (RM M), (5) Any outstanding payment disputes. Sort by passenger volume. Highlight airlines with OTP below 80% in amber and outstanding payment disputes in red.'
          ]
        },
        {
          tool: '📝 Copilot in Word',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open 03_Zava_Group_Strategy_Framework.docx. Ask Copilot: Draft the MAVCOM regulatory submission for the aeronautical charge review. The submission should cover: (1) Business overview and FY2024 performance, (2) The MYR 2.8B KLIA2 expansion rationale — capacity, connectivity, and passenger experience, (3) The regulated cost base — RM 4.2B total assets, (4) WACC calculation and the required return, (5) The proposed aeronautical charge per pax for the next regulatory period (2026–2029), (6) Response to airline objections — service quality improvements justifying the increase. 15 pages, formal regulatory submission format.',
            'Ask Copilot: Draft a stakeholder communication plan for the MAVCOM charge review process. Identify: (1) Key stakeholders — airlines, MAVCOM, Ministry of Transport, tourism associations, (2) Key messages for each stakeholder, (3) Communication channels and timeline, (4) How to address airline media campaigns opposing the charge increase. Format as a 3-page communication plan.',
            'Ask Copilot: Write a KLIA2 expansion project brief for the Ministry of Transport\'s Cabinet presentation. Cover: (1) Current capacity constraint — 73.4M pax, terminal operating at 98% during peak hours, (2) Expansion scope — 15M pax additional capacity, international terminal extension, landside development, (3) Investment — MYR 2.8B, funding via government grant MYR 1.0B and own funds MYR 1.8B, (4) Timeline — completion by Q4 2028, (5) Economic impact — direct and induced, (6) Decision required: Cabinet approval for funding commitment.'
          ]
        },
        {
          tool: '🎯 Copilot in PowerPoint',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Ask Copilot in PowerPoint: Create a 12-slide MAVCOM regulatory submission presentation. Include: (1) MAHB business overview — 39 airports, 73.4M pax, (2) FY2024 financial performance, (3) KLIA2 expansion — scope, rationale, investment, (4) Regulated asset base — cost base justification, (5) WACC calculation — 7.8% and the regulated return requirement, (6) Proposed aeronautical charge increase — from RM 52 to RM 64 per pax, (7) Service quality commitments — OTP, passenger satisfaction, (8) Response to airline objections, (9) Comparable international airport charges, (10) Economic contribution of MAHB to Malaysia, (11) Sensitivity analysis, (12) Regulatory determination requested. Dark navy and blue colour scheme.',
            'Ask Copilot: Create a passenger experience slide showing our key service quality investments in the KLIA2 expansion: new check-in hall, additional immigration lanes (immigration clearance reduced from 45 to 22 minutes), expanded retail and F&B, smart parking. Use a "Before and After 2028" visual format.',
            'Ask Copilot: Create a competitive benchmarking slide showing aeronautical charges per passenger at 10 comparable international airports: Changi, Suvarnabhumi, NAIA, CTICC, Schiphol, Heathrow, Dubai, KLIA (current), KLIA (proposed). Show KLIA proposed charge is still 28% below the Asian regional average.'
          ]
        },
        {
          tool: '📧 Copilot in Outlook',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Ask Copilot in Outlook: Draft a letter to MAVCOM formally submitting the aeronautical charge review submission. The letter should: confirm the submission, highlight the 3 key points of our case, note our willingness to engage in the public consultation process, and request a bilateral meeting with MAVCOM commissioners before the final determination. Formal regulatory submission format.',
            'Ask Copilot: Draft an email to the CEOs of the top 5 airlines at KLIA (by passenger volume) ahead of the MAVCOM charge review. The email should: acknowledge their concerns about the proposed charge increase, explain the investment rationale (KLIA2 expansion), offer a phased charge increase over 3 years rather than immediate, and propose a bilateral meeting to discuss the transition plan. Diplomatic but firm commercial tone.',
            'Ask Copilot: Draft a press release response to a negative airline industry body media statement claiming our proposed charge increase will increase airfare by RM 18 per ticket and harm Malaysian tourism competitiveness. The response should: correct the claim (PSC is absorbed by airlines, not automatically passed to passengers), explain the investment rationale, note our charges remain below regional averages, and invite media to a briefing on the KLIA2 expansion.'
          ]
        },
        {
          tool: '🎙 Copilot in Teams',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Use your OWN existing recorded Teams meetings. Open a meeting recap in Teams > Recap tab. Copilot generates summaries, action items, and follow-up drafts grounded in the actual transcript.',
          prompts: [
            'Open an existing recorded Teams meeting recap from a regulatory or stakeholder meeting. Ask Copilot: Identify all MAVCOM regulatory issues discussed, the airlines\' objections, and the agreed response strategy. Create an action log for the regulatory submission team.',
            'Ask Copilot: Draft follow-up actions from the aeronautical charge review strategy meeting. Group by workstream: Regulatory Submission | Airline Engagement | Media & Communications | Legal | Financial Modelling. Include owner and deadline.',
            'Ask Copilot: Were there any internal concerns raised about the financial sustainability of the MYR 2.8B expansion if MAVCOM does not approve the charge increase? Summarise the risk and the contingency discussed.'
          ]
        },
        {
          tool: '📓 Copilot Notebook',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via copilot.microsoft.com > Notebook tab. Upload up to 5 files and set a system instruction. Best for synthesising insights across multiple documents simultaneously.',
          prompts: [
            'Upload 01_Zava_Group_Financial_Performance.xlsx and 03_Zava_Group_Strategy_Framework.docx to Copilot Notebook. Set instruction: "You are a regulatory economics advisor helping MAHB prepare its aeronautical charge submission to MAVCOM." Ask: Based on the financial data and strategy, what is the minimum charge increase needed to fund the KLIA2 expansion at our WACC? What happens to our dividend capacity if MAVCOM denies the increase?',
            'Upload 03_Zava_Group_Strategy_Framework.docx. Ask: Airlines are threatening to reduce capacity at KLIA if charges increase. This would be a commercial own-goal for Malaysia tourism. Design a stakeholder engagement strategy that reframes the charge increase as a shared investment in Malaysia\'s aviation competitiveness — identify 3 allies who would support our case (tourism associations, cargo industry, business council) and what message each should deliver.'
          ]
        },
        {
          tool: '🤝 Cowork (Frontier)',
          license: 'M365 Copilot + Frontier Program',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Cowork is an autonomous agent that takes actions across Microsoft 365 on your behalf — sending emails, scheduling meetings, creating documents, posting in Teams, and scheduling recurring tasks. Access: m365.cloud.microsoft > left nav > Agents > Cowork. Requires Frontier program enrollment.',
          prompts: [
            'Do all of the following: (1) Research aeronautical charge determination decisions by airport regulators in Singapore, Australia, and the UK in the past 3 years and extract the key precedents that support a charge increase for capacity expansion investment. (2) Draft a 3-page regulatory precedent summary for our MAVCOM submission. (3) Save to OneDrive as "Regulatory Precedent Summary". (4) Email to the Regulatory Affairs Director and external legal counsel for review. (5) Schedule a regulatory submission review meeting with all workstream leaders.',
            'Do all of the following for airline stakeholder management: (1) Research publicly available statements by AirAsia, Malaysia Airlines, and Batik Air on MAVCOM charge reviews. (2) Draft a bilateral engagement proposal for each of the top 5 airlines — customised to each airline\'s specific concerns. (3) Email each draft to the VP Commercial Airports for review before sending. (4) Schedule bilateral meetings with airline CEOs over the next 3 weeks. (5) Post a MAVCOM submission update in the internal #regulatory-affairs Teams channel.'
          ]
        },
        {
          tool: '🤖 Word Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to a Word document. Open the .docx in Word for Web > Copilot pane > + New Agent > name it, write a description, set the document as knowledge source > Share. Colleagues chat with it in Teams or M365 Copilot.',
          prompts: [
            'Open 03_Zava_Group_Strategy_Framework.docx in Word for Web. Create an agent called "MAHB Regulatory & Strategy Bot". Description: "Answers questions from MAHB\'s regulatory, commercial, and finance teams on MAVCOM charge framework, KLIA2 expansion milestones, airline contractual terms, and airport regulatory precedents." Share with the regulatory and commercial teams.',
            'Demo: A regulatory analyst asks "What is the single most important precedent from another airport regulatory determination that we should cite in our MAVCOM submission to justify including the full MYR 2.8B KLIA2 capex in the regulated asset base?" Show the agent providing a regulation-grounded, evidence-based answer.'
          ]
        },
        {
          tool: '🤖 PowerPoint Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to a PowerPoint presentation. Great for strategy decks or Board presentations many people need to reference. Same setup as Word Agent but using a .pptx file.',
          prompts: [
            'Create a PowerPoint from the MAVCOM submission presentation. Create an agent called "MAHB Regulatory Submission Q&A Bot". Share with the MAVCOM submission team and external advisors.',
            'Demo: A MAVCOM commissioner (playing devil\'s advocate) asks "Your WACC of 7.8% is 1.2 percentage points above the Changi Airport determination — why should Malaysian passengers fund a higher return for MAHB than Singapore passengers fund for Changi?" Show the agent providing a technically-grounded regulatory economics response.'
          ]
        },
        {
          tool: '🤖 Excel Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to an Excel workbook. Colleagues ask data questions in plain English without opening Excel. Open .xlsx in Excel for Web > Copilot pane > + New Agent > set workbook as knowledge source > share.',
          prompts: [
            'Open 01_Zava_Group_Financial_Performance.xlsx in Excel for Web. Create an agent called "MAHB Financial Performance Q&A". Description: "Instant answers on passenger volumes, aeronautical revenue, non-aeronautical revenue, KLIA2 capex progress, and regulatory financial modelling for the CFO and regulatory team." Share with the finance and regulatory leadership.',
            'Demo: Ask "What is our current non-aeronautical revenue as a % of total and how does that compare to the 40% target?" Then: "If MAVCOM approves a charge increase to RM 60 (not our proposed RM 64) and KLIA2 reaches 90% utilisation by 2029, what is the ROIC and does it cover our WACC of 7.8%?" Show the CFO getting instant regulatory economics intelligence.'
          ]
        },
        {
          tool: '🏗 Agent Builder (Copilot Studio)',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Build a custom declarative agent in Copilot Studio — no coding required. Access: copilotstudio.microsoft.com > Create > New Agent. Add name, description, knowledge sources (SharePoint URLs or uploaded files), topics/actions. Publish to Teams in under 10 minutes.',
          prompts: [
            'Go to copilotstudio.microsoft.com > Create > New Agent. Name it "MAHB Airports Intelligence Agent". Description: "Supports MAHB\'s regulatory, commercial, finance, and operations teams with instant answers on aeronautical charge frameworks, KLIA2 expansion status, airline performance, passenger volume trends, and regulatory precedents — enabling faster, smarter airport management decisions." Upload 01_Zava_Group_Financial_Performance.xlsx and 03_Zava_Group_Strategy_Framework.docx. Add topics: "MAVCOM Regulatory Review", "KLIA2 Expansion", "Airline Relations", "Passenger Performance". Publish to Teams.',
            'Demo the agent: The Group CEO is called into an unscheduled meeting with the Minister of Transport in 20 minutes. The Minister has seen media reports that the aeronautical charge increase will raise airfares and hurt tourism. The CEO asks the agent: "Give me 3 facts that prove our proposed charge increase will NOT increase passenger airfares, 2 data points showing our charges are still below regional competitors even at RM 64, and tell me how many jobs the KLIA2 expansion will create — I need all of this in 90 seconds." Show how the agent prepares the CEO for a high-pressure ministerial meeting.'
          ]
        }
      ]
    },
    {
      id: 'retail-grocery',
      sectorId: 'retail',
      subsector: '',
      name: 'Retail & Grocery',
      icon: '🛒',
      color: '#2E7D32',
      accent: '#388E3C',
      company: 'BrightMart Group',
      tagline: '148 stores — private label 34% mix target + supply chain shrinkage 2.1% issue.',
      scenario: 'BrightMart Group operates 148 grocery stores across Peninsular Malaysia with MYR 4.2B annual gross merchandising value. Private label products are 28% of sales vs a 34% target. Supply chain shrinkage is 2.1% — double the 1.0% industry benchmark. A fresh food expansion is adding 18 stores in FY2025.',
      files: [
        'RT_01_BrightMart_Group.xlsx',
        'RT_02_BrightMart_Strategy.docx'
      ],
      prompts: [
        {
          tool: '🤖 Copilot Chat (Basic)',
          license: 'Free — no M365 Copilot license needed',
          account: 'Sasha Ouellet — SashaO@ABSx62256373.OnMicrosoft.com',
          desc: '',
          prompts: [
            'I am the CEO of a Malaysian grocery chain with 148 stores and MYR 4.2B GMV. Our supply chain shrinkage is 2.1% vs a 1.0% industry benchmark — representing MYR 46M in annual losses (theft, spoilage, administrative errors). Draft a 250-word shrinkage reduction brief for my operations team. Cover: (1) The 3 main categories of shrinkage and their typical proportion of total losses, (2) The highest-ROI technology investment to reduce shrinkage in a supermarket context (RFID, CCTV analytics, shelf sensors), (3) What a 0.5 percentage point shrinkage reduction would mean in MYR annual savings at our scale.',
            'What is the business case for increasing private label (own brand) products in a supermarket chain? What are the typical gross margin advantages of private label vs national brand equivalents, what percentage is industry best practice, and what investment is required to develop and quality-control a robust private label range?',
            'Explain the Retailer-Supplier joint business planning process — how large grocery retailers typically negotiate annual trade terms with FMCG suppliers, what a promotional calendar looks like, and how listing fees, shelf placement, and promotional spend are structured.'
          ]
        },
        {
          tool: '🔍 Researcher',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via Microsoft 365 Copilot Chat (copilot.microsoft.com or Teams) > click Agents > Researcher. Grounds answers in live web sources and your organisation data with full citations.',
          prompts: [
            'Research the Malaysian grocery retail market in 2024–2025. I need: (1) Market size and growth rate — total grocery retail GMV, (2) Key competitive dynamics — Lotus\'s, Giant, Jaya Grocer, AEON, and the rise of convenience stores and online grocery, (3) Consumer trends — health, halal, local brands, (4) Private label penetration rate in Malaysia vs regional benchmarks. Cite Nielsen, Kantar, or Euromonitor sources.',
            'Research supply chain shrinkage reduction technologies and best practices for grocery retailers. What specific technologies (RFID, computer vision at self-checkout, AI demand forecasting) have delivered the best ROI for mid-size grocery chains? Cite case studies with quantified results.'
          ]
        },
        {
          tool: '📊 Analyst',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via Microsoft 365 Copilot Chat > click Agents > Analyst. Upload an Excel or CSV file. Analyst runs Python-style analysis, builds charts, and interprets results without you writing a single formula.',
          prompts: [
            'Upload RT_01_BrightMart_Group.xlsx to Analyst. Ask: Analyse the shrinkage data by store category (large hypermarket, supermarket, neighbourhood store) and by product category (fresh food, dry grocery, health & beauty, general merchandise). Which combination of store type and product category has the highest shrinkage rate? Create a heat map: store type on X-axis, product category on Y-axis, shrinkage rate in each cell. Identify the top 5 highest-shrinkage cells — these are our priority intervention areas.',
            'Upload RT_01_BrightMart_Group.xlsx. Ask: Build a private label expansion ROI model. Current private label GMV: MYR 1.18B (28% of MYR 4.2B GMV). Target: MYR 1.43B (34% mix). Average private label gross margin: 42% vs national brand equivalent 28%. Calculate: (1) Additional GMV from increasing mix to 34%, (2) Gross margin uplift from shifting GMV from national brands to private label, (3) Required investment in private label development (product design, quality testing, packaging). Calculate payback period.'
          ]
        },
        {
          tool: '📊 Copilot in Excel',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open RT_01_BrightMart_Group.xlsx. Navigate to the Store Performance sheet. Ask Copilot: Build a shrinkage tracker dashboard on a new sheet. For each of the 148 stores, show: (1) Store name and region, (2) Monthly GMV (RM M), (3) Shrinkage amount (RM M), (4) Shrinkage rate %, (5) Category contributing most to shrinkage, (6) Last security audit date. Highlight stores with shrinkage above 2.5% in red, 1.5–2.5% in amber, below 1.0% in green. Sort by shrinkage rate, highest first. Show top 10 worst stores.',
            'Ask Copilot: Create a private label performance dashboard on a new sheet. For each private label category (bread & bakery, dairy, household cleaners, personal care, frozen food, snacks), show: (1) Current GMV (RM M), (2) % of category GMV, (3) Gross margin %, (4) YoY GMV growth, (5) Target mix %, (6) Gap to target (RM M). Calculate total uplift if all categories reach their target mix.',
            'Ask Copilot: Build a fresh food expansion tracker for the 18 new stores being opened in FY2025. For each store, show: (1) Location and planned opening date, (2) Fresh food selling area (sq m), (3) Fresh food categories planned (produce, meat, seafood, bakery, deli), (4) Target daily fresh food sales (RM), (5) Supplier partnerships confirmed, (6) Cold chain infrastructure status. Flag any store where cold chain is not yet confirmed 30 days before opening.'
          ]
        },
        {
          tool: '📝 Copilot in Word',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open RT_02_BrightMart_Strategy.docx. Ask Copilot: Draft a shrinkage reduction action plan document. Cover: (1) Executive summary — MYR 46M annual loss, target to halve shrinkage to 1.0% in 18 months, (2) Root cause analysis — theft (external and internal) 45%, fresh food spoilage 35%, administrative errors 20%, (3) Technology intervention — CCTV analytics at high-shrinkage stores (investment RM 12M), improved inventory cycle counting system, (4) Process improvements — staff accountability programme, fresh food markdown policy, (5) Supplier accountability — invoice reconciliation process, (6) 18-month implementation timeline. 8 pages, formal action plan format.',
            'Ask Copilot: Draft a supplier joint business plan template for BrightMart\'s top 50 FMCG suppliers. The template should cover: (1) Annual volume commitment and growth target, (2) Promotional calendar — 12 months of planned promotions with BrightMart and supplier funding split, (3) New product launches, (4) Private label collaboration — for suppliers willing to co-manufacture BrightMart private label, (5) Supply chain reliability SLA — fill rate target 98.5%. Provide as a Word template.',
            'Ask Copilot: Write a private label strategy document for the BrightMart Board. Cover: (1) Current private label performance — 28% mix, 42% margin vs national brand 28%, (2) Target — 34% mix by FY2026, (3) Expansion categories — bread, dairy, cleaning, frozen, (4) Private label development process — product brief, supplier qualification, quality testing, (5) Marketing strategy — shelf placement, own media promotion, (6) Financial impact — MYR XX gross profit improvement. 10 pages.'
          ]
        },
        {
          tool: '🎯 Copilot in PowerPoint',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Ask Copilot in PowerPoint: Create a 10-slide Board presentation for BrightMart. Include: (1) FY2025 snapshot — 148 stores, MYR 4.2B GMV, (2) Shrinkage crisis — MYR 46M loss, root cause, (3) Shrinkage reduction plan — technology and process, (4) Private label strategy — 28% to 34%, (5) Fresh food expansion — 18 new stores, (6) Digital transformation — loyalty app, online grocery, (7) Competitive response — vs Lotus\'s and Jaya Grocer, (8) 3-year financial outlook, (9) Key risks, (10) Board decisions. Green and white colour scheme.',
            'Ask Copilot: Create a 3-slide private label pitch for a potential private label manufacturing partner. Slide 1: BrightMart\'s scale — 148 stores, MYR 4.2B GMV, 8M customer transactions/month. Slide 2: Our private label vision — 5 categories we want to launch, target volumes. Slide 3: Partnership model — quality specifications, volume commitment, co-investment in product development.',
            'Ask Copilot: Create a competitor positioning slide showing BrightMart vs Lotus\'s, Giant, and Jaya Grocer on 4 dimensions: store count, private label %, price index (relative to market average), and fresh food quality score. Show as a spider/radar chart.'
          ]
        },
        {
          tool: '📧 Copilot in Outlook',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Ask Copilot in Outlook: Draft an email to all 148 Store Managers announcing the shrinkage reduction programme. The email should: state the current shrinkage rate and the MYR impact, announce the 3 key interventions (CCTV analytics upgrade, new inventory cycle counting requirement, staff reporting protocol), set the 12-month target of 1.5% shrinkage, and motivate managers by connecting shrinkage reduction to their annual bonus. Energetic, performance-focused tone.',
            'Ask Copilot: Draft a letter to our top 10 FMCG suppliers inviting them to the annual joint business planning workshop. The letter should: confirm the workshop date (3 days), list the agenda topics (promotional calendar, volume targets, private label collaboration), ask suppliers to bring their category sales data, and confirm that fill rate performance data will be reviewed as part of the supplier scorecard. Professional commercial tone.',
            'Ask Copilot: Draft a press release announcing the opening of BrightMart\'s expanded fresh food concept at 3 pilot stores. Announce: the enhanced fresh produce section (50% larger), new in-store bakery, halal-certified fresh meat counter, and same-day seafood delivery. Quote the CEO on BrightMart\'s fresh food commitment.'
          ]
        },
        {
          tool: '🎙 Copilot in Teams',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Use your OWN existing recorded Teams meetings. Open a meeting recap in Teams > Recap tab. Copilot generates summaries, action items, and follow-up drafts grounded in the actual transcript.',
          prompts: [
            'Open an existing recorded Teams meeting recap from a retail operations or commercial meeting. Ask Copilot: Identify all shrinkage-related discussions, store performance concerns, and private label review points. Create an action list for the operations and commercial teams.',
            'Ask Copilot: Draft the weekly commercial update for the BrightMart leadership team. Structure: (1) GMV by region vs target, (2) Shrinkage top 5 worst-performing stores this week, (3) Private label GMV vs target, (4) Fresh food expansion status, (5) Top 3 supplier issues.',
            'Ask Copilot: From this meeting, which store regions are consistently underperforming on shrinkage and what specific causes have been identified? Has the security team been engaged and what are their proposed interventions?'
          ]
        },
        {
          tool: '📓 Copilot Notebook',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via copilot.microsoft.com > Notebook tab. Upload up to 5 files and set a system instruction. Best for synthesising insights across multiple documents simultaneously.',
          prompts: [
            'Upload RT_01_BrightMart_Group.xlsx and RT_02_BrightMart_Strategy.docx to Copilot Notebook. Set instruction: "You are a retail operations consultant advising BrightMart on shrinkage reduction and private label growth." Ask: Which single intervention would have the highest ROI on shrinkage reduction given our store size mix? Should we invest in CCTV analytics (RM 12M) or in improved fresh food cold chain management (RM 8M)? Provide a data-backed recommendation.',
            'Upload RT_02_BrightMart_Strategy.docx. Ask: BrightMart wants to launch a private label bread range. We need to identify the right contract manufacturer. Design an RFP scoring matrix with 8 criteria (food safety certification, capacity, pricing, halal certification, delivery reliability, product customisation capability, sustainability practices, financial strength). Weight each criterion and give me a scoring guide for each criterion.'
          ]
        },
        {
          tool: '🤝 Cowork (Frontier)',
          license: 'M365 Copilot + Frontier Program',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Cowork is an autonomous agent that takes actions across Microsoft 365 on your behalf — sending emails, scheduling meetings, creating documents, posting in Teams, and scheduling recurring tasks. Access: m365.cloud.microsoft > left nav > Agents > Cowork. Requires Frontier program enrollment.',
          prompts: [
            'Do all of the following: (1) Research the top 3 CCTV analytics and anti-theft technology vendors for grocery retail in Malaysia — evaluate their capabilities, pricing, and references. (2) Draft an RFP for shrinkage reduction technology covering CCTV analytics at self-checkout, shelf sensors, and inventory management integration. (3) Save to OneDrive as "Shrinkage Technology RFP". (4) Email to the COO and Head of Loss Prevention asking for review within 1 week. (5) Schedule an RFP vendor briefing for all 3 shortlisted vendors.',
            'Do all of the following for private label expansion: (1) Research the top 5 contract food manufacturers in Malaysia and Indonesia who could co-manufacture private label dairy and bakery products to FSSC 22000 standards. (2) Draft a private label manufacturing partner evaluation brief with selection criteria. (3) Email to the Head of Private Label asking for review. (4) Schedule a shortlisting meeting with the commercial team next week. (5) Create a private label product launch calendar for FY2026 in SharePoint.'
          ]
        },
        {
          tool: '🤖 Word Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to a Word document. Open the .docx in Word for Web > Copilot pane > + New Agent > name it, write a description, set the document as knowledge source > Share. Colleagues chat with it in Teams or M365 Copilot.',
          prompts: [
            'Open RT_02_BrightMart_Strategy.docx in Word for Web. Create an agent called "BrightMart Retail Operations Bot". Description: "Answers questions from Store Managers and regional operations teams on shrinkage procedures, private label requirements, fresh food standards, and promotional compliance — ensuring consistent operational excellence across 148 stores." Share with all Store Managers.',
            'Demo: A Store Manager asks "A supplier\'s delivery today was short by 48 cartons of cooking oil but I already signed the delivery note. Our shrinkage target is at risk this month. What is the BrightMart procedure for raising a delivery variance claim against a supplier after the delivery note is signed, and what is the cut-off time to raise the claim?" Show the agent providing an instant, procedure-grounded answer that helps the manager recover the loss.'
          ]
        },
        {
          tool: '🤖 PowerPoint Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to a PowerPoint presentation. Great for strategy decks or Board presentations many people need to reference. Same setup as Word Agent but using a .pptx file.',
          prompts: [
            'Create a PowerPoint from the Board presentation. Create an agent called "BrightMart Board & Commercial Q&A Bot". Share with the Board and regional directors.',
            'Demo: A regional director asks "My region has the second-highest shrinkage rate in the group. What are the 3 specific interventions that have been approved in the shrinkage reduction plan for high-shrinkage stores and when will the CCTV analytics upgrade be deployed to my region?" Show the agent providing a programme-specific, region-relevant answer.'
          ]
        },
        {
          tool: '🤖 Excel Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to an Excel workbook. Colleagues ask data questions in plain English without opening Excel. Open .xlsx in Excel for Web > Copilot pane > + New Agent > set workbook as knowledge source > share.',
          prompts: [
            'Open RT_01_BrightMart_Group.xlsx in Excel for Web. Create an agent called "BrightMart Store Performance Q&A". Description: "Instant answers on store-level GMV, shrinkage rates, private label mix, and fresh food performance for the CEO, COO, and regional directors." Share with operations leadership.',
            'Demo: Ask "What are the 5 stores with the highest shrinkage rate this month and what is the combined RM loss from these 5 stores?" Then: "What is our current private label mix in the dairy category and how does it compare to the 34% group target?" Show the COO getting instant multi-store intelligence.'
          ]
        },
        {
          tool: '🏗 Agent Builder (Copilot Studio)',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Build a custom declarative agent in Copilot Studio — no coding required. Access: copilotstudio.microsoft.com > Create > New Agent. Add name, description, knowledge sources (SharePoint URLs or uploaded files), topics/actions. Publish to Teams in under 10 minutes.',
          prompts: [
            'Go to copilotstudio.microsoft.com > Create > New Agent. Name it "BrightMart Retail Intelligence Agent". Description: "Supports BrightMart\'s Store Managers, regional directors, and Group leadership with instant answers on store performance, shrinkage procedures, private label standards, fresh food requirements, and supplier policies — enabling faster, smarter retail decisions across 148 stores." Upload RT_01_BrightMart_Group.xlsx and RT_02_BrightMart_Strategy.docx. Add topics: "Shrinkage Management", "Private Label", "Store Operations", "Supplier Relations". Publish to Teams.',
            'Demo the agent: A Store Manager calls the regional director on a Saturday evening: "Our self-checkout CCTV flagged 3 potential theft incidents today. One involves a loyalty member who has been shopping with us for 8 years and MYR 42,000 cumulative spend. What is our policy on confronting suspected shoplifters and do I need manager approval before reviewing CCTV footage of a high-value loyalty customer?" Show how the agent provides an instant, policy-grounded answer that protects both the business and the customer relationship.'
          ]
        }
      ]
    },
    {
      id: 'media-entertainment',
      sectorId: 'media',
      subsector: '',
      name: 'Media & Entertainment',
      icon: '📺',
      color: '#6A1B9A',
      accent: '#7B1FA2',
      company: 'Prism Media Group',
      tagline: 'Linear TV audience -34% — digital pivot + content IP monetisation strategy.',
      scenario: 'Prism Media Group operates 4 free-to-air TV channels, 2 radio networks, an OTT streaming platform (PrismPlay), and a content production studio. Linear TV audience has declined 34% in 5 years. PrismPlay has 2.1M subscribers with 28% annual churn. The content studio has 340 hours of unmonetised IP in its library.',
      files: [
        'TC_01_ClearWave_Communications.xlsx',
        'TC_02_ClearWave_Strategy.docx'
      ],
      prompts: [
        {
          tool: '🤖 Copilot Chat (Basic)',
          license: 'Free — no M365 Copilot license needed',
          account: 'Sasha Ouellet — SashaO@ABSx62256373.OnMicrosoft.com',
          desc: '',
          prompts: [
            'I am the CEO of a Malaysian free-to-air broadcaster facing a 34% audience decline in 5 years from cord-cutting and digital alternatives. Our OTT platform has 2.1M subscribers but a 28% annual churn rate. Draft a 250-word brief for my Board on the strategic path forward. Cover: (1) The realistic future of free-to-air broadcasting in Malaysia given the demographic trends, (2) Whether we should invest aggressively in OTT to grow PrismPlay or focus on defending the FTA broadcast business, (3) How comparable broadcasters (Astro, TV3, RTM) have adapted their strategies.',
            'What is a content library monetisation strategy for a broadcasting company? We have 340 hours of unmonetised TV content IP. What are the key revenue streams — streaming licensing, international distribution, format sales, YouTube monetisation — and which typically generate the best return for Malaysian content in regional markets?',
            'Explain what churn rate means for a streaming platform, what a 28% annual churn rate implies for subscriber lifetime value, and what the 3 most effective tactics to reduce streaming platform churn are. Focus on tactics relevant to a Malaysian OTT platform competing with Netflix, Disney+, and YouTube.'
          ]
        },
        {
          tool: '🔍 Researcher',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via Microsoft 365 Copilot Chat (copilot.microsoft.com or Teams) > click Agents > Researcher. Grounds answers in live web sources and your organisation data with full citations.',
          prompts: [
            'Research the Malaysian media and OTT streaming market in 2024–2025. I need: (1) Total OTT subscribers in Malaysia and growth rate, (2) Competitive landscape — Netflix, Disney+, Astro GO, sooka, YouTube Premium, (3) Content preferences of Malaysian audiences — local vs international, Malay vs English vs Chinese language, (4) Advertising market trends — digital vs broadcast. Cite Nielsen, Kantar, or MCMC data.',
            'Research content library monetisation strategies for regional broadcasters. I need: (1) How broadcasters like ABS-CBN (Philippines), TVRI (Indonesia), and Thai PBS have monetised their content libraries internationally, (2) The value of Southeast Asian content IP in international markets, (3) YouTube Shorts and short-form video monetisation potential for broadcast content. Cite industry sources.'
          ]
        },
        {
          tool: '📊 Analyst',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via Microsoft 365 Copilot Chat > click Agents > Analyst. Upload an Excel or CSV file. Analyst runs Python-style analysis, builds charts, and interprets results without you writing a single formula.',
          prompts: [
            'Upload TC_01_ClearWave_Communications.xlsx to Analyst (use as media company data proxy). Ask: Build a subscriber lifetime value (LTV) model for PrismPlay. Inputs: 2.1M subscribers, monthly ARPU MYR 18, 28% annual churn rate. Calculate: (1) Average subscriber lifetime in months, (2) LTV per subscriber, (3) If churn reduces to 20%, what is the LTV improvement? (4) If ARPU increases to MYR 22, what is the LTV improvement? (5) What is the total subscriber value at risk from the current 28% churn vs industry benchmark 18%? Show as a scenario comparison table.',
            'Upload TC_01_ClearWave_Communications.xlsx. Ask: Analyse the content library monetisation opportunity. 340 hours of content IP. Estimate potential revenue from 5 channels: (1) Licensing to international OTT (assume USD 8,000 per hour), (2) YouTube channel monetisation (assume 2M views/month at USD 3 CPM), (3) Format sales — 5 show formats at USD 180,000 per format, (4) Domestic streaming rights sale to competitor, (5) Content repackaging for Shorts (assume 40% of content suitable). Calculate total addressable revenue from content library monetisation.'
          ]
        },
        {
          tool: '📊 Copilot in Excel',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open TC_01_ClearWave_Communications.xlsx. Navigate to the Digital Performance sheet. Ask Copilot: Build a PrismPlay subscriber dashboard on a new sheet. Show monthly data for the past 12 months: (1) New subscriber additions, (2) Churned subscribers, (3) Net subscriber change, (4) Total subscribers at month end, (5) Monthly churn rate %, (6) ARPU (MYR), (7) Monthly recurring revenue (MYR M). Add a trendline. Highlight months where churn exceeded 2.5% in red.',
            'Ask Copilot: Create a content library value dashboard on a new sheet. For each of the top 50 content titles by estimated market value, show: (1) Title, (2) Genre, (3) Production year, (4) Duration (hours), (5) Language, (6) Awards/recognition, (7) Historical viewing data available (Y/N), (8) Rights status (owned/partial/expired), (9) Estimated streaming license value (RM), (10) Monetisation status (Unexploited/In Progress/Monetised). Calculate total unexploited library value.',
            'Ask Copilot: Build a digital pivot investment plan on a new sheet. For each digital investment initiative (PrismPlay content spend increase, app UX upgrade, AI personalisation engine, creator partnership programme, live sports streaming rights), show: investment required (RM M), expected subscriber impact (net new or churn reduction), expected ARPU impact, Year 1 and Year 3 revenue contribution, and ROI at 3 years. Sort by Year 3 ROI, highest first.'
          ]
        },
        {
          tool: '📝 Copilot in Word',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open TC_02_ClearWave_Strategy.docx. Ask Copilot: Draft a 10-page digital transformation strategy for Prism Media Group. Cover: (1) Market context — linear TV decline, OTT growth, Malaysian consumer behaviour, (2) PrismPlay growth strategy — subscriber target 5M by FY2027, churn reduction to 18%, ARPU to MYR 22, (3) Content strategy — local content investment, premium originals, live sports, reality formats, (4) Content library monetisation — 3-year plan for the 340 hours of IP, (5) Advertising transformation — programmatic digital, addressable TV, branded content, (6) Technology investment — AI personalisation, recommendation engine, data analytics, (7) Financial projections — 3-year revenue and EBITDA. Formal strategy document format.',
            'Ask Copilot: Draft a content licensing proposal to a major regional streaming platform (e.g., WeTV or iQIYI). The proposal should: introduce Prism Media Group and our content credentials, highlight our top 10 content titles available for licensing, describe our content quality (HD, with English/Chinese subtitles), propose a licensing package of 200 hours at USD 8,000 per hour plus a first-look agreement for new productions. Professional content distribution format.',
            'Ask Copilot: Write a creator partnership programme brief for PrismPlay\'s new creator economy initiative. The programme invites Malaysian content creators with 100K+ followers to produce short-form content for PrismPlay. Cover: (1) Programme overview and goals, (2) Creator eligibility criteria, (3) Revenue share model (60% creator, 40% PrismPlay), (4) Content guidelines — content types, language, duration, (5) Application process. Format as an attractive creator pitch document.'
          ]
        },
        {
          tool: '🎯 Copilot in PowerPoint',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Ask Copilot in PowerPoint: Create a 12-slide strategy presentation for the Prism Media Group Board. Include: (1) The burning platform — linear TV audience -34%, (2) PrismPlay performance — 2.1M subscribers, 28% churn, (3) Market opportunity — 5M subscriber target, (4) Content strategy — local originals, live sports, creator economy, (5) Content library monetisation — 340 hours, RM XX addressable value, (6) Technology investment — AI personalisation, (7) Advertising transformation, (8) Digital organisation restructuring, (9) 3-year financial projections, (10) Investment required — RM XX, (11) Key risks, (12) Board decisions. Purple and white colour scheme.',
            'Ask Copilot: Create a 3-slide churn reduction pitch for the PrismPlay product team. Slide 1: Current churn vs benchmark — 28% vs 18% — and the revenue impact (MYR XX annualised loss). Slide 2: The 3 root causes of churn based on exit surveys — content, price, UX. Slide 3: The 3 targeted interventions and their expected churn reduction impact.',
            'Ask Copilot: Create a content library opportunity slide — "Our Hidden Asset". Visual: 340 hours of content IP shown as stacked bars by genre. Table showing: monetisation channel, addressable revenue, time to revenue. Total library value estimate at top right. Key message: "We are sitting on RM XX of unexploited value."'
          ]
        },
        {
          tool: '📧 Copilot in Outlook',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Ask Copilot in Outlook: Draft an email to the CEOs of WeTV (Tencent) and iQIYI proposing a content licensing partnership for Prism Media Group\'s library. The email should: introduce our 340-hour library, highlight our top 5 drama and reality formats, propose a content preview session at their regional offices, and note our interest in a co-production agreement for new Malaysian content targeting pan-ASEAN audiences.',
            'Ask Copilot: Draft an email to PrismPlay\'s top 200 subscribers who have been with the platform for over 24 months and have not engaged in the last 30 days. The email should: acknowledge their loyalty, offer a 2-month plan upgrade at no extra cost, highlight 3 new content titles matching their viewing history, and include a personalised "We miss you" message. Warm, personalised tone.',
            'Ask Copilot: Draft a press release announcing Prism Media Group\'s digital pivot strategy. Announce: the 5M PrismPlay subscriber target by FY2027, the RM 180M content investment programme for original local productions, the creator partnership programme launch, and the content library international licensing initiative. Quote the CEO and the Head of Digital.'
          ]
        },
        {
          tool: '🎙 Copilot in Teams',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Use your OWN existing recorded Teams meetings. Open a meeting recap in Teams > Recap tab. Copilot generates summaries, action items, and follow-up drafts grounded in the actual transcript.',
          prompts: [
            'Open an existing recorded Teams meeting recap from an editorial, content, or strategy meeting. Ask Copilot: Identify all content performance discussions, churn-related concerns, and digital strategy action items. Flag any decisions about content investment or platform development.',
            'Ask Copilot: Draft follow-up actions from the PrismPlay churn reduction taskforce meeting. Group by workstream: Content Acquisition | UX & Product | Pricing & Promotions | Personalisation & AI | Customer Success. Include owner and deadline.',
            'Ask Copilot: Based on this meeting, what specific content genres are being proposed for the local originals programme? Who are the production partners being considered and what is the indicative budget per episode?'
          ]
        },
        {
          tool: '📓 Copilot Notebook',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via copilot.microsoft.com > Notebook tab. Upload up to 5 files and set a system instruction. Best for synthesising insights across multiple documents simultaneously.',
          prompts: [
            'Upload TC_01_ClearWave_Communications.xlsx and TC_02_ClearWave_Strategy.docx to Copilot Notebook. Set instruction: "You are a digital media strategy advisor helping Prism Media Group prioritise their digital investment." Ask: Given a total investment budget of RM 180M over 3 years, how should we allocate between: local original content, technology (AI personalisation), live sports rights, content library monetisation, and creator economy? Provide a data-backed allocation recommendation with expected subscriber and ARPU impact.',
            'Upload TC_02_ClearWave_Strategy.docx. Ask: PrismPlay is losing subscribers to YouTube Shorts — 18% of churned subscribers cite short-form video preference as their reason for leaving. Should PrismPlay launch a short-form content platform within the app, or partner with YouTube through a branded channel? Analyse both options and recommend the better path for a Malaysian broadcaster with RM 20M to spend on this initiative.'
          ]
        },
        {
          tool: '🤝 Cowork (Frontier)',
          license: 'M365 Copilot + Frontier Program',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Cowork is an autonomous agent that takes actions across Microsoft 365 on your behalf — sending emails, scheduling meetings, creating documents, posting in Teams, and scheduling recurring tasks. Access: m365.cloud.microsoft > left nav > Agents > Cowork. Requires Frontier program enrollment.',
          prompts: [
            'Do all of the following: (1) Research the top 5 Malaysian content creators with 100K+ followers across YouTube, TikTok, and Instagram who align with PrismPlay\'s entertainment and lifestyle content strategy. (2) Draft personalised partnership outreach messages for each creator in a friendly, collaborative tone. (3) Save to OneDrive as "PrismPlay Creator Partnership Outreach". (4) Email to the Head of Digital Partnerships for review. (5) Schedule a creator partnership launch event to present the programme to 50 creators next month.',
            'Do all of the following for the content library: (1) Research WeTV, iQIYI, and Viu\'s content acquisition strategies for Southeast Asian drama and reality content — what types they buy and at what price points. (2) Draft a content catalogue pitch document for our top 50 titles. (3) Email to the Content Distribution Director with a request to review and approve within 3 days. (4) Create a content licensing pipeline tracker in SharePoint. (5) Schedule a content preview screening for regional streaming platforms in Kuala Lumpur next quarter.'
          ]
        },
        {
          tool: '🤖 Word Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to a Word document. Open the .docx in Word for Web > Copilot pane > + New Agent > name it, write a description, set the document as knowledge source > Share. Colleagues chat with it in Teams or M365 Copilot.',
          prompts: [
            'Open TC_02_ClearWave_Strategy.docx in Word for Web. Create an agent called "Prism Media Digital Strategy Bot". Description: "Answers questions from the PrismPlay product, content, and commercial teams on digital strategy priorities, content investment guidelines, creator programme requirements, and OTT platform targets." Share with the digital and content teams.',
            'Demo: A content acquisitions manager asks "We have a chance to acquire exclusive streaming rights to a popular Korean drama for RM 2.4M. Our content investment guideline requires a minimum 80,000 new-to-platform subscribers triggered by a single title. Based on comparable Korean drama acquisitions, does this title meet our investment threshold?" Show how the agent provides a content investment framework-grounded answer.'
          ]
        },
        {
          tool: '🤖 PowerPoint Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to a PowerPoint presentation. Great for strategy decks or Board presentations many people need to reference. Same setup as Word Agent but using a .pptx file.',
          prompts: [
            'Create a PowerPoint from the Board strategy presentation. Create an agent called "Prism Media Board Strategy Q&A Bot". Share with the Board and Group executive leadership.',
            'Demo: A Board member asks "If we invest RM 180M in digital over 3 years and reach 5M PrismPlay subscribers, what is the projected EBITDA in FY2027 compared to FY2024 — and at what subscriber level does PrismPlay become cash flow positive?" Show the agent providing a financial projection-grounded investment case answer.'
          ]
        },
        {
          tool: '🤖 Excel Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to an Excel workbook. Colleagues ask data questions in plain English without opening Excel. Open .xlsx in Excel for Web > Copilot pane > + New Agent > set workbook as knowledge source > share.',
          prompts: [
            'Open TC_01_ClearWave_Communications.xlsx in Excel for Web. Create an agent called "Prism Media Performance Q&A". Description: "Instant answers on PrismPlay subscriber metrics, churn trends, content library value, digital advertising revenue, and linear TV ratings for the CEO and digital leadership." Share with the senior leadership team.',
            'Demo: Ask "What is PrismPlay\'s monthly net subscriber change for the past 3 months and is churn accelerating or decelerating?" Then: "What is the current estimated revenue of the unexploited content library and which content genre has the highest international licensing value?" Show the CEO getting instant media business intelligence.'
          ]
        },
        {
          tool: '🏗 Agent Builder (Copilot Studio)',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Build a custom declarative agent in Copilot Studio — no coding required. Access: copilotstudio.microsoft.com > Create > New Agent. Add name, description, knowledge sources (SharePoint URLs or uploaded files), topics/actions. Publish to Teams in under 10 minutes.',
          prompts: [
            'Go to copilotstudio.microsoft.com > Create > New Agent. Name it "Prism Media Intelligence Agent". Description: "Supports Prism Media Group\'s content, digital, and commercial teams with instant answers on PrismPlay subscriber performance, churn drivers, content investment criteria, creator programme requirements, content library licensing, and digital advertising strategy — enabling faster, smarter media and entertainment decisions." Upload TC_01_ClearWave_Communications.xlsx and TC_02_ClearWave_Strategy.docx. Add topics: "PrismPlay Performance", "Content Strategy", "Creator Economy", "Content Library Licensing". Publish to Teams.',
            'Demo the agent: A content producer pitches an original Malay drama series to the Head of Content at 8am via Teams. The Head of Content quickly asks the agent before the meeting: "For a 13-episode original Malay drama at RM 280,000 per episode (total RM 3.64M), what is the minimum subscriber acquisition we need to justify the investment, and does this genre typically perform well enough to meet our content ROI threshold? Also, have we licensed any similar drama content internationally and at what price?" Show how the agent enables faster, data-driven content commissioning decisions.'
          ]
        }
      ]
    },
    {
      id: 'glc-investment',
      sectorId: 'glc',
      subsector: '',
      name: 'GLC Investment Arm',
      icon: '🏛',
      color: '#1A237E',
      accent: '#283593',
      company: 'Danamas Capital Berhad',
      tagline: 'MYR 48.2B AUM — mandate review + Khazanah-style strategic equity portfolio refresh.',
      scenario: 'Danamas Capital Berhad is Malaysia\'s state-linked strategic investment arm managing MYR 48.2B AUM across 34 investee companies. The government has initiated a mandate review to clarify the balance between commercial returns and national development objectives. The portfolio includes 3 underperforming GLCs requiring either active engagement or divestment.',
      files: [
        'GLC_01_Danamas_Capital.xlsx',
        'GLC_02_Danamas_Strategy.docx'
      ],
      prompts: [
        {
          tool: '🤖 Copilot Chat (Basic)',
          license: 'Free — no M365 Copilot license needed',
          account: 'Sasha Ouellet — SashaO@ABSx62256373.OnMicrosoft.com',
          desc: '',
          prompts: [
            'I am the CEO of a Malaysian government-linked investment arm managing MYR 48.2B AUM across 34 investee companies, similar to Khazanah Nasional. The government has asked us to review our mandate — specifically whether we should prioritise commercial returns (like Temasek) or developmental impact (like the old Khazanah mandate). Draft a 300-word brief for the Minister covering: (1) The key differences between a pure commercial investment mandate and a developmental investment mandate, (2) How Temasek (Singapore), Khazanah (Malaysia), and PNB have each balanced commercial and developmental objectives, (3) A recommended hybrid framework that serves both objectives without compromising either.',
            'What are the key governance requirements for a GLC investment arm in Malaysia? How does Khazanah\'s governance structure differ from a conventional fund manager? What are the Putrajaya Committee guidelines for GLC governance and how do they apply to a strategic investment entity?',
            'Explain what an active ownership strategy means for a GLC investor. When should a GLC investment arm intervene in an underperforming investee company — replacing the Board, issuing a performance turnaround mandate, or divesting? What triggers are typically used by Khazanah or Temasek before escalating to active intervention?'
          ]
        },
        {
          tool: '🔍 Researcher',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via Microsoft 365 Copilot Chat (copilot.microsoft.com or Teams) > click Agents > Researcher. Grounds answers in live web sources and your organisation data with full citations.',
          prompts: [
            'Research the governance and investment strategies of major Asian sovereign and government-linked investment arms — specifically Temasek (Singapore), Khazanah Nasional (Malaysia), GIC (Singapore), and KWAP (Malaysia). I need: (1) Their AUM and portfolio composition, (2) How they balance commercial returns vs national development, (3) Their ESG integration approach, (4) Their performance measurement frameworks. Cite annual reports and academic sources.',
            'Research the current landscape of GLCs (Government-Linked Companies) in Malaysia. What are the biggest GLCs by market cap? How has GLC financial performance compared to the broader Bursa Malaysia index over the past 5 years? Are there any GLCs currently under active government restructuring? Cite Putrajaya GLC Transformation Programme reports and Bursa data.'
          ]
        },
        {
          tool: '📊 Analyst',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via Microsoft 365 Copilot Chat > click Agents > Analyst. Upload an Excel or CSV file. Analyst runs Python-style analysis, builds charts, and interprets results without you writing a single formula.',
          prompts: [
            'Upload GLC_01_Danamas_Capital.xlsx to Analyst. Ask: Analyse the MYR 48.2B portfolio across 34 investee companies. Segment by: (1) Sector (financial services, infrastructure, plantation, manufacturing, utilities), (2) Ownership stake (majority >50%, strategic 20-50%, minority <20%), (3) Performance (outperforming vs underperforming vs turnaround). Create a portfolio matrix: X-axis = commercial return (ROCE vs benchmark), Y-axis = strategic importance (development impact score). Place all 34 investees. Identify the 3 quadrant "harvest" candidates (high return, low strategic importance) and the 3 "transform or exit" candidates (low return, low strategic importance).',
            'Upload GLC_01_Danamas_Capital.xlsx. Ask: Build a portfolio return attribution analysis. For the MYR 48.2B AUM: (1) Total return for FY2024 — dividends + capital appreciation, (2) Return by sector and by ownership stake tier, (3) Compare total portfolio return vs the FBM KLCI benchmark and a pure commercial return benchmark (MSCI Malaysia), (4) Identify the 5 investees contributing most to total return and the 5 dragging total return. Calculate the incremental AUM that could be created if the 5 worst performers improved to median portfolio return.'
          ]
        },
        {
          tool: '📊 Copilot in Excel',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open GLC_01_Danamas_Capital.xlsx. Navigate to the Portfolio sheet. Ask Copilot: Build a portfolio health dashboard on a new sheet. For each of the 34 investee companies, show: (1) Company name and sector, (2) Danamas ownership % and book value (MYR M), (3) Market value (MYR M), (4) ROCE %, (5) EBITDA margin %, (6) Dividend received (MYR M), (7) Performance status (Outperform / In-line / Underperform / Turnaround Required). Highlight Underperform in amber and Turnaround Required in red. Total column for portfolio-level aggregates.',
            'Ask Copilot: Create a turnaround performance scorecard for the 3 underperforming investees. For each, show: (1) Original investment value, (2) Current market value, (3) Total return since investment vs FBM KLCI benchmark, (4) Key financial distress indicators (leverage, interest coverage, cash burn), (5) Previous turnaround actions taken (Board changes, new CEO, asset sales), (6) Current turnaround plan status. Apply RAG status.',
            'Ask Copilot: Build an ESG portfolio score dashboard. For each of the 34 investees, show: (1) Bursa Malaysia sustainability rating, (2) GHG Scope 1 intensity, (3) Women on Board %, (4) Anti-corruption training completion %, (5) MSCI ESG rating if available. Calculate Danamas\'s weighted average ESG score. Highlight companies below the portfolio ESG target.'
          ]
        },
        {
          tool: '📝 Copilot in Word',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open GLC_02_Danamas_Strategy.docx. Ask Copilot: Draft a 10-page investment mandate review document for the Minister of Finance. Cover: (1) Executive summary — Danamas AUM, portfolio composition, FY2024 return, (2) Current mandate ambiguity — the tension between commercial and developmental objectives, (3) Proposed hybrid mandate framework — 60% commercial, 40% developmental, (4) Portfolio implications — which assets to grow, hold, or divest under the new mandate, (5) Governance enhancements — Board composition, investment committee charter, (6) Performance metrics — commercial return target (KLCI+3%), developmental impact metrics, (7) 5-year strategic plan. Formal ministerial briefing format.',
            'Ask Copilot: Draft an active ownership engagement letter to the Board Chairman of one underperforming investee company. As the major shareholder (43% stake), Danamas is formally requiring: (1) A 100-day turnaround plan within 6 weeks, (2) An independent business review by a credible advisory firm, (3) Monthly performance reporting to Danamas, (4) Specific improvements in 4 financial KPIs within 12 months. The letter should be firm but respectful of the Board\'s governance role. Reference the Putrajaya GLC governance guidelines.',
            'Ask Copilot: Write a chapter for Danamas Capital\'s annual report — "Active Ownership and Developmental Impact in FY2024." Cover: (1) Portfolio value creation summary — total return MYR XX, (2) 3 active engagement successes — turnarounds, Board improvements, sustainability upgrades, (3) Developmental impact — jobs created, infrastructure enabled, Bumiputera economic participation, (4) ESG integration progress — portfolio weighted ESG score improvement. GRI-aligned format.'
          ]
        },
        {
          tool: '🎯 Copilot in PowerPoint',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Ask Copilot in PowerPoint: Create a 12-slide Minister of Finance briefing on Danamas Capital\'s mandate review. Include: (1) Danamas overview — MYR 48.2B AUM, 34 investees, (2) FY2024 portfolio performance vs benchmark, (3) Current mandate — tensions between commercial and developmental, (4) Temasek vs Khazanah model comparison, (5) Proposed hybrid mandate framework, (6) Portfolio segmentation — grow, hold, divest, (7) The 3 underperforming investees — turnaround plans, (8) ESG integration — portfolio sustainability score, (9) Governance enhancement proposal, (10) 5-year AUM and return targets, (11) Key risks, (12) Ministerial decisions required. Dark navy and gold colour scheme.',
            'Ask Copilot: Create a 3-slide portfolio health summary for the Danamas Board quarterly review. Slide 1: Portfolio overview — total AUM, weighted return, vs benchmark. Slide 2: Top 5 performers and bottom 5 performers with key metrics. Slide 3: Turnaround progress on the 3 underperforming investees — RAG status for each KPI in the turnaround plan.',
            'Ask Copilot: Create a 2-slide developmental impact summary. Slide 1: Quantified impact — jobs created, Bumiputera economic participation %, infrastructure projects enabled, SME linkages generated. Slide 2: ESG portfolio evolution — portfolio average ESG score over 5 years vs target.'
          ]
        },
        {
          tool: '📧 Copilot in Outlook',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Ask Copilot in Outlook: Draft an email from the Danamas CEO to the 34 investee company CEOs announcing the new portfolio performance reporting requirements under the refreshed mandate. The email should: state the new quarterly reporting format, list the 12 KPIs now required, note that ESG reporting will be mandatory from Q2 FY2026, and invite all CEOs to the annual Danamas Investee CEO Forum in 6 weeks. Professional but authoritative GLC investor tone.',
            'Ask Copilot: Draft a letter to the Minister of Finance formally submitting the Danamas mandate review document. The letter should: summarise the 3 key recommendations (hybrid mandate, portfolio segmentation, governance enhancements), request a bilateral meeting to discuss the ministerial decisions, and note the timeline for implementation. Formal government correspondence format.',
            'Ask Copilot: Draft an email to the Chairman and CEO of the most underperforming investee company requesting an urgent meeting within 7 days. The email should signal clearly that Danamas is reviewing its options as the 43% shareholder — including escalation to a formal active ownership intervention. Firm but diplomatically worded.'
          ]
        },
        {
          tool: '🎙 Copilot in Teams',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Use your OWN existing recorded Teams meetings. Open a meeting recap in Teams > Recap tab. Copilot generates summaries, action items, and follow-up drafts grounded in the actual transcript.',
          prompts: [
            'Open an existing recorded Teams meeting recap from an investment committee or portfolio review meeting. Ask Copilot: Identify all investee performance discussions — which companies were reviewed, what concerns were raised, and what decisions or escalations were approved. Create an action tracker for the investment management team.',
            'Ask Copilot: Draft an investment committee follow-up memo on the turnaround status of the 3 underperforming investees. For each, summarise: current financial status, turnaround actions in progress, any Board changes approved, and the next key milestone.',
            'Ask Copilot: Were there any discussions about portfolio divestment candidates? Which investees are being considered for divestment and what is the rationale (strategic fit, return, ESG) for each?'
          ]
        },
        {
          tool: '📓 Copilot Notebook',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via copilot.microsoft.com > Notebook tab. Upload up to 5 files and set a system instruction. Best for synthesising insights across multiple documents simultaneously.',
          prompts: [
            'Upload GLC_01_Danamas_Capital.xlsx and GLC_02_Danamas_Strategy.docx to Copilot Notebook. Set instruction: "You are a sovereign wealth fund advisor helping Danamas Capital design its new investment mandate." Ask: Based on the portfolio data and strategic context, what is the optimal portfolio composition under a 60/40 commercial/developmental mandate — and which of the 34 current investees should be classified as core, strategic, or divest?',
            'Upload GLC_02_Danamas_Strategy.docx. Ask: Danamas is considering selling its 38% stake in a well-performing plantation company (MYR 4.2B market value, 8.4% ROCE, but low developmental impact score). The proceeds could be reinvested in a loss-making but strategically important EV charging infrastructure company. Is this trade-off consistent with the proposed hybrid mandate? What should the investment committee recommend?'
          ]
        },
        {
          tool: '🤝 Cowork (Frontier)',
          license: 'M365 Copilot + Frontier Program',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Cowork is an autonomous agent that takes actions across Microsoft 365 on your behalf — sending emails, scheduling meetings, creating documents, posting in Teams, and scheduling recurring tasks. Access: m365.cloud.microsoft > left nav > Agents > Cowork. Requires Frontier program enrollment.',
          prompts: [
            'Do all of the following: (1) Research Temasek Holdings\' and Khazanah Nasional\'s most recent annual reports — extract their mandate frameworks, portfolio performance metrics, and ESG targets. (2) Draft a 5-page mandate comparison brief for the Danamas Board showing best practices from both. (3) Save to OneDrive as "Mandate Benchmarking - Temasek vs Khazanah". (4) Email to the CEO and Chief Investment Officer for review before the Minister briefing. (5) Schedule a Board mandate workshop for 2 weeks from now.',
            'Do all of the following for the underperforming investee turnaround: (1) Research what governance interventions sovereign and GLC funds typically use to drive turnaround in underperforming portfolio companies — Board refreshment, CEO replacement, independent review, strategic partnership. (2) Draft a formal active ownership intervention letter for the most critical underperformer. (3) Email to the General Counsel for legal review before sending. (4) Prepare a Board resolution template authorising the intervention. (5) Schedule an investment committee special session to approve the intervention.'
          ]
        },
        {
          tool: '🤖 Word Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to a Word document. Open the .docx in Word for Web > Copilot pane > + New Agent > name it, write a description, set the document as knowledge source > Share. Colleagues chat with it in Teams or M365 Copilot.',
          prompts: [
            'Open GLC_02_Danamas_Strategy.docx in Word for Web. Create an agent called "Danamas Investment Policy & Governance Bot". Description: "Answers questions from the Danamas investment team on mandate requirements, GLC governance standards, Putrajaya guidelines, ESG reporting obligations, and active ownership intervention criteria." Share with the investment management and governance teams.',
            'Demo: An investment manager asks "We hold a 22% strategic stake in a GLC that has just announced a related-party transaction with the CEO\'s family company worth RM 180M. As a 22% shareholder, what governance rights do we have to challenge this transaction and what actions should we take within the next 48 hours?" Show the agent providing a governance-grounded, action-oriented answer.'
          ]
        },
        {
          tool: '🤖 PowerPoint Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to a PowerPoint presentation. Great for strategy decks or Board presentations many people need to reference. Same setup as Word Agent but using a .pptx file.',
          prompts: [
            'Create a PowerPoint from the Minister briefing presentation. Create an agent called "Danamas Capital Q&A Bot". Share with the Minister of Finance\'s office and the Danamas Board.',
            'Demo: A Ministry official asks "How does Danamas\'s proposed 60/40 mandate compare to Khazanah\'s current mandate and what evidence is there that a hybrid mandate can achieve both commercial and developmental objectives simultaneously?" Show the agent providing an evidence-based, benchmarked policy answer.'
          ]
        },
        {
          tool: '🤖 Excel Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to an Excel workbook. Colleagues ask data questions in plain English without opening Excel. Open .xlsx in Excel for Web > Copilot pane > + New Agent > set workbook as knowledge source > share.',
          prompts: [
            'Open GLC_01_Danamas_Capital.xlsx in Excel for Web. Create an agent called "Danamas Portfolio Q&A". Description: "Instant answers on the MYR 48.2B portfolio — investee performance, return attribution, ESG scores, and turnaround status — for the CEO, CIO, and investment committee." Share with the Danamas leadership.',
            'Demo: Ask "Which 5 investees have delivered the highest total return (dividends + capital appreciation) over the past 3 years and what was the combined value created?" Then: "What is the weighted average ROCE of the portfolio and how does that compare to the FBM KLCI benchmark?" Show the CIO getting instant portfolio intelligence.'
          ]
        },
        {
          tool: '🏗 Agent Builder (Copilot Studio)',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Build a custom declarative agent in Copilot Studio — no coding required. Access: copilotstudio.microsoft.com > Create > New Agent. Add name, description, knowledge sources (SharePoint URLs or uploaded files), topics/actions. Publish to Teams in under 10 minutes.',
          prompts: [
            'Go to copilotstudio.microsoft.com > Create > New Agent. Name it "Danamas Capital Intelligence Agent". Description: "Supports Danamas Capital\'s investment team, CEO, and Board with instant answers on portfolio performance, GLC governance requirements, Putrajaya guidelines, active ownership thresholds, ESG obligations, and mandate framework — enabling faster, smarter GLC investment decisions." Upload GLC_01_Danamas_Capital.xlsx and GLC_02_Danamas_Strategy.docx. Add topics: "Portfolio Performance", "GLC Governance", "Active Ownership", "ESG & Developmental Impact". Publish to Teams.',
            'Demo the agent: The Danamas CEO receives an urgent call from a journalist: a major investee company has just published a profit warning revealing a RM 340M accounting irregularity. The CEO has a Ministerial press conference in 40 minutes. The CEO asks the agent: "What is Danamas\'s ownership stake in this company, what was the last reported financial health status, and what are our legal obligations as a major shareholder when an investee discloses a material misstatement? Do we need to issue a statement before or after the Minister\'s press conference?" Show how the agent prepares the CEO for a crisis in real time.'
          ]
        }
      ]
    },
    {
      id: 'financial-regulator',
      sectorId: 'government',
      subsector: '',
      name: 'Financial Regulator',
      icon: '⚖️',
      color: '#1B5E20',
      accent: '#2E7D32',
      company: 'Bank Negara Malaysia / OJK Proxy',
      tagline: 'NPL monitoring + IFSA digital banking licence review + systemic risk report.',
      scenario: 'A central bank supervisory team is monitoring 18 licensed financial institutions. NPL in the personal loan segment has breached the 3.5% system-wide threshold. 2 new digital banking licences are under post-approval operational review. The annual systemic risk report to the Board of Governors is due in 3 weeks.',
      files: [
        'BNK_02_Meridian_Bank_Strategy.docx',
        'Email_06_BNM_Regulatory_Correspondence.docx'
      ],
      prompts: [
        {
          tool: '🤖 Copilot Chat (Basic)',
          license: 'Free — no M365 Copilot license needed',
          account: 'Sasha Ouellet — SashaO@ABSx62256373.OnMicrosoft.com',
          desc: '',
          prompts: [
            'I am a senior supervisor at a central bank overseeing 18 licensed financial institutions. The system-wide NPL for personal loans has just breached the 3.5% supervisory threshold — driven by 3 institutions with NPL above 15%. Draft a 250-word supervisory escalation brief for the Governor covering: (1) The scale and nature of the NPL breach, (2) The 3 institutions most at risk, (3) The supervisory tools available under IFSA 2013 to compel remediation — Enhanced Monitoring, Corrective Action Plan, Statutory Management, (4) The systemic risk implications if 2 of the 3 institutions require statutory intervention simultaneously.',
            'Explain what a Digital Banking Licence operational review entails in Malaysia. What operational milestones must a newly licensed digital bank meet in its first 12 months? What are the typical KPIs that BNM monitors during the post-licence build-out phase and what triggers a supervisory intervention?',
            'What is a systemic risk report for a central bank Board of Governors? What sections must it include, how is systemic risk measured in a small open economy like Malaysia, and what early warning indicators should be highlighted in the current environment of high household debt and NPL pressure?'
          ]
        },
        {
          tool: '🔍 Researcher',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via Microsoft 365 Copilot Chat (copilot.microsoft.com or Teams) > click Agents > Researcher. Grounds answers in live web sources and your organisation data with full citations.',
          prompts: [
            'Research international central bank supervisory practices for managing NPL breaches in the banking system. I need: (1) How comparable regulators (MAS Singapore, BSP Philippines, OJK Indonesia) have responded to system-wide NPL increases, (2) The typical supervisory toolkit used — enhanced monitoring, capital surcharges, lending restrictions, (3) Any research on the effectiveness of different supervisory interventions in reducing NPL. Cite BIS or IMF papers.',
            'Research the digital banking landscape in Malaysia. I need: (1) The 5 licensed digital banks and their operational progress to date, (2) Technology and risk management challenges typical for newly licensed digital banks, (3) How MAS Singapore and BSP Philippines have supervised digital bank post-licence build-outs. Cite official sources and fintech research.'
          ]
        },
        {
          tool: '📊 Analyst',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via Microsoft 365 Copilot Chat > click Agents > Analyst. Upload an Excel or CSV file. Analyst runs Python-style analysis, builds charts, and interprets results without you writing a single formula.',
          prompts: [
            'Upload BNK_02_Meridian_Bank_Strategy.docx (use as banking sector reference). Ask Analyst: Assume a dataset of 18 licensed banks with NPL data by segment. Build a system-wide NPL monitoring dashboard. For each segment (corporate, SME, mortgage, personal loans, auto loans, Islamic), show: (1) Current system NPL %, (2) BNM supervisory threshold, (3) Breach status, (4) 4-quarter trend, (5) Number of institutions above threshold. Identify which segments are breaching or approaching threshold and rank systemic risk from highest to lowest.',
            'Ask Analyst: Model the systemic risk scenario. If the 3 highest-NPL institutions require capital injection: Institution A needs MYR 1.8B, Institution B needs MYR 1.2B, Institution C needs MYR 0.8B. Sources of capital: (1) Existing provisions at 80% coverage, (2) Rights issue (market receptive?), (3) DUITNOW Resolution Fund (limited to MYR 3B). Calculate whether combined capital shortfall can be absorbed without systemic recourse. Show as a stress scenario table.'
          ]
        },
        {
          tool: '📊 Copilot in Excel',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open BNK_02_Meridian_Bank_Strategy.docx in Word and create a companion Excel workbook. Ask Copilot to create: A supervisory monitoring dashboard on Sheet 1. For 18 licensed institutions, show columns: Institution Name | Tier | CET1 Ratio | Tier 1 Capital | Total Capital Ratio | NPL % by segment | LCR | NSFR | Supervisory Status (Normal / Enhanced Monitoring / Corrective Action / Statutory Management) | Action Due Date. Apply conditional formatting: green = normal, amber = enhanced monitoring, red = corrective action or statutory.',
            'Ask Copilot: Create a digital bank operational review scorecard on Sheet 2. For each of the 5 digital banks, show 15 post-licence milestones: Core banking system live (Y/N), BNM supervisory reporting system connected (Y/N), AML/CFT framework operational (Y/N), Customer onboarding live (Y/N), etc. Calculate % completion. Highlight digital banks below 70% completion — flag as "Supervisory Concern".',
            'Ask Copilot: Build a systemic risk indicator dashboard on Sheet 3. Track 10 early warning indicators monthly for the past 24 months: (1) System NPL %, (2) Household debt to GDP %, (3) Bank capital buffers above minimum, (4) FX reserves adequacy (months of import cover), (5) Corporate leverage (net debt/EBITDA), (6) Property price index, (7) MYR exchange rate volatility, (8) Credit growth rate %, (9) Non-bank credit growth, (10) Cross-border capital flow volatility. Show trend charts for each.'
          ]
        },
        {
          tool: '📝 Copilot in Word',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open Email_06_BNM_Regulatory_Correspondence.docx. Ask Copilot: Draft the systemic risk report for the Board of Governors. Structure: (1) Executive Summary — the 3 key systemic risks in the current environment, (2) Banking System Overview — capital adequacy, liquidity, NPL by segment, (3) NPL Deep Dive — personal loan segment breach, 3 institutions at risk, supervisory actions taken, (4) Digital Banking Operational Review — 5 banks, milestone completion status, (5) External Risks — global monetary tightening, US-China trade risks, energy price volatility, (6) Early Warning Dashboard — 10 indicators, current reading vs threshold, (7) Board Decisions Required — approve Enhanced Monitoring for 2 institutions, approve capital adequacy waiver for digital bank X. 20 pages, formal central bank report format.',
            'Ask Copilot: Draft the Enhanced Monitoring notice to Institution A (the institution with 21.7% personal loan NPL). The notice should: state the supervisory concern under IFSA 2013 Section 68, list the 6 specific remediation actions required, set a 90-day timeline for the Corrective Action Plan submission, note that failure to submit will trigger Statutory Management review, and require weekly reporting to the supervisory division. Formal central bank supervisory notice format.',
            'Ask Copilot: Write a public statement on the system-wide NPL situation for BNM\'s website. The statement should: acknowledge the personal loan NPL trend, reassure the public that the banking system remains sound with strong capital buffers (CET1 14.2% system average), note the supervisory actions being taken, and remind consumers of responsible borrowing. 2 paragraphs, measured central bank communication style.'
          ]
        },
        {
          tool: '🎯 Copilot in PowerPoint',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Ask Copilot in PowerPoint: Create a 10-slide Board of Governors briefing on systemic risk. Include: (1) Current risk environment — key global and domestic risks, (2) Banking system health — capital and liquidity, (3) NPL dashboard — system and segment breakdown, (4) Personal loan NPL breach — 3 institutions at risk, (5) Supervisory actions underway, (6) Digital banking operational review, (7) External risk stress test results, (8) Early warning indicator dashboard, (9) Recommended supervisory escalations, (10) Board decisions required. Dark green and white central bank colour scheme.',
            'Ask Copilot: Create a 2-slide NPL situation briefing for a press conference. Slide 1: System NPL is below the crisis threshold — compare Malaysia to regional peers. Slide 2: The personal loan segment is elevated but contained — actions being taken. Frame as a reassurance communication, not alarm.',
            'Ask Copilot: Create a digital bank readiness scorecard slide showing the 5 digital banks on a 1-100 scale across 5 readiness dimensions: Technology Infrastructure, AML/CFT, Customer Onboarding, Capital Adequacy, Regulatory Reporting. Use a radar chart for each bank.'
          ]
        },
        {
          tool: '📧 Copilot in Outlook',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open Email_06_BNM_Regulatory_Correspondence.docx. Ask Copilot: Draft the formal Enhanced Monitoring notification letter to Institution A. The letter must: reference the IFSA 2013 supervisory powers, state the specific concern (personal loan NPL 21.7% vs threshold 3.5%), list 6 mandatory remediation actions with deadlines, require a Corrective Action Plan submission within 90 days, and note the escalation path if actions are not taken. Use BNM formal supervisory letter format.',
            'Ask Copilot: Draft an email to the CEOs of all 18 licensed institutions informing them of the supervisory NPL review and requesting updated NPL data segmented by product type within 5 business days. Formal regulatory request format.',
            'Ask Copilot: Draft an email to BIS (Bank for International Settlements) requesting participation in their next quarterly emerging market banking system stability forum. BNM wishes to present a case study on digital banking supervision in Malaysia. Include a 100-word abstract of our proposed presentation.'
          ]
        },
        {
          tool: '🎙 Copilot in Teams',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Use your OWN existing recorded Teams meetings. Open a meeting recap in Teams > Recap tab. Copilot generates summaries, action items, and follow-up drafts grounded in the actual transcript.',
          prompts: [
            'Open an existing recorded Teams meeting recap from a supervisory review or risk assessment meeting. Ask Copilot: Identify all supervisory decisions made, institutions flagged for review, and any escalations approved. Create a regulatory action tracker.',
            'Ask Copilot: Draft the supervisory team\'s follow-up actions from the NPL review meeting. Group by workstream: Enhanced Monitoring | Corrective Action | Digital Bank Review | Systemic Risk Report | External Communications. Include officer responsible and deadline.',
            'Ask Copilot: Were there any discussions about the 2 digital banks that are behind on their operational milestones? What specific supervisory interventions were discussed and what is the timeline for a formal notice?'
          ]
        },
        {
          tool: '📓 Copilot Notebook',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via copilot.microsoft.com > Notebook tab. Upload up to 5 files and set a system instruction. Best for synthesising insights across multiple documents simultaneously.',
          prompts: [
            'Upload BNK_02_Meridian_Bank_Strategy.docx and Email_06_BNM_Regulatory_Correspondence.docx to Copilot Notebook. Set instruction: "You are a banking supervision specialist advising the central bank on NPL management and systemic risk." Ask: Based on the correspondence and strategy documents, what is the most proportionate supervisory intervention for an institution with 21.7% personal loan NPL — Enhanced Monitoring, Corrective Action Plan, or immediate Statutory Management? What evidence would be needed to justify each level of intervention?',
            'Upload Email_06_BNM_Regulatory_Correspondence.docx. Ask: A digital bank is 9 months into its licence period and has only completed 6 of its 15 post-licence operational milestones. The missing milestones include real-time AML transaction monitoring and stress testing framework. What is the supervisory response — issue a warning, impose a deposit cap, or suspend new customer onboarding? What is the proportionality principle in digital bank supervision?'
          ]
        },
        {
          tool: '🤝 Cowork (Frontier)',
          license: 'M365 Copilot + Frontier Program',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Cowork is an autonomous agent that takes actions across Microsoft 365 on your behalf — sending emails, scheduling meetings, creating documents, posting in Teams, and scheduling recurring tasks. Access: m365.cloud.microsoft > left nav > Agents > Cowork. Requires Frontier program enrollment.',
          prompts: [
            'Do all of the following: (1) Research how MAS Singapore and BSP Philippines have responded to elevated consumer loan NPL in their banking systems in the past 2 years — extract specific supervisory actions taken and outcomes. (2) Draft a 3-page international supervisory benchmarking note for the Governor. (3) Save to OneDrive as "International NPL Supervisory Benchmarking". (4) Email to the Head of Banking Supervision and the Deputy Governor for review. (5) Schedule an urgent supervisory strategy session with the NPL task force.',
            'Do all of the following for the systemic risk report: (1) Research recent IMF Article IV consultation findings on Malaysia\'s banking system and household debt. (2) Extract any IMF or BIS warnings relevant to our current NPL situation. (3) Draft the external risk chapter for the Board of Governors systemic risk report. (4) Save to OneDrive as "Systemic Risk Report - External Risk Chapter". (5) Email to the Research Director asking for review and integration into the full report within 48 hours.'
          ]
        },
        {
          tool: '🤖 Word Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to a Word document. Open the .docx in Word for Web > Copilot pane > + New Agent > name it, write a description, set the document as knowledge source > Share. Colleagues chat with it in Teams or M365 Copilot.',
          prompts: [
            'Open BNK_02_Meridian_Bank_Strategy.docx in Word for Web. Create an agent called "BNM Supervisory Policy Bot". Description: "Assists central bank supervisors with instant answers on IFSA 2013 supervisory powers, Basel III capital requirements, NPL threshold frameworks, digital banking licence conditions, and AML/CFT regulatory obligations." Share with the banking supervision division.',
            'Demo: A junior supervisor asks "An institution has submitted a Corrective Action Plan but has missed 2 of 6 required milestone deadlines. Under IFSA 2013, what are our supervisory options at this point — can we impose conditions on the institution\'s lending activities and what is the due process required before imposing a conditional lending restriction?" Show the agent providing a legally-grounded, proportionate supervisory guidance answer.'
          ]
        },
        {
          tool: '🤖 PowerPoint Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to a PowerPoint presentation. Great for strategy decks or Board presentations many people need to reference. Same setup as Word Agent but using a .pptx file.',
          prompts: [
            'Create a PowerPoint from the Board of Governors briefing. Create an agent called "Systemic Risk Report Q&A Bot". Share with the Board of Governors and senior management.',
            'Demo: A Governor asks "If Institution A fails to meet its NPL remediation targets by the 90-day deadline, what is the supervisory escalation path and what powers does the central bank have under IFSA 2013 to protect depositors?" Show the agent providing a precise, legally-grounded supervisory escalation answer.'
          ]
        },
        {
          tool: '🤖 Excel Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to an Excel workbook. Colleagues ask data questions in plain English without opening Excel. Open .xlsx in Excel for Web > Copilot pane > + New Agent > set workbook as knowledge source > share.',
          prompts: [
            'Create the supervisory monitoring dashboard workbook and open in Excel for Web. Create an agent called "Banking System Supervisory Q&A". Description: "Instant answers on capital ratios, NPL by institution and segment, digital bank readiness, and systemic risk indicators for the Governor, Deputy Governors, and supervisory division heads." Share with senior banking supervision leadership.',
            'Demo: Ask "Which 3 institutions have the highest personal loan NPL and what is the combined capital shortfall if we require provisioning to 100% coverage?" Then: "What is the system-wide CET1 ratio and how does it compare to the regulatory minimum and to MAS Singapore?" Show the Deputy Governor getting instant systemic intelligence.'
          ]
        },
        {
          tool: '🏗 Agent Builder (Copilot Studio)',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Build a custom declarative agent in Copilot Studio — no coding required. Access: copilotstudio.microsoft.com > Create > New Agent. Add name, description, knowledge sources (SharePoint URLs or uploaded files), topics/actions. Publish to Teams in under 10 minutes.',
          prompts: [
            'Go to copilotstudio.microsoft.com > Create > New Agent. Name it "Central Bank Supervisory Intelligence Agent". Description: "Supports the banking supervision division, senior management, and the Board of Governors with instant answers on IFSA 2013 supervisory powers, NPL monitoring thresholds, capital adequacy requirements, digital banking milestones, and systemic risk indicators — enabling faster, more consistent and legally-sound supervisory decisions across 18 licensed financial institutions." Upload BNK_02_Meridian_Bank_Strategy.docx and Email_06_BNM_Regulatory_Correspondence.docx. Add topics: "NPL Supervision", "IFSA Regulatory Powers", "Digital Banking Review", "Systemic Risk". Publish to Teams (restricted to supervisory division only).',
            'Demo the agent: A supervisory officer receives an urgent notification at 6:30am: a licensed bank has just filed a Material Adverse Event report under IFSA, disclosing a cyberattack that compromised customer data and temporarily disabled core banking operations for 4 hours overnight. The officer asks the agent: "What are the mandatory notification timelines under IFSA 2013 and PDPA for a cyberattack at a licensed institution? What supervisory actions must we initiate in the next 24 hours? Does the Governor need to be notified personally?" Show how the agent enables a swift, legally-grounded supervisory response to a banking crisis.'
          ]
        }
      ]
    }
  ],
  departments: [
    {
      id: 'dept-hr',
      sectorId: 'department',
      subsector: '',
      name: 'Human Resources',
      icon: '👥',
      color: '#1565C0',
      accent: '#1976D2',
      company: 'Zava Group Holdings — Group HR Division',
      tagline: '87,000 employees, 32% BPO attrition crisis, ESG DEI targets, plantation replanting displacement.',
      scenario: 'The Group HR Division manages talent strategy, compensation, and people analytics for 87,420 employees across 11 divisions and 3 countries. Critical issues: Bengaluru BPO attrition at 31.2%, plantation estate worker displacement from replanting, Zava Bank losing talent to fintech, and new DEI commitment (40% women leadership by 2028).',
      files: [
        '18_Zava_HR_Analytics.xlsx',
        '02_Zava_Group_Policy_Handbook.docx'
      ],
      prompts: [
        {
          tool: '🤖 Copilot Chat (Basic)',
          license: 'Free — no M365 Copilot license needed',
          account: 'Sasha Ouellet — SashaO@ABSx62256373.OnMicrosoft.com',
          desc: '',
          prompts: [
            'I am the Group CHRO of a Malaysian conglomerate with 87,420 employees. Our BPO division in Bengaluru has 31.2% annual attrition — one of the highest in our group. Research shows the main causes are: IT sector salary competition, limited career progression, and remote work policy restrictions. Draft a 250-word retention strategy brief for the BPO MD covering: 3 immediate retention levers, 2 medium-term structural changes, and how we measure success in 12 months.',
            'What is the HR analytics maturity model and where should a large conglomerate HR function be on that model? We currently use basic headcount and attrition reports. What are the 5 most impactful people analytics use cases for a 87,000-employee conglomerate?',
            'Explain what a 40% women in leadership target means in practice. How do leading Malaysian conglomerates measure "leadership" — is it C-suite only, all management grades, or a specific band? What policies and programmes have proven most effective at closing the gender leadership gap in Asian corporate settings?'
          ]
        },
        {
          tool: '🔍 Researcher',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via Microsoft 365 Copilot Chat (copilot.microsoft.com or Teams) > click Agents > Researcher. Grounds answers in live web sources and your organisation data with full citations.',
          prompts: [
            'Research BPO industry attrition best practices in India (Bengaluru, Hyderabad, Chennai). What attrition benchmarks exist for Malaysian-owned BPO operators in India? What retention programmes have worked for mid-size BPO companies competing with IT majors like Infosys and Wipro? Cite industry reports.',
            'Research DEI (Diversity, Equity, Inclusion) best practices in Malaysian GLCs and conglomerates. What are the most effective programmes for increasing women in senior leadership? How have companies like Maybank, Sime Darby, and Petronas progressed on their DEI targets? Cite MSWG or MyCERT data.'
          ]
        },
        {
          tool: '📊 Analyst',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via Microsoft 365 Copilot Chat > click Agents > Analyst. Upload an Excel or CSV file. Analyst runs Python-style analysis, builds charts, and interprets results without you writing a single formula.',
          prompts: [
            'Upload 18_Zava_HR_Analytics.xlsx to Analyst. Ask: Run an attrition regression analysis. Which factors (salary vs benchmark, commute distance, team size, manager tenure) correlate most strongly with attrition across divisions? For the BPO Bengaluru centre, identify the 3 highest-risk employee segments — rank by predicted attrition probability. Create a risk heatmap: X-axis = grade, Y-axis = years of service.',
            'Upload 18_Zava_HR_Analytics.xlsx. Ask: Build a succession planning gap analysis. For C5-C7 grade positions across the 11 divisions, how many have a ready successor identified vs no successor? Calculate the bench strength ratio (successors/positions). Identify the 5 most critical "succession desert" roles — high business impact, no successor. Create a visual showing the succession pipeline strength by division.'
          ]
        },
        {
          tool: '📊 Copilot in Excel',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open 18_Zava_HR_Analytics.xlsx. Navigate to the Attrition Analysis sheet. Ask Copilot: Build a compensation benchmark dashboard on a new sheet. For each grade (C1-C7) and country (MY, ID, IN), show: (1) Current median salary at Zava, (2) Market median salary (sourced from Aon Hewitt or Mercer benchmark), (3) Compa-ratio (our median / market median), (4) % below market, (5) RAG status: green (90-110% of market), amber (80-89%), red (<80%). Highlight any grade/country where we are more than 15% below market.',
            'Ask Copilot: Create a DEI progress tracker on a new sheet. For each division and each management grade (C5+), show: (1) Total positions, (2) Women in role, (3) Women %, (4) Target %, (5) Gap to target (positions needed). Sum to group level. Calculate how many women need to be promoted to C5+ to reach the 40% target by 2028 — assuming 3% annual promotion pool.',
            'Ask Copilot: Build a learning & development ROI dashboard. For each training programme in FY2024 (leadership, technical, compliance, DEI), show: (1) Participants, (2) Cost per participant (MYR), (3) Total cost (MYR M), (4) 90-day retention rate post-training vs non-participants, (5) Productivity score change (if measured), (6) Estimated ROI. Rank by ROI and flag any programme with negative ROI.'
          ]
        },
        {
          tool: '📝 Copilot in Word',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open 02_Zava_Group_Policy_Handbook.docx. Ask Copilot: Draft a new chapter "AI & Copilot Usage Policy" for the Policy Handbook. Cover: (1) Approved AI tools — Microsoft 365 Copilot and its applications, (2) Prohibited uses — sharing confidential data, generating misleading content, bypassing compliance review, (3) Prompt writing guidelines — GCSE framework, (4) Data classification rules — what data may be used as Copilot context, (5) Responsibility — employee accountability for AI-generated output, (6) Training requirement — all employees must complete the Zava AI Literacy module before using Copilot. 4 pages, policy format.',
            'Ask Copilot: Draft a Group HR communication to all 87,420 employees (filtered for managers C5+) announcing the Microsoft 365 Copilot rollout. The email should: explain what Copilot is in simple terms, note the 3 key benefits for their day-to-day work, announce the training schedule (2-hour mandatory session within 30 days), and share 3 simple use cases from the HR function — drafting JDs, analysing attrition data, and summarising engagement surveys. Engaging, positive tone.',
            'Ask Copilot: Draft the Zava Group FY2025 Annual Workforce Report (30 pages). Cover all sections: Headcount summary by division and country, Attrition analysis, Compensation benchmarking, DEI progress, L&D investment, Safety statistics, Employee engagement score, Talent pipeline, and People strategy outlook. Use data from the HR Analytics file.'
          ]
        },
        {
          tool: '🎯 Copilot in PowerPoint',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Ask Copilot in PowerPoint: Create a 10-slide Group HR presentation for the Board. Include: (1) Workforce overview — 87,420 employees, (2) Attrition crisis — BPO Bengaluru 31.2%, (3) Retention programme — cost and expected impact, (4) Compensation benchmarking — 3 grades below market, (5) DEI progress — 28% women in leadership vs 40% target, (6) L&D investment — ROI by programme, (7) Succession planning — bench strength by division, (8) People analytics upgrade — 3-year roadmap, (9) FY2026 HR priorities, (10) Board decisions. Blue and white colour scheme.',
            'Ask Copilot: Create a 2-slide M365 Copilot for HR use case pitch. Slide 1: 5 HR use cases with Copilot (JD generation, attrition analysis, engagement survey synthesis, policy update drafting, exit interview summarisation) — each with time saved per month. Slide 2: Investment vs time savings ROI calculation — show payback in months.',
            'Ask Copilot: Create a DEI roadmap slide showing the 2025-2028 timeline with 4 milestones: 30% women in leadership (FY2025), 35% (FY2026), 38% (FY2027), 40% (FY2028). Show current position at 28% and the specific programmes at each milestone that will drive progress.'
          ]
        },
        {
          tool: '📧 Copilot in Outlook',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Ask Copilot in Outlook: Draft an email to all BPO Bengaluru team leaders and managers (620 people) announcing the new retention programme. The email should: acknowledge the high attrition and thank existing employees for their commitment, announce the 3 new retention benefits (12-month cliff bonus, remote work 3 days/week, accelerated career track programme), state the effective date (1 month from today), and invite questions at the Q&A session next Friday. Warm, human tone.',
            'Ask Copilot: Draft a targeted email to our 148 employees at Bengaluru who have been with Zava BPO for 3+ years. The email should: personalise the opening ("You have been with us for over 3 years — and that means a great deal"), announce the senior employee retention benefit (additional 10% salary uplift for C2-C3 staff with 3+ years tenure), and express genuine appreciation. CONFIDENTIAL — only for this segment.',
            'Ask Copilot: Draft a letter to the estate worker union representatives at Ladang Sri Murni (Sarawak) regarding the replanting programme that will displace 240 workers for 18 months. The letter should: explain the replanting necessity (aging palms, declining yield), outline the 18-month support package (housing maintained, 85% salary retention), describe the retraining options (machinery operation, safety certification), and note the priority re-hire commitment. Empathetic, respectful tone.'
          ]
        },
        {
          tool: '🎙 Copilot in Teams',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Use your OWN existing recorded Teams meetings. Open a meeting recap in Teams > Recap tab. Copilot generates summaries, action items, and follow-up drafts grounded in the actual transcript.',
          prompts: [
            'Open an existing recorded Teams meeting recap from an HR leadership or town hall meeting. Ask Copilot: Identify all workforce concerns discussed — attrition, compensation, DEI, L&D. Create an action tracker for the CHRO team with owner and deadline.',
            'Ask Copilot: Draft follow-up actions from the quarterly HR leadership review. Group by workstream: Attrition & Retention | Compensation Benchmarking | DEI | L&D | People Analytics. Include HRBP owner and deadline.',
            'Ask Copilot: Were there any discussions about the BNM salary increase for bank officers affecting Zava Bank\'s ability to retain staff? What retention measures were proposed and what is the budget implication?'
          ]
        },
        {
          tool: '📓 Copilot Notebook',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via copilot.microsoft.com > Notebook tab. Upload up to 5 files and set a system instruction. Best for synthesising insights across multiple documents simultaneously.',
          prompts: [
            'Upload 18_Zava_HR_Analytics.xlsx and 02_Zava_Group_Policy_Handbook.docx to Copilot Notebook. Set instruction: "You are the Group CHRO preparing the people strategy for the Board." Ask: Based on the workforce data and company policies, what is the single biggest talent risk facing Zava Group in FY2026? What is the recommended 90-day action plan to address it?',
            'Upload 18_Zava_HR_Analytics.xlsx. Ask: Our replacement cost is MYR 1.5x annual salary per departing employee. The Bengaluru BPO has 2,960 staff with 31.2% attrition. Calculate the annual turnover cost. If a retention programme costing MYR 8.4M reduces attrition to 22%, calculate the net saving and the ROI of the retention investment.'
          ]
        },
        {
          tool: '🤝 Cowork (Frontier)',
          license: 'M365 Copilot + Frontier Program',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Cowork is an autonomous agent that takes actions across Microsoft 365 on your behalf — sending emails, scheduling meetings, creating documents, posting in Teams, and scheduling recurring tasks. Access: m365.cloud.microsoft > left nav > Agents > Cowork. Requires Frontier program enrollment.',
          prompts: [
            'Do all of the following: (1) Research salary benchmarks for BPO analysts and senior analysts in Bengaluru for 2025 — compare to Infosys, Wipro, and TCS. (2) Identify the 3 salary grades where Zava BPO is most below market. (3) Draft a compensation correction proposal for CFO approval — estimated cost MYR 14.2M annually. (4) Email to CHRO and CFO asking for an urgent review before the Q2 compensation review cycle. (5) Schedule a compensation committee meeting within 2 weeks.',
            'Do all of the following for DEI: (1) Research the most effective sponsorship and mentoring programmes for women in leadership in Malaysian corporates. (2) Draft a "Zava Women in Leadership" programme design covering: sponsorship programme, accelerated development track, external Board director placement, and flexible work policy. (3) Save to OneDrive as "Zava Women in Leadership Programme". (4) Email to the CHRO and Group CEO for approval. (5) Schedule a DEI taskforce kickoff meeting with Division HRBPs.'
          ]
        },
        {
          tool: '🤖 Word Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to a Word document. Open the .docx in Word for Web > Copilot pane > + New Agent > name it, write a description, set the document as knowledge source > Share. Colleagues chat with it in Teams or M365 Copilot.',
          prompts: [
            'Open 02_Zava_Group_Policy_Handbook.docx in Word for Web. Create an agent called "Zava Group HR Policy Bot". Description: "Answers questions from managers, HRBPs, and employees across all 11 divisions on HR policies, compensation bands, leave entitlements, performance management, DEI commitments, and people processes — ensuring consistent policy application across 87,420 employees." Share with all 11 Division HRBPs and publish to the employee portal.',
            'Demo: A Line Manager at Zava Bank asks "I want to put my team member on a Performance Improvement Plan (PIP). She has been underperforming for 3 months but she is also 4 months pregnant. What are the HR policy requirements for issuing a PIP, and are there any special considerations or protections that apply during pregnancy?" Show how the agent provides a policy-grounded, legally-aware HR guidance answer that protects both the employee and the company.'
          ]
        },
        {
          tool: '🤖 PowerPoint Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to a PowerPoint presentation. Great for strategy decks or Board presentations many people need to reference. Same setup as Word Agent but using a .pptx file.',
          prompts: [
            'Create a PowerPoint from the Board HR presentation. Create an agent called "Group HR Board Q&A Bot". Share with Board members and the Group CEO.',
            'Demo: A Board member asks "Our BPO Bengaluru attrition is the highest in the group. If it stays at 31.2%, how long until we lose the senior talent required to maintain the PETRONAS Chemicals BPO contract — and what is the revenue risk?" Show the agent providing a workforce-risk-to-commercial-risk answer.'
          ]
        },
        {
          tool: '🤖 Excel Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to an Excel workbook. Colleagues ask data questions in plain English without opening Excel. Open .xlsx in Excel for Web > Copilot pane > + New Agent > set workbook as knowledge source > share.',
          prompts: [
            'Open 18_Zava_HR_Analytics.xlsx in Excel for Web. Create an agent called "Group HR Analytics Q&A". Description: "Instant answers on headcount, attrition, compensation benchmarking, DEI progress, and L&D ROI for the CHRO, Group CEO, and Division HRBPs." Share with HR leadership.',
            'Demo: Ask "Which division has the highest attrition-related replacement cost this year and what is the MYR amount?" Then: "How many women are currently in C5+ leadership roles and how many more need to be promoted each year to reach the 40% target by 2028?" Show the CHRO getting instant people analytics intelligence.'
          ]
        },
        {
          tool: '🏗 Agent Builder (Copilot Studio)',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Build a custom declarative agent in Copilot Studio — no coding required. Access: copilotstudio.microsoft.com > Create > New Agent. Add name, description, knowledge sources (SharePoint URLs or uploaded files), topics/actions. Publish to Teams in under 10 minutes.',
          prompts: [
            'Go to copilotstudio.microsoft.com > Create > New Agent. Name it "Zava Group HR Intelligence Agent". Description: "The Group HR team\'s intelligent assistant — answers questions on workforce analytics, policy interpretation, compensation benchmarking, DEI progress, and talent risk across all 11 divisions and 87,420 employees. Helps HR leaders make faster, more consistent, data-driven people decisions." Upload 18_Zava_HR_Analytics.xlsx and 02_Zava_Group_Policy_Handbook.docx. Add topics: "Compensation & Benefits", "Attrition & Retention", "DEI", "Policy Guidance", "Succession Planning". Publish to Teams for HR leaders.',
            'Demo the agent: The CHRO is in a Board meeting when a director asks an unexpected question: "We have 87,420 employees but our revenue per employee is only MYR 513K — how does that compare to similar conglomerates and which of our 11 divisions is the most and least productive on a revenue-per-employee basis?" The CHRO discreetly asks the HR agent on their phone and gets an instant, data-backed answer to share with the Board.'
          ]
        }
      ]
    },
    {
      id: 'dept-finance',
      sectorId: 'department',
      subsector: '',
      name: 'Finance & Treasury',
      icon: '💰',
      color: '#1B5E20',
      accent: '#2E7D32',
      company: 'Zava Group Holdings — Group Finance Division',
      tagline: 'MYR 18.4B net debt, FOREX hedging 11 currencies, NPL breach remediation, REIT IPO structuring.',
      scenario: 'The Group Finance Division manages group treasury, reporting, tax, and investor relations. Net debt is MYR 18.4B at 0.82x gearing. FOREX exposure spans MYR, IDR, USD, SGD, INR, and 6 other currencies. Group CFO Hadar Caspit is preparing the FY2025 half-year results, the REIT IPO financial model, and the BNM remediation plan for Zava Bank.',
      files: [
        '01_Zava_Group_Financial_Performance.xlsx',
        '03_Zava_Group_Strategy_Framework.docx'
      ],
      prompts: [
        {
          tool: '🤖 Copilot Chat (Basic)',
          license: 'Free — no M365 Copilot license needed',
          account: 'Sasha Ouellet — SashaO@ABSx62256373.OnMicrosoft.com',
          desc: '',
          prompts: [
            'I am the Group CFO of a MYR 44.8B revenue conglomerate with MYR 18.4B net debt. Our gearing is 0.82x net debt/EBITDA. Our debt covenants require us to maintain gearing below 3.5x on a net debt/EBITDA basis — we are well within that. However, 2 divisions are underperforming and the Zava Bank NPL issue has increased provisioning costs by MYR 420M. Draft a 250-word brief for the Board\'s Audit Committee covering: (1) The current group financial position, (2) The impact of Zava Bank provisioning on group PAT, (3) The FOREX exposure — 11 currencies, largest being IDR (MYR 2.1B equivalent), (4) The hedge ratio and our FOREX hedging strategy.',
            'Explain how a conglomerate treasury manages FOREX risk across 11 operating currencies. What is a natural hedge and when is it insufficient? What derivative instruments (forwards, options, cross-currency swaps) are appropriate for each currency pair in a Malaysian conglomerate with significant IDR and USD exposure?',
            'What is a REIT IPO financial model? How does a property company calculate the NAV per unit, distribution per unit (DPU), and target IPO price for a REIT? What are the key inputs — NOI, cap rate, gearing, distribution rate — and how does the REIT IPO price relate to NAV?'
          ]
        },
        {
          tool: '🔍 Researcher',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via Microsoft 365 Copilot Chat (copilot.microsoft.com or Teams) > click Agents > Researcher. Grounds answers in live web sources and your organisation data with full citations.',
          prompts: [
            'Research the current Malaysian ringgit (MYR) and Indonesian rupiah (IDR) outlook for FY2025-FY2026. I need: (1) Consensus MYR/USD and IDR/USD forecasts from investment banks, (2) Key risk factors — US Fed policy, Bank Negara Malaysia stance, oil prices, (3) How other Malaysian conglomerates with significant IDR exposure are managing FOREX risk. Cite Bloomberg consensus or investment bank research.',
            'Research FY2025 earnings guidance trends for Malaysian listed conglomerates. What are analysts saying about Sime Darby, IOI, and IHH in terms of earnings recovery? How is the plantation sector expected to perform given CPO price movements? Cite broker research or Bloomberg.'
          ]
        },
        {
          tool: '📊 Analyst',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via Microsoft 365 Copilot Chat > click Agents > Analyst. Upload an Excel or CSV file. Analyst runs Python-style analysis, builds charts, and interprets results without you writing a single formula.',
          prompts: [
            'Upload 01_Zava_Group_Financial_Performance.xlsx to Analyst. Ask: Build a group financial performance dashboard. For FY2022, FY2023, FY2024, and FY2025 YTD: (1) Revenue by division, (2) EBITDA by division, (3) EBITDA margin %, (4) PAT, (5) PATAMI. Create a waterfall chart showing the FY2023-to-FY2024 EBITDA bridge by division — show which divisions contributed positively and which negatively to the change. Highlight the Zava Bank provisioning impact in a separate bar.',
            'Upload 01_Zava_Group_Financial_Performance.xlsx. Ask: Run 3 FY2025 full-year scenarios: (A) Base — all divisions at current trajectory, (B) Bear — Zava Bank NPL worsens by 30%, CPO price -10%, IDR weakens 8% vs MYR, (C) Bull — Zava Bank NPL stabilises, CPO price +15%, IDR stable. For each scenario, calculate: group revenue, EBITDA, PATAMI, EPS, net gearing, and interest coverage ratio. Show as a 3-column comparison table.'
          ]
        },
        {
          tool: '📊 Copilot in Excel',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open 01_Zava_Group_Financial_Performance.xlsx. Navigate to the Group P&L sheet. Ask Copilot: Build a FOREX sensitivity analysis on a new sheet. Show the group PATAMI impact of currency movements: MYR/USD ±5%, IDR/MYR ±5%, INR/MYR ±5%, SGD/MYR ±3%. Create a 2-dimensional sensitivity table: Y-axis = MYR/USD movement (-10% to +10%), X-axis = IDR/MYR movement (-10% to +10%). Each cell shows PATAMI impact in MYR M. Highlight cells where PATAMI drops >10% in red.',
            'Ask Copilot: In the Balance Sheet sheet, calculate the group net gearing under 3 scenarios: (1) REIT IPO proceeds MYR 3.2B used to pay down debt, (2) No REIT IPO, (3) REIT IPO proceeds reinvested in new assets. For each scenario, calculate: net debt, EBITDA, net gearing ratio, and debt covenant headroom. Show side-by-side. Highlight any scenario that breaches the 3.5x covenant.',
            'Ask Copilot: Build a half-year earnings release model. Using the FY2024 actuals and H1 FY2025 data, draft the P&L for H1 FY2025 showing: revenue growth vs H1 FY2024, EBITDA margin expansion/contraction, exceptional items (Zava Bank provision), and PATAMI. Add analyst consensus comparison column. Flag any line where we are >5% below consensus in red.'
          ]
        },
        {
          tool: '📝 Copilot in Word',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open 03_Zava_Group_Strategy_Framework.docx. Ask Copilot: Draft the Group CFO\'s commentary for the H1 FY2025 financial results announcement. The commentary should: (1) Open with the group headline — revenue, EBITDA, and PATAMI, (2) Explain the Zava Bank provisioning impact — transparent but measured, (3) Comment on CPO price tailwinds for the Agribusiness division, (4) Note the Manufacturing division\'s OEE improvement programme, (5) Provide FY2025 full-year guidance — revenue growth 4-6%, EBITDA margin 15.5-16.5%. Tone: confident, transparent, and forward-looking. Analyst investor communication style.',
            'Ask Copilot: Draft the Group Treasury Policy update paper for the Finance Committee. Propose: (1) Updated FOREX hedge ratio targets (from current 60% to 75% of 12-month FOREX exposure), (2) Centralisation of IDR hedging — all 5 Indonesian divisions to use the Group Treasury desk, (3) New derivative instruments to be approved — USD put options for plantation USD revenue, (4) Updated counterparty limits for derivative transactions. 5 pages, formal committee paper.',
            'Ask Copilot: Draft the investor Q&A preparation document for the H1 FY2025 results briefing. Anticipate the 10 most likely analyst questions (Zava Bank NPL, commodity price outlook, REIT IPO timeline, debt reduction plan, FY2025 guidance). For each question, provide a suggested 2-3 sentence answer. This is an internal briefing tool for the CFO and IR team.'
          ]
        },
        {
          tool: '🎯 Copilot in PowerPoint',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Ask Copilot in PowerPoint: Create a 14-slide H1 FY2025 results investor presentation. Include: (1) H1 headline — revenue, EBITDA, PATAMI, (2) Group financial highlights, (3) Division performance — revenue and EBITDA by division, (4) Zava Bank — NPL situation and provisioning, (5) Agribusiness — CPO production and price, (6) FOREX exposure and hedge ratio, (7) Balance sheet and gearing, (8) REIT IPO — timeline and expected proceeds, (9) Capital allocation — FY2025-2026 capex, (10) FY2025 full-year guidance, (11) Dividend — DPS and yield, (12) ESG highlight, (13) Analyst consensus vs actual, (14) Q&A slide. Standard investor presentation format.',
            'Ask Copilot: Create a 3-slide REIT IPO investor teaser. Slide 1: Asset overview — 12 REIT-eligible assets, MYR 8.2B. Slide 2: Key investment highlights — NPI yield, WALE, occupancy. Slide 3: Transaction overview — IPO structure, indicative timeline, expected DPU yield.',
            'Ask Copilot: Create a slide showing the FY2025 guidance visual — a bridge from H1 actuals to the full-year guidance range. Show the key drivers: Agribusiness CPO second half, Manufacturing recovery, BPO revenue growth, offset by Bank provisioning. Use a waterfall chart format.'
          ]
        },
        {
          tool: '📧 Copilot in Outlook',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Ask Copilot in Outlook: Draft the H1 FY2025 results analyst briefing invitation. Send to 48 analysts covering Zava Group on Bursa Malaysia and IDX Jakarta. The invitation should: confirm the date/time/format (in-person KL + virtual), note the pre-results quiet period (no discussion of financial performance), attach the results presentation and press release (redacted — placeholders only), and provide the audio webcast link. Include a Q&A session calendar invite.',
            'Ask Copilot: Draft the Group CFO\'s email to all Division CFOs ahead of the H1 FY2025 results. The email should: confirm the group financial position, note the 3 key messages for the H1 announcement, remind all Division CFOs that no divisional results should be shared externally before the Bursa announcement, and request final division P&L sign-off by end of business tomorrow.',
            'Ask Copilot: Draft a letter to the 3 lead relationship banks (CIMB, Maybank, and Hong Leong Bank) providing the semi-annual covenant compliance certificate for the MYR 6.4B revolving credit facility. Confirm: net gearing 0.82x vs covenant 3.5x, interest coverage 4.8x vs covenant 2.5x, EBITDA MYR 7.2B vs minimum MYR 4.8B. All covenants satisfied.'
          ]
        },
        {
          tool: '🎙 Copilot in Teams',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Use your OWN existing recorded Teams meetings. Open a meeting recap in Teams > Recap tab. Copilot generates summaries, action items, and follow-up drafts grounded in the actual transcript.',
          prompts: [
            'Open an existing recorded Teams meeting recap from a finance or CFO leadership meeting. Ask Copilot: Identify all financial performance concerns discussed, FOREX positions flagged, and decisions made about debt management or investor communications. Create an action tracker.',
            'Ask Copilot: Draft the Group Finance weekly update for the CFO. Structure: (1) Cash position and liquidity, (2) FOREX movements this week vs hedge positions, (3) Division P&L variance vs budget — top 3 movers, (4) Zava Bank NPL status, (5) REIT IPO progress, (6) Upcoming investor/analyst engagements.',
            'Ask Copilot: From this meeting transcript, what was decided about the Group Treasury\'s proposed IDR hedge ratio increase? What concerns did the Division CFOs raise about the centralised hedging model?'
          ]
        },
        {
          tool: '📓 Copilot Notebook',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via copilot.microsoft.com > Notebook tab. Upload up to 5 files and set a system instruction. Best for synthesising insights across multiple documents simultaneously.',
          prompts: [
            'Upload 01_Zava_Group_Financial_Performance.xlsx and 03_Zava_Group_Strategy_Framework.docx to Copilot Notebook. Set instruction: "You are advising the Group CFO on H1 FY2025 results communication." Ask: Based on the financial data and strategy, what is the single most important narrative the CFO must control in the H1 FY2025 analyst briefing? What is the question that analysts will ask that poses the biggest risk and what is the best answer?',
            'Upload 01_Zava_Group_Financial_Performance.xlsx. Ask: The group is targeting FY2025 PATAMI growth of 8-12%. With Zava Bank provisioning MYR 420M above budget, is this guidance achievable? Which divisions must outperform their H2 budget to offset the Bank shortfall? Quantify the required outperformance for each division.'
          ]
        },
        {
          tool: '🤝 Cowork (Frontier)',
          license: 'M365 Copilot + Frontier Program',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Cowork is an autonomous agent that takes actions across Microsoft 365 on your behalf — sending emails, scheduling meetings, creating documents, posting in Teams, and scheduling recurring tasks. Access: m365.cloud.microsoft > left nav > Agents > Cowork. Requires Frontier program enrollment.',
          prompts: [
            'Do all of the following for H1 results preparation: (1) Research what analyst consensus is for Zava Group\'s H1 FY2025 results based on publicly available broker estimates. (2) Draft the key messages document for the H1 investor briefing. (3) Create a Q&A preparation document with 12 anticipated questions and suggested answers. (4) Email to CFO and Head of Investor Relations for review. (5) Schedule the results analyst briefing and create the Teams webcast event.',
            'Do all of the following for treasury: (1) Research current MYR/IDR cross rate and 12-month forward rate from Bloomberg. (2) Calculate the unhedged IDR exposure impact on group PATAMI if IDR weakens 8% over 12 months. (3) Draft a hedging recommendation paper for the Finance Committee. (4) Email to the Group Treasurer asking for market data validation. (5) Schedule an urgent Finance Committee call to approve the updated hedge ratio.'
          ]
        },
        {
          tool: '🤖 Word Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to a Word document. Open the .docx in Word for Web > Copilot pane > + New Agent > name it, write a description, set the document as knowledge source > Share. Colleagues chat with it in Teams or M365 Copilot.',
          prompts: [
            'Open 03_Zava_Group_Strategy_Framework.docx in Word for Web. Create an agent called "Group Finance & Strategy Q&A Bot". Description: "Supports the Group Finance team and Division CFOs with instant answers on group financial policies, FOREX hedging guidelines, covenant requirements, REIT IPO structuring, and investor communication protocols." Share with all Division CFOs.',
            'Demo: A Division CFO asks "We have a USD 12M receivable from a US customer due in 90 days. Should I hedge this at the Group Treasury desk or manage it ourselves? What is the Group Treasury Policy on Division-level FOREX hedging and what are the authorised instruments?" Show the agent providing a treasury-policy-grounded answer.'
          ]
        },
        {
          tool: '🤖 PowerPoint Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to a PowerPoint presentation. Great for strategy decks or Board presentations many people need to reference. Same setup as Word Agent but using a .pptx file.',
          prompts: [
            'Create a PowerPoint from the H1 results investor presentation. Create an agent called "Zava Group Investor Relations Q&A Bot". Share with analysts, fund managers, and the IR team.',
            'Demo: An analyst asks "What is the Group\'s sensitivity to a 10% decline in CPO prices and how would that affect FY2025 PATAMI guidance? Also, at what gearing level would you need to cut the dividend?" Show the agent providing a financial model-grounded investor Q&A answer.'
          ]
        },
        {
          tool: '🤖 Excel Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to an Excel workbook. Colleagues ask data questions in plain English without opening Excel. Open .xlsx in Excel for Web > Copilot pane > + New Agent > set workbook as knowledge source > share.',
          prompts: [
            'Open 01_Zava_Group_Financial_Performance.xlsx in Excel for Web. Create an agent called "Group Finance Performance Q&A". Description: "Instant answers on group P&L, EBITDA by division, FOREX sensitivity, gearing, covenant headroom, and REIT IPO financials for the CFO, Group CEO, and Division CFOs." Share with Group Finance leadership.',
            'Demo: Ask "What is the group net gearing now and what would it be after REIT IPO proceeds are used to repay debt?" Then: "Which 3 divisions are most below their H1 FY2025 EBITDA budget and by how much in MYR M?" Show the CFO getting instant group financial intelligence.'
          ]
        },
        {
          tool: '🏗 Agent Builder (Copilot Studio)',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Build a custom declarative agent in Copilot Studio — no coding required. Access: copilotstudio.microsoft.com > Create > New Agent. Add name, description, knowledge sources (SharePoint URLs or uploaded files), topics/actions. Publish to Teams in under 10 minutes.',
          prompts: [
            'Go to copilotstudio.microsoft.com > Create > New Agent. Name it "Zava Group Finance Intelligence Agent". Description: "The Group CFO\'s intelligent assistant — provides instant answers on group P&L performance, FOREX exposure, covenant compliance, REIT IPO financial modelling, investor communication requirements, and divisional financial KPIs. Supports faster, more data-driven financial decision-making across the Zava Group." Upload 01_Zava_Group_Financial_Performance.xlsx and 03_Zava_Group_Strategy_Framework.docx. Add topics: "Group P&L", "FOREX & Treasury", "REIT IPO", "Investor Relations", "Covenants". Publish to Teams for Group Finance leadership.',
            'Demo the agent: The Group CFO is at a dinner with Malaysia\'s largest institutional fund manager, who asks unexpectedly: "I\'m thinking of increasing my position in Zava Group but I\'m worried about the Zava Bank NPL exposure. Can you walk me through the worst-case provisioning scenario and confirm that your MYR 6.4B RCF has no cross-default clause linked to Zava Bank\'s NPL ratio?" The CFO discreetly asks the Finance agent on their phone and gets a precise, numbers-backed answer to continue the investor conversation with confidence.'
          ]
        }
      ]
    },
    {
      id: 'dept-legal',
      sectorId: 'department',
      subsector: '',
      name: 'Legal & Corporate Secretarial',
      icon: '⚖️',
      color: '#4A148C',
      accent: '#6A1B9A',
      company: 'Zava Group Holdings — Group Legal Division',
      tagline: 'NDA pipeline, JV agreements, Bursa disclosures, BPOM/BNM regulatory response management.',
      scenario: 'The Group Legal Division manages contract review, regulatory compliance, M&A legal support, and corporate secretarial obligations for the dual-listed Zava Group (Bursa Malaysia + IDX Jakarta). Current workload includes 14 active NDAs, 3 JV agreement negotiations, 2 regulatory responses (BNM and BPOM), and an upcoming Bursa Malaysia circular for shareholder approval of the REIT IPO.',
      files: [
        '02_Zava_Group_Policy_Handbook.docx',
        'Email_07_Emergency_Board_Meeting.docx'
      ],
      prompts: [
        {
          tool: '🤖 Copilot Chat (Basic)',
          license: 'Free — no M365 Copilot license needed',
          account: 'Sasha Ouellet — SashaO@ABSx62256373.OnMicrosoft.com',
          desc: '',
          prompts: [
            'I am the Group General Counsel of a dual-listed ASEAN conglomerate. We have 3 concurrent JV agreement negotiations — in Indonesia (property development), Singapore (commodity trading), and India (BPO). Draft a 250-word brief for our legal team on: (1) The 3 most critical clauses in any JV agreement that must be negotiated from strength, (2) How deadlock resolution mechanisms differ between MY, ID, and SG legal frameworks, (3) The typical timeline and process for Bursa Malaysia approval of a material JV transaction.',
            'What are a listed company\'s disclosure obligations on Bursa Malaysia when it enters into a material transaction? What is the threshold for "interested person transactions" and when is shareholder approval required? How does this differ from the equivalent IDX (Indonesia Stock Exchange) requirement?',
            'Explain GDPR vs Malaysia PDPA vs Indonesia UU PDP differences in terms of data processor obligations, cross-border transfer restrictions, and breach notification requirements. Which applies to Zava Group given our MYR 45B revenue across MY and ID?'
          ]
        },
        {
          tool: '🔍 Researcher',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via Microsoft 365 Copilot Chat (copilot.microsoft.com or Teams) > click Agents > Researcher. Grounds answers in live web sources and your organisation data with full citations.',
          prompts: [
            'Research the legal framework for cross-border M&A transactions involving Malaysian and Indonesian companies. What are the key regulatory approvals required (MIDA, BKPM, competition authorities)? What deal structures are commonly used to navigate foreign ownership restrictions in Indonesia? Cite legal sources.',
            'Research the latest Malaysia Anti-Corruption Commission (MACC) guidelines for corporate compliance. What are the requirements under Section 17A of the MACC Act 2009 for GLCs and listed companies? What are the key elements of an "adequate procedures" compliance programme? Cite official MACC resources.'
          ]
        },
        {
          tool: '📊 Analyst',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via Microsoft 365 Copilot Chat > click Agents > Analyst. Upload an Excel or CSV file. Analyst runs Python-style analysis, builds charts, and interprets results without you writing a single formula.',
          prompts: [
            'Upload 02_Zava_Group_Policy_Handbook.docx (use as reference). Ask Analyst to help structure: Build a legal matter tracking model. For 14 active NDAs: categorise by counterparty risk (high/medium/low), expiry date, and whether a renewal or escalation to full agreement is needed. For 3 JV agreements: calculate negotiation timeline, key milestone dates, and risk-weighted deal value. Show as a prioritised legal workload matrix.',
            'Ask Analyst: Build a regulatory response timeline model. For the BNM remediation plan (90-day deadline, 6 action items) and the BPOM corrective action plan (60-day deadline, 8 action items), create a Gantt chart showing all tasks, dependencies, responsible parties, and completion %. Flag any task on the critical path that risks missing the regulatory deadline.'
          ]
        },
        {
          tool: '📊 Copilot in Excel',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open 02_Zava_Group_Policy_Handbook.docx. Create a companion Legal Matter Tracker workbook. Ask Copilot: Create Sheet 1 with columns: Matter | Type (NDA/JV/Regulatory/Litigation) | Division | Counterparty | Status | Key Risk | Next Action | Deadline | External Counsel | Estimated Cost (MYR M). Add conditional formatting: red = overdue, amber = due within 7 days, green = on track. Sort by deadline.',
            'Ask Copilot: Create a Bursa Disclosure Calendar on Sheet 2. For each material transaction or event requiring Bursa announcement (REIT IPO circular, JV agreements, Board changes, results announcements, dividend declarations), show: event, Bursa deadline, draft due from Legal, Board approval date, expected announcement date. Highlight any where Legal\'s internal deadline has passed.',
            'Ask Copilot: Build a contract expiry tracker on Sheet 3. For all major contracts — BPO client agreements, plant offtake agreements, banking facilities, insurance policies — show: contract party, division, value (MYR M), expiry date, auto-renewal clause (Y/N), renegotiation lead time needed (months), action status. Flag contracts expiring within 6 months with no renegotiation started.'
          ]
        },
        {
          tool: '📝 Copilot in Word',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open 02_Zava_Group_Policy_Handbook.docx. Ask Copilot: Review the Data Privacy & Cybersecurity Policy section. Identify: (1) Any gaps vs the new Malaysia PDPA 2024 amendments, (2) Any gaps vs Indonesia\'s UU PDP 2022, (3) Recommended policy updates for each gap. Present as a gap analysis table: Current Policy Clause | Gap | Required Update | Urgency (High/Medium/Low).',
            'Ask Copilot: Draft a template Non-Disclosure Agreement for Zava Group. The NDA should: cover bilateral confidentiality, define confidential information broadly (including oral disclosures with 48-hour written confirmation), include a 3-year confidentiality period post-termination, specify Malaysian law and KL courts as jurisdiction, and include a specific carve-out for information required by Bursa Malaysia or IDX disclosure obligations. 4-page formal NDA.',
            'Open Email_07_Emergency_Board_Meeting.docx. Ask Copilot: Draft the Board resolution for the emergency meeting. The resolution should: confirm quorum, approve the 3 decisions required (coal trading breach remediation plan, Zava Bank corrective action plan, REIT IPO timeline approval), and record the Director votes. Use standard Malaysian Board resolution format.'
          ]
        },
        {
          tool: '🎯 Copilot in PowerPoint',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Ask Copilot in PowerPoint: Create a 5-slide Group Legal & Compliance quarterly update for the Board Audit Committee. Include: (1) Litigation risk register — 8 matters, quantum, and provision status, (2) Regulatory compliance status — BNM, BPOM, Bursa, MACC, (3) M&A legal workstream — 3 JV agreements, status, (4) Data privacy — PDPA/UU PDP compliance rating, (5) Legal spend vs budget. Purple and white colour scheme.',
            'Ask Copilot: Create a 2-slide MACC Section 17A compliance overview for the Audit Committee. Slide 1: What is "adequate procedures" under Section 17A and our current compliance rating. Slide 2: The 3 actions required to strengthen our anti-corruption programme before the annual compliance assessment.',
            'Ask Copilot: Create a Bursa Malaysia disclosure timeline slide for the REIT IPO. Show: all required Bursa filings, shareholder circular deadlines, SC application timeline, expected announcement dates, and the final IPO day. As a horizontal timeline visual.'
          ]
        },
        {
          tool: '📧 Copilot in Outlook',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Ask Copilot in Outlook: Draft the legal instruction letter to our external counsel (Skrine & Co) on the Indonesia JV agreement negotiation. The letter should: confirm the commercial terms agreed by the business (50:50 equity, Zava as managing partner, 10-year term), instruct counsel to draft the JV agreement, highlight 3 non-negotiable clauses (drag-along rights, deadlock by third-party arbitration, ASEAN ADRIC rules), and set the first draft deadline at 3 weeks.',
            'Ask Copilot: Draft a cease-and-desist letter to a competitor who has been using Zava Group\'s registered trademark "ZavaGen" for pharmaceutical products without licence. The letter should: identify the trademark registration details, describe the infringing use, demand immediate cessation within 14 days, and note that legal proceedings will be commenced if the demand is not complied with.',
            'Ask Copilot: Draft the Group General Counsel\'s email to all Division Legal Heads reminding them of the updated Delegation of Authority for contract signing. Specifically: all JV agreements above MYR 50M require Group GC and Group CEO sign-off; all NDAs may be signed by Division MD. Attach the updated DOA matrix as reference.'
          ]
        },
        {
          tool: '🎙 Copilot in Teams',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Use your OWN existing recorded Teams meetings. Open a meeting recap in Teams > Recap tab. Copilot generates summaries, action items, and follow-up drafts grounded in the actual transcript.',
          prompts: [
            'Open an existing recorded Teams meeting recap from a legal or risk committee meeting. Ask Copilot: Identify all legal matters discussed — active litigations, regulatory deadlines, JV negotiation issues. Create an action tracker with the legal team owner and deadline for each item.',
            'Ask Copilot: Draft the post-meeting legal team tasks from the regulatory response review. Group by matter: BNM Response | BPOM Corrective Action | Bursa Circular | MACC Compliance. Include responsible lawyer and deadline.',
            'Ask Copilot: Were there any discussions about the coal trading breach and potential securities disclosure obligations? What was the General Counsel\'s advice on timing of the Bursa announcement?'
          ]
        },
        {
          tool: '📓 Copilot Notebook',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via copilot.microsoft.com > Notebook tab. Upload up to 5 files and set a system instruction. Best for synthesising insights across multiple documents simultaneously.',
          prompts: [
            'Upload 02_Zava_Group_Policy_Handbook.docx and Email_07_Emergency_Board_Meeting.docx to Copilot Notebook. Set instruction: "You are advising the Group GC on legal risk management for the Board emergency meeting." Ask: What are the top 3 legal risks the Board must be advised of at Monday\'s emergency meeting? For each, what is the maximum exposure and what immediate action should the Board authorise?',
            'Upload 02_Zava_Group_Policy_Handbook.docx. Ask: Our anti-bribery policy requires all Zava employees and agents to complete annual MACC training. We have 87,420 employees. Only 62% have completed this year\'s training. Does this incomplete compliance constitute a "failure of adequate procedures" under MACC Section 17A? What is the legal risk and what remedial action is needed within 30 days?'
          ]
        },
        {
          tool: '🤝 Cowork (Frontier)',
          license: 'M365 Copilot + Frontier Program',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Cowork is an autonomous agent that takes actions across Microsoft 365 on your behalf — sending emails, scheduling meetings, creating documents, posting in Teams, and scheduling recurring tasks. Access: m365.cloud.microsoft > left nav > Agents > Cowork. Requires Frontier program enrollment.',
          prompts: [
            'Do all of the following: (1) Research MACC Section 17A adequate procedures guidelines and the latest 2024 updates. (2) Audit our 02_Zava_Group_Policy_Handbook.docx anti-bribery chapter against the 5 required adequate procedures pillars. (3) Draft a gap analysis and remediation plan for any missing elements. (4) Save to OneDrive as "MACC Section 17A Compliance Audit". (5) Email to GC and CFO requesting urgent review before the Board audit committee meeting.',
            'Do all of the following for the JV agreement: (1) Research the key legal requirements for a 50:50 JV company registration in Indonesia (PT PMA). (2) Draft a term sheet for the Indonesia JV based on the agreed commercial terms. (3) Email to external counsel requesting confirmation that the term sheet is consistent with Indonesian company law. (4) Create a JV legal project folder in SharePoint. (5) Schedule a weekly JV legal steering meeting until signing.'
          ]
        },
        {
          tool: '🤖 Word Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to a Word document. Open the .docx in Word for Web > Copilot pane > + New Agent > name it, write a description, set the document as knowledge source > Share. Colleagues chat with it in Teams or M365 Copilot.',
          prompts: [
            'Open 02_Zava_Group_Policy_Handbook.docx in Word for Web. Create an agent called "Zava Group Legal & Compliance Policy Bot". Description: "Answers questions from Zava employees, managers, and Division legal teams on anti-bribery policy, data privacy obligations, contract signing authority, Bursa disclosure requirements, and legal compliance procedures." Share with all Division legal teams and publish to the employee portal.',
            'Demo: A senior manager asks "A government procurement officer has invited me to a golf day organised by the government — value approximately MYR 800. Under our Gifts & Hospitality Policy, can I accept? And do I need to declare it even if I decline?" Show the agent providing a precise, policy-grounded anti-bribery compliance answer.'
          ]
        },
        {
          tool: '🤖 PowerPoint Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to a PowerPoint presentation. Great for strategy decks or Board presentations many people need to reference. Same setup as Word Agent but using a .pptx file.',
          prompts: [
            'Create a PowerPoint from the Board legal update. Create an agent called "Group Legal Update Q&A Bot". Share with the Audit Committee and Board.',
            'Demo: An Audit Committee member asks "What is our total litigation exposure across all 8 active matters and how much have we provisioned vs the risk-weighted exposure? Are any of the 8 matters potentially material enough to require Bursa disclosure?" Show the agent providing a litigation-risk-and-disclosure-grounded answer.'
          ]
        },
        {
          tool: '🤖 Excel Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to an Excel workbook. Colleagues ask data questions in plain English without opening Excel. Open .xlsx in Excel for Web > Copilot pane > + New Agent > set workbook as knowledge source > share.',
          prompts: [
            'Create the Legal Matter Tracker workbook and open in Excel for Web. Create an agent called "Group Legal Matter Tracker Q&A". Description: "Instant answers on active legal matters, contract expiry deadlines, regulatory response timelines, and Bursa disclosure obligations for the GC and Division Legal Heads." Share with the Group Legal team.',
            'Demo: Ask "Which contracts are expiring within 90 days with no renegotiation started?" Then: "Are there any regulatory deadlines (BNM or BPOM) that we risk missing in the next 30 days and which matters are on critical path?" Show the GC getting instant legal risk intelligence.'
          ]
        },
        {
          tool: '🏗 Agent Builder (Copilot Studio)',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Build a custom declarative agent in Copilot Studio — no coding required. Access: copilotstudio.microsoft.com > Create > New Agent. Add name, description, knowledge sources (SharePoint URLs or uploaded files), topics/actions. Publish to Teams in under 10 minutes.',
          prompts: [
            'Go to copilotstudio.microsoft.com > Create > New Agent. Name it "Zava Legal Intelligence Agent". Description: "Supports the Group Legal Division and Division Legal teams with instant answers on contract management, MACC compliance, Bursa disclosure obligations, data privacy requirements, regulatory deadlines, and cross-border legal frameworks — enabling faster, consistent, and legally sound decisions across the Zava Group." Upload 02_Zava_Group_Policy_Handbook.docx and Email_07_Emergency_Board_Meeting.docx. Add topics: "Contract Management", "MACC Compliance", "Bursa Disclosure", "Data Privacy", "Regulatory Deadlines". Publish to Teams.',
            'Demo the agent: The Group GC receives a WhatsApp message from a journalist at 7pm on a Friday: "I have documents suggesting Zava Group knowingly continued operating the Cilegon plant for 6 weeks after receiving an BPOM enforcement notice. Can you comment for my story running tomorrow?" The GC immediately asks the agent: "What are our legal obligations to respond to a media inquiry about regulatory enforcement, does our press relations policy require a response within a specific timeframe, and what language should I categorically NOT use in any statement related to an active regulatory matter?" Show how the agent provides an instant, legally-grounded crisis communication guidance.'
          ]
        }
      ]
    },
    {
      id: 'dept-risk',
      sectorId: 'department',
      subsector: '',
      name: 'Risk & Internal Audit',
      icon: '🛡',
      color: '#B71C1C',
      accent: '#C62828',
      company: 'Zava Group Holdings — Group Risk Division',
      tagline: 'ERM framework refresh, coal trading limit breach, Zava Bank NPL, Cilegon enforcement — 4 active risk events.',
      scenario: 'The Group Risk Division manages Enterprise Risk Management, Internal Audit, and Board Risk Committee reporting across Zava Group. Four active risk events: coal trading position limit breach, Zava Bank NPL breach, Cilegon plant 3 BPOM enforcement notices, Perkebunan Lestari RSPO suspension. Board Risk Committee meets monthly; a special meeting has been called.',
      files: [
        '01_Zava_Group_Financial_Performance.xlsx',
        '20_Zava_ESG_Sustainability_Framework.docx'
      ],
      prompts: [
        {
          tool: '🤖 Copilot Chat (Basic)',
          license: 'Free — no M365 Copilot license needed',
          account: 'Sasha Ouellet — SashaO@ABSx62256373.OnMicrosoft.com',
          desc: '',
          prompts: [
            'I am the Group Chief Risk Officer of a diversified ASEAN conglomerate. We have 4 simultaneous active risk events: (1) coal trading limit breach USD 2.4M, (2) bank NPL breach 21.7%, (3) chemical plant 3 regulatory enforcement notices, (4) plantation RSPO suspension. Draft a 250-word brief for the Board Risk Committee on: how to prioritise the 4 events by systemic impact, what is the combined worst-case financial exposure, and what is the primary governance question the Board must decide.',
            'What is an Enterprise Risk Management (ERM) framework and how does it differ for a diversified conglomerate vs a single-industry company? Explain the ISO 31000 standard and how it applies to a group with 11 divisions and MYR 45B revenue.',
            'What is the "three lines of defence" model in risk management? How should each line (business units, risk function, internal audit) respond to the 4 active risk events at a conglomerate? Who is responsible for what?'
          ]
        },
        {
          tool: '🔍 Researcher',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via Microsoft 365 Copilot Chat (copilot.microsoft.com or Teams) > click Agents > Researcher. Grounds answers in live web sources and your organisation data with full citations.',
          prompts: [
            'Research enterprise risk management frameworks for diversified conglomerates in Southeast Asia. How do comparable groups (Sime Darby, IJM, Axiata) structure their ERM frameworks? What are the best practices for Group-level risk aggregation when you have 11 diverse business units? Cite ISO 31000, COSO ERM 2017, or comparable frameworks.',
            'Research Malaysian listed company risk disclosure requirements. What does Bursa Malaysia require in the annual report risk section for a company in multiple sectors? How do companies like Petronas and Maybank communicate risk appetite and emerging risks to shareholders? Cite Bursa guidelines.'
          ]
        },
        {
          tool: '📊 Analyst',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via Microsoft 365 Copilot Chat > click Agents > Analyst. Upload an Excel or CSV file. Analyst runs Python-style analysis, builds charts, and interprets results without you writing a single formula.',
          prompts: [
            'Upload 01_Zava_Group_Financial_Performance.xlsx to Analyst. Ask: Build an enterprise risk heat map. For 15 key risks (commodity price, FOREX, NPL/credit, regulatory/enforcement, ESG/RSPO, operational/OEE, succession, cyber, climate, trading limits), score each on: (1) likelihood (1-5), (2) financial impact (1-5 mapped to MYR M thresholds), (3) velocity (how fast it can materialise). Plot on a 5x5 heat map. Identify the top 5 risks requiring immediate Board attention.',
            'Upload 01_Zava_Group_Financial_Performance.xlsx. Ask: Stress test the group financials against a combined adverse scenario: CPO -15%, IDR -10% vs MYR, Zava Bank NPL provisions +MYR 600M, Cilegon plant production loss 6 months, coal trading counterparty default (USD 6.8M loss). Calculate: (1) Impact on group EBITDA, (2) Impact on PAT, (3) New net gearing ratio, (4) Whether any debt covenant is breached. Show as a stress scenario table.'
          ]
        },
        {
          tool: '📊 Copilot in Excel',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open 01_Zava_Group_Financial_Performance.xlsx. Navigate to the risk data section. Ask Copilot: Build a 4-event risk dashboard on a new sheet. For each of the 4 active risk events (coal trading breach, bank NPL, Cilegon enforcement, RSPO suspension), show: (1) Event description, (2) Financial exposure (MYR M), (3) Provision taken, (4) Unresolved exposure, (5) Remediation status (% complete), (6) Board action required (Y/N), (7) Next deadline. Apply RAG status. Add a total group exposure row.',
            'Ask Copilot: Create an Internal Audit progress tracker on a new sheet. For each of the 24 internal audit engagements planned for FY2025 (across 11 divisions), show: (1) Entity and area, (2) Planned start and end date, (3) Status, (4) High/medium/low findings count, (5) Management response received (Y/N), (6) Overdue findings from prior audit. Highlight engagements where the management response is overdue.',
            'Ask Copilot: Build a risk appetite statement dashboard on a new sheet. For each risk category (credit, market, operational, compliance, ESG, strategic), show: (1) Risk appetite statement (one sentence), (2) Key risk metric, (3) Tolerance threshold, (4) Current level, (5) Status (Within / Approaching / Breaching). Flag breaching risks in red.'
          ]
        },
        {
          tool: '📝 Copilot in Word',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open 20_Zava_ESG_Sustainability_Framework.docx. Ask Copilot: Draft the Board Risk Committee special meeting report on the 4 concurrent risk events. For each event: (1) 1-paragraph situation summary, (2) Quantified financial exposure, (3) Immediate actions taken, (4) Remediation timeline, (5) Board decision required. Include an opening executive summary covering the aggregate risk exposure and a single recommendation for the Board. 12 pages, formal Board Risk Committee paper format.',
            'Ask Copilot: Draft an update to Zava Group\'s Risk Appetite Statement. Current appetites are defined for 6 risk categories. The 4 active risk events suggest our risk appetite in operational risk and trading was set too broadly. Propose revised appetite thresholds for: (1) Single counterparty trading exposure (reduce from USD 20M to USD 15M), (2) Regulatory enforcement tolerance (zero tolerance for >2 enforcement notices at any single facility), (3) NPL appetite for Zava Bank consumer loans (reduce from 5% to 3.5% triggering immediate CRO notification). Format as a Risk Appetite Statement amendment paper.',
            'Ask Copilot: Draft the Internal Audit findings management letter to the Cilegon Plant Manager on the 3 BPOM enforcement notices. The letter should: summarise the audit findings (control failure in EHS compliance monitoring), list 8 required management actions, set a 60-day deadline for each, and note that a follow-up audit will be conducted within 90 days. Formal audit management letter format.'
          ]
        },
        {
          tool: '🎯 Copilot in PowerPoint',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Ask Copilot in PowerPoint: Create an 8-slide Board Risk Committee special meeting deck. Include: (1) Agenda — 4 active risk events, (2) Event 1: Coal Trading Breach — situation, exposure, remediation, (3) Event 2: Zava Bank NPL — situation, provisioning, BNM plan, (4) Event 3: Cilegon Enforcement — situation, corrective action, (5) Event 4: RSPO Suspension — situation, remediation, (6) Combined risk exposure — stress test results, (7) ERM framework gap — what control failed in each event, (8) Board decisions required. Red and white colour scheme — this is a crisis meeting.',
            'Ask Copilot: Create a 2-slide ERM framework gap analysis. Slide 1: For each of the 4 events, identify the specific ERM control that failed — monitoring frequency? Escalation trigger? Risk appetite threshold? Slide 2: The 5 specific ERM enhancements that would have prevented or minimised each event.',
            'Ask Copilot: Create a group risk heat map slide showing 15 key risks on a 5x5 likelihood-impact matrix. Colour the matrix: green (low), yellow (medium), orange (high), red (critical). Mark the 4 active risk events with a special marker showing they have already materialised.'
          ]
        },
        {
          tool: '📧 Copilot in Outlook',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Ask Copilot in Outlook: Draft the CRO\'s notification email to all Division Risk Officers and CEOs announcing the 4 active risk events at Group level. The email should: state that a special Board Risk Committee meeting has been called, request each division to review their own risk registers for similar exposures, and ask for a written risk status update from each division by end of week. Tone: serious, professional, and urgent.',
            'Ask Copilot: Draft the Group Risk Division\'s quarterly update letter to KPMG (external auditors) informing them of the 4 active risk events and the related financial provisions. The letter should disclose: coal trading exposure MYR 28.4M, Zava Bank provision MYR 420M additional, Cilegon production loss estimate MYR 85M, RSPO remediation cost estimate MYR 42M. Request their view on any additional audit procedures required.',
            'Ask Copilot: Draft the CRO\'s email to the internal audit team instructing a special unplanned audit of the Group Trading Desk following the coal trading limit breach. The audit should cover: position limit monitoring controls, daily mark-to-market reporting process, Risk Committee escalation procedures, and the approval process for limit increases. Timeline: 3-week fieldwork, report in 6 weeks.'
          ]
        },
        {
          tool: '🎙 Copilot in Teams',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Use your OWN existing recorded Teams meetings. Open a meeting recap in Teams > Recap tab. Copilot generates summaries, action items, and follow-up drafts grounded in the actual transcript.',
          prompts: [
            'Open an existing recorded Teams meeting recap from a risk committee or crisis management meeting. Ask Copilot: Identify all risk events discussed, risk mitigation actions committed, and any decisions made about escalation or disclosure. Create an action tracker.',
            'Ask Copilot: Draft the post-meeting risk management team follow-up actions. Group by risk event: Trading Breach | Bank NPL | Cilegon Enforcement | RSPO. Include action, owner, and deadline.',
            'Ask Copilot: From this meeting, which Board members expressed the most concern about the combined risk exposure? What additional information did they request before the next Board meeting?'
          ]
        },
        {
          tool: '📓 Copilot Notebook',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via copilot.microsoft.com > Notebook tab. Upload up to 5 files and set a system instruction. Best for synthesising insights across multiple documents simultaneously.',
          prompts: [
            'Upload 01_Zava_Group_Financial_Performance.xlsx and 20_Zava_ESG_Sustainability_Framework.docx to Copilot Notebook. Set instruction: "You are the Group CRO preparing for the Board Risk Committee special meeting." Ask: Which of the 4 active risk events poses the highest systemic risk to the group — considering financial exposure, regulatory implications, reputation impact, and speed of escalation? What is the single most important decision the Board must make at Monday\'s special meeting?',
            'Upload 20_Zava_ESG_Sustainability_Framework.docx. Ask: Our ERM framework last had a full refresh in 2021. The 4 concurrent risk events suggest the framework has gaps. Identify the 5 most critical ERM framework improvements that would have provided earlier warning of these 4 events. Prioritise by ease of implementation and impact.'
          ]
        },
        {
          tool: '🤝 Cowork (Frontier)',
          license: 'M365 Copilot + Frontier Program',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Cowork is an autonomous agent that takes actions across Microsoft 365 on your behalf — sending emails, scheduling meetings, creating documents, posting in Teams, and scheduling recurring tasks. Access: m365.cloud.microsoft > left nav > Agents > Cowork. Requires Frontier program enrollment.',
          prompts: [
            'Do all of the following immediately: (1) Research how comparable ASEAN conglomerates have responded to simultaneous multi-division risk events — identify best practice from Sime Darby or Axiata crisis management. (2) Draft a 2-page crisis risk management protocol for the Group CRO to activate when 3 or more major risk events are active simultaneously. (3) Save to OneDrive as "Group Crisis Risk Protocol". (4) Email to CRO and GC for review. (5) Schedule a crisis management taskforce meeting with all Division CROs for tomorrow.',
            'Do all of the following for the Board Risk Committee meeting: (1) Compile the 4 active risk event summaries from the divisional CROs into one master Board Risk Committee brief. (2) Calculate the combined worst-case financial exposure. (3) Create a colour-coded risk dashboard for the Board presentation. (4) Email to Board Secretary for inclusion in the Board papers. (5) Schedule a 1-hour pre-Board CRO briefing with the Chairman of the Risk Committee.'
          ]
        },
        {
          tool: '🤖 Word Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to a Word document. Open the .docx in Word for Web > Copilot pane > + New Agent > name it, write a description, set the document as knowledge source > Share. Colleagues chat with it in Teams or M365 Copilot.',
          prompts: [
            'Open 20_Zava_ESG_Sustainability_Framework.docx in Word for Web. Create an agent called "Zava Group Risk & Audit Policy Bot". Description: "Answers questions from Division Risk Officers, Internal Auditors, and business leaders on the ERM framework, risk appetite thresholds, internal audit procedures, escalation requirements, and regulatory compliance obligations." Share with all Division Risk Officers.',
            'Demo: A Division Risk Officer asks "Our plantation division has just received its 2nd BPOM enforcement notice this year. Under the Group Risk Appetite Statement, does a 2nd enforcement notice at a single facility trigger mandatory escalation to Group CRO? And what is the timeframe for the escalation?" Show the agent providing a policy-grounded, escalation-clear risk management answer.'
          ]
        },
        {
          tool: '🤖 PowerPoint Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to a PowerPoint presentation. Great for strategy decks or Board presentations many people need to reference. Same setup as Word Agent but using a .pptx file.',
          prompts: [
            'Create a PowerPoint from the Board Risk Committee presentation. Create an agent called "Board Risk Committee Q&A Bot". Share with Board Risk Committee members.',
            'Demo: A Board member asks "If the RSPO suspension at Perkebunan Lestari continues for 18 months instead of 6, what is the additional financial impact and does it change our FY2025 EBITDA guidance?" Show the agent providing a risk-scenario-grounded financial impact answer.'
          ]
        },
        {
          tool: '🤖 Excel Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to an Excel workbook. Colleagues ask data questions in plain English without opening Excel. Open .xlsx in Excel for Web > Copilot pane > + New Agent > set workbook as knowledge source > share.',
          prompts: [
            'Open 01_Zava_Group_Financial_Performance.xlsx in Excel for Web. Create an agent called "Group Risk Dashboard Q&A". Description: "Instant answers on active risk events, financial exposures, ERM risk register status, and internal audit findings for the CRO and Board Risk Committee." Share with risk leadership.',
            'Demo: Ask "What is the combined worst-case financial exposure from all 4 active risk events if none are resolved?" Then: "Which division has the highest number of overdue internal audit findings and what is the total value at risk from those findings?" Show the CRO getting instant risk intelligence.'
          ]
        },
        {
          tool: '🏗 Agent Builder (Copilot Studio)',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Build a custom declarative agent in Copilot Studio — no coding required. Access: copilotstudio.microsoft.com > Create > New Agent. Add name, description, knowledge sources (SharePoint URLs or uploaded files), topics/actions. Publish to Teams in under 10 minutes.',
          prompts: [
            'Go to copilotstudio.microsoft.com > Create > New Agent. Name it "Zava Risk Intelligence Agent". Description: "Supports the Group CRO, Division Risk Officers, and Internal Audit with instant answers on risk event status, ERM framework requirements, risk appetite thresholds, audit procedures, and regulatory compliance obligations — enabling faster, more consistent risk management decisions across all 11 Zava divisions." Upload 01_Zava_Group_Financial_Performance.xlsx and 20_Zava_ESG_Sustainability_Framework.docx. Add topics: "Risk Events", "ERM Framework", "Internal Audit", "Risk Appetite", "Regulatory Compliance". Publish to Teams for risk and audit teams.',
            'Demo the agent: The Group CRO receives an urgent Saturday morning call from the Cilegon Plant Manager: the plant has just received a 4th BPOM enforcement notice — this time for an accidental chemical release that requires a 72-hour production shutdown. The CRO asks the agent: "Under our ERM escalation protocol, does a 4th enforcement notice at the same facility triggering a production shutdown require immediate Board notification? What is the maximum financial exposure from a 72-hour shutdown and does this breach our operational risk appetite threshold?" Show the agent enabling a swift, policy-grounded crisis response decision.'
          ]
        }
      ]
    },
    {
      id: 'dept-strategy',
      sectorId: 'department',
      subsector: '',
      name: 'Strategy & M&A',
      icon: '🎯',
      color: '#E65100',
      accent: '#F57C00',
      company: 'Zava Group Holdings — Group Strategy Division',
      tagline: 'ZAVA FORWARD 2030 — 4 healthcare M&A targets, REIT IPO, pharma Vietnam expansion.',
      scenario: 'The Group Strategy Division drives the ZAVA FORWARD 2030 strategic plan — 5 pillars, MYR 12.4B capex over 5 years. Current M&A pipeline: 4 healthcare targets in evaluation (PrimeCare Holdings being the priority), REIT IPO 2026, Pharma expansion into Vietnam and Philippines. Divestment: 2 non-core assets identified.',
      files: [
        '04_Zava_MA_Evaluation_Framework.docx',
        '01_Zava_Group_Financial_Performance.xlsx'
      ],
      prompts: [
        {
          tool: '🤖 Copilot Chat (Basic)',
          license: 'Free — no M365 Copilot license needed',
          account: 'Sasha Ouellet — SashaO@ABSx62256373.OnMicrosoft.com',
          desc: '',
          prompts: [
            'I am the Group Chief Strategy Officer of a MYR 45B ASEAN conglomerate. We have 4 healthcare M&A targets in active evaluation. Our Board has set a strict criteria: deals must be EPS-accretive within 3 years and ROIC must exceed our WACC of 9.2% by Year 5. Draft a 250-word brief explaining: (1) How to determine if a healthcare acquisition is EPS-accretive within 3 years — key assumptions needed, (2) How ROIC is calculated for an M&A deal and what synergies count towards ROIC, (3) Why the healthcare sector commands a premium valuation multiple and whether the premium is justified given our strategic rationale.',
            'Explain what a strategic portfolio review is for a diversified conglomerate. How should a Board decide which businesses to grow, hold, or divest? What frameworks (GE-McKinsey, BCG matrix) are most useful and how are they adapted for a conglomerate with 11 divisions?',
            'What does "ZAVA FORWARD 2030" as a strategic plan need to include to be credible to institutional investors and analysts? What are the 5 most important components of a well-structured 5-year conglomerate strategy and how should it be communicated on Investor Day?'
          ]
        },
        {
          tool: '🔍 Researcher',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via Microsoft 365 Copilot Chat (copilot.microsoft.com or Teams) > click Agents > Researcher. Grounds answers in live web sources and your organisation data with full citations.',
          prompts: [
            'Research the Southeast Asian private hospital and healthcare M&A market. I need: (1) Current EV/EBITDA multiples for hospital acquisitions in Malaysia and Indonesia, (2) Key strategic rationale for conglomerate hospital investments — IHH, Columbia Asia, Pantai, (3) How healthcare M&A deals are structured in Malaysia (acquisition of shares vs assets, minority buy-in vs full acquisition). Cite Mergermarket or healthcare sector M&A reports.',
            'Research Vietnam pharma market entry strategies for Malaysian generic drug manufacturers. What are the licensing requirements from the DAV (Drug Administration of Vietnam)? Who are the existing Malaysian pharma companies in Vietnam and what entry mode did they use (greenfield, JV, acquisition, distributor)? Cite industry sources.'
          ]
        },
        {
          tool: '📊 Analyst',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via Microsoft 365 Copilot Chat > click Agents > Analyst. Upload an Excel or CSV file. Analyst runs Python-style analysis, builds charts, and interprets results without you writing a single formula.',
          prompts: [
            'Upload 04_Zava_MA_Evaluation_Framework.docx and 01_Zava_Group_Financial_Performance.xlsx. Ask Analyst: Evaluate the 4 healthcare M&A targets against the 7-category framework. Score each target on: (1) Strategic fit (1-5), (2) Financial performance — EBITDA margin and growth, (3) Integration complexity, (4) Price vs comparable transactions, (5) Management quality, (6) Regulatory risk, (7) ESG profile. Rank the 4 targets from most to least attractive. Identify which target best meets our ROIC>WACC threshold by Year 5.',
            'Upload 01_Zava_Group_Financial_Performance.xlsx. Ask: Build an M&A deal capacity analysis. Current net debt MYR 18.4B, EBITDA MYR 7.2B, gearing 0.82x. Covenant: net debt/EBITDA < 3.5x. Assuming we maintain gearing below 2.5x (conservative target), what is the maximum deal size we can fund with: (1) 100% debt financing, (2) 70% debt / 30% equity (rights issue or new shares), (3) Using REIT IPO proceeds as partial funding? Calculate for each.'
          ]
        },
        {
          tool: '📊 Copilot in Excel',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open 01_Zava_Group_Financial_Performance.xlsx. Navigate to the M&A sheet. Ask Copilot: Build a deal scorecard on a new sheet for the 4 healthcare targets. For each target, show: (1) Enterprise value (MYR M), (2) EV/EBITDA multiple paid, (3) Revenue and EBITDA (current year), (4) Projected Year 3 EBITDA with synergies, (5) EPS accretion in Year 3 (bps), (6) ROIC at Year 5 vs WACC 9.2%, (7) Recommended action (Proceed / Further Diligence / Pass). Apply colour coding.',
            'Ask Copilot: Create a strategic portfolio matrix on a new sheet. For each of the 11 Zava divisions, plot on a 3x3 McKinsey matrix (Industry Attractiveness vs Business Unit Strength). Classify each as Grow (top-right), Hold (diagonal), or Divest (bottom-left). For the 2 non-core assets identified for divestment, calculate estimated divestment proceeds and the use of proceeds.',
            'Ask Copilot: Build a ZAVA FORWARD 2030 capex tracker. For MYR 12.4B total capex over 5 years, show allocation by: (1) Division (Healthcare expansion MYR 3.2B, Properties REIT MYR 1.4B, Pharma MYR 0.8B, Manufacturing upgrade MYR 1.6B, Digital transformation MYR 0.9B, others), (2) Year, (3) Funding source (own cash, debt, REIT IPO proceeds). Show cumulative capex vs budget by year.'
          ]
        },
        {
          tool: '📝 Copilot in Word',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open 04_Zava_MA_Evaluation_Framework.docx. Ask Copilot: Update the M&A Evaluation Framework to add a new ESG scoring category. The new category should include: (1) GHG Scope 1/2 intensity vs sector benchmark, (2) RSPO/ISPO certification status if plantation involved, (3) Labour practices and human rights screening, (4) Governance quality — independent directors, related party transaction history, (5) EUDR compliance if applicable. Assign a 15% weight to ESG in the overall deal score. Revise the framework document accordingly.',
            'Ask Copilot: Draft the Executive Summary of the PrimeCare Holdings M&A Information Memorandum. The IM should cover: (1) Transaction overview — Zava Group\'s proposed acquisition of 60% equity stake, (2) PrimeCare overview — 8 hospitals, MYR 680M revenue, 14.2% EBITDA margin, (3) Strategic rationale — accelerates Zava Healthcare to 18 hospitals, fills MY Central region gap, (4) Valuation — MYR 1.84B EV at 11.2x EV/EBITDA, (5) Deal structure — MYR 1.1B upfront, MYR 280M deferred, (6) Key conditions — regulatory approval, CIMSA accreditation maintained. 4 pages, investment banking IM style.',
            'Ask Copilot: Draft the Board paper recommending approval of the PrimeCare acquisition. Cover: strategic rationale, financial impact (EPS accretion Year 3), deal structure, risk factors and mitigants, WACC vs ROIC analysis, regulatory approval timeline, and the Board resolution requested. 15 pages, formal Board paper.'
          ]
        },
        {
          tool: '🎯 Copilot in PowerPoint',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Ask Copilot in PowerPoint: Create a 14-slide Investor Day strategy presentation for ZAVA FORWARD 2030. Include: (1) Group overview — MYR 44.8B, 11 divisions, (2) Market context — ASEAN growth outlook, (3) 5 strategic pillars, (4) Portfolio optimisation — grow, hold, divest decisions, (5) Healthcare M&A — pipeline and PrimeCare, (6) Properties REIT IPO 2026, (7) Pharma expansion — Vietnam and Philippines, (8) Digital transformation, (9) ESG leadership, (10) Capital allocation — MYR 12.4B, (11) 5-year financial targets, (12) Dividend policy, (13) Key risks and mitigants, (14) Summary — why Zava Group is the ASEAN conglomerate to own. Dark navy and gold.',
            'Ask Copilot: Create a 5-slide M&A strategy summary for the Board\'s Strategy & Investment Committee. Slide 1: M&A deal capacity. Slides 2-5: Each of the 4 healthcare targets — one slide each with scorecard, recommendation, and key condition.',
            'Ask Copilot: Create a 3-slide Vietnam pharma market entry analysis. Slide 1: Vietnam pharma market — size, growth, key therapeutic areas. Slide 2: Entry options — JV vs greenfield vs acquisition, comparing speed, cost, and risk. Slide 3: Recommended entry mode and 24-month implementation plan.'
          ]
        },
        {
          tool: '📧 Copilot in Outlook',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Ask Copilot in Outlook: Draft a Non-Disclosure Agreement cover letter to PrimeCare Holdings\' CEO proposing the commencement of due diligence. The letter should: confirm our interest in exploring a 60% equity acquisition, request execution of the mutual NDA, and propose a 2-week timeline for the management presentation. Confidential, professional M&A engagement letter tone.',
            'Ask Copilot: Draft the strategy communication to all Division CEOs following the ZAVA FORWARD 2030 Investor Day. The email should: summarise the 5 strategic pillars as they apply to each division, confirm the individual division capex allocation, and call for division 3-year operating plans to be submitted within 6 weeks. Energising, leadership tone.',
            'Ask Copilot: Draft an email to our financial advisors (Goldman Sachs and Maybank Investment Bank) confirming the mandate for the PrimeCare M&A advisory engagement. Confirm: deal structure, advisory fee structure (retainer MYR 180K/month + success fee 0.8% of deal value), milestones for success fee trigger, and the 6-month exclusivity period.'
          ]
        },
        {
          tool: '🎙 Copilot in Teams',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Use your OWN existing recorded Teams meetings. Open a meeting recap in Teams > Recap tab. Copilot generates summaries, action items, and follow-up drafts grounded in the actual transcript.',
          prompts: [
            'Open an existing recorded Teams meeting recap from a strategy or M&A committee meeting. Ask Copilot: Identify all M&A target discussions, deal structure debates, and strategic divestment mentions. Extract the 3 most important decisions made and the follow-up actions for the deal team.',
            'Ask Copilot: Draft the M&A deal team weekly update. Structure: (1) PrimeCare — due diligence status, (2) 3 other targets — preliminary status, (3) Regulatory approval timeline, (4) Board paper preparation timeline, (5) Financial advisor engagement.',
            'Ask Copilot: From this meeting, what concerns did the CFO raise about the combined M&A capacity? What was the debate about whether to proceed with 1 deal now or to wait until the REIT IPO proceeds are available?'
          ]
        },
        {
          tool: '📓 Copilot Notebook',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via copilot.microsoft.com > Notebook tab. Upload up to 5 files and set a system instruction. Best for synthesising insights across multiple documents simultaneously.',
          prompts: [
            'Upload 04_Zava_MA_Evaluation_Framework.docx and 01_Zava_Group_Financial_Performance.xlsx to Copilot Notebook. Set instruction: "You are advising the Group CSO on the healthcare M&A strategy." Ask: Based on the evaluation framework and financial capacity, should Zava Group proceed with the PrimeCare acquisition now or wait 12 months until the REIT IPO proceeds are available to reduce the debt financing proportion? What is the quantified cost/benefit of waiting?',
            'Upload 04_Zava_MA_Evaluation_Framework.docx. Ask: One of the 4 healthcare M&A targets is a Shariah-compliant hospital group in Malaysia. They require that any acquisition be structured using Islamic financing (Sukuk) and that the hospital operations maintain JAKIM halal certification. How does this constraint affect our deal structure and ROIC calculation? Does an Islamic deal structure typically deliver a better or worse outcome for the acquirer than conventional financing at our current cost of debt of 5.8%?'
          ]
        },
        {
          tool: '🤝 Cowork (Frontier)',
          license: 'M365 Copilot + Frontier Program',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Cowork is an autonomous agent that takes actions across Microsoft 365 on your behalf — sending emails, scheduling meetings, creating documents, posting in Teams, and scheduling recurring tasks. Access: m365.cloud.microsoft > left nav > Agents > Cowork. Requires Frontier program enrollment.',
          prompts: [
            'Do all of the following for PrimeCare M&A: (1) Research PrimeCare Holdings\' publicly available information — financial performance, hospital locations, JCI accreditation status, and any news in the past 12 months. (2) Draft a 3-page target profile summary. (3) Create a PrimeCare due diligence data room structure in SharePoint with 12 folders covering all due diligence workstreams. (4) Email to the M&A deal team lead, GC, and CFO confirming the data room structure and access permissions. (5) Schedule a weekly M&A deal team meeting for 20 weeks.',
            'Do all of the following for ZAVA FORWARD 2030 Investor Day: (1) Research the top 10 questions that ASEAN conglomerate analysts ask at strategy Investor Days — compile from Morgan Stanley, UBS, and CIMB research. (2) Draft a 2-page investor Q&A preparation guide for the CEO and CFO covering the 10 most challenging anticipated questions. (3) Save to OneDrive as "Investor Day Q&A Prep - CONFIDENTIAL". (4) Email to CEO, CFO, and Head of IR for review. (5) Schedule a 3-hour investor day rehearsal 2 weeks before the event.'
          ]
        },
        {
          tool: '🤖 Word Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to a Word document. Open the .docx in Word for Web > Copilot pane > + New Agent > name it, write a description, set the document as knowledge source > Share. Colleagues chat with it in Teams or M365 Copilot.',
          prompts: [
            'Open 04_Zava_MA_Evaluation_Framework.docx in Word for Web. Create an agent called "Zava M&A Strategy Bot". Description: "Answers questions from the Group Strategy and M&A team on the M&A evaluation framework, deal scoring methodology, healthcare sector M&A norms, regulatory approval requirements, and ZAVA FORWARD 2030 strategic priorities." Share with the Strategy and M&A team.',
            'Demo: An M&A analyst asks "Our second-ranked target has a 38% founding family minority stake. They have refused drag-along rights and want a preferred dividend of 8% before common shareholders. How does this minority shareholder structure affect our ROIC calculation and does it change our deal recommendation?" Show the agent providing a deal-structure-aware M&A answer.'
          ]
        },
        {
          tool: '🤖 PowerPoint Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to a PowerPoint presentation. Great for strategy decks or Board presentations many people need to reference. Same setup as Word Agent but using a .pptx file.',
          prompts: [
            'Create a PowerPoint from the Investor Day presentation. Create an agent called "ZAVA FORWARD 2030 Investor Q&A Bot". Share with institutional investors and the IR team.',
            'Demo: An analyst asks "Your 5-year capex is MYR 12.4B against current EBITDA of MYR 7.2B. That\'s nearly 2x EBITDA. How do you fund this without breaching your 2.5x gearing target and why should shareholders not expect a rights issue?" Show the agent providing a capital-allocation-grounded answer to a tough Investor Day question.'
          ]
        },
        {
          tool: '🤖 Excel Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to an Excel workbook. Colleagues ask data questions in plain English without opening Excel. Open .xlsx in Excel for Web > Copilot pane > + New Agent > set workbook as knowledge source > share.',
          prompts: [
            'Open 01_Zava_Group_Financial_Performance.xlsx in Excel for Web. Create an agent called "Zava Strategy & M&A Q&A". Description: "Instant answers on M&A deal capacity, portfolio matrix scores, capex allocation, ZAVA FORWARD 2030 targets, and deal scoring for the CSO, CFO, and M&A team." Share with the strategy leadership.',
            'Demo: Ask "What is our current M&A deal capacity in MYR M if we maintain gearing below 2.5x?" Then: "Based on the deal scoring, which of the 4 healthcare targets has the highest ROIC vs WACC by Year 5?" Show the CSO getting instant strategic portfolio intelligence.'
          ]
        },
        {
          tool: '🏗 Agent Builder (Copilot Studio)',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Build a custom declarative agent in Copilot Studio — no coding required. Access: copilotstudio.microsoft.com > Create > New Agent. Add name, description, knowledge sources (SharePoint URLs or uploaded files), topics/actions. Publish to Teams in under 10 minutes.',
          prompts: [
            'Go to copilotstudio.microsoft.com > Create > New Agent. Name it "Zava Strategy Intelligence Agent". Description: "Supports the Group Strategy and M&A team with instant answers on M&A evaluation criteria, deal capacity, ZAVA FORWARD 2030 strategic priorities, portfolio matrix scores, healthcare sector norms, and pharma expansion requirements — enabling faster, smarter strategic decisions across the Zava Group." Upload 04_Zava_MA_Evaluation_Framework.docx and 01_Zava_Group_Financial_Performance.xlsx. Add topics: "M&A Evaluation", "Portfolio Strategy", "Healthcare Expansion", "Pharma", "REIT IPO". Publish to Teams for the Strategy Division.',
            'Demo the agent: The Group CSO gets a call from a Goldman Sachs banker at 6pm on a Friday: "A distressed hospital group with 12 hospitals in Peninsular Malaysia has just hired us. Their Board is looking for a buyer within 90 days. EV is approximately MYR 2.1B. Given your publicly stated healthcare strategy, would Zava Group be interested?" The CSO asks the agent: "How does a MYR 2.1B deal for a 12-hospital group compare to our 4 existing targets on EV/hospital metrics? Do we have the balance sheet capacity without a rights issue? And does the 90-day timeline leave enough time for our M&A evaluation and Board approval process?" Show how the agent enables an instant, data-backed strategic response call.'
          ]
        }
      ]
    },
    {
      id: 'dept-marketing',
      sectorId: 'department',
      subsector: '',
      name: 'Marketing & Communications',
      icon: '📢',
      color: '#AD1457',
      accent: '#C2185B',
      company: 'Zava Group Holdings — Group Marketing & Comms',
      tagline: 'Investor Day comms, Zava Bank NPL media risk, Perkebunan Lestari ESG reputation management.',
      scenario: 'Group Marketing & Communications manages brand, PR, investor communications, and crisis communications for all 11 Zava divisions and the Group. Three live communications challenges: Investor Day messaging for ZAVA FORWARD 2030, media risk from Zava Bank NPL coverage, and ESG reputation risk from the Perkebunan Lestari RSPO suspension.',
      files: [
        '03_Zava_Group_Strategy_Framework.docx',
        'Email_08_Coal_Trading_Breach.docx'
      ],
      prompts: [
        {
          tool: '🤖 Copilot Chat (Basic)',
          license: 'Free — no M365 Copilot license needed',
          account: 'Sasha Ouellet — SashaO@ABSx62256373.OnMicrosoft.com',
          desc: '',
          prompts: [
            'I am the Group CCO of a dual-listed ASEAN conglomerate. A financial journalist has written a story headlined "Zava Bank\'s NPL Crisis: Is Malaysia\'s oldest conglomerate running out of road?" The story is factually accurate but sensationalised. We are 3 weeks from our H1 results announcement. Draft a 250-word crisis communications brief: (1) Should we respond proactively or wait for the results announcement, (2) If we respond, what are the 3 key messages to rebut the headline, (3) What stakeholders must be briefed before we issue any public statement.',
            'What is a stakeholder communications plan for a conglomerate preparing for Investor Day? Which stakeholder groups need to be briefed before, during, and after the Investor Day event? What are the typical confidentiality boundaries before the formal announcement?',
            'Explain how brand purpose communicates differently for a diversified conglomerate vs a single-brand company. How does Zava Group build a coherent brand narrative when it operates hospitals, palm oil estates, a bank, and a chemicals plant?'
          ]
        },
        {
          tool: '🔍 Researcher',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via Microsoft 365 Copilot Chat (copilot.microsoft.com or Teams) > click Agents > Researcher. Grounds answers in live web sources and your organisation data with full citations.',
          prompts: [
            'Research best practices for investor day communications for Asian conglomerates. What are the most effective formats, content elements, and follow-up strategies? How do Sime Darby, IHH, and Axiata structure their investor days? Cite IR best practice resources.',
            'Research the current media coverage of Malaysian banking NPL issues and ESG controversies in palm oil. What is the media and investor sentiment toward Malaysian conglomerates with diversified exposure in 2024-2025? Are there any specific journalists or publications most influential in this space? Cite media analysis.'
          ]
        },
        {
          tool: '📊 Analyst',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via Microsoft 365 Copilot Chat > click Agents > Analyst. Upload an Excel or CSV file. Analyst runs Python-style analysis, builds charts, and interprets results without you writing a single formula.',
          prompts: [
            'Upload 03_Zava_Group_Strategy_Framework.docx (use as reference). Ask Analyst to help structure: Build a stakeholder sentiment mapping model. For 8 key stakeholder groups (institutional investors, retail investors, financial media, ESG rating agencies, regulators, plantation NGOs, employees, communities), score current sentiment (1=very negative, 5=very positive) and our communications effectiveness (1=very poor, 5=excellent). Plot as a matrix. Identify stakeholders where sentiment is negative AND our communications is poor — these are priority focus areas.',
            'Ask Analyst: Build a media monitoring dashboard. Track sentiment for 5 key topics (Zava Bank NPL, RSPO suspension, Coal trading breach, REIT IPO, ZAVA FORWARD 2030) across 3 media segments (financial media, ESG media, mainstream news). Score 1-5 and show trend over the past 6 months. Identify which topic is most at risk of media escalation.'
          ]
        },
        {
          tool: '📊 Copilot in Excel',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open 03_Zava_Group_Strategy_Framework.docx. Create a companion Communications Tracker workbook. Ask Copilot: Create Sheet 1 with columns for each active communications issue: Issue | Stakeholder | Sentiment (1-5) | Our Response Status | Key Message | Next Action | Owner | Deadline. Populate with 5 current issues. Apply RAG conditional formatting.',
            'Ask Copilot: Build an Investor Day content tracker on Sheet 2. For each presentation section, show: Section | Presenter | Key Message | Key Data Point | Draft Status | Approved By | Time Allocated. Track 14 sections. Highlight any section without an approved draft 3 weeks before the event.',
            'Ask Copilot: Create a brand monitoring dashboard on Sheet 3. For Zava Group and 3 competitors (Sime Darby, IOI, IJM), show quarterly: (1) Share of Voice in financial media (estimated %), (2) Net sentiment score (-100 to +100), (3) ESG mentions — positive vs negative, (4) Key themes covered. Show trend over 4 quarters.'
          ]
        },
        {
          tool: '📝 Copilot in Word',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open 03_Zava_Group_Strategy_Framework.docx. Ask Copilot: Draft the Zava Group Investor Day speech for the Group CEO. The speech (12 minutes / ~1,800 words) should: open with a compelling vision statement for 2030, acknowledge the challenges (Bank NPL, RSPO suspension) honestly, pivot to the strategic opportunity (healthcare, REIT, pharma), present the 5 pillars of ZAVA FORWARD 2030, and close with a personal commitment from the CEO. Energetic, authentic, investor-facing tone.',
            'Open Email_08_Coal_Trading_Breach.docx. Ask Copilot: Draft the Zava Group holding statement on the coal trading breach for media. The statement should: acknowledge a risk control issue has occurred, state that the matter is being investigated internally, confirm no material financial impact is expected, note that governance enhancements are being implemented, and direct media to the forthcoming H1 results announcement for full disclosure. Measured, factual, no admission of fault language.',
            'Ask Copilot: Draft the internal employee communication on the coal trading breach, Zava Bank NPL, and RSPO suspension — 3 separate brief paragraphs for the Group intranet. Each paragraph should: describe the situation in plain language, emphasise management action, reassure employees that Zava Group is financially strong, and note what employees should say if customers or media ask. Honest, reassuring tone.'
          ]
        },
        {
          tool: '🎯 Copilot in PowerPoint',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Ask Copilot in PowerPoint: Create a 5-slide crisis communications playbook for Zava Group. Slide 1: Crisis classification framework (Tier 1/2/3 based on financial, reputational, and legal impact). Slide 2: Response timeline — who must be notified and in what order within 2 hours, 24 hours, 72 hours. Slide 3: Approved spokespersons by crisis type. Slide 4: Holding statement template. Slide 5: Post-crisis reputation recovery actions. Red and white crisis management visual.',
            'Ask Copilot: Create the Investor Day visual identity slide deck theme. Design: dark navy (#1F2D55) background, gold accents (#D4AF37), clean sans-serif font, "ZAVA FORWARD 2030" branding on every slide. Apply to a 3-slide sample: title slide, agenda slide, and a content slide. This template will be used for all 14 investor day sections.',
            'Ask Copilot: Create a 2-slide ESG reputation recovery plan for the Perkebunan Lestari RSPO suspension. Slide 1: Current media narrative and key stakeholder concerns. Slide 2: 6-month reputation recovery roadmap — proactive ESG announcements, NGO engagement, RSPO reinstatement milestone, CEO community visit.'
          ]
        },
        {
          tool: '📧 Copilot in Outlook',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Ask Copilot in Outlook: Draft the Group CEO\'s personalised letter to the top 15 institutional shareholders ahead of Investor Day. The letter should: acknowledge their continued support, invite them to Investor Day (date, venue, registration link), offer a 30-minute pre-event bilateral meeting, and build anticipation for the ZAVA FORWARD 2030 strategy announcement. Warm, CEO-personal tone.',
            'Ask Copilot: Draft a proactive media outreach email to 10 financial journalists proposing a background briefing on ZAVA FORWARD 2030. The briefing will be under embargo until Investor Day. The email should: invite the journalist, note the key themes to be covered, confirm the background-only ground rules, and offer a post-Investor Day exclusive follow-up interview with the CEO.',
            'Ask Copilot: Draft the Group CCO\'s email to all 11 Division Communications Heads with the media handling guidelines for the current sensitive period. The guidelines should: list the 4 approved spokespersons for media enquiries, categorise topics as "approved to discuss", "refer to holding statement", or "no comment", and remind them that all media enquiries must be logged in the Communications Tracker within 2 hours.'
          ]
        },
        {
          tool: '🎙 Copilot in Teams',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Use your OWN existing recorded Teams meetings. Open a meeting recap in Teams > Recap tab. Copilot generates summaries, action items, and follow-up drafts grounded in the actual transcript.',
          prompts: [
            'Open an existing recorded Teams meeting recap from a communications, PR, or investor relations meeting. Ask Copilot: Identify all active media or reputation issues discussed, the agreed response strategies, and any approvals obtained. Create a communications action log.',
            'Ask Copilot: Draft the weekly communications status update for the Group CEO. Structure: (1) Key media mentions this week — positive/negative, (2) Active issues and response status, (3) Investor Day preparation progress, (4) Next week\'s scheduled communications activities, (5) Actions needed from CEO.',
            'Ask Copilot: From this meeting, what was the debate about whether to respond proactively to the Zava Bank NPL media story? What were the arguments for and against responding before the H1 results?'
          ]
        },
        {
          tool: '📓 Copilot Notebook',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via copilot.microsoft.com > Notebook tab. Upload up to 5 files and set a system instruction. Best for synthesising insights across multiple documents simultaneously.',
          prompts: [
            'Upload 03_Zava_Group_Strategy_Framework.docx and Email_08_Coal_Trading_Breach.docx to Copilot Notebook. Set instruction: "You are a senior communications advisor helping Zava Group manage 3 simultaneous reputation risks." Ask: Given the 3 active reputation risks (Bank NPL, RSPO, coal breach), which one poses the greatest long-term brand damage if not addressed proactively? What is the recommended communications priority order and the single most important action in the next 7 days?',
            'Upload 03_Zava_Group_Strategy_Framework.docx. Ask: The ZAVA FORWARD 2030 strategy emphasises ESG leadership as Pillar 3. But we have an active RSPO suspension in our plantation division. How do we credibly communicate an ESG leadership position while acknowledging the RSPO failure? Draft the specific language for the Investor Day ESG section that is honest about the challenge but compelling about our commitment.'
          ]
        },
        {
          tool: '🤝 Cowork (Frontier)',
          license: 'M365 Copilot + Frontier Program',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Cowork is an autonomous agent that takes actions across Microsoft 365 on your behalf — sending emails, scheduling meetings, creating documents, posting in Teams, and scheduling recurring tasks. Access: m365.cloud.microsoft > left nav > Agents > Cowork. Requires Frontier program enrollment.',
          prompts: [
            'Do all of the following: (1) Monitor Malaysian financial media (The Edge, StarBiz, Reuters) for any Zava Group mentions in the past 48 hours. (2) Draft 2 holding statements — one for NPL enquiries, one for RSPO enquiries. (3) Save to OneDrive as "Media Holding Statements - APPROVED". (4) Email to Group CCO and GC for approval before distribution. (5) Distribute to all 11 Division Communications Heads once approved.',
            'Do all of the following for Investor Day: (1) Draft the 2-page Investor Day media invitation and pre-event Q&A talking points for journalists. (2) Create the Investor Day registration page on SharePoint. (3) Email invitations to the 25-person media list. (4) Prepare the media briefing room layout and logistics checklist. (5) Schedule a full Investor Day rehearsal with all presenters 2 weeks before the event.'
          ]
        },
        {
          tool: '🤖 Word Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to a Word document. Open the .docx in Word for Web > Copilot pane > + New Agent > name it, write a description, set the document as knowledge source > Share. Colleagues chat with it in Teams or M365 Copilot.',
          prompts: [
            'Open 03_Zava_Group_Strategy_Framework.docx in Word for Web. Create an agent called "Zava Communications Playbook Bot". Description: "Answers questions from Division Communications Heads on approved messages, holding statements, media handling protocols, spokespersons by issue type, and Investor Day communications guidelines." Share with all 11 Division Communications Heads.',
            'Demo: A Division Communications Head gets a call from Reuters at 5:30pm asking about the coal trading breach: "Can you confirm that Zava Group\'s coal trading desk exceeded its position limit by USD 2.4M and that a trader has been suspended?" The team member immediately asks the agent: "What is our approved holding statement for the coal trading breach and what topics are we authorised to discuss vs redirect to Group CCO?" Show the agent enabling an instant, policy-consistent media response.'
          ]
        },
        {
          tool: '🤖 PowerPoint Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to a PowerPoint presentation. Great for strategy decks or Board presentations many people need to reference. Same setup as Word Agent but using a .pptx file.',
          prompts: [
            'Create a PowerPoint from the crisis playbook. Create an agent called "Zava Crisis Communications Q&A Bot". Share with all Communications Heads and senior management.',
            'Demo: The CCO asks "A Tier 2 crisis has just materialised — a social media post alleging Zava bank mis-sold an investment product to elderly customers has gone viral with 45,000 shares. Under our crisis playbook, what is the mandatory response timeline, who is the approved spokesperson, and what is the Tier 2 holding statement template?" Show the agent providing an instant, playbook-grounded crisis response.'
          ]
        },
        {
          tool: '🤖 Excel Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to an Excel workbook. Colleagues ask data questions in plain English without opening Excel. Open .xlsx in Excel for Web > Copilot pane > + New Agent > set workbook as knowledge source > share.',
          prompts: [
            'Open the Communications Tracker workbook in Excel for Web. Create an agent called "Zava Communications Issue Tracker Q&A". Description: "Instant answers on active media issues, Investor Day preparation status, and stakeholder sentiment for the CCO and Group CEO." Share with communications leadership.',
            'Demo: Ask "Which active communication issue has the most negative stakeholder sentiment and is our response classified as adequate?" Then: "How many Investor Day presentation sections are still awaiting CEO approval and when is the deadline?" Show the CCO getting instant communications programme intelligence.'
          ]
        },
        {
          tool: '🏗 Agent Builder (Copilot Studio)',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Build a custom declarative agent in Copilot Studio — no coding required. Access: copilotstudio.microsoft.com > Create > New Agent. Add name, description, knowledge sources (SharePoint URLs or uploaded files), topics/actions. Publish to Teams in under 10 minutes.',
          prompts: [
            'Go to copilotstudio.microsoft.com > Create > New Agent. Name it "Zava Communications Intelligence Agent". Description: "Supports the Group Communications team with instant answers on holding statements, crisis protocols, Investor Day preparation status, media sentiment trends, and stakeholder engagement strategies — enabling faster, consistent, on-brand communications across all 11 Zava divisions." Upload 03_Zava_Group_Strategy_Framework.docx and Email_08_Coal_Trading_Breach.docx. Add topics: "Crisis Communications", "Media Handling", "Investor Day", "Stakeholder Sentiment". Publish to Teams for Communications teams.',
            'Demo the agent: It is 11pm on a Sunday. The Group CCO sees a tweet going viral: a palm oil NGO has posted satellite images allegedly showing fresh deforestation at Perkebunan Lestari — captioned "Zava Group destroys rainforest while claiming ESG leadership". The tweet has 12,000 retweets in 2 hours. The CCO asks the agent: "What are the facts about Perkebunan Lestari\'s current status, what is our approved holding statement for RSPO-related media, and should I activate a Tier 1 or Tier 2 crisis response given the social media virality?" Show how the agent enables a calm, informed crisis response at 11pm.'
          ]
        }
      ]
    },
    {
      id: 'dept-it-digital',
      sectorId: 'department',
      subsector: '',
      name: 'IT & Digital',
      icon: '💻',
      color: '#006064',
      accent: '#00838F',
      company: 'Zava Group Holdings — Group IT Division',
      tagline: 'M365 Copilot rollout 87K users, ERP harmonisation, cybersecurity incident response, data lake.',
      scenario: 'The Group IT Division leads digital transformation across 87,420 users in 3 countries. Current priorities: Microsoft 365 Copilot rollout (Phase 1: 2,400 licences, Phase 2: full estate), ERP harmonisation (3 ERPs → SAP S/4HANA single platform), shared data lake on Azure, and a cybersecurity posture uplift following a phishing incident at Zava Bank.',
      files: [
        '03_Zava_Group_Strategy_Framework.docx',
        '02_Zava_Group_Policy_Handbook.docx'
      ],
      prompts: [
        {
          tool: '🤖 Copilot Chat (Basic)',
          license: 'Free — no M365 Copilot license needed',
          account: 'Sasha Ouellet — SashaO@ABSx62256373.OnMicrosoft.com',
          desc: '',
          prompts: [
            'I am the Group CIO of an 87,000-employee Malaysian conglomerate. We are rolling out Microsoft 365 Copilot to 2,400 priority users in Phase 1. The biggest adoption barrier is that most employees have not changed their daily work habits and are using Copilot only for occasional email drafting. Draft a 250-word Copilot adoption acceleration plan covering: (1) How to identify and develop Copilot champions in each division, (2) The 3 highest-value use cases by department that should be demonstrated in the first 30 days, (3) How to measure adoption (daily active usage, time saved, use case diversity).',
            'What is a shared data lake architecture for a diversified conglomerate? How should we structure the Azure Data Lake Gen2 for a group with 11 divisions across different industries — each with different data formats, governance requirements, and security classifications? What are the key design decisions?',
            'Explain what the cybersecurity incident response process should be for a financial services institution in Malaysia. What are the BNM reporting obligations after a phishing incident that compromised 48 employee credentials at Zava Bank? What containment and remediation steps should be completed within 24, 48, and 72 hours?'
          ]
        },
        {
          tool: '🔍 Researcher',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via Microsoft 365 Copilot Chat (copilot.microsoft.com or Teams) > click Agents > Researcher. Grounds answers in live web sources and your organisation data with full citations.',
          prompts: [
            'Research Microsoft 365 Copilot adoption best practices for large enterprises. What are the proven adoption frameworks — Microsoft\'s own, Gartner, Forrester? What are the key metrics that indicate successful Copilot adoption? How have comparable Asian conglomerates structured their Copilot rollout? Cite Microsoft or analyst reports.',
            'Research SAP S/4HANA implementation best practices for multi-division conglomerates in ASEAN. What are the common failure modes in large SAP implementations? What is the typical implementation timeline and cost for 87,000 users across MY, ID, and IN? How do successful companies manage the change management challenge? Cite Gartner or SAP partner reports.'
          ]
        },
        {
          tool: '📊 Analyst',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via Microsoft 365 Copilot Chat > click Agents > Analyst. Upload an Excel or CSV file. Analyst runs Python-style analysis, builds charts, and interprets results without you writing a single formula.',
          prompts: [
            'Upload 03_Zava_Group_Strategy_Framework.docx (use as reference). Ask Analyst to help structure: Build a Copilot adoption ROI model. Inputs: 2,400 users in Phase 1, MYR 195/user/month licence cost. Savings assumptions from Microsoft benchmark data: email drafting saves 2hrs/week, meeting summaries saves 1.5hrs/week, document drafting saves 3hrs/week. Average cost per employee-hour: MYR 42. Calculate: (1) Weekly time saving per user, (2) Annual cost saving for 2,400 users, (3) Licence cost vs saving, (4) ROI and payback in months. Show sensitivity to adoption rate (30%, 50%, 70% of users actively using).',
            'Ask Analyst: Build a cybersecurity risk heat map. For 12 attack vectors (phishing, ransomware, insider threat, supply chain, API attack, DDoS, social engineering, credential stuffing, zero-day exploit, physical security, cloud misconfiguration, third-party vendor), score: (1) Likelihood (1-5) based on current controls, (2) Impact (1-5) based on assets at risk. Plot on a 5x5 matrix. For the top 5 risks, calculate the estimated financial impact if a breach occurs (downtime cost + remediation + regulatory fine + reputational damage).'
          ]
        },
        {
          tool: '📊 Copilot in Excel',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open 03_Zava_Group_Strategy_Framework.docx. Create a companion IT Programme Tracker workbook. Ask Copilot: Create Sheet 1 with columns: Programme | Division Scope | Budget (MYR M) | Spent to Date | % Spent | Timeline | Current Phase | Status | Key Risk | Next Milestone. Populate with 5 IT programmes (Copilot rollout, SAP S/4HANA, Data Lake, Cybersecurity posture, Digital workplace). Apply RAG conditional formatting.',
            'Ask Copilot: Build a Copilot adoption dashboard on Sheet 2. For each of the 11 divisions in Phase 1 rollout, show: (1) Licences allocated, (2) Monthly active users, (3) Adoption rate %, (4) Top 3 Copilot use cases by department, (5) Average prompts per user per day, (6) User satisfaction score. Highlight divisions with adoption below 40% in red — these need targeted intervention.',
            'Ask Copilot: Create a cybersecurity incident tracker on Sheet 3. For each security incident in the past 12 months: (1) Date, (2) Type, (3) Division affected, (4) Systems compromised, (5) Data at risk, (6) Response time (hours), (7) Containment status, (8) BNM/PDPA notification made (Y/N), (9) Root cause, (10) Remediation completed (Y/N). Calculate average response time and % incidents with BNM notification completed within required timeframe.'
          ]
        },
        {
          tool: '📝 Copilot in Word',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open 02_Zava_Group_Policy_Handbook.docx. Ask Copilot: Update the Data Privacy & Cybersecurity Policy with a new chapter on M365 Copilot Data Governance. Cover: (1) What data Copilot can access — only Microsoft Graph data within the user\'s permission boundary, (2) What data employees must NOT input into Copilot — PDPA-classified personal data, board-sensitive information, unpublished financial results, (3) How to classify a prompt before sending it, (4) Who is responsible for Copilot-generated content — the employee, not Microsoft, (5) Incident reporting if sensitive data is accidentally shared. 4 pages, policy format.',
            'Ask Copilot: Draft the Zava Group Copilot Rollout Communication for all 2,400 Phase 1 users. The communication should: explain what M365 Copilot is in 3 simple sentences, describe the top 5 use cases for each user\'s role (tailored for Finance, HR, Operations, and Senior Management), provide links to the 3 training resources, note the DLP data handling rules, and invite users to the first Copilot Champions session next week. Exciting, accessible tone.',
            'Ask Copilot: Draft the SAP S/4HANA Business Case for the Board approval paper. Cover: (1) Current state — 3 ERPs (SAP ECC for manufacturing, Oracle for financial services, Microsoft Dynamics for BPO), (2) The integration pain — monthly intercompany reconciliation takes 22 person-days, (3) Proposed solution — SAP S/4HANA single ERP, 42-month implementation, (4) Investment — MYR 84M total, (5) Benefits — 14-day monthly close reduced to 5 days, real-time group P&L, MYR 22M annual operational saving, (6) Risk — parallel run, data migration complexity. Board paper format.'
          ]
        },
        {
          tool: '🎯 Copilot in PowerPoint',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Ask Copilot in PowerPoint: Create a 10-slide IT Digital Transformation Board update. Include: (1) Digital transformation roadmap overview, (2) M365 Copilot — Phase 1 adoption results and Phase 2 plan, (3) Copilot ROI — time saved and cost avoided, (4) SAP S/4HANA business case, (5) Azure Data Lake — architecture and progress, (6) Cybersecurity posture — phishing incident and remediation, (7) Cybersecurity heat map — top 5 risks, (8) Digital workplace modernisation, (9) IT budget vs spend by programme, (10) FY2026 IT priorities. Teal and white colour scheme.',
            'Ask Copilot: Create a 3-slide Copilot adoption showcase for the CEO town hall. Slide 1: What Copilot can do — 5 use cases with before/after time comparison. Slide 2: Adoption results from Phase 1 — which divisions are leading, which are lagging. Slide 3: Phase 2 rollout plan — all 87,420 users by end of FY2026.',
            'Ask Copilot: Create a 2-slide cybersecurity incident summary for the Board Audit Committee. Slide 1: The phishing incident — what happened, how many credentials compromised, immediate containment actions. Slide 2: The 5 cybersecurity posture improvements implemented since the incident and the updated risk heat map.'
          ]
        },
        {
          tool: '📧 Copilot in Outlook',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Ask Copilot in Outlook: Draft the Group CIO\'s email to all Division IT Heads announcing the Microsoft 365 Copilot Phase 2 rollout plan. The email should: confirm the Phase 2 timeline (Q3 FY2025 — all remaining users), division-by-division rollout schedule, mandatory Copilot literacy training requirement, and the DLP data governance rules that must be communicated to all users before activation.',
            'Ask Copilot: Draft the BNM cybersecurity incident notification letter following the phishing incident at Zava Bank. Under BNM\'s Risk Management in Technology (RMiT) policy, this notification is required within 24 hours of discovering the incident. The letter should: describe the incident (48 credentials compromised via phishing email, no customer data accessed, contained within 6 hours), confirm containment actions, and state the remediation timeline.',
            'Ask Copilot: Draft an invitation email to all 2,400 Phase 1 Copilot users for the first "Copilot Champions Showcase" event. The email should: announce the event date and format (2-hour online), note that 5 employees will present their top Copilot use cases and time savings, invite attendees to register, and offer a Copilot productivity toolkit download link. Energetic, community-building tone.'
          ]
        },
        {
          tool: '🎙 Copilot in Teams',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Use your OWN existing recorded Teams meetings. Open a meeting recap in Teams > Recap tab. Copilot generates summaries, action items, and follow-up drafts grounded in the actual transcript.',
          prompts: [
            'Open an existing recorded Teams meeting recap from an IT steering or project meeting. Ask Copilot: Identify all IT programme delays, adoption blockers, and technical issues discussed. Create an action log with the IT team owner and deadline.',
            'Ask Copilot: Draft the IT leadership weekly update for the CIO. Structure: (1) Copilot Phase 1 adoption rate this week vs target, (2) SAP S/4HANA implementation — phase and milestones, (3) Data Lake — datasets onboarded this week, (4) Cybersecurity — any new incidents or alerts, (5) Budget status vs plan.',
            'Ask Copilot: From this meeting, what specific concerns did Division MDs raise about the SAP S/4HANA implementation timeline? Was there any discussion about delaying the go-live date?'
          ]
        },
        {
          tool: '📓 Copilot Notebook',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via copilot.microsoft.com > Notebook tab. Upload up to 5 files and set a system instruction. Best for synthesising insights across multiple documents simultaneously.',
          prompts: [
            'Upload 03_Zava_Group_Strategy_Framework.docx and 02_Zava_Group_Policy_Handbook.docx to Copilot Notebook. Set instruction: "You are the Group CIO advising on Copilot adoption and digital transformation." Ask: Based on the strategy and policy documents, which 3 divisions should be prioritised for Phase 2 Copilot rollout to maximise business impact? For each, identify the top 2 use cases that would drive the highest ROI.',
            'Upload 02_Zava_Group_Policy_Handbook.docx. Ask: Under our current Data Privacy & Cybersecurity Policy, is an employee allowed to paste Zava Bank customer loan data into M365 Copilot to ask it to summarise the NPL trends? If not, what is the policy basis for the prohibition and what alternative approach should the employee use?'
          ]
        },
        {
          tool: '🤝 Cowork (Frontier)',
          license: 'M365 Copilot + Frontier Program',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Cowork is an autonomous agent that takes actions across Microsoft 365 on your behalf — sending emails, scheduling meetings, creating documents, posting in Teams, and scheduling recurring tasks. Access: m365.cloud.microsoft > left nav > Agents > Cowork. Requires Frontier program enrollment.',
          prompts: [
            'Do all of the following for Copilot Phase 2 planning: (1) Research Microsoft\'s recommended large-scale Copilot rollout methodology for enterprises with 50K+ users. (2) Draft the Phase 2 rollout plan covering all 11 divisions and 85,000 remaining users — phased over 12 months with division priority, training timeline, and DLP governance. (3) Save to OneDrive as "Copilot Phase 2 Rollout Plan". (4) Email to CIO, CHRO, and all Division IT Heads for review. (5) Schedule a Phase 2 kickoff meeting with all Division IT Heads.',
            'Do all of the following for cybersecurity: (1) Research the BNM RMiT 2023 requirements for technology risk management at licensed banks — specifically for phishing incident response and multi-factor authentication mandates. (2) Draft a 90-day cybersecurity posture improvement plan for Zava Bank. (3) Email to the Zava Bank CIO and Head of IT Security for review. (4) Create a cybersecurity remediation tracker in SharePoint. (5) Schedule a weekly cybersecurity taskforce meeting until all critical items are resolved.'
          ]
        },
        {
          tool: '🤖 Word Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to a Word document. Open the .docx in Word for Web > Copilot pane > + New Agent > name it, write a description, set the document as knowledge source > Share. Colleagues chat with it in Teams or M365 Copilot.',
          prompts: [
            'Open 02_Zava_Group_Policy_Handbook.docx in Word for Web. Create an agent called "Zava IT & Digital Policy Bot". Description: "Answers questions from IT teams, Division CIOs, and employees on Copilot data governance rules, cybersecurity policies, acceptable use of IT systems, incident reporting procedures, and the SAP S/4HANA implementation requirements." Share with all Division IT Heads and publish to the employee IT helpdesk portal.',
            'Demo: An employee asks "I want to use Copilot to summarise the last 3 months of email threads about a confidential M&A deal we are working on. Is this allowed under the Copilot Data Governance Policy and what classification does M&A correspondence fall under?" Show the agent providing a precise, data-governance-grounded answer.'
          ]
        },
        {
          tool: '🤖 PowerPoint Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to a PowerPoint presentation. Great for strategy decks or Board presentations many people need to reference. Same setup as Word Agent but using a .pptx file.',
          prompts: [
            'Create a PowerPoint from the Board IT update. Create an agent called "IT Digital Transformation Q&A Bot". Share with Board members and the Group CEO.',
            'Demo: A Board member asks "We approved MYR 84M for the SAP S/4HANA implementation 12 months ago. We\'re 30% through the budget — are we on track and what is the current projected final cost?" Show the agent providing a programme-progress-grounded answer.'
          ]
        },
        {
          tool: '🤖 Excel Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to an Excel workbook. Colleagues ask data questions in plain English without opening Excel. Open .xlsx in Excel for Web > Copilot pane > + New Agent > set workbook as knowledge source > share.',
          prompts: [
            'Open the IT Programme Tracker workbook in Excel for Web. Create an agent called "IT Programme Q&A". Description: "Instant answers on Copilot adoption rates, SAP implementation progress, cybersecurity incidents, and IT budget vs spend for the CIO and Group CEO." Share with IT leadership.',
            'Demo: Ask "Which division has the lowest Copilot adoption rate and what percentage of their Phase 1 licences are being used daily?" Then: "How many security incidents have occurred in the past 3 months and what is our average containment time vs the BNM requirement?" Show the CIO getting instant IT programme intelligence.'
          ]
        },
        {
          tool: '🏗 Agent Builder (Copilot Studio)',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Build a custom declarative agent in Copilot Studio — no coding required. Access: copilotstudio.microsoft.com > Create > New Agent. Add name, description, knowledge sources (SharePoint URLs or uploaded files), topics/actions. Publish to Teams in under 10 minutes.',
          prompts: [
            'Go to copilotstudio.microsoft.com > Create > New Agent. Name it "Zava IT Digital Intelligence Agent". Description: "Supports the Group IT Division and Division IT teams with instant answers on Copilot data governance, cybersecurity policies, SAP implementation requirements, data lake standards, and digital transformation programme status — enabling faster, policy-consistent IT decisions across 87,420 users in 11 divisions." Upload 03_Zava_Group_Strategy_Framework.docx and 02_Zava_Group_Policy_Handbook.docx. Add topics: "Copilot Governance", "Cybersecurity Policy", "SAP Implementation", "Data Lake", "Incident Response". Publish to Teams for IT teams.',
            'Demo the agent: The Zava Bank Head of IT Security calls the Group CIO at 10pm: "We\'ve just detected what appears to be a ransomware payload that has encrypted 12 servers in our Petaling Jaya data centre. Our DR plan requires us to failover to our disaster recovery site in Cyberjaya within 4 hours. What is our BNM notification obligation and timeline, and does this qualify as a Tier 1 crisis that requires immediate Group CEO and Board notification?" Show how the agent enables an instant, policy-grounded cyber crisis response.'
          ]
        }
      ]
    },
    {
      id: 'dept-esg',
      sectorId: 'department',
      subsector: '',
      name: 'ESG & Sustainability',
      icon: '🌱',
      color: '#1B5E20',
      accent: '#2E7D32',
      company: 'Zava Group Holdings — Group ESG Division',
      tagline: 'RSPO suspension, EUDR non-compliance, Net Zero 2050, Bursa sustainability reporting.',
      scenario: 'The Group ESG Division drives sustainability strategy, reporting, and stakeholder engagement. Critical issues: Perkebunan Lestari RSPO suspension (8,200ha peatland), EUDR compliance deadline Q4 2025, Bursa Malaysia enhanced sustainability reporting from FY2025, and the Net Zero 2050 pathway requiring a 40% Scope 1 reduction by 2030.',
      files: [
        '20_Zava_ESG_Sustainability_Framework.docx',
        '22_Zava_Plantation_RSPO_Audit.docx'
      ],
      prompts: [
        {
          tool: '🤖 Copilot Chat (Basic)',
          license: 'Free — no M365 Copilot license needed',
          account: 'Sasha Ouellet — SashaO@ABSx62256373.OnMicrosoft.com',
          desc: '',
          prompts: [
            'I am the Group Chief Sustainability Officer of a Malaysian palm oil and diversified conglomerate. Our Perkebunan Lestari estate has had its RSPO certification suspended due to 8,200ha of peatland being cultivated beyond 3 metres depth — a major nonconformance. European CPO buyers are threatening to cancel contracts. Draft a 250-word brief for our Board on: (1) What RSPO suspension means commercially — which markets are now blocked, (2) The remediation options for a peatland nonconformance (rewetting, conservation set-aside, cessation of cultivation), (3) The minimum timeline to achieve RSPO reinstatement and the interim commercial mitigation options.',
            'Explain what EUDR (EU Deforestation Regulation) requires from a palm oil exporter. What is the due diligence system they must maintain, what supply chain documentation is required, and what are the consequences for failing to comply by the EUDR enforcement date?',
            'What is a credible Net Zero 2050 pathway for a diversified conglomerate with emissions from chemicals, palm oil, banking, manufacturing, and BPO? How should we set Science-Based Targets (SBTi) when we have 11 different business units with very different emission profiles?'
          ]
        },
        {
          tool: '🔍 Researcher',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via Microsoft 365 Copilot Chat (copilot.microsoft.com or Teams) > click Agents > Researcher. Grounds answers in live web sources and your organisation data with full citations.',
          prompts: [
            'Research RSPO suspension remediation requirements. What are the specific steps a palm oil company must take to achieve reinstatement after suspension? Are there any precedent cases of companies successfully reinstating RSPO certification after a peatland nonconformance, and how long did it take? Cite RSPO official documentation.',
            'Research EUDR compliance requirements for Malaysian palm oil exporters. What is the practical implementation timeline, what systems and certifications are needed, and how are Malaysian exporters responding — MPOA, MPIC, or individual company approaches? Cite official EU, MPOB, or industry sources.'
          ]
        },
        {
          tool: '📊 Analyst',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via Microsoft 365 Copilot Chat > click Agents > Analyst. Upload an Excel or CSV file. Analyst runs Python-style analysis, builds charts, and interprets results without you writing a single formula.',
          prompts: [
            'Upload 20_Zava_ESG_Sustainability_Framework.docx (use as reference). Ask Analyst to help structure: Build an ESG performance dashboard. For Zava Group FY2022-FY2024, track: (1) GHG Scope 1 and Scope 2 (tCO2e), (2) GHG intensity per MYR M revenue, (3) RSPO certified area %, (4) EUDR compliance status by estate, (5) Women in leadership %, (6) TRIR (safety), (7) Community investment (MYR M). Compare against our FY2025 and FY2030 targets. Show as a RAG scorecard.',
            'Upload 20_Zava_ESG_Sustainability_Framework.docx. Ask: Model 3 Net Zero pathways to 2050. Scenario A: Business as usual — no major decarbonisation investment, reach Net Zero 2050 through offsets only. Scenario B: Managed transition — MYR 1.8B decarbonisation investment over 10 years, achieve 60% Scope 1 reduction by 2040. Scenario C: Accelerated — MYR 3.2B investment, meet SBTi 1.5°C pathway, exit coal by 2028. For each scenario, calculate cumulative emissions, cumulative cost, and carbon offset cost at USD 45/tCO2e. Which is cheapest over 30 years?'
          ]
        },
        {
          tool: '📊 Copilot in Excel',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open 20_Zava_ESG_Sustainability_Framework.docx. Create a companion ESG Dashboard workbook. Ask Copilot: Create Sheet 1 with the Group ESG KPI scorecard for FY2024. For each of 18 KPIs (Scope 1-3 emissions, RSPO certified area, EUDR compliance, TRIR, women in leadership, waste diversion, water intensity, community investment, ESG rating), show: (1) FY2022 actual, (2) FY2023 actual, (3) FY2024 actual, (4) FY2025 target, (5) FY2030 target, (6) Status (On Track/At Risk/Missed). Apply RAG formatting.',
            'Ask Copilot: Build an EUDR compliance tracker on Sheet 2. For each of the 12 estates, show: (1) Estate name and country, (2) Total area (ha), (3) EUDR-compliant area (ha), (4) Non-compliant area (ha), (5) Non-compliance reason (peatland, HCV overlap, deforestation risk), (6) EUDR compliance action status, (7) Target compliance date. Calculate overall EUDR compliance rate. Highlight non-compliant estates in red.',
            'Ask Copilot: Create a RSPO reinstatement roadmap on Sheet 3. For the 4 major nonconformances at Perkebunan Lestari, show: (1) Nonconformance description, (2) Root cause, (3) Required corrective action, (4) Responsible team, (5) Estimated cost (MYR M), (6) Timeline, (7) Evidence required for RSPO reinstatement auditor. Calculate total remediation cost and the earliest possible reinstatement date.'
          ]
        },
        {
          tool: '📝 Copilot in Word',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open 22_Zava_Plantation_RSPO_Audit.docx. Ask Copilot: Draft the RSPO Corrective Action Plan (CAP) response document for submission to RSPO. For each of the 4 major nonconformances: (1) NC description and audit finding reference, (2) Root cause analysis (using 5-Why methodology), (3) Specific corrective actions with milestones and deadlines, (4) Evidence to be provided at the re-audit, (5) Responsible team and manager name. Format as a formal RSPO CAP document.',
            'Open 20_Zava_ESG_Sustainability_Framework.docx. Ask Copilot: Draft the EUDR compliance communication for our 14 European CPO buyers. The letter should: acknowledge the EUDR deadline, confirm our EUDR due diligence system is in place for 10 of 12 estates, disclose that Perkebunan Lestari and Perkebunan Nusantara Zava require remediation, explain our EUDR remediation timeline, and propose supply continuity from our 10 fully compliant estates during the remediation period. Professional, transparent tone.',
            'Ask Copilot: Write the Bursa Malaysia Sustainability Report climate risk section. Follow TCFD requirements: (1) Governance — who oversees climate risk at Board and management level, (2) Strategy — climate risks and opportunities identified, impact on financial planning, (3) Risk Management — how we identify, assess, and manage climate risks, (4) Metrics and Targets — Scope 1/2/3 emissions data, GHG reduction targets, SBTi status. Use TCFD 2023 framework, with Malaysian Bursa SR guidelines cross-reference.'
          ]
        },
        {
          tool: '🎯 Copilot in PowerPoint',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Ask Copilot in PowerPoint: Create a 10-slide ESG Board presentation. Include: (1) Group ESG overview — performance vs targets FY2024, (2) RSPO suspension — situation, remediation plan, commercial impact, (3) EUDR compliance — 10/12 estates compliant, 2 requiring action, (4) Net Zero 2050 — 3 pathways, recommended scenario, (5) Scope 1/2 emissions dashboard, (6) Social — safety TRIR trend, DEI progress, community investment, (7) Bursa sustainability reporting — compliance status, (8) MSCI ESG rating — current and improvement actions, (9) ESG-linked financing — green sukuk opportunity, (10) Board decisions required. Green and white ESG colour scheme.',
            'Ask Copilot: Create a 3-slide EUDR compliance update for European CPO buyers. Slide 1: Our EUDR compliance status — 10/12 estates compliant (show on map). Slide 2: The 2 non-compliant estates — remediation timeline and interim supply plan. Slide 3: Our long-term EUDR commitment — No Deforestation, No Peat, No Exploitation policy.',
            'Ask Copilot: Create a 2-slide Net Zero 2050 pathway comparison. Slide 1: 3 scenarios — cumulative emissions and cost. Slide 2: Our recommended pathway (Scenario B) — key investments, milestone emissions targets, and cumulative offset cost avoided vs Scenario A.'
          ]
        },
        {
          tool: '📧 Copilot in Outlook',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Ask Copilot in Outlook: Draft a letter to RSPO\'s Certification Team formally submitting Zava Agribusiness\'s Corrective Action Plan for the Perkebunan Lestari suspension. The letter should: reference the audit report date and CB (certification body), confirm our commitment to full remediation, highlight the 3 corrective actions already completed, attach the full CAP document, and request a timeline for the re-audit scheduling. Formal RSPO correspondence format.',
            'Ask Copilot: Draft a proactive email to our top 6 European CPO buyers (who collectively represent 34% of our export volume) ahead of the EUDR enforcement date. The email should: confirm our EUDR readiness for 10 estates, disclose the 2 non-compliant estates transparently, provide the remediation timeline, and offer a contract amendment for the transitional period to supply only from compliant estates. Transparent, partnership-focused tone.',
            'Ask Copilot: Draft the Group CSO\'s email to all 12 estate managers announcing the mandatory EUDR due diligence training programme. The training covers the geolocation mapping requirement, supply chain documentation, and the customer declaration process. All estate managers must complete the training within 30 days. Emphasise that EUDR compliance is not optional — non-compliance puts EU export contracts at risk.'
          ]
        },
        {
          tool: '🎙 Copilot in Teams',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Use your OWN existing recorded Teams meetings. Open a meeting recap in Teams > Recap tab. Copilot generates summaries, action items, and follow-up drafts grounded in the actual transcript.',
          prompts: [
            'Open an existing recorded Teams meeting recap from an ESG or sustainability committee meeting. Ask Copilot: Identify all RSPO, EUDR, and carbon target discussions. Create an action log for the ESG team covering remediation, reporting, and stakeholder engagement.',
            'Ask Copilot: Draft the ESG team\'s weekly update for the Group CSO. Structure: (1) RSPO CAP submission status, (2) EUDR compliance progress by estate, (3) Scope 1 emissions tracker — vs target, (4) Bursa Sustainability Report — sections completed, (5) MSCI ESG rating engagement.',
            'Ask Copilot: From this meeting, what was the debate about whether to engage an independent third-party consultant to support the RSPO reinstatement process? What were the budget concerns raised?'
          ]
        },
        {
          tool: '📓 Copilot Notebook',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via copilot.microsoft.com > Notebook tab. Upload up to 5 files and set a system instruction. Best for synthesising insights across multiple documents simultaneously.',
          prompts: [
            'Upload 20_Zava_ESG_Sustainability_Framework.docx and 22_Zava_Plantation_RSPO_Audit.docx to Copilot Notebook. Set instruction: "You are the Group CSO advising the Board on ESG risk management." Ask: Based on the ESG framework and RSPO audit, what is the realistic fastest timeline for RSPO reinstatement at Perkebunan Lestari if we commit maximum resources? What is the commercial cost of every additional month the suspension continues?',
            'Upload 20_Zava_ESG_Sustainability_Framework.docx. Ask: Zava Group is considering applying for a Green Sukuk to fund our Net Zero transition investments. What ESG credentials must we demonstrate to achieve a Green Sukuk certification under SC Malaysia\'s Sustainable and Responsible Investment (SRI) sukuk framework? What is the gap between our current ESG performance and the required standard?'
          ]
        },
        {
          tool: '🤝 Cowork (Frontier)',
          license: 'M365 Copilot + Frontier Program',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Cowork is an autonomous agent that takes actions across Microsoft 365 on your behalf — sending emails, scheduling meetings, creating documents, posting in Teams, and scheduling recurring tasks. Access: m365.cloud.microsoft > left nav > Agents > Cowork. Requires Frontier program enrollment.',
          prompts: [
            'Do all of the following: (1) Research the RSPO CAP (Corrective Action Plan) requirements and download the latest RSPO CAP template from the RSPO website. (2) Draft the full RSPO CAP for Perkebunan Lestari covering all 4 major nonconformances using the official template. (3) Save to OneDrive as "Perkebunan Lestari RSPO CAP - DRAFT". (4) Email to the Group CSO and the estate manager for review within 5 days. (5) Schedule a CAP review meeting with the RSPO certification body representative.',
            'Do all of the following for the Bursa Sustainability Report: (1) Research Bursa Malaysia\'s FY2025 enhanced sustainability reporting requirements for main market listed companies. (2) Identify any new mandatory disclosures vs FY2024. (3) Draft the new mandatory disclosures for the Group ESG team. (4) Email to Group CSO and the Company Secretary for review. (5) Create a Bursa Sustainability Report tracker in SharePoint with all required sections and deadlines.'
          ]
        },
        {
          tool: '🤖 Word Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to a Word document. Open the .docx in Word for Web > Copilot pane > + New Agent > name it, write a description, set the document as knowledge source > Share. Colleagues chat with it in Teams or M365 Copilot.',
          prompts: [
            'Open 20_Zava_ESG_Sustainability_Framework.docx in Word for Web. Create an agent called "Zava ESG & Sustainability Policy Bot". Description: "Answers questions from estate managers, division sustainability teams, and the Group ESG Division on RSPO requirements, EUDR compliance obligations, GRI reporting standards, Bursa SR requirements, and the Group Net Zero pathway." Share with all Division Sustainability teams and estate managers.',
            'Demo: An estate manager asks "I have just discovered a new drainage channel was dug in our estate last month — it appears to be within 500 metres of a protected peat area. Under our Group NDPE Policy, is this a reportable incident and do I need to notify the RSPO certification body before our next planned audit?" Show the agent providing a policy-grounded, action-oriented compliance answer.'
          ]
        },
        {
          tool: '🤖 PowerPoint Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to a PowerPoint presentation. Great for strategy decks or Board presentations many people need to reference. Same setup as Word Agent but using a .pptx file.',
          prompts: [
            'Create a PowerPoint from the ESG Board presentation. Create an agent called "Group ESG Board Q&A Bot". Share with Board members and the Group CSO.',
            'Demo: A Board member asks "If we miss the EUDR enforcement date for the 2 non-compliant estates, what is the estimated volume of CPO exports at risk and what is the MYR revenue impact on our Agribusiness division?" Show the agent providing a commercial-impact-grounded ESG risk answer.'
          ]
        },
        {
          tool: '🤖 Excel Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to an Excel workbook. Colleagues ask data questions in plain English without opening Excel. Open .xlsx in Excel for Web > Copilot pane > + New Agent > set workbook as knowledge source > share.',
          prompts: [
            'Open the ESG Dashboard workbook in Excel for Web. Create an agent called "Group ESG Performance Q&A". Description: "Instant answers on GHG emissions, RSPO compliance, EUDR status, safety TRIR, DEI metrics, and Bursa SR requirements for the Group CSO and Board ESG Committee." Share with ESG leadership.',
            'Demo: Ask "What is our Scope 1 GHG emissions trajectory vs our 2030 reduction target — are we on track?" Then: "What is the total certified RSPO area across all 12 estates and what % of our CPO volume is RSPO-certified?" Show the CSO getting instant ESG performance intelligence.'
          ]
        },
        {
          tool: '🏗 Agent Builder (Copilot Studio)',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Build a custom declarative agent in Copilot Studio — no coding required. Access: copilotstudio.microsoft.com > Create > New Agent. Add name, description, knowledge sources (SharePoint URLs or uploaded files), topics/actions. Publish to Teams in under 10 minutes.',
          prompts: [
            'Go to copilotstudio.microsoft.com > Create > New Agent. Name it "Zava ESG Intelligence Agent". Description: "Supports the Group ESG Division, Division Sustainability teams, and estate managers with instant answers on RSPO requirements, EUDR compliance, GHG reporting standards, Bursa sustainability disclosures, Net Zero pathway, and NDPE policy obligations — enabling faster, consistent, and credible ESG management across all 11 Zava divisions." Upload 20_Zava_ESG_Sustainability_Framework.docx and 22_Zava_Plantation_RSPO_Audit.docx. Add topics: "RSPO Compliance", "EUDR Requirements", "GHG Reporting", "Bursa SR", "Net Zero Pathway". Publish to Teams.',
            'Demo the agent: The Group CSO is in a meeting with the Milieudefensie (Dutch environmental NGO) who is threatening to publish a report linking Zava Group\'s Perkebunan Lestari peatland to climate damage and supply chain connections to European FMCG brands. The NGO asks: "What specific peat depth measurements were taken at the 8,200ha area and what does your remediation plan specifically commit to?" The CSO quietly asks the ESG agent: "What do our RSPO audit records show about the peat depth data at Perkebunan Lestari and what are the specific commitments in our Corrective Action Plan?" Show how the agent provides instant, fact-based answers to NGO challenges.'
          ]
        }
      ]
    },
    {
      id: 'dept-operations',
      sectorId: 'department',
      subsector: '',
      name: 'Operations & COO Office',
      icon: '⚙️',
      color: '#37474F',
      accent: '#455A64',
      company: 'Zava Group Holdings — Group COO Office',
      tagline: 'Nilai plant OEE crisis, Cilegon enforcement notices, supply chain resilience, cross-division OpEx.',
      scenario: 'The Group COO Office oversees operational excellence across 6 factories, 12 plantations, 3 chemical plants, 10 hospitals, and 5 BPO delivery centres. Live crises: Nilai automotive plant OEE has declined from 76% to 62% in 18 months, Cilegon Chemicals has 3 BPOM enforcement notices, and the CPO feedstock shortage is impacting chemical plant utilisation. Group-wide OpEx reduction target: MYR 480M in FY2025.',
      files: [
        '12_Zava_Manufacturing_KPIs.xlsx',
        '15_Zava_BPO_Operations.xlsx'
      ],
      prompts: [
        {
          tool: '🤖 Copilot Chat (Basic)',
          license: 'Free — no M365 Copilot license needed',
          account: 'Sasha Ouellet — SashaO@ABSx62256373.OnMicrosoft.com',
          desc: '',
          prompts: [
            'I am the Group COO of an ASEAN conglomerate. Our Nilai automotive plant OEE has declined from 76% to 62% in 18 months. The primary cause is unplanned spindle motor failures on our 12-year-old CNC machines, but there are also quality issues (defect rate rising from 1.2% to 3.8%) and a maintenance backlog. Draft a 250-word brief on: (1) What OEE recovery actions can be implemented immediately at zero cost, (2) What the financial impact of 62% vs 76% OEE is at 850 units/day capacity with MYR 1,200 revenue per unit and 310 working days, (3) The business case threshold for replacing the spindle motors vs replacing the machines entirely.',
            'What is Total Productive Maintenance (TPM) and how is it used to sustainably improve OEE? What are the 8 TPM pillars and which ones would address our specific issues of unplanned breakdowns, quality defects, and slow changeovers?',
            'How should a group COO manage OpEx reduction when every division head claims their operations are already at minimum cost? What is the structured approach to identifying genuine OpEx reduction opportunities vs cost cuts that damage capability?'
          ]
        },
        {
          tool: '🔍 Researcher',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via Microsoft 365 Copilot Chat (copilot.microsoft.com or Teams) > click Agents > Researcher. Grounds answers in live web sources and your organisation data with full citations.',
          prompts: [
            'Research OEE benchmarks for automotive component manufacturing plants in ASEAN. What is a world-class OEE for precision stamping and CNC machining? What are the documented root causes of OEE decline in aging manufacturing plants and what are the proven remediation approaches? Cite industry sources like ARC Advisory, LNS Research, or Siemens.',
            'Research process safety management best practices for chemical plants in Indonesia regulated by BPOM. What are the BPOM enforcement procedures when an enforcement notice is issued? What are the typical timeline and requirements to lift a production suspension? Cite BPOM regulations or official Indonesian industrial safety sources.'
          ]
        },
        {
          tool: '📊 Analyst',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via Microsoft 365 Copilot Chat > click Agents > Analyst. Upload an Excel or CSV file. Analyst runs Python-style analysis, builds charts, and interprets results without you writing a single formula.',
          prompts: [
            'Upload 12_Zava_Manufacturing_KPIs.xlsx. Ask Analyst: (1) Plot the Nilai plant OEE decline from Jan 2023 to Dec 2024 on a time series chart. Overlay the dates of key events (first spindle failure, parts ordered, training scheduled) to show the correlation. (2) Calculate the revenue lost due to OEE decline vs the world-class OEE benchmark of 85% — show monthly and cumulative. (3) Decompose the OEE into Availability, Performance, and Quality components and show which is contributing most to the decline. Highlight the trend clearly.',
            'Upload 15_Zava_BPO_Operations.xlsx. Ask Analyst: (1) Calculate the total annual revenue at risk from the 3 BPO contracts expiring within 6 months. (2) For each expiring contract, score the renewal probability (High/Medium/Low) based on NPS score and SLA performance. (3) If all 3 are lost, calculate the impact on BPO Division revenue, headcount utilisation, and profitability. (4) Plot a revenue cliff chart showing the contracted revenue falling off in the next 12 months if no renewals are secured.'
          ]
        },
        {
          tool: '📊 Copilot in Excel',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open 12_Zava_Manufacturing_KPIs.xlsx. Ask Copilot: Add a column on Sheet 1 (Factory Dashboard) calculating the annual revenue impact of current OEE vs target OEE (85%) for each factory. Formula: (Target OEE% - Actual OEE%) × Installed Capacity/day × Working Days × Revenue per Unit. Show as a revenue opportunity column. Highlight factories where the gap represents more than MYR 20M annual revenue opportunity in red.',
            'Open 15_Zava_BPO_Operations.xlsx. Ask Copilot: Add a contract risk score on Sheet 1 (Client Dashboard) based on: NPS score < 45 = 2 points, SLA score < 92% = 2 points, contract expiry within 6 months = 3 points, renewal status "At Risk" = 3 points. Sum the scores. Score 6+ = High Risk (red), 3-5 = Medium Risk (amber), 0-2 = Low Risk (green). Calculate the total revenue at risk for High Risk contracts.',
            'Ask Copilot: Create an OpEx tracker on a new sheet. For each of the 11 divisions, show: (1) FY2024 OpEx (MYR M), (2) FY2025 OpEx Budget, (3) FY2025 YTD Actual, (4) Variance MYR M, (5) Variance %, (6) OpEx reduction target (MYR M), (7) Savings achieved to date, (8) % of target achieved. Sum group totals. Highlight divisions where savings are below 30% of target in red — these need COO intervention.'
          ]
        },
        {
          tool: '📝 Copilot in Word',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open 12_Zava_Manufacturing_KPIs.xlsx. Ask Copilot to draft a briefing document: "Nilai Plant OEE Crisis — Root Cause Analysis and Recovery Plan". Structure: (1) Executive Summary — OEE at 62%, financial impact, recovery timeline, (2) Root Cause Analysis — 5-Why analysis of spindle motor failures, (3) Immediate actions — 5 things that can start this week, (4) Short-term actions (30-90 days) — maintenance programme, spare parts, training, (5) Long-term investment — MYR 8.2M spindle motor replacement business case, (6) Recovery milestones — OEE targets at 30/60/90/180 days. 4 pages.',
            'Ask Copilot: Draft the formal response letter to BPOM regarding the 3 enforcement notices at Cilegon Specialty Chemicals. The letter should: reference each enforcement notice number and date, for each notice provide (1) root cause, (2) immediate corrective action taken, (3) preventive measure implemented, (4) evidence attached. Request a reinspection to lift the production suspension. Formal Indonesian regulatory correspondence format.',
            'Ask Copilot: Write the Group COO\'s quarterly Operations Review narrative for the Board. Structure: (1) Group OEE performance — 3 world class plants, 2 acceptable, 1 crisis (Nilai), (2) Quality performance — group defect rate trend, (3) Safety — TRIR vs benchmark, any critical incidents, (4) BPO contract risk — 3 contracts expiring, renewal status, (5) OpEx reduction — progress vs MYR 480M target, (6) Capex programme — 12 projects status, (7) Division-by-division operational highlights and concerns. 6 pages, Board report format.'
          ]
        },
        {
          tool: '🎯 Copilot in PowerPoint',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Ask Copilot in PowerPoint: Create a 12-slide Operations Review Board presentation. Include: (1) Group operational highlights, (2) Manufacturing OEE dashboard — 6 factories, (3) Nilai plant crisis — OEE trend and recovery plan, (4) Quality performance — defect rate trend, (5) Safety performance — TRIR, enforcement notices, (6) BPO contract renewal risk — 3 expiring contracts revenue at risk, (7) BPO headcount and delivery centre utilisation, (8) Chemicals — Cilegon enforcement notice status, (9) Plantation operations — CPO production vs target, (10) OpEx reduction — division by division vs target, (11) Capex programme — 12 projects traffic light, (12) Actions required from Board. Grey and navy operations colour scheme.',
            'Ask Copilot: Create a 3-slide Nilai Plant Recovery Plan for the Plant Manager town hall. Slide 1: The OEE crisis in plain numbers — what 62% vs 85% means for our revenue and jobs. Slide 2: The 7 recovery actions — 3 this week, 4 in 30 days. Slide 3: The 6-month OEE improvement targets. Straightforward, factory-worker-facing language.',
            'Ask Copilot: Create a 2-slide BPO Contract Retention Strategy for the EXCO. Slide 1: The 3 contracts at risk — USD 26.4M combined ARR, renewal probability and reasoning. Slide 2: The retention playbook — price, scope, relationship, and service improvement actions for each client.'
          ]
        },
        {
          tool: '📧 Copilot in Outlook',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Ask Copilot in Outlook: Draft the Group COO\'s urgent email to the Nilai Plant Manager and Group Manufacturing VP escalating the OEE crisis. The email should: state the financial impact (revenue loss vs 85% OEE benchmark: MYR 40M annualised), note the spindle motor replacement has been pending approval for 6 months, request a 5-day OEE recovery plan submission, and schedule a site visit for the following week. Firm but constructive tone.',
            'Ask Copilot: Draft the Group COO\'s email to the Zava BPO CEO regarding the 3 expiring BPO contracts. The email should: name the 3 contracts (Bank Mandiri, Sime Darby, Pan Pacific Hotels), note the combined USD 26.4M ARR at risk, request the current renewal negotiation status and the retention strategy for each, and set a deadline of 2 weeks for a detailed renewal plan.',
            'Ask Copilot: Draft the Board Operations Committee invitation for an emergency meeting to discuss the Nilai plant OEE crisis and Cilegon enforcement notices. The agenda should: cover the financial impact of both issues, the recovery plans, the capital investment required (MYR 8.2M Nilai + MYR 2.4M Cilegon remediation), and the Board decisions required. Professional committee meeting format.'
          ]
        },
        {
          tool: '🎙 Copilot in Teams',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Use your OWN existing recorded Teams meetings. Open a meeting recap in Teams > Recap tab. Copilot generates summaries, action items, and follow-up drafts grounded in the actual transcript.',
          prompts: [
            'Open an existing recorded Teams meeting recap from a manufacturing or operations review meeting. Ask Copilot: What operational KPIs were discussed? Identify the 3 most critical operational issues raised and the decisions made. Create a COO action log.',
            'Ask Copilot: Draft the COO\'s daily operations flash report for today. Structure: (1) Manufacturing — any unplanned downtime or quality alerts across 6 factories, (2) BPO — any SLA breaches or client escalations, (3) Chemicals — Cilegon status, any new BPOM developments, (4) Plantation — production vs plan, (5) Actions required by 5pm today.',
            'Ask Copilot: From this Operations Review meeting, what was the disagreement between the Manufacturing VP and the Plant Manager about the root cause of the Nilai OEE decline? Was it resolved and what was the agreed action?'
          ]
        },
        {
          tool: '📓 Copilot Notebook',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via copilot.microsoft.com > Notebook tab. Upload up to 5 files and set a system instruction. Best for synthesising insights across multiple documents simultaneously.',
          prompts: [
            'Upload 12_Zava_Manufacturing_KPIs.xlsx and 15_Zava_BPO_Operations.xlsx to Copilot Notebook. Set instruction: "You are the Group COO reviewing all operational risks." Ask: Based on all operational data, which 3 operational issues have the largest combined financial impact on the Group in the next 12 months? For each, what is the single most important action that the COO should personally drive in the next 30 days?',
            'Upload 12_Zava_Manufacturing_KPIs.xlsx. Ask: The Nilai plant has an 8.2M MYR spindle motor replacement project that has been 15% complete for 6 months. Also the plant has a 12.4M MYR MES system that has not started. Given the OEE crisis, should we sequence these projects differently? What would be the OEE impact of completing the spindle motor replacement first?'
          ]
        },
        {
          tool: '🤝 Cowork (Frontier)',
          license: 'M365 Copilot + Frontier Program',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Cowork is an autonomous agent that takes actions across Microsoft 365 on your behalf — sending emails, scheduling meetings, creating documents, posting in Teams, and scheduling recurring tasks. Access: m365.cloud.microsoft > left nav > Agents > Cowork. Requires Frontier program enrollment.',
          prompts: [
            'Do all of the following for the Nilai plant crisis: (1) Research lean manufacturing OEE improvement methodologies from the Toyota Production System and Siemens SCADA platforms. (2) Draft a 90-day Nilai Plant OEE Recovery Action Plan. (3) Calculate the financial impact of each 1% OEE improvement. (4) Email to the Group Manufacturing VP and Plant Manager for implementation. (5) Create a daily OEE recovery tracker in SharePoint. (6) Schedule weekly COO check-in on Nilai plant OEE until it reaches 72%.',
            'Do all of the following for BPO contract retention: (1) Research best practice BPO contract renewal negotiation strategies for contracts with NPS below 50. (2) For each of the 3 at-risk contracts (Bank Mandiri, Sime Darby, Pan Pacific), draft a tailored retention proposal addressing their specific SLA breaches and NPS issues. (3) Email each proposal to the respective BPO client relationship manager. (4) Schedule face-to-face retention meetings with each client within 3 weeks.'
          ]
        },
        {
          tool: '🤖 Word Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to a Word document. Open the .docx in Word for Web > Copilot pane > + New Agent > name it, write a description, set the document as knowledge source > Share. Colleagues chat with it in Teams or M365 Copilot.',
          prompts: [
            'Open 12_Zava_Manufacturing_KPIs.xlsx in Word for Web (or create a companion Word summary). Create an agent called "Zava Operations Intelligence Bot". Description: "Answers questions from Plant Managers, Division Operations heads, and the Group COO on OEE benchmarks, manufacturing best practices, BPO SLA standards, safety protocols, and Cilegon enforcement notice compliance requirements." Share with all 6 factory managers and BPO centre managers.',
            'Demo: A Plant Manager at the Shah Alam Consumer Goods factory asks "Our OEE dropped from 82.4% to 79.1% in the last 2 months. We\'ve identified that the main cause is scheduled changeover time on our bottle cap line increasing from 45 to 75 minutes. Under our Group TPM standards, what is the target changeover time for a consumer goods line of this type and what is the SMED methodology we should apply?" Show the agent providing a technically grounded, actionable answer.'
          ]
        },
        {
          tool: '🤖 PowerPoint Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to a PowerPoint presentation. Great for strategy decks or Board presentations many people need to reference. Same setup as Word Agent but using a .pptx file.',
          prompts: [
            'Create a PowerPoint from the Operations Review Board presentation. Create an agent called "Operations Review Q&A Bot". Share with Board Operations Committee.',
            'Demo: A Board member asks "The Cilegon enforcement notices have now been outstanding for 4 months. What is the total revenue and EBITDA impact of the 2 suspended product lines and when do we expect BPOM to lift the suspension?" Show the agent providing a financially quantified, timeline-grounded answer.'
          ]
        },
        {
          tool: '🤖 Excel Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to an Excel workbook. Colleagues ask data questions in plain English without opening Excel. Open .xlsx in Excel for Web > Copilot pane > + New Agent > set workbook as knowledge source > share.',
          prompts: [
            'Open the Manufacturing KPIs and BPO Operations workbooks in Excel for Web. Create an agent called "COO Operations Dashboard Q&A". Description: "Instant answers on OEE by factory, quality metrics, BPO SLA performance, contract renewal risk, OpEx vs target, and capex programme status for the Group COO." Share with COO leadership.',
            'Demo: Ask "Which factory has the highest OEE and which has the lowest — and what is the MYR revenue gap between their actual output and what they would produce at 85% OEE?" Then: "For the 3 BPO contracts expiring in the next 6 months, what is the total contracted USD value at risk?" Show the COO getting instant cross-division operational intelligence.'
          ]
        },
        {
          tool: '🏗 Agent Builder (Copilot Studio)',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Build a custom declarative agent in Copilot Studio — no coding required. Access: copilotstudio.microsoft.com > Create > New Agent. Add name, description, knowledge sources (SharePoint URLs or uploaded files), topics/actions. Publish to Teams in under 10 minutes.',
          prompts: [
            'Go to copilotstudio.microsoft.com > Create > New Agent. Name it "Zava Operations Intelligence Agent". Description: "Supports the Group COO, Plant Managers, and Division Operations heads with instant answers on OEE benchmarks, manufacturing standards, BPO contract risk, safety compliance, OpEx reduction targets, and capex programme status — enabling faster, data-driven operational decisions across 6 factories, 3 chemical plants, 12 estates, and 5 BPO delivery centres." Upload 12_Zava_Manufacturing_KPIs.xlsx and 15_Zava_BPO_Operations.xlsx. Add topics: "OEE Management", "Quality Control", "BPO Contract Risk", "Safety Compliance", "OpEx Reduction". Publish to Teams.',
            'Demo the agent: The Group COO receives a call from the Nilai Plant Manager at 11pm: "We\'ve just had 3 CNC machines go down simultaneously — a catastrophic spindle failure across the C, D, and E lines. This will stop all production for at least 5 days. We need 3 replacement spindles urgently — the procurement team says the standard lead time is 12 weeks." The COO asks the agent: "What is the financial impact per day of having 3 lines down at Nilai, what is our approved emergency procurement protocol for critical spare parts that bypasses the standard 12-week lead time, and do we have any risk buffer stock of spindle motors at any other Zava manufacturing facility?" Show how the agent enables an instant, data-informed crisis response.'
          ]
        }
      ]
    },
    {
      id: 'dept-board',
      sectorId: 'department',
      subsector: '',
      name: 'Board & Executive Office',
      icon: '🏛',
      color: '#1A237E',
      accent: '#283593',
      company: 'Zava Group Holdings — Group CEO & Board Secretariat',
      tagline: 'Q1 FY2025 Board pack, ZAVA FORWARD 2030 strategy briefing, dual listing compliance.',
      scenario: 'The Group CEO and Board Secretariat serve the 11-member Board of Directors of Zava Group Holdings Berhad (Bursa main market, IDX dual-listed). Priorities: Q1 FY2025 Board pack covering NPL breach, RSPO suspension, coal breach, and OEE crisis. Annual General Meeting preparation. ZAVA FORWARD 2030 strategy presentation. Corporate governance compliance for Bursa and IDX simultaneous disclosure obligations.',
      files: [
        '01_Zava_Group_Financial_Performance.xlsx',
        'Email_07_Emergency_Board_Meeting.docx'
      ],
      prompts: [
        {
          tool: '🤖 Copilot Chat (Basic)',
          license: 'Free — no M365 Copilot license needed',
          account: 'Sasha Ouellet — SashaO@ABSx62256373.OnMicrosoft.com',
          desc: '',
          prompts: [
            'I am the Company Secretary of a dual-listed ASEAN conglomerate (Bursa Malaysia and Indonesia Stock Exchange). We have 4 simultaneous material issues that must be disclosed at the upcoming Board meeting: (1) Zava Bank retail personal loans NPL at 21.7% — breaching the BNM 3.5% threshold, (2) Perkebunan Lestari RSPO certification suspended, (3) Coal trading position limit breach USD 22.4M vs USD 20M limit, (4) Nilai manufacturing plant OEE at 62% with MYR 40M annualised revenue impact. Draft a 200-word brief on the sequence in which these should be presented to the Board — which is the most material for Bursa disclosure and why?',
            'What is the Corporate Governance Code of Best Practices (MCCG) requirement for a Malaysian main board listed company regarding Board Risk Committee composition and meeting frequency? How does dual listing on IDX change the governance obligations?',
            'Explain what a Board succession planning framework looks like for a diversified conglomerate with an 11-member Board. What skills matrix should be used, what is the typical director tenure policy, and how is independence of NEDs assessed under MCCG 2021?'
          ]
        },
        {
          tool: '🔍 Researcher',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via Microsoft 365 Copilot Chat (copilot.microsoft.com or Teams) > click Agents > Researcher. Grounds answers in live web sources and your organisation data with full citations.',
          prompts: [
            'Research Bursa Malaysia\'s mandatory immediate announcement requirements under the Listing Requirements. When must a company make an immediate announcement vs a next business day announcement? What specifically must be disclosed when a subsidiary bank breaches a regulatory capital ratio or NPL threshold? Cite Bursa Listing Requirements or SC circulars.',
            'Research Malaysian corporate governance best practices for conglomerate holding company boards. What are the MCCG 2021 requirements for Board composition (executive vs non-executive, independent), Board committees (Audit, Risk, Remuneration, Nomination), and Board effectiveness evaluation? How are the top Malaysian conglomerates (Sime Darby, IHH, IOI) rated on governance by MSWG or Bursa? Cite MCCG 2021 or governance rating reports.'
          ]
        },
        {
          tool: '📊 Analyst',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via Microsoft 365 Copilot Chat > click Agents > Analyst. Upload an Excel or CSV file. Analyst runs Python-style analysis, builds charts, and interprets results without you writing a single formula.',
          prompts: [
            'Upload 01_Zava_Group_Financial_Performance.xlsx. Ask Analyst: (1) Create an EPS bridge from FY2023 to FY2024 showing the contribution of each division to the change in group EPS. (2) Plot the FY2022-FY2025F earnings trajectory and analyst consensus vs actual for the last 4 quarters. (3) Calculate the implied P/E ratio vs the group\'s 5-year historical average and vs sector peer (Sime Darby, IOI, IHH). (4) Identify which single division contributed most to the FY2024 vs FY2023 EBITDA improvement and which most to the decline. Present as Board-ready charts.',
            'Upload 01_Zava_Group_Financial_Performance.xlsx. Ask: Model the financial impact of 3 simultaneous downside scenarios for FY2025F: (A) Zava Bank NPL requires MYR 800M additional provision, (B) Perkebunan Lestari suspension continues for full year — CPO volume loss at MYR 3,920/MT, (C) Nilai plant continues at 62% OEE for full year vs 85% target. Calculate: (1) Impact on Group EBITDA, (2) Impact on Group PAT, (3) Impact on EPS, (4) Impact on Net Gearing. Then show combined scenario if all 3 occur simultaneously.'
          ]
        },
        {
          tool: '📊 Copilot in Excel',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open 01_Zava_Group_Financial_Performance.xlsx. Ask Copilot: Create a Board KPI Dashboard sheet. For each of 15 Group-level KPIs (Revenue, EBITDA margin, PATAMI, EPS, Net Gearing, ROAE, DPS, Zava Bank NPL, Group TRIR, Group RSPO compliance, OEE weighted average, BPO SLA weighted average, Employee engagement, Women in leadership, ESG rating), show: (1) FY2024 Actual, (2) FY2025 Target, (3) FY2025 YTD, (4) Status (On Track/At Risk/Off Track). Apply RAG formatting. Create the Board\'s single-page Group performance dashboard.',
            'Ask Copilot: Build a Board meeting tracker on a new sheet. For each of the last 4 Board meetings, show: (1) Meeting date, (2) Key resolutions passed, (3) Outstanding actions from previous meeting, (4) Status of each action, (5) Days since resolution and overdue actions. Highlight overdue Board actions in red.',
            'Ask Copilot: Build an investor relations dashboard. For each of our 15 top institutional shareholders (approximate): (1) Fund name, (2) Country, (3) Estimated % stake, (4) Last engagement date, (5) Current sentiment (Positive/Neutral/Negative), (6) Key concerns raised, (7) Next engagement planned. Highlight shareholders with negative sentiment and no engagement in the last 90 days in amber.'
          ]
        },
        {
          tool: '📝 Copilot in Word',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Open Email_07_Emergency_Board_Meeting.docx. Ask Copilot: Draft the Group CEO\'s Board Paper on the Q1 FY2025 simultaneous crises. Section 1: Group financial performance — revenue and EBITDA vs target. Section 2: Zava Bank NPL crisis — current status, BNM response, remediation plan, provision impact. Section 3: Perkebunan Lestari RSPO suspension — situation, commercial impact, remediation timeline. Section 4: Coal trading limit breach — what happened, risk control failure, immediate actions. Section 5: Nilai plant OEE crisis — financial impact, recovery plan, capex required. Section 6: Recommendations — 7 specific Board resolutions required. 12 pages, Board paper format with executive summary.',
            'Ask Copilot: Draft the Board resolution template for the 7 Board decisions required at the Q1 FY2025 emergency Board meeting: (1) Approve Zava Bank NPL remediation plan and MYR 800M provision, (2) Approve Perkebunan Lestari RSPO remediation budget MYR 140M, (3) Approve Coal Trading Risk Control enhancement — position limit reduction and risk committee oversight, (4) Approve Nilai plant spindle motor replacement MYR 8.2M, (5) Approve Group CEO authority to engage with BNM on NPL breach, (6) Approve RSPO CAP submission to RSPO certification body, (7) Approve EUDR compliance investment MYR 28M. Standard Malaysian Board resolution format.',
            'Ask Copilot: Draft the Chairman\'s opening address for the Board meeting. The address should: acknowledge the extraordinary challenges of the quarter honestly, frame the 4 crises as manageable and being actively remediated, express confidence in the management team, remind Directors of their fiduciary duties and the Bursa disclosure obligations, and set the tone for a constructive and decisive Board discussion. Statesman-like, measured tone.'
          ]
        },
        {
          tool: '🎯 Copilot in PowerPoint',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Ask Copilot in PowerPoint: Create the full Q1 FY2025 Board presentation (20 slides). Include: (1) Chairman\'s opening remarks context, (2) Q1 FY2025 Group financial highlights, (3) Division performance scorecard — 11 divisions, (4) Group financial KPI dashboard, (5) Zava Bank NPL crisis and remediation, (6) Perkebunan Lestari RSPO suspension, (7) Coal trading breach and risk control response, (8) Nilai plant OEE crisis and recovery, (9) Group ESG performance, (10) IT Digital transformation update, (11) M&A pipeline, (12) REIT IPO preparation, (13) ZAVA FORWARD 2030 progress, (14) FY2025 full-year guidance revision, (15) Capital allocation update, (16) Dividend consideration, (17) Investor relations update, (18) Regulatory engagement update, (19) Board decisions required, (20) Appendix — supporting data. Dark navy Board presentation.',
            'Ask Copilot: Create the ZAVA FORWARD 2030 strategy presentation for the Annual General Meeting (15 slides). Include: (1) Our journey — Zava Group from founding to today, (2) ASEAN opportunity, (3) Vision 2030 — Asia\'s most trusted diversified conglomerate, (4) 5 Strategic Pillars overview, (5) Pillar 1: Portfolio Optimisation — healthcare M&A, REIT IPO, (6) Pillar 2: Digital Transformation — Copilot, SAP, data lake, (7) Pillar 3: ESG Leadership — Net Zero, RSPO, EUDR, (8) Pillar 4: Talent Excellence — 87K employees, DEI, (9) Pillar 5: Capital Efficiency — 0.82x gearing to 0.65x, (10) Financial targets FY2027: Revenue MYR 52B, EBITDA 18%, (11) Dividend commitment — progressive policy, (12) Our people, (13) Our communities, (14) Our planet, (15) The Zava Promise. Polished investor-facing design.',
            'Ask Copilot: Create a 3-slide media briefing pack for the Q1 FY2025 results announcement. Slide 1: 3 key messages from the Group CEO. Slide 2: Q1 financial highlights in clean table format. Slide 3: FY2025 guidance — revenue range, EBITDA margin target, and DPS forecast. Journalist-accessible, no jargon.'
          ]
        },
        {
          tool: '📧 Copilot in Outlook',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: '',
          prompts: [
            'Ask Copilot in Outlook: Draft the Group CEO\'s email to all 11 Division CEOs and CFOs calling for urgent submissions for the emergency Board meeting. The email should: list the 4 simultaneous issues requiring Board presentation, request a 2-page "situation-action-status" brief from each affected division by Friday noon, confirm the emergency Board meeting date, and emphasise that the Board will ask tough questions — all answers must be evidenced and quantified. Authoritative, urgent tone.',
            'Ask Copilot: Draft the Company Secretary\'s Bursa Malaysia announcement for the Zava Bank NPL situation. Under Bursa Listing Requirements, the announcement must: describe the material information (Retail Personal Loans NPL at 21.7%, breach of BNM threshold), note the date of discovery, confirm BNM has been notified, state management actions (MYR 800M provision, remediation plan), and provide guidance on financial impact. Formal Bursa announcement format.',
            'Ask Copilot: Draft the Chairman\'s personal letter to the 4 largest institutional shareholders (EPF, KWAP, PNB, Permodalan MY) providing advance notification of the Q1 FY2025 challenges. The letter should: acknowledge the issues candidly, describe the remediation actions management has taken, express personal confidence in the strategy and management team, and invite a bilateral engagement before the public results announcement. Personal, statesman-like tone.'
          ]
        },
        {
          tool: '🎙 Copilot in Teams',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Use your OWN existing recorded Teams meetings. Open a meeting recap in Teams > Recap tab. Copilot generates summaries, action items, and follow-up drafts grounded in the actual transcript.',
          prompts: [
            'Open an existing recorded Teams meeting recap from a Board or EXCO meeting. Ask Copilot: What were the key strategic decisions made and what Board resolutions were passed? Identify all action items assigned to the CEO and their deadlines. Create a Board action tracker.',
            'Ask Copilot: Draft the Group CEO\'s weekly executive report for the Board. Structure: (1) Top 3 strategic priorities this week, (2) Financial performance flash — revenue and EBITDA vs plan, (3) Critical issues — Zava Bank NPL, RSPO, coal breach, Nilai — status update, (4) External environment — any regulatory or market developments, (5) Upcoming key decisions and decisions needed from Board.',
            'Ask Copilot: From this Board meeting recap, what was the Board\'s reaction to the NPL breach disclosure? Were there any dissenting views among Board members? What specific questions did the Board ask management that were not answered satisfactorily?'
          ]
        },
        {
          tool: '📓 Copilot Notebook',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Access via copilot.microsoft.com > Notebook tab. Upload up to 5 files and set a system instruction. Best for synthesising insights across multiple documents simultaneously.',
          prompts: [
            'Upload 01_Zava_Group_Financial_Performance.xlsx and Email_07_Emergency_Board_Meeting.docx to Copilot Notebook. Set instruction: "You are the Group CEO preparing for an emergency Board meeting." Ask: Based on the financial data and the email context, if I were the Board Chairman seeing these 4 simultaneous crises for the first time, what would be my 5 hardest questions for management? For each question, draft a 3-sentence answer that management should prepare.',
            'Upload 01_Zava_Group_Financial_Performance.xlsx. Ask: The Board must decide whether to revise down the FY2025 guidance that was given to Bursa at the Q4 FY2024 results. Original guidance: Revenue MYR 47.2B, EBITDA margin 16.8%. Based on the 4 simultaneous issues and their financial impact, should guidance be revised? If so, what is the defensible revised guidance range and what is the rationale that management should present?'
          ]
        },
        {
          tool: '🤝 Cowork (Frontier)',
          license: 'M365 Copilot + Frontier Program',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Cowork is an autonomous agent that takes actions across Microsoft 365 on your behalf — sending emails, scheduling meetings, creating documents, posting in Teams, and scheduling recurring tasks. Access: m365.cloud.microsoft > left nav > Agents > Cowork. Requires Frontier program enrollment.',
          prompts: [
            'Do all of the following to prepare for the emergency Board meeting: (1) Compile the Q1 FY2025 Board pack by pulling together: Group financial flash, Zava Bank NPL brief, RSPO situation brief, Coal trading breach brief, and Nilai OEE brief. (2) Draft the Chairman\'s briefing note on the 7 Board resolutions required. (3) Create the Board action log tracking all outstanding items from the previous 2 Board meetings. (4) Send all Board materials to Board members 5 days before the meeting via secure SharePoint link. (5) Schedule pre-meeting calls between the Chairman and each independent NED to brief them privately before the full Board meeting.',
            'Do all of the following for the Annual General Meeting: (1) Draft the full AGM Notice of Meeting including agenda, proxy form, and Explanatory Notes on resolutions. (2) Prepare the Integrated Annual Report summary (4-page highlights version). (3) Draft Q&A talking points for the Chairman and Group CEO covering the 20 most likely shareholder questions. (4) Prepare the ZAVA FORWARD 2030 strategy video script for the AGM screening. (5) Email the AGM Notice to the Company\'s share registrar for mailing to all registered shareholders.'
          ]
        },
        {
          tool: '🤖 Word Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to a Word document. Open the .docx in Word for Web > Copilot pane > + New Agent > name it, write a description, set the document as knowledge source > Share. Colleagues chat with it in Teams or M365 Copilot.',
          prompts: [
            'Open Email_07_Emergency_Board_Meeting.docx in Word for Web. Create an agent called "Zava Board & Governance Q&A Bot". Description: "Answers questions from Board Directors, the Chairman, Group CEO, and Company Secretary on Bursa Listing Requirements, MCCG 2021 governance obligations, Board resolution procedures, dual-listing disclosure requirements, and Board meeting protocols." Share with Board members and the Company Secretary.',
            'Demo: An Independent Non-Executive Director asks "A whistleblower email has just been forwarded to me by an employee alleging that a senior manager at Zava Trading has been inflating commodity trading profits to avoid a bonus malus. As an INED, what is my disclosure obligation under Bursa Listing Requirements, what is the proper escalation pathway under our Whistleblower Policy, and must I disclose this to the full Board at the next meeting or can I handle it privately through the Audit Committee?" Show the agent providing a governance-grounded, regulatory-precise answer.'
          ]
        },
        {
          tool: '🤖 PowerPoint Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to a PowerPoint presentation. Great for strategy decks or Board presentations many people need to reference. Same setup as Word Agent but using a .pptx file.',
          prompts: [
            'Create a PowerPoint from the ZAVA FORWARD 2030 AGM presentation. Create an agent called "ZAVA FORWARD 2030 Strategy Q&A". Share with Board members, EXCO, and investor relations team.',
            'Demo: An institutional shareholder analyst asks "In your ZAVA FORWARD 2030, you target EBITDA margin improvement from 16.1% to 18.0% by FY2027. But you currently have 4 simultaneous operational crises. Which of the 5 strategic pillars is most at risk and what is the contingency if EBITDA margin misses the 18% target by more than 1 percentage point?" Show the agent providing a strategy-grounded, quantified investor response.'
          ]
        },
        {
          tool: '🤖 Excel Agent',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Create a declarative agent scoped to an Excel workbook. Colleagues ask data questions in plain English without opening Excel. Open .xlsx in Excel for Web > Copilot pane > + New Agent > set workbook as knowledge source > share.',
          prompts: [
            'Open the Group Financial Performance workbook in Excel for Web. Create an agent called "Group Financial Intelligence Q&A". Description: "Instant answers on Group financial performance, division P&L, EPS trend, analyst consensus, net gearing, and FY2025 guidance for the Group CEO, CFO, and Board." Share with Board members and EXCO.',
            'Demo: Ask "What is our Q1 FY2025 EBITDA margin vs target and which division has the largest negative variance?" Then: "If the Zava Bank NPL requires an MYR 800M provision, what is the impact on Group PAT and EPS — and does it breach any of our debt covenants?" Show the Board getting instant, scenario-aware financial intelligence.'
          ]
        },
        {
          tool: '🏗 Agent Builder (Copilot Studio)',
          license: 'M365 Copilot',
          account: 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          desc: 'Build a custom declarative agent in Copilot Studio — no coding required. Access: copilotstudio.microsoft.com > Create > New Agent. Add name, description, knowledge sources (SharePoint URLs or uploaded files), topics/actions. Publish to Teams in under 10 minutes.',
          prompts: [
            'Go to copilotstudio.microsoft.com > Create > New Agent. Name it "Zava Board Intelligence Agent". Description: "Supports the Group CEO, Chairman, Board Directors, Company Secretary, and Investor Relations team with instant answers on Group financial performance, governance obligations, Bursa/IDX disclosure requirements, MCCG compliance, Board resolution procedures, and ZAVA FORWARD 2030 strategy — enabling faster, governance-consistent Board decision-making across the Zava Group conglomerate." Upload 01_Zava_Group_Financial_Performance.xlsx and Email_07_Emergency_Board_Meeting.docx. Add topics: "Group Financial Performance", "Bursa Disclosure", "Board Governance", "MCCG 2021", "Strategy". Publish to Teams for Board members.',
            'Demo the agent: The Group CEO receives a call from a Bloomberg journalist at 6am: "We have received a tip that Zava Group is planning a major rights issue to address the Zava Bank capital ratio decline. Is this true and do you have a comment?" The CEO asks the agent: "Under Bursa Listing Requirements, is a potential rights issue a price-sensitive immediate announcement trigger? Am I allowed to say No Comment, and if I confirm or deny, which statement puts us in a stronger Bursa disclosure position?" Show how the agent enables an instant, legally grounded media handling decision at 6am.'
          ]
        }
      ]
    }
  ]
};