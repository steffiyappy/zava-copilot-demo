// IDMY Copilot Industry Hub — Data File
// Update prompts and whats-new monthly

window.HUB_DATA = {

  whatsNew: [
    { date: "May 2026", title: "Copilot in Excel — Python integration GA", desc: "Run Python analytics directly in Excel with Copilot — no coding required. Great for financial modelling demos.", tag: "Excel", color: "#217346" },
    { date: "May 2026", title: "Copilot Notebooks — multi-file reasoning", desc: "Copilot Notebook can now reason across multiple uploaded files simultaneously. Perfect for multi-document analysis demos.", tag: "Notebook", color: "#0078D4" },
    { date: "Apr 2026", title: "Copilot in Teams — meeting coach", desc: "Real-time speaking suggestions and post-meeting coaching report. Demo in any Teams meeting scenario.", tag: "Teams", color: "#6264A7" },
    { date: "Apr 2026", title: "Copilot Pages — shared canvas GA", desc: "Collaborative AI-generated pages — works like a shared Notepad powered by Copilot. Great for working-session demos.", tag: "Pages", color: "#FF6B35" },
    { date: "Mar 2026", title: "Copilot in Outlook — Priority Inbox AI", desc: "Copilot scores and surfaces high-priority emails automatically. Demo the 'start your day' scenario.", tag: "Outlook", color: "#0078D4" }
  ],

  industries: [
    {
      id: "general",
      name: "General (Any Role)",
      icon: "⭐",
      color: "#1F2D55",
      accent: "#0078D4",
      company: "Zava Group Holdings Berhad",
      tagline: "Cross-role everyday scenarios | Suitable for any industry | Start here for new audiences",
      scenario: "It's Monday morning at Zava Group. Sasha Ouellet (Group CSO) has 47 unread emails, a Risk Committee meeting in 2 hours, and a Board pre-read due by 3pm. MOD Administrator (Group IT Director) is rolling out M365 Copilot to 1,200 KL office staff and needs to show the full breadth of what Copilot can do — from email triage to multi-document analysis. This is your 'start here' demo track — every tool, every persona, real files from Zava's operations.",
      files: [
        "Email_07_Emergency_Board_Meeting.docx",
        "Email_09_Risk_Committee_Prep.docx",
        "01_Zava_Group_Financial_Performance.xlsx",
        "03_Zava_Group_Strategy_Framework.docx",
        "02_Zava_Group_Policy_Handbook.docx"
      ],
      prompts: [
        { tool: "🤖 Copilot Chat (Basic — no M365 license)", license: "Free / Basic", account: "Basic (Sasha — SashaO@ABSx62256373.OnMicrosoft.com)", prompts: [
          { title: "Start the week with a quick briefing", prompt: "I'm the Chief Strategy Officer of a diversified ASEAN conglomerate. Give me a 5-bullet briefing on the top macro risks for a Malaysian conglomerate with palm oil, chemicals, banking and BPO businesses — as of today." },
          { title: "Explain a regulatory term", prompt: "Explain what BNM's Section 47 Direction means for a licensed Malaysian commercial bank. What are the obligations of the bank once a Direction is issued, and what happens if it is not remediated within the specified timeframe?" },
          { title: "Draft a message from scratch", prompt: "Draft a short WhatsApp-style message to my COO, Daichi Maruyama, reminding him that the Risk Committee prep pack must be sent to all members by noon today. Keep it professional but direct. Under 3 sentences." },
          { title: "Research before a meeting", prompt: "I have a meeting with PETRONAS Chemicals in 30 minutes. Give me a 1-page briefing on PETRONAS Chemicals Group — key business divisions, recent financials, strategic priorities, and any recent news I should reference in conversation." }
        ]},
        { tool: "📧 Copilot in Outlook", license: "M365 Copilot", account: "Premium (MOD Admin — admin@ABSx62256373.onmicrosoft.com)", prompts: [
          { title: "Triage a long email thread", prompt: "Open Email_07_Emergency_Board_Meeting.docx and copy the email thread into Outlook. Then ask Copilot: 'Summarise this email thread. List: (1) what triggered the emergency meeting, (2) who has been informed, (3) all outstanding actions with owner names, and (4) the most recent update.'", fileRef: "Email_07_Emergency_Board_Meeting.docx" },
          { title: "Draft a reply with the right tone", prompt: "Using the Risk Committee prep email thread (Email_09), draft a reply from Hadar Caspit (Group CFO) to the Risk Committee members confirming that the updated NPL briefing pack has been reviewed and approved for circulation. Tone: formal but reassuring.", fileRef: "Email_09_Risk_Committee_Prep.docx" },
          { title: "Coaching: improve my draft", prompt: "I wrote this reply to a regulator: 'Hi, thanks for your email. We will try our best to fix this issue and get back to you.' Use Copilot Coaching to improve the tone, formality, and clarity. Keep it under 80 words." },
          { title: "Prepare for a meeting", prompt: "I have a 1:1 with Sonia Ramirez (Group CHRO) in 1 hour to review the Bengaluru BPO attrition update. Use Copilot to prepare me: pull relevant emails from the last 2 weeks, summarise the current situation, and suggest 3 questions I should ask." }
        ]},
        { tool: "📝 Copilot in Word", license: "M365 Copilot", account: "Premium (MOD Admin)", prompts: [
          { title: "Summarise a long document into a Board pre-read", prompt: "Open 03_Zava_Group_Strategy_Framework.docx. Ask Copilot: 'Summarise the entire document into a 1-page Board pre-read. Use the format: (1) Strategic Context — 2 sentences, (2) 5 Key Priorities — bullet points, (3) Top 3 Risks — bullet points, (4) What the Board needs to decide — 2 sentences.'", fileRef: "03_Zava_Group_Strategy_Framework.docx" },
          { title: "Rewrite for a different audience", prompt: "Open 02_Zava_Group_Policy_Handbook.docx and navigate to the Data Privacy & Cybersecurity Policy section. Ask Copilot: 'Rewrite this section in plain, conversational English for a non-technical employee. Avoid jargon. Aim for a reading age of 14.'", fileRef: "02_Zava_Group_Policy_Handbook.docx" },
          { title: "Draft a new section", prompt: "In a new Word document, ask Copilot: 'Draft a 400-word AI & Microsoft Copilot Usage Policy for Zava Group Holdings Berhad. Cover: permitted uses, data classification rules (do not paste confidential data into public AI), responsibility for AI outputs, and compliance with PDPA Malaysia.'" },
          { title: "Create meeting minutes from notes", prompt: "Type the following rough notes into Word, then ask Copilot to format them as formal meeting minutes:\n'Risk Comm 5 May 2025. Present: Hadar, Omar, Will, Sonia, MOD Admin. NPL at 21.7% personal financing — Hadar presented. Omar says risk limit breach on coal trading resolved. Will — BNM response letter going out Friday. Next meeting 2 June.'" }
        ]},
        { tool: "📊 Copilot in Excel", license: "M365 Copilot", account: "Premium (MOD Admin)", prompts: [
          { title: "Instantly understand a financial dashboard", prompt: "Open 01_Zava_Group_Financial_Performance.xlsx. Ask Copilot: 'Give me a plain-English summary of this workbook. Which division has the highest revenue? Which has the worst EBITDA margin trend? Are there any numbers I should be worried about?'", fileRef: "01_Zava_Group_Financial_Performance.xlsx" },
          { title: "Add a formula with no typing", prompt: "In the Group P&L sheet, ask Copilot: 'Add a column showing EBITDA margin % for each division in each year. Highlight in red any cell where margin drops more than 2 percentage points year-on-year.'" },
          { title: "Create a chart instantly", prompt: "Ask Copilot: 'Create a clustered bar chart comparing FY2023 vs FY2024 EBITDA by division. Use Zava's navy blue (#1F2D55) for FY2024 bars and light grey for FY2023. Add a title: Zava Group — Division EBITDA Comparison FY2023 vs FY2024.'" },
          { title: "Ask a question in natural language", prompt: "Ask Copilot: 'Which 3 divisions had the highest revenue growth from FY2023 to FY2024? Express growth as both absolute MYR change and percentage. Present as a simple table.'" }
        ]},
        { tool: "🎙 Copilot in Teams (Meeting Recap)", license: "M365 Copilot", account: "Premium (MOD Admin)", prompts: [
          { title: "Recap a meeting you missed", prompt: "After a recorded Teams meeting, open the meeting recap and ask: 'I missed this meeting. Give me a 5-sentence summary: what was discussed, what decisions were made, and what actions were assigned to me or my team.'" },
          { title: "Extract all action items", prompt: "From the Risk Committee meeting recap, ask Copilot: 'List every action item from this meeting. For each: who is the owner, what is the deadline, and what is the context (why it was assigned)?'" },
          { title: "Turn recap into Copilot Pages", prompt: "After the meeting recap is generated, click 'Open in Copilot Pages'. Then ask: 'Reorganise this into a structured action plan grouped by department: Finance, Risk, Legal, HR. Add a status column (Not Started / In Progress / Done) to each action.'" }
        ]},
        { tool: "📓 Copilot Notebook", license: "M365 Copilot", account: "Premium (MOD Admin)", prompts: [
          { title: "Multi-document synthesis — Board prep", prompt: "Upload: 03_Zava_Group_Strategy_Framework.docx + 01_Zava_Group_Financial_Performance.xlsx + Email_09_Risk_Committee_Prep.docx.\n\nIn the Instructions box type: 'You are preparing the Group CEO (Dato' Sri Irfan Zavaree) for tomorrow's Board meeting. Using all 3 files, write a 1-page CEO Talking Points brief covering: (1) the FY2024 financial story, (2) the top 3 strategic updates, (3) the 2 risk items requiring Board attention.'", fileRef: "03_Zava_Group_Strategy_Framework.docx, 01_Zava_Group_Financial_Performance.xlsx, Email_09_Risk_Committee_Prep.docx" },
          { title: "Policy gap analysis", prompt: "Upload: 02_Zava_Group_Policy_Handbook.docx\n\nIn the Instructions box type: 'Review this policy handbook and identify any gaps relative to the following 5 areas: (1) AI & Copilot usage, (2) Remote work security, (3) Third-party vendor access to systems, (4) Whistleblower anonymity, (5) Cross-border data transfers. For each area: state whether there is a policy, summarise it in 1 sentence, and flag if it needs updating.'", fileRef: "02_Zava_Group_Policy_Handbook.docx" }
        ]}
      ]
    },
    {
      id: "banking",
      name: "Banking & Financial Services",
      icon: "🏦",
      color: "#0D47A1",
      accent: "#1976D2",
      company: "Meridian Bank Berhad",
      tagline: "Mid-tier Malaysian commercial bank | MYR 68.4B assets | NPL recovery underway",
      scenario: "Meridian Bank is navigating a Personal Financing NPL crisis (14.2% vs BNM threshold 3.5%) while executing a digital banking transformation. The CFO needs to prepare for a BNM bilateral meeting, the Risk team is rebuilding credit scoring models, and the digital team is launching a new mobile app.",
      files: ["BNK_01_Meridian_Bank.xlsx", "BNK_02_Meridian_Bank_Strategy.docx"],
      prompts: [
        { tool: "📊 Copilot in Excel", license: "M365", account: "Premium", prompts: [
          { title: "NPL trend analysis", prompt: "Analyse the Personal Financing NPL trend in the Loan Portfolio sheet. Identify which quarters showed the sharpest deterioration and calculate the rate of change. Summarise in 3 bullet points." },
          { title: "Provision gap modelling", prompt: "In the Financial Performance sheet, calculate the additional provision required to reach 80% provision coverage on the Personal Financing portfolio. Show the impact on pre-tax profit." },
          { title: "Digital KPI benchmarking", prompt: "Compare our Digital Banking KPIs against the Industry Benchmark column. Highlight the top 3 gaps and suggest which gaps, if closed, would have the highest revenue impact." },
          { title: "Capital ratio forecast", prompt: "Model three scenarios for CET1 ratio recovery: (a) rights issue only, (b) asset recycling only, (c) combined. Plot the projected CET1 ratio by quarter for the next 4 quarters." }
        ]},
        { tool: "📝 Copilot in Word", license: "M365", account: "Premium", prompts: [
          { title: "BNM briefing memo", prompt: "Using the strategy document, draft a 1-page briefing memo for the CEO ahead of the BNM bilateral meeting. Include: current NPL position, remediation actions taken, timeline to compliance, and key messages to convey to BNM." },
          { title: "Credit quality recovery plan", prompt: "Based on the Credit Quality Recovery section of the strategy document, draft a structured 2-page recovery plan with SMART objectives, KPIs, and a 6-month milestone timeline." },
          { title: "Digital transformation summary", prompt: "Summarise the Digital Banking Transformation section into a 1-page executive summary suitable for a Board pre-read. Highlight investment, expected outcomes, and risk." }
        ]},
        { tool: "🤖 Copilot Chat", license: "Basic (no M365 license)", account: "Basic", prompts: [
          { title: "Explain BNM NPL framework", prompt: "Explain what BNM's Prudential Credit Oversight Standards (PCOS) framework means for a bank that has breached NPL thresholds. What are the typical supervisory actions BNM can take?" },
          { title: "Research digital banking trends", prompt: "What are the top digital banking trends in Malaysia and Southeast Asia for 2025-2026? Which features are driving the highest customer adoption?" },
          { title: "Draft investor FAQ", prompt: "Draft a Q&A document for investor relations covering 5 likely questions about a bank's rising NPL ratio. Keep answers factual, balanced, and under 80 words each." }
        ]},
        { tool: "🔍 Copilot in Outlook", license: "M365", account: "Premium", prompts: [
          { title: "Summarise regulatory thread", prompt: "Summarise this email thread and list all action items with owners and deadlines." },
          { title: "Draft BNM response letter", prompt: "Draft a formal response to BNM's supervisory enquiry. Acknowledge their concerns, provide an update on the Debt Restructuring Programme, and confirm our next reporting milestone." }
        ]},
        { tool: "📓 Copilot Notebook", license: "M365", account: "Premium", prompts: [
          { title: "Multi-file credit analysis", prompt: "I've uploaded the Loan Portfolio data and the Strategy document. Synthesise the key credit quality issues, the recovery actions planned, and the financial impact. Present as a structured briefing note I can share with the Board." }
        ]}
      ]
    },
    {
      id: "healthcare",
      name: "Healthcare & Life Sciences",
      icon: "🏥",
      color: "#1B5E20",
      accent: "#2E7D32",
      company: "Apex Health Group Berhad",
      tagline: "Malaysia's 3rd largest private hospital network | 12 hospitals | MYR 2.84B revenue",
      scenario: "Apex Health Group is dealing with a nursing shortage (18.4% attrition), a 6-week waiting list at its Cancer Centre, and a medical tourism recovery programme. The CHRO needs to build the retention case for the Board, while the COO prepares for JCI accreditation at Apex Penang.",
      files: ["HC_01_Apex_Health_Group.xlsx", "HC_02_Apex_Health_Strategy.docx"],
      prompts: [
        { tool: "📊 Copilot in Excel", license: "M365", account: "Premium", prompts: [
          { title: "Revenue by speciality analysis", prompt: "In the Revenue by Service sheet, calculate which 3 specialities have the highest revenue per bed and the highest YoY growth. What does this suggest about where to invest in new capacity?" },
          { title: "Hospital KPI dashboard summary", prompt: "Review the Hospital KPIs sheet. Flag any KPI that is below target by more than 10%. For each flagged KPI, suggest one specific operational action." },
          { title: "Nurse attrition cost model", prompt: "Using the HR data in the Clinical Quality sheet, calculate the total annual cost of 18.4% nurse attrition assuming 4,200 nurses total and MYR 48,000 replacement cost per nurse. What is the break-even point for a salary increase?" }
        ]},
        { tool: "📝 Copilot in Word", license: "M365", account: "Premium", prompts: [
          { title: "Board retention proposal", prompt: "Based on the nursing shortage section of the strategy document, draft a 2-page Board proposal for the Nurse Career Ladder v2.0 programme. Include: problem statement, proposed solution, budget, ROI, and timeline." },
          { title: "JCI accreditation checklist", prompt: "Summarise the key requirements for JCI accreditation from the strategy document and create a structured checklist with status (completed/in-progress/not started) for Apex Penang's Q3 2025 application." },
          { title: "Medical tourism recovery plan", prompt: "Draft a 1-page action plan to recover medical tourism revenue to pre-pandemic levels (MYR 532M). Focus on the Indonesian patient segment and the Prudential Indonesia MOU." }
        ]},
        { tool: "🤖 Copilot Chat", license: "Basic", account: "Basic", prompts: [
          { title: "JCI accreditation research", prompt: "What are the main requirements for JCI (Joint Commission International) hospital accreditation? How long does the process typically take and what are common gaps for Malaysian private hospitals?" },
          { title: "Nurse retention benchmarks", prompt: "What are global best practices for reducing nurse attrition in private hospitals? What salary and non-monetary factors have the biggest impact on retention?" }
        ]},
        { tool: "📓 Copilot Notebook", license: "M365", account: "Premium", prompts: [
          { title: "Oncology capacity brief", prompt: "I've uploaded the hospital KPI data and strategy document. Analyse the oncology capacity constraint — 6-week waiting list, 94% LINAC utilisation — and prepare a decision brief with 3 options (investment required, timeline, revenue impact for each)." }
        ]}
      ]
    },
    {
      id: "og",
      name: "Oil, Gas & Energy",
      icon: "⛽",
      color: "#E65100",
      accent: "#F57C00",
      company: "Nusantara Energy Berhad",
      tagline: "Malaysian integrated O&G company | 22,400 workforce | Upstream + LNG + Refining",
      scenario: "Nusantara Energy had a Tier 1 Process Safety Event at Miri Gas Compression and two offshore spills. The HSE Director needs to prepare the annual HSE report for the Board, while the Environment team is working on GHG reduction targets aligned to Malaysia's Net Zero 2050 pathway.",
      files: ["OG_01_Nusantara_Energy.xlsx", "OG_02_Nusantara_HSE_Report.docx"],
      prompts: [
        { tool: "📊 Copilot in Excel", license: "M365", account: "Premium", prompts: [
          { title: "Safety KPI variance analysis", prompt: "Compare actual vs target for all safety KPIs in the data. Which assets are exceeding targets and which are at-risk? Produce a RAG (Red/Amber/Green) summary table." },
          { title: "GHG reduction trajectory", prompt: "Plot the GHG Scope 1+2 reduction trajectory from FY2022 to FY2030 target. Calculate the annual reduction rate required. Is the current trajectory sufficient to meet the 2030 goal?" },
          { title: "Incident cost analysis", prompt: "Estimate the total cost of the FY2024 incidents: Tier 1 PSE at Miri (downtime, investigation, remediation), two spills (cleanup, regulatory penalties). Use industry benchmark costs where exact data is not available." }
        ]},
        { tool: "📝 Copilot in Word", license: "M365", account: "Premium", prompts: [
          { title: "Board HSE report", prompt: "Using the HSE annual report document, draft a 2-page Board summary. Include: FY2024 headline performance vs targets, the Miri PSE root cause and closure status, and the 3 priority actions for FY2025." },
          { title: "CAPA closure letter", prompt: "Draft a formal CAPA (Corrective Action and Preventive Action) closure letter to PETRONAS HSE Division confirming all actions from the Miri Tier 1 PSE are complete. Include each action, completion date, and verification method." },
          { title: "Net Zero commitment statement", prompt: "Draft a 1-page Net Zero commitment statement for Nusantara Energy's annual sustainability report. Reference the GHG reduction milestones and the methane intensity target." }
        ]},
        { tool: "🤖 Copilot Chat", license: "Basic", account: "Basic", prompts: [
          { title: "PSM standards research", prompt: "Explain the OSHA Process Safety Management (PSM) standard and how it applies to gas compression facilities. What are the 14 PSM elements most relevant to the Miri incident?" },
          { title: "EUDR and O&G", prompt: "Does the EU Deforestation Regulation (EUDR) apply to upstream oil and gas companies operating in Indonesia? What due diligence requirements might apply?" }
        ]},
        { tool: "📓 Copilot Notebook", license: "M365", account: "Premium", prompts: [
          { title: "HSE performance synthesis", prompt: "I've uploaded the O&G KPI data and the HSE annual report. Synthesise the full HSE performance picture for FY2024 — what went well, what went wrong, and what the top 3 priorities should be for FY2025. Format as a CEO briefing note." }
        ]}
      ]
    },
    {
      id: "telco",
      name: "Telecommunications",
      icon: "📡",
      color: "#4A148C",
      accent: "#7B1FA2",
      company: "ClearWave Communications Berhad",
      tagline: "Malaysia's 2nd largest telco | 14.8M subscribers | MYR 8.4B revenue",
      scenario: "ClearWave is under MCMC penalty for network outages exceeding Class A licence limits, while also trying to monetise 5G and grow enterprise B2B revenue. The CTO needs to prepare a network quality recovery plan, and the CMO is designing the Nexus Home convergence bundle.",
      files: ["TC_01_ClearWave_Communications.xlsx", "TC_02_ClearWave_Strategy.docx"],
      prompts: [
        { tool: "📊 Copilot in Excel", license: "M365", account: "Premium", prompts: [
          { title: "5G monetisation gap analysis", prompt: "In the subscriber data, calculate the revenue gap between actual 5G plan adoption (12.4%) and the 20% target. What incremental revenue would be generated if we close this gap? Show the model." },
          { title: "Enterprise segment growth analysis", prompt: "Analyse enterprise revenue by segment. Which segment has the highest CAGR and which has the highest revenue per account? Recommend where to focus the sales team's effort in H2 FY2025." },
          { title: "Network quality penalty tracker", prompt: "Create a compliance tracker showing current outage minutes vs MCMC Class A licence limit of 120 minutes. Project the end-of-year position at the current run rate. Calculate the penalty exposure." }
        ]},
        { tool: "📝 Copilot in Word", license: "M365", account: "Premium", prompts: [
          { title: "MCMC compliance response", prompt: "Based on the strategy document's network quality section, draft a formal response to MCMC's penalty notice. Acknowledge the breach, explain root cause, and present a concrete 90-day remediation plan with milestones." },
          { title: "Nexus Home go-to-market brief", prompt: "Draft a 2-page go-to-market brief for the Nexus Home convergence bundle launch. Include: target customer segment, bundle components, pricing rationale, channel strategy, and 90-day launch KPIs." },
          { title: "5G enterprise proposal", prompt: "Draft a 1-page private 5G network proposal template for a manufacturing client. Include: use cases (predictive maintenance, quality vision AI, AGV), coverage design, SLA commitments, and indicative investment range." }
        ]},
        { tool: "🤖 Copilot Chat", license: "Basic", account: "Basic", prompts: [
          { title: "5G use case research", prompt: "What are the top 5G enterprise use cases generating the most revenue for telcos in Southeast Asia? Which industries are adopting private 5G fastest?" },
          { title: "Convergence bundle benchmarks", prompt: "How are leading telcos in Asia Pacific structuring their fixed-mobile convergence (FMC) bundles? What ARPU uplift are they seeing compared to standalone products?" }
        ]},
        { tool: "🎯 Copilot in PowerPoint", license: "M365", account: "Premium", prompts: [
          { title: "5G business case deck", prompt: "Create a 6-slide business case presentation for investing MYR 84M in 5G network quality improvement. Include: current state, target state, investment breakdown, ROI analysis, risk mitigation, and recommendation." },
          { title: "Enterprise sales pitch", prompt: "Create a 5-slide private 5G pitch deck for a manufacturing client. Use a compelling narrative: 'Your factory of the future starts with 5G connectivity.'" }
        ]}
      ]
    },
    {
      id: "insurance",
      name: "Insurance & Takaful",
      icon: "🛡",
      color: "#1A237E",
      accent: "#283593",
      company: "Pacific Shield Insurance Berhad",
      tagline: "Malaysia's 3rd largest general insurer | MYR 3.84B GWP | Motor + Medical focus",
      scenario: "Pacific Shield's motor portfolio has a combined ratio of 108% — losing money for the 3rd consecutive year. The Head of Claims is launching an AI fraud detection programme, while the Chief Actuary is preparing a pricing strategy for BNM's motor detariffication framework.",
      files: ["INS_01_Pacific_Shield_Insurance.xlsx", "INS_02_Pacific_Shield_Strategy.docx"],
      prompts: [
        { tool: "📊 Copilot in Excel", license: "M365", account: "Premium", prompts: [
          { title: "Combined ratio drill-down", prompt: "Calculate the combined ratio for each line of business using the premium and claims data. Which lines are profitable and which are loss-making? What is the weighted average combined ratio for the overall portfolio?" },
          { title: "Claims inflation modelling", prompt: "In the claims data, calculate the year-on-year claims inflation rate for motor and medical lines. Project the combined ratio for FY2026 if claims inflation continues at the current rate with no pricing action." },
          { title: "Fraud detection priority scoring", prompt: "Using the claims data, create a prioritisation matrix for fraud investigation based on: claim amount, claim type, days to report, and workshop used. Flag the top 20% of claims for manual review." }
        ]},
        { tool: "📝 Copilot in Word", license: "M365", account: "Premium", prompts: [
          { title: "Motor detariffication strategy", prompt: "Based on the strategy document, draft a 2-page submission to BNM outlining Pacific Shield's motor pricing strategy under the phased detariffication framework. Include risk segmentation approach, UBI pilot results, and target combined ratio timeline." },
          { title: "AI fraud detection business case", prompt: "Draft a business case for the AI fraud detection programme (Project SWIFT CLAIM). Include: current fraud rate vs industry, proposed AI model approach, investment required, expected savings, and implementation timeline." },
          { title: "Medical inflation action plan", prompt: "Draft a structured action plan to address medical claims inflation. Cover the 4 interventions mentioned in the strategy: fee schedule, step therapy, pre-authorisation AI, and copay structures." }
        ]},
        { tool: "🤖 Copilot Chat", license: "Basic", account: "Basic", prompts: [
          { title: "Detariffication explained", prompt: "Explain what motor insurance detariffication means in the Malaysian context. What opportunities and risks does it create for insurers?" },
          { title: "UBI insurance research", prompt: "How does usage-based insurance (UBI) work? What telematics data is typically collected and how is it used to price motor insurance risk?" }
        ]},
        { tool: "📓 Copilot Notebook", license: "M365", account: "Premium", prompts: [
          { title: "Motor portfolio turnaround brief", prompt: "I've uploaded the insurance KPI data and the strategy document. Prepare a comprehensive turnaround brief for the motor portfolio: root causes of the 108% combined ratio, all planned interventions, projected combined ratio by year end if all interventions succeed, and the single biggest risk to the plan." }
        ]}
      ]
    },
    {
      id: "retail",
      name: "Retail & Consumer",
      icon: "🛒",
      color: "#B71C1C",
      accent: "#C62828",
      company: "BrightMart Group Berhad",
      tagline: "Malaysia's 2nd largest grocery chain | 284 stores | 8.2M loyalty members",
      scenario: "BrightMart's average basket size has fallen 11.9% since FY2022 as consumers downtrade. The CMO is launching TikTok Shop live commerce and the CEO wants a private label acceleration strategy to hit 22% penetration. The Ops team is designing the zero-checkout BrightMart Go format.",
      files: ["RT_01_BrightMart_Group.xlsx", "RT_02_BrightMart_Strategy.docx"],
      prompts: [
        { tool: "📊 Copilot in Excel", license: "M365", account: "Premium", prompts: [
          { title: "Store format profitability", prompt: "Compare revenue per square foot and YoY growth across all store formats (Hypermarket, Supermarket, Express, Go). Which format has the best economics? What does this suggest for the capital allocation strategy?" },
          { title: "Private label penetration gap", prompt: "Model the revenue and margin impact of increasing private label penetration from 14.8% to 22% by FY2027. Assume private label GM is 28.4% vs branded 18.4%. What is the EBITDA uplift?" },
          { title: "E-commerce basket analysis", prompt: "Compare average order value (AOV) across GrabMart, GoFood, own darkstores, and TikTok Live. Calculate gross profit per order for each channel after delivery cost. Which channel is most profitable?" }
        ]},
        { tool: "📝 Copilot in Word", license: "M365", account: "Premium", prompts: [
          { title: "BrightMart Go concept paper", prompt: "Draft a 2-page concept paper for the BrightMart Go zero-checkout format. Include: consumer insight, technology requirement (RFID, computer vision), unit economics, rollout plan from 2 to 40 stores, and risk assessment." },
          { title: "Private label strategy memo", prompt: "Draft a memo to the Board recommending the private label acceleration strategy. Make the case with data: basket size trends, margin uplift, competitor benchmarks, and 3-year revenue impact." },
          { title: "TikTok live commerce playbook", prompt: "Based on the pilot results (14 sessions, MYR 1.84M GMV), draft a live commerce playbook for scaling TikTok Shop to 3x/week. Include: host selection, product mix, promotional mechanics, and success metrics." }
        ]},
        { tool: "🤖 Copilot Chat", license: "Basic", account: "Basic", prompts: [
          { title: "Downtrade research", prompt: "What strategies are leading FMCG retailers using globally to defend against consumer downtrade? Which tactics have worked best in Southeast Asian markets?" },
          { title: "Quick commerce economics", prompt: "What is the typical unit economics model for quick commerce grocery delivery? What basket size is needed to break even on a 60-minute delivery model?" }
        ]},
        { tool: "🎯 Copilot in PowerPoint", license: "M365", account: "Premium", prompts: [
          { title: "Investor day deck", prompt: "Create a 7-slide investor day presentation for BrightMart. Narrative: 'From Big Box to Omnichannel Leader.' Cover: market context, business model evolution, digital acceleration, private label strategy, financials, and outlook." }
        ]}
      ]
    },
    {
      id: "glc",
      name: "Government & GLC",
      icon: "🏛",
      color: "#004D40",
      accent: "#00695C",
      company: "Danamas Capital Berhad",
      tagline: "Malaysian GLIC | MYR 284B portfolio | 9 portfolio companies | MOF-owned",
      scenario: "Danamas Capital's National Digital Infrastructure Fund has only 35% disbursement rate with a 84% coverage target due by Dec 2025. The Investment team is evaluating a port privatisation (MYR 4.8B). The portfolio oversight team is preparing for Parliamentary Accounts Committee (PAC) scrutiny.",
      files: ["GLC_01_Danamas_Capital.xlsx", "GLC_02_Danamas_Strategy.docx"],
      prompts: [
        { tool: "📊 Copilot in Excel", license: "M365", account: "Premium", prompts: [
          { title: "Programme disbursement risk analysis", prompt: "In the Programme KPIs sheet, identify all programmes with disbursement rate below 50%. Calculate the budget at risk (uncommitted by year end) and the PAC risk level. Create a priority ranking for remediation action." },
          { title: "Portfolio ROE benchmarking", prompt: "Compare ROE across all portfolio companies. Which companies are below the cost of capital (assume 8%)? What is the total value destruction if underperformers are not turned around in 3 years?" },
          { title: "Investment pipeline IRR analysis", prompt: "In the Investment Pipeline sheet, rank all investments by IRR. Identify which deals have the best risk-adjusted return. Calculate the weighted average portfolio IRR if all pipeline deals close." }
        ]},
        { tool: "📝 Copilot in Word", license: "M365", account: "Premium", prompts: [
          { title: "PAC testimony preparation", prompt: "Based on the strategy document, draft a 3-page briefing for the CEO ahead of Parliamentary Accounts Committee testimony on the National Digital Infrastructure Fund. Address: disbursement shortfall, root causes, corrective actions, and revised timeline." },
          { title: "Port privatisation investment memo", prompt: "Draft a 2-page investment committee memo recommending the Port Klang North privatisation (MYR 4.8B, 30-year concession, 10.8% IRR target). Include strategic rationale, financial summary, key risks, and board approval sought." },
          { title: "ESG impact report section", prompt: "Draft the 'Social Impact' section of Danamas Capital's annual integrated report. Highlight: jobs created by portfolio companies, affordable housing units delivered, SMEs financed, and Bumiputera vendor spend." }
        ]},
        { tool: "🤖 Copilot Chat", license: "Basic", account: "Basic", prompts: [
          { title: "GLC governance best practices", prompt: "What are the OECD guidelines for corporate governance of state-owned enterprises? How do leading GLICs in Asia (like Temasek, Khazanah) structure their portfolio oversight?" },
          { title: "EUDR and palm oil GLCs", prompt: "How does the EU Deforestation Regulation affect Malaysian government-linked plantation companies? What actions are GLCs in Malaysia taking to comply?" }
        ]},
        { tool: "📧 Copilot in Outlook", license: "M365", account: "Premium", prompts: [
          { title: "Chase programme owners", prompt: "Draft a firm but constructive email to programme owners whose disbursement rates are below 40%, requesting an urgent action plan within 5 working days. Attach the programme KPI tracker." },
          { title: "MOF update briefing", prompt: "Summarise the portfolio performance for Q1 FY2025 into a concise brief suitable for the Minister of Finance. Highlight the 2 underperforming portfolio companies and the 2 programmes at PAC risk." }
        ]}
      ]
    },
    {
      id: "education",
      name: "Education & EdTech",
      icon: "🎓",
      color: "#1A237E",
      accent: "#283593",
      company: "Citra University Group Berhad",
      tagline: "Malaysia's 5th largest private HEI | 55,620 students | 7 campuses in MY, ID, AU",
      scenario: "Citra University needs to climb from QS 401-450 to Top 350 by FY2027. The Provost is designing a research commercialisation strategy via the new Technology Transfer Office, while the Indonesia team is preparing for BAN-PT 'Unggul' accreditation and a new Bandung campus.",
      files: ["EDU_01_Citra_University_Group.xlsx", "EDU_02_Citra_University_Strategy.docx"],
      prompts: [
        { tool: "📊 Copilot in Excel", license: "M365", account: "Premium", prompts: [
          { title: "QS ranking gap analysis", prompt: "From the Academic Performance sheet, calculate the gap between current performance and Top 350 thresholds for each QS metric. Which metric, if improved first, would have the fastest impact on overall ranking?" },
          { title: "Research grant ROI", prompt: "In the Research & Grants sheet, calculate research output (papers) per MYR million of grant funding for each research centre. Which centres have the best research productivity? Which are underperforming?" },
          { title: "Enrolment revenue model", prompt: "Model the revenue impact of growing international student percentage from 22% to 30% by FY2027 across all campuses. Assume international students pay 1.8x local tuition. What is the revenue uplift?" }
        ]},
        { tool: "📝 Copilot in Word", license: "M365", account: "Premium", prompts: [
          { title: "Board QS strategy paper", prompt: "Based on the strategy document, draft a 2-page Board paper recommending the QS Top 350 investment plan. Include: gap analysis summary, 5 targeted interventions, total investment required (MYR), and 3-year milestone plan." },
          { title: "BAN-PT Unggul application narrative", prompt: "Draft the institutional narrative section for Citra Indonesia's BAN-PT Unggul accreditation application. Highlight academic achievements, research output, industry linkages, and graduate outcomes. Tone: confident and evidence-based." },
          { title: "CitraVentures pitch deck narrative", prompt: "Write a compelling narrative for the CitraVentures startup studio investor pitch. Cover: why universities make great startup studios, Citra's IP pipeline, the 3 investment thesis areas, and the fund structure." }
        ]},
        { tool: "🤖 Copilot Chat", license: "Basic", account: "Basic", prompts: [
          { title: "QS ranking methodology", prompt: "Explain how the QS World University Rankings are calculated. What are the 6 indicators and their weightings? Which indicators are most actionable for a university currently ranked 401-450?" },
          { title: "EdTech market in Indonesia", prompt: "What is the size and growth rate of the private higher education market in Indonesia? Which segments (online, vocational, postgraduate) are growing fastest?" }
        ]},
        { tool: "🤝 Copilot in Teams", license: "M365", account: "Premium", prompts: [
          { title: "Faculty meeting recap", prompt: "Generate meeting notes from today's Academic Senate discussion. List all decisions made, motions passed, and action items with owners. Flag any items requiring follow-up before the next meeting." },
          { title: "Research collaboration proposal", prompt: "Draft a message to the UGM (Universitas Gadjah Mada) partnership team proposing the 3 joint research centres agenda for our next video call. Include suggested timeline and expected outcomes." }
        ]}
      ]
    },
    {
      id: "hospitality",
      name: "Hospitality & Tourism",
      icon: "🏨",
      color: "#4A148C",
      accent: "#6A1B9A",
      company: "Suria Hotels & Resorts Berhad",
      tagline: "Premium hotel group | 9 properties | MY + ID | MYR 1.84B revenue",
      scenario: "Suria Hotels' Bali property is the top performer (88% occupancy, NPS 88) while the Labuan property is underperforming (62% occupancy). The Revenue Manager needs to optimise pricing across the portfolio, and the F&B Director is planning a TikTok-driven beachclub marketing campaign.",
      files: ["HT_01_Suria_Hotels_Resorts.xlsx"],
      prompts: [
        { tool: "📊 Copilot in Excel", license: "M365", account: "Premium", prompts: [
          { title: "RevPAR performance ranking", prompt: "Rank all 9 hotels by RevPAR and RevPAR YoY growth. Identify the top 3 and bottom 3 performers. For the bottom 3, calculate the RevPAR gap to group average and estimate the revenue recovery if they close 50% of the gap." },
          { title: "F&B profitability analysis", prompt: "In the F&B Operations sheet, calculate GOP per cover for each outlet. Which outlets have the highest margin? What is the relationship between cover volume and GOP%?" },
          { title: "Demand segmentation strategy", prompt: "In the Revenue & Demand Forecast sheet, analyse the leisure vs corporate vs MICE revenue mix by property. Which properties are over-indexed on low-margin OTA bookings? What pricing actions would shift the mix to higher direct booking?" }
        ]},
        { tool: "📝 Copilot in Word", license: "M365", account: "Premium", prompts: [
          { title: "Revenue optimisation strategy", prompt: "Draft a 2-page revenue optimisation strategy for the Suria Labuan Marina hotel, which is underperforming at 62% occupancy. Include: market analysis, demand drivers (oil & gas sector), pricing strategy, MICE targeting, and 12-month RevPAR recovery target." },
          { title: "Beachclub marketing proposal", prompt: "Draft a digital marketing proposal for the Suria Bali Beachclub targeting international millennials. Include: TikTok and Instagram content strategy, influencer tier (nano/micro/macro), event calendar, and 90-day KPIs." },
          { title: "MICE sales kit", prompt: "Create a 1-page MICE sales kit for the Suria Grand KL Ballroom. Include: capacity configurations, AV capabilities, catering packages, accommodation block rates, and booking incentives for corporate clients." }
        ]},
        { tool: "🤖 Copilot Chat", license: "Basic", account: "Basic", prompts: [
          { title: "Hotel pricing strategy", prompt: "What is dynamic pricing in hotel revenue management? How do leading hotels use AI to set optimal room rates in real time? What tools are commonly used?" },
          { title: "MICE market outlook", prompt: "What is the outlook for the MICE (Meetings, Incentives, Conferences, Exhibitions) market in Malaysia and Southeast Asia for 2025-2026? Which segments are growing fastest post-pandemic?" }
        ]},
        { tool: "🎯 Copilot in PowerPoint", license: "M365", account: "Premium", prompts: [
          { title: "Owner's report presentation", prompt: "Create a 6-slide quarterly owner's report presentation. Include: portfolio occupancy dashboard, RevPAR vs budget, F&B performance highlights, NPS scores by property, key operational issues, and 90-day outlook." }
        ]}
      ]
    },
    {
      id: "plantation",
      name: "Plantation & Agribusiness",
      icon: "🌿",
      color: "#1B5E20",
      accent: "#2E7D32",
      company: "Zava Agribusiness (Perkebunan Lestari)",
      tagline: "RSPO suspended | 8,200 ha peat | EUDR risk Jan 2026 | Use Zava demo files",
      scenario: "Perkebunan Lestari's RSPO certification has been suspended over 8,200 ha of peatland. The Sustainability Director must prepare the Corrective Action Plan for RSPO reinstatement while managing the EUDR compliance risk for EU export markets.",
      files: ["11_Zava_Agribusiness_Plantations.xlsx", "22_Zava_Plantation_RSPO_Audit.docx", "20_Zava_ESG_Sustainability_Framework.docx"],
      prompts: [
        { tool: "📊 Copilot in Excel", license: "M365", account: "Premium", prompts: [
          { title: "CPO price impact analysis", prompt: "Calculate the revenue impact of the RSPO suspension. Use the price discount of MYR 80-120/MT for non-certified CPO vs RSPO-certified CPO, applied to Perkebunan Lestari's production volume. What is the FY2025 revenue loss?" },
          { title: "Yield benchmark analysis", prompt: "Compare FFB yield per hectare across all estates. Which estates are above and below the industry benchmark of 20 MT/ha/yr? Calculate the potential revenue uplift from bringing underperforming estates to benchmark." },
          { title: "Worker welfare metrics", prompt: "Review the worker welfare KPIs. Which estates have the highest absenteeism and attrition? Is there a correlation with housing quality scores? Suggest which estate to prioritise for the housing upgrade programme." }
        ]},
        { tool: "📝 Copilot in Word", license: "M365", account: "Premium", prompts: [
          { title: "RSPO corrective action plan", prompt: "Draft the Corrective Action Plan (CAP) for RSPO P&C reinstatement. Structure it around the 3 RSPO requirements: independent peatland assessment, worker rights audit, and CAP submission. Include milestones, responsible parties, and evidence required." },
          { title: "EUDR compliance roadmap", prompt: "Based on the ESG framework document, draft a 2-page EUDR compliance roadmap for Perkebunan Lestari. Include: geolocation data collection plan, deforestation-free polygon mapping, traceability platform selection, and EU counsel engagement." },
          { title: "Sustainability report section", prompt: "Draft the Plantation chapter for Zava Group's annual sustainability report. Cover: RSPO status, peatland management, worker welfare, biodiversity, and FY2026 targets. Tone: transparent, addressing challenges honestly." }
        ]},
        { tool: "🤖 Copilot Chat", license: "Basic", account: "Basic", prompts: [
          { title: "RSPO reinstatement process", prompt: "Explain the RSPO certification reinstatement process. What steps must a plantation company take after suspension? How long does reinstatement typically take?" },
          { title: "EUDR palm oil requirements", prompt: "What specific due diligence requirements does the EU Deforestation Regulation impose on palm oil exporters? What geolocation and traceability data is required?" }
        ]},
        { tool: "📓 Copilot Notebook", license: "M365", account: "Premium", prompts: [
          { title: "RSPO + EUDR risk synthesis", prompt: "I've uploaded the plantation KPI data, the RSPO audit document, and the ESG framework. Synthesise the full sustainability risk picture: RSPO reinstatement timeline, EUDR compliance gaps, financial impact, and a prioritised action plan. Format as a Board risk memo." }
        ]}
      ]
    },
    {
      id: "manufacturing",
      name: "Manufacturing & Industrial",
      icon: "🏭",
      color: "#37474F",
      accent: "#455A64",
      company: "Zava Manufacturing (Nilai Plant)",
      tagline: "OEE declined 76%→62% | Spindle motor failure | Use Zava demo files",
      scenario: "The Nilai manufacturing plant's OEE has dropped from 76% to 62% over 24 months due to a spindle motor failure. The Plant Manager needs to build a capital case for replacement, while the Operations Director is implementing TPM (Total Productive Maintenance) to prevent further decline.",
      files: ["12_Zava_Manufacturing_KPIs.xlsx", "21_Zava_Chemical_Safety_HIRARC.docx"],
      prompts: [
        { tool: "📊 Copilot in Excel", license: "M365", account: "Premium", prompts: [
          { title: "OEE root cause analysis", prompt: "Analyse the OEE decline from 76% to 62% across the Availability, Performance, and Quality components. Which component drove the most decline? Calculate the revenue impact of the 14-point OEE drop." },
          { title: "Maintenance cost vs downtime", prompt: "Plot the relationship between planned maintenance spend and unplanned downtime hours by month. Is there a correlation? Calculate the break-even point for the MYR 18.4M spindle motor replacement capex." },
          { title: "Production loss quantification", prompt: "Quantify the production volume lost due to OEE decline. Multiply lost production hours by standard output rate and average selling price per unit. What is the cumulative revenue loss over 24 months?" }
        ]},
        { tool: "📝 Copilot in Word", license: "M365", account: "Premium", prompts: [
          { title: "Capex approval request", prompt: "Draft a capital expenditure approval request for the MYR 18.4M spindle motor replacement. Include: current state (OEE 62%), proposed solution, financial justification (NPV, payback period), risk of not investing, and project timeline." },
          { title: "TPM implementation plan", prompt: "Draft a 90-day Total Productive Maintenance (TPM) implementation plan for the Nilai plant. Cover the 8 TPM pillars, prioritise the top 3 most impactful, and define KPIs to measure success." },
          { title: "Chemical safety HIRARC summary", prompt: "Summarise the top 5 hazards identified in the Chemical Safety HIRARC document. For each hazard, state the risk rating, current controls, and recommended additional controls." }
        ]},
        { tool: "🤖 Copilot Chat", license: "Basic", account: "Basic", prompts: [
          { title: "OEE improvement strategies", prompt: "What are the most effective strategies for improving Overall Equipment Effectiveness (OEE) in a discrete manufacturing plant? Which improvement typically delivers the fastest results?" },
          { title: "Industry 4.0 for maintenance", prompt: "How are manufacturers using IoT sensors and predictive maintenance to prevent equipment failures? What is the typical ROI on a predictive maintenance implementation?" }
        ]},
        { tool: "📊 Copilot in Excel (Advanced)", license: "M365", account: "Premium", prompts: [
          { title: "Predictive maintenance model", prompt: "Build a simple predictive maintenance scoring model using the equipment vibration, temperature, and hours-run data. Score each machine 1-10 for failure risk in the next 30 days. Highlight machines above score 7." }
        ]}
      ]
    },
    {
      id: "pharma",
      name: "Pharmaceutical & Biotech",
      icon: "💊",
      color: "#880E4F",
      accent: "#AD1457",
      company: "Zava Pharma (ZavaGen Sitagliptin)",
      tagline: "BPfK registration in progress | MYR 132M Year 1 revenue target | Use Zava demo files",
      scenario: "Zava Pharma's Sitagliptin registration has advanced to BPfK Phase 2 evaluation after successfully closing all 3 deficiencies. The Regulatory Affairs team is now managing the BPOM Indonesia parallel submission and preparing the commercial launch plan for Q2 2026.",
      files: ["17_Zava_Pharma_Pipeline.xlsx", "Email_11_Sitagliptin_BPOM_Registration.docx"],
      prompts: [
        { tool: "📊 Copilot in Excel", license: "M365", account: "Premium", prompts: [
          { title: "Pipeline revenue at risk", prompt: "In the Pharma Pipeline sheet, identify all products with registration delays >3 months vs plan. Calculate the cumulative revenue at risk in Year 1. Rank by revenue impact." },
          { title: "Market share modelling", prompt: "Model Sitagliptin market share scenarios: 5%, 10%, and 15% of the Malaysian oral antidiabetic market (estimated MYR 840M). At each scenario, calculate revenue and gross margin at 62% pharmaceutical margin." },
          { title: "ASEAN registration timeline", prompt: "Create a Gantt-style timeline showing the registration status for all pipeline products across Malaysia, Indonesia, Thailand, and Philippines. Flag products where Malaysia and Indonesia timelines are more than 6 months apart." }
        ]},
        { tool: "📝 Copilot in Word", license: "M365", account: "Premium", prompts: [
          { title: "Regulatory response draft", prompt: "Using the email thread as context, draft a formal response to BPfK addressing Deficiency 2 (BCS classification). Adopt the BCS Class III reclassification strategy and include the biowaiver argument for the 25mg and 50mg strengths." },
          { title: "Launch readiness plan", prompt: "Draft a 2-page commercial launch readiness plan for ZavaGen Sitagliptin targeting Q2 2026. Include: market access strategy, pricing (reference Januvia® positioning), channel strategy (hospital vs retail pharmacy), KOL engagement, and 90-day post-launch KPIs." },
          { title: "Medical affairs brief", prompt: "Draft a Medical Affairs briefing document for the Sitagliptin BCS Class III reclassification. Explain the scientific rationale to the medical sales team in plain language, and provide 3 key messages for KOL discussions." }
        ]},
        { tool: "🤖 Copilot Chat", license: "Basic", account: "Basic", prompts: [
          { title: "BCS classification explained", prompt: "Explain the Biopharmaceutics Classification System (BCS) for drug products. What is the difference between BCS Class II and Class III, and why does the classification matter for bioequivalence study requirements?" },
          { title: "Generic drug market Malaysia", prompt: "What is the size of the generic pharmaceutical market in Malaysia? How does the government's generic first policy affect market dynamics for new generic entrants?" }
        ]},
        { tool: "📓 Copilot Notebook", license: "M365", account: "Premium", prompts: [
          { title: "Regulatory dossier analysis", prompt: "I've uploaded the pharma pipeline data and the BPfK email correspondence. Analyse the overall regulatory risk profile of our pipeline — which products are most at risk of delay, what are the common deficiency themes across products, and what process improvements would reduce future regulatory risks?" }
        ]}
      ]
    },
    {
      id: "property",
      name: "Real Estate & Property",
      icon: "🏗",
      color: "#E65100",
      accent: "#BF360C",
      company: "Zava Properties (REIT Candidate)",
      tagline: "MYR 8.2B portfolio | REIT IPO FY2026 | Office + Retail + Industrial | Use Zava demo files",
      scenario: "Zava Properties is preparing for a REIT IPO in FY2026. JLL has provided a draft MYR 8.2B portfolio valuation. The Head of Real Estate needs to prepare the REIT feasibility study, while the Asset Management team is working to improve occupancy at underperforming assets before the listing.",
      files: ["14_Zava_Properties_Portfolio.xlsx", "03_Zava_Group_Strategy_Framework.docx"],
      prompts: [
        { tool: "📊 Copilot in Excel", license: "M365", account: "Premium", prompts: [
          { title: "REIT eligibility screening", prompt: "Review the property portfolio. Identify which assets meet REIT eligibility criteria: income-producing, >80% occupancy, >3 years operating history. Calculate the REIT-eligible portfolio value and projected distribution per unit at 90% payout." },
          { title: "Occupancy gap analysis", prompt: "Identify properties with occupancy below 85%. For each, calculate the rental income uplift if occupancy reaches 90%. What is the total portfolio income impact?" },
          { title: "Valuation cap rate analysis", prompt: "Using the portfolio data, calculate implied cap rates for each asset class (office, retail, industrial, logistics). Compare to market cap rates from the JLL report. Which assets appear over or under valued?" }
        ]},
        { tool: "📝 Copilot in Word", license: "M365", account: "Premium", prompts: [
          { title: "REIT feasibility executive summary", prompt: "Draft the executive summary of the REIT feasibility study. Cover: portfolio overview, REIT structure proposed, IPO size estimate, target investor base (retail vs institutional), listing timeline, and key value creation thesis." },
          { title: "Asset management strategy", prompt: "Draft a 2-page asset management improvement plan for the 3 highest vacancy properties. For each: root cause of vacancy, proposed leasing strategy, capex for asset enhancement, and target occupancy within 18 months." },
          { title: "Investor relations fact sheet", prompt: "Create a 1-page investor fact sheet for the proposed Zava REIT. Include: portfolio summary, financial highlights (NPI yield, gearing), management team, dividend policy, and growth strategy." }
        ]},
        { tool: "🤖 Copilot Chat", license: "Basic", account: "Basic", prompts: [
          { title: "REIT listing requirements Malaysia", prompt: "What are the listing requirements for a REIT on Bursa Malaysia? What minimum asset value, distribution rate, and gearing limits apply?" },
          { title: "Office market outlook Malaysia", prompt: "What is the outlook for Grade A office space demand in Kuala Lumpur for 2025-2026? How is flexible workspace affecting traditional office leasing?" }
        ]},
        { tool: "🎯 Copilot in PowerPoint", license: "M365", account: "Premium", prompts: [
          { title: "REIT IPO roadshow deck", prompt: "Create a 10-slide REIT IPO roadshow presentation. Include: Malaysia REIT market context, portfolio highlights, financial performance, growth strategy, management team, and investment highlights. Professional investor-grade design." }
        ]}
      ]
    },
    {
      id: "bpo",
      name: "BPO & Technology Services",
      icon: "💻",
      color: "#01579B",
      accent: "#0277BD",
      company: "Zava BPO (Bengaluru Centre)",
      tagline: "3,000+ FTE | 31.2% attrition → recovery | USD 98M ARR | Use Zava demo files",
      scenario: "Zava BPO's Bengaluru centre had a 31.2% attrition crisis. The CHRO has launched a retention programme and attrition is now falling (24.8% in March). The VP Client Management is fighting to retain Bank Mandiri against Infosys pricing pressure, while deploying the DOCUAI accuracy engine.",
      files: ["15_Zava_BPO_Operations.xlsx", "18_Zava_HR_Analytics.xlsx", "Email_13_Bengaluru_Attrition_Crisis.docx", "Email_12_BPO_Contract_Pipeline.docx"],
      prompts: [
        { tool: "📊 Copilot in Excel", license: "M365", account: "Premium", prompts: [
          { title: "Attrition cost model", prompt: "Using the BPO operations data, calculate the full cost of 31.2% attrition: replacement cost per FTE × number of leavers. Then model the savings at 22% attrition (target). What is the ROI of the retention programme?" },
          { title: "Contract renewal revenue analysis", prompt: "Analyse the 3 contract renewals: Sime Darby (USD 8.42M), Bank Mandiri (USD 7.4M bid vs USD 8.4M current), Panasonic (USD 3.8M). Calculate total ARR impact vs prior year. What is net revenue change if Bank Mandiri is won vs lost?" },
          { title: "SLA performance tracker", prompt: "Review the SLA performance data for each client account. Flag any accounts with SLA scores below target for 2 consecutive quarters. Calculate the penalty exposure if SLAs are not remediated." }
        ]},
        { tool: "📝 Copilot in Word", license: "M365", account: "Premium", prompts: [
          { title: "Bank Mandiri RFP response", prompt: "Draft the 'Quality & Track Record' section of the Bank Mandiri RFP response. Honestly address the Q3 FY2024 SLA breach, explain root cause (client system migration), actions taken, and current Q1 FY2025 SLA performance (clean month)." },
          { title: "Retention ROI board paper", prompt: "Using the attrition email thread as context, draft a 2-page Board paper presenting the Bengaluru retention programme ROI. Include: investment (USD 1.932M Year 1), savings (USD 1.206M), net position, and strategic value beyond the numbers." },
          { title: "DOCUAI capability statement", prompt: "Write a 1-page technology capability statement for DOCUAI (the AI document classification engine) to include in the Bank Mandiri RFP. Include: how it works, accuracy improvement (from 97.2% to 99.8%), go-live timeline, and references." }
        ]},
        { tool: "🤖 Copilot Chat", license: "Basic", account: "Basic", prompts: [
          { title: "BPO pricing benchmarks India", prompt: "What is the current market rate for BPO document processing services delivered from India? How does Infosys BPM, WNS, and Genpact typically price per-FTE vs transaction-based models?" },
          { title: "AI in BPO industry trends", prompt: "How is AI and automation changing the BPO industry? Which processes are most amenable to automation? What does this mean for headcount-based BPO pricing models?" }
        ]},
        { tool: "📧 Copilot in Outlook", license: "M365", account: "Premium", prompts: [
          { title: "Summarise attrition thread", prompt: "Summarise the Bengaluru attrition email thread. List: (1) the key decisions made, (2) the actions taken and by whom, (3) the current status as of the latest email, (4) what still needs to be done." },
          { title: "Client update email", prompt: "Draft a proactive client update email to Bank Mandiri's Head of Operations. Share the Q1 FY2025 SLA performance improvement, introduce the DOCUAI deployment plan, and propose a partnership review meeting." }
        ]}
      ]
    }
  ]
};
