import uuid

from django.core.serializers.json import DjangoJSONEncoder
from django.db import models
from django_use_email_as_username.models import BaseUser, BaseUserManager

from . import enums, utils
from .pages import EvaluationPageStatus, get_default_page_statuses


class UUIDPrimaryKeyBase(models.Model):
    class Meta:
        abstract = True

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


class User(BaseUser, UUIDPrimaryKeyBase):
    objects = BaseUserManager()
    username = None
    verified = models.BooleanField(default=False, blank=True, null=True)
    last_token_sent_at = models.DateTimeField(editable=False, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.email = self.email.lower()
        super().save(*args, **kwargs)


class NamedModel:
    _name_field = "name"

    def set_name(self, value):
        setattr(self, self._name_field, value)

    def get_name(self):
        return getattr(self, self._name_field)


class EvaluationTypeOptions(utils.Choices):
    IMPACT = "Impact evaluation"
    PROCESS = "Process evaluation"
    ECONOMIC = "Economic evaluation"
    OTHER = "Other"


class OutcomeType(utils.Choices):
    PRIMARY = "Primary"
    SECONDARY = "Secondary"


class OutcomeMeasure(utils.Choices):
    DIRECT = "Direct"
    SURROGATE = "Surrogate"


class YesNo(utils.Choices):
    YES = "Yes"
    NO = "No"


class YesNoPartial(utils.Choices):
    YES = "Yes"
    NO = "No"
    PARTIAL = "Partial"


class FullNoPartial(utils.Choices):
    FULL = "Full"
    PARTIAL = "Partial"
    NO = "No"


class MeasureType(utils.Choices):
    CONTINUOUS = "Continuous"
    DISCRETE = "Discrete"
    BINARY = "Binary"
    ORDINAL = "Ordinal"
    NOMINAL = "Nominal"
    OTHER = "Other"


# TODO - to improve
class Topic(utils.Choices):
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


class EvaluationStatus(utils.Choices):
    DRAFT = "Draft"
    CIVIL_SERVICE = "Civil Service"
    PUBLIC = "Public"


class DocumentType(utils.Choices):
    SCOPING_REPORT = "Scoping report"
    FEASIBILITY_STUDY_REPORT = "Feasibility study report"
    STUDY_PROTOCOL = "Study protocol"
    ANALYSIS_PLAN = "Analysis plan"
    THEORY_OF_CHANGE = "Theory of change/Causal-chain map/Logic model"
    SUMMARY_INTERIM = "Summary interim results report"
    MAIN_INTERIM = "Main interim results report"
    SUMMARY_FINAL = "Summary final results report"
    MAIN_FINAL = "Main final results report"
    TECHNICAL_REPORT = "Technical report"
    DATASET = "Data set"
    ANALYSIS_CODE = "Analysis code"
    OTHER = "Other"


class EventDateOption(utils.Choices):
    EVALUATION_START = "Evaluation start"
    EVALUATION_END = "Evaluation end"
    FIRST_PARTICIPANT_RECRUITED = "First participant recruited"
    LAST_PARTICIPANT_RECRUITED = "Last participant recruited"
    INTERVENTION_START_DATE = "Intervention start date"
    INTERVENTION_END_DATE = "Intervention end date"
    INTERIM_DATA_EXTRACTION_DATE = "Interim data extraction date"
    INTERIM_DATA_ANALYSIS_START = "Interim data analysis start"
    INTERIM_DATA_ANALYSIS_END = "Interim data analysis end"
    PUBLICATION_INTERIM_RESULTS = "Publication of interim results"
    FINAL_DATA_EXTRACTION_DATE = "Final data extraction date"
    FINAL_DATA_ANALYSIS_START = "Final data analysis start"
    FINAL_DATA_ANALYSIS_END = "Final data analysis end"
    PUBLICATION_FINAL_RESULTS = "Publication of final results"
    OTHER = "Other"


class EventDateType(utils.Choices):
    INTENDED = "Intended"
    ACTUAL = "Actual"


class EconomicEvaluationType(utils.Choices):
    COST_MINIMISATION = "Cost minimisation"
    COST_EFFECTIVENESS_ANALYSIS = "Cost-effectiveness analysis"
    COST_BENEFIT_ANALYSIS = "Cost-benefit analysis"
    COST_UTILITY_ANALYSIS = "Cost-utility analysis"


# TODO - nested choices
class ImpactEvalInterpretation(utils.Choices):
    SUPERIORITY_SUPERIOR = "Superiority framework: Superior"
    SUPERIORITY_INFERIOR = "Superiority framework: Inferior"
    SUPERIORITY_INCONCLUSIVE = "Superiority framework: Inconclusive"
    NON_INFERIORITY_SUPERIOR = "Non-inferiority framework: Superior"
    NON_INFERIORITY_NON_INFERIOR = "Non-inferiority framework: Non-inferior"
    NON_INFERIORITY_INFERIOR = "Non-inferiority framework: Inferior"
    NON_INFERIORITY_INCONCLUSIVE = "Non-inferiority framework: Inconclusive"
    EQUIVALENCE_EQUIVALENT = "Equivalence framework: Equivalent"
    EQUIVALENCE_NON_EQUIVALENT = "Equivalence framework: Non-equivalent"
    EQUIVALENCE_NON_EQUIVALENT_SUPERIOR = "Equivalence framework: Non-equivalent (superior)"
    EQUIVALENCE_NON_EQUIVALENT_INFERIOR = "Equivalence framework: Non-equivalent (inferior)"
    EQUIVALENCE_NON_EQUIVALENT_INCONCLUSIVE = "Equivalence framework: Inconclusive"
    OTHER = "Other"


# TODO - nested choices
class ImpactEvalDesign(utils.Choices):
    RCT = "Experimental methods for impact evaluation: Randomised controlled trial (RCT)"
    CLUSTER_RCT = "Experimental methods for impact evaluation: Cluster randomised RCT"
    STEPPED_WEDGE_RCT = "Experimental methods for impact evaluation: Stepped wedge RCT"
    WAITLIST_RCT = "Experimental methods for impact evaluation: Wait-list RCT"
    PROPENSITY_SCORE_MATCHING = "Quasi-experimental methods for impact evaluation: Propensity score matching"
    TIMING_OF_EVENTS = "Quasi-experimental methods for impact evaluation: Timing of events"
    INTERRUPTED_TIME_SERIES_ANALYSIS = (
        "Quasi-experimental methods for impact evaluation: Interrupted time series analysis"
    )
    INSTRUMENTAL_VARIABLES = "Quasi-experimental methods for impact evaluation: Instrumental variables"
    SYNTHETIC_CONTROL_METHODS = "Quasi-experimental methods for impact evaluation: Synthetic control methods"
    DIFF_IN_DIFF = "Quasi-experimental methods for impact evaluation: Difference-in-difference"
    REGRESSION_DISCONTINUITY = "Quasi-experimental methods for impact evaluation: Regression discontinuity"
    QCA = "Theory-based methods for impact evaluation: Qualitative comparative analysis (QCA)"
    REALISE_EVALUATION = "Theory-based methods for impact evaluation: Realist evaluation"
    PROCESS_TRACING = "Theory-based methods for impact evaluation: Process tracing"
    CONSTRIBUTION_ANALYSIS = "Theory-based methods for impact evaluation: Contribution analysis"
    BAYESIAN_UPDATING = "Theory-based methods for impact evaluation: Bayesian updating"
    CONTRIBUTION_TRACING = "Theory-based methods for impact evaluation: Contribution tracing"
    MOST_SIGNIFICANT_CHANGE = "Theory-based methods for impact evaluation: Most significant change"
    OUTCOME_HARVESTING = "Theory-based methods for impact evaluation: Outcome harvesting"
    SIMULATION_MODELLING = "Theory-based methods for impact evaluation: Simulation modelling"
    INDIVIDUAL_INTERVIEWS = "Generic research methods used in both process and impact evaluation: Individual interviews"
    FOCUS_GROUPS = (
        "Generic research methods used in both process and impact evaluation: Focus groups or group interviews"
    )
    CASE_STUDIES = "Generic research methods used in both process and impact evaluation: Case studies"
    SURVEYS_AND_POLLING = "Generic research methods used in both process and impact evaluation: Surveys and polling"
    OUTPUT_OR_PERFORMANCE_MONITORING = (
        "Generic research methods used in both process and impact evaluation: Output or performance modelling"
    )
    QUALITATIVE_OBSERVATIONAL_STUDIES = (
        "Generic research methods used in both process and impact evaluation: Qualitative observational studies"
    )
    CONSULTATIVE_METHODS = (
        "Generic research methods used in both process and impact evaluation: Consultative/deliberative methods"
    )
    OTHER = "Other"


class ImpactFramework(utils.Choices):
    SUPERIORITY = "Superiority"
    NON_INFERIORITY = "Non-inferiority"
    EQUIVALENCE = "Equivalence"
    OTHER = "Other"


class ImpactAnalysisBasis(utils.Choices):
    INTENTION_TO_TREAT = "Intention-to-treat"
    PER_PROTOCOL = "Per-protocol"
    OTHER = "Other"


class ImpactMeasureInterval(utils.Choices):
    CONFIDENCE = "Confidence interval"
    BAYESIAN = "Bayesian credible interval"
    NONE = "None"
    OTHER = "Other"


class ImpactInterpretationType(utils.Choices):
    INTERVALS = "Interpretation of intervals"
    HYPOTHESIS = "Hypothesis testing"
    NONE = "None"
    OTHER = "Other"


class ImpactMeasureType(utils.Choices):
    ABSOLUTE = "Absolute measure"
    RELATIVE = "Relative measure"
    OTHER = "Other"


def get_topic_display_name(db_name):
    result = [topic[1] for topic in Topic.choices if topic[0] == db_name]
    return result[0]


def get_organisation_display_name(db_name):
    result = [organisation[1] for organisation in enums.Organisation.choices if organisation[0] == db_name]
    return result[0]


def get_status_display_name(db_name):
    result = [status[1] for status in EvaluationStatus.choices if status[0] == db_name]
    return result[0]


def get_page_status_display_name(db_name):
    if db_name in EvaluationPageStatus:
        return EvaluationPageStatus[db_name].label
    else:
        return None


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(editable=False, auto_now_add=True)
    modified_at = models.DateTimeField(editable=False, auto_now=True)

    class Meta:
        abstract = True


class Event(TimeStampedModel):
    name = models.CharField(max_length=256)
    data = models.JSONField(encoder=DjangoJSONEncoder)


# TODO - throughout have used TextField (where spec was for 10,000 chars - is limit actually necessary?)
class Evaluation(TimeStampedModel, UUIDPrimaryKeyBase, NamedModel):
    users = models.ManyToManyField(User, related_name="evaluations")

    title = models.CharField(max_length=256, blank=True, null=True)
    short_title = models.CharField(max_length=64, blank=True, null=True)
    brief_description = models.TextField(blank=True, null=True)
    topics = models.JSONField(default=list)  # TODO - do we use these?
    organisations = models.JSONField(default=list)  # TODO - how are we going to do orgs?
    status = models.CharField(
        max_length=256, blank=False, null=False, choices=EvaluationStatus.choices, default=EvaluationStatus.DRAFT.value
    )
    doi = models.CharField(max_length=64, blank=True, null=True)
    page_statuses = models.JSONField(default=get_default_page_statuses)

    # Issue description
    issue_description = models.TextField(blank=True, null=True)
    those_experiencing_issue = models.TextField(blank=True, null=True)
    why_improvements_matter = models.TextField(blank=True, null=True)
    who_improvements_matter_to = models.TextField(blank=True, null=True)
    current_practice = models.TextField(blank=True, null=True)
    issue_relevance = models.TextField(blank=True, null=True)

    # Evaluation type (multiselect)
    evaluation_type = models.JSONField(default=list)

    # Studied population
    studied_population = models.TextField(blank=True, null=True)
    eligibility_criteria = models.TextField(blank=True, null=True)
    sample_size = models.PositiveIntegerField(blank=True, null=True)
    sample_size_units = models.CharField(max_length=256, blank=True, null=True)
    sample_size_details = models.TextField(blank=True, null=True)

    # Participant recruitment approach
    process_for_recruitment = models.TextField(blank=True, null=True)
    recruitment_schedule = models.TextField(blank=True, null=True)
    # TODO - what happens with dates?

    # Ethical considerations
    ethics_committee_approval = models.CharField(max_length=3, blank=True, null=True, choices=YesNo.choices)
    ethics_committee_details = models.TextField(blank=True, null=True)
    ethical_state_given_existing_evidence_base = models.TextField(blank=True, null=True)
    risks_to_participants = models.TextField(blank=True, null=True)
    risks_to_study_team = models.TextField(blank=True, null=True)
    participant_involvement = models.TextField(blank=True, null=True)
    participant_information = models.TextField(blank=True, null=True)
    participant_consent = models.TextField(blank=True, null=True)
    participant_payment = models.TextField(blank=True, null=True)
    confidentiality_and_personal_data = models.TextField(blank=True, null=True)
    breaking_confidentiality = models.TextField(blank=True, null=True)
    other_ethical_information = models.TextField(blank=True, null=True)

    # Impact evaluation design
    impact_eval_design_name = models.JSONField(default=list)
    impact_eval_design_justification = models.TextField(blank=True, null=True)
    impact_eval_design_description = models.TextField(blank=True, null=True)
    impact_eval_design_features = models.TextField(blank=True, null=True)
    impact_eval_design_equity = models.TextField(blank=True, null=True)
    impact_eval_design_assumptions = models.TextField(blank=True, null=True)
    impact_eval_design_approach_limitations = models.TextField(blank=True, null=True)

    # Impact evaluation analysis
    # TODO - add analysis plan document?
    impact_eval_framework = models.CharField(max_length=64, blank=True, null=True)
    impact_eval_basis = models.CharField(max_length=64, blank=True, null=True)
    impact_eval_analysis_set = models.TextField(blank=True, null=True)
    impact_eval_effect_measure_type = models.CharField(
        max_length=64, choices=ImpactMeasureType.choices, blank=True, null=True
    )
    impact_eval_primary_effect_size_measure = models.TextField(blank=True, null=True)
    impact_eval_effect_measure_interval = models.CharField(max_length=64, blank=True, null=True)
    impact_eval_primary_effect_size_desc = models.TextField(blank=True, null=True)
    impact_eval_interpretation_type = models.CharField(max_length=64, blank=True, null=True)
    impact_eval_sensitivity_analysis = models.TextField(blank=True, null=True)
    impact_eval_subgroup_analysis = models.TextField(blank=True, null=True)
    impact_eval_missing_data_handling = models.TextField(blank=True, null=True)
    impact_eval_fidelity = models.CharField(max_length=10, choices=YesNo.choices, blank=True, null=True)
    impact_eval_desc_planned_analysis = models.TextField(blank=True, null=True)
    # TODO - add more

    # Process evaluation design
    process_eval_methods = models.CharField(blank=True, null=True, max_length=256)
    # TODO - add more

    # Process evaluation analysis
    # TODO - add analysis plan document
    process_eval_analysis_description = models.TextField(blank=True, null=True)

    # Economic evaluation design
    economic_eval_type = models.CharField(max_length=256, choices=EconomicEvaluationType.choices, blank=True, null=True)
    perspective_costs = models.TextField(blank=True, null=True)
    perspective_benefits = models.TextField(blank=True, null=True)
    monetisation_approaches = models.TextField(blank=True, null=True)
    economic_eval_design_details = models.TextField(blank=True, null=True)

    # Economic evaluation analysis
    economic_eval_analysis_description = models.TextField(blank=True, null=True)
    # TODO - add more details

    # Other evaluation design
    other_eval_design_type = models.TextField(blank=True, null=True)
    other_eval_design_details = models.TextField(blank=True, null=True)

    # Other evaluation analysis
    other_eval_analysis_description = models.TextField(blank=True, null=True)
    # TODO - add more

    # Impact evaluation findings
    impact_eval_comparison = models.TextField(blank=True, null=True)
    impact_eval_outcome = models.TextField(blank=True, null=True)
    impact_eval_interpretation = models.CharField(max_length=256, blank=True, null=True)
    impact_eval_point_estimate_diff = models.TextField(blank=True, null=True)
    impact_eval_lower_uncertainty = models.TextField(blank=True, null=True)
    impact_eval_upper_uncertainty = models.TextField(blank=True, null=True)

    # Economic evaluation findings
    economic_eval_summary_findings = models.TextField(blank=True, null=True)
    economic_eval_findings = models.TextField(blank=True, null=True)

    # Process evaluation findings
    process_eval_summary_findings = models.TextField(blank=True, null=True)
    process_eval_findings = models.TextField(blank=True, null=True)

    # Other evaluation findings
    other_eval_summary_findings = models.TextField(blank=True, null=True)
    other_eval_findings = models.TextField(blank=True, null=True)

    # TODO - add fields on evaluation design, analysis and findings

    def update_evaluation_page_status(self, page_name, status):
        # TODO: Fix ignoring unknown pages
        if page_name not in self.page_statuses:
            return
        if self.page_statuses[page_name] == EvaluationPageStatus.DONE.name:
            return
        self.page_statuses[page_name] = status
        self.save()

    def get_list_topics_display_names(self):
        return [get_topic_display_name(x) for x in self.topics]

    def get_list_organisations_display_names(self):
        return [get_organisation_display_name(x) for x in self.organisations]

    def get_status_display_name(self):
        return get_status_display_name(self.status)

    def __str__(self):
        return f"{self.id} : {self.title}"


class Intervention(TimeStampedModel, UUIDPrimaryKeyBase, NamedModel):
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
    geographical_information = models.TextField(blank=True, null=True)


class OutcomeMeasure(TimeStampedModel, UUIDPrimaryKeyBase, NamedModel):
    evaluation = models.ForeignKey(Evaluation, related_name="outcome_measures", on_delete=models.CASCADE)
    name = models.CharField(max_length=256, blank=True, null=True)
    primary_or_secondary = models.CharField(max_length=10, blank=True, null=True, choices=OutcomeType.choices)
    direct_or_surrogate = models.CharField(max_length=10, blank=True, null=True, choices=OutcomeMeasure.choices)
    measure_type = models.CharField(max_length=256, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    collection_process = models.TextField(blank=True, null=True)
    timepoint = models.TextField(blank=True, null=True)
    minimum_difference = models.TextField(blank=True, null=True)
    relevance = models.TextField(blank=True, null=True)


class OtherMeasure(TimeStampedModel, UUIDPrimaryKeyBase, NamedModel):
    evaluation = models.ForeignKey(Evaluation, related_name="other_measures", on_delete=models.CASCADE)
    name = models.CharField(max_length=256, blank=True, null=True)
    measure_type = models.CharField(max_length=256, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    collection_process = models.TextField(blank=True, null=True)


class ProcessStandard(TimeStampedModel, UUIDPrimaryKeyBase, NamedModel):
    evaluation = models.ForeignKey(Evaluation, related_name="process_standards", on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    conformity = models.CharField(max_length=10, blank=True, null=True, choices=FullNoPartial.choices)
    description = models.TextField(blank=True, null=True)


class Document(TimeStampedModel, UUIDPrimaryKeyBase, NamedModel):
    evaluation = models.ForeignKey(Evaluation, related_name="documents", on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    url = models.URLField(max_length=512, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    document_types = models.JSONField(default=list)
    # TODO - file upload

    _name_field = "title"


class EventDate(TimeStampedModel, UUIDPrimaryKeyBase, NamedModel):
    evaluation = models.ForeignKey(Evaluation, related_name="event_dates", on_delete=models.CASCADE)
    event_date_name = models.CharField(max_length=256, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    event_date_type = models.CharField(max_length=10, blank=True, null=True, choices=EventDateType.choices)
    reasons_for_change = models.TextField(blank=True, null=True)

    _name_field = "event_date_name"


class LinkOtherService(TimeStampedModel, UUIDPrimaryKeyBase, NamedModel):
    evaluation = models.ForeignKey(Evaluation, related_name="link_other_services", on_delete=models.CASCADE)
    name_of_service = models.CharField(max_length=256, blank=True, null=True)
    link_or_identifier = models.CharField(max_length=256, blank=True, null=True)

    _name_field = "name_of_service"


class EvaluationCost(TimeStampedModel, UUIDPrimaryKeyBase, NamedModel):
    evaluation = models.ForeignKey(Evaluation, related_name="costs", on_delete=models.CASCADE)
    item_name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    item_cost = models.FloatField(blank=True, null=True)
    earliest_spend_date = models.DateField(blank=True, null=True)
    latest_spend_date = models.DateField(blank=True, null=True)
    # TODO - add a total cost for eval
    # TODO - add column for notes on evaluation costs

    _name_field = "item_name"


dropdown_choices = {
    "document_types": DocumentType.choices,
    "economic_eval_type": EconomicEvaluationType.choices,
    "evaluation_type": EvaluationTypeOptions.choices,
    "event_date_name": EventDateOption.choices,
    "event_date_type": EventDateType.choices,
    "impact_eval_basis": ImpactAnalysisBasis.choices,
    "impact_eval_design_name": ImpactEvalDesign.choices,
    "impact_eval_effect_measure_interval": ImpactMeasureInterval.choices,
    "impact_eval_effect_measure_type": ImpactMeasureType.choices,
    "impact_eval_framework": ImpactFramework.choices,
    "impact_eval_interpretation": ImpactEvalInterpretation.choices,
    "impact_eval_interpretation_type": ImpactEvalInterpretation.choices,
    "measure_type": MeasureType.choices,
    "organisations": enums.Organisation.choices,
    "topics": Topic.choices,
}
