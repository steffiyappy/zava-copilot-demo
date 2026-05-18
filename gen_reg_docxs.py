"""Builders for the 10 regulator/cross-dept DOCX stubs."""
from gen_reg_helpers import _docx, out


def build_aud_auditee_walkthrough():
    title = "Internal Audit — Auditee Walkthrough Pack"
    sections = [
        ("h1", title),
        ("p", "Owner: Group Internal Audit (Daichi Maruyama)  •  Cycle: FY2026 Q2 thematic — Vendor lifecycle and access management"),
        ("h2", "1. Purpose and scope"),
        ("p", "This walkthrough pack supports the FY2026 Q2 thematic audit on vendor lifecycle, contracting controls, and privileged-access management. It is the standard primer issued to first-line and second-line auditees ahead of fieldwork."),
        ("h2", "2. Scope boundaries"),
        ("bullets", [
            "In scope: Group Procurement, IT Operations, Information Security, Vendor Risk, three business-unit finance teams.",
            "In scope: vendors onboarded between 2024-01-01 and 2026-03-31.",
            "Out of scope: pure consumables (sub USD 5,000) and intra-group transactions.",
            "Out of scope: SAP and Workday access (covered by the Q4 platform audit).",
        ]),
        ("h2", "3. Walkthrough flow"),
        ("numbered", [
            "Process owner briefs Internal Audit on end-to-end vendor lifecycle.",
            "Sample of 12 vendor onboardings reviewed live with the system in screen-share.",
            "Joiner-mover-leaver (JML) flow walked through for the three impacted platforms.",
            "Exception logs (rejected onboardings, revoked accesses) reviewed.",
            "Open issues from the prior audit cycle (FY2025 Q3) revisited.",
        ]),
        ("h2", "4. Documentation requested"),
        ("bullets", [
            "Standard operating procedures (current version + change log for past 24 months).",
            "Vendor master extract with onboarding date, risk tier, status, and last review date.",
            "Privileged-access role catalogue and approval workflow screenshots.",
            "Recent control self-assessment results.",
            "Issue register (open and closed in the last 12 months).",
        ]),
        ("h2", "5. Auditee responsibilities"),
        ("p", "Nominate a single point of contact; provide read-only audit access to the relevant systems within 5 business days of fieldwork start; flag any document requests that conflict with confidentiality undertakings so that Internal Audit can co-design an alternative evidence path."),
        ("h2", "6. Communication protocol"),
        ("bullets", [
            "Daily 20-minute stand-up during fieldwork weeks (Tuesday and Thursday at 09:00).",
            "Issues raised in writing within 48 hours of identification.",
            "Auditee given 5 business days to respond to draft findings before reporting.",
        ]),
    ]
    _docx(out("AUD_Auditee_Walkthrough.docx"), title, sections)


def build_hr_strategic_priorities_2030():
    title = "Group Human Resources — Strategic Priorities to 2030"
    sections = [
        ("h1", title),
        ("p", "Owner: Group Chief Human Resources Office (Sasha Ouellet)  •  Status: Endorsed by Group ExCo 2026-03-14"),
        ("h2", "1. Context"),
        ("p", "Zava Conglomerate is on a five-year transformation arc to FY2030. The workforce that ran the FY2020–FY2025 cycle (heavy on transactional roles, regional silos, manual data work) is not the workforce that will deliver the FY2025–FY2030 strategy (digital-first operations, AI-augmented decision-making, regulated-product growth in financial services, downstream specialty-chemicals expansion). This document sets the HR strategic priorities to bridge that gap."),
        ("h2", "2. Five strategic priorities"),
        ("numbered", [
            "Critical-skill build-out — data, AI, financial-services regulation, downstream-specialty engineering, ESG assurance.",
            "Leadership pipeline depth — every Group-level role 2-deep within 24 months.",
            "Culture shift — from compliance-and-control to outcomes-and-ownership.",
            "Workforce mix — reduce contractor reliance in mission-critical roles to under 20%.",
            "Geographic redistribution — grow Centralia and Vietnam hubs; rebalance Metro headcount.",
        ]),
        ("h2", "3. Headcount envelope"),
        ("p", "FY2026 envelope is 8,420 FTE (-2% vs FY2025). The reduction is concentrated in administrative back-office, with selective net growth in regulated financial services (+120 FTE) and downstream specialty (+85 FTE). All movements pass through the Group HR Capacity Council."),
        ("h2", "4. Operating principles"),
        ("bullets", [
            "Buy-borrow-build — default to building internal capability; borrow only where speed-to-market demands it.",
            "Internal-first hiring for any role above grade M3.",
            "Mobility — minimum 8% of grade M2+ population should rotate per year.",
            "Pay-for-skill, not pay-for-tenure — annual market calibration on the priority skills.",
        ]),
        ("h2", "5. Measurement"),
        ("bullets", [
            "Critical-skill coverage ratio (target ≥ 0.95 by FY2028).",
            "Voluntary attrition in regretted-loss population (target < 6% rolling 12 months).",
            "Internal-fill rate for grade M3+ roles (target ≥ 65%).",
            "Engagement composite score (target ≥ 78).",
            "Diversity-of-talent metrics (gender, age, nationality) at every promotion review.",
        ]),
        ("h2", "6. Risks"),
        ("p", "Wage inflation in priority skills, regulatory uncertainty in financial services, attrition of high-performers to fintechs and regional competitors, and execution risk on the contractor-conversion programme. Each risk owned and reported quarterly."),
    ]
    _docx(out("HR_Strategic_Priorities_2030.docx"), title, sections)


