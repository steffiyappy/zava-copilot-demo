
import sys; sys.path.insert(0,'.')
from util import *

INDUSTRIES_2 = [

# ── INVESTMENT BANKING ─────────────────────────────────────────────────────
ind('investment-banking','banking-fs','Investment Banking','💹','#0D47A1','#1565C0',
    'Kenanga Capital Group',
    'MYR 18.4B AUM — 3 IPO mandates in pipeline, ESG fund launch Q2 FY2026.',
    'Kenanga Capital Group manages MYR 18.4B in assets under management and has three IPO mandates in the pipeline totalling a combined market cap of MYR 4.2B. An ESG-themed fund is being structured for launch in Q2 FY2026. The Securities Commission quarterly regulatory filing is due in two weeks and the M&A advisory team is evaluating a cross-border acquisition target.',
    ['GLC_01_Danamas_Capital.xlsx','GLC_02_Danamas_Strategy.docx','04_Zava_MA_Evaluation_Framework.docx'],
    [
      tool(T_CHAT, FREE_LIC, FREE_ACCT, [
        'I am an investment banker preparing a pitch to a tech company that wants to list on Bursa Malaysia. They are profitable but relatively small — MYR 180M revenue, MYR 22M EBITDA — and the founders are worried about whether the IPO window is open. Draft a 5-bullet talking points document I can use to open the pitch meeting. Cover: current Bursa market sentiment for tech listings, typical listing requirements for the ACE Market vs Main Market, the realistic timeline from mandate to listing day, and what we would need from them to start the due diligence process.',
        'Explain what an ESG-themed fund is, how it differs from a conventional equity fund, and what the key regulatory requirements are from the Securities Commission Malaysia for marketing an ESG fund to retail investors. Keep the explanation suitable for a senior client who understands investments but is new to ESG frameworks.',
        'What are the five most important factors that determine the success of an IPO in Malaysia? Rank them in order of importance and explain each in two to three sentences. Include one recent Malaysian IPO example to illustrate each factor.'
      ]),
      tool(T_RESEARCHER, M365_LIC, M365_ACCT, [
        'Research the Malaysian IPO market in 2025 and 2026. I need: (1) Total number of IPOs listed and total funds raised on Bursa Malaysia in 2024 and year-to-date 2025, (2) Sectors with the highest demand from institutional investors, (3) Average price-to-earnings multiples achieved by tech and consumer sector IPOs. Provide source citations and present as an investment research brief.',
        'Research global ESG fund regulations relevant to Malaysian fund managers — specifically SEC, MAS, and Securities Commission Malaysia requirements for ESG disclosure. Identify the three key differences between SC Malaysia\'s ESG framework and the EU SFDR, and explain the implications for a Malaysian fund manager distributing to European institutional investors.'
      ], DESC_RESEARCHER),
      tool(T_ANALYST, M365_LIC, M365_ACCT, [
        'Analyse the AUM trend across all fund categories (equity, fixed income, ESG, alternative) over the past 8 quarters. Which categories are growing and which are in outflow? Calculate the net flow rate for each category and identify which fund manager or product has the highest alpha generation. Create a bubble chart showing AUM size vs net flow rate vs alpha.',
        'Perform a peer comparison of Kenanga Capital\'s fee structure against the 4 closest competitors listed in the data. Which fee categories (management fee, performance fee, entry/exit fee) are above or below market median? Show as a heatmap table: Product Category | Our Fee | Market Median | Position (Above/Below/At).'
      ], DESC_ANALYST),
      tool(T_EXCEL, M365_LIC, M365_ACCT, [
        'Using the IPO Pipeline tab in this workbook, For each of the three IPO mandates in the pipeline, calculate the estimated deal fee revenue based on the assumed offer price, shares offered, and our advisory fee rate (2.5% of gross proceeds). Show total expected revenue from all three mandates and flag which deal has the highest fee risk if the IPO is withdrawn.',
        'Create an ESG fund performance attribution model on a new sheet. The model should break down fund return into: (1) Market beta contribution, (2) ESG factor premium/discount, (3) Stock selection alpha, (4) Sector allocation effect. Use the returns data in the Fund Performance sheet and show monthly attribution for the last 12 months.',
        'In the Client AUM sheet, identify the top 20 clients by AUM and calculate the revenue concentration risk — what percentage of total management fee revenue comes from the top 5 clients. Highlight in red any client where a 30% AUM withdrawal would reduce our total fee revenue by more than 5%.',
      ]),
      tool(T_WORD, M365_LIC, M365_ACCT, [
        'Draft an ESG fund prospectus introduction of 400 words for the new fund launching in Q2 FY2026. Cover: the fund\'s ESG investment philosophy, the screening methodology (negative exclusions + ESG scoring), the benchmark index, the target investor profile, and the expected distribution yield. Use language that meets SC Malaysia\'s disclosure standards for ESG funds.',
        'Identify all sections in this strategy document related to M&A and corporate advisory. For each section, extract the key strategic rationale and create a one-page M&A pitch template that our advisory team can customise for new mandates. The template should have five sections: Client Situation, Strategic Rationale, Deal Mechanics, Our Credentials, and Proposed Fee Structure.',
        'Draft a 300-word "Chairman\'s Letter to Investors" for the annual fund report. The letter should acknowledge market volatility in FY2025, highlight our top-performing fund (the ESG equity fund returned 14.2%), reaffirm our investment philosophy, and outline our key strategic priorities for FY2026 — growing ESG AUM to MYR 2B and launching two new alternative investment products.'
      ]),
      tool(T_PPT, M365_LIC, M365_ACCT, [
        'Create a 12-slide IPO pitch deck for a Malaysian tech company targeting a Main Market listing at MYR 420M market cap. Include: company overview, financial highlights (Revenue CAGR 28%, EBITDA margin 22%), industry tailwinds, competitive positioning, IPO structure and use of proceeds, valuation methodology (DCF + comparable companies), Bursa listing timeline, risk factors, and why now is the right time to list. Professional blue and silver theme.',
        'Generate a 6-slide ESG fund investor update presentation. Slides: (1) Portfolio overview and ESG score distribution, (2) Top 10 holdings with ESG ratings, (3) Carbon footprint vs benchmark, (4) Active ownership highlights — engagements and votes, (5) Performance attribution, (6) Outlook and strategy. Include speaker notes for each slide.',
        'Redesign slide 3 of this presentation to replace the text-heavy bullet list with a 2x2 matrix showing deal complexity vs fee potential for our pipeline. Place each of the three IPO mandates in the appropriate quadrant and add a one-line rationale.'
      ]),
      tool(T_OUTLOOK, M365_LIC, M365_ACCT, [
        'I have a meeting with a sovereign wealth fund potential investor next week about our ESG fund. Draft a pre-meeting email that introduces our ESG fund, attaches a one-pager (note: attach manually), proposes a 45-minute meeting agenda, and requests information on their typical ESG fund allocation size and return expectations. Keep the tone professional but not overly formal — this is a relationship-building email, not a hard sell.',
        'Draft the Securities Commission quarterly regulatory filing cover letter. The letter should reference the relevant SC circular, confirm the accuracy of the enclosed statements, note any material changes to the fund strategy or fee structure, and request acknowledgement of receipt. Use the formal tone required for SC correspondence.',
        'Summarise my inbox from the past two weeks and flag any emails related to our IPO pipeline mandates. Categorise them as: Urgent (client needs response today), Action Required (needs response this week), and FYI. List each email with sender, subject, and one-line summary.'
      ]),
      tool(T_TEAMS, M365_LIC, M365_ACCT, [
        'Open an existing recorded Teams meeting recap from a deal team or investment committee meeting. Summarise all investment recommendations made, the key rationale for each, any dissenting views, and the final decision. Format as an investment committee minute suitable for regulatory record-keeping.',
        'Ask Copilot in the recap: Identify all client commitments made in this meeting — any promise to deliver a document, update, or recommendation to a client by a specific date. List each commitment with the staff member who made it and the agreed deadline, so I can follow up before end of week.',
        'Based on this meeting transcript, draft an action item register for the M&A deal team. Include four columns: Action | Owner | Deadline | Dependencies. Sort by deadline, earliest first.'
      ], DESC_TEAMS),
      tool(T_NOTEBOOK, M365_LIC, M365_ACCT, [
        'Upload GLC_01_Danamas_Capital.xlsx, GLC_02_Danamas_Strategy.docx, and 04_Zava_MA_Evaluation_Framework.docx to Copilot Notebook. Set instruction: "You are a senior M&A advisor preparing a cross-border acquisition recommendation." Ask: Based on the capital position in the data file, the strategic priorities in the strategy document, and the evaluation framework, what is the maximum acquisition size Kenanga Capital could prudently pursue without impairing its capital ratios or fund management licence? What type of acquisition target would best complement the current AUM mix?',
        'Upload GLC_02_Danamas_Strategy.docx and 04_Zava_MA_Evaluation_Framework.docx. Ask: The M&A evaluation framework lists 12 criteria for target assessment. Apply these criteria to a hypothetical acquisition of a Malaysia-based digital wealth management platform with MYR 800M AUM and 45,000 retail clients. Score the target out of 100 and recommend whether to proceed to indicative offer stage.'
      ], DESC_NOTEBOOK),
      tool(T_COWORK, FRONTIER_LIC, M365_ACCT, [
        'Do all of the following: (1) Research the top 5 ESG fund managers in Southeast Asia by AUM and their fund performance over the past 3 years. (2) Draft a competitive positioning brief comparing Kenanga Capital\'s ESG fund against these peers — 2 pages, with a summary table showing AUM, returns, expense ratio, and ESG methodology. (3) Save to OneDrive as "ESG Fund Competitive Analysis - [Date]". (4) Email to the Head of Fund Management and CEO asking for review before the investor roadshow next week. (5) Schedule a 60-minute "ESG Fund Investor Roadshow Prep" meeting for Tuesday at 9am.',
        'Do all of the following: (1) Check the Securities Commission Malaysia website for any new circulars or guidelines published in the past 30 days. (2) Identify any that affect our fund management licence or ESG fund offering. (3) Draft a compliance alert memo for the Chief Compliance Officer summarising the new requirements and recommended actions. (4) Post a summary in the #compliance-team Teams channel. (5) Schedule a 45-minute compliance briefing for the fund management team for this Friday.'
      ], DESC_COWORK),
      tool(T_WORD_AGT, M365_LIC, M365_ACCT, [
        'Open GLC_02_Danamas_Strategy.docx in Word for Web. Create an agent called "Capital Strategy Q&A Bot". Description: "Answers questions from investment managers and relationship managers about Kenanga Capital\'s investment strategy, ESG fund framework, and M&A evaluation criteria." Share with the investment management and advisory teams.',
        'Demo: Ask the agent "What is the minimum ESG score threshold for a company to be included in our ESG fund portfolio? What happens if a holding\'s score drops below the threshold after inclusion?" Show how the fund management team gets consistent policy answers without calling compliance.'
      ], DESC_WORD_AGT),
      tool(T_PPT_AGT, M365_LIC, M365_ACCT, [
        'Create a PowerPoint summary of the IPO pitch deck and open in PowerPoint for Web. Create an agent called "IPO Pitch Deck Q&A". Description: "Answers due diligence questions from potential IPO clients about Kenanga Capital\'s track record, deal process, timeline, and fee structure." Share with the corporate finance team to use in client pitches.',
        'Demo: A client asks the agent "How long does the IPO process typically take from mandate signing to listing day on Bursa Main Market?" Then: "What is your typical underwriting fee structure and are there any performance-linked fee arrangements?" Show how the agent handles common client questions consistently.'
      ], DESC_PPT_AGT),
      tool(T_XL_AGT, M365_LIC, M365_ACCT, [
        'Open GLC_01_Danamas_Capital.xlsx in Excel for Web. Create an agent called "AUM & Performance Q&A". Description: "Provides instant answers on Kenanga Capital\'s fund AUM, performance data, client concentration, and pipeline deal metrics." Share with senior management and investor relations.',
        'Demo: Ask the agent "What is the total AUM across all equity funds and what was the average return in FY2025?" Then: "Which client accounts for the largest single AUM concentration and what is the revenue exposure if they redeem?" Show how management gets instant portfolio intelligence.'
      ], DESC_XL_AGT),
      tool(T_BUILDER, M365_LIC, M365_ACCT, [
        'Go to copilotstudio.microsoft.com > Create > New Agent. Name it "Kenanga Investor Intelligence Bot". Description: "An AI assistant for Kenanga Capital\'s client-facing team — answers investor questions about fund performance, ESG methodology, IPO pipeline, and regulatory compliance using official strategy and fund documents." Upload GLC_01_Danamas_Capital.xlsx and GLC_02_Danamas_Strategy.docx. Add topics: "Fund Performance Query", "ESG Methodology", "IPO Services". Publish to Teams for the client advisory team.',
        'Demo in Teams: Ask the bot "An institutional client wants to know how our ESG fund screens for climate risk — can you walk me through our methodology and name two examples of companies we excluded in the last 12 months?" Then: "What is our current track record for IPO mandates — how many have we completed and what was the average first-day trading premium?" Show how the advisory team answers complex client questions confidently and consistently.'
      ], DESC_BUILDER),
    ]),

# ── GENERAL INSURANCE ─────────────────────────────────────────────────────
ind('general-insurance','insurance','General Insurance','🛡','#1A237E','#283593',
    'Pacific Shield Insurance Berhad',
    'Motor combined ratio at 108% — claims leakage and fraud costing MYR 84M annually.',
    'Pacific Shield Insurance Berhad is Malaysia\'s fourth-largest general insurer. The motor segment combined ratio has breached 108%, well above the 95% profitability threshold, driven by rising claims frequency and a suspected claims fraud syndicate (Project SWIFT CLAIM). BNM\'s detariffication deadline creates additional pricing pressure.',
    ['INS_01_Pacific_Shield_Insurance.xlsx','INS_02_Pacific_Shield_Strategy.docx'],
    [
      tool(T_CHAT, FREE_LIC, FREE_ACCT, [
        'I am the Head of Claims at a Malaysian general insurer. Our motor combined ratio has risen to 108% and we suspect a fraud syndicate is inflating repair bills through workshop collusion. Draft a structured fraud investigation brief of approximately 250 words that I can use to brief our investigators. Cover: the suspected fraud pattern, the data signals we should look for in claims records, the legal framework for fraud investigation in Malaysia, and the key questions our investigators should ask suspicious claimants. Keep the tone professional and factual.',
        'Explain the BNM motor detariffication framework in plain language. What does it mean for insurers, what pricing freedoms does it create, and what risks does it introduce if an insurer prices too aggressively in the first year? Limit the explanation to 200 words suitable for a Board Risk Committee briefing.',
        'What are the five key metrics used to assess the profitability of a general insurance portfolio? Define each metric, provide the industry benchmark for Malaysian general insurers, and indicate whether a higher or lower number is desirable for each.'
      ]),
      tool(T_RESEARCHER, M365_LIC, M365_ACCT, [
        'Research insurance fraud detection technology trends in Southeast Asia for 2025 and 2026. I need: (1) The most effective AI and machine learning approaches used by leading insurers to detect motor claims fraud, (2) Two or three vendor solutions deployed in the region with documented fraud reduction results, (3) Any regulatory guidance from BNM or the Malaysia Insurance Institute on fraud analytics. Provide citations.',
        'Research how Malaysian general insurers are responding to BNM motor detariffication. What pricing strategies are the top 5 insurers using? Has the detariffication led to market share shifts? Are there any BNM supervisory concerns about underpricing? Present as a competitive intelligence brief.'
      ], DESC_RESEARCHER),
      tool(T_ANALYST, M365_LIC, M365_ACCT, [
        'Analyse the motor claims data to identify patterns consistent with fraud. Look for: (1) workshops with unusually high average claim values, (2) policyholders with multiple claims in 12 months, (3) claims submitted within 30 days of policy inception, (4) claims where repair cost exceeds 70% of vehicle value. Create a fraud risk score for each workshop and rank the top 10 highest-risk workshops. Show as a table and a bar chart.',
        'Decompose the motor combined ratio of 108% into its component parts: claims frequency, average claims severity, expense ratio, and reinsurance recovery rate. Which component has deteriorated most year-on-year? Show the trend over 8 quarters with a waterfall chart showing how each component has contributed to the combined ratio movement from 95% to 108%.'
      ], DESC_ANALYST),
      tool(T_EXCEL, M365_LIC, M365_ACCT, [
        'Using the Claims Analysis tab in this workbook, Create a fraud detection dashboard on a new sheet. For each motor workshop in the data, calculate: (1) Average claim value vs national average, (2) Claims rejection rate, (3) Percentage of claims submitted by the same loss adjuster, (4) Average repair days vs industry benchmark of 12 days. Highlight in red any workshop that triggers 3 or more of these fraud indicators.',
        'Build a detariffication pricing model on a new sheet. For each motor risk category (private car, commercial vehicle, motorcycle), calculate the breakeven premium rate that achieves a 95% combined ratio target. Assume: current claims frequency, projected 5% claims inflation, and our current expense ratio of 28%. Show the new premium rate and the percentage change from the current tariff rate.',
        'In the Policy Renewal sheet, identify all policies where the renewal date is within the next 30 days, the current premium is below breakeven, and the policyholder has made more than one claim in the past 12 months. These are high-risk renewals we should either reprice or decline. List with policy number, current premium, breakeven premium, and claims history.',
      ]),
      tool(T_WORD, M365_LIC, M365_ACCT, [
        'Draft a 2-page Project SWIFT CLAIM investigation report for the Board Audit Committee. Structure: (1) Background — fraud suspected based on claims data analysis, (2) Evidence Summary — key data signals identified, (3) Top 5 suspicious workshops with supporting data, (4) Recommended Actions — referral to police, claims suspension, blacklisting, (5) Financial Impact — estimated annual claims leakage of MYR 84M. Use a formal, legally cautious tone that avoids prejudging guilt.',
        'Identify all sections in this strategy document that reference claims management or fraud prevention. Summarise the current fraud prevention commitments and identify any gaps relative to industry best practice. Create a gap analysis table: Current Practice | Best Practice | Gap | Recommended Action.',
        'Draft a customer communication letter that will be sent to policyholders whose claims are being reviewed as part of Project SWIFT CLAIM. The letter must: inform them of the review without alleging fraud, explain that a small delay in claims payment should be expected, provide contact details for queries, and maintain a respectful, non-accusatory tone. Keep it under 250 words.'
      ]),
      tool(T_PPT, M365_LIC, M365_ACCT, [
        'Create a 10-slide Board presentation on Project SWIFT CLAIM and detariffication strategy. Slides: (1) Executive summary — combined ratio at 108% and key drivers, (2) Fraud analysis — claims leakage breakdown, (3) Top 10 suspicious workshops heat map, (4) Investigation plan and timeline, (5) Detariffication pricing strategy, (6) New premium rates by risk category, (7) Retention vs repricing decision matrix, (8) Financial impact — if fraud reduced by 50% and detariffication implemented, (9) Key risks, (10) Recommended decisions for Board approval. Use navy blue and white colour scheme.',
        'Create speaker notes for each slide. The CEO presenting has a habit of going off-topic — the notes should include a bracketed "[STOP HERE]" marker to help her stay on time. Each slide should be 45 seconds maximum.',
        'Add an appendix slide with a 2x2 risk matrix showing the four key risks to our detariffication strategy: underprice risk, competitor aggression, BNM supervisory scrutiny, and claims inflation. Place each risk in the appropriate quadrant based on likelihood and impact.'
      ]),
      tool(T_OUTLOOK, M365_LIC, M365_ACCT, [
        'Draft a formal notification letter to BNM\'s Insurance Supervision Department regarding the suspected claims fraud syndicate. The letter should: explain the nature and scale of the suspected fraud, describe the internal investigation steps taken, request guidance on whether BNM expects a formal regulatory notification, and propose a meeting to discuss. Use the formal tone required for BNM correspondence.',
        'Draft an internal email to all claims adjusters and investigators briefing them on Project SWIFT CLAIM. The email should explain the investigation without naming specific workshops yet, instruct adjusters to flag any motor claim over MYR 15,000 for secondary review, and ask them to report any unusual patterns they have observed. Remind them of the strict confidentiality requirement.',
        'Summarise the last 10 emails in my inbox related to claims or fraud. Identify any that require a response today, any that contain regulatory communications, and any where a commitment was made that has not yet been fulfilled. Present as a prioritised action list.'
      ]),
      tool(T_TEAMS, M365_LIC, M365_ACCT, [
        'Open an existing recorded Teams meeting recap from a claims committee or fraud taskforce meeting. Summarise all fraud case updates discussed, decisions made on claims suspension or rejection, and any escalation actions agreed. Format as a fraud committee minute.',
        'Ask Copilot in the recap: Draft a follow-up email to the investigation team summarising the actions agreed in this meeting. Include a table: Action | Owner | Deadline | Status (In Progress / Not Started).',
        'Were any specific workshop names or policy numbers discussed in this meeting? List them with the context in which they were mentioned so I can update the fraud watch list.'
      ], DESC_TEAMS),
      tool(T_NOTEBOOK, M365_LIC, M365_ACCT, [
        'Upload INS_01_Pacific_Shield_Insurance.xlsx and INS_02_Pacific_Shield_Strategy.docx to Copilot Notebook. Set instruction: "You are a senior insurance executive preparing a combined ratio recovery plan." Ask: Based on the claims data and our strategic priorities, what is a realistic combined ratio target we can achieve in 12 months if we implement both the fraud reduction programme and the detariffication repricing? Show your working and flag the two biggest assumptions in your estimate.',
        'Upload INS_01_Pacific_Shield_Insurance.xlsx and INS_02_Pacific_Shield_Strategy.docx. Ask: The strategy document commits to growing motor insurance market share. The claims data shows motor is deeply unprofitable at 108% CR. Is there a direct tension between these two objectives? How should the Board resolve this tension? Suggest two options with the financial trade-off for each.'
      ], DESC_NOTEBOOK),
      tool(T_COWORK, FRONTIER_LIC, M365_ACCT, [
        'Do all of the following: (1) Research the BNM guidelines on insurance fraud reporting obligations and the Malaysia Anti-Corruption Commission (MACC) referral process for insurance fraud syndicates. (2) Draft a 3-page legal and regulatory obligations summary for our General Counsel and Compliance Officer. (3) Save to OneDrive as "SWIFT CLAIM Regulatory Obligations Brief". (4) Email to the General Counsel and Chief Compliance Officer asking for review by Thursday. (5) Schedule a 90-minute "Project SWIFT CLAIM Legal Review" meeting for Friday at 2pm with the General Counsel, CRO, and Head of Claims.',
        'Do all of the following: (1) For each of the top 10 suspicious workshops identified in the fraud analysis, search our claims system emails for any prior complaints or irregularities. (2) Draft a workshop suspension notification letter template. (3) Create a tracking spreadsheet listing all 10 workshops with columns: Workshop Name | Fraud Score | Total Claims Value | Action Status | Date of Suspension Letter. (4) Save the spreadsheet to the Claims Team SharePoint folder. (5) Post in the #claims-fraud-taskforce Teams channel: "Top 10 suspicious workshops identified — suspension letters to be issued this week. See SharePoint for tracker."'
      ], DESC_COWORK),
      tool(T_WORD_AGT, M365_LIC, M365_ACCT, [
        'Open INS_02_Pacific_Shield_Strategy.docx in Word for Web. Create an agent called "Claims Policy Assistant". Description: "Answers questions from claims adjusters and investigators about Pacific Shield\'s claims handling procedures, fraud detection protocols, and workshop blacklisting policy." Share with the claims operations team.',
        'Demo: Ask the Claims Policy Assistant "A workshop has submitted three claims in 5 days for the same vehicle, all for different parts. What is our fraud flag threshold and what investigation steps am I required to take before approving any of the three claims?" Show how the agent provides consistent, policy-grounded guidance.'
      ], DESC_WORD_AGT),
      tool(T_PPT_AGT, M365_LIC, M365_ACCT, [
        'Create a PowerPoint from the Board fraud presentation and open in PowerPoint for Web. Create an agent called "SWIFT CLAIM Board Briefing Bot". Description: "Answers Board and Audit Committee questions about Project SWIFT CLAIM, fraud data, and the detariffication pricing strategy." Share with Board members ahead of the meeting.',
        'Demo: A Board member asks the agent "What is the estimated annual financial impact if we successfully reduce workshop fraud by 50%?" Then: "What legal risks do we face if we wrongly suspend a legitimate workshop?" Show how Board members get data-grounded answers before the meeting.'
      ], DESC_PPT_AGT),
      tool(T_XL_AGT, M365_LIC, M365_ACCT, [
        'Open INS_01_Pacific_Shield_Insurance.xlsx in Excel for Web. Create an agent called "Claims Analytics Q&A". Description: "Answers questions about Pacific Shield\'s motor claims data, combined ratio breakdown, fraud indicators, and renewal portfolio — for claims managers and the pricing team." Share with the actuarial and claims leadership.',
        'Demo: Ask the agent "What is the average claim value submitted by the top 3 highest-risk workshops compared to the national average?" Then: "How many policies are up for renewal in the next 30 days where the premium is below our breakeven rate?" Show instant access to critical pricing and claims intelligence.'
      ], DESC_XL_AGT),
      tool(T_BUILDER, M365_LIC, M365_ACCT, [
        'Go to copilotstudio.microsoft.com > Create > New Agent. Name it "Pacific Shield Claims Intelligence Agent". Description: "An AI assistant for Pacific Shield\'s claims and underwriting teams — answers questions about fraud detection, claims handling policy, combined ratio targets, and detariffication pricing strategy using official strategy and data documents." Upload INS_01_Pacific_Shield_Insurance.xlsx and INS_02_Pacific_Shield_Strategy.docx. Add a starter topic: "Help me assess a potentially fraudulent claim." Publish to Teams for Claims and Underwriting.',
        'Demo the agent in Teams. A claims adjuster asks: "I have a motor claim for MYR 28,000 from a workshop that has submitted 8 claims this month. Three of the claims involve the same loss adjuster. What fraud indicators should I document and what is the escalation path?" Show how the agent provides a structured investigation checklist and escalation guidance grounded in company policy.'
      ], DESC_BUILDER),
    ]),

# ── LIFE INSURANCE ─────────────────────────────────────────────────────────
ind('life-insurance','insurance','Life Insurance','💗','#283593','#3949AB',
    'Meridian Life Assurance Berhad',
    'RBC ratio 182% — agent channel productivity declining 18% as digital disruptors gain share.',
    'Meridian Life Assurance Berhad manages MYR 8.4B in life fund assets with an RBC ratio of 182% — comfortable but declining. Agent channel productivity has dropped 18% year-on-year as digital insurtech platforms capture first-time buyers. A new digital distribution initiative is being piloted in Q2 FY2026.',
    ['INS_01_Pacific_Shield_Insurance.xlsx','INS_02_Pacific_Shield_Strategy.docx'],
    [
      tool(T_CHAT, FREE_LIC, FREE_ACCT, [
        'I am the Chief Distribution Officer of a Malaysian life insurer. Our agent productivity has fallen 18% year-on-year and digital insurtech platforms are capturing the 25–35 age segment. Draft a strategic options paper of 300 words presenting three distinct approaches we could take: (1) defend and enhance the agent channel, (2) launch our own digital platform, (3) partner or acquire an insurtech. For each option, summarise the key advantages, risks, and estimated timeline to see results.',
        'Explain the BNM Risk-Based Capital (RBC) framework for Malaysian life insurers. What does an RBC ratio of 182% indicate, what are the regulatory minimum and supervisory target levels, and what actions would BNM take if the ratio fell below 130%? Keep the explanation suitable for a Board member with a legal background.',
        'What are the five key trends shaping the life insurance industry in Malaysia and Southeast Asia in 2025 and 2026? Focus on customer behaviour, regulation, and technology. Summarise each trend in three sentences.'
      ]),
      tool(T_RESEARCHER, M365_LIC, M365_ACCT, [
        'Research the competitive landscape for digital life insurance distribution in Malaysia. I need: (1) The main insurtech and digital-first life insurance platforms operating in Malaysia and their estimated market share, (2) The customer segments they are targeting, (3) Any BNM licensing requirements for digital insurance distribution. Summarise as a competitive intelligence brief with sources.',
        'Research life insurance product innovation trends in Southeast Asia — specifically investment-linked products (ILPs) and micro-insurance. Which markets are growing fastest and why? What product features are driving take-up among millennial and Gen Z buyers? Cite recent industry reports or research.'
      ], DESC_RESEARCHER),
      tool(T_ANALYST, M365_LIC, M365_ACCT, [
        'Analyse agent productivity data over the past 8 quarters. Calculate new policies per active agent, average premium per policy, and lapse rate by agent tier (Platinum, Gold, Silver, Bronze). Which agent tier has the highest lapse rate and lowest productivity? Create a scatter plot of agent tenure vs productivity score and identify whether newer agents (under 2 years) are performing better or worse than tenured agents.',
        'Perform a lapse rate cohort analysis — group policyholders by the year they purchased their policy and calculate the cumulative lapse rate at 1 year, 2 years, 3 years, and 5 years. Which vintage has the highest early lapse rate? Show as a cohort table and a line chart.'
      ], DESC_ANALYST),
      tool(T_EXCEL, M365_LIC, M365_ACCT, [
        'Using the Agent Performance tab in this workbook, Create a tier-based productivity dashboard for our 3,200 active agents. For each tier (Platinum, Gold, Silver, Bronze), calculate: (1) Average new annual premium equivalents (APE) per agent, (2) Persistency ratio (13-month), (3) Average income earned. Highlight in red any tier where persistency has dropped below 80%.',
        'In the Product Mix sheet, analyse the shift in product mix from FY2022 to FY2025. Has the proportion of ILP (Investment-Linked Plans) vs traditional life products changed? Calculate the revenue impact of this shift given that ILPs have lower margin than whole life products. Show as a stacked bar chart by year.',
        'Build a digital channel vs agent channel comparison on a new sheet. Compare: (1) Customer acquisition cost, (2) Average premium size, (3) Lapse rate at 12 months, (4) Cross-sell rate. If the digital channel has a 40% lower customer acquisition cost but 25% higher lapse rate, calculate the 5-year lifetime value difference between the two channels.'
      ]),
      tool(T_WORD, M365_LIC, M365_ACCT, [
        'Draft a 2-page agent productivity recovery plan. Cover: (1) Root causes of the 18% productivity decline (3 key reasons), (2) Three initiatives to reverse the trend — training uplift, digital tools for agents, performance incentive restructuring, (3) KPIs and targets for 12 months, (4) Investment required and expected ROI. Use an executive memo format.',
        'Identify all product mentions in this strategy document. For each product, determine whether it is positioned for the agent channel, digital channel, or both. Create a product-channel matrix table showing which products are currently channel-appropriate and which may need repositioning as the digital channel grows.',
        'Draft a 400-word internal communication from the CEO to all 3,200 agents explaining the digital initiative. The message should: reassure agents that the digital channel complements rather than replaces them, explain the new digital tools being rolled out to help agents, and invite agents to a town hall session next month. Tone: motivating and honest, not corporate-speak.'
      ]),
      tool(T_PPT, M365_LIC, M365_ACCT, [
        'Create an 8-slide presentation for the Board on the Digital Distribution Initiative. Include: (1) Problem statement — agent productivity decline and digital competition, (2) Market opportunity — digital life insurance market size, (3) Our proposed digital strategy, (4) Technology platform requirements, (5) Financial projections — APE and margin at Year 1, 2, 3, (6) Risk and mitigation, (7) Change management plan, (8) Decision required. Use a modern teal and white design.',
        'Generate a one-slide agent value proposition that clearly explains to our agent force why the digital initiative helps them rather than threatens them. Use three key messages, each with a supporting statistic. Design it as a simple visual slide they can share with their teams.',
        'Add a competitive landscape slide showing the digital insurtech players in Malaysia, their estimated market share, and the customer segment each targets. Use a simple 2x2 matrix (digital experience vs price) to position each player.'
      ]),
      tool(T_OUTLOOK, M365_LIC, M365_ACCT, [
        'Draft an email to BNM\'s Insurance Supervision Department requesting a pre-consultation meeting regarding our digital distribution platform. The email should describe the initiative at a high level, explain how it will comply with BNM\'s digital insurance guidelines, and request a 45-minute meeting to discuss regulatory expectations before we launch the pilot.',
        'Draft a recruitment email to three potential digital platform technology partners inviting them to submit a proposal for our digital distribution platform. The email should outline our requirements: policy issuance capability, e-KYC integration, BNM takaful separation compliance, and API-first architecture. Request a proposal within 3 weeks.',
        'I have 47 unread emails from my agents in the past week about the digital initiative announcement. Categorise them into: Concerns (worried about job security), Questions (want more information), Positive (supportive), and Suggestions. Draft a single FAQ document that addresses the top 5 concerns and 5 questions raised.'
      ]),
      tool(T_TEAMS, M365_LIC, M365_ACCT, [
        'Open a recorded Teams meeting recap from an agent or distribution team meeting. Identify all concerns raised about the digital initiative, any specific suggestions agents made for improving the agent toolset, and any commitments the management team made in response. Format as a structured feedback summary for the Digital Transformation team.',
        'Ask Copilot in the recap: Draft follow-up actions from this town hall meeting. Group actions into three categories: Immediate (this week), Short-term (this month), and Strategic (this quarter). Assign an owner to each.',
        'Based on this meeting, what is the overall sentiment of the agent force toward the digital initiative — positive, neutral, or negative? Identify the three most commonly expressed concerns and the one area where agents expressed the strongest support.'
      ], DESC_TEAMS),
      tool(T_NOTEBOOK, M365_LIC, M365_ACCT, [
        'Upload INS_01_Pacific_Shield_Insurance.xlsx and INS_02_Pacific_Shield_Strategy.docx. Set instruction: "You are the Chief Strategy Officer preparing the digital transformation business case for the Board." Ask: Based on the agent productivity data and our strategic objectives, what is the minimum number of digital policies we need to sell in Year 1 to offset the projected further decline in agent channel APE? What customer segment should we target first and why?',
        'Upload INS_01_Pacific_Shield_Insurance.xlsx and INS_02_Pacific_Shield_Strategy.docx. Ask: Are there any internal contradictions in our current strategy? Specifically, the document commits to growing APE by 12% while agent productivity is declining 18%. Is this growth target realistic without the digital channel? If not, what is a more credible target and what must we execute on to achieve it?'
      ], DESC_NOTEBOOK),
      tool(T_COWORK, FRONTIER_LIC, M365_ACCT, [
        'Do all of the following: (1) Research the top 5 insurtech platforms in Southeast Asia that offer white-label digital life insurance distribution and identify which ones have Malaysian regulatory approval. (2) Draft a vendor evaluation brief comparing their capabilities against our requirements. (3) Save to OneDrive as "Digital Distribution Vendor Shortlist". (4) Email to the CTO and CDO asking for input before the vendor RFP closes on Friday. (5) Schedule a 2-hour vendor review meeting for next Wednesday and invite the CTO, CDO, Head of Digital, and Head of Products.',
        'Do all of the following for agent productivity recovery: (1) Review the agent performance data and identify the bottom 20% of agents by APE who have been with the company more than 2 years. (2) Draft personalised coaching emails to each underperforming agent — the email should acknowledge their tenure, offer a 1-on-1 coaching session, and outline the new digital tools available to help them. (3) Schedule individual 30-minute coaching sessions for each agent over the next 4 weeks. (4) Create a tracking sheet in OneDrive with columns: Agent Name | Tier | Current APE | Target APE | Coaching Date | Follow-up Date.'
      ], DESC_COWORK),
      tool(T_WORD_AGT, M365_LIC, M365_ACCT, [
        'Open INS_02_Pacific_Shield_Strategy.docx in Word for Web. Create an agent called "Life Insurance Strategy Bot". Description: "Answers questions from agents and managers about Meridian Life\'s product strategy, distribution approach, RBC requirements, and digital initiative. Helps the agent force understand how the strategy affects their role and what tools are available to them." Share with the agent network.',
        'Demo: Ask the Strategy Bot "The digital platform is launching next quarter. Does this mean my territory will be split with digital customers? Will my commissions change for policies purchased online?" Show how the agent gets a clear, consistent answer from the official strategy document rather than rumour.'
      ], DESC_WORD_AGT),
      tool(T_PPT_AGT, M365_LIC, M365_ACCT, [
        'Create a PowerPoint from the Digital Distribution Initiative Board presentation. Create an agent called "Digital Initiative Board Q&A". Share with Board members before the meeting so they can review and prepare questions.',
        'Demo: A Board member asks "What is our projected RBC ratio impact if the digital initiative requires MYR 80M of capital investment over 3 years?" Then: "What happens to agent channel productivity projections if we do nothing — what does the 3-year outlook look like without the digital investment?" Show how the agent helps Board members challenge assumptions before the meeting.'
      ], DESC_PPT_AGT),
      tool(T_XL_AGT, M365_LIC, M365_ACCT, [
        'Open INS_01_Pacific_Shield_Insurance.xlsx in Excel for Web. Create an agent called "Life Portfolio Analytics Q&A". Description: "Instant answers on Meridian Life\'s policy portfolio, agent productivity, lapse rates, product mix, and RBC position — for actuarial, distribution, and senior management teams." Share broadly across the insurance division.',
        'Demo: Ask "What is the current 13-month persistency ratio for Platinum-tier agents and how does it compare to Silver-tier?" Then: "How many policies lapsed in the first 12 months across the investment-linked product range in FY2025?" Show how the actuarial and distribution teams access precise portfolio intelligence instantly.'
      ], DESC_XL_AGT),
      tool(T_BUILDER, M365_LIC, M365_ACCT, [
        'Go to copilotstudio.microsoft.com > Create > New Agent. Name it "Meridian Life Agent Support Bot". Description: "Supports Meridian Life\'s 3,200 agents with instant answers on products, policy administration, RBC position, commission structures, and the digital transformation initiative — reducing calls to the agency support desk and ensuring agents have consistent, accurate information." Upload INS_02_Pacific_Shield_Strategy.docx. Add topics: "Product Questions", "Commission & Incentives", "Digital Tools", "RBC & Financial Questions". Publish to Teams for all agents.',
        'Demo the agent: An agent asks "I have a client who wants to surrender a 3-year ILP policy. What is the surrender value calculation and are there any early surrender penalties? What alternatives should I discuss before the client decides to surrender?" Show how the agent provides a complete, policy-grounded response that helps the agent retain the client rather than simply processing a surrender.'
      ], DESC_BUILDER),
    ]),

# ── TAKAFUL ─────────────────────────────────────────────────────────────────
ind('takaful','insurance','Takaful','☪','#1A237E','#1976D2',
    'Amanah Takaful Group Berhad',
    'MYR 4.2B tabarru\' fund — wakalah fee model under BNM IFSA Takaful review.',
    'Amanah Takaful Group Berhad manages a MYR 4.2B tabarru\' fund under a wakalah fee model. The BNM IFSA Takaful Operational Framework review is due in 6 weeks. Re-takaful arrangements with Middle East counterparties need renegotiation, and the family takaful segment is facing lapse pressure from new competitors offering lower wakalah fees.',
    ['INS_01_Pacific_Shield_Insurance.xlsx','INS_02_Pacific_Shield_Strategy.docx'],
    [
      tool(T_CHAT, FREE_LIC, FREE_ACCT, [
        'Explain the difference between the wakalah and mudharabah fee models in takaful in plain language. Which model is more common in Malaysia and why? What are the key considerations a takaful operator must disclose to participants under BNM\'s IFSA Takaful Operational Framework? Keep the explanation under 200 words.',
        'What is the role of a re-takaful arrangement and how does it differ from conventional reinsurance? List three key structuring principles that must be met for a re-takaful arrangement to comply with Shariah requirements, and name two major Middle Eastern re-takaful operators that are active in Southeast Asia.',
        'Draft a simple FAQ for family takaful participants who are asking about lapse consequences. The FAQ should cover: what happens to the tabarru\' fund contribution if they lapse, whether they can reinstate a lapsed certificate, the qard (loan) provision if the fund is insufficient, and the surrender value calculation. Use plain, jargon-free language.'
      ]),
      tool(T_RESEARCHER, M365_LIC, M365_ACCT, [
        'Research the competitive landscape for family takaful in Malaysia — specifically how new digital takaful operators are pricing their wakalah fees versus established operators. I need market data on average wakalah fee rates, the fastest-growing takaful distribution channels, and any BNM statements on competitive pricing in takaful. Provide citations.',
        'Research BNM\'s IFSA Takaful Operational Framework requirements updated since 2023. What are the key changes operators must implement? Specifically, what are the requirements around tabarru\' fund surplus distribution, waqf-linked takaful, and participant disclosure? Present as a compliance checklist.'
      ], DESC_RESEARCHER),
      tool(T_ANALYST, M365_LIC, M365_ACCT, [
        'Upload INS_01_Pacific_Shield_Insurance.xlsx (use as takaful portfolio proxy). Ask Analyst: Analyse the tabarru\' fund surplus/deficit trend over the past 8 quarters. Is the fund trending toward deficit? Calculate the required additional contribution rate increase to maintain a 15% surplus buffer. Show as a chart and a sensitivity table under three scenarios: claims stay flat, claims rise 10%, claims rise 20%.',
        'Compare lapse rates across the three main family takaful product categories. Which product has the highest lapse rate and at what certificate duration does lapsing peak? Create a lapse rate heat map by product and certificate age (years 1 through 5).'
      ], DESC_ANALYST),
      tool(T_EXCEL, M365_LIC, M365_ACCT, [
        'Using the relevant tab in this workbook, Build a tabarru\' fund sustainability model on a new sheet. Inputs: current fund balance of MYR 4.2B, annual new contribution inflow, claims outgo, wakalah fee deduction (15% of contributions), and investment income at 4.8% return. Show a 5-year projection under three scenarios: no growth, 5% contribution growth, and 10% lapse increase. Highlight in red any scenario where the fund balance drops below the BNM minimum surplus threshold.',
        'Create a wakalah fee benchmarking table comparing Amanah Takaful\'s 15% wakalah fee against the five largest family takaful operators in Malaysia. For each competitor, show the wakalah fee rate, market share, and 5-year lapse rate trend. Source: use data from the portfolio sheet and add competitor data manually where available.',
        'In the Re-Takaful Arrangements sheet, identify the three largest re-takaful treaties by ceded premium. For each, calculate the cession ratio, the retention after re-takaful, and the expiry date. Flag any treaty expiring within 6 months that has not been marked as "Renewal In Progress".'
      ]),
      tool(T_WORD, M365_LIC, M365_ACCT, [
        'Draft a 2-page BNM IFSA Takaful Operational Framework compliance readiness assessment. Structure: (1) Key framework requirements, (2) Our current compliance status for each (Compliant / Partial / Gap), (3) Action plan for the 3 gap areas, (4) Timeline to full compliance before the review in 6 weeks. Use a formal regulatory tone.',
        'Draft a re-takaful renegotiation brief for the CFO. Cover: the three re-takaful treaties being renegotiated, the current terms, our negotiating objectives (target cession ratio reduction from 40% to 32%, maintain catastrophe cover), the walk-away terms, and a BATNA (Best Alternative to a Negotiated Agreement). Keep it to one page.',
        'Write a participant communication explaining the annual tabarru\' fund surplus distribution. The letter should explain how the surplus was calculated, how much each participant will receive based on their contribution, the payment date, and the option to donate their surplus to a waqf fund. Keep it warm and clear, under 300 words.'
      ]),
      tool(T_PPT, M365_LIC, M365_ACCT, [
        'Create an 8-slide BNM IFSA compliance presentation for the Board Shariah and Audit Committee. Include: (1) IFSA framework overview and key changes, (2) Our compliance status — RAG dashboard, (3) Top 3 gap areas and remediation plan, (4) Re-takaful renegotiation update, (5) Tabarru\' fund sustainability — 5-year projection, (6) Lapse rate concern and retention strategy, (7) Key risks and mitigants, (8) Decisions required. Use a teal and gold Islamic-themed design.',
        'Add a one-page Shariah compliance declaration slide that can be included in our annual report. It should confirm that all products and investments comply with the BNM Shariah Advisory Council standards, reference the specific fatwas relied upon, and include a quote from our Shariah Committee Chairman.',
        'Create a 3-slide mini-presentation on our lapse reduction strategy for the agency network. Slides: (1) Current lapse rate by product and agent tier, (2) Root causes — top 3 reasons participants lapse, (3) Retention action plan with agent incentives. Keep it simple — this will be shown at a branch level town hall.'
      ]),
      tool(T_OUTLOOK, M365_LIC, M365_ACCT, [
        'Draft a formal letter to BNM\'s Takaful Supervision Unit ahead of the IFSA review. The letter should: confirm we have received the review schedule, provide a brief self-assessment of our compliance status, note two areas where we are seeking regulatory guidance, and request a pre-review engagement meeting. Use formal BNM correspondence tone.',
        'Draft a re-takaful renegotiation invitation letter to our three Middle Eastern re-takaful counterparties. The letter should: acknowledge the expiry of the current treaties, propose a face-to-face negotiation meeting in Kuala Lumpur or Dubai, outline our key negotiating priorities, and suggest three available weeks for the meeting.',
        'Summarise the last 3 months of email correspondence with our largest re-takaful counterparty. Identify their key concerns, any commitments we made in writing, and any open items that need to be resolved before treaty renewal.'
      ]),
      tool(T_TEAMS, M365_LIC, M365_ACCT, [
        'Open an existing recorded Teams meeting recap from a risk or compliance committee. Identify all IFSA compliance-related action items discussed. For each, note the owner, the deadline, and whether it was marked as completed or still pending at the time of the meeting.',
        'Draft a post-meeting summary for the Re-Takaful Renegotiation Taskforce based on this meeting. Include: key terms agreed, points still in negotiation, the next negotiation round date, and the escalation path if the parties cannot reach agreement on the cession ratio.',
        'Were any Shariah compliance concerns raised in this meeting? List each concern with the context and the proposed resolution. Flag any that will require Shariah Committee sign-off before implementation.'
      ], DESC_TEAMS),
      tool(T_NOTEBOOK, M365_LIC, M365_ACCT, [
        'Upload INS_01_Pacific_Shield_Insurance.xlsx and INS_02_Pacific_Shield_Strategy.docx. Set instruction: "You are a takaful expert advising the CEO on BNM IFSA compliance and competitive positioning." Ask: Based on the portfolio data and our strategy, what is the single biggest risk to our tabarru\' fund sustainability over the next 3 years? What one action should the Board approve immediately to address it?',
        'Upload INS_01_Pacific_Shield_Insurance.xlsx and INS_02_Pacific_Shield_Strategy.docx. Ask: Our wakalah fee of 15% is above the market median of 12%. The strategy document commits to growing family takaful market share. Are these two objectives consistent? What would we need to do to reduce the wakalah fee to 12% without impairing profitability, and how long would the transition take?'
      ], DESC_NOTEBOOK),
      tool(T_COWORK, FRONTIER_LIC, M365_ACCT, [
        'Do all of the following: (1) Research the latest BNM IFSA Takaful Operational Framework updates and any accompanying guidance notes published since 2024. (2) Summarise the 5 most critical requirements in a compliance action plan document. (3) Save to OneDrive as "IFSA Takaful Compliance Action Plan - [Date]". (4) Email to the Chief Compliance Officer and Head of Shariah Compliance asking for review and sign-off by Wednesday. (5) Schedule a 2-hour IFSA Compliance Readiness Workshop for Thursday with the compliance, product, and operations teams.',
        'Do all of the following for the lapse reduction initiative: (1) Identify all family takaful certificates that have been inactive (no premium payment) for 60–90 days and are at risk of lapsing. (2) Draft a personalised re-engagement message to each participant — the message should remind them of their takaful coverage, explain the lapse consequence, and offer a payment extension. (3) Send the messages via email to all identified participants. (4) Create a tracking log in SharePoint with participant name, certificate number, last payment date, and re-engagement email sent date. (5) Schedule a follow-up check for 2 weeks later to identify who has resumed payment.'
      ], DESC_COWORK),
      tool(T_WORD_AGT, M365_LIC, M365_ACCT, [
        'Open INS_02_Pacific_Shield_Strategy.docx in Word for Web. Create an agent called "Takaful Operations Policy Bot". Description: "Answers questions from operations staff, agents, and Shariah compliance teams about Amanah Takaful\'s operational policies, IFSA compliance requirements, and product structures." Share with the takaful operations and compliance teams.',
        'Demo: Ask the agent "A participant wants to increase their tabarru\' contribution mid-term. What is the process, and does it require a new medical underwriting assessment? Is there a minimum increase amount?" Show how the agent gives a policy-accurate response that the operations team can act on confidently.'
      ], DESC_WORD_AGT),
      tool(T_PPT_AGT, M365_LIC, M365_ACCT, [
        'Create a PowerPoint from the IFSA Board compliance presentation. Create an agent called "IFSA Compliance Board Bot". Share with Board members and the Shariah Committee.',
        'Demo: A Shariah Committee member asks "What is our current tabarru\' fund surplus ratio and what is the minimum BNM requires before we can distribute surplus to participants?" Show how the agent provides a precise, data-grounded answer based on the presentation content.'
      ], DESC_PPT_AGT),
      tool(T_XL_AGT, M365_LIC, M365_ACCT, [
        'Open INS_01_Pacific_Shield_Insurance.xlsx in Excel for Web. Create an agent called "Takaful Fund Analytics Q&A". Description: "Answers questions about Amanah Takaful\'s fund performance, lapse rates, re-takaful cession ratios, and wakalah fee benchmarks." Share with actuarial and senior management.',
        'Demo: Ask "What is the current lapse rate for family takaful policies in their second year of contribution?" Then: "If lapse rates increase by 15%, by how much would the tabarru\' fund balance decline in year 1, assuming all other factors remain constant?" Show how management gets scenario intelligence rapidly.'
      ], DESC_XL_AGT),
      tool(T_BUILDER, M365_LIC, M365_ACCT, [
        'Go to copilotstudio.microsoft.com > Create > New Agent. Name it "Amanah Takaful Participant Assistant". Description: "Helps participants and agents answer questions about family takaful coverage, contributions, tabarru\' fund surplus, lapse consequences, and Shariah compliance — grounded in official takaful documents and policy terms." Upload INS_02_Pacific_Shield_Strategy.docx. Add topics: "Coverage Questions", "Contribution & Payment", "Lapse & Reinstatement", "Surplus Distribution". Publish to Teams and the participant self-service portal.',
        'Demo the agent: A participant asks "I missed two months of contributions due to a medical emergency. Can I reinstate my certificate and what is the grace period? Will my existing coverage remain valid during the reinstatement process?" Show how the agent gives a complete, Shariah-compliant response that helps the participant make an informed decision.'
      ], DESC_BUILDER),
    ]),
]

print(f"Batch 2 written: {len(INDUSTRIES_2)} entries")
