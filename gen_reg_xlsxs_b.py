"""Builders for regulator/cross-dept XLSX stubs — part B (11 of 22).

Covers HR_*, IE_*, LEG_*, PRC_* workbooks.
"""
from gen_reg_helpers import _xlsx, out


def build_hr_outsourcing_and_contract_staff():
    sheets = [
        ("Contract staff register", "Contract staff register — group-wide",
         ["Worker ID", "Vendor", "Role family", "Business unit", "Start date", "Day rate USD", "End date"],
         [
             ["C-1001", "Apex Specialty Services", "IT support", "Group IT", "2024-07-01", 220, "2026-12-31"],
             ["C-1002", "Apex Specialty Services", "IT support", "Group IT", "2024-07-01", 220, "2026-12-31"],
             ["C-1003", "Pacific Engineering Resources", "Plant engineer", "Industrial Mfg", "2025-01-15", 340, "2026-12-31"],
             ["C-1004", "Pacific Engineering Resources", "Plant engineer", "Industrial Mfg", "2025-01-15", 340, "2026-12-31"],
             ["C-1005", "Asianova Finance Outsourcing", "AP clerk", "Group Finance", "2025-04-01", 160, "2026-09-30"],
             ["C-1006", "Asianova Finance Outsourcing", "AR clerk", "Group Finance", "2025-04-01", 160, "2026-09-30"],
             ["C-1007", "Asianova Finance Outsourcing", "AP clerk", "Group Finance", "2025-04-01", 160, "2026-09-30"],
             ["C-1008", "Centralia Legal Outsourcing", "Paralegal", "Group Legal", "2025-08-01", 240, "2027-07-31"],
             ["C-1009", "Centralia Legal Outsourcing", "Paralegal", "Group Legal", "2025-08-01", 240, "2027-07-31"],
             ["C-1010", "Maruyama Data Services", "Data engineer", "Group IT", "2025-10-01", 360, "2027-03-31"],
             ["C-1011", "Maruyama Data Services", "Data analyst", "Group IT", "2025-10-01", 280, "2027-03-31"],
             ["C-1012", "Ouellet Cyber Defence", "SOC analyst", "Group IT", "2025-09-01", 300, "2027-08-31"],
             ["C-1013", "Ouellet Cyber Defence", "SOC analyst", "Group IT", "2025-09-01", 300, "2027-08-31"],
             ["C-1014", "Hadar Consulting", "PMO lead", "Group Strategy", "2026-01-15", 480, "2026-12-15"],
             ["C-1015", "Hadar Consulting", "Programme analyst", "Group Strategy", "2026-01-15", 320, "2026-12-15"],
             ["C-1016", "Apex Specialty Services", "Field tech", "Energy", "2025-11-01", 200, "2026-10-31"],
             ["C-1017", "Apex Specialty Services", "Field tech", "Energy", "2025-11-01", 200, "2026-10-31"],
             ["C-1018", "Pacific Engineering Resources", "QA inspector", "Industrial Mfg", "2025-06-01", 240, "2027-05-31"],
             ["C-1019", "Asianova Finance Outsourcing", "Tax analyst", "Group Finance", "2026-02-01", 240, "2026-12-31"],
             ["C-1020", "Maruyama Data Services", "BI developer", "Group IT", "2026-03-01", 320, "2027-02-28"],
         ]),
        ("Vendor concentration", "Vendor spend concentration",
         ["Vendor", "Workers", "Annual spend USD", "Critical roles?"],
         [
             ["Apex Specialty Services", 28, 1820000, "Yes — field ops"],
             ["Pacific Engineering Resources", 14, 1450000, "Yes — plant"],
             ["Asianova Finance Outsourcing", 22, 1120000, "Partial"],
             ["Centralia Legal Outsourcing", 9, 540000, "Partial"],
             ["Maruyama Data Services", 11, 940000, "Yes — data"],
             ["Ouellet Cyber Defence", 6, 540000, "Yes — SOC"],
             ["Hadar Consulting", 4, 380000, "Partial"],
         ]),
        ("Role family view", "Spend by role family",
         ["Role family", "Workers", "Annual spend USD"],
         [
             ["IT support", 14, 720000],
             ["Plant engineer", 9, 940000],
             ["AP/AR clerk", 16, 720000],
             ["Paralegal", 9, 540000],
             ["Data engineer/analyst", 8, 740000],
             ["SOC analyst", 6, 540000],
             ["PMO/Programme analyst", 4, 380000],
             ["QA inspector", 5, 510000],
             ["Field tech", 12, 770000],
             ["Tax analyst", 3, 360000],
             ["BI developer", 3, 320000],
         ]),
    ]
    _xlsx(out("HR_Outsourcing_and_Contract_Staff.xlsx"), sheets)


