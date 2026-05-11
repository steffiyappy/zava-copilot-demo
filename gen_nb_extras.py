"""Generate the 9 Notebook Library reference files still missing after notebook-files
promotion. Run from repo root: `python _gen_nb_extras.py`.

Files produced (all in files/):
  Audit_Assurance_Findings.docx       - compliance_register
  Auditor_Open_Queries.docx           - compliance_register
  Benefits_Guide.pdf                  - new_hire_onboarding
  Buddy_Programme_Notes.docx          - new_hire_onboarding
  Prior_Year_Disclosure.pdf           - esg_reporting
  Role_Specific_Onboarding_Plan.docx  - new_hire_onboarding
  Root_Cause_Investigations.docx      - incident_postmortem
  Sustainability_Strategy.docx        - esg_reporting
  Transfer_Pricing_Documentation.pdf  - treasury_tax
"""
from pathlib import Path
import random
random.seed(99)

# Reuse primitives from gen_cowork_files.py
import importlib.util
spec = importlib.util.spec_from_file_location('_g', str(Path(__file__).parent / 'gen_cowork_files.py'))
g = importlib.util.module_from_spec(spec)
# avoid running the __main__ block
import sys as _sys
_prev_argv = _sys.argv
_sys.argv = ['_g']
spec.loader.exec_module(g)
_sys.argv = _prev_argv
_docx = g._docx
_pdf = g._pdf

OUT = Path(__file__).parent / 'files'
OUT.mkdir(exist_ok=True)


def b_audit_assurance_findings():
    _docx(OUT / 'Audit_Assurance_Findings.docx',
          'Internal Audit & Assurance — Findings Report (FY2025 cycle)', [
        ('p', 'Issued by: Group Internal Audit | Approver: Hadar Caspit (Group CFO, Risk Committee Chair) | Date: 15 May 2026 | Distribution: Audit Committee, Group ExCo, BNM auditor liaison.'),
        ('h1', '1. Executive summary'),
        ('p', 'Of the 36 audit engagements completed in the FY2025 cycle, 4 produced High-severity findings, 9 Medium, 18 Low, and 5 closed with no finding. The cumulative risk-weighted exposure for the 13 open High+Medium issues is estimated at MYR 28.4M revenue-at-risk plus MYR 9.6M one-off remediation cost. 22 of 31 findings from prior cycles have been verified closed; 9 remain past target close date and have been escalated to ExCo.'),
        ('h1', '2. High-severity findings (4 open)'),
        ('table', [
            ['Ref', 'Area', 'Finding', 'Owner', 'Target close'],
            ['HF-01', 'Banking — Credit risk', 'BNM PD/LGD model recalibration overdue 9 months; FY2024 backtest deviation > 3 stdev on 4 sub-portfolios.', 'Head of Risk', '2026-08-31'],
            ['HF-02', 'Treasury', 'Bank account reconciliation backlog at 38 of 142 accounts > 30 days. Suspected duplicate FX swap entries (MYR 14.2M nominal) unresolved.', 'Group Treasurer', '2026-06-30'],
            ['HF-03', 'IT — Access', 'Privileged account review not completed for 11 of 28 production systems in 6 months. SOX 404 evidence gap.', 'CIO', '2026-07-15'],
            ['HF-04', 'Plantation — HSE', 'Lost-time injury under-reporting suspected at 2 mills based on independent re-count of incident log.', 'Head of HSE', '2026-09-30'],
        ]),
        ('h1', '3. Medium-severity findings (9 open)'),
        ('bullets', [
            'MF-01 Procurement — 14 contracts > MYR 5M renewed without DOA approval (CFO discretionary band breached).',
            'MF-02 Payroll — manual journal lines > MYR 50k posted by single preparer at month-end (segregation of duties).',
            'MF-03 Property — REIT valuer rotation not enforced; same firm 6 consecutive years on 4 assets.',
            'MF-04 Insurance — outstanding claim provisioning Bornhuetter-Ferguson model not validated independently in 18 months.',
            'MF-05 Healthcare — narcotics stock-take variance > 0.5% across 3 hospitals; controlled-drug register not signed off daily.',
            'MF-06 Telco — vendor SLA credits not reconciled to GL; estimated MYR 3.4M under-recovered.',
            'MF-07 ESG — Scope 3 data quality marked High variance in 8 of 14 categories.',
            'MF-08 Corporate secretarial — board pack distribution > 7 days late on 3 of 12 meetings (MMLR breach).',
            'MF-09 Tax — withholding tax positions on 5 cross-border related-party flows not re-evaluated under new ASEAN BEPS guidance.',
        ]),
        ('h1', '4. Closure tracking (prior cycles)'),
        ('table', [
            ['Status', 'Count', 'Risk-weighted exposure', 'Action'],
            ['Verified closed', '22', 'MYR 0', '—'],
            ['On track', '6', 'MYR 8.4M', 'Quarterly progress to AC'],
            ['Past target close — < 60 days overdue', '5', 'MYR 4.2M', 'ExCo escalation issued'],
            ['Past target close — > 60 days overdue', '4', 'MYR 11.8M', 'Risk-accept paper to AC for 2 items'],
        ]),
        ('h1', '5. Audit Committee resolutions requested'),
        ('numbered', [
            'Approve MYR 6.4M one-off remediation budget for HF-01 (model recalibration + independent validation).',
            'Note 9 medium findings; escalate any not closed by FY2026 Q2 to High severity automatically.',
            'Endorse risk-accept paper for 2 plantation HSE legacy items (residual MYR 2.8M).',
            'Approve refreshed audit universe and FY2026 audit plan (separate paper).',
        ]),
    ])


