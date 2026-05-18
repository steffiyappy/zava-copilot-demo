"""Builders for regulator/cross-dept XLSX stubs — part A (11 of 22).

Covers REG_* and AUD_* workbooks.
"""
from gen_reg_helpers import _xlsx, out


def build_aud_findings_tracker():
    sheets = [
        ("Open findings", "FY2026 Internal Audit — open findings tracker",
         ["ID", "Theme", "Severity", "Owner", "Target close", "Status", "Latest update"],
         [
             ["F-2026-001", "Vendor master — duplicates", "High", "Group Procurement", "2026-07-31", "In progress", "Cleansing run scheduled 2026-06-12"],
             ["F-2026-002", "Privileged access — shared accounts", "Critical", "Group IT Security", "2026-06-15", "In progress", "Shared admin retired on 18 of 22 platforms"],
             ["F-2026-003", "JML — leaver access not revoked", "High", "Group HR", "2026-08-30", "In progress", "Automation pilot on Workday in test"],
             ["F-2026-004", "Vendor risk tiering — outdated", "Medium", "Group Procurement", "2026-09-30", "Open", "Awaiting refreshed risk model"],
             ["F-2026-005", "Contract repository — version control", "Medium", "Group Legal", "2026-10-31", "Open", "Migration plan being scoped"],
             ["F-2026-006", "Segregation of duties — AP team", "High", "Group Finance", "2026-08-15", "In progress", "Workflow split deployed in 3 of 5 markets"],
             ["F-2026-007", "Vendor due diligence — sanctions screening", "High", "Group Compliance", "2026-07-15", "In progress", "Vendor refresh batch 2 of 4 in train"],
             ["F-2026-008", "Data classification — missing labels", "Medium", "Group IT Security", "2026-11-30", "Open", "Awaiting tooling rollout"],
             ["F-2026-009", "Penetration test — high finding", "High", "Group IT Security", "2026-07-31", "In progress", "Patch deployment in change window"],
             ["F-2026-010", "Records retention — over-retention", "Medium", "Group Legal", "2026-12-15", "Open", "Policy refresh underway"],
             ["F-2026-011", "Travel expense — late approvals", "Low", "Group Finance", "2026-09-30", "Open", "Workflow change scoped"],
             ["F-2026-012", "Outsourcing — annual attestation gap", "Medium", "Group Risk", "2026-08-31", "In progress", "10 of 14 attestations received"],
             ["F-2026-013", "Business continuity — exercise overdue", "High", "Group Risk", "2026-07-31", "In progress", "Tabletop scheduled 2026-06-20"],
             ["F-2026-014", "Whistleblowing — case ageing", "High", "Group Compliance", "2026-06-30", "In progress", "Backlog cleared from 14 to 4 cases"],
             ["F-2026-015", "Conflict of interest — annual declarations", "Medium", "Group HR", "2026-09-30", "Open", "Refresh launch in July"],
         ]),
        ("Closed FY26 YTD", "Findings closed in FY2026 year-to-date",
         ["ID", "Theme", "Severity", "Closed on", "Effectiveness validation"],
         [
             ["F-2025-082", "Period-end accruals", "Medium", "2026-02-15", "Sample tested — pass"],
             ["F-2025-091", "Inventory cycle-count coverage", "Medium", "2026-03-04", "Sample tested — pass"],
             ["F-2025-103", "IT change advisory board attendance", "Low", "2026-03-22", "Self-attestation accepted"],
             ["F-2025-118", "Bank reconciliation ageing", "Medium", "2026-04-11", "Sample tested — pass"],
             ["F-2025-124", "Vendor PO three-way match", "High", "2026-04-25", "Sample tested — pass"],
             ["F-2025-131", "Customer credit limit overrides", "Medium", "2026-05-08", "Sample tested — pass"],
             ["F-2025-137", "Cyber-incident response runbook", "High", "2026-05-19", "Tabletop validated"],
             ["F-2025-142", "Data-room access reviews", "Medium", "2026-05-29", "Sample tested — pass"],
         ]),
        ("Ageing summary", "Open findings — ageing buckets",
         ["Severity", "0-30 days", "31-90 days", "91-180 days", "180+ days"],
         [
             ["Critical", 1, 0, 0, 0],
             ["High", 3, 2, 1, 0],
             ["Medium", 2, 3, 1, 1],
             ["Low", 0, 1, 0, 0],
         ]),
    ]
    _xlsx(out("AUD_Findings_Tracker.xlsx"), sheets)


