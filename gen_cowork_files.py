"""Generate the 75 missing Cowork + Notebook sample-input files referenced in data.js.

Cowork files use looser naming (PREFIX_Topic_Topic.ext, no _\\d{2}_ segment).
Notebook generic files have no prefix (Account_Plan.docx, CEO_Report.docx, etc).

For each missing file:
  .xlsx -> 3-sheet workbook (KPIs + Driver bridge + Watchlist) tied to prefix industry context
  .docx -> 5-section document (Exec Summary, Background, Detail, Actions, Appendix)
  .pdf  -> 4-page PDF (cover + 3 content pages) via reportlab
  .png  -> sample image (bank statement / scorecard) via PIL

Run: python gen_cowork_files.py
"""

import os, random, re
from datetime import datetime, timedelta
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter
from docx import Document
from docx.shared import Pt, RGBColor, Inches
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.abspath(__file__))
FILES_DIR = os.path.join(ROOT, 'files')
os.makedirs(FILES_DIR, exist_ok=True)

HEADER_FILL = PatternFill(start_color='1F4E78', end_color='1F4E78', fill_type='solid')
HEADER_FONT = Font(bold=True, color='FFFFFF', size=11)
TITLE_FONT = Font(bold=True, color='1F4E78', size=14)
SUBTITLE_FONT = Font(italic=True, color='555555', size=10)

# ----- Prefix -> Industry context lookup --------------------------------------