def b_auditor_open_queries():
    _docx(OUT / 'Auditor_Open_Queries.docx',
          'External Auditor — Open Queries (FY2025 audit)', [
        ('p', 'External auditor: Tier-1 firm | Partner: D. Tan | Manager: F. Lim | Open as of: 15 May 2026 | Group lead: Hadar Caspit (Group CFO).'),
        ('p', 'The auditor has 28 open queries outstanding for FY2025 sign-off (target: 15 Jun). Group Finance is requested to triage and respond within 5 working days unless flagged below.'),
        ('h1', '1. Revenue recognition (6 queries)'),
        ('table', [
            ['Ref', 'Topic', 'Auditor ask', 'Group response status'],
            ['Q-REV-01', 'Property — bundled handover', 'Provide POC schedule + variation order log for Bandar Zava Phase 2 to evidence 5-step model.', 'Drafting; due 18 May'],
            ['Q-REV-02', 'Construction', 'Substantiate the MYR 84.2M variation order claim included in revenue.', 'Pending — depends on counterparty position paper'],
            ['Q-REV-03', 'Telco — bundled handsets', 'Allocation of TCV to handset vs service obligation; provide SSP study.', 'Drafting'],
            ['Q-REV-04', 'Insurance — IFRS 17 CSM', 'Walk-through of CSM release for 3 cohorts; explain confidence-level methodology change.', 'Awaiting CRO sign-off'],
            ['Q-REV-05', 'Hospitality', 'Loyalty programme breakage rate change rationale (from 28% to 21%).', 'Drafting'],
            ['Q-REV-06', 'Logistics', 'Cut-off testing: 14 shipments at year-end straddle period.', 'Closed pending evidence pack'],
        ]),
        ('h1', '2. Impairment (5 queries)'),
        ('bullets', [
            'Q-IMP-01 — Plantation: WACC inputs for FFB price scenario; sensitivity ± 50 MYR/MT.',
            'Q-IMP-02 — Telco towers CGU: long-term growth rate justification (current 2.0% vs prior 2.5%).',
            'Q-IMP-03 — Goodwill on Apex Banking acquisition: refresh impairment test post-MFRS 9 cycle.',
            'Q-IMP-04 — Healthcare brand: indefinite-life intangible re-test with 3 new competitor entrants.',
            'Q-IMP-05 — Renewable energy: PPA-based DCF; provide hedged vs spot scenario split.',
        ]),
        ('h1', '3. Tax + transfer pricing (4 queries)'),
        ('bullets', [
            'Q-TAX-01 — TP master file: provide updated FAR analysis for 3 related-party flows.',
            'Q-TAX-02 — Indonesia branch: provide P3B treaty positions for 2 royalty flows (PT Zava Niaga).',
            'Q-TAX-03 — Deferred tax: walk MYR 412M opening to MYR 478M closing balance by component.',
            'Q-TAX-04 — Uncertain tax positions: FY2024 IRB query (MYR 38M) — provide latest correspondence and provisioning rationale.',
        ]),
        ('h1', '4. Going concern + liquidity (3 queries)'),
        ('bullets', [
            'Q-GC-01 — Provide 12-month rolling cash forecast (base + downside).',
            'Q-GC-02 — Covenant headroom analysis at 31 Mar; provide forward 4Q ratios with sensitivities.',
            'Q-GC-03 — Refinancing of USD 280M sukuk due Sep 2026 — provide signed MOU or term sheets.',
        ]),
        ('h1', '5. Other (10 queries)'),
        ('p', 'Includes: 2 related-party transactions (BoD member director-related), 2 share-based payment fair value re-measurements, 2 climate-related disclosure (TCFD), 1 contingent liability (LIT-2024-001), 2 going-concern non-financial events post balance sheet, 1 first-time IFRS S2 adoption.'),
        ('h1', '6. Triage plan'),
        ('p', 'Hadar Caspit, Group CFO, owns the response register. Daily 8:30am stand-up with audit team. Items not closed by 1 June will be escalated to the Audit Committee Chair and may delay sign-off.'),
    ])


