from django.db import models
from django_use_email_as_username.models import BaseUser, BaseUserManager

from . import choices


class User(BaseUser):
    objects = BaseUserManager()
    username = None

    def save(self, *args, **kwargs):
        self.email = self.email.lower()
        super().save(*args, **kwargs)


class EvaluationType(choices.Choices):
    UNKNOWN = "Unknown"


class OutcomeType(choices.Choices):
    PRIMARY = "Primary"
    SECONDARY = "Secondary"


class OutcomeMeasure(choices.Choices):
    DIRECT = "Direct"
    SURROGATE = "Surrogate"


# TODO - to improve, for now just have UK Gov depts
class Organisation(choices.Choices):
    NO10 = "Prime Minister's Office, 10 Downing Street"
    ATTORNEY_GENERAL = "Attorney General's Office"
    CABINET_OFFICE = "Cabinet Office"
    BEIS = "Department for Business, Energy & Industrial Strategy"
    DCMS = "Department for Digital, Culture, Media & Sport"
    DFE = "Department for Education"
    DEFRA = "Department for Environment Food & Rural Affairs"
    DIT = "Department for International Trade"
    DLUHC = "Department for Levelling Up, Housing & Communities"
    DFT = "Department for Transport"
    DWP = "Department for Work & Pensions"
    DHSC = "Department of Health & Social Care"
    FCDO = "Foreign, Commonwealth & Development Office"
    HMT = "HM Treasury"
    HO = "Home Office"
    MOD = "Ministry of Defence"
    MOJ = "Ministry of Justice"
    NI_OFFICE = "Northern Ireland Office"
    ADVOCATE_GENERAL_SCOT = "Office of the Advocate General for Scotland"
    LEADER_HOC = "Office of the Leader of the House of Commons"
    LEADER_HOL = "Office of the Leader of the House of Lords"
    SCOT_OFFICE = "Office of the Secretary of State for Scotland"
    WALES_OFFICE = "Office of the Secretary of State for Wales"
    UKEF = "UK Export Finance"
    CHARITY_COMMISSION = "The Charity Commission"
    CMA = "Competition and Markets Authority"
    CPS = "Crown Prosecution Service"
    FSA = "Food Standards Agency"
    FORESTRY_COMMISSION = "Forestry Commission"
    GAD = "Government Actuary's Department"
    GLD = "Government Legal Department"
    HMLR = "HM Land Registry"
    HMRC = "HM Revenue & Customs"
    NSI = "NS&I"
    NATIONAL_ARCHIVES = "The National Archives"
    NCA = "National Crime Agency"
    ORR = "Office of Rail and Road"
    OFGEM = "Ofgem"
    OFQUAL = "Ofqual"
    OFSTED = "Ofsted"
    SERIOUS_FRAUD_OFFICE = "Serious Fraud Office"
    SUPREME_COURT = "Supreme Court of the United Kingdom"
    UK_STATS_AUTHORITY = "UK Statistics Authority"
    WATER_SERVICES_REGULATION_AUTHORITY = "The Water Services Regulation Authority"


class Evaluation(models.Model):
    # TODO - how do evaluations interact with users?
    # (Probably) a few users should be able to amend a particular evaluation.
    user = models.ForeignKey(User, related_name="evaluations", on_delete=models.CASCADE)

    title = models.CharField(max_length=256, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    # Issue description
    issue_description = models.TextField(blank=True, null=True)
    # TODO - think of good names for the subsequent issue fields!
    issue_relevance = models.TextField(blank=True, null=True)

    # TODO - need to be able to add multiple evaluations
    evaluation_type = models.CharField(max_length=128, blank=True, null=True, choices=EvaluationType.choices)


class Intervention(models.Model):
    evaluation = models.ForeignKey(Evaluation, related_name="interventions", on_delete=models.CASCADE)
    name = models.CharField(max_length=256, blank=True, null=True)
    brief_description = models.TextField(blank=True, null=True, verbose_name="Brief description of intervention")
    rationale = models.TextField(blank=True, null=True, verbose_name="Rationale, theory or goals of intervention elements")
    materials_used = models.TextField(blank=True, null=True, verbose_name="Description of physical or informational materials used in the intervention, including those used in intervention delivery or in training of intervention providers")
    procedures = models.TextField(blank=True, null=True, verbose_name="Description of each of the procedures, activities and/or processes used in the intervention, including enabling or supporting activities")
    modes_of_delivery = models.TextField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    frequency_of_delivery = models.TextField(blank=True, null=True)
    tailoring = models.TextField(blank=True, null=True)
    fidelity = models.TextField(blank=True, null=True)
    resource_requirements = models.TextField(blank=True, null=True)
    # TODO - add date


class OutcomeMeasure(models.Model):
    evaluation = models.ForeignKey(Evaluation, related_name="outcome_measures", on_delete=models.CASCADE)
    name = models.CharField(max_length=256, blank=True, null=True)
    primary_or_secondary = models.CharField(max_length=10, blank=True, null=True, choices=OutcomeType.choices)
    direct_or_surrogate = models.CharField(max_length=10, blank=True, null=True, choices=OutcomeMeasure.choices)
    description = models.TextField(blank=True, null=True)
    collection_process = models.TextField(blank=True, null=True)
    timepoint = models.TextField(blank=True, null=True)
    minimum_difference = models.TextField(blank=True, null=True)
    relevance = models.TextField(blank=True, null=True)


class OtherMeasure(models.Model):
    evaluation = models.ForeignKey(Evaluation, related_name="other_measures", on_delete=models.CASCADE)
    name = models.CharField(max_length=256, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    collection_process = models.TextField(blank=True, null=True)
