from datetime import date

from marshmallow import Schema

from etf.evaluation import models, schemas
from etf.evaluation.schemas import DateAndBlankField, EvaluationSchema


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


def check_schema_model_match_fields(model_name, schema_name, related_fields_to_ignore):
    model = getattr(models, model_name)
    schema = getattr(schemas, schema_name)
    model_field_names = {f.name for f in model._meta.get_fields()}
    model_field_names_to_include = model_field_names.difference(related_fields_to_ignore)
    schema_field_names = set(schema._declared_fields.keys())
    assert schema_field_names == model_field_names_to_include


def test_evaluation_schema_has_relevant_fields():
    related_fields_to_ignore = {
        "interventions",
        "outcome_measures",
        "evaluation_types",
        "other_measures",
        "process_standard",
        "documents",
        "event_date",
        "link_other_service",
        "cost",
    }
    check_schema_model_match_fields(
        model_name="Evaluation", schema_name="EvaluationSchema", related_fields_to_ignore=related_fields_to_ignore
    )


# TODO - add more tests for schemas, esp after validation added
