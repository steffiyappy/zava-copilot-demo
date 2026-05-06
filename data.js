// IDMY Copilot Industry Hub — Data File
// Update prompts and whats-new monthly
window.HUB_DATA = {
  whatsNew: [
    { date: "May 2026", title: "Copilot in Excel — Python integration GA", desc: "Run Python scripts directly inside Excel cells via Copilot. Analyse data, build models, and visualise results without leaving the grid.", tag: "Excel", color: "#217346" },
    { date: "May 2026", title: "Copilot Notebook — multi-file reasoning", desc: "Upload up to 5 files into a single Notebook session. Copilot now reasons across all files simultaneously, surfacing cross-document insights in one response.", tag: "Notebook", color: "#0078D4" },
    { date: "Apr 2026", title: "Copilot in Teams — meeting coach", desc: "After each recorded meeting, Copilot rates your communication: clarity, conciseness, and listening ratio. One-click suggestions to improve next time.", tag: "Teams", color: "#6264A7" },
    { date: "Apr 2026", title: "Copilot Pages — shared canvas GA", desc: "Copilot Pages is now generally available. Co-edit AI-generated content with your team in real time. Pages sync to SharePoint and Teams channels automatically.", tag: "Pages", color: "#FF6B35" },
    { date: "Mar 2026", title: "Copilot in Outlook — Priority Inbox AI", desc: "Priority Inbox AI now scores every email 1–10 for urgency and business impact. Copilot surfaces the top 3 emails to act on each morning, with a one-line action summary.", tag: "Outlook", color: "#0078D4" }
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
      scenario: "It is Monday morning at Zava Group Holdings Berhad. Sasha Ouellet, Group Chief Strategy Officer, has 47 unread emails, a Risk Committee meeting in 2 hours, and a Board pre-read due by 3pm — all with a free Copilot Chat account. MOD Administrator, Group IT Director, is rolling out M365 Copilot to 1,200 KL office staff and needs to demonstrate the full breadth of what Copilot can do: from email triage and regulatory drafting, to multi-document synthesis and AI agents scoped to company knowledge. This is the start-here demo track — every tool, every persona, real files from Zava Group operations.",
      files: ["Email_07_Emergency_Board_Meeting.docx", "Email_09_Risk_Committee_Prep.docx", "01_Zava_Group_Financial_Performance.xlsx", "03_Zava_Group_Strategy_Framework.docx", "02_Zava_Group_Policy_Handbook.docx"],
      prompts: [
        {
          tool: "🤖 Copilot Chat (Basic)",
          license: "Free — no M365 license needed",
          account: "Sasha Ouellet — SashaO@ABSx62256373.OnMicrosoft.com",
          prompts: [
            {
              title: "Understand M365 Copilot licensing tiers",
              prompt: "Ask Copilot: \"Explain the difference between the free Microsoft 365 Copilot Chat (included with a work account) and the paid M365 Copilot license. List the features available in each tier formatted as a 2-column table: Free vs Paid. Specifically cover: grounded web search, document upload and analysis, Teams meeting recap, Outlook email drafting and coaching, Excel formula generation, and SharePoint knowledge search. My audience is a Group IT Director presenting to 1,200 Zava Group staff who are about to receive M365 Copilot licences.\""
            },
            {
              title: "Brief me before a Monday Risk Committee meeting",
              prompt: "Ask Copilot: \"I am the Chief Strategy Officer of Zava Group Holdings Berhad, a Malaysian diversified conglomerate with banking, chemicals, agribusiness, manufacturing, financial services, properties, BPO, and trading divisions. It is Monday morning. I have a Risk Committee meeting at 10am and a Board pre-read due by 3pm. Give me a structured 5-bullet Monday briefing covering: MYR currency risk, commodity price volatility for palm oil and coal, Bursa Malaysia ESG compliance deadlines, BNM banking regulatory environment, and generative AI adoption pressure from competitors. Each bullet: 2 sentences maximum.\""
            },
            {
              title: "Draft a Teams message to my COO",
              prompt: "Ask Copilot: \"Draft a direct, professional Teams message to Daichi Maruyama, Group COO of Zava Group, reminding him that the Risk Committee briefing pack — covering the Meridian Bank NPL crisis update, the Bengaluru BPO attrition programme, and the PETRONAS compliance audit timeline — must be distributed to all 8 committee members by 11:30am today, before the 1pm pre-read session. Ask him to confirm send. Maximum 60 words. Suitable for Microsoft Teams chat. Professional but not overly formal.\""
            }
          ]
        },
        {
          tool: "�� Researcher",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Research M365 Copilot ROI evidence for internal business case",
              prompt: "In Copilot Chat, switch to the Researcher agent. Upload 03_Zava_Group_Strategy_Framework.docx. Ask: \"Analyse our group strategy document for AI readiness gaps, then search the web for the most recent Microsoft 365 Copilot ROI studies from Forrester, IDC, and the Microsoft Work Trend Index 2024 and 2025. Cross-reference: which of our stated 5-year strategic priorities would benefit most from M365 Copilot deployment, based on the published evidence? Format as a 3-column table: Strategic Priority | AI Opportunity | ROI Evidence Source. Include at least 3 credible citations with URLs.\"",
              fileRef: "03_Zava_Group_Strategy_Framework.docx"
            },
            {
              title: "Research Bursa Malaysia ESG mandatory disclosure requirements",
              prompt: "In Copilot Chat, switch to the Researcher agent. Ask: \"Search the web for Bursa Malaysia's mandatory ESG and sustainability reporting requirements for Main Market PLCs taking effect in 2025 and 2026. Cover: the Sustainability Reporting Guide 3rd edition, TCFD-aligned climate disclosures, Scope 1/2/3 GHG reporting thresholds by company size, and board-level ESG governance requirements. Also check for any recent Bursa enforcement actions or queries related to ESG non-disclosure. Format as a structured compliance briefing under 4 headings, suitable for presentation to a Board Sustainability and Governance Committee.\""
            },
            {
              title: "Research global conglomerate digital transformation case studies",
              prompt: "In Copilot Chat, switch to the Researcher agent. Upload GLC_02_Danamas_Strategy.docx. Ask: \"Review the Danamas strategy document, then search the web for recent examples of large Asian conglomerates or GLCs — including Temasek, Khazanah, and major BUMN companies in Indonesia — that have implemented group-wide digital transformation programs. What governance structures, technology platforms, and change management approaches did they use? Also search for any recent Malaysian EPU or MOF guidance on GLC digital transformation. Present key learnings as a comparative table of 4 organisations with their approach and outcomes.\"",
              fileRef: "GLC_02_Danamas_Strategy.docx"
            }
          ]
        },
        {
          tool: "📊 Analyst",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Analyse group financial performance trends FY2022-FY2024",
              prompt: "In Copilot Chat, switch to the Analyst agent. Upload 01_Zava_Group_Financial_Performance.xlsx. Ask: \"Run a comprehensive trend analysis across all Zava Group divisions from FY2022 to FY2024. Calculate: (1) Revenue compound annual growth rate per division, (2) EBITDA margin trend — improving or deteriorating — with exact percentage point change, (3) the 2 divisions with the highest and lowest return on equity, (4) group-level net debt to EBITDA. Flag any division where EBITDA margin declined more than 3 percentage points in 2 consecutive years. Output as structured Python-generated insights with a division comparison chart.\"",
              fileRef: "01_Zava_Group_Financial_Performance.xlsx"
            },
            {
              title: "Analyse group HR attrition patterns",
              prompt: "In Copilot Chat, switch to the Analyst agent. Upload 18_Zava_HR_Analytics.xlsx. Ask: \"Analyse Zava Group HR data to identify attrition risk hotspots. Find: (1) the 3 business units with the highest voluntary attrition rates, (2) any statistical correlation between attrition rate and average compensation band, (3) whether attrition is concentrated in the 0-1 year or 1-3 year tenure bands, (4) the gender breakdown of voluntary resignations across divisions. The BPO Bengaluru centre has reported 31.2% attrition — confirm whether the data aligns. Present as a heatmap-ready summary with 5 actionable findings for the Group CHRO.\"",
              fileRef: "18_Zava_HR_Analytics.xlsx"
            },
            {
              title: "Model NPL scenario impact on group financials",
              prompt: "In Copilot Chat, switch to the Analyst agent. Upload 13_Zava_Financial_Services.xlsx. Ask: \"Analyse the Financial Services division data. Model 3 NPL scenarios for the banking segment: Base case (NPL stays at 14.2%), Recovery (NPL reduces to 9% by Q4 FY2025), and Stress (NPL rises to 18%). For each scenario calculate: (1) additional provision requirement in MYR millions, (2) impact on pre-tax profit as a percentage change, (3) estimated CET1 capital ratio sensitivity, (4) whether BNM's 3.5% NPL threshold breach triggers regulatory consequences. Present as a 5-column scenario comparison table suitable for the Group CFO's Board presentation.\"",
              fileRef: "13_Zava_Financial_Services.xlsx"
            }
          ]
        },
        {
          tool: "📊 Copilot in Excel",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Instant group financial workbook summary",
              prompt: "Open 01_Zava_Group_Financial_Performance.xlsx. In the Copilot pane on the right, ask: \"Give me a plain-English executive summary of this entire workbook. Which division has the highest FY2024 revenue? Which has the most concerning EBITDA margin trend from FY2022 to FY2024? Flag any number that looks significantly outside the group average or shows a deteriorating pattern over 2 consecutive years. Format the answer as: a 2-sentence overview paragraph, then a numbered watch-list of 3 specific data concerns with the sheet and cell reference for each.\"",
              fileRef: "01_Zava_Group_Financial_Performance.xlsx"
            },
            {
              title: "Add EBITDA margin formula with conditional formatting",
              prompt: "Open 01_Zava_Group_Financial_Performance.xlsx and navigate to the Group P&L sheet. Ask Copilot: \"Add a new column called EBITDA Margin % to the right of the EBITDA column. The formula should divide each division's EBITDA by its Revenue for the same year and period. Then apply conditional formatting: green fill if margin is above 15%, amber fill if between 10% and 15%, red fill if below 10%. Confirm how many cells were updated and show me the exact formula syntax used so I can audit it.\"",
              fileRef: "01_Zava_Group_Financial_Performance.xlsx"
            },
            {
              title: "Create an executive division performance chart",
              prompt: "Open 01_Zava_Group_Financial_Performance.xlsx. Ask Copilot: \"Create a clustered bar chart comparing FY2023 and FY2024 EBITDA in MYR millions for each of Zava Group's business divisions. Use dark navy blue (#1F2D55) for FY2024 bars and light grey for FY2023. Add the chart title: Zava Group Division EBITDA FY2023 vs FY2024. Include data labels on each bar showing the exact MYR million value. Position the legend at the bottom. This chart will be exported and pasted directly into the Board presentation slide deck.\"",
              fileRef: "01_Zava_Group_Financial_Performance.xlsx"
            },
            {
              title: "Answer a natural-language financial question",
              prompt: "Open 01_Zava_Group_Financial_Performance.xlsx. Ask Copilot: \"Which 3 business divisions achieved the strongest revenue growth from FY2022 to FY2024? Express growth as both absolute MYR change in millions and percentage growth over the full 2-year period. Also tell me: which single division had the highest absolute revenue in FY2024, and what percentage of total group revenue does that division represent? Present the answer as a clean 4-column table: Division | FY2022 Revenue MYR M | FY2024 Revenue MYR M | 2-Year Growth %. No formulas — just the answer in the table.\"",
              fileRef: "01_Zava_Group_Financial_Performance.xlsx"
            }
          ]
        },
        {
          tool: "📝 Copilot in Word",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Summarise strategy document into a Board pre-read",
              prompt: "Open 03_Zava_Group_Strategy_Framework.docx. In the Copilot pane, ask: \"Summarise this entire strategy framework document into a structured 1-page Board pre-read memo. Use this exact format: Section 1 — Strategic Context (2 sentences on the macro environment), Section 2 — Five Key Priorities for 2025-2027 (bullet points with 1-sentence rationale each), Section 3 — Top 3 Strategic Risks (with likelihood and impact rating), Section 4 — What the Board is asked to approve (2 sentences). Write in formal Board memo style. Audience: non-executive directors with financial backgrounds. Maximum 400 words total.\"",
              fileRef: "03_Zava_Group_Strategy_Framework.docx"
            },
            {
              title: "Rewrite data privacy policy for non-technical staff",
              prompt: "Open 02_Zava_Group_Policy_Handbook.docx. Navigate to the Data Privacy and Cybersecurity Policy section. Ask Copilot: \"Rewrite this policy section in plain, conversational English for a non-technical employee with no IT background. Remove all technical and legal jargon. Use short sentences of no more than 20 words. Add 3 practical Do and Do Not examples that any staff member would recognise from daily work. The rewritten version should be under 300 words and should be easily understood by someone with a secondary school education.\"",
              fileRef: "02_Zava_Group_Policy_Handbook.docx"
            },
            {
              title: "Draft Zava Group AI and Copilot Usage Policy",
              prompt: "In a blank Word document, open the Copilot pane and ask: \"Draft a 400-word AI and Microsoft 365 Copilot Usage Policy for Zava Group Holdings Berhad. The policy must cover: (1) Permitted uses — document drafting, data analysis, email assistance; (2) Prohibited uses — uploading client PII, confidential financial data, or trade secrets to any public AI model; (3) Data classification rules: Public, Internal Confidential, and Strictly Confidential; (4) Employee responsibility for verifying all AI-generated outputs before use; (5) Compliance obligations under Malaysia's PDPA 2010 and BNM's RMiT framework. Format as a formal numbered policy document with an effective date of 1 January 2026.\""
            },
            {
              title: "Convert rough notes to formal Risk Committee minutes",
              prompt: "Open a new Word document. Type these rough notes, then ask Copilot to format them as formal meeting minutes: \"Risk Comm 5 May 2025. Present: Hadar Caspit CFO, Omar Ahmad CRO, William Tan GC, Sonia Ramirez CHRO, MOD Admin IT Director. Meridian Bank NPL at 14.2% personal financing — Hadar confirmed BNM bilateral on 20 May. Omar: coal trading limit breach resolved 2 May. William: BNM formal response letter going out Friday. Sonia flagged Bengaluru attrition 31.2%. Next meeting 2 June.\" Ask Copilot: \"Convert these rough notes into formal Risk Committee minutes with: heading block, attendees table, numbered agenda item summaries, decisions table, and action items table with Owner and Deadline columns.\""
            }
          ]
        },
        {
          tool: "🎯 Copilot in PowerPoint",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Create a Board FY2024 executive summary deck",
              prompt: "Open a new PowerPoint presentation. In the Copilot pane, ask: \"Create a 6-slide Board executive summary presentation for Zava Group Holdings Berhad FY2024 performance review. Slide 1: Title slide with company name and date placeholder. Slide 2: FY2024 Group Financial Highlights — 3 key metrics in large font: Total Revenue, Group EBITDA, Profit After Tax. Slide 3: Division Performance Summary in a simple table or bar chart. Slide 4: Top 3 Strategic Priorities for 2025 with owner divisions. Slide 5: Risk Dashboard with 3 risks and traffic-light status. Slide 6: Board Decisions Required. Dark navy blue theme (#1F2D55), white text, minimal design, no clipart.\""
            },
            {
              title: "Generate leadership strategy update slides",
              prompt: "Open a new PowerPoint. Ask Copilot: \"Create a 5-slide strategy update presentation for Zava Group's Group Leadership Team quarterly briefing. Base it on our 5 strategic pillars as a diversified Malaysian conglomerate. Slide themes: Overview and Context, Market Environment 2025, Strategic Pillars and Progress, Key Risks and Mitigations, Next 90-Day Priorities. Each slide: one headline, maximum 5 bullet points, and a suggested visual or icon. Use corporate navy blue and white. Keep slides text-minimal — under 50 words of body text per slide. Presentation style should match a McKinsey or BCG deck.\""
            },
            {
              title: "Add a competitive landscape matrix slide",
              prompt: "In an open PowerPoint presentation, place cursor on a new blank slide after the Market Context slide. Ask Copilot: \"Create a competitive landscape slide for a Malaysian diversified conglomerate. Draw a 2x2 positioning matrix with Digital Maturity on the x-axis and Revenue Diversification on the y-axis. Position Zava Group in the upper-right quadrant. Add 3 competitor markers: Sime Darby Berhad, YTL Corporation, and Boustead Holdings. Include a 2-sentence text box explaining Zava's differentiated position. Clean, modern design, logo placeholder in top right corner. This slide will be presented to the Board Strategy Committee.\""
            }
          ]
        },
        {
          tool: "📧 Copilot in Outlook",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Triage the Emergency Board Meeting email thread",
              prompt: "Open Outlook and locate the email thread from Email_07_Emergency_Board_Meeting.docx (copy the thread content into a draft or open the actual forwarded email). Click the Copilot icon and ask: \"Summarise this entire email thread for me. I need 4 things: (1) What specifically triggered the emergency Board meeting — state the exact issue or crisis event; (2) Who has been formally notified and who is still unaware; (3) All outstanding actions listed with the owner's name and whether each has been completed; (4) The most recent status update as of the last email. Format under 4 headings. Maximum 200 words total.\"",
              fileRef: "Email_07_Emergency_Board_Meeting.docx"
            },
            {
              title: "Draft a formal BNM response letter from CFO",
              prompt: "Open Email_06_BNM_Regulatory_Correspondence.docx and review the regulator's correspondence. In Outlook, start a new reply. Ask Copilot: \"Draft a formal response from Hadar Caspit, Group CFO, to Bank Negara Malaysia's Supervision Department. The response should: (1) Acknowledge receipt of BNM's regulatory Direction issued 15 April 2025; (2) Confirm submission of the NPL Remediation Plan by the required deadline; (3) Outline in 3 brief bullets the remediation steps already underway — credit scoring model rebuild, provision top-up, digital channel restructure; (4) Request a bilateral meeting on 20 May 2025 to present the plan in person. Tone: formal, respectful, and confident. Maximum 300 words.\"",
              fileRef: "Email_06_BNM_Regulatory_Correspondence.docx"
            },
            {
              title: "Copilot Coaching — improve a draft to a regulator",
              prompt: "In Outlook, open a new email draft. Type this rough message: \"Hi BNM team, thanks for your email. We are working on fixing the NPL issue and will send the plan soon. Sorry for the delay and please let us know if you need anything else. Regards, Hadar.\" Then click Copilot and select Coaching. Ask: \"I am the Group CFO writing to Bank Negara Malaysia's Supervision Department. Identify the problems with my draft in 3 areas: tone and formality, vagueness of commitments, and professionalism. Then provide a fully rewritten version that is appropriate for senior regulatory correspondence. Show both original and improved versions side by side.\""
            }
          ]
        },
        {
          tool: "🎙 Copilot in Teams",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Catch up after missing a leadership meeting",
              prompt: "Open an existing Teams meeting that was recorded and has a Copilot-generated recap — ideally a project update, leadership standup, or committee meeting from your own calendar. Click the meeting in Teams to open the recap tab. Ask Copilot: \"I missed this meeting completely. Give me a structured 5-point briefing: (1) Main topic and purpose of the meeting, (2) Key decisions that were made and are now confirmed, (3) Items that were unresolved or deferred to a future meeting, (4) Any actions that were assigned specifically to me or my team, (5) The single most important next step before the next meeting. Keep it under 200 words.\""
            },
            {
              title: "Extract all action items with owners and deadlines",
              prompt: "Open an existing recorded Teams meeting recap — a project review, committee, or board preparation meeting from your actual calendar. In the Copilot recap panel, ask: \"List every action item from this meeting as a structured table. For each action include: Action Description — exactly what needs to be done; Owner — the person responsible by name; Deadline — the date committed to, or Not Specified if none was given; Context — one sentence explaining why this action was assigned. If there are more than 8 action items, group them by owner. Format as a clean table I can paste directly into an email or SharePoint page.\""
            },
            {
              title: "Generate a meeting follow-up email from the recap",
              prompt: "Open an existing recorded Teams meeting recap from your calendar. After reviewing the Copilot recap summary, ask Copilot: \"Draft a professional follow-up email to all meeting participants. Include: Subject line formatted as Meeting Recap and Actions — [Meeting Topic] — [Date]; a 3-sentence summary of what was discussed and decided; a numbered list of all action items with the owner name and deadline for each; confirmation of the next meeting date if one was agreed; and a professional sign-off. Write in a tone appropriate for a senior management team. This email should be ready to send directly from Outlook without edits.\""
            }
          ]
        },
        {
          tool: "📓 Copilot Notebook",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Multi-document CEO briefing for Board meeting",
              prompt: "Go to copilot.microsoft.com. Click Notebook in the left navigation. Upload these 3 files: 03_Zava_Group_Strategy_Framework.docx, 01_Zava_Group_Financial_Performance.xlsx, Email_09_Risk_Committee_Prep.docx. In the Instructions box type: \"You are preparing Group CEO Dato Sri Irfan Zavaree for tomorrow's Board meeting. Using all 3 uploaded files together, write a structured 1-page CEO Talking Points Brief covering: (1) The FY2024 financial story in 3 sentences — the headline number, the highlight, and the concern; (2) Top 3 strategic updates requiring Board awareness; (3) 2 risk items requiring Board decision with recommended positions; (4) Any urgent flag from the Risk Committee email thread. Use Board memo style with clear numbered headings.\"",
              fileRef: "03_Zava_Group_Strategy_Framework.docx, 01_Zava_Group_Financial_Performance.xlsx, Email_09_Risk_Committee_Prep.docx"
            },
            {
              title: "Group policy compliance gap analysis across 5 risk areas",
              prompt: "Go to Copilot Notebook. Upload 02_Zava_Group_Policy_Handbook.docx. In the Instructions box type: \"Conduct a policy gap analysis of this Zava Group Policy Handbook against 5 critical risk areas: (1) Generative AI and Microsoft 365 Copilot usage — does a formal policy exist or is there a gap; (2) Remote and hybrid work endpoint security; (3) Third-party vendor and outsourcing data access controls; (4) Whistleblower anonymity and non-retaliation protections; (5) Cross-border data transfers, specifically Malaysia to India BPO flows under PDPA 2010. For each area: state whether a policy exists and cite the section, summarise it in 1 sentence, and assign a RAG status: Red gap, Amber needs updating, Green compliant.\"",
              fileRef: "02_Zava_Group_Policy_Handbook.docx"
            }
          ]
        },
        {
          tool: "🤝 Cowork (Pages)",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Turn risk committee prep into a Board action plan",
              prompt: "In Copilot Chat, upload Email_09_Risk_Committee_Prep.docx and ask Copilot to summarise the key risks and outstanding items. After Copilot generates the analysis, click the Open in Copilot Pages icon at the top right of the response. In the Pages collaborative canvas, ask: \"Reorganise this risk summary into a structured Board Action Plan with 3 sections: (1) Immediate Actions — due within 7 days — with Owner, Action, and Expected Outcome columns; (2) Short-term Workstreams — next 30 days — with milestone dates; (3) Escalation Triggers — conditions that would require emergency Board intervention. Format so I can share this page directly with Risk Committee members for collaborative editing.\"",
              fileRef: "Email_09_Risk_Committee_Prep.docx"
            },
            {
              title: "Build a collaborative strategy planning canvas",
              prompt: "In Copilot Chat, upload 03_Zava_Group_Strategy_Framework.docx and ask for a strategy overview. When Copilot responds, click Open in Copilot Pages. In the Pages canvas ask: \"Expand this strategy overview into a collaborative workshop canvas for the Zava Group Leadership Team offsite. Add 6 sections: (1) Strategic Context and Key Assumptions, (2) Five Strategic Pillars with sub-initiatives listed, (3) Ownership Matrix showing which division leads each pillar, (4) 2025 Success Metrics with measurable KPIs, (5) Key Risks and Mitigation Owners, (6) Parking Lot for items to revisit. Format so all 12 division heads can add their inputs simultaneously.\"",
              fileRef: "03_Zava_Group_Strategy_Framework.docx"
            }
          ]
        },
        {
          tool: "🤖 Word Agent",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Set up a Zava Policy Assistant agent on the handbook",
              prompt: "In Microsoft Word, open 02_Zava_Group_Policy_Handbook.docx. Open the Copilot pane on the right side of the screen. Click the agent builder icon or select Create an agent from the Copilot pane menu. Name the agent Zava Policy Assistant. Set the document scope to this policy handbook. In the Instructions field type: \"Answer questions about Zava Group's internal policies. Always cite the relevant policy section by name and number. If a question falls outside the scope of this handbook, clearly say so and suggest where the person should look.\" Save the agent. Demo immediately: type \"What is Zava Group's policy on accepting gifts from external vendors?\"",
              fileRef: "02_Zava_Group_Policy_Handbook.docx"
            },
            {
              title: "Demo the Policy Assistant — 3 realistic colleague queries",
              prompt: "With the Zava Policy Assistant agent active and scoped to 02_Zava_Group_Policy_Handbook.docx, demonstrate 3 realistic queries a new Zava employee might ask. Query 1: \"I need to bring my personal laptop to a client office to present. Is this permitted under the IT security policy?\" Query 2: \"I accidentally forwarded an internal finance report to an external email address. What do I need to do — is this a reportable incident?\" Query 3: \"Our department wants to engage a freelance graphic designer in Vietnam. What data access restrictions apply under the third-party vendor and PDPA policies?\" Observe how the agent cites specific policy sections for each answer.",
              fileRef: "02_Zava_Group_Policy_Handbook.docx"
            }
          ]
        },
        {
          tool: "🤖 PowerPoint Agent",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Set up a Strategy Briefing agent on the group presentation",
              prompt: "First, create a PowerPoint presentation by asking Copilot to generate slides based on 03_Zava_Group_Strategy_Framework.docx. Save it as Zava_Group_Strategy_2025.pptx. Open the Copilot pane, click Create an agent, name it Zava Strategy Advisor, and scope it to this presentation. In the Instructions field type: \"Answer questions about Zava Group's 2025-2027 strategy. Reference specific slide numbers. Keep answers under 100 words. Do not speculate beyond what is in the presentation.\" Demo immediately: type \"What are the 3 most important strategic priorities for the Zava BPO division in FY2025?\""
            },
            {
              title: "Demo the Strategy Advisor — leadership team queries",
              prompt: "With the Zava Strategy Advisor agent active and scoped to the strategy PowerPoint, ask 3 queries that a division head or Board member would realistically ask. Query 1: \"Which division has been allocated the highest capital expenditure priority for 2025 to 2027?\" Query 2: \"Summarise the key external risks to the group's revenue target and explain how management plans to address them.\" Query 3: \"What does success look like for the digital transformation pillar by end of 2027 — what are the specific KPIs or milestones?\" Show how the agent references specific slides and synthesises answers across the full deck."
            }
          ]
        },
        {
          tool: "🤖 Excel Agent",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Set up a Finance Assistant agent on the group financials",
              prompt: "In Microsoft Excel, open 01_Zava_Group_Financial_Performance.xlsx. Open the Copilot pane on the right. Click Create an agent or use the agent builder icon. Name the agent Zava Finance Assistant. Scope it to this workbook. In the Instructions field type: \"Answer financial questions about Zava Group using data in this workbook only. Always cite the sheet name and row or column reference. Express all amounts in MYR millions unless the user specifies otherwise. If data is not in this workbook, say so.\" Save the agent. Demo immediately: type \"What was the group total revenue in FY2024 and how does it compare to the FY2022 baseline?\"",
              fileRef: "01_Zava_Group_Financial_Performance.xlsx"
            },
            {
              title: "Demo the Finance Assistant — cross-division queries",
              prompt: "With the Zava Finance Assistant agent active and scoped to 01_Zava_Group_Financial_Performance.xlsx, run 3 realistic finance queries from a non-finance colleague. Query 1: \"Which 2 divisions showed declining EBITDA margins in both FY2023 and FY2024 — and by how many percentage points?\" Query 2: \"What is the group total debt as of FY2024 and what is the net debt to EBITDA ratio?\" Query 3: \"If the Financial Services division increases revenue by 10% in FY2025 and all other divisions stay flat, what would the new group total revenue be?\" Demonstrate how colleagues can query a complex spreadsheet in plain English without knowing a single Excel formula.",
              fileRef: "01_Zava_Group_Financial_Performance.xlsx"
            }
          ]
        }
      ]
    },
    {
      id: "banking",
      name: "Banking & Financial Services",
      icon: "🏦",
      color: "#1B4F72",
      accent: "#2980B9",
      company: "Meridian Bank Berhad",
      tagline: "NPL crisis management | BNM Section 47 Direction | Digital transformation | MYR 68.4B assets",
      scenario: "Meridian Bank Berhad (Meridian) is a Malaysian licensed commercial bank with MYR 68.4 billion in total assets and a network of 148 branches nationwide. The bank has received a Section 47 Direction from Bank Negara Malaysia (BNM) requiring a formal NPL Remediation Plan after the personal financing NPL ratio reached 14.2% — four times the 3.5% system-wide BNM threshold. Group CEO Akinlabi Farouq and CFO Hadar Caspit have 30 days to submit a credible remediation plan, prepare for a bilateral meeting with BNM's Supervision Director, and brief the full Board. Digital collections technology, credit scoring model upgrades, and governance strengthening are all on the table.",
      files: ["BNK_01_Meridian_Bank.xlsx", "BNK_02_Meridian_Bank_Strategy.docx", "Email_06_BNM_Regulatory_Correspondence.docx"],
      prompts: [
        {
          tool: "🤖 Copilot Chat (Basic)",
          license: "Free — no M365 license needed",
          account: "Sasha Ouellet — SashaO@ABSx62256373.OnMicrosoft.com",
          prompts: [
            {
              title: "Explain BNM Section 47 Direction in plain English",
              prompt: "Ask Copilot: \"Explain in plain English what Bank Negara Malaysia's Section 47 Direction means for a Malaysian licensed bank. My bank, Meridian Bank Berhad, has received a Section 47 Direction related to our personal financing NPL rate of 14.2%, which is significantly above BNM's 3.5% industry threshold. Explain: (1) What Section 47 legally requires us to do, (2) The timeline BNM typically imposes for remediation plans, (3) The escalation path if we fail to comply, including whether a formal licence review is possible, (4) How this compares to similar recent BNM enforcement actions. Answer as a briefing note for a non-lawyer board member.\""
            },
            {
              title: "What is an NPL ratio and why does 14.2% matter",
              prompt: "Ask Copilot: \"I need to brief Meridian Bank's Board on our NPL situation. Explain: (1) What is a Non-Performing Loan ratio and how is it calculated under BNM's MFRS 9 framework, (2) What is a normal NPL ratio for Malaysian banks — include the BNM system-wide figure and what the best-performing local banks achieve, (3) Why is our 14.2% NPL ratio in the personal financing segment alarming — put this in context against the 3.5% BNM threshold, (4) What operational and regulatory consequences arise once a bank's NPL ratio breaches regulatory thresholds. Use plain language. Avoid jargon. Maximum 250 words with clear numbered sections.\""
            },
            {
              title: "Brief me before the BNM bilateral meeting",
              prompt: "Ask Copilot: \"I am the Group CEO of Meridian Bank Berhad, scheduled for a bilateral meeting with BNM's Bank Supervision Director tomorrow at 2pm. The agenda is our NPL remediation plan submission. Prepare a structured 1-page meeting brief for me covering: (1) The 4 key messages I must land with BNM — confidence in remediation, specific timeline commitments, data governance improvements, and digital collection channel investment; (2) The 3 most challenging questions the BNM supervisor is likely to ask and my recommended answers for each; (3) Tone guidance — assertive, cooperative, or deferential — and why that tone is correct for this meeting. Format as an executive brief I can read in 5 minutes before the meeting.\""
            }
          ]
        },
        {
          tool: "�� Researcher",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Research Malaysian NPL management strategies and BNM enforcement",
              prompt: "In Copilot Chat, switch to the Researcher agent. Upload BNK_02_Meridian_Bank_Strategy.docx. Ask: \"Analyse Meridian Bank's current strategy document and cross-reference with web research. Search the web for: recent BNM enforcement actions and Section 47 Directions issued between 2022 and 2025; NPL remediation strategies used by Malaysian banks with elevated NPL ratios; and digital collections technology platforms deployed by Asian retail banks. What proven approaches — credit scoring model upgrades, digital collection channels, NPL workout units, or portfolio sales — align best with Meridian's current strategic priorities? Present as a 4-column options table: Approach | Evidence of Success | Cost Implication | Meridian Fit Rating.\"",
              fileRef: "BNK_02_Meridian_Bank_Strategy.docx"
            },
            {
              title: "Research digital banking transformation in ASEAN",
              prompt: "In Copilot Chat, switch to the Researcher agent. Ask: \"Search the web for ASEAN digital banking transformation case studies from 2023 to 2025. Focus on: Malaysian banks (CIMB, Maybank, RHB) that have deployed AI-powered credit risk models or digital collections platforms; the ASEAN digital banking licence landscape including Malaysia's licensed digital banks; and BNM's published guidelines on responsible AI use in financial services. Also search for any recent Gartner or McKinsey reports on AI in retail banking in Southeast Asia. Summarise the 5 most actionable technology strategies that Meridian Bank could deploy within 12 months, with citations.\""
            },
            {
              title: "Research MFRS 9 provisioning best practice",
              prompt: "In Copilot Chat, switch to the Researcher agent. Upload BNK_01_Meridian_Bank.xlsx. Ask: \"Review Meridian Bank's financial data, then search the web for current MFRS 9 Expected Credit Loss provisioning methodologies and best practices for Malaysian banks under BNM's Jawi Prudential Standards. Research: how leading Malaysian banks calculate Stage 1, Stage 2, and Stage 3 ECL for personal financing portfolios; recent BNM supervisory expectations letters on provisioning adequacy; and any enforcement actions arising from under-provisioning. What is the likely provision coverage gap for a bank with a 14.2% NPL ratio in personal financing if BNM requires a minimum 80% coverage ratio? Show the MYR calculation.\"",
              fileRef: "BNK_01_Meridian_Bank.xlsx"
            }
          ]
        },
        {
          tool: "📊 Analyst",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Analyse Meridian Bank NPL trends and provision adequacy",
              prompt: "In Copilot Chat, switch to the Analyst agent. Upload BNK_01_Meridian_Bank.xlsx. Ask: \"Analyse the full NPL dataset. For the personal financing portfolio: (1) Calculate the NPL ratio trend from Q1 FY2023 to Q4 FY2024 — is it improving, stable, or deteriorating quarter-on-quarter; (2) Calculate the current provision coverage ratio and identify the additional MYR million provision required to reach BNM's minimum 80% coverage expectation; (3) Identify the 3 customer segments or loan cohorts with the highest NPL rates — segment by income band, loan tenor, and origination channel; (4) Project the NPL ratio for Q2 FY2025 under current collection performance. Format findings as a CEO credit risk briefing with a supporting data table.\"",
              fileRef: "BNK_01_Meridian_Bank.xlsx"
            },
            {
              title: "Model provision scenarios and capital impact",
              prompt: "In Copilot Chat, switch to the Analyst agent. Upload BNK_01_Meridian_Bank.xlsx. Ask: \"Build a provision scenario model for Meridian Bank. Model 3 cases: (1) Base — NPL remains at 14.2%, (2) Recovery — NPL reduces to 8% by Q4 FY2025 through digital collections and portfolio write-offs, (3) Stress — NPL rises to 19% if BNM imposes a lending moratorium. For each scenario calculate: additional provision top-up in MYR millions, impact on pre-tax profit as a percentage, estimated CET1 capital ratio change assuming a 12.5% starting point, and whether the scenario triggers BNM's 3.5% systemic threshold. Output as a 5-column table with a clear recommendation highlighted for the CFO Board pack.\"",
              fileRef: "BNK_01_Meridian_Bank.xlsx"
            },
            {
              title: "Analyse digital banking KPI performance vs market",
              prompt: "In Copilot Chat, switch to the Analyst agent. Upload BNK_01_Meridian_Bank.xlsx. Ask: \"Analyse Meridian Bank's digital banking performance metrics against the industry benchmarks provided. Calculate: (1) Digital channel adoption rate versus the Malaysian banking industry average of 78%; (2) Mobile app monthly active user growth rate from FY2022 to FY2024; (3) Cost-to-income ratio for digital versus branch channels — what is the cost savings potential if the digital mix increases from current levels to 75%; (4) Customer acquisition cost via digital versus branch, and the payback period. Express all improvements as percentage gains and MYR savings. Present as a digital transformation investment case summary.\"",
              fileRef: "BNK_01_Meridian_Bank.xlsx"
            }
          ]
        },
        {
          tool: "📊 Copilot in Excel",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Summarise the Meridian Bank NPL workbook instantly",
              prompt: "Open BNK_01_Meridian_Bank.xlsx. Ask Copilot: \"Give me an immediate plain-English executive summary of this entire workbook. What is the current NPL ratio in the personal financing segment? Which loan cohort or origination year has the highest NPL concentration? What is the total loan portfolio size in MYR billions, and what is the overall bank NPL ratio including all segments? Identify the 2 most concerning trends visible in any sheet of this workbook. Format: 2-sentence overview, then a watch-list of 3 specific data concerns with sheet name and row number for each.\"",
              fileRef: "BNK_01_Meridian_Bank.xlsx"
            },
            {
              title: "Build NPL trend chart for Board presentation",
              prompt: "Open BNK_01_Meridian_Bank.xlsx and navigate to the NPL Trend sheet. Ask Copilot: \"Create a line chart showing the quarterly NPL ratio for the personal financing segment from Q1 FY2023 to Q4 FY2024. Add a horizontal reference line at 3.5% labelled BNM Threshold. Use red for the NPL ratio line and dashed orange for the BNM threshold line. Add data labels on the NPL ratio line showing the exact percentage at each quarter. Chart title: Meridian Bank — Personal Financing NPL Trend vs BNM Threshold. This chart will be embedded in the BNM remediation submission.\"",
              fileRef: "BNK_01_Meridian_Bank.xlsx"
            },
            {
              title: "Add provision coverage formula with scenario toggle",
              prompt: "Open BNK_01_Meridian_Bank.xlsx. Navigate to the Provision Analysis sheet. Ask Copilot: \"Add a formula in a new column called Required Additional Provision. The formula should calculate the difference between (Outstanding NPL Balance × Target Coverage Ratio 80%) and the Existing Provision Balance for each loan segment row. If the result is negative — meaning we are already over-provisioned — show zero. Apply red number formatting to cells where additional provision exceeds MYR 50 million. Tell me which segment requires the largest additional provision and the total group provision top-up in MYR millions.\"",
              fileRef: "BNK_01_Meridian_Bank.xlsx"
            },
            {
              title: "Natural language query — key risk ratios",
              prompt: "Open BNK_01_Meridian_Bank.xlsx. Ask Copilot: \"Without me navigating the sheets myself, answer these 4 questions from the data in this workbook: (1) What is the Loan-to-Deposit ratio as of the latest available quarter and is it above or below the BNM guideline of 90%; (2) What is the bank's net interest margin compared to the previous year; (3) What percentage of total loans does the personal financing segment represent; (4) What is the loan growth rate in FY2024 compared to FY2023. Present as a 2-column table: Question and Answer. Cite the exact sheet and cell for each answer so I can verify.\"",
              fileRef: "BNK_01_Meridian_Bank.xlsx"
            }
          ]
        },
        {
          tool: "📝 Copilot in Word",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Summarise BNM remediation strategy into action brief",
              prompt: "Open BNK_02_Meridian_Bank_Strategy.docx. Ask Copilot: \"Summarise this strategy document specifically focusing on Meridian Bank's NPL remediation plan. Extract: (1) The stated root causes of the NPL spike — list all that are explicitly named; (2) The 5 remediation workstreams with their specific milestones and Q-by-Q timeline; (3) The investment committed in MYR millions for digital collections and credit scoring upgrade; (4) The Board-level governance mechanism being put in place to oversee the plan; (5) The single most credible evidence that the bank expects this plan to work. Format as a 2-page Board executive summary with numbered headings. Maximum 500 words.\"",
              fileRef: "BNK_02_Meridian_Bank_Strategy.docx"
            },
            {
              title: "Draft BNM Section 47 remediation submission cover letter",
              prompt: "Open a new Word document. Ask Copilot: \"Draft the formal cover letter for Meridian Bank Berhad's NPL Remediation Plan submission to Bank Negara Malaysia's Supervision Department, as required under the Section 47 Direction received 15 April 2025. The letter should: be dated 30 April 2025; be signed by Akinlabi Farouq, Group CEO; formally acknowledge the Section 47 Direction and its required submission deadline; confirm that the accompanying remediation plan addresses all 4 supervisory concerns raised in BNM's examination report; commit to quarterly NPL reduction milestones of 12.5%, 10.8%, 8.2%, and 6.0% for Q1 through Q4 FY2025; and request a bilateral presentation meeting. Formal regulatory correspondence tone. 350 words maximum.\""
            },
            {
              title: "Rewrite the credit risk policy for operational staff",
              prompt: "Open BNK_02_Meridian_Bank_Strategy.docx and locate the Credit Risk Governance section. Ask Copilot: \"Rewrite this credit risk governance section in plain, operational language suitable for a Meridian Bank branch credit officer or loan processing staff member — not a risk professional or lawyer. Remove all regulatory references and replace them with practical steps. Add a decision tree: if a customer's debt service ratio exceeds a threshold, what does the credit officer do next? Limit the rewritten section to 400 words. Use numbered steps and a simple table where needed.\"",
              fileRef: "BNK_02_Meridian_Bank_Strategy.docx"
            },
            {
              title: "Convert rough risk committee notes to formal minutes",
              prompt: "Open a new Word document. Paste these rough notes: \"Risk Comm 5 May 2025. CEO, CFO, CRO, GC, 2 NEDs. BNM bilateral set for 20 May. NPL remediation plan to be signed off by 10 May — CFO owns. Digital collections go-live delayed 2 weeks to 28 May — IT Director to resolve. SWIFT CLAIM project Phase 2 approved. Next meeting 2 June.\" Ask Copilot: \"Format these notes as formal Risk Committee minutes for Meridian Bank Berhad. Include: formal heading block with date, venue, chair, and attendees table; numbered agenda items with resolution status; a decisions and resolutions table; action items table with Owner and Deadline; and circulation list. Board governance standard. 400 words maximum.\""
            }
          ]
        },
        {
          tool: "🎯 Copilot in PowerPoint",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Create NPL crisis update deck for BNM bilateral",
              prompt: "Open a new PowerPoint. Ask Copilot: \"Create a 7-slide NPL remediation presentation for Meridian Bank Berhad's bilateral meeting with Bank Negara Malaysia Supervision Department on 20 May 2025. Slide 1: Title and purpose. Slide 2: Current NPL situation — 14.2% personal financing NPL vs 3.5% BNM threshold, with timeline of escalation. Slide 3: Root causes — top 3 identified root causes with evidence. Slide 4: Remediation plan — 5 workstreams with owners and milestones. Slide 5: NPL reduction timeline — quarterly milestones Q1 to Q4 FY2025. Slide 6: Governance framework — monthly Board NPL Committee oversight. Slide 7: Request from BNM — specific ask or commitment. Dark blue Meridian Bank theme, professional. No clipart.\""
            },
            {
              title: "Generate digital banking transformation roadmap slides",
              prompt: "Open a new PowerPoint. Ask Copilot: \"Create a 5-slide technology transformation roadmap for Meridian Bank to support NPL remediation. Focus on the 3 technology investments: (1) AI-powered credit scoring model using bureau and behavioural data, (2) Digital collections platform with automated early warning system, (3) Mobile-first digital banking channel to reduce acquisition cost. Each technology gets one slide showing: business problem addressed, solution overview, investment in MYR millions, expected NPL impact, and go-live timeline. Slide 5: consolidated roadmap Gantt chart from May to December 2025. Clean, modern design suitable for a technology committee presentation. Navy blue and white.\""
            },
            {
              title: "Add competitive benchmarking slide",
              prompt: "In an open Meridian Bank PowerPoint, add a new slide after the remediation plan slide. Ask Copilot: \"Create a banking competitive landscape benchmarking slide showing Meridian Bank's NPL ratio at 14.2% compared to Maybank, CIMB, RHB, and the BNM industry average of approximately 1.8%. Use a horizontal bar chart with Meridian's bar in red and others in navy blue. Add a vertical line at the 3.5% BNM threshold. Title: NPL Ratio Comparison — Meridian Bank vs Malaysian Banking System. Include a 2-sentence text box noting that Meridian's remediation target is to return to below 6% by Q4 FY2025 and below 3.5% by FY2026.\""
            }
          ]
        },
        {
          tool: "📧 Copilot in Outlook",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Triage NPL escalation email thread for CEO",
              prompt: "Open Outlook and open Email_06_BNM_Regulatory_Correspondence.docx — copy the content into a draft or open the forwarded email thread. Click the Copilot summarise icon. Ask: \"Summarise this BNM regulatory correspondence thread for our CEO. I need: (1) The specific regulatory concern BNM has raised about Meridian Bank and what they are requiring us to do; (2) The hard deadline for the remediation plan submission and whether we are on track; (3) Any BNM language indicating escalation risk — such as references to further supervisory action, licence conditions, or an examination; (4) The 3 most urgent internal actions that must happen before the BNM bilateral on 20 May. Maximum 200 words.\"",
              fileRef: "Email_06_BNM_Regulatory_Correspondence.docx"
            },
            {
              title: "Draft CEO update to the Board on NPL crisis",
              prompt: "In Outlook, start a new email to board members. Ask Copilot: \"Draft a formal email from Akinlabi Farouq, Group CEO of Meridian Bank Berhad, to the full Board of Directors providing a crisis update on the BNM Section 47 Direction received 15 April 2025. The email should: (1) State the facts clearly — 14.2% NPL in personal financing, BNM threshold 3.5%, Direction received, submission due 30 April; (2) Confirm the key steps already taken — emergency Risk Committee convened 17 April, external counsel engaged, remediation plan drafted; (3) Communicate the bilateral meeting with BNM scheduled for 20 May 2025; (4) Request Board approval for an emergency meeting on 8 May to review and approve the remediation plan. Formal CEO-to-Board tone. 350 words.\""
            },
            {
              title: "Copilot coaching on NPL remediation email to BNM",
              prompt: "In Outlook, type a rough first draft: \"Dear BNM, we acknowledge your direction and we are working on it. We will send the NPL plan on time and hope you will be satisfied with our response. Our CEO will call to discuss. Regards, Meridian Bank.\" Click the Copilot coaching icon. Ask: \"I am a Group CEO writing to Bank Negara Malaysia's Supervision Director. Score this draft on 3 dimensions: (1) Regulatory tone — is it appropriately formal and deferential without being subservient; (2) Commitment specificity — does it make clear, measurable commitments; (3) Risk signalling — does it inadvertently suggest non-compliance risk. Then provide a fully rewritten version at CEO-to-regulator standard.\""
            }
          ]
        },
        {
          tool: "🎙 Copilot in Teams",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Recap emergency NPL crisis management meeting",
              prompt: "Open an existing Teams meeting recap that was recorded — ideally a project review or executive meeting from your calendar. In the Copilot recap pane, ask: \"I am the Meridian Bank Group CFO and I missed this meeting because I was on a call with BNM. Catch me up with a structured 5-point brief: (1) What triggered the meeting and what was the stated agenda; (2) What decisions were made or commitments given — list each with the name of the person who committed; (3) What agenda items were left unresolved or deferred to the next meeting; (4) Any specific action assigned to the CFO or Finance team; (5) The single most urgent thing I need to do before close of business today.\""
            },
            {
              title: "Extract BNM remediation plan action register from meeting",
              prompt: "Open an existing recorded Teams meeting recap from your calendar — a governance, committee, or project meeting. In the Copilot recap pane, ask: \"Extract all action items from this meeting and format as a formal action register table with these columns: Action ID (sequential number); Action Description (what must be done exactly); Owner (person responsible, full name); Deadline (specific date or business days); Priority (Critical, High, or Normal); and Status (Not Started at this point). If more than 10 items exist, highlight in bold the 3 items with the nearest deadlines. This action register will be circulated to the full Meridian Bank Risk Committee within the hour.\""
            },
            {
              title: "Generate BNM bilateral meeting pre-brief from prep meeting recap",
              prompt: "Open an existing recorded Teams meeting recap from your calendar — a preparation or planning meeting. In the Copilot recap panel, ask: \"Using the discussion and decisions from this meeting, draft a structured pre-brief memo for the bilateral meeting with Bank Negara Malaysia's Supervision Department. Format as: (1) Meeting Objective — 1 sentence; (2) Key Messages — 3 bullet points that Meridian's CEO must land with BNM; (3) Supporting Evidence Available — financial data and milestones we have ready to present; (4) Known BNM Concerns to Address — 2 to 3 anticipated questions and our prepared response for each; (5) Red Lines — what we are not prepared to commit to in this meeting and why. Tone: formal, strategic. Under 300 words.\""
            }
          ]
        },
        {
          tool: "📓 Copilot Notebook",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Full BNM submission brief from 3 source documents",
              prompt: "Go to copilot.microsoft.com and click Notebook. Upload 3 files: BNK_01_Meridian_Bank.xlsx, BNK_02_Meridian_Bank_Strategy.docx, and Email_06_BNM_Regulatory_Correspondence.docx. In the Instructions box type: \"Using all 3 uploaded files together, prepare a comprehensive BNM submission brief for Meridian Bank's CEO. Synthesise the financial data, the current strategy, and the regulatory correspondence into: (1) A 3-sentence executive situation statement — current NPL position, what BNM has formally required, and submission deadline; (2) A 5-point remediation plan summary with specific Q-by-Q NPL targets for FY2025; (3) A 3-point pre-bilateral talking track for the CEO; (4) Any gaps between the strategy document and the remediation commitments implied by the regulatory correspondence.\"",
              fileRef: "BNK_01_Meridian_Bank.xlsx, BNK_02_Meridian_Bank_Strategy.docx, Email_06_BNM_Regulatory_Correspondence.docx"
            },
            {
              title: "Board NPL governance and evidence pack analysis",
              prompt: "Go to Copilot Notebook. Upload BNK_02_Meridian_Bank_Strategy.docx and Email_06_BNM_Regulatory_Correspondence.docx. In the Instructions box type: \"I am an independent non-executive director of Meridian Bank Berhad. I need to fulfil my governance obligations around this NPL crisis. Using both documents, answer: (1) Is the remediation plan specific enough to satisfy a BNM supervisor — identify any vague commitments that need quantifying; (2) What Board-level governance mechanism is in place to monitor monthly NPL progress — is it adequate; (3) Does the strategy document address the 4 root causes identified in BNM's examination — cross-reference each root cause to the remediation workstream; (4) What would I, as an NED, formally request at the Board meeting on 8 May to strengthen oversight?\"",
              fileRef: "BNK_02_Meridian_Bank_Strategy.docx, Email_06_BNM_Regulatory_Correspondence.docx"
            }
          ]
        },
        {
          tool: "🤝 Cowork (Pages)",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Convert NPL analysis into collaborative remediation tracker",
              prompt: "In Copilot Chat, upload BNK_01_Meridian_Bank.xlsx and ask for an NPL segment analysis. When Copilot responds, click Open in Copilot Pages. In the Pages canvas ask: \"Reorganise this NPL analysis into a live remediation tracker for the Meridian Bank Risk Committee. Structure as: (1) NPL Dashboard — key metrics from the financial data with traffic-light status; (2) Workstream Tracker — 5 remediation workstreams with owner, current status, and next milestone; (3) Risk Flags — 3 items that could derail the remediation timeline; (4) BNM Reporting Calendar — next 4 reporting milestones with dates. Format so the Risk Committee can update this page collaboratively each week.\"",
              fileRef: "BNK_01_Meridian_Bank.xlsx"
            },
            {
              title: "Build a joint NPL remediation planning canvas",
              prompt: "In Copilot Chat, upload BNK_02_Meridian_Bank_Strategy.docx and ask Copilot to summarise the remediation plan. When Copilot responds, click Open in Copilot Pages. Ask: \"Expand this remediation plan summary into a collaborative working canvas for the Meridian Bank NPL Remediation Task Force — 8 members including CEO, CFO, CRO, IT Director, and 4 workstream leads. Structure as: (1) Problem Statement and Regulatory Context; (2) 5 Workstreams with sub-tasks and owner assignments; (3) Week-by-week milestone calendar from May to December 2025; (4) Decision Log for items escalated to Board; (5) Open Questions parking lot. Format for shared editing by all 8 task force members.\"",
              fileRef: "BNK_02_Meridian_Bank_Strategy.docx"
            }
          ]
        },
        {
          tool: "🤖 Word Agent",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Set up a Meridian Bank Strategy Advisor agent",
              prompt: "Open BNK_02_Meridian_Bank_Strategy.docx in Microsoft Word. In the Copilot pane, click Create an agent. Name it Meridian Strategy Advisor. Scope it to this document. In the Instructions field type: \"Answer questions about Meridian Bank's current strategy and NPL remediation plan. Always cite the relevant section of the document. Keep answers under 150 words. If a question cannot be answered from this document, say so and recommend who to ask.\" Save and demo immediately: type \"What is the target NPL ratio that Meridian commits to achieving by end of FY2025, and what are the 3 main workstreams to get there?\"",
              fileRef: "BNK_02_Meridian_Bank_Strategy.docx"
            },
            {
              title: "Demo the Meridian Strategy Advisor — 3 banking queries",
              prompt: "With the Meridian Strategy Advisor agent active and scoped to BNK_02_Meridian_Bank_Strategy.docx, ask 3 realistic questions a Board member or regulator might ask. Query 1: \"What investment is committed to the digital collections platform and what NPL reduction does management expect it to deliver?\" Query 2: \"Who is the Board-level owner of the NPL remediation programme and what is the oversight governance cadence?\" Query 3: \"If the digital collections platform launch is delayed by 6 weeks, does the strategy document have a contingency or fallback plan?\" Observe how the agent synthesises answers from different sections of a dense 40-page strategy document in seconds.",
              fileRef: "BNK_02_Meridian_Bank_Strategy.docx"
            }
          ]
        },
        {
          tool: "🤖 PowerPoint Agent",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Set up BNM Presentation Agent on remediation deck",
              prompt: "Create or open the Meridian Bank NPL remediation PowerPoint — either the one generated in the PPT demo or saved from a prior session. Save as Meridian_Bank_BNM_Remediation_2025.pptx. Open the Copilot pane, click Create an agent, name it BNM Prep Coach, and scope it to this presentation. In the Instructions field type: \"Answer questions about the content of Meridian Bank's BNM remediation presentation. Cite slide numbers. Keep answers under 100 words.\" Demo immediately: type \"Which slide covers the 5 remediation workstreams and what are the committed completion dates for each?\""
            },
            {
              title: "Demo the BNM Prep Coach — pre-bilateral preparation",
              prompt: "With the BNM Prep Coach agent active and scoped to the remediation PowerPoint, ask 3 questions that mimic how a CEO would prepare for a regulator meeting. Query 1: \"If BNM asks why NPL rose from 3.5% to 14.2% — which slide has the most credible explanation?\" Query 2: \"What is our strongest piece of evidence that the remediation plan is already working — which slide should I turn to?\" Query 3: \"BNM might ask if we have considered external portfolio sales or workout unit options — is that addressed anywhere in the deck?\" Show how the agent turns a 35-slide deck into an intelligent preparation tool."
            }
          ]
        },
        {
          tool: "🤖 Excel Agent",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Set up a Credit Risk Dashboard agent on Meridian Bank workbook",
              prompt: "Open BNK_01_Meridian_Bank.xlsx in Excel. In the Copilot pane, click Create an agent. Name it Meridian Credit Risk Advisor. Scope it to this workbook. Instructions: \"Answer questions about Meridian Bank's financial and credit risk data. Always cite the sheet name. Express amounts in MYR millions. Highlight if any number exceeds a regulatory threshold.\" Demo immediately: type \"What is the current Stage 3 NPL balance in MYR millions and what is the corresponding provision coverage ratio?\"",
              fileRef: "BNK_01_Meridian_Bank.xlsx"
            },
            {
              title: "Demo the Credit Risk Advisor — regulator Q&A simulation",
              prompt: "With the Meridian Credit Risk Advisor agent active and scoped to BNK_01_Meridian_Bank.xlsx, simulate the data questions a BNM examiner would ask. Query 1: \"What is the year-on-year change in the personal financing NPL ratio from FY2022 to FY2024 — is the trend worsening?\" Query 2: \"What is the total provision shortfall in MYR millions if BNM requires 80% coverage on all Stage 3 loans?\" Query 3: \"What percentage of total loans are classified as Stage 2 under MFRS 9, and has this percentage increased since last year?\" Show how colleagues can interrogate complex financial data using plain English during a live regulator meeting.",
              fileRef: "BNK_01_Meridian_Bank.xlsx"
            }
          ]
        }
      ]
    },
    {
      id: "healthcare",
      name: "Healthcare",
      icon: "🏥",
      color: "#1A6B4A",
      accent: "#27AE60",
      company: "Apex Health Group",
      tagline: "JCI accreditation | Nurse attrition 18.4% | Medical tourism MYR 532M | 12 hospitals",
      scenario: "Apex Health Group (Apex) is Malaysia's third-largest private healthcare group operating 12 hospitals with a combined 2,800 beds and MYR 2.84 billion in annual revenue. Three priority challenges dominate the FY2025 leadership agenda: (1) The flagship KL hospital's JCI accreditation survey is in 9 months and a critical nurse-to-patient ratio gap exists; (2) Registered nurse attrition has reached 18.4% — above the 12% target — driving up agency costs and threatening care continuity; (3) The 6-week oncology appointment wait time is causing revenue leakage to competitors and creating patient safety risk. CEO Rania Aziz and Group CMO Dr Priya Nadarajan need Copilot to accelerate strategy analysis, workforce modelling, regulatory preparation, and clinical team communication across 12 hospitals.",
      files: ["HC_01_Apex_Health_Group.xlsx", "HC_02_Apex_Health_Strategy.docx", "Email_03_MOH_Audit_Notification.docx"],
      prompts: [
        {
          tool: "🤖 Copilot Chat (Basic)",
          license: "Free — no M365 license needed",
          account: "Sasha Ouellet — SashaO@ABSx62256373.OnMicrosoft.com",
          prompts: [
            {
              title: "What does JCI accreditation require for a hospital?",
              prompt: "Ask Copilot: \"Explain what Joint Commission International (JCI) accreditation requires for an acute care hospital in Malaysia. My organisation is Apex Health Group, operating 12 hospitals with a flagship 520-bed tertiary hospital in Kuala Lumpur. Specifically cover: (1) The 6 main JCI accreditation standards chapters and what each evaluates in clinical operations, (2) The most common JCI deficiency findings at Malaysian hospitals based on published audit data, (3) The approximate timeline from application to full accreditation for a hospital of 520 beds, (4) How JCI accreditation supports Malaysia's medical tourism revenue — Apex currently earns MYR 532 million from medical tourism. Maximum 250 words, structured with clear headings.\""
            },
            {
              title: "Brief me on the nurse attrition problem before the CHRO call",
              prompt: "Ask Copilot: \"I am the Group CEO of Apex Health Group. I have a call with our Group CHRO in 20 minutes about our 18.4% registered nurse attrition rate, which is significantly above the Malaysian healthcare sector average. Before the call prepare a structured brief covering: (1) The financial cost of 18.4% attrition across 12 hospitals — include cost of agency nurses, overtime, and new hire training, assuming 1,500 registered nurses total; (2) The 3 most common root causes of high nurse attrition in Malaysian private hospitals based on published research; (3) The 3 most effective retention strategies used by comparable ASEAN private hospital groups; (4) The single most important question I should ask the CHRO during the call. Maximum 200 words.\""
            },
            {
              title: "Explain the 6-week oncology wait-time clinical risk",
              prompt: "Ask Copilot: \"Explain the clinical and patient safety implications of a 6-week oncology appointment wait time for a patient referred for suspected colorectal cancer. Cover: (1) The clinical staging risk — what is the probability of disease progression from Stage II to Stage III in a 6-week window for a typical colorectal cancer presentation; (2) The patient safety and medico-legal exposure for the hospital if delayed diagnosis leads to a worse outcome; (3) The KKM and MOH Private Healthcare Facilities Act 1998 obligations for timely specialist access in Malaysia; (4) The revenue and market share risk if patients with private insurance seek faster access at competing hospitals. Maximum 200 words, clinical and business angles equally weighted.\""
            }
          ]
        },
        {
          tool: "�� Researcher",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Research JCI accreditation best practices and gaps",
              prompt: "In Copilot Chat, switch to the Researcher agent. Upload HC_02_Apex_Health_Strategy.docx. Ask: \"Review Apex Health Group's strategy document, then search the web for: current JCI International Patient Safety Goals for 2024-2025; the most common JCI deficiency findings for Malaysian and Southeast Asian hospitals in recent accreditation cycles; and benchmarks for nurse-to-patient ratios in JCI-accredited acute care hospitals. Cross-reference with Apex's current strategy — which JCI standards areas are most at risk given the 18.4% nurse attrition rate and 6-week oncology wait time? Present as a gap analysis table with Apex's current status, JCI standard, and a remediation recommendation for each gap.\"",
              fileRef: "HC_02_Apex_Health_Strategy.docx"
            },
            {
              title: "Research medical tourism trends in Malaysia and ASEAN",
              prompt: "In Copilot Chat, switch to the Researcher agent. Ask: \"Search the web for the current state of Malaysia's medical tourism industry. Find: the latest Tourism Malaysia and MHTC medical tourist arrival and revenue statistics for 2024 and 2025; the top 5 competitor countries for medical tourism in ASEAN and their pricing advantage; trends in specific high-revenue clinical specialties attracting international patients — orthopedics, cardiology, oncology, and fertility; and any government incentives or policies under Malaysia MADANI supporting medical tourism growth. Apex Health Group earns MYR 532 million from medical tourism currently. What is the realistic 5-year market growth opportunity? Cite all sources with URLs.\""
            },
            {
              title: "Research nurse retention strategies in private healthcare",
              prompt: "In Copilot Chat, switch to the Researcher agent. Upload HC_01_Apex_Health_Group.xlsx. Ask: \"Review the Apex Health HR data, then search the web for evidence-based nurse retention strategies used by top-performing private hospital groups in ASEAN and Australia. Specific search areas: flexible rostering and self-scheduling technology; structured career ladder programmes for RNs at private hospitals in Malaysia; the impact of nurse-to-patient ratio mandates on retention; and any published data on agency nurse costs versus staff nurse costs in Malaysian healthcare. Given Apex's 18.4% attrition across 1,500 nurses and an estimated replacement cost of MYR 28,000 per nurse, calculate the annual attrition cost and expected savings from reducing attrition to 12%.\"",
              fileRef: "HC_01_Apex_Health_Group.xlsx"
            }
          ]
        },
        {
          tool: "📊 Analyst",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Analyse Apex Health Group financial and clinical KPIs",
              prompt: "In Copilot Chat, switch to the Analyst agent. Upload HC_01_Apex_Health_Group.xlsx. Ask: \"Analyse the full Apex Health Group dataset. Calculate: (1) Revenue per hospital for the 12 hospitals — which 3 hospitals contribute the highest revenue and which 2 are underperforming vs the MYR 236 million group average; (2) The correlation between bed occupancy rate and EBITDA margin across hospitals — is there a threshold occupancy level where profitability improves significantly; (3) Medical tourism revenue as a percentage of total MYR 2.84 billion group revenue, and the implied revenue impact if medical tourism grows 15% in FY2025; (4) The workforce cost as a percentage of revenue — compare the 3 highest-attrition hospitals versus the 3 lowest. Format as a CEO clinical and financial dashboard with 5 key insights.\"",
              fileRef: "HC_01_Apex_Health_Group.xlsx"
            },
            {
              title: "Analyse oncology wait time and capacity utilisation",
              prompt: "In Copilot Chat, switch to the Analyst agent. Upload HC_01_Apex_Health_Group.xlsx. Ask: \"Analyse the oncology and specialist capacity data in this workbook. Identify: (1) The current oncology appointment wait time by hospital — which hospitals have the worst delays; (2) The consultant oncologist utilisation rate — are there specific clinicians or time slots with low utilisation while overall wait time is 6 weeks; (3) The revenue lost per week due to the 6-week wait — if Apex loses 15% of referred oncology patients to competitors because of wait time, calculate the annual revenue impact at the hospital average revenue per oncology case; (4) The additional number of oncology consultation slots needed per week to reduce wait time to 2 weeks. Present as a capacity optimisation recommendation.\"",
              fileRef: "HC_01_Apex_Health_Group.xlsx"
            },
            {
              title: "Model nurse attrition cost and retention ROI",
              prompt: "In Copilot Chat, switch to the Analyst agent. Upload HC_01_Apex_Health_Group.xlsx. Ask: \"Build a nurse attrition cost model. Inputs: 1,500 registered nurses total across Apex Health Group, current attrition rate 18.4%, estimated replacement cost MYR 28,000 per nurse including agency fees, overtime, and new hire training. Calculate: (1) Current annual attrition cost in MYR millions, (2) Cost if attrition reduces to 12% through a nurse retention programme costing MYR 2.5 million per year — net savings, (3) Breakeven point in months for the retention programme investment, (4) The impact on nurse-to-patient ratio stability and JCI accreditation readiness if attrition drops to 12%. Format as a CFO investment case: investment, savings, payback period, and strategic benefit.\"",
              fileRef: "HC_01_Apex_Health_Group.xlsx"
            }
          ]
        },
        {
          tool: "📊 Copilot in Excel",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Instant hospital performance dashboard summary",
              prompt: "Open HC_01_Apex_Health_Group.xlsx. Ask Copilot: \"Give me a plain-English executive summary of all 12 Apex Health hospitals. Which hospital has the highest bed occupancy rate? Which has the worst nurse attrition? Which has the highest medical tourism revenue? Flag any hospital where either EBITDA margin is below 10% or nurse attrition is above 25%. Also tell me: what is the group-wide average occupancy rate compared to the 85% industry benchmark, and what does the current trend suggest about whether Apex will meet its FY2025 MYR 2.84 billion revenue target? Format: 3-sentence overview, then 4 specific flagged findings with sheet and row reference.\"",
              fileRef: "HC_01_Apex_Health_Group.xlsx"
            },
            {
              title: "Add nurse attrition cost column with conditional formatting",
              prompt: "Open HC_01_Apex_Health_Group.xlsx. Navigate to the HR and Workforce sheet. Ask Copilot: \"Add a new column called Annual Attrition Cost MYR. The formula should multiply the number of registered nurses in each hospital by the attrition rate for that hospital, then multiply by MYR 28,000 replacement cost per nurse. Apply conditional formatting: red fill for hospitals where annual attrition cost exceeds MYR 4 million; amber for MYR 2 to 4 million; green for under MYR 2 million. Tell me which hospital has the highest absolute attrition cost and the total group attrition cost in MYR millions.\"",
              fileRef: "HC_01_Apex_Health_Group.xlsx"
            },
            {
              title: "Create hospital EBITDA margin comparison chart",
              prompt: "Open HC_01_Apex_Health_Group.xlsx. Ask Copilot: \"Create a horizontal bar chart showing EBITDA margin percentage for all 12 Apex Health hospitals sorted from highest to lowest margin. Use green fill for hospitals above 15% EBITDA margin, amber for 10 to 15%, and red for below 10%. Add a vertical reference line at 15% labelled Target Margin. Include the hospital name and exact EBITDA margin percentage on each bar. Chart title: Apex Health Group — Hospital EBITDA Margin FY2024. This chart will be used in the Group CFO's investor relations presentation.\"",
              fileRef: "HC_01_Apex_Health_Group.xlsx"
            },
            {
              title: "Natural language query — medical tourism revenue analysis",
              prompt: "Open HC_01_Apex_Health_Group.xlsx. Ask Copilot: \"Without navigating sheets yourself, answer these questions: (1) What is the total medical tourism revenue across all 12 hospitals and which single hospital generates the most — express as both MYR million and percentage of that hospital's total revenue; (2) What is the average medical tourist spend per visit compared to a domestic patient visit; (3) Which clinical specialty generates the highest medical tourism revenue — orthopedics, cardiology, or oncology; (4) If Apex invests MYR 3 million in a dedicated international patient concierge service and this drives a 10% uplift in medical tourism revenue, what is the payback period in months? Present as a 2-column answer table.\"",
              fileRef: "HC_01_Apex_Health_Group.xlsx"
            }
          ]
        },
        {
          tool: "📝 Copilot in Word",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Summarise Apex Health strategy into a Board pre-read",
              prompt: "Open HC_02_Apex_Health_Strategy.docx. Ask Copilot: \"Summarise this strategy document into a 1-page Board pre-read memo for Apex Health Group's Board of Directors. Focus on: (1) The 3 most material challenges — nurse attrition 18.4%, oncology wait time 6 weeks, and JCI accreditation timeline; (2) The 3 growth opportunities — medical tourism expansion, new cancer centre launch, digital health technology; (3) Capital allocation requested for FY2025 and the expected financial returns; (4) The 2 most critical Board decisions required. Write in formal Board memo style. Non-executive directors are the audience. Maximum 400 words. Use clear numbered headings and bullet points.\"",
              fileRef: "HC_02_Apex_Health_Strategy.docx"
            },
            {
              title: "Draft nurse retention action plan document",
              prompt: "Open a new Word document. Ask Copilot: \"Draft a formal 400-word Nurse Retention and Workforce Stability Action Plan for Apex Health Group covering 12 hospitals with 1,500 registered nurses and a current attrition rate of 18.4% versus the 12% target. The plan must include: (1) Problem Statement — business impact of 18.4% attrition including financial cost and JCI accreditation risk; (2) Root Cause Analysis — top 3 identified causes with brief evidence; (3) Three Retention Initiatives with owner, investment required, and 12-month target; (4) Governance — how the Group CHRO will monitor monthly progress; (5) Success Metrics — what 12-month success looks like in measurable terms. Format as a formal internal governance document.\""
            },
            {
              title: "Rewrite the JCI Accreditation readiness section for ward staff",
              prompt: "Open HC_02_Apex_Health_Strategy.docx. Locate the JCI Accreditation Readiness section. Ask Copilot: \"Rewrite this JCI accreditation readiness section in plain English for a ward nurse with 3 years of experience — not a quality or compliance professional. Replace all JCI standards codes and acronyms with plain-language descriptions of what staff must actually do on the ward. Add a 3-item daily checklist at the end that a nurse can follow to stay compliant with the most commonly assessed JCI standards: patient identification, medication safety, and handover communication. Maximum 300 words. The tone should be supportive and practical, not threatening.\"",
              fileRef: "HC_02_Apex_Health_Strategy.docx"
            },
            {
              title: "Draft oncology wait time improvement memo",
              prompt: "Open a new Word document. Ask Copilot: \"Draft a formal memo from Dr Priya Nadarajan, Group Chief Medical Officer, to all Head of Oncology Specialists across Apex Health Group's 12 hospitals. The memo addresses the critical issue of 6-week oncology appointment wait times and the patient safety, accreditation, and revenue risks this creates. The memo should: (1) State the current position clearly — 6-week average wait, JCI standard expectation of under 2 weeks, and revenue leakage estimate; (2) Require each hospital to submit a capacity plan within 14 days showing how they will reduce wait time to 2 weeks; (3) Announce a group-wide oncology capacity working group meeting on 15 June 2025; (4) Note that consultant locum appointments have been pre-approved if required. Formal medical leadership style.\""
            }
          ]
        },
        {
          tool: "🎯 Copilot in PowerPoint",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Create investor relations presentation for Apex Health",
              prompt: "Open a new PowerPoint. Ask Copilot: \"Create a 7-slide investor relations presentation for Apex Health Group, a Malaysian private healthcare group with 12 hospitals and MYR 2.84 billion in annual revenue. Slide 1: Apex Health Group — FY2024 Performance Overview with date. Slide 2: Group Highlights — revenue MYR 2.84B, 12 hospitals, medical tourism MYR 532M. Slide 3: Clinical and Operational KPIs — bed occupancy, patient volumes, key quality metrics. Slide 4: Strategic Priorities FY2025-2027. Slide 5: Growth Opportunities — medical tourism expansion, cancer centre, digital health. Slide 6: Challenges and Mitigation — nurse attrition, JCI accreditation, oncology capacity. Slide 7: FY2025 Guidance and Investor Ask. Clean healthcare blue and white theme, no clipart.\""
            },
            {
              title: "Generate JCI accreditation readiness update deck",
              prompt: "Open a new PowerPoint. Ask Copilot: \"Create a 5-slide JCI Accreditation Readiness Update presentation for the Apex Health Group Quality Committee. Slide 1: JCI Accreditation — Timeline and What is at Stake. Slide 2: Current Readiness Assessment by Standards Chapter — use a traffic light table. Slide 3: Top 3 Priority Gaps — with specific remediation actions and owners for each. Slide 4: Workforce Impact — how the 18.4% nurse attrition affects JCI standards compliance, particularly staffing ratio requirements. Slide 5: 90-Day Sprint Plan to close the critical gaps before the mock survey. Use clean healthcare white and teal design. One key takeaway per slide.\""
            },
            {
              title: "Add medical tourism competitive landscape slide",
              prompt: "In an open Apex Health PowerPoint, place cursor on a new blank slide. Ask Copilot: \"Create a medical tourism competitive positioning slide for Apex Health Group. Use a quadrant matrix with Cost vs Clinical Excellence as axes. Position Apex in the upper-right quadrant. Add 3 competitor positions: Prince Court Medical Centre, Gleneagles Kuala Lumpur, and Thailand's Bangkok Hospital. Add a text box noting Apex's MYR 532 million medical tourism revenue and 3 key differentiators: JCI accreditation, Mandarin and Arabic language concierge services, and Malaysia's cost advantage over Singapore. Clean design, healthcare teal and white.\""
            }
          ]
        },
        {
          tool: "📧 Copilot in Outlook",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Triage the MOH audit notification email",
              prompt: "Open Outlook and locate Email_03_MOH_Audit_Notification.docx — copy the content into a draft or open the email. Click the Copilot icon and ask: \"Summarise this MOH audit notification for me. I need 4 things: (1) What type of audit is being conducted, which hospital or facilities are in scope, and the scheduled date; (2) What clinical or operational areas will be audited — list every area explicitly mentioned; (3) Any specific documents or evidence that MOH requires us to prepare in advance; (4) The 3 most urgent internal actions I must complete before the audit date. Format under 4 headings. Maximum 200 words.\"",
              fileRef: "Email_03_MOH_Audit_Notification.docx"
            },
            {
              title: "Draft Group CMO response to senior consultant resignation",
              prompt: "Open a new Outlook email. Ask Copilot: \"Draft a formal response email from Dr Priya Nadarajan, Group Chief Medical Officer of Apex Health Group, to Dr Suresh Pillai, a senior oncologist at Sunway Medical Centre Apex who has submitted his resignation citing work-life balance and a competing offer from Singapore General Hospital. The email should: (1) Acknowledge his decision with genuine appreciation for 8 years of service and his role in building the oncology programme to MYR 84 million annual revenue; (2) Request a face-to-face retention conversation before the resignation is processed — propose 3 specific business days; (3) Hint at a counter-offer under consideration without specifying terms; (4) Maintain the relationship even if he ultimately leaves. Professional, warm, and senior. 300 words.\""
            },
            {
              title: "Copilot coaching on JCI audit response email",
              prompt: "In Outlook, type a rough draft: \"Dear MOH auditor, thank you for the notification. We will prepare for the audit. Our quality team will get the documents ready. Please let us know if you need anything. Regards, Apex Health.\" Ask Copilot to coach this email. Request: \"I am the Group CEO responding to the Ministry of Health audit team. Evaluate this draft on: (1) Tone — is it sufficiently formal and demonstrates institutional confidence; (2) Specificity — does it commit to anything concrete; (3) Governance signals — does it demonstrate that we have a quality committee and proper audit management process. Then rewrite the email at CEO-to-regulator standard with a specific document preparation commitment and named contact person.\""
            }
          ]
        },
        {
          tool: "🎙 Copilot in Teams",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Catch up on missed JCI Accreditation Committee meeting",
              prompt: "Open an existing Teams meeting that was recorded and has a Copilot recap — a committee or project meeting from your own calendar. In the recap pane, ask Copilot: \"I am the Group Chief Medical Officer of Apex Health Group and I missed this meeting due to a patient safety emergency. I need a structured catch-up covering: (1) What was the main agenda topic — summarise in 2 sentences; (2) What specific JCI or quality-related decisions were made and who is responsible for each; (3) Any unresolved issues or items parked for the next meeting; (4) Actions specifically assigned to the CMO or Quality team — list with owner and deadline; (5) Is there anything time-critical that I need to respond to before close of business today?\""
            },
            {
              title: "Extract nurse attrition action items from HR review meeting",
              prompt: "Open an existing recorded Teams meeting recap — a management, HR, or operational review meeting from your calendar. In the Copilot recap pane, ask: \"Extract all action items relating to workforce, staffing, or talent issues from this meeting. Format as a table: Action; Owner (full name); Deadline (specific date or TBC); Priority (Critical if patient safety or accreditation is affected, High if financial impact, Normal otherwise). If no specific deadline was mentioned, flag it as Needs Confirmation. Also identify: was any decision made about nurse compensation or scheduling flexibility changes? Summarise any such decision in a single sentence at the bottom of the table.\""
            },
            {
              title: "Generate CMO update email from clinical team meeting",
              prompt: "Open an existing recorded Teams meeting recap — a clinical leadership, ward management, or department head meeting from your calendar. In the Copilot recap pane, ask: \"Draft a concise clinical update email from Dr Priya Nadarajan, Group CMO, to be sent to all hospital medical directors. The email should synthesise: a 3-sentence summary of the main clinical or operational topics discussed; all key decisions with the responsible consultant or director named; all outstanding action items with deadlines; and an urgent flag if any patient safety, JCI compliance, or MOH audit issue was raised. Format so it is ready to send from Outlook. Professional CMO communication style. Under 250 words.\""
            }
          ]
        },
        {
          tool: "📓 Copilot Notebook",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Cross-document Board briefing for Apex Health CEO",
              prompt: "Go to Copilot Notebook. Upload HC_01_Apex_Health_Group.xlsx, HC_02_Apex_Health_Strategy.docx, and Email_03_MOH_Audit_Notification.docx. In the Instructions box type: \"Using all 3 documents together, prepare a structured Board briefing for Apex Health Group CEO Rania Aziz covering the 3 most pressing issues: (1) For the MOH audit — synthesise from the email what is being audited, then cross-reference with the financial data to identify which hospitals are most exposed; (2) For the 18.4% nurse attrition — combine the HR data from the Excel file and the strategy document to build a fact-based summary of the problem and the current plan; (3) For the 6-week oncology wait — identify the business case for investing in additional consultant capacity. Format: each issue on a separate numbered section with a recommended Board action at the end.\"",
              fileRef: "HC_01_Apex_Health_Group.xlsx, HC_02_Apex_Health_Strategy.docx, Email_03_MOH_Audit_Notification.docx"
            },
            {
              title: "JCI gap analysis using strategy and financial data",
              prompt: "Go to Copilot Notebook. Upload HC_01_Apex_Health_Group.xlsx and HC_02_Apex_Health_Strategy.docx. In the Instructions box type: \"Conduct a JCI accreditation readiness assessment using both documents. For 5 JCI standard areas — patient safety, staffing adequacy, medication management, quality improvement, and governance — evaluate: (1) What does the strategy document say about our current readiness in each area; (2) What does the financial or HR data suggest about actual operational conditions — for example does the nurse-to-patient data support the staffing claims in the strategy; (3) Where is there a gap between stated strategy and actual data; (4) Which area poses the highest JCI failure risk based on combined evidence. Format as a 5-row gap analysis table with RAG status for each area.\"",
              fileRef: "HC_01_Apex_Health_Group.xlsx, HC_02_Apex_Health_Strategy.docx"
            }
          ]
        },
        {
          tool: "🤝 Cowork (Pages)",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Build a clinical quality improvement tracker canvas",
              prompt: "In Copilot Chat, upload HC_01_Apex_Health_Group.xlsx and ask for a hospital quality KPI summary. When Copilot generates the response, click Open in Copilot Pages. Ask: \"Reorganise this quality summary into a live Clinical Quality Improvement Tracker for the Apex Health Quality Committee. Include 4 sections: (1) Hospital Quality Scorecard — key metrics for each of the 12 hospitals with traffic light status; (2) JCI Readiness Tracker — 6 standards chapters with current status and next milestone; (3) Active Improvement Projects — with owner and expected completion date; (4) Escalation Log — any metric that has deteriorated in the last 30 days. Format so the CMO and all 12 hospital medical directors can update collaboratively.\"",
              fileRef: "HC_01_Apex_Health_Group.xlsx"
            },
            {
              title: "Collaborative nurse retention planning canvas",
              prompt: "In Copilot Chat, upload HC_02_Apex_Health_Strategy.docx and ask for a summary of the nurse retention section. Click Open in Copilot Pages. Ask: \"Expand this nurse retention summary into a collaborative planning canvas for the Apex Health Group CHRO and 12 Hospital HR Managers. Structure as: (1) Problem Context — attrition 18.4%, financial cost, JCI risk; (2) Root Causes Confirmed by Hospital HR Managers — collaborative input section; (3) Retention Initiatives — 5 proposed initiatives with owner, investment, and target; (4) Hospital-Level Attrition Targets for FY2025 — each hospital to input their committed target; (5) Progress Check-in Log — monthly updates. Format for shared editing and use in monthly HR governance reviews.\"",
              fileRef: "HC_02_Apex_Health_Strategy.docx"
            }
          ]
        },
        {
          tool: "🤖 Word Agent",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Set up an Apex Health Strategy Assistant on the strategy doc",
              prompt: "Open HC_02_Apex_Health_Strategy.docx in Word. In the Copilot pane, click Create an agent. Name it Apex Health Advisor. Scope it to this document. Instructions: \"Answer questions about Apex Health Group's clinical and business strategy. Cite the section title for each answer. Keep answers under 150 words. Focus on topics relevant to clinical leadership, quality, and business development.\" Save and demo: type \"What is Apex Health's plan to reduce the 6-week oncology wait time and what is the target wait time by end of FY2025?\"",
              fileRef: "HC_02_Apex_Health_Strategy.docx"
            },
            {
              title: "Demo the Apex Health Advisor — clinical leadership queries",
              prompt: "With the Apex Health Advisor active and scoped to HC_02_Apex_Health_Strategy.docx, ask 3 queries a medical director or Board member would ask. Query 1: \"What is the investment committed to the new Cancer Centre and when is the expected opening date?\" Query 2: \"How does the strategy plan to achieve JCI accreditation for all 12 hospitals and what is the timeline for the flagship KL hospital?\" Query 3: \"What specific nurse retention programmes are committed in the strategy and what attrition target do they aim to achieve?\" Show how a complex 50-page healthcare strategy document becomes instantly queryable.",
              fileRef: "HC_02_Apex_Health_Strategy.docx"
            }
          ]
        },
        {
          tool: "🤖 PowerPoint Agent",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Set up a JCI Accreditation Presenter agent on the deck",
              prompt: "Create the JCI Accreditation Readiness Update PowerPoint from the PPT demo step or open the saved file. Save as Apex_JCI_Readiness_2025.pptx. Open Copilot pane, click Create an agent, name it JCI Readiness Advisor, scope to this deck. Instructions: \"Answer questions about Apex Health Group's JCI accreditation readiness based on the content of these slides. Reference slide numbers. Keep answers under 100 words.\" Demo immediately: type \"Which standards chapter has the worst current traffic light rating and what are the 2 most urgent remediation actions?\""
            },
            {
              title: "Demo the JCI Readiness Advisor — committee queries",
              prompt: "With the JCI Readiness Advisor active and scoped to the accreditation PowerPoint, run 3 queries a Quality Committee member would ask. Query 1: \"What is the planned date for the mock JCI survey and how many standards gaps need to be closed before then?\" Query 2: \"Which hospital has the most critical JCI staffing standards gaps and what is the plan to address them?\" Query 3: \"If the nurse attrition problem is not resolved in 90 days, which specific JCI standard areas would move to Red status?\" Demonstrate how a Board committee can interrogate a complex quality presentation using plain English questions."
            }
          ]
        },
        {
          tool: "🤖 Excel Agent",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Set up a Hospital Performance Agent on the Apex Health workbook",
              prompt: "Open HC_01_Apex_Health_Group.xlsx in Excel. In the Copilot pane, click Create an agent. Name it Apex Hospital Advisor. Scope to this workbook. Instructions: \"Answer questions about Apex Health Group hospital performance data. Always cite the sheet and column name. Express financial figures in MYR millions. Highlight if any metric is outside the target range stated in the workbook.\" Demo immediately: type \"Which hospital has the highest bed occupancy and which has the lowest — and what is the group average compared to the 85% target?\"",
              fileRef: "HC_01_Apex_Health_Group.xlsx"
            },
            {
              title: "Demo the Hospital Advisor — CMO operational queries",
              prompt: "With the Apex Hospital Advisor active and scoped to HC_01_Apex_Health_Group.xlsx, ask 3 operational queries the CMO would ask without navigating the spreadsheet. Query 1: \"Which 3 hospitals have nurse attrition above 20% — and is there a correlation with low EBITDA margin at those same hospitals?\" Query 2: \"What is the total number of oncology specialist appointment slots per week across all 12 hospitals and how many additional slots are needed to reduce wait time from 6 to 2 weeks?\" Query 3: \"What percentage of Apex Health's total revenue comes from international medical tourists and which nationality accounts for the highest spend per visit?\" Show how a CMO can get clinical-operational answers without opening a single spreadsheet formula.",
              fileRef: "HC_01_Apex_Health_Group.xlsx"
            }
          ]
        }
      ]
    },
    {
      id: "og",
      name: "Oil & Gas",
      icon: "🛢️",
      color: "#4A2C0A",
      accent: "#E67E22",
      company: "Nusantara Energy Berhad",
      tagline: "PETRONAS PSC audit | 2 Tier 1 PSEs | Net Zero 2050 | 22,400 staff offshore Sarawak",
      scenario: "Nusantara Energy Berhad (Nusantara) is a Malaysian upstream oil and gas company operating under Production Sharing Contracts (PSCs) with PETRONAS across 6 offshore platforms in Sarawak and Sabah. The company employs 22,400 staff and produces approximately 84,000 barrels of oil equivalent per day. FY2024 was a challenging year: 2 Tier 1 Process Safety Events at the Miri A platform triggered a PETRONAS operational audit, and 2 offshore hydrocarbon releases have generated regulatory and environmental exposure. VP HSE Aziz Rahman has 6 weeks to achieve full PETRONAS audit readiness, close the process safety management gaps, and demonstrate credible progress on the Net Zero 2050 carbon intensity reduction pathway before the audit team arrives.",
      files: ["OG_01_Nusantara_Energy.xlsx", "OG_02_Nusantara_HSE_Report.docx", "Email_02_PETRONAS_Audit_Notice.docx"],
      prompts: [
        {
          tool: "🤖 Copilot Chat (Basic)",
          license: "Free — no M365 license needed",
          account: "Sasha Ouellet — SashaO@ABSx62256373.OnMicrosoft.com",
          prompts: [
            {
              title: "Explain Tier 1 PSE and why it matters for PETRONAS audits",
              prompt: "Ask Copilot: \"Explain what a Tier 1 Process Safety Event (PSE) is under the API Recommended Practice 754 framework, which PETRONAS uses in its production-sharing contract (PSC) audits of upstream operators in Malaysia. Nusantara Energy has 2 Tier 1 PSEs in the Miri offshore sector in FY2024. Explain: (1) The precise API 754 definition of a Tier 1 PSE and what it requires in terms of loss of primary containment; (2) The PETRONAS audit consequences for a PSC operator with 2 Tier 1 PSEs in a fiscal year; (3) How Tier 1 PSEs relate to DOSH Petroleum Safety Act compliance in Malaysia; (4) The reputational and contractual risk under the PSC if PETRONAS triggers a Show Cause Notice. Maximum 250 words.\""
            },
            {
              title: "Brief me before the PETRONAS operational audit",
              prompt: "Ask Copilot: \"I am the VP HSE of Nusantara Energy Berhad, a Malaysian upstream oil and gas company with 22,400 staff and offshore operations in Sarawak and Sabah under a PETRONAS PSC. PETRONAS has scheduled an operational safety audit of our Miri offshore operations in 6 weeks. Prepare a structured HSE audit readiness brief covering: (1) The 5 most commonly cited PETRONAS HSE audit findings for offshore upstream operators; (2) The specific documentation PETRONAS auditors require — HIRARC registers, PTW logs, emergency response plans, and environmental management plans; (3) The 3 most important preparation actions for our 6-week window; (4) What a Tier 1 PSE finding means for the audit outcome and our PSC status. Maximum 200 words.\""
            },
            {
              title: "Explain Net Zero 2050 obligations for upstream O&G in Malaysia",
              prompt: "Ask Copilot: \"Explain what Net Zero by 2050 means in practice for an upstream oil and gas company operating in Malaysia under a PETRONAS PSC. Nusantara Energy has stated a Net Zero 2050 commitment. Cover: (1) PETRONAS's own Net Zero 2050 roadmap and what it requires from PSC operators by 2030 and 2040 in terms of methane intensity and carbon intensity reduction; (2) The Malaysian government's National Energy Transition Roadmap and how it affects upstream E&P companies; (3) The 3 most technically and commercially feasible decarbonisation levers for an offshore operator of Nusantara's scale — electrification, flaring reduction, CCUS, or EOR; (4) The cost range per tonne of CO2 abated for each option at current commodity prices. Maximum 300 words.\""
            }
          ]
        },
        {
          tool: "�� Researcher",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Research PETRONAS PSC compliance requirements and enforcement",
              prompt: "In Copilot Chat, switch to the Researcher agent. Upload OG_02_Nusantara_HSE_Report.docx. Ask: \"Review Nusantara Energy's HSE report, then search the web for PETRONAS Production Sharing Contract compliance requirements for offshore operators, specifically: PETRONAS HSSE audit frameworks and the consequences of Tier 1 PSE findings for PSC continuation; recent PETRONAS enforcement actions or Show Cause Notices to E&P operators between 2022 and 2025; API 754 Tier 1 PSE industry benchmarks for offshore operators of Nusantara's scale; and Malaysia DOSH Petroleum Safety Act inspection and enforcement actions. Cross-reference with the HSE report to identify the 3 highest-priority compliance gaps. Format as an audit readiness gap table with RAG status.\"",
              fileRef: "OG_02_Nusantara_HSE_Report.docx"
            },
            {
              title: "Research offshore process safety best practices",
              prompt: "In Copilot Chat, switch to the Researcher agent. Ask: \"Search the web for offshore process safety management best practices relevant to Malaysian upstream operators. Find: the PETRONAS Technical Standards on process safety management applicable to PSC operators; international offshore safety case frameworks — UK OPEP, Australian NOPSA — and what offshore operators learn from them; the most cited root causes of Tier 1 PSE incidents in offshore Asia-Pacific operations from 2020 to 2025 including any published IADC or IOGP incident data; and digital safety management system platforms deployed by major Asian E&P companies. What are the top 5 technical and procedural improvements Nusantara should implement before the PETRONAS audit? Cite all sources.\""
            },
            {
              title: "Research energy transition strategies for upstream operators",
              prompt: "In Copilot Chat, switch to the Researcher agent. Upload OG_01_Nusantara_Energy.xlsx. Ask: \"Review Nusantara Energy's operational data. Then search the web for: Southeast Asian upstream oil and gas companies that have published credible Net Zero or carbon intensity reduction plans; the current methane intensity performance benchmarks from the OGMP 2.0 framework and how Malaysian operators compare; PETRONAS's stated expectations for Scope 1 and Scope 2 emissions reductions from PSC operators by 2030; and any carbon pricing or emissions trading schemes in Malaysia or Indonesia affecting upstream E&P economics. Given Nusantara's production profile and field age, model the 3 most realistic carbon reduction options with cost per tonne of abatement.\"",
              fileRef: "OG_01_Nusantara_Energy.xlsx"
            }
          ]
        },
        {
          tool: "📊 Analyst",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Analyse Nusantara Energy safety and production KPIs",
              prompt: "In Copilot Chat, switch to the Analyst agent. Upload OG_01_Nusantara_Energy.xlsx. Ask: \"Analyse the full Nusantara Energy operational dataset. Calculate: (1) The Total Recordable Incident Rate (TRIR) and Lost Time Injury Frequency (LTIF) for FY2024 — how do these compare to the IOGP industry median for offshore Asia-Pacific operators; (2) The production efficiency rate — what percentage of planned production days were lost to unplanned shutdowns in FY2024; (3) The environmental performance — number of reportable spills, volumes released, and comparison to the FY2023 baseline; (4) Which of the 6 offshore platforms has the worst TRIR and which has the worst production efficiency — are they the same platform? Present as a VP HSE operations dashboard with 5 key findings and a recommendation.\"",
              fileRef: "OG_01_Nusantara_Energy.xlsx"
            },
            {
              title: "Model production impact of 2 offshore spills",
              prompt: "In Copilot Chat, switch to the Analyst agent. Upload OG_01_Nusantara_Energy.xlsx. Ask: \"Analyse the financial and operational impact of the 2 offshore spills in the Miri sector. From the production data calculate: (1) The total production downtime in days caused by post-spill shutdown and inspection across both incidents; (2) The revenue loss in USD millions at the current Brent crude price of USD 84/bbl; (3) The estimated remediation and containment cost range based on the spill volumes reported; (4) The total cost of non-compliance including regulatory fines, PETRONAS penalties, and clean-up — express as a percentage of FY2024 EBITDA; (5) The post-incident production recovery curve — are we back to pre-spill production levels. Format as a crisis financial impact summary.\"",
              fileRef: "OG_01_Nusantara_Energy.xlsx"
            },
            {
              title: "Analyse carbon intensity and Net Zero pathway",
              prompt: "In Copilot Chat, switch to the Analyst agent. Upload OG_01_Nusantara_Energy.xlsx. Ask: \"Analyse Nusantara Energy's carbon performance data. Calculate: (1) The current Scope 1 carbon intensity in kgCO2e per barrel of oil equivalent and how it compares to the PETRONAS PSC operator benchmark; (2) The flare intensity ratio and whether our flaring reduction projects are meeting the planned trajectory toward the 2030 near-zero routine flaring commitment; (3) The energy intensity of our operations and the potential carbon reduction from transitioning 2 platforms to renewable-powered compression; (4) The methane intensity percentage and what reduction is needed to qualify for OGMP Level 4 Gold certification by 2026. Format as a Net Zero progress dashboard suitable for the Board Sustainability Committee.\"",
              fileRef: "OG_01_Nusantara_Energy.xlsx"
            }
          ]
        },
        {
          tool: "📊 Copilot in Excel",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Summarise Nusantara Energy KPI workbook for HSE committee",
              prompt: "Open OG_01_Nusantara_Energy.xlsx. Ask Copilot: \"Give me a plain-English executive summary of this entire workbook for the VP HSE. What is the current TRIR and how does it compare to the FY2023 baseline? Which of the 6 offshore platforms has the most concerning safety performance? What was the total production impact in barrels of oil equivalent from the 2 Miri offshore spills? Flag any metric that is trending in the wrong direction over the last 3 quarters. Format: 3-sentence overview, then 4 specific flagged concerns with sheet name and row reference for each.\"",
              fileRef: "OG_01_Nusantara_Energy.xlsx"
            },
            {
              title: "Create a production efficiency waterfall chart",
              prompt: "Open OG_01_Nusantara_Energy.xlsx. Navigate to the Production Performance sheet. Ask Copilot: \"Create a waterfall chart showing the breakdown of production losses in barrels of oil equivalent per day from the planned production baseline to the actual FY2024 production. Categories to show: Planned Maintenance Shutdowns, Unplanned Equipment Failure, Post-Spill Shutdown, Weather Downtime, and Reservoir Performance. Use red bars for unplanned losses and blue for planned. Add a green bar for the Actual Production total. Title: Nusantara Energy — FY2024 Production Efficiency Waterfall. This chart will be included in the PETRONAS audit pack submission.\"",
              fileRef: "OG_01_Nusantara_Energy.xlsx"
            },
            {
              title: "Add TRIR trend formula with regulatory threshold indicator",
              prompt: "Open OG_01_Nusantara_Energy.xlsx. Navigate to the Safety KPI sheet. Ask Copilot: \"Add a new column called TRIR Status to the safety KPI table. The formula should compare each platform's TRIR against the PETRONAS threshold of 1.0 per million man-hours. If TRIR is above 1.0, display the text Breached in red. If between 0.8 and 1.0, display Watch in amber. If below 0.8, display Compliant in green. Tell me how many platforms are currently in Breached status and what the Nusantara fleet-wide average TRIR is compared to the PETRONAS threshold.\"",
              fileRef: "OG_01_Nusantara_Energy.xlsx"
            },
            {
              title: "Natural language query — offshore spill impact",
              prompt: "Open OG_01_Nusantara_Energy.xlsx. Ask Copilot: \"Without me navigating sheets, answer: (1) What were the exact dates and volumes of the 2 offshore spills in the Miri sector and which platform was involved in each; (2) What is the total production days lost specifically attributable to those 2 spill incidents — not planned shutdowns; (3) At the current Brent crude price of USD 84 per barrel and Nusantara's average gross production rate, what is the USD revenue lost per day of shutdown; (4) What is the combined environmental liability estimate for both spills if Malaysia DOSH imposes the maximum penalty under Petroleum Safety Act. Format as a 2-column answer table.\"",
              fileRef: "OG_01_Nusantara_Energy.xlsx"
            }
          ]
        },
        {
          tool: "📝 Copilot in Word",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Summarise Nusantara HSE report into executive brief",
              prompt: "Open OG_02_Nusantara_HSE_Report.docx. Ask Copilot: \"Summarise this HSE report into a 1-page executive brief for Nusantara Energy's Group CEO and Board Safety Committee. Format as: (1) FY2024 HSE Performance Overview — 4 headline metrics with FY2023 comparison and trend indicator; (2) Critical Incidents — the 2 offshore spills and 2 Tier 1 PSEs — specific dates, locations, and remediation status; (3) PETRONAS Audit Readiness — current compliance status and the 3 most urgent preparation actions before the 6-week audit window; (4) Net Zero 2050 Progress — current carbon intensity vs trajectory; (5) Board Recommendation — 2 decisions required. Formal HSE leadership document. 400 words maximum.\"",
              fileRef: "OG_02_Nusantara_HSE_Report.docx"
            },
            {
              title: "Draft PETRONAS Show Cause response for Tier 1 PSE",
              prompt: "Open a new Word document. Ask Copilot: \"Draft a formal Show Cause response from Nusantara Energy Berhad to PETRONAS Production Sharing Division following a Show Cause Notice issued after 2 Tier 1 Process Safety Events at the Miri A offshore platform in FY2024. The response must: (1) Acknowledge the PSEs with specific dates and confirm immediate containment actions taken; (2) Present the Root Cause Analysis findings — equipment isolation failure on Miri A, and concurrent maintenance scheduling conflict; (3) Detail the 5 corrective and preventive actions with completion dates and responsible engineers; (4) Provide assurance of enhanced process safety management governance including monthly PSE Review Board; (5) Request continuation of PSC operations while remediation is underway. Formal regulatory correspondence, signed by the VP HSE. 500 words.\""
            },
            {
              title: "Rewrite the Permit to Work procedure for offshore crew",
              prompt: "Open OG_02_Nusantara_HSE_Report.docx. Locate the Permit to Work governance section. Ask Copilot: \"Rewrite this Permit to Work procedure section in plain, operational language for an offshore maintenance technician with 3 years of experience, not an HSE manager. Replace all regulatory references with clear step-by-step instructions. Add a simple visual checklist: the 6 checks a technician must complete before accepting any PTW for hot work on an offshore platform. The rewrite must be under 300 words, use numbered steps, and be understandable by someone who reads English as a second language. This version will be laminated and posted at offshore accommodation modules.\"",
              fileRef: "OG_02_Nusantara_HSE_Report.docx"
            },
            {
              title: "Draft emergency response communication to PETRONAS",
              prompt: "Open a new Word document. Ask Copilot: \"Draft an emergency response notification letter from Nusantara Energy Berhad to PETRONAS Emergency Response Director following an uncontrolled hydrocarbon release on the Miri A platform. The letter must follow PETRONAS PSC Emergency Notification Protocol and include: (1) Incident type — uncontrolled release of gas condensate from a wellhead isolation valve; (2) Location — Miri A platform, Block SK 318, Sarawak offshore; (3) Time and duration of release; (4) Environmental impact — estimated volume released and sea surface area affected; (5) Immediate response actions taken — platform evacuation, SOPEP activation, marine barrier deployment; (6) Current personnel safety status — all 84 personnel accounted for; (7) Notification of DOSH, Maritime Department Malaysia, and PETRONAS HSSE simultaneously. Formal incident reporting tone. Under 400 words.\""
            }
          ]
        },
        {
          tool: "🎯 Copilot in PowerPoint",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Create PETRONAS audit readiness presentation",
              prompt: "Open a new PowerPoint. Ask Copilot: \"Create a 7-slide PETRONAS HSE Audit Readiness briefing for Nusantara Energy Berhad. Slide 1: Audit Overview — PETRONAS audit scope, date, and Nusantara preparation status. Slide 2: FY2024 Safety Performance Summary — TRIR, LTIF, Tier 1 PSEs. Slide 3: Process Safety Event — 2 Miri A incidents — root cause, remediation, and status. Slide 4: Environmental Performance — 2 offshore spills, remediation status, and environmental liability. Slide 5: Audit Readiness Tracker — 6 audit domains with traffic light status for each. Slide 6: 6-Week Sprint Plan — critical preparation actions with owner and deadline. Slide 7: Board Safety Committee Request — 2 decisions required. Dark navy O&G theme, professional.\""
            },
            {
              title: "Generate Net Zero 2050 roadmap slides",
              prompt: "Open a new PowerPoint. Ask Copilot: \"Create a 5-slide Net Zero 2050 Roadmap presentation for Nusantara Energy Berhad's investor and PETRONAS stakeholder briefing. Slide 1: Nusantara Net Zero 2050 Commitment and Baseline. Slide 2: Our Carbon Baseline — Scope 1, Scope 2, and methane intensity vs PETRONAS benchmark. Slide 3: Four Decarbonisation Pillars — flaring reduction, electrification, CCUS, and EOR — with timeline and cost. Slide 4: 2025-2030 Milestone Roadmap with specific carbon intensity reduction targets per year. Slide 5: Governance and Accountability — Board Sustainability Committee, ESG reporting framework, OGMP 2.0 Gold certification target. Clean, modern energy transition design. Green and navy blue.\""
            },
            {
              title: "Add process safety performance benchmarking slide",
              prompt: "In an open Nusantara Energy PowerPoint, place cursor on a new slide. Ask Copilot: \"Create a process safety benchmarking slide comparing Nusantara Energy's FY2024 Tier 1 PSE rate against the IOGP industry average for offshore Asia-Pacific operators. Use a vertical bar chart: Nusantara in red at 2 Tier 1 PSEs, IOGP Industry Average in navy blue, and PETRONAS PSC Best-in-Class in green. Add a horizontal dashed line at the PETRONAS threshold. Include a callout box stating the business impact: PETRONAS audit triggered and PSC continuation at risk. Title: Process Safety — Nusantara vs Industry Benchmarks FY2024. This slide is for the Board Safety Committee pack.\""
            }
          ]
        },
        {
          tool: "📧 Copilot in Outlook",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Triage PETRONAS audit notification email thread",
              prompt: "Open Outlook and locate the email from Email_02_PETRONAS_Audit_Notice.docx — copy content into a draft or open the forwarded thread. Click Copilot and ask: \"Summarise this PETRONAS audit notification for me. I need: (1) What is the exact scope of the PETRONAS audit — which platforms, which HSE management systems, and which incidents are in scope; (2) What specific documentation must be submitted before the audit date and by when; (3) How many calendar days do we have to prepare from today; (4) The 3 most urgent internal preparation actions I need to assign today. Format under 4 headings. Maximum 200 words.\"",
              fileRef: "Email_02_PETRONAS_Audit_Notice.docx"
            },
            {
              title: "Draft VP HSE weekly update to Group CEO",
              prompt: "Open a new Outlook email. Ask Copilot: \"Draft a formal weekly HSE status update email from Nusantara Energy's VP HSE to Group CEO Lena Hartmann. The email should summarise the current week's key HSE status in 5 structured points: (1) PETRONAS Audit Preparation — current readiness percentage and top 3 open gaps; (2) Miri A Tier 1 PSE Remediation — corrective actions completion status as at this week; (3) Offshore Spill Remediation — environmental containment and DOSH reporting status; (4) Fleet-wide TRIR trend — this week versus FY2024 target; (5) Three Decisions Needed from CEO — specific items requiring CEO approval to unblock preparation. Tone: factual, concise, no spin. Under 300 words.\""
            },
            {
              title: "Copilot coaching on VP HSE email to PETRONAS",
              prompt: "In Outlook, type a rough draft to a PETRONAS auditor: \"Dear PETRONAS team, we will be ready for the audit and we have been working on fixing our safety issues. The Miri incidents have been addressed. Please let us know what you need. Thanks.\" Ask Copilot for coaching: \"I am the VP HSE of an upstream E&P company writing to the PETRONAS Upstream Safety team. Evaluate my draft on: (1) Does it convey operational credibility and regulatory confidence; (2) Is the remediation commitment specific enough for a sophisticated regulator; (3) Does the tone match a formal HSE bilateral correspondence. Rewrite the email at VP HSE standard with a 3-point remediation status summary and an offer to present evidence at the bilateral meeting.\""
            }
          ]
        },
        {
          tool: "🎙 Copilot in Teams",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Catch up on missed PETRONAS audit preparation meeting",
              prompt: "Open an existing Teams meeting that was recorded and has a Copilot recap — a project management or operations meeting from your own calendar. In the Copilot recap pane ask: \"I am Nusantara Energy's VP HSE and I missed this meeting because I was offshore doing a platform inspection. I need a structured catch-up: (1) What was the main topic and purpose of the meeting; (2) What was decided about our PETRONAS audit preparation — any deadlines or go/no-go decisions; (3) Which specific platform HSE teams have been assigned pre-audit tasks and what tasks; (4) Any action assigned directly to the VP HSE that I need to pick up today; (5) Is there a critical path item that could delay audit readiness if not resolved in the next 48 hours.\""
            },
            {
              title: "Extract all HSE action items from the weekly safety review",
              prompt: "Open an existing recorded Teams meeting recap from your calendar. In the Copilot recap pane ask: \"List all HSE action items from this meeting as a formal HSE Action Register table. Columns: Action Reference (sequential number); Action Description; Owner (full name and title); Platform or Location; Target Completion Date; Priority — Critical for PETRONAS audit-related items, High for incident remediation, Normal for routine. Group by platform. Highlight in red any action where the deadline falls within the next 14 days. This register will be submitted to the VP HSE and shared with all offshore installation managers before the end of the day.\""
            },
            {
              title: "Generate a platform HSE briefing from the ops review",
              prompt: "Open an existing recorded Teams meeting recap — an operations review or management meeting from your calendar. In the Copilot recap pane ask: \"Draft an HSE briefing email from the VP HSE to be sent to all 6 offshore installation managers based on the outcomes of this meeting. Include: (1) Key HSE topics discussed and agreed positions — 3 bullet points; (2) Fleet-wide TRIR update vs the annual target; (3) PETRONAS audit preparation requirements specific to offshore installations; (4) Any incident reports or near-miss trends discussed; (5) Actions specifically assigned to installation managers with deadlines. Format as a structured briefing email. Tone: direct and operationally focused. Under 300 words.\""
            }
          ]
        },
        {
          tool: "📓 Copilot Notebook",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Full PETRONAS audit brief from 3 HSE documents",
              prompt: "Go to Copilot Notebook. Upload OG_01_Nusantara_Energy.xlsx, OG_02_Nusantara_HSE_Report.docx, and Email_02_PETRONAS_Audit_Notice.docx. In Instructions: \"Using all 3 documents together, prepare a structured PETRONAS audit readiness brief for VP HSE. (1) From the audit notice email — extract the audit scope, documentation requirements, and submission deadlines; (2) From the HSE report — identify the 5 most critical open findings that PETRONAS will focus on, including the 2 Tier 1 PSEs and 2 offshore spills; (3) Cross-reference the financial data to quantify the production and revenue impact of the safety incidents; (4) Build a prioritised 6-week preparation action list with owner role for each item; (5) Flag the single biggest audit risk that needs CEO-level attention.\"",
              fileRef: "OG_01_Nusantara_Energy.xlsx, OG_02_Nusantara_HSE_Report.docx, Email_02_PETRONAS_Audit_Notice.docx"
            },
            {
              title: "Net Zero evidence pack and gap analysis",
              prompt: "Go to Copilot Notebook. Upload OG_01_Nusantara_Energy.xlsx and OG_02_Nusantara_HSE_Report.docx. In Instructions: \"Using both documents, conduct a Net Zero 2050 pathway gap analysis for Nusantara Energy. For 4 carbon reduction pillars — routine flaring elimination, platform electrification, methane leak detection and repair (LDAR), and carbon capture investment — analyse: (1) What does the current HSE report say about progress on each pillar; (2) What does the production and emissions data in the Excel workbook show about actual versus planned carbon intensity trajectory; (3) Where is there a gap between stated commitments and current data; (4) What is the credibility risk if PETRONAS or an ESG rating agency reviews these 2 documents together. Format as a 4-row evidence quality assessment.\"",
              fileRef: "OG_01_Nusantara_Energy.xlsx, OG_02_Nusantara_HSE_Report.docx"
            }
          ]
        },
        {
          tool: "🤝 Cowork (Pages)",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Build PETRONAS audit readiness tracker in Pages",
              prompt: "In Copilot Chat, upload OG_02_Nusantara_HSE_Report.docx and ask for an audit readiness summary. When Copilot responds, click Open in Copilot Pages. Ask: \"Reorganise this into a collaborative PETRONAS Audit Readiness Tracker for the Nusantara Energy HSE leadership team of 8 members. Structure as: (1) Audit Scope and Timeline — dates and in-scope platforms; (2) Documentation Submission Tracker — each required document with owner and status; (3) Platform Readiness Status — 6 offshore platforms with traffic light RAG status; (4) Critical Path Items — top 3 items that could cause audit failure with escalation owner; (5) Daily Status Update log. Format for collaborative editing by all 6 offshore installation managers and the KL HSE team.\"",
              fileRef: "OG_02_Nusantara_HSE_Report.docx"
            },
            {
              title: "Collaborative incident investigation and learning canvas",
              prompt: "In Copilot Chat, upload OG_02_Nusantara_HSE_Report.docx and ask Copilot to summarise the 2 Miri platform incident reports. Click Open in Copilot Pages. Ask: \"Expand these incident summaries into a collaborative Safety Learning Canvas for the Nusantara Energy Process Safety team. Structure as: (1) Incident Timeline — both Miri incidents with key events; (2) Root Cause Tree — contributory causes, immediate causes, and root causes to be confirmed collaboratively; (3) Contributing Factors — systemic factors the team will add insights to; (4) Corrective Actions — each action with owner, deadline, and verification method; (5) Lessons Learned Library — findings to be shared across all 6 platforms. Format for multi-author collaborative input.\"",
              fileRef: "OG_02_Nusantara_HSE_Report.docx"
            }
          ]
        },
        {
          tool: "🤖 Word Agent",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Set up a Nusantara HSE Policy Agent",
              prompt: "Open OG_02_Nusantara_HSE_Report.docx in Word. In the Copilot pane, click Create an agent. Name it Nusantara HSE Advisor. Scope it to this document. Instructions: \"Answer questions about Nusantara Energy HSE policies, incidents, and compliance requirements. Cite the relevant section. Keep answers under 150 words. If the question relates to live operational data not in this document, direct the user to the VP HSE team.\" Demo immediately: type \"What is the stated root cause of the Miri A Tier 1 PSE and what corrective actions have been committed to?\"",
              fileRef: "OG_02_Nusantara_HSE_Report.docx"
            },
            {
              title: "Demo the Nusantara HSE Advisor — platform crew queries",
              prompt: "With the Nusantara HSE Advisor active and scoped to OG_02_Nusantara_HSE_Report.docx, ask 3 queries an offshore installation manager would realistically ask. Query 1: \"What is the permit-to-work escalation process if a contractor hot work PTW is challenged by a production operator — what does policy say?\" Query 2: \"After a Tier 1 PSE what is the minimum investigation timeline and who must review and approve the RCA report before it is submitted to PETRONAS?\" Query 3: \"What are the 3 most critical non-negotiable requirements we must demonstrate during a PETRONAS HSE audit of our platform?\" Show how an intelligent document agent replaces searching through 80-page reports.",
              fileRef: "OG_02_Nusantara_HSE_Report.docx"
            }
          ]
        },
        {
          tool: "🤖 PowerPoint Agent",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Set up a PETRONAS Audit Presenter agent on the readiness deck",
              prompt: "Create or open the PETRONAS Audit Readiness PowerPoint from the PPT demo step. Save as Nusantara_PETRONAS_Audit_2025.pptx. Open Copilot pane, click Create an agent, name it PETRONAS Audit Coach, scope to this deck. Instructions: \"Answer questions about Nusantara Energy's PETRONAS audit readiness based on slide content. Reference slide numbers. Keep answers concise — under 100 words.\" Demo immediately: type \"Which platforms are currently showing Red status in the audit readiness tracker and what are the specific gaps for each?\""
            },
            {
              title: "Demo the PETRONAS Audit Coach — pre-audit queries",
              prompt: "With the PETRONAS Audit Coach active, run 3 queries that simulate how the VP HSE would prepare team leaders before the PETRONAS audit. Query 1: \"What is the single most critical corrective action that PETRONAS auditors will expect to see evidence for on day one of the audit?\" Query 2: \"Which slide shows the process safety event timeline and what is the current status of all RCA corrective actions?\" Query 3: \"If PETRONAS asks why we had 2 Tier 1 PSEs in one fiscal year, which slide gives the most credible explanation of the root causes and our systemic response?\" Demonstrate how the agent turns a complex audit pack into an instant preparation tool."
            }
          ]
        },
        {
          tool: "🤖 Excel Agent",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Set up a Production Safety Dashboard agent",
              prompt: "Open OG_01_Nusantara_Energy.xlsx in Excel. Create an agent named Nusantara Safety Analyst. Scope to this workbook. Instructions: \"Answer questions about Nusantara Energy safety and production performance data. Always cite the sheet name. Express TRIR as per million man-hours. Flag any metric above the PETRONAS threshold.\" Demo immediately: type \"What is the fleet-wide TRIR for FY2024 and which platform has the highest TRIR — is it above the PETRONAS threshold of 1.0?\"",
              fileRef: "OG_01_Nusantara_Energy.xlsx"
            },
            {
              title: "Demo the Safety Analyst — PETRONAS audit queries",
              prompt: "With the Nusantara Safety Analyst active and scoped to OG_01_Nusantara_Energy.xlsx, simulate the data questions a PETRONAS auditor would ask on day one. Query 1: \"What was the total number of Lost Time Injuries in FY2024 and how does the LTIF compare to the FY2023 baseline — is the trend improving?\" Query 2: \"What is the total production days lost from unplanned shutdowns in FY2024 including both the spill-related and equipment-failure shutdowns?\" Query 3: \"What percentage of planned maintenance was completed on schedule for the Miri A platform in FY2024, and did any deferred maintenance contribute to the Tier 1 PSE events?\"",
              fileRef: "OG_01_Nusantara_Energy.xlsx"
            }
          ]
        }
      ]
    },
    {
      id: "telco",
      name: "Telco & Communications",
      icon: "📡",
      color: "#2C3E50",
      accent: "#3498DB",
      company: "ClearWave Communications Berhad",
      tagline: "5G rollout 12.4% vs 20% | MCMC QoS breach | B2B MYR 2.1B target | 14.8M subscribers",
      scenario: "ClearWave Communications Berhad (ClearWave) is Malaysia's third-largest mobile network operator with 14.8 million subscribers and a national mobile and fibre footprint. Two regulatory challenges dominate the FY2025 leadership agenda: a 5G population coverage gap at 12.4% against the MCMC licence commitment of 20%, and a Q3 network outage that lasted 180 minutes — 60 minutes above the MCMC Quality of Service threshold of 120 minutes, triggering a Show Cause Notice. Commercially, the MYR 2.1 billion B2B enterprise revenue target is behind plan as competitors close the enterprise 5G gap. Group CEO Sven Lindqvist and VP Regulatory Affairs need Copilot to prepare the MCMC bilateral response, accelerate B2B sales strategy, and manage customer communication after the outage.",
      files: ["TC_01_ClearWave_Communications.xlsx", "TC_02_ClearWave_Strategy.docx", "Email_05_MCMC_Notice.docx"],
      prompts: [
        {
          tool: "🤖 Copilot Chat (Basic)",
          license: "Free — no M365 license needed",
          account: "Sasha Ouellet — SashaO@ABSx62256373.OnMicrosoft.com",
          prompts: [
            {
              title: "Explain MCMC outage reporting obligations for mobile operators",
              prompt: "Ask Copilot: \"Explain the Malaysian Communications and Multimedia Commission (MCMC) regulatory obligations for a mobile network operator regarding major network outage reporting. ClearWave Communications had a network outage that lasted 180 minutes in Q3 FY2024 against the MCMC regulatory threshold of 120 minutes — meaning we breached the threshold. Explain: (1) What MCMC's Quality of Service standard requires for outage reporting, duration, and compensation; (2) The specific reporting timeline after a major outage — how many hours to notify, to whom, and in what format; (3) The penalty range for exceeding the 120-minute threshold; (4) Whether a repeat breach in the same fiscal year triggers additional regulatory consequences. Maximum 250 words.\""
            },
            {
              title: "Brief me on 5G deployment gap before the MCMC bilateral",
              prompt: "Ask Copilot: \"I am the Group CEO of ClearWave Communications Berhad, Malaysia's third-largest mobile operator. Our 5G population coverage is 12.4% against the MCMC licence commitment of 20% by year-end. I have a bilateral meeting with the MCMC Chairman in 3 days. Prepare a structured brief covering: (1) The MCMC licence condition ClearWave committed to and the exact current gap; (2) The 2 most credible technical and commercial explanations for the deployment delay that MCMC will find acceptable; (3) The 3 most important commitments we should offer — specific milestones and timelines — to avoid a Show Cause Notice; (4) The risk if MCMC imposes a licence variation or spectrum recall. Maximum 200 words.\""
            },
            {
              title: "What is B2B enterprise connectivity and why does it matter?",
              prompt: "Ask Copilot: \"Explain what enterprise B2B connectivity services mean for a Malaysian telco like ClearWave Communications. ClearWave has a MYR 2.1 billion B2B enterprise revenue target. Cover: (1) The key B2B telco product categories — managed WAN, SD-WAN, private 5G networks, IoT connectivity, and cloud interconnect; (2) Why large Malaysian corporates and GLCs are priority B2B targets; (3) How enterprise 5G private network deployments differ from public 5G and what the revenue model is; (4) The 3 main competitors for B2B enterprise contracts in Malaysia — Telekom Malaysia, Maxis Business, Celcom Axiata — and ClearWave's differentiation opportunity. Maximum 200 words.\""
            }
          ]
        },
        {
          tool: "�� Researcher",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Research MCMC regulatory enforcement actions and 5G benchmarks",
              prompt: "In Copilot Chat, switch to the Researcher agent. Upload TC_02_ClearWave_Strategy.docx. Ask: \"Review ClearWave's strategy document, then search the web for: MCMC enforcement actions against Malaysian mobile network operators for QoS threshold breaches between 2022 and 2025; MCMC's 5G deployment licence requirements and the population coverage milestones committed by operators under the 5G sharing model; international benchmarks for 5G deployment pace — South Korea, UAE, Saudi Arabia — that ClearWave could reference in a regulatory bilateral; and recent Malaysian Spectrum Management decisions affecting mobile operators. Cross-reference with ClearWave's strategy to identify the 3 most urgent regulatory risk mitigations.\"",
              fileRef: "TC_02_ClearWave_Strategy.docx"
            },
            {
              title: "Research B2B enterprise telco market in Malaysia",
              prompt: "In Copilot Chat, switch to the Researcher agent. Ask: \"Search the web for the Malaysian enterprise B2B telco market landscape for 2024 and 2025. Find: the total addressable market for enterprise connectivity in Malaysia — total MYR market size; the top 5 enterprise telco revenue opportunities — SD-WAN, private 5G, managed security, IoT platform, cloud interconnect; the main enterprise customer segments driving the most B2B telco spending in Malaysia — banks, manufacturing, GLCs, and healthcare; and analyst reports on 5G enterprise use cases generating measurable ROI in ASEAN markets. ClearWave has a MYR 2.1 billion B2B target. What are the 5 most realistic growth vectors to accelerate B2B revenue? Cite all sources.\""
            },
            {
              title: "Research 5G network deployment acceleration strategies",
              prompt: "In Copilot Chat, switch to the Researcher agent. Upload TC_01_ClearWave_Communications.xlsx. Ask: \"Review ClearWave's network deployment data, then search the web for: proven strategies used by mobile operators in comparable markets to accelerate 5G rollout when facing regulatory deployment timelines — active infrastructure sharing, small cell densification, and neutral host models; any MCMC guidance on flexible deployment commitments for operators facing civil works or permitting delays; and 5G performance benchmarks — throughput, latency, enterprise NPS — for operators at 12% to 15% population coverage. Given ClearWave's current deployment pace, what is a credible timeline to reach 20% coverage and what would accelerate it most?\"",
              fileRef: "TC_01_ClearWave_Communications.xlsx"
            }
          ]
        },
        {
          tool: "📊 Analyst",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Analyse ClearWave subscriber and revenue KPIs",
              prompt: "In Copilot Chat, switch to the Analyst agent. Upload TC_01_ClearWave_Communications.xlsx. Ask: \"Analyse the full ClearWave Communications dataset. Calculate: (1) Net subscriber adds by segment — postpaid, prepaid, B2B — for each quarter of FY2024 and identify which quarter had the worst net adds; (2) Revenue per user (ARPU) trend for postpaid and B2B segments — is ARPU improving or declining on a quarterly basis; (3) B2B enterprise revenue as a percentage of total MYR revenue — actual vs the MYR 2.1 billion target; (4) The churn rate by segment and whether high-value postpaid subscribers are churning at a higher rate than the overall average; (5) The 3 revenue levers that could close the B2B revenue gap fastest. Present as a CEO commercial dashboard.\"",
              fileRef: "TC_01_ClearWave_Communications.xlsx"
            },
            {
              title: "Analyse 5G deployment progress and MCMC compliance gap",
              prompt: "In Copilot Chat, switch to the Analyst agent. Upload TC_01_ClearWave_Communications.xlsx. Ask: \"Analyse the 5G deployment data. Calculate: (1) Current 5G population coverage at 12.4% versus the MCMC licence obligation of 20% — how many additional sites need to be activated to close the gap; (2) The average 5G site activation rate per month in FY2024 — and at this rate, in how many months will 20% coverage be achieved; (3) The deployment cost to close the gap — using the average capital cost per 5G site from the workbook; (4) The revenue contribution from 5G subscribers versus non-5G subscribers — is there measurable ARPU uplift justifying the investment; (5) MCMC penalty risk at current deployment pace. Format as a regulatory risk and investment case.\"",
              fileRef: "TC_01_ClearWave_Communications.xlsx"
            },
            {
              title: "Analyse network outage financial and regulatory impact",
              prompt: "In Copilot Chat, switch to the Analyst agent. Upload TC_01_ClearWave_Communications.xlsx. Ask: \"Analyse the FY2024 network outage data. Calculate: (1) The Q3 outage duration at 180 minutes vs the MCMC 120-minute threshold — what is the regulatory breach severity; (2) The estimated subscriber compensation liability if MCMC requires ClearWave to compensate all affected subscribers — based on affected subscriber count and daily ARPU; (3) The MCMC maximum penalty for a QoS threshold breach and how this compares to ClearWave's quarterly EBITDA; (4) The customer satisfaction impact — NPS score movement in the quarter following the outage versus baseline; (5) The revenue and ARPU impact if 0.5% of affected high-value subscribers churn as a result. Format as a regulatory financial impact assessment.\"",
              fileRef: "TC_01_ClearWave_Communications.xlsx"
            }
          ]
        },
        {
          tool: "📊 Copilot in Excel",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Instant ClearWave commercial performance summary",
              prompt: "Open TC_01_ClearWave_Communications.xlsx. Ask Copilot: \"Give me a plain-English executive summary of this entire workbook. What is the total subscriber base? What is the B2B enterprise revenue versus the MYR 2.1 billion target? What is the postpaid ARPU trend? What is the 5G coverage percentage versus the MCMC 20% target? Flag any metric where performance is more than 10% below target or shows 2 consecutive quarters of decline. Format: 2-sentence overview, then 4 specific flagged concerns with sheet name and row reference.\"",
              fileRef: "TC_01_ClearWave_Communications.xlsx"
            },
            {
              title: "Build 5G deployment coverage chart vs MCMC milestones",
              prompt: "Open TC_01_ClearWave_Communications.xlsx. Navigate to the 5G Deployment sheet. Ask Copilot: \"Create a line chart showing ClearWave's 5G population coverage percentage month by month from Q1 FY2023 to Q4 FY2024. Add a horizontal reference line at 20% labelled MCMC Licence Obligation. Use a red line for ClearWave's actual coverage progress and a dashed blue line for the MCMC target. Add a callout annotation at Q3 FY2024 showing the current gap of 7.6 percentage points. Chart title: ClearWave 5G Population Coverage — Actual vs MCMC Licence Obligation. This chart will be used in the MCMC bilateral presentation.\"",
              fileRef: "TC_01_ClearWave_Communications.xlsx"
            },
            {
              title: "Add B2B revenue tracking with variance analysis",
              prompt: "Open TC_01_ClearWave_Communications.xlsx. Navigate to the B2B Revenue sheet. Ask Copilot: \"Add a new column called Variance vs MYR 2.1B Target for each quarter. The formula should calculate the cumulative B2B revenue from Q1 to the current quarter and subtract it from the prorated quarterly target (MYR 525 million per quarter). Apply conditional formatting: red for quarters where the negative variance exceeds MYR 100 million, amber for MYR 50 to 100 million, green if on track. Tell me the total FY2024 B2B revenue shortfall in MYR millions and the quarterly trend — is the gap closing or widening?\"",
              fileRef: "TC_01_ClearWave_Communications.xlsx"
            },
            {
              title: "Natural language query — churn and ARPU analysis",
              prompt: "Open TC_01_ClearWave_Communications.xlsx. Ask Copilot: \"Without navigating sheets, answer: (1) What is the current postpaid churn rate and how does it compare to the industry average of 1.8% per month for Malaysian operators; (2) What is the ARPU difference between a 5G subscriber and a non-5G postpaid subscriber and does the data support the business case for 5G rollout investment; (3) Which customer segment — postpaid, prepaid, or B2B enterprise — has the highest average revenue per account; (4) In the quarter following the 180-minute outage in Q3, what was the net subscriber movement in postpaid — did we lose subscribers. Present as a 2-column Q and A table.\"",
              fileRef: "TC_01_ClearWave_Communications.xlsx"
            }
          ]
        },
        {
          tool: "📝 Copilot in Word",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Summarise ClearWave strategy into MCMC bilateral brief",
              prompt: "Open TC_02_ClearWave_Strategy.docx. Ask Copilot: \"Summarise this strategy document into a structured 1-page brief for the Group CEO to use before the MCMC bilateral meeting. Focus on: (1) ClearWave's 5G deployment commitment versus current performance at 12.4% coverage; (2) The planned 5G acceleration programme — investment committed, additional sites planned, and revised timeline; (3) The B2B enterprise growth strategy and its dependency on 5G infrastructure; (4) The QoS improvement programme following the Q3 network outage; (5) The 2 specific commitments the CEO will make to MCMC about coverage milestones and compensation. Maximum 400 words. Format as a CEO meeting brief with numbered headings.\"",
              fileRef: "TC_02_ClearWave_Strategy.docx"
            },
            {
              title: "Draft formal response to MCMC Show Cause Notice",
              prompt: "Open a new Word document. Ask Copilot: \"Draft a formal response from ClearWave Communications Berhad Group CEO to the MCMC Deputy Director General — Regulatory Affairs — responding to a Show Cause Notice issued after the 180-minute Q3 FY2024 network outage exceeded the 120-minute QoS threshold. The response must: (1) Formally acknowledge the QoS breach with exact outage dates and duration; (2) Explain the root cause — fibre cut at a critical transmission node cascaded to 3 regional exchanges; (3) Confirm immediate remediation actions: rerouting completed within 4 hours, affected subscribers credited, and root cause report submitted; (4) Commit to 4 specific network resilience investments to prevent recurrence with delivery dates; (5) Request the MCMC close the Show Cause Notice. Formal regulatory correspondence. 450 words.\""
            },
            {
              title: "Rewrite 5G enterprise proposition for non-technical customers",
              prompt: "Open TC_02_ClearWave_Strategy.docx. Locate the 5G Enterprise Services section. Ask Copilot: \"Rewrite this 5G enterprise services section in plain, commercial language for a Head of Operations at a Malaysian manufacturing company with no IT background. Remove all technical specifications — bands, latency in milliseconds, and throughput in Gbps — and replace them with real business outcomes. For each 5G enterprise use case, write 1 sentence explaining what the technology does and 1 sentence on the specific business benefit — cost saved, productivity gained, or risk reduced. Maximum 300 words. This rewrite will be used as a B2B sales leave-behind document by the ClearWave enterprise account team.\"",
              fileRef: "TC_02_ClearWave_Strategy.docx"
            },
            {
              title: "Draft 5G acceleration programme proposal memo",
              prompt: "Open a new Word document. Ask Copilot: \"Draft a formal programme proposal memo from ClearWave's Group CTO to Group CEO seeking approval to accelerate 5G rollout. The memo should cover: (1) Current position — 12.4% population coverage vs 20% MCMC commitment; (2) Proposed acceleration approach — additional capital deployment of MYR 280 million to add 600 new 5G sites by Q4 FY2025; (3) Technical approach — combination of macro sites in top 20 cities and small cell densification in industrial and commercial zones; (4) Revenue case — expected B2B revenue uplift of MYR 340 million from enterprise private 5G customers; (5) MCMC bilateral talking track — milestones we will commit to. Format as a formal Board memo requiring sign-off. 500 words.\""
            }
          ]
        },
        {
          tool: "🎯 Copilot in PowerPoint",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Create MCMC bilateral presentation for 5G and QoS",
              prompt: "Open a new PowerPoint. Ask Copilot: \"Create a 7-slide presentation for ClearWave Communications Berhad's bilateral meeting with MCMC. Slide 1: ClearWave — MCMC Bilateral Q4 FY2024 — Regulatory Update. Slide 2: 5G Deployment Progress — 12.4% actual vs 20% licence commitment with timeline. Slide 3: 5G Acceleration Programme — investment MYR 280M, additional sites, revised coverage milestones. Slide 4: Q3 Network Outage — root cause, remediation completed, subscriber compensation. Slide 5: QoS Improvement Roadmap — network resilience investments and timeline. Slide 6: B2B Enterprise 5G Commitment — how 5G deployment unlocks MYR 2.1 billion B2B revenue. Slide 7: MCMC Engagement Commitments — 3 specific milestones with dates. Corporate blue and white theme.\""
            },
            {
              title: "Generate B2B enterprise sales pitch deck",
              prompt: "Open a new PowerPoint. Ask Copilot: \"Create a 6-slide B2B enterprise sales pitch for ClearWave Communications targeting Malaysian manufacturing companies. Slide 1: ClearWave Enterprise — Your 5G Connectivity Partner. Slide 2: The Manufacturing Connectivity Challenge — operational downtime, OT-IT integration gaps, real-time data needs. Slide 3: ClearWave's Enterprise 5G Solution — private 5G, SD-WAN, IoT platform. Slide 4: Three Customer Case Studies — anonymised outcomes in manufacturing, logistics, and port operations. Slide 5: Why ClearWave — price benchmark vs Telekom Malaysia, 98.6% SLA, 24-hour NOC, local support. Slide 6: Call to Action — 30-day proof of concept offer. Modern, technology-forward design. Corporate blue and silver.\""
            },
            {
              title: "Add competitive market share benchmarking slide",
              prompt: "In an open ClearWave PowerPoint, add a new slide. Ask Copilot: \"Create a competitive market share slide for ClearWave Communications. Use a stacked bar chart showing Malaysian mobile operator market share by revenue for FY2022, FY2023, and FY2024. Include Maxis, Celcom Axiata, Digi, ClearWave, and U Mobile. Show ClearWave's market share trend. Add a callout box showing ClearWave's total subscriber base at 14.8 million and a 2-sentence commentary on market position. Title: ClearWave Market Position — Malaysian Mobile Market FY2022-FY2024. This slide is for the investor relations presentation.\""
            }
          ]
        },
        {
          tool: "📧 Copilot in Outlook",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Triage MCMC Show Cause Notice email",
              prompt: "Open Outlook and locate the email from Email_05_MCMC_Notice.docx — copy the content into a draft or open the forwarded email. Ask Copilot to summarise: \"I am the ClearWave Group CEO and I have just received a forwarded copy of this MCMC correspondence. Summarise for me: (1) What regulatory breach is MCMC citing and what evidence are they relying on; (2) What is the response deadline and what specifically must I submit; (3) Is there a penalty indicated or is this a preliminary notice only; (4) The 3 most urgent internal actions I need to assign in the next 2 hours before MCMC business hours start. Format under 4 headings. Maximum 150 words.\"",
              fileRef: "Email_05_MCMC_Notice.docx"
            },
            {
              title: "Draft CEO response to top enterprise customer threatening churn",
              prompt: "Open a new Outlook email. Ask Copilot: \"Draft a personal email from ClearWave Group CEO to the CEO of a top enterprise account — a Malaysian bank with 8,000 ClearWave SIM cards and MYR 14.4 million annual contract value — who has emailed to express severe dissatisfaction after the Q3 180-minute outage affected their branch network connectivity across 48 branches. The email should: (1) Acknowledge the operational impact on the customer's business directly and personally; (2) Confirm the compensation applied — prorated credit and service quality audit committed; (3) Offer a dedicated account service review and technology upgrade consultation; (4) Invite the customer CEO to a private briefing on ClearWave's network investment programme. Personal, senior, non-defensive. Under 300 words.\""
            },
            {
              title: "Copilot coaching on ClearWave B2B proposal email",
              prompt: "In Outlook, type a rough email draft to a prospective enterprise customer: \"Hi, I wanted to follow up on our 5G proposal we sent last week. We have a good network and competitive prices. Please let me know if you want to proceed or if you have questions. Regards, ClearWave B2B Team.\" Ask Copilot for coaching: \"I am a B2B enterprise sales director writing to a Malaysian conglomerate Head of IT. Evaluate my draft on 3 dimensions: (1) Personalization — does it reference the customer's specific needs; (2) Value proposition — does it communicate a clear business outcome; (3) Call to action — is it specific and easy to act on. Rewrite the email with a specific reference to their industry, a measurable ROI claim, and a concrete next step.\""
            }
          ]
        },
        {
          tool: "🎙 Copilot in Teams",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Catch up on missed 5G network operations review",
              prompt: "Open an existing Teams meeting that was recorded and has a Copilot recap — a technical, operations, or project meeting from your calendar. In the Copilot recap pane, ask: \"I am the ClearWave VP Network who missed this meeting. Catch me up with a structured brief: (1) What was the main technical or network topic discussed — summarise in 2 sentences; (2) Were any 5G deployment decisions made — new site approvals, contractor changes, spectrum allocation; (3) Any network incident or SLA breach discussed and the responsible team; (4) Specific action items assigned to the VP Network or the network planning team; (5) Is there any critical path decision needed in the next 48 hours for the MCMC bilateral preparation.\""
            },
            {
              title: "Extract B2B sales pipeline actions from commercial review",
              prompt: "Open an existing recorded Teams meeting from your calendar — a sales, commercial, or executive meeting. In the Copilot recap pane, ask: \"Extract all B2B enterprise sales pipeline actions and commercial commitments from this meeting. Format as a table: Account Name (or Anonymous if not named); Opportunity Value MYR M; Next Action; Owner; Deadline; Status — Active, Stalled, or At Risk. Highlight in red any account marked as At Risk or where the next action deadline has already passed. Also note: was the MYR 2.1 billion B2B revenue target discussed — if so, what was the forecast gap and recovery plan mentioned?\""
            },
            {
              title: "Draft B2B team update email from weekly pipeline meeting",
              prompt: "Open an existing recorded Teams meeting recap from your calendar. In the Copilot recap pane, ask: \"Draft a B2B Enterprise Sales team update email from the VP Enterprise to be sent to all 24 account managers. Based on this meeting: (1) Summarise the 3 key messages about pipeline progress and priorities for this week; (2) List all specific account actions that were assigned with owner and deadline; (3) Call out any account at risk of churning or delaying a deal close; (4) Confirm the quarterly pipeline target and current forecast coverage. Professional sales leadership communication. Motivating but direct. Under 250 words.\""
            }
          ]
        },
        {
          tool: "📓 Copilot Notebook",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Full MCMC bilateral brief from 3 documents",
              prompt: "Go to Copilot Notebook. Upload TC_01_ClearWave_Communications.xlsx, TC_02_ClearWave_Strategy.docx, and Email_05_MCMC_Notice.docx. In Instructions: \"Using all 3 documents, prepare a comprehensive MCMC bilateral meeting brief for ClearWave CEO. (1) From the MCMC notice email — what exactly is MCMC requiring, what is the deadline, and what is the regulatory risk level; (2) From the strategy document — what is ClearWave's plan to close the 5G gap and when; (3) From the operational data — what does the current 5G deployment pace and QoS data say about credibility of the plan; (4) Build a 3-point CEO talking track for the MCMC bilateral; (5) Identify any gap between the strategy document commitments and the actual data that MCMC could challenge. Format as a structured bilateral brief.\"",
              fileRef: "TC_01_ClearWave_Communications.xlsx, TC_02_ClearWave_Strategy.docx, Email_05_MCMC_Notice.docx"
            },
            {
              title: "B2B enterprise market opportunity and strategy analysis",
              prompt: "Go to Copilot Notebook. Upload TC_01_ClearWave_Communications.xlsx and TC_02_ClearWave_Strategy.docx. In Instructions: \"Using both documents, develop a B2B enterprise revenue acceleration analysis for the ClearWave VP Enterprise. (1) From the financial data — what is the current B2B revenue run rate and the MYR 2.1 billion target gap; (2) From the strategy document — which B2B customer segments and product lines are prioritised for growth; (3) Cross-reference: which B2B product lines have shown the highest revenue growth rate in the financial data — do they align with the strategy; (4) Identify the top 3 B2B growth opportunities that combine highest revenue potential with the fastest timeline to revenue. Format as an enterprise sales leadership decision brief.\"",
              fileRef: "TC_01_ClearWave_Communications.xlsx, TC_02_ClearWave_Strategy.docx"
            }
          ]
        },
        {
          tool: "🤝 Cowork (Pages)",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Build MCMC compliance tracker in Pages",
              prompt: "In Copilot Chat, upload TC_01_ClearWave_Communications.xlsx and ask for a regulatory compliance summary. Click Open in Copilot Pages. Ask: \"Reorganise this into a collaborative MCMC Regulatory Compliance Tracker for the ClearWave Regulatory team of 5 members. Structure as: (1) 5G Coverage Obligation Tracker — monthly milestones from now to the 20% target with RAG status; (2) QoS Performance Monitor — monthly outage metrics vs 120-minute threshold; (3) Show Cause Response Tracker — submission status and deadline; (4) Bilateral Meeting Preparation — open items and owner; (5) Regulator Engagement Log — all MCMC correspondence with dates. Format for collaborative editing by the Regulatory Director and 4 specialists.\"",
              fileRef: "TC_01_ClearWave_Communications.xlsx"
            },
            {
              title: "Build B2B enterprise sales acceleration canvas",
              prompt: "In Copilot Chat, upload TC_02_ClearWave_Strategy.docx and ask for a B2B enterprise growth strategy summary. Click Open in Copilot Pages. Ask: \"Expand this into a collaborative B2B Enterprise Sales Acceleration Canvas for the ClearWave VP Enterprise and 4 regional sales directors. Structure as: (1) Target Market Priorities — top 5 industry segments with revenue potential; (2) Product Portfolio Map — which 5G enterprise product targets which segment; (3) Top 20 Account Target List — for regional sales directors to populate; (4) Conversion Tactics — 3 proven approaches per product type; (5) Weekly Pipeline Review cadence. Format for collaborative input from all 4 regional teams simultaneously.\"",
              fileRef: "TC_02_ClearWave_Strategy.docx"
            }
          ]
        },
        {
          tool: "🤖 Word Agent",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Set up a ClearWave Strategy Advisor on the strategy doc",
              prompt: "Open TC_02_ClearWave_Strategy.docx in Word. Create an agent named ClearWave Strategy Advisor. Instructions: \"Answer questions about ClearWave's commercial and regulatory strategy. Cite document sections. Keep answers under 150 words.\" Demo: type \"What is ClearWave's plan to reach 20% 5G population coverage and by what date does the strategy commit to achieving it?\"",
              fileRef: "TC_02_ClearWave_Strategy.docx"
            },
            {
              title: "Demo the Strategy Advisor — leadership queries",
              prompt: "With the ClearWave Strategy Advisor active, ask 3 queries a Board member or regulator would ask. Query 1: \"What specific capital investment is committed to 5G deployment acceleration and over what timeline?\" Query 2: \"How does ClearWave plan to grow B2B enterprise revenue to MYR 2.1 billion — which customer segments and product lines are the priority?\" Query 3: \"Is there a contingency plan in the strategy if MCMC imposes a penalty or licence variation for the 5G coverage gap?\" Demonstrate how a dense telco strategy document becomes instantly searchable.",
              fileRef: "TC_02_ClearWave_Strategy.docx"
            }
          ]
        },
        {
          tool: "🤖 PowerPoint Agent",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Set up an MCMC Bilateral Presenter agent",
              prompt: "Create or open the MCMC bilateral PowerPoint from the PPT demo. Save as ClearWave_MCMC_Bilateral_2025.pptx. Create an agent named MCMC Meeting Coach. Instructions: \"Answer questions about the content of ClearWave's MCMC bilateral presentation. Reference slide numbers. Keep answers under 100 words.\" Demo: type \"Which slide covers the 5G acceleration programme and what is the committed coverage milestone for Q2 FY2025?\""
            },
            {
              title: "Demo the MCMC Meeting Coach — regulatory prep",
              prompt: "With the MCMC Meeting Coach active, run 3 queries simulating CEO bilateral preparation. Query 1: \"If the MCMC Chairman asks why we have not met the 20% 5G commitment, which slide has the most credible explanation?\" Query 2: \"What is the total investment we are committing to network resilience improvements — which slide details this?\" Query 3: \"Does the presentation address subscriber compensation for the Q3 outage and if so, what slide and what is the total amount?\" Show how an executive can prepare for a regulator meeting in 5 minutes."
            }
          ]
        },
        {
          tool: "🤖 Excel Agent",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Set up a ClearWave Commercial Data agent",
              prompt: "Open TC_01_ClearWave_Communications.xlsx. Create an agent named ClearWave Commercial Advisor. Instructions: \"Answer commercial and network performance questions using data from this workbook. Always cite sheet name. Express revenue in MYR millions.\" Demo: type \"What is the current B2B enterprise revenue run rate in MYR millions and how large is the gap to the MYR 2.1 billion full-year target?\"",
              fileRef: "TC_01_ClearWave_Communications.xlsx"
            },
            {
              title: "Demo the Commercial Advisor — CEO queries",
              prompt: "With the ClearWave Commercial Advisor active, simulate 3 CEO-level queries. Query 1: \"What is the total revenue impact of postpaid subscriber churn in Q3 and Q4 FY2024 combined — in MYR millions?\" Query 2: \"What percentage of ClearWave's 14.8 million subscribers are on 5G-enabled plans and what is the ARPU premium compared to 4G subscribers?\" Query 3: \"Which B2B industry vertical — financial services, manufacturing, or government — contributed the most incremental B2B revenue in FY2024?\" Demonstrate natural language data interrogation of a complex commercial workbook.",
              fileRef: "TC_01_ClearWave_Communications.xlsx"
            }
          ]
        }
      ]
    },
    {
      id: "insurance",
      name: "Insurance",
      icon: "🛡️",
      color: "#4A235A",
      accent: "#8E44AD",
      company: "Pacific Shield Insurance Berhad",
      tagline: "Motor combined ratio 108% | SWIFT CLAIM fraud AI | UBI 8,400 pilots | MYR 3.84B GWP",
      scenario: "Pacific Shield Insurance Berhad (Pacific Shield) is a Malaysian composite insurer with MYR 3.84 billion in gross written premium across motor, medical, fire, and marine lines. The motor portfolio is under severe profitability pressure with a combined ratio of 108% driven by organised claims fraud and inflated workshop repair invoices — triggering heightened BNM supervisory attention. Two strategic responses are in flight: SWIFT CLAIM, an AI-powered claims fraud detection system whose Phase 1 identified MYR 12.4 million in fraudulent claims, and a UBI telematics pilot with 8,400 policyholders generating significantly better loss ratios than the standard motor book. CEO Farida Mensah and Chief Actuarial Officer Kemi Oduola need Copilot to build the BNM remediation case, accelerate the SWIFT CLAIM Phase 2 investment case, and manage broker and regulatory communications.",
      files: ["INS_01_Pacific_Shield_Insurance.xlsx", "INS_02_Pacific_Shield_Strategy.docx", "Email_04_BNM_Insurance_Direction.docx"],
      prompts: [
        {
          tool: "🤖 Copilot Chat (Basic)",
          license: "Free — no M365 license needed",
          account: "Sasha Ouellet — SashaO@ABSx62256373.OnMicrosoft.com",
          prompts: [
            {
              title: "Explain combined ratio and why 108% is a crisis",
              prompt: "Ask Copilot: \"Explain what a motor insurance combined ratio is and why Pacific Shield Insurance's motor combined ratio of 108% represents a serious profitability crisis. Specifically: (1) Define combined ratio and the formula — claims incurred plus expenses divided by earned premium; (2) Why the break-even point is 100% and what a 108% ratio means for underwriting loss in MYR per MYR of premium collected; (3) What industry benchmarks Malaysian general insurers maintain — BNM industry data for motor combined ratio; (4) What BNM's supervisory expectations are when an insurer's motor book combined ratio exceeds 105% for 2 consecutive quarters; (5) The 3 most common root causes of elevated motor combined ratio in the Malaysian market. Maximum 250 words.\""
            },
            {
              title: "Brief me on the SWIFT CLAIM AI fraud detection project",
              prompt: "Ask Copilot: \"I am the CTO of Pacific Shield Insurance Berhad, a Malaysian general insurer with MYR 3.84 billion in gross written premium. We have a project called SWIFT CLAIM that uses AI to detect fraudulent motor claims. Brief me on the technical and business context: (1) What specific types of motor insurance fraud patterns does AI and machine learning detect most effectively — staged accidents, duplicate claims, inflated repair estimates; (2) What is a typical fraud detection rate improvement from deploying ML-based claims fraud detection — industry benchmark before and after; (3) What data inputs does such a system typically use — telematics, workshop repair patterns, claims history; (4) What BNM RMiT compliance considerations apply to AI-based claims decisioning in Malaysia. Maximum 250 words.\""
            },
            {
              title: "What is UBI insurance and how does it work?",
              prompt: "Ask Copilot: \"Explain usage-based insurance (UBI) in plain English for a Malaysian general insurance Board of Directors. Pacific Shield has 8,400 UBI policyholders in a pilot programme. Cover: (1) What is UBI and how does telematics data — GPS, accelerometer, braking — translate into a personalised premium; (2) How does UBI change the risk selection and adverse selection problem in motor insurance; (3) What is the expected claims frequency difference between UBI policyholders and standard policyholders based on published industry data; (4) The 3 main technology and data privacy challenges to scaling UBI in Malaysia under PDPA 2010; (5) What scale — number of policyholders and years of data — is needed before UBI delivers a measurable combined ratio benefit. Maximum 250 words.\""
            }
          ]
        },
        {
          tool: "�� Researcher",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Research motor insurance fraud detection and InsurTech in Malaysia",
              prompt: "In Copilot Chat, switch to the Researcher agent. Upload INS_02_Pacific_Shield_Strategy.docx. Ask: \"Review Pacific Shield's strategy document, then search the web for: AI and machine learning claims fraud detection platforms deployed by Asian general insurers between 2022 and 2025; BNM's Regulatory Sandbox outcomes for InsurTech fraud solutions; Malaysian motor insurance fraud statistics and the estimated annual fraud cost across the industry; and UBI telematics platforms available in Southeast Asia. Cross-reference with Pacific Shield's current SWIFT CLAIM project and UBI pilot to identify the 3 most high-impact technology investments that could reduce the motor combined ratio from 108% toward 100%. Cite all sources.\"",
              fileRef: "INS_02_Pacific_Shield_Strategy.docx"
            },
            {
              title: "Research medical inflation management strategies",
              prompt: "In Copilot Chat, switch to the Researcher agent. Ask: \"Search the web for strategies to manage 12.4% medical claims inflation in group medical insurance products. Find: the current Malaysian medical inflation rate data from BNM, ISM, and major reinsurers — Munchener Re and Swiss Re reports; network pricing and preferred provider organisation models used by Malaysian insurers to contain medical cost inflation; prior authorisation and managed care integration approaches that reduce unnecessary utilisation; and clinical pathway and DRG-based claims adjudication models. Pacific Shield has a 12.4% medical inflation figure. What are the 5 proven strategies to reduce effective claims cost without losing policyholder NPS? Cite sources.\""
            },
            {
              title: "Research UBI and telematics scaling opportunities",
              prompt: "In Copilot Chat, switch to the Researcher agent. Upload INS_01_Pacific_Shield_Insurance.xlsx. Ask: \"Review Pacific Shield's UBI programme data. Then search the web for: UBI programme scaling benchmarks — how many policyholders does a programme need before producing statistically significant risk differentiation; telematics data providers operating in Malaysia and Indonesia; Privacy Impact Assessment requirements for telematics data under Malaysia's PDPA 2010 and Indonesia's PDP Law; and international case studies of UBI programmes that reached 50,000+ policyholders in ASEAN markets. Pacific Shield currently has 8,400 UBI policyholders. What is the roadmap to scale to 50,000 and what will be the combined ratio impact at that scale?\"",
              fileRef: "INS_01_Pacific_Shield_Insurance.xlsx"
            }
          ]
        },
        {
          tool: "📊 Analyst",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Analyse Pacific Shield portfolio profitability by product line",
              prompt: "In Copilot Chat, switch to the Analyst agent. Upload INS_01_Pacific_Shield_Insurance.xlsx. Ask: \"Analyse Pacific Shield's insurance portfolio. Calculate: (1) Combined ratio by product line — motor, medical, fire, and marine — identify which lines are profitable and which are loss-making; (2) The motor segment underwriting loss in MYR millions at a 108% combined ratio on the motor gross written premium; (3) The medical line claims inflation rate by year from FY2022 to FY2024 — confirm whether the 12.4% medical inflation figure is consistent with the data; (4) The UBI pilot — compare claims frequency and average claims cost for UBI policyholders versus standard motor policyholders — is the UBI segment already outperforming; (5) Gross written premium growth rate by line. Present as a Group CEO underwriting performance dashboard.\"",
              fileRef: "INS_01_Pacific_Shield_Insurance.xlsx"
            },
            {
              title: "Model SWIFT CLAIM fraud detection ROI",
              prompt: "In Copilot Chat, switch to the Analyst agent. Upload INS_01_Pacific_Shield_Insurance.xlsx. Ask: \"Model the financial ROI of the SWIFT CLAIM AI fraud detection project. Inputs from the workbook: total motor claims paid MYR millions, estimated fraud rate before AI — use 8% industry estimate, projected fraud detection improvement — from 12% detection to 68% detection post-deployment. Calculate: (1) The annual fraud cost currently being paid out in MYR millions; (2) The annual savings from detecting 68% of fraudulent claims versus 12%; (3) The 3-year cumulative saving and the payback period on a MYR 8.4 million project investment; (4) The combined ratio improvement in percentage points from fraud reduction alone. Format as a Board technology investment case with clear financial ROI.\"",
              fileRef: "INS_01_Pacific_Shield_Insurance.xlsx"
            },
            {
              title: "Analyse UBI programme performance and scaling pathway",
              prompt: "In Copilot Chat, switch to the Analyst agent. Upload INS_01_Pacific_Shield_Insurance.xlsx. Ask: \"Analyse the UBI pilot programme performance data for Pacific Shield. Calculate: (1) Claims frequency for UBI policyholders vs standard motor policyholders — is the UBI cohort lower risk as expected; (2) Average claims cost per incident for UBI vs standard; (3) The combined ratio for the UBI segment specifically — is it already below 100%; (4) Premium retention rate for UBI policyholders at renewal versus standard motor — are UBI customers stickier; (5) At 8,400 current UBI policyholders, what scale needs to be reached — and by when — before UBI meaningfully reduces the motor book combined ratio below 104%. Format as a product scaling investment case.\"",
              fileRef: "INS_01_Pacific_Shield_Insurance.xlsx"
            }
          ]
        },
        {
          tool: "📊 Copilot in Excel",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Instant Pacific Shield underwriting performance summary",
              prompt: "Open INS_01_Pacific_Shield_Insurance.xlsx. Ask Copilot: \"Give me a plain-English executive summary of this insurance portfolio workbook. What is the overall motor combined ratio and in which quarters did it exceed 105%? What is the total gross written premium and the year-on-year growth rate? Which product line has the worst combined ratio? What is the UBI segment's claims frequency compared to the standard motor segment? Flag any product line where the combined ratio has exceeded 100% for 3 or more consecutive quarters. Format: 3-sentence overview, then 4 specific data concerns with sheet name and row reference.\"",
              fileRef: "INS_01_Pacific_Shield_Insurance.xlsx"
            },
            {
              title: "Build combined ratio trend chart by product line",
              prompt: "Open INS_01_Pacific_Shield_Insurance.xlsx. Navigate to the Underwriting Performance sheet. Ask Copilot: \"Create a multi-line chart showing the quarterly combined ratio trend from Q1 FY2022 to Q4 FY2024 for 4 product lines: Motor, Medical, Fire, and Marine. Use red for Motor, blue for Medical, green for Fire, and orange for Marine. Add a horizontal dashed black line at 100% labelled Break-Even. Add data labels at Q4 FY2024 for each line showing the exact ratio. Title: Pacific Shield Insurance — Combined Ratio Trend by Product Line. This chart will be used in the Actuarial Committee presentation to the BNM-supervised internal audit.\"",
              fileRef: "INS_01_Pacific_Shield_Insurance.xlsx"
            },
            {
              title: "Add UBI versus standard motor comparison table",
              prompt: "Open INS_01_Pacific_Shield_Insurance.xlsx. Navigate to the UBI Analysis sheet. Ask Copilot: \"Create a comparison table showing 4 key metrics for the UBI segment versus the Standard Motor segment: Claims Frequency per 100 policyholders, Average Claims Cost MYR, Combined Ratio %, and Premium Retention Rate at Renewal %. Calculate the absolute and percentage difference for each metric between UBI and Standard. Apply green formatting where UBI outperforms Standard and red where it underperforms. Tell me whether the UBI pilot is performing as expected and what the 3 most significant differences between the two segments are.\"",
              fileRef: "INS_01_Pacific_Shield_Insurance.xlsx"
            },
            {
              title: "Natural language query — SWIFT CLAIM fraud project impact",
              prompt: "Open INS_01_Pacific_Shield_Insurance.xlsx. Ask Copilot: \"Without navigating sheets, answer: (1) What was the total motor claims paid in FY2024 and what percentage of this is estimated to be fraudulent based on the 8% industry fraud rate; (2) What would be the combined ratio if all fraudulent motor claims were successfully prevented — calculate the new combined ratio assuming fraud-free claims; (3) How many unique motor claims were processed in FY2024 and how many involved third-party workshops flagged as high-risk; (4) What was the largest single motor claims batch payment in FY2024 and which workshop processed it. Present as a 2-column Q and A table for the Chief Claims Officer.\"",
              fileRef: "INS_01_Pacific_Shield_Insurance.xlsx"
            }
          ]
        },
        {
          tool: "📝 Copilot in Word",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Summarise Pacific Shield strategy into Board pre-read",
              prompt: "Open INS_02_Pacific_Shield_Strategy.docx. Ask Copilot: \"Summarise this strategy document into a 1-page Board pre-read for Pacific Shield Insurance Berhad. Include: (1) The 2 most material challenges — motor combined ratio 108% and medical inflation 12.4% — with the BNM supervisory risk implication; (2) The 3 strategic responses — SWIFT CLAIM fraud project, UBI programme scaling, and medical managed care partnership; (3) Capital and technology investment requested for FY2025; (4) The 2 Board decisions required: SWIFT CLAIM Phase 2 budget approval and UBI scaling mandate. Formal Board memo style. Non-executive director audience. Maximum 400 words.\"",
              fileRef: "INS_02_Pacific_Shield_Strategy.docx"
            },
            {
              title: "Draft BNM engagement letter on motor combined ratio",
              prompt: "Open a new Word document. Ask Copilot: \"Draft a proactive engagement letter from Pacific Shield Insurance Berhad CEO to BNM's Insurance Regulation and Prudential Supervision Director sharing our motor combined ratio remediation plan. The letter should: (1) Acknowledge the elevated motor combined ratio at 108% and our commitment to BNM's supervisory expectations; (2) Present the 3-pillar remediation plan: SWIFT CLAIM AI fraud detection going live Q1 FY2025, UBI programme scaling to 50,000 policyholders by FY2026, and 8 high-fraud workshop deregistrations completed in Q4 FY2024; (3) Provide the projected combined ratio improvement trajectory to 103% by Q4 FY2025 and 99% by FY2026; (4) Request a bilateral meeting to present the full actuarial model. Formal regulatory correspondence. 400 words.\""
            },
            {
              title: "Rewrite motor claims SOP for frontline staff",
              prompt: "Open INS_02_Pacific_Shield_Strategy.docx. Locate the Motor Claims Management section. Ask Copilot: \"Rewrite this motor claims management section in plain operational language for Pacific Shield's frontline claims handlers — staff who receive first notification of loss calls and process motor claims assessments. Replace all actuarial and regulatory terms with practical instructions. Add a simple decision tree: when should a claims handler refer a claim to the SWIFT CLAIM fraud screening queue versus processing it as a standard claim. The rewritten version should be under 350 words, use numbered steps, and include a 5-item checklist for high-value claims above MYR 30,000.\"",
              fileRef: "INS_02_Pacific_Shield_Strategy.docx"
            },
            {
              title: "Draft SWIFT CLAIM Phase 2 business case memo",
              prompt: "Open a new Word document. Ask Copilot: \"Draft a formal business case memo from Pacific Shield's Chief Claims Officer to Group CEO seeking Board approval for SWIFT CLAIM AI Fraud Detection System Phase 2. Phase 1 deployed in Q3 FY2024 with 3-month results: 847 fraudulent claims identified and declined, estimated fraud savings MYR 12.4 million, false positive rate 2.1%. Phase 2 adds: telematics integration for staged accident detection, workshop invoice AI analysis, and real-time fraud score API. Investment required: MYR 4.8 million. Expected Phase 2 annual fraud savings: MYR 28 million. Combined ratio improvement contribution: 1.8 percentage points. Formal Board memo format. 500 words.\""
            }
          ]
        },
        {
          tool: "🎯 Copilot in PowerPoint",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Create BNM supervisory engagement presentation",
              prompt: "Open a new PowerPoint. Ask Copilot: \"Create a 7-slide supervisory engagement presentation for Pacific Shield Insurance Berhad to present to Bank Negara Malaysia's Insurance Regulation department. Slide 1: Pacific Shield — FY2024 Performance Review and Remediation Update. Slide 2: Portfolio Overview — MYR 3.84B GWP, product mix, and market position. Slide 3: Motor Combined Ratio Deep Dive — 108% current, root causes, and trajectory. Slide 4: SWIFT CLAIM Fraud Detection — project status, Phase 1 results, Phase 2 plan. Slide 5: UBI Programme — 8,400 policyholders, performance data, scaling roadmap. Slide 6: Combined Ratio Remediation Roadmap — quarterly targets to FY2026. Slide 7: Governance and Oversight Commitments. Corporate dark blue and white. Professional.\""
            },
            {
              title: "Generate InsurTech transformation strategy deck",
              prompt: "Open a new PowerPoint. Ask Copilot: \"Create a 5-slide technology transformation strategy presentation for Pacific Shield Insurance Berhad's Board Technology Committee. Slide 1: Why Pacific Shield Must Digitally Transform — combined ratio pressure, claims fraud, customer expectations. Slide 2: SWIFT CLAIM AI — technology architecture, fraud detection model, Phase 1 results. Slide 3: UBI Telematics Platform — data flow, risk scoring model, privacy compliance. Slide 4: Customer Digital Journey — app, FNOL, claims tracking, renewal. Slide 5: Technology Investment Plan FY2025-FY2027 — total MYR 42 million, 3 platforms, expected combined ratio benefit. Modern technology design. Dark navy blue and tech orange accents.\""
            },
            {
              title: "Add motor fraud analytics benchmarking slide",
              prompt: "In an open Pacific Shield PowerPoint, add a new slide. Ask Copilot: \"Create a motor insurance fraud benchmarking slide comparing Pacific Shield's fraud detection rate before and after SWIFT CLAIM versus 3 Malaysian and regional insurance benchmarks. Show: Pre-SWIFT CLAIM detection rate 12%, Post Phase 1 detection rate 41%, Industry average 28%, and Best-in-class 68%. Use a vertical bar chart with red for Pacific Shield pre, orange for post Phase 1, grey for industry average, and green for best-in-class. Add a callout showing the MYR 12.4 million Phase 1 savings and the target for Phase 2. Title: SWIFT CLAIM — Fraud Detection Performance vs Industry. For the Group Board IT and Technology Committee.\""
            }
          ]
        },
        {
          tool: "📧 Copilot in Outlook",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Triage BNM supervisory letter on motor combined ratio",
              prompt: "Open Outlook and locate Email_04_BNM_Insurance_Direction.docx. Copy into a draft or open the forwarded email. Ask Copilot to summarise: \"I am Pacific Shield's Chief Actuarial Officer and I have received this BNM supervisory letter forwarded by our CEO. Summarise: (1) What specific concern is BNM raising and what data are they citing — is it our motor combined ratio, our reserves, or something else; (2) What is BNM formally requiring us to submit and by what deadline; (3) Are there any early signals this could escalate to a formal supervisory intervention or increased capital surcharge; (4) The 3 most urgent internal actions I must kick off in the next 48 hours. Format under 4 headings. Maximum 200 words.\"",
              fileRef: "Email_04_BNM_Insurance_Direction.docx"
            },
            {
              title: "Draft CEO letter to top corporate broker on medical pricing",
              prompt: "Open a new Outlook email. Ask Copilot: \"Draft a formal letter from Pacific Shield Group CEO to the Managing Director of a top insurance broker — a firm that places MYR 180 million of corporate medical insurance business annually with Pacific Shield. The letter addresses a necessary 18% premium renewal increase on all group medical policies for FY2025, driven by 12.4% medical claims inflation and utilisation creep. The letter should: (1) Acknowledge the partnership and the increase impact honestly; (2) Explain the 3 data-driven reasons for the increase with specific numbers; (3) Offer 3 value-adds to soften the increase — claims analytics dashboard, wellness programme partnership, managed care integration; (4) Invite a joint review meeting. Professional, transparent, 350 words.\""
            },
            {
              title: "Copilot coaching on motor claims denial letter",
              prompt: "In Outlook, type a rough claims denial draft: \"Dear policyholder, your motor claim has been declined because we found that the accident was staged based on our investigation. You have 30 days to appeal. Regards, Pacific Shield Claims.\" Ask Copilot for coaching: \"I am a senior claims manager at an insurer. Evaluate this denial letter on: (1) Legal and regulatory compliance — does it meet BNM's Insurance Act 1996 requirements for a written reasons for denial; (2) Customer experience — does it treat the customer fairly even in a fraud case; (3) Appeal clarity — does it give the customer enough information to exercise their appeal rights. Rewrite the letter at a compliant, fair, and professional standard.\""
            }
          ]
        },
        {
          tool: "🎙 Copilot in Teams",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Catch up on missed motor underwriting review meeting",
              prompt: "Open an existing Teams meeting that was recorded and has a Copilot recap from your calendar. In the Copilot recap pane ask: \"I am Pacific Shield's Chief Underwriting Officer and I missed this meeting due to a BNM call. Catch me up: (1) What was the main topic of discussion — was it motor pricing, claims experience, or the SWIFT CLAIM project; (2) What underwriting decisions were made — new pricing bands, workshop deregistrations, or policy wording changes; (3) Any fraud case or suspicious claims batch discussed; (4) Any specific action assigned to the Underwriting team with deadline; (5) Was the motor combined ratio trajectory discussed — if so, what was the assessment of the Q4 forecast.\""
            },
            {
              title: "Extract claims operations actions from the weekly review",
              prompt: "Open an existing recorded Teams meeting from your calendar. In the Copilot recap pane ask: \"Extract all claims operations and fraud management action items from this meeting. Format as a claims action register: Action Description; Owner (full name); Department; Deadline; Category — Fraud Investigation, Workshop Management, Claims Processing, or SWIFT CLAIM Project. Highlight Critical priority for any action where a BNM submission deadline is involved. Also note: was any workshop recommended for deregistration from the approved repairer panel — if so, which ones and who made the recommendation?\""
            },
            {
              title: "Generate claims team briefing from the fraud review meeting",
              prompt: "Open an existing recorded Teams meeting recap from your calendar. In the Copilot recap pane ask: \"Draft a claims team briefing email from the Chief Claims Officer to all 84 motor claims handlers and 12 fraud investigators. Based on this meeting: (1) Summarise the 3 key messages about claims fraud trends and operational priorities for this week; (2) List new SWIFT CLAIM workflow instructions or rule changes that take effect immediately; (3) Call out any specific fraud patterns or workshops to flag for enhanced scrutiny; (4) Confirm monthly claims volume targets and current performance. Professional claims operations communication. Direct and operationally specific. Under 250 words.\""
            }
          ]
        },
        {
          tool: "📓 Copilot Notebook",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Full BNM supervisory brief from 3 insurance documents",
              prompt: "Go to Copilot Notebook. Upload INS_01_Pacific_Shield_Insurance.xlsx, INS_02_Pacific_Shield_Strategy.docx, and Email_04_BNM_Insurance_Direction.docx. In Instructions: \"Using all 3 documents, prepare a BNM supervisory engagement brief for Pacific Shield CEO and CAO. (1) From the BNM letter — what is the regulator specifically asking for and what is the deadline; (2) From the financial data — what does the motor combined ratio data show for the quarters BNM is likely to cite; (3) From the strategy — is the remediation plan credible and specific enough to satisfy a BNM supervisor; (4) Are there any gaps or inconsistencies between the strategy document and the actual performance data that BNM could challenge; (5) Build a 3-point CEO talking track for the BNM bilateral meeting.\"",
              fileRef: "INS_01_Pacific_Shield_Insurance.xlsx, INS_02_Pacific_Shield_Strategy.docx, Email_04_BNM_Insurance_Direction.docx"
            },
            {
              title: "SWIFT CLAIM and UBI technology ROI analysis",
              prompt: "Go to Copilot Notebook. Upload INS_01_Pacific_Shield_Insurance.xlsx and INS_02_Pacific_Shield_Strategy.docx. In Instructions: \"Using both documents, build a technology investment ROI analysis for Pacific Shield's Board Technology Committee. For 2 technology projects: SWIFT CLAIM AI fraud detection and UBI telematics programme. For each project analyse: (1) What does the strategy document commit to in terms of investment and expected outcomes; (2) What does the financial data show about the current baseline problem — fraud cost for SWIFT CLAIM, claims frequency differential for UBI; (3) What is the combined ratio improvement each project is expected to deliver and by when; (4) Is the strategy document's financial case internally consistent with the data in the workbook. Format as a 2-project investment case summary for the Board.\"",
              fileRef: "INS_01_Pacific_Shield_Insurance.xlsx, INS_02_Pacific_Shield_Strategy.docx"
            }
          ]
        },
        {
          tool: "🤝 Cowork (Pages)",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Build motor combined ratio remediation tracker",
              prompt: "In Copilot Chat, upload INS_01_Pacific_Shield_Insurance.xlsx and ask for a motor underwriting performance summary. Click Open in Copilot Pages. Ask: \"Reorganise this into a collaborative Motor Combined Ratio Remediation Tracker for the Pacific Shield Underwriting Committee of 6 members. Structure as: (1) Combined Ratio Dashboard — current vs target by quarter; (2) Remediation Workstream Tracker — SWIFT CLAIM, UBI scaling, workshop deregistration, medical managed care — with owner and status; (3) BNM Reporting Calendar — submission dates and checklist; (4) Fraud Intelligence Log — workshop patterns flagged for investigation; (5) Weekly Status Update section. Format for collaborative editing by all 6 committee members.\"",
              fileRef: "INS_01_Pacific_Shield_Insurance.xlsx"
            },
            {
              title: "Build SWIFT CLAIM project management canvas",
              prompt: "In Copilot Chat, upload INS_02_Pacific_Shield_Strategy.docx and ask for a SWIFT CLAIM project summary. Click Open in Copilot Pages. Ask: \"Expand this into a collaborative SWIFT CLAIM Project Management Canvas for the Pacific Shield IT and Claims teams, 12 members total. Structure as: (1) Project Status and Phase 2 Roadmap; (2) Technical Integration Tracker — 4 integration streams with completion status; (3) Fraud Model Performance Log — weekly detection rate and false positive rate; (4) Workshop Risk Register — approved repairers under enhanced monitoring; (5) BNM Approval and Compliance Status. Format for daily collaborative updates by the Project Manager and 4 technical stream leads.\"",
              fileRef: "INS_02_Pacific_Shield_Strategy.docx"
            }
          ]
        },
        {
          tool: "🤖 Word Agent",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Set up a Pacific Shield Strategy Advisor",
              prompt: "Open INS_02_Pacific_Shield_Strategy.docx in Word. Create an agent named Pacific Shield Advisor. Instructions: \"Answer questions about Pacific Shield Insurance's strategy, SWIFT CLAIM project, and UBI programme. Cite document sections. Keep answers under 150 words.\" Demo: type \"What is the Phase 2 investment for SWIFT CLAIM and what combined ratio improvement does Phase 2 aim to achieve?\"",
              fileRef: "INS_02_Pacific_Shield_Strategy.docx"
            },
            {
              title: "Demo the Pacific Shield Advisor — Board-level queries",
              prompt: "With the agent active, ask 3 queries a Board member or regulator would ask. Query 1: \"What is the stated timeline for reducing the motor combined ratio from 108% to below 100% and which workstream contributes the most?\" Query 2: \"How does the strategy address BNM's supervisory concern about motor reserving adequacy?\" Query 3: \"What is the UBI programme exit strategy if the pilot does not deliver the expected claims frequency reduction after 2 years?\"",
              fileRef: "INS_02_Pacific_Shield_Strategy.docx"
            }
          ]
        },
        {
          tool: "🤖 PowerPoint Agent",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Set up a BNM Presentation Coach agent",
              prompt: "Create or open the BNM supervisory engagement PowerPoint from the PPT demo. Save as Pacific_Shield_BNM_2025.pptx. Create an agent named BNM Presentation Coach. Instructions: \"Answer questions about Pacific Shield's BNM supervisory presentation. Reference slide numbers. Under 100 words per answer.\" Demo: type \"Which slide addresses the motor combined ratio remediation trajectory and what is the Q4 FY2025 target ratio shown?\""
            },
            {
              title: "Demo the BNM Presentation Coach — regulatory prep queries",
              prompt: "With the BNM Presentation Coach active, run 3 queries simulating how the Chief Actuarial Officer prepares for the BNM bilateral. Query 1: \"If BNM asks specifically about reserving adequacy for motor claims IBNR, which slide addresses this most directly?\" Query 2: \"What evidence does the presentation provide that SWIFT CLAIM is a credible fraud control — Phase 1 results — rather than just a future plan?\" Query 3: \"Which slide shows the governance mechanism the Board has put in place to oversee the combined ratio remediation?\""
            }
          ]
        },
        {
          tool: "🤖 Excel Agent",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Set up an Insurance Portfolio Advisor agent",
              prompt: "Open INS_01_Pacific_Shield_Insurance.xlsx. Create an agent named Pacific Shield Portfolio Advisor. Instructions: \"Answer underwriting and claims performance questions using data from this workbook. Always cite sheet name. Express amounts in MYR millions.\" Demo: type \"What is the current motor combined ratio and in how many of the last 8 quarters has it exceeded 100%?\"",
              fileRef: "INS_01_Pacific_Shield_Insurance.xlsx"
            },
            {
              title: "Demo the Portfolio Advisor — actuarial queries",
              prompt: "With the Pacific Shield Portfolio Advisor active, run 3 queries the Chief Actuarial Officer would ask. Query 1: \"What is the total motor claims incurred in FY2024 and how much of this is attributable to the top 10 workshop repairers by claims volume?\" Query 2: \"What is the year-on-year medical claims inflation rate for the group medical product line in FY2023 and FY2024?\" Query 3: \"What is the UBI segment's claims frequency per 100 policyholders and how does it compare to standard motor — expressed as both absolute number and percentage difference?\"",
              fileRef: "INS_01_Pacific_Shield_Insurance.xlsx"
            }
          ]
        }
      ]
    },
    {
      id: "retail",
      name: "Retail & Consumer",
      icon: "🛒",
      color: "#1A6E4A",
      accent: "#27AE60",
      company: "BrightMart Group Berhad",
      tagline: "Basket size -11.9% | Private label write-down MYR 28.4M | TikTok MYR 1.84M GMV | 284 stores",
      scenario: "BrightMart Group Berhad (BrightMart) is Malaysia's second-largest grocery retailer with 284 stores — hypermarkets, supermarkets, and BrightMart Express — across Peninsular Malaysia and Sabah. Three commercial challenges define the FY2025 leadership agenda: a basket size decline of 11.9% year-on-year driven by trading-down behaviour and competitive pressure from discounters; a MYR 28.4 million private label inventory write-down from an over-extended range expansion; and a digital channel that is growing but still sub-scale — TikTok Shop at MYR 1.84 million GMV against a MYR 18 million opportunity. Chief Commercial Officer Priya Singh and Group CDO Marcus Lim need Copilot to drive basket recovery through loyalty personalisation, rationalise the private label range, and build a credible social commerce scaling case for the Board.",
      files: ["RT_01_BrightMart_Group.xlsx", "RT_02_BrightMart_Strategy.docx", "Email_08_Supplier_Escalation.docx"],
      prompts: [
        {
          tool: "🤖 Copilot Chat (Basic)",
          license: "Free — no M365 license needed",
          account: "Sasha Ouellet — SashaO@ABSx62256373.OnMicrosoft.com",
          prompts: [
            {
              title: "Explain the basket size decline problem and what causes it",
              prompt: "Ask Copilot: \"I am the Chief Commercial Officer of BrightMart Group, Malaysia's second-largest supermarket chain with 284 stores and 8.2 million loyalty members. Our average basket size has declined by 11.9% year-on-year. Explain: (1) The top 5 structural causes of basket size decline in a modern grocery supermarket context — inflation-driven trading down, format preference shift, online channel migration, category mix issues, and competitive pressure; (2) Which of these causes is most consistent with an 11.9% decline in a single fiscal year; (3) The 3 most proven commercial interventions to reverse basket size decline — targeted promotions, category cross-sell, or digital personalisation; (4) How BrightMart's 8.2 million loyalty members represent an untapped data asset to address the problem. Maximum 250 words.\""
            },
            {
              title: "Brief me on the private label strategy and MYR 28.4M write-down",
              prompt: "Ask Copilot: \"I am the BrightMart Group CFO. Our private label programme is targeting growth from 14.8% to 22% of revenue, but we have a MYR 28.4 million inventory write-down on private label slow-moving stock. Brief me on: (1) Why private label inventory write-downs occur in a grocery retailer and what the most common root causes are — over-projection of demand, aggressive range expansion, or poor category management; (2) What the financial accounting treatment of a MYR 28.4 million inventory write-down looks like in our P&L and balance sheet; (3) The range rationalisation and SKU discontinuation strategies that leading Asian grocers use to reduce excess private label inventory; (4) Whether the write-down signals that the 22% private label target is unrealistic. Maximum 250 words.\""
            },
            {
              title: "Explain social commerce and TikTok Shop opportunity",
              prompt: "Ask Copilot: \"Explain social commerce and the TikTok Shop channel opportunity for a Malaysian grocery and FMCG retailer like BrightMart Group. We currently generate MYR 1.84 million GMV on TikTok. Cover: (1) What is social commerce and how does the TikTok Shop algorithm differ from a traditional e-commerce marketplace; (2) Which grocery and FMCG product categories perform best on TikTok Shop in Malaysia and Indonesia — fresh food, packaged snacks, health supplements, or household; (3) The revenue growth trajectory of Malaysian brands that have scaled TikTok Shop from MYR 1 million to MYR 10 million GMV in 12 months; (4) The fulfillment and cold chain logistics challenges for a multi-category grocery retailer on TikTok Shop. Maximum 250 words.\""
            }
          ]
        },
        {
          tool: "�� Researcher",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Research Malaysian grocery retail landscape and competitive trends",
              prompt: "In Copilot Chat, switch to the Researcher agent. Upload RT_02_BrightMart_Strategy.docx. Ask: \"Review BrightMart's strategy document, then search the web for: the latest Euromonitor or Nielsen data on the Malaysian grocery retail market structure — modern trade, traditional trade, and e-commerce shares; competitive positioning of the top 5 Malaysian grocery chains by store count, revenue, and private label penetration; TikTok Shop and Shopee growth in grocery and FMCG in Malaysia 2024-2025; and the performance of private label programmes at Lotus's, AEON, and Jaya Grocer. Cross-reference with BrightMart's strategy to identify the 3 most important competitive threats to address in FY2025. Cite all sources with URLs.\"",
              fileRef: "RT_02_BrightMart_Strategy.docx"
            },
            {
              title: "Research private label strategy and grocery personalisation",
              prompt: "In Copilot Chat, switch to the Researcher agent. Ask: \"Search the web for evidence on private label growth strategies in Asian grocery retail. Find: the average private label penetration rate of leading Asian grocery chains — Aeon, Meiji, and FairPrice — and how they reached those levels; best practices for private label range rationalisation and reducing slow-moving private label stock in a hypermarket format; and grocery loyalty programme personalisation technology that drives basket size recovery — specifically AI-powered promotional targeting platforms that have delivered measurable results for a retailer with 5 to 10 million active loyalty members. BrightMart has 8.2 million members. What are the top 3 data-driven personalisation investments with the clearest ROI? Cite sources.\""
            },
            {
              title: "Research social commerce scaling for FMCG and grocery",
              prompt: "In Copilot Chat, switch to the Researcher agent. Upload RT_01_BrightMart_Group.xlsx. Ask: \"Review BrightMart's channel performance data. Then search the web for: TikTok Shop GMV growth benchmarks for Malaysian and Indonesian grocery and FMCG sellers in 2024 and 2025; the product categories on TikTok Shop that have the highest repeat purchase and GMV growth rates in Southeast Asia; fulfillment and last-mile strategies used by large-format retailers entering TikTok Shop; and any case studies of brick-and-mortar Malaysian retailers that successfully integrated social commerce into their revenue mix. BrightMart currently generates MYR 1.84 million GMV on TikTok. What is a realistic 12-month GMV target and what investment is required to achieve it?\"",
              fileRef: "RT_01_BrightMart_Group.xlsx"
            }
          ]
        },
        {
          tool: "📊 Analyst",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Analyse BrightMart commercial performance and basket trends",
              prompt: "In Copilot Chat, switch to the Analyst agent. Upload RT_01_BrightMart_Group.xlsx. Ask: \"Analyse the full BrightMart dataset. Calculate: (1) Average basket size trend from Q1 FY2022 to Q4 FY2024 — confirm the 11.9% year-on-year decline and identify which quarter it was most severe; (2) Same-store sales growth rate for FY2024 — express as a percentage; (3) The 3 categories with the largest basket contribution decline — which categories are dragging basket size down most; (4) Revenue contribution by channel — in-store, app, and TikTok Shop — and the online penetration trend; (5) Private label revenue as a percentage of total and the quarterly trend toward the 22% target. Present as a Group CCO commercial performance dashboard with a 5-point action agenda.\"",
              fileRef: "RT_01_BrightMart_Group.xlsx"
            },
            {
              title: "Analyse private label programme and inventory write-down",
              prompt: "In Copilot Chat, switch to the Analyst agent. Upload RT_01_BrightMart_Group.xlsx. Ask: \"Analyse the private label programme data. Identify: (1) The SKU count of private label lines and the percentage of SKUs that account for 80% of private label revenue — Pareto analysis; (2) The 10 slowest-moving private label SKUs ranked by days-of-inventory and MYR write-down value — do they concentrate in a specific category; (3) The total inventory write-down of MYR 28.4 million broken down by category — which 3 categories represent the majority of the write-down; (4) The private label gross margin versus own-brand equivalent — is the margin advantage being eroded by the inventory cost; (5) A revised private label SKU rationalisation target — how many SKUs should be discontinued to stabilise inventory cost. Format as a Category Management Committee decision paper.\"",
              fileRef: "RT_01_BrightMart_Group.xlsx"
            },
            {
              title: "Analyse loyalty member behaviour and personalisation opportunity",
              prompt: "In Copilot Chat, switch to the Analyst agent. Upload RT_01_BrightMart_Group.xlsx. Ask: \"Analyse BrightMart's 8.2 million loyalty programme data. Calculate: (1) The monthly active rate of loyalty card holders — what percentage shopped at least once in Q4 FY2024; (2) The basket size differential between loyalty members and non-members — do members spend more per visit; (3) The top 3 loyalty member segments by spending frequency and average basket size — define segments by visit frequency and annual spend; (4) The churn rate of top-tier loyalty members — are our highest-value customers churning at a higher rate than average; (5) The revenue opportunity if the bottom 30% of loyalty members increase their basket size by 15% through personalised promotions. Present as a loyalty and CRM investment case.\"",
              fileRef: "RT_01_BrightMart_Group.xlsx"
            }
          ]
        },
        {
          tool: "📊 Copilot in Excel",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Instant BrightMart commercial performance summary",
              prompt: "Open RT_01_BrightMart_Group.xlsx. Ask Copilot: \"Give me a plain-English executive summary of this entire workbook. What is the current average basket size and how does it compare to the FY2023 baseline? What is the total revenue and year-on-year growth rate? What is the private label revenue percentage? What is the TikTok Shop GMV figure? Flag any metric that shows 3 or more consecutive quarters of decline or is more than 10% below the annual target. Format: 3-sentence overview, then 4 specific flagged concerns with sheet name and row reference.\"",
              fileRef: "RT_01_BrightMart_Group.xlsx"
            },
            {
              title: "Create basket size trend chart by store format",
              prompt: "Open RT_01_BrightMart_Group.xlsx. Navigate to the Commercial KPI sheet. Ask Copilot: \"Create a multi-line chart showing quarterly average basket size from Q1 FY2022 to Q4 FY2024 broken down by store format: Hypermarket, Supermarket, and Express. Use navy blue for Hypermarket, orange for Supermarket, and green for Express. Add data labels at Q4 FY2024 for each format showing the current average basket value in MYR. Add a horizontal dashed line at the Q1 FY2023 basket size showing the pre-decline baseline. Title: BrightMart Group — Average Basket Size Trend by Format FY2022-FY2024. This chart will be embedded in the Board commercial review presentation.\"",
              fileRef: "RT_01_BrightMart_Group.xlsx"
            },
            {
              title: "Add private label SKU velocity and write-down analysis",
              prompt: "Open RT_01_BrightMart_Group.xlsx. Navigate to the Private Label sheet. Ask Copilot: \"For each private label SKU in this table, add 2 new columns. Column 1: Days of Inventory — calculated as Current Stock Units divided by Average Weekly Sales Units, times 7. Column 2: Write-down Risk — if Days of Inventory exceeds 180, display High Risk in red; if 90 to 180, display Monitor in amber; if under 90, display Healthy in green. Tell me: how many SKUs are in High Risk status, what is the total current stock value of those SKUs in MYR, and which product category has the most High Risk SKUs.\"",
              fileRef: "RT_01_BrightMart_Group.xlsx"
            },
            {
              title: "Natural language query — loyalty and digital channel analysis",
              prompt: "Open RT_01_BrightMart_Group.xlsx. Ask Copilot: \"Without navigating sheets, answer: (1) What is the monthly active user count of the BrightMart loyalty app and what is the year-on-year growth rate; (2) What percentage of total revenue is currently generated through digital channels — app plus TikTok Shop combined; (3) Which store region has the highest loyalty programme penetration as a percentage of transactions; (4) What is the average redemption rate of loyalty points and are there unredeemed points accumulating that represent a future liability. Present as a 2-column Q and A table for the Group Chief Digital Officer.\"",
              fileRef: "RT_01_BrightMart_Group.xlsx"
            }
          ]
        },
        {
          tool: "📝 Copilot in Word",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Summarise BrightMart strategy into investor brief",
              prompt: "Open RT_02_BrightMart_Strategy.docx. Ask Copilot: \"Summarise this strategy document into a 1-page investor relations brief for BrightMart Group. Include: (1) The 2 most material challenges — basket size decline 11.9% and private label write-down MYR 28.4M; (2) The 3 strategic growth pillars — private label scaling to 22%, loyalty personalisation platform, and TikTok Shop social commerce; (3) Capital investment plan for FY2025; (4) The KPIs by which investors should judge success in 12 months. Formal investor relations memo style. 400 words maximum. Clear numbered headings.\"",
              fileRef: "RT_02_BrightMart_Strategy.docx"
            },
            {
              title: "Draft private label category rationalisation proposal",
              prompt: "Open a new Word document. Ask Copilot: \"Draft a formal Category Management proposal memo from BrightMart's Chief Commercial Officer to Group CEO and Board Commercial Committee. The memo proposes a private label SKU rationalisation programme to address the MYR 28.4 million inventory write-down. Include: (1) Problem statement — 284 private label SKUs with more than 180 days of inventory representing MYR 28.4 million in write-down risk; (2) Rationalisation proposal — discontinue the bottom 180 SKUs based on velocity, margin, and strategic fit criteria; (3) Financial impact — write-down crystallisation schedule, new lower inventory carrying cost, and improved gross margin on the surviving 420 SKUs; (4) Governance — Category Management Committee monthly reviews with P&L accountability. Formal Board memo. 500 words.\""
            },
            {
              title: "Rewrite loyalty programme benefits for the BrightMart app",
              prompt: "Open RT_02_BrightMart_Strategy.docx. Locate the Loyalty Programme section. Ask Copilot: \"Rewrite this loyalty programme section in plain, enthusiastic, customer-friendly language suitable for the BrightMart mobile app home screen. Replace all business strategy language with direct benefits to the shopper. Use short punchy sentences of maximum 15 words. Structure as 5 benefit statements: Points, Personalised Deals, Birthday Rewards, Early Sale Access, and BrightMart Select VIP tier. Each benefit: 1 headline sentence and 1 supporting sentence. Total under 200 words. Tone: warm, exciting, and personal. This copy will be used directly in the app UI for the loyalty programme onboarding screen.\"",
              fileRef: "RT_02_BrightMart_Strategy.docx"
            },
            {
              title: "Draft TikTok Shop expansion proposal",
              prompt: "Open a new Word document. Ask Copilot: \"Draft a formal business case memo from BrightMart's Chief Digital Officer to Group CEO seeking approval to invest MYR 4.2 million to scale the TikTok Shop channel from MYR 1.84 million current GMV to MYR 18 million GMV in 12 months. The memo should cover: (1) Current TikTok Shop performance baseline — GMV, top-selling categories, and conversion rate; (2) Growth plan — 3 full-time content creators, 1 live-stream commerce manager, dedicated fulfilment team at KL distribution centre, and 120 SKU optimised product catalogue; (3) Financial model — GMV target, gross margin on social commerce, payback period on MYR 4.2 million investment; (4) Risk — competition from FMCG brand direct sellers and Shopee. Formal Board memo format. 500 words.\""
            }
          ]
        },
        {
          tool: "🎯 Copilot in PowerPoint",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Create BrightMart Board commercial turnaround deck",
              prompt: "Open a new PowerPoint. Ask Copilot: \"Create a 7-slide Board presentation for BrightMart Group covering the commercial turnaround plan for FY2025. Slide 1: BrightMart Group — FY2025 Commercial Turnaround Plan. Slide 2: Where We Are — basket size -11.9%, private label write-down MYR 28.4M, TikTok Shop opportunity. Slide 3: The Fix — 3 strategic pillars. Slide 4: Private Label Rationalisation and Recovery — SKU reduction plan, margin improvement, Q-by-Q inventory targets. Slide 5: Loyalty Personalisation — 8.2M members, AI targeting, basket recovery model. Slide 6: Social Commerce Acceleration — TikTok Shop MYR 18M GMV target, investment, and timeline. Slide 7: Board Decisions Required — 2 investment approvals. Corporate retail green and white theme, modern. Clean.\""
            },
            {
              title: "Generate private label strategy pitch for suppliers",
              prompt: "Open a new PowerPoint. Ask Copilot: \"Create a 5-slide private label manufacturer pitch presentation for BrightMart Group to show to tier-2 FMCG manufacturers at a supplier development conference. Slide 1: BrightMart Private Label — Partnering for Growth. Slide 2: BrightMart Scale — 284 stores, 8.2M members, 320,000 daily transactions. Slide 3: Private Label Partnership Model — exclusive supply, co-development, joint marketing support. Slide 4: Why Work with BrightMart — data insights, route to market, guaranteed volume. Slide 5: How to Apply — qualification criteria and process timeline. Modern, professional retail design. Green and white BrightMart brand colours.\""
            },
            {
              title: "Add competitive basket size benchmarking slide",
              prompt: "In an open BrightMart PowerPoint, add a new slide. Ask Copilot: \"Create a competitive benchmarking slide showing average basket size for BrightMart versus 4 Malaysian grocery retailers: Lotus's, AEON, Jaya Grocer, and Mydin. BrightMart current average basket MYR 68. Use a horizontal bar chart with BrightMart in red (to flag the problem) and competitors in navy blue. Add a target bar for BrightMart at MYR 78 — the FY2025 recovery target — in green. Title: BrightMart — Average Basket Size vs Malaysian Grocery Peers. Add a 2-sentence commentary on what closing the gap to MYR 78 means in annual incremental revenue for a base of 8.2 million active members.\""
            }
          ]
        },
        {
          tool: "📧 Copilot in Outlook",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Triage the private label supplier escalation email",
              prompt: "Open Outlook and find Email_08_Supplier_Escalation.docx. Copy into a draft or open the email. Ask Copilot: \"I am BrightMart's Head of Private Label Category and I have received this supplier escalation email. Summarise: (1) What is the supplier complaining about specifically — is it payment terms, volume shortfall, quality dispute, or contract terms; (2) What financial exposure is at risk if this supplier terminates the contract — MYR amount; (3) What is the response deadline and what does the supplier want as resolution; (4) The 3 actions I should take in the next 24 hours to prevent escalation. Format under 4 headings. Maximum 200 words.\"",
              fileRef: "Email_08_Supplier_Escalation.docx"
            },
            {
              title: "Draft Group CEO message to all store managers on basket recovery",
              prompt: "Open a new Outlook email. Ask Copilot: \"Draft an email from BrightMart Group CEO to all 284 store managers addressing the 11.9% basket size decline. The email should: (1) Acknowledge the challenge directly — no spin — and show 2 specific data points that show the impact; (2) Explain the 3 key actions every store manager must implement this week to support basket recovery: upselling cross-category promotions at checkout, private label sampling in the top 20 categories, and BrightMart app sign-up conversion target of 30% of new transactions; (3) Announce that basket size will now be a primary KPI tracked weekly by regional managers; (4) Close with an energising message about the opportunity ahead. Direct, honest, energising. 300 words.\""
            },
            {
              title: "Copilot coaching on supplier price increase negotiation email",
              prompt: "In Outlook, type a rough draft to a top FMCG supplier: \"Hi, we have seen your price increase request. We are not happy with it because it will affect our margins. Please reconsider or we will look at alternative suppliers. Thanks.\" Ask Copilot for coaching: \"I am BrightMart's Head of Procurement writing to a tier-1 FMCG supplier. Evaluate this draft on: (1) Negotiating power projection — does it clearly signal our leverage and alternatives; (2) Commercial language precision — is the counter-proposal specific and data-backed; (3) Relationship preservation — does it leave room for a constructive commercial dialogue. Rewrite the email with specific data — our annual purchase volume in MYR, our comparable supplier alternative, and a counter-offer timeline.\""
            }
          ]
        },
        {
          tool: "🎙 Copilot in Teams",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Catch up on missed private label category review",
              prompt: "Open an existing Teams meeting that was recorded and has a Copilot recap from your calendar. In the Copilot recap pane ask: \"I am BrightMart's Head of Private Label who missed this meeting because I was at a supplier site visit. Catch me up: (1) What private label categories or SKUs were discussed — were any flagged for discontinuation; (2) What was decided about the MYR 28.4 million write-down — is there an approved rationalisation plan; (3) Any supplier changes or new private label product launches discussed and approved; (4) Actions assigned to the Head of Private Label or Category Management team; (5) Was the 22% private label revenue target discussed — if so, is it still being maintained or revised.\""
            },
            {
              title: "Extract commercial actions from the weekly trading meeting",
              prompt: "Open an existing recorded Teams meeting from your calendar. In the Copilot recap pane ask: \"Extract all commercial and trading action items from this meeting formatted as a structured action register. Columns: Action Description; Owner (full name); Category or Channel (Private Label, Loyalty, TikTok Shop, Store Operations); Deadline; Priority — Critical if a Board approval or supplier contract decision is involved, High if a revenue target is at risk, Normal for routine. Group actions by Category or Channel. Also note: was the basket size KPI reviewed in this meeting and if so what was the weekly trend number reported?\""
            },
            {
              title: "Generate commercial team update email from trading review",
              prompt: "Open an existing recorded Teams meeting recap from your calendar. In the Copilot recap pane ask: \"Draft a weekly commercial update email from BrightMart's Chief Commercial Officer to all 8 regional commercial managers and 4 category heads. Based on this meeting: (1) Top 3 commercial priorities for the week with specific actions; (2) Basket size KPI status — this week versus last week and year-on-year; (3) Private label programme update — write-down status and SKU rationalisation progress; (4) TikTok Shop GMV update — weekly performance versus target; (5) Any promotional campaigns launching this week across all 284 stores. Direct, commercially energised communication. Under 300 words.\""
            }
          ]
        },
        {
          tool: "📓 Copilot Notebook",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Full commercial turnaround brief from 3 documents",
              prompt: "Go to Copilot Notebook. Upload RT_01_BrightMart_Group.xlsx, RT_02_BrightMart_Strategy.docx, and Email_08_Supplier_Escalation.docx. In Instructions: \"Using all 3 documents, prepare a commercial turnaround brief for BrightMart Group CEO. (1) From the financial data — confirm the basket size decline trajectory and private label write-down impact on EBITDA; (2) From the strategy — is the private label 22% target still credible given the write-down data; (3) From the supplier email — how does the escalation risk compound the write-down problem and what is the combined commercial exposure; (4) Cross-reference: are the 3 strategic priorities in the strategy document consistent with what the financial data says is most urgent; (5) Build a 3-point CEO action agenda for the Board meeting.\"",
              fileRef: "RT_01_BrightMart_Group.xlsx, RT_02_BrightMart_Strategy.docx, Email_08_Supplier_Escalation.docx"
            },
            {
              title: "Loyalty personalisation and social commerce data analysis",
              prompt: "Go to Copilot Notebook. Upload RT_01_BrightMart_Group.xlsx and RT_02_BrightMart_Strategy.docx. In Instructions: \"Using both documents, build a digital growth investment analysis for BrightMart's Group CDO. For 2 digital investment areas — loyalty personalisation engine and TikTok Shop scaling: (1) What does the financial data show about current performance in each area; (2) What investment does the strategy document commit to and what is the expected ROI; (3) Are there any gaps between the loyalty member data and the strategy's assumptions about personalisation ROI; (4) What is the payback period for each investment based on the most conservative reasonable assumption. Format as a digital investment roadmap summary with a recommended priority order.\"",
              fileRef: "RT_01_BrightMart_Group.xlsx, RT_02_BrightMart_Strategy.docx"
            }
          ]
        },
        {
          tool: "🤝 Cowork (Pages)",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Build commercial turnaround tracker in Pages",
              prompt: "In Copilot Chat, upload RT_01_BrightMart_Group.xlsx and ask for a basket size and commercial KPI summary. Click Open in Copilot Pages. Ask: \"Reorganise this into a collaborative Commercial Turnaround Tracker for BrightMart's Commercial Leadership team of 10 members. Structure as: (1) Basket Recovery KPI Dashboard — weekly basket size vs target; (2) Private Label Rationalisation Tracker — SKU discontinuation progress and write-down reduction; (3) Loyalty Activation Campaign Log — weekly campaign performance and member response; (4) TikTok Shop GMV Tracker — weekly GMV vs target; (5) Supplier Relationship Status — top 20 private label suppliers with contract health. Format for daily collaborative updates.\"",
              fileRef: "RT_01_BrightMart_Group.xlsx"
            },
            {
              title: "Build category management planning canvas",
              prompt: "In Copilot Chat, upload RT_02_BrightMart_Strategy.docx and ask for a private label and category strategy summary. Click Open in Copilot Pages. Ask: \"Expand this into a collaborative Category Management Planning Canvas for BrightMart's 12 Category Managers. Structure as: (1) Category Health Scorecard — basket contribution, growth rate, private label mix; (2) Rationalisation Decision Matrix — SKUs flagged for discontinuation, monitor, or accelerate; (3) New Product Development Pipeline — upcoming private label launches by category; (4) Supplier Partnership Status — key supplier relationship health for each category; (5) Category KPI Targets for FY2025. Format for simultaneous editing by all 12 category managers.\"",
              fileRef: "RT_02_BrightMart_Strategy.docx"
            }
          ]
        },
        {
          tool: "🤖 Word Agent",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Set up a BrightMart Strategy Advisor on the strategy doc",
              prompt: "Open RT_02_BrightMart_Strategy.docx in Word. Create an agent named BrightMart Strategy Advisor. Instructions: \"Answer questions about BrightMart's commercial strategy, private label programme, loyalty platform, and social commerce. Cite document sections. Under 150 words.\" Demo: type \"What is BrightMart's private label revenue target as a percentage of total revenue and what are the 3 key actions in the strategy to reach it?\"",
              fileRef: "RT_02_BrightMart_Strategy.docx"
            },
            {
              title: "Demo the BrightMart Strategy Advisor — commercial queries",
              prompt: "With the agent active, ask 3 queries a Board member or investor would ask. Query 1: \"What is the strategy's plan to recover basket size from the current decline — which specific interventions are committed and by when?\" Query 2: \"How does the loyalty personalisation platform investment contribute to the basket size recovery and what is the expected ROI?\" Query 3: \"What is the TikTok Shop GMV target for FY2025 and what investment has been committed to reach it?\"",
              fileRef: "RT_02_BrightMart_Strategy.docx"
            }
          ]
        },
        {
          tool: "🤖 PowerPoint Agent",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Set up a Board Commercial Presenter agent",
              prompt: "Create or open the BrightMart Board commercial turnaround PowerPoint from the PPT demo. Save as BrightMart_Board_Commercial_2025.pptx. Create an agent named BrightMart Commercial Coach. Instructions: \"Answer questions about BrightMart's commercial turnaround presentation. Reference slide numbers. Under 100 words.\" Demo: type \"Which slide shows the basket size recovery model and what is the FY2025 basket size target in MYR?\""
            },
            {
              title: "Demo the Commercial Coach — Board prep queries",
              prompt: "With the BrightMart Commercial Coach active, run 3 Board preparation queries. Query 1: \"If a Board member asks why basket size declined 11.9% while the market grew, which slide has the most credible answer?\" Query 2: \"What investment is being requested for the loyalty personalisation platform and on which slide is the ROI shown?\" Query 3: \"Which slide covers the private label write-down and what is the recovery plan for reducing the MYR 28.4 million risk?\""
            }
          ]
        },
        {
          tool: "🤖 Excel Agent",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Set up a BrightMart Commercial Data agent",
              prompt: "Open RT_01_BrightMart_Group.xlsx. Create an agent named BrightMart Commercial Advisor. Instructions: \"Answer commercial performance questions using data from this workbook. Always cite sheet name. Express amounts in MYR millions.\" Demo: type \"What is the current average basket size in MYR and how does it compare to the same period last year?\"",
              fileRef: "RT_01_BrightMart_Group.xlsx"
            },
            {
              title: "Demo the Commercial Advisor — category and loyalty queries",
              prompt: "With the BrightMart Commercial Advisor active, run 3 queries the CCO would ask. Query 1: \"Which 3 product categories have shown the largest year-on-year basket contribution decline in FY2024?\" Query 2: \"What percentage of total BrightMart transactions are made by loyalty members and what is the average basket size difference between members and non-members?\" Query 3: \"What is the total private label revenue in MYR millions for FY2024 and what percentage of total sales does this represent — is it above or below the 14.8% FY2023 baseline?\"",
              fileRef: "RT_01_BrightMart_Group.xlsx"
            }
          ]
        }
      ]
    },
    {
      id: "glc",
      name: "GLC / Investment Holdings",
      icon: "🏛️",
      color: "#1C3A6E",
      accent: "#2E86AB",
      company: "Danamas Capital Group",
      tagline: "MYR 48.2B AUM | 3 underperformers on PIP | Danamas Infra concession risk | 14 investees",
      scenario: "Danamas Capital Group (Danamas) is a Malaysian government-linked investment holding company managing a MYR 48.2 billion portfolio of 14 investee companies across infrastructure, financial services, property, and industrial sectors on behalf of government-linked funds. Three investees are on formal Performance Improvement Plans after failing to meet the 8% ROE threshold for 3 consecutive years. The flagship Danamas Infrastructure Berhad faces a concession renewal risk following service reliability disputes with the Ministry of Works. Group CEO Azrul Hashim and CIO Faridah Omar must deliver credible turnaround evidence to the Ministry of Finance annual review, manage the Danamas Infra concession stakeholder process, and ensure all 14 listed investees meet Bursa Malaysia's mandatory sustainability reporting deadlines.",
      files: ["GLC_01_Danamas_Capital.xlsx", "GLC_02_Danamas_Strategy.docx", "Email_11_Investee_Performance.docx"],
      prompts: [
        {
          tool: "🤖 Copilot Chat (Basic)",
          license: "Free — no M365 license needed",
          account: "Sasha Ouellet — SashaO@ABSx62256373.OnMicrosoft.com",
          prompts: [
            {
              title: "Explain GLC governance obligations under Putrajaya Committee guidelines",
              prompt: "Ask Copilot: \"Explain the governance obligations for a Malaysian Government-Linked Company (GLC) under the Putrajaya Committee on GLC High Performance guidelines and Bursa Malaysia Listing Requirements. Danamas Capital Group manages a MYR 48.2 billion portfolio of 14 investee companies on behalf of government-linked funds. Explain: (1) What the Putrajaya Committee's GLC Transformation Programme mandates for Board composition, risk governance, and performance accountability of investee companies; (2) How Danamas as the holding company manages its fiduciary duty to the government unitholders versus its legal obligations to investee company minority shareholders; (3) The 3 most common GLC governance failures cited in Bursa regulatory actions in Malaysia; (4) What a Performance Improvement Plan intervention in an underperforming investee looks like. Maximum 250 words.\""
            },
            {
              title: "Brief me on the Danamas Infra concession renewal risk",
              prompt: "Ask Copilot: \"I am the CEO of Danamas Capital Group, managing a MYR 48.2 billion portfolio of 14 Malaysian GLC investees. One of our key assets is Danamas Infrastructure Berhad, an expressway and port concession company whose government concession renewal is under risk due to a service reliability dispute with the Ministry of Works. Brief me on: (1) What a government concession renewal risk means — what the Ministry can do if it is not satisfied with service standards; (2) The financial valuation impact on Danamas Capital's overall portfolio if Danamas Infra's concession is shortened or not renewed — express as MYR billions of NAV impact; (3) The 3 key stakeholder relationships I need to manage — Ministry of Works, Prime Minister's Department, and UKAS; (4) The precedent from recent Malaysian infrastructure concession re-negotiations. Maximum 250 words.\""
            },
            {
              title: "What is NAV and why does portfolio diversification matter for a GLC?",
              prompt: "Ask Copilot: \"Explain in plain English what Net Asset Value (NAV) means for a government-linked investment holding company like Danamas Capital Group, with a MYR 48.2 billion portfolio. Cover: (1) How NAV is calculated for a diversified investee portfolio that includes listed and unlisted companies; (2) Why sector diversification matters for NAV stability — use the example of having 3 underperforming investees in Danamas Capital's 14-company portfolio; (3) What a 10% decline in a single investee's equity value means for Danamas Capital's total NAV; (4) Why Malaysian GLCs are subject to additional scrutiny on NAV performance from government unitholders and the Auditor General. Maximum 250 words.\""
            }
          ]
        },
        {
          tool: "�� Researcher",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Research Malaysian GLC performance and governance standards",
              prompt: "In Copilot Chat, switch to the Researcher agent. Upload GLC_02_Danamas_Strategy.docx. Ask: \"Review Danamas Capital's strategy document, then search the web for: the latest Putrajaya Committee GLC High Performance scorecards and any public results for Malaysian GLCs; recent Bursa Malaysia enforcement actions or queries related to GLC governance in 2023-2025; international best practices for sovereign wealth fund and GLC portfolio management — Temasek, Khazanah, PNB; and the performance of infrastructure concession asset monetisation strategies in Malaysia. Cross-reference with Danamas's 3 underperforming investees to identify what turnaround governance approaches are most effective. Cite all sources with URLs.\"",
              fileRef: "GLC_02_Danamas_Strategy.docx"
            },
            {
              title: "Research infrastructure concession renewal strategies in Malaysia",
              prompt: "In Copilot Chat, switch to the Researcher agent. Ask: \"Search the web for recent Malaysian government infrastructure concession renegotiations and renewals — expressways, ports, and utilities — between 2020 and 2025. Find: cases where concessions were shortened, amended, or not renewed and the financial impact on the concession company; the role of UKAS, Ministry of Works, and MOF in concession governance; the 5 most important contractual and operational performance metrics that the government monitors for concession renewal eligibility; and financial modelling approaches for concession asset valuation during renewal uncertainty. Danamas Infra is facing concession renewal risk. What are the 3 most important actions to strengthen its renewal case?\""
            },
            {
              title: "Research ESG integration for Malaysian GLC portfolios",
              prompt: "In Copilot Chat, switch to the Researcher agent. Upload GLC_01_Danamas_Capital.xlsx. Ask: \"Review Danamas Capital's portfolio data. Then search the web for: Bursa Malaysia's mandatory sustainability reporting requirements for Main Market issuers and how they apply to GLC holding companies; Khazanah Nasional and PNB's published ESG integration frameworks for portfolio company management; the EPU's ESG expectations for government-linked fund investees under the Malaysia MADANI framework; and international GLC governance and ESG benchmark indices. Which of Danamas's 14 investees appears most exposed to ESG reporting and compliance risk based on the portfolio data? Format as a portfolio ESG risk matrix.\"",
              fileRef: "GLC_01_Danamas_Capital.xlsx"
            }
          ]
        },
        {
          tool: "📊 Analyst",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Analyse Danamas Capital portfolio performance and underperformers",
              prompt: "In Copilot Chat, switch to the Analyst agent. Upload GLC_01_Danamas_Capital.xlsx. Ask: \"Analyse the Danamas Capital portfolio. Calculate: (1) Total NAV by investee and the 3 investees contributing the highest NAV concentration risk; (2) The 3 underperforming investees — identify them by ROE below the 8% portfolio threshold and EBITDA margin below sector median; (3) The portfolio dividend yield for FY2024 — total dividends received as a percentage of total NAV; (4) The weighted average ROE for the full 14-investee portfolio and the gap to the 12% GLC performance target; (5) What the NAV impact would be if the 3 underperformers each decline in equity value by 20%. Present as a Portfolio Investment Committee dashboard.\"",
              fileRef: "GLC_01_Danamas_Capital.xlsx"
            },
            {
              title: "Model Danamas Infra concession risk and NAV impact",
              prompt: "In Copilot Chat, switch to the Analyst agent. Upload GLC_01_Danamas_Capital.xlsx. Ask: \"Build a concession risk sensitivity model for the Danamas Infra asset. From the portfolio data: (1) What is Danamas Infra's current equity value in MYR billions as a percentage of total portfolio NAV; (2) Model 3 concession renewal scenarios — Full Renewal (no change), Shortened Renewal (5-year reduction), and Non-Renewal (concession ends, asset monetised at distressed valuation 30% discount); (3) For each scenario calculate the NAV impact for Danamas Capital in MYR billions and as a percentage of total portfolio NAV; (4) At current distributions, how many years of dividends from Danamas Infra would be lost in the Non-Renewal scenario. Format as a Board Investment Committee risk scenario paper.\"",
              fileRef: "GLC_01_Danamas_Capital.xlsx"
            },
            {
              title: "Analyse GLC investee ROE and dividend performance",
              prompt: "In Copilot Chat, switch to the Analyst agent. Upload GLC_01_Danamas_Capital.xlsx. Ask: \"Analyse the GLC investee performance data. For all 14 investees: (1) Rank by ROE for FY2024 — highest to lowest — and identify investees below the 8% minimum threshold; (2) Calculate the total dividend income to Danamas Capital in MYR millions and identify the 3 highest dividend-contributing investees; (3) Determine the 3 sectors with the highest average ROE and the 3 with the lowest; (4) Identify any investees where ROE has declined in 2 or more consecutive years — these are the systemic underperformers; (5) Calculate what increase in weighted average ROE across the 3 underperformers would be needed to bring the portfolio to the 12% target. Format as a Portfolio Review Board paper.\"",
              fileRef: "GLC_01_Danamas_Capital.xlsx"
            }
          ]
        },
        {
          tool: "📊 Copilot in Excel",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Instant Danamas Capital portfolio summary",
              prompt: "Open GLC_01_Danamas_Capital.xlsx. Ask Copilot: \"Give me a plain-English executive summary of this entire portfolio workbook. What is the total portfolio NAV? Which 3 investees have the highest NAV concentration? Which investees are currently showing ROE below the 8% threshold? What is the total dividend income received in FY2024? Flag any investee where both ROE and EBITDA margin are below threshold simultaneously. Format: 3-sentence overview, then 4 specific flagged concerns with sheet name and row reference.\"",
              fileRef: "GLC_01_Danamas_Capital.xlsx"
            },
            {
              title: "Build portfolio performance heatmap",
              prompt: "Open GLC_01_Danamas_Capital.xlsx. Ask Copilot: \"Create a heatmap table for all 14 investee companies showing 4 performance metrics: ROE, EBITDA Margin, Dividend Yield, and NAV Growth. Apply green fill for metrics above target, amber for within 20% below target, and red for more than 20% below target. Include the investee name in column A and 4 metric columns. Sort by ROE descending. Add a totals or averages row at the bottom. Title: Danamas Capital Portfolio Performance Heatmap FY2024. This will be presented to the Board Investment Committee.\"",
              fileRef: "GLC_01_Danamas_Capital.xlsx"
            },
            {
              title: "Add NAV concentration and sector allocation analysis",
              prompt: "Open GLC_01_Danamas_Capital.xlsx. Navigate to the Portfolio Allocation sheet. Ask Copilot: \"Add two analyses: First, calculate each investee's NAV as a percentage of total portfolio NAV and flag any single investee that represents more than 15% of total NAV as a concentration risk — highlight in amber. Second, group the 14 investees by sector — infrastructure, financial services, property, and industrial — and calculate the sector NAV allocation as a percentage of total portfolio. Tell me which sector represents the highest concentration and whether Danamas Infra alone exceeds 15% of total portfolio NAV.\"",
              fileRef: "GLC_01_Danamas_Capital.xlsx"
            },
            {
              title: "Natural language query — underperformer financial profile",
              prompt: "Open GLC_01_Danamas_Capital.xlsx. Ask Copilot: \"Without navigating sheets, answer: (1) Name the 3 investees with the lowest ROE in FY2024 and state their exact ROE percentages; (2) What is the total equity value of these 3 underperformers in MYR billions and what percentage of total portfolio NAV do they represent; (3) Have all 3 underperformers received formal Performance Improvement Plan notices from Danamas Capital — what does the data show; (4) What was the total net loss or profit of the underperformers combined in FY2024 and is any of them loss-making at the net profit level. Present as a 2-column Q and A table.\"",
              fileRef: "GLC_01_Danamas_Capital.xlsx"
            }
          ]
        },
        {
          tool: "📝 Copilot in Word",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Summarise Danamas strategy into a government stakeholder brief",
              prompt: "Open GLC_02_Danamas_Strategy.docx. Ask Copilot: \"Summarise this strategy document into a 1-page brief for submission to Malaysia's Ministry of Finance as part of the annual GLC performance review. Include: (1) Portfolio overview — 14 investees, MYR 48.2 billion NAV, FY2024 total returns; (2) The 3 underperformer interventions and expected turnaround timelines; (3) The Danamas Infra concession renewal programme status; (4) The ESG and Bursa sustainability compliance progress across all investees; (5) The 2 strategic investments planned for FY2025. Formal government correspondence style. Maximum 400 words.\"",
              fileRef: "GLC_02_Danamas_Strategy.docx"
            },
            {
              title: "Draft underperformer Performance Improvement Plan letter",
              prompt: "Open a new Word document. Ask Copilot: \"Draft a formal Performance Improvement Plan (PIP) letter from Danamas Capital Group CEO to the Board Chairman of one of the 3 underperforming investee companies. The letter must: (1) Cite the specific performance shortfall — ROE of 4.2% versus the 8% minimum threshold for 3 consecutive years; (2) Outline the 5 improvement areas Danamas requires: cost rationalisation, capital structure optimisation, digital operations investment, management bench strength, and ESG reporting; (3) Set a 12-month improvement milestones schedule with quarterly review checkpoints; (4) State the governance consequence if milestones are not met — Danamas will exercise rights to Board seat replacement; (5) Offer Danamas Capital advisory support including strategy and digital transformation resources. Formal GLC governance correspondence. 500 words.\""
            },
            {
              title: "Rewrite GLC governance principles for investee non-executive directors",
              prompt: "Open GLC_02_Danamas_Strategy.docx. Locate the Corporate Governance Framework section. Ask Copilot: \"Rewrite this governance framework section in clear, practical language for an independent non-executive director who has just been appointed to an investee company Board by Danamas Capital. They have a finance background but are not a governance specialist. Replace all policy references and committee structure acronyms with plain-language descriptions of their specific responsibilities. Add a 5-item checklist of what the NED must do in their first 90 days on the investee Board. Maximum 350 words. Supportive and practical tone.\"",
              fileRef: "GLC_02_Danamas_Strategy.docx"
            },
            {
              title: "Draft Danamas Infra concession renewal engagement memo",
              prompt: "Open a new Word document. Ask Copilot: \"Draft a formal memo from Danamas Capital Group CEO to the Danamas Infrastructure Berhad CEO outlining the Group's expectations and support plan for the upcoming concession renewal negotiation with the Ministry of Works. The memo should: (1) State the strategic importance of the concession renewal to the MYR 48.2 billion portfolio — express the NAV at risk; (2) Set 3 specific conditions Danamas Capital requires Danamas Infra to fulfill before entering Ministry negotiations — service reliability target of 99.2%, customer complaint resolution SLA of 48 hours, and financial model submission by 15 June 2025; (3) Offer Danamas Capital advisory team support for the negotiation; (4) Establish a weekly steering committee chaired by the Group CEO. Formal GLC governance tone. 450 words.\""
            }
          ]
        },
        {
          tool: "🎯 Copilot in PowerPoint",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Create annual GLC portfolio performance presentation",
              prompt: "Open a new PowerPoint. Ask Copilot: \"Create a 7-slide annual performance review presentation for Danamas Capital Group to present to the Malaysian Ministry of Finance and Putrajaya Committee. Slide 1: Danamas Capital — FY2024 Annual Performance Review. Slide 2: Portfolio Overview — MYR 48.2B NAV, 14 investees, sector breakdown. Slide 3: FY2024 Returns — weighted ROE, dividend yield, NAV growth. Slide 4: Underperformer Interventions — 3 companies, root causes, PIP status. Slide 5: Danamas Infra Concession Renewal Programme — timeline and stakeholder map. Slide 6: ESG and Sustainability — Bursa compliance status across all investees. Slide 7: FY2025 Strategic Priorities. Corporate navy blue and gold government theme. Formal, minimal design.\""
            },
            {
              title: "Generate underperformer turnaround strategy deck",
              prompt: "Open a new PowerPoint. Ask Copilot: \"Create a 5-slide turnaround strategy presentation for one of Danamas Capital's underperforming investees, to be reviewed at the Board Investment Committee. Slide 1: Investee Overview and Performance Problem Statement. Slide 2: Root Cause Analysis — 3 core issues with data evidence. Slide 3: Turnaround Plan — 5 workstreams with owners and quarterly milestones. Slide 4: Financial Recovery Model — ROE trajectory from 4.2% to 8% over 3 years. Slide 5: Governance Oversight — Danamas Capital Board seat appointment and monthly review cadence. Clean professional design suitable for government and institutional investor audience.\""
            },
            {
              title: "Add portfolio sector allocation and NAV concentration slide",
              prompt: "In an open Danamas Capital PowerPoint, add a new slide. Ask Copilot: \"Create a portfolio composition slide for Danamas Capital Group with 2 charts side by side. Left chart: a pie chart showing NAV allocation by sector — Infrastructure, Financial Services, Property, Industrial, and Others. Right chart: a horizontal bar chart showing the top 5 investees by NAV contribution in MYR billions with Danamas Infra highlighted in a different colour. Add a concentration risk callout noting if any single investee exceeds 15% of total NAV. Title: Danamas Capital — Portfolio Composition and Concentration Analysis FY2024.\""
            }
          ]
        },
        {
          tool: "📧 Copilot in Outlook",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Triage email from underperforming investee CEO",
              prompt: "Open Outlook and locate Email_11_Investee_Performance.docx — copy into a draft or open the email. Ask Copilot to summarise: \"I am the Danamas Capital Group CIO and I have received this email from the CEO of one of our 3 underperforming investees. Summarise: (1) What specifically is the investee CEO reporting or requesting; (2) Does the email acknowledge the performance shortfall or is it defensive; (3) Are there any requests for additional capital or governance concessions; (4) My 3 recommended responses — what should I agree to, what should I push back on, and what escalates to Group CEO. Maximum 200 words.\"",
              fileRef: "Email_11_Investee_Performance.docx"
            },
            {
              title: "Draft formal investee annual performance review letter",
              prompt: "Open a new Outlook email. Ask Copilot: \"Draft a formal annual portfolio performance review letter from Danamas Capital Group CEO to all 14 investee company Board Chairmen. The letter should: (1) Acknowledge the portfolio's overall FY2024 performance and Danamas Capital's satisfaction or concern; (2) Name the 3 underperforming investees and confirm they remain on formal PIP monitoring; (3) Remind all investees of the FY2025 performance targets — minimum 8% ROE and Bursa sustainability reporting compliance by Q2 FY2025; (4) Announce the annual GLC Performance Review bilateral meetings scheduled in June 2025; (5) Offer Danamas Capital strategy advisory support. Formal GLC governance tone. 350 words.\""
            },
            {
              title: "Copilot coaching on concession renewal stakeholder email",
              prompt: "In Outlook, type a rough draft to the Ministry of Works: \"Dear Ministry, we would like to discuss the Danamas Infra concession renewal. We believe our performance has been acceptable and we hope you will renew it. Please let us know a good time to meet. Thanks.\" Ask Copilot for coaching: \"I am a GLC CEO writing to the Secretary General of the Ministry of Works about a major infrastructure concession worth MYR 2.8 billion. Evaluate on: (1) Strategic framing — does it position the renewal as mutually beneficial for the government and the GLC; (2) Evidence of performance — does it reference specific service delivery data; (3) Relationship tone — is it appropriately formal. Rewrite at CEO-to-Ministry standard with service data and a clear value proposition for renewal.\""
            }
          ]
        },
        {
          tool: "🎙 Copilot in Teams",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Catch up on missed investee performance review meeting",
              prompt: "Open an existing Teams meeting that was recorded and has a Copilot recap from your calendar. Ask: \"I am the Danamas Capital Group CIO and I missed this investee performance review because I was at a Board meeting. Catch me up: (1) Which investee companies were reviewed and what was the overall assessment for each; (2) Were any investees placed on formal PIP or had their PIP status changed; (3) What specific governance actions were decided — Board seat changes, CEO performance warnings; (4) Actions assigned to the CIO or Investment Management team; (5) Was the Danamas Infra concession renewal discussed and if so, what was the timeline update.\""
            },
            {
              title: "Extract investee management actions from quarterly review",
              prompt: "Open an existing recorded Teams meeting from your calendar. Ask: \"Extract all investee management and governance action items from this quarterly review meeting. Format as a GLC Action Register: Investee Name; Action Type (PIP, Board Action, Capital Decision, ESG Compliance); Specific Action Required; Owner (Danamas Capital team member); Deadline; Status. Highlight Critical priority for any action related to BNM or Bursa Malaysia regulatory compliance deadlines. Also note: how many investees are currently on formal PIP monitoring and did any investee miss a milestone this quarter?\""
            },
            {
              title: "Draft portfolio review summary email from leadership meeting",
              prompt: "Open an existing recorded Teams meeting recap from your calendar. Ask: \"Draft a quarterly portfolio review summary email from the Danamas Capital Group CEO to the full investment management team of 18 professionals. Based on this meeting: (1) Portfolio NAV and returns summary for the quarter; (2) Underperformer status update — PIP progress and any governance actions taken; (3) Danamas Infra concession renewal update; (4) FY2025 priority actions for the next 90 days. Professional investment management communication. Under 300 words.\""
            }
          ]
        },
        {
          tool: "📓 Copilot Notebook",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Full MOF submission brief from 3 portfolio documents",
              prompt: "Go to Copilot Notebook. Upload GLC_01_Danamas_Capital.xlsx, GLC_02_Danamas_Strategy.docx, and Email_11_Investee_Performance.docx. In Instructions: \"Using all 3 documents, prepare a comprehensive Ministry of Finance annual GLC submission brief for Danamas Capital CEO. (1) From the portfolio data — summarise FY2024 returns, NAV, and underperformer status with specific numbers; (2) From the strategy document — does the strategy credibly address the underperformer problem and the concession renewal risk; (3) From the investee email — does it indicate that the PIP intervention is working or failing; (4) Cross-reference: any gap between the strategy document's turnaround claims and the actual portfolio data; (5) Build a 3-point CEO talking track for the MOF annual review meeting.\"",
              fileRef: "GLC_01_Danamas_Capital.xlsx, GLC_02_Danamas_Strategy.docx, Email_11_Investee_Performance.docx"
            },
            {
              title: "Portfolio ESG gap analysis and Bursa compliance check",
              prompt: "Go to Copilot Notebook. Upload GLC_01_Danamas_Capital.xlsx and GLC_02_Danamas_Strategy.docx. In Instructions: \"Using both documents, conduct a Bursa Malaysia ESG and sustainability compliance gap analysis for all 14 Danamas Capital investees. For each investee: (1) Is there evidence in either document that Bursa sustainability reporting has been completed; (2) Does the strategy document address ESG governance for each investee; (3) Which investees appear most at risk of Bursa ESG non-compliance based on the portfolio data — any without ESG reporting data; (4) What are the governance consequences for Danamas Capital if a listed investee misses the mandatory Bursa sustainability reporting deadline. Format as a 14-row compliance status matrix with RAG status.\"",
              fileRef: "GLC_01_Danamas_Capital.xlsx, GLC_02_Danamas_Strategy.docx"
            }
          ]
        },
        {
          tool: "🤝 Cowork (Pages)",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Build investee performance monitoring canvas",
              prompt: "In Copilot Chat, upload GLC_01_Danamas_Capital.xlsx and ask for a portfolio performance summary. Click Open in Copilot Pages. Ask: \"Reorganise this into a collaborative Investee Performance Monitoring Canvas for the Danamas Capital Investment Management team of 18 professionals. Structure as: (1) Portfolio Dashboard — NAV, ROE, dividend yield with quarterly trend; (2) Underperformer PIP Tracker — 3 companies with milestone status; (3) Danamas Infra Concession Renewal Tracker — stakeholder, milestones, timeline; (4) ESG Compliance Tracker — 14 investees with Bursa reporting status; (5) Investment Committee Decision Log. Format for collaborative editing by all 18 investment managers.\"",
              fileRef: "GLC_01_Danamas_Capital.xlsx"
            },
            {
              title: "Build investee turnaround planning canvas",
              prompt: "In Copilot Chat, upload GLC_02_Danamas_Strategy.docx and ask for a turnaround strategy summary. Click Open in Copilot Pages. Ask: \"Expand this into a collaborative Investee Turnaround Planning Canvas for 3 underperformer task forces, each with a 4-member Danamas Capital advisory team. Structure as: (1) Problem Statement per investee with key financial metrics; (2) Workstream Tracker — 5 turnaround pillars with owner and milestone; (3) 90-Day Sprint Plan with weekly milestones; (4) Decision Escalation Log for Board-level decisions; (5) Financial Recovery Model — quarterly ROE projections. Format for simultaneous editing by 3 task forces.\"",
              fileRef: "GLC_02_Danamas_Strategy.docx"
            }
          ]
        },
        {
          tool: "🤖 Word Agent",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Set up a Danamas Capital Strategy Advisor",
              prompt: "Open GLC_02_Danamas_Strategy.docx in Word. Create an agent named Danamas Portfolio Advisor. Instructions: \"Answer questions about Danamas Capital's portfolio strategy, investee performance, and governance. Cite document sections. Under 150 words.\" Demo: type \"What are the 3 underperforming investees and what are the specific ROE milestones they must achieve under their PIPs?\"",
              fileRef: "GLC_02_Danamas_Strategy.docx"
            },
            {
              title: "Demo the Danamas Portfolio Advisor — MOF review queries",
              prompt: "With the agent active, ask 3 queries a Ministry of Finance official would ask. Query 1: \"What is Danamas Capital's plan for the Danamas Infra concession renewal and what timeline is committed?\" Query 2: \"Which investees have received formal Performance Improvement Plans and what are the consequences of non-compliance?\" Query 3: \"What ESG and Bursa sustainability commitments has Danamas Capital made for its 14 investee companies?\"",
              fileRef: "GLC_02_Danamas_Strategy.docx"
            }
          ]
        },
        {
          tool: "🤖 PowerPoint Agent",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Set up a Portfolio Review Presenter agent",
              prompt: "Create or open the GLC portfolio performance PowerPoint. Save as Danamas_Capital_MOF_Review_2025.pptx. Create an agent named Danamas Portfolio Coach. Instructions: \"Answer questions about Danamas Capital's annual performance presentation. Reference slide numbers. Under 100 words.\" Demo: type \"Which slide shows the 3 underperformer companies and what are their current ROE figures?\""
            },
            {
              title: "Demo the Portfolio Coach — MOF bilateral preparation",
              prompt: "With the Danamas Portfolio Coach active, run 3 MOF bilateral preparation queries. Query 1: \"If MOF asks whether the PIP interventions are working — which slide has the most credible evidence of progress?\" Query 2: \"What is the total dividend yield of the portfolio for FY2024 and which slide shows the government unitholder returns?\" Query 3: \"Which slide addresses the Danamas Infra concession risk and what is the stated contingency plan if renewal is delayed?\""
            }
          ]
        },
        {
          tool: "🤖 Excel Agent",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Set up a Portfolio Analytics agent on Danamas workbook",
              prompt: "Open GLC_01_Danamas_Capital.xlsx. Create an agent named Danamas Portfolio Analytics. Instructions: \"Answer GLC portfolio questions using data from this workbook. Always cite the sheet. Express NAV in MYR billions and all other amounts in MYR millions.\" Demo: type \"What is the total portfolio NAV in MYR billions and which single investee has the highest NAV concentration as a percentage of the total?\"",
              fileRef: "GLC_01_Danamas_Capital.xlsx"
            },
            {
              title: "Demo the Portfolio Analytics — investment committee queries",
              prompt: "With the agent active, run 3 queries. Query 1: \"Which 3 investees have the lowest ROE in FY2024 and by how many percentage points is each below the 8% minimum threshold?\" Query 2: \"What was the total dividend income received by Danamas Capital from all 14 investees in FY2024 as a yield on total portfolio NAV?\" Query 3: \"What is the Danamas Infra equity value in MYR billions and what percentage of total portfolio NAV does it represent?\"",
              fileRef: "GLC_01_Danamas_Capital.xlsx"
            }
          ]
        }
      ]
    },
    {
      id: "education",
      name: "Education & Higher Learning",
      icon: "🎓",
      color: "#1A3A6E",
      accent: "#3498DB",
      company: "Citra University Group",
      tagline: "MQA audit in 8 weeks | Retention 84.2% vs 90% benchmark | 28,400 students | MYR 84M endowment",
      scenario: "Citra University Group (Citra) is a Malaysian private university group with 28,400 students across 4 campuses in Kuala Lumpur, Petaling Jaya, Johor Bahru, and Kota Kinabalu. Two strategic challenges dominate the FY2025 leadership agenda: an MQA programme accreditation audit in 8 weeks and a student retention rate of 84.2% — 5.8 percentage points below the 90% MQA benchmark. The retention gap represents approximately MYR 18 million in lost annual tuition revenue and poses accreditation risk for programmes with the weakest completion rates. Provost Dr Suraya Azman and the Board Academic Quality Committee need Copilot to accelerate audit preparation across 8 faculties, build a data-driven student at-risk early warning model, and present a credible endowment growth and scholarship expansion case to major donors.",
      files: ["EDU_01_Citra_University_Group.xlsx", "EDU_02_Citra_University_Strategy.docx", "Email_12_MQA_Notification.docx"],
      prompts: [
        {
          tool: "🤖 Copilot Chat (Basic)",
          license: "Free — no M365 license needed",
          account: "Sasha Ouellet — SashaO@ABSx62256373.OnMicrosoft.com",
          prompts: [
            {
              title: "Explain MQA accreditation and why student retention matters",
              prompt: "Ask Copilot: \"Explain what MQA (Malaysian Qualifications Agency) accreditation means for a private university in Malaysia and why Citra University Group's student retention rate of 84.2% — below the 90% industry benchmark — creates accreditation risk. Cover: (1) What MQA programme accreditation requires in terms of student completion rates and attrition thresholds; (2) What happens to a university's MQA accreditation if student retention falls below prescribed levels for 2 consecutive cycles; (3) The financial revenue impact of a 5.8 percentage point gap between 84.2% and the 90% benchmark across 28,400 students; (4) The 3 most common root causes of high student attrition at Malaysian private universities. Maximum 250 words.\""
            },
            {
              title: "Brief me before the MQA programme audit",
              prompt: "Ask Copilot: \"I am the Provost of Citra University Group, a Malaysian private university group with 28,400 students across 4 campuses. Our MQA programme audit is in 8 weeks. Brief me on: (1) The 5 most commonly cited MQA audit findings at Malaysian private universities — student records completeness, lecturer qualification ratios, curriculum delivery evidence, assessment moderation, and financial viability; (2) What specific documents and evidence MQA auditors review on the first day of an audit visit; (3) The 3 preparation actions that will have the highest impact in the 8-week window; (4) What a Conditional Accreditation outcome means for Citra's revenue and student intake for the next intake cycle. Maximum 200 words.\""
            },
            {
              title: "What is university endowment management and how does MYR 84M compare?",
              prompt: "Ask Copilot: \"Explain what a university endowment fund is and how it is managed. Citra University Group has a MYR 84 million endowment. Give context: (1) How large is MYR 84 million relative to comparable Malaysian private university endowments and to the top ASEAN university endowments; (2) What the typical endowment spending rule is — the 4-5% annual draw principle — and what MYR 84 million generates per year for Citra; (3) How endowment funds are typically invested by Malaysian private university foundations — equities, fixed income, and property; (4) The case for endowment growth — what impact would doubling the endowment to MYR 168 million have on Citra's annual scholarship and research budget. Maximum 250 words.\""
            }
          ]
        },
        {
          tool: "�� Researcher",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Research Malaysian private university competitive landscape",
              prompt: "In Copilot Chat, switch to the Researcher agent. Upload EDU_02_Citra_University_Strategy.docx. Ask: \"Review Citra University's strategy document, then search the web for: the competitive ranking of Malaysian private universities — Sunway, Taylor's, UCSI, INTI, and Multimedia University — by student enrolment, revenue, and graduate employment rate; recent MQA audit outcomes and enforcement actions for Malaysian private HEIs; student experience and retention best practices at private Asian universities with 20,000+ students; and Malaysia's TVET and Higher Education 2.0 policy implications for private universities. Cross-reference with Citra's strategy to identify the 3 most urgent competitive and regulatory priorities. Cite all sources.\"",
              fileRef: "EDU_02_Citra_University_Strategy.docx"
            },
            {
              title: "Research student retention strategies for higher education",
              prompt: "In Copilot Chat, switch to the Researcher agent. Ask: \"Search the web for evidence-based student retention strategies for private universities with 20,000 to 35,000 students. Find: AI-powered early warning systems for student at-risk identification used by Australian or UK universities with measurable retention improvement; mentoring programme models that have improved retention by 5 or more percentage points at comparable institutions; the financial ROI of a 1 percentage point improvement in student retention for a university earning average annual fees per student; and any Malaysian MQA guidance on minimum retention requirements for programme accreditation. Citra University has 28,400 students and 84.2% retention. What are the 3 highest-impact investments to close the 5.8 point gap to 90%? Cite sources.\""
            },
            {
              title: "Research international student recruitment for Malaysian universities",
              prompt: "In Copilot Chat, switch to the Researcher agent. Upload EDU_01_Citra_University_Group.xlsx. Ask: \"Review Citra's enrolment data. Then search the web for: Malaysia Education Blueprint 2015-2025 targets for international student enrolment at private universities; the top source countries for international students at Malaysian private universities in 2024 and 2025; marketing and scholarship strategies used by Malaysian universities that have grown international enrolment to 30% or more; and the Education Malaysia Global Services (EMGS) visa processing improvements for 2025. Citra's international student percentage and its growth potential — what investment would be needed to increase international enrolment by 20% in 2 years? Format as an internationalisation strategy brief.\"",
              fileRef: "EDU_01_Citra_University_Group.xlsx"
            }
          ]
        },
        {
          tool: "📊 Analyst",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Analyse Citra University enrolment and financial KPIs",
              prompt: "In Copilot Chat, switch to the Analyst agent. Upload EDU_01_Citra_University_Group.xlsx. Ask: \"Analyse the full Citra University dataset. Calculate: (1) Total enrolment trend by campus for FY2022 to FY2024 — which campus is growing and which is declining; (2) Student retention rate by programme — which faculties have retention below 80% and which programmes are driving the 84.2% overall; (3) Revenue per student by campus and programme type — identify the 3 most financially productive programmes; (4) Tuition fee revenue versus total operating cost — what is the EBITDA margin per campus; (5) Endowment fund return versus MYR 84 million principal — what is the annual yield. Present as a Provost academic and financial dashboard.\"",
              fileRef: "EDU_01_Citra_University_Group.xlsx"
            },
            {
              title: "Analyse student at-risk patterns and retention drivers",
              prompt: "In Copilot Chat, switch to the Analyst agent. Upload EDU_01_Citra_University_Group.xlsx. Ask: \"Analyse student retention data to identify at-risk patterns. Find: (1) The 3 faculties or programmes with the highest dropout rate — express as both number of students and percentage; (2) Whether attrition is concentrated in Year 1, Year 2, or final year students — which year is the highest-risk transition point; (3) The correlation between student academic performance in Semester 1 and subsequent dropout risk — is there a GPA threshold below which dropout probability spikes; (4) The financial aid and scholarship coverage rate — do students without financial support drop out at higher rates; (5) The total annual revenue lost per percentage point of retention improvement — what is the MYR value of going from 84.2% to 85.2% retention. Format as a Student Success investment case.\"",
              fileRef: "EDU_01_Citra_University_Group.xlsx"
            },
            {
              title: "Model endowment growth and scholarship programme ROI",
              prompt: "In Copilot Chat, switch to the Analyst agent. Upload EDU_01_Citra_University_Group.xlsx. Ask: \"Build a scholarship and endowment ROI model for Citra University. From the data: (1) What is the current endowment value at MYR 84 million and the annual income at a 4.5% annual draw rate; (2) If Citra launches a fundraising campaign to grow the endowment to MYR 150 million, what additional annual scholarship budget does this create; (3) Model the retention ROI: if MYR 5 million additional scholarships per year improve retention from 84.2% to 89%, calculate the incremental tuition revenue from retaining more students versus the scholarship cost; (4) What is the net financial benefit to Citra and the payback period. Format as an endowment expansion business case for the Board.\"",
              fileRef: "EDU_01_Citra_University_Group.xlsx"
            }
          ]
        },
        {
          tool: "📊 Copilot in Excel",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Instant Citra University performance summary",
              prompt: "Open EDU_01_Citra_University_Group.xlsx. Ask Copilot: \"Give me a plain-English executive summary of this workbook. What is the total student enrolment and year-on-year growth? What is the current student retention rate? Which campus has the lowest retention? What is the endowment fund current value? Flag any campus or programme where retention is below 80% or enrolment has declined 2 years in a row. Format: 3-sentence overview, then 4 specific flagged concerns with sheet name and row reference.\"",
              fileRef: "EDU_01_Citra_University_Group.xlsx"
            },
            {
              title: "Build student retention trend chart by campus",
              prompt: "Open EDU_01_Citra_University_Group.xlsx. Ask Copilot: \"Create a multi-line chart showing annual student retention rate from FY2020 to FY2024 for each of the 4 Citra University campuses. Add a horizontal reference line at 90% labelled MQA Benchmark and another at 84.2% labelled FY2024 Actual. Use different colours for each campus and add data labels at FY2024. Title: Citra University Group — Student Retention Rate by Campus FY2020-FY2024. This chart will be presented to the Board Academic and Quality Committee.\"",
              fileRef: "EDU_01_Citra_University_Group.xlsx"
            },
            {
              title: "Add revenue per student and programme profitability table",
              prompt: "Open EDU_01_Citra_University_Group.xlsx. Navigate to the Programme Financials sheet. Ask Copilot: \"Add 2 new calculated columns: (1) Revenue per Student — divide Programme Revenue by Student Enrolment for each programme; (2) Contribution Margin per Student — subtract Average Variable Cost per Student from Revenue per Student. Apply red formatting to any programme where Contribution Margin per Student is below MYR 8,000 per year. Tell me which 3 programmes have the highest revenue per student and which 3 have the lowest contribution margin.\"",
              fileRef: "EDU_01_Citra_University_Group.xlsx"
            },
            {
              title: "Natural language query — MQA audit readiness indicators",
              prompt: "Open EDU_01_Citra_University_Group.xlsx. Ask Copilot: \"Without navigating sheets, answer: (1) What percentage of programmes currently have student retention rates below the 90% MQA threshold — how many programmes out of the total; (2) What is the lecturer-to-student ratio across all 4 campuses and is it within MQA's minimum standard; (3) Which faculty or school has the highest Year 1 dropout rate and what is the percentage; (4) What is the total number of students currently on academic probation or at-risk monitoring and what percentage of total enrolment is this. Format as a 2-column MQA Audit Readiness Q and A.\"",
              fileRef: "EDU_01_Citra_University_Group.xlsx"
            }
          ]
        },
        {
          tool: "📝 Copilot in Word",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Summarise Citra University strategy into Board pre-read",
              prompt: "Open EDU_02_Citra_University_Strategy.docx. Ask Copilot: \"Summarise this strategy document into a 1-page Board pre-read for Citra University Group. Include: (1) The 3 strategic priorities for FY2025-2027; (2) The student retention challenge and the remediation plan; (3) MQA accreditation audit readiness status; (4) Endowment fund strategy — growth target and scholarship programme; (5) The 2 Board decisions required. Formal academic governance style. Maximum 400 words.\"",
              fileRef: "EDU_02_Citra_University_Strategy.docx"
            },
            {
              title: "Draft student retention action plan",
              prompt: "Open a new Word document. Ask Copilot: \"Draft a Student Retention Action Plan for Citra University Group addressing the 84.2% retention rate against the 90% MQA benchmark across 28,400 students on 4 campuses. The plan should include: (1) Root causes — top 3 identified: financial hardship, academic under-preparedness, and campus engagement; (2) Three initiatives: AI early warning system for at-risk students, financial aid expansion from MYR 8.4M to MYR 14M, and first-year experience programme redesign; (3) Campus-level retention targets for FY2025; (4) Governance — monthly Retention Committee chaired by the Provost; (5) MQA compliance milestones. Formal academic governance document. 500 words.\""
            },
            {
              title: "Rewrite student study skills guide for Year 1 students",
              prompt: "Open EDU_02_Citra_University_Strategy.docx. Locate the Student Success Framework section. Ask Copilot: \"Rewrite this student success framework section as a practical, friendly study skills and campus life guide for Citra University Year 1 students in their first 4 weeks. Replace all academic management policy language with direct advice for an 18-year-old student arriving from secondary school. Include: 5 practical tips for managing university workload, how to find a tutor or study group, how to request financial aid, and 3 campus resources they should use in Week 1. Maximum 350 words. Warm, encouraging, youth-friendly tone.\"",
              fileRef: "EDU_02_Citra_University_Strategy.docx"
            },
            {
              title: "Draft MQA audit response memo to all faculty deans",
              prompt: "Open a new Word document. Ask Copilot: \"Draft a formal memo from Citra University Provost to all 8 Faculty Deans informing them of the upcoming MQA programme audit in 8 weeks and their preparation responsibilities. The memo should: (1) State the audit scope — all undergraduate programmes across 4 campuses; (2) List the 5 documentation sets each Dean must prepare: student records, assessment moderation evidence, lecturer qualification files, curriculum delivery logs, and graduate employment data; (3) Assign a senior academic quality officer as the audit liaison for each faculty; (4) Set the internal mock audit date for 3 weeks before the MQA visit; (5) Emphasise that the Provost will conduct a spot-check of each faculty's preparation at week 4. Formal academic governance tone. 450 words.\""
            }
          ]
        },
        {
          tool: "🎯 Copilot in PowerPoint",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Create MQA audit readiness presentation",
              prompt: "Open a new PowerPoint. Ask Copilot: \"Create a 7-slide MQA Audit Readiness presentation for Citra University Group Board and Academic Quality Committee. Slide 1: Citra University — MQA Audit Readiness Update. Slide 2: Audit Overview — scope, date, and programmes in review. Slide 3: Student Retention — 84.2% actual vs 90% MQA benchmark with root cause analysis. Slide 4: Audit Readiness by Faculty — traffic light table for 8 faculties. Slide 5: Documentation Preparation Status — 5 evidence categories with completion percentage. Slide 6: 8-Week Sprint Plan — critical actions with owner and deadline. Slide 7: Board Support Needed — 2 decisions. Academic institution blue and white. Professional clean design.\""
            },
            {
              title: "Generate student experience transformation deck",
              prompt: "Open a new PowerPoint. Ask Copilot: \"Create a 5-slide student experience transformation strategy for Citra University Group Board. Slide 1: Why Student Experience is Citra's Competitive Advantage. Slide 2: Current State — retention 84.2%, at-risk early warning gap, financial aid utilisation. Slide 3: The Fix — AI early warning, expanded financial aid MYR 14M, first-year programme redesign. Slide 4: Expected Outcomes — retention to 90%, NPS improvement, MQA compliance. Slide 5: Investment and Timeline — MYR 12M over 2 years, payback via retained tuition revenue. Clean modern higher education design.\""
            },
            {
              title: "Add competitor university benchmarking slide",
              prompt: "In an open Citra University PowerPoint, add a new slide. Ask Copilot: \"Create a competitive benchmarking slide comparing Citra University Group against 4 comparable Malaysian private university groups: Sunway University, Taylor's University, UCSI University, and INTI International University. Compare 3 metrics: student retention rate, graduate employment rate at 6 months, and international student percentage. Use a clustered bar chart with Citra highlighted in the university brand colour and competitors in grey. Add a callout showing Citra's target positions for FY2027. Title: Citra University — Competitor Benchmarking FY2024.\""
            }
          ]
        },
        {
          tool: "📧 Copilot in Outlook",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Triage MQA audit notification email",
              prompt: "Open Outlook and locate Email_12_MQA_Notification.docx. Copy into a draft or open the email. Ask Copilot: \"I am the Citra University Registrar and I have received this MQA audit notification. Summarise: (1) The exact scope of the audit — which campuses, which programmes, and which MQA standards are being assessed; (2) What documentation must be prepared and by when; (3) The dates of the MQA site visit; (4) My 3 most urgent actions in the next 72 hours to initiate preparation. Maximum 200 words.\"",
              fileRef: "Email_12_MQA_Notification.docx"
            },
            {
              title: "Draft Provost email to students on retention support programme",
              prompt: "Open a new Outlook email. Ask Copilot: \"Draft an email from the Citra University Group Provost to all 28,400 enrolled students announcing the launch of the Student Success Programme. The email should: (1) Acknowledge that Citra cares about every student's success journey; (2) Describe 3 new support services: the Student Success Coach (one-on-one academic mentoring), the Financial Aid Fast-Track (same-week decisions for hardship applications), and the Peer Learning Circle (structured study group matching); (3) Include a clear call-to-action with a link to register and a 15 June 2025 deadline; (4) Close with an encouraging personal message from the Provost. Warm, student-centred, energising. Under 300 words.\""
            },
            {
              title: "Copilot coaching on response to parent complaint about student withdrawal",
              prompt: "In Outlook, type a rough draft response: \"Dear parent, we understand your concern. Your son's withdrawal was processed as per our procedures. If you want to appeal, you have 14 days. Regards, Citra University.\" Ask Copilot for coaching: \"I am the Dean of Students at a Malaysian private university. Evaluate this response on: (1) Empathy and tone — does it acknowledge the parent's distress; (2) Information completeness — does it explain what support was offered before withdrawal; (3) Process transparency — is the appeal process clearly explained. Rewrite at a standards-compliant, empathetic student affairs standard that reflects Citra's student-first values.\""
            }
          ]
        },
        {
          tool: "🎙 Copilot in Teams",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Catch up on missed academic quality committee meeting",
              prompt: "Open an existing Teams meeting that was recorded and has a Copilot recap from your calendar. Ask: \"I am the Citra University Deputy Provost and missed this Academic Quality Committee meeting. Catch me up: (1) Which programmes or campuses were discussed in the context of MQA compliance; (2) Were any programmes flagged for conditional accreditation risk; (3) Any specific actions assigned to the Deputy Provost or Academic Quality team; (4) Was the student retention programme discussed — if so, what was the status update; (5) Any decisions about the Faculty of Engineering programme that is below the 80% retention threshold.\""
            },
            {
              title: "Extract faculty action items from academic review",
              prompt: "Open an existing recorded Teams meeting from your calendar. Ask: \"Extract all academic and MQA compliance action items from this meeting. Format as: Action Description; Faculty or Department; Owner (role and name); Deadline; MQA Standard Reference if applicable; Priority — Critical if MQA audit is within 8 weeks, High if relates to student retention, Normal for routine. Also note: which faculty dean committed to completing their documentation preparation earliest and was there any faculty that appeared most behind on audit readiness.\""
            },
            {
              title: "Generate weekly academic update email from staff meeting",
              prompt: "Open an existing recorded Teams meeting recap from your calendar. Ask: \"Draft a weekly academic update email from the Citra University Provost to all 8 Faculty Deans and 4 Campus Directors. Based on this meeting: (1) MQA audit preparation status by faculty — 3-sentence overview; (2) Student retention programme launch update; (3) Key academic decisions made this week; (4) Next week's priority items for each faculty. Professional academic governance tone. Collaborative and supportive. Under 300 words.\""
            }
          ]
        },
        {
          tool: "📓 Copilot Notebook",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Full MQA audit brief from 3 university documents",
              prompt: "Go to Copilot Notebook. Upload EDU_01_Citra_University_Group.xlsx, EDU_02_Citra_University_Strategy.docx, and Email_12_MQA_Notification.docx. In Instructions: \"Using all 3 documents, prepare a comprehensive MQA audit readiness brief for the Citra University Provost. (1) From the MQA notification — what exactly is being audited, the visit dates, and evidence requirements; (2) From the financial and enrolment data — which campuses and programmes are most exposed to MQA scrutiny based on retention data; (3) From the strategy — does the strategy's retention improvement plan address the MQA risk within the 8-week preparation window; (4) What are the top 3 preparation actions that will have the highest MQA audit impact; (5) Build a Provost briefing paragraph for the Board meeting.\"",
              fileRef: "EDU_01_Citra_University_Group.xlsx, EDU_02_Citra_University_Strategy.docx, Email_12_MQA_Notification.docx"
            },
            {
              title: "Student retention and endowment strategy analysis",
              prompt: "Go to Copilot Notebook. Upload EDU_01_Citra_University_Group.xlsx and EDU_02_Citra_University_Strategy.docx. In Instructions: \"Using both documents, build a student retention and endowment ROI analysis for the Citra University Board. (1) From the enrolment data — quantify the annual revenue lost from students who withdraw — the cost of being at 84.2% vs 90% retention across 28,400 students at average annual fees; (2) From the strategy — what is the proposed investment in retention initiatives and scholarship expansion; (3) Calculate the payback period: if MYR 12M in retention investment over 2 years improves retention to 89%, what is the incremental tuition revenue and what is the net financial benefit; (4) Are there gaps between the strategy document's retention plan and the actual at-risk data in the workbook.\"",
              fileRef: "EDU_01_Citra_University_Group.xlsx, EDU_02_Citra_University_Strategy.docx"
            }
          ]
        },
        {
          tool: "🤝 Cowork (Pages)",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Build MQA audit preparation tracker in Pages",
              prompt: "In Copilot Chat, upload EDU_01_Citra_University_Group.xlsx and ask for an academic quality summary. Click Open in Copilot Pages. Ask: \"Reorganise this into a collaborative MQA Audit Preparation Tracker for the Citra University Academic Quality team of 12 members. Structure as: (1) Audit Scope and Timeline; (2) Documentation Readiness by Faculty — 8 faculties with traffic light status for 5 evidence categories each; (3) Student Retention Remediation Tracker; (4) Mock Audit Schedule; (5) Outstanding Actions with owner and deadline. Format for collaborative editing by all 8 Faculty Deans.\"",
              fileRef: "EDU_01_Citra_University_Group.xlsx"
            },
            {
              title: "Build student success programme planning canvas",
              prompt: "In Copilot Chat, upload EDU_02_Citra_University_Strategy.docx and ask for a student retention strategy summary. Click Open in Copilot Pages. Ask: \"Expand this into a collaborative Student Success Programme Planning Canvas for the Citra University Student Affairs team across 4 campuses. Structure as: (1) At-Risk Student Identification Framework; (2) Intervention Programme Tracker — 3 initiatives with campus rollout status; (3) Financial Aid Case Pipeline — weekly new applications and decisions; (4) Peer Learning Circle coordination across campuses; (5) Weekly Retention KPI Dashboard. Format for simultaneous input from all 4 campus Student Affairs Directors.\"",
              fileRef: "EDU_02_Citra_University_Strategy.docx"
            }
          ]
        },
        {
          tool: "🤖 Word Agent",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Set up a Citra University Academic Quality Advisor",
              prompt: "Open EDU_02_Citra_University_Strategy.docx in Word. Create an agent named Citra Academic Advisor. Instructions: \"Answer questions about Citra University's academic strategy, MQA compliance, and student success programmes. Cite sections. Under 150 words.\" Demo: type \"What is the strategy's plan to raise student retention from 84.2% to 90% and what are the three main initiatives?\"",
              fileRef: "EDU_02_Citra_University_Strategy.docx"
            },
            {
              title: "Demo the Academic Advisor — Board and MQA queries",
              prompt: "With the agent active, ask 3 queries. Query 1: \"What is the timeline in the strategy for achieving full MQA compliance across all 4 campuses?\" Query 2: \"What investment is committed to the AI early warning system for at-risk students and what retention improvement is expected?\" Query 3: \"How does the strategy plan to grow the endowment from MYR 84 million and what is the 5-year target?\"",
              fileRef: "EDU_02_Citra_University_Strategy.docx"
            }
          ]
        },
        {
          tool: "🤖 PowerPoint Agent",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Set up an MQA Readiness Presenter agent",
              prompt: "Create or open the MQA audit readiness PowerPoint from the PPT demo. Save as Citra_MQA_Readiness_2025.pptx. Create an agent named MQA Audit Coach. Instructions: \"Answer questions about Citra University's MQA audit readiness presentation. Reference slide numbers. Under 100 words.\" Demo: type \"Which slide shows the faculty audit readiness traffic light table and how many faculties are currently in Red or Amber status?\""
            },
            {
              title: "Demo the MQA Audit Coach — Board queries",
              prompt: "With the MQA Audit Coach active, run 3 queries. Query 1: \"What is the most critical MQA compliance gap and which faculty is responsible?\" Query 2: \"Which slide shows the student retention trend and what is Citra's retention rate compared to the MQA 90% benchmark?\" Query 3: \"What are the 3 most important Board decisions needed to support MQA audit preparation in the next 8 weeks?\""
            }
          ]
        },
        {
          tool: "🤖 Excel Agent",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Set up a University Performance Agent",
              prompt: "Open EDU_01_Citra_University_Group.xlsx. Create an agent named Citra University Advisor. Instructions: \"Answer questions about Citra University's enrolment, retention, and financial performance. Cite sheet names. Express revenue in MYR millions.\" Demo: type \"What is the student retention rate for FY2024 and which campus has the lowest retention?\"",
              fileRef: "EDU_01_Citra_University_Group.xlsx"
            },
            {
              title: "Demo the University Advisor — academic and financial queries",
              prompt: "With the agent active, run 3 queries. Query 1: \"Which 3 faculties have student retention below 80% and how many students does this represent in total?\" Query 2: \"What is the total tuition fee revenue for FY2024 and what is the implied revenue loss from the 5.8 percentage point gap between actual 84.2% and the 90% target?\" Query 3: \"What is the endowment fund annual income at the current 4.5% draw rate and how does this compare to the annual scholarship budget?\"",
              fileRef: "EDU_01_Citra_University_Group.xlsx"
            }
          ]
        }
      ]
    },
    {
      id: "hospitality",
      name: "Hospitality & Tourism",
      icon: "🏨",
      color: "#8B4513",
      accent: "#E67E22",
      company: "Suria Hotels and Resorts Group",
      tagline: "RevPAR MYR 284 vs MYR 308 target | F&B down 18% | Turnover 32% | 18 properties Malaysia",
      scenario: "Suria Hotels and Resorts Group (Suria) operates 18 upscale and upper-midscale hotels across Peninsular Malaysia and East Malaysia, including city business hotels, beach resorts, and convention properties. Three interconnected performance challenges define the FY2025 leadership agenda: a RevPAR of MYR 284 against a MYR 308 target driven by below-target occupancy at 68.4%; F&B revenue down 18% year-on-year across all 18 outlet operations; and a staff turnover rate of 32% driving up recruitment and training costs. Group CEO Azrina Hamid and the revenue management team need Copilot to diagnose the performance gaps by property, build the F&B recovery programme, make the revenue management system investment case, and present a credible workforce retention strategy at the upcoming General Managers Annual Conference.",
      files: ["HT_01_Suria_Hotels_Resorts.xlsx", "Email_13_Corporate_Account.docx"],
      prompts: [
        {
          tool: "🤖 Copilot Chat (Basic)",
          license: "Free — no M365 license needed",
          account: "Sasha Ouellet — SashaO@ABSx62256373.OnMicrosoft.com",
          prompts: [
            {
              title: "Explain RevPAR and what MYR 284 means for a Malaysian hotel group",
              prompt: "Ask Copilot: \"Explain Revenue Per Available Room (RevPAR) for a hotel management audience and put Suria Hotels and Resorts Group's current RevPAR of MYR 284 in context. Cover: (1) The RevPAR formula — ADR multiplied by occupancy rate — and how a RevPAR of MYR 284 at 68.4% occupancy implies an ADR; (2) What MYR 284 RevPAR means versus the Malaysian hotel market benchmarks for upscale and upper-upscale properties in KL and the islands; (3) Why Suria's 68.4% occupancy is below the 72% target and what the revenue impact is across 18 properties; (4) The 3 most effective RevPAR improvement levers for a mid-to-upscale Malaysian hotel group. Maximum 250 words.\""
            },
            {
              title: "Brief me on the F&B revenue decline before the GM conference",
              prompt: "Ask Copilot: \"I am the Group CEO of Suria Hotels and Resorts Group, operating 18 properties. Our F&B revenue is down 18% year-on-year — a significant decline. I have a General Managers conference next week where I need to address this. Brief me on: (1) The 5 most common root causes of F&B revenue decline in hotel groups — competitive pressure from standalone restaurants, occupancy correlation, menu and concept fatigue, pricing elasticity, and pandemic hangover shifts in dining behaviour; (2) Which of these is most consistent with an 18% decline across 18 hotels simultaneously; (3) The 3 most commercially effective F&B turnaround interventions for a hotel group of Suria's scale; (4) How F&B profitability compares to room revenue in terms of contribution margin. Maximum 200 words.\""
            },
            {
              title: "What causes high hotel staff turnover and how does 32% compare?",
              prompt: "Ask Copilot: \"Explain the hotel industry staff turnover problem. Suria Hotels and Resorts has a 32% staff turnover rate. Contextualise: (1) What the average hotel staff turnover rate is in Malaysia and globally for upscale hotel properties — cite industry benchmarks from AHLA or Horwath HTL; (2) The fully-loaded financial cost of 32% turnover across 18 hotels — include recruitment cost, training cost, productivity loss during ramp-up, and service quality impact; (3) The 3 specific hotel roles with the highest turnover rate industry-wide and why; (4) The 3 hotel-specific retention strategies that deliver the fastest turnover reduction — flexible scheduling, tipping programme formalisation, or career progression pathways. Maximum 250 words.\""
            }
          ]
        },
        {
          tool: "�� Researcher",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Research Malaysian hotel market recovery and competitive trends",
              prompt: "In Copilot Chat, switch to the Researcher agent. Upload HT_01_Suria_Hotels_Resorts.xlsx. Ask: \"Review Suria Hotels' performance data, then search the web for: Malaysian hotel industry performance data from Tourism Malaysia and STR Global for 2024-2025 — average occupancy, ADR, and RevPAR for upscale hotels in KL, Penang, and beach resort segments; competitive analysis of Malaysian hotel chains — YTL Hotels, Shangri-La, and Berjaya Hotels — and their RevPAR and F&B performance; and the impact of the Visit Malaysia Year 2026 campaign on hotel forward bookings. Cross-reference with Suria's current performance to identify the 3 most urgent revenue recovery opportunities. Cite all sources.\"",
              fileRef: "HT_01_Suria_Hotels_Resorts.xlsx"
            },
            {
              title: "Research F&B turnaround strategies for hotel groups",
              prompt: "In Copilot Chat, switch to the Researcher agent. Ask: \"Search the web for evidence-based F&B revenue turnaround strategies for hotel groups with 15 to 25 properties in ASEAN. Find: dynamic pricing and yield management tools for hotel F&B that improve revenue per seat; restaurant concept refresh and menu engineering approaches used by Malaysian and Thai hotel groups; all-inclusive F&B package models that have improved F&B revenue per occupied room; and hotel F&B digital ordering and delivery integration with GrabFood and delivery super-apps. Suria Hotels has F&B revenue down 18%. What are the 3 highest-impact F&B recovery strategies with measurable revenue uplift within 12 months? Cite sources.\""
            },
            {
              title: "Research hotel staff retention and scheduling technology",
              prompt: "In Copilot Chat, switch to the Researcher agent. Upload HT_01_Suria_Hotels_Resorts.xlsx. Ask: \"Review Suria Hotels' HR data. Then search the web for: hotel workforce management technology platforms — HotSchedules, Fourth, and Quinyx — and their measurable impact on hotel staff turnover; compensation benchmarking data for Malaysian hotel F&B and rooms division staff in upscale properties; hotel group employee value proposition best practices — benefits, flexible rostering, career ladder programmes; and Malaysia's hotel and hospitality sector average wages against the MTUC living wage framework. Suria has 32% turnover. What retention programme would have the highest impact and at what cost per employee retained?\"",
              fileRef: "HT_01_Suria_Hotels_Resorts.xlsx"
            }
          ]
        },
        {
          tool: "📊 Analyst",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Analyse Suria Hotels revenue and RevPAR performance",
              prompt: "In Copilot Chat, switch to the Analyst agent. Upload HT_01_Suria_Hotels_Resorts.xlsx. Ask: \"Analyse the full Suria Hotels dataset. Calculate: (1) RevPAR for each of the 18 properties and identify the 3 best-performing and 3 worst-performing hotels; (2) The total room revenue shortfall from current 68.4% occupancy versus the 72% target — across all 18 properties at average ADR; (3) F&B revenue per occupied room room-night and the trend from FY2022 to FY2024 — confirming the 18% decline; (4) The EBITDA margin contribution from rooms versus F&B — which is more profitable per revenue MYR; (5) The workforce cost as a percentage of total revenue and the correlation with properties that have highest turnover. Present as a Group CEO hospitality KPI dashboard.\"",
              fileRef: "HT_01_Suria_Hotels_Resorts.xlsx"
            },
            {
              title: "Model RevPAR improvement and occupancy recovery",
              prompt: "In Copilot Chat, switch to the Analyst agent. Upload HT_01_Suria_Hotels_Resorts.xlsx. Ask: \"Build a RevPAR recovery model for Suria Hotels. From the data: (1) Calculate the total incremental room revenue in MYR millions if occupancy recovers from 68.4% to 72% across all 18 properties at current ADR; (2) Calculate the additional revenue if ADR also increases by 8% through revenue management software — combined effect with occupancy recovery; (3) Model a F&B recovery scenario: if F&B revenue per occupied room-night recovers by 10% through menu engineering and digital ordering integration, what is the total annual F&B revenue uplift in MYR millions; (4) Total combined revenue opportunity. Format as a Group Revenue Management investment case.\"",
              fileRef: "HT_01_Suria_Hotels_Resorts.xlsx"
            },
            {
              title: "Analyse staff turnover cost and retention programme ROI",
              prompt: "In Copilot Chat, switch to the Analyst agent. Upload HT_01_Suria_Hotels_Resorts.xlsx. Ask: \"Analyse the staff turnover cost and retention ROI for Suria Hotels. From the data: (1) Calculate the total annual staff turnover cost across 18 properties at 32% turnover — use MYR 8,400 per departure as the fully-loaded replacement and training cost; (2) Build 3 turnover reduction scenarios: Reduce to 25% (modest improvement), 22% (industry average), and 18% (best-in-class). For each: annual cost saving in MYR millions; (3) Model the ROI of a MYR 3.8 million per year retention programme — flexible scheduling technology, enhanced benefits, and career pathways — that achieves 25% turnover reduction; (4) Payback period. Format as a Group CHRO retention investment case.\"",
              fileRef: "HT_01_Suria_Hotels_Resorts.xlsx"
            }
          ]
        },
        {
          tool: "📊 Copilot in Excel",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Instant Suria Hotels performance summary",
              prompt: "Open HT_01_Suria_Hotels_Resorts.xlsx. Ask Copilot: \"Give me a plain-English executive summary of this hotel group workbook. What is the group average RevPAR and how does it compare to the MYR 308 target? What is the average occupancy versus the 72% target? What is the F&B revenue decline percentage? What is the staff turnover rate? Flag any property with occupancy below 60% or F&B revenue decline more than 25%. Format: 3-sentence overview, then 4 specific flagged concerns with sheet name and row reference.\"",
              fileRef: "HT_01_Suria_Hotels_Resorts.xlsx"
            },
            {
              title: "Build RevPAR waterfall and property comparison chart",
              prompt: "Open HT_01_Suria_Hotels_Resorts.xlsx. Ask Copilot: \"Create a horizontal bar chart ranking all 18 Suria Hotels properties by FY2024 RevPAR from highest to lowest. Add a vertical reference line at MYR 284 labelled Group Average and another at MYR 308 labelled RevPAR Target. Use green bars for properties above MYR 284 and red bars for those below. Add property name and exact RevPAR value on each bar. Title: Suria Hotels and Resorts — Property RevPAR Ranking FY2024. For the General Managers conference presentation.\"",
              fileRef: "HT_01_Suria_Hotels_Resorts.xlsx"
            },
            {
              title: "Add F&B revenue per room and staff cost per room analysis",
              prompt: "Open HT_01_Suria_Hotels_Resorts.xlsx. Navigate to the Property KPI sheet. Ask Copilot: \"Add 2 calculated columns: (1) F&B Revenue per Occupied Room-Night — F&B Revenue divided by Total Occupied Room-Nights; (2) Staff Cost per Available Room — Total Staff Cost divided by Total Available Rooms. Apply red formatting to the F&B metric for properties below MYR 42 per occupied room-night (the group minimum target). Apply amber to Staff Cost per Available Room above MYR 85,000 (the cost threshold). Tell me which properties fail both metrics simultaneously and what that indicates about profitability.\"",
              fileRef: "HT_01_Suria_Hotels_Resorts.xlsx"
            },
            {
              title: "Natural language query — GM conference preparation",
              prompt: "Open HT_01_Suria_Hotels_Resorts.xlsx. Ask Copilot: \"Without navigating sheets, answer these questions I need for the General Managers conference: (1) Which 5 properties have the highest RevPAR improvement from FY2023 to FY2024 — list them and state the MYR improvement; (2) Which 5 properties have the worst F&B revenue decline percentage — list them; (3) What is the correlation between occupancy rate and F&B revenue — do high-occupancy hotels have proportionally higher F&B revenue or not; (4) Which property has the lowest staff turnover and what is its RevPAR — is low turnover associated with better RevPAR performance. Format as a 2-column Q and A table for the GM conference.\"",
              fileRef: "HT_01_Suria_Hotels_Resorts.xlsx"
            }
          ]
        },
        {
          tool: "📝 Copilot in Word",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Summarise hotel group strategy into Board pre-read",
              prompt: "In Copilot Chat, upload HT_01_Suria_Hotels_Resorts.xlsx and ask for a hotel group summary then open Word or open HC_02_Apex_Health_Strategy.docx as the reference. Actually: Open a new Word document. Ask Copilot: \"Write a 1-page Board pre-read memo for Suria Hotels and Resorts Group summarising FY2024 performance and FY2025 priorities. Include: (1) Key FY2024 metrics — RevPAR MYR 284 vs MYR 308 target, occupancy 68.4% vs 72% target, F&B down 18%, staff turnover 32%; (2) The 3 strategic priorities for FY2025 — revenue management systems investment, F&B concept refresh at 6 properties, and workforce retention programme; (3) Capital investment required; (4) The 2 Board decisions needed. Formal hotel Board memo style. Maximum 400 words.\""
            },
            {
              title: "Draft F&B turnaround programme for General Managers",
              prompt: "Open a new Word document. Ask Copilot: \"Draft a formal F&B Revenue Recovery Programme brief from the Suria Hotels Group F&B Director to all 18 General Managers. The brief addresses the 18% F&B revenue decline and outlines a 90-day recovery programme. Include: (1) Root cause diagnosis — 3 identified issues: menu fatigue at flagship restaurants, loss of corporate lunch business, and low digital ordering adoption; (2) Three recovery actions effective immediately: daily F&B yield meeting at each property, GrabFood integration at all 18 F&B outlets by 1 July 2025, and a weekday set-lunch promotion at MYR 48 targeted at corporate and hotel guests; (3) F&B revenue target per property for Q3 FY2025; (4) Weekly reporting cadence to Group F&B Director. Operational, direct, clear. 450 words.\""
            },
            {
              title: "Rewrite hotel staff induction guide for F&B team",
              prompt: "Open a new Word document. Ask Copilot: \"Write a fresh, engaging Staff Induction Guide for new F&B team members joining any Suria Hotels property. The guide should cover: (1) Welcome from the Group CEO — 2 sentences about Suria's culture and commitment to staff; (2) Your First Week — 5 practical things to do in your first 5 days including uniform collection, systems training, property tour, shadow shifts, and meeting your supervisor; (3) Suria's Service Standards — 3 service values translated into 3 observable behaviours each; (4) Career Pathway — how a F&B server can progress to Team Leader, Outlet Supervisor, and Outlet Manager in 3 years; (5) Where to Get Help. Maximum 400 words. Warm, practical, professional.\""
            },
            {
              title: "Draft revenue management investment proposal memo",
              prompt: "Open a new Word document. Ask Copilot: \"Draft a formal Board memo from the Suria Hotels Group Chief Revenue Officer proposing investment in a dynamic revenue management system for all 18 properties. The memo should cover: (1) Problem statement — current RevPAR of MYR 284 versus MYR 308 target; manual rate-setting across 18 properties causing rate leakage and OTA margin loss; (2) Proposed system — an AI-powered RMS integrated with all OTAs, direct booking engine, and GDS, costing MYR 2.8 million implementation plus MYR 280,000 annual licence; (3) Financial case — expected RevPAR improvement of MYR 18 per property through optimised pricing and length-of-stay controls; (4) Payback period at group revenue level. Formal hotel Board approval memo. 500 words.\""
            }
          ]
        },
        {
          tool: "🎯 Copilot in PowerPoint",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Create General Managers annual conference presentation",
              prompt: "Open a new PowerPoint. Ask Copilot: \"Create an 8-slide presentation for the Suria Hotels and Resorts Group General Managers Annual Conference. Slide 1: Suria Hotels — FY2024 Review and FY2025 Direction. Slide 2: Group Performance Dashboard — RevPAR, occupancy, F&B, turnover. Slide 3: RevPAR Ranking — all 18 properties horizontal bar chart. Slide 4: F&B Turnaround Programme — problem, plan, targets. Slide 5: Revenue Management Technology — RMS investment case. Slide 6: Workforce Retention Programme — 32% to 22% target, 3 initiatives. Slide 7: FY2025 Property Targets — occupancy, RevPAR, F&B targets per GM. Slide 8: CEO Message. Warm hospitality gold and white theme. Energising and visual.\""
            },
            {
              title: "Generate hotel group investor pitch deck",
              prompt: "Open a new PowerPoint. Ask Copilot: \"Create a 5-slide investor pitch for Suria Hotels and Resorts Group targeting a Malaysian sovereign wealth fund considering a stake investment. Slide 1: Suria Hotels — 18 Properties, MYR 284 RevPAR, Built for Malaysia's Tourism Recovery. Slide 2: Our Portfolio — property type mix, geographic spread, brand positioning. Slide 3: The Revenue Opportunity — RevPAR recovery to MYR 308, F&B turnaround, Visit Malaysia 2026 tailwind. Slide 4: Investment Plan — MYR 38M capex over 3 years, 3 growth levers, projected EBITDA uplift. Slide 5: Investment Ask and Returns. Professional investor-grade design. Gold and navy blue.\""
            },
            {
              title: "Add hotel market benchmarking slide",
              prompt: "In an open Suria Hotels PowerPoint, add a new slide. Ask Copilot: \"Create a Malaysian hotel market benchmarking slide comparing Suria Hotels against 3 comparable upscale hotel chains: YTL Hotels, Berjaya Hotels and Resorts, and Shangri-La Malaysia. Compare RevPAR, occupancy rate, and F&B revenue as a percentage of total revenue for the most recent fiscal year. Use a 3-metric clustered bar chart with Suria highlighted in gold. Add a callout showing the revenue opportunity if Suria closes the RevPAR gap to the sector leader. Title: Suria Hotels — Market Performance vs Upscale Hotel Peers Malaysia FY2024.\""
            }
          ]
        },
        {
          tool: "📧 Copilot in Outlook",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Triage urgent review from a corporate account threatening to renegotiate",
              prompt: "Open Outlook and locate Email_13_Corporate_Account.docx. Copy into a draft or open the email. Ask Copilot: \"I am the Suria Hotels Group Director of Sales and I have received this email from a top corporate account — a Malaysian bank that provides 280 room-nights per month at MYR 388 ADR. Summarise: (1) What is the client specifically complaining about — service quality, pricing, or competitive alternative; (2) What are they threatening — renegotiation, suspension, or churn to a competitor; (3) The MYR annual revenue at risk if this account moves; (4) My 3 recommended actions in the next 48 hours to retain the account. Maximum 200 words.\"",
              fileRef: "Email_13_Corporate_Account.docx"
            },
            {
              title: "Draft Group CEO letter to all hotel partners and suppliers on F&B recovery",
              prompt: "Open a new Outlook email. Ask Copilot: \"Draft a formal letter from Suria Hotels Group CEO to the group's top 20 F&B suppliers announcing the F&B Revenue Recovery Programme. The letter should: (1) Acknowledge that Suria's F&B revenue has declined and explain the Group's commitment to rebuilding F&B strength; (2) Outline 3 changes that will affect suppliers positively: increased menu rotation, pilot of 4 new concept outlets at flagship properties, and digital ordering integration expanding reach; (3) Invite suppliers to a joint F&B Innovation Day at the flagship KL property on 20 June 2025 to co-develop new menu concepts; (4) Reaffirm Suria's commitment to supporting Malaysian food and beverage brands in all outlets. Warm, professional, partnership-focused. 300 words.\""
            },
            {
              title: "Copilot coaching on response to TripAdvisor review escalation",
              prompt: "In Outlook, type a rough draft response to a guest complaints email escalation: \"Dear guest, sorry you had a bad experience. We will look into it. Thanks for your feedback.\" Ask Copilot for coaching: \"I am the Guest Experience Director at a Malaysian upscale hotel group. Evaluate this response on: (1) Service recovery language — does it demonstrate genuine empathy and urgency; (2) Resolution specificity — does it commit to a specific remedy; (3) Brand protection — does it reflect the standards of a premium hotel. Rewrite the response at a 5-star guest experience standard with a specific compensation offer and direct contact details for follow-up.\""
            }
          ]
        },
        {
          tool: "🎙 Copilot in Teams",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Catch up on missed revenue management review",
              prompt: "Open an existing Teams meeting that was recorded and has a Copilot recap from your calendar. Ask: \"I am the Suria Hotels Group Chief Revenue Officer and I missed this meeting because I was at a property opening. Catch me up: (1) Which properties were discussed in the RevPAR and occupancy review; (2) Were any pricing or rate changes approved for the upcoming peak season; (3) Was the RMS investment decision discussed — if so, what was the outcome; (4) Actions assigned to the CRO or Revenue Management team; (5) Any F&B pricing or menu decisions taken that affect the outlet revenue targets.\""
            },
            {
              title: "Extract operations actions from the GM weekly briefing",
              prompt: "Open an existing recorded Teams meeting from your calendar. Ask: \"Extract all hotel operations and F&B action items from this weekly GM briefing. Format as: Property Name; Action Type (RevPAR, F&B, Staffing, or Capital); Specific Action; GM Owner; Deadline; Priority — Critical for actions affecting Q3 revenue targets, High for guest experience actions, Normal for routine. Highlight any property where 3 or more action items are assigned simultaneously as it may indicate an operational stress point.\""
            },
            {
              title: "Draft GM conference follow-up email from CEO",
              prompt: "Open an existing recorded Teams meeting recap from your calendar — a leadership, conference, or executive meeting. Ask: \"Draft a follow-up email from the Suria Hotels Group CEO to all 18 General Managers after the annual conference. Based on this meeting: (1) Summarise the 3 key strategic priorities communicated at the conference; (2) Confirm each GM's individual property targets for FY2025 — RevPAR, occupancy, and F&B; (3) Launch the monthly GM performance scorecard reporting — due 5th of each month; (4) Thank the GMs personally for their commitment. Warm but commercially focused CEO communication. Under 300 words.\""
            }
          ]
        },
        {
          tool: "📓 Copilot Notebook",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Full hotel performance brief from 2 documents",
              prompt: "Go to Copilot Notebook. Upload HT_01_Suria_Hotels_Resorts.xlsx and Email_13_Corporate_Account.docx. In Instructions: \"Using both documents, prepare a revenue recovery brief for the Suria Hotels Group CEO. (1) From the hotel performance data — identify the 3 most urgent revenue recovery opportunities across the 18-property portfolio; (2) From the corporate account email — quantify the annual revenue at risk and determine whether the account's concerns are addressable without renegotiating price; (3) Cross-reference: is the account's complaint consistent with the performance data for that specific property; (4) Build a 5-point CEO action agenda for the first week addressing both the portfolio revenue gap and the corporate account retention. Format as a CEO daily priorities brief.\"",
              fileRef: "HT_01_Suria_Hotels_Resorts.xlsx, Email_13_Corporate_Account.docx"
            },
            {
              title: "F&B recovery and staff retention investment analysis",
              prompt: "Go to Copilot Notebook. Upload HT_01_Suria_Hotels_Resorts.xlsx. In Instructions: \"Using the hotel performance data, build 2 connected investment analyses for the Suria Hotels Board. First — F&B Recovery ROI: if the 18% F&B decline is reversed through a MYR 4.2 million menu refresh and digital ordering programme, and F&B revenue per occupied room-night improves by MYR 12, calculate total annual revenue uplift across 18 properties and payback period. Second — Staff Retention ROI: if MYR 3.8 million per year in retention investment reduces turnover from 32% to 22%, calculate the total annual cost saving from reduced recruitment and training, the impact on guest satisfaction scores, and the net financial benefit. Present as 2 connected investment cases for the Board.\"",
              fileRef: "HT_01_Suria_Hotels_Resorts.xlsx"
            }
          ]
        },
        {
          tool: "🤝 Cowork (Pages)",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Build hotel revenue recovery tracker in Pages",
              prompt: "In Copilot Chat, upload HT_01_Suria_Hotels_Resorts.xlsx and ask for a property performance summary. Click Open in Copilot Pages. Ask: \"Reorganise this into a collaborative Revenue Recovery Tracker for the Suria Hotels Group Revenue Management and F&B teams. Structure as: (1) Group RevPAR Dashboard — actual vs target by property; (2) F&B Recovery Tracker — 18 properties with weekly F&B revenue vs Q3 target; (3) Occupancy and Pricing Calendar — rate strategy for the next 90 days; (4) Corporate Account Pipeline — key accounts with contract renewal status; (5) Weekly Actions Log. Format for collaborative editing by 18 GMs and the Group CRO.\"",
              fileRef: "HT_01_Suria_Hotels_Resorts.xlsx"
            },
            {
              title: "Build workforce retention planning canvas",
              prompt: "In Copilot Chat, type a workforce management problem statement and ask for a retention programme outline. Click Open in Copilot Pages. Ask: \"Create a collaborative Workforce Retention Planning Canvas for the Suria Hotels Group CHRO and 18 property HR Managers. The context: 32% staff turnover and a programme to reduce it to 22%. Structure as: (1) Turnover Diagnosis by Property — each GM to input their root cause; (2) Retention Initiative Tracker — 3 group-wide initiatives with property-level rollout status; (3) Compensation Benchmarking Grid — current vs market for F&B and rooms roles; (4) Career Pathway Showcase — open internal promotion opportunities; (5) Monthly Turnover KPI Log. Format for simultaneous input from all 18 properties.\""
            }
          ]
        },
        {
          tool: "🤖 Word Agent",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Set up a Suria Hotels Revenue Strategy Advisor",
              prompt: "Open a recently created or saved Suria Hotels strategy document in Word — or create one by asking Copilot to generate an F&B and revenue recovery strategy summary and saving it as Suria_Hotels_Strategy_2025.docx. Create an agent named Suria Revenue Advisor. Instructions: \"Answer questions about Suria Hotels revenue strategy, F&B recovery, and workforce retention. Cite sources. Under 150 words.\" Demo: type \"What is the plan to recover F&B revenue from the current 18% decline and what are the 3 key initiatives?\""
            },
            {
              title: "Demo the Suria Revenue Advisor — GM conference queries",
              prompt: "With the agent active, ask 3 queries a General Manager would ask. Query 1: \"What is the specific RevPAR improvement target for my property and what does the strategy say are the most effective levers at property level?\" Query 2: \"What F&B concept refresh programmes are approved for rollout in FY2025 and which properties are first in line?\" Query 3: \"How does the workforce retention programme affect my property's staffing budget for FY2025?\""
            }
          ]
        },
        {
          tool: "🤖 PowerPoint Agent",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Set up a GM Conference Presenter agent",
              prompt: "Create or open the GM Conference PowerPoint from the PPT demo. Save as Suria_Hotels_GM_Conference_2025.pptx. Create an agent named GM Conference Coach. Instructions: \"Answer questions about Suria Hotels' GM conference presentation. Reference slide numbers. Under 100 words.\" Demo: type \"Which slide shows each property's individual FY2025 RevPAR target and what is the group average target?\""
            },
            {
              title: "Demo the GM Conference Coach — GM preparation queries",
              prompt: "With the agent active, run 3 queries a General Manager would ask before presenting to their hotel team. Query 1: \"Which slide covers the F&B recovery programme and what are the 3 immediate actions every GM is required to take?\" Query 2: \"What slide shows the staff retention initiative and when does the flexible scheduling technology go live?\" Query 3: \"If my property is currently below the group average RevPAR, which slide gives me the most useful benchmarking context to share with my team?\""
            }
          ]
        },
        {
          tool: "🤖 Excel Agent",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Set up a Hotel Performance Agent on Suria workbook",
              prompt: "Open HT_01_Suria_Hotels_Resorts.xlsx. Create an agent named Suria Hotels Advisor. Instructions: \"Answer hotel performance questions using data from this workbook. Cite sheet names. Express revenue in MYR millions.\" Demo: type \"What is the group average RevPAR for FY2024 and which single property has the highest RevPAR?\"",
              fileRef: "HT_01_Suria_Hotels_Resorts.xlsx"
            },
            {
              title: "Demo the Hotel Advisor — revenue and workforce queries",
              prompt: "With the agent active, run 3 queries. Query 1: \"Which 3 properties have the lowest occupancy rate in FY2024 and by how many percentage points are they below the 72% target?\" Query 2: \"What is the total F&B revenue across all 18 properties in FY2024 compared to FY2023 — confirm the percentage decline?\" Query 3: \"Which 3 properties have staff turnover above 40% and is there any correlation between high turnover and below-average RevPAR at those same properties?\"",
              fileRef: "HT_01_Suria_Hotels_Resorts.xlsx"
            }
          ]
        }
      ]
    },
    {
      id: "plantation",
      name: "Plantation & Agribusiness",
      icon: "🌴",
      color: "#1A4D2E",
      accent: "#2ECC71",
      company: "Perkebunan Lestari Group",
      tagline: "RSPO 2 mills suspended | EUDR Jan 2026 deadline | OER 19.4% vs 21.2% | 184,200 ha",
      scenario: "Perkebunan Lestari Group (Lestari) is a Malaysian palm oil plantation company operating 184,200 hectares across Sabah, Sarawak, and Kalimantan with 18 crude palm oil mills processing 4.2 million tonnes of fresh fruit bunches annually. Three interconnected sustainability and operational challenges define the FY2025 leadership agenda: 2 mills were suspended from RSPO certification in Q4 FY2024 after failing traceability and no-burn compliance audits; the EU Deforestation Regulation (EUDR) compliance deadline of January 2026 requires plot-level geolocation data across all 184,200 hectares; and oil extraction rate (OER) at 19.4% trails the industry benchmark of 21.2%, costing significant CPO production revenue annually. Group CEO Salmah Ahmad and Group Sustainability Director Ahmad Razali need Copilot to manage the RSPO reinstatement, accelerate EUDR compliance, and build the OER improvement investment case.",
      files: ["11_Zava_Agribusiness_Plantations.xlsx", "22_Zava_Plantation_RSPO_Audit.docx", "Email_10_RSPO_Suspension.docx"],
      prompts: [
        {
          tool: "🤖 Copilot Chat (Basic)",
          license: "Free — no M365 license needed",
          account: "Sasha Ouellet — SashaO@ABSx62256373.OnMicrosoft.com",
          prompts: [
            {
              title: "Explain EUDR and what it means for a Malaysian palm oil company",
              prompt: "Ask Copilot: \"Explain the EU Deforestation Regulation (EUDR) and what it means for a Malaysian palm oil plantation company in practical terms. Perkebunan Lestari Group manages 184,200 hectares and exports palm oil products to the European Union. Cover: (1) What the EUDR requires — due diligence, geolocation, and legal compliance evidence for all supply chain origins; (2) The key EUDR compliance date that affects exports to the EU — now scheduled for January 2026 after the extension — and the consequences of non-compliance; (3) What Malaysian palm oil companies specifically must document — plot-level geolocation data and deforestation-free evidence since December 2020; (4) The 3 most common EUDR compliance gaps for Malaysian plantation companies. Maximum 250 words.\""
            },
            {
              title: "Explain RSPO certification and why 2 suspended mills matter",
              prompt: "Ask Copilot: \"Explain what RSPO (Roundtable on Sustainable Palm Oil) certification means for a palm oil company and why having 2 mills suspended from RSPO certification represents a serious business risk for Perkebunan Lestari Group. Specifically: (1) What RSPO certification requires — the 8 RSPO principles and key criteria most commonly failed; (2) What RSPO suspension means for the supply chain — can the suspended mills' FFB still be processed and sold, and at what price discount; (3) The downstream customer impact — which European and US FMCG companies mandate RSPO-certified supply; (4) The reputational and financial premium difference between RSPO and non-RSPO certified palm oil in export markets. Maximum 250 words.\""
            },
            {
              title: "What is OER and why is 19.4% vs 21.2% significant?",
              prompt: "Ask Copilot: \"Explain Oil Extraction Rate (OER) for a palm oil mill operator. Perkebunan Lestari Group has an OER of 19.4% against a benchmark of 21.2% — a significant underperformance. Explain: (1) What OER is and how it is calculated — tonnes of CPO extracted per tonne of Fresh Fruit Bunches processed; (2) The financial impact of a 1.8 percentage point OER gap for a plantation group processing 4.2 million tonnes of FFB per year — calculate the CPO tonnes lost and MYR revenue impact at the current CPO price; (3) The 5 most common causes of low OER — ripeness distribution, sterilisation efficiency, digester performance, or press conditions; (4) How quickly OER can be recovered through operational adjustments versus capital investment. Maximum 250 words.\""
            }
          ]
        },
        {
          tool: "�� Researcher",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Research EUDR compliance requirements for Malaysian palm oil",
              prompt: "In Copilot Chat, switch to the Researcher agent. Upload 22_Zava_Plantation_RSPO_Audit.docx. Ask: \"Review the RSPO audit report, then search the web for: the current status of the EU Deforestation Regulation implementation and the latest compliance date for palm oil exporters; the specific documentation Malaysian palm oil companies must provide to EU importers under EUDR due diligence obligations; any MSPO and RSPO equivalency rulings under the EUDR — is Malaysian Sustainable Palm Oil certification accepted by the EU; and published EUDR readiness assessments for Malaysian palm oil companies. Cross-reference with Lestari's RSPO suspension situation. What are the 3 most urgent EUDR compliance actions that must be completed before January 2026? Cite all sources.\"",
              fileRef: "22_Zava_Plantation_RSPO_Audit.docx"
            },
            {
              title: "Research RSPO reinstatement process and best practices",
              prompt: "In Copilot Chat, switch to the Researcher agent. Ask: \"Search the web for RSPO certification suspension and reinstatement processes. Find: the formal RSPO corrective action request process and the typical timeline from suspension to reinstatement for a palm oil mill; the most common RSPO certification non-conformances that lead to mill suspension in Malaysia — traceability gaps, peat drainage, no burn policy violations; and case studies of Malaysian plantation companies that successfully reinstated RSPO certification within 6 months. Also search for the current RSPO market premium — the price differential between RSPO and non-RSPO certified CPO in European spot markets. Perkebunan Lestari has 2 mills suspended. What is the priority remediation plan for reinstatement?\""
            },
            {
              title: "Research OER improvement technology for palm oil mills",
              prompt: "In Copilot Chat, switch to the Researcher agent. Upload 11_Zava_Agribusiness_Plantations.xlsx. Ask: \"Review the plantation operational data. Then search the web for: OER improvement technology and operational best practices for palm oil mills — specifically sterilisation cycle optimisation, digester efficiency, and screw press maintenance; digital mill management systems that have demonstrably improved OER at Malaysian and Indonesian plantation mills; and the current CPO and palm kernel price per tonne to monetise the OER improvement opportunity. At Perkebunan Lestari's OER of 19.4% versus the 21.2% benchmark and FFB throughput of 4.2 million tonnes per year, calculate the annual revenue opportunity from closing the OER gap. Format as a mill investment case.\"",
              fileRef: "11_Zava_Agribusiness_Plantations.xlsx"
            }
          ]
        },
        {
          tool: "📊 Analyst",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Analyse plantation performance and OER gap financials",
              prompt: "In Copilot Chat, switch to the Analyst agent. Upload 11_Zava_Agribusiness_Plantations.xlsx. Ask: \"Analyse the full plantation dataset. Calculate: (1) OER by mill — which mill or mills are dragging down the 19.4% group average and what is each mill's individual OER; (2) The CPO revenue loss from the OER gap — 19.4% actual versus 21.2% benchmark — at 4.2 million tonnes FFB throughput and current CPO price per tonne in MYR; (3) The RSPO-certified percentage of total production — what proportion of CPO sold is achieving the RSPO premium and what is the premium in MYR per tonne; (4) Cost per tonne of CPO produced by mill — are the suspended mills also the highest cost mills; (5) EUDR-compliant plot coverage as a percentage of total hectares. Present as a Group CEO plantation KPI dashboard.\"",
              fileRef: "11_Zava_Agribusiness_Plantations.xlsx"
            },
            {
              title: "Model RSPO reinstatement and EUDR compliance ROI",
              prompt: "In Copilot Chat, switch to the Analyst agent. Upload 11_Zava_Agribusiness_Plantations.xlsx. Ask: \"Build 2 investment ROI models. First — RSPO Reinstatement: if reinstating the 2 suspended mills costs MYR 4.2 million in corrective actions and takes 6 months, calculate: the annual revenue recovery from selling at RSPO premium price versus non-certified price; the payback period; and the EUDR compliance benefit of having RSPO as evidence of deforestation-free sourcing. Second — OER Improvement: if mill process optimisation investment of MYR 8.4 million improves average OER from 19.4% to 20.8% within 12 months, calculate: additional CPO tonnes produced per year; additional revenue in MYR millions at current CPO price; payback period. Present as a Board capital allocation paper.\"",
              fileRef: "11_Zava_Agribusiness_Plantations.xlsx"
            },
            {
              title: "Analyse EUDR compliance exposure and documentation gaps",
              prompt: "In Copilot Chat, switch to the Analyst agent. Upload 11_Zava_Agribusiness_Plantations.xlsx. Ask: \"Analyse Perkebunan Lestari's EUDR compliance exposure. Calculate: (1) What percentage of total planted hectares currently have plot-level geolocation data that meets EUDR standards; (2) How many smallholder FFB supplier plots lack EUDR-compliant sourcing documentation — this is typically the highest-risk gap; (3) The total EU-bound CPO and palm oil product volume in tonnes and value in MYR millions that would be blocked from EU export if EUDR compliance is not achieved by January 2026; (4) The cost estimate for geolocation data collection across all plots lacking data. Format as a EUDR Risk and Compliance Investment assessment for the CEO.\"",
              fileRef: "11_Zava_Agribusiness_Plantations.xlsx"
            }
          ]
        },
        {
          tool: "📊 Copilot in Excel",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Instant plantation performance summary",
              prompt: "Open 11_Zava_Agribusiness_Plantations.xlsx. Ask Copilot: \"Give me a plain-English executive summary of this plantation workbook. What is the group OER versus the 21.2% benchmark? How many mills are RSPO-certified versus suspended? What percentage of planted hectares have EUDR-compliant geolocation data? What is the total CPO production in tonnes? Flag any mill with OER below 19% or with RSPO suspension status. Format: 3-sentence overview, then 4 specific flagged concerns with sheet name and row reference.\"",
              fileRef: "11_Zava_Agribusiness_Plantations.xlsx"
            },
            {
              title: "Create OER performance chart by mill",
              prompt: "Open 11_Zava_Agribusiness_Plantations.xlsx. Ask Copilot: \"Create a horizontal bar chart showing OER by mill for all mills in the Perkebunan Lestari Group. Add a vertical reference line at 21.2% labelled Industry Benchmark and another at 19.4% labelled Group Average. Use green bars for mills above 21%, amber for 19-21%, and red for below 19%. Add the OER value on each bar. Title: Perkebunan Lestari — Oil Extraction Rate by Mill FY2024. This chart will be used in the Board Plantation Operations Committee presentation.\"",
              fileRef: "11_Zava_Agribusiness_Plantations.xlsx"
            },
            {
              title: "Add RSPO and EUDR compliance status columns",
              prompt: "Open 11_Zava_Agribusiness_Plantations.xlsx. Navigate to the Mill and Estate Compliance sheet. Ask Copilot: \"Add 2 new status columns to the mill data table. Column 1: RSPO Status — display Certified in green, Suspended in red, or Under Review in amber based on the existing certification data. Column 2: EUDR Readiness — display Ready in green if 95% or more of supplying plots have geolocation data; Partial in amber if 70-95%; Critical in red if below 70%. Tell me how many mills are in Critical EUDR status and how many tonnes of CPO from those mills is destined for EU export.\"",
              fileRef: "11_Zava_Agribusiness_Plantations.xlsx"
            },
            {
              title: "Natural language query — EU export revenue at risk",
              prompt: "Open 11_Zava_Agribusiness_Plantations.xlsx. Ask Copilot: \"Without navigating sheets, answer: (1) What is the total annual CPO and palm oil product export volume to EU-based buyers in tonnes and MYR millions; (2) What percentage of this EU-bound production comes from the 2 RSPO-suspended mills; (3) If both suspended mills are unable to certify by January 2026, what is the annual revenue at risk from EU market exclusion; (4) What is the OER improvement in CPO tonnes that would result from all mills achieving the 21.2% benchmark — and at current CPO price, what is the MYR uplift. Present as a 2-column Q and A table.\"",
              fileRef: "11_Zava_Agribusiness_Plantations.xlsx"
            }
          ]
        },
        {
          tool: "📝 Copilot in Word",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Summarise RSPO audit report into Board brief",
              prompt: "Open 22_Zava_Plantation_RSPO_Audit.docx. Ask Copilot: \"Summarise this RSPO audit report into a 1-page Board brief for Perkebunan Lestari Group. Include: (1) The RSPO audit outcome — which 2 mills were suspended and the exact non-conformances cited; (2) The corrective action requirements and RSPO reinstatement timeline; (3) The financial impact — RSPO premium revenue at risk per year; (4) The EUDR linkage — how RSPO suspension affects January 2026 EU export compliance; (5) 2 Board decisions required. Formal plantation Board memo style. Maximum 400 words.\"",
              fileRef: "22_Zava_Plantation_RSPO_Audit.docx"
            },
            {
              title: "Draft RSPO corrective action plan",
              prompt: "Open a new Word document. Ask Copilot: \"Draft a formal RSPO Corrective Action Plan for Perkebunan Lestari Group to submit to RSPO following the suspension of 2 certified mills. The plan must: (1) Acknowledge the specific non-conformances cited by the RSPO auditor for each suspended mill; (2) For each non-conformance, state: root cause, corrective action, responsible officer, completion date, and evidence to be submitted; (3) Commit to a reinstatement audit by RSPO within 5 months; (4) Describe the governance oversight — monthly RSPO Compliance Committee chaired by the Group CEO; (5) Provide evidence that the no-burn policy is being rigorously enforced across all 18 mills. Formal RSPO submission format. 500 words.\""
            },
            {
              title: "Rewrite RSPO traceability procedures for estate supervisors",
              prompt: "Open 22_Zava_Plantation_RSPO_Audit.docx. Locate the Traceability and Supply Chain section. Ask Copilot: \"Rewrite this RSPO traceability requirements section in plain, operational language for an estate supervisor or field manager with no RSPO audit background. Replace all RSPO certification codes with plain-language descriptions of what the supervisor must actually do: what to record, when, how, and where. Add a simple daily checklist — the 5 things a supervisor must document every day to maintain RSPO traceability compliance. Maximum 350 words. Written in Bahasa Melayu tone but in English.\"",
              fileRef: "22_Zava_Plantation_RSPO_Audit.docx"
            },
            {
              title: "Draft EUDR customer assurance letter to EU buyers",
              prompt: "Open a new Word document. Ask Copilot: \"Draft a formal EUDR Customer Assurance Letter from Perkebunan Lestari Group CEO to all EU-based palm oil product buyers. The letter should: (1) Confirm Perkebunan Lestari's commitment to EUDR compliance and the January 2026 timeline; (2) Describe the 3 compliance measures underway: plot-level geolocation data collection across all 184,200 hectares, RSPO traceability system upgrade, and smallholder supplier EUDR documentation programme; (3) Confirm that 94% of production areas are already geolocation-mapped and EUDR-ready; (4) Offer a direct EUDR compliance portal login for each EU buyer to access live supply chain documentation; (5) Invite buyers to a EUDR Compliance Day at the head office on 1 September 2025. Formal trade correspondence. 400 words.\""
            }
          ]
        },
        {
          tool: "🎯 Copilot in PowerPoint",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Create RSPO reinstatement and EUDR compliance Board deck",
              prompt: "Open a new PowerPoint. Ask Copilot: \"Create a 7-slide Board presentation for Perkebunan Lestari Group covering RSPO reinstatement and EUDR compliance. Slide 1: Perkebunan Lestari — Sustainability Compliance Update FY2024. Slide 2: RSPO Situation — 2 mills suspended, financial impact, reinstatement timeline. Slide 3: RSPO Corrective Action Plan — non-conformances, actions, timeline. Slide 4: EUDR Readiness — plot coverage %, gap analysis, January 2026 deadline. Slide 5: EUDR Compliance Programme — 3 workstreams with milestones. Slide 6: OER Improvement Plan — mill optimisation investment case. Slide 7: Board Decisions Required. Palm oil industry green and gold theme. Clean, formal.\""
            },
            {
              title: "Generate sustainability investor pitch for palm oil portfolio",
              prompt: "Open a new PowerPoint. Ask Copilot: \"Create a 5-slide sustainability investor pitch for Perkebunan Lestari Group targeting European institutional investors who require EUDR and RSPO compliance from palm oil suppliers. Slide 1: Perkebunan Lestari — Responsible Palm Oil from Malaysia. Slide 2: Our Sustainability Credentials — RSPO scope, EUDR readiness, MSPO certification. Slide 3: Net Zero Pathway — peat drainage cessation, no-burn, biodiversity corridors. Slide 4: EUDR Compliance Programme — geolocation coverage, smallholder inclusion, traceability system. Slide 5: Why Buy from Perkebunan Lestari — certified, traceable, cost-competitive. Sustainably designed slides in green and earth tones.\""
            },
            {
              title: "Add OER and sustainability benchmarking slide",
              prompt: "In an open Perkebunan Lestari PowerPoint, add a new slide. Ask Copilot: \"Create a sustainability and operational benchmarking slide comparing Perkebunan Lestari against 3 leading Malaysian plantation companies: IOI Group, Sime Darby Plantation, and FGV Holdings. Compare 3 metrics: OER %, RSPO-certified production percentage, and carbon intensity per tonne of CPO. Use a clustered bar chart with Lestari highlighted. Add a callout showing the OER improvement opportunity and the revenue impact of closing the gap to the benchmark. Title: Perkebunan Lestari — Sustainability and OER Performance vs Malaysian Palm Oil Peers.\""
            }
          ]
        },
        {
          tool: "📧 Copilot in Outlook",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Triage urgent RSPO suspension notification email",
              prompt: "Open Outlook and locate Email_10_RSPO_Suspension.docx. Copy into a draft or open the email. Ask Copilot: \"I am Perkebunan Lestari's Group Sustainability Director and I have just received this RSPO suspension notification. Summarise: (1) Which specific mills are suspended and what are the exact non-conformances cited; (2) What is the RSPO's required response deadline and what must I submit; (3) Is there a trading restriction on the suspended mills' CPO during the suspension period; (4) My 3 most urgent internal actions in the next 48 hours. Maximum 200 words.\"",
              fileRef: "Email_10_RSPO_Suspension.docx"
            },
            {
              title: "Draft CEO message to all estate managers on RSPO and EUDR compliance",
              prompt: "Open a new Outlook email. Ask Copilot: \"Draft a formal message from the Perkebunan Lestari Group CEO to all 28 estate managers regarding the critical importance of RSPO and EUDR compliance in FY2025. The message should: (1) State the business stakes clearly — RSPO suspension of 2 mills and EUDR deadline in January 2026 put our EU export revenue at risk; (2) Assign 3 specific responsibilities to every estate manager: complete plot geolocation data for all assigned plots by 30 September 2025, ensure all smallholder suppliers have signed EUDR declarations, and maintain daily FFB traceability logs without exception; (3) Announce monthly estate compliance audits by the Group Sustainability team; (4) Commit to support — a dedicated compliance officer will visit each estate within 6 weeks. Direct, serious. 300 words.\""
            },
            {
              title: "Copilot coaching on response to EU buyer requesting EUDR compliance evidence",
              prompt: "In Outlook, type a rough draft to a European palm oil buyer: \"Dear customer, we are working on EUDR compliance and will provide documents when ready. Our team is handling it. Please be patient.\" Ask Copilot for coaching: \"I am the Head of Export Sales at a Malaysian palm oil company writing to a European trader requiring EUDR compliance documentation. Evaluate on: (1) Credibility — does the response inspire confidence in our compliance readiness; (2) Specificity — does it commit to a specific documentation delivery date; (3) Commercial risk awareness — does it address the buyer's supply security concern. Rewrite at a credible export commercial standard with specific timeline and a portal login offer.\""
            }
          ]
        },
        {
          tool: "🎙 Copilot in Teams",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Catch up on missed RSPO compliance emergency meeting",
              prompt: "Open an existing Teams meeting that was recorded and has a Copilot recap from your calendar. Ask: \"I am the Perkebunan Lestari Group CEO and I missed this emergency RSPO compliance meeting. Catch me up: (1) Which mills were confirmed as suspended and what are the specific audit findings; (2) What corrective action commitments were made and by whom; (3) Was there a decision on trading the suspended mills' CPO during the suspension period; (4) Any actions specifically requiring my sign-off as CEO; (5) Was the EUDR impact of the suspension discussed — what was the conclusion on EU export revenue at risk.\""
            },
            {
              title: "Extract estate compliance actions from the sustainability review",
              prompt: "Open an existing recorded Teams meeting from your calendar. Ask: \"Extract all estate and mill compliance action items from this sustainability management review. Format as a Compliance Action Register: Estate or Mill Name; Compliance Area (RSPO, EUDR, Environmental, Labour); Specific Action; Officer Responsible; Deadline; Non-conformance Reference if applicable; Priority — Critical for RSPO reinstatement or EUDR deadline actions, High for environmental incidents. Group by compliance area. Highlight in red any action with a deadline within the next 30 days.\""
            },
            {
              title: "Draft estate operations weekly update email from sustainability review",
              prompt: "Open an existing recorded Teams meeting recap from your calendar. Ask: \"Draft a weekly sustainability operations update email from the Perkebunan Lestari Group Sustainability Director to all 28 estate managers and 18 mill managers. Based on this meeting: (1) RSPO reinstatement progress update — corrective actions completion status; (2) EUDR geolocation data collection progress across all estates — percentage complete; (3) This week's priority compliance actions for each estate; (4) Any enforcement or audit events upcoming. Direct, compliance-focused. Under 300 words.\""
            }
          ]
        },
        {
          tool: "📓 Copilot Notebook",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Full sustainability compliance brief from 3 documents",
              prompt: "Go to Copilot Notebook. Upload 11_Zava_Agribusiness_Plantations.xlsx, 22_Zava_Plantation_RSPO_Audit.docx, and Email_10_RSPO_Suspension.docx. In Instructions: \"Using all 3 documents, prepare a comprehensive sustainability compliance brief for the Perkebunan Lestari Group CEO. (1) From the RSPO suspension email — what exactly has RSPO required and by when; (2) From the RSPO audit report — what are the specific non-conformances and the reinstatement process; (3) From the plantation financial data — quantify the EU revenue at risk from both the RSPO suspension and EUDR non-compliance; (4) Identify any gap between the RSPO audit findings and the operational data; (5) Build a 5-point CEO immediate action agenda for the first week. Format as a CEO crisis brief.\"",
              fileRef: "11_Zava_Agribusiness_Plantations.xlsx, 22_Zava_Plantation_RSPO_Audit.docx, Email_10_RSPO_Suspension.docx"
            },
            {
              title: "EUDR and RSPO combined compliance pathway analysis",
              prompt: "Go to Copilot Notebook. Upload 11_Zava_Agribusiness_Plantations.xlsx and 22_Zava_Plantation_RSPO_Audit.docx. In Instructions: \"Using both documents, build a combined RSPO and EUDR compliance pathway analysis for the Board. (1) What is the current RSPO certification status across all 18 mills and what % of production is RSPO-certified; (2) What is the current EUDR geolocation data coverage and the gap to 100% compliance by January 2026; (3) Are the 2 RSPO-suspended mills also the highest EUDR-risk mills — if so, the combined compliance risk is concentrated; (4) What is the total investment needed to achieve both RSPO reinstatement and EUDR compliance; (5) Build a risk matrix showing probability and financial impact of 3 scenarios: Full Compliance, Partial Compliance, and Non-Compliance.\"",
              fileRef: "11_Zava_Agribusiness_Plantations.xlsx, 22_Zava_Plantation_RSPO_Audit.docx"
            }
          ]
        },
        {
          tool: "🤝 Cowork (Pages)",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Build RSPO and EUDR compliance tracker in Pages",
              prompt: "In Copilot Chat, upload 11_Zava_Agribusiness_Plantations.xlsx and ask for a sustainability compliance status. Click Open in Copilot Pages. Ask: \"Reorganise this into a collaborative RSPO and EUDR Compliance Tracker for the Perkebunan Lestari Sustainability team of 8 specialists. Structure as: (1) RSPO Status Dashboard — 18 mills with certification status; (2) RSPO Corrective Action Tracker — suspended mills with actions and deadlines; (3) EUDR Geolocation Coverage Map — estate-level completion percentage; (4) Smallholder Supplier Declaration Tracker; (5) Compliance Incident Log. Format for daily collaborative updates by estate and mill compliance officers.\"",
              fileRef: "11_Zava_Agribusiness_Plantations.xlsx"
            },
            {
              title: "Build OER improvement programme canvas",
              prompt: "In Copilot Chat, upload 11_Zava_Agribusiness_Plantations.xlsx and ask for an OER performance analysis. Click Open in Copilot Pages. Ask: \"Expand this into a collaborative OER Improvement Programme Canvas for the Perkebunan Lestari Mill Operations team. Structure as: (1) OER Performance Dashboard — all 18 mills with current OER vs 21.2% target; (2) Mill Optimisation Action Tracker — specific technical interventions per mill with engineer owner; (3) Investment Approval Log — capital items requiring Board or management approval; (4) Weekly OER Log — each mill reports weekly; (5) Best Practice Sharing — top-performing mills share their operating parameters. Format for simultaneous editing by all 18 mill managers.\"",
              fileRef: "11_Zava_Agribusiness_Plantations.xlsx"
            }
          ]
        },
        {
          tool: "🤖 Word Agent",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Set up an RSPO Compliance Advisor on the audit report",
              prompt: "Open 22_Zava_Plantation_RSPO_Audit.docx in Word. Create an agent named RSPO Compliance Advisor. Instructions: \"Answer questions about Perkebunan Lestari's RSPO audit findings and corrective actions. Cite audit sections. Under 150 words.\" Demo: type \"What are the specific non-conformances cited for the 2 suspended mills and what corrective actions are required for each?\"",
              fileRef: "22_Zava_Plantation_RSPO_Audit.docx"
            },
            {
              title: "Demo the RSPO Advisor — audit and EUDR queries",
              prompt: "With the agent active, ask 3 queries. Query 1: \"What is the RSPO reinstatement timeline and what evidence must be submitted to RSPO to achieve reinstatement?\" Query 2: \"Which RSPO principle or criteria did the suspended mills fail most severely and what operational changes are required?\" Query 3: \"How does the RSPO audit report address the EUDR compliance requirement — is RSPO traceability documentation sufficient for EUDR due diligence?\"",
              fileRef: "22_Zava_Plantation_RSPO_Audit.docx"
            }
          ]
        },
        {
          tool: "🤖 PowerPoint Agent",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Set up a Sustainability Compliance Presenter agent",
              prompt: "Create or open the RSPO and EUDR compliance PowerPoint from the PPT demo. Save as Lestari_Sustainability_Compliance_2025.pptx. Create an agent named Lestari Sustainability Coach. Instructions: \"Answer questions about Perkebunan Lestari's sustainability compliance presentation. Reference slide numbers. Under 100 words.\" Demo: type \"Which slide shows the RSPO reinstatement timeline for the 2 suspended mills and what is the completion date?\""
            },
            {
              title: "Demo the Sustainability Coach — Board queries",
              prompt: "With the agent active, run 3 queries. Query 1: \"What is the total EU export revenue at risk if EUDR compliance is not achieved by January 2026 — which slide has this calculation?\" Query 2: \"What Board decisions are needed immediately to fund the RSPO corrective actions and EUDR compliance programme?\" Query 3: \"Which slide shows the OER improvement investment case and what is the expected annual revenue uplift from closing the OER gap?\""
            }
          ]
        },
        {
          tool: "🤖 Excel Agent",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Set up a Plantation Performance Agent",
              prompt: "Open 11_Zava_Agribusiness_Plantations.xlsx. Create an agent named Lestari Plantation Advisor. Instructions: \"Answer questions about Perkebunan Lestari plantation performance, OER, and compliance data. Cite sheet names. Express CPO volumes in tonnes and revenue in MYR millions.\" Demo: type \"What is the group average OER for FY2024 and which mill has the lowest individual OER?\"",
              fileRef: "11_Zava_Agribusiness_Plantations.xlsx"
            },
            {
              title: "Demo the Plantation Advisor — operations queries",
              prompt: "With the agent active, run 3 queries. Query 1: \"What is the total CPO production in tonnes for FY2024 and what would production be at the 21.2% OER benchmark — how many additional tonnes is the gap?\" Query 2: \"How many mills are currently RSPO-certified and producing at RSPO premium versus the 2 suspended mills — what is the percentage of total production at premium pricing?\" Query 3: \"What percentage of total planted hectares currently have EUDR-compliant geolocation data and how many hectares remain without documentation?\"",
              fileRef: "11_Zava_Agribusiness_Plantations.xlsx"
            }
          ]
        }
      ]
    },
    {
      id: "manufacturing",
      name: "Manufacturing & Industrial",
      icon: "🏭",
      color: "#2C3E50",
      accent: "#7F8C8D",
      company: "Zava Manufacturing Sdn Bhd",
      tagline: "OEE 76%→62% | Spindle failure CNC Line 3 | SIRIM audit 8 weeks | Backlog 2,800 units MYR 14.2M",
      scenario: "Zava Manufacturing Sdn Bhd (Zava Manufacturing) is a Malaysian precision components manufacturer supplying aerospace and automotive customers from its Shah Alam plant. The company employs 480 engineers, technicians, and operators across 3 shifts. A spindle motor failure on CNC Line 3 in Q3 FY2024 triggered a cascading OEE decline from 76% to 62%, creating a production backlog of 2,800 units worth MYR 14.2 million and risking delivery penalty clauses in aerospace customer contracts. A SIRIM AS9100D aerospace quality management audit is scheduled in 8 weeks. Plant General Manager Siti Nur Aisyah and VP Operations Ahmad Fadzillah need Copilot to manage the backlog recovery, prepare for the SIRIM audit, build the predictive maintenance investment case, and communicate credibly with aerospace and automotive customers.",
      files: ["12_Zava_Manufacturing_KPIs.xlsx", "Email_01_Production_Emergency.docx", "21_Zava_Chemical_Safety_HIRARC.docx"],
      prompts: [
        {
          tool: "🤖 Copilot Chat (Basic)",
          license: "Free — no M365 license needed",
          account: "Sasha Ouellet — SashaO@ABSx62256373.OnMicrosoft.com",
          prompts: [
            {
              title: "Explain OEE decline and what spindle motor failure means for a plant",
              prompt: "Ask Copilot: \"Explain Overall Equipment Effectiveness (OEE) and what a decline from 76% to 62% means for Zava Manufacturing's precision components plant. Also explain what a spindle motor failure on a CNC machining line means operationally. Cover: (1) The OEE formula — Availability × Performance × Quality — and what each factor represents; (2) The financial impact of a 14 percentage point OEE decline: if the plant produces precision components at MYR 84,000 per day at full OEE, what is the daily revenue loss at 62% OEE; (3) What a spindle motor failure on a multi-spindle CNC means for line availability: estimated downtime, repair cost, and lead time for a replacement spindle motor from Germany or Japan; (4) Why the 2,800-unit backlog worth MYR 14.2 million is accumulating. Maximum 250 words.\""
            },
            {
              title: "Brief me on the SIRIM audit and what it means for our ISO certification",
              prompt: "Ask Copilot: \"I am the Plant General Manager of Zava Manufacturing, a precision aerospace and automotive components manufacturer in Malaysia. SIRIM has scheduled an ISO 9001:2015 and AS9100D (aerospace quality) audit in 8 weeks. Brief me on: (1) What SIRIM QAS International audits for in an AS9100D aerospace quality management system audit — the top 5 most commonly cited non-conformances; (2) What happens to our ISO and AS9100D certification if SIRIM finds major non-conformances — can customers cancel contracts immediately; (3) The 3 most important documentation and operational preparations we should complete in 8 weeks; (4) What the OEE decline from 76% to 62% and the 2,800-unit backlog implies for SIRIM's Production Monitoring assessment. Maximum 250 words.\""
            },
            {
              title: "What is a customer delivery backlog and how does MYR 14.2M compare?",
              prompt: "Ask Copilot: \"Explain what a production backlog means for a B2B precision components manufacturer and put the MYR 14.2 million backlog at Zava Manufacturing in context. Cover: (1) How a production backlog is calculated — units outstanding multiplied by unit selling price — and what the 2,800-unit backlog implies about Zava Manufacturing's weekly production output gap; (2) The commercial consequences of a growing backlog for a tier-1 aerospace or automotive component supplier: contractual delivery penalties, customer demand allocation changes, and relationship risk; (3) At MYR 14.2 million in delayed revenue, what is the working capital impact for Zava Manufacturing; (4) The threshold at which automotive OEM customers typically trigger supply alternative sourcing. Maximum 250 words.\""
            }
          ]
        },
        {
          tool: "�� Researcher",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Research CNC spindle motor failure root causes and repair options",
              prompt: "In Copilot Chat, switch to the Researcher agent. Upload 12_Zava_Manufacturing_KPIs.xlsx. Ask: \"Review Zava Manufacturing's equipment performance data. Then search the web for: CNC multi-spindle motor failure root causes and preventive maintenance best practices from Okuma, Mazak, and Yamazaki; spindle motor replacement lead times from German and Japanese manufacturers — how long does a new spindle motor take to deliver to Malaysia; contract maintenance and spindle motor rebinding services in Malaysia and Singapore that can reduce downtime; and Industry 4.0 predictive maintenance solutions that detect spindle deterioration before failure. Given the current OEE of 62% with the spindle failure as the primary cause, what is the fastest route to recovering OEE to above 70%? Cite all sources.\"",
              fileRef: "12_Zava_Manufacturing_KPIs.xlsx"
            },
            {
              title: "Research AS9100D audit preparation best practices",
              prompt: "In Copilot Chat, switch to the Researcher agent. Ask: \"Search the web for AS9100D aerospace quality management system audit preparation best practices. Find: the top 10 AS9100D non-conformances cited by IAQG and SIRIM auditors at Malaysian and ASEAN aerospace component manufacturers; how to prepare traceability documentation and first article inspection records for an AS9100D audit; the specific differences between AS9100D and ISO 9001:2015 audit requirements that catch manufacturers off-guard; and any SIRIM QAS International audit notices or guidance for Malaysian aerospace suppliers. Zava Manufacturing has 8 weeks to prepare. What are the 5 most critical preparation priorities that will protect the AS9100D certification status?\""
            },
            {
              title: "Research Industry 4.0 and predictive maintenance for precision manufacturing",
              prompt: "In Copilot Chat, switch to the Researcher agent. Upload 12_Zava_Manufacturing_KPIs.xlsx. Ask: \"Review the manufacturing KPI data. Then search the web for: Industry 4.0 and IIoT predictive maintenance platforms deployed at Malaysian and ASEAN precision manufacturers — Siemens MindSphere, Bosch Nexeed, and local Malaysian platforms; OEE improvement results from Industry 4.0 deployments in automotive and aerospace component manufacturing; MIDA and MDEC grants available for Malaysian manufacturers investing in smart factory technology in 2024-2025; and total productive maintenance (TPM) programmes that have recovered OEE from 60-65% to above 75% within 12 months. What is the investment and payback timeline for a predictive maintenance platform at Zava's scale? Cite sources.\"",
              fileRef: "12_Zava_Manufacturing_KPIs.xlsx"
            }
          ]
        },
        {
          tool: "📊 Analyst",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Analyse Zava Manufacturing OEE and production KPIs",
              prompt: "In Copilot Chat, switch to the Analyst agent. Upload 12_Zava_Manufacturing_KPIs.xlsx. Ask: \"Analyse the full manufacturing dataset. Calculate: (1) OEE trend by quarter from Q1 FY2023 to Q4 FY2024 — confirm the decline from 76% to 62% and identify which quarter had the steepest drop; (2) The OEE components breakdown — what percentage of the decline is explained by Availability loss versus Performance loss versus Quality loss; (3) The daily revenue impact at 62% OEE versus 76% OEE at MYR 84,000 revenue per day at full OEE — and the cumulative lost revenue in FY2024; (4) The backlog accumulation rate — how many units per week are being added to the 2,800-unit backlog; (5) Machine-specific downtime by CNC line — which lines are contributing most to availability loss. Present as a Plant General Manager OEE recovery dashboard.\"",
              fileRef: "12_Zava_Manufacturing_KPIs.xlsx"
            },
            {
              title: "Model backlog clearance and OEE recovery scenarios",
              prompt: "In Copilot Chat, switch to the Analyst agent. Upload 12_Zava_Manufacturing_KPIs.xlsx. Ask: \"Build a backlog clearance model for Zava Manufacturing. From the data: (1) At current 62% OEE, how many weeks will it take to clear the 2,800-unit backlog assuming the order pipeline is maintained at current rate; (2) If OEE recovers to 72% through spindle motor repair and line optimisation, how does the clearance timeline improve; (3) If overtime production is added — 2 additional shifts per week — combined with OEE recovery to 72%, when will the backlog reach zero; (4) What is the delivery penalty liability if the backlog is not cleared within 90 days assuming a 1.5% penalty per week in customer contracts; (5) The revenue recovery timeline. Format as a crisis operations plan with a Go or No-Go decision matrix.\"",
              fileRef: "12_Zava_Manufacturing_KPIs.xlsx"
            },
            {
              title: "Analyse SIRIM audit risk and quality KPI performance",
              prompt: "In Copilot Chat, switch to the Analyst agent. Upload 12_Zava_Manufacturing_KPIs.xlsx. Ask: \"Analyse the quality and compliance KPI data in context of the upcoming SIRIM AS9100D audit. Calculate: (1) First pass yield trend from Q1 FY2023 to Q4 FY2024 — is quality declining alongside OEE; (2) Customer complaint and non-conformance report rate per 1,000 units — is it trending above the AS9100D target; (3) Preventive maintenance completion rate — what percentage of scheduled PM was completed on time in FY2024; (4) Calibration records currency — what percentage of measuring instruments are within their calibration due date; (5) Which of the 8 AS9100D critical process areas has the weakest data evidence. Present as a SIRIM Audit Risk Assessment.\"",
              fileRef: "12_Zava_Manufacturing_KPIs.xlsx"
            }
          ]
        },
        {
          tool: "📊 Copilot in Excel",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Instant manufacturing KPI summary for GM review",
              prompt: "Open 12_Zava_Manufacturing_KPIs.xlsx. Ask Copilot: \"Give me a plain-English executive summary of this manufacturing workbook. What is the current OEE and how does it compare to the 76% baseline? What is the backlog in units and MYR value? What is the spindle motor downtime? Which production line has the worst availability? Flag any metric that is more than 10 percentage points below target or trending downward for 3 consecutive months. Format: 3-sentence overview, then 4 specific flagged concerns with sheet name and row reference.\"",
              fileRef: "12_Zava_Manufacturing_KPIs.xlsx"
            },
            {
              title: "Create OEE waterfall breakdown chart",
              prompt: "Open 12_Zava_Manufacturing_KPIs.xlsx. Navigate to the OEE Analysis sheet. Ask Copilot: \"Create a waterfall chart showing the OEE breakdown from the 76% baseline target down to the current 62% actual. Show the contributions of each loss type: Planned Downtime, Unplanned Downtime (including the spindle motor failure), Minor Stops and Speed Loss, and Quality Defects. Use red bars for each loss component and green for the residual OEE. Add data labels showing the percentage point loss for each component. Title: Zava Manufacturing — OEE Waterfall FY2024 — 76% Target vs 62% Actual. For the Board Operations and Capital Committee.\"",
              fileRef: "12_Zava_Manufacturing_KPIs.xlsx"
            },
            {
              title: "Add backlog clearance projection formula",
              prompt: "Open 12_Zava_Manufacturing_KPIs.xlsx. Navigate to the Production Backlog sheet. Ask Copilot: \"Add a Projected Clearance Date column that calculates how many weeks it will take to clear the current unit backlog for each customer order, given: (1) The current weekly production rate for that part number at 62% OEE, (2) The customer's weekly demand rate. If the backlog will not clear within 12 weeks, highlight the cell in red. If 8 to 12 weeks, amber. If under 8 weeks, green. Also calculate the total penalty exposure in MYR assuming 1.5% per week delay fee on the contract value of each delayed order.\"",
              fileRef: "12_Zava_Manufacturing_KPIs.xlsx"
            },
            {
              title: "Natural language query — SIRIM audit risk indicators",
              prompt: "Open 12_Zava_Manufacturing_KPIs.xlsx. Ask Copilot: \"Without navigating sheets, answer: (1) What is the current first-pass yield rate and is it above or below the AS9100D minimum acceptable quality level; (2) How many preventive maintenance work orders were overdue at end of FY2024 — as both count and percentage of total PM schedule; (3) What is the calibration compliance rate — percentage of instruments in calibration; (4) What is the customer nonconformance report rate per 1,000 units shipped for FY2024 and how does it compare to the FY2023 baseline. Present as a 2-column SIRIM Audit Risk Q and A.\"",
              fileRef: "12_Zava_Manufacturing_KPIs.xlsx"
            }
          ]
        },
        {
          tool: "📝 Copilot in Word",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Draft SIRIM AS9100D audit preparation brief for all department heads",
              prompt: "Open a new Word document. Ask Copilot: \"Draft a formal audit preparation brief from the Zava Manufacturing Plant General Manager to all 8 department heads (Production, Quality, Maintenance, Supply Chain, HR, Finance, Health and Safety, and IT). The brief addresses the SIRIM AS9100D and ISO 9001:2015 audit in 8 weeks. Include: (1) Audit scope and what SIRIM auditors will assess in each department; (2) Top 3 documentation requirements each department must prepare — calibration records, PM completion logs, or training competency matrices as applicable; (3) Internal mock audit schedule — 4 weeks before SIRIM visit; (4) Consequences of major non-conformances — certification suspension risk and customer contract impact; (5) Contact: Quality Manager as the audit coordination lead. Formal plant management memo. 500 words.\""
            },
            {
              title: "Draft customer communication about delivery backlog",
              prompt: "Open a new Word document. Ask Copilot: \"Draft a formal customer communication letter from Zava Manufacturing's Vice President Operations to all affected customers regarding the current delivery backlog of 2,800 units and MYR 14.2 million in delayed orders. The letter must: (1) Acknowledge the delivery shortfall directly and honestly; (2) Explain the root cause — spindle motor failure on CNC Line 3 causing 38% availability loss — and the repair status: new spindle ordered, delivery in 18 days from Germany; (3) Provide revised delivery schedule for each customer's affected orders; (4) Confirm the overtime and capacity augmentation plan to clear the backlog within 90 days; (5) Commit to a weekly delivery update call with each account. Professional B2B customer communication. 400 words.\""
            },
            {
              title: "Rewrite the AS9100D non-conformance procedure for shop floor staff",
              prompt: "Open 21_Zava_Chemical_Safety_HIRARC.docx to use as a reference format, then open a new document. Ask Copilot: \"Draft a plain-language Non-Conforming Product and Corrective Action Procedure for Zava Manufacturing shop floor operators and quality inspectors. Replace all AS9100D references with plain step-by-step instructions. Include: (1) How to identify and tag a non-conforming part in 3 steps; (2) What to write on the Non-Conformance Report form — 5 fields only; (3) Who to call immediately if a non-conformance involves a safety-critical aerospace component; (4) How an operator requests a corrective action and tracks its completion. Maximum 350 words. Practical and visual — use numbered steps and a checkbox format.\""
            },
            {
              title: "Draft predictive maintenance technology investment proposal",
              prompt: "Open a new Word document. Ask Copilot: \"Draft a formal capital investment proposal from Zava Manufacturing's Head of Maintenance to Plant General Manager for a predictive maintenance IIoT system. The proposal covers: (1) Problem: OEE declined from 76% to 62% due to unplanned failures including the spindle motor incident — cost of unplanned downtime in FY2024 in MYR; (2) Proposed solution: vibration and thermal sensor network on all 12 CNC lines, connected to a cloud-based predictive maintenance platform with 48-hour failure prediction; (3) Investment: MYR 1.84 million hardware and software, MYR 180,000 annual platform licence; (4) Financial case: expected unplanned downtime reduction of 65%, OEE recovery to 74%, payback period; (5) SIRIM benefit: PM record completeness supports AS9100D compliance. Formal capex proposal. 500 words.\""
            }
          ]
        },
        {
          tool: "🎯 Copilot in PowerPoint",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Create operations recovery Board presentation",
              prompt: "Open a new PowerPoint. Ask Copilot: \"Create a 7-slide operations recovery presentation for Zava Manufacturing's Board Operations and Capital Committee. Slide 1: Zava Manufacturing — Operations Recovery Plan FY2025. Slide 2: OEE Crisis — 76% to 62% decline, root causes, financial impact. Slide 3: Spindle Motor Recovery — repair timeline, CNC Line 3 restoration, OEE trajectory. Slide 4: Backlog Clearance Plan — 2,800 units, MYR 14.2M, weekly milestone chart. Slide 5: SIRIM AS9100D Audit Readiness — 8-week sprint plan, traffic light by department. Slide 6: Predictive Maintenance Investment — MYR 1.84M, OEE recovery to 74%, payback. Slide 7: Board Decisions Required — 2 approvals. Industrial blue and grey theme, professional.\""
            },
            {
              title: "Generate Industry 4.0 transformation strategy deck",
              prompt: "Open a new PowerPoint. Ask Copilot: \"Create a 5-slide Industry 4.0 transformation strategy presentation for Zava Manufacturing targeting the Group CEO and digital transformation committee. Slide 1: Zava Manufacturing — Smart Factory Roadmap 2025-2028. Slide 2: The Problem — OEE 62%, reactive maintenance culture, paper-based quality records. Slide 3: Our Industry 4.0 Vision — predictive maintenance, digital quality management, connected CNC analytics. Slide 4: Implementation Roadmap — Phase 1 sensors and connectivity (MYR 1.84M), Phase 2 AI analytics platform, Phase 3 full digital twin; Slide 5: ROI — OEE 74%, backlog elimination, SIRIM compliance benefit, payback period. Modern industrial smart factory design.\""
            },
            {
              title: "Add manufacturing OEE benchmarking slide",
              prompt: "In an open Zava Manufacturing PowerPoint, add a new slide. Ask Copilot: \"Create an OEE benchmarking slide comparing Zava Manufacturing's current 62% OEE against 3 benchmarks: Zava FY2023 baseline at 76%, Malaysian precision manufacturing industry average at 71%, and World-class OEE standard at 85%. Use a horizontal bar chart with Zava current in red, Zava FY2023 in amber, industry average in blue, and world-class in green. Add a callout showing the MYR revenue recovery opportunity from closing the gap to 75%. Title: Zava Manufacturing — OEE Benchmarking FY2024 vs Industry.\""
            }
          ]
        },
        {
          tool: "📧 Copilot in Outlook",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Triage the production emergency email from the plant manager",
              prompt: "Open Outlook and locate Email_01_Production_Emergency.docx. Copy into a draft or open the email. Ask Copilot: \"I am the Zava Manufacturing VP Operations and I have received this emergency production email. Summarise: (1) What is the production emergency — specific machine, line, or event; (2) How many units are affected and what is the revenue at risk; (3) What has already been done and what is the next action pending; (4) What I need to escalate to the Group CEO and Board within the next 2 hours. Maximum 200 words.\"",
              fileRef: "Email_01_Production_Emergency.docx"
            },
            {
              title: "Draft customer-facing backlog update email",
              prompt: "Open a new Outlook email. Ask Copilot: \"Draft a professional customer service email from the Zava Manufacturing Account Manager to a top aerospace customer — a Malaysian subsidiary of an Airbus Tier-1 supplier — providing an update on their 480-unit delivery backlog. The email should: (1) Acknowledge the delay and specify the revised delivery schedule by week; (2) Explain the root cause — CNC Line 3 spindle motor failure and the repair timeline; (3) Confirm the expedited processing of their order once Line 3 is restored; (4) Offer a 20% delivery credit for the delay as a goodwill gesture pending management approval; (5) Provide direct contact for the Customer Service Director for daily updates. Professional, honest, B2B aerospace tone. 300 words.\""
            },
            {
              title: "Copilot coaching on response to SIRIM pre-audit query",
              prompt: "In Outlook, type a rough draft to SIRIM: \"Dear SIRIM team, we are preparing for the audit and will have the documents ready. Our quality team is handling it. We look forward to your visit.\" Ask Copilot for coaching: \"I am a Quality Director at a Malaysian aerospace component manufacturer writing to the SIRIM QAS audit team. Evaluate on: (1) Confidence and credibility — does it demonstrate organised audit readiness; (2) Specificity — does it confirm which document categories will be ready; (3) Regulatory tone — is it appropriately formal. Rewrite at a certified manufacturer standard that lists the 4 documentation packages being prepared and invites a pre-audit document review.\""
            }
          ]
        },
        {
          tool: "🎙 Copilot in Teams",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Catch up on the emergency production crisis response meeting",
              prompt: "Open an existing Teams meeting that was recorded and has a Copilot recap from your calendar. Ask: \"I am the Zava Manufacturing Plant General Manager and I was on the production floor during this meeting. Catch me up: (1) What production crisis was being managed — CNC failure, backlog escalation, or customer complaint; (2) What recovery actions were committed and by whom; (3) Was Board or Group CEO escalation discussed — if so, what was decided; (4) Actions specifically requiring my sign-off as Plant GM; (5) Was the SIRIM audit preparation discussed in the context of the OEE decline.\""
            },
            {
              title: "Extract operations and quality actions from the weekly review",
              prompt: "Open an existing recorded Teams meeting from your calendar. Ask: \"Extract all manufacturing operations and quality action items from this review. Format as: Machine or Process; Action Type (Maintenance, Quality, Customer, SIRIM Prep); Specific Action; Engineer or Supervisor Owner; Deadline; Priority — Critical for SIRIM audit actions or customer contract delivery deadlines, High for OEE recovery, Normal for routine. Also note: was a specific OEE recovery target and timeline confirmed at this meeting — if so, state it.\""
            },
            {
              title: "Draft production team daily update from operations review",
              prompt: "Open an existing recorded Teams meeting recap from your calendar. Ask: \"Draft a daily production floor update bulletin from the Zava Manufacturing Production Manager to all shift supervisors, CNC operators, and quality inspectors. Based on this meeting: (1) OEE for the previous day — actual vs 70% recovery target; (2) CNC Line 3 spindle repair status; (3) Backlog clearance progress — units cleared this week vs target; (4) Quality alert if any batch non-conformances were raised; (5) Tonight's shift priorities. Practical, direct, no-nonsense production floor communication. Under 200 words.\""
            }
          ]
        },
        {
          tool: "📓 Copilot Notebook",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Full manufacturing crisis brief from 3 documents",
              prompt: "Go to Copilot Notebook. Upload 12_Zava_Manufacturing_KPIs.xlsx, Email_01_Production_Emergency.docx, and 20_Zava_ESG_Sustainability_Framework.docx. In Instructions: \"Using all 3 documents, prepare a manufacturing crisis management brief for the Zava Group CEO. (1) From the production emergency email — what is the exact crisis, the revenue at risk, and immediate status; (2) From the manufacturing KPIs — quantify the OEE decline, backlog accumulation rate, and customer penalty exposure; (3) From the ESG framework — does the manufacturing crisis have any health and safety or environmental reporting obligations; (4) Build a 5-point Group CEO action agenda; (5) Identify the Board-level escalation points that require immediate attention.\"",
              fileRef: "12_Zava_Manufacturing_KPIs.xlsx, Email_01_Production_Emergency.docx, 20_Zava_ESG_Sustainability_Framework.docx"
            },
            {
              title: "SIRIM audit and OEE recovery cross-document analysis",
              prompt: "Go to Copilot Notebook. Upload 12_Zava_Manufacturing_KPIs.xlsx and 21_Zava_Chemical_Safety_HIRARC.docx. In Instructions: \"Using both documents, prepare a combined SIRIM audit readiness and OEE recovery analysis for the Plant General Manager. (1) From the KPI data — which AS9100D quality metrics are most at risk given the OEE decline; (2) From the HSE document — are there any health and safety gaps in the CNC maintenance procedures that SIRIM will assess during the audit; (3) Cross-reference: does the spindle motor failure incident suggest any HSE policy gaps in lockout/tagout or machine guarding; (4) Build an 8-week audit preparation priority list combining quality and HSE requirements. Format as an integrated audit readiness plan.\"",
              fileRef: "12_Zava_Manufacturing_KPIs.xlsx, 21_Zava_Chemical_Safety_HIRARC.docx"
            }
          ]
        },
        {
          tool: "🤝 Cowork (Pages)",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Build OEE recovery and backlog tracker in Pages",
              prompt: "In Copilot Chat, upload 12_Zava_Manufacturing_KPIs.xlsx and ask for a production KPI summary. Click Open in Copilot Pages. Ask: \"Reorganise this into a collaborative OEE Recovery and Backlog Tracker for the Zava Manufacturing Operations team of 12 supervisors. Structure as: (1) Daily OEE Dashboard — actual vs 70% recovery target by line; (2) CNC Line 3 Spindle Repair Tracker — daily status update; (3) Backlog Clearance Tracker — 2,800 units by customer with weekly progress; (4) Customer Delivery Status — RAG by account; (5) SIRIM Audit Preparation Checklist. Format for daily updates by shift supervisors and quality managers.\"",
              fileRef: "12_Zava_Manufacturing_KPIs.xlsx"
            },
            {
              title: "Build SIRIM audit preparation planning canvas",
              prompt: "In Copilot Chat, type a manufacturing quality audit preparation prompt. Click Open in Copilot Pages. Ask: \"Create a collaborative SIRIM AS9100D Audit Preparation Canvas for the Zava Manufacturing Quality team of 8 members. Context: audit in 8 weeks, OEE 62%, backlog 2,800 units. Structure as: (1) Department Readiness Status — 8 departments with traffic light; (2) Documentation Preparation Tracker — 6 document categories with completion status; (3) Internal Mock Audit Schedule — dates and assessors; (4) Non-Conformance Resolution Log — open NCRs to be closed before audit; (5) Auditor Hosting Plan — logistics and room preparation. Format for collaborative input from all 8 department heads.\""
            }
          ]
        },
        {
          tool: "🤖 Word Agent",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Set up a Manufacturing Quality Advisor agent",
              prompt: "Open 21_Zava_Chemical_Safety_HIRARC.docx in Word — or save a Zava Manufacturing quality procedures document. Create an agent named Zava Manufacturing Quality Advisor. Instructions: \"Answer questions about Zava Manufacturing's quality and HSE procedures relevant to AS9100D and SIRIM compliance. Cite procedure sections. Under 150 words.\" Demo: type \"What is the non-conforming product control procedure and what are the 5 steps a quality inspector must follow when they identify a non-conforming aerospace component?\"",
              fileRef: "21_Zava_Chemical_Safety_HIRARC.docx"
            },
            {
              title: "Demo the Manufacturing Quality Advisor — SIRIM audit queries",
              prompt: "With the agent active, ask 3 queries. Query 1: \"What are the corrective action request process steps and what is the maximum time allowed between raising an NCR and closing it under our quality management system?\" Query 2: \"What does the risk assessment procedure require before performing non-routine maintenance on a CNC spindle assembly?\" Query 3: \"What customer notification is required when a batch of shipped components is recalled due to a quality non-conformance?\"",
              fileRef: "21_Zava_Chemical_Safety_HIRARC.docx"
            }
          ]
        },
        {
          tool: "🤖 PowerPoint Agent",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Set up an Operations Recovery Presenter agent",
              prompt: "Create or open the operations recovery PowerPoint from the PPT demo. Save as Zava_Manufacturing_Recovery_2025.pptx. Create an agent named Zava Manufacturing Coach. Instructions: \"Answer questions about Zava Manufacturing's operations recovery presentation. Reference slide numbers. Under 100 words.\" Demo: type \"Which slide shows the backlog clearance timeline and when is the projected date to clear all 2,800 units?\""
            },
            {
              title: "Demo the Manufacturing Coach — Board queries",
              prompt: "With the agent active, run 3 queries. Query 1: \"Which slide shows the OEE waterfall breakdown and what is the single biggest contributor to the OEE decline?\" Query 2: \"What is the total capital investment being requested and what is the expected OEE improvement — which slide?\" Query 3: \"What are the 2 Board decisions required and what is the risk of delay to each decision?\""
            }
          ]
        },
        {
          tool: "🤖 Excel Agent",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Set up a Manufacturing KPI Agent",
              prompt: "Open 12_Zava_Manufacturing_KPIs.xlsx. Create an agent named Zava Manufacturing Advisor. Instructions: \"Answer questions about Zava Manufacturing's OEE, backlog, and quality KPIs. Cite sheet names. Express revenue in MYR millions.\" Demo: type \"What is the current OEE percentage and how does it compare to the FY2023 baseline of 76%?\"",
              fileRef: "12_Zava_Manufacturing_KPIs.xlsx"
            },
            {
              title: "Demo the Manufacturing Advisor — operations queries",
              prompt: "With the agent active, run 3 queries. Query 1: \"What is the current backlog in units and MYR value and at the current weekly clearance rate, how many weeks to clear it?\" Query 2: \"Which CNC production line has the highest unplanned downtime in FY2024 and how many hours of availability loss did it accumulate?\" Query 3: \"What is the first-pass yield rate for FY2024 and is it above or below the AS9100D minimum acceptable quality level of 98.5%?\"",
              fileRef: "12_Zava_Manufacturing_KPIs.xlsx"
            }
          ]
        }
      ]
    },
    {
      id: "pharma",
      name: "Pharmaceutical & Life Sciences",
      icon: "💊",
      color: "#1A3A5C",
      accent: "#2980B9",
      company: "Zava Pharmaceutical Industries Sdn Bhd",
      tagline: "BPfK Sitagliptin Q3 2025 | 3 BPOM notices closed Apr 2025 | GDP audit 6 weeks | 4 Phase II/III",
      scenario: "Zava Pharmaceutical Industries Sdn Bhd (Zava Pharma) is a Malaysian generic and specialty pharmaceutical company with a growing pipeline of 4 Phase II and Phase III clinical products. The company received 3 BPOM Indonesia manufacturing notices in FY2024 — all formally closed as of April 2025 — and has a GDP (Good Distribution Practice) audit scheduled in 6 weeks. The strategic priority is the BPfK Sitagliptin 100mg product registration submission targeting Q3 2025, which would open a significant generic market opportunity in Malaysia's MYR 840 million oral antidiabetic segment. Head of Regulatory Affairs Dr Maisarah Zainuddin and VP Research and Development Dr Sanjay Menon need Copilot to manage the BPfK dossier preparation, GDP audit readiness, ASEAN regulatory strategy, and clinical pipeline communication.",
      files: ["17_Zava_Pharma_Pipeline.xlsx", "Email_09_Risk_Committee_Prep.docx"],
      prompts: [
        {
          tool: "🤖 Copilot Chat (Basic)",
          license: "Free — no M365 license needed",
          account: "Sasha Ouellet — SashaO@ABSx62256373.OnMicrosoft.com",
          prompts: [
            {
              title: "Explain BPfK product registration and timeline in Malaysia",
              prompt: "Ask Copilot: \"Explain the Biro Pengawalan Farmaseutikal Kebangsaan (BPfK) product registration process for pharmaceutical companies in Malaysia. Zava Pharma has a Sitagliptin 100mg product registration submission targeting Q3 2025. Cover: (1) The BPfK product registration pathway for a generic pharmaceutical — the NDA-2 or ACTD format required, and the typical review timeline; (2) The 5 most common reasons BPfK returns or queries a pharmaceutical product registration dossier; (3) What a Q3 2025 submission target means for the preparation timeline — how many months before submission should dossier preparation begin; (4) The post-registration requirements — labelling approval, GMP site audit. Maximum 250 words.\""
            },
            {
              title: "Brief me before the BPfK regulatory pre-submission meeting",
              prompt: "Ask Copilot: \"I am the Head of Regulatory Affairs at Zava Pharma, a Malaysian pharmaceutical company. We have a pre-submission meeting with BPfK next week regarding our Sitagliptin 100mg registration dossier and 3 previous BPOM notices. Brief me on: (1) What BPfK pre-submission meetings typically cover — what questions to expect from the BPfK reviewer; (2) How to address the 3 BPOM Indonesia notices in the meeting — all 3 are closed as of April 2025 but BPfK may ask about them; (3) The GDP (Good Distribution Practice) audit scheduled in 6 weeks — how this audit relates to the registration timeline; (4) The single most important message to land with BPfK about Zava Pharma's quality standards. Maximum 200 words.\""
            },
            {
              title: "What is GDP audit and why does it matter for a pharma distributor?",
              prompt: "Ask Copilot: \"Explain Good Distribution Practice (GDP) in pharmaceutical distribution and why a GDP audit is important for a Malaysian pharmaceutical company like Zava Pharma. Cover: (1) What GDP requires — cold chain management, storage conditions, documentation of product movements; (2) The regulatory consequences of failing a GDP audit in Malaysia — BPfK can suspend distribution licences; (3) What the 6-week lead time before a GDP audit means for preparation — what documentation must be current and what processes must be demonstrably compliant; (4) How GDP compliance evidence supports a product registration application with BPfK — is there an explicit link; (5) The 3 most common GDP audit findings in Malaysian pharmaceutical distribution. Maximum 250 words.\""
            }
          ]
        },
        {
          tool: "�� Researcher",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Research BPfK registration requirements for generic pharmaceuticals",
              prompt: "In Copilot Chat, switch to the Researcher agent. Upload 17_Zava_Pharma_Pipeline.xlsx. Ask: \"Review Zava Pharma's product pipeline data. Then search the web for: current BPfK product registration requirements for generic pharmaceuticals under the ACTD format — any updated guidelines from 2023 to 2025; the typical BPfK review timeline for a standard NDA-2 generic drug application versus an expedited pathway; any recent BPfK enforcement actions or registration refusals for Malaysian pharmaceutical companies that could provide benchmarks; and ASEAN MRA harmonised dossier requirements that could accelerate Sitagliptin registration across Malaysia and ASEAN markets simultaneously. Zava Pharma targets Q3 2025 submission. What preparation is needed today to hit that deadline? Cite all sources.\"",
              fileRef: "17_Zava_Pharma_Pipeline.xlsx"
            },
            {
              title: "Research pharma Phase II and III clinical trial management in ASEAN",
              prompt: "In Copilot Chat, switch to the Researcher agent. Ask: \"Search the web for clinical trial management best practices and regulatory requirements in Malaysia and ASEAN for Phase II and Phase III pharmaceutical trials. Find: NMRR (National Medical Research Register) requirements for clinical trials in Malaysia; ASEAN CTD (Common Technical Document) submission standards; contract research organisation (CRO) capabilities in Malaysia and Singapore that Zava Pharma could engage for its 4 active Phase II and III trials; and patient recruitment benchmarks for diabetology and cardiovascular Phase III trials in Southeast Asia. Zava Pharma has 4 active Phase II and III products. What are the 3 most important operational actions to accelerate trial milestones?\""
            },
            {
              title: "Research BPOM Indonesia compliance and pharma market",
              prompt: "In Copilot Chat, switch to the Researcher agent. Upload 17_Zava_Pharma_Pipeline.xlsx. Ask: \"Review Zava Pharma's pipeline and compliance data. Then search the web for: BPOM Indonesia regulatory requirements for pharmaceutical manufacturing and distribution — what triggers a manufacturing notice or warning letter; the process for closing a BPOM notice and what evidence BPOM requires to confirm remediation; the Indonesian pharmaceutical market size, growth rate, and generic segment dynamics; and registration requirements for exporting Malaysian generic pharmaceuticals to the Indonesian market under ASEAN MRA. Zava Pharma received 3 BPOM notices — all closed April 2025. What does full BPOM compliance require going forward and what are the market entry opportunities?\"",
              fileRef: "17_Zava_Pharma_Pipeline.xlsx"
            }
          ]
        },
        {
          tool: "📊 Analyst",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Analyse Zava Pharma pipeline and revenue KPIs",
              prompt: "In Copilot Chat, switch to the Analyst agent. Upload 17_Zava_Pharma_Pipeline.xlsx. Ask: \"Analyse the full Zava Pharma pipeline and financial dataset. Calculate: (1) Total revenue by product line and the year-on-year growth rate from FY2022 to FY2024; (2) The pipeline probability-weighted NPV — assign 50% probability to Phase II and 70% to Phase III products and calculate the expected revenue contribution; (3) The R&D investment as a percentage of revenue — is it above or below the 12% industry benchmark for specialty pharma; (4) The Sitagliptin 100mg projected peak sales in Malaysia post-registration, assuming 8% market share in the Malaysian oral antidiabetic market; (5) Revenue at risk if BPfK registration is delayed by 2 quarters. Present as a Board pharma strategy dashboard.\"",
              fileRef: "17_Zava_Pharma_Pipeline.xlsx"
            },
            {
              title: "Analyse GDP compliance readiness and BPfK registration timeline",
              prompt: "In Copilot Chat, switch to the Analyst agent. Upload 17_Zava_Pharma_Pipeline.xlsx. Ask: \"Analyse the regulatory timeline data for Zava Pharma. Calculate: (1) The number of days from today to the Sitagliptin Q3 2025 BPfK submission target and whether the current dossier preparation progress is on track; (2) The GDP audit in 6 weeks — how many distribution site visits, storage condition reports, and documentation categories must be current; (3) The revenue impact of a 2-quarter BPfK registration delay on Sitagliptin — lost first-mover generic market advantage in MYR millions; (4) For the 4 Phase II and III products, what are the trial completion dates and the earliest BPfK filing dates for each; (5) The total pipeline risk if all 3 BPOM notices had not been closed. Format as a Regulatory Affairs and Finance dashboard.\"",
              fileRef: "17_Zava_Pharma_Pipeline.xlsx"
            },
            {
              title: "Model Sitagliptin registration and peak sales projection",
              prompt: "In Copilot Chat, switch to the Analyst agent. Upload 17_Zava_Pharma_Pipeline.xlsx. Ask: \"Build a Sitagliptin 100mg commercial model. From the pipeline data and general pharmaceutical market assumptions: (1) The Malaysian oral antidiabetic drug market size in MYR millions — total and generic segment; (2) Zava Pharma's expected market share trajectory in years 1 to 5 post-registration — start at 4% and build to 8% as per strategy; (3) Revenue in MYR millions per year from launch to Year 5; (4) The gross margin on a generic oral antidiabetic drug — typically 55-65%; (5) NPV of the Sitagliptin product at a 12% discount rate over 10 years — this is the financial justification for the BPfK registration investment. Format as a product commercial case.\"",
              fileRef: "17_Zava_Pharma_Pipeline.xlsx"
            }
          ]
        },
        {
          tool: "📊 Copilot in Excel",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Instant Zava Pharma pipeline and compliance summary",
              prompt: "Open 17_Zava_Pharma_Pipeline.xlsx. Ask Copilot: \"Give me a plain-English executive summary of this pharma pipeline workbook. How many products are in Phase II and Phase III? What is the Sitagliptin 100mg registration target date? What was the BPOM notice closure status? What is the GDP audit timeline? Flag any product where the regulatory filing deadline is within 90 days and preparation is less than 70% complete. Format: 3-sentence overview, then 4 specific flagged concerns with sheet name and row reference.\"",
              fileRef: "17_Zava_Pharma_Pipeline.xlsx"
            },
            {
              title: "Create pipeline stage and NPV chart",
              prompt: "Open 17_Zava_Pharma_Pipeline.xlsx. Ask Copilot: \"Create a pipeline bubble chart showing all active Zava Pharma products. X-axis: Development Stage from Phase I to Registered. Y-axis: Probability-Weighted NPV in MYR millions. Bubble size: Annual Revenue Potential in MYR millions. Use different colours for Phase II, Phase III, Pre-Registration, and Registered. Label each bubble with the product name. Title: Zava Pharma — Pipeline Portfolio NPV vs Development Stage. This chart will be used in the Board Pharmaceutical Strategy Committee presentation.\"",
              fileRef: "17_Zava_Pharma_Pipeline.xlsx"
            },
            {
              title: "Add regulatory timeline Gantt and deadline status",
              prompt: "Open 17_Zava_Pharma_Pipeline.xlsx. Navigate to the Regulatory Timeline sheet. Ask Copilot: \"For each product in the regulatory pipeline, add a Deadline Status column. If the BPfK or BPOM submission deadline is within 90 days and preparation progress is below 80%, display At Risk in red. If within 90 days but preparation is above 80%, display On Track in green. If beyond 90 days, display Planned in blue. Tell me how many products are At Risk and which product has the nearest submission deadline with the most critical preparation gap.\"",
              fileRef: "17_Zava_Pharma_Pipeline.xlsx"
            },
            {
              title: "Natural language query — revenue pipeline and market opportunity",
              prompt: "Open 17_Zava_Pharma_Pipeline.xlsx. Ask Copilot: \"Without navigating sheets, answer: (1) What is the total probability-weighted NPV of the Zava Pharma clinical pipeline for all Phase II and Phase III products combined; (2) What is the projected first-year revenue from Sitagliptin 100mg if BPfK registration is achieved by Q1 2026 and Zava captures 4% market share in year 1; (3) How many active Phase III products does Zava Pharma have and what is the earliest expected regulatory submission date for any of them; (4) What was the total R&D expenditure in FY2024 and what percentage of total revenue does it represent. Format as a 2-column pipeline Q and A.\"",
              fileRef: "17_Zava_Pharma_Pipeline.xlsx"
            }
          ]
        },
        {
          tool: "📝 Copilot in Word",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Summarise Zava Pharma strategy for Board pre-read",
              prompt: "Open a new Word document. Ask Copilot: \"Draft a 1-page Board pre-read memo for Zava Pharma covering FY2025 strategic priorities. Include: (1) Pipeline overview — 4 Phase II and III products, Sitagliptin 100mg BPfK submission Q3 2025; (2) Regulatory compliance update — 3 BPOM notices closed April 2025, GDP audit in 6 weeks; (3) Commercial strategy — generic antidiabetic and cardiovascular focus, ASEAN market expansion; (4) R&D investment — current level vs 12% of revenue benchmark; (5) 2 Board decisions required: Sitagliptin commercial launch budget and Phase III trial CRO appointment. Formal pharmaceutical Board memo style. Maximum 400 words.\""
            },
            {
              title: "Draft BPfK pre-submission meeting brief",
              prompt: "Open a new Word document. Ask Copilot: \"Draft a formal Pre-Submission Meeting Brief for Zava Pharma's BPfK pre-submission consultation on the Sitagliptin 100mg product registration. The brief must: (1) Introduce Zava Pharma and our regulatory track record; (2) Describe the Sitagliptin dossier — ACTD format, reference product, bioequivalence data summary; (3) Address the 3 BPOM Indonesia manufacturing notices — all closed April 2025 — and confirm current GMP compliance; (4) Request BPfK's guidance on: preferred reference product, any specific Malaysian labelling requirements, and expedited review eligibility under the National Medicine Policy for oral antidiabetics; (5) Propose a Q3 2025 submission target and request feedback on timeline feasibility. Formal regulatory submission tone. 500 words.\""
            },
            {
              title: "Rewrite Good Distribution Practice checklist for warehouse staff",
              prompt: "Open a new Word document. Ask Copilot: \"Write a plain-language Good Distribution Practice (GDP) daily compliance checklist for Zava Pharma warehouse and distribution staff with no regulatory background. The checklist should cover: (1) Cold chain temperature monitoring — what to check, when, and how to record; (2) Stock rotation — FIFO first-in-first-out procedure in 4 steps; (3) Batch traceability — what documents to complete when receiving or dispatching a pharmaceutical batch; (4) Quarantine area management — how to segregate rejected or recalled stock; (5) BPfK inspection readiness — the 3 things to check every day that auditors look for first. Maximum 350 words. Practical, numbered steps, checkbox format.\""
            },
            {
              title: "Draft GDP audit preparation memo to distribution team",
              prompt: "Open a new Word document. Ask Copilot: \"Draft a formal memo from Zava Pharma's Head of Quality Assurance to the Distribution, Logistics, and Warehouse teams regarding the GDP audit scheduled in 6 weeks. The memo must: (1) State what GDP audit scope covers — storage conditions, documentation, cold chain, batch traceability; (2) List 5 specific documentation packages each team must prepare by audit week: temperature monitoring logs for 12 months, batch release certificates for all stocked products, returns and recalls log, delivery and receipt records, and staff training records; (3) Announce an internal mock audit 2 weeks before BPfK to identify gaps; (4) Assign the Quality Manager as audit coordination lead and provide their contact; (5) State the consequence of audit failure — potential suspension of distribution licence. Formal, urgent tone. 450 words.\""
            }
          ]
        },
        {
          tool: "🎯 Copilot in PowerPoint",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Create pharmaceutical Board strategy presentation",
              prompt: "Open a new PowerPoint. Ask Copilot: \"Create a 7-slide Board strategy presentation for Zava Pharma. Slide 1: Zava Pharma — FY2025 Pharmaceutical Strategy Review. Slide 2: Pipeline Overview — 4 Phase II and III products, NPV, and development timeline. Slide 3: Sitagliptin 100mg — product profile, BPfK submission timeline, commercial opportunity. Slide 4: Regulatory Compliance — BPOM notices closed, GDP audit preparation, BPfK relationship. Slide 5: ASEAN Market Expansion — Malaysia, Indonesia, Singapore regulatory strategy. Slide 6: R&D Investment Plan — FY2025-FY2027, pipeline progression milestones. Slide 7: Board Decisions Required — 2 approvals. Clean pharmaceutical white and navy blue design.\""
            },
            {
              title: "Generate BPfK pre-submission meeting slides",
              prompt: "Open a new PowerPoint. Ask Copilot: \"Create a 5-slide BPfK pre-submission consultation presentation for Zava Pharma's Sitagliptin 100mg product registration. Slide 1: Zava Pharma — Sitagliptin 100mg Pre-Submission Consultation BPfK. Slide 2: Product Profile — mechanism, indication, target population, comparator study summary. Slide 3: Dossier Readiness — ACTD module completion status, bioequivalence data summary. Slide 4: Regulatory History — 3 BPOM notices and current compliance status, GMP certificate dates. Slide 5: Questions for BPfK — 3 specific guidance requests: reference product confirmation, labelling requirements, and review timeline feasibility. Clean, professional pharmaceutical regulatory design.\""
            },
            {
              title: "Add ASEAN pharmaceutical market opportunity benchmarking slide",
              prompt: "In an open Zava Pharma PowerPoint, add a new slide. Ask Copilot: \"Create an ASEAN pharmaceutical market opportunity slide showing the oral antidiabetic market size in 5 markets: Malaysia, Indonesia, Thailand, Vietnam, and Philippines. Use a horizontal bar chart showing total market size in USD millions and generic segment percentage for each market. Highlight Malaysia and Indonesia as Zava Pharma's priority markets with a green callout. Add a text box showing Sitagliptin's projected market share and revenue in each market at Year 3. Title: Zava Pharma — ASEAN Oral Antidiabetic Market Opportunity.\""
            }
          ]
        },
        {
          tool: "📧 Copilot in Outlook",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Triage BPfK query letter on Sitagliptin dossier",
              prompt: "Open Outlook and find a BPfK query email or use Email_09_Risk_Committee_Prep.docx as a proxy — copy it and ask Copilot: \"I am the Zava Pharma Head of Regulatory Affairs and I have received a query from BPfK about our Sitagliptin registration dossier. Summarise: (1) What specific aspect of the dossier is BPfK querying — bioequivalence, labelling, or reference product; (2) What supporting documentation are they requesting; (3) The response deadline; (4) My 3 immediate actions to draft the response. Maximum 200 words.\""
            },
            {
              title: "Draft regulatory affairs update email to Group CEO",
              prompt: "Open a new Outlook email. Ask Copilot: \"Draft a formal monthly regulatory affairs update email from Zava Pharma's Head of Regulatory Affairs to the Group CEO and CFO. The email should summarise: (1) Sitagliptin 100mg dossier status — percentage complete and risk assessment for the Q3 2025 BPfK submission target; (2) GDP audit in 6 weeks — preparation status and any gaps identified; (3) BPOM notices status — all 3 confirmed closed April 2025, certificate received; (4) Phase II and III clinical trial milestones — which studies are on track and which are delayed; (5) 3 decisions needed from the CEO this month. Professional regulatory update tone. Under 300 words.\""
            },
            {
              title: "Copilot coaching on response to BPfK dossier query",
              prompt: "In Outlook, type a rough draft to BPfK: \"Dear BPfK, thank you for your query. We will review and provide a response. Our regulatory team is looking into it. Regards, Zava Pharma.\" Ask Copilot for coaching: \"I am a Head of Regulatory Affairs at a Malaysian pharmaceutical company responding to a BPfK product registration query. Evaluate on: (1) Regulatory credibility — does it demonstrate that we have a competent, organised regulatory function; (2) Commitment specificity — does it state a specific response timeline; (3) Tone — is it appropriately respectful to the national medicines regulator. Rewrite at a certified pharmaceutical company regulatory affairs standard with a 10-working-day response commitment and named contact.\""
            }
          ]
        },
        {
          tool: "🎙 Copilot in Teams",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Catch up on missed regulatory and pipeline review meeting",
              prompt: "Open an existing Teams meeting that was recorded and has a Copilot recap from your calendar. Ask: \"I am the Zava Pharma Regulatory Director and I missed this regulatory review meeting. Catch me up: (1) Which product submissions or BPfK correspondence were discussed; (2) Was the GDP audit preparation reviewed — what was the assessment of readiness; (3) Were any clinical trial milestone delays discussed and what was the impact on the BPfK filing calendar; (4) Actions assigned to the Regulatory team or myself; (5) Was the BPOM notice closure certificate discussed — has it been formally received from BPOM Indonesia.\""
            },
            {
              title: "Extract regulatory and clinical actions from the pipeline review",
              prompt: "Open an existing recorded Teams meeting from your calendar. Ask: \"Extract all regulatory, clinical, and quality assurance action items from this pharma pipeline review. Format as: Product Name; Regulatory Body (BPfK, BPOM, other); Action Type (Submission, Response, Audit Prep, Clinical); Specific Action; Owner; Deadline; Priority — Critical if BPfK or GDP audit related, High if a trial milestone, Normal for routine. Also note: is the Sitagliptin Q3 2025 submission on schedule based on this meeting discussion — was any risk to the timeline raised?\""
            },
            {
              title: "Draft pharma team clinical trial update from the monthly review",
              prompt: "Open an existing recorded Teams meeting recap from your calendar. Ask: \"Draft a monthly clinical trial and regulatory update email from the Zava Pharma VP Research and Development to all 12 scientists, clinical researchers, and regulatory affairs managers. Based on this meeting: (1) Pipeline update — trial status for each Phase II and III product; (2) Regulatory milestones due this month; (3) GDP audit preparation status; (4) BPOM Indonesia compliance confirmation; (5) Next 30-day priorities for R&D and Regulatory teams. Professional pharmaceutical R&D management communication. Under 300 words.\""
            }
          ]
        },
        {
          tool: "📓 Copilot Notebook",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Full regulatory compliance brief from 2 pharma documents",
              prompt: "Go to Copilot Notebook. Upload 17_Zava_Pharma_Pipeline.xlsx and Email_09_Risk_Committee_Prep.docx (as a proxy for a regulatory update email). In Instructions: \"Using both documents, prepare a comprehensive regulatory compliance brief for the Zava Pharma CEO. (1) From the pipeline data — what is the Sitagliptin registration readiness status and the gap to the Q3 2025 BPfK submission target; (2) From the email or update document — what regulatory risks or concerns have been raised; (3) What is the total pipeline revenue at risk if BPfK or GDP audit results delay any registration by 2 or more quarters; (4) Build a 30-day regulatory action agenda for the Head of Regulatory Affairs; (5) Identify the single most important Board-level decision to protect the Sitagliptin timeline.\"",
              fileRef: "17_Zava_Pharma_Pipeline.xlsx, Email_09_Risk_Committee_Prep.docx"
            },
            {
              title: "Pipeline NPV and commercial strategy analysis",
              prompt: "Go to Copilot Notebook. Upload 17_Zava_Pharma_Pipeline.xlsx. In Instructions: \"Using the pipeline data, build a comprehensive commercial strategy analysis for the Zava Pharma Board. (1) Calculate the total probability-weighted NPV of all active pipeline products using Phase II = 50% and Phase III = 70% success probability; (2) For the 3 highest-NPV products, model the revenue contribution to Zava Pharma in Year 1, Year 3, and Year 5 post-launch; (3) Identify the 2 products most at risk of pipeline failure based on development stage and timeline; (4) Calculate R&D spend efficiency — NPV per MYR million invested in R&D; (5) Recommend which pipeline product should receive the highest resource allocation priority. Format as a Board Strategy Committee pipeline investment paper.\"",
              fileRef: "17_Zava_Pharma_Pipeline.xlsx"
            }
          ]
        },
        {
          tool: "🤝 Cowork (Pages)",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Build regulatory compliance tracker in Pages",
              prompt: "In Copilot Chat, upload 17_Zava_Pharma_Pipeline.xlsx and ask for a regulatory timeline summary. Click Open in Copilot Pages. Ask: \"Reorganise this into a collaborative Regulatory Compliance Tracker for the Zava Pharma Regulatory Affairs team of 6 specialists. Structure as: (1) BPfK Submission Pipeline — all products with submission date and dossier completion status; (2) GDP Audit Preparation Tracker — 6 documentation categories with completion %; (3) BPOM Indonesia Compliance Log — notices, closures, certificates; (4) Clinical Trial Milestone Calendar; (5) Regulatory Correspondence Log. Format for daily collaborative editing by all 6 regulatory specialists.\"",
              fileRef: "17_Zava_Pharma_Pipeline.xlsx"
            },
            {
              title: "Build clinical pipeline planning canvas",
              prompt: "In Copilot Chat, upload 17_Zava_Pharma_Pipeline.xlsx and ask for a Phase II and III pipeline summary. Click Open in Copilot Pages. Ask: \"Expand this into a collaborative Clinical Pipeline Management Canvas for the Zava Pharma R&D team of 8 scientists and clinical managers. Structure as: (1) Phase II Product Tracker — trial status, patient recruitment, and next milestone; (2) Phase III Product Tracker — same; (3) CRO Partnership Status — CRO name, contract status, and performance; (4) Patient Recruitment Log — weekly enrolment vs target per trial; (5) Regulatory Submission Calendar. Format for simultaneous editing by all 8 R&D team members.\"",
              fileRef: "17_Zava_Pharma_Pipeline.xlsx"
            }
          ]
        },
        {
          tool: "🤖 Word Agent",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Set up a Zava Pharma Pipeline Advisor",
              prompt: "Open a Zava Pharma strategy or pipeline document in Word — or create one by asking Copilot to generate a Sitagliptin product profile summary and saving as Zava_Pharma_Pipeline_Strategy.docx. Create an agent named Zava Pharma Pipeline Advisor. Instructions: \"Answer questions about Zava Pharma's pharmaceutical pipeline, BPfK registration, and regulatory strategy. Cite document sections. Under 150 words.\" Demo: type \"What is the current status of the Sitagliptin 100mg BPfK submission and what are the 3 most critical dossier preparation tasks remaining?\""
            },
            {
              title: "Demo the Pharma Pipeline Advisor — Board and regulatory queries",
              prompt: "With the agent active, ask 3 queries. Query 1: \"Which Phase III product has the highest NPV and what is the expected BPfK submission date?\" Query 2: \"How does the GDP audit timeline interact with the Sitagliptin BPfK submission — could a GDP audit failure delay registration?\" Query 3: \"What is Zava Pharma's total R&D investment as a percentage of revenue and how does it compare to the 12% industry benchmark?\""
            }
          ]
        },
        {
          tool: "🤖 PowerPoint Agent",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Set up a BPfK Pre-Submission Presenter agent",
              prompt: "Create or open the BPfK pre-submission PowerPoint from the PPT demo. Save as Zava_Pharma_BPfK_PreSub_2025.pptx. Create an agent named BPfK Presentation Coach. Instructions: \"Answer questions about Zava Pharma's BPfK pre-submission presentation. Reference slide numbers. Under 100 words.\" Demo: type \"Which slide addresses the BPOM Indonesia notice history and what is the current compliance status shown?\""
            },
            {
              title: "Demo the BPfK Presentation Coach — pre-meeting queries",
              prompt: "With the agent active, run 3 queries simulating BPfK pre-submission preparation. Query 1: \"If BPfK asks about the bioequivalence study design for Sitagliptin, which slide summarises the BE data?\" Query 2: \"What slide shows our GDP compliance status and what evidence do we have ready to present to BPfK?\" Query 3: \"Which specific questions are we asking BPfK in this meeting and where are they on the slide deck?\""
            }
          ]
        },
        {
          tool: "🤖 Excel Agent",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Set up a Pharma Pipeline Analytics agent",
              prompt: "Open 17_Zava_Pharma_Pipeline.xlsx. Create an agent named Zava Pharma Pipeline Analyst. Instructions: \"Answer questions about Zava Pharma's product pipeline, revenue projections, and regulatory timelines. Cite sheet names. Express all financial figures in MYR millions.\" Demo: type \"How many products are currently in Phase II or Phase III and what is the combined probability-weighted NPV?\"",
              fileRef: "17_Zava_Pharma_Pipeline.xlsx"
            },
            {
              title: "Demo the Pipeline Analyst — commercial and regulatory queries",
              prompt: "With the agent active, run 3 queries. Query 1: \"What is the projected Year 1 revenue from Sitagliptin 100mg assuming Q3 2025 BPfK registration and a 4% initial market share in the Malaysian oral antidiabetic segment?\" Query 2: \"Which Phase III product has the nearest trial completion date and what is the expected BPfK filing date?\" Query 3: \"What is the total R&D expenditure in FY2024 and as a percentage of total Zava Pharma revenue for the same year?\"",
              fileRef: "17_Zava_Pharma_Pipeline.xlsx"
            }
          ]
        }
      ]
    },
    {
      id: "property",
      name: "Property & Real Estate",
      icon: "🏢",
      color: "#1A3A5C",
      accent: "#27AE60",
      company: "Zava Properties Group Bhd",
      tagline: "MYR 4.84B portfolio | REIT IPO 2026 | 2 anchor tenants Dec 2025 | Penang MYR 2.1B GDV",
      scenario: "Zava Properties Group Bhd is a Malaysian commercial property developer and asset manager with 6 prime commercial assets totalling MYR 4.84 billion in portfolio value, generating stable rental income from office, retail, and industrial properties across the Klang Valley and Penang. The company is preparing for a Bursa Malaysia REIT IPO in 2026 to unlock institutional capital and fund the Penang mixed-use development pipeline valued at MYR 2.1 billion GDV. The critical near-term risk is the expiry of 2 anchor tenant leases in December 2025, which together represent a significant percentage of portfolio gross rental income and could impair REIT IPO pricing and investor confidence. Group CEO Datin Rohani Hashim and CFO Brian Lim need Copilot to manage the REIT IPO preparation, anchor tenant retention strategy, asset performance analysis, and Penang development planning.",
      files: ["14_Zava_Properties_Portfolio.xlsx", "Email_09_Risk_Committee_Prep.docx"],
      prompts: [
        {
          tool: "🤖 Copilot Chat (Basic)",
          license: "Free — no M365 license needed",
          account: "Sasha Ouellet — SashaO@ABSx62256373.OnMicrosoft.com",
          prompts: [
            {
              title: "Explain Malaysian property market and REIT structures",
              prompt: "Ask Copilot: \"Explain Malaysian Real Estate Investment Trust (REIT) structures and how a property developer converts assets to a REIT IPO. Zava Properties is considering listing 6 commercial assets with a total portfolio value of MYR 4.84 billion. Cover: (1) The M-REIT regulatory framework — Securities Commission guidelines and Bursa Malaysia listing requirements; (2) The typical IPO process for an M-REIT — from asset injection to listing, and the timeline; (3) The key metrics fund managers and institutional investors look for — yield, occupancy, weighted average lease expiry (WALE), and NTA per unit; (4) The most common reason Malaysian REIT IPOs are delayed or undersubscribed; (5) The impact of anchor tenant losses on REIT IPO pricing. Maximum 250 words.\""
            },
            {
              title: "Brief me before the REIT IPO investor pre-marketing road show",
              prompt: "Ask Copilot: \"I am the CEO of Zava Properties, a Malaysian property company with a MYR 4.84 billion commercial portfolio. I am preparing for a REIT IPO investor road show. Brief me on: (1) The 5 key questions institutional investors always ask at a REIT IPO road show — and my best answers for a MYR 4.84 billion Malaysian commercial portfolio; (2) How to handle investor concerns about the 2 anchor tenants whose leases expire in December 2025; (3) How the Penang MYR 2.1 billion GDV development pipeline increases the REIT's growth story; (4) How Malaysian REITs are valued by institutional investors — capitalisation rate approach versus NAV approach; (5) The single most compelling message to open the investor meeting with. Maximum 200 words.\""
            },
            {
              title: "What is capitalisation rate and how does it affect property valuation?",
              prompt: "Ask Copilot: \"Explain capitalisation rate (cap rate) in commercial property valuation and how it affects asset pricing for a Malaysian property portfolio. Zava Properties has 6 commercial assets worth MYR 4.84 billion in total. Cover: (1) How cap rate is calculated — Net Operating Income divided by Asset Value; (2) What drives cap rate compression or expansion in the Malaysian commercial property market; (3) How a 25 basis point increase in cap rates would affect the value of a MYR 4.84 billion portfolio — give the MYR impact; (4) The difference between retail, office, and industrial cap rates in Klang Valley today; (5) Why a REIT IPO investor focuses on cap rate, WALE, and occupancy above all other metrics. Maximum 250 words.\""
            }
          ]
        },
        {
          tool: "�� Researcher",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Research Malaysian commercial property market and REIT outlook",
              prompt: "In Copilot Chat, switch to the Researcher agent. Upload 14_Zava_Properties_Portfolio.xlsx. Ask: \"Review Zava Properties' portfolio data. Then search the web for: Malaysian commercial property market outlook for 2025 and 2026 — office, retail, and industrial asset class performance; current REIT IPO activity on Bursa Malaysia — any REITs listed in 2024 or 2025 and their performance and initial yields; institutional investor appetite for Malaysian REIT IPOs; and the Penang commercial property development pipeline — specific data on Penang GDV and project completion timelines for 2025 and 2026. What are the 3 most important market conditions affecting whether to proceed with the Zava REIT IPO in 2026? Cite all sources.\"",
              fileRef: "14_Zava_Properties_Portfolio.xlsx"
            },
            {
              title: "Research anchor tenant lease renewal benchmarks",
              prompt: "In Copilot Chat, switch to the Researcher agent. Ask: \"Search the web for commercial property anchor tenant lease renewal best practices and benchmarks. Specifically find: typical Malaysian commercial property anchor tenant lease terms — duration, rental rate escalation, and break clauses; how Malaysian property companies and REITs have handled anchor tenant departures — case studies of occupancy impact; rental rate concession benchmarks that landlords offer to retain anchor tenants in Malaysian malls and office buildings; and the WALE (weighted average lease expiry) standards that institutional REIT investors require before investing in a commercial property fund. Zava Properties has 2 anchor tenants with leases expiring December 2025 and must decide whether to offer lease incentives.\""
            },
            {
              title: "Research Penang commercial property and GDV project feasibility",
              prompt: "In Copilot Chat, switch to the Researcher agent. Upload 14_Zava_Properties_Portfolio.xlsx. Ask: \"Review Zava Properties' Penang pipeline data. Then search the web for: Penang commercial property development pipeline and current GDV benchmarks; Penang Island versus Seberang Perai commercial development demand — office, retail, and mixed-use; regulatory approvals required for a MYR 2.1 billion GDV mixed-use development in Penang — state government, MBPP or MBSP, and federal agencies; and infrastructure and connectivity improvements in Penang that would support demand for commercial space. Zava Properties is planning a MYR 2.1 billion GDV Penang development. What are the 3 most critical feasibility risks and how should they be mitigated?\"",
              fileRef: "14_Zava_Properties_Portfolio.xlsx"
            }
          ]
        },
        {
          tool: "📊 Analyst",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Analyse Zava Properties portfolio KPIs and REIT readiness",
              prompt: "In Copilot Chat, switch to the Analyst agent. Upload 14_Zava_Properties_Portfolio.xlsx. Ask: \"Analyse the full Zava Properties portfolio dataset. Calculate: (1) Total portfolio net operating income (NOI) by asset and aggregate, and the NOI yield on total portfolio value of MYR 4.84 billion; (2) Portfolio WALE (weighted average lease expiry) weighted by rental income — what is the WALE today versus post December 2025 if both anchor tenants are lost; (3) The cap rate implied by the current NOI and portfolio value — compare to Klang Valley prime office and retail benchmark cap rates; (4) Gross rental income growth year-on-year from FY2022 to FY2024; (5) The revenue impact if both December 2025 anchor tenants are not renewed and the assets remain vacant for 12 months. Format as a REIT IPO due diligence dashboard.\"",
              fileRef: "14_Zava_Properties_Portfolio.xlsx"
            },
            {
              title: "Analyse REIT IPO pricing and investor yield modelling",
              prompt: "In Copilot Chat, switch to the Analyst agent. Upload 14_Zava_Properties_Portfolio.xlsx. Ask: \"Build a REIT IPO pricing model for Zava Properties. (1) At a 5.5% and 6.0% distribution yield — what is the implied IPO unit price range given the forecast distributable income; (2) What percentage of the MYR 4.84 billion portfolio must be injected into the REIT at IPO versus retained by Zava Properties as a sponsor; (3) How does the Penang MYR 2.1 billion GDV pipeline affect the REIT growth story — model the GDV as a pipeline injection into the REIT in Year 3 and Year 5; (4) The impact of losing the 2 anchor tenants on distributable income and IPO yield — provide a sensitivity table; (5) What is the REIT's projected market capitalisation at IPO? Format as an IPO feasibility model.\"",
              fileRef: "14_Zava_Properties_Portfolio.xlsx"
            },
            {
              title: "Model Penang GDV pipeline and return on investment",
              prompt: "In Copilot Chat, switch to the Analyst agent. Upload 14_Zava_Properties_Portfolio.xlsx. Ask: \"Build a Penang development return model. From the pipeline data: (1) Total development cost for the MYR 2.1 billion GDV Penang project — land, construction, and soft costs as a percentage of GDV; (2) Project net profit margin — GDV minus total development cost; (3) IRR assuming a 4-year development timeline, phased sell-down, and typical Penang commercial property take-up rates; (4) The construction financing cost — how much bank borrowing is required and what is the debt service coverage; (5) The revenue contribution of the Penang project to Zava Properties Group in Year 4 and Year 5. Format as a development project investment committee paper.\"",
              fileRef: "14_Zava_Properties_Portfolio.xlsx"
            }
          ]
        },
        {
          tool: "📊 Copilot in Excel",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Instant Zava Properties portfolio executive summary",
              prompt: "Open 14_Zava_Properties_Portfolio.xlsx. Ask Copilot: \"Give me a plain-English executive summary of this commercial property portfolio workbook. What is the total portfolio value and number of assets? Which 2 anchor tenants have leases expiring December 2025 and what percentage of gross rental income do they represent? What is the Penang pipeline GDV and what stage is the project at? Flag any asset with occupancy below 85% or a lease with under 12 months to expiry. Format: 3-sentence portfolio overview, then 4 flagged concerns with sheet and row reference.\"",
              fileRef: "14_Zava_Properties_Portfolio.xlsx"
            },
            {
              title: "Create portfolio yield and cap rate comparison chart",
              prompt: "Open 14_Zava_Properties_Portfolio.xlsx. Ask Copilot: \"Create a dual-axis bar and line chart for all 6 Zava Properties commercial assets. Bar chart (left axis): Gross Rental Income in MYR millions per asset. Line chart (right axis): Implied cap rate as percentage per asset. Sort assets by cap rate from lowest to highest. Add a horizontal dashed reference line at the 5.5% Klang Valley prime benchmark cap rate. Label each bar with the asset name and occupancy rate. Title: Zava Properties — Rental Income and Cap Rate by Asset FY2024.\"",
              fileRef: "14_Zava_Properties_Portfolio.xlsx"
            },
            {
              title: "Add WALE and lease renewal risk flag column",
              prompt: "Open 14_Zava_Properties_Portfolio.xlsx. Navigate to the Tenant Lease Registry sheet. Ask Copilot: \"For each tenant row, add a Lease Risk Status column. If the lease expires within 6 months and the tenant is classified as anchor or major tenant, display Critical Renewal in red. If the lease expires within 12 months and the tenant is anchor or major, display High Renewal Risk in orange. If the tenant is a minor tenant expiring within 12 months, display Monitor in yellow. Otherwise display Stable in grey. Tell me: how many tenants are Critical Renewal today and what percentage of total gross rental income do they represent?\"",
              fileRef: "14_Zava_Properties_Portfolio.xlsx"
            },
            {
              title: "Natural language query — portfolio yield and REIT readiness",
              prompt: "Open 14_Zava_Properties_Portfolio.xlsx. Ask Copilot: \"Without navigating sheets, answer: (1) What is the portfolio-level net operating income yield on the MYR 4.84 billion total portfolio value; (2) What is the current WALE weighted by rental income and what does it drop to if the 2 December 2025 anchor tenant leases are not renewed; (3) Which single asset has the highest gross rental income and what is its occupancy rate; (4) What is the total annual rental income at risk from the 2 expiring anchor tenant leases. Format as a 2-column REIT due diligence Q and A.\"",
              fileRef: "14_Zava_Properties_Portfolio.xlsx"
            }
          ]
        },
        {
          tool: "📝 Copilot in Word",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Summarise Zava Properties REIT strategy for Board pre-read",
              prompt: "Open a new Word document. Ask Copilot: \"Draft a 1-page Board pre-read memo for Zava Properties covering the MYR 4.84 billion commercial portfolio and the REIT IPO strategy. Include: (1) Portfolio overview — 6 assets, total value, portfolio yield; (2) REIT IPO strategy — timeline, target distribution yield, estimated market cap; (3) Key risk — 2 anchor tenant leases expiring December 2025; (4) Penang GDV pipeline — MYR 2.1 billion, development timeline, contribution to REIT growth story; (5) 2 Board decisions required: approve anchor tenant retention incentives and confirm REIT IPO sponsor injected asset list. Formal Board memo style. Maximum 400 words.\""
            },
            {
              title: "Draft anchor tenant lease renewal proposal letter",
              prompt: "Open a new Word document. Ask Copilot: \"Draft a formal lease renewal proposal letter from Zava Properties Group CEO to the CEO of an anchor tenant whose lease expires in December 2025. The letter should: (1) Thank the tenant for their long tenancy and commitment to the property; (2) Present the lease renewal offer — tenure options of 3 or 5 years, rental rate with a 2% annual escalation clause, landlord-funded fit-out contribution, and a 2-month rental-free fit-out period; (3) Explain the benefits of the renewed location — upcoming Penang development pipeline, improved facilities, and the REIT structure ensuring long-term investment in the asset; (4) Request a meeting in the next 2 weeks to discuss the terms; (5) Include a formal Acceptance of Offer section. Professional property formal tone. 600 words.\""
            },
            {
              title: "Rewrite investment pitch narrative for REIT IPO road show",
              prompt: "Open a new Word document. Ask Copilot: \"Write a compelling 1-page REIT IPO investor pitch narrative for Zava REIT, the proposed Bursa Malaysia REIT from Zava Properties. The pitch should: (1) Open with a compelling statement about the MYR 4.84 billion portfolio quality and defensive income characteristics; (2) Describe the asset quality — commercial assets in KL, Selangor, and Penang with a diversified tenant mix; (3) Present the REIT's income story — target distribution yield of 5.5 to 6.0%, stable occupancy; (4) Explain the growth story — Penang MYR 2.1 billion GDV pipeline as future asset injection; (5) End with a clear investment thesis: Zava REIT — quality Malaysian commercial property income with an ASEAN growth pipeline. Target audience: institutional fund managers. Maximum 400 words.\""
            },
            {
              title: "Draft REIT IPO feasibility approval memo to the Board",
              prompt: "Open a new Word document. Ask Copilot: \"Draft a formal Board approval memo seeking approval to proceed with the Zava REIT IPO process. The memo should cover: (1) Executive summary — the IPO rationale, proposed asset injection, and estimated proceeds; (2) Financial summary — portfolio NOI, target yield, implied IPO market capitalisation; (3) Risk assessment — anchor tenant lease risk, cap rate sensitivity, Malaysian REIT IPO market conditions; (4) Penang pipeline injection — timeline and financial impact; (5) Approvals sought: appoint investment banker, approve anchor tenant incentive budget, and authorise IPO prospectus preparation. Formal Board investment approval memo. 600 words.\""
            }
          ]
        },
        {
          tool: "🎯 Copilot in PowerPoint",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Create Zava REIT IPO investor road show deck",
              prompt: "Open a new PowerPoint. Ask Copilot: \"Create a 10-slide REIT IPO investor road show presentation for Zava REIT. Slide 1: Zava REIT — Quality Malaysian Commercial Property Income with ASEAN Growth. Slide 2: Investment Highlights — 5 key reasons to invest. Slide 3: Portfolio Overview — 6 assets, MYR 4.84B total value, occupancy, WALE. Slide 4: Asset-by-Asset Highlights — top 3 assets by value and income. Slide 5: Financial Performance — NOI, distributable income, distribution yield. Slide 6: Tenant Profile — diversified tenant mix, anchor tenants, sector breakdown. Slide 7: Growth Story — Penang MYR 2.1B GDV pipeline injection roadmap. Slide 8: Market Outlook — Malaysian commercial property and REIT market. Slide 9: Risk and Mitigation. Slide 10: Investment Summary. Clean institutional property tone.\""
            },
            {
              title: "Generate anchor tenant retention decision slides",
              prompt: "Open a new PowerPoint. Ask Copilot: \"Create a 4-slide internal Board decision slide deck for Zava Properties on the anchor tenant lease renewal decision. Slide 1: Anchor Tenant Renewal — December 2025 Lease Risk and Revenue Impact. Slide 2: The 2 anchor tenants — rental income contribution, lease history, and strategic importance to the REIT IPO. Slide 3: Renewal offer options — a cost-benefit table comparing Option A (full market rate) versus Option B (below-market incentive rate plus fit-out contribution). Slide 4: Board Recommendation — decision required and proposed approval timeline. Professional property Board presentation design.\""
            },
            {
              title: "Add Penang GDV pipeline and development programme slide",
              prompt: "In an open Zava Properties PowerPoint, add a new slide. Ask Copilot: \"Create a Penang GDV development programme slide. Include: (1) Penang project location map or district callout; (2) Project breakdown — GDV MYR 2.1 billion, total NLA or NFA in sq ft, development components; (3) Development timeline Gantt — from planning approval to construction start to phased completion; (4) Revenue and cashflow projection by year; (5) REIT injection timeline — when the Penang assets will be injected into Zava REIT. Title: Zava Properties — Penang MYR 2.1 Billion GDV Development Programme.\""
            }
          ]
        },
        {
          tool: "📧 Copilot in Outlook",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Triage anchor tenant lease expiry email and flag urgency",
              prompt: "Open Outlook and find an email from a commercial tenant or use Email_09_Risk_Committee_Prep.docx as a proxy — copy it and ask Copilot: \"I am the Zava Properties Asset Management Director and I have received an email from an anchor tenant about their December 2025 lease renewal. Summarise: (1) What specific lease terms they are requesting — rent, duration, fit-out; (2) Any concerns they have raised about the property or the REIT IPO; (3) The urgency level — December 2025 is approaching; (4) My 3 immediate action steps to respond. Maximum 150 words.\""
            },
            {
              title: "Draft property team asset management update email to CEO",
              prompt: "Open a new Outlook email. Ask Copilot: \"Draft a formal monthly asset management update email from Zava Properties' Asset Management Director to the Group CEO and CFO. The email should cover: (1) Occupancy summary — portfolio-level occupancy rate for all 6 assets; (2) Anchor tenant lease renewal status — 2 December 2025 leases, negotiation progress; (3) Rental income performance — month versus budget variance; (4) Penang GDV project — planning and approval status; (5) 3 decisions needed from the CEO this month. Professional property asset management tone. Under 300 words.\""
            },
            {
              title: "Copilot coaching on investor query email about REIT IPO",
              prompt: "In Outlook, type a rough draft to a fund manager: \"Thanks for your interest. The REIT IPO is progressing. We will share more details when we can. Regards, Zava Properties.\" Ask Copilot for coaching: \"I am a CEO of a Malaysian property company responding to an institutional investor who asked about our REIT IPO and the anchor tenant lease risk. Evaluate on: (1) Investor confidence — does it reassure the institutional fund manager; (2) Transparency — does it appropriately address the December 2025 anchor lease question without revealing confidential IPO information; (3) Tone — is it appropriately professional for an institutional investor communication. Rewrite at an investor relations professional standard with a specific follow-up meeting offer.\""
            }
          ]
        },
        {
          tool: "🎙 Copilot in Teams",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Catch up on missed REIT IPO and asset management meeting",
              prompt: "Open an existing Teams meeting that was recorded and has a Copilot recap from your calendar. Ask: \"I am the Zava Properties CEO and I missed this REIT IPO progress and asset management meeting. Catch me up: (1) What was the latest REIT IPO readiness assessment — investment banker feedback or SC discussion; (2) Was the anchor tenant lease renewal strategy agreed — what was the proposed rental concession or incentive package; (3) What did the team discuss about the Penang MYR 2.1 billion GDV project planning status; (4) Actions assigned to the CEO or myself; (5) Any portfolio KPI — occupancy, rental income — that was flagged as requiring attention.\""
            },
            {
              title: "Extract all asset management and REIT actions from meeting",
              prompt: "Open an existing recorded Teams meeting from your calendar. Ask: \"Extract all property asset management, REIT IPO, and Penang development action items from this meeting. Format as: Asset or Project; Action Type (Lease Renewal, IPO Prep, Development, Finance); Specific Action; Owner; Deadline; Priority — Critical if anchor tenant or IPO related, High if Penang project milestone, Normal for routine. Also note: was any target decision date for the anchor tenant lease incentive approved by the CEO?\""
            },
            {
              title: "Draft property team REIT IPO update email from meeting notes",
              prompt: "Open an existing recorded Teams meeting recap from your calendar. Ask: \"Draft a REIT IPO progress update email from the Zava Properties CFO to the Senior Management team of 8 property, finance, and legal managers. Based on this meeting: (1) REIT IPO process status — investment banker selection, SC consultation, IPO timeline; (2) Anchor tenant lease status; (3) Portfolio occupancy and NOI YTD versus budget; (4) Penang GDV project progress; (5) 30-day action priorities for each team. Professional property investment tone. Under 300 words.\""
            }
          ]
        },
        {
          tool: "📓 Copilot Notebook",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Build full REIT IPO feasibility brief from 2 documents",
              prompt: "Go to Copilot Notebook. Upload 14_Zava_Properties_Portfolio.xlsx and Email_09_Risk_Committee_Prep.docx (as a proxy for a REIT committee update). In Instructions: \"Using both documents, prepare a REIT IPO feasibility brief for the Zava Properties Board. (1) From the portfolio data — what is the total NOI, implied cap rate, WALE, and occupancy rate across all 6 assets; (2) From the committee document — what financial, legal, and market risks are flagged for the REIT IPO; (3) What is the revenue impact of the 2 anchor tenant lease expirations on the IPO valuation and distribution yield; (4) Build a REIT IPO decision checklist: what 10 conditions must be met before the Board can approve the IPO prospectus filing; (5) Recommend the optimal IPO timing given current Malaysian REIT market conditions.\"",
              fileRef: "14_Zava_Properties_Portfolio.xlsx, Email_09_Risk_Committee_Prep.docx"
            },
            {
              title: "Portfolio cash flow and GDV contribution analysis",
              prompt: "Go to Copilot Notebook. Upload 14_Zava_Properties_Portfolio.xlsx. In Instructions: \"Using the portfolio data, build a comprehensive cash flow and portfolio strategy analysis for the Zava Properties Board. (1) Total rental income by asset class — retail, office, industrial — for FY2022 to FY2024 with CAGR; (2) NOI by asset and portfolio WALE changes if all 6 December 2025 leases at risk are not renewed; (3) Penang MYR 2.1 billion GDV project contribution to Group revenue and EBITDA in Year 3 and Year 5; (4) Sensitivity analysis — how does a 50 basis point increase in cap rates affect the MYR 4.84 billion portfolio valuation; (5) The optimal capital structure for the Zava REIT — how much debt and equity to optimise distributable income. Format as a Board investment strategy paper.\"",
              fileRef: "14_Zava_Properties_Portfolio.xlsx"
            }
          ]
        },
        {
          tool: "🤝 Cowork (Pages)",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Build REIT IPO workstream tracker in Pages",
              prompt: "In Copilot Chat, upload 14_Zava_Properties_Portfolio.xlsx and ask for a REIT IPO readiness summary. Click Open in Copilot Pages. Ask: \"Reorganise this into a collaborative REIT IPO Workstream Tracker for the Zava Properties team of 8 property, finance, legal, and investor relations managers. Structure as: (1) Portfolio Readiness — asset valuations, legal title status, occupancy; (2) Regulatory Process — SC registration, Bursa listing application timeline; (3) Anchor Tenant Lease Tracker — 6 expiring leases, renewal status, incentive budget; (4) IPO Marketing Preparation — investor road show schedule, analyst briefing; (5) Penang GDV Pipeline Injection Timeline. Format for simultaneous editing by all 8 team members.\"",
              fileRef: "14_Zava_Properties_Portfolio.xlsx"
            },
            {
              title: "Build anchor tenant retention strategy canvas",
              prompt: "In Copilot Chat, upload 14_Zava_Properties_Portfolio.xlsx and ask for a lease expiry analysis. Click Open in Copilot Pages. Ask: \"Expand this into a collaborative Anchor Tenant Retention Strategy Canvas for the Zava Properties leasing team of 5 managers. Structure as: (1) Anchor Tenant Profile — each tenant, income contribution, lease history; (2) Renewal Offer Options — Option A full market rate versus Option B incentive terms; (3) Negotiation Status Log — latest discussion, tenant requirements, Zava response; (4) REIT IPO Impact Assessment — what lease renewal or non-renewal does to IPO valuation and yield; (5) Decision Timeline — dates by which the CEO must approve incentives. Format for real-time collaboration.\"",
              fileRef: "14_Zava_Properties_Portfolio.xlsx"
            }
          ]
        },
        {
          tool: "🤖 Word Agent",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Set up a Zava Properties REIT Advisor",
              prompt: "Open a Zava Properties strategy or REIT document — create one by asking Copilot to generate a REIT IPO executive summary and saving as Zava_Properties_REIT_Strategy.docx. Create an agent named Zava Properties REIT Advisor. Instructions: \"Answer questions about Zava Properties' commercial portfolio, REIT IPO strategy, and Penang GDV pipeline. Cite document sections. Under 150 words.\" Demo: type \"What is the portfolio WALE today and how does it change if both December 2025 anchor tenants do not renew?\""
            },
            {
              title: "Demo the REIT Advisor — IPO and portfolio queries",
              prompt: "With the agent active, ask 3 queries. Query 1: \"What is the target distribution yield for the Zava REIT IPO and what does that imply for the market capitalisation?\" Query 2: \"How does the Penang MYR 2.1 billion GDV pipeline strengthen the REIT growth story for institutional investors?\" Query 3: \"What is the Board decision timeline for approving the anchor tenant retention incentive budget?\""
            }
          ]
        },
        {
          tool: "🤖 PowerPoint Agent",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Set up a REIT IPO Road Show Coach agent",
              prompt: "Create or open the Zava REIT IPO investor road show PowerPoint from the PPT demo. Save as Zava_REIT_IPO_Roadshow_2025.pptx. Create an agent named REIT Road Show Coach. Instructions: \"Answer questions about Zava REIT's investment thesis, portfolio, and IPO terms. Reference slide numbers. Under 100 words.\" Demo: type \"Which slide addresses the anchor tenant lease expiry risk and what is the proposed mitigation?\""
            },
            {
              title: "Demo the REIT Road Show Coach — investor query rehearsal",
              prompt: "With the agent active, run 3 investor question rehearsals. Query 1: \"If an investor asks why two anchor tenants are leaving in December 2025, which slide covers this and what is the key message?\" Query 2: \"Which slide shows the Penang GDV pipeline and how does it translate into REIT distribution income growth?\" Query 3: \"An investor questions whether the target 5.5 to 6.0% yield is achievable given the lease risk — which slide addresses income stability and WALE?\""
            }
          ]
        },
        {
          tool: "🤖 Excel Agent",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Set up a Portfolio Analytics agent",
              prompt: "Open 14_Zava_Properties_Portfolio.xlsx. Create an agent named Zava Properties Portfolio Analyst. Instructions: \"Answer questions about Zava Properties' commercial portfolio, cap rates, rental income, and REIT IPO feasibility. Cite sheet names. Express all financial figures in MYR millions.\" Demo: type \"What is the total portfolio NOI for FY2024 and the implied cap rate on the MYR 4.84 billion portfolio value?\"",
              fileRef: "14_Zava_Properties_Portfolio.xlsx"
            },
            {
              title: "Demo the Portfolio Analyst — IPO and tenant queries",
              prompt: "With the agent active, run 3 queries. Query 1: \"What is the current WALE weighted by rental income and how does it change if the 2 December 2025 anchor tenants exit?\" Query 2: \"Which single asset has the highest cap rate and what does that imply about its relative risk compared to the rest of the portfolio?\" Query 3: \"What is the projected NOI contribution from the Penang MYR 2.1 billion GDV project in Year 3 based on current development assumptions?\"",
              fileRef: "14_Zava_Properties_Portfolio.xlsx"
            }
          ]
        }
      ]
    },
    {
      id: "bpo",
      name: "BPO & Shared Services",
      icon: "🖥️",
      color: "#1A3A5C",
      accent: "#8E44AD",
      company: "Zava BPO Services Sdn Bhd",
      tagline: "USD 98M ARR | 3,000+ FTE Bengaluru | Attrition 31.2%→24.8% | DOCUAI 99.8% | Bank Mandiri renewal",
      scenario: "Zava BPO Services Sdn Bhd is a Malaysian-headquartered Business Process Outsourcing company with over 3,000 full-time employees at its Bengaluru operations centre, serving banking, insurance, and financial services clients across Southeast Asia and India with USD 98 million in Annual Recurring Revenue. The company has made significant operational improvements — reducing Bengaluru attrition from 31.2% to 24.8% and improving DOCUAI AI document processing accuracy from 97.2% to 99.8% — and is positioning these as competitive differentiators against Infosys BPO in the strategic Bank Mandiri contract renewal. Group CEO Priya Subramaniam and COO Marcus Tan need Copilot to manage the Bank Mandiri renewal strategy, talent transformation programme, AI automation roadmap, and executive communication with BPO clients and the Board.",
      files: ["15_Zava_BPO_Operations.xlsx", "Email_09_Risk_Committee_Prep.docx"],
      prompts: [
        {
          tool: "🤖 Copilot Chat (Basic)",
          license: "Free — no M365 license needed",
          account: "Sasha Ouellet — SashaO@ABSx62256373.OnMicrosoft.com",
          prompts: [
            {
              title: "Explain BPO attrition and its commercial impact",
              prompt: "Ask Copilot: \"Explain employee attrition in the Business Process Outsourcing (BPO) industry and why it is a critical commercial and operational metric. Zava BPO Services has improved attrition from 31.2% to 24.8% at its Bengaluru operations centre but still targets sub-20%. Cover: (1) How BPO attrition is calculated — headcount exits in a year divided by average headcount; (2) The cost of each percentage point of attrition — hiring, training, productivity ramp, and client delivery risk; (3) Why Indian BPO operations have structurally higher attrition than Southeast Asian or Philippine BPO operations; (4) The talent retention levers that reduce BPO attrition most effectively; (5) Why a client like Bank Mandiri would benchmark its service provider attrition against Infosys. Maximum 250 words.\""
            },
            {
              title: "Brief me before the Bank Mandiri contract renewal negotiation",
              prompt: "Ask Copilot: \"I am the CEO of Zava BPO Services, a Malaysian-headquartered BPO company with 3,000+ FTE in Bengaluru and USD 98 million ARR. We are about to enter a contract renewal negotiation with Bank Mandiri, our largest banking client. Brief me on: (1) What Bank Mandiri will want to see improved — based on typical bank BPO KPIs: SLA compliance, first contact resolution, attrition rate, data security; (2) How to present our DOCUAI performance improvement (97.2% to 99.8% accuracy) as competitive differentiation; (3) How to address the Infosys comparison — they have lower attrition and more global scale; (4) The commercial levers I have — volume commitments, SLA penalties, gainsharing; (5) The 2 most important concessions to secure in the renewal. Maximum 200 words.\""
            },
            {
              title: "What is DOCUAI document processing and why does accuracy matter in banking?",
              prompt: "Ask Copilot: \"Explain AI-powered document processing (like DOCUAI) in BPO operations for banking clients. Zava BPO increased DOCUAI document processing accuracy from 97.2% to 99.8% for Bank Mandiri. Cover: (1) What document processing accuracy means in a banking BPO context — loan documents, trade finance, account opening; (2) Why 97.2% is insufficient for banking compliance and 99.8% is the industry SLA threshold; (3) How a 2.6 percentage point improvement in accuracy reduces error-related cost — each misprocessed document requires manual review; (4) How to quantify this improvement in a client contract renewal — cost savings and SLA penalty avoided; (5) Why AI document processing accuracy is increasingly a BPO contract differentiator versus labour arbitrage pricing alone. Maximum 250 words.\""
            }
          ]
        },
        {
          tool: "�� Researcher",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Research BPO industry talent and attrition benchmarks",
              prompt: "In Copilot Chat, switch to the Researcher agent. Upload 15_Zava_BPO_Operations.xlsx. Ask: \"Review Zava BPO's operations and attrition data. Then search the web for: India BPO industry attrition benchmarks for 2024 and 2025 — average, best-in-class, and sector-specific for banking and financial services BPO; talent retention strategies that reduced attrition in Indian BPO operations — specific programmes at Infosys BPO, Wipro, or HCL that demonstrate measurable results; the talent market in Bengaluru for multilingual financial services BPO — salary escalation, competitive dynamics; and how Malaysia-headquartered BPO companies compete for talent in India versus Indian BPO firms. Zava BPO reduced attrition from 31.2% to 24.8%. What are the 3 most effective interventions to reach sub-20% attrition? Cite all sources.\"",
              fileRef: "15_Zava_BPO_Operations.xlsx"
            },
            {
              title: "Research AI document processing and BPO automation trends",
              prompt: "In Copilot Chat, switch to the Researcher agent. Ask: \"Search the web for AI document processing and intelligent automation trends in banking BPO. Find: accuracy benchmarks for AI document processing in trade finance and account opening — what accuracy rates are clients demanding in 2025; competitive landscape for AI-powered BPO platforms — leading vendors, accuracy claims, and pricing models; how BPO companies are transitioning from labour arbitrage to AI augmentation as their value proposition; and how DOCUAI or similar solutions compare to Infosys AI Document Intelligence or Wipro Holmes. Zava BPO improved DOCUAI accuracy from 97.2% to 99.8%. What additional AI capability investments would strengthen Zava BPO's competitive position against Infosys?\""
            },
            {
              title: "Research Bank Mandiri and Indonesian banking BPO market",
              prompt: "In Copilot Chat, switch to the Researcher agent. Upload 15_Zava_BPO_Operations.xlsx. Ask: \"Review Zava BPO's client data including Bank Mandiri contract details. Then search the web for: Bank Mandiri's BPO and digital transformation strategy — public announcements about outsourcing or insourcing decisions; Indonesian banking sector BPO spending — market size and growth; how Indonesian banks manage BPO contract renewals — typical contract terms, SLA requirements, and pricing pressure; and Infosys BPO capabilities in Indonesia and its existing Bank Mandiri or Indonesian banking client relationships. Zava BPO faces Infosys competition in the Bank Mandiri renewal. What are the 3 competitive advantages Zava BPO should lead with in the renewal proposal? Cite all sources.\"",
              fileRef: "15_Zava_BPO_Operations.xlsx"
            }
          ]
        },
        {
          tool: "📊 Analyst",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Analyse Zava BPO operations and ARR KPIs",
              prompt: "In Copilot Chat, switch to the Analyst agent. Upload 15_Zava_BPO_Operations.xlsx. Ask: \"Analyse the full Zava BPO operations dataset. Calculate: (1) Total ARR by client and the top 3 clients as a percentage of total USD 98 million ARR; (2) Attrition cost at 31.2% versus 24.8% — assuming an average annual cost per BPO employee of USD 14,000 and a replacement cost of 50% of annual salary, what is the annual attrition cost saving from the improvement; (3) DOCUAI processing volume by client and the error rate reduction in absolute document numbers — how many fewer misprocessed documents at 99.8% versus 97.2%; (4) SLA compliance rate for all clients — which client has the lowest SLA compliance and what is the contractual penalty exposure; (5) Revenue at risk if Bank Mandiri moves to Infosys — what percentage of ARR does Bank Mandiri represent? Format as a BPO operations dashboard.\"",
              fileRef: "15_Zava_BPO_Operations.xlsx"
            },
            {
              title: "Analyse attrition cost and talent investment ROI",
              prompt: "In Copilot Chat, switch to the Analyst agent. Upload 15_Zava_BPO_Operations.xlsx. Ask: \"Build a talent investment ROI model for Zava BPO Bengaluru. (1) Calculate the total attrition cost at 31.2% versus 24.8% — hiring, training, productivity ramp, and client SLA penalty risk; (2) Model the cost of an additional talent retention investment of USD 2 million annually — what attrition reduction is required to make this ROI positive; (3) If attrition reaches sub-20%, what is the annual saving versus the current 24.8% rate; (4) For each 1 percentage point attrition improvement, what is the ROI in USD millions; (5) The 3 talent retention interventions — manager quality training, salary benchmarking, career pathing — and their estimated cost and attrition impact. Format as a CHRO and CFO talent investment paper.\"",
              fileRef: "15_Zava_BPO_Operations.xlsx"
            },
            {
              title: "Model Bank Mandiri renewal commercial terms and Infosys competitive analysis",
              prompt: "In Copilot Chat, switch to the Analyst agent. Upload 15_Zava_BPO_Operations.xlsx. Ask: \"Build a Bank Mandiri contract renewal commercial model. From the operations data: (1) Current Bank Mandiri ARR and the revenue impact of a 10% price reduction versus a volume increase commitment; (2) The DOCUAI accuracy improvement from 97.2% to 99.8% — quantify this in cost savings to Bank Mandiri in USD thousands per year; (3) An SLA gainsharing proposal — if DOCUAI accuracy is sustained above 99.5%, Zava BPO shares 20% of the additional efficiency savings with Bank Mandiri; (4) A comparison of Zava BPO versus Infosys on 5 dimensions: attrition, DOCUAI accuracy, SLA compliance, implementation risk of transition, and price; (5) The total economic value of renewal to Zava BPO over a 3-year contract term. Format as a contract renewal commercial decision paper.\"",
              fileRef: "15_Zava_BPO_Operations.xlsx"
            }
          ]
        },
        {
          tool: "📊 Copilot in Excel",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Instant Zava BPO operations executive summary",
              prompt: "Open 15_Zava_BPO_Operations.xlsx. Ask Copilot: \"Give me a plain-English executive summary of this BPO operations workbook. What is the total ARR? How many FTE in Bengaluru? What is the current attrition rate and DOCUAI accuracy? Which client has the Bank Mandiri contract renewal pending and what is their ARR contribution? Flag any client with SLA compliance below 98% or attrition above 25% in a service delivery unit. Format: 3-sentence BPO overview, then 4 flagged concerns with sheet and row reference.\"",
              fileRef: "15_Zava_BPO_Operations.xlsx"
            },
            {
              title: "Create ARR by client and SLA compliance chart",
              prompt: "Open 15_Zava_BPO_Operations.xlsx. Ask Copilot: \"Create a dual-axis bar and line chart for all Zava BPO clients. Bar chart (left axis): Annual Recurring Revenue in USD millions per client. Line chart (right axis): SLA compliance rate as percentage. Sort clients by ARR from highest to lowest. Add a horizontal dashed reference line at the 99% SLA target level. Label each bar with the client name and attrition rate for that service delivery unit. Highlight Bank Mandiri in red. Title: Zava BPO — ARR and SLA Compliance by Client FY2024.\"",
              fileRef: "15_Zava_BPO_Operations.xlsx"
            },
            {
              title: "Add attrition trend and cost impact column",
              prompt: "Open 15_Zava_BPO_Operations.xlsx. Navigate to the Service Delivery Units sheet. Ask Copilot: \"For each service delivery unit row, add two new columns: (1) Annual Attrition Cost — calculate the replacement cost as 50% of average annual salary per FTE multiplied by attrition rate multiplied by FTE headcount; and (2) SLA Penalty Risk — if SLA compliance is below 99%, mark Penalty Risk in orange; if below 98%, mark High Penalty Risk in red; if 99% or above, mark Compliant in green. Tell me the total annual attrition cost across all Bengaluru service delivery units at the current 24.8% rate.\"",
              fileRef: "15_Zava_BPO_Operations.xlsx"
            },
            {
              title: "Natural language query — ARR concentration and renewal risk",
              prompt: "Open 15_Zava_BPO_Operations.xlsx. Ask Copilot: \"Without navigating sheets, answer: (1) What is the total ARR and how much of it comes from the top 3 clients as a percentage; (2) What is the Bank Mandiri ARR and what percentage of total USD 98 million ARR does it represent; (3) What is the improvement in DOCUAI accuracy and what does that mean for annual error volumes at Bank Mandiri's document processing volumes; (4) What is the total attrition cost saving from reducing attrition from 31.2% to 24.8% assuming USD 14,000 average annual cost per BPO employee. Format as a 2-column BPO Q and A.\"",
              fileRef: "15_Zava_BPO_Operations.xlsx"
            }
          ]
        },
        {
          tool: "📝 Copilot in Word",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Summarise Zava BPO strategy for Board pre-read",
              prompt: "Open a new Word document. Ask Copilot: \"Draft a 1-page Board pre-read memo for Zava BPO Services covering FY2025 strategic priorities. Include: (1) Operations overview — 3,000+ FTE in Bengaluru, USD 98 million ARR, top 3 clients; (2) Talent transformation — attrition reduced from 31.2% to 24.8%, target sub-20%; (3) AI-powered differentiation — DOCUAI accuracy improved from 97.2% to 99.8%; (4) Commercial risk — Bank Mandiri renewal, Infosys competitive threat; (5) 2 Board decisions required: approve talent retention investment budget and authorise Bank Mandiri renewal negotiation mandate. Formal Board memo style. Maximum 400 words.\""
            },
            {
              title: "Draft Bank Mandiri contract renewal proposal",
              prompt: "Open a new Word document. Ask Copilot: \"Draft a formal BPO contract renewal proposal from Zava BPO Services CEO to Bank Mandiri VP Operations and Procurement. The proposal must: (1) Thank Bank Mandiri for the existing partnership and summarise the service improvements delivered; (2) Present the DOCUAI accuracy achievement — from 97.2% to 99.8% — and quantify the cost saving to Bank Mandiri; (3) Address the attrition improvement — 31.2% to 24.8% — and the operational continuity benefit; (4) Propose renewal terms — 3-year contract, volume commitment increase, SLA gainsharing for DOCUAI accuracy above 99.5%; (5) Include a comparison to Infosys on transition risk and implementation cost. Professional BPO contract proposal tone. 700 words.\""
            },
            {
              title: "Rewrite attrition reduction action plan for HR and operations",
              prompt: "Open a new Word document. Ask Copilot: \"Write a plain-language attrition reduction action plan for Zava BPO Bengaluru. The plan should cover 5 initiatives to reduce attrition from 24.8% to sub-20% over 12 months: (1) Manager quality training — 2-day leadership skills programme for all team leads managing 20+ agents; (2) Salary benchmarking — annual salary review cycle aligned to Bengaluru BPO market benchmarks; (3) Career pathing — structured promotion pathways from Agent to Specialist to Team Lead to Manager; (4) Recognition programme — monthly top performer awards with cash incentives; (5) Exit interview analytics — track and act on top 3 exit reasons monthly. Each initiative: 3 implementation steps, cost estimate in USD, and expected attrition reduction. 500 words.\""
            },
            {
              title: "Draft AI transformation roadmap memo to CTO and CDO",
              prompt: "Open a new Word document. Ask Copilot: \"Draft a formal memo from the Zava BPO CEO to the CTO and Chief Digital Officer outlining the AI and automation roadmap for FY2025 and FY2026. The memo must: (1) State the AI differentiation strategy — moving from labour arbitrage to AI-augmented BPO; (2) DOCUAI programme priorities — expand to 3 additional banking clients, target 99.9% accuracy across all clients; (3) Next automation investments — intelligent workflow routing for claims and trade finance; (4) Competitive positioning against Infosys — what AI capabilities Zava BPO must build to defend the Bank Mandiri account and win new banking clients; (5) Investment required in FY2025 and FY2026. 550 words, formal technology strategy memo format.\""
            }
          ]
        },
        {
          tool: "🎯 Copilot in PowerPoint",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Create BPO Board strategy presentation",
              prompt: "Open a new PowerPoint. Ask Copilot: \"Create a 7-slide Board strategy presentation for Zava BPO Services. Slide 1: Zava BPO — FY2025 Strategy and Performance Review. Slide 2: Operations Overview — Bengaluru headcount, ARR, client mix, key KPIs. Slide 3: Talent Transformation — attrition journey 31.2% to 24.8%, target sub-20%, key initiatives. Slide 4: AI-Powered Differentiation — DOCUAI accuracy 97.2% to 99.8%, automation roadmap. Slide 5: Commercial Performance — ARR MYR growth, top clients, renewal pipeline. Slide 6: Bank Mandiri Renewal — competitive analysis versus Infosys, proposed terms. Slide 7: Board Decisions Required — 2 approvals. Clean professional BPO blue and white design.\""
            },
            {
              title: "Generate Bank Mandiri renewal competitive analysis slides",
              prompt: "Open a new PowerPoint. Ask Copilot: \"Create a 4-slide internal Board competitive analysis presentation for the Bank Mandiri contract renewal decision. Slide 1: Bank Mandiri Account — Current Status and Renewal Stakes. Slide 2: Zava BPO versus Infosys — a 5-row comparison table: DOCUAI accuracy, attrition rate, SLA compliance, transition risk, and price. Slide 3: Renewal Proposal — contract terms, SLA gainsharing, volume commitment, and commercial offer. Slide 4: Recommendation — proceed with renewal on proposed terms, key negotiation red lines, and CEO mandate required. Professional competitive analysis Board design.\""
            },
            {
              title: "Add Bengaluru talent pipeline and attrition improvement slide",
              prompt: "In an open Zava BPO PowerPoint, add a new slide. Ask Copilot: \"Create a Bengaluru talent pipeline and attrition improvement slide. Include: (1) A line chart showing monthly attrition rate from January 2023 to December 2024 — from 31.2% peak down to 24.8%; (2) The 5 talent retention initiatives and their implementation dates as callout annotations on the timeline; (3) The 12-month projection to reach sub-20% attrition with a shaded target zone; (4) Cost of attrition at 31.2% versus 24.8% versus target 20% in USD millions per year. Title: Zava BPO — Bengaluru Talent Transformation 2023–2025.\""
            }
          ]
        },
        {
          tool: "📧 Copilot in Outlook",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Triage Bank Mandiri RFP or contract renewal email",
              prompt: "Open Outlook and find an email from a major client or use Email_09_Risk_Committee_Prep.docx as a proxy — copy it and ask Copilot: \"I am the Zava BPO CEO and I have received a formal contract renewal or RFP email from Bank Mandiri. Summarise: (1) What Bank Mandiri is asking for — is it a renewal of existing terms, a rebid, or an RFP with new scope; (2) What performance concerns they have raised — attrition, SLA, DOCUAI accuracy; (3) The decision timeline — when must we respond; (4) My 3 immediate actions to prepare the renewal proposal. Maximum 150 words.\""
            },
            {
              title: "Draft BPO quarterly business review email to Bank Mandiri",
              prompt: "Open a new Outlook email. Ask Copilot: \"Draft a formal BPO quarterly business review email from Zava BPO Services Client Success Director to Bank Mandiri VP Operations. The email should cover: (1) Q4 2024 SLA performance — compliance rate against all contracted SLA metrics; (2) DOCUAI document processing accuracy for Q4 2024 — improvement to 99.8% and volume processed; (3) Staffing update — attrition at 24.8%, down from 31.2%, team stability improvement; (4) Service improvement initiatives launched this quarter; (5) Agenda proposal for the renewal negotiation meeting next month. Professional BPO client management tone. Under 300 words.\""
            },
            {
              title: "Copilot coaching on internal update email about Infosys threat",
              prompt: "In Outlook, type a rough internal draft: \"Team, we heard Bank Mandiri is talking to Infosys. We need to respond ASAP. Thoughts?\" Ask Copilot for coaching: \"I am the CEO of Zava BPO Services and I sent this message to my senior leadership team. Evaluate on: (1) Strategic clarity — does it communicate the seriousness of the competitive threat without causing panic; (2) Call to action — does it direct the team to specific urgent actions; (3) Tone — is it appropriate for a CEO communication to a senior leadership team. Rewrite as a clear, urgent internal leadership communication with 3 specific action assignments and a 48-hour response deadline.\""
            }
          ]
        },
        {
          tool: "🎙 Copilot in Teams",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Catch up on missed Bank Mandiri renewal strategy meeting",
              prompt: "Open an existing Teams meeting that was recorded and has a Copilot recap from your calendar. Ask: \"I am the Zava BPO CEO and I missed this Bank Mandiri renewal strategy meeting. Catch me up: (1) What was the latest Bank Mandiri feedback — are they actively evaluating Infosys or just using it as leverage; (2) What renewal terms did the team propose — pricing, SLA, DOCUAI gainsharing; (3) Was the attrition improvement data presented to Bank Mandiri and what was their reaction; (4) Actions assigned to me or the CEO office; (5) What is the current probability assessment of a successful renewal?\""
            },
            {
              title: "Extract BPO client and operations actions from meeting",
              prompt: "Open an existing recorded Teams meeting from your calendar. Ask: \"Extract all client management, operations, talent, and AI transformation action items from this BPO strategy meeting. Format as: Account or Workstream; Action Type (Client, Talent, AI, Finance); Specific Action; Owner; Deadline; Priority — Critical if Bank Mandiri or ARR at risk, High if attrition target related, Normal for routine. Also note: was any CEO decision required on the Bank Mandiri negotiation mandate and what was the conclusion?\""
            },
            {
              title: "Draft BPO senior leadership update email from meeting notes",
              prompt: "Open an existing recorded Teams meeting recap from your calendar. Ask: \"Draft a BPO leadership update email from the Zava BPO CEO to the senior leadership team of 10 operations, commercial, HR, and technology managers. Based on this meeting: (1) Bank Mandiri renewal strategy — our position and the competitive threat from Infosys; (2) Attrition programme update — current rate, initiative status, and path to sub-20%; (3) DOCUAI expansion plan — which clients to target next; (4) ARR growth pipeline — new client opportunities; (5) 30-day action priorities. Professional BPO leadership communication. Under 300 words.\""
            }
          ]
        },
        {
          tool: "📓 Copilot Notebook",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Full BPO competitive brief from 2 operations documents",
              prompt: "Go to Copilot Notebook. Upload 15_Zava_BPO_Operations.xlsx and Email_09_Risk_Committee_Prep.docx (as a proxy for a client risk update). In Instructions: \"Using both documents, prepare a comprehensive BPO competitive intelligence brief for the Zava BPO CEO. (1) From the operations data — what is the Bank Mandiri ARR and what percentage of total ARR does it represent; (2) From the email or update document — what commercial or operational concerns are flagged; (3) What is the total revenue at risk if Bank Mandiri moves to Infosys — calculate 12-month ARR impact; (4) Build a Bank Mandiri renewal preparation checklist — the 8 steps to complete in the next 4 weeks; (5) Identify the single most compelling differentiation point Zava BPO has over Infosys for this specific client.\"",
              fileRef: "15_Zava_BPO_Operations.xlsx, Email_09_Risk_Committee_Prep.docx"
            },
            {
              title: "Attrition and AI transformation programme analysis",
              prompt: "Go to Copilot Notebook. Upload 15_Zava_BPO_Operations.xlsx. In Instructions: \"Using the operations data, build a comprehensive talent and AI transformation analysis for the Zava BPO Board. (1) Calculate the total Bengaluru attrition cost at 31.2% versus 24.8% versus 20% target — what is the annual saving if the target is achieved; (2) Model the ROI of a USD 2 million talent retention investment — how many percentage points of attrition reduction are needed to break even in Year 1; (3) DOCUAI expansion economics — if DOCUAI accuracy improvement is replicated across 3 additional clients at similar volume, what is the annual SLA penalty avoided and gainsharing revenue; (4) Build a 2-year AI roadmap showing which automation investments deliver the highest ROI; (5) Recommend the single most important investment for the FY2025 Board to approve. Format as a Board AI strategy paper.\"",
              fileRef: "15_Zava_BPO_Operations.xlsx"
            }
          ]
        },
        {
          tool: "🤝 Cowork (Pages)",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Build Bank Mandiri renewal workstream tracker in Pages",
              prompt: "In Copilot Chat, upload 15_Zava_BPO_Operations.xlsx and ask for a Bank Mandiri account and renewal summary. Click Open in Copilot Pages. Ask: \"Reorganise this into a collaborative Bank Mandiri Contract Renewal Workstream Tracker for the Zava BPO commercial and operations team of 8 managers. Structure as: (1) Commercial Proposal Tracker — pricing, SLA gainsharing, volume commitment status; (2) Competitive Intelligence Log — Infosys capabilities, Bank Mandiri evaluation criteria, our differentiation; (3) Operations Evidence Pack — DOCUAI accuracy data, SLA compliance records, attrition trend; (4) Negotiation Timeline — decision dates and internal approval milestones; (5) Risk Register — scenarios if Bank Mandiri moves to Infosys. Format for simultaneous editing by all 8 team members.\"",
              fileRef: "15_Zava_BPO_Operations.xlsx"
            },
            {
              title: "Build talent transformation programme canvas",
              prompt: "In Copilot Chat, upload 15_Zava_BPO_Operations.xlsx and ask for an attrition and talent summary. Click Open in Copilot Pages. Ask: \"Expand this into a collaborative Talent Transformation Programme Canvas for the Zava BPO Bengaluru HR and Operations team of 6 managers. Structure as: (1) Attrition Tracker — monthly rate by service delivery unit, target, and trend; (2) Retention Initiative Status — 5 initiatives with completion percentage and impact estimate; (3) Exit Interview Analytics — top 3 exit reasons by team and month; (4) Salary Benchmarking Tracker — current vs Bengaluru BPO market for 4 job grades; (5) Manager Quality Scorecard — team lead NPS and team attrition for each of 12 team leads. Format for real-time daily editing.\"",
              fileRef: "15_Zava_BPO_Operations.xlsx"
            }
          ]
        },
        {
          tool: "🤖 Word Agent",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Set up a Zava BPO Strategy Advisor",
              prompt: "Open a Zava BPO strategy document — create one by asking Copilot to generate a Bank Mandiri renewal executive strategy summary and saving as Zava_BPO_Renewal_Strategy.docx. Create an agent named Zava BPO Strategy Advisor. Instructions: \"Answer questions about Zava BPO's client operations, attrition improvement, DOCUAI performance, and Bank Mandiri renewal strategy. Cite document sections. Under 150 words.\" Demo: type \"What is the single most compelling competitive advantage Zava BPO has over Infosys for the Bank Mandiri renewal?\""
            },
            {
              title: "Demo the BPO Strategy Advisor — renewal and talent queries",
              prompt: "With the agent active, ask 3 queries. Query 1: \"What is the Bank Mandiri ARR and how does it change if we offer a 5% price reduction to retain the contract for 3 years?\" Query 2: \"What is the DOCUAI accuracy improvement story — how should we present the 97.2% to 99.8% improvement to Bank Mandiri in the renewal meeting?\" Query 3: \"What is the sub-20% attrition target timeline and what talent investment is needed to achieve it?\""
            }
          ]
        },
        {
          tool: "🤖 PowerPoint Agent",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Set up a BPO Board Strategy Presenter agent",
              prompt: "Create or open the Zava BPO Board strategy PowerPoint. Save as Zava_BPO_Strategy_2025.pptx. Create an agent named BPO Strategy Coach. Instructions: \"Answer questions about Zava BPO's strategy, Bank Mandiri renewal, and talent transformation programme. Reference slide numbers. Under 100 words.\" Demo: type \"Which slide covers the Bank Mandiri versus Infosys competitive comparison and what is the key differentiator we lead with?\""
            },
            {
              title: "Demo the BPO Strategy Coach — Board and client queries",
              prompt: "With the agent active, run 3 queries. Query 1: \"If the Board asks why Zava BPO should invest in talent retention when attrition is already down, which slide shows the cost-benefit case?\" Query 2: \"Which slide shows the DOCUAI accuracy improvement and how does it translate into client value?\" Query 3: \"What slide addresses the transition risk if Bank Mandiri switches to Infosys and how do we quantify the switching cost for the client?\""
            }
          ]
        },
        {
          tool: "🤖 Excel Agent",
          license: "M365 Copilot",
          account: "MOD Administrator — admin@ABSx62256373.onmicrosoft.com",
          prompts: [
            {
              title: "Set up a BPO Operations Analytics agent",
              prompt: "Open 15_Zava_BPO_Operations.xlsx. Create an agent named Zava BPO Operations Analyst. Instructions: \"Answer questions about Zava BPO's ARR, attrition, SLA compliance, and DOCUAI performance. Cite sheet names. Express ARR in USD millions and attrition as a percentage.\" Demo: type \"What is the total ARR for FY2024 and what percentage does Bank Mandiri contribute?\"",
              fileRef: "15_Zava_BPO_Operations.xlsx"
            },
            {
              title: "Demo the Operations Analyst — client and talent queries",
              prompt: "With the agent active, run 3 queries. Query 1: \"What is the annual attrition cost saving from reducing Bengaluru attrition from 31.2% to 24.8% at a USD 14,000 average annual cost per employee and 50% replacement cost?\" Query 2: \"Which client has the lowest SLA compliance rate and what is the contractual penalty exposure in USD thousands per month?\" Query 3: \"What is the DOCUAI accuracy improvement from 97.2% to 99.8% worth in terms of misprocessed documents avoided annually at Bank Mandiri's estimated daily volume?\"",
              fileRef: "15_Zava_BPO_Operations.xlsx"
            }
          ]
        }
      ]
    }
  ]
};
