from marshmallow import Schema, fields, validate

from . import models


class DateAndBlankField(fields.Date):
    def _deserialize(self, value, attr, data, **kwargs):
        if value:
            return super()._deserialize(value, attr, data, **kwargs)
        else:
            return None


class FloatAndBlankField(fields.Float):
    def _deserialize(self, value, attr, data, **kwargs):
        if value:
            return super()._deserialize(value, attr, data, **kwargs)
        else:
            return None


class IntAndBlankField(fields.Int):
    def _deserialize(self, value, attr, data, **kwargs):
        if value:
            return super()._deserialize(value, attr, data, **kwargs)
        else:
            return None


def is_non_neg_int_or_none(value):
    error = validate.ValidationError("Value should be a non-negative integer")
    if not isinstance(value, int):
        if not value:
            value = None
        else:
            raise error
    elif value < 0:
        raise error


class UserSchema(Schema):
    email = fields.Str()


class TimeStampedModelSchema(Schema):
    created_at = fields.DateTime(dump_only=True)
    modified_at = fields.DateTime(dump_only=True)


class EvaluationSchema(TimeStampedModelSchema):
    # TODO - add more validation esp. for choice fields, around dates
    users = fields.Function(lambda o: UserSchema(many=True).dump(o.users.all()))
    id = fields.UUID()
    title = fields.Str(required=True, validate=validate.Length(max=256))
    short_title = fields.Str(validate=validate.Length(max=64))
    brief_description = fields.Str()
    topics = fields.Raw()
    organisations = fields.Raw()
    status = fields.Str(validate=validate.Length(max=256), default=models.EvaluationStatus.DRAFT.value)
    doi = fields.Str(validate=validate.Length(max=64))
    page_statuses = fields.Raw()

    # Issue description
    issue_description = fields.Str()
    those_experiencing_issue = fields.Str()
    why_improvements_matter = fields.Str()
    who_improvements_matter_to = fields.Str()
    current_practice = fields.Str()
    issue_relevance = fields.Str()

    # Evaluation type
    evaluation_type = fields.Raw()

    # Studied population
    studied_population = fields.Str()
    eligibility_criteria = fields.Str()
    sample_size = IntAndBlankField(validate=is_non_neg_int_or_none)
    sample_size_units = fields.Str(validate=validate.Length(max=256))
    sample_size_details = fields.Str()

    # Participant recruitment approach
    process_for_recruitment = fields.Str()
    recruitment_schedule = fields.Str()

    # Ethical considerations
    ethics_committee_approval = fields.Str()
    ethics_committee_details = fields.Str()
    ethical_state_given_existing_evidence_base = fields.Str()
    risks_to_participants = fields.Str()
    risks_to_study_team = fields.Str()
    participant_involvement = fields.Str()
    participant_information = fields.Str()
    participant_consent = fields.Str()
    participant_payment = fields.Str()
    confidentiality_and_personal_data = fields.Str()
    breaking_confidentiality = fields.Str()
    other_ethical_information = fields.Str()

    # Impact evaluation design
    impact_eval_design_name = fields.Raw()
    impact_eval_design_justification = fields.Str()
    impact_eval_design_description = fields.Str()
    impact_eval_design_features = fields.Str()
    impact_eval_design_equity = fields.Str()
    impact_eval_design_assumptions = fields.Str()
    impact_eval_design_approach_limitations = fields.Str()

    # Impact evaluation analysis
    impact_eval_framework = fields.Str(validate=validate.Length(max=64))
    impact_eval_basis = fields.Str(validate=validate.Length(max=64))
    impact_eval_analysis_set = fields.Str()
    impact_eval_effect_measure_type = fields.Str(validate=validate.Length(max=64))
    impact_eval_primary_effect_size_measure = fields.Str()
    impact_eval_effect_measure_interval = fields.Str(validate=validate.Length(max=64))
    impact_eval_primary_effect_size_desc = fields.Str()
    impact_eval_interpretation_type = fields.Str(validate=validate.Length(max=64))
    impact_eval_sensitivity_analysis = fields.Str()
    impact_eval_subgroup_analysis = fields.Str()
    impact_eval_missing_data_handling = fields.Str()
    impact_eval_fidelity = fields.Str(validate=validate.Length(max=10))
    impact_eval_desc_planned_analysis = fields.Str()

    # Process evaluation design
    process_eval_methods = fields.Str(validate=validate.Length(max=256))

    # Process evaluation analysis
    process_eval_analysis_description = fields.Str()

    # Economic evaluation design
    economic_eval_type = fields.Str(validate=validate.Length(max=256))
    perspective_costs = fields.Str()
    perspective_benefits = fields.Str()
    monetisation_approaches = fields.Str()
    economic_eval_design_details = fields.Str()

    # Economic evaluation analysis
    economic_eval_analysis_description = fields.Str()

    # Other evaluation design
    other_eval_design_type = fields.Str()
    other_eval_design_details = fields.Str()

    # Other evaluation analysis
    other_eval_analysis_description = fields.Str()

    # Impact evaluation findings
    impact_eval_comparison = fields.Str()
    impact_eval_outcome = fields.Str()
    impact_eval_interpretation = fields.Str(validate=validate.Length(max=256))
    impact_eval_point_estimate_diff = fields.Str()
    impact_eval_lower_uncertainty = fields.Str()
    impact_eval_upper_uncertainty = fields.Str()

    # Economic evaluation findings
    economic_eval_summary_findings = fields.Str()
    economic_eval_findings = fields.Str()

    # Process evaluation findings
    process_eval_summary_findings = fields.Str()
    process_eval_findings = fields.Str()

    # Other evaluation findings
    other_eval_summary_findings = fields.Str()
    other_eval_findings = fields.Str()