def build_ie_bilingual_content_library():
    title = "Investor Education — Bilingual Content Library Index"
    sections = [
        ("h1", title),
        ("p", "Owner: Group Investor Education (Mod Admin)  •  Languages covered: English + Bahasa Malaysia + Bahasa Indonesia"),
        ("h2", "1. Purpose"),
        ("p", "This index lists every approved investor-education asset across the group, the audience it targets, the language variants available, the last review date, and the assigned subject-matter expert. It is the source of truth used by the Marketing, Compliance, and Investor Relations teams when planning campaigns."),
        ("h2", "2. Content pillars"),
        ("numbered", [
            "Investor protection basics (recognising scams, verifying licences, due diligence).",
            "Public markets literacy (how an IPO works, secondary trading, dividends, rights issues).",
            "Private markets literacy (PE, VC, private credit, single family offices).",
            "Sustainable and responsible investing (ESG ratings, green sukuk, climate-aligned funds).",
            "Personal finance hygiene (budgeting, emergency funds, retirement planning).",
        ]),
        ("h2", "3. Format inventory"),
        ("bullets", [
            "Long-form explainers (PDF, ~12 pages each).",
            "Short-form social cards (Instagram + TikTok + LinkedIn versions).",
            "Video shorts (60–90 seconds, captioned).",
            "Webinar replays with timestamped chapters.",
            "Print-ready posters for partner branch lobbies.",
        ]),
        ("h2", "4. Sample asset map (excerpt)"),
        ("table", [
            ["Asset ID", "Title", "Format", "Languages", "SME owner"],
            ["IE-001", "How to verify an investment licence", "PDF + 3 social cards", "EN / BM / ID", "Compliance"],
            ["IE-014", "What is an IPO?", "Video short + explainer PDF", "EN / BM / ID", "Capital Markets"],
            ["IE-027", "Private credit basics for HNWIs", "Webinar + slide pack", "EN / BM", "Wealth"],
            ["IE-035", "Green sukuk explained", "Long-form PDF", "EN / BM / ID", "ESG"],
            ["IE-049", "Spotting Telegram investment scams", "3 social cards + 1 video", "EN / BM / ID", "Enforcement"],
        ]),
        ("h2", "5. Governance"),
        ("p", "Every asset reviewed annually by the assigned SME and the Compliance counter-signatory. Assets older than 24 months without review are auto-archived and removed from the library."),
    ]
    _docx(out("IE_Bilingual_Content_Library.docx"), title, sections)