def b_benefits_guide():
    _pdf(OUT / 'Benefits_Guide.pdf',
         'Zava Group — Employee Benefits Guide (FY2026)', [
        ('h1', 'Welcome to Zava'),
        ('p', 'This guide summarises the benefits available to permanent Zava Group employees in Malaysia and Indonesia. Specific local terms may vary by employing entity. Refer to your Employee Handbook for the full policy text and SOP.'),
        ('h1', '1. Medical & dental'),
        ('p', 'Group Hospitalisation & Surgical — RM 200,000 annual limit for employee, RM 150,000 for spouse, RM 100,000 per dependant child. Direct admission via panel hospital. Self-pay claim window: 90 days.'),
        ('p', 'Outpatient — RM 1,500 per family per year at panel clinics. RM 400 dental + RM 300 optical sub-limits.'),
        ('p', 'Maternity — full hospitalisation cover for normal + Caesarean delivery; ante- and post-natal RM 1,800 sub-limit.'),
        ('h1', '2. Leave entitlements'),
        ('table', [
            ['Type', 'Years 1-2', 'Years 3-5', 'Years 6+', 'Notes'],
            ['Annual leave', '16 days', '20 days', '24 days', 'Carry forward up to 5 days; balance forfeited 31 Dec.'],
            ['Medical leave', '14 days', '18 days', '22 days', 'Plus 60 days if hospitalised.'],
            ['Maternity', '98 days', '98 days', '98 days', 'Per Akta Kerja 2022.'],
            ['Paternity', '7 days', '7 days', '7 days', 'Within 60 days of birth.'],
            ['Compassionate', '3 days', '3 days', '3 days', 'Immediate family.'],
            ['Marriage', '3 days', '3 days', '3 days', 'Once during employment.'],
            ['Exam (study)', '3 days', '3 days', '3 days', 'Approved course.'],
        ]),
        ('h1', '3. Retirement + insurance'),
        ('bullets', [
            'EPF — employer 13% (basic salary <= RM 5,000) or 12% (above). Voluntary contribution programme available.',
            'Group Term Life — 36 months base salary (minimum RM 500k).',
            'Group Personal Accident — 36 months base salary; covers loss of limbs / TPD.',
            'Critical Illness — RM 150,000 lump-sum on 36 listed illnesses.',
            'Long-Term Service Award — at 10/15/20/25/30 years with cash gratuity + 1 week additional leave.',
        ]),
        ('h1', '4. Learning & development'),
        ('bullets', [
            'Tuition assistance — up to RM 12,000 / year for approved external courses.',
            'Professional membership — annual subscription paid for 1 body (CFA, ICAEW, MIA, Bar, etc.).',
            'LinkedIn Learning + Coursera Plus subscriptions provided to all employees.',
            'Internal mentor / coach matching available via HR Portal.',
        ]),
        ('h1', '5. Flexible work + family'),
        ('bullets', [
            'Hybrid working — minimum 2 days in office per week (role permitting).',
            'Flexi-hours — core hours 10am-3pm, balance flexible.',
            'Childcare subsidy — RM 350/month per child under 6 (panel centres).',
            'Eldercare leave — 5 days / year on top of compassionate leave.',
            'Sabbatical — eligible after 7 years; unpaid 3-6 months.',
        ]),
        ('h1', '6. Wellness + extras'),
        ('bullets', [
            'Annual health screening — full panel at panel clinic (employee + spouse).',
            'Gym + wellness subsidy — RM 1,200 / year reimbursable.',
            'Employee Assistance Programme — 24/7 confidential counselling, 6 sessions / year.',
            'Mobile + broadband subsidy for eligible job grades — refer Allowance Matrix.',
            'Employee discount programme — 200+ panel merchants in MY + ID.',
        ]),
        ('h1', '7. How to claim'),
        ('p', 'All claims are submitted via the HR Portal (https://hrportal.zavagroup.com). Medical and outpatient claims auto-route to panel; reimbursable claims pay within 14 working days. Questions: hrhelpdesk@zavagroup.com or extension 7100.'),
    ])


