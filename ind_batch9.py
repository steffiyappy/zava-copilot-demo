import sys; sys.path.insert(0,'.')
from batch_prompt_factory import build_entry

ENTRY_CONFIGS = [{'accent': '#283593',
'agent_name': 'Amanah Modal Portfolio Intelligence Agent',
'agent_share': 'the CEO office, investment committee members, and governance leads',
'board_body': 'Board Investment Committee',
'builder_crisis': 'A Ministerial aide calls 40 minutes before a press briefing to ask why dividend receipts are down '
'while one strategic holding has missed its mandate-compliance thresholds for two consecutive '
'quarters.',
'challenge': 'the mandate refresh, the three holdings below hurdle rate, and the tension between commercial return '
'and national-development objectives',
'color': '#1A237E',
'company': 'Amanah Modal Nasional Berhad',
'companyID': 'PT Investasi Negara Nusantara',
'deadline': 'six weeks',
'demo_question': 'Which three holdings are Red today, what evidence from the portfolio tabs supports that view, and '
'what action should the Board approve first?',
'external_party': 'the Ministry of Finance and investee company chairs',
'files': ['GLC_01_Investment_Portfolio.xlsx',
'GLC_02_Investment_Policy_Statement.docx',
'GLC_03_Governance_Charter.docx'],
'icon': '��',
'id': 'glc-investment',
'name': 'GLC Investment Arm',
'peer_set': 'Khazanah, Temasek, GIC, KWAP, and comparable sovereign-style investors',
'regulators': 'the Ministry of Finance, Bursa Malaysia disclosure expectations, and government-linked company '
'governance norms',
'roles': ['Chief Investment Officer', 'Head of Portfolio Strategy', 'Head of Governance & Stewardship'],
'scenario': 'Amanah Modal Nasional Berhad is a Malaysian state-linked investment arm managing MYR 52.4B across '
'listed and strategic national assets. The Board wants a refreshed mandate that balances commercial '
'returns, nation-building outcomes, and ESG expectations before the next Ministerial review. Three '
'legacy holdings are dragging NAV, dividend flow is under pressure, and the investment team must show a '
'sharper stewardship model within six weeks.',
'sectorId': 'glc',
'sheets': ['Portfolio Summary', 'NAV Tracker', 'Dividend Income', 'Mandate Compliance', 'ESG Scorecard'],
'short_name': 'Amanah Modal',
'stakeholders': 'the Board Chair, the Ministerial review team, and the Chief Risk Officer',
'tagline': 'MYR 52.4B portfolio mandate refresh, dividend pressure, and three strategic holdings below hurdle rate.',
'taglineID': 'Mandat portofolio BUMN dengan pengawasan OJK, tekanan dividen, dan tiga aset strategis di bawah hurdle '
'rate.',
'team': 'the investment, stewardship, and portfolio strategy teams',
'topics': ['portfolio performance',
'mandate compliance',
'dividend strategy',
'active ownership',
'ESG stewardship']},
{'accent': '#2E7D32',
'agent_name': 'Supervisory Intelligence Agent',
'agent_share': 'senior supervision leaders and policy heads',
'board_body': 'Board of Commissioners',
'builder_crisis': 'A licensed institution reports a sudden spike in delinquency plus a critical control failure at '
'6:30am, and leadership wants to know the immediate supervisory response before markets open.',
'challenge': 'the elevated personal-loan NPL trend, delayed digital-bank readiness, and the need to justify '
'proportionate supervisory escalation',
'color': '#1B5E20',
'company': 'Suruhanjaya Kewangan Malaysia',
'companyID': 'Otoritas Jasa Keuangan Nusantara',
'deadline': 'three weeks',
'demo_question': 'Which entities are Red across credit quality, conduct, and operational readiness, and what '
'proportionate intervention should we trigger first?',
'external_party': 'regulated institutions and the Deputy Governor',
'files': ['REG_01_Supervisory_Dashboard.xlsx',
'REG_02_Supervisory_Framework.docx',
'REG_03_Regulatory_Policy_Manual.docx'],
'icon': '⚖️',
'id': 'financial-regulator',
'name': 'Financial Regulator',
'peer_set': 'MAS, BSP, OJK, BIS, IMF, and comparable prudential authorities',
'regulators': 'IFSA-style prudential expectations, digital-bank operating conditions, and systemic-risk governance '
'norms',
'roles': ['Director of Banking Supervision', 'Head of Prudential Analytics', 'Head of Supervisory Policy'],
'scenario': 'Suruhanjaya Kewangan Malaysia is preparing a Board-level systemic-risk review while supervisory teams '
'track rising weakness in consumer credit. The personal-loan segment has moved above its internal risk '
'trigger, two digital-license holders are behind critical operational milestones, and market conduct '
'concerns are surfacing across several entities. Supervisors need a tighter evidence base, clearer '
'escalation logic, and a defensible narrative on proportional intervention within three weeks.',
'sectorId': 'government',
'sheets': ['Entity Compliance Matrix',
'Enforcement Action Log',
'Risk Rating Summary',
'Market Conduct Report',
'Financial Stability KPIs'],
'short_name': 'Supervisory',
'stakeholders': 'the Governor, Deputy Governors, and supervision heads',
'tagline': 'Personal-loan NPL deterioration, digital-bank readiness gaps, and a systemic-risk review due in three '
'weeks.',
'taglineID': 'Pengawasan OJK dan BI atas NPL konsumer, kesiapan bank digital, dan laporan stabilitas sistem keuangan '
'kepada dewan komisioner.',
'team': 'the prudential supervision, analytics, and policy teams',
'topics': ['NPL supervision', 'digital bank review', 'enforcement actions', 'market conduct', 'systemic risk']}]

INDUSTRIES_9 = [build_entry(cfg) for cfg in ENTRY_CONFIGS]

print(f"Batch 9 written: {len(INDUSTRIES_9)} entries")
