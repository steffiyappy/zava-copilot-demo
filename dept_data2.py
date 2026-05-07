import sys; sys.path.insert(0,'.')
from batch_prompt_factory import build_entry

ENTRY_CONFIGS = [{'accent': '#6A1B9A',
'agent_name': 'Seri Angkasa Legal Intelligence Agent',
'agent_share': 'legal leaders, company secretariat staff, and compliance managers',
'board_body': 'Board Governance Committee',
'builder_crisis': 'A regulator asks for additional documents with a 48-hour deadline while the Board secretariat is '
'still waiting for two critical approvals on a major transaction.',
'challenge': 'the backlog of 340 contracts, the live regulatory inquiry, and the strain this is placing on board '
'approval timelines',
'color': '#4A148C',
'company': 'Seri Angkasa Holdings Berhad — Group Legal Division',
'companyID': 'PT Seri Angkasa Nusantara — Divisi Legal',
'deadline': '21 days',
'demo_question': 'Which matters are Red, what is the exact approval bottleneck, and which item must the General '
'Counsel personally escalate today?',
'external_party': 'external counsel, regulators, and business sponsors',
'files': ['LEG_01_Legal_Matter_Register.xlsx',
'LEG_02_Compliance_Manual.docx',
'LEG_03_Delegation_of_Authority.docx'],
'icon': '⚖️',
'id': 'dept-legal',
'name': 'Legal & Corporate Secretarial',
'peer_set': 'regional listed-company legal teams, corporate secretariat functions, and regulatory-response playbooks',
'regulators': 'BNM-style inquiry handling, Bursa governance discipline, and disclosure best practice',
'roles': ['Group General Counsel', 'Head of Corporate Secretarial', 'Head of Regulatory Affairs'],
'scenario': 'Group Legal is struggling with a growing contract queue while regulatory correspondence and '
'board-secretariat work compete for the same specialist capacity. Leadership wants faster turnaround '
'without sacrificing clause control, disclosure quality, or approval discipline. The legal team must '
'also show how Malaysian and Indonesian obligations are being triaged consistently.',
'sectorId': 'department',
'sheets': ['Contract Backlog',
'Regulatory Inquiry Log',
'Litigation Tracker',
'Board Resolution Calendar',
'Policy Exceptions'],
'short_name': 'Legal',
'stakeholders': 'the CEO, Company Secretary, and division legal heads',
'tagline': 'Contract approval backlog stands at 340 agreements, a BNM inquiry is live, and board approvals are '
'slipping.',
'taglineID': 'Respons kontrak dan regulator Indonesia harus selaras dengan OJK, BI, dan tata kelola korporasi lintas '
'entitas.',
'team': 'the legal advisory, company secretarial, and regulatory response teams',
'topics': ['contract backlog',
'regulatory inquiry',
'board approvals',
'delegation of authority',
'policy exceptions']},
{'accent': '#C62828',
'agent_name': 'Seri Angkasa Risk Intelligence Agent',
'agent_share': 'risk leaders, internal audit managers, and control owners',
'board_body': 'Board Risk Committee',
'builder_crisis': 'An overnight incident lands on top of several overdue High findings, and the CRO must decide '
'before 8:00am whether immediate Board notification is warranted.',
'challenge': 'the 47 open audit findings, the 12 High-rated items, and the need to show a cleaner enterprise-risk '
'picture before committee review',
'color': '#B71C1C',
'company': 'Seri Angkasa Holdings Berhad — Group Risk & Internal Audit',
'companyID': 'PT Seri Angkasa Nusantara — Divisi Risiko dan Audit Internal',
'deadline': 'two weeks',
'demo_question': 'Which findings are truly Red today, what does the evidence say about residual exposure, and who '
'must close them before committee review?',
'external_party': 'the Audit Committee Chair and external auditors',
'files': ['RSK_01_Enterprise_Risk_Register.xlsx', 'RSK_02_ERM_Framework.docx', 'RSK_03_Internal_Audit_Plan.docx'],
'icon': '🛡',
'id': 'dept-risk',
'name': 'Risk & Internal Audit',
'peer_set': 'Malaysian listed-company risk functions, three-lines-of-defence benchmarks, and internal-audit '
'remediation playbooks',
'regulators': 'risk governance expectations, audit follow-up discipline, and committee reporting norms',
'roles': ['Chief Risk Officer', 'Head of Internal Audit', 'Head of Enterprise Risk'],
'scenario': 'Risk & Internal Audit needs to reduce overdue findings, tighten issue ownership, and refresh the '
'enterprise risk story before a special committee review. Three incidents in Q3 have already tested '
'management confidence, and the audit backlog is beginning to obscure which risks truly matter most. The '
'CRO needs a cleaner RAG narrative and stronger escalation logic fast.',
'sectorId': 'department',
'sheets': ['Risk Heatmap', 'Incident Log', 'Control Testing', 'Risk Appetite Metrics', 'Audit Findings'],
'short_name': 'Risk',
'stakeholders': 'the CEO, Board Risk Committee Chair, and division risk owners',
'tagline': 'There are 47 outstanding audit findings, 12 rated High, and an enterprise-risk review is due in two '
'weeks.',
'taglineID': 'Temuan audit dan pengawasan risiko Indonesia harus siap diuji terhadap ekspektasi OJK serta komite '
'risiko grup.',
'team': 'the enterprise risk, controls, and internal audit teams',
'topics': ['risk incidents', 'audit findings', 'risk appetite', 'control testing', 'committee reporting']},
{'accent': '#F57C00',
'agent_name': 'Seri Angkasa Strategy Navigator',
'agent_share': 'strategy leaders, PMO owners, and executive committee members',
'board_body': 'Strategy Committee',
'builder_crisis': 'The CEO asks one hour before the strategy workshop which initiative should be paused immediately '
'if funding remains constrained for the next two quarters.',
'challenge': 'the delayed strategic initiatives, the need to reprioritise capex, and the requirement to refresh the '
'FY2026 growth thesis',
'color': '#E65100',
'company': 'Seri Angkasa Holdings Berhad — Group Strategy Division',
'companyID': 'PT Seri Angkasa Nusantara — Divisi Strategi Korporat',
'deadline': 'four weeks',
'demo_question': 'Which initiatives are Red, what is the quantified value at risk, and which capex moves should '
'leadership defer, accelerate, or stop?',
'external_party': 'the CEO, investment committee, and business-unit heads',
'files': ['STR_01_Strategy_Tracker.xlsx', 'STR_02_Corporate_Plan.docx', 'STR_03_Portfolio_Review.docx'],
'icon': '🎯',
'id': 'dept-strategy',
'name': 'Strategy & Corporate Planning',
'peer_set': 'ASEAN corporate planning functions, portfolio-review frameworks, and capital-allocation best practice',
'regulators': 'market-disclosure expectations for strategy statements and capital allocation governance norms',
'roles': ['Chief Strategy Officer', 'Head of Corporate Planning', 'Head of Portfolio Strategy'],
'scenario': 'Corporate Planning is updating the medium-term plan while several flagship initiatives are drifting and '
'capital allocation assumptions are being challenged. The CEO wants a sharper growth thesis, tighter '
'sequencing, and better linkage between strategy milestones and value creation. Strategy also has to '
'explain what moves first if resources stay constrained.',
'sectorId': 'department',
'sheets': ['Strategic Initiatives', 'KPI Tree', 'Capital Allocation', 'Scenario Modelling', 'PMO Dashboard'],
'short_name': 'Strategy',
'stakeholders': 'the CEO, CFO, and strategy committee members',
'tagline': 'Three strategic initiatives are behind schedule, capex reprioritisation is required, and FY2026 growth '
'assumptions need refreshing.',
'taglineID': 'Strategi Indonesia harus mempertimbangkan OJK, BI, dan dinamika pasar lokal saat menilai portofolio '
'dan alokasi modal.',
'team': 'the strategy, PMO, and corporate development teams',
'topics': ['strategic initiatives', 'capital allocation', 'scenario planning', 'portfolio review', 'PMO tracking']}]

DEPARTMENTS_2 = [build_entry(cfg) for cfg in ENTRY_CONFIGS]

print(f"Departments 2 written: {len(DEPARTMENTS_2)} entries")
