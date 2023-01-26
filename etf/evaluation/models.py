import uuid

from django.db import models
from django_use_email_as_username.models import BaseUser, BaseUserManager

from . import choices


class User(BaseUser):
    objects = BaseUserManager()
    username = None

    def save(self, *args, **kwargs):
        self.email = self.email.lower()
        super().save(*args, **kwargs)


# TODO - is there a better way to nest choices? (ie for economic evaluation)
class EvaluationTypeOptions(choices.Choices):
    IMPACT = "Impact evaluation"
    PROCESS = "Process evaluation"
    ECONOMIC_COST_MINIMISATION = "Economic evaluation: Cost-minimisation analysis"
    ECONOMIC_COST_EFFECTIVENESS = "Economic evaluation: Cost-effectiveness analysis"
    ECONOMIC_COST_BENEFIT = "Economic evaluation: Cost-benefit analysis"
    ECONOMIC_COST_UTILITY = "Economic evaluation: Cost-utility"
    OTHER = "Other"


class OutcomeType(choices.Choices):
    PRIMARY = "Primary"
    SECONDARY = "Secondary"


class OutcomeMeasure(choices.Choices):
    DIRECT = "Direct"
    SURROGATE = "Surrogate"


class YesNoPartial(choices.Choices):
    YES = "Yes"
    NO = "No"
    PARTIAL = "Partial"


# TODO - to improve
class Topic(choices.Choices):
    BREXIT = "Brexit"
    BUSINESS_AND_INDUSTRY = "Business and industry"
    CORONAVIRUS = "Coronavirus"
    CORPORATE_INFORMATION = "Corporate information"
    CRIME_JUSTICE_AND_LAW = "Crime, justice and law"
    DEFENCE_AND_ARMED_FORCES = "Defence and armed forces"
    EDUCATION_TRAINING_AND_SKILLS = "Education, training and skills"
    ENTERING_AND_STAYING_IN_THE_UK = "Entering and staying in the UK"
    ENVIRONMENT = "Environment"
    GOING_AND_BEING_ABROAD = "Going and being abroad"
    GOVERNMENT = "Government"
    HEALTH_AND_SOCIAL_CARE = "Health and social care"
    HOUSING_LOCAL_AND_COMMUNITY = "Housing, local and community"
    INTERNATIONAL = "International"
    LIFE_CIRCUMSTANCES = "Life circumstances"
    MONEY = "Money"
    PARENTING_CHILDCARE_AND_CHILDRENS_SERVICES = "Parenting, childcare and children's services"
    REGIONAL_AND_LOCAL_GOVERNMENT = "Regional and local government"
    SOCIETY_AND_CULTURE = "Society and culture"
    TRANSPORT = "Transport"
    WELFARE = "Welfare"


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


def get_topic_display_name(db_name):
    result = [topic[1] for topic in Topic.choices if topic[0] == db_name]
    return result[0]


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(editable=False, auto_now_add=True)
    modified_at = models.DateTimeField(editable=False, auto_now=True)

    class Meta:
        abstract = True


# TODO - throughout have used TextField (where spec was for 10,000 chars - is limit actually necessary?)


