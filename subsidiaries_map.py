"""
SUBSIDIARIES_MAP — real ASEAN account-list subsidiaries that map onto each industry.
Source: customer accounts list shared in this project (Copilot - IDMY 203 Accounts).
Used by build_master.py to attach a `subsidiaries` field on every industry record.

These names appear in the entry's data and in the search haystack so the demo team
can search "Sunway Construction" and land on the construction industry, etc.

Real names will still be scrubbed to fictional brands at display time by _scrubReal()
in gen_hub.py. The chip strip on the hero shows them as live (account-list) examples
so demoers can map customer conversations to industry pages.
"""

SUBSIDIARIES_MAP = {
    "commercial-banking": [
        "Maybank", "CIMB Bank", "Public Bank", "Hong Leong Bank",
        "Alliance Bank Malaysia", "AmBank", "MBSB Bank",
        "Bank Mayapada", "Bank Panin", "BANK NISP",
        "Bank Pembangunan Daerah Jawa Barat", "Bank Pembangunan Daerah Jawa Tengah",
        "Bank Agroniaga", "BPD Sumatera Selatan",
    ],
    "islamic-banking": [
        "Maybank Islamic", "CIMB Islamic", "Bank Islam (Malaysia)",
        "RHB Islamic", "Al Rajhi Banking & Investment (M)",
        "Bank Syariah Muamalat Indonesia", "Bank Syariah Indonesia",
    ],
    "investment-banking": [
        "Kenanga Investment Bank", "KAF Investment Funds",
        "Maybank Investment Bank", "CIMB Investment Bank",
        "Affin Hwang Investment Bank", "Danareksa Sekuritas",
    ],
    "mortgage-finance": [
        "Cagamas", "Bank Pembangunan Malaysia",
        "Lembaga Pembiayaan Ekspor Indonesia (Indonesia Eximbank)",
        "BFI Finance Indonesia", "PT KB Finansia Multi Finance",
        "Mitsui Leasing Capital Indonesia",
    ],
    "general-insurance": [
        "MSIG Insurance (M)", "Tokio Marine Insurans (M)",
        "Lonpac Insurance", "Pacific & Orient Insurance",
        "MNRB Holdings", "Asuransi Permata Nipponkoa Indonesia",
        "Asuransi Multi Artha Guna", "Mitsui Sumitomo Insurance Group",
    ],
    "life-insurance": [
        "Sun Life Malaysia Assurance", "Allianz Life Indonesia",
        "AIA Bhd", "Manulife (M)", "Prudential Assurance",
        "IFG Life",
    ],
    "takaful": [
        "Etiqa Takaful (Maybank)", "Takaful Ikhlas (MNRB)",
        "Syarikat Takaful Malaysia", "Prudential BSN Takaful",
        "Sun Life Malaysia Takaful",
    ],
    "fintech-payments": [
        "Tranglo", "Soft Space", "Macro Kiosk", "Web Bytes",
        "Scicom (MSC)", "CTOS Data Systems", "BASS",
        "Anabatic Technologies", "E-Metrodata Com",
    ],
    "cross-border-remittance": [
        "Merchantrade Asia", "Tranglo", "BigPay (AirAsia)",
        "Touch n Go eWallet (CIMB-Ant)", "Soft Space cross-border",
    ],
    "hospital-network": [
        "Pantai Holdings (IHH)", "Columbia Asia",
        "KPJ Healthcare", "Sunway Medical Centre",
        "Mahkota Medical (Health Mgmt Intl)",
        "Siloam Hospitals (Lippo)", "Mitra Keluarga", "Hermina Hospital",
    ],
    "pharmaceutical": [
        "Kalbe Farma", "Darya Varia Laboratoria",
        "Soho Industri Pharmasi", "Anugerah Pharmindo Lestari",
        "Pharmaniaga (Boustead)", "Hovid", "Y.S.P. Industries",
        "Duopharma Biotech",
    ],
    "og-upstream": [
        "Hibiscus Petroleum", "Bumi Armada",
        "Sapura Energy (Sapura Holdings)",
        "Wah Seong (O&G arm)", "Pearl Oil",
        "Indonesia Petroleum", "Energasindo Heksa Karya",
    ],
    "og-downstream": [
        "Petron Fuel International", "Hengyuan Refining",
        "Dialog Group (Dialog Corporate)", "Deleum",
        "AKR Corporindo (petroleum)", "Lautan Luas (chemicals)",
    ],
    "renewable-energy": [
        "Edra Power Holdings", "Star Energy (Barito Pacific)",
        "Cirebon Power (Indika)", "Enerren Technologies",
        "YTL Power renewables", "Sarawak Energy hydro",
    ],
    "industrial-manufacturing": [
        "Daikin Malaysia (DAMA)", "Yokogawa Electric (M)",
        "Toray Industries (M)", "Niro Ceramic",
        "Pentamaster Contract Manufacturing",
        "Ann Joo Resources (steel)", "Lion Industrial Corporation (steel)",
        "Surya Toto Indonesia", "Indo Kordsa", "PT Inalum (smelting)",
        "Krakatau Steel (peer)",
    ],
    "rubber-gloves": [
        "Top Glove", "Hartalega", "Kossan Rubber Industries",
        "Supermax (peer)", "Riverstone (peer)",
    ],
    "semiconductor": [
        "Western Digital (M)", "Micron Technology",
        "ESCATEC", "Iris Technologies (M)",
        "Pentamaster Contract Manufacturing",
        "Inari Amertron (peer)", "Vitrox (peer)",
    ],
    "automotive": [
        "Perusahaan Otomobil Kedua (Perodua)",
        "Tan Chong Motor Holdings",
        "Hasjrat Abadi (Toyota dealer ID)",
        "Mitra Pinasthika Mustika (MPM Honda dealer)",
        "Daya Adira Mustika (Triputra)",
        "DRB-Hicom Auto",
    ],
    "auto-tyres": [
        "Continental Tire PJ", "Goodyear (M)", "Toyo Tyre (M)",
        "Gajah Tunggal Mulia (ID tyres)", "Bridgestone Indonesia (peer)",
    ],
    "construction": [
        "Gamuda", "WCT Holdings", "IJM Corporation",
        "Malaysian Resources Corporation (MRCB)",
        "Sunway Construction", "Hutama Karya (ID)",
        "Total Bangun Persada", "Surya Semesta Internusa",
        "Tripatra (Indika Energy EPC)",
    ],
    "food-fmcg": [
        "Mamee Double Decker", "Spritzer",
        "Permanis Sandilands", "Mewah-Oils",
        "Fraser & Neave (Singapore)", "Malayan Flour Mills",
        "QL Resources", "PPB Group", "Padiberas Nasional (Bernas)",
        "Nutrifood Indonesia", "Nippon Indosari Corp (Sari Roti)",
        "Kino Indonesia", "Ajinomoto Indonesia", "Sinar Sosro",
        "ABC President Indonesia", "Aneka Tuna Indonesia",
        "Sriboga Raturaya", "Japfa Comfeed Indonesia",
    ],
    "plantation": [
        "Kuala Lumpur Kepong (KLK)", "Boustead Plantations",
        "Hap Seng Plantations", "TDM",
        "IOI Group plantations", "Bumitama Gunajaya Agro",
        "Musim Mas", "Triputra Agro Persada",
        "Evans Indonesia", "Bd Agriculture (M)",
        "East West Seed Indonesia", "FKS Multi Agro",
        "Bakrie Sumatera Plantations",
    ],
    "bpo-services": [
        "Scicom (MSC)", "PersolKelly Consulting",
        "Sg Global Support Services", "Crowe Malaysia",
        "Anabatic Technologies", "E-Metrodata Com",
        "Averis", "IOI Global Services", "MI HCM Asia",
    ],
    "telco": [
        "Time Dotcom", "Maxis (peer)", "Celcom (peer)",
        "TM Berhad (peer)", "Telekomsel (peer)",
        "Bakrie Telecom (ID)", "Macro Kiosk (telco-tech)",
    ],
    "diversified-conglomerate": [
        "Sunway Group", "YTL Corporation", "Berjaya Corporation",
        "Boustead Holdings", "Hap Seng Consolidated",
        "Sapura Holdings", "Tradewinds Corporation",
        "Mulpha International", "Sampoerna Strategic",
        "Bakrie & Brothers", "Indika Energy", "Barito Pacific",
        "Triputra Investindo Arya", "Gunung Sewu Group",
        "Rodamas Company", "See Hoy Chan",
        "Haji Kalla", "Agung Sedayu Group",
    ],
    "government-agency": [
        "Kerajaan Negeri Johor", "Kerajaan Negeri Sarawak",
        "Kerajaan Negeri Selangor", "Kerajaan Negeri Sabah",
        "Kerajaan Negeri Pulau Pinang",
        "Kementerian Sumber Manusia",
        "Hutama Karya (ID state)", "POS Indonesia",
        "Sarana Multi Infrastruktur (PT SMI)",
        "PT MRT Jakarta",
        "Komisi Pemberantasan Korupsi (KPK)",
    ],
    "financial-regulator": [
        "Securities Commission Malaysia",
        "Otoritas Jasa Keuangan (OJK)",
        "Bank Negara Malaysia (BNM)",
        "Bursa Malaysia",
        "Bursa Efek Indonesia (BEI)",
    ],
    "glc-investment": [
        "Permodalan Nasional Berhad (PNB)",
        "Khazanah Nasional",
        "Mining Industry Indonesia (Mind ID)",
        "Sampoerna Strategic",
        "Tabung Haji",
    ],
    "property-reit": [
        "Sunway REIT", "KLCC Property", "Pavilion REIT",
        "IGB REIT", "YTL Hospitality REIT",
        "Sentral REIT (MRCB)",
    ],
    "logistics-3pl": [
        "Tiki Jalur Nugraha Ekakurir", "GD Express",
        "POS Indonesia", "Leschaco (M)",
        "Samudera Indonesia Logistics",
        "Catur Mitra Sejati Sentosa (MITRA 10 hardware DC)",
        "Reka Sinergi Pratama",
    ],
    "aviation-airports": [
        "Malaysia Airports Holdings",
        "Angkasa Pura I/II (peer)",
    ],
    "aviation-airlines": [
        "AirAsia", "Malaysia Airlines (peer)",
        "Garuda Indonesia (peer)", "Lion Air (peer)",
        "Batik Air (peer)",
    ],
    "coal-mining": [
        "Indo Tambangraya Megah",
        "Indika Indonesia Resources (Indika Energy)",
        "Bumi Resources (Bakrie)", "Adaro Energy (peer)",
    ],
    "rare-earth": [
        "Lynas (M)", "Malaysia Mining Corporation (MMC)",
        "Indonesia Asahan Aluminium (Inalum, Mind ID)",
        "PT Timah (Mind ID, tin)",
    ],
    "retail-grocery": [
        "AEON Co (M)", "Mydin (peer)", "Lotuss (peer)",
        "Sunway Pyramid retail estate",
        "Mitra Adiperkasa (ID retail)",
        "Rodamas distribution",
        "Berjaya Group retail (7-Eleven peer)",
    ],
    "hotel-resort": [
        "Berjaya Hotels & Resorts", "Sunway Resort",
        "YTL Hotels", "Mulpha Sanctuary Cove",
        "Sampoerna Strategic Square",
        "See Hoy Chan hospitality",
    ],
    "media-entertainment": [
        "Media Prima", "Magnum Corporation",
        "Pan Malaysian Pools", "Berjaya Sports Toto",
        "Astro (peer)",
    ],
    "education": [
        "Sunway University",
        "Open Learning Global (M)",
        "INTI International (peer)",
        "Taylor's University (peer)",
        "Universiti Tunku Abdul Rahman (peer)",
        "PT Paragon Technology and Innovation (training arm)",
    ],
    "power-utilities": [
        "Sarawak Energy", "Edra Power Holdings",
        "YTL Power International",
        "Pengurusan Air Selangor (water)",
        "PT Paiton Operation and Maintenance Indonesia",
    ],
    "property-development": [
        "S P Setia", "Gamuda Land", "Sunway Property",
        "YTL Land", "Mulpha Norwest", "WCT Property",
        "Berjaya Land", "Ciputra Development",
        "Agung Sedayu Group",
        "Java Industrial Estate (JIIPE / AKR)",
        "Surya Semesta Internusa",
    ],
    "ecommerce-superapp": [
        "Shopee (peer)", "Lazada (peer)",
        "Grab (peer)", "Gojek (peer)",
        "AirAsia Superapp (BigPay)",
        "Anabatic Technologies (e-commerce platform)",
        "Web Bytes (POS-as-a-service)",
    ],
    "maritime-shipping": [
        "MMC Port Holdings (peer)", "MTT Shipping",
        "Samudera Indonesia Group",
        "PT Meratus Line",
        "Indika Energy logistics arm",
    ],
}
