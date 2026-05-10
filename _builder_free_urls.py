# Per-entry URL overrides for the free-tier (Copilot Chat) Agent Builder catalog.
#
# User feedback: "the agent builder for free license one... why the website all
# the same one... it should be different for different industries no???"
#
# Diagnosis: _builder_free_catalog.py defines 12 PACKS (banking, insurance,
# healthcare, energy, manufacturing, agri, retail, hospitality, telco-tech,
# transport, public-sector, departments). Each pack's 3 archetypes share the
# SAME 3 URLs across every entry that maps to that pack — so all 9 banking
# entries (commercial-banking / islamic-banking / fintech-payments / mortgage-
# finance / cross-border-remittance / etc.) get the IDENTICAL 9 URLs.
#
# Fix: define a per-entry-id URL override table. Each entry maps to up to 3
# archetype URL groups (one per pack archetype). Each archetype gives 3 unique
# (url, note) tuples that match THAT specific industry / department subdomain.
# Render falls back to the pack default if an entry isn't overridden.

# Helper short-hands for url groups that repeat across entries (rare —
# kept minimal so each entry's URLs really are entry-specific).
_ASEAN_DISCLOSURES = [
    ('https://www.bursamalaysia.com/market_information/announcements/company_announcement', 'Bursa Malaysia listed-co announcements'),
    ('https://www.idx.co.id/en/news/announcement/', 'IDX listed-co disclosures'),
    ('https://www.sgx.com/securities/company-announcements', 'SGX company announcements'),
]


