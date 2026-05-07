import io, re

with open('util.py','r',encoding='utf-8') as f: s = f.read()

new_teams = "DESC_TEAMS = 'For this demo we use Copilot grounded in the Teams Recap on the demo tenant for one of four meetings: \"New Software Implementation\", \"Potential Merger\", \"Negotiating Marketing Contract\", or \"Marketing Campaign Performance Review\". Workflow: Open the meeting in your Teams calendar > the Recap page opens with AI Notes, chapters, transcript and action items > click the Copilot icon in the top right of the Recap page > Copilot opens grounded in the meeting transcript > type your minutes prompt > copy the structured output into a new Word document (or open M365 Copilot Chat with a /transcript reference and ask Copilot to produce a .docx). Note: Teams Recap has no Export to Word button \\u2014 the workflow is Copilot pane > copy/paste OR M365 Copilot Chat. Requires M365 Copilot license + Teams Premium for full Recap features.'"

old_teams = r"""DESC_TEAMS = 'For this demo we DO NOT type Teams Copilot prompts directly \u2014 instead use the Teams Recap on the demo tenant for one of three meetings: \"New Software Implementation\", \"Potential Merger\", or \"Negotiating Marketing Contract\". Workflow: Open meeting in Teams > Recap tab > review AI summary + chapters > click Export > Open in Word > use Copilot in Word \"Edit with Copilot\" to format into the Group meeting-minutes template. Requires M365 Copilot license.'"""

s2 = s.replace(old_teams, new_teams, 1)
print('changed' if s != s2 else 'NO CHANGE')

with open('util.py','w',encoding='utf-8') as f: f.write(s2)