# Each prefix returns (industry_name, kpi_columns, sheet_titles, unit_labels)
PREFIX_CONTEXT = {
    'AIR': ('Aviation', ['Load Factor %', 'CASK', 'RASK', 'On-time %', 'Cancellation %'],
            ('Route P&L', 'Disruption Bridge', 'Recovery Plan'),
            ['KUL-SIN','KUL-BKK','KUL-CGK','KUL-HKG','KUL-NRT','KUL-DXB','KUL-LHR','Group Total']),
    'AUTO': ('Automotive', ['VIN Affected k','Recall Cost MYR M','Field Failure ppm','Open Cases','Closure %'],
            ('VIN Master', 'Failure Mode Bridge', 'Closure Tracker'),
            ['Sedan A','Sedan B','SUV A','SUV B','MPV','Pickup','Electric','Group Total']),
    'AVI': ('Aviation Ground Ops', ['Slot Util %','On-time %','PAX k','Cargo MT','Gate Delays'],
            ('Slot Master', 'Allocation Bridge', 'Risk Watchlist'),
            ['T1 AM','T1 PM','T2 AM','T2 PM','Cargo','Charter','International','Group Total']),
    'BNK': ('Banking', ['NIM %','CIR %','NPL %','CET1 %','ROE %'],
            ('Borrower Profile', 'Covenant Bridge', 'Watch Borrowers'),
            ['Corporate-1','Corporate-2','Commercial-1','SME-1','SME-2','Retail-Mortgage','Retail-Auto','Group Total']),
    'BNM': ('Banking Regulator', ['Loan Growth %','NPL %','CET1 %','LCR %','NSFR %'],
            ('Loan Book', 'Sector Bridge', 'Regulatory Watch'),
            ['Mortgage','Hire Purchase','Personal','Cards','SME','Corporate','Trade Finance','Group Total']),
    'BPO': ('BPO Services', ['CSAT','FCR %','AHT s','Attrition %','Margin %'],
            ('Client SLA', 'Variance Bridge', 'Escalation Watch'),
            ['Voice-EN','Voice-BM','Voice-ID','Chat','Email','Back-office','Trust&Safety','Group Total']),
    'BRD': ('Board Pack', ['Revenue MYR M','EBITDA MYR M','EBITDA %','FCF MYR M','Net Debt/EBITDA'],
            ('Q4 P&L Pack', 'Variance Bridge', 'Board Watchlist'),
            ['Banking','Property','Plantation','Energy','Telco','Healthcare','Manufacturing','Group Total']),
    'COAL': ('Coal Mining', ['Production kt','Strip Ratio','Cash Cost USD/t','Recovery %','Reserves yrs'],
            ('Mine Plan', 'Variance Bridge', 'HSE Watch'),
            ['Pit A','Pit B','Pit C','Pit D','Stockpile','Wash Plant','Logistics','Group Total']),
    'CON': ('Construction', ['Progress %','Cost MYR M','Float days','Variation MYR M','HSE LTI'],
            ('Project Summary', 'Variation Bridge', 'Risk Watchlist'),
            ['Foundation','Structure','MEP','Facade','Finishes','External Works','Snagging','Total']),
    'CSEC': ('Corp Sec / Board', ['Director Attendance %','Resolution Pass %','Filings On-time %','Q&A Logged','Action Items Open'],
            ('AGM Minutes Index', 'Action Tracker', 'Risk Watchlist'),
            ['AGM','EGM','Audit Cmte','Risk Cmte','Nominations','Remuneration','ESG Cmte','Total']),
    'DBS': ('Banking Statement', ['Opening Bal','Deposits','Withdrawals','Closing Bal','Available Bal'],
            ('Statement Summary','Transaction Log','Reconciliation'),
            ['Current','Savings','FX','Time Deposit','Loan','Credit Card','Investment','Total']),
    'ECOM': ('E-commerce', ['GMV MYR M','Take Rate %','MAU k','Conversion %','Repeat %'],
            ('Sale Funnel', 'Post-mortem Bridge', 'Action Owners'),
            ['Electronics','Fashion','Beauty','Grocery','Home','Toys','Cross-border','Total']),
    'EDU': ('Education', ['Enrolment k','Completion %','NPS','Tuition MYR M','Cost/Student'],
            ('Cohort Snapshot', 'Performance Bridge', 'At-risk Watchlist'),
            ['Pre-school','Primary','Secondary','A-Level','Diploma','Degree','Postgraduate','Group Total']),
    'ESG': ('ESG Disclosure', ['Scope 1 ktCO2e','Scope 2 ktCO2e','Scope 3 ktCO2e','Energy GJ','Water ML'],
            ('Emissions Inventory', 'Reduction Bridge', 'Disclosure Tracker'),
            ['Plantation','Manufacturing','Power','Property','Logistics','Retail','Office','Group Total']),
    'FIN': ('Finance / Treasury', ['Cash MYR M','AR Days','AP Days','Working Capital MYR M','Net Debt MYR M'],
            ('Trial Balance', 'Reconciliation Bridge', 'Open Items'),
            ['Assets','Liabilities','Equity','Revenue','COGS','Opex','Tax','Total Check']),
    'FMCG': ('Food & FMCG', ['Market Share %','GP %','Volume k cs','ACV %','Promo ROI'],
            ('Brand Snapshot', 'Channel Bridge', 'Risk Watchlist'),
            ['Brand A','Brand B','Brand C','Brand D','Brand E','Modern Trade','Traditional Trade','Group Total']),
    'GENINS': ('General Insurance', ['GWP MYR M','Loss Ratio %','Expense Ratio %','Combined Ratio %','Solvency %'],
            ('Open Claims', 'Reserves Bridge', 'Recovery Watchlist'),
            ['Motor','Fire','Marine','Aviation','Liability','Engineering','Health','Group Total']),
    'GLC': ('GLC Portfolio', ['NAV MYR B','IRR %','Carry MYR M','Holdings #','Realised %'],
            ('Portfolio Master', 'Performance Bridge', 'Asset Watchlist'),
            ['Banking','Plantation','Property','Energy','Telco','Healthcare','Tech','Total']),
    'GLV': ('Rubber Gloves', ['OEE %','Reject ppm','Capacity MT','ASP USD/k','EBITDA Margin %'],
            ('Plant Snapshot', 'Yield Bridge', 'Change Control Log'),
            ['Plant 1','Plant 2','Plant 3','Plant 4','Plant 5','Plant 6','Plant 7','Total']),
    'GOV': ('Government', ['PQ Open','Days to Answer','Citizen NPS','Programme Spend %','KPI Met %'],
            ('PQ Tracker', 'Resolution Bridge', 'Escalation Watchlist'),
            ['Ministry A','Ministry B','Ministry C','Agency 1','Agency 2','Agency 3','GLC-1','Total']),
    'GRP': ('Group Capex', ['Capex MYR M','Spend %','Approvals Open','Slippage %','ROI %'],
            ('Capex Pipeline', 'Approval Bridge', 'Slippage Watchlist'),
            ['Banking','Plantation','Property','Energy','Telco','Healthcare','Manufacturing','Total']),
    'HC': ('Healthcare', ['Bed Occupancy %','ALOS days','Patient NPS','Margin %','Pharma Rev %'],
            ('Patient EMR Sample', 'Pathway Bridge', 'Clinical Watchlist'),
            ['Cardiology','Oncology','Orthopaedic','Paediatrics','ICU','ED','Outpatient','Group Total']),
    'HOTEL': ('Hospitality', ['Occupancy %','ADR MYR','RevPAR MYR','GOPPAR MYR','NPS'],
            ('Booking Pace', 'Channel Bridge', 'Yield Watchlist'),
            ['KL-Downtown','KL-Airport','Penang','Langkawi','JB','KK','International','Group Total']),
    'HR': ('Human Resources', ['Attrition %','TtH days','eNPS','Coverage %','Salary Movement %'],
            ('Performance Snapshot', 'Bridge by Function', 'Hot-spot Watchlist'),
            ['Engineering','Sales','Operations','Finance','HR','Marketing','Customer','Group Total']),
    'HSE': ('HSE / Safety', ['LTI rate','TRIR','Near-miss','Open NCRs','Closure %'],
            ('Incident Log', 'Root-cause Bridge', 'Action Tracker'),
            ['Upstream','Refinery','Logistics','Construction','Office','Plant 1','Plant 2','Group Total']),
    'IB': ('Investment Banking', ['Revenue MYR M','EBITDA MYR M','Margin %','Net Debt MYR M','Multiple x'],
            ('3-yr Financials', 'Comparable Bridge', 'Deal Watchlist'),
            ['Target FY-3','Target FY-2','Target FY-1','Target LTM','Peer Median','Peer High','Peer Low','Group Implied']),
    'INC': ('Crisis Channel Log', ['Posts','Threads','Open Items','Closed','Escalations'],
            ('Channel Log','Decision Bridge','Action Items'),
            ['Wartime-General','Ops','Comms','Legal','Regulator','Customer','Vendor','Total']),
    'IR': ('Investor Relations', ['Active Holders','Targeted Holders','Meetings','Q&A','Coverage'],
            ('Strategy Frame', 'Disclosure Bridge', 'Holder Watchlist'),
            ['Long-only','Hedge','Index','Sovereign','Retail','Coverage Buy','Coverage Sell','Total']),
    'IT': ('IT Incident', ['Sev1 Open','MTTR mins','SLA Met %','Tickets','Backlog'],
            ('Incident Timeline', 'Root-cause Bridge', 'Resolution Tracker'),
            ['Network','Compute','Storage','DB','Application','Security','Cloud','Total']),
    'KYC': ('KYC / Compliance', ['Cases Open','High-risk %','SAR Filed','Closure days','Backlog'],
            ('Corporate Registry', 'Risk Bridge', 'Escalation Watchlist'),
            ['Corporate','Trust','SME','High-risk','PEP','Sanctions','Adverse','Total']),
    'LEG': ('Legal Contract', ['Open Matters','Closed','Avg Days','Risk Tier 1','Spend MYR M'],
            ('Contract Index', 'Risk Bridge', 'Negotiation Tracker'),
            ['Commercial','Procurement','Employment','M&A','Litigation','Regulatory','IP','Total']),
    'LIFE': ('Life Insurance', ['APE MYR M','Persistency %','VNB MYR M','EV MYR M','SCR Ratio %'],
            ('Policy Master', 'Persistency Bridge', 'Lapse Watchlist'),
            ['Endowment','Whole Life','Term','ULP','Annuity','Group','Riders','Total']),
    'LOG': ('Logistics', ['OTIF %','Cost/TEU','Fleet Util %','Empty Mile %','Damage %'],
            ('Network Capacity', 'Lane Bridge', 'Customer Watchlist'),
            ['Port-KL','Port-PG','Port-PKG','Inland Hub-1','Inland Hub-2','Cross-border','Last-mile','Total']),
    'MEDIA': ('Media / Marketing', ['Reach M','CPM MYR','Engagement %','VTR %','ROAS x'],
            ('Campaign Brief', 'Channel Bridge', 'Creative Watchlist'),
            ['Search','Social','Display','Video','OOH','TV','Influencer','Total']),
    'MKT': ('Marketing Brand', ['Brand Score','SOV %','NPS','Awareness %','Consideration %'],
            ('Brand Strategy', 'Funnel Bridge', 'Activation Watchlist'),
            ['Master Brand','Sub-brand A','Sub-brand B','Sub-brand C','Innovation','Loyalty','New-to-brand','Total']),
    'MTG': ('Mortgage Finance', ['DPD 30 %','DPD 60 %','DPD 90 %','Cure Rate %','LTV %'],
            ('Past Due Roll', 'Cure Bridge', 'Recovery Watchlist'),
            ['Owner-occ','Investment','HDB','Landed','Condo','Commercial','Refi','Total']),
    'OEE': ('Manufacturing OEE', ['Availability %','Performance %','Quality %','OEE %','Downtime hrs'],
            ('Line 5 Log', 'Downtime Bridge', 'Maintenance Watchlist'),
            ['Shift A','Shift B','Shift C','Day 1','Day 2','Day 3','Maintenance','Total']),
    'OGU': ('O&G Upstream', ['Production kboed','Decline %','Opex/boe','HSE LTI','Reserves yrs'],
            ('Field Forecast', 'Decline Bridge', 'Asset Watchlist'),
            ['Field A','Field B','Field C','Field D','Field E','New Wells','Decommission','Group Total']),
    'OPS': ('Operations', ['Throughput','Yield %','OEE %','Cost/unit','Defect ppm'],
            ('BU1 Procedure', 'Process Bridge', 'Improvement Watchlist'),
            ['Step 1','Step 2','Step 3','Step 4','Step 5','QC','Packaging','Total']),
    'PAY': ('Payments', ['TPV MYR M','Take Rate bps','Fraud bps','Auth Rate %','Chargeback bps'],
            ('Transaction Log', 'Channel Bridge', 'Fraud Watchlist'),
            ['Card-domestic','Card-cross-border','Wallet','QR','Bank Transfer','BNPL','Crypto','Total']),
    'PD': ('Property Development', ['Sales MYR M','Take-up %','GDV MYR M','Margin %','Cost MYR M'],
            ('Project Feasibility', 'Sales Bridge', 'Risk Watchlist'),
            ['Phase 1A','Phase 1B','Phase 2','Phase 3','Common','Retail Lot','Service Apt','Group Total']),
    'PHA': ('Pharmaceutical', ['Yield %','Reject ppm','OOS Open','Deviations','Closure %'],
            ('Change Control Pack', 'Deviation Bridge', 'CAPA Tracker'),
            ['Vial Line','Tablet Line','Capsule Line','Liquid Line','Packaging','QC Lab','Warehouse','Total']),
    'PLT': ('Plantation', ['FFB MT','CPO MT','Yield t/ha','OER %','Cost/MT'],
            ('Audit NCRs', 'Closure Bridge', 'Estate Watchlist'),
            ['Estate A','Estate B','Estate C','Estate D','Mill 1','Mill 2','Mill 3','Group Total']),
    'PROC': ('Procurement', ['Bid Spend MYR M','Savings %','TAT days','Award %','Open RFPs'],
            ('Bid Master', 'Savings Bridge', 'Vendor Watchlist'),
            ['Direct','Indirect','IT','Marketing','Capex','Services','Logistics','Total']),
    'QA': ('Quality Assurance', ['Failed Tests','Pass %','Defects','Closure days','Open NCRs'],
            ('Failed Test Run', 'Root-cause Bridge', 'Remediation Tracker'),
            ['Unit','Integration','System','UAT','Performance','Security','Smoke','Total']),
    'REF': ('Refining', ['Throughput kbpd','Margin USD/bbl','Energy Index','Yield %','Downtime hrs'],
            ('Crude Slate T0', 'Yield Bridge', 'Operations Watchlist'),
            ['CDU','VDU','Hydrocracker','Reformer','Hydrotreater','Polymerization','Blending','Total']),
    'REG': ('Regulator Risk', ['Open Issues','Escalations','Days Open','Closure %','High-risk #'],
            ('Entity Risk Profile', 'Risk Bridge', 'Action Tracker'),
            ['Banking','Insurance','Capital Markets','Payments','Crypto','Fintech','SI','Total']),
    'REIT': ('REIT / Property', ['Occupancy %','NOI Yield %','Rent Growth %','WALE yrs','Capex Ratio %'],
            ('Tenant Master', 'Rent Bridge', 'Tenant Watchlist'),
            ['Office-A','Office-B','Retail-A','Retail-B','Industrial','Logistics','Hospitality','Group Total']),
    'REM': ('Remittance Corridor', ['Volume USD M','Take Rate bps','Win Rate %','Recipients k','Senders k'],
            ('Corridor Volume', 'Channel Bridge', 'Compliance Watchlist'),
            ['MY-ID','MY-PH','MY-VN','MY-IN','MY-BD','MY-NP','MY-MM','Total']),
    'REN': ('Renewable Energy', ['Capacity MW','PLF %','LCOE USD/MWh','Energy Yield GWh','Curtailment %'],
            ('Resource Assessment', 'PLF Bridge', 'Site Watchlist'),
            ['Solar Site 1','Solar Site 2','Solar Site 3','Wind Site 1','Wind Site 2','Hydro 1','Storage','Total']),
    'RE': ('Rare Earth Export', ['Tonnage MT','REE Grade %','Export Value MYR M','Compliance %','Open Permits'],
            ('Export Application', 'Volume Bridge', 'Permit Tracker'),
            ['LREE','MREE','HREE','Concentrate','Mixed Carbonate','Oxide','Metal','Total']),
    'RSK': ('Risk / RAS', ['RWA MYR B','VaR MYR M','Concentration %','Stress Loss MYR M','RAS Util %'],
            ('Current RAS', 'Risk Bridge', 'Concentration Watchlist'),
            ['Credit','Market','Operational','Liquidity','Climate','Conduct','Compliance','Total']),
    'RTL': ('Retail Stores', ['SSSG %','Footfall k','Basket Size MYR','Gross Margin %','Stock Turn x'],
            ('Store P&L', 'Variance Bridge', 'Performance Watchlist'),
            ['Store-A','Store-B','Store-C','Store-D','Store-E','Store-F','Store-G','Total']),
    'SC': ('Supply Chain', ['Backlog days','OTIF %','Inventory MYR M','Stock-out %','Cost/unit'],
            ('Backlog by Customer', 'Allocation Bridge', 'Recovery Watchlist'),
            ['Cust-A Node 1','Cust-A Node 2','Cust-B Node 1','Cust-B Node 2','Cust-C','Cust-D','Cust-E','Total']),
    'SHC': ('Shariah Compliance', ['Open Findings','Closure %','Tabarru MYR M','Surplus %','Audit Days'],
            ('Audit Findings', 'Closure Bridge', 'Risk Watchlist'),
            ['Underwriting','Investment','Marketing','Distribution','Operations','IT','Governance','Total']),
    'SHIP': ('Maritime Shipping', ['Fleet Util %','Voyage Days','Charter USD/day','Bunker USD/MT','TCE USD/day'],
            ('Fleet Schedule', 'Voyage Bridge', 'Dry-dock Watchlist'),
            ['VLCC-1','VLCC-2','Suezmax-1','Aframax-1','LR-1','MR-1','Container','Group Total']),
    'STR': ('Strategy Macro', ['GDP %','Inflation %','FX MYR/USD','OPR %','Confidence Idx'],
            ('Macro Inputs', 'Scenario Bridge', 'Indicator Watchlist'),
            ['Base FY26','Upside FY26','Downside FY26','Base FY27','Upside FY27','Downside FY27','Stress','Total']),
    'TELCO': ('Telco Outage', ['Sites Affected','Customers k','MTTR mins','SLA Met %','Penalty MYR M'],
            ('Outage Timeline', 'Root-cause Bridge', 'Restoration Tracker'),
            ['Core','Access','Transport','RAN','Microwave','Fibre','Power','Total']),
    'TH': ('Town Hall', ['Slides #','Speaker Notes #','Q&A','Attendees','NPS'],
            ('CEO Script', 'Theme Bridge', 'Q&A Watchlist'),
            ['Vision','Performance','Strategy','People','ESG','Customer','Wrap-up','Total']),
    'TKF': ('Takaful', ['Tabarru MYR M','Wakalah Fee MYR M','Surplus %','Combined Ratio %','Solvency %'],
            ('Tabarru Position', 'Surplus Bridge', 'Risk Watchlist'),
            ['Family','General','Medical','Motor','Marine','Aviation','Engineering','Total']),
    'TYR': ('Auto Tyres', ['Test Cycles','Defect ppm','Wear Index','Grip Score','Energy kWh/u'],
            ('Trial Data Run', 'Variance Bridge', 'Process Watchlist'),
            ['Trial 41','Trial 42','Trial 43','Trial 44','Baseline','Spec A','Spec B','Total']),
    'UTIL': ('Power Utility', ['Outage hrs','SAIDI mins','SAIFI #','Customers Affected k','Restoration %'],
            ('Outage Telemetry', 'Cause Bridge', 'Asset Watchlist'),
            ['Substation A','Substation B','Substation C','Feeder 1','Feeder 2','Feeder 3','Transmission','Total']),
}

