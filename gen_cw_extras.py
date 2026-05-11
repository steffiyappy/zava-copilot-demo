"""Generate the 9 Cowork Library reference files still missing.

Files produced (all in files/):
  BRD_Audit_Cmte_Minutes.docx
  BRD_Risk_Quarterly_Update.docx
  BRD_Strategy_Memo.docx
  INC_Customer_Complaint_Emails.docx
  INC_Monitoring_Metrics.xlsx
  INC_OnCall_Rota.xlsx
  TH_HR_Quarterly_Scorecard.xlsx
  TH_Prior_Town_Hall_QA.docx
  TH_Pulse_Survey_Results.xlsx
"""
from pathlib import Path
import datetime as dt
import random
random.seed(77)

# Reuse primitives
import importlib.util, sys as _sys
spec = importlib.util.spec_from_file_location('_g', str(Path(__file__).parent / 'gen_cowork_files.py'))
g = importlib.util.module_from_spec(spec)
_prev = _sys.argv
_sys.argv = ['_g']
spec.loader.exec_module(g)
_sys.argv = _prev
_docx, _pdf, _xlsx = g._docx, g._pdf, g._xlsx

OUT = Path(__file__).parent / 'files'
OUT.mkdir(exist_ok=True)


def b_brd_audit_cmte_minutes():
    _docx(OUT / 'BRD_Audit_Cmte_Minutes.docx',
          'Zava Group Audit Committee — Minutes of the Meeting', [
        ('p', 'Date: 28 April 2026 | Venue: Board Room, Level 38, Zava Tower KL + Teams hybrid | Quorum: 5 of 5 (4 INED + 1 NED) | Chair: Y.M. Tunku Adel (INED) | In attendance: Hadar Caspit (Group CFO), Vijay Subramaniam (Head of Internal Audit), Catherine Wong (External Auditor partner), Mod Admin (Group Strategy).'),
        ('h1', '1. Apologies + declaration of interest'),
        ('p', 'No apologies received. No new conflicts declared. Existing standing declarations remain on file.'),
        ('h1', '2. Confirmation of prior minutes'),
        ('p', 'Minutes of the 24 January 2026 meeting were tabled and confirmed without amendment. Matters arising are tracked in the Action Log (Appendix A).'),
        ('h1', '3. FY2025 Internal Audit cycle — closure report'),
        ('p', 'The Head of Internal Audit presented the FY2025 cycle closure: 36 engagements completed, 4 High-severity findings, 9 Medium, 18 Low, 5 closed with no finding. Cumulative risk-weighted exposure of open High+Medium issues estimated at MYR 28.4M revenue-at-risk plus MYR 9.6M remediation cost.'),
        ('p', 'The Committee noted concerns on the timeliness of closure of HF-01 (BNM model recalibration). The Committee resolved to require Group CFO to provide a remediation plan with monthly milestones by 31 May 2026.'),
        ('h1', '4. External audit — open queries'),
        ('p', 'The External Auditor partner reported 28 open queries outstanding for FY2025 sign-off (target: 15 June 2026). Top areas of concern: revenue recognition (6), impairment (5), tax/TP (4), going concern/liquidity (3). The auditor confirmed no fundamental issues identified to date.'),
        ('p', 'The Committee noted the volume of late queries and requested Group Finance to triage and respond within 5 working days, with daily stand-ups commencing immediately.'),
        ('h1', '5. Risk + compliance update'),
        ('bullets', [
            'Compliance register: 30 active items, no Red status. Two Amber items relate to PDPA breach assessment outcomes — both have remediation plans in flight.',
            'Litigation register: 24 cases, 1 High-severity (LIT-2024-001, MYR 8.4M quantum, trial Q4 2026).',
            'BNM AMLA review: scheduled June 2026; Group Compliance preparation on track.',
            'Whistleblowing: 8 cases received Q1, 6 closed (no findings), 2 in investigation.',
        ]),
        ('h1', '6. FY2026 Audit Plan + budget'),
        ('p', 'The Committee approved the FY2026 Internal Audit plan covering 38 engagements, MYR 4.8M budget (flat vs FY2025), and headcount of 24 (vs 22 in FY2025 — 2 additional positions in data analytics).'),
        ('p', 'The Committee requested specific FY2026 focus on: (a) climate disclosure controls (IFRS S2), (b) Pillar 2 minimum tax data readiness, (c) operational resilience under BNM RMiT framework.'),
        ('h1', '7. Resolutions'),
        ('numbered', [
            'Approved: closure report for FY2025 IA cycle with remediation plan requirement for HF-01.',
            'Approved: FY2026 Internal Audit plan + budget + headcount.',
            'Approved: refreshed AC terms of reference (separately tabled).',
            'Noted: external audit progress + open query position.',
            'Noted: risk + compliance + litigation registers.',
        ]),
        ('h1', '8. Next meeting'),
        ('p', 'Next meeting: 25 July 2026, Board Room. Standing agenda + interim AGM-prep deep-dive on going concern and FY2026 H1 closing position.'),
        ('p', 'Meeting closed at 11:42am.'),
    ])