def build_hr_skill_gap_survey_2025():
    sheets = [
        ("Skill inventory", "2025 group skill inventory",
         ["Skill family", "Skill", "Headcount with skill", "Headcount needed by 2030", "Gap"],
         [
             ["Data and AI", "Python data engineering", 142, 320, 178],
             ["Data and AI", "ML/MLOps engineering", 38, 140, 102],
             ["Data and AI", "Generative AI prompt design", 64, 480, 416],
             ["Data and AI", "Data governance and lineage", 22, 90, 68],
             ["Cyber", "SOC operations", 48, 120, 72],
             ["Cyber", "Application security", 26, 80, 54],
             ["Cyber", "Identity and access engineering", 31, 70, 39],
             ["Energy transition", "Renewable project structuring", 18, 90, 72],
             ["Energy transition", "Carbon accounting", 12, 60, 48],
             ["Energy transition", "Hydrogen and storage", 4, 40, 36],
             ["Industrial digital", "Plant analytics", 41, 120, 79],
             ["Industrial digital", "Industrial cybersecurity (OT)", 22, 80, 58],
             ["Industrial digital", "Predictive maintenance", 35, 110, 75],
             ["Risk and compliance", "Model risk management", 14, 50, 36],
             ["Risk and compliance", "Sanctions screening operations", 38, 110, 72],
             ["Risk and compliance", "ESG assurance", 17, 70, 53],
             ["Investor and capital markets", "Equity research", 22, 60, 38],
             ["Investor and capital markets", "Private credit underwriting", 14, 50, 36],
             ["Investor and capital markets", "Public market communications", 31, 70, 39],
             ["Customer", "Digital product management", 38, 130, 92],
             ["Customer", "UX research", 18, 70, 52],
             ["Customer", "Customer analytics", 47, 140, 93],
         ]),
        ("Critical skills", "Top 10 critical skills (board view)",
         ["Skill", "Strategic theme", "Gap by 2030", "Severity"],
         [
             ["Generative AI prompt design", "AI everywhere", 416, "Critical"],
             ["Python data engineering", "AI everywhere", 178, "High"],
             ["Carbon accounting", "Net zero pathway", 48, "Critical"],
             ["Renewable project structuring", "Net zero pathway", 72, "Critical"],
             ["Industrial cybersecurity (OT)", "Resilient operations", 58, "Critical"],
             ["SOC operations", "Resilient operations", 72, "High"],
             ["Private credit underwriting", "Capital markets evolution", 36, "High"],
             ["Plant analytics", "Operational excellence", 79, "High"],
             ["ESG assurance", "Trusted disclosures", 53, "High"],
             ["Customer analytics", "Customer obsession", 93, "High"],
         ]),
        ("Source mix", "Sourcing mix preference for critical skills",
         ["Skill", "Internal reskill %", "External hire %", "Contract/partner %"],
         [
             ["Generative AI prompt design", 70, 20, 10],
             ["Python data engineering", 40, 50, 10],
             ["Carbon accounting", 30, 40, 30],
             ["Renewable project structuring", 20, 60, 20],
             ["Industrial cybersecurity (OT)", 40, 30, 30],
             ["SOC operations", 30, 40, 30],
             ["Private credit underwriting", 20, 70, 10],
             ["Plant analytics", 60, 30, 10],
             ["ESG assurance", 50, 30, 20],
             ["Customer analytics", 60, 30, 10],
         ]),
    ]
    _xlsx(out("HR_Skill_Gap_Survey_2025.xlsx"), sheets)