def build_aud_risk_universe():
    sheets = [
        ("Risk universe", "Group Internal Audit — FY2026 risk universe",
         ["Risk ID", "Risk title", "Category", "Inherent rating", "Residual rating", "Audit cycle"],
         [
             ["R-001", "Cyber and information security", "Technology", "Critical", "High", "Annual"],
             ["R-002", "Data privacy and PDPA compliance", "Compliance", "High", "Medium", "Annual"],
             ["R-003", "Sanctions and AML screening", "Compliance", "High", "Medium", "Annual"],
             ["R-004", "Vendor lifecycle and concentration", "Operational", "High", "Medium", "Biennial"],
             ["R-005", "Capital projects governance", "Financial", "High", "Medium", "Annual"],
             ["R-006", "Treasury and FX risk", "Financial", "High", "Medium", "Annual"],
             ["R-007", "Process safety and HSE", "Operational", "Critical", "High", "Annual"],
             ["R-008", "Climate transition risk", "Strategic", "High", "High", "Biennial"],
             ["R-009", "Talent attraction and retention", "Strategic", "High", "Medium", "Biennial"],
             ["R-010", "Tax and transfer pricing", "Financial", "High", "Medium", "Annual"],
             ["R-011", "Regulatory change", "Compliance", "High", "Medium", "Annual"],
             ["R-012", "Fraud and corruption", "Compliance", "High", "Medium", "Annual"],
             ["R-013", "Business continuity and crisis", "Operational", "High", "Medium", "Annual"],
             ["R-014", "Customer conduct and complaints", "Compliance", "Medium", "Low", "Biennial"],
             ["R-015", "M&A integration", "Strategic", "Medium", "Medium", "Event-driven"],
             ["R-016", "Outsourcing and offshoring", "Operational", "Medium", "Low", "Biennial"],
             ["R-017", "IT change and resilience", "Technology", "High", "Medium", "Annual"],
             ["R-018", "Insider trading and market abuse", "Compliance", "Medium", "Low", "Biennial"],
         ]),
        ("Coverage plan", "FY2026 audit coverage plan",
         ["Cycle", "Risk", "Audit subject", "Weeks", "Lead"],
         [
             ["Q1", "R-001", "Privileged access review (group-wide)", 6, "Daichi Maruyama"],
             ["Q2", "R-004", "Vendor lifecycle thematic", 8, "Sasha Ouellet"],
             ["Q2", "R-007", "Process safety — Centralia complex", 5, "Hadar Caspit"],
             ["Q3", "R-006", "Treasury and FX hedging", 6, "Daichi Maruyama"],
             ["Q3", "R-003", "Sanctions screening effectiveness", 5, "Mod Admin"],
             ["Q4", "R-005", "Capital projects governance", 7, "Sasha Ouellet"],
             ["Q4", "R-012", "Fraud and corruption thematic", 6, "Mod Admin"],
         ]),
    ]
    _xlsx(out("AUD_Risk_Universe.xlsx"), sheets)


