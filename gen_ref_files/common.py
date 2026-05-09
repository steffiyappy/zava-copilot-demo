"""Shared constants for the 6 Zava reference files (FY2025 emergency Board scenario).

ALL numbers internally consistent: 11-division ASEAN conglomerate, FY2025 EBITDA
miss of ~18% against budget, 3 divisions in negative EBITDA territory.

Currency: MYR Million unless stated.
Years: FY2022A, FY2023A, FY2024A, FY2025A (the miss), FY2026F (recovery plan).
"""

# Divisions — ordered by Group's published reporting hierarchy ----------------
DIVISIONS = [
    # (id, name, country, sector, hq_city)
    ('chem',   'Zava Chemicals',          'Malaysia',  'Specialty Chemicals',     'Kuala Lumpur'),
    ('agri',   'Zava Agribusiness',       'Indonesia', 'Palm Oil & Agribusiness', 'Jakarta'),
    ('mfg',    'Zava Manufacturing',      'Malaysia',  'Industrial Manufacturing','Penang'),
    ('fs',     'Zava Financial Services', 'Malaysia',  'Asset Management',        'Kuala Lumpur'),
    ('prop',   'Zava Properties',         'Malaysia',  'Real Estate Development', 'Petaling Jaya'),
    ('bpo',    'Zava BPO',                'Malaysia',  'Business Process Outsourcing','Cyberjaya'),
    ('trade',  'Zava Trading',            'Singapore', 'Commodity Trading',       'Singapore'),
    ('pharma', 'Zava Pharma',             'Indonesia', 'Generic Pharmaceuticals', 'Surabaya'),
    ('hc',     'Zava Healthcare',         'Malaysia',  'Hospital Operations',     'Subang Jaya'),
    ('retail', 'Zava Retail',             'Malaysia',  'Specialty Retail',        'Shah Alam'),
    ('treas',  'Zava Group Treasury',     'Malaysia',  'Treasury & Holdings',     'Kuala Lumpur'),
]

DIVISION_IDS = [d[0] for d in DIVISIONS]
DIVISION_NAMES = {d[0]: d[1] for d in DIVISIONS}

# FY2025 budget vs actual (MYR M) -- the centrepiece data set ---------------------
# Engineered to deliver: Group rev miss ~4%, EBITDA miss ~18%, 3 divisions in
# negative EBITDA territory (Properties, Healthcare, Retail).
FY25 = {
    # id      bud_rev  act_rev  bud_eb_pct  act_eb_pct  status
    'chem':   (7800,   7300,    0.170,      0.162,      'Amber'),
    'agri':   (6500,   6200,    0.180,      0.165,      'Amber'),
    'mfg':    (7200,   7100,    0.160,      0.155,      'Green'),
    'fs':     (5500,   5800,    0.220,      0.231,      'Green'),
    'prop':   (2200,   1800,    0.280,    -0.005,       'Red'),    # negative EBITDA
    'bpo':    (3100,   3300,    0.160,      0.168,      'Green'),
    'trade':  (5800,   5400,    0.080,      0.070,      'Amber'),
    'pharma': (1900,   1900,    0.240,      0.237,      'Green'),
    'hc':     (1500,   1200,    0.140,    -0.005,       'Red'),    # negative EBITDA
    'retail': (2500,   2200,    0.080,    -0.005,       'Red'),    # negative EBITDA
    'treas':  ( 200,    180,    0.600,      0.556,      'Green'),
}

def fy25_eb(d, kind):
    """kind in {'bud_eb','act_eb','bud_rev','act_rev','bud_eb_pct','act_eb_pct','status','rev_var','eb_var','eb_var_pct'}."""
    rec = FY25[d]
    bud_rev, act_rev, bud_pct, act_pct, status = rec
    bud_eb = bud_rev * bud_pct
    act_eb = act_rev * act_pct
    if kind == 'bud_rev': return bud_rev
    if kind == 'act_rev': return act_rev
    if kind == 'bud_eb_pct': return bud_pct
    if kind == 'act_eb_pct': return act_pct
    if kind == 'bud_eb': return bud_eb
    if kind == 'act_eb': return act_eb
    if kind == 'rev_var': return act_rev - bud_rev
    if kind == 'eb_var': return act_eb - bud_eb
    if kind == 'eb_var_pct':
        return (act_eb - bud_eb) / bud_eb if bud_eb else 0
    if kind == 'status': return status
    raise ValueError(kind)


def status_color(status):
    return {'Red':'FFC7CE','Amber':'FFEB9C','Green':'C6EFCE'}.get(status, 'D9E1F2')