def build_leg_standard_terms_schedule():
    title = "Group Legal — Standard Terms Schedule (Vendor Contracts)"
    sections = [
        ("h1", title),
        ("p", "Owner: Group Legal (Hadar Caspit, Group GC)  •  Version: 4.2  •  Last reviewed: 2026-02-10"),
        ("h2", "1. Purpose"),
        ("p", "This schedule consolidates Zava Conglomerate's standard vendor-contract terms. It is mandatory for any contract above USD 250,000 annual value or any contract that touches personal data, regulated services, or safety-critical operations."),
        ("h2", "2. Term and termination"),
        ("bullets", [
            "Default term: 24 months with two 12-month extension options exercisable by Zava only.",
            "Termination for convenience: 60 days' notice.",
            "Termination for cause: 30 days' cure period, then immediate.",
            "Termination for insolvency: immediate, on written notice.",
            "Post-termination transition assistance: up to 6 months at then-current rates.",
        ]),
        ("h2", "3. Pricing and payment"),
        ("bullets", [
            "All pricing fixed in USD or local currency at Zava's election.",
            "Annual price adjustments capped at the lower of CPI or 4%.",
            "Standard payment terms: 60 days from valid invoice receipt.",
            "Volume rebates documented in the commercial schedule.",
        ]),
        ("h2", "4. Liability"),
        ("p", "Total aggregate liability capped at the greater of (a) 200% of fees paid in the 12 months preceding the claim or (b) the value of the master order form. Unlimited liability for breach of confidentiality, IP infringement, data protection, fraud, and personal injury."),
        ("h2", "5. Data protection and information security"),
        ("bullets", [
            "Compliance with Zava's Information Security Schedule (Annex A).",
            "Sub-processor approval required in writing.",
            "Data-breach notification within 24 hours.",
            "Right to audit on 10 business days' notice.",
            "Return or certified destruction of data on termination.",
        ]),
        ("h2", "6. Boilerplate"),
        ("p", "Confidentiality 5 years post-termination. IP — Zava-developed materials remain Zava's; vendor pre-existing IP licensed back. Anti-bribery and sanctions warranties. Governing law: Centralia, ASEAN. Dispute resolution: arbitration under the Centralia International Arbitration Centre rules, seat Centralia, English language, 3-arbitrator panel for disputes above USD 5 million."),
    ]
    _docx(out("LEG_Standard_Terms_Schedule.docx"), title, sections)


def build_leg_vendor_contract_draft():
    title = "Vendor Contract Draft — Apex Specialty Services (Procurement Lot 14)"
    sections = [
        ("h1", title),
        ("p", "Counterparty: Apex Specialty Services Sdn Bhd  •  Lot: Centralia Site Industrial Cleaning  •  Annual value: USD 1.62 million  •  Drafted by: Procurement & Legal — review cycle 3"),
        ("h2", "1. Background"),
        ("p", "Apex Specialty Services (Apex) will provide industrial cleaning, hazardous-waste handling preparation, and confined-space cleaning services at the Centralia downstream complex for a 24-month term. This draft is the third revision after counterparty mark-up."),
        ("h2", "2. Scope of services"),
        ("bullets", [
            "Routine industrial cleaning (daily and shift-based).",
            "Hazardous-waste preparation for collection by the licensed waste contractor.",
            "Confined-space cleaning per the site permit-to-work system.",
            "Emergency-response cleaning (24/7 callout).",
            "Provision of trained, certified, and equipped personnel.",
        ]),
        ("h2", "3. Negotiation status (cross-reference to clause library)"),
        ("table", [
            ["Clause", "Zava standard", "Apex counter", "Status"],
            ["Liability cap", "200% of fees / unlimited carve-outs", "100% of fees / fewer carve-outs", "Open — Legal escalation"],
            ["Indemnity scope", "Broad", "Mutual and narrowed", "Open"],
            ["Payment terms", "60 days", "30 days", "Open — Finance escalation"],
            ["Audit rights", "10 business days' notice", "20 business days' notice", "Compromise: 15 days"],
            ["Termination for convenience", "60 days", "120 days", "Compromise: 90 days"],
            ["Sub-contracting", "Prior written consent", "Notification only", "Open — Procurement escalation"],
            ["Data protection schedule", "Annex A mandatory", "Accepted", "Closed"],
            ["Anti-bribery warranty", "Standard", "Accepted", "Closed"],
        ]),
        ("h2", "4. Open commercial items"),
        ("bullets", [
            "Volume-rebate tiers above USD 1.8 million annual run-rate.",
            "Indexation mechanism for fuel surcharge.",
            "Service-credit regime for missed SLAs.",
        ]),
        ("h2", "5. Internal sign-off path"),
        ("p", "Once open clauses are resolved, the draft requires sign-off from (a) Group Procurement (Hadar Caspit), (b) Group Legal (Mod Admin), (c) Site Operations (Daichi Maruyama), and (d) Group Finance for the payment-term variance."),
    ]
    _docx(out("LEG_Vendor_Contract_Draft.docx"), title, sections)