# Generic context for the 12 Notebook unprefixed files
GENERIC_CONTEXT = {
    'Account_Plan': ('Strategic Account Plan', ['Revenue MYR M','Growth %','Margin %','Wallet Share %','NPS'],
                     ('Account Snapshot','Opportunity Bridge','Action Plan'),
                     ['Industry Cluster A','Industry Cluster B','Government','GLC','Multinational','SME','Mid-market','Group Total']),
    'CEO_Report': ('CEO Report', ['Revenue MYR M','EBITDA MYR M','FCF MYR M','Net Debt MYR M','Headcount'],
                   ('Group P&L','Variance Bridge','Strategic Watchlist'),
                   ['Banking','Plantation','Property','Energy','Telco','Healthcare','Manufacturing','Group Total']),
    'Campaign_Brief': ('Campaign Brief', ['Reach M','Frequency','Engagement %','VTR %','ROAS x'],
                       ('Campaign Plan','Channel Bridge','Creative Watchlist'),
                       ['Awareness','Consideration','Conversion','Retention','Advocacy','Brand','Performance','Total']),
    'Capex_Model_Base': ('Capex Base Model', ['Capex MYR M','Approval Stage','ROI %','Payback yrs','IRR %'],
                         ('Pipeline','Approval Bridge','Slippage Watchlist'),
                         ['Banking','Property','Plantation','Energy','Telco','Healthcare','Manufacturing','Total']),
    'Emissions_Inventory': ('GHG Emissions Inventory', ['Scope 1 ktCO2e','Scope 2 ktCO2e','Scope 3 ktCO2e','Energy GJ','Water ML'],
                            ('Inventory','Reduction Bridge','Disclosure Tracker'),
                            ['Plantation','Manufacturing','Power','Property','Logistics','Retail','Office','Group Total']),
    'Incident_Timeline': ('Incident Timeline', ['Detection mins','Triage mins','Containment mins','Recovery mins','Customers Affected'],
                          ('Timeline Log','Root-cause Bridge','Remediation Tracker'),
                          ['T-15','T-10','T-5','T0','T+5','T+15','T+30','T+60']),
    'Site_Performance_Dashboard': ('Site Performance Dashboard', ['Throughput','Yield %','OEE %','Cost/unit','Defect ppm'],
                                   ('Site Snapshot','Performance Bridge','Risk Watchlist'),
                                   ['Site A','Site B','Site C','Site D','Site E','Site F','Site G','Group Total']),
    'Target_Financials_3Y': ('3-Year Target Financials', ['Revenue MYR M','EBITDA MYR M','EBITDA %','FCF MYR M','Net Debt MYR M'],
                             ('Target Co Financials','Variance Bridge','Sensitivity Watchlist'),
                             ['FY-3','FY-2','FY-1','LTM','FY+1','FY+2','FY+3','Multiple']),
    'Tax_Position_Summary': ('Tax Position Summary', ['Current Tax MYR M','Deferred Tax MYR M','Effective Tax %','Exposures MYR M','Closed %'],
                             ('Position Summary','Variance Bridge','Audit Watchlist'),
                             ['Direct Tax','Indirect Tax','Transfer Pricing','Withholding','Customs','Stamp Duty','Other','Group Total']),
}

