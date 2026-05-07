import sys; sys.path.insert(0,'.')
from util import *

INDUSTRIES_8 = [

    {
      'id': 'construction',
      'sectorId': 'construction',
      'name': 'Construction',
      'icon': '🏗',
      'color': '#E65100',
      'accent': '#F57C00',
      'company': 'Wawasan Bina Infra Berhad',
      'tagline': 'Variation orders, site safety, and cash flow now define tender credibility.',
      'companyID': 'PT Wawasan Konstruksi Nusantara Tbk',
      'taglineID': 'PUPR-facing delivery risk rises as claims and compliance backlog widen.',
      'scenario': 'Wawasan Bina Infra Berhad and PT Wawasan Konstruksi Nusantara Tbk deliver civil, building, and infrastructure packages across Malaysia and Indonesia. Variation orders are stacking up, subcontractor performance is uneven, and safety incidents are raising questions about execution discipline on current jobs and upcoming tenders. Management needs tighter project controls and a clearer client narrative before more cash is trapped in disputes.',
      'files': ['CON_01_Project_Portfolio.xlsx', 'CON_02_Project_Management_Manual.docx', 'CON_03_HSE_Policy.docx'],
      'prompts': [
        {
          'tool': '🤖 Copilot Chat (Basic)',
          'license': 'Free — no M365 Copilot license needed',
          'account': 'Sasha Ouellet — SashaO@ABSx62256373.OnMicrosoft.com',
          'prompts': [
            'You are the Chief Executive Officer at Wawasan Bina Infra Berhad. Using CON_01_Project_Portfolio.xlsx, focus on the Project Status Dashboard, Variation Order Log, and Safety Incident Register sheets to assess variation-order disputes, cash-flow strain, and recurring safety incidents. Quantify the immediate downside, name the 3 decisions management must take in the next 30 days, and present the answer as a RAG table with Red, Amber, and Green actions.',
            'You are the Head of Projects at Wawasan Bina Infra Berhad. Using the Cash Flow Tracker and Subcontractor Performance sheets in CON_01_Project_Portfolio.xlsx together with CON_02_Project_Management_Manual.docx, explain how the current operating issue affects strategy, capital allocation, and stakeholder confidence. Present the response as a RAG memo with sections for What We Know, What We Do Not Yet Know, and What We Should Do Next.',
            'You are the Chief Financial Officer at Wawasan Bina Infra Berhad. Using the Project Status Dashboard and Cash Flow Tracker sheets in CON_01_Project_Portfolio.xlsx, benchmark our current position against the 2024 to 2025 Malaysia and Indonesia infrastructure and building construction market. Summarise the 5 most important leading indicators to watch over the next 2 quarters and show them in a RAG scorecard with a short management implication beside each.'
          ]
        },
        {
          'tool': '🔍 Researcher',
          'license': 'Free — no M365 Copilot license needed',
          'account': 'Sasha Ouellet — SashaO@ABSx62256373.OnMicrosoft.com',
          'desc': 'Access via Microsoft 365 Copilot Chat > Agents > Researcher. Researcher automatically critiques every source — verifying claims against the original before including them in the report. Grounds answers in live web sources and your organisation\'s data with full citations. Faster and more reliable than manual research.',
          'prompts': [
            'You are the Head of Projects at Wawasan Bina Infra Berhad. Using CON_01_Project_Portfolio.xlsx, especially the Project Status Dashboard, Variation Order Log, and Cash Flow Tracker sheets, plus CON_02_Project_Management_Manual.docx, research 2024 to 2025 market benchmarks, peer disclosures, and financing or valuation signals relevant to variation-order disputes, cash-flow strain, and recurring safety incidents. Present a RAG table with Red for immediate threats, Amber for watchlist items, and Green for supporting market signals, with citations to every source and a one-line implication for management. Flag any claim that could not be independently verified.',
            'You are the Chief Executive Officer at Wawasan Bina Infra Berhad. Using the Subcontractor Performance and Safety Incident Register sheets in CON_01_Project_Portfolio.xlsx and the policy positions in CON_03_HSE_Policy.docx, research how Kementerian PUPR and SIRIM or comparable published authorities and industry bodies are treating this issue across Malaysia and Indonesia. Separate mandatory requirements from market practice, cite each source, and present the findings as a RAG matrix with columns for Issue, Malaysia, Indonesia, Timing, and Management Action. Flag any claim that could not be independently verified.',
            'You are the Chief Financial Officer at Wawasan Bina Infra Berhad. Using the Project Status Dashboard, Cash Flow Tracker, and Subcontractor Performance sheets in CON_01_Project_Portfolio.xlsx, research the demand, pricing, and competitor trends that will most influence our next 12 months. Present the answer as a RAG table ranking the top 10 external signals by likely impact and management preparedness, with citations beside every row. Flag any claim that could not be independently verified.'
          ]
        },
        {
          'tool': '📊 Analyst',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'desc': 'Access via Microsoft 365 Copilot Chat > click Agents > Analyst. Upload an Excel or CSV file. Analyst runs Python-style analysis, builds charts, and interprets results without you writing a single formula.',
          'prompts': [
            'You are the Chief Financial Officer at Wawasan Bina Infra Berhad. Upload CON_01_Project_Portfolio.xlsx to Analyst and use the Project Status Dashboard, Variation Order Log, and Cash Flow Tracker sheets to identify the 5 biggest sources of underperformance or stress in the current plan. Quantify the variance where possible, flag each item Red, Amber, or Green based on financial materiality, and end with one corrective action per Red item.',
            'You are the Chief Executive Officer at Wawasan Bina Infra Berhad. Upload CON_01_Project_Portfolio.xlsx to Analyst and use the Subcontractor Performance and Safety Incident Register sheets to model 3 scenarios for variation-order disputes, cash-flow strain, and recurring safety incidents: downside, base case, and recovery case. Show the impact on revenue, margin or cash, plus the operational trigger that would move an item from Amber to Red.',
            'You are the Head of Projects at Wawasan Bina Infra Berhad. Upload CON_01_Project_Portfolio.xlsx to Analyst and use the Project Status Dashboard, Cash Flow Tracker, and Safety Incident Register sheets to build a 13-week watchlist of the metrics most likely to surprise management. Present the output as a RAG dashboard table with columns for Metric, Current Level, Threshold, Risk Status, and Recommended Owner.'
          ]
        },
        {
          'tool': '📊 Copilot in Excel',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'prompts': [
            'You are the Head of Projects at Wawasan Bina Infra Berhad. Using CON_01_Project_Portfolio.xlsx, build a new sheet called \'Wawasan Bina Executive Dashboard\' from the Project Status Dashboard, Variation Order Log, and Cash Flow Tracker sheets. Show the 10 most important KPIs, add a RAG status column driven by clear thresholds, and place an executive summary box at the top that updates automatically.',
            'You are the Chief Executive Officer at Wawasan Bina Infra Berhad. Using CON_01_Project_Portfolio.xlsx, create a risk tracker that pulls from the Variation Order Log, Subcontractor Performance, and Safety Incident Register sheets. For each material issue, show owner, due date, estimated financial exposure, and Red/Amber/Green status, then sort Red issues first.',
            'You are the Chief Financial Officer at Wawasan Bina Infra Berhad. Using CON_01_Project_Portfolio.xlsx, build a scenario sensitivity sheet using the Project Status Dashboard, Cash Flow Tracker, and Safety Incident Register sheets as inputs. Show downside, base, and upside cases side by side, add conditional formatting for RAG thresholds, and include a short note on the trigger that would require management escalation.'
          ]
        },
        {
          'tool': '📝 Copilot in Word',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'prompts': [
            'You are the Chief Executive Officer at Wawasan Bina Infra Berhad. Using CON_02_Project_Management_Manual.docx together with the Project Status Dashboard and Safety Incident Register sheets in CON_01_Project_Portfolio.xlsx, draft a 2-page Board paper on variation-order disputes, cash-flow strain, and recurring safety incidents. Structure it as Situation, Risks, Decisions Required, and Next 30 Days, and place a compact RAG summary at the top.',
            'You are the Head of Projects at Wawasan Bina Infra Berhad. Using CON_03_HSE_Policy.docx and the Variation Order Log and Subcontractor Performance sheets in CON_01_Project_Portfolio.xlsx, draft a policy or action-plan note for the leadership team that translates the data into clear operating actions. Present the recommendations as a RAG table with owners, timing, and expected impact.',
            'You are the Chief Financial Officer at Wawasan Bina Infra Berhad. Using CON_02_Project_Management_Manual.docx, CON_03_HSE_Policy.docx, and the Project Status Dashboard sheet in CON_01_Project_Portfolio.xlsx, draft an external stakeholder briefing note that explains our position factually and shows what management is doing next. After the draft, add a 3-line RAG risk summary covering timing, evidence strength, and stakeholder reaction.'
          ]
        },
        {
          'tool': '🎯 Copilot in PowerPoint',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'prompts': [
            'You are the Chief Executive Officer at Wawasan Bina Infra Berhad. Create a 6-slide executive deck using CON_01_Project_Portfolio.xlsx and CON_02_Project_Management_Manual.docx, grounded in the Project Status Dashboard, Cash Flow Tracker, and Safety Incident Register sheets. Cover construction performance, root causes, key risks, management response, scenario outlook, and decisions required, with one headline takeaway per slide and a visible RAG status marker.',
            'You are the Head of Projects at Wawasan Bina Infra Berhad. Create a 3-slide operating review using the Variation Order Log, Cash Flow Tracker, and Subcontractor Performance sheets in CON_01_Project_Portfolio.xlsx. Show what is Red, what is Amber, and what is Green, then close with the 5 highest-priority actions and owners.',
            'You are the Chief Financial Officer at Wawasan Bina Infra Berhad. Build a 2-slide stakeholder briefing from CON_01_Project_Portfolio.xlsx and CON_03_HSE_Policy.docx, using the Project Status Dashboard and Safety Incident Register sheets as the fact base. The first slide should summarise the issue and the second should show the recovery path in a RAG timeline.'
          ]
        },
        {
          'tool': '📧 Copilot in Outlook',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'prompts': [
            'You are the Chief Executive Officer at Wawasan Bina Infra Berhad. Using the Project Status Dashboard and Safety Incident Register sheets in CON_01_Project_Portfolio.xlsx, draft an email to major clients, project lenders, and bond providers explaining the current situation, the evidence supporting our view, and the immediate next step we want from them. After the draft, add a short RAG summary of delivery risk, likely objections, and follow-up timing.',
            'You are the Head of Projects at Wawasan Bina Infra Berhad. Using the Cash Flow Tracker and Subcontractor Performance sheets in CON_01_Project_Portfolio.xlsx plus CON_02_Project_Management_Manual.docx, draft a regulator-ready note for Kementerian PUPR and SIRIM or the most relevant authority. Keep the tone factual, distinguish confirmed facts from assumptions, and end with a RAG table of issues that may require further disclosure.',
            'You are the Chief Financial Officer at Wawasan Bina Infra Berhad. Using the Project Status Dashboard, Variation Order Log, and Cash Flow Tracker sheets in CON_01_Project_Portfolio.xlsx, draft an internal leadership email that aligns owners around the top 5 actions for the next 14 days. Finish with a RAG checklist titled Do Today, Do This Week, and Monitor.'
          ]
        },
        {
          'tool': '🎙 Copilot in Teams',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'desc': 'Use your OWN existing recorded Teams meetings. Open a meeting recap in Teams > Recap tab. Copilot generates summaries, action items, and follow-up drafts grounded in the actual transcript.',
          'prompts': [
            'You are the Head of Projects at Wawasan Bina Infra Berhad. Using this recorded Teams meeting recap and the Project Status Dashboard and Cash Flow Tracker sheets in CON_01_Project_Portfolio.xlsx as the operating benchmark, extract all decisions, risks, and unresolved items related to variation-order disputes, cash-flow strain, and recurring safety incidents. Present the result as a RAG table with owners and due dates.',
            'You are the Chief Executive Officer at Wawasan Bina Infra Berhad. Using the Variation Order Log and Safety Incident Register sheets in CON_01_Project_Portfolio.xlsx as reference points, draft follow-up actions from the meeting grouped by Project Controls | Commercial | HSE | Procurement | Client Management. For each action, include owner, deadline, and whether the item is Red, Amber, or Green.',
            'You are the Chief Financial Officer at Wawasan Bina Infra Berhad. Using this meeting recap and the Subcontractor Performance sheet in CON_01_Project_Portfolio.xlsx as context, identify whether any comments suggest hidden downside not yet reflected in management reporting. Summarise the findings as a RAG note with direct quotes or paraphrased evidence from the recap.'
          ]
        },
        {
          'tool': '📓 Copilot Notebook',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'desc': 'Access via copilot.microsoft.com > Notebook tab. Upload up to 5 files and set a system instruction. Best for synthesising insights across multiple documents simultaneously.',
          'prompts': [
            'You are the Chief Executive Officer at Wawasan Bina Infra Berhad. Upload CON_01_Project_Portfolio.xlsx, CON_02_Project_Management_Manual.docx, and CON_03_HSE_Policy.docx to Copilot Notebook and focus on the Project Status Dashboard, Cash Flow Tracker, and Safety Incident Register sheets. Ask Notebook to produce a cross-file RAG synthesis of the top risks, the 3 most credible management actions, and the evidence supporting each recommendation, citing the source file for every major point.',
            'You are the Head of Projects at Wawasan Bina Infra Berhad. Upload CON_01_Project_Portfolio.xlsx and CON_02_Project_Management_Manual.docx to Copilot Notebook and focus on the Variation Order Log, Subcontractor Performance, and Safety Incident Register sheets. Ask Notebook to model a downside scenario for variation-order disputes, cash-flow strain, and recurring safety incidents, explain which assumptions matter most, and present the answer as a RAG table with immediate, next-quarter, and monitor-only actions.',
            'You are the Chief Financial Officer at Wawasan Bina Infra Berhad. Upload CON_01_Project_Portfolio.xlsx, CON_02_Project_Management_Manual.docx, and CON_03_HSE_Policy.docx to Copilot Notebook and focus on the Project Status Dashboard, Variation Order Log, and Subcontractor Performance sheets. Ask Notebook to rank the top 5 opportunities to stabilise performance without creating new compliance or stakeholder risk, and return the answer as a RAG prioritisation table with expected impact and implementation difficulty.'
          ]
        },
        {
          'tool': '🤝 Cowork (Frontier)',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'desc': 'Cowork is an autonomous agent that takes actions across Microsoft 365 on your behalf — sending emails, scheduling meetings, creating documents, posting in Teams, and scheduling recurring tasks. Access: m365.cloud.microsoft > left nav > Agents > Cowork. Requires Frontier program enrollment.',
          'prompts': [
            'You are the Chief Executive Officer at Wawasan Bina Infra Berhad. Using CON_01_Project_Portfolio.xlsx, CON_02_Project_Management_Manual.docx, and CON_03_HSE_Policy.docx, especially the Project Status Dashboard, Cash Flow Tracker, and Safety Incident Register sheets, research the current market context, draft a 2-page management brief, save it to OneDrive, and email it to the leadership team for review. Then schedule a 30-minute follow-up meeting for next week and label the agenda items Red, Amber, and Green.',
            'You are the Head of Projects at Wawasan Bina Infra Berhad. Using the Variation Order Log, Subcontractor Performance, and Safety Incident Register sheets in CON_01_Project_Portfolio.xlsx, prepare a task tracker, draft the related stakeholder email, store both in SharePoint or OneDrive, and send them to the named owners. Then book a checkpoint meeting and make sure the work is grouped by Project Controls | Commercial | HSE | Procurement | Client Management with clear RAG priorities.'
          ]
        },
        {
          'tool': '✏️ Edit with Copilot',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'desc': 'Edit with Copilot is an agentic mode in Word, Excel, and PowerPoint (web) that executes multi-step editing tasks across your entire document in one instruction — reformatting, restructuring, building formulas, generating new sections. Access: open any Office file in browser > Copilot pane > Edit with Copilot. Requires M365 Copilot licence.',
          'prompts': [
            'You are the Chief Executive Officer at Wawasan Bina Infra Berhad. Using CON_02_Project_Management_Manual.docx in Word for the web and the Project Status Dashboard and Safety Incident Register sheets in CON_01_Project_Portfolio.xlsx as the fact base, add a new section that sharpens the narrative around variation-order disputes, cash-flow strain, and recurring safety incidents. Restructure the content into Situation, Key Data, Decisions, and Next Steps, and insert a small RAG summary box at the top.',
            'You are the Chief Financial Officer at Wawasan Bina Infra Berhad. Using CON_01_Project_Portfolio.xlsx in Excel for the web, redesign the sheets fed by Variation Order Log, Cash Flow Tracker, and Safety Incident Register so executives can see the highest-risk items first. Standardise labels, improve formulas where needed, and add a RAG status column plus a one-row summary that updates automatically.'
          ]
        },
        {
          'tool': '🤖 Word Agent',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'desc': 'Create a declarative agent scoped to a Word document. Open the .docx in Word for Web > Copilot pane > + New Agent > name it, write a description, set the document as knowledge source > Share. Colleagues chat with it in Teams or M365 Copilot.',
          'prompts': [
            'You are the Head of Projects at Wawasan Bina Infra Berhad. Open CON_02_Project_Management_Manual.docx in Word for Web and create an agent called \'Wawasan Bina Word Guide\'. Describe it as an assistant that answers questions using CON_02_Project_Management_Manual.docx plus the Project Status Dashboard and Cash Flow Tracker sheets in CON_01_Project_Portfolio.xlsx, then share it with the relevant leadership team.',
            'You are the Chief Financial Officer at Wawasan Bina Infra Berhad. Demo the \'Wawasan Bina Word Guide\' agent by asking: \'What is our most urgent operating risk, what evidence from the Variation Order Log and Safety Incident Register sheets supports it, and what action does CON_02_Project_Management_Manual.docx imply we should take first?\'. Show the answer as a short RAG response with the supporting source references.'
          ]
        },
        {
          'tool': '🤖 PowerPoint Agent',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'desc': 'Create a declarative agent scoped to a PowerPoint presentation. Great for strategy decks or Board presentations many people need to reference. Same setup as Word Agent but using a .pptx file.',
          'prompts': [
            'You are the Chief Executive Officer at Wawasan Bina Infra Berhad. Create the leadership presentation in PowerPoint for Web using CON_01_Project_Portfolio.xlsx and CON_03_HSE_Policy.docx, then create an agent called \'Wawasan Bina Deck Navigator\'. Tell users it can answer questions tied to the Project Status Dashboard, Subcontractor Performance, and Safety Incident Register sheets, then share it with the executive team.',
            'You are the Head of Projects at Wawasan Bina Infra Berhad. Demo the \'Wawasan Bina Deck Navigator\' agent by asking: \'Which slide best explains our Red risks, what does the Safety Incident Register sheet say about exposure, and what decision do leaders need this week?\'. Request a RAG answer in under 120 words.'
          ]
        },
        {
          'tool': '🤖 Excel Agent',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'desc': 'Create a declarative agent scoped to an Excel workbook. Colleagues ask data questions in plain English without opening Excel. Open .xlsx in Excel for Web > Copilot pane > + New Agent > set workbook as knowledge source > share.',
          'prompts': [
            'You are the Chief Financial Officer at Wawasan Bina Infra Berhad. Open CON_01_Project_Portfolio.xlsx in Excel for Web and create an agent called \'Wawasan Bina Data Q&A\'. Describe it as an assistant for the Project Status Dashboard, Variation Order Log, Cash Flow Tracker, Subcontractor Performance, and Safety Incident Register sheets that gives instant Red, Amber, and Green answers on performance and risk, then share it with the leadership team.',
            'You are the Chief Executive Officer at Wawasan Bina Infra Berhad. Demo the \'Wawasan Bina Data Q&A\' agent by asking which 3 items are currently Red in the Project Status Dashboard and Safety Incident Register sheets and what management action each implies. Then ask which single Amber item could become Red fastest and why.'
          ]
        },
        {
          'tool': '🏗 Agent Builder (Copilot Studio)',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'desc': 'Build a custom declarative agent in Copilot Studio — no coding required. Access: copilotstudio.microsoft.com > Create > New Agent. Add name, description, knowledge sources (SharePoint URLs or uploaded files), topics/actions. Publish to Teams in under 10 minutes.',
          'prompts': [
            'You are the Chief Executive Officer at Wawasan Bina Infra Berhad. Go to Copilot Studio and create an agent called \'Wawasan Bina Intelligence Agent\' using CON_01_Project_Portfolio.xlsx, CON_02_Project_Management_Manual.docx, and CON_03_HSE_Policy.docx as knowledge sources. Tell the agent to answer questions across the Project Status Dashboard, Variation Order Log, Cash Flow Tracker, Subcontractor Performance, and Safety Incident Register sheets, add topics for Project Status, Variation Orders, Cash Flow, Safety Incidents, and require every answer to end with a RAG recommendation.',
            'You are the Head of Projects at Wawasan Bina Infra Berhad. Demo the \'Wawasan Bina Intelligence Agent\' by asking for a 2-minute briefing on the biggest Red issue in the Project Status Dashboard and Safety Incident Register sheets, the best Amber mitigation in CON_03_HSE_Policy.docx, and the Green signals management can still rely on. Ask for the answer in a RAG table with next-step owners.'
          ]
        }
      ]
    },

    {
      'id': 'aviation-airports',
      'sectorId': 'aviation',
      'name': 'Aviation & Airports',
      'icon': '✈️',
      'color': '#01579B',
      'accent': '#0277BD',
      'company': 'Cakrawala Airport Holdings Berhad',
      'tagline': 'Charge review and terminal expansion timing drive the next earnings cycle.',
      'companyID': 'PT Cakrawala Bandar Udara Tbk',
      'taglineID': 'Route recovery is improving, but capex recovery and compliance timing remain tight.',
      'scenario': 'Cakrawala Airport Holdings Berhad and PT Cakrawala Bandar Udara Tbk manage gateway airports serving business and leisure traffic. Passenger throughput is recovering, but aeronautical charge settings, non-aero monetisation, and expansion timing are all moving at different speeds under close regulatory attention. Management needs a fact-based position for regulators, airlines, and investors before the next tariff and capex review cycle.',
      'files': ['AVN_01_Airport_Operations.xlsx', 'AVN_02_Airport_Concession_Policy.docx', 'AVN_03_Emergency_Response_Plan.docx'],
      'prompts': [
        {
          'tool': '🤖 Copilot Chat (Basic)',
          'license': 'Free — no M365 Copilot license needed',
          'account': 'Sasha Ouellet — SashaO@ABSx62256373.OnMicrosoft.com',
          'prompts': [
            'You are the Chief Financial Officer at Cakrawala Airport Holdings Berhad. Using AVN_01_Airport_Operations.xlsx, focus on the Passenger Volume, Flight Movement Log, and Safety Compliance Score sheets to assess passenger recovery volatility, aeronautical charge review pressure, and expansion timing risk. Quantify the immediate downside, name the 3 decisions management must take in the next 30 days, and present the answer as a RAG table with Red, Amber, and Green actions.',
            'You are the Head of Airport Operations at Cakrawala Airport Holdings Berhad. Using the Aeronautical Revenue and Non-Aero Revenue sheets in AVN_01_Airport_Operations.xlsx together with AVN_02_Airport_Concession_Policy.docx, explain how the current operating issue affects strategy, capital allocation, and stakeholder confidence. Present the response as a RAG memo with sections for What We Know, What We Do Not Yet Know, and What We Should Do Next.',
            'You are the Head of Strategy at Cakrawala Airport Holdings Berhad. Using the Passenger Volume and Aeronautical Revenue sheets in AVN_01_Airport_Operations.xlsx, benchmark our current position against the 2024 to 2025 regional airport and aviation infrastructure market. Summarise the 5 most important leading indicators to watch over the next 2 quarters and show them in a RAG scorecard with a short management implication beside each.'
          ]
        },
        {
          'tool': '🔍 Researcher',
          'license': 'Free — no M365 Copilot license needed',
          'account': 'Sasha Ouellet — SashaO@ABSx62256373.OnMicrosoft.com',
          'desc': 'Access via Microsoft 365 Copilot Chat > Agents > Researcher. Researcher automatically critiques every source — verifying claims against the original before including them in the report. Grounds answers in live web sources and your organisation\'s data with full citations. Faster and more reliable than manual research.',
          'prompts': [
            'You are the Head of Airport Operations at Cakrawala Airport Holdings Berhad. Using AVN_01_Airport_Operations.xlsx, especially the Passenger Volume, Flight Movement Log, and Aeronautical Revenue sheets, plus AVN_02_Airport_Concession_Policy.docx, research 2024 to 2025 market benchmarks, peer disclosures, and financing or valuation signals relevant to passenger recovery volatility, aeronautical charge review pressure, and expansion timing risk. Present a RAG table with Red for immediate threats, Amber for watchlist items, and Green for supporting market signals, with citations to every source and a one-line implication for management. Flag any claim that could not be independently verified.',
            'You are the Chief Financial Officer at Cakrawala Airport Holdings Berhad. Using the Non-Aero Revenue and Safety Compliance Score sheets in AVN_01_Airport_Operations.xlsx and the policy positions in AVN_03_Emergency_Response_Plan.docx, research how CAAM, MAVCOM, and DGCA/DJPU or comparable published authorities and industry bodies are treating this issue across Malaysia and Indonesia. Separate mandatory requirements from market practice, cite each source, and present the findings as a RAG matrix with columns for Issue, Malaysia, Indonesia, Timing, and Management Action. Flag any claim that could not be independently verified.',
            'You are the Head of Strategy at Cakrawala Airport Holdings Berhad. Using the Passenger Volume, Aeronautical Revenue, and Non-Aero Revenue sheets in AVN_01_Airport_Operations.xlsx, research the demand, pricing, and competitor trends that will most influence our next 12 months. Present the answer as a RAG table ranking the top 10 external signals by likely impact and management preparedness, with citations beside every row. Flag any claim that could not be independently verified.'
          ]
        },
        {
          'tool': '📊 Analyst',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'desc': 'Access via Microsoft 365 Copilot Chat > click Agents > Analyst. Upload an Excel or CSV file. Analyst runs Python-style analysis, builds charts, and interprets results without you writing a single formula.',
          'prompts': [
            'You are the Head of Strategy at Cakrawala Airport Holdings Berhad. Upload AVN_01_Airport_Operations.xlsx to Analyst and use the Passenger Volume, Flight Movement Log, and Aeronautical Revenue sheets to identify the 5 biggest sources of underperformance or stress in the current plan. Quantify the variance where possible, flag each item Red, Amber, or Green based on financial materiality, and end with one corrective action per Red item.',
            'You are the Chief Financial Officer at Cakrawala Airport Holdings Berhad. Upload AVN_01_Airport_Operations.xlsx to Analyst and use the Non-Aero Revenue and Safety Compliance Score sheets to model 3 scenarios for passenger recovery volatility, aeronautical charge review pressure, and expansion timing risk: downside, base case, and recovery case. Show the impact on revenue, margin or cash, plus the operational trigger that would move an item from Amber to Red.',
            'You are the Head of Airport Operations at Cakrawala Airport Holdings Berhad. Upload AVN_01_Airport_Operations.xlsx to Analyst and use the Passenger Volume, Aeronautical Revenue, and Safety Compliance Score sheets to build a 13-week watchlist of the metrics most likely to surprise management. Present the output as a RAG dashboard table with columns for Metric, Current Level, Threshold, Risk Status, and Recommended Owner.'
          ]
        },
        {
          'tool': '📊 Copilot in Excel',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'prompts': [
            'You are the Head of Airport Operations at Cakrawala Airport Holdings Berhad. Using AVN_01_Airport_Operations.xlsx, build a new sheet called \'Cakrawala Airport Executive Dashboard\' from the Passenger Volume, Flight Movement Log, and Aeronautical Revenue sheets. Show the 10 most important KPIs, add a RAG status column driven by clear thresholds, and place an executive summary box at the top that updates automatically.',
            'You are the Chief Financial Officer at Cakrawala Airport Holdings Berhad. Using AVN_01_Airport_Operations.xlsx, create a risk tracker that pulls from the Flight Movement Log, Non-Aero Revenue, and Safety Compliance Score sheets. For each material issue, show owner, due date, estimated financial exposure, and Red/Amber/Green status, then sort Red issues first.',
            'You are the Head of Strategy at Cakrawala Airport Holdings Berhad. Using AVN_01_Airport_Operations.xlsx, build a scenario sensitivity sheet using the Passenger Volume, Aeronautical Revenue, and Safety Compliance Score sheets as inputs. Show downside, base, and upside cases side by side, add conditional formatting for RAG thresholds, and include a short note on the trigger that would require management escalation.'
          ]
        },
        {
          'tool': '📝 Copilot in Word',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'prompts': [
            'You are the Chief Financial Officer at Cakrawala Airport Holdings Berhad. Using AVN_02_Airport_Concession_Policy.docx together with the Passenger Volume and Safety Compliance Score sheets in AVN_01_Airport_Operations.xlsx, draft a 2-page Board paper on passenger recovery volatility, aeronautical charge review pressure, and expansion timing risk. Structure it as Situation, Risks, Decisions Required, and Next 30 Days, and place a compact RAG summary at the top.',
            'You are the Head of Airport Operations at Cakrawala Airport Holdings Berhad. Using AVN_03_Emergency_Response_Plan.docx and the Flight Movement Log and Non-Aero Revenue sheets in AVN_01_Airport_Operations.xlsx, draft a policy or action-plan note for the leadership team that translates the data into clear operating actions. Present the recommendations as a RAG table with owners, timing, and expected impact.',
            'You are the Head of Strategy at Cakrawala Airport Holdings Berhad. Using AVN_02_Airport_Concession_Policy.docx, AVN_03_Emergency_Response_Plan.docx, and the Passenger Volume sheet in AVN_01_Airport_Operations.xlsx, draft an external stakeholder briefing note that explains our position factually and shows what management is doing next. After the draft, add a 3-line RAG risk summary covering timing, evidence strength, and stakeholder reaction.'
          ]
        },
        {
          'tool': '🎯 Copilot in PowerPoint',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'prompts': [
            'You are the Chief Financial Officer at Cakrawala Airport Holdings Berhad. Create a 6-slide executive deck using AVN_01_Airport_Operations.xlsx and AVN_02_Airport_Concession_Policy.docx, grounded in the Passenger Volume, Aeronautical Revenue, and Safety Compliance Score sheets. Cover aviation & airports performance, root causes, key risks, management response, scenario outlook, and decisions required, with one headline takeaway per slide and a visible RAG status marker.',
            'You are the Head of Airport Operations at Cakrawala Airport Holdings Berhad. Create a 3-slide operating review using the Flight Movement Log, Aeronautical Revenue, and Non-Aero Revenue sheets in AVN_01_Airport_Operations.xlsx. Show what is Red, what is Amber, and what is Green, then close with the 5 highest-priority actions and owners.',
            'You are the Head of Strategy at Cakrawala Airport Holdings Berhad. Build a 2-slide stakeholder briefing from AVN_01_Airport_Operations.xlsx and AVN_03_Emergency_Response_Plan.docx, using the Passenger Volume and Safety Compliance Score sheets as the fact base. The first slide should summarise the issue and the second should show the recovery path in a RAG timeline.'
          ]
        },
        {
          'tool': '📧 Copilot in Outlook',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'prompts': [
            'You are the Chief Financial Officer at Cakrawala Airport Holdings Berhad. Using the Passenger Volume and Safety Compliance Score sheets in AVN_01_Airport_Operations.xlsx, draft an email to airlines, regulators, and infrastructure investors explaining the current situation, the evidence supporting our view, and the immediate next step we want from them. After the draft, add a short RAG summary of delivery risk, likely objections, and follow-up timing.',
            'You are the Head of Airport Operations at Cakrawala Airport Holdings Berhad. Using the Aeronautical Revenue and Non-Aero Revenue sheets in AVN_01_Airport_Operations.xlsx plus AVN_02_Airport_Concession_Policy.docx, draft a regulator-ready note for CAAM, MAVCOM, and DGCA/DJPU or the most relevant authority. Keep the tone factual, distinguish confirmed facts from assumptions, and end with a RAG table of issues that may require further disclosure.',
            'You are the Head of Strategy at Cakrawala Airport Holdings Berhad. Using the Passenger Volume, Flight Movement Log, and Aeronautical Revenue sheets in AVN_01_Airport_Operations.xlsx, draft an internal leadership email that aligns owners around the top 5 actions for the next 14 days. Finish with a RAG checklist titled Do Today, Do This Week, and Monitor.'
          ]
        },
        {
          'tool': '🎙 Copilot in Teams',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'desc': 'Use your OWN existing recorded Teams meetings. Open a meeting recap in Teams > Recap tab. Copilot generates summaries, action items, and follow-up drafts grounded in the actual transcript.',
          'prompts': [
            'You are the Head of Airport Operations at Cakrawala Airport Holdings Berhad. Using this recorded Teams meeting recap and the Passenger Volume and Aeronautical Revenue sheets in AVN_01_Airport_Operations.xlsx as the operating benchmark, extract all decisions, risks, and unresolved items related to passenger recovery volatility, aeronautical charge review pressure, and expansion timing risk. Present the result as a RAG table with owners and due dates.',
            'You are the Chief Financial Officer at Cakrawala Airport Holdings Berhad. Using the Flight Movement Log and Safety Compliance Score sheets in AVN_01_Airport_Operations.xlsx as reference points, draft follow-up actions from the meeting grouped by Operations | Commercial | Regulatory | Capex | Stakeholder. For each action, include owner, deadline, and whether the item is Red, Amber, or Green.',
            'You are the Head of Strategy at Cakrawala Airport Holdings Berhad. Using this meeting recap and the Non-Aero Revenue sheet in AVN_01_Airport_Operations.xlsx as context, identify whether any comments suggest hidden downside not yet reflected in management reporting. Summarise the findings as a RAG note with direct quotes or paraphrased evidence from the recap.'
          ]
        },
        {
          'tool': '📓 Copilot Notebook',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'desc': 'Access via copilot.microsoft.com > Notebook tab. Upload up to 5 files and set a system instruction. Best for synthesising insights across multiple documents simultaneously.',
          'prompts': [
            'You are the Chief Financial Officer at Cakrawala Airport Holdings Berhad. Upload AVN_01_Airport_Operations.xlsx, AVN_02_Airport_Concession_Policy.docx, and AVN_03_Emergency_Response_Plan.docx to Copilot Notebook and focus on the Passenger Volume, Aeronautical Revenue, and Safety Compliance Score sheets. Ask Notebook to produce a cross-file RAG synthesis of the top risks, the 3 most credible management actions, and the evidence supporting each recommendation, citing the source file for every major point.',
            'You are the Head of Airport Operations at Cakrawala Airport Holdings Berhad. Upload AVN_01_Airport_Operations.xlsx and AVN_02_Airport_Concession_Policy.docx to Copilot Notebook and focus on the Flight Movement Log, Non-Aero Revenue, and Safety Compliance Score sheets. Ask Notebook to model a downside scenario for passenger recovery volatility, aeronautical charge review pressure, and expansion timing risk, explain which assumptions matter most, and present the answer as a RAG table with immediate, next-quarter, and monitor-only actions.',
            'You are the Head of Strategy at Cakrawala Airport Holdings Berhad. Upload AVN_01_Airport_Operations.xlsx, AVN_02_Airport_Concession_Policy.docx, and AVN_03_Emergency_Response_Plan.docx to Copilot Notebook and focus on the Passenger Volume, Flight Movement Log, and Non-Aero Revenue sheets. Ask Notebook to rank the top 5 opportunities to stabilise performance without creating new compliance or stakeholder risk, and return the answer as a RAG prioritisation table with expected impact and implementation difficulty.'
          ]
        },
        {
          'tool': '🤝 Cowork (Frontier)',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'desc': 'Cowork is an autonomous agent that takes actions across Microsoft 365 on your behalf — sending emails, scheduling meetings, creating documents, posting in Teams, and scheduling recurring tasks. Access: m365.cloud.microsoft > left nav > Agents > Cowork. Requires Frontier program enrollment.',
          'prompts': [
            'You are the Chief Financial Officer at Cakrawala Airport Holdings Berhad. Using AVN_01_Airport_Operations.xlsx, AVN_02_Airport_Concession_Policy.docx, and AVN_03_Emergency_Response_Plan.docx, especially the Passenger Volume, Aeronautical Revenue, and Safety Compliance Score sheets, research the current market context, draft a 2-page management brief, save it to OneDrive, and email it to the leadership team for review. Then schedule a 30-minute follow-up meeting for next week and label the agenda items Red, Amber, and Green.',
            'You are the Head of Airport Operations at Cakrawala Airport Holdings Berhad. Using the Flight Movement Log, Non-Aero Revenue, and Safety Compliance Score sheets in AVN_01_Airport_Operations.xlsx, prepare a task tracker, draft the related stakeholder email, store both in SharePoint or OneDrive, and send them to the named owners. Then book a checkpoint meeting and make sure the work is grouped by Operations | Commercial | Regulatory | Capex | Stakeholder with clear RAG priorities.'
          ]
        },
        {
          'tool': '✏️ Edit with Copilot',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'desc': 'Edit with Copilot is an agentic mode in Word, Excel, and PowerPoint (web) that executes multi-step editing tasks across your entire document in one instruction — reformatting, restructuring, building formulas, generating new sections. Access: open any Office file in browser > Copilot pane > Edit with Copilot. Requires M365 Copilot licence.',
          'prompts': [
            'You are the Chief Financial Officer at Cakrawala Airport Holdings Berhad. Using AVN_02_Airport_Concession_Policy.docx in Word for the web and the Passenger Volume and Safety Compliance Score sheets in AVN_01_Airport_Operations.xlsx as the fact base, add a new section that sharpens the narrative around passenger recovery volatility, aeronautical charge review pressure, and expansion timing risk. Restructure the content into Situation, Key Data, Decisions, and Next Steps, and insert a small RAG summary box at the top.',
            'You are the Head of Strategy at Cakrawala Airport Holdings Berhad. Using AVN_01_Airport_Operations.xlsx in Excel for the web, redesign the sheets fed by Flight Movement Log, Aeronautical Revenue, and Safety Compliance Score so executives can see the highest-risk items first. Standardise labels, improve formulas where needed, and add a RAG status column plus a one-row summary that updates automatically.'
          ]
        },
        {
          'tool': '🤖 Word Agent',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'desc': 'Create a declarative agent scoped to a Word document. Open the .docx in Word for Web > Copilot pane > + New Agent > name it, write a description, set the document as knowledge source > Share. Colleagues chat with it in Teams or M365 Copilot.',
          'prompts': [
            'You are the Head of Airport Operations at Cakrawala Airport Holdings Berhad. Open AVN_02_Airport_Concession_Policy.docx in Word for Web and create an agent called \'Cakrawala Airport Word Guide\'. Describe it as an assistant that answers questions using AVN_02_Airport_Concession_Policy.docx plus the Passenger Volume and Aeronautical Revenue sheets in AVN_01_Airport_Operations.xlsx, then share it with the relevant leadership team.',
            'You are the Head of Strategy at Cakrawala Airport Holdings Berhad. Demo the \'Cakrawala Airport Word Guide\' agent by asking: \'What is our most urgent operating risk, what evidence from the Flight Movement Log and Safety Compliance Score sheets supports it, and what action does AVN_02_Airport_Concession_Policy.docx imply we should take first?\'. Show the answer as a short RAG response with the supporting source references.'
          ]
        },
        {
          'tool': '🤖 PowerPoint Agent',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'desc': 'Create a declarative agent scoped to a PowerPoint presentation. Great for strategy decks or Board presentations many people need to reference. Same setup as Word Agent but using a .pptx file.',
          'prompts': [
            'You are the Chief Financial Officer at Cakrawala Airport Holdings Berhad. Create the leadership presentation in PowerPoint for Web using AVN_01_Airport_Operations.xlsx and AVN_03_Emergency_Response_Plan.docx, then create an agent called \'Cakrawala Airport Deck Navigator\'. Tell users it can answer questions tied to the Passenger Volume, Non-Aero Revenue, and Safety Compliance Score sheets, then share it with the executive team.',
            'You are the Head of Airport Operations at Cakrawala Airport Holdings Berhad. Demo the \'Cakrawala Airport Deck Navigator\' agent by asking: \'Which slide best explains our Red risks, what does the Safety Compliance Score sheet say about exposure, and what decision do leaders need this week?\'. Request a RAG answer in under 120 words.'
          ]
        },
        {
          'tool': '🤖 Excel Agent',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'desc': 'Create a declarative agent scoped to an Excel workbook. Colleagues ask data questions in plain English without opening Excel. Open .xlsx in Excel for Web > Copilot pane > + New Agent > set workbook as knowledge source > share.',
          'prompts': [
            'You are the Head of Strategy at Cakrawala Airport Holdings Berhad. Open AVN_01_Airport_Operations.xlsx in Excel for Web and create an agent called \'Cakrawala Airport Data Q&A\'. Describe it as an assistant for the Passenger Volume, Flight Movement Log, Aeronautical Revenue, Non-Aero Revenue, and Safety Compliance Score sheets that gives instant Red, Amber, and Green answers on performance and risk, then share it with the leadership team.',
            'You are the Chief Financial Officer at Cakrawala Airport Holdings Berhad. Demo the \'Cakrawala Airport Data Q&A\' agent by asking which 3 items are currently Red in the Passenger Volume and Safety Compliance Score sheets and what management action each implies. Then ask which single Amber item could become Red fastest and why.'
          ]
        },
        {
          'tool': '🏗 Agent Builder (Copilot Studio)',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'desc': 'Build a custom declarative agent in Copilot Studio — no coding required. Access: copilotstudio.microsoft.com > Create > New Agent. Add name, description, knowledge sources (SharePoint URLs or uploaded files), topics/actions. Publish to Teams in under 10 minutes.',
          'prompts': [
            'You are the Chief Financial Officer at Cakrawala Airport Holdings Berhad. Go to Copilot Studio and create an agent called \'Cakrawala Airport Intelligence Agent\' using AVN_01_Airport_Operations.xlsx, AVN_02_Airport_Concession_Policy.docx, and AVN_03_Emergency_Response_Plan.docx as knowledge sources. Tell the agent to answer questions across the Passenger Volume, Flight Movement Log, Aeronautical Revenue, Non-Aero Revenue, and Safety Compliance Score sheets, add topics for Passenger Volume, Flight Movements, Revenue, Safety Compliance, and require every answer to end with a RAG recommendation.',
            'You are the Head of Airport Operations at Cakrawala Airport Holdings Berhad. Demo the \'Cakrawala Airport Intelligence Agent\' by asking for a 2-minute briefing on the biggest Red issue in the Passenger Volume and Safety Compliance Score sheets, the best Amber mitigation in AVN_03_Emergency_Response_Plan.docx, and the Green signals management can still rely on. Ask for the answer in a RAG table with next-step owners.'
          ]
        }
      ]
    },

    {
      'id': 'retail-grocery',
      'sectorId': 'retail',
      'name': 'Retail & Grocery',
      'icon': '🛒',
      'color': '#2E7D32',
      'accent': '#388E3C',
      'company': 'Segar Rakyat Retail Berhad',
      'tagline': 'Margins leak through shrinkage, promo waste, and stock imbalance.',
      'companyID': 'PT Ritel Segar Nusantara Tbk',
      'taglineID': 'Traffic is holding, but inventory losses are masking store productivity.',
      'scenario': 'Segar Rakyat Retail Berhad and PT Ritel Segar Nusantara Tbk operate supermarkets and neighbourhood stores across Malaysia and Indonesia. Same-store sales are resilient in selected regions, yet category margin pressure, inventory shrinkage, and weak promotion ROI are diluting the benefit. Management must decide how to defend value perception while improving store economics and supplier discipline.',
      'files': ['RT_01_Store_Performance.xlsx', 'RT_02_Store_Operations_Manual.docx', 'RT_03_Supplier_Management_Policy.docx'],
      'prompts': [
        {
          'tool': '🤖 Copilot Chat (Basic)',
          'license': 'Free — no M365 Copilot license needed',
          'account': 'Sasha Ouellet — SashaO@ABSx62256373.OnMicrosoft.com',
          'prompts': [
            'You are the Chief Merchandising Officer at Segar Rakyat Retail Berhad. Using RT_01_Store_Performance.xlsx, focus on the Store Sales Dashboard, Category Margin Tracker, and Supply Chain KPIs sheets to assess gross margin compression, shrinkage, and promotion inefficiency across the store base. Quantify the immediate downside, name the 3 decisions management must take in the next 30 days, and present the answer as a RAG table with Red, Amber, and Green actions.',
            'You are the Chief Operating Officer at Segar Rakyat Retail Berhad. Using the Inventory Shrinkage and Promotion ROI sheets in RT_01_Store_Performance.xlsx together with RT_02_Store_Operations_Manual.docx, explain how the current operating issue affects strategy, capital allocation, and stakeholder confidence. Present the response as a RAG memo with sections for What We Know, What We Do Not Yet Know, and What We Should Do Next.',
            'You are the Chief Financial Officer at Segar Rakyat Retail Berhad. Using the Store Sales Dashboard and Inventory Shrinkage sheets in RT_01_Store_Performance.xlsx, benchmark our current position against the 2024 to 2025 Malaysia and Indonesia grocery retail market. Summarise the 5 most important leading indicators to watch over the next 2 quarters and show them in a RAG scorecard with a short management implication beside each.'
          ]
        },
        {
          'tool': '🔍 Researcher',
          'license': 'Free — no M365 Copilot license needed',
          'account': 'Sasha Ouellet — SashaO@ABSx62256373.OnMicrosoft.com',
          'desc': 'Access via Microsoft 365 Copilot Chat > Agents > Researcher. Researcher automatically critiques every source — verifying claims against the original before including them in the report. Grounds answers in live web sources and your organisation\'s data with full citations. Faster and more reliable than manual research.',
          'prompts': [
            'You are the Chief Operating Officer at Segar Rakyat Retail Berhad. Using RT_01_Store_Performance.xlsx, especially the Store Sales Dashboard, Category Margin Tracker, and Inventory Shrinkage sheets, plus RT_02_Store_Operations_Manual.docx, research 2024 to 2025 market benchmarks, peer disclosures, and financing or valuation signals relevant to gross margin compression, shrinkage, and promotion inefficiency across the store base. Present a RAG table with Red for immediate threats, Amber for watchlist items, and Green for supporting market signals, with citations to every source and a one-line implication for management. Flag any claim that could not be independently verified.',
            'You are the Chief Merchandising Officer at Segar Rakyat Retail Berhad. Using the Promotion ROI and Supply Chain KPIs sheets in RT_01_Store_Performance.xlsx and the policy positions in RT_03_Supplier_Management_Policy.docx, research how Kementerian Perdagangan, DOSM, and OJK or comparable published authorities and industry bodies are treating this issue across Malaysia and Indonesia. Separate mandatory requirements from market practice, cite each source, and present the findings as a RAG matrix with columns for Issue, Malaysia, Indonesia, Timing, and Management Action. Flag any claim that could not be independently verified.',
            'You are the Chief Financial Officer at Segar Rakyat Retail Berhad. Using the Store Sales Dashboard, Inventory Shrinkage, and Promotion ROI sheets in RT_01_Store_Performance.xlsx, research the demand, pricing, and competitor trends that will most influence our next 12 months. Present the answer as a RAG table ranking the top 10 external signals by likely impact and management preparedness, with citations beside every row. Flag any claim that could not be independently verified.'
          ]
        },
        {
          'tool': '📊 Analyst',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'desc': 'Access via Microsoft 365 Copilot Chat > click Agents > Analyst. Upload an Excel or CSV file. Analyst runs Python-style analysis, builds charts, and interprets results without you writing a single formula.',
          'prompts': [
            'You are the Chief Financial Officer at Segar Rakyat Retail Berhad. Upload RT_01_Store_Performance.xlsx to Analyst and use the Store Sales Dashboard, Category Margin Tracker, and Inventory Shrinkage sheets to identify the 5 biggest sources of underperformance or stress in the current plan. Quantify the variance where possible, flag each item Red, Amber, or Green based on financial materiality, and end with one corrective action per Red item.',
            'You are the Chief Merchandising Officer at Segar Rakyat Retail Berhad. Upload RT_01_Store_Performance.xlsx to Analyst and use the Promotion ROI and Supply Chain KPIs sheets to model 3 scenarios for gross margin compression, shrinkage, and promotion inefficiency across the store base: downside, base case, and recovery case. Show the impact on revenue, margin or cash, plus the operational trigger that would move an item from Amber to Red.',
            'You are the Chief Operating Officer at Segar Rakyat Retail Berhad. Upload RT_01_Store_Performance.xlsx to Analyst and use the Store Sales Dashboard, Inventory Shrinkage, and Supply Chain KPIs sheets to build a 13-week watchlist of the metrics most likely to surprise management. Present the output as a RAG dashboard table with columns for Metric, Current Level, Threshold, Risk Status, and Recommended Owner.'
          ]
        },
        {
          'tool': '📊 Copilot in Excel',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'prompts': [
            'You are the Chief Operating Officer at Segar Rakyat Retail Berhad. Using RT_01_Store_Performance.xlsx, build a new sheet called \'Segar Rakyat Executive Dashboard\' from the Store Sales Dashboard, Category Margin Tracker, and Inventory Shrinkage sheets. Show the 10 most important KPIs, add a RAG status column driven by clear thresholds, and place an executive summary box at the top that updates automatically.',
            'You are the Chief Merchandising Officer at Segar Rakyat Retail Berhad. Using RT_01_Store_Performance.xlsx, create a risk tracker that pulls from the Category Margin Tracker, Promotion ROI, and Supply Chain KPIs sheets. For each material issue, show owner, due date, estimated financial exposure, and Red/Amber/Green status, then sort Red issues first.',
            'You are the Chief Financial Officer at Segar Rakyat Retail Berhad. Using RT_01_Store_Performance.xlsx, build a scenario sensitivity sheet using the Store Sales Dashboard, Inventory Shrinkage, and Supply Chain KPIs sheets as inputs. Show downside, base, and upside cases side by side, add conditional formatting for RAG thresholds, and include a short note on the trigger that would require management escalation.'
          ]
        },
        {
          'tool': '📝 Copilot in Word',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'prompts': [
            'You are the Chief Merchandising Officer at Segar Rakyat Retail Berhad. Using RT_02_Store_Operations_Manual.docx together with the Store Sales Dashboard and Supply Chain KPIs sheets in RT_01_Store_Performance.xlsx, draft a 2-page Board paper on gross margin compression, shrinkage, and promotion inefficiency across the store base. Structure it as Situation, Risks, Decisions Required, and Next 30 Days, and place a compact RAG summary at the top.',
            'You are the Chief Operating Officer at Segar Rakyat Retail Berhad. Using RT_03_Supplier_Management_Policy.docx and the Category Margin Tracker and Promotion ROI sheets in RT_01_Store_Performance.xlsx, draft a policy or action-plan note for the leadership team that translates the data into clear operating actions. Present the recommendations as a RAG table with owners, timing, and expected impact.',
            'You are the Chief Financial Officer at Segar Rakyat Retail Berhad. Using RT_02_Store_Operations_Manual.docx, RT_03_Supplier_Management_Policy.docx, and the Store Sales Dashboard sheet in RT_01_Store_Performance.xlsx, draft an external stakeholder briefing note that explains our position factually and shows what management is doing next. After the draft, add a 3-line RAG risk summary covering timing, evidence strength, and stakeholder reaction.'
          ]
        },
        {
          'tool': '🎯 Copilot in PowerPoint',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'prompts': [
            'You are the Chief Merchandising Officer at Segar Rakyat Retail Berhad. Create a 6-slide executive deck using RT_01_Store_Performance.xlsx and RT_02_Store_Operations_Manual.docx, grounded in the Store Sales Dashboard, Inventory Shrinkage, and Supply Chain KPIs sheets. Cover retail & grocery performance, root causes, key risks, management response, scenario outlook, and decisions required, with one headline takeaway per slide and a visible RAG status marker.',
            'You are the Chief Operating Officer at Segar Rakyat Retail Berhad. Create a 3-slide operating review using the Category Margin Tracker, Inventory Shrinkage, and Promotion ROI sheets in RT_01_Store_Performance.xlsx. Show what is Red, what is Amber, and what is Green, then close with the 5 highest-priority actions and owners.',
            'You are the Chief Financial Officer at Segar Rakyat Retail Berhad. Build a 2-slide stakeholder briefing from RT_01_Store_Performance.xlsx and RT_03_Supplier_Management_Policy.docx, using the Store Sales Dashboard and Supply Chain KPIs sheets as the fact base. The first slide should summarise the issue and the second should show the recovery path in a RAG timeline.'
          ]
        },
        {
          'tool': '📧 Copilot in Outlook',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'prompts': [
            'You are the Chief Merchandising Officer at Segar Rakyat Retail Berhad. Using the Store Sales Dashboard and Supply Chain KPIs sheets in RT_01_Store_Performance.xlsx, draft an email to key suppliers, landlords, and lending banks explaining the current situation, the evidence supporting our view, and the immediate next step we want from them. After the draft, add a short RAG summary of delivery risk, likely objections, and follow-up timing.',
            'You are the Chief Operating Officer at Segar Rakyat Retail Berhad. Using the Inventory Shrinkage and Promotion ROI sheets in RT_01_Store_Performance.xlsx plus RT_02_Store_Operations_Manual.docx, draft a regulator-ready note for Kementerian Perdagangan, DOSM, and OJK or the most relevant authority. Keep the tone factual, distinguish confirmed facts from assumptions, and end with a RAG table of issues that may require further disclosure.',
            'You are the Chief Financial Officer at Segar Rakyat Retail Berhad. Using the Store Sales Dashboard, Category Margin Tracker, and Inventory Shrinkage sheets in RT_01_Store_Performance.xlsx, draft an internal leadership email that aligns owners around the top 5 actions for the next 14 days. Finish with a RAG checklist titled Do Today, Do This Week, and Monitor.'
          ]
        },
        {
          'tool': '🎙 Copilot in Teams',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'desc': 'Use your OWN existing recorded Teams meetings. Open a meeting recap in Teams > Recap tab. Copilot generates summaries, action items, and follow-up drafts grounded in the actual transcript.',
          'prompts': [
            'You are the Chief Operating Officer at Segar Rakyat Retail Berhad. Using this recorded Teams meeting recap and the Store Sales Dashboard and Inventory Shrinkage sheets in RT_01_Store_Performance.xlsx as the operating benchmark, extract all decisions, risks, and unresolved items related to gross margin compression, shrinkage, and promotion inefficiency across the store base. Present the result as a RAG table with owners and due dates.',
            'You are the Chief Merchandising Officer at Segar Rakyat Retail Berhad. Using the Category Margin Tracker and Supply Chain KPIs sheets in RT_01_Store_Performance.xlsx as reference points, draft follow-up actions from the meeting grouped by Merchandising | Store Ops | Supply Chain | Marketing | Finance. For each action, include owner, deadline, and whether the item is Red, Amber, or Green.',
            'You are the Chief Financial Officer at Segar Rakyat Retail Berhad. Using this meeting recap and the Promotion ROI sheet in RT_01_Store_Performance.xlsx as context, identify whether any comments suggest hidden downside not yet reflected in management reporting. Summarise the findings as a RAG note with direct quotes or paraphrased evidence from the recap.'
          ]
        },
        {
          'tool': '📓 Copilot Notebook',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'desc': 'Access via copilot.microsoft.com > Notebook tab. Upload up to 5 files and set a system instruction. Best for synthesising insights across multiple documents simultaneously.',
          'prompts': [
            'You are the Chief Merchandising Officer at Segar Rakyat Retail Berhad. Upload RT_01_Store_Performance.xlsx, RT_02_Store_Operations_Manual.docx, and RT_03_Supplier_Management_Policy.docx to Copilot Notebook and focus on the Store Sales Dashboard, Inventory Shrinkage, and Supply Chain KPIs sheets. Ask Notebook to produce a cross-file RAG synthesis of the top risks, the 3 most credible management actions, and the evidence supporting each recommendation, citing the source file for every major point.',
            'You are the Chief Operating Officer at Segar Rakyat Retail Berhad. Upload RT_01_Store_Performance.xlsx and RT_02_Store_Operations_Manual.docx to Copilot Notebook and focus on the Category Margin Tracker, Promotion ROI, and Supply Chain KPIs sheets. Ask Notebook to model a downside scenario for gross margin compression, shrinkage, and promotion inefficiency across the store base, explain which assumptions matter most, and present the answer as a RAG table with immediate, next-quarter, and monitor-only actions.',
            'You are the Chief Financial Officer at Segar Rakyat Retail Berhad. Upload RT_01_Store_Performance.xlsx, RT_02_Store_Operations_Manual.docx, and RT_03_Supplier_Management_Policy.docx to Copilot Notebook and focus on the Store Sales Dashboard, Category Margin Tracker, and Promotion ROI sheets. Ask Notebook to rank the top 5 opportunities to stabilise performance without creating new compliance or stakeholder risk, and return the answer as a RAG prioritisation table with expected impact and implementation difficulty.'
          ]
        },
        {
          'tool': '🤝 Cowork (Frontier)',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'desc': 'Cowork is an autonomous agent that takes actions across Microsoft 365 on your behalf — sending emails, scheduling meetings, creating documents, posting in Teams, and scheduling recurring tasks. Access: m365.cloud.microsoft > left nav > Agents > Cowork. Requires Frontier program enrollment.',
          'prompts': [
            'You are the Chief Merchandising Officer at Segar Rakyat Retail Berhad. Using RT_01_Store_Performance.xlsx, RT_02_Store_Operations_Manual.docx, and RT_03_Supplier_Management_Policy.docx, especially the Store Sales Dashboard, Inventory Shrinkage, and Supply Chain KPIs sheets, research the current market context, draft a 2-page management brief, save it to OneDrive, and email it to the leadership team for review. Then schedule a 30-minute follow-up meeting for next week and label the agenda items Red, Amber, and Green.',
            'You are the Chief Operating Officer at Segar Rakyat Retail Berhad. Using the Category Margin Tracker, Promotion ROI, and Supply Chain KPIs sheets in RT_01_Store_Performance.xlsx, prepare a task tracker, draft the related stakeholder email, store both in SharePoint or OneDrive, and send them to the named owners. Then book a checkpoint meeting and make sure the work is grouped by Merchandising | Store Ops | Supply Chain | Marketing | Finance with clear RAG priorities.'
          ]
        },
        {
          'tool': '✏️ Edit with Copilot',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'desc': 'Edit with Copilot is an agentic mode in Word, Excel, and PowerPoint (web) that executes multi-step editing tasks across your entire document in one instruction — reformatting, restructuring, building formulas, generating new sections. Access: open any Office file in browser > Copilot pane > Edit with Copilot. Requires M365 Copilot licence.',
          'prompts': [
            'You are the Chief Merchandising Officer at Segar Rakyat Retail Berhad. Using RT_02_Store_Operations_Manual.docx in Word for the web and the Store Sales Dashboard and Supply Chain KPIs sheets in RT_01_Store_Performance.xlsx as the fact base, add a new section that sharpens the narrative around gross margin compression, shrinkage, and promotion inefficiency across the store base. Restructure the content into Situation, Key Data, Decisions, and Next Steps, and insert a small RAG summary box at the top.',
            'You are the Chief Financial Officer at Segar Rakyat Retail Berhad. Using RT_01_Store_Performance.xlsx in Excel for the web, redesign the sheets fed by Category Margin Tracker, Inventory Shrinkage, and Supply Chain KPIs so executives can see the highest-risk items first. Standardise labels, improve formulas where needed, and add a RAG status column plus a one-row summary that updates automatically.'
          ]
        },
        {
          'tool': '🤖 Word Agent',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'desc': 'Create a declarative agent scoped to a Word document. Open the .docx in Word for Web > Copilot pane > + New Agent > name it, write a description, set the document as knowledge source > Share. Colleagues chat with it in Teams or M365 Copilot.',
          'prompts': [
            'You are the Chief Operating Officer at Segar Rakyat Retail Berhad. Open RT_02_Store_Operations_Manual.docx in Word for Web and create an agent called \'Segar Rakyat Word Guide\'. Describe it as an assistant that answers questions using RT_02_Store_Operations_Manual.docx plus the Store Sales Dashboard and Inventory Shrinkage sheets in RT_01_Store_Performance.xlsx, then share it with the relevant leadership team.',
            'You are the Chief Financial Officer at Segar Rakyat Retail Berhad. Demo the \'Segar Rakyat Word Guide\' agent by asking: \'What is our most urgent operating risk, what evidence from the Category Margin Tracker and Supply Chain KPIs sheets supports it, and what action does RT_02_Store_Operations_Manual.docx imply we should take first?\'. Show the answer as a short RAG response with the supporting source references.'
          ]
        },
        {
          'tool': '🤖 PowerPoint Agent',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'desc': 'Create a declarative agent scoped to a PowerPoint presentation. Great for strategy decks or Board presentations many people need to reference. Same setup as Word Agent but using a .pptx file.',
          'prompts': [
            'You are the Chief Merchandising Officer at Segar Rakyat Retail Berhad. Create the leadership presentation in PowerPoint for Web using RT_01_Store_Performance.xlsx and RT_03_Supplier_Management_Policy.docx, then create an agent called \'Segar Rakyat Deck Navigator\'. Tell users it can answer questions tied to the Store Sales Dashboard, Promotion ROI, and Supply Chain KPIs sheets, then share it with the executive team.',
            'You are the Chief Operating Officer at Segar Rakyat Retail Berhad. Demo the \'Segar Rakyat Deck Navigator\' agent by asking: \'Which slide best explains our Red risks, what does the Supply Chain KPIs sheet say about exposure, and what decision do leaders need this week?\'. Request a RAG answer in under 120 words.'
          ]
        },
        {
          'tool': '🤖 Excel Agent',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'desc': 'Create a declarative agent scoped to an Excel workbook. Colleagues ask data questions in plain English without opening Excel. Open .xlsx in Excel for Web > Copilot pane > + New Agent > set workbook as knowledge source > share.',
          'prompts': [
            'You are the Chief Financial Officer at Segar Rakyat Retail Berhad. Open RT_01_Store_Performance.xlsx in Excel for Web and create an agent called \'Segar Rakyat Data Q&A\'. Describe it as an assistant for the Store Sales Dashboard, Category Margin Tracker, Inventory Shrinkage, Promotion ROI, and Supply Chain KPIs sheets that gives instant Red, Amber, and Green answers on performance and risk, then share it with the leadership team.',
            'You are the Chief Merchandising Officer at Segar Rakyat Retail Berhad. Demo the \'Segar Rakyat Data Q&A\' agent by asking which 3 items are currently Red in the Store Sales Dashboard and Supply Chain KPIs sheets and what management action each implies. Then ask which single Amber item could become Red fastest and why.'
          ]
        },
        {
          'tool': '🏗 Agent Builder (Copilot Studio)',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'desc': 'Build a custom declarative agent in Copilot Studio — no coding required. Access: copilotstudio.microsoft.com > Create > New Agent. Add name, description, knowledge sources (SharePoint URLs or uploaded files), topics/actions. Publish to Teams in under 10 minutes.',
          'prompts': [
            'You are the Chief Merchandising Officer at Segar Rakyat Retail Berhad. Go to Copilot Studio and create an agent called \'Segar Rakyat Intelligence Agent\' using RT_01_Store_Performance.xlsx, RT_02_Store_Operations_Manual.docx, and RT_03_Supplier_Management_Policy.docx as knowledge sources. Tell the agent to answer questions across the Store Sales Dashboard, Category Margin Tracker, Inventory Shrinkage, Promotion ROI, and Supply Chain KPIs sheets, add topics for Store Sales, Margins & Shrinkage, Promotions, Supply Chain, and require every answer to end with a RAG recommendation.',
            'You are the Chief Operating Officer at Segar Rakyat Retail Berhad. Demo the \'Segar Rakyat Intelligence Agent\' by asking for a 2-minute briefing on the biggest Red issue in the Store Sales Dashboard and Supply Chain KPIs sheets, the best Amber mitigation in RT_03_Supplier_Management_Policy.docx, and the Green signals management can still rely on. Ask for the answer in a RAG table with next-step owners.'
          ]
        }
      ]
    },

    {
      'id': 'media-entertainment',
      'sectorId': 'media',
      'name': 'Media & Entertainment',
      'icon': '📺',
      'color': '#6A1B9A',
      'accent': '#7B1FA2',
      'company': 'Layar Digital Media Berhad',
      'tagline': 'Subscriber churn and content ROI pressure are colliding with ad softness.',
      'companyID': 'PT Layar Hiburan Nusantara Tbk',
      'taglineID': 'Digital growth is real, but monetisation still trails content spend.',
      'scenario': 'Layar Digital Media Berhad and PT Layar Hiburan Nusantara Tbk run broadcast, streaming, and advertising businesses across Malaysia and Indonesia. Viewership fragmentation, soft advertising demand, and tighter scrutiny on content monetisation are stretching the economics of the digital pivot. Management needs sharper choices on content mix, subscriber growth, and platform investment before the next slate is commissioned.',
      'files': ['ME_01_Content_Performance.xlsx', 'ME_02_Content_Policy.docx', 'ME_03_Digital_Strategy_Framework.docx'],
      'prompts': [
        {
          'tool': '🤖 Copilot Chat (Basic)',
          'license': 'Free — no M365 Copilot license needed',
          'account': 'Sasha Ouellet — SashaO@ABSx62256373.OnMicrosoft.com',
          'prompts': [
            'You are the Chief Digital Officer at Layar Digital Media Berhad. Using ME_01_Content_Performance.xlsx, focus on the Viewership Ratings, Digital Subscriber Metrics, and Platform KPIs sheets to assess subscriber churn, content ROI pressure, and advertising revenue volatility. Quantify the immediate downside, name the 3 decisions management must take in the next 30 days, and present the answer as a RAG table with Red, Amber, and Green actions.',
            'You are the Head of Content Strategy at Layar Digital Media Berhad. Using the Advertising Revenue and Content Cost Tracker sheets in ME_01_Content_Performance.xlsx together with ME_02_Content_Policy.docx, explain how the current operating issue affects strategy, capital allocation, and stakeholder confidence. Present the response as a RAG memo with sections for What We Know, What We Do Not Yet Know, and What We Should Do Next.',
            'You are the Chief Financial Officer at Layar Digital Media Berhad. Using the Viewership Ratings and Advertising Revenue sheets in ME_01_Content_Performance.xlsx, benchmark our current position against the 2024 to 2025 Malaysia and Indonesia media, streaming, and advertising market. Summarise the 5 most important leading indicators to watch over the next 2 quarters and show them in a RAG scorecard with a short management implication beside each.'
          ]
        },
        {
          'tool': '🔍 Researcher',
          'license': 'Free — no M365 Copilot license needed',
          'account': 'Sasha Ouellet — SashaO@ABSx62256373.OnMicrosoft.com',
          'desc': 'Access via Microsoft 365 Copilot Chat > Agents > Researcher. Researcher automatically critiques every source — verifying claims against the original before including them in the report. Grounds answers in live web sources and your organisation\'s data with full citations. Faster and more reliable than manual research.',
          'prompts': [
            'You are the Head of Content Strategy at Layar Digital Media Berhad. Using ME_01_Content_Performance.xlsx, especially the Viewership Ratings, Digital Subscriber Metrics, and Advertising Revenue sheets, plus ME_02_Content_Policy.docx, research 2024 to 2025 market benchmarks, peer disclosures, and financing or valuation signals relevant to subscriber churn, content ROI pressure, and advertising revenue volatility. Present a RAG table with Red for immediate threats, Amber for watchlist items, and Green for supporting market signals, with citations to every source and a one-line implication for management. Flag any claim that could not be independently verified.',
            'You are the Chief Digital Officer at Layar Digital Media Berhad. Using the Content Cost Tracker and Platform KPIs sheets in ME_01_Content_Performance.xlsx and the policy positions in ME_03_Digital_Strategy_Framework.docx, research how KPI TVRI and DOSM or comparable published authorities and industry bodies are treating this issue across Malaysia and Indonesia. Separate mandatory requirements from market practice, cite each source, and present the findings as a RAG matrix with columns for Issue, Malaysia, Indonesia, Timing, and Management Action. Flag any claim that could not be independently verified.',
            'You are the Chief Financial Officer at Layar Digital Media Berhad. Using the Viewership Ratings, Advertising Revenue, and Content Cost Tracker sheets in ME_01_Content_Performance.xlsx, research the demand, pricing, and competitor trends that will most influence our next 12 months. Present the answer as a RAG table ranking the top 10 external signals by likely impact and management preparedness, with citations beside every row. Flag any claim that could not be independently verified.'
          ]
        },
        {
          'tool': '📊 Analyst',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'desc': 'Access via Microsoft 365 Copilot Chat > click Agents > Analyst. Upload an Excel or CSV file. Analyst runs Python-style analysis, builds charts, and interprets results without you writing a single formula.',
          'prompts': [
            'You are the Chief Financial Officer at Layar Digital Media Berhad. Upload ME_01_Content_Performance.xlsx to Analyst and use the Viewership Ratings, Digital Subscriber Metrics, and Advertising Revenue sheets to identify the 5 biggest sources of underperformance or stress in the current plan. Quantify the variance where possible, flag each item Red, Amber, or Green based on financial materiality, and end with one corrective action per Red item.',
            'You are the Chief Digital Officer at Layar Digital Media Berhad. Upload ME_01_Content_Performance.xlsx to Analyst and use the Content Cost Tracker and Platform KPIs sheets to model 3 scenarios for subscriber churn, content ROI pressure, and advertising revenue volatility: downside, base case, and recovery case. Show the impact on revenue, margin or cash, plus the operational trigger that would move an item from Amber to Red.',
            'You are the Head of Content Strategy at Layar Digital Media Berhad. Upload ME_01_Content_Performance.xlsx to Analyst and use the Viewership Ratings, Advertising Revenue, and Platform KPIs sheets to build a 13-week watchlist of the metrics most likely to surprise management. Present the output as a RAG dashboard table with columns for Metric, Current Level, Threshold, Risk Status, and Recommended Owner.'
          ]
        },
        {
          'tool': '📊 Copilot in Excel',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'prompts': [
            'You are the Head of Content Strategy at Layar Digital Media Berhad. Using ME_01_Content_Performance.xlsx, build a new sheet called \'Layar Digital Executive Dashboard\' from the Viewership Ratings, Digital Subscriber Metrics, and Advertising Revenue sheets. Show the 10 most important KPIs, add a RAG status column driven by clear thresholds, and place an executive summary box at the top that updates automatically.',
            'You are the Chief Digital Officer at Layar Digital Media Berhad. Using ME_01_Content_Performance.xlsx, create a risk tracker that pulls from the Digital Subscriber Metrics, Content Cost Tracker, and Platform KPIs sheets. For each material issue, show owner, due date, estimated financial exposure, and Red/Amber/Green status, then sort Red issues first.',
            'You are the Chief Financial Officer at Layar Digital Media Berhad. Using ME_01_Content_Performance.xlsx, build a scenario sensitivity sheet using the Viewership Ratings, Advertising Revenue, and Platform KPIs sheets as inputs. Show downside, base, and upside cases side by side, add conditional formatting for RAG thresholds, and include a short note on the trigger that would require management escalation.'
          ]
        },
        {
          'tool': '📝 Copilot in Word',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'prompts': [
            'You are the Chief Digital Officer at Layar Digital Media Berhad. Using ME_02_Content_Policy.docx together with the Viewership Ratings and Platform KPIs sheets in ME_01_Content_Performance.xlsx, draft a 2-page Board paper on subscriber churn, content ROI pressure, and advertising revenue volatility. Structure it as Situation, Risks, Decisions Required, and Next 30 Days, and place a compact RAG summary at the top.',
            'You are the Head of Content Strategy at Layar Digital Media Berhad. Using ME_03_Digital_Strategy_Framework.docx and the Digital Subscriber Metrics and Content Cost Tracker sheets in ME_01_Content_Performance.xlsx, draft a policy or action-plan note for the leadership team that translates the data into clear operating actions. Present the recommendations as a RAG table with owners, timing, and expected impact.',
            'You are the Chief Financial Officer at Layar Digital Media Berhad. Using ME_02_Content_Policy.docx, ME_03_Digital_Strategy_Framework.docx, and the Viewership Ratings sheet in ME_01_Content_Performance.xlsx, draft an external stakeholder briefing note that explains our position factually and shows what management is doing next. After the draft, add a 3-line RAG risk summary covering timing, evidence strength, and stakeholder reaction.'
          ]
        },
        {
          'tool': '🎯 Copilot in PowerPoint',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'prompts': [
            'You are the Chief Digital Officer at Layar Digital Media Berhad. Create a 6-slide executive deck using ME_01_Content_Performance.xlsx and ME_02_Content_Policy.docx, grounded in the Viewership Ratings, Advertising Revenue, and Platform KPIs sheets. Cover media & entertainment performance, root causes, key risks, management response, scenario outlook, and decisions required, with one headline takeaway per slide and a visible RAG status marker.',
            'You are the Head of Content Strategy at Layar Digital Media Berhad. Create a 3-slide operating review using the Digital Subscriber Metrics, Advertising Revenue, and Content Cost Tracker sheets in ME_01_Content_Performance.xlsx. Show what is Red, what is Amber, and what is Green, then close with the 5 highest-priority actions and owners.',
            'You are the Chief Financial Officer at Layar Digital Media Berhad. Build a 2-slide stakeholder briefing from ME_01_Content_Performance.xlsx and ME_03_Digital_Strategy_Framework.docx, using the Viewership Ratings and Platform KPIs sheets as the fact base. The first slide should summarise the issue and the second should show the recovery path in a RAG timeline.'
          ]
        },
        {
          'tool': '📧 Copilot in Outlook',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'prompts': [
            'You are the Chief Digital Officer at Layar Digital Media Berhad. Using the Viewership Ratings and Platform KPIs sheets in ME_01_Content_Performance.xlsx, draft an email to advertisers, platform partners, and investors explaining the current situation, the evidence supporting our view, and the immediate next step we want from them. After the draft, add a short RAG summary of delivery risk, likely objections, and follow-up timing.',
            'You are the Head of Content Strategy at Layar Digital Media Berhad. Using the Advertising Revenue and Content Cost Tracker sheets in ME_01_Content_Performance.xlsx plus ME_02_Content_Policy.docx, draft a regulator-ready note for KPI TVRI and DOSM or the most relevant authority. Keep the tone factual, distinguish confirmed facts from assumptions, and end with a RAG table of issues that may require further disclosure.',
            'You are the Chief Financial Officer at Layar Digital Media Berhad. Using the Viewership Ratings, Digital Subscriber Metrics, and Advertising Revenue sheets in ME_01_Content_Performance.xlsx, draft an internal leadership email that aligns owners around the top 5 actions for the next 14 days. Finish with a RAG checklist titled Do Today, Do This Week, and Monitor.'
          ]
        },
        {
          'tool': '🎙 Copilot in Teams',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'desc': 'Use your OWN existing recorded Teams meetings. Open a meeting recap in Teams > Recap tab. Copilot generates summaries, action items, and follow-up drafts grounded in the actual transcript.',
          'prompts': [
            'You are the Head of Content Strategy at Layar Digital Media Berhad. Using this recorded Teams meeting recap and the Viewership Ratings and Advertising Revenue sheets in ME_01_Content_Performance.xlsx as the operating benchmark, extract all decisions, risks, and unresolved items related to subscriber churn, content ROI pressure, and advertising revenue volatility. Present the result as a RAG table with owners and due dates.',
            'You are the Chief Digital Officer at Layar Digital Media Berhad. Using the Digital Subscriber Metrics and Platform KPIs sheets in ME_01_Content_Performance.xlsx as reference points, draft follow-up actions from the meeting grouped by Content | Product | Advertising | Partnerships | Finance. For each action, include owner, deadline, and whether the item is Red, Amber, or Green.',
            'You are the Chief Financial Officer at Layar Digital Media Berhad. Using this meeting recap and the Content Cost Tracker sheet in ME_01_Content_Performance.xlsx as context, identify whether any comments suggest hidden downside not yet reflected in management reporting. Summarise the findings as a RAG note with direct quotes or paraphrased evidence from the recap.'
          ]
        },
        {
          'tool': '📓 Copilot Notebook',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'desc': 'Access via copilot.microsoft.com > Notebook tab. Upload up to 5 files and set a system instruction. Best for synthesising insights across multiple documents simultaneously.',
          'prompts': [
            'You are the Chief Digital Officer at Layar Digital Media Berhad. Upload ME_01_Content_Performance.xlsx, ME_02_Content_Policy.docx, and ME_03_Digital_Strategy_Framework.docx to Copilot Notebook and focus on the Viewership Ratings, Advertising Revenue, and Platform KPIs sheets. Ask Notebook to produce a cross-file RAG synthesis of the top risks, the 3 most credible management actions, and the evidence supporting each recommendation, citing the source file for every major point.',
            'You are the Head of Content Strategy at Layar Digital Media Berhad. Upload ME_01_Content_Performance.xlsx and ME_02_Content_Policy.docx to Copilot Notebook and focus on the Digital Subscriber Metrics, Content Cost Tracker, and Platform KPIs sheets. Ask Notebook to model a downside scenario for subscriber churn, content ROI pressure, and advertising revenue volatility, explain which assumptions matter most, and present the answer as a RAG table with immediate, next-quarter, and monitor-only actions.',
            'You are the Chief Financial Officer at Layar Digital Media Berhad. Upload ME_01_Content_Performance.xlsx, ME_02_Content_Policy.docx, and ME_03_Digital_Strategy_Framework.docx to Copilot Notebook and focus on the Viewership Ratings, Digital Subscriber Metrics, and Content Cost Tracker sheets. Ask Notebook to rank the top 5 opportunities to stabilise performance without creating new compliance or stakeholder risk, and return the answer as a RAG prioritisation table with expected impact and implementation difficulty.'
          ]
        },
        {
          'tool': '🤝 Cowork (Frontier)',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'desc': 'Cowork is an autonomous agent that takes actions across Microsoft 365 on your behalf — sending emails, scheduling meetings, creating documents, posting in Teams, and scheduling recurring tasks. Access: m365.cloud.microsoft > left nav > Agents > Cowork. Requires Frontier program enrollment.',
          'prompts': [
            'You are the Chief Digital Officer at Layar Digital Media Berhad. Using ME_01_Content_Performance.xlsx, ME_02_Content_Policy.docx, and ME_03_Digital_Strategy_Framework.docx, especially the Viewership Ratings, Advertising Revenue, and Platform KPIs sheets, research the current market context, draft a 2-page management brief, save it to OneDrive, and email it to the leadership team for review. Then schedule a 30-minute follow-up meeting for next week and label the agenda items Red, Amber, and Green.',
            'You are the Head of Content Strategy at Layar Digital Media Berhad. Using the Digital Subscriber Metrics, Content Cost Tracker, and Platform KPIs sheets in ME_01_Content_Performance.xlsx, prepare a task tracker, draft the related stakeholder email, store both in SharePoint or OneDrive, and send them to the named owners. Then book a checkpoint meeting and make sure the work is grouped by Content | Product | Advertising | Partnerships | Finance with clear RAG priorities.'
          ]
        },
        {
          'tool': '✏️ Edit with Copilot',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'desc': 'Edit with Copilot is an agentic mode in Word, Excel, and PowerPoint (web) that executes multi-step editing tasks across your entire document in one instruction — reformatting, restructuring, building formulas, generating new sections. Access: open any Office file in browser > Copilot pane > Edit with Copilot. Requires M365 Copilot licence.',
          'prompts': [
            'You are the Chief Digital Officer at Layar Digital Media Berhad. Using ME_02_Content_Policy.docx in Word for the web and the Viewership Ratings and Platform KPIs sheets in ME_01_Content_Performance.xlsx as the fact base, add a new section that sharpens the narrative around subscriber churn, content ROI pressure, and advertising revenue volatility. Restructure the content into Situation, Key Data, Decisions, and Next Steps, and insert a small RAG summary box at the top.',
            'You are the Chief Financial Officer at Layar Digital Media Berhad. Using ME_01_Content_Performance.xlsx in Excel for the web, redesign the sheets fed by Digital Subscriber Metrics, Advertising Revenue, and Platform KPIs so executives can see the highest-risk items first. Standardise labels, improve formulas where needed, and add a RAG status column plus a one-row summary that updates automatically.'
          ]
        },
        {
          'tool': '🤖 Word Agent',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'desc': 'Create a declarative agent scoped to a Word document. Open the .docx in Word for Web > Copilot pane > + New Agent > name it, write a description, set the document as knowledge source > Share. Colleagues chat with it in Teams or M365 Copilot.',
          'prompts': [
            'You are the Head of Content Strategy at Layar Digital Media Berhad. Open ME_02_Content_Policy.docx in Word for Web and create an agent called \'Layar Digital Word Guide\'. Describe it as an assistant that answers questions using ME_02_Content_Policy.docx plus the Viewership Ratings and Advertising Revenue sheets in ME_01_Content_Performance.xlsx, then share it with the relevant leadership team.',
            'You are the Chief Financial Officer at Layar Digital Media Berhad. Demo the \'Layar Digital Word Guide\' agent by asking: \'What is our most urgent operating risk, what evidence from the Digital Subscriber Metrics and Platform KPIs sheets supports it, and what action does ME_02_Content_Policy.docx imply we should take first?\'. Show the answer as a short RAG response with the supporting source references.'
          ]
        },
        {
          'tool': '🤖 PowerPoint Agent',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'desc': 'Create a declarative agent scoped to a PowerPoint presentation. Great for strategy decks or Board presentations many people need to reference. Same setup as Word Agent but using a .pptx file.',
          'prompts': [
            'You are the Chief Digital Officer at Layar Digital Media Berhad. Create the leadership presentation in PowerPoint for Web using ME_01_Content_Performance.xlsx and ME_03_Digital_Strategy_Framework.docx, then create an agent called \'Layar Digital Deck Navigator\'. Tell users it can answer questions tied to the Viewership Ratings, Content Cost Tracker, and Platform KPIs sheets, then share it with the executive team.',
            'You are the Head of Content Strategy at Layar Digital Media Berhad. Demo the \'Layar Digital Deck Navigator\' agent by asking: \'Which slide best explains our Red risks, what does the Platform KPIs sheet say about exposure, and what decision do leaders need this week?\'. Request a RAG answer in under 120 words.'
          ]
        },
        {
          'tool': '🤖 Excel Agent',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'desc': 'Create a declarative agent scoped to an Excel workbook. Colleagues ask data questions in plain English without opening Excel. Open .xlsx in Excel for Web > Copilot pane > + New Agent > set workbook as knowledge source > share.',
          'prompts': [
            'You are the Chief Financial Officer at Layar Digital Media Berhad. Open ME_01_Content_Performance.xlsx in Excel for Web and create an agent called \'Layar Digital Data Q&A\'. Describe it as an assistant for the Viewership Ratings, Digital Subscriber Metrics, Advertising Revenue, Content Cost Tracker, and Platform KPIs sheets that gives instant Red, Amber, and Green answers on performance and risk, then share it with the leadership team.',
            'You are the Chief Digital Officer at Layar Digital Media Berhad. Demo the \'Layar Digital Data Q&A\' agent by asking which 3 items are currently Red in the Viewership Ratings and Platform KPIs sheets and what management action each implies. Then ask which single Amber item could become Red fastest and why.'
          ]
        },
        {
          'tool': '🏗 Agent Builder (Copilot Studio)',
          'license': 'M365 Copilot',
          'account': 'MOD Administrator — admin@ABSx62256373.onmicrosoft.com',
          'desc': 'Build a custom declarative agent in Copilot Studio — no coding required. Access: copilotstudio.microsoft.com > Create > New Agent. Add name, description, knowledge sources (SharePoint URLs or uploaded files), topics/actions. Publish to Teams in under 10 minutes.',
          'prompts': [
            'You are the Chief Digital Officer at Layar Digital Media Berhad. Go to Copilot Studio and create an agent called \'Layar Digital Intelligence Agent\' using ME_01_Content_Performance.xlsx, ME_02_Content_Policy.docx, and ME_03_Digital_Strategy_Framework.docx as knowledge sources. Tell the agent to answer questions across the Viewership Ratings, Digital Subscriber Metrics, Advertising Revenue, Content Cost Tracker, and Platform KPIs sheets, add topics for Viewership, Subscriber Metrics, Advertising Revenue, Content Costs, and require every answer to end with a RAG recommendation.',
            'You are the Head of Content Strategy at Layar Digital Media Berhad. Demo the \'Layar Digital Intelligence Agent\' by asking for a 2-minute briefing on the biggest Red issue in the Viewership Ratings and Platform KPIs sheets, the best Amber mitigation in ME_03_Digital_Strategy_Framework.docx, and the Green signals management can still rely on. Ask for the answer in a RAG table with next-step owners.'
          ]
        }
      ]
    }
]

print(f"Batch 8 written: {len(INDUSTRIES_8)} entries")