def b_brd_risk_quarterly_update():
    _docx(OUT / 'BRD_Risk_Quarterly_Update.docx',
          'Group Risk — Quarterly Update to the Risk Committee (Q1 FY2026)', [
        ('p', 'For: Risk Committee, 28 April 2026 | Prepared by: Group Risk (Will Henderson, Head of Risk) | Sponsor: Hadar Caspit (Group CFO, Risk Committee Chair). Confidential.'),
        ('h1', '1. Executive summary'),
        ('p', 'Q1 FY2026 was characterised by an emerging credit-cycle softening in Banking, continued sovereign and FX headwinds in Indonesia, and a deteriorating Scope 3 disclosure position as data-quality gaps surfaced ahead of FY2025 reporting. Net risk profile is Amber overall (3 risks Red, 8 Amber, 14 Green).'),
        ('p', 'The most material movements quarter-on-quarter: (a) Credit risk — banking division — moved from Amber to Red as NPL formation indicator crossed appetite threshold; (b) Cyber risk improved from Amber to Green following MFA rollout completion and SOC maturity Tier 2 certification; (c) Climate-physical risk (plantation) was reclassified from Green to Amber after RCP 8.5 scenario refresh.'),
        ('h1', '2. Top risks vs appetite'),
        ('table', [
            ['Risk', 'Q4 FY25', 'Q1 FY26', 'Direction', 'Owner'],
            ['Credit — Banking', 'Amber', 'Red', 'Deteriorating', 'Head of Risk (Banking)'],
            ['FX volatility — IDR', 'Amber', 'Amber', 'Stable adverse', 'Group Treasurer'],
            ['Climate — physical (plantation)', 'Green', 'Amber', 'Deteriorating', 'Head of Plantation'],
            ['Climate — transition (Indonesia carbon tax)', 'Amber', 'Amber', 'Stable adverse', 'Group CFO'],
            ['Cyber + IT resilience', 'Amber', 'Green', 'Improving', 'CIO'],
            ['Conduct + AML', 'Amber', 'Amber', 'Stable', 'Group Compliance'],
            ['Liquidity', 'Green', 'Green', 'Stable', 'Group Treasurer'],
            ['Operational — property handover', 'Amber', 'Amber', 'Stable adverse', 'Head of Property'],
            ['Regulatory — IFRS S2 disclosure', 'Amber', 'Amber', 'Stable adverse', 'Group CFO'],
            ['Geopolitical — supply chain', 'Green', 'Amber', 'Deteriorating', 'COO'],
        ]),
        ('h1', '3. Risk appetite breaches (Red items)'),
        ('bullets', [
            'Banking — NPL formation 12-month trailing 2.84% vs appetite 2.5%. CAR remains comfortably above limits but capital generation slowing.',
            'Operational — property handover backlog at 142 units vs appetite 100; H2 ramp plan in progress.',
            'Climate — Scope 3 data quality High variance on 8 of 14 categories vs appetite < 4. Remediation programme funded MYR 6.4M FY2026-FY2027.',
        ]),
        ('h1', '4. Emerging risks (next 12 months)'),
        ('bullets', [
            'Sovereign credit watchlist — 2 ASEAN sovereigns flagged by rating agencies; review FX exposure quarterly.',
            'Pillar 2 minimum tax — first-time application FY2025; possible top-up tax of MYR 28-45M.',
            'AI + GenAI usage — governance framework in flight; risk of data leakage and IP exposure.',
            'Talent + key-person risk — 11 critical roles flagged for succession refresh.',
            'Supply chain — chip + commodity sourcing concentration; mitigation via dual-sourcing programme.',
        ]),
        ('h1', '5. Stress + scenario testing'),
        ('p', 'A 12-month forward stress was completed in Q1, combining: NPL +200bps in Banking, IDR -15% to MYR, palm oil price -RM 800/MT, and a 4-week IT outage. Group EBITDA impact in the base + stress: -MYR 1.8B (-26%). Covenant headroom remains positive across all facilities under stress, with the tightest at Interest Coverage 4.4x (vs covenant 4.0x).'),
        ('h1', '6. Risk Committee requests'),
        ('numbered', [
            'Approve update to risk appetite statement (separate paper) — recalibration of credit + climate metrics.',
            'Note Red status for 3 items and the remediation plans tabled.',
            'Endorse risk-accept paper for 2 climate-physical legacy items (residual MYR 2.8M).',
            'Approve MYR 6.4M remediation budget for Scope 3 data quality.',
        ]),
    ])


