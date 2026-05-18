import sys; sys.path.insert(0,'.')
from util import *


def _oxford(items):
    items = [str(x) for x in items if str(x).strip()]
    if not items:
        return ''
    if len(items) == 1:
        return items[0]
    if len(items) == 2:
        return f"{items[0]} and {items[1]}"
    return ", ".join(items[:-1]) + f", and {items[-1]}"


def _sentences(*parts):
    return " ".join(str(p).strip() for p in parts if str(p).strip())


def _sheet_ref(workbook, sheets, idxs, doc1, doc2, prefix='Use'):
    chosen = [sheets[i] for i in idxs]
    return f"{prefix} {workbook}, especially the {_oxford(chosen)} sheets, together with {doc1} and {doc2} as source context"


def _prompt(role, company, ref_sentence, task_sentence, output_sentence, analysis_sentence=None):
    analysis_sentence = analysis_sentence or 'Quantify the issue, separate confirmed facts from assumptions, and make the Red, Amber, and Green items explicit.'
    return _sentences(
        f"You are the {role} at {company}.",
        f"{ref_sentence} for {task_sentence}.",
        analysis_sentence,
        output_sentence,
    )


def _research_prompt(role, company, ref_sentence, task_sentence, output_sentence):
    return _sentences(
        f"You are the {role} at {company}.",
        f"{ref_sentence} while you research {task_sentence}.",
        output_sentence,
        'Flag any claim that could not be independently verified.',
    )