ENTRY_URLS = {
    # ── Banking & Finance ────────────────────────────────────────────────
    'commercial-banking': [
        [
            ('https://www.bnm.gov.my/banking-sector', 'BNM banking supervision policy documents'),
            ('https://www.ojk.go.id/id/kanal/perbankan/Pages/default.aspx', 'OJK Perbankan Konvensional regulations'),
            ('https://www.mas.gov.sg/regulation/banking', 'MAS banking regulations & circulars'),
        ],
        [
            ('https://www.bursamalaysia.com/market_information/listed_companies/list_of_companies/main_market', 'Bursa Main Market — Banking sector'),
            ('https://www.idx.co.id/en/listed-companies/listed-stock-summary/', 'IDX listed banks summary'),
            ('https://www.sgx.com/research-education/sectors-stocks/financial-services', 'SGX banking & finance sector'),
        ],
        [
            ('https://www.bnm.gov.my/-/monthly-highlights-statistics-msb', 'BNM Monthly Statistical Bulletin (banking indicators)'),
            ('https://www.bi.go.id/id/publikasi/laporan/Default.aspx?id=SEKI', 'Bank Indonesia banking statistics (SEKI)'),
            ('https://www.ram.com.my/insights/sector-research', 'RAM Ratings banking sector outlook'),
        ],
    ],
    'investment-banking': [
        [
            ('https://www.sc.com.my/regulation/guidelines', 'Securities Commission Malaysia capital-markets guidelines'),
            ('https://www.ojk.go.id/en/kanal/pasar-modal/regulasi/Default.aspx', 'OJK Pasar Modal regulations'),
            ('https://www.mas.gov.sg/regulation/capital-markets', 'MAS capital markets regulation'),
        ],
        [
            ('https://www.bursamalaysia.com/market_information/equities_prices', 'Bursa Malaysia capital-markets data'),
            ('https://www.idx.co.id/en/listed-companies/ipo-pipeline/', 'IDX IPO pipeline'),
            ('https://www.sgx.com/securities/securities-products/listings', 'SGX recent listings & IPOs'),
        ],
        [
            ('https://www.asifma.org/research/', 'ASIFMA Asia capital-markets research'),
            ('https://www.icmagroup.org/', 'ICMA Asia bond markets'),
            ('https://www.ifre.com/', 'IFR Asia syndicated lending & DCM'),
        ],
    ],
    'islamic-banking': [
        [
            ('https://www.bnm.gov.my/islamic-banking-takaful', 'BNM Islamic banking & takaful policy'),
            ('https://www.ojk.go.id/id/kanal/syariah/Pages/default.aspx', 'OJK Perbankan Syariah'),
            ('https://aaoifi.com/standard/?lang=en', 'AAOIFI Shariah standards'),
        ],
        [
            ('https://www.bursamalaysia.com/market_information/equities_prices?legend[]=[S]', 'Bursa Malaysia Shariah-compliant securities'),
            ('https://www.idx.co.id/en/products/index/?_idx=jii', 'IDX Jakarta Islamic Index (JII)'),
            ('https://www.ifsb.org/published.php', 'IFSB published standards & stability reports'),
        ],
        [
            ('https://www.isra.my/publication.html', 'ISRA Islamic-finance research'),
            ('https://www.iifm.net/sukuk-reports/', 'IIFM Sukuk Report (annual)'),
            ('https://www.bnm.gov.my/-/monthly-highlights-statistics-isb', 'BNM Islamic banking monthly statistics'),
        ],
    ],
    'mortgage-finance': [
        [
            ('https://www.bnm.gov.my/property-market', 'BNM property-finance policy & TDSR rules'),
            ('https://www.ojk.go.id/id/kanal/perbankan/Pages/default.aspx', 'OJK KPR (mortgage) regulations'),
            ('https://www.mas.gov.sg/regulation/Notices/Notice-632', 'MAS Notice 632 — Residential property loans (TDSR)'),
        ],
        [
            ('https://www.cagamas.com.my/', 'Cagamas (Malaysian secondary mortgage corp)'),
            ('https://napic2.jpph.gov.my/en', 'NAPIC Malaysian property market reports'),
            ('https://rehda.com/', 'REHDA Malaysian property developer survey'),
        ],
        [
            ('https://www.dosm.gov.my/portal-main/release-content/malaysian-house-price-index-mhpi', 'DOSM Malaysian House Price Index'),
            ('https://www.bps.go.id/subject/14/perumahan.html', 'BPS Indonesia housing & property statistics'),
            ('https://www.ura.gov.sg/Corporate/Media-Room/Media-Releases', 'URA Singapore property price index releases'),
        ],
    ],
    'cross-border-remittance': [
        [
            ('https://www.bnm.gov.my/money-services-business', 'BNM Money Services Business framework'),
            ('https://www.ojk.go.id/id/kanal/iknb/Pages/transfer-dana.aspx', 'OJK Penyelenggara Transfer Dana'),
            ('https://www.mas.gov.sg/regulation/payments', 'MAS Payment Services Act (cross-border)'),
        ],
        [
            ('https://www.visa.com.my/about-visa/visa-economic-empowerment-institute.html', 'Visa Economic Empowerment Institute SEA'),
            ('https://www.mastercard.com/news/insights/2024/new-payments-index/', 'Mastercard New Payments Index Asia'),
            ('https://www.knomad.org/data/remittances', 'KNOMAD World Bank remittance data'),
        ],
        [
            ('https://www.worldbank.org/en/topic/migrationremittancesdiasporaissues/brief/migration-remittances-data', 'World Bank Migration & Remittances brief'),
            ('https://www.bis.org/cpmi/', 'BIS CPMI cross-border payments programme'),
            ('https://www.imf.org/en/Topics/imf-and-the-policy-network-on-financial-issues/sdr', 'IMF SDR & FX rates'),
        ],
    ],
    'fintech-payments': [
        [
            ('https://www.bnm.gov.my/digital-banks-electronic-money', 'BNM Electronic Money issuers list'),
            ('https://www.ojk.go.id/id/kanal/iknb/Pages/Inovasi-Keuangan-Digital.aspx', 'OJK Inovasi Keuangan Digital sandbox'),
            ('https://www.mas.gov.sg/regulation/payments/payment-services-act', 'MAS Payment Services Act licensees'),
        ],
        [
            ('https://www.fintechnews.my/', 'Fintech News Malaysia'),
            ('https://aftech.or.id/', 'AFTECH Indonesian fintech association'),
            ('https://singaporefintech.org/', 'Singapore Fintech Association'),
        ],
        [
            ('https://www.bis.org/about/bisih/', 'BIS Innovation Hub research papers'),
            ('https://www.imf.org/en/Topics/fintech', 'IMF Fintech Notes'),
            ('https://www.afi-global.org/publications/', 'AFI financial-inclusion reports'),
        ],
    ],
    'financial-regulator': [
        [
            ('https://www.imf.org/en/Publications/FSAP', 'IMF Financial Sector Assessment Program'),
            ('https://www.bis.org/bcbs/publications.htm', 'BIS Basel Committee publications'),
            ('https://www.fatf-gafi.org/en/publications.html', 'FATF AML/CFT publications'),
        ],
        [
            ('https://www.bursamalaysia.com/regulation/listing_requirements', 'Bursa listing requirements'),
            ('https://www.ojk.go.id/en/regulasi/Pages/default.aspx', 'OJK regulations portal'),
            ('https://www.mas.gov.sg/regulation/notices', 'MAS notices & circulars'),
        ],
        [
            ('https://www.worldbank.org/en/country/malaysia/overview', 'World Bank Malaysia country reports'),
            ('https://www.imf.org/en/Countries/IDN', 'IMF Indonesia Article IV consultations'),
            ('https://www.oecd.org/economy/surveys/', 'OECD Indonesia economic surveys'),
        ],
    ],
    'cooperative-banking': [
        [
            ('https://www.bnm.gov.my/development-financial-institutions', 'BNM development financial institutions framework'),
            ('https://www.skm.gov.my/', 'Suruhanjaya Koperasi Malaysia'),
            ('https://depkop.go.id/', 'Kementerian Koperasi UKM Indonesia'),
        ],
        [
            ('https://www.angkasa.coop/', 'ANGKASA Malaysian cooperatives apex'),
            ('https://www.bankrakyat.com.my/about-us/news-events', 'Bank Rakyat Malaysia announcements'),
            ('https://www.icaap.coop/', 'ICA Asia-Pacific cooperative news'),
        ],
        [
            ('https://www.ica.coop/en/cooperatives/facts-and-figures', 'International Co-operative Alliance facts'),
            ('https://www.adb.org/sectors/finance/main', 'ADB inclusive finance reports'),
            ('https://www.afi-global.org/policy-areas/digital-financial-services/', 'AFI digital financial services policy'),
        ],
    ],

    # ── Insurance ────────────────────────────────────────────────────────
    'general-insurance': [
        [
            ('https://www.bnm.gov.my/insurance-takaful', 'BNM Insurance & Takaful policy documents'),
            ('https://www.ojk.go.id/en/kanal/iknb/Pages/Insurance.aspx', 'OJK IKNB Insurance regulations'),
            ('https://www.mas.gov.sg/regulation/insurance', 'MAS Insurance Act & guidelines'),
        ],
        [
            ('https://www.piam.org.my/news-publications/', 'PIAM (General Insurance Assoc Msia) publications'),
            ('https://aaui.or.id/publikasi/', 'AAUI Indonesia general-insurance association'),
            ('https://www.gia.org.sg/news-publications', 'GIA Singapore general-insurance association'),
        ],
        [
            ('https://www.swissre.com/institute/research/sigma-research.html', 'Swiss Re Sigma series'),
            ('https://www.munichre.com/en/insights/natural-disaster-and-climate-change.html', 'Munich Re NatCat reports'),
            ('https://www.aon.com/insights/reports', 'Aon insurance market insights'),
        ],
    ],
    'life-insurance': [
        [
            ('https://www.bnm.gov.my/-/risk-based-capital-framework-for-insurers', 'BNM RBC framework for insurers'),
            ('https://www.ojk.go.id/id/kanal/iknb/data-dan-statistik/asuransi/Default.aspx', 'OJK IKNB life-insurance statistics'),
            ('https://www.mas.gov.sg/regulation/insurance/notices', 'MAS life insurance notices'),
        ],
        [
            ('https://www.liam.org.my/publications/', 'LIAM Life Insurance Association of Malaysia'),
            ('https://aaji.or.id/publikasi/', 'AAJI Indonesia life-insurance association'),
            ('https://www.lia.org.sg/industry/industry-news/', 'LIA Singapore life-insurance association'),
        ],
        [
            ('https://www.swissre.com/institute/research/topics-and-risk-dialogues/health-and-longevity.html', 'Swiss Re mortality & longevity research'),
            ('https://www.worldbank.org/en/topic/financialinclusion/brief/global-pension-database', 'World Bank pension & insurance database'),
            ('https://www.oecd.org/finance/insurance/', 'OECD insurance statistics'),
        ],
    ],
    'takaful': [
        [
            ('https://www.bnm.gov.my/-/operational-framework-for-takaful', 'BNM Operational Framework for Takaful'),
            ('https://www.ojk.go.id/id/kanal/syariah/data-dan-statistik/asuransi-syariah/Default.aspx', 'OJK Asuransi Syariah statistics'),
            ('https://malaysiantakaful.com.my/publications/', 'Malaysian Takaful Association publications'),
        ],
        [
            ('https://www.isra.my/publication.html', 'ISRA Islamic insurance research'),
            ('https://www.ifsb.org/published.php', 'IFSB takaful stability indicators'),
            ('https://aaoifi.com/standard/?lang=en', 'AAOIFI Takaful standards'),
        ],
        [
            ('https://www.milliman.com/en/products/global-takaful-report', 'Milliman Global Takaful Report'),
            ('https://www.swissre.com/institute/research/topics-and-risk-dialogues/financial-and-monetary-policy.html', 'Swiss Re Takaful & emerging markets'),
            ('https://www.bnm.gov.my/-/monthly-highlights-statistics-isb', 'BNM Islamic finance monthly statistics'),
        ],
    ],
    'reinsurance': [
        [
            ('https://www.bnm.gov.my/insurance-takaful', 'BNM reinsurance & retakaful framework'),
            ('https://www.ojk.go.id/en/kanal/iknb/Pages/Reasuransi.aspx', 'OJK reasuransi regulations'),
            ('https://www.mas.gov.sg/regulation/insurance/regulations', 'MAS reinsurance regulations'),
        ],
        [
            ('https://www.malaysianre.com.my/publications/', 'Malaysian Re publications'),
            ('https://www.indonesiare.co.id/en/publications', 'Indonesia Re publications'),
            ('https://www.singaporere.com/news', 'Singapore Re news'),
        ],
        [
            ('https://www.swissre.com/institute/research.html', 'Swiss Re Institute reinsurance research'),
            ('https://www.munichre.com/en/insights.html', 'Munich Re reinsurance insights'),
            ('https://www.lloyds.com/about-lloyds/research/research-reports', "Lloyd's of London research reports"),
        ],
    ],
    'health-insurance': [
        [
            ('https://www.bnm.gov.my/-/medical-and-health-insurance-takaful', 'BNM Medical & Health Insurance/Takaful'),
            ('https://bpjs-kesehatan.go.id/bpjs/index.php/post/read/2014/1/Regulasi', 'BPJS Kesehatan regulations'),
            ('https://www.moh.gov.sg/policies-and-legislation/medishield-life', 'MOH Singapore MediShield Life policy'),
        ],
        [
            ('https://www.aphm.org.my/', 'APHM private hospitals association'),
            ('https://persi.or.id/', 'PERSI Indonesian hospital association'),
            ('https://www.singaporeinsurance.com.sg/', 'GIA-MOH integrated shield insurers'),
        ],
        [
            ('https://www.who.int/health-topics/health-financing', 'WHO health financing reports'),
            ('https://www.oecd.org/health/health-systems/health-data.htm', 'OECD health data'),
            ('https://data.worldbank.org/indicator/SH.XPD.CHEX.GD.ZS', 'World Bank health expenditure data'),
        ],
    ],

    # ── Healthcare ───────────────────────────────────────────────────────
    'hospital-network': [
        [
            ('https://www.moh.gov.my/index.php/database_stores/store_view/17', 'MOH Malaysia private healthcare establishments'),
            ('https://yankes.kemkes.go.id/regulasi', 'Kemenkes Indonesia health-services regulations'),
            ('https://www.moh.gov.sg/policies-and-legislation/healthcare-services-act', 'MOH Singapore Healthcare Services Act'),
        ],
        [
            ('https://www.aphm.org.my/news-events/', 'APHM Association of Private Hospitals Malaysia news'),
            ('https://persi.or.id/berita/', 'PERSI Indonesian Hospital Association news'),
            ('https://www.healthxchange.sg/news', 'SingHealth healthcare-network news'),
        ],
        [
            ('https://www.who.int/westernpacific/publications', 'WHO Western Pacific publications'),
            ('https://www.oecd.org/health/health-data.htm', 'OECD health statistics'),
            ('https://www.frost.com/research/industry/healthcare/', 'Frost & Sullivan healthcare reports'),
        ],
    ],
    'pharmaceutical': [
        [
            ('https://www.npra.gov.my/index.php/en/announcement.html', 'NPRA Malaysia drug-registration announcements'),
            ('https://www.pom.go.id/new/index.php/view/berita', 'BPOM Indonesia drug-control announcements'),
            ('https://www.hsa.gov.sg/announcements', 'HSA Singapore therapeutic-products announcements'),
        ],
        [
            ('https://phama.org.my/', 'PhAMA Pharmaceutical Association of Malaysia'),
            ('https://www.gpfarmasi.org/', 'GP Farmasi Indonesia association'),
            ('https://www.sapi.org.sg/', 'SAPI Singapore Association of Pharmaceutical Industries'),
        ],
        [
            ('https://www.iqvia.com/insights/the-iqvia-institute', 'IQVIA Asia-Pacific reports'),
            ('https://www.frost.com/research/industry/pharmaceutical/', 'Frost & Sullivan pharma reports'),
            ('https://www.who.int/teams/regulation-prequalification/regulation-and-safety/medicines-and-vaccines', 'WHO Prequalification of Medicines'),
        ],
    ],
    'medical-devices': [
        [
            ('https://mdb.moh.gov.my/news-and-announcements', 'MDA Malaysia Medical Device Authority announcements'),
            ('https://www.kemkes.go.id/folder/view/01/structure-publikasi-pusat-1-alat-kesehatan.html', 'Kemenkes Indonesia medical-device regulation'),
            ('https://www.hsa.gov.sg/medical-devices', 'HSA Singapore medical devices'),
        ],
        [
            ('https://www.amdi.org.my/', 'AMDI Malaysian medical devices industry'),
            ('https://gakeslab.id/', 'GAKESLAB Indonesia association of medical-device producers'),
            ('https://www.smdtia.org.sg/', 'SMDTIA Singapore medical-device association'),
        ],
        [
            ('https://www.imdrf.org/documents.html', 'IMDRF International Medical Device Regulators Forum'),
            ('https://www.fda.gov/medical-devices/products-and-medical-procedures/asia-pacific', 'US FDA medical-device guidance'),
            ('https://www.frost.com/research/industry/medical-devices-imaging/', 'Frost & Sullivan medical-devices reports'),
        ],
    ],
    'aged-care': [
        [
            ('https://www.jkm.gov.my/jkm/', 'JKM Department of Social Welfare Malaysia (aged-care licensing)'),
            ('https://kemensos.go.id/', 'Kemensos Indonesia social affairs aged-care'),
            ('https://www.aic.sg/care-services', 'AIC Singapore aged-care services framework'),
        ],
        [
            ('https://www.aphm.org.my/', 'APHM aged-care division'),
            ('https://persi.or.id/', 'PERSI Indonesia long-term care'),
            ('https://www.aic.sg/news', 'AIC Singapore news & alerts'),
        ],
        [
            ('https://www.who.int/ageing/en/', 'WHO Ageing & Life Course'),
            ('https://www.oecd.org/els/health-systems/long-term-care.htm', 'OECD long-term care reports'),
            ('https://www.adb.org/themes/social-development/aging-population', 'ADB ageing population reports'),
        ],
    ],
    'health-insurance-svcs': [
        [
            ('https://www.bnm.gov.my/-/medical-and-health-insurance-takaful', 'BNM medical & health insurance framework'),
            ('https://bpjs-kesehatan.go.id/', 'BPJS Kesehatan regulations'),
            ('https://www.moh.gov.sg/policies-and-legislation/medishield-life', 'MOH Singapore MediShield Life'),
        ],
        [
            ('https://www.liam.org.my/medical/', 'LIAM medical-insurance committee'),
            ('https://aaji.or.id/asuransi-kesehatan/', 'AAJI Indonesia health-insurance products'),
            ('https://www.lia.org.sg/industry/our-members/', 'LIA Singapore IP/MediShield insurers'),
        ],
        [
            ('https://www.who.int/health-topics/universal-health-coverage', 'WHO universal health coverage'),
            ('https://www.oecd.org/els/health-systems/health-spending.htm', 'OECD health-spending statistics'),
            ('https://data.worldbank.org/topic/health', 'World Bank health indicators'),
        ],
    ],

    # ── Energy ───────────────────────────────────────────────────────────
    'og-upstream': [
        [
            ('https://www.petronas.com/our-business/upstream', 'Petronas upstream Malaysia portal'),
            ('https://www.skkmigas.go.id/en/news', 'SKK Migas Indonesia upstream news & data'),
            ('https://www.dosh.gov.my/index.php/legislation/petroleum-act', 'DOSH Malaysia petroleum-safety legislation'),
        ],
        [
            ('https://www.petronas.com/media/media-releases', 'Petronas activity outlook & releases'),
            ('https://www.skkmigas.go.id/en/page/work-program-and-budget', 'SKK Migas WP&B activity tracking'),
            ('https://www.offshore-energy.biz/category/asia-oceania/', 'Offshore Energy Asia-Oceania news'),
        ],
        [
            ('https://www.opec.org/opec_web/en/publications/202.htm', 'OPEC Monthly Oil Market Report'),
            ('https://www.eia.gov/outlooks/steo/', 'EIA Short-Term Energy Outlook'),
            ('https://www.iea.org/reports/oil-market-report', 'IEA Oil Market Report'),
        ],
    ],
    'og-downstream': [
        [
            ('https://www.bpdp.or.id/en/regulations', 'BPDPKS Indonesia palm-oil & biofuel subsidies'),
            ('https://www.kpdn.gov.my/portal/index.php/en/announcements/news', 'KPDN Malaysia downstream pricing announcements'),
            ('https://www.ema.gov.sg/regulations-licences-publications.aspx', 'EMA Singapore downstream-fuels licensing'),
        ],
        [
            ('https://www.petronas.com/our-business/downstream', 'Petronas downstream operations'),
            ('https://www.pertamina.com/en/news-room', 'Pertamina downstream news'),
            ('https://www.src.com.sg/about-src/news-and-media', 'Singapore Refining Company news'),
        ],
        [
            ('https://www.theice.com/marketdata/reports/355', 'ICE Brent & Asian crack spreads'),
            ('https://www.iata.org/en/programs/ops-infra/fuel/fuel-monitor/', 'IATA jet-fuel price monitor'),
            ('https://www.argusmedia.com/en/oil-products', 'Argus Asia oil-products report'),
        ],
    ],
    'renewable-energy': [
        [
            ('https://www.seda.gov.my/regulatory/', 'SEDA Malaysia renewable-energy regulations'),
            ('https://www.esdm.go.id/en/regulations', 'KemESDM Indonesia EBTKE renewable regulations'),
            ('https://www.ema.gov.sg/SolarUploadingPlatform.aspx', 'EMA Singapore solar regulations'),
        ],
        [
            ('https://www.tnb.com.my/sustainability', 'TNB Malaysia renewables portfolio'),
            ('https://web.pln.co.id/cms/sustainability/', 'PLN Indonesia ESG & renewables'),
            ('https://www.sembcorp.com/en/sustainability', 'Sembcorp Singapore renewables portfolio'),
        ],
        [
            ('https://www.irena.org/publications', 'IRENA renewable-energy reports'),
            ('https://www.iea.org/reports/renewables-2024', 'IEA Renewables annual'),
            ('https://about.bnef.com/asia-pacific/', 'BloombergNEF Asia Pacific clean-energy'),
        ],
    ],
    'power-utilities': [
        [
            ('https://www.st.gov.my/en/web/general/announcement', 'Suruhanjaya Tenaga Malaysia announcements'),
            ('https://www.esdm.go.id/en/regulations', 'KemESDM Indonesia electricity regulations'),
            ('https://www.ema.gov.sg/regulations-licences-publications.aspx', 'EMA Singapore electricity licensing'),
        ],
        [
            ('https://www.tnb.com.my/announcements/', 'TNB Malaysia announcements'),
            ('https://web.pln.co.id/media/siaran-pers', 'PLN Indonesia press releases'),
            ('https://www.sptel.com.sg/about-sp-group/news-and-resources', 'SP Group Singapore news'),
        ],
        [
            ('https://www.iea.org/reports/electricity-market-report-2024', 'IEA Electricity Market Report'),
            ('https://www.adb.org/sectors/energy/main', 'ADB Asia energy reports'),
            ('https://www.spglobal.com/commodityinsights/en/our-methodology/price-assessments/electric-power', 'S&P Platts electric-power price assessments'),
        ],
    ],
    'coal-mining': [
        [
            ('https://www.minerals.gov.my/', 'JMG Malaysia mineral/coal regulator'),
            ('https://www.minerba.esdm.go.id/', 'KemESDM Indonesia mineral & coal directorate'),
            ('https://www.icmm.com/en-gb/about-us', 'ICMM mining-industry framework'),
        ],
        [
            ('https://apbi-icma.org/news/', 'APBI Indonesia coal-producers association'),
            ('https://www.malaysiaminerals.com/', 'Malaysian Mining Industry portal'),
            ('https://www.iccaaustralia.com.au/news', 'International Coal Council news'),
        ],
        [
            ('https://www.spglobal.com/commodityinsights/en/our-methodology/price-assessments/coal', 'S&P Platts coal price assessments'),
            ('https://www.argusmedia.com/en/coal', 'Argus Coal Daily International'),
            ('https://www.woodmac.com/our-expertise/focus/Metals--Mining/coal/', 'Wood Mackenzie coal market reports'),
        ],
    ],
    'rare-earth': [
        [
            ('https://www.aelb.gov.my/aelbv2/?p=8485', 'AELB Malaysia atomic-energy/rare-earth licensing'),
            ('https://www.minerba.esdm.go.id/', 'KemESDM Indonesia rare-earth directorate'),
            ('https://www.usgs.gov/centers/national-minerals-information-center/rare-earths-statistics-and-information', 'USGS rare-earth statistics'),
        ],
        [
            ('https://www.lynasrareearths.com/investors/announcements/', 'Lynas Rare Earths announcements'),
            ('https://www.minerba.esdm.go.id/', 'Indonesia mineral & coal monthly statistics'),
            ('https://en.cnia.com.cn/', 'China Rare Earth Industry Association news'),
        ],
        [
            ('https://www.argusmedia.com/en/metals/rare-earths', 'Argus Rare Earths assessments'),
            ('https://www.woodmac.com/our-expertise/focus/Metals--Mining/rare-earth-elements/', 'Wood Mackenzie REE reports'),
            ('https://www.iea.org/reports/critical-minerals-market-review-2024', 'IEA Critical Minerals Market Review'),
        ],
    ],

    # ── Manufacturing ────────────────────────────────────────────────────
    'industrial-manufacturing': [
        [
            ('https://www.dosh.gov.my/index.php/legislation', 'DOSH Malaysia OSH Act regulations'),
            ('https://kemenperin.go.id/regulasi', 'Kemenperin Indonesia manufacturing regulations'),
            ('https://www.mom.gov.sg/workplace-safety-and-health', 'MOM Singapore Workplace Safety & Health'),
        ],
        [
            ('https://www.fmm.org.my/news-events.aspx', 'FMM Federation of Manufacturers Malaysia news'),
            ('https://www.kadin.id/news/', 'Kadin Indonesia chamber news'),
            ('https://www.smfederation.org.sg/news/', 'SMF Singapore Manufacturing Federation news'),
        ],
        [
            ('https://www.spglobal.com/marketintelligence/en/mi/products/asean-pmi.html', 'S&P Global ASEAN Manufacturing PMI'),
            ('https://www.ismworld.org/supply-management-news-and-reports/reports/ism-report-on-business/', 'ISM Manufacturing PMI'),
            ('https://data.worldbank.org/indicator/NV.IND.MANF.ZS', 'World Bank manufacturing value-added stats'),
        ],
    ],
    'food-fmcg': [
        [
            ('https://www.moh.gov.my/index.php/pages/view/2179', 'MOH Malaysia Food Safety & Quality Division'),
            ('https://www.pom.go.id/new/index.php/view/peraturan', 'BPOM Indonesia food regulations'),
            ('https://www.sfa.gov.sg/food-information/regulations', 'Singapore Food Agency regulations'),
        ],
        [
            ('https://halal.gov.my/v4/', 'JAKIM Halal Hub portal'),
            ('https://gapmmi.id/page/news', 'GAPMMI Indonesia food & beverage association'),
            ('https://smfederation.org.sg/group/sma/', 'Singapore Manufacturers Association food chapter'),
        ],
        [
            ('https://www.nielsen.com/insights/?_pubdate=last-12&_topic=fmcg-and-retail', 'Nielsen FMCG insights'),
            ('https://www.euromonitor.com/our-expertise/packaged-food', 'Euromonitor packaged-food reports'),
            ('https://www.kantarworldpanel.com/global', 'Kantar Worldpanel global FMCG'),
        ],
    ],
    'rubber-gloves': [
        [
            ('https://www.margma.com.my/', 'MARGMA Malaysian Rubber Glove Mfg Association'),
            ('https://www.lgm.gov.my/', 'Lembaga Getah Malaysia rubber industry regulator'),
            ('https://www.fda.gov/medical-devices/general-hospital-devices-and-supplies/medical-gloves', 'US FDA 21 CFR 880 medical gloves'),
        ],
        [
            ('https://www.margma.com.my/category/news/', 'MARGMA monthly export & production stats'),
            ('https://www.gapkindo.org/news', 'GAPKINDO Indonesian rubber association'),
            ('https://www.rubberstudy.org/welcome', 'IRSG International Rubber Study Group'),
        ],
        [
            ('https://www.frost.com/research/industry/healthcare/medical-devices/medical-gloves/', 'Frost & Sullivan glove-market reports'),
            ('https://www.rubberstudy.org/statistics-publications', 'IRSG rubber statistical bulletin'),
            ('https://www.lgm.gov.my/maklumat-statistik/perangkaan-getah/', 'LGM monthly rubber statistics'),
        ],
    ],
    'auto-tyres': [
        [
            ('https://www.jpj.gov.my/en/announcement', 'JPJ Malaysia Road Transport Department'),
            ('https://kemenperin.go.id/', 'Kemenperin Indonesia automotive industry'),
            ('https://www.lta.gov.sg/content/ltagov/en/newsroom.html', 'LTA Singapore newsroom'),
        ],
        [
            ('https://www.maa.org.my/news.html', 'MAA Malaysian Automotive Association sales data'),
            ('https://www.gaikindo.or.id/', 'GAIKINDO Indonesian automotive association'),
            ('https://www.mida.gov.my/sectors/automotive/', 'MIDA automotive sector portal'),
        ],
        [
            ('https://www.oica.net/category/production-statistics/', 'OICA production statistics'),
            ('https://www.aaf-asean.com/news', 'ASEAN Automotive Federation news'),
            ('https://www.wardsauto.com/', "Ward's Auto industry news"),
        ],
    ],
    'semiconductor': [
        [
            ('https://www.mosti.gov.my/web/en/', 'MOSTI Malaysia National Semiconductor Strategy'),
            ('https://kemenperin.go.id/', 'Kemenperin Indonesia Industri 4.0 semiconductor'),
            ('https://www.edb.gov.sg/en/about-edb/media-releases-publications.html', 'EDB Singapore semiconductor releases'),
        ],
        [
            ('https://www.semi.org/en/connect/regions/southeast-asia', 'SEMI Southeast Asia industry group'),
            ('https://www.mida.gov.my/sectors/electrical-electronics/', 'MIDA E&E sector portal'),
            ('https://www.asti.or.id/', 'ASTI Indonesia electronics association'),
        ],
        [
            ('https://www.gartner.com/en/industries/high-tech/semiconductors', 'Gartner Semiconductor research'),
            ('https://www.idc.com/getdoc.jsp?containerId=IDC_P39788', 'IDC Worldwide Semiconductor Tracker'),
            ('https://www.wsts.org/76/Recent-News-Release', 'WSTS World Semiconductor Trade Statistics'),
        ],
    ],
    'electronics-mfg': [
        [
            ('https://www.mosti.gov.my/web/en/', 'MOSTI Malaysia electronics strategy'),
            ('https://kemenperin.go.id/', 'Kemenperin Indonesia electronics directorate'),
            ('https://www.imda.gov.sg/regulations-and-licensing-listing/electronic-equipment-listing', 'IMDA Singapore electronics regulation'),
        ],
        [
            ('https://www.mida.gov.my/sectors/electrical-electronics/', 'MIDA Electrical & Electronics sector'),
            ('https://gabel.or.id/', 'GABEL Indonesia electronics association'),
            ('https://www.ipi.org.sg/', 'IPI Singapore electronics & precision'),
        ],
        [
            ('https://www.idc.com/promo/global-electronics', 'IDC Worldwide Electronics Tracker'),
            ('https://www.gartner.com/en/industries/high-tech', 'Gartner High-Tech research'),
            ('https://www.statista.com/markets/418/topic/479/consumer-electronics/', 'Statista consumer electronics'),
        ],
    ],

    # ── Agriculture & Plantation ────────────────────────────────────────
    'plantation': [
        [
            ('https://www.mpob.gov.my/regulatory/policies-and-rulings', 'MPOB Malaysia palm-oil policies'),
            ('https://www.bpdp.or.id/en/regulations', 'BPDPKS Indonesia palm-oil board regulations'),
            ('https://rspo.org/resources/standards/', 'RSPO sustainability standards'),
        ],
        [
            ('https://www.bursamalaysia.com/market_information/listed_companies/list_of_companies/main_market', 'Bursa Plantation listed cos'),
            ('https://gapki.id/news', 'GAPKI Indonesian palm-oil producers'),
            ('https://www.mpoa.org.my/news.html', 'MPOA Malaysian Palm Oil Association news'),
        ],
        [
            ('https://www.fas.usda.gov/regions/southeast-asia', 'USDA FAS Southeast Asia attaché reports'),
            ('https://mpoc.org.my/market-info/', 'MPOC market intelligence'),
            ('https://www.worldbank.org/en/research/commodity-markets', 'World Bank commodity markets'),
        ],
    ],
    'agritech': [
        [
            ('https://www.doa.gov.my/index.php/en/', 'Department of Agriculture Malaysia'),
            ('https://www.pertanian.go.id/', 'Kementerian Pertanian Indonesia'),
            ('https://www.sfa.gov.sg/animal-fish/farming-in-singapore', 'Singapore Food Agency urban-farming'),
        ],
        [
            ('https://www.mardi.gov.my/index.php/en/', 'MARDI Malaysian Agricultural Research Institute'),
            ('https://www.bsi.bappenas.go.id/', 'Bappenas Indonesia agritech innovation'),
            ('https://www.a-star.edu.sg/Research/Research-Initiatives/agritech', 'A*STAR Singapore agritech research'),
        ],
        [
            ('https://www.fao.org/asiapacific/perspectives/agritech/en/', 'FAO Asia Pacific agritech perspectives'),
            ('https://www.adb.org/sectors/agriculture-food-security/main', 'ADB agriculture & food-security reports'),
            ('https://www.cgiar.org/news-events/news/', 'CGIAR international agriculture research'),
        ],
    ],
    'fisheries-aquaculture': [
        [
            ('https://www.dof.gov.my/en/', 'Department of Fisheries Malaysia'),
            ('https://kkp.go.id/', 'Kementerian Kelautan & Perikanan Indonesia'),
            ('https://www.sfa.gov.sg/animal-fish/aquaculture', 'SFA Singapore aquaculture regulation'),
        ],
        [
            ('https://www.malaysianaquaculture.com/', 'Malaysian Aquaculture network news'),
            ('https://shrimpclubindonesia.org/', 'Shrimp Club Indonesia'),
            ('https://www.aquatraining.com/', 'Aqua training & industry news'),
        ],
        [
            ('https://www.fao.org/fishery/en/sofia', 'FAO State of World Fisheries & Aquaculture'),
            ('https://www.seafdec.org/publications/', 'SEAFDEC Southeast Asian fisheries reports'),
            ('https://www.worldbank.org/en/topic/oceans-fisheries-and-coastal-economies', 'World Bank oceans & fisheries'),
        ],
    ],

    # ── Retail & Consumer ────────────────────────────────────────────────
    'retail-grocery': [
        [
            ('https://www.kpdn.gov.my/portal/index.php/en/announcements/news', 'KPDN Malaysia consumer-affairs announcements'),
            ('https://www.kemendag.go.id/', 'Kemendag Indonesia trade ministry'),
            ('https://www.enterprisesg.gov.sg/news', 'Enterprise Singapore retail news'),
        ],
        [
            ('https://www.mra.com.my/', 'MRA Malaysia Retailers Association'),
            ('https://aprindo.id/news/', 'APRINDO Indonesian retail association'),
            ('https://www.sra.org.sg/news-resources', 'SRA Singapore Retailers Association'),
        ],
        [
            ('https://www.nielsen.com/insights/?_topic=fmcg-and-retail', 'Nielsen retail insights'),
            ('https://www.euromonitor.com/our-expertise/retailing', 'Euromonitor retailing reports'),
            ('https://www.kantar.com/inspiration/retail', 'Kantar retail trends'),
        ],
    ],
    'retail-luxury': [
        [
            ('https://www.kpdn.gov.my/portal/', 'KPDN Malaysia luxury-goods consumer affairs'),
            ('https://www.kemendag.go.id/', 'Kemendag Indonesia luxury-import duties'),
            ('https://www.enterprisesg.gov.sg/news', 'Enterprise Singapore luxury retail trends'),
        ],
        [
            ('https://www.tourism.gov.my/statistics', 'Tourism Malaysia spend statistics'),
            ('https://www.kemenparekraf.go.id/', 'Kemenparekraf Indonesia luxury & lifestyle'),
            ('https://www.stb.gov.sg/content/stb/en/statistics-and-market-research.html', 'STB Singapore visitor-spend'),
        ],
        [
            ('https://www.bain.com/insights/topics/luxury-goods/', 'Bain Luxury Goods Worldwide Market Study'),
            ('https://www.statista.com/markets/420/topic/485/luxury-goods/', 'Statista luxury-goods market'),
            ('https://www.mckinsey.com/industries/retail/our-insights', 'McKinsey luxury retail insights'),
        ],
    ],
    'consumer-goods': [
        [
            ('https://www.kpdn.gov.my/portal/index.php/en/', 'KPDN Malaysia consumer-affairs portal'),
            ('https://www.kemendag.go.id/', 'Kemendag Indonesia trade ministry'),
            ('https://www.cccs.gov.sg/news/recent-news', 'CCCS Singapore consumer-protection news'),
        ],
        [
            ('https://www.fmm.org.my/news-events.aspx', 'FMM Malaysia consumer-goods chapter'),
            ('https://gapmmi.id/page/news', 'GAPMMI Indonesia FMCG association'),
            ('https://smfederation.org.sg/group/sma/', 'SMA Singapore consumer-products group'),
        ],
        [
            ('https://www.euromonitor.com/our-expertise/packaged-food', 'Euromonitor consumer-goods reports'),
            ('https://www.nielsen.com/insights/', 'Nielsen consumer-insights'),
            ('https://www.kantar.com/north-america/inspiration/consumer-goods', 'Kantar consumer-goods trends'),
        ],
    ],

    # ── Hospitality & Property ───────────────────────────────────────────
    'hotel-resort': [
        [
            ('https://www.motac.gov.my/en/announcements/news', 'MOTAC Malaysia tourism & culture announcements'),
            ('https://www.kemenparekraf.go.id/berita', 'Kemenparekraf Indonesia tourism & creative news'),
            ('https://www.stb.gov.sg/content/stb/en/about-stb/newsroom.html', 'STB Singapore tourism news'),
        ],
        [
            ('https://www.mahotels.org/news.html', 'MAH Malaysian Association of Hotels news'),
            ('https://phri.or.id/news', 'PHRI Indonesia hotel & restaurant association'),
            ('https://www.sha.org.sg/news', 'SHA Singapore Hotel Association news'),
        ],
        [
            ('https://str.com/data-insights-blog', 'STR hotel performance reports'),
            ('https://skift.com/asia/', 'Skift Asia travel-industry news'),
            ('https://www.jll.com.sg/en/research', 'JLL Asia hotels & hospitality research'),
        ],
    ],
    'property-development': [
        [
            ('https://napic2.jpph.gov.my/en', 'NAPIC Malaysia property market reports'),
            ('https://pu.go.id/regulasi-bangunan-gedung', 'Kementerian PUPR Indonesia building regulations'),
            ('https://www.ura.gov.sg/Corporate/Media-Room/Media-Releases', 'URA Singapore property releases'),
        ],
        [
            ('https://rehda.com/news/', 'REHDA Malaysian property developers news'),
            ('https://www.rei.or.id/news', 'REI Indonesian property developers association'),
            ('https://www.redas.com/news', 'REDAS Singapore developers association'),
        ],
        [
            ('https://www.jll.com.my/en/research', 'JLL Asia Pacific property research'),
            ('https://www.knightfrank.com.my/research', 'Knight Frank Asia property reports'),
            ('https://www.colliers.com/en-my/research', 'Colliers Asia property research'),
        ],
    ],
    'property-reit': [
        [
            ('https://www.sc.com.my/regulation/guidelines/reits', 'SC Malaysia REIT Guidelines'),
            ('https://www.ojk.go.id/id/kanal/pasar-modal/Pages/dire.aspx', 'OJK DIRE (Indonesian REIT) regulations'),
            ('https://www.mas.gov.sg/regulation/codes/code-on-collective-investment-schemes', 'MAS Code on Collective Investment Schemes (S-REITs)'),
        ],
        [
            ('https://www.bursamalaysia.com/market_information/equities_prices?board=REIT', 'Bursa Malaysian REITs'),
            ('https://www.idx.co.id/en/products/structured-warrant-and-others/dire/', 'IDX KIK-DIRE Indonesian REITs'),
            ('https://www.sgx.com/securities/reits', 'SGX S-REITs index'),
        ],
        [
            ('https://www.aprea.asia/research/', 'APREA Asia Pacific REIT statistics'),
            ('https://www.jll.com.sg/en/research', 'JLL REIT research'),
            ('https://www.epra.com/research', 'EPRA NAREIT Asia REIT data'),
        ],
    ],

    # ── Telco / Tech ─────────────────────────────────────────────────────
    'telco': [
        [
            ('https://www.mcmc.gov.my/en/legal/policies', 'MCMC Malaysia telco policies'),
            ('https://www.kominfo.go.id/index.php/all_content/regulation', 'Kominfo Indonesia telco regulations'),
            ('https://www.imda.gov.sg/regulations-and-licensing-listing/telecommunications', 'IMDA Singapore telco licensing'),
        ],
        [
            ('https://www.mcmc.gov.my/en/resources/statistics', 'MCMC quarterly telco statistics'),
            ('https://atsi.or.id/', 'ATSI Indonesian Telco Association'),
            ('https://www.gsma.com/asiapacific/news/', 'GSMA Asia Pacific telco news'),
        ],
        [
            ('https://www.gsma.com/mobileeconomy/asia-pacific/', 'GSMA Mobile Economy Asia Pacific'),
            ('https://omdia.tech.informa.com/topic-pages/telecoms', 'Omdia telecoms research'),
            ('https://www.itu.int/en/ITU-D/Statistics/Pages/publications/world.aspx', 'ITU World Telecommunication Indicators'),
        ],
    ],
    'media-entertainment': [
        [
            ('https://www.mcmc.gov.my/en/legal/codes', 'MCMC Malaysia content codes'),
            ('https://www.kominfo.go.id/', 'Kominfo Indonesia broadcast regulations'),
            ('https://www.imda.gov.sg/regulations-and-licensing-listing/content-standards-and-classification', 'IMDA Singapore content standards'),
        ],
        [
            ('https://www.atvm.org.my/', 'ATVM Malaysia free-to-air broadcasters'),
            ('https://atvsi.or.id/', 'ATVSI Indonesia private broadcasters'),
            ('https://asec.sg/', 'ASEC Asian Subscription TV association'),
        ],
        [
            ('https://www.pwc.com/gx/en/industries/tmt/media/outlook.html', 'PwC Global Entertainment & Media Outlook'),
            ('https://wearesocial.com/asia-pacific/', 'We Are Social Asia digital reports'),
            ('https://www.statista.com/markets/417/topic/489/media/', 'Statista media-industry data'),
        ],
    ],
    'ecommerce-superapp': [
        [
            ('https://www.kpdn.gov.my/portal/index.php/en/announcements', 'KPDN Malaysia e-commerce consumer protection'),
            ('https://www.kemendag.go.id/', 'Kemendag Indonesia e-commerce regulations'),
            ('https://www.imda.gov.sg/regulations-and-licensing-listing', 'IMDA Singapore digital-services licensing'),
        ],
        [
            ('https://mdec.my/news/', 'MDEC Malaysia digital economy news'),
            ('https://idea.or.id/', 'idEA Indonesian e-commerce association'),
            ('https://www.asme.org.sg/news/', 'ASME Singapore digital SMEs news'),
        ],
        [
            ('https://www.bain.com/insights/topics/southeast-asias-internet-economy/', 'Bain SEA Internet Economy report'),
            ('https://services.google.com/fh/files/misc/e_conomy_sea_2023_report.pdf', 'Google e-Conomy SEA report'),
            ('https://www.techinasia.com/', 'Tech in Asia daily news'),
        ],
    ],
    'edtech-saas': [
        [
            ('https://www.mqa.gov.my/portalmqav3/', 'MQA Malaysia accreditation regulations'),
            ('https://www.kemdikbud.go.id/main/blog', 'Kemendikbud Indonesia education news'),
            ('https://www.moe.gov.sg/education-news', 'MOE Singapore education news'),
        ],
        [
            ('https://www.mdec.my/', 'MDEC EdTech catalysts'),
            ('https://aftech.or.id/', 'AFTECH Indonesian edtech sandbox'),
            ('https://www.scs.org.sg/', 'SCS Singapore Computer Society edtech'),
        ],
        [
            ('https://www.holoniq.com/notes', 'HolonIQ global education insights'),
            ('https://www.gartner.com/en/industries/education', 'Gartner education-technology research'),
            ('https://www.idc.com/getdoc.jsp?containerId=IDC_P22241', 'IDC Worldwide EdTech Spending Guide'),
        ],
    ],
    'data-center-cloud': [
        [
            ('https://www.mcmc.gov.my/en/sectors/data-protection', 'MCMC Malaysia data-centre & cloud policies'),
            ('https://www.kominfo.go.id/content/all/regulation', 'Kominfo Indonesia PSE/data-centre regulations'),
            ('https://www.imda.gov.sg/regulations-and-licensing-listing/data-centre-call-for-application', 'IMDA Singapore data-centre licensing'),
        ],
        [
            ('https://www.mdec.my/digital-economy/', 'MDEC Malaysia data-centre clusters'),
            ('https://aptiknas.or.id/news', 'APTIKNAS Indonesia ICT/data-centre association'),
            ('https://www.scs.org.sg/cloud-it-asia/news', 'SCS cloud Asia news'),
        ],
        [
            ('https://www.gartner.com/en/industries/high-tech/cloud', 'Gartner Cloud research'),
            ('https://www.idc.com/promo/cloud', 'IDC Worldwide Cloud Tracker'),
            ('https://451research.com/research/data-centers', '451 Research data-centre intelligence'),
        ],
    ],

    # ── Transport ────────────────────────────────────────────────────────
    'aviation-airlines': [
        [
            ('https://www.mavcom.my/en/', 'MAVCOM Malaysian Aviation Commission announcements'),
            ('https://hubud.dephub.go.id/hubud/website/Berita', 'Kemenhub Indonesia DGCA aviation news'),
            ('https://www.caas.gov.sg/who-we-are/newsroom', 'CAAS Singapore newsroom'),
        ],
        [
            ('https://www.aapairlines.org/news.aspx', 'AAPA Association of Asia Pacific Airlines'),
            ('https://www.inaca.or.id/', 'INACA Indonesian airlines association'),
            ('https://www.iata.org/en/pressroom/', 'IATA newsroom'),
        ],
        [
            ('https://www.iata.org/en/publications/store/airlines-financial-monitor/', 'IATA Airlines Financial Monitor'),
            ('https://www.icao.int/Newsroom/Pages/default.aspx', 'ICAO newsroom & guidance'),
            ('https://www.oag.com/blog', 'OAG schedule analysis blog'),
        ],
    ],
    'maritime-shipping': [
        [
            ('https://www.marine.gov.my/', 'Marine Department Malaysia'),
            ('https://hubla.dephub.go.id/home/news', 'Kemenhub Indonesia maritime news'),
            ('https://www.mpa.gov.sg/web/portal/home/about-mpa/news-publications', 'MPA Singapore news & publications'),
        ],
        [
            ('https://www.masa.org.my/news/', 'MASA Malaysia Shipowners Association'),
            ('https://www.dpp-insa.com/', 'INSA Indonesian Shipowners Association'),
            ('https://www.ssa.org.sg/news/', 'SSA Singapore Shipping Association'),
        ],
        [
            ('https://www.bimco.org/news', 'BIMCO maritime market reports'),
            ('https://www.drewry.co.uk/', 'Drewry container & shipping research'),
            ('https://www.clarksons.com/research/', 'Clarksons shipping intelligence'),
        ],
    ],
    'logistics-3pl': [
        [
            ('https://www.customs.gov.my/en/Pages/index.aspx', 'Royal Malaysian Customs (RMCD)'),
            ('https://www.beacukai.go.id/', 'Bea Cukai Indonesia customs'),
            ('https://www.customs.gov.sg/news-and-media', 'Singapore Customs news'),
        ],
        [
            ('https://fmff.com.my/news-and-events/', 'FMFF Malaysia Federation of Freight Forwarders'),
            ('https://alfi.or.id/news', 'ALFI Indonesian logistics association'),
            ('https://www.sla.org.sg/news/', 'SLA Singapore Logistics Association'),
        ],
        [
            ('https://lpi.worldbank.org/', 'World Bank Logistics Performance Index'),
            ('https://www.mds-transmodal.com/', 'MDS Transmodal logistics analysis'),
            ('https://www.kearney.com/global-logistics-outlook', 'A.T. Kearney Global Logistics Outlook'),
        ],
    ],
    'rail-mass-transit': [
        [
            ('https://www.apad.gov.my/en/', 'APAD Land Public Transport Agency Malaysia'),
            ('https://djka.dephub.go.id/', 'Kemenhub Indonesia DJKA railway directorate'),
            ('https://www.lta.gov.sg/content/ltagov/en/newsroom.html', 'LTA Singapore newsroom'),
        ],
        [
            ('https://www.ktmb.com.my/news.html', 'KTMB Malaysian railway news'),
            ('https://www.kai.id/information/single/keterangan-pers', 'KAI Indonesia rail news'),
            ('https://www.smrt.com.sg/News', 'SMRT Singapore news'),
        ],
        [
            ('https://www.uic.org/com/enews/', 'UIC International Union of Railways news'),
            ('https://www.uitp.org/news/asia-pacific/', 'UITP public-transport reports'),
            ('https://www.adb.org/themes/transport/main', 'ADB transport sector reports'),
        ],
    ],

    # ── Public sector & special ─────────────────────────────────────────
    'government-agency': [
        [
            ('https://www.pmo.gov.my/2019/07/announcement/', 'PMO Malaysia announcements'),
            ('https://setkab.go.id/category/berita/', 'Sekretariat Kabinet Indonesia news'),
            ('https://www.pmo.gov.sg/Newsroom', 'PMO Singapore newsroom'),
        ],
        [
            ('https://data.worldbank.org/country/MY', 'World Bank Malaysia open data'),
            ('https://www.imf.org/en/Countries/IDN', 'IMF Indonesia country reports'),
            ('https://www.adb.org/publications/asia-bond-monitor', 'ADB Asia Bond Monitor'),
        ],
        [
            ('https://www.dosm.gov.my/portal-main/release-content/', 'DOSM Malaysia statistical releases'),
            ('https://www.bps.go.id/pressrelease.html', 'BPS Indonesia press releases'),
            ('https://www.singstat.gov.sg/whats-new/news', 'SingStat Singapore news'),
        ],
    ],
    'sovereign-wealth': [
        [
            ('https://www.khazanah.com.my/news-publications/', 'Khazanah Nasional publications'),
            ('https://www.pnb.com.my/announcement.html', 'PNB Malaysia announcements'),
            ('https://www.ina.go.id/news', 'INA Indonesia Investment Authority news'),
        ],
        [
            ('https://www.temasek.com.sg/en/news-and-resources', 'Temasek news & resources'),
            ('https://www.gic.com.sg/en/newsroom/', 'GIC Singapore newsroom'),
            ('https://www.adia.ae/en/news-publications', 'ADIA Abu Dhabi news (peer)'),
        ],
        [
            ('https://www.swfinstitute.org/research/sovereign-wealth-fund', 'SWF Institute sovereign-wealth fund rankings'),
            ('https://www.ifswf.org/publications-page', 'IFSWF International Forum of SWFs publications'),
            ('https://www.worldbank.org/en/topic/sovereign-wealth-funds', 'World Bank SWF research'),
        ],
    ],
    'state-owned-conglomerate': [
        [
            ('https://www.mof.gov.my/portal/en/announcement/news', 'MOF Inc Malaysia GLC announcements'),
            ('https://www.bumn.go.id/page/berita/all', 'Kementerian BUMN Indonesia state-owned news'),
            ('https://www.mof.gov.sg/news-publications', 'MOF Singapore Temasek-linked news'),
        ],
        [
            ('https://www.bursamalaysia.com/market_information/announcements/company_announcement', 'Bursa GLC announcements'),
            ('https://www.idx.co.id/id/perusahaan-tercatat/news/', 'IDX BUMN listed-companies'),
            ('https://www.sgx.com/securities/company-announcements', 'SGX listed Temasek-portfolio cos'),
        ],
        [
            ('https://www.oecd.org/corporate/soes/', 'OECD State-Owned Enterprises corporate governance'),
            ('https://www.adb.org/publications/series/glc-reform', 'ADB GLC reform series'),
            ('https://www.imf.org/en/Topics/state-owned-enterprises', 'IMF SOE research'),
        ],
    ],
    'general': [
        [
            ('https://www.bursamalaysia.com/market_information/announcements/company_announcement', 'Bursa Malaysia listed-co announcements'),
            ('https://www.idx.co.id/en/news/announcement/', 'IDX listed-co disclosures'),
            ('https://www.sgx.com/securities/company-announcements', 'SGX company announcements'),
        ],
        [
            ('https://www.mswg.org.my/', 'MSWG Malaysia minority-shareholder watch'),
            ('https://www.ojk.go.id/id/kanal/pasar-modal/tata-kelola-perusahaan/Pages/default.aspx', 'OJK Corporate Governance roadmap'),
            ('https://sias.org.sg/news/', 'SIAS Singapore investor association'),
        ],
        [
            ('https://www.imf.org/en/Countries/MYS', 'IMF Malaysia & SEA economic outlook'),
            ('https://www.adb.org/news/regions/asean', 'ADB ASEAN news & outlook'),
            ('https://data.worldbank.org/country/MYS', 'World Bank ASEAN open data'),
        ],
    ],
    'education': [
        [
            ('https://www2.mqa.gov.my/', 'MQA Malaysian Qualifications Agency'),
            ('https://www.kemdikbud.go.id/', 'Kemendikbud Indonesia ministry of education'),
            ('https://www.moe.gov.sg/news/press-releases', 'MOE Singapore press releases'),
        ],
        [
            ('https://www.timeshighereducation.com/world-university-rankings/by-region/asia', 'Times Higher Education Asia rankings'),
            ('https://www.topuniversities.com/asia-rankings', 'QS Asia University Rankings'),
            ('https://www.aaou.org/about/news/', 'AAOU Asian Association of Open Universities'),
        ],
        [
            ('https://uis.unesco.org/', 'UNESCO Institute for Statistics'),
            ('https://www.oecd.org/education/education-at-a-glance/', 'OECD Education at a Glance'),
            ('https://datatopics.worldbank.org/education/', 'World Bank EdStats'),
        ],
    ],

    # ── Departments (cross-industry, role-specific URLs) ────────────────
    'dept-finance': [
        [
            ('https://www.masb.org.my/', 'MASB Malaysian Accounting Standards Board'),
            ('https://web.iaiglobal.or.id/standar-akuntansi-keuangan/', 'IAI Indonesia accounting standards'),
            ('https://www.acra.gov.sg/legislation/legislative-reform', 'ACRA Singapore reporting requirements'),
        ],
        [
            ('https://www.mia.org.my/v2/news.aspx', 'MIA Malaysian Institute of Accountants news'),
            ('https://web.iaiglobal.or.id/news', 'IAI Indonesia accountants association news'),
            ('https://isca.org.sg/news/', 'ISCA Singapore CFO professional body'),
        ],
        [
            ('https://www.ifrs.org/news-and-events/', 'IFRS Foundation news & standards'),
            ('https://www.ifac.org/knowledge-gateway', 'IFAC global accounting knowledge'),
            ('https://www2.deloitte.com/global/en/pages/finance/articles/cfo-insights.html', 'Deloitte CFO Insights'),
        ],
    ],
    'dept-hr': [
        [
            ('https://jtksm.mohr.gov.my/index.php/en/', 'JTKSM Department of Labour Malaysia'),
            ('https://kemnaker.go.id/news/all', 'Kemnaker Indonesia ministry of manpower'),
            ('https://www.mom.gov.sg/newsroom', 'MOM Singapore newsroom'),
        ],
        [
            ('https://www.mihrm.com/', 'MIHRM Malaysian Institute of HR Management'),
            ('https://www.pmsm-indonesia.org/', 'PMSM Indonesia HR association'),
            ('https://www.shri.org.sg/news/', 'SHRI Singapore Human Resources Institute'),
        ],
        [
            ('https://www.mercer.com/our-thinking/career/total-remuneration-survey.html', 'Mercer Asia salary surveys'),
            ('https://www.aon.com/asia/insights/insights.jsp', 'Aon Asia talent insights'),
            ('https://www.kornferry.com/insights/this-week-in-leadership', 'Korn Ferry SEA leadership insights'),
        ],
    ],
    'dept-it-digital': [
        [
            ('https://mydigital.gov.my/news-publications/', 'MyDigital MDEC announcements'),
            ('https://www.kominfo.go.id/index.php/all_content/regulation', 'Kominfo Indonesia ICT regulations'),
            ('https://www.imda.gov.sg/about-imda/news-and-publications', 'IMDA Singapore news & publications'),
        ],
        [
            ('https://mtsfb.org.my/news/', 'MTSFB Malaysia Technical Standards Forum'),
            ('https://www.mikti.or.id/news', 'MIKTI Indonesian creative-tech industries'),
            ('https://www.scs.org.sg/news', 'SCS Singapore Computer Society news'),
        ],
        [
            ('https://www.gartner.com/en/industries/asia-pacific', 'Gartner SEA tech research'),
            ('https://www.idc.com/ap', 'IDC Asia Pacific research'),
            ('https://www.forrester.com/blogs/category/asia-pacific/', 'Forrester Asia tech insights'),
        ],
    ],
    'dept-marketing': [
        [
            ('https://www.iabm.com.my/', 'IAB Malaysia advertising standards'),
            ('https://www.amm.or.id/', 'AMM Indonesia marketing association'),
            ('https://www.ias.org.sg/standards', 'IAS Singapore advertising standards'),
        ],
        [
            ('https://www.marketing-interactive.com/region/southeast-asia', 'Marketing-Interactive SEA news'),
            ('https://maa.com.my/news/', 'MAA Malaysian Advertisers Association'),
            ('https://aaai.id/news/', 'AAI Indonesian advertising association'),
        ],
        [
            ('https://www.warc.com/asia-pacific', 'WARC Asia marketing intelligence'),
            ('https://www.kantar.com/inspiration/region/asia', 'Kantar Asia consumer insights'),
            ('https://www.nielsen.com/insights/?_topic=advertising-and-marketing', 'Nielsen marketing insights'),
        ],
    ],
    'dept-legal': [
        [
            ('https://www.malaysianbar.org.my/article/news', 'Bar Council Malaysia news'),
            ('https://www.peradi.or.id/index.php/news', 'PERADI Indonesia advocates association'),
            ('https://www.lawsociety.org.sg/news-publications/news/', 'Law Society Singapore news'),
        ],
        [
            ('https://www.mylawnet.com.my/', 'MyLawNet Malaysian legal updates'),
            ('https://www.hukumonline.com/', 'Hukumonline Indonesian legal portal'),
            ('https://www.asialaw.com/', 'Asialaw Asia legal directory'),
        ],
        [
            ('https://www.ibanet.org/Publications', 'IBA International Bar Association publications'),
            ('https://www.insol.org/Publications', 'INSOL Asia insolvency'),
            ('https://www.arbitration-icca.org/publications', 'ICCA arbitration publications'),
        ],
    ],
    'dept-corpsec': [
        [
            ('https://www.bursamalaysia.com/regulation/listing_requirements', 'Bursa listing requirements'),
            ('https://www.ojk.go.id/en/regulasi/Pages/default.aspx', 'OJK POJK regulations'),
            ('https://rulebook.sgx.com/', 'SGX Listing Rules rulebook'),
        ],
        [
            ('https://maicsa.org.my/news/', 'MAICSA Malaysia chartered secretaries'),
            ('https://icsa.com.sg/news', 'SAICSA Singapore corporate secretaries'),
            ('https://www.theicgn.org/news', 'ICGN governance news'),
        ],
        [
            ('https://www.theicgn.org/policy/global-governance-principles', 'ICGN Global Governance Principles'),
            ('https://www.oecd.org/corporate/principles-corporate-governance/', 'OECD Corporate Governance Principles'),
            ('https://www.icsa.org.uk/knowledge', 'ICSA global corporate governance knowledge'),
        ],
    ],
    'dept-strategy': [
        [
            ('https://www.sc.com.my/regulation/capital-market-masterplan', 'SC Malaysia Capital Market Masterplan'),
            ('https://www.ojk.go.id/en/Pages/Master-Plan-Sektor-Jasa-Keuangan-Indonesia.aspx', 'OJK Master Plan Indonesia financial services'),
            ('https://www.mas.gov.sg/news/speeches-and-monetary-policy-statements', 'MAS Industry Transformation Map'),
        ],
        [
            ('https://www.mckinsey.com/featured-insights/asia-pacific', 'McKinsey SEA insights'),
            ('https://www.bcg.com/about/locations/asia-pacific', 'BCG Asia Pacific insights'),
            ('https://www.bain.com/about/our-locations/southeast-asia/', 'Bain SEA insights'),
        ],
        [
            ('https://www.weforum.org/agenda/asia/', 'WEF Asia Pacific agenda'),
            ('https://www.adb.org/publications/asian-development-outlook-2024', 'ADB Asian Development Outlook'),
            ('https://www.oecd.org/southeast-asia/', 'OECD Southeast Asia outlook'),
        ],
    ],
    'dept-operations': [
        [
            ('https://www.dosh.gov.my/index.php/legislation', 'DOSH Malaysia OSH regulations'),
            ('https://kemnaker.go.id/news/k3', 'Kemnaker Indonesia K3 occupational safety'),
            ('https://www.mom.gov.sg/workplace-safety-and-health', 'MOM Singapore Workplace Safety & Health'),
        ],
        [
            ('https://www.iienet.org/', 'IIE Industrial Engineers Asia chapter'),
            ('https://www.ascm.org/', 'ASCM (formerly APICS) Asia operations community'),
            ('https://www.lean.org/lean-news/', 'Lean Enterprise Institute news'),
        ],
        [
            ('https://www.gartner.com/en/supply-chain/insights', 'Gartner Supply Chain insights'),
            ('https://www.mckinsey.com/capabilities/operations/our-insights', 'McKinsey Operations Practice'),
            ('https://www2.deloitte.com/global/en/pages/operations/articles/operations-services.html', 'Deloitte Industry 4.0 reports'),
        ],
    ],
    'dept-investor-relations': [
        [
            ('https://www.bursamalaysia.com/regulation/corporate_governance', 'Bursa IR best practices'),
            ('https://www.ojk.go.id/en/kanal/pasar-modal/tata-kelola-perusahaan/Pages/default.aspx', 'OJK CG roadmap for IR'),
            ('https://www.sgx.com/sustainable-listing/sustainability-reporting', 'SGX IR & sustainability reporting'),
        ],
        [
            ('https://mira.com.my/', 'MIRA Malaysian IR Association'),
            ('https://www.aeri.or.id/', 'AERI Indonesian IR Association'),
            ('https://irpas.org.sg/news/', 'IRPAS Singapore IR Professionals'),
        ],
        [
            ('https://www.niri.org/about-niri/news', 'NIRI National IR Institute news'),
            ('https://www.edelman.com/trust/2024/trust-barometer', 'Edelman Trust Barometer (IR)'),
            ('https://www.irmagazine.com/articles/asia', 'IR Magazine Asia coverage'),
        ],
    ],
    'dept-procurement': [
        [
            ('https://www.treasury.gov.my/index.php/en/government-procurement.html', 'MOF Malaysia government procurement'),
            ('https://www.lkpp.go.id/v3/news', 'LKPP Indonesia procurement agency news'),
            ('https://www.mof.gov.sg/policies/government-procurement', 'MOF Singapore government procurement'),
        ],
        [
            ('https://www.mipmm.com.my/', 'MIPMM Malaysian Institute of Procurement & Materials Management'),
            ('https://www.iapi.or.id/', 'IAPI Indonesia association of procurement'),
            ('https://www.cips.org/who-we-are/news/', 'CIPS Asia procurement news'),
        ],
        [
            ('https://www.gartner.com/en/supply-chain/insights/strategic-sourcing-and-procurement', 'Gartner Procurement research'),
            ('https://www2.deloitte.com/global/en/pages/operations/articles/global-cpo-survey.html', 'Deloitte Global CPO Survey'),
            ('https://www.mckinsey.com/capabilities/operations/how-we-help-clients/procurement', 'McKinsey Procurement insights'),
        ],
    ],
    'dept-esg': [
        [
            ('https://www.bursamalaysia.com/regulation/sustainability', 'Bursa Sustainability Reporting Guide'),
            ('https://www.ojk.go.id/sustainable-finance', 'OJK Sustainable Finance roadmap'),
            ('https://www.sgx.com/sustainable-listing', 'SGX sustainability reporting framework'),
        ],
        [
            ('https://www.wbcsd.org/Sector-Projects/asia-pacific', 'WBCSD Asia-Pacific sustainability'),
            ('https://www.globalreporting.org/news/news-center/', 'GRI sustainability standards news'),
            ('https://sasb.ifrs.org/standards/', 'SASB sustainability accounting standards'),
        ],
        [
            ('https://www.fsb-tcfd.org/recommendations/', 'TCFD climate-disclosure recommendations'),
            ('https://www.ifrs.org/issued-standards/ifrs-sustainability-standards-navigator/', 'IFRS S1/S2 ISSB sustainability standards'),
            ('https://www.msci.com/our-solutions/esg-investing', 'MSCI ESG indices & ratings'),
        ],
    ],
    'dept-risk': [
        [
            ('https://www.bnm.gov.my/-/risk-management', 'BNM risk-management framework'),
            ('https://www.ojk.go.id/id/kanal/perbankan/regulasi/manajemen-risiko/Default.aspx', 'OJK manajemen risiko regulations'),
            ('https://www.mas.gov.sg/regulation/Risk-Management', 'MAS Risk Management Guidelines'),
        ],
        [
            ('https://www.theirm.org/about/news-and-events/', 'IRM Institute of Risk Management news'),
            ('https://www.ferma.eu/', 'FERMA European/Asia federation of risk managers'),
            ('https://www.rims.org/news/recent-news', 'RIMS risk-management society news'),
        ],
        [
            ('https://www.coso.org/Pages/erm.aspx', 'COSO Enterprise Risk Management framework'),
            ('https://www.iso.org/iso-31000-risk-management.html', 'ISO 31000 Risk Management standard'),
            ('https://www.marsh.com/us/insights/research.html', 'Marsh Asia Pacific risk surveys'),
        ],
    ],
    # ── Other real industries (added to align with actual entry IDs) ──────
    'bpo-services': [
        [
            ('https://outsourcingmalaysia.com.my/', 'Outsourcing Malaysia industry association'),
            ('https://www.iaoa.id/', 'Indonesian Association of Outsourcing'),
            ('https://www.ida.gov.sg/', 'IMDA Singapore (services accreditation)'),
        ],
        [
            ('https://www.gartner.com/en/insights/business-process-outsourcing', 'Gartner BPO insights'),
            ('https://everestgrp.com/research/', 'Everest Group BPO research'),
            ('https://nasscom.in/', 'NASSCOM India (peer industry body)'),
        ],
        [
            ('https://www.weforum.org/agenda/future-of-work/', 'WEF Future of Work'),
            ('https://www.deloitte.com/global/en/services/consulting/perspectives/global-shared-services.html', 'Deloitte Global Shared Services Survey'),
            ('https://www.kearney.com/service/digital/article/-/insights/global-services-location-index', 'Kearney GSLI BPO ranking'),
        ],
    ],
    'diversified-conglomerate': [
        [
            ('https://www.mof.gov.my/portal/en/announcement/news', 'MOF Inc Malaysia GLC announcements'),
            ('https://www.bumn.go.id/page/berita/all', 'Kementerian BUMN Indonesia state-owned news'),
            ('https://www.mof.gov.sg/news-publications', 'MOF Singapore Temasek-linked news'),
        ],
        [
            ('https://www.bursamalaysia.com/market_information/announcements/company_announcement', 'Bursa GLC announcements'),
            ('https://www.idx.co.id/id/perusahaan-tercatat/news/', 'IDX BUMN listed-companies'),
            ('https://www.sgx.com/securities/company-announcements', 'SGX listed Temasek-portfolio cos'),
        ],
        [
            ('https://www.oecd.org/corporate/soes/', 'OECD State-Owned Enterprise Guidelines'),
            ('https://www.ifc.org/en/insights-reports/2025/state-owned-enterprises', 'IFC State-Owned Enterprises insights'),
            ('https://www.worldbank.org/en/topic/governance/brief/corporate-governance-state-owned-enterprises', 'World Bank SOE governance'),
        ],
    ],
    'glc-investment': [
        [
            ('https://www.pnb.com.my/announcement.html', 'PNB Malaysia announcements'),
            ('https://www.ina.go.id/news', 'INA Indonesia Investment Authority news'),
            ('https://www.khazanah.com.my/news-press-releases/', 'Khazanah Nasional press releases'),
        ],
        [
            ('https://www.temasek.com.sg/en/news-and-resources', 'Temasek news & resources'),
            ('https://www.gic.com.sg/en/newsroom/', 'GIC Singapore newsroom'),
            ('https://www.adia.ae/en/news-publications', 'ADIA Abu Dhabi news (peer)'),
        ],
        [
            ('https://www.swfinstitute.org/research/sovereign-wealth-fund', 'SWF Institute sovereign-wealth fund rankings'),
            ('https://www.ifswf.org/publications-page', 'IFSWF International Forum of SWFs publications'),
            ('https://www.worldbank.org/en/topic/sovereign-wealth-funds', 'World Bank SWF research'),
        ],
    ],
    'construction': [
        [
            ('https://www.cidb.gov.my/en/announcement/', 'CIDB Malaysia announcements'),
            ('https://www.pu.go.id/halaman/peraturan-jasa-konstruksi', 'Kementerian PUPR construction regulations'),
            ('https://www1.bca.gov.sg/about-us/news-and-publications', 'BCA Singapore news + publications'),
        ],
        [
            ('https://mbam.org.my/news/', 'Master Builders Association Malaysia news'),
            ('https://aki.or.id/berita-aki/', 'AKI Indonesia construction association news'),
            ('https://www.scal.com.sg/news/', 'SCAL Singapore Contractors Association news'),
        ],
        [
            ('https://www.gibo.com/en/insights', 'Global Infrastructure Outlook insights'),
            ('https://www.mckinsey.com/industries/private-capital/our-insights', 'McKinsey infrastructure insights'),
            ('https://www.adb.org/what-we-do/sectors/transport/main', 'ADB transport / infrastructure'),
        ],
    ],
    'aviation-airports': [
        [
            ('https://www.mavcom.my/en/industry/airport-infrastructure/', 'MAVCOM Malaysia airport regulation'),
            ('https://hubud.dephub.go.id/', 'Ditjen Perhubungan Udara Indonesia'),
            ('https://www.caas.gov.sg/who-we-are/newsroom/', 'CAAS Singapore newsroom'),
        ],
        [
            ('https://www.malaysiaairports.com.my/media-centre', 'Malaysia Airports press releases'),
            ('https://ap2.co.id/news/', 'Angkasa Pura II news'),
            ('https://www.changiairport.com/corporate/media-centre.html', 'Changi Airport corporate news'),
        ],
        [
            ('https://www.aci.aero/insights/', 'Airports Council International insights'),
            ('https://www.iata.org/en/publications/economics/', 'IATA economic reports'),
            ('https://www.icao.int/sustainability/Pages/default.aspx', 'ICAO sustainability'),
        ],
    ],
    'automotive': [
        [
            ('https://www.mai.org.my/', 'Malaysia Automotive Association industry news'),
            ('https://www.gaikindo.or.id/category/news/', 'GAIKINDO Indonesia automotive association'),
            ('https://www.maa.org.my/maa/news.html', 'Malaysia Automotive Association statistics'),
        ],
        [
            ('https://www.proton.com/news', 'Proton newsroom'),
            ('https://www.astra-otoparts.com/news', 'Astra Otoparts Indonesia news'),
            ('https://www.mida.gov.my/industries/manufacturing/automotive-industry/', 'MIDA automotive industry overview'),
        ],
        [
            ('https://www.oica.net/category/production-statistics/', 'OICA global automotive production statistics'),
            ('https://www.mckinsey.com/industries/automotive-and-assembly/our-insights', 'McKinsey automotive insights'),
            ('https://www.frost.com/research/automotive-and-transportation/', 'Frost & Sullivan automotive research'),
        ],
    ],
}