def b_brd_strategy_memo():
    _docx(OUT / 'BRD_Strategy_Memo.docx',
          'Strategy Memo — Capital Allocation Re-baselining FY2026', [
        ('p', 'For: Board Strategy Committee, 28 April 2026 | Author: Mod Admin (Group Strategy Director) | Sponsor: Hadar Caspit (Group CFO). Confidential.'),
        ('h1', '1. The decision we want the Board to take'),
        ('p', 'The Board is asked to approve a re-baselining of the FY2026-FY2030 capital allocation envelope from MYR 12.4B to MYR 14.8B (a 19% uplift) and to formally tilt the allocation toward Banking + Property and away from Plantation + Logistics. The funding profile is preserved (51% internal, 31% sukuk, 18% bank facilities), so no additional shareholder dilution is required.'),
        ('h1', '2. Why we propose this re-baselining'),
        ('bullets', [
            'Banking integration with Apex Banking Group has progressed faster than planned; ROIC trajectory now ahead of underwriting case by 80bps; incremental MYR 1.6B capex unlocks the next phase of digital banking + cross-sell.',
            'Property — Bandar Zava Phase 2 will be MYR 600M over-budget due to specification upgrades and a sub-contractor litigation provision. Proposed: contain to MYR 350M overrun + accelerate Phase 3 to capture demand.',
            'Plantation — replanting capex demand is MYR 480M LESS than originally modelled because of yield-enhancement programme outperformance. Funds redeployable.',
            'Logistics — last-mile JV with Tropika Sdn Bhd materially de-risked; only MYR 220M of the originally-modelled MYR 580M is now required.',
        ]),
        ('h1', '3. Proposed allocation (MYR B, FY2026-FY2030)'),
        ('table', [
            ['Division', 'Current envelope', 'Proposed', 'Delta', 'Rationale'],
            ['Banking', '2.8', '4.4', '+1.6', 'Apex integration phase 2 + digital'],
            ['Property', '2.4', '2.7', '+0.3', 'Phase 2 overrun + Phase 3 acceleration'],
            ['Insurance', '0.8', '0.8', '0.0', 'No change'],
            ['Healthcare', '1.6', '2.1', '+0.5', 'Specialty hospital + tele-medicine'],
            ['Plantation', '2.4', '1.92', '-0.48', 'Replanting demand lower'],
            ['Logistics', '0.6', '0.22', '-0.38', 'JV scope contraction'],
            ['Telco + media', '0.8', '0.8', '0.0', 'No change'],
            ['Renewable energy', '0.8', '1.6', '+0.8', 'PPA pipeline + grid asset'],
            ['Group / corporate / digital', '0.2', '0.26', '+0.06', 'Treasury system refresh'],
            ['Total', '12.4', '14.8', '+2.4', ''],
        ]),
        ('h1', '4. Risk + sensitivity'),
        ('p', 'The proposal is robust under -10% revenue downside (covenant headroom > 1.5x) and under -200bp PD adverse in Banking (post-allocation Tier 1 12.4%, well above 11% appetite). Cash flow break-even at MYR 14.8B is reached at FY2028 vs FY2029 in the original case.'),
        ('h1', '5. Implementation milestones'),
        ('bullets', [
            'Board approval: 28 April 2026.',
            'Q1 sukuk issuance MYR 2.4B: target pricing 1-30 May 2026.',
            'Bank facility refresh MYR 1.4B: target signing 15 June 2026.',
            'First capital draw (Banking phase 2): 1 July 2026.',
            'Quarterly progress review to Board Strategy Committee.',
        ]),
        ('h1', '6. Resolution requested'),
        ('p', 'That the Board approves: (a) the re-baselining of the FY2026-FY2030 capital allocation envelope to MYR 14.8B, (b) the divisional allocation as set out in Section 3, (c) the funding plan and issuance timetable, and (d) delegation to the Group CFO to execute issuance within the parameters of this memo without further Board approval.'),
    ])