def build_hr_workforce_fy2026():
    sheets = [
        ("Headcount by BU", "Headcount by business unit (FY2026 budget)",
         ["Business unit", "FY2025 actual", "FY2026 budget", "Movement", "Notes"],
         [
             ["Group Corporate Centre", 412, 438, 26, "Strategy + Risk uplift"],
             ["Banking and Financial Services", 4820, 4920, 100, "Branch digitisation offsets growth"],
             ["Industrial Manufacturing", 6240, 6180, -60, "Automation rollout"],
             ["Energy (Oil & Gas)", 3120, 3080, -40, "Tail-asset divestment"],
             ["Energy (Renewables)", 740, 920, 180, "Project pipeline ramp"],
             ["Healthcare", 5180, 5440, 260, "New facility staffing"],
             ["Property Development", 920, 940, 20, ""],
             ["Property REIT", 180, 190, 10, ""],
             ["Retail and FMCG", 4120, 4140, 20, ""],
             ["Logistics and 3PL", 2240, 2310, 70, ""],
             ["Telecommunications", 2080, 2050, -30, ""],
             ["Technology and Data", 1140, 1340, 200, "Talent build"],
             ["Plantation and Agribusiness", 11200, 11150, -50, ""],
             ["Total group", 42412, 43098, 686, ""],
         ]),
        ("FTE by grade", "FTE by grade band (group-wide)",
         ["Grade band", "FY2025 actual", "FY2026 budget", "Movement"],
         [
             ["Executive (EVP and above)", 38, 41, 3],
             ["Senior leadership (SVP/VP)", 412, 438, 26],
             ["Management (M1 to M4)", 3820, 3920, 100],
             ["Professional (P1 to P5)", 14820, 15240, 420],
             ["Specialist (S1 to S5)", 8420, 8480, 60],
             ["Operations (O1 to O6)", 14902, 14979, 77],
         ]),
        ("Movement plan", "Movement plan — FY2026",
         ["Move type", "Volume", "Cost USD m", "Owner"],
         [
             ["Internal promotions", 1120, 6.4, "BU HR Business Partners"],
             ["Internal cross-BU transfers", 480, 1.2, "Group Talent"],
             ["External hires — graduate", 380, 5.1, "Group Talent Acquisition"],
             ["External hires — experienced", 940, 18.6, "Group Talent Acquisition"],
             ["Reskill — critical skills", 720, 8.2, "Group Learning"],
             ["Outplacement / managed exits", 240, 4.1, "BU HR Business Partners"],
             ["Contract conversion (in)", 120, 1.8, "BU HR Business Partners"],
             ["Contract conversion (out)", 90, 1.4, "BU HR Business Partners"],
         ]),
    ]
    _xlsx(out("HR_Workforce_FY2026.xlsx"), sheets)


def build_ie_budget_vs_actual():
    sheets = [
        ("Programme budget", "Investor education programme — FY2026 budget vs actual",
         ["Programme", "Audience", "Budget USD", "Actual YTD USD", "Variance USD", "Variance %"],
         [
             ["First-jobber starter series", "Age 22-30", 180000, 96000, -84000, -47],
             ["Family financial planning", "Age 30-50", 220000, 142000, -78000, -35],
             ["Pre-retirement planning", "Age 50+", 160000, 88000, -72000, -45],
             ["Anti-scam awareness (mass)", "All adults", 280000, 188000, -92000, -33],
             ["Tertiary student campus tour", "Tertiary students", 140000, 70000, -70000, -50],
             ["Sukuk and Islamic finance literacy", "All adults", 120000, 54000, -66000, -55],
             ["IPO and capital markets basics", "Retail investors", 160000, 82000, -78000, -49],
             ["Private credit and alts risk", "HNW retail", 80000, 32000, -48000, -60],
             ["Tertiary educator masterclass", "Tertiary educators", 60000, 28000, -32000, -53],
         ]),
        ("Channel split", "Channel split — FY2026 YTD",
         ["Channel", "Budget USD", "Actual USD", "Variance %"],
         [
             ["In-person events", 480000, 220000, -54],
             ["Webinars and livestream", 220000, 138000, -37],
             ["Bilingual social content", 280000, 184000, -34],
             ["Podcast", 80000, 32000, -60],
             ["Short-form video", 180000, 116000, -36],
             ["School and campus tour", 260000, 90000, -65],
         ]),
        ("Variance commentary", "Variance commentary",
         ["Programme or channel", "Driver", "Owner"],
         [
             ["Pre-retirement planning", "Two scheduled regional roadshows postponed to H2", "Investor Affairs"],
             ["Anti-scam awareness (mass)", "Pacing slightly behind plan; H2 surge expected with Q3 enforcement wave", "Investor Affairs + Comms"],
             ["Tertiary student campus tour", "Universities released calendar later than expected", "Investor Affairs + HR"],
             ["Sukuk and Islamic finance literacy", "Awaiting partner content sign-off", "Investor Affairs + Legal"],
             ["Private credit and alts risk", "Programme launch deferred to Q3 pending policy paper", "Investor Affairs"],
         ]),
    ]
    _xlsx(out("IE_Budget_vs_Actual.xlsx"), sheets)