def build_aud_working_papers():
    sheets = [
        ("Walkthrough index", "Walkthroughs index — Vendor Lifecycle audit",
         ["Ref", "Process step", "Date", "Auditor", "Auditee", "Status"],
         [
             ["WP-01", "Vendor request initiation", "2026-04-04", "DM", "Procurement Ops", "Documented"],
             ["WP-02", "Vendor due diligence", "2026-04-05", "DM", "Compliance", "Documented"],
             ["WP-03", "Vendor master creation", "2026-04-08", "SO", "Procurement Ops", "Documented"],
             ["WP-04", "Contract signature workflow", "2026-04-09", "SO", "Legal", "Documented"],
             ["WP-05", "Purchase order issuance", "2026-04-11", "MA", "Procurement Ops", "Documented"],
             ["WP-06", "Goods or service receipt", "2026-04-15", "MA", "Site Ops", "Documented"],
             ["WP-07", "Invoice processing", "2026-04-17", "HC", "Finance Ops", "Documented"],
             ["WP-08", "Payment release", "2026-04-19", "HC", "Treasury", "Documented"],
             ["WP-09", "Vendor performance review", "2026-04-23", "DM", "Procurement Ops", "Documented"],
             ["WP-10", "Vendor offboarding", "2026-04-25", "SO", "Procurement Ops", "Documented"],
         ]),
        ("Sample selection", "Sample selection — onboarding population",
         ["Sample ID", "Vendor", "Onboarding date", "Risk tier", "Tested by"],
         [
             ["S-01", "Apex Specialty Services", "2025-08-12", "Tier 1", "DM"],
             ["S-02", "Pacific Logistics", "2025-09-04", "Tier 1", "DM"],
             ["S-03", "Asianova Cleaning", "2025-09-19", "Tier 2", "SO"],
             ["S-04", "Centralia Engineering", "2025-10-08", "Tier 2", "SO"],
             ["S-05", "Hadar Consulting", "2025-10-22", "Tier 1", "MA"],
             ["S-06", "Caspit Technical Inspection", "2025-11-07", "Tier 1", "MA"],
             ["S-07", "Ouellet Lab Services", "2025-12-03", "Tier 2", "HC"],
             ["S-08", "Maruyama Industrial Software", "2026-01-15", "Tier 1", "HC"],
             ["S-09", "Mod Admin Compliance Tooling", "2026-02-10", "Tier 1", "DM"],
             ["S-10", "Asianova Travel Management", "2026-02-25", "Tier 3", "SO"],
             ["S-11", "Pacific Cyber Defence", "2026-03-12", "Tier 1", "MA"],
             ["S-12", "Centralia Stationery", "2026-03-28", "Tier 3", "HC"],
         ]),
        ("Issues log", "Working-paper issues log",
         ["Ref", "Issue", "Severity", "Aligned with auditee?", "Goes to report?"],
         [
             ["I-01", "Sanctions screening not re-run on Tier-1 change of beneficial owner", "High", "Yes", "Yes"],
             ["I-02", "Backup-supplier panel not refreshed in 18 months", "Medium", "Yes", "Yes"],
             ["I-03", "Vendor risk tier not recalibrated when spend doubled", "Medium", "Partial", "Yes"],
             ["I-04", "Three-way match exception ageing > 30 days for 11 invoices", "Medium", "Yes", "Yes"],
             ["I-05", "Contract repository missing executed copy for 4 of 12 sampled", "High", "Yes", "Yes"],
             ["I-06", "Vendor performance review evidence absent for 6 of 12 sampled", "Medium", "Partial", "Yes"],
         ]),
    ]
    _xlsx(out("AUD_Working_Papers.xlsx"), sheets)