def b_inc_customer_complaint_emails():
    _docx(OUT / 'INC_Customer_Complaint_Emails.docx',
          'Customer Complaint Emails — Incident Channel Log (extract)', [
        ('p', 'Incident: SEV-1 Auth + Payment outage, 12 May 2026 14:18-15:00 MYT. Source: customer.support@zavagroup.com inbox. Extracted by Customer Care for incident postmortem use. Customer names anonymised.'),
        ('h1', 'Email 1 — 12 May 2026 14:42'),
        ('p', 'Subject: URGENT — cannot login to my account.'),
        ('p', 'Hello, I have been trying to login for 20 minutes and keep getting an error. I have a transfer that absolutely must clear today before 4pm or I lose a property deposit of MYR 28,000. Please call me back urgently. — Customer M.'),
        ('h1', 'Email 2 — 12 May 2026 14:51'),
        ('p', 'Subject: Payment failed twice — please advise.'),
        ('p', 'I tried to pay my supplier earlier and the page just hung. I tried again and it said "transaction timed out". My supplier now says they will charge me a late fee. Is your system down? — Customer T.'),
        ('h1', 'Email 3 — 12 May 2026 14:58'),
        ('p', 'Subject: Charged twice for a single transaction.'),
        ('p', 'I sent MYR 8,500 to my brother. The first time it failed. I tried again. Now my account shows BOTH transactions debited but only one credited his account. Please reverse the duplicate immediately. — Customer L.'),
        ('h1', 'Email 4 — 12 May 2026 15:04'),
        ('p', 'Subject: When will service resume?'),
        ('p', 'I have been on hold with your call centre for 25 minutes. The app keeps timing out. We are operating a business and cannot accept your "we are working on it" social media post. What is the resolution ETA and what compensation is available? — Customer S.'),
        ('h1', 'Email 5 — 12 May 2026 15:18'),
        ('p', 'Subject: Account shows wrong balance after the outage.'),
        ('p', 'I see my balance has dropped by MYR 4,200 but I have no record of that transaction. My session was active during your outage. Please confirm my balance is correct. I have screenshots from before and after. — Customer R.'),
        ('h1', 'Themes the team identified'),
        ('bullets', [
            'Time-critical transfers (rent, deposits, supplier payments) — high anxiety',
            'Duplicate-charge fears (validates the importance of the customer-facing comms on reconciliation)',
            'Mobile-app dependency — physical branch is no longer a fall-back for most customers',
            'Call-centre saturation — additional capacity needed for SEV-1 events',
            'Balance reconciliation — visible balance vs available balance confusion peaks during outages',
        ]),
        ('h1', 'Apology + recovery script suggestions'),
        ('numbered', [
            'Acknowledge specific symptom (login fail / payment timeout / duplicate charge).',
            'Confirm we have reconciled or are reconciling and timeline.',
            'Where applicable, offer waiver (late fee absorbed, transfer fee refunded) — see playbook.',
            'Offer direct callback rather than queue.',
            'Confirm root cause + permanence of fix in plain language.',
        ]),
    ])