DEFAULT_CONTEXT = ('Group', ['KPI 1','KPI 2','KPI 3','KPI 4','KPI 5'],
                   ('Snapshot','Variance Bridge','Watchlist'),
                   ['Unit 1','Unit 2','Unit 3','Unit 4','Unit 5','Unit 6','Unit 7','Group Total'])


def _context_for(fname):
    stem = re.sub(r'\.[^.]+$', '', fname)
    # Try generic first
    if stem in GENERIC_CONTEXT:
        return stem, GENERIC_CONTEXT[stem]
    # Then prefix
    prefix = stem.split('_', 1)[0]
    if prefix in PREFIX_CONTEXT:
        return stem, PREFIX_CONTEXT[prefix]
    return stem, DEFAULT_CONTEXT


# ----- XLSX builder ------------------------------------------------------------

def _make_xlsx(path, fname):
    stem, (industry, cols, sheets, units) = _context_for(fname)
    rnd = random.Random(sum(ord(c) for c in fname) * 13)
    wb = Workbook()
    title_part = stem.replace('_', ' ')

    # Sheet 1
    ws = wb.active
    ws.title = sheets[0][:31]
    ws['A1'] = f"{industry} — {title_part}"
    ws['A1'].font = TITLE_FONT
    ws.merge_cells('A1:H1')
    ws['A2'] = f"Working dataset for {industry.lower()} use case. FY2025 actuals + FY2026 plan (illustrative)."
    ws['A2'].font = SUBTITLE_FONT
    ws.merge_cells('A2:H2')
    headers = ['Unit / Segment', 'FY24 Actual', 'FY25 Actual'] + cols
    for j, h in enumerate(headers, 1):
        c = ws.cell(row=4, column=j, value=h)
        c.font = HEADER_FONT
        c.fill = HEADER_FILL
        c.alignment = Alignment(horizontal='center')
    # Expand to ~30 rows: each unit gets repeated quarterly variants
    quarters = ['Q1', 'Q2', 'Q3', 'Q4']
    row_idx = 5
    for u in units:
        is_total = ('Total' in u) or ('Variance' in u)
        for q in quarters:
            label = u if is_total else f"{u} {q}"
            ws.cell(row=row_idx, column=1, value=label).font = Font(bold=is_total)
            ws.cell(row=row_idx, column=2, value=round(rnd.uniform(120, 1480), 1))
            ws.cell(row=row_idx, column=3, value=round(rnd.uniform(130, 1620), 1))
            for k in range(len(cols)):
                ws.cell(row=row_idx, column=4 + k, value=round(rnd.uniform(0.4, 99.0), 1))
            row_idx += 1
            if is_total:
                break  # totals don't get quarter split
    ws.column_dimensions['A'].width = 38
    for j in range(2, len(headers) + 1):
        ws.column_dimensions[get_column_letter(j)].width = 14
    ws.freeze_panes = 'B5'

    # Sheet 2 — Driver / Bridge
    wb.create_sheet(sheets[1][:31])
    ws2 = wb[sheets[1][:31]]
    ws2['A1'] = f"{title_part} — {sheets[1]}"
    ws2['A1'].font = TITLE_FONT
    ws2.merge_cells('A1:F1')
    headers2 = ['Driver', 'FY25 Impact', 'FY26 Plan', 'Owner', 'Status', 'Notes']
    for j, h in enumerate(headers2, 1):
        c = ws2.cell(row=3, column=j, value=h)
        c.font = HEADER_FONT
        c.fill = HEADER_FILL
    drivers = [
        'Volume / Mix', 'Pricing & Discount', 'Cost Base Reset', 'Capex Re-baseline',
        'Working Capital', 'Regulatory Provisions', 'FX & Hedging', 'Productivity / Automation',
        'Talent / Headcount', 'Vendor Consolidation', 'Process Re-design', 'IT Migration',
        'M&A / Disposal', 'Sustainability Levers', 'Customer Experience', 'Risk Re-rating',
    ]
    owners = ['CFO', 'COO', 'CRO', 'CSO', 'CTO', 'CHRO', 'CMO']
    statuses = ['On track', 'At risk', 'Behind', 'Recovered', 'Mitigated']
    for i, d in enumerate(drivers, start=4):
        ws2.cell(row=i, column=1, value=d)
        ws2.cell(row=i, column=2, value=round(rnd.uniform(-180, 240), 1))
        ws2.cell(row=i, column=3, value=round(rnd.uniform(50, 320), 1))
        ws2.cell(row=i, column=4, value=rnd.choice(owners))
        ws2.cell(row=i, column=5, value=rnd.choice(statuses))
        ws2.cell(row=i, column=6, value=f"See {sheets[2]} for triggers and owner watchlist.")
    for j, w in enumerate([30, 14, 14, 10, 12, 46], start=1):
        ws2.column_dimensions[get_column_letter(j)].width = w

    # Sheet 3 — Watchlist
    wb.create_sheet(sheets[2][:31])
    ws3 = wb[sheets[2][:31]]
    ws3['A1'] = f"{title_part} — {sheets[2]}"
    ws3['A1'].font = TITLE_FONT
    ws3.merge_cells('A1:G1')
    headers3 = ['Item', 'Indicator', 'FY25', 'Threshold', 'Headroom', 'Trigger?', 'Owner']
    for j, h in enumerate(headers3, 1):
        c = ws3.cell(row=3, column=j, value=h)
        c.font = HEADER_FONT
        c.fill = HEADER_FILL
    items = [
        f"Top customer concentration", f"Top vendor exposure",
        f"Flagship product margin", f"Regulator submission cycle",
        f"Largest contract renewal", f"Board KPI #1",
        f"Board KPI #2", f"ESG signal — emissions",
        f"ESG signal — water", f"Talent risk — critical roles",
        f"IT vulnerability backlog", f"Open litigation",
        f"Liquidity buffer days", f"Counter-party rating drift",
    ]
    for i, it in enumerate(items, start=4):
        actual = round(rnd.uniform(40, 95), 1)
        thresh = round(rnd.uniform(60, 90), 1)
        ws3.cell(row=i, column=1, value=it)
        ws3.cell(row=i, column=2, value=rnd.choice(cols))
        ws3.cell(row=i, column=3, value=actual)
        ws3.cell(row=i, column=4, value=thresh)
        ws3.cell(row=i, column=5, value=round(actual - thresh, 1))
        ws3.cell(row=i, column=6, value='Watch' if abs(actual - thresh) < 5 else ('Yes' if actual < thresh else 'No'))
        ws3.cell(row=i, column=7, value=rnd.choice(owners))
    for j, w in enumerate([36, 18, 10, 12, 12, 10, 12], start=1):
        ws3.column_dimensions[get_column_letter(j)].width = w

    wb.save(path)