class InterventionSchema(TimeStampedModelSchema):
    evaluation = fields.Nested(EvaluationSchema())
    id = fields.UUID(dump_only=True)
    intervention_name = fields.Str(validate=validate.Length(max=256))
    intervention_brief_description = fields.Str()
    intervention_rationale = fields.Str()
    intervention_materials_used = fields.Str()
    intervention_procedures = fields.Str()
    intervention_provider_description = fields.Str()
    intervention_modes_of_delivery = fields.Str()
    intervention_location = fields.Str()
    intervention_frequency_of_delivery = fields.Str()
    intervention_tailoring = fields.Str()
    intervention_fidelity = fields.Str()
    intervention_resource_requirements = fields.Str()
    intervention_geographical_information = fields.Str()


class OutcomeMeasureSchema(TimeStampedModelSchema):
    evaluation = fields.Nested(EvaluationSchema)
    id = fields.UUID(dump_only=True)
    outcome_measure_name = fields.Str(validate=validate.Length(max=256))
    outcome_measure_primary_or_secondary = fields.Str(validate=validate.Length(max=10))  # TODO - choices
    outcome_measure_direct_or_surrogate = fields.Str(validate=validate.Length(max=10))  # TODO - choices
    outcome_measure_measure_type = fields.Str(validate=validate.Length(max=256))
    outcome_measure_description = fields.Str()
    outcome_measure_collection_process = fields.Str()
    outcome_measure_timepoint = fields.Str()
    outcome_measure_minimum_difference = fields.Str()
    outcome_measure_relevance = fields.Str()


class OtherMeasureSchema(TimeStampedModelSchema):
    evaluation = fields.Nested(EvaluationSchema)
    id = fields.UUID(dump_only=True)
    other_measures_name = fields.Str(validate=validate.Length(max=256))
    other_measures_measure_type = fields.Str(validate=validate.Length(max=256))
    other_measures_description = fields.Str()
    other_measures_collection_process = fields.Str()


class ProcessStandardSchema(TimeStampedModelSchema):
    evaluation = fields.Nested(EvaluationSchema)
    id = fields.UUID(dump_only=True)
    process_standard_name = fields.Str(validate=validate.Length(max=256))
    process_standard_conformity = fields.Str(validate=validate.Length(max=10))
    process_standard_description = fields.Str()


class DocumentSchema(TimeStampedModelSchema):
    evaluation = fields.Nested(EvaluationSchema)
    id = fields.UUID(dump_only=True)
    document_title = fields.Str(validate=validate.Length(max=256))
    document_url = fields.Url(validate=validate.Length(max=512))
    document_description = fields.Str()
    document_types = fields.Raw()


class EventDateSchema(TimeStampedModelSchema):
    evaluation = fields.Nested(EvaluationSchema)
    id = fields.UUID(dump_only=True)
    event_date_name = fields.Str(validate=validate.Length(max=256))
    event_date_date = DateAndBlankField()
    event_date_type = fields.Str(validate=validate.Length(max=10))
    event_date_reasons_for_change = fields.Str()


class LinkOtherServiceSchema(TimeStampedModelSchema):
    evaluation = fields.Nested(EvaluationSchema)
    id = fields.UUID(dump_only=True)
    links_name_of_service = fields.Str(validate=validate.Length(max=256))
    links_link_or_identifier = fields.Str(validate=validate.Length(max=256))


class EvaluationCostSchema(TimeStampedModelSchema):
    evaluation = fields.Nested(EvaluationSchema)
    id = fields.UUID(dump_only=True)
    evaluation_cost_item_name = fields.Str()
    evaluation_cost_description = fields.Str()
    evaluation_cost_item_cost = FloatAndBlankField()
    evaluation_cost_earliest_spend_date = DateAndBlankField()
    evaluation_cost_latest_spend_date = DateAndBlankField()
