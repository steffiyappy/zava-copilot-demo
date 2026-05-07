import sys; sys.path.insert(0,'.')
from util import *

INDUSTRIES_7 = [

    {
      'id': 'property-reit',
      'sectorId': 'property',
      'name': 'Property & REIT',
      'icon': '🏢',
      'color': '#1565C0',
      'accent': '#1976D2',
      'company': 'Aman Jaya Property Berhad',
      'tagline': 'Anchor lease rollover threatens REIT launch valuation.',
      'companyID': 'PT Graha Aman Jaya Tbk',
      'taglineID': 'Jakarta occupancy softness clouds the dual-market story.',
      'scenario': 'Aman Jaya Property Berhad manages office, logistics, and mixed-use assets in Malaysia while PT Graha Aman Jaya Tbk operates office and retail assets in Indonesia. The group wants a 2026 REIT launch, but a major Kuala Lumpur anchor lease sits inside the risk window, Jakarta occupancy is softening, and refinancing must stay within covenant guardrails. Management needs a cross-border view of valuation, occupancy, and debt resilience before locking the final asset injection perimeter.',
      'files': ['PROP_01_Portfolio_Performance.xlsx', 'PROP_02_Asset_Management_Policy.docx', 'PROP_03_Development_Brief.docx'],
      'prompts': [
        {
          'tool': '🤖 Copilot Chat (Basic)',
          'license': 'Free — no M365 Copilot license needed',
          'account': 'Sasha Ouellet — SashaO@ABSx62256373.OnMicrosoft.com',
          'prompts': [
            'You are the Chief Investment Officer at Aman Jaya Property Berhad. Using PROP_01_Portfolio_Performance.xlsx, focus on the Asset NAV Summary, Rental Yield Tracker, and Debt Covenant Monitor sheets to assess an anchor-tenant rollover, softer occupancy, and covenant sensitivity ahead of a REIT launch. Quantify the immediate downside, name the 3 decisions management must take in the next 30 days, and present the answer as a RAG table with Red, Amber, and Green actions.',
            'You are the Head of Asset Management at Aman Jaya Property Berhad. Using the Occupancy Dashboard and Development Pipeline sheets in PROP_01_Portfolio_Performance.xlsx together with PROP_02_Asset_Management_Policy.docx, explain how the current operating issue affects strategy, capital allocation, and stakeholder confidence. Present the response as a RAG memo with sections for What We Know, What We Do Not Yet Know, and What We Should Do Next.',
            'You are the Chief Financial Officer at Aman Jaya Property Berhad. Using the Asset NAV Summary and Occupancy Dashboard sheets in PROP_01_Portfolio_Performance.xlsx, benchmark our current position against the 2024 to 2025 Malaysian and Indonesian commercial property and REIT market. Summarise the 5 most important leading indicators to watch over the next 2 quarters and show them in a RAG scorecard with a short management implication beside each.'
          ]
        },
        {
          'tool': '🔍 Researcher',
          'license': 'Free — no M365 Copilot license needed',
          'account': 'Sasha Ouellet — SashaO@ABSx62256373.OnMicrosoft.com',
          'desc': 'Access via Microsoft 365 Copilot Chat > Agents > Researcher. Researcher automatically critiques every source — verifying claims against the original before including them in the report. Grounds answers in live web sources and your organisation\'s data with full citations. Faster and more reliable than manual research.',
          'prompts': [
            'You are the Head of Asset Management at Aman Jaya Property Berhad. Using PROP_01_Portfolio_Performance.xlsx, especially the Asset NAV Summary, Rental Yield Tracker, and Occupancy Dashboard sheets, plus PROP_02_Asset_Management_Policy.docx, research 2024 to 2025 market benchmarks, peer disclosures, and financing or valuation signals relevant to an anchor-tenant rollover, softer occupancy, and covenant sensitivity ahead of a REIT launch. Present a RAG table with Red for immediate threats, Amber for watchlist items, and Green for supporting market signals, with citations to every source and a one-line implication for management. Flag any claim that could not be independently verified.',
            'You are the Chief Investment Officer at Aman Jaya Property Berhad. Using the Development Pipeline and Debt Covenant Monitor sheets in PROP_01_Portfolio_Performance.xlsx and the policy positions in PROP_03_Development_Brief.docx, research how DBKL, NAPIC, and OJK or comparable published authorities and industry bodies are treating this issue across Malaysia and Indonesia. Separate mandatory requirements from market practice, cite each source, and present the findings as a RAG matrix with columns for Issue, Malaysia, Indonesia, Timing, and Management Action. Flag any claim that could not be independently verified.',
            'You are the Chief Financial Officer at Aman Jaya Property Berhad. Using the Asset NAV Summary, Occupancy Dashboard, and Development Pipeline sheets in PROP_01_Portfolio_Performance.xlsx, research the demand, pricing, and competitor trends that will most influence our next 12 months. Present the answer as a RAG table ranking the top 10 external signals by likely impact and management preparedness, with citations beside every row. Flag any claim that could not be independently verified.'
          ]
        },
        {
          'tool': '📊 Analyst',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'desc': 'Access via Microsoft 365 Copilot Chat > click Agents > Analyst. Upload an Excel or CSV file. Analyst runs Python-style analysis, builds charts, and interprets results without you writing a single formula.',
          'prompts': [
            'You are the Chief Financial Officer at Aman Jaya Property Berhad. Upload PROP_01_Portfolio_Performance.xlsx to Analyst and use the Asset NAV Summary, Rental Yield Tracker, and Occupancy Dashboard sheets to identify the 5 biggest sources of underperformance or stress in the current plan. Quantify the variance where possible, flag each item Red, Amber, or Green based on financial materiality, and end with one corrective action per Red item.',
            'You are the Chief Investment Officer at Aman Jaya Property Berhad. Upload PROP_01_Portfolio_Performance.xlsx to Analyst and use the Development Pipeline and Debt Covenant Monitor sheets to model 3 scenarios for an anchor-tenant rollover, softer occupancy, and covenant sensitivity ahead of a REIT launch: downside, base case, and recovery case. Show the impact on revenue, margin or cash, plus the operational trigger that would move an item from Amber to Red.',
            'You are the Head of Asset Management at Aman Jaya Property Berhad. Upload PROP_01_Portfolio_Performance.xlsx to Analyst and use the Asset NAV Summary, Occupancy Dashboard, and Debt Covenant Monitor sheets to build a 13-week watchlist of the metrics most likely to surprise management. Present the output as a RAG dashboard table with columns for Metric, Current Level, Threshold, Risk Status, and Recommended Owner.'
          ]
        },
        {
          'tool': '📊 Copilot in Excel',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'prompts': [
            'You are the Head of Asset Management at Aman Jaya Property Berhad. Using PROP_01_Portfolio_Performance.xlsx, build a new sheet called \'Aman Jaya Property Executive Dashboard\' from the Asset NAV Summary, Rental Yield Tracker, and Occupancy Dashboard sheets. Show the 10 most important KPIs, add a RAG status column driven by clear thresholds, and place an executive summary box at the top that updates automatically.',
            'You are the Chief Investment Officer at Aman Jaya Property Berhad. Using PROP_01_Portfolio_Performance.xlsx, create a risk tracker that pulls from the Rental Yield Tracker, Development Pipeline, and Debt Covenant Monitor sheets. For each material issue, show owner, due date, estimated financial exposure, and Red/Amber/Green status, then sort Red issues first.',
            'You are the Chief Financial Officer at Aman Jaya Property Berhad. Using PROP_01_Portfolio_Performance.xlsx, build a scenario sensitivity sheet using the Asset NAV Summary, Occupancy Dashboard, and Debt Covenant Monitor sheets as inputs. Show downside, base, and upside cases side by side, add conditional formatting for RAG thresholds, and include a short note on the trigger that would require management escalation.'
          ]
        },
        {
          'tool': '📝 Copilot in Word',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'prompts': [
            'You are the Chief Investment Officer at Aman Jaya Property Berhad. Using PROP_02_Asset_Management_Policy.docx together with the Asset NAV Summary and Debt Covenant Monitor sheets in PROP_01_Portfolio_Performance.xlsx, draft a 2-page Board paper on an anchor-tenant rollover, softer occupancy, and covenant sensitivity ahead of a REIT launch. Structure it as Situation, Risks, Decisions Required, and Next 30 Days, and place a compact RAG summary at the top.',
            'You are the Head of Asset Management at Aman Jaya Property Berhad. Using PROP_03_Development_Brief.docx and the Rental Yield Tracker and Development Pipeline sheets in PROP_01_Portfolio_Performance.xlsx, draft a policy or action-plan note for the leadership team that translates the data into clear operating actions. Present the recommendations as a RAG table with owners, timing, and expected impact.',
            'You are the Chief Financial Officer at Aman Jaya Property Berhad. Using PROP_02_Asset_Management_Policy.docx, PROP_03_Development_Brief.docx, and the Asset NAV Summary sheet in PROP_01_Portfolio_Performance.xlsx, draft an external stakeholder briefing note that explains our position factually and shows what management is doing next. After the draft, add a 3-line RAG risk summary covering timing, evidence strength, and stakeholder reaction.'
          ]
        },
        {
          'tool': '🎯 Copilot in PowerPoint',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'prompts': [
            'You are the Chief Investment Officer at Aman Jaya Property Berhad. Create a 6-slide executive deck using PROP_01_Portfolio_Performance.xlsx and PROP_02_Asset_Management_Policy.docx, grounded in the Asset NAV Summary, Occupancy Dashboard, and Debt Covenant Monitor sheets. Cover property & reit performance, root causes, key risks, management response, scenario outlook, and decisions required, with one headline takeaway per slide and a visible RAG status marker.',
            'You are the Head of Asset Management at Aman Jaya Property Berhad. Create a 3-slide operating review using the Rental Yield Tracker, Occupancy Dashboard, and Development Pipeline sheets in PROP_01_Portfolio_Performance.xlsx. Show what is Red, what is Amber, and what is Green, then close with the 5 highest-priority actions and owners.',
            'You are the Chief Financial Officer at Aman Jaya Property Berhad. Build a 2-slide stakeholder briefing from PROP_01_Portfolio_Performance.xlsx and PROP_03_Development_Brief.docx, using the Asset NAV Summary and Debt Covenant Monitor sheets as the fact base. The first slide should summarise the issue and the second should show the recovery path in a RAG timeline.'
          ]
        },
        {
          'tool': '📧 Copilot in Outlook',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'prompts': [
            'You are the Chief Investment Officer at Aman Jaya Property Berhad. Using the Asset NAV Summary and Debt Covenant Monitor sheets in PROP_01_Portfolio_Performance.xlsx, draft an email to lead banks and cornerstone investors explaining the current situation, the evidence supporting our view, and the immediate next step we want from them. After the draft, add a short RAG summary of delivery risk, likely objections, and follow-up timing.',
            'You are the Head of Asset Management at Aman Jaya Property Berhad. Using the Occupancy Dashboard and Development Pipeline sheets in PROP_01_Portfolio_Performance.xlsx plus PROP_02_Asset_Management_Policy.docx, draft a regulator-ready note for DBKL, NAPIC, and OJK or the most relevant authority. Keep the tone factual, distinguish confirmed facts from assumptions, and end with a RAG table of issues that may require further disclosure.',
            'You are the Chief Financial Officer at Aman Jaya Property Berhad. Using the Asset NAV Summary, Rental Yield Tracker, and Occupancy Dashboard sheets in PROP_01_Portfolio_Performance.xlsx, draft an internal leadership email that aligns owners around the top 5 actions for the next 14 days. Finish with a RAG checklist titled Do Today, Do This Week, and Monitor.'
          ]
        },
        {
          'tool': '🎙 Copilot in Teams',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'desc': 'Use your OWN existing recorded Teams meetings. Open a meeting recap in Teams > Recap tab. Copilot generates summaries, action items, and follow-up drafts grounded in the actual transcript.',
          'prompts': [
            'You are the Head of Asset Management at Aman Jaya Property Berhad. Using this recorded Teams meeting recap and the Asset NAV Summary and Occupancy Dashboard sheets in PROP_01_Portfolio_Performance.xlsx as the operating benchmark, extract all decisions, risks, and unresolved items related to an anchor-tenant rollover, softer occupancy, and covenant sensitivity ahead of a REIT launch. Present the result as a RAG table with owners and due dates.',
            'You are the Chief Investment Officer at Aman Jaya Property Berhad. Using the Rental Yield Tracker and Debt Covenant Monitor sheets in PROP_01_Portfolio_Performance.xlsx as reference points, draft follow-up actions from the meeting grouped by Leasing | Capital Markets | Development | Treasury | Legal. For each action, include owner, deadline, and whether the item is Red, Amber, or Green.',
            'You are the Chief Financial Officer at Aman Jaya Property Berhad. Using this meeting recap and the Development Pipeline sheet in PROP_01_Portfolio_Performance.xlsx as context, identify whether any comments suggest hidden downside not yet reflected in management reporting. Summarise the findings as a RAG note with direct quotes or paraphrased evidence from the recap.'
          ]
        },
        {
          'tool': '📓 Copilot Notebook',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'desc': 'Access via copilot.microsoft.com > Notebook tab. Upload up to 5 files and set a system instruction. Best for synthesising insights across multiple documents simultaneously.',
          'prompts': [
            'You are the Chief Investment Officer at Aman Jaya Property Berhad. Upload PROP_01_Portfolio_Performance.xlsx, PROP_02_Asset_Management_Policy.docx, and PROP_03_Development_Brief.docx to Copilot Notebook and focus on the Asset NAV Summary, Occupancy Dashboard, and Debt Covenant Monitor sheets. Ask Notebook to produce a cross-file RAG synthesis of the top risks, the 3 most credible management actions, and the evidence supporting each recommendation, citing the source file for every major point.',
            'You are the Head of Asset Management at Aman Jaya Property Berhad. Upload PROP_01_Portfolio_Performance.xlsx and PROP_02_Asset_Management_Policy.docx to Copilot Notebook and focus on the Rental Yield Tracker, Development Pipeline, and Debt Covenant Monitor sheets. Ask Notebook to model a downside scenario for an anchor-tenant rollover, softer occupancy, and covenant sensitivity ahead of a REIT launch, explain which assumptions matter most, and present the answer as a RAG table with immediate, next-quarter, and monitor-only actions.',
            'You are the Chief Financial Officer at Aman Jaya Property Berhad. Upload PROP_01_Portfolio_Performance.xlsx, PROP_02_Asset_Management_Policy.docx, and PROP_03_Development_Brief.docx to Copilot Notebook and focus on the Asset NAV Summary, Rental Yield Tracker, and Development Pipeline sheets. Ask Notebook to rank the top 5 opportunities to stabilise performance without creating new compliance or stakeholder risk, and return the answer as a RAG prioritisation table with expected impact and implementation difficulty.'
          ]
        },
        {
          'tool': '🤝 Cowork (Frontier)',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'desc': 'Cowork is an autonomous agent that takes actions across Microsoft 365 on your behalf — sending emails, scheduling meetings, creating documents, posting in Teams, and scheduling recurring tasks. Access: m365.cloud.microsoft > left nav > Agents > Cowork. Requires Frontier program enrollment.',
          'prompts': [
            'You are the Chief Investment Officer at Aman Jaya Property Berhad. Using PROP_01_Portfolio_Performance.xlsx, PROP_02_Asset_Management_Policy.docx, and PROP_03_Development_Brief.docx, especially the Asset NAV Summary, Occupancy Dashboard, and Debt Covenant Monitor sheets, research the current market context, draft a 2-page management brief, save it to OneDrive, and email it to the leadership team for review. Then schedule a 30-minute follow-up meeting for next week and label the agenda items Red, Amber, and Green.',
            'You are the Head of Asset Management at Aman Jaya Property Berhad. Using the Rental Yield Tracker, Development Pipeline, and Debt Covenant Monitor sheets in PROP_01_Portfolio_Performance.xlsx, prepare a task tracker, draft the related stakeholder email, store both in SharePoint or OneDrive, and send them to the named owners. Then book a checkpoint meeting and make sure the work is grouped by Leasing | Capital Markets | Development | Treasury | Legal with clear RAG priorities.'
          ]
        },
        {
          'tool': '✏️ Edit with Copilot',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'desc': 'Edit with Copilot is an agentic mode in Word, Excel, and PowerPoint (web) that executes multi-step editing tasks across your entire document in one instruction — reformatting, restructuring, building formulas, generating new sections. Access: open any Office file in browser > Copilot pane > Edit with Copilot. Requires M365 Copilot licence.',
          'prompts': [
            'You are the Chief Investment Officer at Aman Jaya Property Berhad. Using PROP_02_Asset_Management_Policy.docx in Word for the web and the Asset NAV Summary and Debt Covenant Monitor sheets in PROP_01_Portfolio_Performance.xlsx as the fact base, add a new section that sharpens the narrative around an anchor-tenant rollover, softer occupancy, and covenant sensitivity ahead of a REIT launch. Restructure the content into Situation, Key Data, Decisions, and Next Steps, and insert a small RAG summary box at the top.',
            'You are the Chief Financial Officer at Aman Jaya Property Berhad. Using PROP_01_Portfolio_Performance.xlsx in Excel for the web, redesign the sheets fed by Rental Yield Tracker, Occupancy Dashboard, and Debt Covenant Monitor so executives can see the highest-risk items first. Standardise labels, improve formulas where needed, and add a RAG status column plus a one-row summary that updates automatically.'
          ]
        },
        {
          'tool': '🤖 Word Agent',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'desc': 'Create a declarative agent scoped to a Word document. Open the .docx in Word for Web > Copilot pane > + New Agent > name it, write a description, set the document as knowledge source > Share. Colleagues chat with it in Teams or M365 Copilot.',
          'prompts': [
            'You are the Head of Asset Management at Aman Jaya Property Berhad. Open PROP_02_Asset_Management_Policy.docx in Word for Web and create an agent called \'Aman Jaya Property Word Guide\'. Describe it as an assistant that answers questions using PROP_02_Asset_Management_Policy.docx plus the Asset NAV Summary and Occupancy Dashboard sheets in PROP_01_Portfolio_Performance.xlsx, then share it with the relevant leadership team.',
            'You are the Chief Financial Officer at Aman Jaya Property Berhad. Demo the \'Aman Jaya Property Word Guide\' agent by asking: \'What is our most urgent operating risk, what evidence from the Rental Yield Tracker and Debt Covenant Monitor sheets supports it, and what action does PROP_02_Asset_Management_Policy.docx imply we should take first?\'. Show the answer as a short RAG response with the supporting source references.'
          ]
        },
        {
          'tool': '🤖 PowerPoint Agent',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'desc': 'Create a declarative agent scoped to a PowerPoint presentation. Great for strategy decks or Board presentations many people need to reference. Same setup as Word Agent but using a .pptx file.',
          'prompts': [
            'You are the Chief Investment Officer at Aman Jaya Property Berhad. Create the leadership presentation in PowerPoint for Web using PROP_01_Portfolio_Performance.xlsx and PROP_03_Development_Brief.docx, then create an agent called \'Aman Jaya Property Deck Navigator\'. Tell users it can answer questions tied to the Asset NAV Summary, Development Pipeline, and Debt Covenant Monitor sheets, then share it with the executive team.',
            'You are the Head of Asset Management at Aman Jaya Property Berhad. Demo the \'Aman Jaya Property Deck Navigator\' agent by asking: \'Which slide best explains our Red risks, what does the Debt Covenant Monitor sheet say about exposure, and what decision do leaders need this week?\'. Request a RAG answer in under 120 words.'
          ]
        },
        {
          'tool': '🤖 Excel Agent',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'desc': 'Create a declarative agent scoped to an Excel workbook. Colleagues ask data questions in plain English without opening Excel. Open .xlsx in Excel for Web > Copilot pane > + New Agent > set workbook as knowledge source > share.',
          'prompts': [
            'You are the Chief Financial Officer at Aman Jaya Property Berhad. Open PROP_01_Portfolio_Performance.xlsx in Excel for Web and create an agent called \'Aman Jaya Property Data Q&A\'. Describe it as an assistant for the Asset NAV Summary, Rental Yield Tracker, Occupancy Dashboard, Development Pipeline, and Debt Covenant Monitor sheets that gives instant Red, Amber, and Green answers on performance and risk, then share it with the leadership team.',
            'You are the Chief Investment Officer at Aman Jaya Property Berhad. Demo the \'Aman Jaya Property Data Q&A\' agent by asking which 3 items are currently Red in the Asset NAV Summary and Debt Covenant Monitor sheets and what management action each implies. Then ask which single Amber item could become Red fastest and why.'
          ]
        },
        {
          'tool': '🏗 Agent Builder (Copilot Studio)',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'desc': 'Build a custom declarative agent in Copilot Studio — no coding required. Access: copilotstudio.microsoft.com > Create > New Agent. Add name, description, knowledge sources (SharePoint URLs or uploaded files), topics/actions. Publish to Teams in under 10 minutes.',
          'prompts': [
            'You are the Chief Investment Officer at Aman Jaya Property Berhad. Go to Copilot Studio and create an agent called \'Aman Jaya Property Intelligence Agent\' using PROP_01_Portfolio_Performance.xlsx, PROP_02_Asset_Management_Policy.docx, and PROP_03_Development_Brief.docx as knowledge sources. Tell the agent to answer questions across the Asset NAV Summary, Rental Yield Tracker, Occupancy Dashboard, Development Pipeline, and Debt Covenant Monitor sheets, add topics for Portfolio Performance, Leasing Risk, Development Pipeline, Debt & REIT Readiness, and require every answer to end with a RAG recommendation.',
            'You are the Head of Asset Management at Aman Jaya Property Berhad. Demo the \'Aman Jaya Property Intelligence Agent\' by asking for a 2-minute briefing on the biggest Red issue in the Asset NAV Summary and Debt Covenant Monitor sheets, the best Amber mitigation in PROP_03_Development_Brief.docx, and the Green signals management can still rely on. Ask for the answer in a RAG table with next-step owners.'
          ]
        }
      ]
    },

    {
      'id': 'logistics-3pl',
      'sectorId': 'logistics',
      'name': 'Logistics & 3PL',
      'icon': '🚢',
      'color': '#00695C',
      'accent': '#00796B',
      'company': 'Rangkaian Logistik Nasional Berhad',
      'tagline': 'SLA pressure collides with cold-chain expansion spend.',
      'companyID': 'PT Rantai Logistik Nusantara Tbk',
      'taglineID': 'Transit delays and reefer capex are squeezing the Indonesia network.',
      'scenario': 'Rangkaian Logistik Nasional Berhad and PT Rantai Logistik Nusantara Tbk run regional freight, warehousing, and cold-chain operations across Malaysia and Indonesia. On-time delivery is slipping, warehouse utilisation is uneven, and the fleet plan requires capex before several major customer SLA renewals. Management must stabilise service levels and decide where to expand cold-chain capacity without eroding margins.',
      'files': ['LOG_01_Operations_Dashboard.xlsx', 'LOG_02_Service_Level_Agreement.docx', 'LOG_03_Fleet_Management_Policy.docx'],
      'prompts': [
        {
          'tool': '🤖 Copilot Chat (Basic)',
          'license': 'Free — no M365 Copilot license needed',
          'account': 'Sasha Ouellet — SashaO@ABSx62256373.OnMicrosoft.com',
          'prompts': [
            'You are the Chief Operating Officer at Rangkaian Logistik Nasional Berhad. Using LOG_01_Operations_Dashboard.xlsx, focus on the Shipment KPIs, On-Time Delivery, and Customer SLA Report sheets to assess on-time-delivery slippage, uneven warehouse utilisation, and cold-chain expansion risk. Quantify the immediate downside, name the 3 decisions management must take in the next 30 days, and present the answer as a RAG table with Red, Amber, and Green actions.',
            'You are the Head of Network Planning at Rangkaian Logistik Nasional Berhad. Using the Warehouse Utilisation and Fleet Management sheets in LOG_01_Operations_Dashboard.xlsx together with LOG_02_Service_Level_Agreement.docx, explain how the current operating issue affects strategy, capital allocation, and stakeholder confidence. Present the response as a RAG memo with sections for What We Know, What We Do Not Yet Know, and What We Should Do Next.',
            'You are the Chief Financial Officer at Rangkaian Logistik Nasional Berhad. Using the Shipment KPIs and Warehouse Utilisation sheets in LOG_01_Operations_Dashboard.xlsx, benchmark our current position against the 2024 to 2025 ASEAN contract logistics and cold-chain market. Summarise the 5 most important leading indicators to watch over the next 2 quarters and show them in a RAG scorecard with a short management implication beside each.'
          ]
        },
        {
          'tool': '🔍 Researcher',
          'license': 'Free — no M365 Copilot license needed',
          'account': 'Sasha Ouellet — SashaO@ABSx62256373.OnMicrosoft.com',
          'desc': 'Access via Microsoft 365 Copilot Chat > Agents > Researcher. Researcher automatically critiques every source — verifying claims against the original before including them in the report. Grounds answers in live web sources and your organisation\'s data with full citations. Faster and more reliable than manual research.',
          'prompts': [
            'You are the Head of Network Planning at Rangkaian Logistik Nasional Berhad. Using LOG_01_Operations_Dashboard.xlsx, especially the Shipment KPIs, On-Time Delivery, and Warehouse Utilisation sheets, plus LOG_02_Service_Level_Agreement.docx, research 2024 to 2025 market benchmarks, peer disclosures, and financing or valuation signals relevant to on-time-delivery slippage, uneven warehouse utilisation, and cold-chain expansion risk. Present a RAG table with Red for immediate threats, Amber for watchlist items, and Green for supporting market signals, with citations to every source and a one-line implication for management. Flag any claim that could not be independently verified.',
            'You are the Chief Operating Officer at Rangkaian Logistik Nasional Berhad. Using the Fleet Management and Customer SLA Report sheets in LOG_01_Operations_Dashboard.xlsx and the policy positions in LOG_03_Fleet_Management_Policy.docx, research how SIRIM, Kementerian Perdagangan, and BKPM or comparable published authorities and industry bodies are treating this issue across Malaysia and Indonesia. Separate mandatory requirements from market practice, cite each source, and present the findings as a RAG matrix with columns for Issue, Malaysia, Indonesia, Timing, and Management Action. Flag any claim that could not be independently verified.',
            'You are the Chief Financial Officer at Rangkaian Logistik Nasional Berhad. Using the Shipment KPIs, Warehouse Utilisation, and Fleet Management sheets in LOG_01_Operations_Dashboard.xlsx, research the demand, pricing, and competitor trends that will most influence our next 12 months. Present the answer as a RAG table ranking the top 10 external signals by likely impact and management preparedness, with citations beside every row. Flag any claim that could not be independently verified.'
          ]
        },
        {
          'tool': '📊 Analyst',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'desc': 'Access via Microsoft 365 Copilot Chat > click Agents > Analyst. Upload an Excel or CSV file. Analyst runs Python-style analysis, builds charts, and interprets results without you writing a single formula.',
          'prompts': [
            'You are the Chief Financial Officer at Rangkaian Logistik Nasional Berhad. Upload LOG_01_Operations_Dashboard.xlsx to Analyst and use the Shipment KPIs, On-Time Delivery, and Warehouse Utilisation sheets to identify the 5 biggest sources of underperformance or stress in the current plan. Quantify the variance where possible, flag each item Red, Amber, or Green based on financial materiality, and end with one corrective action per Red item.',
            'You are the Chief Operating Officer at Rangkaian Logistik Nasional Berhad. Upload LOG_01_Operations_Dashboard.xlsx to Analyst and use the Fleet Management and Customer SLA Report sheets to model 3 scenarios for on-time-delivery slippage, uneven warehouse utilisation, and cold-chain expansion risk: downside, base case, and recovery case. Show the impact on revenue, margin or cash, plus the operational trigger that would move an item from Amber to Red.',
            'You are the Head of Network Planning at Rangkaian Logistik Nasional Berhad. Upload LOG_01_Operations_Dashboard.xlsx to Analyst and use the Shipment KPIs, Warehouse Utilisation, and Customer SLA Report sheets to build a 13-week watchlist of the metrics most likely to surprise management. Present the output as a RAG dashboard table with columns for Metric, Current Level, Threshold, Risk Status, and Recommended Owner.'
          ]
        },
        {
          'tool': '📊 Copilot in Excel',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'prompts': [
            'You are the Head of Network Planning at Rangkaian Logistik Nasional Berhad. Using LOG_01_Operations_Dashboard.xlsx, build a new sheet called \'Rangkaian Logistics Executive Dashboard\' from the Shipment KPIs, On-Time Delivery, and Warehouse Utilisation sheets. Show the 10 most important KPIs, add a RAG status column driven by clear thresholds, and place an executive summary box at the top that updates automatically.',
            'You are the Chief Operating Officer at Rangkaian Logistik Nasional Berhad. Using LOG_01_Operations_Dashboard.xlsx, create a risk tracker that pulls from the On-Time Delivery, Fleet Management, and Customer SLA Report sheets. For each material issue, show owner, due date, estimated financial exposure, and Red/Amber/Green status, then sort Red issues first.',
            'You are the Chief Financial Officer at Rangkaian Logistik Nasional Berhad. Using LOG_01_Operations_Dashboard.xlsx, build a scenario sensitivity sheet using the Shipment KPIs, Warehouse Utilisation, and Customer SLA Report sheets as inputs. Show downside, base, and upside cases side by side, add conditional formatting for RAG thresholds, and include a short note on the trigger that would require management escalation.'
          ]
        },
        {
          'tool': '📝 Copilot in Word',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'prompts': [
            'You are the Chief Operating Officer at Rangkaian Logistik Nasional Berhad. Using LOG_02_Service_Level_Agreement.docx together with the Shipment KPIs and Customer SLA Report sheets in LOG_01_Operations_Dashboard.xlsx, draft a 2-page Board paper on on-time-delivery slippage, uneven warehouse utilisation, and cold-chain expansion risk. Structure it as Situation, Risks, Decisions Required, and Next 30 Days, and place a compact RAG summary at the top.',
            'You are the Head of Network Planning at Rangkaian Logistik Nasional Berhad. Using LOG_03_Fleet_Management_Policy.docx and the On-Time Delivery and Fleet Management sheets in LOG_01_Operations_Dashboard.xlsx, draft a policy or action-plan note for the leadership team that translates the data into clear operating actions. Present the recommendations as a RAG table with owners, timing, and expected impact.',
            'You are the Chief Financial Officer at Rangkaian Logistik Nasional Berhad. Using LOG_02_Service_Level_Agreement.docx, LOG_03_Fleet_Management_Policy.docx, and the Shipment KPIs sheet in LOG_01_Operations_Dashboard.xlsx, draft an external stakeholder briefing note that explains our position factually and shows what management is doing next. After the draft, add a 3-line RAG risk summary covering timing, evidence strength, and stakeholder reaction.'
          ]
        },
        {
          'tool': '🎯 Copilot in PowerPoint',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'prompts': [
            'You are the Chief Operating Officer at Rangkaian Logistik Nasional Berhad. Create a 6-slide executive deck using LOG_01_Operations_Dashboard.xlsx and LOG_02_Service_Level_Agreement.docx, grounded in the Shipment KPIs, Warehouse Utilisation, and Customer SLA Report sheets. Cover logistics & 3pl performance, root causes, key risks, management response, scenario outlook, and decisions required, with one headline takeaway per slide and a visible RAG status marker.',
            'You are the Head of Network Planning at Rangkaian Logistik Nasional Berhad. Create a 3-slide operating review using the On-Time Delivery, Warehouse Utilisation, and Fleet Management sheets in LOG_01_Operations_Dashboard.xlsx. Show what is Red, what is Amber, and what is Green, then close with the 5 highest-priority actions and owners.',
            'You are the Chief Financial Officer at Rangkaian Logistik Nasional Berhad. Build a 2-slide stakeholder briefing from LOG_01_Operations_Dashboard.xlsx and LOG_03_Fleet_Management_Policy.docx, using the Shipment KPIs and Customer SLA Report sheets as the fact base. The first slide should summarise the issue and the second should show the recovery path in a RAG timeline.'
          ]
        },
        {
          'tool': '📧 Copilot in Outlook',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'prompts': [
            'You are the Chief Operating Officer at Rangkaian Logistik Nasional Berhad. Using the Shipment KPIs and Customer SLA Report sheets in LOG_01_Operations_Dashboard.xlsx, draft an email to top contract customers and lending banks explaining the current situation, the evidence supporting our view, and the immediate next step we want from them. After the draft, add a short RAG summary of delivery risk, likely objections, and follow-up timing.',
            'You are the Head of Network Planning at Rangkaian Logistik Nasional Berhad. Using the Warehouse Utilisation and Fleet Management sheets in LOG_01_Operations_Dashboard.xlsx plus LOG_02_Service_Level_Agreement.docx, draft a regulator-ready note for SIRIM, Kementerian Perdagangan, and BKPM or the most relevant authority. Keep the tone factual, distinguish confirmed facts from assumptions, and end with a RAG table of issues that may require further disclosure.',
            'You are the Chief Financial Officer at Rangkaian Logistik Nasional Berhad. Using the Shipment KPIs, On-Time Delivery, and Warehouse Utilisation sheets in LOG_01_Operations_Dashboard.xlsx, draft an internal leadership email that aligns owners around the top 5 actions for the next 14 days. Finish with a RAG checklist titled Do Today, Do This Week, and Monitor.'
          ]
        },
        {
          'tool': '🎙 Copilot in Teams',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'desc': 'Use your OWN existing recorded Teams meetings. Open a meeting recap in Teams > Recap tab. Copilot generates summaries, action items, and follow-up drafts grounded in the actual transcript.',
          'prompts': [
            'You are the Head of Network Planning at Rangkaian Logistik Nasional Berhad. Using this recorded Teams meeting recap and the Shipment KPIs and Warehouse Utilisation sheets in LOG_01_Operations_Dashboard.xlsx as the operating benchmark, extract all decisions, risks, and unresolved items related to on-time-delivery slippage, uneven warehouse utilisation, and cold-chain expansion risk. Present the result as a RAG table with owners and due dates.',
            'You are the Chief Operating Officer at Rangkaian Logistik Nasional Berhad. Using the On-Time Delivery and Customer SLA Report sheets in LOG_01_Operations_Dashboard.xlsx as reference points, draft follow-up actions from the meeting grouped by Operations | Fleet | Warehousing | Commercial | Compliance. For each action, include owner, deadline, and whether the item is Red, Amber, or Green.',
            'You are the Chief Financial Officer at Rangkaian Logistik Nasional Berhad. Using this meeting recap and the Fleet Management sheet in LOG_01_Operations_Dashboard.xlsx as context, identify whether any comments suggest hidden downside not yet reflected in management reporting. Summarise the findings as a RAG note with direct quotes or paraphrased evidence from the recap.'
          ]
        },
        {
          'tool': '📓 Copilot Notebook',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'desc': 'Access via copilot.microsoft.com > Notebook tab. Upload up to 5 files and set a system instruction. Best for synthesising insights across multiple documents simultaneously.',
          'prompts': [
            'You are the Chief Operating Officer at Rangkaian Logistik Nasional Berhad. Upload LOG_01_Operations_Dashboard.xlsx, LOG_02_Service_Level_Agreement.docx, and LOG_03_Fleet_Management_Policy.docx to Copilot Notebook and focus on the Shipment KPIs, Warehouse Utilisation, and Customer SLA Report sheets. Ask Notebook to produce a cross-file RAG synthesis of the top risks, the 3 most credible management actions, and the evidence supporting each recommendation, citing the source file for every major point.',
            'You are the Head of Network Planning at Rangkaian Logistik Nasional Berhad. Upload LOG_01_Operations_Dashboard.xlsx and LOG_02_Service_Level_Agreement.docx to Copilot Notebook and focus on the On-Time Delivery, Fleet Management, and Customer SLA Report sheets. Ask Notebook to model a downside scenario for on-time-delivery slippage, uneven warehouse utilisation, and cold-chain expansion risk, explain which assumptions matter most, and present the answer as a RAG table with immediate, next-quarter, and monitor-only actions.',
            'You are the Chief Financial Officer at Rangkaian Logistik Nasional Berhad. Upload LOG_01_Operations_Dashboard.xlsx, LOG_02_Service_Level_Agreement.docx, and LOG_03_Fleet_Management_Policy.docx to Copilot Notebook and focus on the Shipment KPIs, On-Time Delivery, and Fleet Management sheets. Ask Notebook to rank the top 5 opportunities to stabilise performance without creating new compliance or stakeholder risk, and return the answer as a RAG prioritisation table with expected impact and implementation difficulty.'
          ]
        },
        {
          'tool': '🤝 Cowork (Frontier)',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'desc': 'Cowork is an autonomous agent that takes actions across Microsoft 365 on your behalf — sending emails, scheduling meetings, creating documents, posting in Teams, and scheduling recurring tasks. Access: m365.cloud.microsoft > left nav > Agents > Cowork. Requires Frontier program enrollment.',
          'prompts': [
            'You are the Chief Operating Officer at Rangkaian Logistik Nasional Berhad. Using LOG_01_Operations_Dashboard.xlsx, LOG_02_Service_Level_Agreement.docx, and LOG_03_Fleet_Management_Policy.docx, especially the Shipment KPIs, Warehouse Utilisation, and Customer SLA Report sheets, research the current market context, draft a 2-page management brief, save it to OneDrive, and email it to the leadership team for review. Then schedule a 30-minute follow-up meeting for next week and label the agenda items Red, Amber, and Green.',
            'You are the Head of Network Planning at Rangkaian Logistik Nasional Berhad. Using the On-Time Delivery, Fleet Management, and Customer SLA Report sheets in LOG_01_Operations_Dashboard.xlsx, prepare a task tracker, draft the related stakeholder email, store both in SharePoint or OneDrive, and send them to the named owners. Then book a checkpoint meeting and make sure the work is grouped by Operations | Fleet | Warehousing | Commercial | Compliance with clear RAG priorities.'
          ]
        },
        {
          'tool': '✏️ Edit with Copilot',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'desc': 'Edit with Copilot is an agentic mode in Word, Excel, and PowerPoint (web) that executes multi-step editing tasks across your entire document in one instruction — reformatting, restructuring, building formulas, generating new sections. Access: open any Office file in browser > Copilot pane > Edit with Copilot. Requires M365 Copilot licence.',
          'prompts': [
            'You are the Chief Operating Officer at Rangkaian Logistik Nasional Berhad. Using LOG_02_Service_Level_Agreement.docx in Word for the web and the Shipment KPIs and Customer SLA Report sheets in LOG_01_Operations_Dashboard.xlsx as the fact base, add a new section that sharpens the narrative around on-time-delivery slippage, uneven warehouse utilisation, and cold-chain expansion risk. Restructure the content into Situation, Key Data, Decisions, and Next Steps, and insert a small RAG summary box at the top.',
            'You are the Chief Financial Officer at Rangkaian Logistik Nasional Berhad. Using LOG_01_Operations_Dashboard.xlsx in Excel for the web, redesign the sheets fed by On-Time Delivery, Warehouse Utilisation, and Customer SLA Report so executives can see the highest-risk items first. Standardise labels, improve formulas where needed, and add a RAG status column plus a one-row summary that updates automatically.'
          ]
        },
        {
          'tool': '🤖 Word Agent',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'desc': 'Create a declarative agent scoped to a Word document. Open the .docx in Word for Web > Copilot pane > + New Agent > name it, write a description, set the document as knowledge source > Share. Colleagues chat with it in Teams or M365 Copilot.',
          'prompts': [
            'You are the Head of Network Planning at Rangkaian Logistik Nasional Berhad. Open LOG_02_Service_Level_Agreement.docx in Word for Web and create an agent called \'Rangkaian Logistics Word Guide\'. Describe it as an assistant that answers questions using LOG_02_Service_Level_Agreement.docx plus the Shipment KPIs and Warehouse Utilisation sheets in LOG_01_Operations_Dashboard.xlsx, then share it with the relevant leadership team.',
            'You are the Chief Financial Officer at Rangkaian Logistik Nasional Berhad. Demo the \'Rangkaian Logistics Word Guide\' agent by asking: \'What is our most urgent operating risk, what evidence from the On-Time Delivery and Customer SLA Report sheets supports it, and what action does LOG_02_Service_Level_Agreement.docx imply we should take first?\'. Show the answer as a short RAG response with the supporting source references.'
          ]
        },
        {
          'tool': '🤖 PowerPoint Agent',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'desc': 'Create a declarative agent scoped to a PowerPoint presentation. Great for strategy decks or Board presentations many people need to reference. Same setup as Word Agent but using a .pptx file.',
          'prompts': [
            'You are the Chief Operating Officer at Rangkaian Logistik Nasional Berhad. Create the leadership presentation in PowerPoint for Web using LOG_01_Operations_Dashboard.xlsx and LOG_03_Fleet_Management_Policy.docx, then create an agent called \'Rangkaian Logistics Deck Navigator\'. Tell users it can answer questions tied to the Shipment KPIs, Fleet Management, and Customer SLA Report sheets, then share it with the executive team.',
            'You are the Head of Network Planning at Rangkaian Logistik Nasional Berhad. Demo the \'Rangkaian Logistics Deck Navigator\' agent by asking: \'Which slide best explains our Red risks, what does the Customer SLA Report sheet say about exposure, and what decision do leaders need this week?\'. Request a RAG answer in under 120 words.'
          ]
        },
        {
          'tool': '🤖 Excel Agent',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'desc': 'Create a declarative agent scoped to an Excel workbook. Colleagues ask data questions in plain English without opening Excel. Open .xlsx in Excel for Web > Copilot pane > + New Agent > set workbook as knowledge source > share.',
          'prompts': [
            'You are the Chief Financial Officer at Rangkaian Logistik Nasional Berhad. Open LOG_01_Operations_Dashboard.xlsx in Excel for Web and create an agent called \'Rangkaian Logistics Data Q&A\'. Describe it as an assistant for the Shipment KPIs, On-Time Delivery, Warehouse Utilisation, Fleet Management, and Customer SLA Report sheets that gives instant Red, Amber, and Green answers on performance and risk, then share it with the leadership team.',
            'You are the Chief Operating Officer at Rangkaian Logistik Nasional Berhad. Demo the \'Rangkaian Logistics Data Q&A\' agent by asking which 3 items are currently Red in the Shipment KPIs and Customer SLA Report sheets and what management action each implies. Then ask which single Amber item could become Red fastest and why.'
          ]
        },
        {
          'tool': '🏗 Agent Builder (Copilot Studio)',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'desc': 'Build a custom declarative agent in Copilot Studio — no coding required. Access: copilotstudio.microsoft.com > Create > New Agent. Add name, description, knowledge sources (SharePoint URLs or uploaded files), topics/actions. Publish to Teams in under 10 minutes.',
          'prompts': [
            'You are the Chief Operating Officer at Rangkaian Logistik Nasional Berhad. Go to Copilot Studio and create an agent called \'Rangkaian Logistics Intelligence Agent\' using LOG_01_Operations_Dashboard.xlsx, LOG_02_Service_Level_Agreement.docx, and LOG_03_Fleet_Management_Policy.docx as knowledge sources. Tell the agent to answer questions across the Shipment KPIs, On-Time Delivery, Warehouse Utilisation, Fleet Management, and Customer SLA Report sheets, add topics for Shipment KPIs, On-Time Delivery, Warehouse Utilisation, Fleet Management, and require every answer to end with a RAG recommendation.',
            'You are the Head of Network Planning at Rangkaian Logistik Nasional Berhad. Demo the \'Rangkaian Logistics Intelligence Agent\' by asking for a 2-minute briefing on the biggest Red issue in the Shipment KPIs and Customer SLA Report sheets, the best Amber mitigation in LOG_03_Fleet_Management_Policy.docx, and the Green signals management can still rely on. Ask for the answer in a RAG table with next-step owners.'
          ]
        }
      ]
    },

    {
      'id': 'coal-mining',
      'sectorId': 'mining',
      'name': 'Coal Mining',
      'icon': '⛏',
      'color': '#424242',
      'accent': '#616161',
      'company': 'Bara Jaya Mining Berhad',
      'tagline': 'Strip ratio spike and safety incidents threaten export margins.',
      'companyID': 'PT Bara Jaya Energi Tbk',
      'taglineID': 'Permit scrutiny rises as haul-road safety and rainfall disrupt output.',
      'scenario': 'Bara Jaya Mining Berhad and PT Bara Jaya Energi Tbk supply thermal coal into regional utility and industrial markets. The strip ratio is rising, export costs per tonne are climbing, and recent safety incidents are increasing scrutiny on operating discipline and environmental controls. Management needs to defend output, cash generation, and licence-to-operate at the same time.',
      'files': ['COAL_01_Mining_Operations.xlsx', 'COAL_02_Mine_Safety_Manual.docx', 'COAL_03_Environmental_Management_Plan.docx'],
      'prompts': [
        {
          'tool': '🤖 Copilot Chat (Basic)',
          'license': 'Free — no M365 Copilot license needed',
          'account': 'Sasha Ouellet — SashaO@ABSx62256373.OnMicrosoft.com',
          'prompts': [
            'You are the Chief Operating Officer at Bara Jaya Mining Berhad. Using COAL_01_Mining_Operations.xlsx, focus on the Production Log, Strip Ratio Tracker, and Operating Cost per Tonne sheets to assess a rising strip ratio, recurring safety incidents, and margin pressure on export tonnes. Quantify the immediate downside, name the 3 decisions management must take in the next 30 days, and present the answer as a RAG table with Red, Amber, and Green actions.',
            'You are the Head of Sustainability at Bara Jaya Mining Berhad. Using the Safety Incident Register and Export Volume Dashboard sheets in COAL_01_Mining_Operations.xlsx together with COAL_02_Mine_Safety_Manual.docx, explain how the current operating issue affects strategy, capital allocation, and stakeholder confidence. Present the response as a RAG memo with sections for What We Know, What We Do Not Yet Know, and What We Should Do Next.',
            'You are the Chief Financial Officer at Bara Jaya Mining Berhad. Using the Production Log and Safety Incident Register sheets in COAL_01_Mining_Operations.xlsx, benchmark our current position against the 2024 to 2025 regional seaborne thermal coal market. Summarise the 5 most important leading indicators to watch over the next 2 quarters and show them in a RAG scorecard with a short management implication beside each.'
          ]
        },
        {
          'tool': '🔍 Researcher',
          'license': 'Free — no M365 Copilot license needed',
          'account': 'Sasha Ouellet — SashaO@ABSx62256373.OnMicrosoft.com',
          'desc': 'Access via Microsoft 365 Copilot Chat > Agents > Researcher. Researcher automatically critiques every source — verifying claims against the original before including them in the report. Grounds answers in live web sources and your organisation\'s data with full citations. Faster and more reliable than manual research.',
          'prompts': [
            'You are the Head of Sustainability at Bara Jaya Mining Berhad. Using COAL_01_Mining_Operations.xlsx, especially the Production Log, Strip Ratio Tracker, and Safety Incident Register sheets, plus COAL_02_Mine_Safety_Manual.docx, research 2024 to 2025 market benchmarks, peer disclosures, and financing or valuation signals relevant to a rising strip ratio, recurring safety incidents, and margin pressure on export tonnes. Present a RAG table with Red for immediate threats, Amber for watchlist items, and Green for supporting market signals, with citations to every source and a one-line implication for management. Flag any claim that could not be independently verified.',
            'You are the Chief Operating Officer at Bara Jaya Mining Berhad. Using the Export Volume Dashboard and Operating Cost per Tonne sheets in COAL_01_Mining_Operations.xlsx and the policy positions in COAL_03_Environmental_Management_Plan.docx, research how OJK and BKPM or comparable published authorities and industry bodies are treating this issue across Malaysia and Indonesia. Separate mandatory requirements from market practice, cite each source, and present the findings as a RAG matrix with columns for Issue, Malaysia, Indonesia, Timing, and Management Action. Flag any claim that could not be independently verified.',
            'You are the Chief Financial Officer at Bara Jaya Mining Berhad. Using the Production Log, Safety Incident Register, and Export Volume Dashboard sheets in COAL_01_Mining_Operations.xlsx, research the demand, pricing, and competitor trends that will most influence our next 12 months. Present the answer as a RAG table ranking the top 10 external signals by likely impact and management preparedness, with citations beside every row. Flag any claim that could not be independently verified.'
          ]
        },
        {
          'tool': '📊 Analyst',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'desc': 'Access via Microsoft 365 Copilot Chat > click Agents > Analyst. Upload an Excel or CSV file. Analyst runs Python-style analysis, builds charts, and interprets results without you writing a single formula.',
          'prompts': [
            'You are the Chief Financial Officer at Bara Jaya Mining Berhad. Upload COAL_01_Mining_Operations.xlsx to Analyst and use the Production Log, Strip Ratio Tracker, and Safety Incident Register sheets to identify the 5 biggest sources of underperformance or stress in the current plan. Quantify the variance where possible, flag each item Red, Amber, or Green based on financial materiality, and end with one corrective action per Red item.',
            'You are the Chief Operating Officer at Bara Jaya Mining Berhad. Upload COAL_01_Mining_Operations.xlsx to Analyst and use the Export Volume Dashboard and Operating Cost per Tonne sheets to model 3 scenarios for a rising strip ratio, recurring safety incidents, and margin pressure on export tonnes: downside, base case, and recovery case. Show the impact on revenue, margin or cash, plus the operational trigger that would move an item from Amber to Red.',
            'You are the Head of Sustainability at Bara Jaya Mining Berhad. Upload COAL_01_Mining_Operations.xlsx to Analyst and use the Production Log, Safety Incident Register, and Operating Cost per Tonne sheets to build a 13-week watchlist of the metrics most likely to surprise management. Present the output as a RAG dashboard table with columns for Metric, Current Level, Threshold, Risk Status, and Recommended Owner.'
          ]
        },
        {
          'tool': '📊 Copilot in Excel',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'prompts': [
            'You are the Head of Sustainability at Bara Jaya Mining Berhad. Using COAL_01_Mining_Operations.xlsx, build a new sheet called \'Bara Jaya Mining Executive Dashboard\' from the Production Log, Strip Ratio Tracker, and Safety Incident Register sheets. Show the 10 most important KPIs, add a RAG status column driven by clear thresholds, and place an executive summary box at the top that updates automatically.',
            'You are the Chief Operating Officer at Bara Jaya Mining Berhad. Using COAL_01_Mining_Operations.xlsx, create a risk tracker that pulls from the Strip Ratio Tracker, Export Volume Dashboard, and Operating Cost per Tonne sheets. For each material issue, show owner, due date, estimated financial exposure, and Red/Amber/Green status, then sort Red issues first.',
            'You are the Chief Financial Officer at Bara Jaya Mining Berhad. Using COAL_01_Mining_Operations.xlsx, build a scenario sensitivity sheet using the Production Log, Safety Incident Register, and Operating Cost per Tonne sheets as inputs. Show downside, base, and upside cases side by side, add conditional formatting for RAG thresholds, and include a short note on the trigger that would require management escalation.'
          ]
        },
        {
          'tool': '📝 Copilot in Word',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'prompts': [
            'You are the Chief Operating Officer at Bara Jaya Mining Berhad. Using COAL_02_Mine_Safety_Manual.docx together with the Production Log and Operating Cost per Tonne sheets in COAL_01_Mining_Operations.xlsx, draft a 2-page Board paper on a rising strip ratio, recurring safety incidents, and margin pressure on export tonnes. Structure it as Situation, Risks, Decisions Required, and Next 30 Days, and place a compact RAG summary at the top.',
            'You are the Head of Sustainability at Bara Jaya Mining Berhad. Using COAL_03_Environmental_Management_Plan.docx and the Strip Ratio Tracker and Export Volume Dashboard sheets in COAL_01_Mining_Operations.xlsx, draft a policy or action-plan note for the leadership team that translates the data into clear operating actions. Present the recommendations as a RAG table with owners, timing, and expected impact.',
            'You are the Chief Financial Officer at Bara Jaya Mining Berhad. Using COAL_02_Mine_Safety_Manual.docx, COAL_03_Environmental_Management_Plan.docx, and the Production Log sheet in COAL_01_Mining_Operations.xlsx, draft an external stakeholder briefing note that explains our position factually and shows what management is doing next. After the draft, add a 3-line RAG risk summary covering timing, evidence strength, and stakeholder reaction.'
          ]
        },
        {
          'tool': '🎯 Copilot in PowerPoint',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'prompts': [
            'You are the Chief Operating Officer at Bara Jaya Mining Berhad. Create a 6-slide executive deck using COAL_01_Mining_Operations.xlsx and COAL_02_Mine_Safety_Manual.docx, grounded in the Production Log, Safety Incident Register, and Operating Cost per Tonne sheets. Cover coal mining performance, root causes, key risks, management response, scenario outlook, and decisions required, with one headline takeaway per slide and a visible RAG status marker.',
            'You are the Head of Sustainability at Bara Jaya Mining Berhad. Create a 3-slide operating review using the Strip Ratio Tracker, Safety Incident Register, and Export Volume Dashboard sheets in COAL_01_Mining_Operations.xlsx. Show what is Red, what is Amber, and what is Green, then close with the 5 highest-priority actions and owners.',
            'You are the Chief Financial Officer at Bara Jaya Mining Berhad. Build a 2-slide stakeholder briefing from COAL_01_Mining_Operations.xlsx and COAL_03_Environmental_Management_Plan.docx, using the Production Log and Operating Cost per Tonne sheets as the fact base. The first slide should summarise the issue and the second should show the recovery path in a RAG timeline.'
          ]
        },
        {
          'tool': '📧 Copilot in Outlook',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'prompts': [
            'You are the Chief Operating Officer at Bara Jaya Mining Berhad. Using the Production Log and Operating Cost per Tonne sheets in COAL_01_Mining_Operations.xlsx, draft an email to lenders, insurers, and export offtakers explaining the current situation, the evidence supporting our view, and the immediate next step we want from them. After the draft, add a short RAG summary of delivery risk, likely objections, and follow-up timing.',
            'You are the Head of Sustainability at Bara Jaya Mining Berhad. Using the Safety Incident Register and Export Volume Dashboard sheets in COAL_01_Mining_Operations.xlsx plus COAL_02_Mine_Safety_Manual.docx, draft a regulator-ready note for OJK and BKPM or the most relevant authority. Keep the tone factual, distinguish confirmed facts from assumptions, and end with a RAG table of issues that may require further disclosure.',
            'You are the Chief Financial Officer at Bara Jaya Mining Berhad. Using the Production Log, Strip Ratio Tracker, and Safety Incident Register sheets in COAL_01_Mining_Operations.xlsx, draft an internal leadership email that aligns owners around the top 5 actions for the next 14 days. Finish with a RAG checklist titled Do Today, Do This Week, and Monitor.'
          ]
        },
        {
          'tool': '🎙 Copilot in Teams',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'desc': 'Use your OWN existing recorded Teams meetings. Open a meeting recap in Teams > Recap tab. Copilot generates summaries, action items, and follow-up drafts grounded in the actual transcript.',
          'prompts': [
            'You are the Head of Sustainability at Bara Jaya Mining Berhad. Using this recorded Teams meeting recap and the Production Log and Safety Incident Register sheets in COAL_01_Mining_Operations.xlsx as the operating benchmark, extract all decisions, risks, and unresolved items related to a rising strip ratio, recurring safety incidents, and margin pressure on export tonnes. Present the result as a RAG table with owners and due dates.',
            'You are the Chief Operating Officer at Bara Jaya Mining Berhad. Using the Strip Ratio Tracker and Operating Cost per Tonne sheets in COAL_01_Mining_Operations.xlsx as reference points, draft follow-up actions from the meeting grouped by Production | Safety | ESG | Marketing | Treasury. For each action, include owner, deadline, and whether the item is Red, Amber, or Green.',
            'You are the Chief Financial Officer at Bara Jaya Mining Berhad. Using this meeting recap and the Export Volume Dashboard sheet in COAL_01_Mining_Operations.xlsx as context, identify whether any comments suggest hidden downside not yet reflected in management reporting. Summarise the findings as a RAG note with direct quotes or paraphrased evidence from the recap.'
          ]
        },
        {
          'tool': '📓 Copilot Notebook',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'desc': 'Access via copilot.microsoft.com > Notebook tab. Upload up to 5 files and set a system instruction. Best for synthesising insights across multiple documents simultaneously.',
          'prompts': [
            'You are the Chief Operating Officer at Bara Jaya Mining Berhad. Upload COAL_01_Mining_Operations.xlsx, COAL_02_Mine_Safety_Manual.docx, and COAL_03_Environmental_Management_Plan.docx to Copilot Notebook and focus on the Production Log, Safety Incident Register, and Operating Cost per Tonne sheets. Ask Notebook to produce a cross-file RAG synthesis of the top risks, the 3 most credible management actions, and the evidence supporting each recommendation, citing the source file for every major point.',
            'You are the Head of Sustainability at Bara Jaya Mining Berhad. Upload COAL_01_Mining_Operations.xlsx and COAL_02_Mine_Safety_Manual.docx to Copilot Notebook and focus on the Strip Ratio Tracker, Export Volume Dashboard, and Operating Cost per Tonne sheets. Ask Notebook to model a downside scenario for a rising strip ratio, recurring safety incidents, and margin pressure on export tonnes, explain which assumptions matter most, and present the answer as a RAG table with immediate, next-quarter, and monitor-only actions.',
            'You are the Chief Financial Officer at Bara Jaya Mining Berhad. Upload COAL_01_Mining_Operations.xlsx, COAL_02_Mine_Safety_Manual.docx, and COAL_03_Environmental_Management_Plan.docx to Copilot Notebook and focus on the Production Log, Strip Ratio Tracker, and Export Volume Dashboard sheets. Ask Notebook to rank the top 5 opportunities to stabilise performance without creating new compliance or stakeholder risk, and return the answer as a RAG prioritisation table with expected impact and implementation difficulty.'
          ]
        },
        {
          'tool': '🤝 Cowork (Frontier)',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'desc': 'Cowork is an autonomous agent that takes actions across Microsoft 365 on your behalf — sending emails, scheduling meetings, creating documents, posting in Teams, and scheduling recurring tasks. Access: m365.cloud.microsoft > left nav > Agents > Cowork. Requires Frontier program enrollment.',
          'prompts': [
            'You are the Chief Operating Officer at Bara Jaya Mining Berhad. Using COAL_01_Mining_Operations.xlsx, COAL_02_Mine_Safety_Manual.docx, and COAL_03_Environmental_Management_Plan.docx, especially the Production Log, Safety Incident Register, and Operating Cost per Tonne sheets, research the current market context, draft a 2-page management brief, save it to OneDrive, and email it to the leadership team for review. Then schedule a 30-minute follow-up meeting for next week and label the agenda items Red, Amber, and Green.',
            'You are the Head of Sustainability at Bara Jaya Mining Berhad. Using the Strip Ratio Tracker, Export Volume Dashboard, and Operating Cost per Tonne sheets in COAL_01_Mining_Operations.xlsx, prepare a task tracker, draft the related stakeholder email, store both in SharePoint or OneDrive, and send them to the named owners. Then book a checkpoint meeting and make sure the work is grouped by Production | Safety | ESG | Marketing | Treasury with clear RAG priorities.'
          ]
        },
        {
          'tool': '✏️ Edit with Copilot',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'desc': 'Edit with Copilot is an agentic mode in Word, Excel, and PowerPoint (web) that executes multi-step editing tasks across your entire document in one instruction — reformatting, restructuring, building formulas, generating new sections. Access: open any Office file in browser > Copilot pane > Edit with Copilot. Requires M365 Copilot licence.',
          'prompts': [
            'You are the Chief Operating Officer at Bara Jaya Mining Berhad. Using COAL_02_Mine_Safety_Manual.docx in Word for the web and the Production Log and Operating Cost per Tonne sheets in COAL_01_Mining_Operations.xlsx as the fact base, add a new section that sharpens the narrative around a rising strip ratio, recurring safety incidents, and margin pressure on export tonnes. Restructure the content into Situation, Key Data, Decisions, and Next Steps, and insert a small RAG summary box at the top.',
            'You are the Chief Financial Officer at Bara Jaya Mining Berhad. Using COAL_01_Mining_Operations.xlsx in Excel for the web, redesign the sheets fed by Strip Ratio Tracker, Safety Incident Register, and Operating Cost per Tonne so executives can see the highest-risk items first. Standardise labels, improve formulas where needed, and add a RAG status column plus a one-row summary that updates automatically.'
          ]
        },
        {
          'tool': '🤖 Word Agent',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'desc': 'Create a declarative agent scoped to a Word document. Open the .docx in Word for Web > Copilot pane > + New Agent > name it, write a description, set the document as knowledge source > Share. Colleagues chat with it in Teams or M365 Copilot.',
          'prompts': [
            'You are the Head of Sustainability at Bara Jaya Mining Berhad. Open COAL_02_Mine_Safety_Manual.docx in Word for Web and create an agent called \'Bara Jaya Mining Word Guide\'. Describe it as an assistant that answers questions using COAL_02_Mine_Safety_Manual.docx plus the Production Log and Safety Incident Register sheets in COAL_01_Mining_Operations.xlsx, then share it with the relevant leadership team.',
            'You are the Chief Financial Officer at Bara Jaya Mining Berhad. Demo the \'Bara Jaya Mining Word Guide\' agent by asking: \'What is our most urgent operating risk, what evidence from the Strip Ratio Tracker and Operating Cost per Tonne sheets supports it, and what action does COAL_02_Mine_Safety_Manual.docx imply we should take first?\'. Show the answer as a short RAG response with the supporting source references.'
          ]
        },
        {
          'tool': '🤖 PowerPoint Agent',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'desc': 'Create a declarative agent scoped to a PowerPoint presentation. Great for strategy decks or Board presentations many people need to reference. Same setup as Word Agent but using a .pptx file.',
          'prompts': [
            'You are the Chief Operating Officer at Bara Jaya Mining Berhad. Create the leadership presentation in PowerPoint for Web using COAL_01_Mining_Operations.xlsx and COAL_03_Environmental_Management_Plan.docx, then create an agent called \'Bara Jaya Mining Deck Navigator\'. Tell users it can answer questions tied to the Production Log, Export Volume Dashboard, and Operating Cost per Tonne sheets, then share it with the executive team.',
            'You are the Head of Sustainability at Bara Jaya Mining Berhad. Demo the \'Bara Jaya Mining Deck Navigator\' agent by asking: \'Which slide best explains our Red risks, what does the Operating Cost per Tonne sheet say about exposure, and what decision do leaders need this week?\'. Request a RAG answer in under 120 words.'
          ]
        },
        {
          'tool': '🤖 Excel Agent',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'desc': 'Create a declarative agent scoped to an Excel workbook. Colleagues ask data questions in plain English without opening Excel. Open .xlsx in Excel for Web > Copilot pane > + New Agent > set workbook as knowledge source > share.',
          'prompts': [
            'You are the Chief Financial Officer at Bara Jaya Mining Berhad. Open COAL_01_Mining_Operations.xlsx in Excel for Web and create an agent called \'Bara Jaya Mining Data Q&A\'. Describe it as an assistant for the Production Log, Strip Ratio Tracker, Safety Incident Register, Export Volume Dashboard, and Operating Cost per Tonne sheets that gives instant Red, Amber, and Green answers on performance and risk, then share it with the leadership team.',
            'You are the Chief Operating Officer at Bara Jaya Mining Berhad. Demo the \'Bara Jaya Mining Data Q&A\' agent by asking which 3 items are currently Red in the Production Log and Operating Cost per Tonne sheets and what management action each implies. Then ask which single Amber item could become Red fastest and why.'
          ]
        },
        {
          'tool': '🏗 Agent Builder (Copilot Studio)',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'desc': 'Build a custom declarative agent in Copilot Studio — no coding required. Access: copilotstudio.microsoft.com > Create > New Agent. Add name, description, knowledge sources (SharePoint URLs or uploaded files), topics/actions. Publish to Teams in under 10 minutes.',
          'prompts': [
            'You are the Chief Operating Officer at Bara Jaya Mining Berhad. Go to Copilot Studio and create an agent called \'Bara Jaya Mining Intelligence Agent\' using COAL_01_Mining_Operations.xlsx, COAL_02_Mine_Safety_Manual.docx, and COAL_03_Environmental_Management_Plan.docx as knowledge sources. Tell the agent to answer questions across the Production Log, Strip Ratio Tracker, Safety Incident Register, Export Volume Dashboard, and Operating Cost per Tonne sheets, add topics for Production, Safety & ESG, Export Volume, Cost per Tonne, and require every answer to end with a RAG recommendation.',
            'You are the Head of Sustainability at Bara Jaya Mining Berhad. Demo the \'Bara Jaya Mining Intelligence Agent\' by asking for a 2-minute briefing on the biggest Red issue in the Production Log and Operating Cost per Tonne sheets, the best Amber mitigation in COAL_03_Environmental_Management_Plan.docx, and the Green signals management can still rely on. Ask for the answer in a RAG table with next-step owners.'
          ]
        }
      ]
    },

    {
      'id': 'hotel-resort',
      'sectorId': 'hospitality',
      'name': 'Hotel & Resort',
      'icon': '🏨',
      'color': '#AD1457',
      'accent': '#C2185B',
      'company': 'Seri Bayu Hotels & Resorts Berhad',
      'tagline': 'RevPAR softens while guest scores and maintenance costs diverge.',
      'companyID': 'PT Resor Seri Bayu Indonesia',
      'taglineID': 'Bali demand holds, but margin leakage is widening.',
      'scenario': 'Seri Bayu Hotels & Resorts Berhad and PT Resor Seri Bayu Indonesia operate urban hotels and destination resorts across Malaysia and Indonesia. RevPAR momentum is mixed, OTA dependency remains high, guest satisfaction is uneven by property, and deferred maintenance is now visible in owner discussions. Management needs a sharper operating playbook before the next peak season and budgeting cycle.',
      'files': ['HTL_01_Property_Performance.xlsx', 'HTL_02_Brand_Standards_Manual.docx', 'HTL_03_Revenue_Management_Policy.docx'],
      'prompts': [
        {
          'tool': '🤖 Copilot Chat (Basic)',
          'license': 'Free — no M365 Copilot license needed',
          'account': 'Sasha Ouellet — SashaO@ABSx62256373.OnMicrosoft.com',
          'prompts': [
            'You are the Chief Commercial Officer at Seri Bayu Hotels & Resorts Berhad. Using HTL_01_Property_Performance.xlsx, focus on the RevPAR Dashboard, Occupancy Rate, and Maintenance Cost Tracker sheets to assess RevPAR softness, uneven guest satisfaction, and maintenance cost overruns. Quantify the immediate downside, name the 3 decisions management must take in the next 30 days, and present the answer as a RAG table with Red, Amber, and Green actions.',
            'You are the Head of Hotel Operations at Seri Bayu Hotels & Resorts Berhad. Using the F&B Revenue and Guest Satisfaction Scores sheets in HTL_01_Property_Performance.xlsx together with HTL_02_Brand_Standards_Manual.docx, explain how the current operating issue affects strategy, capital allocation, and stakeholder confidence. Present the response as a RAG memo with sections for What We Know, What We Do Not Yet Know, and What We Should Do Next.',
            'You are the Chief Financial Officer at Seri Bayu Hotels & Resorts Berhad. Using the RevPAR Dashboard and F&B Revenue sheets in HTL_01_Property_Performance.xlsx, benchmark our current position against the 2024 to 2025 Malaysia and Indonesia hotel and resort market. Summarise the 5 most important leading indicators to watch over the next 2 quarters and show them in a RAG scorecard with a short management implication beside each.'
          ]
        },
        {
          'tool': '🔍 Researcher',
          'license': 'Free — no M365 Copilot license needed',
          'account': 'Sasha Ouellet — SashaO@ABSx62256373.OnMicrosoft.com',
          'desc': 'Access via Microsoft 365 Copilot Chat > Agents > Researcher. Researcher automatically critiques every source — verifying claims against the original before including them in the report. Grounds answers in live web sources and your organisation\'s data with full citations. Faster and more reliable than manual research.',
          'prompts': [
            'You are the Head of Hotel Operations at Seri Bayu Hotels & Resorts Berhad. Using HTL_01_Property_Performance.xlsx, especially the RevPAR Dashboard, Occupancy Rate, and F&B Revenue sheets, plus HTL_02_Brand_Standards_Manual.docx, research 2024 to 2025 market benchmarks, peer disclosures, and financing or valuation signals relevant to RevPAR softness, uneven guest satisfaction, and maintenance cost overruns. Present a RAG table with Red for immediate threats, Amber for watchlist items, and Green for supporting market signals, with citations to every source and a one-line implication for management. Flag any claim that could not be independently verified.',
            'You are the Chief Commercial Officer at Seri Bayu Hotels & Resorts Berhad. Using the Guest Satisfaction Scores and Maintenance Cost Tracker sheets in HTL_01_Property_Performance.xlsx and the policy positions in HTL_03_Revenue_Management_Policy.docx, research how MyCEB and DOSM or comparable published authorities and industry bodies are treating this issue across Malaysia and Indonesia. Separate mandatory requirements from market practice, cite each source, and present the findings as a RAG matrix with columns for Issue, Malaysia, Indonesia, Timing, and Management Action. Flag any claim that could not be independently verified.',
            'You are the Chief Financial Officer at Seri Bayu Hotels & Resorts Berhad. Using the RevPAR Dashboard, F&B Revenue, and Guest Satisfaction Scores sheets in HTL_01_Property_Performance.xlsx, research the demand, pricing, and competitor trends that will most influence our next 12 months. Present the answer as a RAG table ranking the top 10 external signals by likely impact and management preparedness, with citations beside every row. Flag any claim that could not be independently verified.'
          ]
        },
        {
          'tool': '📊 Analyst',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'desc': 'Access via Microsoft 365 Copilot Chat > click Agents > Analyst. Upload an Excel or CSV file. Analyst runs Python-style analysis, builds charts, and interprets results without you writing a single formula.',
          'prompts': [
            'You are the Chief Financial Officer at Seri Bayu Hotels & Resorts Berhad. Upload HTL_01_Property_Performance.xlsx to Analyst and use the RevPAR Dashboard, Occupancy Rate, and F&B Revenue sheets to identify the 5 biggest sources of underperformance or stress in the current plan. Quantify the variance where possible, flag each item Red, Amber, or Green based on financial materiality, and end with one corrective action per Red item.',
            'You are the Chief Commercial Officer at Seri Bayu Hotels & Resorts Berhad. Upload HTL_01_Property_Performance.xlsx to Analyst and use the Guest Satisfaction Scores and Maintenance Cost Tracker sheets to model 3 scenarios for RevPAR softness, uneven guest satisfaction, and maintenance cost overruns: downside, base case, and recovery case. Show the impact on revenue, margin or cash, plus the operational trigger that would move an item from Amber to Red.',
            'You are the Head of Hotel Operations at Seri Bayu Hotels & Resorts Berhad. Upload HTL_01_Property_Performance.xlsx to Analyst and use the RevPAR Dashboard, F&B Revenue, and Maintenance Cost Tracker sheets to build a 13-week watchlist of the metrics most likely to surprise management. Present the output as a RAG dashboard table with columns for Metric, Current Level, Threshold, Risk Status, and Recommended Owner.'
          ]
        },
        {
          'tool': '📊 Copilot in Excel',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'prompts': [
            'You are the Head of Hotel Operations at Seri Bayu Hotels & Resorts Berhad. Using HTL_01_Property_Performance.xlsx, build a new sheet called \'Seri Bayu Hotels Executive Dashboard\' from the RevPAR Dashboard, Occupancy Rate, and F&B Revenue sheets. Show the 10 most important KPIs, add a RAG status column driven by clear thresholds, and place an executive summary box at the top that updates automatically.',
            'You are the Chief Commercial Officer at Seri Bayu Hotels & Resorts Berhad. Using HTL_01_Property_Performance.xlsx, create a risk tracker that pulls from the Occupancy Rate, Guest Satisfaction Scores, and Maintenance Cost Tracker sheets. For each material issue, show owner, due date, estimated financial exposure, and Red/Amber/Green status, then sort Red issues first.',
            'You are the Chief Financial Officer at Seri Bayu Hotels & Resorts Berhad. Using HTL_01_Property_Performance.xlsx, build a scenario sensitivity sheet using the RevPAR Dashboard, F&B Revenue, and Maintenance Cost Tracker sheets as inputs. Show downside, base, and upside cases side by side, add conditional formatting for RAG thresholds, and include a short note on the trigger that would require management escalation.'
          ]
        },
        {
          'tool': '📝 Copilot in Word',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'prompts': [
            'You are the Chief Commercial Officer at Seri Bayu Hotels & Resorts Berhad. Using HTL_02_Brand_Standards_Manual.docx together with the RevPAR Dashboard and Maintenance Cost Tracker sheets in HTL_01_Property_Performance.xlsx, draft a 2-page Board paper on RevPAR softness, uneven guest satisfaction, and maintenance cost overruns. Structure it as Situation, Risks, Decisions Required, and Next 30 Days, and place a compact RAG summary at the top.',
            'You are the Head of Hotel Operations at Seri Bayu Hotels & Resorts Berhad. Using HTL_03_Revenue_Management_Policy.docx and the Occupancy Rate and Guest Satisfaction Scores sheets in HTL_01_Property_Performance.xlsx, draft a policy or action-plan note for the leadership team that translates the data into clear operating actions. Present the recommendations as a RAG table with owners, timing, and expected impact.',
            'You are the Chief Financial Officer at Seri Bayu Hotels & Resorts Berhad. Using HTL_02_Brand_Standards_Manual.docx, HTL_03_Revenue_Management_Policy.docx, and the RevPAR Dashboard sheet in HTL_01_Property_Performance.xlsx, draft an external stakeholder briefing note that explains our position factually and shows what management is doing next. After the draft, add a 3-line RAG risk summary covering timing, evidence strength, and stakeholder reaction.'
          ]
        },
        {
          'tool': '🎯 Copilot in PowerPoint',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'prompts': [
            'You are the Chief Commercial Officer at Seri Bayu Hotels & Resorts Berhad. Create a 6-slide executive deck using HTL_01_Property_Performance.xlsx and HTL_02_Brand_Standards_Manual.docx, grounded in the RevPAR Dashboard, F&B Revenue, and Maintenance Cost Tracker sheets. Cover hotel & resort performance, root causes, key risks, management response, scenario outlook, and decisions required, with one headline takeaway per slide and a visible RAG status marker.',
            'You are the Head of Hotel Operations at Seri Bayu Hotels & Resorts Berhad. Create a 3-slide operating review using the Occupancy Rate, F&B Revenue, and Guest Satisfaction Scores sheets in HTL_01_Property_Performance.xlsx. Show what is Red, what is Amber, and what is Green, then close with the 5 highest-priority actions and owners.',
            'You are the Chief Financial Officer at Seri Bayu Hotels & Resorts Berhad. Build a 2-slide stakeholder briefing from HTL_01_Property_Performance.xlsx and HTL_03_Revenue_Management_Policy.docx, using the RevPAR Dashboard and Maintenance Cost Tracker sheets as the fact base. The first slide should summarise the issue and the second should show the recovery path in a RAG timeline.'
          ]
        },
        {
          'tool': '📧 Copilot in Outlook',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'prompts': [
            'You are the Chief Commercial Officer at Seri Bayu Hotels & Resorts Berhad. Using the RevPAR Dashboard and Maintenance Cost Tracker sheets in HTL_01_Property_Performance.xlsx, draft an email to hotel owners and asset managers explaining the current situation, the evidence supporting our view, and the immediate next step we want from them. After the draft, add a short RAG summary of delivery risk, likely objections, and follow-up timing.',
            'You are the Head of Hotel Operations at Seri Bayu Hotels & Resorts Berhad. Using the F&B Revenue and Guest Satisfaction Scores sheets in HTL_01_Property_Performance.xlsx plus HTL_02_Brand_Standards_Manual.docx, draft a regulator-ready note for MyCEB and DOSM or the most relevant authority. Keep the tone factual, distinguish confirmed facts from assumptions, and end with a RAG table of issues that may require further disclosure.',
            'You are the Chief Financial Officer at Seri Bayu Hotels & Resorts Berhad. Using the RevPAR Dashboard, Occupancy Rate, and F&B Revenue sheets in HTL_01_Property_Performance.xlsx, draft an internal leadership email that aligns owners around the top 5 actions for the next 14 days. Finish with a RAG checklist titled Do Today, Do This Week, and Monitor.'
          ]
        },
        {
          'tool': '🎙 Copilot in Teams',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'desc': 'Use your OWN existing recorded Teams meetings. Open a meeting recap in Teams > Recap tab. Copilot generates summaries, action items, and follow-up drafts grounded in the actual transcript.',
          'prompts': [
            'You are the Head of Hotel Operations at Seri Bayu Hotels & Resorts Berhad. Using this recorded Teams meeting recap and the RevPAR Dashboard and F&B Revenue sheets in HTL_01_Property_Performance.xlsx as the operating benchmark, extract all decisions, risks, and unresolved items related to RevPAR softness, uneven guest satisfaction, and maintenance cost overruns. Present the result as a RAG table with owners and due dates.',
            'You are the Chief Commercial Officer at Seri Bayu Hotels & Resorts Berhad. Using the Occupancy Rate and Maintenance Cost Tracker sheets in HTL_01_Property_Performance.xlsx as reference points, draft follow-up actions from the meeting grouped by Revenue Management | Operations | F&B | Guest Experience | Engineering. For each action, include owner, deadline, and whether the item is Red, Amber, or Green.',
            'You are the Chief Financial Officer at Seri Bayu Hotels & Resorts Berhad. Using this meeting recap and the Guest Satisfaction Scores sheet in HTL_01_Property_Performance.xlsx as context, identify whether any comments suggest hidden downside not yet reflected in management reporting. Summarise the findings as a RAG note with direct quotes or paraphrased evidence from the recap.'
          ]
        },
        {
          'tool': '📓 Copilot Notebook',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'desc': 'Access via copilot.microsoft.com > Notebook tab. Upload up to 5 files and set a system instruction. Best for synthesising insights across multiple documents simultaneously.',
          'prompts': [
            'You are the Chief Commercial Officer at Seri Bayu Hotels & Resorts Berhad. Upload HTL_01_Property_Performance.xlsx, HTL_02_Brand_Standards_Manual.docx, and HTL_03_Revenue_Management_Policy.docx to Copilot Notebook and focus on the RevPAR Dashboard, F&B Revenue, and Maintenance Cost Tracker sheets. Ask Notebook to produce a cross-file RAG synthesis of the top risks, the 3 most credible management actions, and the evidence supporting each recommendation, citing the source file for every major point.',
            'You are the Head of Hotel Operations at Seri Bayu Hotels & Resorts Berhad. Upload HTL_01_Property_Performance.xlsx and HTL_02_Brand_Standards_Manual.docx to Copilot Notebook and focus on the Occupancy Rate, Guest Satisfaction Scores, and Maintenance Cost Tracker sheets. Ask Notebook to model a downside scenario for RevPAR softness, uneven guest satisfaction, and maintenance cost overruns, explain which assumptions matter most, and present the answer as a RAG table with immediate, next-quarter, and monitor-only actions.',
            'You are the Chief Financial Officer at Seri Bayu Hotels & Resorts Berhad. Upload HTL_01_Property_Performance.xlsx, HTL_02_Brand_Standards_Manual.docx, and HTL_03_Revenue_Management_Policy.docx to Copilot Notebook and focus on the RevPAR Dashboard, Occupancy Rate, and Guest Satisfaction Scores sheets. Ask Notebook to rank the top 5 opportunities to stabilise performance without creating new compliance or stakeholder risk, and return the answer as a RAG prioritisation table with expected impact and implementation difficulty.'
          ]
        },
        {
          'tool': '🤝 Cowork (Frontier)',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'desc': 'Cowork is an autonomous agent that takes actions across Microsoft 365 on your behalf — sending emails, scheduling meetings, creating documents, posting in Teams, and scheduling recurring tasks. Access: m365.cloud.microsoft > left nav > Agents > Cowork. Requires Frontier program enrollment.',
          'prompts': [
            'You are the Chief Commercial Officer at Seri Bayu Hotels & Resorts Berhad. Using HTL_01_Property_Performance.xlsx, HTL_02_Brand_Standards_Manual.docx, and HTL_03_Revenue_Management_Policy.docx, especially the RevPAR Dashboard, F&B Revenue, and Maintenance Cost Tracker sheets, research the current market context, draft a 2-page management brief, save it to OneDrive, and email it to the leadership team for review. Then schedule a 30-minute follow-up meeting for next week and label the agenda items Red, Amber, and Green.',
            'You are the Head of Hotel Operations at Seri Bayu Hotels & Resorts Berhad. Using the Occupancy Rate, Guest Satisfaction Scores, and Maintenance Cost Tracker sheets in HTL_01_Property_Performance.xlsx, prepare a task tracker, draft the related stakeholder email, store both in SharePoint or OneDrive, and send them to the named owners. Then book a checkpoint meeting and make sure the work is grouped by Revenue Management | Operations | F&B | Guest Experience | Engineering with clear RAG priorities.'
          ]
        },
        {
          'tool': '✏️ Edit with Copilot',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'desc': 'Edit with Copilot is an agentic mode in Word, Excel, and PowerPoint (web) that executes multi-step editing tasks across your entire document in one instruction — reformatting, restructuring, building formulas, generating new sections. Access: open any Office file in browser > Copilot pane > Edit with Copilot. Requires M365 Copilot licence.',
          'prompts': [
            'You are the Chief Commercial Officer at Seri Bayu Hotels & Resorts Berhad. Using HTL_02_Brand_Standards_Manual.docx in Word for the web and the RevPAR Dashboard and Maintenance Cost Tracker sheets in HTL_01_Property_Performance.xlsx as the fact base, add a new section that sharpens the narrative around RevPAR softness, uneven guest satisfaction, and maintenance cost overruns. Restructure the content into Situation, Key Data, Decisions, and Next Steps, and insert a small RAG summary box at the top.',
            'You are the Chief Financial Officer at Seri Bayu Hotels & Resorts Berhad. Using HTL_01_Property_Performance.xlsx in Excel for the web, redesign the sheets fed by Occupancy Rate, F&B Revenue, and Maintenance Cost Tracker so executives can see the highest-risk items first. Standardise labels, improve formulas where needed, and add a RAG status column plus a one-row summary that updates automatically.'
          ]
        },
        {
          'tool': '🤖 Word Agent',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'desc': 'Create a declarative agent scoped to a Word document. Open the .docx in Word for Web > Copilot pane > + New Agent > name it, write a description, set the document as knowledge source > Share. Colleagues chat with it in Teams or M365 Copilot.',
          'prompts': [
            'You are the Head of Hotel Operations at Seri Bayu Hotels & Resorts Berhad. Open HTL_02_Brand_Standards_Manual.docx in Word for Web and create an agent called \'Seri Bayu Hotels Word Guide\'. Describe it as an assistant that answers questions using HTL_02_Brand_Standards_Manual.docx plus the RevPAR Dashboard and F&B Revenue sheets in HTL_01_Property_Performance.xlsx, then share it with the relevant leadership team.',
            'You are the Chief Financial Officer at Seri Bayu Hotels & Resorts Berhad. Demo the \'Seri Bayu Hotels Word Guide\' agent by asking: \'What is our most urgent operating risk, what evidence from the Occupancy Rate and Maintenance Cost Tracker sheets supports it, and what action does HTL_02_Brand_Standards_Manual.docx imply we should take first?\'. Show the answer as a short RAG response with the supporting source references.'
          ]
        },
        {
          'tool': '🤖 PowerPoint Agent',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'desc': 'Create a declarative agent scoped to a PowerPoint presentation. Great for strategy decks or Board presentations many people need to reference. Same setup as Word Agent but using a .pptx file.',
          'prompts': [
            'You are the Chief Commercial Officer at Seri Bayu Hotels & Resorts Berhad. Create the leadership presentation in PowerPoint for Web using HTL_01_Property_Performance.xlsx and HTL_03_Revenue_Management_Policy.docx, then create an agent called \'Seri Bayu Hotels Deck Navigator\'. Tell users it can answer questions tied to the RevPAR Dashboard, Guest Satisfaction Scores, and Maintenance Cost Tracker sheets, then share it with the executive team.',
            'You are the Head of Hotel Operations at Seri Bayu Hotels & Resorts Berhad. Demo the \'Seri Bayu Hotels Deck Navigator\' agent by asking: \'Which slide best explains our Red risks, what does the Maintenance Cost Tracker sheet say about exposure, and what decision do leaders need this week?\'. Request a RAG answer in under 120 words.'
          ]
        },
        {
          'tool': '🤖 Excel Agent',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'desc': 'Create a declarative agent scoped to an Excel workbook. Colleagues ask data questions in plain English without opening Excel. Open .xlsx in Excel for Web > Copilot pane > + New Agent > set workbook as knowledge source > share.',
          'prompts': [
            'You are the Chief Financial Officer at Seri Bayu Hotels & Resorts Berhad. Open HTL_01_Property_Performance.xlsx in Excel for Web and create an agent called \'Seri Bayu Hotels Data Q&A\'. Describe it as an assistant for the RevPAR Dashboard, Occupancy Rate, F&B Revenue, Guest Satisfaction Scores, and Maintenance Cost Tracker sheets that gives instant Red, Amber, and Green answers on performance and risk, then share it with the leadership team.',
            'You are the Chief Commercial Officer at Seri Bayu Hotels & Resorts Berhad. Demo the \'Seri Bayu Hotels Data Q&A\' agent by asking which 3 items are currently Red in the RevPAR Dashboard and Maintenance Cost Tracker sheets and what management action each implies. Then ask which single Amber item could become Red fastest and why.'
          ]
        },
        {
          'tool': '🏗 Agent Builder (Copilot Studio)',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'desc': 'Build a custom declarative agent in Copilot Studio — no coding required. Access: copilotstudio.microsoft.com > Create > New Agent. Add name, description, knowledge sources (SharePoint URLs or uploaded files), topics/actions. Publish to Teams in under 10 minutes.',
          'prompts': [
            'You are the Chief Commercial Officer at Seri Bayu Hotels & Resorts Berhad. Go to Copilot Studio and create an agent called \'Seri Bayu Hotels Intelligence Agent\' using HTL_01_Property_Performance.xlsx, HTL_02_Brand_Standards_Manual.docx, and HTL_03_Revenue_Management_Policy.docx as knowledge sources. Tell the agent to answer questions across the RevPAR Dashboard, Occupancy Rate, F&B Revenue, Guest Satisfaction Scores, and Maintenance Cost Tracker sheets, add topics for RevPAR & Occupancy, F&B Performance, Guest Experience, Maintenance Costs, and require every answer to end with a RAG recommendation.',
            'You are the Head of Hotel Operations at Seri Bayu Hotels & Resorts Berhad. Demo the \'Seri Bayu Hotels Intelligence Agent\' by asking for a 2-minute briefing on the biggest Red issue in the RevPAR Dashboard and Maintenance Cost Tracker sheets, the best Amber mitigation in HTL_03_Revenue_Management_Policy.docx, and the Green signals management can still rely on. Ask for the answer in a RAG table with next-step owners.'
          ]
        }
      ]
    }
]

print(f"Batch 7 written: {len(INDUSTRIES_7)} entries")

