"""
cowork_recipient_casts.py
─────────────────────────
User feedback (2026-05-15):
  "the cowork one... why all so similar prompts one... each and everyone in
   the industries and departments...."

Diagnosis: every Cowork prompt across all 55 entries currently ships the
SAME 6-name appendix:
  "Use these named recipients consistently across the email task and the
   Teams meeting task — Hadar (Group CFO), Sasha (Group Chief of Staff),
   Daichi (Head of IR), Sonia (Head of Strategy), Will (Head of Risk) and
   Omar (Head of Procurement) — and adapt the precise distribution per
   sub-task..."

Fix: at build time, replace this generic appendix with an entry-archetype-
specific 6-person cast, so a Banking entry gets BNM/CFO/Treasurer/Wholesale-
Risk casting, Healthcare gets Medical-Director/Chief-Nurse/Pharmacy/Quality
casting, Manufacturing gets Plant-Manager/QA/Customer-Recovery/S&OP casting,
etc. Persona consistency preserved by always retaining 1-2 of the 4
canonical Hadar / Sasha / Daichi / Mod Admin personas in the cast.

Wired in by build_master.py after _normalize_cowork (the approval-gate
appender). Touches `prompts`, `promptsID`, and `promptsBM` arrays.
"""
import re

# ── 1. Canonical recipient casts per archetype ─────────────────────────────
# Each cast = list of 6 (name, role_en) tuples. Roles are translated to
# ID/BM via COWORK_ROLE_TRANS at format time. Names are deliberately diverse
# (Malay / Chinese / Indian / Indonesian / Western) reflecting an ASEAN
# conglomerate's bench.