def build_prc_rfp_requirements():
    title = "RFP — Centralia Industrial Cleaning Services (Requirements Document)"
    sections = [
        ("h1", title),
        ("p", "Owner: Group Procurement (Hadar Caspit)  •  Lot: PRC-2026-LOT-14  •  Issue date: 2026-03-04  •  Submission deadline: 2026-04-15"),
        ("h2", "1. Background"),
        ("p", "Zava Conglomerate is re-tendering its industrial-cleaning services contract for the Centralia downstream complex. The current contract expires 2026-09-30. This RFP seeks to award a 24-month contract to a single primary supplier with a backup-supplier panel."),
        ("h2", "2. Scope of services required"),
        ("numbered", [
            "Routine industrial cleaning across 14 process units and 3 utility blocks.",
            "Preparation of hazardous waste for collection by the licensed waste contractor.",
            "Confined-space cleaning under Zava's permit-to-work regime.",
            "Emergency-response cleaning, 24/7 callout, with maximum response time of 90 minutes during operating hours.",
            "Equipment and consumables provision.",
            "Trained-and-certified personnel including confined-space and breathing-apparatus credentials.",
        ]),
        ("h2", "3. Mandatory requirements (pass/fail)"),
        ("bullets", [
            "Three years of audited financial statements demonstrating financial stability.",
            "Demonstrated industrial-cleaning experience at a comparable hazardous-process site.",
            "ISO 9001, ISO 14001, and ISO 45001 certified management systems.",
            "Zero fatalities in the past 36 months at any operated site.",
            "Insurance certificates at the levels specified in Annex B.",
        ]),
        ("h2", "4. Evaluation criteria"),
        ("table", [
            ["Criterion", "Weighting", "Evaluator"],
            ["Commercial (total cost of ownership over 24 months)", "40%", "Procurement"],
            ["Technical capability and methodology", "25%", "Site Operations"],
            ["HSE record and management system", "20%", "Group HSE"],
            ["Mobilisation plan and transition risk", "10%", "Site Operations"],
            ["ESG and local content", "5%", "Sustainability"],
        ]),
        ("h2", "5. Required vendor submission format"),
        ("bullets", [
            "Section A — Commercial proposal (Annex C template).",
            "Section B — Technical proposal narrative (max 40 pages).",
            "Section C — HSE pack (policies, statistics, certifications).",
            "Section D — Mobilisation plan with Gantt chart.",
            "Section E — Past contracts and references (minimum 3, last 36 months).",
            "Section F — ESG declarations.",
        ]),
        ("h2", "6. Contact for clarifications"),
        ("p", "All clarification questions must be submitted via the procurement portal by 2026-03-25. Responses will be shared with all bidders. Direct contact with site operations is prohibited during the bid window."),
    ]
    _docx(out("PRC_RFP_Requirements.docx"), title, sections)


def build_reg_anti_scam_email_reply_library():
    title = "Anti-Scam Investor Complaints — Standard Reply Library"
    sections = [
        ("h1", title),
        ("p", "Owner: Investor Affairs Desk (Sasha Ouellet)  •  Last reviewed: 2026-04-02  •  Approved by: Group Compliance"),
        ("h2", "1. Purpose"),
        ("p", "This document is the approved library of reply templates for investor complaint correspondence relating to suspected unlicensed investment activity. Each template is written for empathy and clarity, accurate on regulatory boundaries, and free of premature legal conclusions."),
        ("h2", "2. Template A — Acknowledgement of receipt (within 24 hours)"),
        ("p", "\"Dear [Name], thank you for reaching out. We confirm receipt of your complaint reference [Ref]. We treat reports of suspected unlicensed activity with the highest priority. A case officer will be in touch within five business days to gather any additional details. In the meantime, please do not engage further with the party concerned or share any further funds or credentials. If you believe a crime is in progress, please contact your local police hotline.\""),
        ("h2", "3. Template B — Request for additional evidence"),
        ("p", "\"Dear [Name], to allow us to act on your complaint we kindly request the following items: [list of items]. If you can provide these by [date], it would help us speed up the review. Please send them via [secure channel]. We will keep your information confidential to the maximum extent allowed by law.\""),
        ("h2", "4. Template C — Confirmation of investigation in progress"),
        ("p", "\"Dear [Name], we are writing to confirm that the matter you reported is under investigation. We are not able to share investigative details, but we will update you when the case status changes. Please continue to preserve any evidence in your possession.\""),
        ("h2", "5. Template D — Closure where action taken"),
        ("p", "\"Dear [Name], we are writing to inform you that the matter you reported has now been closed at our end. [Brief description of the regulatory action taken, where public.] We appreciate the public interest you served by bringing this to our attention.\""),
        ("h2", "6. Template E — Closure where matter outside remit"),
        ("p", "\"Dear [Name], we have reviewed your report carefully. The matter falls outside our regulatory remit. We have, with your earlier permission, forwarded the report to [agency name], which is the appropriate authority. You may wish to follow up with them directly.\""),
        ("h2", "7. Drafting guardrails"),
        ("bullets", [
            "Do not name suspected parties until enforcement action is public.",
            "Do not promise refunds or specific outcomes.",
            "Do not characterise the operator's conduct as illegal until adjudicated.",
            "Always include the complaint reference and the case-officer point of contact.",
        ]),
    ]
    _docx(out("REG_AntiScam_Email_Reply_Library.docx"), title, sections)