def build_ie_campaign_metrics_q1():
    sheets = [
        ("Campaign list", "Investor education campaigns — Q1 FY2026",
         ["Campaign", "Channel", "Run window", "Audience", "Spend USD", "Status"],
         [
             ["Spot the Scam — Episode 1", "Short-form video", "2026-02-03 to 2026-02-23", "All adults", 22000, "Closed"],
             ["Spot the Scam — Episode 2", "Short-form video", "2026-02-24 to 2026-03-16", "All adults", 22000, "Closed"],
             ["Spot the Scam — Episode 3", "Short-form video", "2026-03-17 to 2026-04-06", "All adults", 22000, "Closed"],
             ["First-jobber starter — Live #1", "Webinar", "2026-02-14", "Age 22-30", 12000, "Closed"],
             ["First-jobber starter — Live #2", "Webinar", "2026-03-14", "Age 22-30", 12000, "Closed"],
             ["Tertiary tour — Apex University", "In-person event", "2026-02-20", "Tertiary students", 14000, "Closed"],
             ["Tertiary tour — Asianova Institute", "In-person event", "2026-03-12", "Tertiary students", 14000, "Closed"],
             ["IPO basics carousel", "Bilingual social content", "2026-02-01 to 2026-03-31", "Retail investors", 18000, "Closed"],
             ["Sukuk literacy livestream", "Webinar", "2026-03-22", "All adults", 8000, "Closed"],
             ["Family planning workshop", "In-person event", "2026-03-29", "Age 30-50", 18000, "Closed"],
         ]),
        ("Reach and engagement", "Reach and engagement",
         ["Campaign", "Reach", "Watch-through %", "Engagement %", "Top-of-funnel pledges"],
         [
             ["Spot the Scam — Episode 1", 482000, 38, 6.4, 1820],
             ["Spot the Scam — Episode 2", 514000, 41, 7.1, 2010],
             ["Spot the Scam — Episode 3", 538000, 43, 7.6, 2240],
             ["First-jobber starter — Live #1", 12400, 64, 9.8, 720],
             ["First-jobber starter — Live #2", 14600, 67, 10.4, 860],
             ["Tertiary tour — Apex University", 1240, 92, 18.4, 410],
             ["Tertiary tour — Asianova Institute", 1180, 89, 16.7, 380],
             ["IPO basics carousel", 318000, None, 4.2, 1410],
             ["Sukuk literacy livestream", 9800, 58, 11.2, 540],
             ["Family planning workshop", 1820, 94, 22.4, 720],
         ]),
        ("Behaviour change proxy", "Behaviour-change proxies — Q1 FY2026",
         ["Indicator", "Baseline", "Q1 FY2026", "Movement %"],
         [
             ["Scam-tip submissions (per 100k pop)", 4.2, 5.1, 21],
             ["Pledge-to-complete on starter series", 0.18, 0.22, 22],
             ["Tertiary student club sign-ups", 920, 1240, 35],
             ["Sukuk literacy quiz pass rate", 0.52, 0.61, 17],
             ["Web traffic to IPO basics hub", 41000, 58200, 42],
         ]),
    ]
    _xlsx(out("IE_Campaign_Metrics_Q1.xlsx"), sheets)