# ----- DOCX builder ------------------------------------------------------------

def _make_docx(path, fname):
    stem, (industry, cols, sheets, units) = _context_for(fname)
    title_part = stem.replace('_', ' ')
    doc = Document()
    h = doc.add_heading(f"{industry} — {title_part}", level=0)
    h.runs[0].font.color.rgb = RGBColor(0x1F, 0x4E, 0x78)
    p = doc.add_paragraph()
    p.add_run(f"Document owner: {industry} Office").italic = True
    p.add_run(f"  ·  Version: FY2025-A  ·  Classification: Internal — Working").italic = True

    doc.add_heading('1. Executive Summary', level=1)
    doc.add_paragraph(
        f"This document is the working artefact for the {title_part.lower()} use case in the "
        f"{industry.lower()} domain. It is staged for a Microsoft 365 Copilot Cowork / Notebook "
        f"demo and contains plausible (illustrative) figures, lists, and narratives — not real "
        f"customer data. The numbers tie back to the companion spreadsheet of the same stem.")
    doc.add_paragraph(
        f"The intended demo flow: a {industry.lower()} stakeholder asks Copilot to summarise, "
        f"compare, draft, or distribute the contents of this file alongside related artefacts. "
        f"Cowork fans the task out into 5 parallel sub-tasks (draft Word, draft email, schedule "
        f"meeting, post Teams message, build action tracker). Notebook adds it as a source and "
        f"answers grounded questions across all sources.")

    doc.add_heading('2. Scenario & Background', level=1)
    doc.add_paragraph(
        f"The Group is mid-cycle on its FY2025 close and is rolling forward into FY2026 planning. "
        f"The {industry.lower()} portfolio has surfaced a mix of on-track lines and corrective items. "
        f"This {title_part.lower()} captures the working position on those items so the Group "
        f"office, the operating committee, and (where relevant) the regulator-facing officer can "
        f"align on next steps.")
    doc.add_paragraph(
        f"The team has triangulated the working dataset against three peer benchmarks and against "
        f"the regulator's published thresholds for the sector. Findings carried over from the prior "
        f"cycle have been re-examined to test whether the original assumptions still hold under "
        f"the FY2026 base case.")

    doc.add_heading('3. Detail & Working', level=1)
    sub_heads = [
        ('3.1 Position at end of period',
         f"The closing position by unit / segment is captured in the {sheets[0]} tab of the "
         f"companion workbook. Headline metrics — {', '.join(cols[:3])} — are within the agreed "
         f"corridors for {units[0]}, {units[1]}, and {units[2]}; outside the corridor for "
         f"{units[3]} and {units[4]}; and under recovery monitoring for {units[5]}."),
        ('3.2 Key drivers',
         f"The driver bridge (see {sheets[1]} tab) attributes the FY25 variance to a balanced mix "
         f"of volume / mix, pricing and discount discipline, cost base reset, capex re-baseline, "
         f"working capital, regulatory provisions, FX and hedging, and productivity / automation. "
         f"Each driver carries an owner and a status (on-track / at-risk / behind / recovered / "
         f"mitigated)."),
        ('3.3 Sensitivities and assumptions',
         f"The base case assumes FY2026 macro inputs hold within plus/minus 50 basis points of "
         f"the current corridor. The upside and downside scenarios stress the headline metrics by "
         f"plus/minus two corridors and re-test the recovery plan owners against the stressed "
         f"position. Key sensitivities: rate path, FX MYR/USD, commodity benchmarks, regulator "
         f"timing, and customer concentration."),
        ('3.4 Open issues and unknowns',
         f"The watchlist (see {sheets[2]} tab) tracks 14 indicators flagged in the prior review. "
         f"Eight are on-track, four are within five points of the threshold (watch), and two have "
         f"breached and triggered the escalation protocol. Owners and remediation dates are "
         f"recorded against each item."),
    ]
    for sh, body in sub_heads:
        doc.add_heading(sh, level=2)
        doc.add_paragraph(body)

    doc.add_heading('4. Recommended Actions', level=1)
    bullets = [
        f"Confirm the {title_part.lower()} narrative with the {industry} CFO before the Board cut-off.",
        f"Lock the assumption set for the recovery plan and circulate to the division MDs for sign-off.",
        f"Pre-brief the regulator-facing officer on the 30/60/90-day commitments.",
        f"Schedule the cross-functional review with risk, legal, IR, and procurement.",
        f"Capture decisions in the Group decision log with named owners, due dates, and tracking links.",
        f"Stand up a 5-day Cowork sprint to publish the variance brief, lender holding lines, IR Q&A pack, and ExCo update.",
    ]
    for b in bullets:
        doc.add_paragraph(b, style='List Bullet')

    doc.add_heading('5. Appendix — Working dataset units', level=1)
    for u in units:
        doc.add_paragraph(u, style='List Bullet')

    doc.add_heading('6. Sign-off & Distribution', level=1)
    doc.add_paragraph(
        f"Prepared by: {industry} Office  ·  Reviewed by: CFO  ·  Approved by: CEO  ·  "
        f"Distributed to: Board, ExCo, Risk Committee, IR, Group Strategy.")

    doc.save(path)