def b_inc_monitoring_metrics():
    sheets = []
    # Sheet 1 — service health timeline
    rows = []
    base = dt.datetime(2026, 5, 12, 13, 0)
    services = ['Auth', 'Payment Gateway', 'Account Read', 'Account Write', 'Notification']
    for i in range(30):
        ts = base + dt.timedelta(minutes=i * 4)
        for s in services:
            if s == 'Auth' and 78 <= i * 4 <= 120:
                p95 = random.randint(2400, 4200)
                err = round(random.uniform(8.0, 14.0), 2)
            elif s == 'Payment Gateway' and 78 <= i * 4 <= 120:
                p95 = random.randint(1800, 3400)
                err = round(random.uniform(3.5, 9.2), 2)
            elif s in ('Account Read', 'Account Write') and 78 <= i * 4 <= 120:
                p95 = random.randint(420, 1200)
                err = round(random.uniform(0.5, 2.4), 2)
            else:
                p95 = random.randint(180, 360)
                err = round(random.uniform(0.01, 0.18), 3)
            rows.append([ts.strftime('%H:%M:%S'), s, p95, err,
                         'Degraded' if p95 > 1000 else 'Healthy'])
    sheets.append(('Service Timeline', 'Service Health Timeline — 12 May 2026',
                   ['Time', 'Service', 'P95 (ms)', 'Error rate (%)', 'Status'], rows))
    # Sheet 2 — pre/during/post comparison
    comp = [
        ['Auth', '280', '3,420', '310', 'Recovered'],
        ['Payment Gateway', '420', '2,180', '440', 'Recovered'],
        ['Account Read', '180', '720', '195', 'Recovered'],
        ['Account Write', '210', '1,140', '230', 'Recovered'],
        ['Notification', '320', '380', '330', 'Stable (latency only)'],
    ]
    sheets.append(('Pre vs During vs Post', 'P95 Latency Pre/During/Post Incident (ms)',
                   ['Service', 'Pre (13:00-14:15)', 'During (14:18-15:00)', 'Post (15:00-16:00)', 'Status'], comp))
    # Sheet 3 — customer impact
    impact = [
        ['Malaysia', 32400, 7300, 1750, 42, 'High'],
        ['Singapore', 12800, 3200, 720, 38, 'Medium'],
        ['Indonesia', 8400, 1980, 410, 44, 'Medium'],
        ['Thailand', 1240, 280, 64, 38, 'Low'],
        ['Vietnam', 980, 220, 48, 38, 'Low'],
    ]
    sheets.append(('Customer Impact', 'Customer Impact by Region',
                   ['Region', 'Affected users', 'Failed auths', 'Delayed Tx', 'Duration (min)', 'Severity'], impact))
    # Sheet 4 — recovery actions
    recovery = [
        ['14:18', 'P1 page fired', 'PagerDuty', 'Auto', 'Open'],
        ['14:22', 'On-call acknowledged', 'L. Tan', 'Manual', 'Acknowledged'],
        ['14:34', 'Root cause identified — JWKS fetch loop', 'L. Tan + Auth team', 'Manual', 'Diagnosed'],
        ['14:41', 'Revert auth-lib v3.2 to v3.1', 'Deploy team', 'Manual', 'Deploying'],
        ['14:48', 'Auth metrics recovering', 'SRE monitoring', 'Auto', 'Recovering'],
        ['14:55', 'Customer comms posted on status page + social', 'Internal Comms', 'Manual', 'Communicated'],
        ['15:00', 'Service nominal — incident resolved', 'SRE Lead', 'Manual', 'Closed'],
        ['15:30', 'Reconciliation sweep starts — duplicate Tx audit', 'Treasury Ops', 'Manual', 'In progress'],
        ['16:00', 'All customer-facing systems stable for 60 min', 'SRE Lead', 'Auto', 'Stable'],
    ]
    sheets.append(('Recovery Actions', 'Recovery Timeline + Actions',
                   ['Time', 'Action', 'Owner', 'Type', 'Status'], recovery))
    _xlsx(OUT / 'INC_Monitoring_Metrics.xlsx', sheets)


def b_inc_oncall_rota():
    sheets = []
    week = dt.date(2026, 5, 11)
    pri = ['L. Tan', 'F. Lim', 'K. Subramaniam', 'D. Maruyama', 'A. Hassan', 'S. Aishah']
    sec = ['Tan Wei Ming', 'Nurul Huda', 'Vijay Raja', 'Chong Kah Wai', 'Farah Idris', 'M. Hassan']
    rows = []
    for d in range(28):
        date = week + dt.timedelta(days=d)
        p = pri[d % 6]
        s = sec[(d + 1) % 6]
        rows.append([date.isoformat(), date.strftime('%A'), p, s,
                     '08:00-08:00 next day', '24h shift'])
    sheets.append(('Rota — May 2026', 'On-Call Rota — May 2026 (P1/P2)',
                   ['Date', 'Day', 'Primary on-call', 'Secondary on-call', 'Hours', 'Notes'], rows))
    # incident-day cross-reference
    incident_day = [
        ['12 May 2026', 'Tuesday', 'L. Tan', 'Tan Wei Ming', '14:18', 'P1 page', '14:22', 'Acknowledged', '4 min ack time'],
    ]
    sheets.append(('Incident Day', 'On-Call Coverage During Incident — 12 May 2026',
                   ['Date', 'Day', 'Primary', 'Secondary', 'Alert time', 'Alert type', 'Ack time', 'Action', 'Notes'], incident_day))
    # SLA performance
    sla = [
        ['P1 ack < 5 min', '12 of 12', '100%', 'Target: 100%', 'Pass'],
        ['P1 mitigation < 30 min', '11 of 12', '92%', 'Target: 95%', 'Just below'],
        ['P2 ack < 15 min', '24 of 26', '92%', 'Target: 95%', 'Just below'],
        ['Mean time to acknowledge (MTTA)', '3.2 min', '', 'Target: < 5 min', 'Pass'],
        ['Mean time to resolve (MTTR)', '28 min', '', 'Target: < 30 min', 'Pass'],
    ]
    sheets.append(('SLA Performance', 'On-Call SLA Performance — Rolling 90 days',
                   ['Metric', 'Result', '%', 'Target', 'Status'], sla))
    _xlsx(OUT / 'INC_OnCall_Rota.xlsx', sheets)