def b_buddy_programme_notes():
    _docx(OUT / 'Buddy_Programme_Notes.docx',
          'New Hire Buddy Programme — Notes for Buddies', [
        ('p', 'Programme owner: Group HR | Buddy coordinator: Catherine Wong | Version: FY2026 v3.1 | Last refreshed: April 2026.'),
        ('h1', '1. What is the buddy programme?'),
        ('p', 'Every new permanent hire at Zava Group is paired with a Buddy in their first 90 days. The Buddy is a peer — not the hiring manager — who helps the new hire navigate the unwritten rules: who to ask for what, how the coffee machine works, what time the canteen closes, which Teams channels matter, and how to read a Zava email distribution list.'),
        ('p', 'The Buddy commits to: a 30-min welcome chat in the first week, a 1:1 lunch in the first month, a check-in at day 45 and day 90, and being reachable for ad-hoc questions on Teams.'),
        ('h1', '2. Buddy commitments by week'),
        ('table', [
            ['When', 'Activity', 'Time', 'Output'],
            ['Day 1', 'Welcome message on Teams + intro post in team channel', '10 min', 'New hire feels welcomed'],
            ['Week 1', '30-min coffee or video call — walk them through the team, IT setup, key tools', '30 min', 'New hire knows who-does-what'],
            ['Week 2', 'Tour of the office floor (or virtual equivalent for remote)', '20 min', 'New hire knows their way around'],
            ['Week 3', 'Introduce 3 key cross-team contacts (Finance partner, HRBP, IT partner)', '15 min', '3 warm intros made'],
            ['Week 4', '1:1 lunch (in-person or virtual) — informal', '60 min', 'Relationship deepens'],
            ['Day 45', 'Check-in: how are things going? What is unclear?', '20 min', 'Buddy escalates blockers'],
            ['Day 90', 'Wrap-up coffee + handover: new hire is now self-sufficient', '20 min', 'Programme closure'],
        ]),
        ('h1', '3. Top 10 things buddies should cover'),
        ('numbered', [
            'How to use the HR Portal (apply leave, claim medical, update personal data).',
            'How to book a meeting room and the etiquette ("no shows" are very visible).',
            'Where the canteen is, hours, and which day has briyani.',
            'How the corporate Teams + email distribution lists are organised.',
            'Who the team gossip is — and who is genuinely senior (titles can be misleading).',
            'How performance reviews work in practice (not just the policy).',
            'Which CEO town halls + ExCo updates actually matter; which to skim.',
            'Where the prayer rooms / wellness rooms / quiet rooms are.',
            'Office parking, public transport, and ride-share spots.',
            'How to escape boring meetings politely (gracefully decline at the calendar stage).',
        ]),
        ('h1', '4. Common buddy questions'),
        ('bullets', [
            '"What if my new hire and I do not click?" — Tell Catherine; we will reassign without drama.',
            '"What if my hiring manager is the bottleneck?" — Coach the new hire to escalate via HRBP; do not work around the manager.',
            '"How much time does this take?" — 4-5 hours total over 90 days. Block it in your calendar.',
            '"Am I evaluated on this?" — No formal KPI. It is recognised in your performance narrative.',
            '"What if my new hire is more senior than me?" — Senior hires also need buddies. The dynamic is collegial, not hierarchical.',
        ]),
        ('h1', '5. Escalation triggers'),
        ('bullets', [
            'New hire mentions interpersonal issues with manager or team member: notify HRBP.',
            'New hire considering early resignation: notify HRBP + hiring manager same day.',
            'Wellbeing concerns (visibly struggling, missing days): notify HRBP and offer EAP.',
            'Compliance / ethics concerns: route to Speak Up channel (anonymous available).',
        ]),
        ('h1', '6. Recognition + closure'),
        ('p', 'Buddies receive a small token (RM 300 e-voucher) on successful 90-day programme closure with feedback completed by the new hire. Buddies are recognised at the quarterly People Forum.'),
    ])


def b_prior_year_disclosure():
    _pdf(OUT / 'Prior_Year_Disclosure.pdf',
         'Zava Group — Sustainability Disclosure (FY2024 extract)', [
        ('h1', 'About this extract'),
        ('p', 'Reproduced from the Zava Group Annual Report FY2024 (pages 184-220). This extract is provided for benchmarking against FY2025 disclosure preparation. The full report and TCFD-aligned climate disclosure are available on https://zavagroup.com/investors/annual-report-fy2024.'),
        ('h1', '1. Reporting frameworks applied'),
        ('table', [
            ['Framework', 'Coverage', 'Assurance', 'Status'],
            ['GRI Standards 2021', 'Comprehensive option, 78 disclosures', 'Limited (ISAE 3000) — Tier 1 firm', 'Reported'],
            ['IFRS S1 (general)', '4 thematic pillars', 'Reasonable on 3 KPIs', 'Reported'],
            ['IFRS S2 (climate)', 'Phase 1 — governance + strategy', 'Limited', 'Reported (phase 1)'],
            ['TCFD', '11 of 11 recommendations', 'Limited', 'Reported'],
            ['Bursa MMLR Sustainability', '13 of 13 indicators + 4 industry-specific', 'Limited', 'Reported'],
            ['SASB — Diversified Financials', '6 of 8 metrics', 'Self-asserted', 'Partially reported'],
            ['CDP Climate Change', 'C-score (FY2023: B)', 'Independent', 'Submitted'],
            ['CDP Water Security', 'C-score', 'Independent', 'Submitted'],
        ]),
        ('h1', '2. Headline metrics (FY2024 vs FY2023)'),
        ('table', [
            ['KPI', 'FY2023', 'FY2024', 'Change', 'Target FY2030'],
            ['Scope 1 emissions (tCO2e)', '184,200', '178,400', '-3.1%', '120,000 (-35%)'],
            ['Scope 2 emissions (tCO2e)', '92,800', '86,100', '-7.2%', '20,000 (-78%)'],
            ['Scope 3 (selected categories) tCO2e', '1,820,000', '1,742,000', '-4.3%', 'In modelling'],
            ['Energy intensity (GJ/MYR M)', '12.4', '11.8', '-4.8%', '< 8.0'],
            ['Renewable electricity %', '14%', '22%', '+8 pp', '50%'],
            ['Lost-time injury frequency (per M hrs)', '1.42', '1.18', '-16.9%', '< 1.0'],
            ['Women in leadership (Bands 1-3)', '28%', '31%', '+3 pp', '40%'],
            ['Local procurement spend %', '64%', '68%', '+4 pp', '75%'],
        ]),
        ('h1', '3. Climate-related risks (TCFD-aligned)'),
        ('bullets', [
            'Physical — flooding: 14 sites flagged High exposure under 2030 RCP 8.5 scenario; resilience capex MYR 124M committed FY2025-2027.',
            'Physical — heat stress: 8 plantation estates; workforce productivity adjustment in 2050 base case (-4% labour hours).',
            'Transition — carbon pricing: MYR 50/tCO2e shadow price applied in capex decisions > MYR 100M.',
            'Transition — policy: Indonesia carbon tax 2025; modelling indicates MYR 38M annualised cost on current scope.',
            'Reputational — palm oil sustainability: zero deforestation commitment + RSPO 100% by FY2028.',
        ]),
        ('h1', '4. Governance + assurance'),
        ('p', 'Board Sustainability Committee — quarterly oversight, chaired by INED. Group CFO accountable for sustainability disclosure controls. Internal Audit annual review. External auditor limited assurance on 14 KPIs (signed off 18 March 2025).'),
        ('h1', '5. Reflection on FY2024 disclosure'),
        ('p', 'Areas the auditor flagged as requiring improvement for FY2025: (a) Scope 3 data quality on 8 of 14 categories (currently High variance); (b) climate scenario analysis quantification under IFRS S2 phase 2; (c) double-counting risk on group consolidation for renewable energy attribute certificates; (d) social KPI methodology for incidents requiring re-categorisation.'),
        ('p', 'These are the primary scope items for FY2025 disclosure preparation now under way.'),
    ])