def build_reg_anti_scam_complaint_register():
    sheets = [
        ("Complaints — open", "Investor Affairs Desk — open complaint register",
         ["Case ID", "Lodged", "Channel", "Alleged operator", "Loss USD", "Triage tier", "Status"],
         [
             ["ZAVA-COMP-2026-0418", "2026-04-18", "Online form", "Zenith Forex AI", 12400, "Tier A", "In review"],
             ["ZAVA-COMP-2026-0421", "2026-04-21", "Phone", "Apex Quant Signals", 8200, "Tier A", "In review"],
             ["ZAVA-COMP-2026-0425", "2026-04-25", "Online form", "Pacific Crypto Yield", 27000, "Tier A", "Escalated"],
             ["ZAVA-COMP-2026-0429", "2026-04-29", "Email", "Asianova Forex Pro", 4100, "Tier B", "In review"],
             ["ZAVA-COMP-2026-0502", "2026-05-02", "Walk-in", "Centralia Gold Yield", 51500, "Tier A", "Escalated"],
             ["ZAVA-COMP-2026-0505", "2026-05-05", "Online form", "Maruyama Mining Tokens", 6800, "Tier B", "In review"],
             ["ZAVA-COMP-2026-0508", "2026-05-08", "Online form", "Ouellet Wealth Bot", 14200, "Tier A", "In review"],
             ["ZAVA-COMP-2026-0511", "2026-05-11", "Phone", "Hadar Capital Markets", 2300, "Tier C", "Acknowledged"],
             ["ZAVA-COMP-2026-0514", "2026-05-14", "Online form", "Caspit Index Yield", 9750, "Tier B", "In review"],
             ["ZAVA-COMP-2026-0518", "2026-05-18", "Email", "Asianova Forex Pro", 18900, "Tier A", "Escalated"],
         ]),
        ("Pattern signals", "Cross-case pattern signals",
         ["Operator brand", "Cases", "Aggregate loss USD", "Common channel", "Common payment route"],
         [
             ["Asianova Forex Pro", 6, 84200, "Facebook ad", "Payment aggregator"],
             ["Zenith Forex AI", 4, 41800, "WhatsApp invite", "Crypto on-ramp"],
             ["Centralia Gold Yield", 3, 122000, "Friend referral", "Wire to mule account"],
             ["Pacific Crypto Yield", 3, 76500, "TikTok video", "Crypto on-ramp"],
             ["Maruyama Mining Tokens", 2, 13200, "Online ad", "Crypto on-ramp"],
         ]),
        ("Closure metrics", "Closure metrics — last 12 months",
         ["Metric", "Value"],
         [
             ["Cases lodged", 412],
             ["Cases closed", 367],
             ["Average days to acknowledge", 1.4],
             ["Average days to first substantive response", 6.2],
             ["Cases escalated to enforcement", 84],
             ["Cases referred to peer agencies", 41],
         ]),
    ]
    _xlsx(out("REG_AntiScam_Complaint_Register.xlsx"), sheets)


