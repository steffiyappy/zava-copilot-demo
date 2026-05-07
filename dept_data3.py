import sys; sys.path.insert(0,'.')
from batch_prompt_factory import build_entry

ENTRY_CONFIGS = [{'accent': '#C2185B',
'agent_name': 'Seri Angkasa Communications Intelligence Agent',
'agent_share': 'marketing leaders, communications heads, and campaign managers',
'board_body': 'Executive Communications Review',
'builder_crisis': 'A journalist calls during launch week with questions about a negative trend that is already '
'visible in social sentiment and leadership wants a response recommendation immediately.',
'challenge': 'the drop in campaign ROI, the mixed brand sentiment, and the need to recover qualified leads without '
'creating message risk',
'color': '#AD1457',
'company': 'Seri Angkasa Holdings Berhad — Brand, Marketing & Communications',
'companyID': 'PT Seri Angkasa Nusantara — Divisi Pemasaran dan Komunikasi',
'deadline': 'three weeks',
'demo_question': 'Which campaigns are Red on ROI and sentiment, what evidence supports that, and which message '
'should we change first?',
'external_party': 'the CEO, sales leadership, and key media contacts',
'files': ['MKT_01_Campaign_Performance.xlsx', 'MKT_02_Brand_Guidelines.docx', 'MKT_03_Communications_Playbook.docx'],
'icon': '📢',
'id': 'dept-marketing',
'name': 'Marketing & Communications',
'peer_set': 'ASEAN brand teams, investor-day communications practice, and campaign-optimisation benchmarks',
'regulators': 'advertising standards, disclosure discipline, and reputation-management best practice',
'roles': ['Chief Marketing Officer', 'Head of Brand Strategy', 'Head of Corporate Communications'],
'scenario': 'Marketing and Communications is balancing performance pressure with reputation management ahead of a '
'high-visibility campaign window. Qualified lead conversion has softened, sentiment is uneven across '
'channels, and leadership wants clearer evidence on what content is working. The team must sharpen its '
'RAG view of message risk, campaign effectiveness, and launch readiness.',
'sectorId': 'department',
'sheets': ['Campaign ROI', 'Brand Tracker', 'Media Sentiment', 'Lead Funnel', 'Content Calendar'],
'short_name': 'Marketing',
'stakeholders': 'the CEO, commercial heads, and communications leads',
'tagline': 'Campaign ROI is slipping, brand sentiment is mixed, and the next launch must recover qualified leads '
'without creating disclosure risk.',
'taglineID': 'Komunikasi pasar Indonesia harus mempertimbangkan aturan OJK untuk produk keuangan dan disiplin pesan '
'lintas kanal digital.',
'team': 'the marketing, brand, and communications teams',
'topics': ['campaign ROI', 'brand sentiment', 'lead funnel', 'media handling', 'content planning']},
{'accent': '#00838F',
'agent_name': 'Seri Angkasa Digital Control Agent',
'agent_share': 'IT leaders, programme managers, and cyber incident owners',
'board_body': 'Technology Steering Committee',
'builder_crisis': 'At 10:00pm the CIO learns that recovery timelines may slip again after a fresh cyber alert, and '
'needs a single answer on impact, readiness, and first actions within minutes.',
'challenge': 'the ERP programme delay, the multi-business-unit cyber incident, and the inconsistent Copilot adoption '
'story',
'color': '#006064',
'company': 'Seri Angkasa Holdings Berhad — Group IT & Digital',
'companyID': 'PT Seri Angkasa Nusantara — Divisi TI dan Digital',
'deadline': '30 days',
'demo_question': 'Which programme or incident is Red today, what is the operational evidence, and what action should '
'the CIO approve before the next steering call?',
'external_party': 'the CEO, business-unit CIOs, and critical technology vendors',
'files': ['IT_01_Transformation_Tracker.xlsx',
'IT_02_IT_Governance_Manual.docx',
'IT_03_Cyber_Response_Playbook.docx'],
'icon': '💻',
'id': 'dept-it-digital',
'name': 'IT & Digital',
'peer_set': 'large-enterprise ERP recovery programmes, cyber-response benchmarks, and Copilot adoption best practice',
'regulators': 'PDPA discipline, cyber incident reporting norms, and financial-sector technology-risk expectations',
'roles': ['Chief Information Officer', 'Head of Enterprise Architecture', 'Head of Cybersecurity'],
'scenario': 'IT & Digital is trying to recover a delayed transformation programme while also proving cyber '
'resilience and adoption value. Legacy architecture is slowing the ERP transition, three business units '
'were disrupted by a recent incident, and executives want clearer evidence that Copilot usage is moving '
'beyond experimentation. The CIO needs one integrated RAG view of programme risk, cyber exposure, and '
'adoption impact.',
'sectorId': 'department',
'sheets': ['ERP Migration Plan',
'Cyber Incident Log',
'Service Desk SLA',
'Application Inventory',
'Copilot Adoption'],
'short_name': 'IT',
'stakeholders': 'the CEO, CFO, and technology steering members',
'tagline': 'ERP migration is six months late, a cyber incident hit three business units, and Copilot adoption is '
'uneven.',
'taglineID': 'Ketahanan siber dan modernisasi digital Indonesia harus memenuhi ekspektasi OJK, BI, dan kewajiban '
'pelaporan insiden.',
'team': 'the architecture, cyber, digital workplace, and programme delivery teams',
'topics': ['ERP migration', 'cyber incidents', 'service levels', 'application rationalisation', 'Copilot adoption']},
{'accent': '#2E7D32',
'agent_name': 'Seri Angkasa ESG Intelligence Agent',
'agent_share': 'ESG leaders, reporting managers, and supply-chain sustainability owners',
'board_body': 'Board Sustainability Committee',
'builder_crisis': 'A major customer asks for immediate proof that our supply-chain controls and climate roadmap are '
'credible before renewing a strategic contract.',
'challenge': 'the emissions trajectory above glidepath, the supplier due-diligence gaps, and the need to be '
'assurance-ready for the Board',
'color': '#1B5E20',
'company': 'Seri Angkasa Holdings Berhad — Group ESG Office',
'companyID': 'PT Seri Angkasa Nusantara — Divisi ESG dan Keberlanjutan',
'deadline': 'five weeks',
'demo_question': 'Which ESG area is Red, what evidence supports that, and what action moves us fastest toward '
'assurance-ready status?',
'external_party': 'the Board Sustainability Committee and priority customers',
'files': ['ESG_01_Sustainability_Dashboard.xlsx',
'ESG_02_Sustainability_Framework.docx',
'ESG_03_Climate_Action_Roadmap.docx'],
'icon': '🌱',
'id': 'dept-esg',
'name': 'ESG & Sustainability',
'peer_set': 'Bursa-style sustainability reporting leaders, ASEAN climate-disclosure practice, and '
'supplier-due-diligence programmes',
'regulators': 'Bursa sustainability expectations, climate-reporting norms, and supply-chain due-diligence frameworks',
'roles': ['Chief Sustainability Officer', 'Head of Sustainability Reporting', 'Head of Climate & Supply Chain'],
'scenario': 'The ESG Office is preparing for a tougher reporting and assurance cycle while several operational '
'indicators are moving in the wrong direction. Emissions intensity is above plan, supplier reviews are '
'inconsistent, and leadership wants a clearer narrative on what is genuinely on track versus at risk. '
'The CSO needs a sharper cross-functional story that can stand up to Board scrutiny.',
'sectorId': 'department',
'sheets': ['Emissions Tracker',
'Compliance Obligations',
'Supplier Due Diligence',
'Community Projects',
'Assurance Log'],
'short_name': 'ESG',
'stakeholders': 'the CEO, Board Sustainability Chair, and operating-unit ESG leads',
'tagline': 'Scope 1 emissions are above glidepath, supplier due diligence gaps are visible, and sustainability '
'assurance must be board-ready.',
'taglineID': 'Pelaporan keberlanjutan Indonesia harus selaras dengan OJK serta pengendalian uji tuntas pemasok dan '
'iklim.',
'team': 'the sustainability reporting, climate, and supply-chain ESG teams',
'topics': ['emissions',
'compliance obligations',
'supplier due diligence',
'community impact',
'assurance readiness']}]

DEPARTMENTS_3 = [build_entry(cfg) for cfg in ENTRY_CONFIGS]

print(f"Departments 3 written: {len(DEPARTMENTS_3)} entries")