CASTS = {
    # Banking & Finance
    'bank': [
        ('Hadar', 'Group CFO'),
        ('Sasha', 'Group Chief of Staff'),
        ('Inderjit', 'Group Treasurer'),
        ('Mei Lin', 'Head of Wholesale Banking Risk'),
        ('Rashid', 'Group Compliance Director'),
        ('Anand', 'Central Bank Liaison'),
    ],
    'ins': [
        ('Hadar', 'Group CFO'),
        ('Sasha', 'Group Chief of Staff'),
        ('Daichi', 'Head of Investor Relations'),
        ('Anwar', 'Group Chief Actuary'),
        ('Priya', 'Head of Underwriting'),
        ('Liana', 'Group Compliance Director'),
    ],
    # Healthcare
    'hc': [
        ('Hadar', 'Group CFO'),
        ('Daichi', 'Head of Investor Relations'),
        ('Aisyah', 'Group Medical Director'),
        ('Rose', 'Group Chief Nurse'),
        ('Bambang', 'Head of Pharmacy'),
        ('Indira', 'Group Quality Director'),
    ],
    # Energy / Mining / Utilities
    'energy': [
        ('Hadar', 'Group CFO'),
        ('Mod Admin', 'Group Strategy Director'),
        ('Yusof', 'Group HSSE Director'),
        ('Vikram', 'Operations VP'),
        ('Siti Hawa', 'Refinery Manager'),
        ('Khairul', 'Energy Regulator Liaison'),
    ],
    # Manufacturing / Auto / Semicon / FMCG
    'mfg': [
        ('Hadar', 'Group CFO'),
        ('Mod Admin', 'Group Strategy Director'),
        ('Robert', 'Flagship Plant Manager'),
        ('Hanif', 'Group QA Director'),
        ('Jenny', 'Customer Recovery Lead'),
        ('Iqbal', 'S&OP Coordinator'),
    ],
    # Agri / Plantation / Forestry
    'agri': [
        ('Hadar', 'Group CFO'),
        ('Daichi', 'Head of Investor Relations'),
        ('Aziz', 'Group Estate GM'),
        ('Lucia', 'Sustainability & Certification Manager'),
        ('Faridah', 'Smallholder Engagement Lead'),
        ('Bambang', 'Mill Operations Lead'),
    ],
    # Retail / QSR / Mall / E-comm
    'retail': [
        ('Hadar', 'Group CFO'),
        ('Sasha', 'Group Chief of Staff'),
        ('Adeline', 'Group Category Director'),
        ('Marcus', 'Store Operations VP'),
        ('Putri', 'Marketing & Promo Lead'),
        ('Henry', 'Loyalty & CX Lead'),
    ],
    # Hospitality / Travel / Aviation / Media
    'hosp': [
        ('Hadar', 'Group CFO'),
        ('Sasha', 'Group Chief of Staff'),
        ('David', 'Flagship Property GM'),
        ('Aishwarya', 'Director of Operations'),
        ('Khaled', 'Service Recovery Lead'),
        ('Lina', 'Reservations & Distribution Lead'),
    ],
    # Telco / Tech / SaaS / BPO
    'tel': [
        ('Hadar', 'Group CFO'),
        ('Mod Admin', 'Group Strategy Director'),
        ('Iskandar', 'SVP Network & Reliability'),
        ('Priya', 'SVP Product'),
        ('Cheng Wei', 'Head of Cyber'),
        ('Ahmad', 'Regulatory Affairs Lead'),
    ],
    # Maritime / Logistics
    'trans': [
        ('Hadar', 'Group CFO'),
        ('Mod Admin', 'Group Strategy Director'),
        ('Tan Boon Heng', 'Group Port Captain'),
        ('Liana', 'Inland Operations Director'),
        ('Hamzah', 'Marine Insurance Liaison'),
        ('Sundari', 'Customs & Compliance Lead'),
    ],
    # Public Sector / Education
    'pub': [
        ('Hadar', 'Group CFO'),
        ('Sasha', 'Group Chief of Staff'),
        ('Yusoff', 'Permanent Secretary'),
        ('Endang', 'Communications Director'),
        ('Razak', 'Inter-Ministry Liaison'),
        ('Nurhayati', 'Citizen Services Director'),
    ],
    # Property / Construction / REIT
    'prop': [
        ('Hadar', 'Group CFO'),
        ('Mod Admin', 'Group Strategy Director'),
        ('Wei Ming', 'Group Project Director'),
        ('Kavitha', 'Asset Management VP'),
        ('Bambang', 'Construction Programme Manager'),
        ('Rosalind', 'Tenant Relations Director'),
    ],

    # Department-specific casts (each dept's own protagonist)
    'dept-finance': [
        ('Hadar', 'Group CFO'),
        ('Sasha', 'Group Chief of Staff'),
        ('Inderjit', 'Group Treasurer'),
        ('Liu Wei', 'Head of FP&A'),
        ('Norliza', 'Group Tax Director'),
        ('Aisha', 'Internal Controls Lead'),
    ],
    'dept-hr': [
        ('Sasha', 'Group Chief of Staff'),
        ('Hadar', 'Group CFO'),
        ('Indira', 'Group CHRO'),
        ('Mei Ling', 'Head of Talent'),
        ('Bayu', 'Head of Reward'),
        ('Farhana', 'Head of Learning'),
    ],
    'dept-legal': [
        ('Hadar', 'Group CFO'),
        ('Sasha', 'Group Chief of Staff'),
        ('Aziz', 'Group General Counsel'),
        ('Anjali', 'Head of Litigation'),
        ('Wei Ming', 'Head of Commercial Legal'),
        ('Ridwan', 'Regulatory Affairs Lead'),
    ],
    'dept-risk': [
        ('Hadar', 'Group CFO'),
        ('Daichi', 'Head of Investor Relations'),
        ('Mahesh', 'Group CRO'),
        ('Yvonne', 'Head of Operational Risk'),
        ('Ridzuan', 'Head of Internal Audit'),
        ('Lina', 'Compliance Director'),
    ],
    'dept-strategy': [
        ('Mod Admin', 'Group Strategy Director'),
        ('Sasha', 'Group Chief of Staff'),
        ('Hadar', 'Group CFO'),
        ('Imran', 'Head of Corp Dev'),
        ('Karina', 'Head of Strategy Execution'),
        ('Daniel', 'Head of Transformation'),
    ],
    'dept-marketing': [
        ('Sasha', 'Group Chief of Staff'),
        ('Daichi', 'Head of Investor Relations'),
        ('Janice', 'Group CMO'),
        ('Reza', 'Head of Brand'),
        ('Putri', 'Head of Digital Marketing'),
        ('Aaron', 'Head of Customer Insights'),
    ],
    'dept-esg': [
        ('Daichi', 'Head of Investor Relations'),
        ('Mod Admin', 'Group Strategy Director'),
        ('Lestari', 'Group Chief Sustainability Officer'),
        ('Tan', 'Head of ESG Reporting'),
        ('Aishwarya', 'Head of Climate Programs'),
        ('Ridho', 'Head of Stakeholder Engagement'),
    ],
    'dept-operations': [
        ('Mod Admin', 'Group Strategy Director'),
        ('Hadar', 'Group CFO'),
        ('Bayu', 'COO'),
        ('Marisa', 'Head of Operations'),
        ('Vikram', 'Head of Process Excellence'),
        ('Wei', 'Head of Quality'),
    ],
    'dept-corpsec': [
        ('Sasha', 'Group Chief of Staff'),
        ('Daichi', 'Head of Investor Relations'),
        ('Datin Lim', 'Company Secretary'),
        ('Ridho', 'Head of Governance'),
        ('Kavitha', 'Board Secretary'),
        ('Anggun', 'Head of Disclosures'),
    ],
    'dept-investor-relations': [
        ('Daichi', 'Head of Investor Relations'),
        ('Hadar', 'Group CFO'),
        ('Sasha', 'Group Chief of Staff'),
        ('Edwin', 'Head of IR Communications'),
        ('Maya', 'Head of Equity Sales Coverage'),
        ('Yusop', 'IR Operations Lead'),
    ],
    'dept-procurement': [
        ('Hadar', 'Group CFO'),
        ('Mod Admin', 'Group Strategy Director'),
        ('Omar', 'Group CPO'),
        ('Mei Yi', 'Head of Strategic Sourcing'),
        ('Hisham', 'Head of Vendor Risk'),
        ('Daniel', 'Head of S2P'),
    ],
    'dept-it-digital': [
        ('Mod Admin', 'Group Strategy Director'),
        ('Hadar', 'Group CFO'),
        ('Cheng Wei', 'Group CIO'),
        ('Priya', 'Head of Cyber'),
        ('Bambang', 'Head of Cloud'),
        ('Aaron', 'Head of Data'),
    ],

    # General entry — keeps the canonical 4 personas
    'general': [
        ('Hadar', 'Group CFO'),
        ('Sasha', 'Group Chief of Staff'),
        ('Daichi', 'Head of Investor Relations'),
        ('Mod Admin', 'Group Strategy Director'),
        ('Will', 'Group Chief Risk Officer'),
        ('Omar', 'Group Chief Procurement Officer'),
    ],
}