# ----- PDF builder -------------------------------------------------------------

def _make_pdf(path, fname):
    stem, (industry, cols, sheets, units) = _context_for(fname)
    title_part = stem.replace('_', ' ')
    doc = SimpleDocTemplate(path, pagesize=A4,
                            leftMargin=2 * cm, rightMargin=2 * cm,
                            topMargin=2 * cm, bottomMargin=2 * cm)
    styles = getSampleStyleSheet()
    h1 = ParagraphStyle('h1', parent=styles['Title'], fontSize=20, textColor=colors.HexColor('#1F4E78'), spaceAfter=14)
    h2 = ParagraphStyle('h2', parent=styles['Heading1'], fontSize=14, textColor=colors.HexColor('#1F4E78'), spaceAfter=10)
    body = ParagraphStyle('body', parent=styles['BodyText'], fontSize=10.5, leading=15, spaceAfter=8)
    italic = ParagraphStyle('italic', parent=body, fontName='Helvetica-Oblique', textColor=colors.HexColor('#555555'))

    story = []
    story.append(Paragraph(f"{industry} &mdash; {title_part}", h1))
    story.append(Paragraph(
        f"Document owner: {industry} Office  ·  Version: FY2025-A  ·  Classification: Internal &mdash; Working", italic))
    story.append(Spacer(1, 12))

    story.append(Paragraph("1. Executive Summary", h2))
    story.append(Paragraph(
        f"This document is the working artefact for the {title_part.lower()} use case in the "
        f"{industry.lower()} domain. It is staged for a Microsoft 365 Copilot Cowork / Notebook "
        f"demo and contains plausible (illustrative) figures, lists, and narratives &mdash; not real "
        f"customer data.", body))
    story.append(Paragraph(
        f"The intended demo flow: a {industry.lower()} stakeholder asks Copilot to summarise, "
        f"compare, draft, or distribute the contents of this file alongside related artefacts. "
        f"Cowork fans the task out into 5 parallel sub-tasks. Notebook adds it as a source and "
        f"answers grounded questions across all sources.", body))

    story.append(Paragraph("2. Headline metrics", h2))
    table_data = [['Segment'] + cols]
    rnd = random.Random(sum(ord(c) for c in fname) * 17)
    for u in units[:6]:
        row = [u] + [str(round(rnd.uniform(40, 95), 1)) for _ in cols]
        table_data.append(row)
    t = Table(table_data, colWidths=[5 * cm] + [2.4 * cm] * len(cols))
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1F4E78')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#CCCCCC')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F4F6F8')]),
        ('ALIGN', (1, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    story.append(t)
    story.append(Spacer(1, 12))

    story.append(PageBreak())
    story.append(Paragraph("3. Scenario & Background", h2))
    story.append(Paragraph(
        f"The Group is mid-cycle on its FY2025 close and is rolling forward into FY2026 planning. "
        f"The {industry.lower()} portfolio has surfaced a mix of on-track lines and corrective "
        f"items. This {title_part.lower()} captures the working position on those items so the "
        f"Group office, the operating committee, and (where relevant) the regulator-facing officer "
        f"can align on next steps.", body))
    story.append(Paragraph(
        f"The team has triangulated the working dataset against three peer benchmarks and against "
        f"the regulator's published thresholds for the sector. Findings carried over from the prior "
        f"cycle have been re-examined to test whether the original assumptions still hold under "
        f"the FY2026 base case.", body))

    story.append(Paragraph("4. Key drivers and recovery levers", h2))
    drivers = [
        ('Volume / Mix', 'CFO', 'On track'),
        ('Pricing & Discount', 'COO', 'At risk'),
        ('Cost Base Reset', 'CFO', 'On track'),
        ('Capex Re-baseline', 'CFO', 'Behind'),
        ('Regulatory Provisions', 'CRO', 'Mitigated'),
        ('Productivity / Automation', 'CTO', 'On track'),
        ('Working Capital', 'CFO', 'On track'),
        ('Talent / Headcount', 'CHRO', 'At risk'),
    ]
    td = [['Driver', 'Owner', 'Status']] + [[d, o, s] for d, o, s in drivers]
    t2 = Table(td, colWidths=[8 * cm, 4 * cm, 4 * cm])
    t2.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1F4E78')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#CCCCCC')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F4F6F8')]),
    ]))
    story.append(t2)

    story.append(PageBreak())
    story.append(Paragraph("5. Open items and unknowns", h2))
    items = [
        "Top customer concentration: monitor monthly until below 18 %.",
        "Top vendor exposure: dual-source by end Q2 FY2026.",
        "Regulator submission cycle: align on April / July / October cadence.",
        "Board KPI #1: green status confirmed after Q4 close.",
        "Board KPI #2: amber — driver tree refresh in flight.",
        "ESG signal — emissions: Scope 1 reduction track on plan; Scope 3 under refinement.",
        "Talent — critical roles: 4 vacancies open more than 60 days; offers in progress.",
        "Liquidity buffer: more than 35 days; covenant headroom unchanged.",
    ]
    for it in items:
        story.append(Paragraph("&bull; " + it, body))

    story.append(Paragraph("6. Sign-off & Distribution", h2))
    story.append(Paragraph(
        f"Prepared by: {industry} Office  ·  Reviewed by: CFO  ·  Approved by: CEO  ·  "
        f"Distributed to: Board, ExCo, Risk Committee, IR, Group Strategy.", body))

    doc.build(story)


