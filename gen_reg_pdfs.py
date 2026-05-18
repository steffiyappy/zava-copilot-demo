"""Builders for the 5 regulator PDF stubs.

Run via gen_regulator_files.py. Each function writes one PDF into files/.
"""
from gen_reg_helpers import _pdf, out


def build_anti_scam_complaint_sample():
    title = "Investor Complaint – Suspected Investment Scam (Sample Intake)"
    sections = [
        ("h1", title),
        ("p", "Reference: ZAVA-COMP-2026-0418  •  Lodged via: Online complaint form  •  Channel: Email + phone follow-up"),
        ("h2", "1. Complainant details"),
        ("bullets", [
            "Name: H. Caspit (placeholder; real names redacted under PDPA)",
            "Resident of: Centralia, ASEAN region",
            "Preferred language: English",
            "Best contact: 09:00–18:00 local time, email or mobile",
        ]),
        ("h2", "2. Summary of complaint"),
        ("p", "Complainant alleges that an unlicensed party operating under the brand name 'Zenith Forex AI' solicited an investment of USD 12,400 through a private Telegram group. Returns of '8% per month, capital-protected' were promised. After two months, withdrawals were blocked and the operator stopped responding."),
        ("h2", "3. Timeline of events"),
        ("bullets", [
            "2026-01-12 — First contact via Facebook ad linking to a WhatsApp number.",
            "2026-01-19 — Onboarding call; complainant asked to download a sideloaded mobile app.",
            "2026-01-22 — First deposit of USD 5,000 wired to a payment-aggregator account.",
            "2026-02-08 — Top-up of USD 7,400 after seeing fabricated portfolio screenshots.",
            "2026-03-15 — Withdrawal request rejected; account 'locked pending verification fee'.",
            "2026-04-01 — Operator stops responding; group closed.",
        ]),
        ("h2", "4. Evidence attached"),
        ("bullets", [
            "Screenshots of WhatsApp / Telegram exchanges (12 images).",
            "Bank wire confirmations (2 PDF receipts).",
            "Marketing video (MP4, 47 seconds).",
            "Copy of forged 'licence certificate' bearing what appears to be a recycled regulator seal.",
        ]),
        ("h2", "5. Requested outcome"),
        ("p", "Complainant requests (a) refund of USD 12,400, (b) public warning naming the operator, and (c) escalation to the cyber crime unit. Complainant is willing to be interviewed and to provide bank records under subpoena."),
        ("h2", "6. Internal triage notes (for case officer use)"),
        ("p", "Apparent indicators of unlicensed scheme: guaranteed returns, sideloaded app, unverifiable licence, payment to third-party aggregator, social-engineering urgency. Recommend Tier-A red-flag classification and routing to Enforcement within 48 hours."),
    ]
    _pdf(out("REG_AntiScam_Complaint_Sample.pdf"), title, sections)


def build_imd_sfo_application_sample():
    title = "Single Family Office (SFO) Licence Application – Sample Submission"
    sections = [
        ("h1", title),
        ("p", "Applicant: Asianova Caspit Holdings Pte Ltd  •  Application ID: IMD-SFO-2026-0027  •  Submission date: 2026-04-22"),
        ("h2", "1. Applicant overview"),
        ("p", "Applicant is the family investment vehicle for the Caspit family (Hadar Caspit and connected persons). Total family net worth disclosed at USD 412 million across operating businesses, listed equities, private equity, real estate, and cash. The proposed SFO will manage approximately USD 180 million of investable assets."),
        ("h2", "2. Source-of-wealth declaration"),
        ("bullets", [
            "Operating businesses (Caspit Industrial Holdings): ~46% of net worth, 3 decades of audited financials available.",
            "Listed equity portfolio (Public Bank, regional REITs): ~22%.",
            "Private equity co-investments (4 ASEAN funds): ~14%.",
            "Real estate (residential and commercial, 6 jurisdictions): ~12%.",
            "Cash and equivalents: ~6%.",
        ]),
        ("h2", "3. Investment policy statement (summary)"),
        ("p", "60% growth (listed equities, PE, hedge), 25% income (fixed income, private credit), 10% real assets, 5% cash. Maximum single-position 8%. ESG screen excludes tobacco, controversial weapons, and thermal coal. Currency hedge policy: 70% USD core, balance unhedged."),
        ("h2", "4. Governance and key persons"),
        ("bullets", [
            "Chief Investment Officer (proposed): Sasha Ouellet — 18 years buy-side experience.",
            "Chief Compliance Officer (proposed): Mod Admin — formerly Head of Compliance at a mid-tier asset manager.",
            "Board: 4 family members + 2 independent advisers.",
            "All key persons cleared for fit-and-proper screening (CVs and references attached).",
        ]),
        ("h2", "5. Operational controls"),
        ("p", "Custody with a Tier-1 bank in the home jurisdiction. NAV struck monthly. Trades executed only via licensed brokers. AML/CFT programme documented and refreshed annually. Independent audit appointed."),
        ("h2", "6. Regulator review notes (blank for internal use)"),
        ("p", "[For desk officer]"),
    ]
    _pdf(out("REG_IMD_SFO_Application_Sample.pdf"), title, sections)