def build_reg_equities_submission_guidelines():
    title = "Equities Issuer Submission Guidelines (Zava Internal Companion)"
    sections = [
        ("h1", title),
        ("p", "Owner: Group Corporate Secretarial & Investor Relations (Daichi Maruyama)  •  Status: Internal companion to the listing-venue rules — does not override them"),
        ("h2", "1. Purpose"),
        ("p", "Zava Conglomerate and its listed subsidiaries make frequent equity-related submissions to the listing venue. This companion document standardises Zava's internal preparation steps. It is not a substitute for the official listing-venue rules."),
        ("h2", "2. Common submission types"),
        ("bullets", [
            "Quarterly financial results.",
            "Material announcements (M&A, asset disposals, major contracts, regulatory action).",
            "Annual report and annual general meeting documentation.",
            "Rights issue, private placement, and bond issuance documents.",
            "Director and substantial-shareholder changes.",
            "Related-party transaction disclosures.",
        ]),
        ("h2", "3. Internal preparation checklist (every submission)"),
        ("numbered", [
            "Confirm materiality with Group Legal.",
            "Cross-check numbers against Group Finance's locked figures.",
            "Apply the standard disclosure template.",
            "Run the language consistency check (EN + BM + ID).",
            "Obtain sign-off from the Disclosure Committee (Chair + 2 members minimum).",
            "Submit through the official portal; archive in the submissions log.",
        ]),
        ("h2", "4. Timing rules of thumb"),
        ("bullets", [
            "Material announcements: as soon as practicable; never delayed for non-trading-day reasons alone.",
            "Quarterly results: target submission within 35 calendar days of period end (regulator deadline is 60 days for many venues).",
            "Annual report: target 90 calendar days from year-end.",
            "AGM circular: minimum 21 clear days before the meeting (verify venue-specific rule).",
        ]),
        ("h2", "5. Common Pitfalls"),
        ("p", "Numbers reissued after submission — re-submission required and prior version withdrawn explicitly. Material announcements drafted in the active voice but ambiguous on financial impact. Forward-looking statements lacking the standard cautionary language. Trading windows breached because the announcement timing pulled a director into a blackout period."),
    ]
    _docx(out("REG_Equities_Submission_Guidelines.docx"), title, sections)