# ── 2. EN role → ID/BM role-title localiser ───────────────────────────────
# ID and BM share the same role string (BM auto-fill copies ID).
ROLE_TRANS = {
    'Group CFO': 'Direktur Keuangan Grup',
    'Group Chief of Staff': 'Kepala Staf Grup',
    'Head of Investor Relations': 'Kepala Hubungan Investor',
    'Group Strategy Director': 'Direktur Strategi Grup',
    'Group Treasurer': 'Treasurer Grup',
    'Head of Wholesale Banking Risk': 'Kepala Risiko Wholesale Banking',
    'Group Compliance Director': 'Direktur Kepatuhan Grup',
    'Central Bank Liaison': 'Penghubung Bank Sentral',
    'Group Chief Actuary': 'Aktuaris Grup',
    'Head of Underwriting': 'Kepala Underwriting',
    'Group Medical Director': 'Direktur Medis Grup',
    'Group Chief Nurse': 'Kepala Perawat Grup',
    'Head of Pharmacy': 'Kepala Farmasi',
    'Group Quality Director': 'Direktur Kualitas Grup',
    'Group HSSE Director': 'Direktur HSSE Grup',
    'Operations VP': 'VP Operasi',
    'Refinery Manager': 'Manajer Kilang',
    'Energy Regulator Liaison': 'Penghubung Regulator Energi',
    'Flagship Plant Manager': 'Manajer Pabrik Andalan',
    'Group QA Director': 'Direktur QA Grup',
    'Customer Recovery Lead': 'Lead Pemulihan Pelanggan',
    'S&OP Coordinator': 'Koordinator S&OP',
    'Group Estate GM': 'GM Estate Grup',
    'Sustainability & Certification Manager': 'Manajer Keberlanjutan & Sertifikasi',
    'Smallholder Engagement Lead': 'Lead Engagement Petani Kecil',
    'Mill Operations Lead': 'Lead Operasi Pabrik',
    'Group Category Director': 'Direktur Kategori Grup',
    'Store Operations VP': 'VP Operasi Toko',
    'Marketing & Promo Lead': 'Lead Pemasaran & Promo',
    'Loyalty & CX Lead': 'Lead Loyalty & CX',
    'Flagship Property GM': 'GM Properti Andalan',
    'Director of Operations': 'Direktur Operasi',
    'Service Recovery Lead': 'Lead Pemulihan Layanan',
    'Reservations & Distribution Lead': 'Lead Reservasi & Distribusi',
    'SVP Network & Reliability': 'SVP Jaringan & Keandalan',
    'SVP Product': 'SVP Produk',
    'Head of Cyber': 'Kepala Cyber',
    'Regulatory Affairs Lead': 'Lead Urusan Regulasi',
    'Group Port Captain': 'Kapten Pelabuhan Grup',
    'Inland Operations Director': 'Direktur Operasi Darat',
    'Marine Insurance Liaison': 'Penghubung Asuransi Marin',
    'Customs & Compliance Lead': 'Lead Bea Cukai & Kepatuhan',
    'Permanent Secretary': 'Sekretaris Permanen',
    'Communications Director': 'Direktur Komunikasi',
    'Inter-Ministry Liaison': 'Penghubung Antar-Kementerian',
    'Citizen Services Director': 'Direktur Layanan Warga',
    'Group Project Director': 'Direktur Proyek Grup',
    'Asset Management VP': 'VP Manajemen Aset',
    'Construction Programme Manager': 'Manajer Program Konstruksi',
    'Tenant Relations Director': 'Direktur Hubungan Penyewa',
    'Head of FP&A': 'Kepala FP&A',
    'Group Tax Director': 'Direktur Pajak Grup',
    'Internal Controls Lead': 'Lead Pengendalian Internal',
    'Group CHRO': 'CHRO Grup',
    'Head of Talent': 'Kepala Talenta',
    'Head of Reward': 'Kepala Reward',
    'Head of Learning': 'Kepala Pembelajaran',
    'Group General Counsel': 'General Counsel Grup',
    'Head of Litigation': 'Kepala Litigasi',
    'Head of Commercial Legal': 'Kepala Legal Komersial',
    'Group CRO': 'CRO Grup',
    'Head of Operational Risk': 'Kepala Risiko Operasional',
    'Head of Internal Audit': 'Kepala Audit Internal',
    'Compliance Director': 'Direktur Kepatuhan',
    'Head of Corp Dev': 'Kepala Corp Dev',
    'Head of Strategy Execution': 'Kepala Eksekusi Strategi',
    'Head of Transformation': 'Kepala Transformasi',
    'Group CMO': 'CMO Grup',
    'Head of Brand': 'Kepala Brand',
    'Head of Digital Marketing': 'Kepala Pemasaran Digital',
    'Head of Customer Insights': 'Kepala Insights Pelanggan',
    'Group Chief Sustainability Officer': 'CSO Grup',
    'Head of ESG Reporting': 'Kepala Pelaporan ESG',
    'Head of Climate Programs': 'Kepala Program Iklim',
    'Head of Stakeholder Engagement': 'Kepala Engagement Stakeholder',
    'COO': 'COO',
    'Head of Operations': 'Kepala Operasi',
    'Head of Process Excellence': 'Kepala Process Excellence',
    'Head of Quality': 'Kepala Kualitas',
    'Company Secretary': 'Sekretaris Perusahaan',
    'Head of Governance': 'Kepala Tata Kelola',
    'Board Secretary': 'Sekretaris Dewan',
    'Head of Disclosures': 'Kepala Disclosures',
    'Head of IR Communications': 'Kepala Komunikasi IR',
    'Head of Equity Sales Coverage': 'Kepala Cakupan Equity Sales',
    'IR Operations Lead': 'Lead Operasi IR',
    'Group CPO': 'CPO Grup',
    'Head of Strategic Sourcing': 'Kepala Sourcing Strategis',
    'Head of Vendor Risk': 'Kepala Risiko Vendor',
    'Head of S2P': 'Kepala S2P',
    'Group CIO': 'CIO Grup',
    'Head of Cloud': 'Kepala Cloud',
    'Head of Data': 'Kepala Data',
    'Group Chief Risk Officer': 'CRO Grup',
    'Group Chief Procurement Officer': 'CPO Grup',
}


