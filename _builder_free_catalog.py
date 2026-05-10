# Free-tier (Copilot Chat) Agent Builder catalog.
# Mirrors _builder_catalog.py but with public URL knowledge instead of file knowledge.
# Free Copilot Chat cannot resolve enterprise file paths — agents in this catalog
# are pinned to public ASEAN regulator / industry-association / news websites.

CATALOG_FREE = {}
PACKS = {}
ENTRY_PACK = {}


def _build_packs():
    """Lazily populate PACKS the first time render_agents_free() is called."""
    if PACKS:
        return
    # Banking & Finance pack
    PACKS['banking'] = [
        {
            'name_tmpl': '{name} Regulator Watch (Public Sources)',
            'desc_tmpl': 'Monitors Bank Negara Malaysia + OJK + MAS announcements relevant to {name}.',
            'instr_tmpl': 'You are an analyst tracking banking-sector regulatory updates relevant to {name}. Pull from the official regulator websites listed in knowledge. Always cite the regulator name + announcement date + source URL. Never speculate beyond what the public page states. Output: 5-bullet weekly watch with severity (Info / Watch / Action) per item.',
            'urls': [
                ('https://www.bnm.gov.my/announcements', 'BNM official announcements list'),
                ('https://www.ojk.go.id/id/berita-dan-kegiatan/siaran-pers/Default.aspx', 'OJK press releases'),
                ('https://www.mas.gov.sg/news', 'MAS news + circulars'),
            ],
            'queries': [
                'Summarise the 5 most recent BNM announcements that would impact {name}, with severity and required action.',
                'Compare OJK and MAS guidance issued this month on AML/CFT — flag where {name} would need to update controls.',
                'Draft a regulator-watch one-pager for the {name} Group Risk Committee using only the cited sources.',
            ],
        },
        {
            'name_tmpl': '{name} Peer Pulse (Public IR)',
            'desc_tmpl': 'Tracks ASEAN banking peers via Bursa + IDX disclosure portals.',
            'instr_tmpl': 'You are an IR analyst tracking listed-bank peer disclosures relevant to {name}. Use ONLY the public disclosure portals listed in knowledge. Cite filing date + ticker + filing type for every claim. Output: peer move log with implications for {name}.',
            'urls': [
                ('https://www.bursamalaysia.com/market_information/announcements/company_announcement', 'Bursa Malaysia listed-co announcements'),
                ('https://www.idx.co.id/en/news/announcement/', 'IDX listed-co disclosures'),
                ('https://www.sgx.com/securities/company-announcements', 'SGX company announcements'),
            ],
            'queries': [
                'List the last 10 quarterly earnings filings by listed banks on Bursa + IDX with NIM, CIR, and gross-NPL figures.',
                'Which peer banks raised provisions or revised guidance in the last 30 days? Show source filings.',
                'Draft a 1-page peer-positioning note for the {name} CFO benchmarking against the 3 closest comparables.',
            ],
        },
        {
            'name_tmpl': '{name} Macro & Rates Scanner',
            'desc_tmpl': 'Pulls BNM/BI/MAS rate decisions + DOSM/BPS macro releases for {name} ALCO.',
            'instr_tmpl': 'You are a macro analyst supporting the {name} ALCO. Source ONLY from the central-bank and statistics-office sites in knowledge. Cite release date + indicator + value. Output: rates dashboard with 3-month outlook scenarios (base / hawkish / dovish).',
            'urls': [
                ('https://www.bnm.gov.my/monetary-policy-statements', 'BNM Monetary Policy Statements'),
                ('https://www.bi.go.id/en/publikasi/kebijakan-moneter/Default.aspx', 'Bank Indonesia monetary policy'),
                ('https://www.dosm.gov.my/portal-main/release-content/consumer-price-index', 'DOSM CPI releases'),
            ],
            'queries': [
                'Summarise the last 4 BNM and BI monetary-policy statements with rate moves and forward guidance.',
                'Pull the latest CPI prints from DOSM and BPS — what is the implication for {name} variable-rate book?',
                'Draft an ALCO macro update for {name} with base/hawkish/dovish scenarios over the next 3 months.',
            ],
        },
    ]
    # Insurance pack
    PACKS['insurance'] = [
        {
            'name_tmpl': '{name} Insurance Regulator Watch',
            'desc_tmpl': 'Tracks BNM Insurance/Takaful + OJK IKNB + MAS Insurance circulars relevant to {name}.',
            'instr_tmpl': 'You are an insurance compliance analyst for {name}. Source ONLY from the regulator + association URLs in knowledge. Cite circular number + date + URL. Output: weekly compliance digest with action owner suggestions.',
            'urls': [
                ('https://www.bnm.gov.my/insurance-takaful', 'BNM Insurance & Takaful policy documents'),
                ('https://www.ojk.go.id/en/kanal/iknb/Pages/Insurance.aspx', 'OJK IKNB Insurance regulations'),
                ('https://www.piam.org.my/', 'PIAM (General Insurance Assoc. Malaysia)'),
            ],
            'queries': [
                'List BNM and OJK insurance circulars issued in the last 90 days with implications for {name}.',
                'Compare RBC and risk-based capital guidance from BNM vs OJK — flag the deltas for {name}.',
                'Draft a weekly compliance digest for {name} legal & risk team using only cited sources.',
            ],
        },
        {
            'name_tmpl': '{name} Claims & Catastrophe Scanner',
            'desc_tmpl': 'Monitors PIAM, AAJI, Met Malaysia + BMKG + ASEAN disaster portals for emerging claims exposure.',
            'instr_tmpl': 'You are a claims-trend analyst for {name}. Use ONLY the catastrophe + association URLs in knowledge. For each event cite source + date + region. Output: rolling 14-day exposure scan.',
            'urls': [
                ('https://www.met.gov.my/', 'Malaysian Meteorological Department warnings'),
                ('https://www.bmkg.go.id/', 'BMKG Indonesia weather + earthquake alerts'),
                ('https://ahacentre.org/situation-update/', 'ASEAN AHA Centre disaster monitoring'),
            ],
            'queries': [
                'Summarise the last 14 days of weather and seismic alerts from Met Malaysia + BMKG + AHA Centre.',
                'Which events overlap {name} concentration zones? List the top 5 by potential gross-loss exposure.',
                'Draft a rolling 14-day catastrophe exposure note for the {name} reinsurance team.',
            ],
        },
        {
            'name_tmpl': '{name} Health & Mortality Trends Scanner',
            'desc_tmpl': 'Tracks MOH Malaysia + Kemenkes + WHO SEARO disease bulletins for life and health pricing.',
            'instr_tmpl': 'You are an actuarial trends analyst for {name}. Source ONLY from the public health URLs in knowledge. Cite bulletin name + date. Output: monthly trend brief flagging pricing or reserve implications.',
            'urls': [
                ('https://www.moh.gov.my/index.php/pages/view/56', 'KKM Press Releases (MOH Malaysia)'),
                ('https://www.kemkes.go.id/id/category/berita', 'Kemenkes Indonesia news'),
                ('https://www.who.int/southeastasia/news', 'WHO South-East Asia Region news'),
            ],
            'queries': [
                'Summarise the last 30 days of disease outbreak bulletins from KKM + Kemenkes + WHO SEARO.',
                'Which conditions show rising incidence relevant to {name} life and health books? Cite each.',
                'Draft a monthly mortality and morbidity trends brief for the {name} pricing committee.',
            ],
        },
    ]
    # Healthcare pack
    PACKS['healthcare'] = [
        {
            'name_tmpl': '{name} Health Regulator Watch',
            'desc_tmpl': 'Tracks KKM/MOH + Kemenkes + BPOM + NPRA announcements relevant to {name}.',
            'instr_tmpl': 'You are a health-regulatory analyst for {name}. Use ONLY the regulator URLs in knowledge. Cite circular + date for every claim. Output: weekly digest of approvals, recalls, and policy moves.',
            'urls': [
                ('https://www.moh.gov.my/index.php/pages/view/56', 'KKM Press Releases'),
                ('https://www.kemkes.go.id/id/category/berita', 'Kemenkes news'),
                ('https://www.npra.gov.my/index.php/en/announcement-news', 'NPRA Malaysia announcements'),
                ('https://www.pom.go.id/news', 'BPOM Indonesia news'),
            ],
            'queries': [
                'Summarise the last 30 days of approvals, recalls, and policy circulars from NPRA + BPOM.',
                'List KKM and Kemenkes announcements that change clinical or operational requirements for {name}.',
                'Draft a regulator digest for the {name} Medical Affairs and Quality Committee.',
            ],
        },
        {
            'name_tmpl': '{name} Clinical Guidelines Tracker',
            'desc_tmpl': 'Tracks MOH CPGs + AMM + Perdoki + WHO SEARO clinical guidance for {name}.',
            'instr_tmpl': 'You are a clinical librarian for {name}. Use ONLY the guideline portals in knowledge. Cite guideline name + revision date. Output: change-log of guidelines with affected service lines.',
            'urls': [
                ('https://www.moh.gov.my/index.php/pages/view/146', 'MOH Clinical Practice Guidelines (CPG)'),
                ('https://www.acadmed.org.my/', 'Academy of Medicine Malaysia'),
                ('https://www.who.int/southeastasia/health-topics', 'WHO SEARO health topics'),
            ],
            'queries': [
                'Which MOH CPGs were revised in the last 6 months? Map each to {name} service lines.',
                'Compare WHO SEARO and MOH guidance on the top 5 conditions by volume at {name}.',
                'Draft a quarterly clinical-guidelines change log for {name} Chief Medical Officer.',
            ],
        },
        {
            'name_tmpl': '{name} Public Health Surveillance Scanner',
            'desc_tmpl': 'Daily scan of KKM CPRC, Kemenkes surveillance, and WHO SEARO outbreak news.',
            'instr_tmpl': 'You are a public-health surveillance analyst for {name}. Source ONLY from the surveillance URLs in knowledge. Cite event + date + source. Output: daily 5-bullet outbreak brief.',
            'urls': [
                ('https://www.moh.gov.my/index.php/pages/view/56', 'KKM CPRC press releases'),
                ('https://www.kemkes.go.id/id/category/berita', 'Kemenkes news'),
                ('https://www.who.int/emergencies/disease-outbreak-news', 'WHO Disease Outbreak News'),
            ],
            'queries': [
                'List the active outbreak signals from KKM and Kemenkes for the last 7 days.',
                'Which events affect {name} catchment areas? Provide a hospital-level exposure read.',
                'Draft a 5-bullet daily public-health surveillance brief for the {name} command centre.',
            ],
        },
    ]
    # Energy / utilities pack
    PACKS['energy'] = [
        {
            'name_tmpl': '{name} Energy Regulator Watch',
            'desc_tmpl': 'Tracks Suruhanjaya Tenaga + ESDM + EMA Singapore policy moves relevant to {name}.',
            'instr_tmpl': 'You are an energy-policy analyst for {name}. Source ONLY from the regulator URLs in knowledge. Cite document + date. Output: weekly policy brief tagged by impact area (tariff / generation / retail / sustainability).',
            'urls': [
                ('https://www.st.gov.my/web/general/announcement', 'Suruhanjaya Tenaga Malaysia announcements'),
                ('https://www.esdm.go.id/en/media-center/news-archives', 'ESDM Indonesia news'),
                ('https://www.ema.gov.sg/news-events/news/media-releases', 'EMA Singapore media releases'),
            ],
            'queries': [
                'Summarise the last 30 days of ST and ESDM announcements relevant to {name}.',
                'List EMA Singapore moves on the wholesale electricity market this quarter.',
                'Draft a weekly policy brief tagged by impact area for the {name} regulatory affairs lead.',
            ],
        },
        {
            'name_tmpl': '{name} Commodity & Tariff Scanner',
            'desc_tmpl': 'Tracks Brent + JKM LNG + EU TTF + ASEAN coal references plus regulated tariff schedules.',
            'instr_tmpl': 'You are a commodity-trends analyst for {name}. Source ONLY from the official commodity and tariff URLs in knowledge. Cite each price + date. Output: monthly commodity scorecard with tariff implications.',
            'urls': [
                ('https://www.eia.gov/petroleum/', 'US EIA petroleum data'),
                ('https://www.tnb.com.my/commercial-industrial/pricing-tariffs1/', 'TNB tariff schedules'),
                ('https://web.pln.co.id/pelanggan/tarif-tenaga-listrik', 'PLN tariff schedules'),
            ],
            'queries': [
                'Pull the last 90 days of Brent, JKM LNG, and TTF prices from EIA and public exchanges.',
                'Show TNB and PLN regulated-tariff revisions over the last 12 months.',
                'Draft a monthly commodity + tariff scorecard for the {name} CFO and trading desk.',
            ],
        },
        {
            'name_tmpl': '{name} Sustainability & Climate Disclosure Scanner',
            'desc_tmpl': 'Tracks Bursa Sustainability + IDX ESG + ISSB + TCFD updates affecting {name}.',
            'instr_tmpl': 'You are a sustainability disclosure analyst for {name}. Source ONLY from the sustainability framework URLs in knowledge. Cite framework + clause + effective date. Output: quarterly disclosure compliance map.',
            'urls': [
                ('https://www.bursamalaysia.com/sustain', 'Bursa Malaysia Sustainability'),
                ('https://www.idx.co.id/en/listed-companies/esg', 'IDX ESG portal'),
                ('https://www.ifrs.org/groups/international-sustainability-standards-board/', 'ISSB (IFRS S1 / S2)'),
            ],
            'queries': [
                'Summarise the latest Bursa + IDX ESG disclosure requirements relevant to {name}.',
                'Map ISSB IFRS S1/S2 clauses to {name} current ESG report — flag the gaps.',
                'Draft a quarterly disclosure compliance map for the {name} sustainability committee.',
            ],
        },
    ]
    # Manufacturing pack
    PACKS['manufacturing'] = [
        {
            'name_tmpl': '{name} Industrial Policy Watch',
            'desc_tmpl': 'Tracks MITI + MIDA + Kemenperin + EDB Singapore policy moves for {name}.',
            'instr_tmpl': 'You are an industrial-policy analyst for {name}. Source ONLY from the agency URLs in knowledge. Cite policy + date. Output: weekly policy brief tagged by impact area (incentives / tariffs / FDI / labour).',
            'urls': [
                ('https://www.miti.gov.my/index.php/pages/view/news', 'MITI Malaysia news'),
                ('https://www.mida.gov.my/media-release/', 'MIDA media releases'),
                ('https://www.kemenperin.go.id/artikel', 'Kemenperin Indonesia articles'),
            ],
            'queries': [
                'Summarise the last 30 days of MITI + MIDA + Kemenperin announcements affecting {name}.',
                'List incentive scheme changes (tax holidays, capex grants) over the last 12 months.',
                'Draft a weekly industrial-policy brief tagged by impact area for the {name} ExCo.',
            ],
        },
        {
            'name_tmpl': '{name} Trade & Tariff Scanner',
            'desc_tmpl': 'Tracks ASEAN FTA + WTO + Customs notices relevant to {name} cross-border flows.',
            'instr_tmpl': 'You are a trade-compliance analyst for {name}. Source ONLY from the trade URLs in knowledge. Cite notice + HS code + date. Output: monthly tariff change log.',
            'urls': [
                ('https://asean.org/our-communities/economic-community/', 'ASEAN Economic Community updates'),
                ('https://www.wto.org/english/news_e/news_e.htm', 'WTO news'),
                ('https://www.customs.gov.my/en/Pages/announcement.aspx', 'Royal Malaysian Customs announcements'),
            ],
            'queries': [
                'Summarise the last 90 days of WTO + ASEAN FTA + Customs notices relevant to {name}.',
                'List HS-code and duty changes affecting {name} top 10 imports / exports.',
                'Draft a monthly tariff and trade change log for the {name} supply chain lead.',
            ],
        },
        {
            'name_tmpl': '{name} Safety & Quality Standards Tracker',
            'desc_tmpl': 'Tracks DOSH + JAS + SIRIM + SNI standard revisions relevant to {name} plants.',
            'instr_tmpl': 'You are a manufacturing standards analyst for {name}. Source ONLY from the standards URLs in knowledge. Cite standard + revision + effective date. Output: change-log of standards with plant-level impact.',
            'urls': [
                ('https://www.dosh.gov.my/index.php/news', 'DOSH Malaysia news'),
                ('https://www.sirim.my/news', 'SIRIM Malaysia news'),
                ('https://www.bsn.go.id/main/berita', 'BSN Indonesia news (SNI)'),
            ],
            'queries': [
                'Summarise the last 90 days of DOSH + SIRIM + BSN announcements relevant to {name}.',
                'List standard revisions affecting {name} plants — flag the ones with hard deadlines.',
                'Draft a quarterly standards change-log with plant-level impact for the {name} plant managers.',
            ],
        },
    ]
    # Agri / plantation pack
    PACKS['agri'] = [
        {
            'name_tmpl': '{name} Plantation Regulator Watch',
            'desc_tmpl': 'Tracks MPOB + Kementerian Pertanian + ISPO + RSPO updates for {name}.',
            'instr_tmpl': 'You are a plantation-policy analyst for {name}. Source ONLY from the agri URLs in knowledge. Cite circular + date. Output: weekly digest tagged by impact area (sustainability / tax / export).',
            'urls': [
                ('https://www.mpob.gov.my/news', 'MPOB news'),
                ('https://ispo.pertanian.go.id/berita', 'ISPO Indonesia news'),
                ('https://rspo.org/news-and-events/', 'RSPO news + events'),
            ],
            'queries': [
                'Summarise the last 30 days of MPOB + ISPO + RSPO announcements relevant to {name}.',
                'List sustainability certification changes affecting {name} concessions.',
                'Draft a weekly plantation policy digest for the {name} Group Sustainability Committee.',
            ],
        },
        {
            'name_tmpl': '{name} Soft Commodity Price Scanner',
            'desc_tmpl': 'Tracks Bursa CPO + ICE Cocoa + Coffee + Sugar references for {name}.',
            'instr_tmpl': 'You are a soft-commodity analyst for {name}. Source ONLY from the public exchange and statistics URLs in knowledge. Cite price + date. Output: monthly commodity scorecard.',
            'urls': [
                ('https://www.bursamalaysia.com/trade/our_products_services/derivatives/equity_n_commodity_derivatives/commodity_derivatives', 'Bursa CPO derivatives'),
                ('https://www.mpob.gov.my/palm-info/daily-palm-oil-prices', 'MPOB daily palm oil prices'),
                ('https://www.bps.go.id/', 'BPS Indonesia agricultural statistics'),
            ],
            'queries': [
                'Pull the last 90 days of CPO daily prices from Bursa and MPOB.',
                'List MPOB and BPS production statistics movements over the last quarter.',
                'Draft a monthly soft-commodity scorecard with production + price for the {name} CFO.',
            ],
        },
        {
            'name_tmpl': '{name} Climate & Weather Risk Scanner',
            'desc_tmpl': 'Tracks Met Malaysia + BMKG + ENSO bulletins for plantation operating conditions.',
            'instr_tmpl': 'You are a climate-risk analyst for {name}. Source ONLY from the meteorological URLs in knowledge. Cite bulletin + date. Output: monthly weather-risk brief tagged by region.',
            'urls': [
                ('https://www.met.gov.my/', 'Met Malaysia'),
                ('https://www.bmkg.go.id/iklim/', 'BMKG climate bulletins'),
                ('https://iri.columbia.edu/our-expertise/climate/forecasts/enso/current/', 'IRI ENSO forecasts'),
            ],
            'queries': [
                'Summarise the latest ENSO and IOD outlooks from IRI and BMKG.',
                'List Met Malaysia and BMKG seasonal outlooks affecting {name} estates.',
                'Draft a monthly weather-risk brief tagged by estate region for the {name} ops team.',
            ],
        },
    ]
    # Retail / FMCG pack
    PACKS['retail'] = [
        {
            'name_tmpl': '{name} Consumer Affairs Watch',
            'desc_tmpl': 'Tracks KPDN + Kemendag + KPKT consumer affairs notices relevant to {name}.',
            'instr_tmpl': 'You are a consumer-affairs analyst for {name}. Source ONLY from the consumer-affairs URLs in knowledge. Cite notice + date. Output: weekly digest tagged by impact area (pricing / labelling / promotions).',
            'urls': [
                ('https://www.kpdn.gov.my/en/media-2/news-2', 'KPDN Malaysia news'),
                ('https://www.kemendag.go.id/berita', 'Kemendag Indonesia news'),
                ('https://www.cccs.gov.sg/media-and-publications/media-releases', 'CCCS Singapore releases'),
            ],
            'queries': [
                'Summarise the last 30 days of KPDN + Kemendag + CCCS announcements relevant to {name}.',
                'List labelling, pricing, and promotion-rule changes affecting {name} stores.',
                'Draft a weekly consumer-affairs digest for the {name} retail compliance lead.',
            ],
        },
        {
            'name_tmpl': '{name} Inflation & Basket Tracker',
            'desc_tmpl': 'Pulls DOSM CPI + BPS CPI + MOM wage data for {name} pricing decisions.',
            'instr_tmpl': 'You are a pricing analyst for {name}. Source ONLY from the statistics URLs in knowledge. Cite indicator + period + value. Output: monthly basket scorecard with elasticity flags.',
            'urls': [
                ('https://www.dosm.gov.my/portal-main/release-content/consumer-price-index', 'DOSM CPI release'),
                ('https://www.bps.go.id/indicator/3/2/1/inflasi.html', 'BPS Indonesia CPI'),
                ('https://stats.mom.gov.sg/Pages/default.aspx', 'MOM Singapore labour stats'),
            ],
            'queries': [
                'Pull the last 12 months of CPI from DOSM and BPS broken down by category.',
                'List wage-growth signals from MOM and DOSM that affect {name} cost base.',
                'Draft a monthly basket scorecard with elasticity flags for the {name} category managers.',
            ],
        },
        {
            'name_tmpl': '{name} E-commerce & Marketplace Pulse',
            'desc_tmpl': 'Tracks Shopee/Lazada/Tokopedia public dashboards + Iprice + DataReportal for {name}.',
            'instr_tmpl': 'You are an e-commerce analyst for {name}. Source ONLY from the public marketplace and analytics URLs in knowledge. Cite dataset + period. Output: monthly marketplace pulse with category share.',
            'urls': [
                ('https://iprice.my/insights/', 'Iprice Insights'),
                ('https://datareportal.com/reports', 'DataReportal regional digital reports'),
                ('https://www.statista.com/markets/423/topic/483/e-commerce/', 'Statista e-commerce snapshots'),
            ],
            'queries': [
                'Summarise the latest DataReportal regional digital reports for {name} markets.',
                'Pull the latest Iprice Insights leaderboards relevant to {name} categories.',
                'Draft a monthly marketplace pulse with category share movements for the {name} digital lead.',
            ],
        },
    ]
    # Hospitality / property pack
    PACKS['hospitality'] = [
        {
            'name_tmpl': '{name} Travel & Tourism Pulse',
            'desc_tmpl': 'Tracks Tourism Malaysia + Kemenparekraf + STB Singapore arrival statistics.',
            'instr_tmpl': 'You are a tourism-trends analyst for {name}. Source ONLY from the tourism URLs in knowledge. Cite indicator + period + source. Output: monthly demand pulse with origin-market mix.',
            'urls': [
                ('https://www.tourism.gov.my/statistics', 'Tourism Malaysia statistics'),
                ('https://kemenparekraf.go.id/statistik/', 'Kemenparekraf statistics'),
                ('https://www.stb.gov.sg/content/stb/en/statistics-and-market-research/statistics-and-market-research.html', 'STB Singapore statistics'),
            ],
            'queries': [
                'Summarise the last 6 months of arrival statistics from Tourism Malaysia + Kemenparekraf + STB.',
                'Identify the top 5 origin markets growing fastest for {name} catchment.',
                'Draft a monthly demand pulse with origin-market mix for the {name} commercial team.',
            ],
        },
        {
            'name_tmpl': '{name} Property Market Tracker',
            'desc_tmpl': 'Tracks NAPIC + JPP + REI + URA property market reports for {name}.',
            'instr_tmpl': 'You are a property-market analyst for {name}. Source ONLY from the property-stats URLs in knowledge. Cite report + period + value. Output: quarterly market scorecard.',
            'urls': [
                ('https://napic2.jpph.gov.my/en/', 'NAPIC Malaysia'),
                ('https://www.rei.or.id/', 'REI Indonesia'),
                ('https://www.ura.gov.sg/Corporate/Media-Room/Media-Releases', 'URA Singapore releases'),
            ],
            'queries': [
                'Summarise the latest NAPIC + REI + URA property reports relevant to {name}.',
                'List the segments showing softening / strengthening for {name} type of asset.',
                'Draft a quarterly property scorecard for the {name} development committee.',
            ],
        },
        {
            'name_tmpl': '{name} Hospitality Operations Benchmark',
            'desc_tmpl': 'Tracks STR + MAH + PHRI public hospitality benchmark releases.',
            'instr_tmpl': 'You are a hospitality benchmark analyst for {name}. Source ONLY from the hospitality association URLs in knowledge. Cite benchmark + period. Output: monthly RevPAR / ADR / occupancy scorecard.',
            'urls': [
                ('https://www.hotels.org.my/', 'MAH (Malaysian Association of Hotels)'),
                ('https://www.phri.or.id/', 'PHRI Indonesia'),
                ('https://www.shla.org.sg/', 'SHLA Singapore Hotel Association'),
            ],
            'queries': [
                'Summarise the latest hospitality benchmark releases from MAH + PHRI + SHLA.',
                'Pull occupancy / ADR / RevPAR signals relevant to {name} portfolio segments.',
                'Draft a monthly RevPAR / ADR / occupancy scorecard for the {name} operations head.',
            ],
        },
    ]
    # Telco / tech / media pack
    PACKS['telco-tech'] = [
        {
            'name_tmpl': '{name} Telecoms Regulator Watch',
            'desc_tmpl': 'Tracks MCMC + Kominfo + IMDA spectrum and licensing announcements for {name}.',
            'instr_tmpl': 'You are a telecoms-regulatory analyst for {name}. Source ONLY from the telco regulator URLs in knowledge. Cite circular + date. Output: weekly digest tagged by impact area (spectrum / licensing / consumer / cyber).',
            'urls': [
                ('https://www.mcmc.gov.my/en/media/announcements', 'MCMC announcements'),
                ('https://www.kominfo.go.id/content/all/siaran_pers', 'Kominfo press releases'),
                ('https://www.imda.gov.sg/resources/press-releases-factsheets-and-speeches', 'IMDA Singapore'),
            ],
            'queries': [
                'Summarise the last 30 days of MCMC + Kominfo + IMDA announcements relevant to {name}.',
                'List spectrum and licensing changes affecting {name} access network.',
                'Draft a weekly telecoms regulatory digest for the {name} regulatory affairs lead.',
            ],
        },
        {
            'name_tmpl': '{name} Cyber & Data Protection Scanner',
            'desc_tmpl': 'Tracks PDP Commissioner + Pusat KKD + PDPC Singapore + ENISA enforcement and guidance.',
            'instr_tmpl': 'You are a cyber & privacy analyst for {name}. Source ONLY from the privacy regulator URLs in knowledge. Cite enforcement + date. Output: monthly enforcement digest plus advisory list.',
            'urls': [
                ('https://www.pdp.gov.my/jpdpv2/announcements/', 'JPDP Malaysia announcements'),
                ('https://pdp.id/', 'Indonesia PDP advocacy + UU PDP updates'),
                ('https://www.pdpc.gov.sg/news-and-events', 'PDPC Singapore news'),
            ],
            'queries': [
                'Summarise the last 90 days of PDP and PDPC enforcement and advisory items relevant to {name}.',
                'List the breaches and fines published in {name} markets — extract the lessons.',
                'Draft a monthly cyber + privacy enforcement digest for the {name} CISO and DPO.',
            ],
        },
        {
            'name_tmpl': '{name} Digital Adoption Scanner',
            'desc_tmpl': 'Tracks DataReportal + DOSM ICT + BPS ICT + Statista regional adoption snapshots.',
            'instr_tmpl': 'You are a digital-adoption analyst for {name}. Source ONLY from the digital adoption URLs in knowledge. Cite dataset + period. Output: quarterly digital adoption scorecard.',
            'urls': [
                ('https://datareportal.com/reports/digital-2025-malaysia', 'DataReportal Malaysia'),
                ('https://datareportal.com/reports/digital-2025-indonesia', 'DataReportal Indonesia'),
                ('https://www.dosm.gov.my/portal-main/release-content/use-of-internet', 'DOSM ICT use of internet'),
            ],
            'queries': [
                'Pull the latest DataReportal Malaysia and Indonesia digital snapshots relevant to {name}.',
                'List DOSM ICT indicators that have moved meaningfully in the last 12 months.',
                'Draft a quarterly digital adoption scorecard for the {name} digital strategy lead.',
            ],
        },
    ]
    # Transport / logistics pack
    PACKS['transport'] = [
        {
            'name_tmpl': '{name} Transport Regulator Watch',
            'desc_tmpl': 'Tracks APAD + MAVCOM + Kemenhub + LTA Singapore announcements relevant to {name}.',
            'instr_tmpl': 'You are a transport-regulatory analyst for {name}. Source ONLY from the transport regulator URLs in knowledge. Cite circular + date. Output: weekly digest tagged by mode (road / rail / aviation / maritime).',
            'urls': [
                ('https://www.apad.gov.my/en/announcements', 'APAD Malaysia announcements'),
                ('https://www.mavcom.my/en/media/news/', 'MAVCOM Malaysia news'),
                ('https://dephub.go.id/post/list/0', 'Kemenhub Indonesia news'),
            ],
            'queries': [
                'Summarise the last 30 days of APAD + MAVCOM + Kemenhub announcements relevant to {name}.',
                'List route, fare, and licensing changes affecting {name} operations.',
                'Draft a weekly transport-regulatory digest for the {name} ops director.',
            ],
        },
        {
            'name_tmpl': '{name} Trade Lane & Freight Pulse',
            'desc_tmpl': 'Tracks port authorities + IATA + IMO + Drewry public reports for {name}.',
            'instr_tmpl': 'You are a freight-lane analyst for {name}. Source ONLY from the public freight URLs in knowledge. Cite indicator + period. Output: monthly trade-lane scorecard.',
            'urls': [
                ('https://www.mpa.gov.sg/web/portal/home/maritime-singapore', 'MPA Singapore maritime data'),
                ('https://www.penangport.com.my/', 'Penang Port public statistics'),
                ('https://www.iata.org/en/pressroom/', 'IATA press room'),
            ],
            'queries': [
                'Summarise the last quarter of IATA pressroom releases relevant to {name}.',
                'Pull MPA Singapore and Penang Port volume statistics relevant to {name} lanes.',
                'Draft a monthly trade-lane scorecard with capacity + rate signals for the {name} commercial team.',
            ],
        },
        {
            'name_tmpl': '{name} Fuel & Carbon Tracker',
            'desc_tmpl': 'Tracks PetrolPrice + ICAO CORSIA + IMO sulphur cap updates for transport ops.',
            'instr_tmpl': 'You are a fuel + carbon analyst for {name}. Source ONLY from the URLs in knowledge. Cite price / scheme + date. Output: monthly fuel + carbon brief.',
            'urls': [
                ('https://www.petrolpriceonline.com/', 'Malaysia retail fuel price tracker'),
                ('https://www.icao.int/environmental-protection/CORSIA/Pages/default.aspx', 'ICAO CORSIA'),
                ('https://www.imo.org/en/MediaCentre/PressBriefings/Pages/Default.aspx', 'IMO press briefings'),
            ],
            'queries': [
                'Pull the last 6 months of retail fuel prices from PetrolPriceOnline relevant to {name}.',
                'Summarise the latest ICAO CORSIA and IMO sulphur cap updates relevant to {name}.',
                'Draft a monthly fuel and carbon brief for the {name} CFO and operations head.',
            ],
        },
    ]
    # Public sector / government pack
    PACKS['public-sector'] = [
        {
            'name_tmpl': '{name} Government Policy Watch',
            'desc_tmpl': 'Tracks PMO + Kementerian Kewangan + Kemenkeu announcements relevant to {name}.',
            'instr_tmpl': 'You are a government-policy analyst for {name}. Source ONLY from the public-sector URLs in knowledge. Cite policy + date. Output: weekly digest tagged by impact area.',
            'urls': [
                ('https://www.pmo.gov.my/news/', 'PMO Malaysia news'),
                ('https://www.mof.gov.my/portal/en/news/press-citations', 'Kementerian Kewangan Malaysia'),
                ('https://www.kemenkeu.go.id/publikasi/siaran-pers', 'Kemenkeu Indonesia press'),
            ],
            'queries': [
                'Summarise the last 30 days of PMO + MOF + Kemenkeu announcements relevant to {name}.',
                'List budget and grant programme changes affecting {name}.',
                'Draft a weekly government-policy digest tagged by impact area for the {name} Group Strategy.',
            ],
        },
        {
            'name_tmpl': '{name} Procurement & Tender Scanner',
            'desc_tmpl': 'Tracks ePerolehan + LPSE Indonesia + GeBIZ Singapore tender portals.',
            'instr_tmpl': 'You are a public-procurement analyst for {name}. Source ONLY from the tender portal URLs in knowledge. Cite tender ID + agency + closing date. Output: weekly opportunity list.',
            'urls': [
                ('https://www.eperolehan.gov.my/', 'ePerolehan Malaysia'),
                ('https://lpse.kemenkeu.go.id/eproc/lelang', 'LPSE Indonesia (Kemenkeu)'),
                ('https://www.gebiz.gov.sg/', 'GeBIZ Singapore'),
            ],
            'queries': [
                'List the live tenders on ePerolehan + LPSE + GeBIZ relevant to {name} capabilities.',
                'Identify the top 5 expiring this week and the top 5 worth highest value.',
                'Draft a weekly tender opportunity list with bid / no-bid recommendation for the {name} BD lead.',
            ],
        },
        {
            'name_tmpl': '{name} Statistical Brief Builder',
            'desc_tmpl': 'Builds briefs from DOSM + BPS + DOS Singapore official statistics.',
            'instr_tmpl': 'You are a statistics-brief builder for {name}. Source ONLY from the official statistics URLs in knowledge. Cite dataset + period + value. Output: monthly statistical brief in plain language.',
            'urls': [
                ('https://www.dosm.gov.my/portal-main/landingv2', 'DOSM landing'),
                ('https://www.bps.go.id/', 'BPS Indonesia'),
                ('https://www.singstat.gov.sg/find-data', 'DOS Singapore find data'),
            ],
            'queries': [
                'Pull the headline indicators from DOSM, BPS, and DOS Singapore for the last 6 months.',
                'Identify the indicators most material to {name} mandate.',
                'Draft a monthly statistical brief in plain language for the {name} senior management.',
            ],
        },
    ]
    # Departments — generic group pack
    PACKS['departments'] = [
        {
            'name_tmpl': '{name} Best-Practice Scanner',
            'desc_tmpl': 'Pulls Big-4 + association best-practice publications relevant to {name}.',
            'instr_tmpl': 'You are a best-practice analyst for the {name} function. Source ONLY from the practitioner URLs in knowledge. Cite publisher + title + date. Output: monthly best-practice digest with adoption recommendation.',
            'urls': [
                ('https://www.mckinsey.com/featured-insights', 'McKinsey featured insights'),
                ('https://www2.deloitte.com/global/en/insights.html', 'Deloitte Insights'),
                ('https://hbr.org/topic/subject/leadership', 'HBR leadership topics'),
            ],
            'queries': [
                'Summarise the latest McKinsey, Deloitte, and HBR publications relevant to {name}.',
                'Identify the 3 practices most worth piloting at {name} this quarter.',
                'Draft a monthly best-practice digest with adoption recommendations for the {name} lead.',
            ],
        },
        {
            'name_tmpl': '{name} Regulator & Standards Watch',
            'desc_tmpl': 'Tracks regional standard-setters + regulators relevant to {name} mandate.',
            'instr_tmpl': 'You are a {name} regulatory analyst. Source ONLY from the standard-setter URLs in knowledge. Cite standard + revision + effective date. Output: monthly compliance digest.',
            'urls': [
                ('https://www.ifrs.org/news-and-events/news/', 'IFRS Foundation news'),
                ('https://www.ifac.org/news-events', 'IFAC news + events'),
                ('https://www.iia.org.my/', 'Institute of Internal Auditors Malaysia'),
            ],
            'queries': [
                'Summarise the last 90 days of IFRS, IFAC, and IIA Malaysia announcements relevant to {name}.',
                'List standard revisions affecting {name} processes — flag the ones with hard deadlines.',
                'Draft a monthly compliance digest with proposed actions for the {name} lead.',
            ],
        },
        {
            'name_tmpl': '{name} Peer Function Benchmark',
            'desc_tmpl': 'Tracks public peer-function disclosures + association surveys for {name}.',
            'instr_tmpl': 'You are a peer-function benchmarker for {name}. Source ONLY from the survey + association URLs in knowledge. Cite survey + period. Output: quarterly benchmark with delta-vs-peers.',
            'urls': [
                ('https://www.gartner.com/en/insights', 'Gartner insights'),
                ('https://www.pwc.com/gx/en/services/consulting.html', 'PwC consulting insights'),
                ('https://www.weforum.org/agenda/', 'World Economic Forum agenda'),
            ],
            'queries': [
                'Pull the latest Gartner, PwC, and WEF publications benchmarking {name} maturity.',
                'Identify {name} top-3 gaps vs peer functions disclosed publicly.',
                'Draft a quarterly peer-function benchmark with delta-vs-peers for the {name} lead.',
            ],
        },
    ]