def b_role_specific_onboarding_plan():
    _docx(OUT / 'Role_Specific_Onboarding_Plan.docx',
          'Role-Specific Onboarding Plan — 30 / 60 / 90 day', [
        ('p', 'New hire: <to be populated> | Role: Senior Manager, Group Finance | Hiring manager: Hadar Caspit (Group CFO) | HRBP: Farah Idris | Buddy: Lim Mei Ling | Plan version: v1.0 | Start date: <to be populated>.'),
        ('p', 'Purpose: This plan sets expectations and milestones for the first 90 days. It is reviewed at day 14, 30, 60, and 90. Both new hire and hiring manager sign off on day 90.'),
        ('h1', 'Days 0-7 — Welcome + setup'),
        ('table', [
            ['Item', 'Owner', 'Deadline', 'Done?'],
            ['Laptop + access setup (M365, network, VPN)', 'IT Onboarding', 'Day 1 by 10am', ''],
            ['HR orientation + benefits enrolment', 'Group HR', 'Day 1 PM', ''],
            ['Team welcome lunch', 'Hiring manager', 'Day 2', ''],
            ['Buddy 1:1 (30 min)', 'Lim Mei Ling', 'Day 3', ''],
            ['Code of Ethics, Anti-Bribery, Data Privacy e-learnings', 'New hire', 'End of Week 1', ''],
            ['Read Group Strategy Framework + FY2026 plan', 'New hire', 'End of Week 1', ''],
        ]),
        ('h1', 'Days 8-30 — Orientation + first deliverable'),
        ('bullets', [
            'Hiring manager 1:1 weekly — review priorities and surface blockers.',
            'Meet all direct stakeholders (Group Treasurer, Group FP&A lead, IR, Group Risk, Tax) — 30-min intro each.',
            'Shadow the monthly close cycle from D-5 to D+5 (observe, do not own yet).',
            'First deliverable: complete a financial close variance analysis for one division (mentored).',
            'Day 14 check-in: hiring manager + HRBP + new hire — 30 min on settling in.',
            'Day 30 review: confirm one quick win delivered; refresh 60-90 day plan.',
        ]),
        ('h1', 'Days 31-60 — Own a workstream'),
        ('bullets', [
            'Take ownership of monthly close for 2 divisions (Finance Manager handover by D+45).',
            'Lead one variance review session with division CFO + Group CFO (D+50).',
            'Complete deep-dive on group capital structure + covenant headroom (memo to Group CFO by D+55).',
            'Begin participation in monthly Risk Committee (observer first, then contributor).',
            'Day 60 review: hiring manager + HRBP + new hire — formal mid-point review.',
        ]),
        ('h1', 'Days 61-90 — Operate independently'),
        ('bullets', [
            'Independently own monthly close + commentary for 3 divisions.',
            'Present one substantive paper to Group CFO (e.g. covenant strategy, working capital optimisation).',
            'Co-author one chapter of the next Investor Day deck.',
            'Coach one junior team member on a defined area (mentee for the next 90 days).',
            'Identify your top 3 development priorities for FY2027.',
            'Day 90 review: confirmed standalone operator. Formal sign-off. Buddy programme closes.',
        ]),
        ('h1', 'Success criteria'),
        ('bullets', [
            'Trust earned with peers and stakeholders (HRBP collects 360-feedback at D+90).',
            'Quick win + substantive contribution both delivered.',
            'No unaddressed compliance / ethics flags.',
            'Wellbeing rating self-assessed and confirmed by hiring manager: green.',
        ]),
        ('h1', 'Escalation + support'),
        ('p', 'If at any point the new hire feels off-track or under-supported, the escalation path is: Buddy first, then HRBP (Farah Idris), then HRBP escalation to Head of HR. Confidentiality is preserved at every level.'),
    ])


