import sys; sys.path.insert(0,'.')
from batch_prompt_factory import build_entry

ENTRY_CONFIGS = [{'accent': '#455A64',
'agent_name': 'Seri Angkasa Operations Intelligence Agent',
'agent_share': 'operations leaders, plant managers, and continuity owners',
'board_body': 'Operations Review Committee',
'builder_crisis': 'A critical supplier signals a possible shutdown overnight and the COO wants to know the likely '
'service impact plus the first recovery move before dawn.',
'challenge': 'the site-level service slippage, the delayed cost-takeout plan, and the supplier disruption '
'threatening continuity',
'color': '#37474F',
'company': 'Seri Angkasa Holdings Berhad — COO Office',
'companyID': 'PT Seri Angkasa Nusantara — Kantor COO',
'deadline': '14 days',
'demo_question': 'Which site or supplier issue is Red, what evidence shows the impact, and which intervention should '
'the COO authorise first?',
'external_party': 'site leaders, major suppliers, and the CEO',
'files': ['OPS_01_Operational_Performance.xlsx',
'OPS_02_Operations_Playbook.docx',
'OPS_03_Business_Continuity_Manual.docx'],
'icon': '⚙️',
'id': 'dept-operations',
'name': 'Operations & COO Office',
'peer_set': 'ASEAN operations excellence programmes, supply-risk recovery benchmarks, and continuity-management best '
'practice',
'regulators': 'Malaysian workplace safety expectations and continuity-governance norms',
'roles': ['Chief Operating Officer', 'Head of Operational Excellence', 'Head of Supply & Continuity'],
'scenario': 'The COO Office is trying to restore execution discipline across multiple sites while costs stay above '
'target and a supplier issue threatens continuity. Site leaders disagree on which bottlenecks matter '
'most, and leadership wants a single RAG tracker that ties service, cost, and continuity together. The '
'next monthly review needs a sharper line of sight from root cause to action owner.',
'sectorId': 'department',
'sheets': ['Plant OEE', 'Supply Risk', 'Service Levels', 'Cost Takeout', 'Capex Tracker'],
'short_name': 'Operations',
'stakeholders': 'the CEO, CFO, and operations committee members',
'tagline': 'Service levels slipped at two sites, cost takeout is behind plan, and a supplier disruption is '
'threatening production continuity.',
'taglineID': 'Operasi Indonesia memerlukan disiplin pemulihan pemasok, keselamatan kerja, dan kesinambungan layanan '
'lintas lokasi.',
'team': 'the operations, supply chain, and business continuity teams',
'topics': ['service levels', 'supply risk', 'cost takeout', 'operational continuity', 'capex tracking']},
{'accent': '#283593',
'agent_name': 'Seri Angkasa Board Intelligence Agent',
'agent_share': 'the Chairman, directors, and board secretariat staff',
'board_body': 'Board of Directors',
'builder_crisis': 'A late-night query from an investor coincides with a new disclosure-watchlist item, and '
'leadership needs to know before market open whether the Board should be convened or simply '
'briefed.',
'challenge': 'the late board papers, the growing disclosure watchlist, and the need for better resolution tracking '
'before quarter-end',
'color': '#1A237E',
'company': 'Seri Angkasa Holdings Berhad — Board & Executive Office',
'companyID': 'PT Seri Angkasa Nusantara — Kantor Direksi dan Dewan',
'deadline': 'two weeks',
'demo_question': 'Which governance item is Red today, what evidence supports that, and what decision must the '
'Chairman or Company Secretary drive immediately?',
'external_party': 'the Chairman, directors, and investor-relations leadership',
'files': ['BRD_01_Board_Pack_Tracker.xlsx', 'BRD_02_Governance_Manual.docx', 'BRD_03_Board_Paper_Standards.docx'],
'icon': '🏛',
'id': 'dept-board',
'name': 'Board & Executive Office',
'peer_set': 'Bursa-listed board offices, governance secretariats, and executive-office operating models',
'regulators': 'MCCG-style governance practice, Bursa disclosure discipline, and IDX or OJK cross-listing '
'expectations',
'roles': ['Company Secretary', 'Chief of Staff', 'Head of Governance'],
'scenario': 'The Board & Executive Office is trying to improve paper quality, decision tracking, and governance '
'visibility before the quarter-end meeting cycle. Directors are frustrated that materials arrive late '
'and resolutions are not always easy to trace back to owners and deadlines. The Company Secretary needs '
'a more disciplined operating rhythm with a clear RAG view of disclosure and governance risks.',
'sectorId': 'department',
'sheets': ['Board Calendar', 'Resolution Log', 'Investor Issues', 'Governance Actions', 'Disclosure Watchlist'],
'short_name': 'Board',
'stakeholders': 'the Chairman, CEO, and board secretariat team',
'tagline': 'Board papers are late, disclosure-watchlist items are growing, and directors want clearer resolution '
'tracking before quarter-end.',
'taglineID': 'Agenda dewan Indonesia harus sinkron dengan IDX, OJK, dan tata kelola pengungkapan lintas entitas '
'regional.',
'team': 'the board secretariat, CEO office, and governance coordination teams',
'topics': ['board calendar', 'resolution tracking', 'investor issues', 'governance actions', 'disclosure watchlist']}]

DEPARTMENTS_4 = [build_entry(cfg) for cfg in ENTRY_CONFIGS]

print(f"Departments 4 written: {len(DEPARTMENTS_4)} entries")