def b_th_hr_quarterly_scorecard():
    sheets = []
    div = ['Banking', 'Insurance', 'Healthcare', 'Plantation', 'Property', 'Logistics', 'Telco + Media', 'Renewables', 'Group Office']
    rows = []
    for d in div:
        hc = random.randint(180, 8200)
        att = round(random.uniform(8.0, 14.0), 1)
        women = round(random.uniform(28.0, 42.0), 1)
        ltif = round(random.uniform(0.4, 1.8), 2)
        engagement = round(random.uniform(68, 82), 1)
        rows.append([d, hc, f'{att}%', f'{women}%', ltif, f'{engagement}%'])
    sheets.append(('Division Scorecard', 'HR Scorecard by Division — Q1 FY2026',
                   ['Division', 'Headcount', 'Attrition (annualised)', 'Women in leadership', 'LTIFR', 'Engagement'], rows))
    # group totals
    group = [
        ['Group total', 'Q4 FY25', 'Q1 FY26', 'Change', 'Target FY26'],
        ['Headcount', '47,820', '48,210', '+390', '48,500'],
        ['Attrition (annualised)', '11.4%', '10.8%', '-0.6 pp', '< 11%'],
        ['Women in leadership', '31%', '32%', '+1 pp', '34%'],
        ['Internal mobility rate', '14%', '15%', '+1 pp', '> 15%'],
        ['LTIFR (per M hrs)', '1.18', '1.12', '-0.06', '< 1.0'],
        ['Engagement score', '74%', '76%', '+2 pp', '> 78%'],
        ['Training hours/employee', '38', '42', '+4', '> 40'],
        ['Critical role succession bench', '76%', '78%', '+2 pp', '> 80%'],
    ]
    sheets.append(('Group Totals', 'Group HR KPIs — Q1 FY2026',
                   ['Metric', 'Q4 FY25', 'Q1 FY26', 'Change', 'Target FY26'], group[1:]))
    # programmes
    prog = [
        ['Leadership academy', '1,240', '1,420', '+180', 'On track'],
        ['Frontline upskilling', '8,400', '9,800', '+1,400', 'Ahead'],
        ['Digital + AI literacy', '24,000', '31,000', '+7,000', 'Ahead'],
        ['Wellbeing programme', 'N/A', '47,800', 'Full rollout', 'Just launched'],
        ['Speak Up training', '46,200', '47,900', '+1,700', 'On track'],
    ]
    sheets.append(('Programmes', 'People Programmes — Participation',
                   ['Programme', 'Q4 FY25 cum.', 'Q1 FY26 cum.', 'Delta', 'Status'], prog))
    _xlsx(OUT / 'TH_HR_Quarterly_Scorecard.xlsx', sheets)