# ----- PNG builder (bank-statement style) --------------------------------------

def _make_png(path, fname):
    stem, (industry, cols, sheets, units) = _context_for(fname)
    width, height = 1240, 1600
    img = Image.new('RGB', (width, height), 'white')
    d = ImageDraw.Draw(img)
    try:
        f_title = ImageFont.truetype('arialbd.ttf', 32)
        f_h = ImageFont.truetype('arialbd.ttf', 18)
        f_b = ImageFont.truetype('arial.ttf', 14)
        f_s = ImageFont.truetype('arial.ttf', 12)
    except Exception:
        f_title = ImageFont.load_default()
        f_h = ImageFont.load_default()
        f_b = ImageFont.load_default()
        f_s = ImageFont.load_default()

    # Header band
    d.rectangle([0, 0, width, 120], fill='#1F4E78')
    d.text((40, 30), f"{industry}", font=f_title, fill='white')
    d.text((40, 80), 'Sample Bank Statement / Scorecard (illustrative)', font=f_h, fill='#CFE2F3')

    # Account block
    y = 160
    d.text((40, y), 'Statement period:  01 Apr 2026  —  30 Apr 2026', font=f_h, fill='#1F2937'); y += 30
    d.text((40, y), 'Account holder:  Zava Group Treasury — Operating Account', font=f_b, fill='#1F2937'); y += 22
    d.text((40, y), 'Account no:  1234-XXXX-5678  (last 4)   ·   Currency:  MYR', font=f_b, fill='#1F2937'); y += 22
    d.text((40, y), 'Branch:  Kuala Lumpur Main   ·   Manager:  Hadar Caspit (Group CFO)', font=f_b, fill='#1F2937'); y += 30

    # Summary band
    d.rectangle([40, y, width - 40, y + 80], fill='#F4F6F8', outline='#CCCCCC')
    d.text((60, y + 10), 'Opening Balance', font=f_s, fill='#555')
    d.text((60, y + 30), 'MYR 12,340,500.00', font=f_h, fill='#1F2937')
    d.text((360, y + 10), 'Total Credits', font=f_s, fill='#555')
    d.text((360, y + 30), 'MYR  4,820,750.00', font=f_h, fill='#1F2937')
    d.text((660, y + 10), 'Total Debits', font=f_s, fill='#555')
    d.text((660, y + 30), 'MYR  3,915,210.00', font=f_h, fill='#1F2937')
    d.text((960, y + 10), 'Closing Balance', font=f_s, fill='#555')
    d.text((960, y + 30), 'MYR 13,246,040.00', font=f_h, fill='#047857')
    y += 100

    # Transaction table header
    d.rectangle([40, y, width - 40, y + 30], fill='#1F4E78')
    d.text((50, y + 7), 'Date',        font=f_h, fill='white')
    d.text((180, y + 7), 'Description', font=f_h, fill='white')
    d.text((720, y + 7), 'Debit (MYR)', font=f_h, fill='white')
    d.text((900, y + 7), 'Credit (MYR)', font=f_h, fill='white')
    d.text((1080, y + 7), 'Balance',    font=f_h, fill='white')
    y += 36

    rnd = random.Random(7)
    bal = 12340500.00
    counter = [
        ('Salary credit',          0, 320500),
        ('Vendor — IT Services',   85400, 0),
        ('Capex draw-down',        450000, 0),
        ('Refund — overpayment',   0, 12300),
        ('Interest credited',      0, 8450),
        ('Tax payment LHDN',       720500, 0),
        ('Dividend received',      0, 1850000),
        ('Vendor — Construction',  1240000, 0),
        ('Insurance premium',      96400, 0),
        ('Payroll batch',          1322910, 0),
        ('Service fee',            8500, 0),
        ('FX revaluation',         0, 645000),
        ('Refund — duplicate',     0, 88500),
        ('Vendor — Marketing',     145210, 0),
        ('Inflow — IPO proceeds',  0, 1896000),
    ]
    for i, (desc, dr, cr) in enumerate(counter):
        date = (datetime(2026, 4, 1) + timedelta(days=2 * i)).strftime('%d %b %Y')
        bal = bal + cr - dr
        bg = '#FFFFFF' if i % 2 == 0 else '#F4F6F8'
        d.rectangle([40, y, width - 40, y + 26], fill=bg)
        d.text((50, y + 4), date,                                 font=f_s, fill='#1F2937')
        d.text((180, y + 4), desc,                                font=f_s, fill='#1F2937')
        d.text((720, y + 4), f"{dr:,.2f}" if dr else '',          font=f_s, fill='#B91C1C')
        d.text((900, y + 4), f"{cr:,.2f}" if cr else '',          font=f_s, fill='#047857')
        d.text((1080, y + 4), f"{bal:,.2f}",                      font=f_s, fill='#1F2937')
        y += 26

    # Footer
    y += 20
    d.line([(40, y), (width - 40, y)], fill='#CCCCCC', width=1)
    y += 10
    d.text((40, y), 'This is an illustrative statement generated for the Copilot demo. Not a real bank statement.', font=f_s, fill='#555')

    img.save(path)