def _entry_pack_map():
    """Map every known entry id (industries + departments) to a PACK key."""
    if ENTRY_PACK:
        return ENTRY_PACK
    banking = [
        'banking', 'banking-malaysia', 'banking-indonesia', 'investment-banking',
        'islamic-banking', 'cooperative-banking', 'mortgage-finance',
        'cross-border-remittance', 'fintech-payments', 'commercial-banking',
        'financial-regulator',
    ]
    insurance = [
        'insurance', 'takaful-malaysia', 'insurance-indonesia', 'takaful',
        'reinsurance', 'health-insurance', 'general-insurance', 'life-insurance',
    ]
    healthcare = [
        'hospital-network', 'pharmaceutical', 'medical-devices',
        'health-insurance-svcs', 'aged-care',
    ]
    energy = [
        'og-upstream', 'og-downstream', 'renewable-energy',
        'power-utilities', 'mining-coal', 'rare-earth', 'coal-mining',
    ]
    manufacturing = [
        'industrial-manufacturing', 'food-fmcg', 'rubber-gloves',
        'auto-tyres', 'semiconductor', 'electronics-mfg', 'automotive',
        'construction',
    ]
    agri = [
        'plantation', 'agritech', 'fisheries-aquaculture',
    ]
    retail = [
        'retail-grocery', 'retail-luxury', 'consumer-goods',
    ]
    hospitality = [
        'hospitality', 'property-development', 'reit-realestate',
        'hotel-resort', 'property-reit',
    ]
    telco_tech = [
        'telco', 'media-entertainment', 'ecommerce-superapp',
        'edtech-saas', 'data-center-cloud', 'bpo-services',
    ]
    transport = [
        'aviation-airlines', 'maritime-shipping', 'logistics-courier',
        'rail-mass-transit', 'logistics-3pl', 'aviation-airports',
    ]
    public_sector = [
        'government-agency', 'sovereign-wealth', 'state-owned-conglomerate',
        'general', 'glc-investment', 'diversified-conglomerate',
    ]
    edu = [
        'education',
    ]
    for k in banking:
        ENTRY_PACK[k] = 'banking'
    for k in insurance:
        ENTRY_PACK[k] = 'insurance'
    for k in healthcare:
        ENTRY_PACK[k] = 'healthcare'
    for k in energy:
        ENTRY_PACK[k] = 'energy'
    for k in manufacturing:
        ENTRY_PACK[k] = 'manufacturing'
    for k in agri:
        ENTRY_PACK[k] = 'agri'
    for k in retail:
        ENTRY_PACK[k] = 'retail'
    for k in hospitality:
        ENTRY_PACK[k] = 'hospitality'
    for k in telco_tech:
        ENTRY_PACK[k] = 'telco-tech'
    for k in transport:
        ENTRY_PACK[k] = 'transport'
    for k in public_sector:
        ENTRY_PACK[k] = 'public-sector'
    for k in edu:
        ENTRY_PACK[k] = 'public-sector'
    # Departments
    for k in [
        'dept-finance', 'dept-hr', 'dept-it-digital', 'dept-marketing',
        'dept-legal', 'dept-corpsec', 'dept-strategy', 'dept-operations',
        'dept-investor-relations', 'dept-procurement', 'dept-esg', 'dept-risk',
    ]:
        ENTRY_PACK[k] = 'departments'
    return ENTRY_PACK


