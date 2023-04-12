"""
Add known domains for government departments: https://www.gov.uk/government/organisations.

This is a list of CIVIL SERVICE domains not PUBLIC SERVICE
eg NHS is public body but not Civil Service.

Arms' Length Bodies can be either - so check before adding.
Domains for ALBs are listed under the corresponding department.

To consider - what do we do when departments change, do we keep the old domains?

"""

# Ministerial departments

ATTORNEY_GENERALS_OFFICE = frozenset([])
CABINET_OFFICE = frozenset(
    [
        "cabinet-office.x.gsi.gov.uk",
        "cabinetoffice.gov.uk",
        "crowncommercial.gov.uk",
        "csep.gov.uk",
        "cslearning.gov.uk",
        "csc.gov.uk",
        "digital.cabinet-office.gov.uk",
        "geo.gov.uk",
        "gpa.gov.uk",
        "ipa.gov.uk",
        "no10.gov.uk",
        "odandd.gov.uk",
    ]
)
DEPT_FOR_BUSINESS_AND_TRADE = frozenset(["beis.gov.uk", "trade.gov.uk", "companieshouse.gov.uk"])
DEPT_FOR_CULTURE_MEDIA_SPORT = frozenset(["dcms.gov.uk"])
DEPT_FOR_EDUCATION = frozenset(["education.gov.uk"])
DEPT_FOR_ENERGY_SECURITY_NET_ZERO = frozenset(["beis.gov.uk"])
DEFRA = frozenset(["defra.gov.uk"])
DLUHC = frozenset(["levellingup.gov.uk"])
DEPT_SCIENCE_INNOVATION_TECHNOLOGY = frozenset(["beis.gov.uk"])
DEPT_TRANSPORT = frozenset(["dft.gov.uk"])
DEPT_WORK_PENSIONS = frozenset(["dwp.gov.uk"])
DEPT_HEALTH_SOCIAL_CARE = frozenset(["dhsc.gov.uk"])
FOREIGN_OFFICE = frozenset(["fcdo.gov.uk"])
HMT = frozenset(["hmtreasury.gov.uk"])
HOME_OFFICE = frozenset(["homeoffice.gov.uk"])
MINISTRY_OF_DEFENCE = frozenset(["mod.gov.uk", "dstl.gov.uk"])
MINISTRY_OF_JUSTICE = frozenset(["justice.gov.uk", "digital.justice.gov.uk"])
NI_OFFICE = frozenset([])
OFFICE_OF_ADVOCATE_GENERAL_FOR_SCOTLAND = frozenset([])
OFFICE_OF_LEADER_OF_HOUSE_OF_COMMONS = frozenset([])
OFFICE_OF_LEADER_HOUSE_OF_LORDS = frozenset([])
OFFICE_OF_SOS_SCOTLAND = frozenset([])
OFFICE_OF_SOS_WALES = frozenset([])
UK_EXPORT_FINANCE = frozenset(["ukexportfinance.gov.uk"])


# Non-ministerial departments

CHARITY_COMMISSION = frozenset([])
COMPETITION_MARKETS_AUTHORITY = frozenset(["cma.gov.uk"])
CROWN_PROSECUTION_SERVICE = frozenset([])
FOOD_STANDARDS_AGENCY = frozenset([])
FORESTRY_COMMISSION = frozenset([])
GOV_ACTUARY_DEPT = frozenset([])
GOV_LEGAL_DEPT = frozenset([])
HM_LAND_REGISTRY = frozenset([])
HMRC = frozenset(["hmrc.gov.uk"])
NS_AND_I = frozenset([])
NATIONAL_ARCHIVES = frozenset([])
NATIONAL_CRIME_AGENCY = frozenset(["nca.gov.uk"])
OFFICE_OF_RAIL_AND_ROAD = frozenset([])
OFGEM = frozenset([])
OFQUAL = frozenset([])
OFSTED = frozenset(["ofsted.gov.uk"])
SERIOUS_FRAUD_OFFICE = frozenset([])
SUPREME_COURT_UK = frozenset([])
UK_STATISTICS_AUTHORITY = frozenset([])
WATER_SERVICES_REGULATION_AUTHORITY = frozenset([])

# Devolved administrations

SCOTTISH_GOVERNMENT = frozenset(["gov.scot"])
WELSH_GOVERNMENT = frozenset([])
NI_GOVERNMENT = frozenset([])  # Note, this is not part of UK Civil Service

# Other emails
# Things like profession emails, Fast Stream emails etc

OTHER = frozenset(["faststream.civilservice.gov.uk"])


# All domains
CIVIL_SERVICE_DOMAINS = frozenset.union(
    ATTORNEY_GENERALS_OFFICE,
    CABINET_OFFICE,
    DEPT_FOR_BUSINESS_AND_TRADE,
    DEPT_FOR_CULTURE_MEDIA_SPORT,
    DEPT_FOR_EDUCATION,
    DEPT_FOR_ENERGY_SECURITY_NET_ZERO,
    DEFRA,
    DLUHC,
    DEPT_SCIENCE_INNOVATION_TECHNOLOGY,
    DEPT_TRANSPORT,
    DEPT_WORK_PENSIONS,
    DEPT_HEALTH_SOCIAL_CARE,
    FOREIGN_OFFICE,
    HMT,
    HOME_OFFICE,
    MINISTRY_OF_DEFENCE,
    MINISTRY_OF_JUSTICE,
    NI_OFFICE,
    OFFICE_OF_ADVOCATE_GENERAL_FOR_SCOTLAND,
    OFFICE_OF_LEADER_OF_HOUSE_OF_COMMONS,
    OFFICE_OF_LEADER_HOUSE_OF_LORDS,
    OFFICE_OF_SOS_SCOTLAND,
    OFFICE_OF_SOS_WALES,
    UK_EXPORT_FINANCE,
    CHARITY_COMMISSION,
    COMPETITION_MARKETS_AUTHORITY,
    CROWN_PROSECUTION_SERVICE,
    FOOD_STANDARDS_AGENCY,
    FORESTRY_COMMISSION,
    GOV_ACTUARY_DEPT,
    GOV_LEGAL_DEPT,
    HM_LAND_REGISTRY,
    HMRC,
    NS_AND_I,
    NATIONAL_ARCHIVES,
    NATIONAL_CRIME_AGENCY,
    OFFICE_OF_RAIL_AND_ROAD,
    OFGEM,
    OFQUAL,
    OFSTED,
    SERIOUS_FRAUD_OFFICE,
    SUPREME_COURT_UK,
    UK_STATISTICS_AUTHORITY,
    WATER_SERVICES_REGULATION_AUTHORITY,
    SCOTTISH_GOVERNMENT,
    WELSH_GOVERNMENT,
    NI_GOVERNMENT,
    OTHER,
)