def build_ie_event_attendance_register():
    sheets = [
        ("Events", "Events held in Q1 FY2026",
         ["Event ID", "Title", "Date", "Venue", "Capacity", "Attended"],
         [
             ["E-2026-001", "Spot the Scam — Town Hall", "2026-02-08", "Centralia Civic Hall", 320, 284],
             ["E-2026-002", "Tertiary Tour — Apex University", "2026-02-20", "Apex University Hall A", 240, 218],
             ["E-2026-003", "Family Planning Workshop A", "2026-02-22", "Asianova Community Centre", 160, 142],
             ["E-2026-004", "Tertiary Tour — Asianova Institute", "2026-03-12", "Asianova Institute Theatre", 220, 198],
             ["E-2026-005", "Family Planning Workshop B", "2026-03-29", "Pacific Community Hall", 180, 168],
             ["E-2026-006", "Sukuk Literacy Forum", "2026-03-22", "Hadar Conference Centre", 140, 122],
             ["E-2026-007", "IPO Basics Lunch & Learn", "2026-03-05", "Caspit Tower Lobby", 80, 76],
         ]),
        ("Attendees sample", "Attendee sample — anonymised",
         ["Attendee ID", "Event ID", "Age band", "City", "First-time?", "Channel"],
         [
             ["A-0001", "E-2026-001", "30-49", "Centralia", "Yes", "Facebook ad"],
             ["A-0002", "E-2026-001", "50+", "Centralia", "No", "Word of mouth"],
             ["A-0003", "E-2026-002", "18-25", "Apex", "Yes", "Campus email"],
             ["A-0004", "E-2026-003", "30-49", "Asianova", "Yes", "WhatsApp invite"],
             ["A-0005", "E-2026-003", "30-49", "Asianova", "Yes", "Friend referral"],
             ["A-0006", "E-2026-004", "18-25", "Asianova", "Yes", "Campus email"],
             ["A-0007", "E-2026-005", "30-49", "Pacific", "No", "Newsletter"],
             ["A-0008", "E-2026-005", "50+", "Pacific", "Yes", "WhatsApp invite"],
             ["A-0009", "E-2026-006", "30-49", "Hadar", "No", "Mosque partner"],
             ["A-0010", "E-2026-006", "50+", "Hadar", "Yes", "Mosque partner"],
             ["A-0011", "E-2026-007", "18-25", "Caspit", "Yes", "LinkedIn ad"],
             ["A-0012", "E-2026-007", "26-29", "Caspit", "Yes", "Office channel"],
         ]),
        ("Feedback summary", "Post-event feedback summary",
         ["Event ID", "Net promoter", "Avg knowledge gain", "Top theme"],
         [
             ["E-2026-001", 41, 1.4, "Scam-route clarity"],
             ["E-2026-002", 56, 1.7, "First-job financial setup"],
             ["E-2026-003", 47, 1.5, "Education planning"],
             ["E-2026-004", 52, 1.6, "Cap-markets basics"],
             ["E-2026-005", 49, 1.4, "Insurance fundamentals"],
             ["E-2026-006", 44, 1.3, "Sukuk vs conventional"],
             ["E-2026-007", 38, 1.2, "IPO process"],
         ]),
    ]
    _xlsx(out("IE_Event_Attendance_Register.xlsx"), sheets)


def build_leg_clause_library_favourable():
    sheets = [
        ("Favourable clauses", "Clause library — Zava-favourable positions",
         ["Clause ID", "Theme", "Position", "Notes"],
         [
             ["CL-01", "Liability cap", "Liability capped at 12 months of fees paid", "Hard cap"],
             ["CL-02", "Indemnity scope", "Mutual indemnity for IP and confidentiality only", "Narrow scope"],
             ["CL-03", "Service levels", "Service credits cap at 30% of monthly fee", "Capped"],
             ["CL-04", "Termination for convenience", "60 days' notice; pro-rated refund", "Operationally clean"],
             ["CL-05", "Audit right", "Annual, with 30 days' notice; once-only per year", "Limited"],
             ["CL-06", "Subcontracting", "Vendor must seek written approval", "Strict"],
             ["CL-07", "Data residency", "Data stored in approved jurisdictions only", "Listed"],
             ["CL-08", "Data return on exit", "Return within 30 days; certified deletion", "Strong"],
             ["CL-09", "Change of control", "Zava may terminate without penalty", "Strong"],
             ["CL-10", "IP ownership of bespoke deliverables", "Vendor assigns to Zava on full payment", "Strong"],
             ["CL-11", "Insurance", "Vendor maintains USD 5m PI + USD 10m PL", "Standard"],
             ["CL-12", "Force majeure", "Excludes vendor's own systems and staffing", "Narrow"],
             ["CL-13", "Governing law", "Singapore", "Default"],
             ["CL-14", "Dispute resolution", "SIAC arbitration, 3 arbitrators", "Default"],
         ]),
        ("Counterparty preferred", "Counterparty-preferred wording — typical asks",
         ["Clause ID", "Counterparty ask", "Our fallback"],
         [
             ["CL-01", "Liability cap at 6 months", "12 months but exclude data-breach events from cap"],
             ["CL-02", "Broader indemnity for negligence", "Carve in only gross negligence + wilful misconduct"],
             ["CL-03", "Service credits as sole remedy", "Service credits + termination right after 3 consecutive misses"],
             ["CL-05", "No audit right", "Annual desktop audit with 60 days' notice"],
             ["CL-06", "Vendor may subcontract freely", "Approval for top tier; notice for others"],
         ]),
        ("Risk score", "Negotiation risk score by clause",
         ["Clause ID", "Risk if conceded", "Drift tolerance"],
         [
             ["CL-01", "High", "Low"],
             ["CL-02", "High", "Low"],
             ["CL-03", "Medium", "Medium"],
             ["CL-04", "Low", "High"],
             ["CL-05", "Low", "Medium"],
             ["CL-06", "Medium", "Medium"],
             ["CL-07", "High", "Low"],
             ["CL-08", "High", "Low"],
             ["CL-09", "Medium", "Medium"],
             ["CL-10", "High", "Low"],
             ["CL-11", "Low", "High"],
             ["CL-12", "Medium", "Medium"],
             ["CL-13", "Low", "High"],
             ["CL-14", "Low", "Medium"],
         ]),
    ]
    _xlsx(out("LEG_Clause_Library_Favourable.xlsx"), sheets)