def build_imd_vcpe_application_sample():
    title = "Venture Capital / Private Equity Fund Manager – Sample Application"
    sections = [
        ("h1", title),
        ("p", "Applicant: Pacific Frontier Capital Partners  •  Application ID: IMD-VCPE-2026-0014  •  Submission date: 2026-04-19"),
        ("h2", "1. Manager overview"),
        ("p", "First-time institutional fund manager raising a USD 75 million ASEAN growth-stage fund (Pacific Frontier Growth Fund I). Strategy: Series B/C in fintech, healthtech, and climate tech across Indonesia, the Philippines, Vietnam, and Malaysia. Target IRR: 22% net of fees."),
        ("h2", "2. Team and track record"),
        ("bullets", [
            "Managing Partner: Daichi Maruyama — 14 years VC, ex-corporate VC arm of a regional bank.",
            "Partner: Hadar Caspit — 11 years growth equity, ex-Tier-2 global PE firm.",
            "Operating partners: 2 retained on advisory basis (fintech regulatory, climate tech go-to-market).",
            "Aggregate prior deals: 27 investments, 6 realised exits, weighted gross MOIC 2.4x.",
        ]),
        ("h2", "3. Fund structure"),
        ("p", "Closed-end limited partnership, 10-year life with two 1-year extensions. Management fee 2.0% on commitments during investment period, then on invested capital. Carry 20% over 8% hurdle, European waterfall. GP commitment 2.5%."),
        ("h2", "4. Compliance and operational readiness"),
        ("bullets", [
            "Administrator and depositary: Tier-1 service provider engaged.",
            "AML/CFT, sanctions, and PEP screening tooling in place.",
            "ESG framework aligned to IFC Performance Standards.",
            "Conflict-of-interest policy and personal-account-dealing policy documented.",
        ]),
        ("h2", "5. Risk disclosures"),
        ("p", "Concentration risk (first fund, single strategy), liquidity risk (10-year lock), foreign exchange risk (multi-jurisdiction), regulatory risk (heterogeneous ASEAN regimes). Mitigations documented in section 7 of full application pack."),
    ]
    _pdf(out("REG_IMD_VCPE_Application_Sample.pdf"), title, sections)


