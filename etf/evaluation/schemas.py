from marshmallow import Schema, fields, validate

from . import models


class DateAndBlankField(fields.Date):
    def _deserialize(self, value, attr, data, **kwargs):
        if value:
            return super()._deserialize(value, attr, data, **kwargs)
        else:
            return None


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
    sample_size = fields.Int()
    sample_size_units = fields.Str(validate=validate.Length(max=256))
    sample_size_details = fields.Str()

    # Participant recruitment approach
    process_for_recruitment = fields.Str()
    recruitment_schedule = fields.Str()

    # Ethical considerations
    ethics_committee_approval = fields.Boolean()
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
    impact_eval_analysis_set = fields.Str()
    impact_eval_effect_measure = fields.Str()

    # Process evaluation design
    process_eval_methods = fields.Str(validate=validate.Length(max=256))

    # Process evaluation analysis
    process_eval_analysis_description = fields.Str()

    # Economic evaluation design
    economic_eval_type = fields.Str(validate=validate.Length(max=256))

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
    id = fields.Int(dump_only=True)
    name = fields.Str(validate=validate.Length(max=256))
    brief_description = fields.Str()
    rationale = fields.Str()
    materials_used = fields.Str()
    procedures = fields.Str()
    provider_description = fields.Str()
    modes_of_delivery = fields.Str()
    location = fields.Str()
    frequency_of_delivery = fields.Str()
    tailoring = fields.Str()
    fidelity = fields.Str()
    resource_requirements = fields.Str()
    geographical_information = fields.Str()


class OutcomeMeasureSchema(TimeStampedModelSchema):
    evaluation = fields.Nested(EvaluationSchema)
    id = fields.Int(dump_only=True)
    name = fields.Str(validate=validate.Length(max=256))
    primary_or_secondary = fields.Str(validate=validate.Length(max=10))  # TODO - choices
    direct_or_surrogate = fields.Str(validate=validate.Length(max=10))  # TODO - choices
    description = fields.Str()
    collection_process = fields.Str()
    timepoint = fields.Str()
    minimum_difference = fields.Str()
    relevance = fields.Str()


class OtherMeasureSchema(TimeStampedModelSchema):
    evaluation = fields.Nested(EvaluationSchema)
    id = fields.Int(dump_only=True)
    name = fields.Str(validate=validate.Length(max=256))
    description = fields.Str()
    collection_process = fields.Str()


class ProcessStandardSchema(TimeStampedModelSchema):
    evaluation = fields.Nested(EvaluationSchema)
    id = fields.Int(dump_only=True)
    name = fields.Str(validate=validate.Length(max=256))
    conformity = fields.Str(validate=validate.Length(max=10))
    description = fields.Str()


class DocumentSchema(TimeStampedModelSchema):
    evaluation = fields.Nested(EvaluationSchema)
    id = fields.Int(dump_only=True)
    title = fields.Str(validate=validate.Length(max=256))
    url = fields.Url(validate=validate.Length(max=512))
    description = fields.Str()


class EventDateSchema(TimeStampedModelSchema):
    evaluation = fields.Nested(EvaluationSchema)
    id = fields.Int(dump_only=True)
    name = fields.Str(validate=validate.Length(max=256))
    date = fields.Date()
    type = fields.Str(validate=validate.Length(max=10))
    reasons_for_change = fields.Str()


class LinkOtherServiceSchema(TimeStampedModelSchema):
    evaluation = fields.Nested(EvaluationSchema)
    id = fields.Int(dump_only=True)
    name_of_service = fields.Str(validate=validate.Length(max=256))
    link_or_identifier = fields.Str(validate=validate.Length(max=256))


class EvaluationCostSchema(TimeStampedModelSchema):
    evaluation = fields.Nested(EvaluationSchema)
    id = fields.Int(dump_only=True)
    item_name = fields.Str()
    description = fields.Str()
    item_cost = fields.Float()
    earliest_spend_date = fields.Date()
    latest_spend_date = fields.Date()