def render_agents_free(entry_id, name):
    """Return list of free-tier (URL knowledge) agent dicts for given entry id + display name."""
    _build_packs()
    mapping = _entry_pack_map()
    pack_key = mapping.get(entry_id, 'departments')
    pack = PACKS.get(pack_key) or PACKS['departments']
    # Per-entry URL overrides — each industry / department gets its own knowledge sources
    try:
        from _builder_free_urls import get_urls as _get_entry_urls
        from _builder_free_urls import get_agent_meta as _get_entry_meta
    except Exception:
        _get_entry_urls = lambda *a, **kw: None
        _get_entry_meta = lambda *a, **kw: None
    agents = []
    for i, arch in enumerate(pack):
        meta = _get_entry_meta(entry_id, i) or {}
        name_tmpl = meta.get('name_tmpl', arch['name_tmpl'])
        desc_tmpl = meta.get('desc_tmpl', arch['desc_tmpl'])
        instr_tmpl = meta.get('instr_tmpl', arch['instr_tmpl'])
        queries_tmpl = meta.get('queries', arch['queries'])
        nm = name_tmpl.format(name=name)
        urls = _get_entry_urls(entry_id, i) or arch['urls']
        a = {
            'icon': '🆓',
            'label': nm,
            'name': nm,
            'desc': desc_tmpl.format(name=name),
            'instructions': instr_tmpl.format(name=name),
            'knowledge': [{'url': u, 'note': n} for (u, n) in urls],
            'knowledgeNote': 'Free Copilot Chat supports PUBLIC URLs only — no SharePoint, OneDrive, or file uploads.',
            'queries': [q.format(name=name) for q in queries_tmpl],
        }
        agents.append(a)
    return agents


def render_agents_free_id(entry_id, name):
    """Indonesia / Bahasa Indonesia overlay — same agents, light wording adjustment."""
    base = render_agents_free(entry_id, name)
    out = []
    for a in base:
        a2 = dict(a)
        a2['desc'] = a['desc'].replace('relevant to', 'yang relevan dengan')
        a2['instructions'] = (
            'Anda adalah analis yang mendukung ' + name + '. ' +
            'Gunakan HANYA URL publik yang tercantum sebagai pengetahuan. ' +
            'Selalu kutip sumber + tanggal + URL. Jangan berspekulasi melampaui yang tertulis.'
        )
        a2['queries'] = [q.replace('Summarise', 'Ringkas')
                         .replace('List ', 'Buat daftar ')
                         .replace('Draft ', 'Susun draf ')
                         .replace('Pull ', 'Tarik ')
                         .replace('Compare ', 'Bandingkan ')
                         .replace('Identify ', 'Identifikasi ')
                         .replace('Which ', 'Mana ')
                         for q in a['queries']]
        out.append(a2)
    return out