def build_reg_broker_fundmanager_database():
    sheets = [
        ("Authorised entities", "Authorised brokers and fund managers",
         ["Entity ID", "Legal name", "Type", "Licence date", "Status", "Lead supervisor"],
         [
             ["BR-001", "Apex Securities", "Stockbroker", "2018-04-12", "Active", "Sasha Ouellet"],
             ["BR-002", "Asianova Capital", "Stockbroker", "2016-09-21", "Active", "Sasha Ouellet"],
             ["BR-003", "Pacific Wealth Brokers", "Stockbroker", "2020-02-08", "Active", "Mod Admin"],
             ["BR-004", "Centralia Securities", "Stockbroker", "2014-11-30", "Active", "Mod Admin"],
             ["BR-005", "Caspit Capital Markets", "Stockbroker", "2022-06-17", "Active — conditions", "Hadar Caspit"],
             ["FM-001", "Apex Asset Management", "Fund manager", "2015-08-04", "Active", "Sasha Ouellet"],
             ["FM-002", "Asianova Investment Partners", "Fund manager", "2017-03-15", "Active", "Mod Admin"],
             ["FM-003", "Pacific Frontier Capital Partners", "Fund manager — VCPE", "2026-04-30", "New — supervised", "Daichi Maruyama"],
             ["FM-004", "Centralia Asset Management", "Fund manager", "2019-01-22", "Active", "Sasha Ouellet"],
             ["FM-005", "Maruyama Private Wealth", "Fund manager — SFO", "2023-10-05", "Active", "Daichi Maruyama"],
             ["FM-006", "Ouellet Macro Partners", "Fund manager — hedge", "2024-07-19", "Active", "Mod Admin"],
             ["FM-007", "Hadar Mezzanine Partners", "Fund manager — PC", "2026-05-15", "Pending licence", "Hadar Caspit"],
         ]),
        ("Specialisation", "Entity specialisation matrix",
         ["Entity ID", "Equities", "Fixed income", "PE/VC", "Hedge", "Private credit", "Crypto-adjacent"],
         [
             ["BR-001", "Yes", "Yes", "No", "No", "No", "No"],
             ["BR-002", "Yes", "Yes", "No", "No", "No", "No"],
             ["BR-003", "Yes", "No", "No", "No", "No", "No"],
             ["BR-004", "Yes", "Yes", "No", "No", "No", "No"],
             ["BR-005", "Yes", "No", "No", "No", "No", "Yes"],
             ["FM-001", "Yes", "Yes", "No", "No", "No", "No"],
             ["FM-002", "Yes", "Yes", "Yes", "No", "No", "No"],
             ["FM-003", "No", "No", "Yes", "No", "No", "No"],
             ["FM-004", "Yes", "Yes", "No", "No", "No", "No"],
             ["FM-005", "Yes", "Yes", "Yes", "Yes", "Yes", "No"],
             ["FM-006", "Yes", "Yes", "No", "Yes", "No", "No"],
             ["FM-007", "No", "No", "No", "No", "Yes", "No"],
         ]),
        ("Supervision schedule", "Supervisory engagement schedule",
         ["Cycle", "Entity ID", "Type", "Lead"],
         [
             ["Q1 onsite", "BR-001", "Full-scope", "Sasha Ouellet"],
             ["Q1 onsite", "FM-002", "Thematic — best execution", "Mod Admin"],
             ["Q2 onsite", "BR-005", "Targeted — conditions follow-up", "Hadar Caspit"],
             ["Q2 desk", "FM-005", "Annual return review", "Daichi Maruyama"],
             ["Q3 onsite", "FM-003", "First-year compliance review", "Daichi Maruyama"],
             ["Q3 desk", "FM-001", "Annual return review", "Sasha Ouellet"],
             ["Q4 onsite", "FM-006", "Targeted — leverage and counterparty", "Mod Admin"],
         ]),
    ]
    _xlsx(out("REG_Broker_FundManager_Database.xlsx"), sheets)


def build_reg_imd_application_tracker():
    sheets = [
        ("Pipeline", "Investment Management Department — application pipeline",
         ["App ID", "Applicant", "Type", "Lodged", "Stage", "Days in stage", "Officer"],
         [
             ["IMD-SFO-2026-0027", "Asianova Caspit Holdings Pte Ltd", "SFO", "2026-04-22", "Initial review", 14, "Daichi Maruyama"],
             ["IMD-VCPE-2026-0014", "Pacific Frontier Capital Partners", "VC/PE manager", "2026-04-19", "Detailed review", 17, "Sasha Ouellet"],
             ["IMD-PC-2026-0009", "Apex Mezzanine Partners Sdn Bhd", "Private credit manager", "2026-04-25", "Detailed review", 11, "Mod Admin"],
             ["IMD-SFO-2026-0028", "Maruyama Family Holdings", "SFO", "2026-04-28", "Initial review", 8, "Daichi Maruyama"],
             ["IMD-VCPE-2026-0015", "Centralia Climate Tech Fund I", "VC/PE manager", "2026-05-02", "Initial review", 5, "Sasha Ouellet"],
             ["IMD-PC-2026-0010", "Ouellet Direct Lending Partners", "Private credit manager", "2026-05-06", "Initial review", 1, "Mod Admin"],
             ["IMD-SFO-2026-0029", "Hadar Caspit Family Office", "SFO", "2026-05-08", "Initial review", -1, "Daichi Maruyama"],
         ]),
        ("Stage SLA", "Stage SLA targets",
         ["Stage", "Target days", "Notes"],
         [
             ["Lodgement to initial review start", 5, "Acknowledgement within 3 days"],
             ["Initial review", 20, "Completeness check; basic risk red flags"],
             ["Detailed review", 45, "Substantive fit-and-proper + business plan"],
             ["Internal approval", 15, "IMD director + Group Compliance"],
             ["Conditions drafting", 10, ""],
             ["Decision + notification", 5, ""],
         ]),
        ("Volume trend", "Volume trend — applications lodged per quarter",
         ["Quarter", "SFO", "VC/PE", "Private credit", "Total"],
         [
             ["Q3 FY2025", 7, 4, 2, 13],
             ["Q4 FY2025", 9, 5, 3, 17],
             ["Q1 FY2026", 11, 6, 4, 21],
             ["Q2 FY2026 YTD", 5, 3, 3, 11],
         ]),
    ]
    _xlsx(out("REG_IMD_Application_Tracker.xlsx"), sheets)