def b_th_prior_town_hall_qa():
    _docx(OUT / 'TH_Prior_Town_Hall_QA.docx',
          'Town Hall Q&A — Prior Quarter (Q4 FY2025) Library', [
        ('p', 'Compiled by: Internal Communications | Town Hall date: 24 January 2026 | Speaker: CEO + Group CFO + CHRO | Format: 30-min CEO address + 25-min live Q&A (Slido + floor). Questions below are anonymised. Used for prep of the next town hall.'),
        ('h1', '1. Compensation + benefits (8 questions)'),
        ('bullets', [
            'Q: Why was last year''s annual increment 4% when CPI was 3.8%? — A: 4% is the median; actual increase varied 2-7% by performance + market band. Bottom band reflects role-pricing realignments.',
            'Q: Are bonuses paid this year? — A: Yes. Group corporate bonus pool is 100% of target.',
            'Q: When does the wellness subsidy increase? — A: Confirmed RM 1,200 from RM 800 effective 1 April 2026.',
            'Q: Can we get more childcare subsidy? — A: Programme review in flight; outcome by Q3.',
            'Q: Will hybrid working continue? — A: Yes, current 2 days in office minimum stays for FY2026.',
            'Q: Tuition assistance for online courses? — A: Yes, RM 12,000 / year covers accredited online (Coursera Plus, LinkedIn Learning already included).',
            'Q: Sabbatical eligibility lowered to 5 years? — A: Under review; no commitment yet.',
            'Q: Parental leave matched between mothers + fathers? — A: Maternity 98 days vs paternity 7 days remains policy. Under review.',
        ]),
        ('h1', '2. Strategy + business performance (6 questions)'),
        ('bullets', [
            'Q: Why is the Banking division flat? — A: Credit cycle softening; we are taking provisions early. EBITDA expected to recover H2 FY2026.',
            'Q: Is Apex Banking integration on track? — A: Yes, ahead of plan. Phase 2 capital approved this quarter.',
            'Q: What is the plan for the Logistics division? — A: JV with Tropika has been re-scoped; capital MYR 220M (was MYR 580M).',
            'Q: Renewable energy capex — what is the timeline? — A: PPA pipeline visible to 2028; MYR 1.6B refreshed envelope.',
            'Q: Will we IPO any subsidiaries? — A: Property arm IPO under exploration; nothing committed.',
            'Q: AI + GenAI — will it replace jobs? — A: We are deploying AI to augment. Reskilling programme is funded for the full workforce.',
        ]),
        ('h1', '3. Culture + ways of working (5 questions)'),
        ('bullets', [
            'Q: Too many meetings — what is being done? — A: ExCo has committed to a "Less Meetings More Doing" charter; meeting-free Wednesday afternoons piloted in 4 divisions.',
            'Q: Wellbeing programme — is it real or PR? — A: 47,800 employees enrolled; 6-session annual EAP free + Tier-1 partnership.',
            'Q: Diversity targets — are managers held accountable? — A: 30% of leadership compensation tied to diversity + engagement metrics from FY2026.',
            'Q: Is feedback during reviews actually anonymous? — A: Yes; 360 feedback platform is operationally separate from HRIS.',
            'Q: Promotion criteria — too opaque. — A: Refreshed career framework + transparent gates launching Q2 FY2026.',
        ]),
        ('h1', '4. ESG + Sustainability (4 questions)'),
        ('bullets', [
            'Q: Are we on track for net zero? — A: -3.1% Scope 1 + -7.2% Scope 2 in FY2024. We are on the trajectory; we are not ahead.',
            'Q: Palm oil + deforestation — what is our position? — A: Zero deforestation commitment + RSPO 100% by FY2028. 1 incident in FY2024 (down from 6 in 2019).',
            'Q: How do you measure Scope 3? — A: Honestly, with significant variance on 8 of 14 categories. Improvement programme funded.',
            'Q: Will we sign on to Race to Zero / SBTi? — A: Engagement under way; intent is yes.',
        ]),
        ('h1', '5. Tough / repeating themes'),
        ('bullets', [
            'Frontline pay vs cost of living — surfaces every quarter; HR market study scheduled Q3.',
            'Manager development — repeating ask; investment increased FY2026.',
            'Decision-making speed — perception that things take too long; Strategy team is mapping decision rights.',
            'Communication consistency — same message lands differently across divisions; comms playbook in refresh.',
        ]),
        ('h1', '6. Use this in the next town hall'),
        ('p', 'Pulse-survey themes for the upcoming Q1 FY2026 town hall (separate document) show high overlap with the above. The CEO speech and Q&A speaker-notes should pre-empt the top 8 recurring themes rather than waiting to be asked.'),
    ])


