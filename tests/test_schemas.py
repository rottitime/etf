from datetime import date
from etf import evaluation

from marshmallow import Schema

from etf.evaluation.schemas import DateAndBlankField, EvaluationSchema
from etf.evaluation.models import Evaluation


class MadeUpSchema(Schema):
    date = DateAndBlankField(allow_none=True)


def test_date_and_blank_field():
    schema = MadeUpSchema()
    deserialized_obj = schema.load({"date": "2022-11-13"})
    assert deserialized_obj["date"] == date(2022, 11, 13)
    deserialized_obj = schema.load({"date": ""})
    assert deserialized_obj["date"] is None
    deserialized_obj = schema.load({"date": None})
    assert deserialized_obj["date"] is None


def test_evaluation_schema_all_fields():
    model_field_names = {f.name for f in Evaluation._meta.get_fields()}
    schema_field_names = set(EvaluationSchema._declared_fields.keys())
    assert schema_field_names == model_field_names


# TODO - add more tests for schemas, esp after validation added