def build_reg_policy_industry_consultation_notes():
    title = "Industry Consultation Notes — FY2026 Policy Refresh"
    sections = [
        ("h1", title),
        ("p", "Owner: Group Public Affairs (Mod Admin)  •  Scope: Stakeholder feedback collected for the FY2026 policy refresh on private-credit licensing and crypto-adjacent activity"),
        ("h2", "1. Engagement programme"),
        ("p", "Between 2026-01-15 and 2026-03-20, the team held 14 round-tables and 11 bilateral consultations with industry stakeholders. Participants included asset managers, banks, custodians, law firms, professional bodies, and consumer-advocacy groups."),
        ("h2", "2. Themes raised by industry"),
        ("numbered", [
            "Definitional clarity on what constitutes 'institutional' versus 'retail' private credit.",
            "Cost of compliance for sub-USD 100 million fund managers.",
            "Operational treatment of stablecoin and tokenised debt instruments.",
            "Cross-jurisdictional recognition of fit-and-proper assessments.",
            "Transition arrangements for already-licensed firms with grandfathered terms.",
        ]),
        ("h2", "3. Themes raised by consumer-advocacy groups"),
        ("bullets", [
            "Stronger disclosures on illiquidity and lock-up periods.",
            "Cooling-off windows for retail-feeder structures.",
            "Faster enforcement on unlicensed solicitation, particularly on social media.",
            "Plain-language explanations of net-return calculations.",
        ]),
        ("h2", "4. Areas of consensus"),
        ("p", "Stakeholders broadly agreed on (a) the need for clearer eligibility rules, (b) a tiered licensing regime that reflects manager size and complexity, (c) the importance of harmonising fit-and-proper recognition with peer regulators, and (d) stronger enforcement on unlicensed soliciting via social platforms."),
        ("h2", "5. Areas of disagreement"),
        ("p", "Stakeholders disagreed on (a) whether stablecoin custody should be brought under the same regime as fund custody, (b) the calibration of the AUM threshold for the lighter-touch tier, and (c) the extent to which retail feeder structures should be permitted at all."),
        ("h2", "6. Indicative drafting positions to be tested"),
        ("bullets", [
            "Three-tier licensing: SFO, sub-USD 250m manager, institutional manager.",
            "Cross-recognition memorandum with two peer regulators for fit-and-proper.",
            "Mandatory cooling-off of 5 business days for retail feeders above USD 50,000 ticket.",
            "Public register of authorised entities with API access for downstream verification.",
        ]),
    ]
    _docx(out("REG_Policy_Industry_Consultation_Notes.docx"), title, sections)


def build_reg_policy_standard_template():
    title = "Group Policy Document — Standard Template"
    sections = [
        ("h1", title),
        ("p", "Owner: Group Public Affairs (Mod Admin)  •  Version: 3.1  •  Reviewers: Group Legal, Group Compliance, Group Strategy"),
        ("h2", "1. Document control"),
        ("table", [
            ["Field", "Description"],
            ["Title", "[Title]"],
            ["Reference number", "[Auto-generated]"],
            ["Version", "[X.Y]"],
            ["Effective date", "[YYYY-MM-DD]"],
            ["Next review date", "[YYYY-MM-DD]"],
            ["Document owner", "[Name + role]"],
            ["Approvers", "[Names + roles]"],
        ]),
        ("h2", "2. Purpose"),
        ("p", "[Two to three sentences describing why this policy exists and the outcome it is intended to achieve.]"),
        ("h2", "3. Scope"),
        ("p", "[Define the entities, geographies, business units, and activities covered. Define what is explicitly out of scope.]"),
        ("h2", "4. Definitions"),
        ("p", "[Tabular glossary of any term used in the policy that may not be uniformly understood across the group.]"),
        ("h2", "5. Policy statements"),
        ("p", "[Numbered statements. Each statement is a single, testable requirement. Avoid stacking multiple requirements in one statement.]"),
        ("h2", "6. Roles and responsibilities"),
        ("p", "[Use RACI or a similar matrix. Each role identified must map to a named function in the group org chart.]"),
        ("h2", "7. Procedures"),
        ("p", "[High-level procedure flow. Detailed step-by-step procedures live in supporting SOPs.]"),
        ("h2", "8. Exceptions and waivers"),
        ("p", "[Specify who can grant a waiver, the documentation required, the maximum waiver period, and the escalation path for repeated waivers.]"),
        ("h2", "9. Measurement and reporting"),
        ("p", "[KPIs, frequency of measurement, reporting line, and the forum that reviews the policy's effectiveness.]"),
        ("h2", "10. Related documents"),
        ("p", "[List the upstream regulator instruments, downstream SOPs, training materials, and forms that pair with this policy.]"),
        ("h2", "11. Version history"),
        ("p", "[Append-only log of every version with the date, author, and summary of change.]"),
    ]
    _docx(out("REG_Policy_Standard_Template.docx"), title, sections)


BUILDERS = [
    build_aud_auditee_walkthrough,
    build_hr_strategic_priorities_2030,
    build_ie_bilingual_content_library,
    build_leg_standard_terms_schedule,
    build_leg_vendor_contract_draft,
    build_prc_rfp_requirements,
    build_reg_anti_scam_email_reply_library,
    build_reg_equities_submission_guidelines,
    build_reg_policy_industry_consultation_notes,
    build_reg_policy_standard_template,
]


if __name__ == "__main__":
    for fn in BUILDERS:
        fn()
        print("Wrote:", fn.__name__)