def build_reg_imd_eligibility_rule_matrix():
    sheets = [
        ("Eligibility matrix", "IMD eligibility rule matrix (consolidated view)",
         ["Rule ID", "Applies to", "Requirement", "Threshold or basis", "Evidence"],
         [
             ["E-01", "SFO", "Minimum family net worth", "USD 30m", "Audited statements or independent valuation"],
             ["E-02", "SFO", "Source of wealth disclosure", "Mandatory", "Narrative + supporting documents"],
             ["E-03", "SFO", "Single-family connection", "Family members ≤ 2 degrees", "Family tree and beneficial-ownership chart"],
             ["E-04", "VCPE", "Minimum manager capital", "USD 250k or equivalent", "Audited balance sheet"],
             ["E-05", "VCPE", "Key persons fit-and-proper", "Mandatory", "CV + references + screening"],
             ["E-06", "VCPE", "Track record", "Two prior closed investments", "Investment memos and exits"],
             ["E-07", "Private credit", "Minimum manager capital", "USD 500k or equivalent", "Audited balance sheet"],
             ["E-08", "Private credit", "Independent risk function", "Mandatory", "Org chart and CV"],
             ["E-09", "Private credit", "Concentration policy", "Single borrower ≤ 15%", "Policy document"],
             ["E-10", "All", "AML/CFT programme", "Documented and tested", "Programme manual + last test report"],
             ["E-11", "All", "Disaster recovery", "Documented and tested", "BCP/DR test report"],
             ["E-12", "All", "Independent custody", "Tier-1 custodian", "Custody agreement"],
             ["E-13", "All", "Compliance officer", "Named, qualified", "CV + reporting line"],
             ["E-14", "All", "Internal audit", "Internal or co-sourced", "Audit charter"],
             ["E-15", "All", "Conflict of interest policy", "Documented", "Policy document"],
         ]),
        ("Common deficiencies", "Common deficiencies seen in submissions",
         ["Deficiency", "Frequency", "Typical fix"],
         [
             ["Source-of-wealth narrative too generic", "Very common", "Itemise by asset class with supporting docs"],
             ["Key-person CV gaps (unexplained periods)", "Common", "Explain or provide alternate references"],
             ["Track record without realised exits", "Common", "Provide interim NAV + LP references"],
             ["AML/CFT policy lifted from template", "Common", "Tailor to applicant's strategy"],
             ["Custody arrangement informal", "Less common", "Formalise with Tier-1 custodian"],
             ["No named compliance officer", "Less common", "Appoint + provide CV"],
         ]),
    ]
    _xlsx(out("REG_IMD_Eligibility_Rule_Matrix.xlsx"), sheets)