def b_root_cause_investigations():
    _docx(OUT / 'Root_Cause_Investigations.docx',
          'Root Cause Investigation Library — Selected Past Incidents', [
        ('p', 'Compiled by: Site Reliability Engineering | Maintained by: Tan Wei Ming (SRE Lead) | Last refreshed: 12 May 2026 | Purpose: pattern library for post-mortem comparison and learning.'),
        ('h1', 'How to use this library'),
        ('p', 'Each entry follows a 5-section template: (1) what happened, (2) what we thought was wrong, (3) what was actually wrong, (4) what we changed, (5) what we still cannot fix easily. The library is searchable on Teams (SRE > Root Cause). Always check this library when triaging a new incident — at least 1 in 3 incidents have a close historical precedent.'),
        ('h1', 'Case 1 — Auth service P95 latency spike (Feb 2026)'),
        ('p', 'What happened: Auth service P95 latency jumped from 280ms to 3,420ms over 4 minutes, error rate from 0.02% to 12.4%. Customer-facing login failures across MY + SG regions. Duration: 42 minutes to recovery.'),
        ('p', 'What we thought was wrong: Initial hypothesis was a downstream database connection pool exhaustion. Team spent the first 18 minutes investigating database.'),
        ('p', 'What was actually wrong: A token validation library update deployed at 13:55 introduced a synchronous JWKS fetch on every request. Local cache TTL was misconfigured to 0. Validation lookups went from in-memory to a remote HTTPS call.'),
        ('p', 'What we changed: (a) reverted library version, (b) introduced canary deployment for auth path, (c) added pre-deployment latency budget test in CI, (d) JWKS cache TTL now enforced > 60 seconds with alarm if 0.'),
        ('p', 'What we still cannot fix easily: there is no synthetic regression test for the auth library across all upstream call patterns. Coverage gap remains.'),
        ('h1', 'Case 2 — Payment gateway intermittent timeouts (Nov 2025)'),
        ('p', 'What happened: 3.4% of payment authorisations timed out over a 90-minute window. Customer complaints spiked. Merchant chargebacks expected.'),
        ('p', 'What we thought was wrong: Issuer side network issue (intermittent).'),
        ('p', 'What was actually wrong: An internal TLS certificate on the inter-DC link expired silently. Connections fell back to a slower path that occasionally exceeded the 30-second issuer timeout.'),
        ('p', 'What we changed: Certificate inventory + 90/60/30/14/7-day expiry alarms. PagerDuty rotation owns cert health.'),
        ('p', 'What we still cannot fix easily: certificates are owned across 3 teams; consolidation is in progress.'),
        ('h1', 'Case 3 — Reporting service OOM cascade (Aug 2025)'),
        ('p', 'What happened: Internal reporting service started OOM-killing pods. Cascading retries from 14 downstream consumers caused a 4-hour internal-only outage (no customer impact).'),
        ('p', 'What we actually fixed: per-tenant memory budget + circuit breaker on downstream retries with jittered backoff.'),
        ('p', 'What we still cannot fix easily: the heavy report consumer is a third-party library we cannot easily replace.'),
        ('h1', 'Case 4 — Mobile app deep-link crash (Jun 2025)'),
        ('p', 'What happened: 0.8% of mobile users on iOS 17.4 crashed on app launch after a marketing campaign deep-link.'),
        ('p', 'What was actually wrong: A nullable field in the campaign config was not handled on the iOS code path. Android was fine.'),
        ('p', 'What we changed: Strict-typed config schema with build-time validation per platform. Hotfix shipped within 6 hours.'),
        ('h1', 'Case 5 — Database failover failure during planned maintenance (Mar 2025)'),
        ('p', 'What happened: Planned failover during scheduled maintenance window failed; primary did not relinquish writes; 11 minutes of inconsistent state.'),
        ('p', 'What was actually wrong: A monitoring agent on the standby was consuming the failover quorum vote due to misconfigured health checks.'),
        ('p', 'What we changed: Quorum participants restricted to database nodes only. Failover drill now monthly (was quarterly).'),
        ('h1', 'Common patterns we see repeatedly'),
        ('bullets', [
            'Configuration drift between environments — staging != production in subtle ways.',
            'Silent dependencies — TLS certs, JWKS endpoints, third-party libraries with implicit network calls.',
            'Insufficient pre-deployment latency / error budget tests for shared services.',
            'Cascading retries without jittered backoff.',
            'Alerting on symptoms not causes — operators waste minutes investigating wrong layer.',
        ]),
        ('h1', 'What to do when triaging a new incident'),
        ('numbered', [
            'Search this library by symptom (latency / error / OOM / timeout / crash).',
            'Compare your incident against the top 3 hits — what did we learn? What changed since?',
            'Verify the historical fix is still in place (it might have regressed).',
            'If genuinely new, capture detailed timeline + diagnostics in your post-mortem.',
            'After the post-mortem, add to this library with a 5-section entry. The library only stays useful if we keep it fed.',
        ]),
    ])