def b_th_pulse_survey_results():
    sheets = []
    themes = [
        ('Compensation + benefits', 4820, 6.8, 78, 'Frontline pay vs cost of living'),
        ('Manager effectiveness', 3940, 7.2, 72, 'Coaching, feedback, accountability'),
        ('Career growth', 3120, 6.5, 68, 'Promotion criteria, internal mobility'),
        ('Workload + wellbeing', 2880, 6.4, 64, 'Meetings overload, burnout signals'),
        ('Recognition', 2410, 6.9, 70, 'Spot rewards, peer recognition'),
        ('Communication from leadership', 2280, 7.1, 74, 'Consistency across divisions'),
        ('Diversity, inclusion + belonging', 2040, 7.4, 76, 'Visibility, equal opportunity'),
        ('Tools + technology', 1860, 6.7, 71, 'GenAI access, hardware refresh'),
        ('Hybrid work flexibility', 1640, 7.6, 79, 'Continuation, expansion'),
        ('Sustainability + purpose', 1220, 7.8, 81, 'Pride in employer'),
    ]
    sheets.append(('Top 10 Themes', 'Pulse Survey — Top 10 Themes (verbatim count + sentiment + favourable %)',
                   ['Theme', 'Verbatim mentions', 'Sentiment (1-10)', 'Favourable %', 'Sub-themes'], themes))
    # NPS trend
    nps = [
        ['Q1 FY25', 'Engagement', 70],
        ['Q2 FY25', 'Engagement', 72],
        ['Q3 FY25', 'Engagement', 73],
        ['Q4 FY25', 'Engagement', 74],
        ['Q1 FY26', 'Engagement', 76],
        ['Q1 FY25', 'eNPS', 22],
        ['Q2 FY25', 'eNPS', 24],
        ['Q3 FY25', 'eNPS', 26],
        ['Q4 FY25', 'eNPS', 28],
        ['Q1 FY26', 'eNPS', 31],
    ]
    sheets.append(('Engagement + eNPS Trend', 'Engagement Score + eNPS — 5-quarter trend',
                   ['Quarter', 'Metric', 'Value'], nps))
    # By division
    by_div = [
        ['Banking', 8240, 72, 28, 'Lower than group; manager effectiveness flagged'],
        ['Insurance', 2480, 76, 32, 'Stable; tools refresh requested'],
        ['Healthcare', 6420, 78, 35, 'Strong; wellbeing programme well-received'],
        ['Plantation', 4180, 71, 24, 'Frontline pay theme dominant'],
        ['Property', 1820, 75, 30, 'Stable; growth recovering'],
        ['Logistics', 3420, 70, 22, 'Lowest; JV uncertainty pre-clarification'],
        ['Telco + Media', 1640, 77, 33, 'Tools + tech investment well-received'],
        ['Renewables', 480, 81, 41, 'Mission-aligned; high engagement'],
        ['Group Office', 1180, 79, 36, 'Stable'],
    ]
    sheets.append(('By Division', 'Engagement by Division — Q1 FY2026',
                   ['Division', 'Respondents', 'Engagement %', 'eNPS', 'Commentary'], by_div))
    # Verbatim selections
    verbatim = [
        ['Compensation', '"Frontline pay has not kept up with the cost of living in KL."', 'Negative'],
        ['Compensation', '"The annual bonus communication was clearer this year, thank you."', 'Positive'],
        ['Manager', '"My manager listens but does not act. Feedback disappears."', 'Negative'],
        ['Manager', '"My manager has been outstanding through a tough quarter. Recognise her."', 'Positive'],
        ['Career', '"Promotion criteria still feel mysterious in my division."', 'Negative'],
        ['Wellbeing', '"Wednesday afternoon meeting-free is the best thing we did this year."', 'Positive'],
        ['DEI', '"Visibility for women in senior roles has visibly improved."', 'Positive'],
        ['Tools', '"Why does the laptop refresh cycle still feel like a battle?"', 'Negative'],
        ['Hybrid', '"Two days in office is reasonable. Please do not change it."', 'Positive'],
        ['Sustainability', '"Proud to work somewhere that takes climate seriously."', 'Positive'],
    ]
    sheets.append(('Verbatim Quotes', 'Selected Verbatim Quotes (anonymised)',
                   ['Theme', 'Quote', 'Sentiment'], verbatim))
    _xlsx(OUT / 'TH_Pulse_Survey_Results.xlsx', sheets)


def main():
    builders = [
        b_brd_audit_cmte_minutes,
        b_brd_risk_quarterly_update,
        b_brd_strategy_memo,
        b_inc_customer_complaint_emails,
        b_inc_monitoring_metrics,
        b_inc_oncall_rota,
        b_th_hr_quarterly_scorecard,
        b_th_prior_town_hall_qa,
        b_th_pulse_survey_results,
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