def build_leg_court_case_precedents():
    sheets = [
        ("Cases", "Court case precedents — vendor disputes",
         ["Case ID", "Year", "Jurisdiction", "Theme", "Outcome (for buyer)"],
         [
             ["P-2018-014", 2018, "Singapore", "Limitation of liability — data breach", "Favourable"],
             ["P-2019-027", 2019, "Singapore", "Service-level credits as sole remedy", "Favourable"],
             ["P-2020-009", 2020, "Hong Kong", "Indemnity scope — IP infringement", "Favourable"],
             ["P-2021-021", 2021, "Singapore", "Termination for convenience refund", "Favourable"],
             ["P-2021-036", 2021, "United Kingdom", "Force majeure — pandemic", "Mixed"],
             ["P-2022-018", 2022, "Singapore", "Data residency obligations", "Favourable"],
             ["P-2023-005", 2023, "Hong Kong", "Subcontracting consent", "Favourable"],
             ["P-2024-011", 2024, "Singapore", "Change of control termination right", "Favourable"],
             ["P-2024-029", 2024, "United Kingdom", "Limitation of liability — gross negligence carve-out", "Favourable"],
             ["P-2025-007", 2025, "Singapore", "Audit right scope", "Favourable"],
         ]),
        ("Holdings", "Key holdings",
         ["Case ID", "Holding"],
         [
             ["P-2018-014", "Liability cap upheld in absence of gross negligence or wilful misconduct"],
             ["P-2019-027", "Service credits not exclusive remedy where vendor breached repeatedly"],
             ["P-2020-009", "Indemnity narrowly construed to IP and confidentiality only"],
             ["P-2021-021", "Pro-rated refund applied on early termination for convenience"],
             ["P-2021-036", "Force majeure does not cover vendor's own staffing decisions"],
             ["P-2022-018", "Data-residency breach itself a material breach"],
             ["P-2023-005", "Subcontracting without consent is breach even if no loss demonstrated"],
             ["P-2024-011", "Change-of-control termination right enforceable without further test"],
             ["P-2024-029", "Gross negligence not subject to cap"],
             ["P-2025-007", "Audit right cannot be limited to vendor-prepared reports only"],
         ]),
        ("Applicability", "Applicability to Zava current cases",
         ["Case ID", "Relevant to", "Notes"],
         [
             ["P-2018-014", "Vendor A IT services renewal", "Cap drafting"],
             ["P-2019-027", "Vendor B managed services dispute", "Repeated SLA misses"],
             ["P-2020-009", "Vendor C software OEM", "IP indemnity scope"],
             ["P-2021-021", "Vendor D ops outsourcing", "Termination refund"],
             ["P-2022-018", "Vendor E data analytics", "Residency"],
             ["P-2023-005", "Vendor F facilities", "Subcontracting"],
             ["P-2024-011", "Vendor G payments", "Change of control"],
             ["P-2024-029", "Vendor H cyber MSSP", "Gross negligence carve-out"],
             ["P-2025-007", "Vendor I print and mail", "Audit rights"],
         ]),
    ]
    _xlsx(out("LEG_Court_Case_Precedents.xlsx"), sheets)