def b_sustainability_strategy():
    _docx(OUT / 'Sustainability_Strategy.docx',
          'Zava Group — Sustainability Strategy 2030', [
        ('p', 'Approver: Board Sustainability Committee | Sponsor: Hadar Caspit (Group CFO) | Co-sponsor: Daichi Maruyama (Head of IR) | Version: 4.0 | Refreshed: April 2026.'),
        ('h1', '1. Why we do this'),
        ('p', 'Sustainability is now a commercial decision, not a compliance overlay. ASEAN customers, regulators, employees, and capital providers all expect Zava to operate within an explicit sustainability envelope. Our cost of capital, talent retention, and licence-to-operate depend on credible action.'),
        ('p', 'This strategy is the Board-endorsed roadmap to 2030. It is reviewed annually by the Board Sustainability Committee. Group CFO is the accountable executive.'),
        ('h1', '2. Our five pillars'),
        ('bullets', [
            'Climate — net-zero Scope 1+2 by 2050; -45% by 2030 vs 2019 baseline.',
            'Nature — zero deforestation across plantation supply chain by 2028; water positive by 2035.',
            'People — top decile diversity and inclusion; LTIFR < 1.0 by 2030.',
            'Communities — 1.5% of group PBT committed to community programmes annually.',
            'Governance — independent assurance on 30+ sustainability KPIs by 2028.',
        ]),
        ('h1', '3. 2030 targets and current progress'),
        ('table', [
            ['Pillar', 'KPI', '2019 baseline', 'FY2024', 'FY2030 target'],
            ['Climate', 'Scope 1+2 (ktCO2e)', '296', '264.5', '156 (-47%)'],
            ['Climate', 'Renewable electricity %', '8%', '22%', '50%'],
            ['Climate', 'Scope 3 (selected) ktCO2e', '2,140', '1,742', '< 1,500'],
            ['Nature', 'Deforestation incidents (plantation)', '6', '1', '0'],
            ['Nature', 'Water withdrawal intensity (m3/MYR M)', '420', '362', '< 280'],
            ['People', 'Women in leadership %', '24%', '31%', '40%'],
            ['People', 'LTIFR (per million hrs)', '1.84', '1.18', '< 1.0'],
            ['Communities', '% PBT committed', '0.8%', '1.4%', '1.5%'],
            ['Governance', '# KPIs externally assured', '6', '14', '30+'],
        ]),
        ('h1', '4. Investment thesis to 2030'),
        ('p', 'Capex envelope FY2025-FY2030 dedicated to sustainability transition: MYR 8.2B (16% of group capex). Top three programmes: (a) plantation supply-chain traceability + replanting (MYR 2.4B), (b) renewable energy + grid efficiency (MYR 2.1B), (c) building electrification + EV fleet (MYR 1.4B).'),
        ('p', 'Expected return profile: portfolio-weighted IRR 11.4%, payback 7.2 years. Cost of capital advantage from sustainability-linked financing (currently 35bp on MYR 12.4B of facilities).'),
        ('h1', '5. Disclosure roadmap'),
        ('bullets', [
            'IFRS S1 — fully adopted FY2025. Reasonable assurance on 5 KPIs.',
            'IFRS S2 — phase 1 (governance + strategy) reported FY2024. Phase 2 (quantified scenario analysis) FY2026.',
            'TCFD — all 11 recommendations met since FY2023.',
            'GRI — comprehensive option since FY2023.',
            'CDP — A- target by FY2028 (current B).',
            'Bursa MMLR Sustainability — full compliance + 4 industry-specific indicators.',
        ]),
        ('h1', '6. Governance + accountability'),
        ('p', 'Board Sustainability Committee — quarterly, chaired by INED. Group CFO is the accountable executive. Each operating division has a sustainability lead reporting both to division CEO and to Group CFO on sustainability matters. Internal Audit reviews sustainability controls annually. External auditor provides limited assurance over 14 KPIs (target 30+ by 2028).'),
        ('h1', '7. Risks we are watching'),
        ('bullets', [
            'Scope 3 data quality — 8 of 14 categories High variance. Improvement plan with suppliers.',
            'Carbon pricing — Indonesia carbon tax 2025; modelled MYR 38M annualised cost.',
            'Greenwashing risk — single-source claims are inadequate; we require minimum two-source verification on every public claim.',
            'Just transition — plantation workforce; reskilling programme needs MYR 240M capex by 2028.',
            'Reporting fatigue — 9 frameworks, 30+ KPIs. Internal teams need automation; data architecture roadmap in flight.',
        ]),
    ])