def build_reg_issuer_compliance_checklist():
    sheets = [
        ("Pre-submission", "Issuer pre-submission compliance checklist",
         ["Item", "Reference", "Status", "Owner", "Evidence"],
         [
             ["Board approval of submission", "Listing rule 8.04", "Pending", "Company Secretary", "Board minutes"],
             ["Auditor sign-off on numbers", "Listing rule 9.02", "Pending", "CFO", "Auditor letter"],
             ["Legal opinion on disclosure", "Listing rule 9.04", "Pending", "GC", "Legal opinion"],
             ["Sponsor confirmation", "Listing rule 10.01", "Pending", "Sponsor", "Sponsor letter"],
             ["Material contract index", "Listing rule 11.06", "Done", "GC", "Index spreadsheet"],
             ["Related-party-transaction disclosure", "Listing rule 12.03", "Done", "CFO", "RPT register"],
             ["Director declarations refreshed", "Listing rule 6.07", "Pending", "Company Secretary", "Refreshed declarations"],
             ["Working capital statement", "Listing rule 9.07", "Pending", "CFO", "Working capital model"],
             ["Use of proceeds narrative", "Listing rule 9.08", "Done", "Strategy", "Narrative section"],
             ["Risk factors review", "Listing rule 9.09", "In review", "Risk + GC", "Risk register"],
         ]),
        ("Open items", "Open items requiring escalation",
         ["Item", "Severity", "Owner", "Deadline"],
         [
             ["Auditor sign-off pending Q4 number lock", "High", "CFO", "2026-06-10"],
             ["Legal opinion subject to final risk factor language", "High", "GC", "2026-06-12"],
             ["Director declarations missing for 2 directors", "Medium", "Company Secretary", "2026-06-08"],
         ]),
    ]
    _xlsx(out("REG_Issuer_Compliance_Checklist.xlsx"), sheets)


def build_reg_issuer_intake_template():
    sheets = [
        ("Submission cover", "Issuer submission cover sheet",
         ["Field", "Value"],
         [
             ["Issuer legal name", ""],
             ["Stock code or proposed code", ""],
             ["Submission type", ""],
             ["Material announcement category", ""],
             ["Lodgement date", ""],
             ["Lodgement time", ""],
             ["Primary contact name", ""],
             ["Primary contact role", ""],
             ["Primary contact email", ""],
             ["Primary contact phone", ""],
             ["Sponsor or adviser", ""],
             ["Auditor", ""],
             ["Legal adviser", ""],
             ["Languages submitted", ""],
             ["Attached documents (count)", ""],
         ]),
        ("Checklist", "Issuer intake checklist (administrative)",
         ["Item", "Required?", "Notes"],
         [
             ["Cover sheet completed", "Yes", "Use this template"],
             ["All attachments listed and labelled", "Yes", ""],
             ["File names match listing convention", "Yes", "[Issuer]_[Type]_[Date]"],
             ["Searchable text PDFs (no flattened images)", "Yes", ""],
             ["English version provided", "Yes", ""],
             ["Local-language version provided", "If listing venue requires", ""],
             ["Director declarations refreshed", "If applicable", ""],
             ["Sponsor letter attached", "If applicable", ""],
             ["Auditor letter attached", "If applicable", ""],
         ]),
    ]
    _xlsx(out("REG_Issuer_Intake_Template.xlsx"), sheets)