def build_ipo_prospectus_sample():
    title = "Zava Conglomerate Industrials Bhd — Draft IPO Prospectus (Sample)"
    sections = [
        ("h1", title),
        ("p", "Issuer: Zava Conglomerate Industrials Bhd  •  Issue size: indicative USD 280–320 million  •  Lead managers: Apex Securities, Asianova Capital  •  Listing venue: ASEAN Stock Exchange"),
        ("h2", "1. Offering summary"),
        ("bullets", [
            "Primary issuance: ~135 million new shares at indicative range USD 1.95–2.20.",
            "Secondary offering: ~45 million shares from existing shareholders.",
            "Greenshoe: 15% over-allotment option.",
            "Lock-up: 180 days for cornerstone investors; 360 days for promoter shareholders.",
        ]),
        ("h2", "2. Business overview"),
        ("p", "Zava Conglomerate Industrials operates across (i) industrial manufacturing, (ii) palm-oil and downstream specialties, (iii) property development, and (iv) financial services. FY2025 revenue USD 1.84 billion, EBITDA USD 312 million, PATAMI USD 178 million."),
        ("h2", "3. Use of proceeds"),
        ("bullets", [
            "USD 110 million — capacity expansion at the Centralia downstream complex.",
            "USD 80 million — repayment of existing bank facilities.",
            "USD 60 million — strategic acquisitions in adjacent specialty-chemicals segments.",
            "USD 30 million — working capital and general corporate purposes.",
        ]),
        ("h2", "4. Risk factors (top 6)"),
        ("bullets", [
            "Commodity price volatility (crude palm oil, naphtha).",
            "FX exposure (revenue split USD/regional currencies).",
            "Regulatory change in environmental and labour standards.",
            "Cyclicality of property development earnings.",
            "Customer concentration in the top-10 industrial offtake list.",
            "Execution risk on the Centralia capacity expansion.",
        ]),
        ("h2", "5. Financial summary (FY2023–FY2025)"),
        ("p", "Revenue CAGR 11.8%; EBITDA margin expanded from 15.2% to 17.0%; net debt to EBITDA reduced from 2.6x to 1.9x; ROIC improved from 9.1% to 11.4%. Full audited financials in Section 9 of the full prospectus."),
        ("h2", "6. Dividend policy"),
        ("p", "Post-listing payout ratio target of 35–45% of PATAMI, subject to maintaining net debt to EBITDA below 2.5x and meeting capex commitments."),
        ("h2", "7. Cornerstone investors (indicative)"),
        ("p", "5 institutional cornerstones for ~38% of the offering, including 2 sovereign wealth funds, 2 regional pension funds, and 1 strategic industrial partner. Final allocations subject to regulator approval."),
    ]
    _pdf(out("REG_IPO_Prospectus_Sample.pdf"), title, sections)


def build_private_credit_application_sample():
    title = "Private Credit Fund Manager — Sample Licence Application"
    sections = [
        ("h1", title),
        ("p", "Applicant: Apex Mezzanine Partners Sdn Bhd  •  Application ID: IMD-PC-2026-0009  •  Submission date: 2026-04-25"),
        ("h2", "1. Strategy"),
        ("p", "Senior secured and unitranche direct lending to ASEAN mid-market sponsors and family-owned businesses. Ticket size USD 10–35 million. Target gross IRR 13–15%, fund-level leverage capped at 1.0x. Sectoral focus: industrials, healthcare services, business services."),
        ("h2", "2. Target investor base"),
        ("bullets", [
            "Pension funds and insurance balance sheets — 55% of target raise.",
            "Sovereign wealth and development finance — 20%.",
            "Family offices and HNWI feeders — 20%.",
            "GP and affiliated commitments — 5%.",
        ]),
        ("h2", "3. Risk framework"),
        ("p", "Single-borrower cap 12% of commitments; sector cap 25%; covenant package required on every facility (maintenance financial covenants, info undertakings, change-of-control); independent valuation quarterly."),
        ("h2", "4. Key persons"),
        ("bullets", [
            "Head of Investments: Mod Admin — 16 years leveraged finance.",
            "Head of Credit: Sasha Ouellet — 13 years credit underwriting.",
            "Head of Compliance: Hadar Caspit — 19 years compliance and risk.",
            "Independent Risk Committee: 2 external members appointed.",
        ]),
        ("h2", "5. Conflict management"),
        ("p", "Cross-fund conflicts (where the same sponsor is in multiple vintages) escalated to the Independent Risk Committee. LP advisory committee consent required for connected-party transactions. Allocation policy documented and refreshed annually."),
    ]
    _pdf(out("REG_PrivateCredit_Application_Sample.pdf"), title, sections)


BUILDERS = [
    build_anti_scam_complaint_sample,
    build_imd_sfo_application_sample,
    build_imd_vcpe_application_sample,
    build_ipo_prospectus_sample,
    build_private_credit_application_sample,
]


if __name__ == "__main__":
    for fn in BUILDERS:
        fn()
        print("Wrote:", fn.__name__)