def b_transfer_pricing_documentation():
    _pdf(OUT / 'Transfer_Pricing_Documentation.pdf',
         'Transfer Pricing Master File — FY2025 (extract)', [
        ('h1', 'About this extract'),
        ('p', 'This extract is the public-distribution version of the Zava Group FY2025 Transfer Pricing Master File prepared under BEPS Action 13 (OECD Three-Tiered Approach). The full Master File + Local Files are available on the Group Tax SharePoint and are restricted to authorised personnel. Date prepared: 28 February 2026. Tax authority: Inland Revenue Board of Malaysia (LHDN) + Direktorat Jenderal Pajak (DJP) Indonesia. Group Tax sponsor: Hadar Caspit (Group CFO).'),
        ('h1', '1. Group structure overview'),
        ('p', 'Zava Group operates 14 reportable business units across 8 ASEAN jurisdictions. The principal holding entity is Zava Holdings Sdn Bhd (Malaysia, KL). Five regional sub-holdings sit beneath the principal. Top 5 inter-company flows by value are listed in Section 3.'),
        ('h1', '2. Functional analysis (FAR) — summary'),
        ('table', [
            ['Entity', 'Function', 'Asset', 'Risk', 'Characterisation'],
            ['Zava Holdings (MY)', 'Strategic IP + brand', 'Marketing IP', 'Bears strategic + market risk', 'Principal'],
            ['Zava Services (MY)', 'Group shared services', 'Limited', 'Low (cost-plus)', 'Routine services provider'],
            ['Zava Treasury (SG)', 'Treasury hub', 'Funding + FX positions', 'Funding + FX risk', 'Limited-risk principal'],
            ['Zava Niaga (ID)', 'Distribution', 'Limited', 'Inventory + market risk (limited)', 'Limited-risk distributor'],
            ['Zava Tech (SG)', 'Software IP development', 'Routine technology', 'Limited routine risk', 'Contract R&D'],
        ]),
        ('h1', '3. Top 5 inter-company flows (FY2025)'),
        ('table', [
            ['Flow', 'From', 'To', 'Annual value', 'TP method'],
            ['Royalty — brand', 'Zava Niaga (ID)', 'Zava Holdings (MY)', 'MYR 184M', 'CUP + benchmarking'],
            ['Management services', 'Zava Holdings (MY)', '12 group entities', 'MYR 92M', 'TNMM cost-plus 8%'],
            ['Intra-group funding', 'Zava Treasury (SG)', '8 group borrowers', 'MYR 6,420M (principal)', 'CUP + interest benchmarking'],
            ['Distribution margin', 'Zava Holdings (MY)', 'Zava Niaga (ID)', 'MYR 2,800M (cost)', 'Resale-minus / TNMM'],
            ['R&D services', 'Zava Tech (SG)', 'Zava Holdings (MY)', 'MYR 68M', 'TNMM cost-plus 7%'],
        ]),
        ('h1', '4. Arm''s-length result + benchmarking'),
        ('bullets', [
            'Cost-plus mark-ups (TNMM) — interquartile range 5% to 11%. Zava entities operate at 7-8%.',
            'Royalty rate — comparables in ASEAN-5 consumer brands range 2.5% to 5.0% of net sales. Zava applies 3.2%.',
            'Funding rate — benchmarked to issuer-rated bonds + 90bp arms-length margin.',
            'Distribution margin — net operating margin of 3.0% to 4.5% within the IQR; Zava Niaga (ID) operates at 3.8%.',
        ]),
        ('h1', '5. Country-by-country reporting'),
        ('p', 'Zava Group is in scope for OECD CbCR (group consolidated revenue > EUR 750M). CbCR is filed annually with LHDN (jurisdiction of ultimate parent). FY2024 filing made 20 November 2025. Notification to other ASEAN tax authorities completed by 30 November 2025.'),
        ('h1', '6. Open audit queries (FY2025)'),
        ('bullets', [
            'LHDN — refresh FAR analysis for 3 related-party flows post-acquisition of Apex Banking.',
            'DJP Indonesia — provide P3B treaty positions for 2 royalty flows (Zava Niaga).',
            'DJP Indonesia — service rendering substance test for management services charges; provide time-tracking samples.',
            'IRB MY — pricing methodology for one intangibles licence (specialty chemicals brand).',
            'Singapore IRAS — Pillar 2 GloBE rules effective FY2025; data prep for top-up calculation.',
        ]),
        ('h1', '7. Risks + monitoring'),
        ('p', 'Highest residual TP exposure relates to (a) royalty-based intangibles flows, where comparables data is sparse outside ASEAN, and (b) financing flows under the new Pillar 2 minimum tax framework. Group Tax monitors both quarterly with external advisor (Tier-1 firm). Provisioning for uncertain tax positions recorded at MYR 38M (FY2024) and reassessed at year-end.'),
    ])


def main():
    builders = [
        b_audit_assurance_findings,
        b_auditor_open_queries,
        b_benefits_guide,
        b_buddy_programme_notes,
        b_prior_year_disclosure,
        b_role_specific_onboarding_plan,
        b_root_cause_investigations,
        b_sustainability_strategy,
        b_transfer_pricing_documentation,
    ]
    for fn in builders:
        try:
            fn()
            print(f'  ok  {fn.__name__}')
        except Exception as e:
            print(f'  ERR {fn.__name__}: {e}')
    print(f'Done. {len(builders)} files processed.')


if __name__ == '__main__':
    main()
