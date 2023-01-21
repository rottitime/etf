from marshmallow import Schema, fields, validate


class UserSchema(Schema):
    email = fields.Str()


class EvaluationSchema(Schema):
    # TODO - add validation?
    user = fields.Nested(UserSchema())
    id = fields.UUID()
    title = fields.Str(validate=validate.Length(max=256))
    description = fields.Str()
    topics = fields.Str() # TODO - this should be a JSON field
    organisation = fields.Str(validate=validate.Length(max=256))
    is_published = fields.Boolean()
    
    # Issue description
    issue_description = fields.Str()
    those_experiencing_issue = fields.Str()
    why_improvements_matter = fields.Str()
    who_improvements_matter_to = fields.Str()
    current_practice = fields.Str()
    issue_relevance = fields.Str()

    created_at = fields.DateTime(dump_only=True)
    modified_at = fields.DateTime(dump_only=True)


class Intervention(Schema):
    evaluation = fields.Nested(EvaluationSchema())
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


class OutcomeMeasureSchema(Schema):
    evaluation = fields.Nested(EvaluationSchema)
    name = fields.Str(validate=validate.Length(max=256))
    primary_or_secondary = fields.Str(validate=validate.Length(max=10)) # TODO - choices
    direct_or_surrogate = fields.Str(validate=validate.Length(max=10)) # TODO - choices
    description = fields.Str()
    collection_process = fields.Str()
    timepoint = fields.Str()
    minimum_difference = fields.Str()
    relevance = fields.Str()