# Sanity-check: every override must be a list of 3 archetype URL groups,
# each archetype must be a list of 3 (url, note) tuples.
for _eid, _groups in ENTRY_URLS.items():
    assert isinstance(_groups, list), f'{_eid}: groups not a list'
    assert len(_groups) == 3, f'{_eid}: expected 3 archetype groups, got {len(_groups)}'
    for _i, _arch in enumerate(_groups):
        assert isinstance(_arch, list), f'{_eid}[{_i}]: archetype not a list'
        assert len(_arch) == 3, f'{_eid}[{_i}]: expected 3 URLs, got {len(_arch)}'
        for _t in _arch:
            assert isinstance(_t, tuple) and len(_t) == 2, f'{_eid}[{_i}]: bad tuple {_t!r}'
            assert _t[0].startswith('http'), f'{_eid}[{_i}]: bad URL {_t[0]!r}'


# ─────────────────────────────────────────────────────────────────────────
# Per-entry full-agent metadata overrides. Used when the pack archetype's
# name/desc/instructions/queries don't semantically fit an entry — even if
# the URLs DO match the entry's domain. Without this override, you get a
# free-tier agent named "Government Policy Watch" pointing at Bursa+IDX+SGX
# disclosure URLs, which is incoherent. ENTRY_AGENT_META keeps name+desc+
# instr+queries aligned with the per-entry URL bucket.
#
# Shape: ENTRY_AGENT_META[entry_id] = list of 3 dicts (one per archetype)
# Each dict optionally provides:
#   name_tmpl, desc_tmpl, instr_tmpl  — strings with {name} placeholder
#   queries — list of 3 strings with {name} placeholder
# Any field not provided falls back to the pack template's value.
ENTRY_AGENT_META = {
    'general': [
        {
            'name_tmpl': 'ASEAN Disclosure Watch ({name})',
            'desc_tmpl': 'Tracks Bursa Malaysia + IDX Indonesia + SGX Singapore listed-co announcements relevant to the {name} group.',
            'instr_tmpl': 'You are a cross-industry disclosure analyst for the {name} group. Source ONLY from the Bursa / IDX / SGX announcement portals in knowledge. Cite filing date + ticker + filing type. Output: weekly cross-industry disclosure log with implications for {name}.',
            'queries': [
                'List the 10 most material listed-co announcements on Bursa, IDX, and SGX in the last 7 days for sectors {name} operates in.',
                'Filter by category (earnings / M&A / restructuring / dividend) — flag the 5 most relevant to {name} portfolio.',
                'Draft a weekly cross-industry disclosure log with {name} CFO implications for each entry.',
            ],
        },
        {
            'name_tmpl': 'Governance & Stewardship Watch ({name})',
            'desc_tmpl': 'Tracks MSWG + OJK Corporate Governance + SIAS investor stewardship updates for the {name} group.',
            'instr_tmpl': 'You are a corporate-governance analyst for the {name} group. Source ONLY from the MSWG / OJK CG / SIAS URLs in knowledge. Cite source + date. Output: monthly governance digest with red-flag list for {name} board.',
            'queries': [
                'Summarise the last 30 days of MSWG, OJK CG, and SIAS publications relevant to listed conglomerates.',
                'List the governance red flags raised at AGMs of {name} peer groups.',
                'Draft a monthly governance digest with proposed actions for the {name} CorpSec lead.',
            ],
        },
        {
            'name_tmpl': 'Macro Brief Builder ({name})',
            'desc_tmpl': 'Builds macro briefs from IMF + ADB + World Bank ASEAN research for the {name} CFO.',
            'instr_tmpl': 'You are a macro-research analyst for the {name} group. Source ONLY from the IMF / ADB / World Bank URLs in knowledge. Cite report + date + chart. Output: monthly macro brief tagged by impact area for {name} divisions.',
            'queries': [
                'Pull the latest IMF Article IV, ADB AMRO, and World Bank ASEAN updates for Malaysia, Indonesia, and Singapore.',
                'Identify the macro themes most material to {name} divisional mix (banking / energy / consumer / property).',
                'Draft a monthly macro brief with base / bear / bull scenarios for the {name} group strategy.',
            ],
        },
    ],
    'glc-investment': [
        {
            'name_tmpl': 'Sovereign Wealth Mandate Watch ({name})',
            'desc_tmpl': 'Tracks PNB + INA + Khazanah official disclosures on mandate, returns, and investments.',
            'instr_tmpl': 'You are a SWF mandate analyst for {name}. Source ONLY from the PNB / INA / Khazanah / Temasek URLs in knowledge. Cite filing + date. Output: monthly mandate-watch summarising peer SWF positioning vs {name} thesis.',
            'queries': [
                'Summarise the last 90 days of PNB, INA, and Khazanah official disclosures (returns / mandate / investments).',
                'Identify the 5 largest peer SWF investments and the rationale stated publicly.',
                'Draft a monthly mandate-watch summarising peer SWF positioning vs {name} portfolio thesis.',
            ],
        },
        {
            'name_tmpl': 'Peer SWF News Tracker ({name})',
            'desc_tmpl': 'Pulls Temasek + GIC + ADIA newsroom articles relevant to {name} peer benchmarking.',
            'instr_tmpl': 'You are a peer SWF analyst for {name}. Source ONLY from the Temasek / GIC / ADIA newsroom URLs. Cite article date + headline. Output: weekly peer-pulse log with deal counts + AUM moves.',
            'queries': [
                'List Temasek, GIC, and ADIA news headlines in the last 30 days, tagged by deal type.',
                'Identify the 3 deals most relevant to {name} sector mandates.',
                'Draft a weekly peer-pulse log with deal counts + AUM moves vs {name}.',
            ],
        },
        {
            'name_tmpl': 'SWF Research Hub ({name})',
            'desc_tmpl': 'Tracks SWF Institute + IFSWF + World Bank SWF research relevant to {name}.',
            'instr_tmpl': 'You are a SWF research analyst for {name}. Source ONLY from the SWF Institute / IFSWF / World Bank URLs. Cite publication + date. Output: monthly research digest with adoption priorities for {name}.',
            'queries': [
                'Summarise SWF Institute, IFSWF, and World Bank SWF publications in the last 90 days.',
                'Identify the 3 governance / disclosure practices most relevant to {name} mandate.',
                'Draft a monthly research digest with adoption priorities for {name} board.',
            ],
        },
    ],
    'diversified-conglomerate': [
        {
            'name_tmpl': 'Conglomerate Mandate Watch ({name})',
            'desc_tmpl': 'Tracks MOF Inc + Kementerian BUMN + MOF Singapore announcements relevant to {name}.',
            'instr_tmpl': 'You are a conglomerate-mandate analyst for {name}. Source ONLY from the MOF Inc / BUMN / MOF SG URLs. Cite source + date. Output: weekly mandate-watch with policy implications for {name}.',
            'queries': [
                'Summarise the last 30 days of MOF Inc, Kementerian BUMN, and MOF SG announcements.',
                'Identify the policy changes most material to {name} divisions.',
                'Draft a weekly mandate-watch with policy implications for {name}.',
            ],
        },
        {
            'name_tmpl': 'Listed-Group Disclosure Tracker ({name})',
            'desc_tmpl': 'Tracks Bursa GLC + IDX BUMN + SGX Temasek-portfolio listed-co disclosures relevant to {name}.',
            'instr_tmpl': 'You are a listed-group disclosure tracker for {name}. Source ONLY from the Bursa / IDX / SGX disclosure portals. Cite filing date + ticker. Output: weekly disclosure log with peer implications for {name}.',
            'queries': [
                'List the 10 most material conglomerate disclosures on Bursa, IDX, and SGX in the last 7 days.',
                'Identify the peer disclosures most relevant to {name} divisions.',
                'Draft a weekly disclosure log with peer implications for {name}.',
            ],
        },
        {
            'name_tmpl': 'OECD Group Governance Hub ({name})',
            'desc_tmpl': 'Tracks OECD SOE + IFC + World Bank governance research relevant to {name}.',
            'instr_tmpl': 'You are a group-governance analyst for {name}. Source ONLY from the OECD / IFC / World Bank URLs. Cite report + date. Output: monthly governance digest with adoption priorities for {name} board.',
            'queries': [
                'Summarise OECD SOE, IFC, and World Bank governance research in the last 90 days.',
                'Identify the 3 practices most relevant to {name} mandate.',
                'Draft a monthly governance digest with adoption priorities for {name} board.',
            ],
        },
    ],
    'education': [
        {
            'name_tmpl': 'Education Policy Watch ({name})',
            'desc_tmpl': 'Tracks MOE Malaysia + Kemendikbud + MOE Singapore policy announcements for {name}.',
            'instr_tmpl': 'You are an education-policy analyst for {name}. Source ONLY from the MOE MY / Kemendikbud / MOE SG URLs. Cite policy + date. Output: weekly policy digest tagged by impact area for {name}.',
            'queries': [
                'Summarise the last 30 days of MOE MY, Kemendikbud, and MOE SG announcements relevant to {name}.',
                'Identify curriculum / accreditation / funding changes affecting {name}.',
                'Draft a weekly policy digest tagged by impact area for {name} academic council.',
            ],
        },
        {
            'name_tmpl': 'Quality & Accreditation Watch ({name})',
            'desc_tmpl': 'Tracks MQA + BAN-PT + SkillsFuture accreditation updates relevant to {name}.',
            'instr_tmpl': 'You are an accreditation analyst for {name}. Source ONLY from the MQA / BAN-PT / SkillsFuture URLs. Cite standard + revision + date. Output: monthly accreditation digest with renewal milestones for {name}.',
            'queries': [
                'List the latest MQA, BAN-PT, and SkillsFuture accreditation revisions affecting {name}.',
                'Flag programmes nearing renewal or with new compliance gaps for {name}.',
                'Draft a monthly accreditation digest with renewal milestones for {name} QA committee.',
            ],
        },
        {
            'name_tmpl': 'Higher-Ed Research Hub ({name})',
            'desc_tmpl': 'Pulls UNESCO + OECD Education + World Bank EdTech research relevant to {name}.',
            'instr_tmpl': 'You are an education-research analyst for {name}. Source ONLY from UNESCO / OECD / WB URLs. Cite report + date. Output: monthly research digest with adoption priorities for {name}.',
            'queries': [
                'Summarise UNESCO, OECD Education, and WB EdTech publications in the last 90 days.',
                'Identify the 3 practices most relevant to {name} programmes.',
                'Draft a monthly research digest with adoption priorities for {name} VC office.',
            ],
        },
    ],
}


def get_agent_meta(entry_id, archetype_index):
    """Return entry-specific agent metadata override (or None if no override)."""
    metas = ENTRY_AGENT_META.get(entry_id)
    if not metas or archetype_index < 0 or archetype_index >= len(metas):
        return None
    return metas[archetype_index]


def get_urls(entry_id, archetype_index):
    """Return entry-specific URL tuples for a given archetype index, or None if no override."""
    groups = ENTRY_URLS.get(entry_id)
    if not groups:
        return None
    if archetype_index >= len(groups):
        return None
    return groups[archetype_index]