def build_prc_industry_benchmark():
    sheets = [
        ("Benchmark — services", "Benchmark — managed IT services",
         ["Metric", "Industry Q1", "Industry median", "Industry Q3", "Our last contract"],
         [
             ["L1 helpdesk rate USD/hr", 18, 24, 30, 32],
             ["L2 deskside rate USD/hr", 28, 36, 44, 46],
             ["L3 engineer rate USD/hr", 64, 82, 102, 108],
             ["Onsite SLA — same-day %", 90, 95, 98, 92],
             ["Monthly retainer USD per 100 seats", 1800, 2400, 3000, 2800],
             ["Annual escalation %", 2.5, 3.5, 4.5, 5.0],
         ]),
        ("Benchmark — cleaning", "Benchmark — corporate cleaning",
         ["Metric", "Industry Q1", "Industry median", "Industry Q3", "Our last contract"],
         [
             ["Day rate per cleaner USD", 55, 70, 88, 96],
             ["Frequency — daily passes per area", 1, 2, 2, 2],
             ["Consumables included?", "Yes", "Yes", "Yes", "Partial"],
             ["Quality audit cadence — weekly?", "No", "Yes", "Yes", "No"],
             ["Annual escalation %", 2.0, 3.0, 4.0, 4.5],
         ]),
        ("Benchmark — security", "Benchmark — onsite security",
         ["Metric", "Industry Q1", "Industry median", "Industry Q3", "Our last contract"],
         [
             ["Unarmed officer USD/hr", 9, 12, 15, 16],
             ["Supervisor USD/hr", 14, 18, 22, 23],
             ["Patrol vehicle USD/shift", 110, 150, 190, 220],
             ["Annual escalation %", 2.5, 3.0, 3.5, 3.5],
         ]),
    ]
    _xlsx(out("PRC_Industry_Benchmark.xlsx"), sheets)


def build_prc_past_contracts():
    sheets = [
        ("Past awards", "Past awards — last 5 cycles",
         ["Cycle", "Service", "Winner", "Contract USD m", "Notes"],
         [
             ["2014-2017", "Managed IT services", "Vendor A", 22.4, "Renewed once"],
             ["2017-2020", "Managed IT services", "Vendor A", 26.8, "Renewed"],
             ["2020-2023", "Managed IT services", "Vendor B", 29.2, "Switched"],
             ["2023-2026", "Managed IT services", "Vendor B", 32.4, "Current"],
             ["2014-2017", "Corporate cleaning", "Vendor C", 6.4, ""],
             ["2017-2020", "Corporate cleaning", "Vendor D", 7.8, "Switched"],
             ["2020-2023", "Corporate cleaning", "Vendor D", 8.9, "Renewed"],
             ["2023-2026", "Corporate cleaning", "Vendor D", 9.6, "Current"],
             ["2014-2017", "Onsite security", "Vendor E", 5.2, ""],
             ["2017-2020", "Onsite security", "Vendor E", 5.8, "Renewed"],
             ["2020-2023", "Onsite security", "Vendor F", 6.4, "Switched"],
             ["2023-2026", "Onsite security", "Vendor F", 7.2, "Current"],
         ]),
        ("Performance", "Vendor performance summary",
         ["Vendor", "Service", "Avg SLA met %", "Complaints per year", "Renewed?"],
         [
             ["Vendor A", "Managed IT services", 94, 14, "Yes"],
             ["Vendor B", "Managed IT services", 91, 22, "Open"],
             ["Vendor C", "Corporate cleaning", 88, 18, "No"],
             ["Vendor D", "Corporate cleaning", 92, 12, "Open"],
             ["Vendor E", "Onsite security", 95, 8, "No"],
             ["Vendor F", "Onsite security", 93, 10, "Open"],
         ]),
        ("Lessons learned", "Lessons learned by service",
         ["Service", "Lesson"],
         [
             ["Managed IT services", "Locking in 5% annual escalator left no room to absorb market drops"],
             ["Managed IT services", "L3 engineer rate above market — challenge in next round"],
             ["Corporate cleaning", "Consumables-included term reduced petty disputes"],
             ["Corporate cleaning", "Quality audit cadence should move from monthly to weekly"],
             ["Onsite security", "Patrol vehicle cost rose faster than headcount cost"],
             ["Onsite security", "Bundle uniformed + control-room into one lot to reduce overhead"],
         ]),
    ]
    _xlsx(out("PRC_Past_Contracts.xlsx"), sheets)