def _archetype(eid):
    """Map entry id → archetype key. Mirrors gen_hub.py:_coworkTipsForEntry
    so the cast bucket and tips bucket stay aligned per entry.
    """
    e = (eid or '').lower()
    if not e:
        return 'general'
    if e == 'general':
        return 'general'
    if e.startswith('dept-'):
        # Use exact dept key if we have one, else fall back to general
        return e if e in CASTS else 'general'
    # Industry archetypes — order matters; first match wins
    if re.search(r'insurance|takaful', e):
        return 'ins'
    if re.search(r'bank|finance|reit|leasing|remittance|fintech|payment|asset-mgmt|securit|broker|wealth|microfinance|investment-banking|stock-exch|mortgage|treasury|invest', e):
        return 'bank'
    if re.search(r'health|hospital|pharma|clinic|medical|diagnos|tcm', e):
        return 'hc'
    if re.search(r'energy|oil|gas|petro|refin|coal|mining|nuclear|solar|wind|geothermal|hydro|power|util|electric|rare-earth|renewable|^og-|-og-', e):
        return 'energy'
    if re.search(r'manufactur|automotiv|auto-tyre|semiconductor|electronics|chemical|cement|steel|fmcg|food|tobacco|rubber|plastic|paper|textile|industrial', e):
        return 'mfg'
    if re.search(r'agri|plantation|palm|forest|fish|aquaculture|livestock|farm', e):
        return 'agri'
    if re.search(r'retail|grocery|qsr|restaurant|fashion|apparel|ecomm|super-app|mall', e):
        return 'retail'
    if re.search(r'hotel|tourism|airline|aviation|cruise|leisure|entertain|gaming|media|broadcast', e):
        return 'hosp'
    if re.search(r'telco|telecom|broadband|tower|isp|tech|software|cloud|data-center|saas|platform|digital|bpo', e):
        return 'tel'
    if re.search(r'maritime|shipping|port|logistic|rail|express|courier|cold-chain|transport|trucking|terminal', e):
        return 'trans'
    if re.search(r'government|gov|public-sector|smart-city|sovereign|regulator|stat-office|water-util|defense|aerospace|education|university', e):
        return 'pub'
    if re.search(r'property|construction|reit|conglomerate|glc-investment|diversified', e):
        return 'prop'
    return 'general'


