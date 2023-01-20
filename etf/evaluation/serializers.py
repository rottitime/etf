from marshmallow import Schema, fields


class UserSchema(Schema):
    email = fields.Str()

class EvaluationSchema(Schema):
    user = fields.Nested(UserSchema())
    id = fields.UUID()