def build_reg_policy_existing_library():
    sheets = [
        ("Active policies", "Active policy library",
         ["Policy ID", "Title", "Version", "Effective date", "Next review", "Owner"],
         [
             ["POL-001", "Code of Ethics", "5.1", "2024-01-01", "2027-01-01", "Group Compliance"],
             ["POL-002", "Anti-Bribery and Corruption", "4.3", "2024-07-01", "2026-07-01", "Group Compliance"],
             ["POL-003", "Whistleblowing", "3.4", "2025-01-01", "2027-01-01", "Group Compliance"],
             ["POL-004", "Sanctions and Trade Controls", "2.2", "2025-03-01", "2026-03-01", "Group Compliance"],
             ["POL-005", "AML/CFT", "3.1", "2025-06-01", "2026-06-01", "Group Compliance"],
             ["POL-006", "Data Privacy", "4.2", "2025-05-01", "2026-05-01", "Group Legal"],
             ["POL-007", "Information Security", "6.0", "2025-09-01", "2026-09-01", "Group IT Security"],
             ["POL-008", "Outsourcing and Third-Party Risk", "2.5", "2024-11-01", "2026-11-01", "Group Risk"],
             ["POL-009", "Conflicts of Interest", "3.2", "2025-02-01", "2027-02-01", "Group Compliance"],
             ["POL-010", "Personal Account Dealing", "2.1", "2025-04-01", "2026-04-01", "Group Compliance"],
             ["POL-011", "Insider Trading and Market Abuse", "2.4", "2024-12-01", "2026-12-01", "Group Compliance"],
             ["POL-012", "Records Management", "3.0", "2024-10-01", "2026-10-01", "Group Legal"],
             ["POL-013", "Health, Safety and Environment", "5.0", "2025-01-01", "2027-01-01", "Group HSE"],
             ["POL-014", "Sustainability", "1.4", "2025-08-01", "2026-08-01", "Group ESG"],
             ["POL-015", "Procurement", "4.1", "2024-09-01", "2026-09-01", "Group Procurement"],
         ]),
        ("Pending refresh", "Policies pending refresh in this cycle",
         ["Policy ID", "Reason for refresh", "Drafter", "Target effective"],
         [
             ["POL-002", "Regulator guidance update", "Mod Admin", "2026-08-01"],
             ["POL-005", "Risk-based approach calibration", "Sasha Ouellet", "2026-07-01"],
             ["POL-010", "Crypto-asset dealing inclusion", "Hadar Caspit", "2026-09-01"],
         ]),
    ]
    _xlsx(out("REG_Policy_Existing_Library.xlsx"), sheets)


def build_reg_policy_peer_regulator_scan():
    sheets = [
        ("Peer scan", "Peer regulator scan — recent instruments",
         ["Peer", "Instrument", "Theme", "Published", "Status"],
         [
             ["Peer A", "Guidelines on private-credit licensing", "Private credit", "2026-01-12", "Final"],
             ["Peer A", "Consultation on retail-feeder cooling-off", "Investor protection", "2026-03-05", "Consultation"],
             ["Peer B", "Notice on stablecoin custody", "Crypto-adjacent", "2025-11-30", "Final"],
             ["Peer B", "Cross-border recognition MoU", "Cross-border", "2026-02-22", "Signed"],
             ["Peer C", "Tiered fund-manager licensing", "Fund management", "2025-09-15", "Final"],
             ["Peer C", "Consultation on AI-assisted advice", "Conduct", "2026-04-09", "Consultation"],
             ["Peer D", "Code on social-media solicitation", "Conduct", "2026-01-29", "Final"],
             ["Peer D", "Sandbox for tokenised debt", "Innovation", "2026-03-18", "Open"],
         ]),
        ("Themes summary", "Themes seen across peers",
         ["Theme", "Peers active", "Implication for Zava"],
         [
             ["Tiered licensing for fund managers", "Peer A, C", "Inform our own private-credit tiering"],
             ["Cooling-off for retail feeders", "Peer A, D", "Consider in policy refresh"],
             ["Stablecoin custody framework", "Peer B", "Watch but defer"],
             ["Social-media solicitation enforcement", "Peer D", "Strengthen our anti-scam playbook"],
             ["Tokenised debt sandbox", "Peer D", "Scout for participation"],
         ]),
    ]
    _xlsx(out("REG_Policy_Peer_Regulator_Scan.xlsx"), sheets)


BUILDERS = [
    build_aud_findings_tracker,
    build_aud_risk_universe,
    build_aud_working_papers,
    build_reg_anti_scam_complaint_register,
    build_reg_broker_fundmanager_database,
    build_reg_imd_application_tracker,
    build_reg_imd_eligibility_rule_matrix,
    build_reg_issuer_compliance_checklist,
    build_reg_issuer_intake_template,
    build_reg_policy_existing_library,
    build_reg_policy_peer_regulator_scan,
]


if __name__ == "__main__":
    for fn in BUILDERS:
        fn()
        print("Wrote:", fn.__name__)