class Evaluation(TimeStampedModel):
    # TODO - how do evaluations interact with users?
    # (Probably) a few users should be able to amend a particular evaluation.
    user = models.ForeignKey(User, related_name="evaluations", on_delete=models.CASCADE)

    # TODO - decide what we're doing with unique IDs for items in registry - this might be public?
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=256, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    topics = models.JSONField(default=list)
    organisation = models.CharField(max_length=256, blank=True, null=True, choices=Organisation.choices)
    is_published = models.BooleanField(blank=True, null=True)

    # Issue description
    issue_description = models.TextField(blank=True, null=True)
    those_experiencing_issue = models.TextField(blank=True, null=True)
    why_improvements_matter = models.TextField(blank=True, null=True)
    who_improvements_matter_to = models.TextField(blank=True, null=True)
    current_practice = models.TextField(blank=True, null=True)
    issue_relevance = models.TextField(blank=True, null=True)

    # Evaluation - event dates
    evaluation_start_date = models.DateField(blank=True, null=True)
    evaluation_end_date = models.DateField(blank=True, null=True)
    date_of_intended_publication = models.DateField(blank=True, null=True)
    reasons_for_delays_in_publication = models.TextField(blank=True, null=True)

    # Participant recruitment approach
    target_population = models.TextField(blank=True, null=True)
    eligibility_criteria = models.TextField(blank=True, null=True)
    process_for_recruitment = models.TextField(blank=True, null=True)
    target_sample_size = models.TextField(blank=True, null=True)
    intended_recruitment_schedule = models.TextField(blank=True, null=True)
    date_of_first_recruitment = models.DateField(blank=True, null=True)

    # Ethical considerations
    ethics_committee_approval = models.BooleanField(blank=True, null=True)
    ethics_committee_details = models.TextField(blank=True, null=True)
    ethical_state_given_existing_evidence_base = models.TextField(blank=True, null=True)
    risks_to_participants = models.TextField(blank=True, null=True)
    risks_to_study_team = models.TextField(blank=True, null=True)
    participant_involvement = models.TextField(blank=True, null=True)
    participant_consent = models.TextField(blank=True, null=True)
    participant_information = models.TextField(blank=True, null=True)
    participant_payment = models.TextField(blank=True, null=True)
    confidentiality_and_personal_data = models.TextField(blank=True, null=True)
    breaking_confidentiality = models.TextField(blank=True, null=True)
    other_ethical_information = models.TextField(blank=True, null=True)

    def get_list_topics_display_names(self):
        return [get_topic_display_name(x) for x in self.topics]

    def __str__(self):
        return f"{self.id} : {self.title}"


class EvaluationType(models.Model):
    evaluation = models.ForeignKey(Evaluation, related_name="evaluation_types", on_delete=models.CASCADE)
    type = models.CharField(max_length=256, blank=True, null=True, choices=EvaluationTypeOptions.choices)
    other_description = models.CharField(max_length=256, blank=True, null=True)


class Intervention(TimeStampedModel):
    evaluation = models.ForeignKey(Evaluation, related_name="interventions", on_delete=models.CASCADE)
    name = models.CharField(max_length=256, blank=True, null=True)
    brief_description = models.TextField(blank=True, null=True)
    rationale = models.TextField(blank=True, null=True)
    materials_used = models.TextField(blank=True, null=True)
    procedures = models.TextField(blank=True, null=True)
    provider_description = models.TextField(blank=True, null=True)
    modes_of_delivery = models.TextField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    frequency_of_delivery = models.TextField(blank=True, null=True)
    tailoring = models.TextField(blank=True, null=True)
    fidelity = models.TextField(blank=True, null=True)
    resource_requirements = models.TextField(blank=True, null=True)
    # TODO - add date


class OutcomeMeasure(TimeStampedModel):
    evaluation = models.ForeignKey(Evaluation, related_name="outcome_measures", on_delete=models.CASCADE)
    name = models.CharField(max_length=256, blank=True, null=True)
    primary_or_secondary = models.CharField(max_length=10, blank=True, null=True, choices=OutcomeType.choices)
    direct_or_surrogate = models.CharField(max_length=10, blank=True, null=True, choices=OutcomeMeasure.choices)
    description = models.TextField(blank=True, null=True)
    collection_process = models.TextField(blank=True, null=True)
    timepoint = models.TextField(blank=True, null=True)
    minimum_difference = models.TextField(blank=True, null=True)
    relevance = models.TextField(blank=True, null=True)


class OtherMeasure(TimeStampedModel):
    evaluation = models.ForeignKey(Evaluation, related_name="other_measures", on_delete=models.CASCADE)
    name = models.CharField(max_length=256, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    collection_process = models.TextField(blank=True, null=True)