def build_prc_vendor_responses():
    sheets = [
        ("Vendor responses summary", "Vendor responses — RFP cycle 2026",
         ["Vendor", "Service", "Bid price USD m", "SLA commitment", "Escalation %", "Risk notes"],
         [
             ["Apex Specialty Services", "Managed IT services", 31.2, "Same-day 96%", 3.5, "Solid"],
             ["Pacific MSP", "Managed IT services", 33.8, "Same-day 95%", 4.0, "Sub-contracts L1"],
             ["Asianova IT Partners", "Managed IT services", 28.6, "Same-day 92%", 4.5, "Thin L3 bench"],
             ["Centralia Tech Services", "Managed IT services", 34.2, "Same-day 97%", 3.0, "Premium quote"],
             ["Apex Cleaning Co", "Corporate cleaning", 9.4, "Weekly audit", 3.5, "Solid"],
             ["Pacific Facilities", "Corporate cleaning", 8.6, "Monthly audit", 4.0, "Audit cadence light"],
             ["Asianova Cleaning", "Corporate cleaning", 10.2, "Weekly audit", 3.0, "Premium quote"],
             ["Apex Guards", "Onsite security", 6.8, "Patrol every 30 min", 3.0, "Solid"],
             ["Pacific Security", "Onsite security", 7.4, "Patrol every 30 min", 3.5, "Higher escalation"],
             ["Asianova Security", "Onsite security", 6.4, "Patrol every 45 min", 3.5, "Patrol cadence weaker"],
         ]),
        ("Score sheet", "Score sheet (50 commercial, 30 technical, 20 ESG)",
         ["Vendor", "Commercial", "Technical", "ESG", "Total"],
         [
             ["Apex Specialty Services", 42, 27, 18, 87],
             ["Pacific MSP", 38, 25, 17, 80],
             ["Asianova IT Partners", 44, 22, 16, 82],
             ["Centralia Tech Services", 36, 28, 19, 83],
             ["Apex Cleaning Co", 41, 26, 18, 85],
             ["Pacific Facilities", 43, 22, 16, 81],
             ["Asianova Cleaning", 38, 28, 19, 85],
             ["Apex Guards", 44, 26, 17, 87],
             ["Pacific Security", 40, 25, 17, 82],
             ["Asianova Security", 45, 22, 15, 82],
         ]),
        ("Clarifications", "Clarifications outstanding",
         ["Vendor", "Question", "Status"],
         [
             ["Apex Specialty Services", "Confirm L3 engineer location split", "Awaiting"],
             ["Pacific MSP", "Detail subcontractor list", "Awaiting"],
             ["Asianova IT Partners", "Provide L3 bench CVs", "Awaiting"],
             ["Centralia Tech Services", "Substantiate same-day SLA in regional sites", "Awaiting"],
             ["Apex Cleaning Co", "Audit methodology document", "Received"],
             ["Pacific Facilities", "Escalation calculation worked example", "Awaiting"],
             ["Asianova Cleaning", "Consumables list and brands", "Received"],
             ["Apex Guards", "Officer training records sample", "Received"],
             ["Pacific Security", "Confirm vehicle fleet age", "Awaiting"],
             ["Asianova Security", "Confirm patrol cadence improvement path", "Awaiting"],
         ]),
    ]
    _xlsx(out("PRC_Vendor_Responses.xlsx"), sheets)


BUILDERS = [
    build_hr_outsourcing_and_contract_staff,
    build_hr_skill_gap_survey_2025,
    build_hr_workforce_fy2026,
    build_ie_budget_vs_actual,
    build_ie_campaign_metrics_q1,
    build_ie_event_attendance_register,
    build_leg_clause_library_favourable,
    build_leg_court_case_precedents,
    build_prc_industry_benchmark,
    build_prc_past_contracts,
    build_prc_vendor_responses,
]


if __name__ == "__main__":
    for fn in BUILDERS:
        fn()
        print("Wrote:", fn.__name__)