# 5-year history for headline P&L (revenue MYR M, EBITDA % of revenue) ------------
# FY22A, FY23A, FY24A, FY25A, FY26F. FY25A column derived from FY25 above.
HISTORY = {
    #          rev: 22A,  23A,   24A,   25A,   26F          eb_pct: 22A,   23A,   24A,   25A,   26F
    'chem':   ((6900, 7300, 7600, 7300, 7700),         (0.179, 0.176, 0.171, 0.162, 0.170)),
    'agri':   ((5800, 6100, 6400, 6200, 6500),         (0.184, 0.179, 0.171, 0.165, 0.176)),
    'mfg':    ((6500, 6800, 7000, 7100, 7400),         (0.165, 0.162, 0.158, 0.155, 0.162)),
    'fs':     ((4900, 5200, 5400, 5800, 6100),         (0.213, 0.218, 0.225, 0.231, 0.235)),
    'prop':   ((3200, 3000, 2400, 1800, 2200),         (0.241, 0.198, 0.092,-0.005, 0.115)),
    'bpo':    ((2400, 2700, 2950, 3300, 3600),         (0.150, 0.158, 0.162, 0.168, 0.175)),
    'trade':  ((5300, 5600, 5800, 5400, 5700),         (0.078, 0.083, 0.082, 0.070, 0.075)),
    'pharma': ((1700, 1800, 1850, 1900, 2050),         (0.231, 0.235, 0.238, 0.237, 0.244)),
    'hc':     ((1200, 1300, 1400, 1200, 1450),         (0.139, 0.131, 0.085,-0.005, 0.087)),
    'retail': ((2200, 2350, 2400, 2200, 2400),         (0.069, 0.062, 0.041,-0.005, 0.038)),
    'treas':  (( 165,  175,  185,  180,  195),         (0.620, 0.610, 0.595, 0.556, 0.580)),
}


def hist_rev(d, year_idx):
    return HISTORY[d][0][year_idx]


def hist_eb_pct(d, year_idx):
    return HISTORY[d][1][year_idx]


def hist_eb(d, year_idx):
    return HISTORY[d][0][year_idx] * HISTORY[d][1][year_idx]


YEARS = ['FY2022A', 'FY2023A', 'FY2024A', 'FY2025A', 'FY2026F']


# Lender register (for Lender Covenant Tracker workbook) ------------------------
LENDERS = [
    # (id, name, jurisdiction, facility_type, facility_myr_m, drawn_myr_m, maturity_year, rate_basis, security)
    ('LF01','Maybank',                    'MY','Revolving Credit',  2500, 2100, 2027, 'KLIBOR+1.45%','Negative pledge'),
    ('LF02','CIMB Bank',                  'MY','Term Loan',          2000, 2000, 2028, 'KLIBOR+1.60%','Asset charge — Properties'),
    ('LF03','Public Bank',                'MY','Revolving Credit',  1500, 1100, 2026, 'KLIBOR+1.40%','Negative pledge'),
    ('LF04','RHB Bank',                   'MY','Term Loan',          1200, 1200, 2029, 'KLIBOR+1.65%','Asset charge — Manufacturing'),
    ('LF05','OCBC Bank',                  'SG','Bilateral Loan',     1300,  900, 2027, 'SOFR+1.85%',  'Negative pledge'),
    ('LF06','DBS Bank',                   'SG','Revolving Credit',  1100,  650, 2027, 'SOFR+1.75%',  'Negative pledge'),
    ('LF07','UOB',                        'SG','Term Loan',          900,  900, 2028, 'SOFR+1.90%',  'Negative pledge'),
    ('LF08','Bank Mandiri',               'ID','Term Loan',          800,  800, 2028, 'JIBOR+2.10%', 'Asset charge — Agribusiness'),
    ('LF09','Bank Central Asia',          'ID','Bilateral Loan',     700,  500, 2026, 'JIBOR+2.00%', 'Negative pledge'),
    ('LF10','Bank Negara Indonesia',      'ID','Term Loan',          600,  600, 2029, 'JIBOR+2.25%', 'Asset charge — Pharma'),
    ('LF11','Sumitomo Mitsui',            'JP','Bilateral Loan',     900,  600, 2028, 'TONA+1.95%',  'Negative pledge'),
    ('LF12','Mizuho Bank',                'JP','Term Loan',          700,  700, 2027, 'TONA+1.85%',  'Negative pledge'),
    ('LF13','MUFG',                       'JP','Revolving Credit',   600,  300, 2026, 'TONA+1.80%',  'Negative pledge'),
    ('LF14','HSBC',                       'UK','Bilateral Loan',     800,  550, 2027, 'SOFR+1.70%',  'Negative pledge'),
    ('LF15','Standard Chartered',         'UK','Revolving Credit',   700,  450, 2027, 'SOFR+1.80%',  'Negative pledge'),
    ('LF16','MUFG MTN Programme',         'JP','MTN',               1500, 1500, 2030, 'Fixed 4.95%', 'Senior unsecured'),
    ('LF17','Bursa Sukuk Murabahah',      'MY','Sukuk',             2000, 2000, 2031, 'Fixed 4.65%', 'Senior unsecured'),
    ('LF18','IDX MTN Programme',          'ID','MTN',                900,  900, 2029, 'Fixed 6.20%', 'Senior unsecured'),
]

# Personas appearing in narrative documents ------------------------------------
PERSONAS = [
    ('Hadar Caspit',        'Group CFO',                 'admin@ABSx62256373.onmicrosoft.com'),
    ('Sasha Ouellet',       'Group Chief of Staff',      'SashaO@ABSx62256373.OnMicrosoft.com'),
    ('Mod Admin',           'Group Strategy Director',   'admin@ABSx62256373.onmicrosoft.com'),
    ('Daichi Maruyama',     'Head of Investor Relations','admin@ABSx62256373.onmicrosoft.com'),
]