def _format_cast(cast, lang):
    """Format a 6-tuple cast as a recipient phrase.
    EN:  'Hadar (Group CFO), Sasha (Group Chief of Staff), ... and Omar (CPO)'
    ID:  'Hadar (Direktur Keuangan Grup), ... dan Omar (CPO Grup)'
    """
    parts = []
    for name, role_en in cast:
        if lang == 'EN':
            role = role_en
        else:
            role = ROLE_TRANS.get(role_en, role_en)
        parts.append(f"{name} ({role})")
    if lang == 'EN':
        return ', '.join(parts[:-1]) + ' and ' + parts[-1]
    else:
        return ', '.join(parts[:-1]) + ' dan ' + parts[-1]


def _build_clause(arche, lang):
    """Wrap the formatted cast in the canonical sentence."""
    cast = CASTS.get(arche, CASTS['general'])
    body = _format_cast(cast, lang)
    if lang == 'EN':
        return (
            'Use these named recipients consistently across the email task and '
            'the Teams meeting task — ' + body + ' — and adapt the precise '
            'distribution per sub-task to keep each communication focused on '
            'the right audience.'
        )
    # ID/BM share the same connector wording (BM auto-fill copies ID).
    return (
        'Gunakan penerima bernama berikut secara konsisten lintas tugas email '
        'dan tugas rapat Teams — ' + body + ' — dan sesuaikan distribusi tepat '
        'per sub-tugas agar tiap komunikasi tetap fokus pada audiens yang tepat.'
    )


# ── 3. Regex matchers for the existing canonical 6-name appendix ──────────
# Match from "Use these named recipients..." to the next sentence-end.
_RE_RECIP_EN = re.compile(
    r'Use these named recipients consistently across the email task and the Teams meeting task[^.]*?per sub-task[^.]*?\.',
    re.DOTALL
)
_RE_RECIP_ID = re.compile(
    r'Gunakan penerima bernama berikut secara konsisten lintas tugas email dan tugas rapat Teams[^.]*?per sub-tugas[^.]*?\.',
    re.DOTALL
)


def diversify_cowork_recipients(entries):
    """Walk every Cowork tool block on every entry. Replace the generic
    6-name appendix with the entry's archetype-specific cast.
    Returns count of prompts updated.
    """
    fixed = 0
    for e in entries:
        eid = e.get('id') if isinstance(e, dict) else None
        if not eid:
            continue
        arche = _archetype(eid)
        clause_en = _build_clause(arche, 'EN')
        clause_id = _build_clause(arche, 'ID')
        for tool in e.get('prompts') or []:
            if 'Cowork' not in (tool.get('tool') or ''):
                continue
            for arr_key, clause in [
                ('prompts',   clause_en),
                ('promptsID', clause_id),
                ('promptsBM', clause_id),
            ]:
                arr = tool.get(arr_key) or []
                for p in arr:
                    if not isinstance(p, dict):
                        continue
                    body = p.get('prompt') or ''
                    if not body:
                        continue
                    new_body = _RE_RECIP_EN.sub(clause, body)
                    new_body = _RE_RECIP_ID.sub(clause, new_body)
                    if new_body != body:
                        p['prompt'] = new_body
                        fixed += 1
    return fixed


__all__ = [
    'CASTS',
    'ROLE_TRANS',
    'diversify_cowork_recipients',
]