def build_entry(cfg):
    workbook, doc1, doc2 = cfg['files']
    sheets = cfg['sheets']
    role1, role2, role3 = cfg['roles']
    challenge = cfg['challenge']
    deadline = cfg['deadline']
    board_body = cfg['board_body']
    team = cfg['team']
    external_party = cfg['external_party']
    stakeholders = cfg['stakeholders']
    peer_set = cfg['peer_set']
    regulators = cfg['regulators']
    agent_name = cfg['agent_name']
    agent_share = cfg['agent_share']
    topics = cfg['topics']
    topic_text = _oxford(topics)
    agent_desc = cfg.get('agent_desc') or (
        f"Supports {team} with instant answers on {topic_text}, helping leaders make faster, evidence-led decisions."
    )
    word_agent_name = cfg.get('word_agent_name') or f"{cfg['short_name']} Word Guide"
    ppt_agent_name = cfg.get('ppt_agent_name') or f"{cfg['short_name']} Deck Navigator"
    xl_agent_name = cfg.get('xl_agent_name') or f"{cfg['short_name']} Data Q&A"
    demo_question = cfg['demo_question']
    builder_crisis = cfg['builder_crisis']

    generic_ref = _sheet_ref(workbook, sheets, [0, 1, 2], doc1, doc2)
    alt_ref = _sheet_ref(workbook, sheets, [1, 2, 3], doc1, doc2)
    late_ref = _sheet_ref(workbook, sheets, [2, 3, 4], doc1, doc2)

    prompts = [
        tool(T_CHAT, FREE_LIC, FREE_ACCT, [
            _prompt(
                role1, company=cfg['company'], ref_sentence=generic_ref,
                task_sentence=challenge,
                output_sentence=f"Present the answer as a RAG table with columns for Issue, Evidence, Impact, and Recommended Decision for the next {deadline}.",
            ),
            _prompt(
                role2, company=cfg['company'], ref_sentence=alt_ref,
                task_sentence=f"a 30-60-90 day recovery and prioritisation plan for {challenge}",
                output_sentence="Present the answer as a RAG action plan with sections for Do Now, Do Next, and Monitor, including the owner for each action.",
            ),
            _prompt(
                role3, company=cfg['company'], ref_sentence=late_ref,
                task_sentence=f"a stakeholder and governance map for {challenge}",
                output_sentence="Present the answer as a RAG matrix with columns for Audience, Message, Timing, Owner, and Risk if delayed.",
            ),
        ]),
        tool(T_RESEARCHER, M365_LIC, M365_ACCT, [
            _research_prompt(
                role2, cfg['company'], generic_ref,
                f"how Malaysia, Indonesia, and wider ASEAN peers have handled comparable situations involving {challenge}, with special attention to {peer_set}",
                "Cite primary sources with publication dates and present the findings as a RAG table with columns for Organisation, Trigger, Action Taken, Outcome, and Relevance.",
            ),
            _research_prompt(
                role3, cfg['company'], alt_ref,
                f"the regulatory and market-practice expectations relevant to this issue, including {regulators}",
                "Separate mandatory requirements from market practice, cite the original regulator or publication for each point, and present the findings as a RAG table with columns for Requirement, Jurisdiction, Timing, and Practical Implication.",
            ),
            _research_prompt(
                role1, cfg['company'], late_ref,
                f"which control, operating-model, and governance practices most reliably reduce repeat issues linked to {challenge}",
                "Present the answer as a RAG playbook with columns for Practice, Evidence, Benefit, and Applicability to our situation, using original-source citations throughout.",
            ),
        ], DESC_RESEARCHER),
        tool(T_ANALYST, M365_LIC, M365_ACCT, [
            _prompt(
                role1, cfg['company'],
                f"Upload {workbook} to Analyst and use the {_oxford([sheets[0], sheets[1], sheets[2]])} sheets, with {doc1} and {doc2} as supporting context",
                challenge,
                "Present the answer as a RAG table with columns for Driver, Evidence, Quantified Impact, and Immediate Action.",
            ),
            _prompt(
                role2, cfg['company'],
                f"Upload {workbook} to Analyst and focus on the {_oxford([sheets[1], sheets[2], sheets[3]])} sheets while cross-checking {doc1} and {doc2}",
                f"the root causes, trend breaks, and concentration risks behind {challenge}",
                "Present the findings as a RAG table with columns for Signal, What Changed, Why It Matters, and Escalation Needed.",
            ),
            _prompt(
                role3, cfg['company'],
                f"Upload {workbook} to Analyst and use the {_oxford([sheets[2], sheets[3], sheets[4]])} sheets with {doc1} and {doc2}",
                f"a forward-looking scenario view of {challenge}",
                "Model a base, downside, and severe case, then present the answer as a RAG watchlist with columns for Scenario, Trigger, Exposure, and Management Response.",
            ),
        ], DESC_ANALYST),
        tool(T_EXCEL, M365_LIC, M365_ACCT, [
            _prompt(
                role2, cfg['company'],
                f"In {workbook}, use the {_oxford([sheets[0], sheets[1]])} sheets and align the output with {doc1} and {doc2}",
                "a leadership dashboard",
                "Create a new worksheet called 'Leadership Dashboard' with key metrics, top exceptions, and RAG conditional formatting that can be used in a weekly executive review.",
                "Calculate the core variances, show the top three Red exceptions at the top of the sheet, and keep the formulas refreshable from the source tabs.",
            ),
            _prompt(
                role1, cfg['company'],
                f"In {workbook}, use the {_oxford([sheets[1], sheets[2], sheets[3]])} sheets with guidance from {doc1} and {doc2}",
                "an exception tracker",
                "Create a new worksheet called 'Exception Tracker' with columns for Issue, Metric, Threshold, Current Value, Owner, Due Date, and RAG Status.",
                "Sort the Red items first, include formulas for threshold breaches, and make the sheet easy to update during live review meetings.",
            ),
            _prompt(
                role3, cfg['company'],
                f"In {workbook}, use the {_oxford([sheets[2], sheets[3], sheets[4]])} sheets and the operating principles in {doc1} and {doc2}",
                "a 90-day watchlist",
                "Create a new worksheet called '90-Day Watchlist' that summarises risks, milestones, owners, and RAG status, with a compact summary block at the top for leadership.",
                "Use formulas, filters, and conditional formatting so the sheet becomes the single working tracker for the next quarter.",
            ),
        ]),
        tool(T_WORD, M365_LIC, M365_ACCT, [
            _prompt(
                role1, cfg['company'], generic_ref,
                f"a 2-page decision memo for the {board_body} on {challenge}",
                "Begin with a RAG executive summary, then structure the paper into Current Position, What Changed, Decisions Required, and Next 30 Days.",
            ),
            _prompt(
                role2, cfg['company'], alt_ref,
                f"an operating paper that translates {challenge} into clear accountabilities for {team}",
                "Present the output as a formal note with a RAG table for Workstream, Owner, Due Date, and Dependency, followed by a concise operating narrative.",
            ),
            _prompt(
                role3, cfg['company'], late_ref,
                f"a stakeholder annex covering how {stakeholders} should be updated on {challenge}",
                "Present the output as a RAG communications annex with Audience, Message, Approval Owner, Timing, and Risk if the wording is wrong.",
            ),
        ]),
        tool(T_PPT, M365_LIC, M365_ACCT, [
            _prompt(
                role1, cfg['company'], generic_ref,
                f"a 5-slide leadership deck on {challenge}",
                "Create a 5-slide deck with one headline message per slide, a clear RAG callout on every slide, and a final slide titled 'Decisions Required This Week'.",
            ),
            _prompt(
                role2, cfg['company'], alt_ref,
                f"a 3-slide working-session deck for {team}",
                "Create a 3-slide deck covering current status, top blockers, and next-step commitments, using RAG coding that can be understood in under 2 minutes per slide.",
            ),
            _prompt(
                role3, cfg['company'], late_ref,
                f"a 2-slide stakeholder update for {external_party}",
                "Create a 2-slide deck with a factual RAG summary, the most important quantified evidence, and the actions now under way.",
            ),
        ]),
        tool(T_OUTLOOK, M365_LIC, M365_ACCT, [
            _prompt(
                role1, cfg['company'], generic_ref,
                f"an internal escalation email on {challenge}",
                "Write a polished email with a strong subject line that opens with a one-line RAG status, summarises the evidence, and asks for the exact decision or approval needed.",
            ),
            _prompt(
                role2, cfg['company'], alt_ref,
                f"an update email to {external_party} on {challenge}",
                "Write a measured external-facing email that includes a short RAG summary, the key facts, what is being done now, and what update will follow next.",
            ),
            _prompt(
                role3, cfg['company'], late_ref,
                f"a mobilisation email to {team}",
                "Write a direct internal email that begins with a RAG summary and ends with three bullets titled 'What must happen today'.",
            ),
        ]),
        tool(T_TEAMS, M365_LIC, M365_ACCT, [
            _prompt(
                role1, cfg['company'],
                f"Use this recorded Teams meeting recap alongside {workbook}, especially the {_oxford([sheets[0], sheets[1], sheets[2]])} sheets, and cross-check against {doc1} and {doc2}",
                challenge,
                "Present the output as a RAG action log with columns for Decision, Owner, Due Date, and Must-Close-Before status.",
            ),
            _prompt(
                role2, cfg['company'],
                f"Use this recorded Teams meeting recap together with {workbook}, especially the {_oxford([sheets[1], sheets[2], sheets[3]])} sheets, and {doc1} plus {doc2}",
                f"extracting the most important decisions, unresolved issues, and follow-up actions related to {challenge}",
                "Summarise the meeting in four sections titled Key Facts, Risks Raised, Decisions Taken, and Follow-Up Actions, with a short RAG status at the top.",
            ),
            _prompt(
                role3, cfg['company'],
                f"Use this recorded Teams meeting recap alongside {workbook}, especially the {_oxford([sheets[2], sheets[3], sheets[4]])} sheets, and the guidance in {doc1} and {doc2}",
                f"identifying which discussion points are most sensitive if mishandled externally or internally for {challenge}",
                "Present the answer as a RAG table with columns for Topic, Why Sensitive, Suggested Holding Line, and Who Must Approve.",
            ),
        ], DESC_TEAMS),
        tool(T_NOTEBOOK, M365_LIC, M365_ACCT, [
            _prompt(
                role1, cfg['company'],
                f"Upload {workbook}, {doc1}, and {doc2} to Copilot Notebook and focus on the {_oxford([sheets[0], sheets[1], sheets[2]])} sheets",
                challenge,
                "Set the instruction to require source citations for every major point, then ask for a RAG synthesis with the sections What We Know, What We Still Need to Verify, and Decisions Required.",
            ),
            _prompt(
                role2, cfg['company'],
                f"Upload {workbook}, {doc1}, and {doc2} to Copilot Notebook and focus on the {_oxford([sheets[1], sheets[3], sheets[4]])} sheets",
                f"comparing the strongest response options for {challenge}",
                "Ask Notebook to produce a RAG option paper with Option, Benefits, Risks, Dependencies, and Recommended Choice, citing the source file for every recommendation.",
            ),
            _prompt(
                role3, cfg['company'],
                f"Upload {workbook}, {doc1}, and {doc2} to Copilot Notebook and focus on the {_oxford([sheets[0], sheets[2], sheets[4]])} sheets",
                f"preparing for the hardest questions leaders will ask about {challenge}",
                "Ask for a RAG-ready briefing with sections for Likely Question, Best Evidence, Gaps to Close, and Pre-Read Needed, all with citations.",
            ),
        ], DESC_NOTEBOOK),
        tool(T_COWORK, FRONTIER_LIC, M365_ACCT, [
            _prompt(
                role1, cfg['company'], generic_ref,
                f"an autonomous work package on {challenge}",
                f"Research the issue, draft a 2-page brief, save it to OneDrive, email it to {stakeholders}, and schedule a review meeting within the next {deadline}. Include a RAG summary at the top of the brief and a task list for {team} owners.",
                "Make the output executive-ready, action-oriented, and easy to circulate without further rewriting.",
            ),
            _prompt(
                role2, cfg['company'], alt_ref,
                f"a coordinated action programme for {challenge}",
                f"Create a working tracker, assign tasks to the right owners across {team}, send the task list by email, and schedule a checkpoint meeting with the decision-makers responsible for {challenge}. Save the tracker to OneDrive and ensure every workstream has a RAG status and due date.",
                "Keep the actions tightly sequenced so leadership can see what will be completed before the next review.",
            ),
        ], DESC_COWORK),
        tool(T_EDIT_COPILOT, M365_LIC, M365_ACCT, [
            _prompt(
                role3, cfg['company'],
                f"Using {doc1} in Word for Web and drawing on the {_oxford([sheets[0], sheets[1], sheets[2]])} sheets in {workbook} plus {doc2}",
                f"editing the document so it better supports {challenge}",
                "Add a new appendix with a decision-rights table, escalation timeline, and RAG checklist, keeping the tone and structure consistent with the existing document.",
                "Only add changes that strengthen execution clarity and make the next review cycle easier to manage.",
            ),
            _prompt(
                role1, cfg['company'],
                f"Using {workbook} in Excel or PowerPoint for Web and focusing on the {_oxford([sheets[1], sheets[2], sheets[3]])} sheets with context from {doc1} and {doc2}",
                f"editing the working materials for {challenge}",
                "Create or refine a RAG tracker that surfaces the top exceptions first, refreshes automatically from source values where possible, and is styled for leadership review.",
                "Reorder the content so decision-makers see the most urgent Red issues before the supporting detail.",
            ),
        ], DESC_EDIT_COPILOT),
        tool(T_WORD_AGT, ANY_LIC, ANY_ACCT, [
            _prompt(
                role3, cfg['company'],
                f"Open {doc1} in Word for Web and use the {_oxford([sheets[0], sheets[2], sheets[4]])} sheets in {workbook} plus {doc2}",
                f"creating a new Word agent called '{word_agent_name}'",
                f"Describe it as an assistant that helps {team} answer questions on {topic_text}, set the document as the knowledge source, and share it with {agent_share}.",
                "Keep the description specific enough that users know exactly when to rely on the agent.",
            ),
            _prompt(
                role1, cfg['company'],
                f"Use the '{word_agent_name}' Word agent together with the context in {workbook}, especially the {_oxford([sheets[0], sheets[1], sheets[2]])} sheets",
                f"demoing how it handles the question: {demo_question}",
                "Show the response as a concise RAG answer that cites the underlying document logic and ends with a clear recommended next step.",
                "Make the demo feel realistic enough for leadership to see immediate value.",
            ),
        ], DESC_WORD_AGT),
        tool(T_PPT_AGT, ANY_LIC, ANY_ACCT, [
            _prompt(
                role1, cfg['company'],
                f"Use {workbook}, especially the {_oxford([sheets[0], sheets[1], sheets[3]])} sheets, with {doc1} and {doc2}",
                f"building the leadership deck and then creating a PowerPoint agent called '{ppt_agent_name}'",
                f"Describe it as a presentation navigator for {topic_text} and share it with {agent_share}.",
                "Ensure the agent can direct users to the right slide, chart, or talking point quickly during a live discussion.",
            ),
            _prompt(
                role2, cfg['company'],
                f"Use the '{ppt_agent_name}' PowerPoint agent together with the deck sourced from {workbook}, especially the {_oxford([sheets[1], sheets[2], sheets[4]])} sheets",
                f"demoing how it answers the question: {demo_question}",
                "Ask it to point to the best slide, summarise the Red issues in under 80 words, and recommend the most important next action.",
                "Keep the demo crisp and executive-facing.",
            ),
        ], DESC_PPT_AGT),
        tool(T_XL_AGT, ANY_LIC, ANY_ACCT, [
            _prompt(
                role2, cfg['company'],
                f"Open {workbook} in Excel for Web and use the {_oxford([sheets[0], sheets[1], sheets[2]])} sheets",
                f"creating an Excel agent called '{xl_agent_name}'",
                f"Describe it as a workbook assistant for {topic_text}, then share it with {agent_share} so users can query the data in plain English.",
                "Make sure the description highlights the most important metrics and why the workbook can be trusted.",
            ),
            _prompt(
                role1, cfg['company'],
                f"Use the '{xl_agent_name}' Excel agent on {workbook}, especially the {_oxford([sheets[1], sheets[3], sheets[4]])} sheets",
                f"demoing how it answers the question: {demo_question}",
                "Ask for a RAG answer that identifies the most important metric, the supporting evidence, and the owner who should act next.",
                "Show how the agent turns workbook data into a decision-ready response in seconds.",
            ),
        ], DESC_XL_AGT),
        tool(T_BUILDER, M365_LIC, M365_ACCT, [
            _prompt(
                role1, cfg['company'],
                f"Go to copilotstudio.microsoft.com and use {workbook}, especially the {_oxford([sheets[0], sheets[1], sheets[2]])} sheets, with {doc1} and {doc2}",
                f"building a new Copilot Studio agent called '{agent_name}'",
                f"Use this description: '{agent_desc}' and add topics for {topic_text}, then publish it for {agent_share}.",
                "Keep the setup focused on fast, trustworthy answers and clear escalation paths for Red items.",
            ),
            _prompt(
                role3, cfg['company'],
                f"Use the '{agent_name}' Copilot Studio agent with the knowledge drawn from {workbook}, especially the {_oxford([sheets[2], sheets[3], sheets[4]])} sheets, plus {doc1} and {doc2}",
                f"demoing how it handles this real-world scenario: {builder_crisis}",
                "Show the agent giving a concise RAG answer, citing the most relevant evidence, and recommending the first action to approve immediately.",
                "Make the demo feel like a live leadership intervention, not a generic chatbot exchange.",
            ),
        ], DESC_BUILDER),
    ]

    return ind(
        cfg['id'],
        cfg['sectorId'],
        cfg['name'],
        cfg['icon'],
        cfg['color'],
        cfg['accent'],
        cfg['company'],
        cfg['tagline'],
        cfg['scenario'],
        cfg['files'],
        prompts,
        companyID=cfg.get('companyID', ''),
        taglineID=cfg.get('taglineID', ''),
        subsector=cfg.get('subsector', ''),
    )
