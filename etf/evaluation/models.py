import uuid

from django.core.serializers.json import DjangoJSONEncoder
from django.db import models
from django_use_email_as_username.models import BaseUser, BaseUserManager

from . import choices, enums
from .pages import EvaluationPageStatus, get_default_page_statuses


class SaveEvaluationOnSave(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        evaluation = self.evaluation
        evaluation.save()


class UUIDPrimaryKeyBase(models.Model):
    class Meta:
        abstract = True

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


class User(BaseUser, UUIDPrimaryKeyBase):
    objects = BaseUserManager()
    username = None
    verified = models.BooleanField(default=False, blank=True, null=True)
    invited_at = models.DateTimeField(default=None, blank=True, null=True)
    invite_accepted_at = models.DateTimeField(default=None, blank=True, null=True)
    last_token_sent_at = models.DateTimeField(editable=False, blank=True, null=True)
    is_external_user = models.BooleanField(editable=True, default=False)

    def save(self, *args, **kwargs):
        self.email = self.email.lower()
        super().save(*args, **kwargs)

    def has_signed_up(self):
        return self.last_login is not None


class NamedModel:
    _name_field = "name"

    def set_name(self, value):
        setattr(self, self._name_field, value)

    def get_name(self):
        if hasattr(self, "get_readable_name"):
            return self.get_readable_name()
        return getattr(self, self._name_field)


def get_topic_display_name(db_name):
    result = [topic[1] for topic in choices.Topic.choices if topic[0] == db_name]
    return result[0]


def get_organisation_display_name(db_name):
    result = [organisation[1] for organisation in enums.Organisation.choices if organisation[0] == db_name]
    return result[0]


def get_list_evaluation_types_display_name(db_name):
    result = [
        evaluation_type[1] for evaluation_type in choices.EvaluationTypeOptions.choices if evaluation_type[0] == db_name
    ]
    return result[0]


def get_status_display_name(db_name):
    result = [status[1] for status in choices.EvaluationStatus.choices if status[0] == db_name]
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

    title = models.CharField(max_length=1024, blank=True, null=True)
    short_title = models.CharField(max_length=128, blank=True, null=True)
    brief_description = models.TextField(blank=True, null=True)
    topics = models.JSONField(default=list)  # TODO - do we use these?
    organisations = models.JSONField(default=list)  # TODO - how are we going to do orgs?
    status = models.CharField(max_length=256, blank=False, null=False, default=choices.EvaluationStatus.DRAFT.value)
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
    evaluation_type_other = models.CharField(max_length=256, blank=True, null=True)

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
    ethics_committee_approval = models.CharField(max_length=3, blank=True, null=True)
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
    impact_design_name = models.JSONField(default=list)
    impact_design_name_other = models.CharField(max_length=256, blank=True, null=True)
    impact_design_justification = models.TextField(blank=True, null=True)
    impact_design_description = models.TextField(blank=True, null=True)
    impact_design_features = models.TextField(blank=True, null=True)
    impact_design_equity = models.TextField(blank=True, null=True)
    impact_design_assumptions = models.TextField(blank=True, null=True)
    impact_design_approach_limitations = models.TextField(blank=True, null=True)

    # Impact evaluation analysis
    # TODO - add analysis plan document?
    impact_framework = models.CharField(max_length=64, blank=True, null=True)
    impact_framework_other = models.CharField(max_length=256, blank=True, null=True)
    impact_basis = models.CharField(max_length=64, blank=True, null=True)
    impact_basis_other = models.CharField(max_length=256, blank=True, null=True)
    impact_analysis_set = models.TextField(blank=True, null=True)
    impact_effect_measure_type = models.CharField(max_length=64, blank=True, null=True)
    impact_effect_measure_type_other = models.CharField(max_length=256, blank=True, null=True)
    impact_primary_effect_size_measure = models.TextField(blank=True, null=True)
    impact_effect_measure_interval = models.CharField(max_length=64, blank=True, null=True)
    impact_effect_measure_interval_other = models.CharField(max_length=256, blank=True, null=True)
    impact_primary_effect_size_desc = models.TextField(blank=True, null=True)
    impact_interpretation_type = models.CharField(max_length=64, blank=True, null=True)
    impact_interpretation_type_other = models.CharField(max_length=256, blank=True, null=True)
    impact_sensitivity_analysis = models.TextField(blank=True, null=True)
    impact_subgroup_analysis = models.TextField(blank=True, null=True)
    impact_missing_data_handling = models.TextField(blank=True, null=True)
    impact_fidelity = models.CharField(max_length=10, blank=True, null=True)
    impact_description_planned_analysis = models.TextField(blank=True, null=True)
    # TODO - add more

    # Process evaluation design
    process_methods = models.CharField(blank=True, null=True, max_length=256)
    # TODO - add more

    # Process evaluation analysis
    # TODO - add analysis plan document
    process_analysis_description = models.TextField(blank=True, null=True)

    # Economic evaluation design
    economic_type = models.CharField(max_length=256, blank=True, null=True)
    perspective_costs = models.TextField(blank=True, null=True)
    perspective_benefits = models.TextField(blank=True, null=True)
    monetisation_approaches = models.TextField(blank=True, null=True)
    economic_design_details = models.TextField(blank=True, null=True)

    # Economic evaluation analysis
    economic_analysis_description = models.TextField(blank=True, null=True)
    # TODO - add more details

    # Other evaluation design
    other_design_type = models.TextField(blank=True, null=True)
    other_design_details = models.TextField(blank=True, null=True)

    # Other evaluation analysis
    other_analysis_description = models.TextField(blank=True, null=True)
    # TODO - add more

    # Impact evaluation findings
    impact_comparison = models.TextField(blank=True, null=True)
    impact_outcome = models.TextField(blank=True, null=True)
    impact_interpretation = models.CharField(max_length=256, blank=True, null=True)
    impact_interpretation_other = models.CharField(max_length=256, blank=True, null=True)
    impact_point_estimate_diff = models.TextField(blank=True, null=True)
    impact_lower_uncertainty = models.TextField(blank=True, null=True)
    impact_upper_uncertainty = models.TextField(blank=True, null=True)

    # Economic evaluation findings
    economic_summary_findings = models.TextField(blank=True, null=True)
    economic_findings = models.TextField(blank=True, null=True)

    # Process evaluation findings
    process_summary_findings = models.TextField(blank=True, null=True)
    process_findings = models.TextField(blank=True, null=True)

    # Other evaluation findings
    other_summary_findings = models.TextField(blank=True, null=True)
    other_findings = models.TextField(blank=True, null=True)

    # Search
    search_text = models.TextField(blank=True, null=True, max_length=65536)

    # For matching with initial data upload from RSM - evaluation id
    rsm_id = models.FloatField(blank=True, null=True)

    def get_readable_name(self):
        return self.title

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

    def get_list_evaluation_types_display_names(self):
        return [get_list_evaluation_types_display_name(x) for x in self.evaluation_type]

    def get_economic_type_display_name(self):
        if self.economic_type in choices.EconomicEvaluationType.names:
            return choices.EconomicEvaluationType.mapping[self.economic_type]
        else:
            return ""

    def get_related_intervention_names(self):
        related_interventions = self.interventions.all()
        names = [i.name for i in related_interventions]
        return names

    def get_related_outcome_measure_names(self):
        related_outcome_measures = self.outcome_measures.all()
        names = [i.name for i in related_outcome_measures]
        return names

    def get_status_display_name(self):
        return get_status_display_name(self.status)

    def get_impact_framework_display_name(self):
        return choices.ImpactFramework.mapping[self.impact_framework]

    def get_impact_basis_display_name(self):
        return choices.ImpactAnalysisBasis.mapping[self.impact_basis]

    def get_impact_effect_measure_type_display_name(self):
        return choices.ImpactMeasureType.mapping[self.impact_effect_measure_type]

    def get_impact_effect_measure_interval_display_name(self):
        return choices.ImpactMeasureInterval.mapping[self.impact_effect_measure_interval]

    def get_impact_interpretation_type_display_name(self):
        return choices.ImpactEvalInterpretation.mapping[self.impact_interpretation_type]

    def get_impact_fidelity_display_name(self):
        return choices.YesNo.mapping[self.impact_fidelity]

    def get_impact_interpretation_display_name(self):
        return choices.ImpactEvalInterpretation.mapping[self.impact_interpretation]

    def get_ethics_committee_approval_display_name(self):
        return choices.YesNo.mapping[self.ethics_committee_approval]

    def get_impact_design_name_display_name(self):
        return [name[1] for name in choices.ImpactEvalDesign.choices if name[0] in self.impact_design_name]

    def __str__(self):
        return f"{self.id} : {self.title}"

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        # TODO: reduce massive duplication in search text calculations
        all_fields = self._meta.fields
        combined_field_data = ""

        # Unique fields
        unique_fields = ["users"]

        # List fields
        list_fields = ["topics", "organisations"]

        # Ignore fields
        search_text_field = "search_text"
        page_statuses_field = "page_statuses"
        status_field = "status"

        # Foreign key fields
        foreign_key_fields = [
            "interventions",
            "outcome_measures",
            "other_measures",
            "process_standards",
            "link_other_services",
            "costs",
            "documents",
            "event_dates",
        ]

        # Multiple choice fields
        multiple_choice_fields = ["evaluation_type"]

        # YesNo and similar fields - can be ignored
        yes_no_fields = [
            "ethics_committee_approval",
            "impact_fidelity",
        ]

        # Single choice fields
        single_choice_fields = [
            "impact_framework",
            "impact_effect_measure_interval",
            "impact_basis",
            "impact_effect_measure_type",
            "impact_interpretation_type",
            "impact_interpretation",
            "economic_type",
        ]

        # Simple fields
        exclusion_fields = (
            foreign_key_fields
            + multiple_choice_fields
            + single_choice_fields
            + [search_text_field]
            + [page_statuses_field]
            + [status_field]
            + list_fields
            + unique_fields
            + yes_no_fields
        )
        simple_fields = [field for field in all_fields if field.name not in exclusion_fields]

        for f in simple_fields:
            value = self.__getattribute__(f.name)
            if value:
                combined_field_data += f"{value}|"
        for foreign_key_field in foreign_key_fields:
            related_field = self._meta.get_field(foreign_key_field)
            relevant_model = related_field.related_model
            related_objects = relevant_model.objects.filter(evaluation_id=self.id)

            if related_objects:
                for related_object in related_objects:
                    related_object_search_text = related_object.get_search_text()
                    if related_object_search_text:
                        combined_field_data += f"{related_object_search_text}|"

        # Multiple choice fields & list fields

        evaluation_type_text = choices.turn_choices_list_to_string(
            self.evaluation_type, choices.EvaluationTypeOptions.options
        )
        combined_field_data += evaluation_type_text

        impact_design_name_text = choices.turn_choices_list_to_string(
            self.impact_design_name, choices.ImpactEvalDesign.options
        )
        combined_field_data += impact_design_name_text

        topics_text = choices.turn_choices_list_to_string(self.topics, choices.Topic.options)
        combined_field_data += topics_text

        organisations_text = choices.turn_choices_list_to_string(self.organisations, enums.Organisation.options)
        combined_field_data += organisations_text

        # Single choice fields

        economic_types_text = choices.map_choice_or_other(
            self.economic_type, choices.EconomicEvaluationType.options, append_separator=True
        )
        combined_field_data += economic_types_text

        impact_design_name_text = choices.map_choice_or_other(
            self.impact_design_name, choices.ImpactEvalDesign.options, append_separator=True
        )
        combined_field_data += impact_design_name_text

        impact_effect_measure_interval_text = choices.map_choice_or_other(
            self.impact_effect_measure_interval, choices.ImpactMeasureInterval.options, append_separator=True
        )
        combined_field_data += impact_effect_measure_interval_text

        impact_framework_text = choices.map_choice_or_other(
            self.impact_framework, choices.ImpactFramework.options, append_separator=True
        )
        combined_field_data += impact_framework_text

        impact_basis_text = choices.map_choice_or_other(
            self.impact_basis, choices.ImpactAnalysisBasis.options, append_separator=True
        )
        combined_field_data += impact_basis_text

        impact_effect_measure_type_text = choices.map_choice_or_other(
            self.impact_effect_measure_type, choices.ImpactMeasureType.options, append_separator=True
        )
        combined_field_data += impact_effect_measure_type_text

        impact_interpretation_type_text = choices.map_choice_or_other(
            self.impact_interpretation_type, choices.ImpactEvalInterpretation.options, append_separator=True
        )
        combined_field_data += impact_interpretation_type_text

        combined_field_data = combined_field_data.strip("|")
        self.search_text = combined_field_data
        return super().save()


class Intervention(TimeStampedModel, UUIDPrimaryKeyBase, NamedModel, SaveEvaluationOnSave):
    evaluation = models.ForeignKey(Evaluation, related_name="interventions", on_delete=models.CASCADE)
    name = models.CharField(max_length=1024, blank=True, null=True)
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

    def get_readable_name(self):
        return self.name

    def get_search_text(self):
        searchable_fields = [
            str(self.name),
            str(self.brief_description),
            str(self.rationale),
            str(self.materials_used),
            str(self.procedures),
            str(self.provider_description),
            str(self.modes_of_delivery),
            str(self.location),
            str(self.frequency_of_delivery),
            str(self.fidelity),
            str(self.resource_requirements),
            str(self.geographical_information),
        ]

        searchable_fields = [field for field in searchable_fields if field not in (None, "", " ", "None")]

        return "|".join(searchable_fields)


class OutcomeMeasure(TimeStampedModel, UUIDPrimaryKeyBase, NamedModel, SaveEvaluationOnSave):
    evaluation = models.ForeignKey(Evaluation, related_name="outcome_measures", on_delete=models.CASCADE)
    name = models.CharField(max_length=256, blank=True, null=True)
    primary_or_secondary = models.CharField(max_length=10, blank=True, null=True)
    direct_or_surrogate = models.CharField(max_length=10, blank=True, null=True)
    measure_type = models.CharField(max_length=256, blank=True, null=True)
    measure_type_other = models.CharField(max_length=256, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    collection_process = models.TextField(blank=True, null=True)
    timepoint = models.TextField(blank=True, null=True)
    minimum_difference = models.TextField(blank=True, null=True)
    relevance = models.TextField(blank=True, null=True)

    def get_readable_name(self):
        return self.name

    def get_primary_or_secondary_display_name(self):
        return choices.OutcomeType.mapping[self.primary_or_secondary]

    def get_direct_or_surrogate_display_name(self):
        return choices.OutcomeMeasure.mapping[self.direct_or_surrogate]

    def get_measure_type_display_name(self):
        return choices.MeasureType.mapping[self.measure_type]

    def get_search_text(self):
        primary_or_secondary = [
            value[1] for value in choices.OutcomeType.choices if value[0] == self.primary_or_secondary
        ]
        direct_or_surrogate = [
            value[1] for value in choices.OutcomeMeasure.choices if value[0] == self.direct_or_surrogate
        ]
        measure_type = [value[1] for value in choices.MeasureType.choices if value[0] == self.measure_type]

        searchable_fields = [
            str(self.name),
            str(self.measure_type_other),
            str(self.description),
            str(self.collection_process),
            str(self.timepoint),
            str(self.minimum_difference),
            str(self.relevance),
            "|".join(primary_or_secondary),
            "|".join(direct_or_surrogate),
            "|".join(measure_type),
        ]

        searchable_fields = [field for field in searchable_fields if field not in (None, "", " ", "None")]

        return "|".join(searchable_fields)


class OtherMeasure(TimeStampedModel, UUIDPrimaryKeyBase, NamedModel, SaveEvaluationOnSave):
    evaluation = models.ForeignKey(Evaluation, related_name="other_measures", on_delete=models.CASCADE)
    name = models.CharField(max_length=256, blank=True, null=True)
    measure_type = models.CharField(max_length=256, blank=True, null=True)
    measure_type_other = models.CharField(max_length=256, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    collection_process = models.TextField(blank=True, null=True)

    def get_readable_name(self):
        return self.name

    def get_measure_type_display_name(self):
        return choices.MeasureType.mapping[self.measure_type]

    def get_search_text(self):
        measure_type = [value[1] for value in choices.MeasureType.choices if value[0] == self.measure_type]

        searchable_fields = [
            str(self.name),
            str(self.measure_type_other),
            str(self.description),
            str(self.collection_process),
            "|".join(measure_type),
        ]

        searchable_fields = [field for field in searchable_fields if field not in (None, "", " ", "None")]

        return "|".join(searchable_fields)


class ProcessStandard(TimeStampedModel, UUIDPrimaryKeyBase, NamedModel, SaveEvaluationOnSave):
    evaluation = models.ForeignKey(Evaluation, related_name="process_standards", on_delete=models.CASCADE)
    name = models.CharField(max_length=1024)
    conformity = models.CharField(max_length=10, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def get_readable_name(self):
        return self.name

    def get_conformity_display_name(self):
        return choices.FullNoPartial.mapping[self.conformity]

    def get_search_text(self):
        conformity = [value[1] for value in choices.YesNoPartial.choices if value[0] == self.conformity]

        searchable_fields = [
            str(self.name),
            str(self.description),
            "|".join(conformity),
        ]

        searchable_fields = [field for field in searchable_fields if field not in (None, "", " ", "None")]

        return "|".join(searchable_fields)


class Document(TimeStampedModel, UUIDPrimaryKeyBase, NamedModel, SaveEvaluationOnSave):
    evaluation = models.ForeignKey(Evaluation, related_name="documents", on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    url = models.URLField(max_length=512, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    document_types = models.JSONField(default=list)
    document_type_other = models.CharField(max_length=256, blank=True, null=True)
    # TODO - file upload

    _name_field = "title"

    def get_readable_name(self):
        return self.title

    def get_search_text(self):
        document_types = [value[1] for value in choices.DocumentType.choices if value[0] in self.document_types]

        searchable_fields = [
            str(self.title),
            str(self.description),
            str(self.url),
            str(self.document_type_other),
            "|".join(document_types),
        ]

        searchable_fields = [field for field in searchable_fields if field not in (None, "", " ", "None")]

        return "|".join(searchable_fields)


class EventDate(TimeStampedModel, UUIDPrimaryKeyBase, NamedModel, SaveEvaluationOnSave):
    evaluation = models.ForeignKey(Evaluation, related_name="event_dates", on_delete=models.CASCADE)
    event_date_name = models.CharField(max_length=256, blank=True, null=True)
    event_date_name_other = models.CharField(max_length=256, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    event_date_type = models.CharField(max_length=10, blank=True, null=True)

    _name_field = "event_date_name"

    def get_readable_name(self):
        if self.event_date_name in choices.EventDateOption.values:
            if self.event_date_name == choices.EventDateOption.OTHER.value:
                return self.event_date_name_other
            return choices.EventDateOption.mapping[self.event_date_name]
        return self.event_date_name

    def get_search_text(self):
        event_date_type = [value[1] for value in choices.EventDateType.choices if value[0] == self.event_date_type]
        event_date_name = [value[1] for value in choices.EventDateOption.choices if value[0] == self.event_date_name]

        searchable_fields = [
            str(self.date),
            "|".join(event_date_type),
            "|".join(event_date_name),
        ]

        searchable_fields = [field for field in searchable_fields if field not in (None, "", " ", "None", [])]

        return "|".join(searchable_fields)


class LinkOtherService(TimeStampedModel, UUIDPrimaryKeyBase, NamedModel, SaveEvaluationOnSave):
    evaluation = models.ForeignKey(Evaluation, related_name="link_other_services", on_delete=models.CASCADE)
    name_of_service = models.CharField(max_length=256, blank=True, null=True)
    link_or_identifier = models.CharField(max_length=256, blank=True, null=True)

    _name_field = "name_of_service"

    def get_readable_name(self):
        return self.name_of_service

    def get_search_text(self):
        searchable_fields = [
            str(self.name_of_service),
            str(self.link_or_identifier),
        ]

        searchable_fields = [field for field in searchable_fields if field not in (None, "", " ", "None")]

        return "|".join(searchable_fields)


class EvaluationCost(TimeStampedModel, UUIDPrimaryKeyBase, NamedModel, SaveEvaluationOnSave):
    evaluation = models.ForeignKey(Evaluation, related_name="costs", on_delete=models.CASCADE)
    item_name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    item_cost = models.FloatField(blank=True, null=True)
    earliest_spend_date = models.DateField(blank=True, null=True)
    latest_spend_date = models.DateField(blank=True, null=True)
    # TODO - add a total cost for eval
    # TODO - add column for notes on evaluation costs

    _name_field = "item_name"

    def get_readable_name(self):
        return self.item_name

    def get_search_text(self):
        searchable_fields = [
            str(self.item_name),
            str(self.description),
            str(self.item_cost),
            str(self.earliest_spend_date),
            str(self.latest_spend_date),
        ]

        searchable_fields = [field for field in searchable_fields if field not in (None, "", " ", "None")]

        return "|".join(searchable_fields)
