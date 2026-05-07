import sys; sys.path.insert(0,'.')
from batch_prompt_factory import build_entry

ENTRY_CONFIGS_1 = [{'accent': '#1976D2',
'agent_name': 'Seri Angkasa HR Intelligence Agent',
'agent_share': 'HR leaders, division HRBPs, and talent acquisition managers',
'board_body': 'People & Remuneration Committee',
'builder_crisis': 'The CEO learns that two priority business units may miss revenue targets because critical roles '
'remain unfilled and wants an immediate recovery plan before tomorrow morning.',
'challenge': 'the 24% Q3 attrition rate, the onboarding backlog of 180 hires, and the need to rebuild bench strength '
'without losing policy control',
'color': '#1565C0',
'company': 'Seri Angkasa Holdings Berhad — People & Culture Division',
'companyID': 'PT Seri Angkasa Nusantara — Divisi SDM',
'deadline': '45 days',
'demo_question': 'Which employee segment is Red on attrition risk, what evidence supports that view, and which '
'intervention should we activate first?',
'external_party': 'division managing directors and key hiring managers',
'files': ['HR_01_Workforce_Analytics.xlsx', 'HR_02_People_Policy_Manual.docx', 'HR_03_Talent_Strategy.docx'],
'icon': '👥',
'id': 'dept-hr',
'name': 'Human Resources',
'peer_set': 'Malaysian GLC talent teams, regional shared-services employers, and high-volume hiring operations',
'regulators': 'Malaysian employment practice, EPF or KWSP, SOCSO or PERKESO, and cross-border workforce policy '
'expectations',
'roles': ['Chief Human Resources Officer', 'Head of Talent Management', 'Head of HR Operations'],
'scenario': 'The People & Culture Division is trying to stabilise attrition, clear an onboarding backlog, and '
'improve leadership bench strength before the next operating review. Business leaders want faster '
'hiring, better retention, and a more defensible talent pipeline without breaking policy discipline. The '
'CHRO also needs a sharper cross-country view covering Malaysia and Indonesia workforce obligations.',
'sectorId': 'department',
'sheets': ['Headcount Dashboard',
'Attrition Tracker',
'Talent Pipeline',
'Compensation Benchmark',
'Onboarding Backlog'],
'short_name': 'HR',
'stakeholders': 'the CEO, CFO, and business-unit HR leads',
'tagline': 'Attrition reached 24% in Q3, headcount is 3,200, and onboarding backlog has risen to 180 hires.',
'taglineID': 'Agenda SDM Indonesia harus mematuhi BPJS Ketenagakerjaan, BPJS Kesehatan, dan kewajiban '
'ketenagakerjaan lintas entitas.',
'team': 'the HR business partner, talent, and shared-services teams',
'topics': ['attrition', 'talent pipeline', 'compensation', 'onboarding', 'HR policy guidance']},
{'accent': '#2E7D32',
'agent_name': 'Seri Angkasa Finance Control Agent',
'agent_share': 'finance leadership, controllers, and treasury managers',
'board_body': 'Audit Committee',
'builder_crisis': 'The CFO is told at 7:00am that a supplier hold has started because overdue invoices are rising, '
'and wants the likely liquidity impact plus the immediate response options before the executive '
'call.',
'challenge': 'the three-day delay in month-end close, the -22% opex variance, and the demand for a 15% cost reset '
'without weakening control quality',
'color': '#1B5E20',
'company': 'Seri Angkasa Holdings Berhad — Group Finance Division',
'companyID': 'PT Seri Angkasa Nusantara — Divisi Keuangan',
'deadline': '30 days',
'demo_question': 'Which cost buckets are Red, what does the cash-flow evidence show, and which corrective action '
'gives the fastest control-compliant improvement?',
'external_party': 'the CEO, business-unit CFOs, and key banking partners',
'files': ['FIN_01_Budget_Performance.xlsx', 'FIN_02_Treasury_Policy.docx', 'FIN_03_Month_End_Close_Playbook.docx'],
'icon': '💰',
'id': 'dept-finance',
'name': 'Finance & Treasury',
'peer_set': 'Malaysian listed-company finance teams, treasury best practice, and regional shared-services finance '
'operations',
'regulators': 'LHDN expectations, Bursa-style reporting discipline, and bank covenant communication norms',
'roles': ['Chief Financial Officer', 'Group Controller', 'Head of Treasury'],
'scenario': 'Group Finance is under pressure to accelerate month-end close, defend liquidity, and cut operating '
'expenditure without damaging control quality. Budget owners are challenging the reset targets, accrual '
'accuracy is inconsistent, and ageing payables are starting to affect supplier confidence. Leadership '
'needs a data-backed story grounded in Malaysian tax and reporting discipline, with Indonesian '
'implications clearly understood.',
'sectorId': 'department',
'sheets': ['Budget vs Actual', 'Cashflow Forecast', 'GL Summary', 'Accruals Register', 'AP Ageing'],
'short_name': 'Finance',
'stakeholders': 'the CEO, Audit Committee Chair, and division finance leads',
'tagline': 'Month-end close is three days late, opex variance is -22%, and the CFO wants a 15% cost reset.',
'taglineID': 'Keuangan Indonesia harus selaras dengan OJK, BI, dan Dirjen Pajak sambil menjaga likuiditas dan '
'disiplin penutupan buku.',
'team': 'the controllership, treasury, and finance shared-services teams',
'topics': ['budget variance', 'cash flow', 'month-end close', 'accrual control', 'payables management']}]

DEPARTMENTS_1 = [build_entry(cfg) for cfg in ENTRY_CONFIGS_1]

print(f"Departments 1 written: {len(DEPARTMENTS_1)} entries")