# ----- Main --------------------------------------------------------------------

def main():
    missing_path = os.path.join(ROOT, '_missing.txt')
    with open(missing_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    names = []
    for ln in lines:
        ln = ln.strip()
        if not ln or ln.startswith('==='):
            continue
        # Strip leading "N. " enumerator if present
        m = re.match(r'^\d+\.\s*(.+)$', ln)
        if m:
            ln = m.group(1).strip()
        if not ln:
            continue
        if re.search(r'\.(xlsx|docx|pdf|png)$', ln, re.IGNORECASE):
            names.append(ln)

    existing = set(os.listdir(FILES_DIR))
    generated = 0
    skipped = 0
    errors = []
    for fname in names:
        if fname in existing:
            skipped += 1
            continue
        path = os.path.join(FILES_DIR, fname)
        try:
            ext = fname.rsplit('.', 1)[-1].lower()
            if ext == 'xlsx':
                _make_xlsx(path, fname)
            elif ext == 'docx':
                _make_docx(path, fname)
            elif ext == 'pdf':
                _make_pdf(path, fname)
            elif ext == 'png':
                _make_png(path, fname)
            else:
                continue
            generated += 1
        except Exception as ex:
            errors.append((fname, repr(ex)))

    print(f'Generated:  {generated}')
    print(f'Skipped:    {skipped}')
    print(f'Errors:     {len(errors)}')
    for f, m in errors[:10]:
        print(f'  {f}: {m}')


if __name__ == '__main__':
    main()
