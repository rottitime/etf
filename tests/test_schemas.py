from datetime import date
from nose.tools import with_setup

from marshmallow import Schema

from etf.evaluation import models, schemas
from etf.evaluation.schemas import DateAndBlankField, EvaluationSchema
from .utils import with_authenticated_client


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


# Might not always want schemas to match, but we do for now
def check_schema_model_match_fields(model_name, schema_name, related_fields_to_ignore={}):
    model = getattr(models, model_name)
    schema = getattr(schemas, schema_name)
    model_field_names = {f.name for f in model._meta.get_fields()}
    model_field_names_to_include = model_field_names.difference(related_fields_to_ignore)
    schema_field_names = set(schema._declared_fields.keys())
    assert schema_field_names == model_field_names_to_include, model_field_names_to_include.difference(
        schema_field_names
    )


def test_evaluation_schema_has_relevant_fields():
    check_schema_model_match_fields(model_name="Evaluation", schema_name="EvaluationSchema")


def test_intervention_schema_has_relevant_fields():
    check_schema_model_match_fields(model_name="Intervention", schema_name="InterventionSchema")


def test_outcome_measure_schema_has_relevant_fields():
    check_schema_model_match_fields(model_name="OutcomeMeasure", schema_name="OutcomeMeasureSchema")


def test_other_measure_schema_has_relevant_fields():
    check_schema_model_match_fields(model_name="OtherMeasure", schema_name="OtherMeasureSchema")


def setup_evaluation():
    user, _ = models.User.objects.get_or_create(email="mrs.tiggywinkle@cabinetoffice.gov.uk")
    user.save()
    new_eval = models.Evaluation(title="Test evaluation schemas")
    new_eval.save()
    # TODO - add more fields
    new_eval.users.add(user)
    new_eval.save()
    model_names = ["OutcomeMeasure", "OtherMeasure", "Intervention"]
    for name in model_names:
        model = getattr(models, name)
        for i in range(3):
            new_obj = model(name=f"New obj {i}", evaluation=new_eval)
            new_obj.save()


def teardown_evaluation():
    evaluation = models.Evaluation.objects.get(title="Test evaluation schemas")
    evaluation.delete()
    user = models.User.objects.get(email="mrs.tiggywinkle@cabinetoffice.gov.uk")
    user.delete()


@with_setup(setup_evaluation, teardown_evaluation)
@with_authenticated_client
def test_evaluation_schema_dump(client):
    evaluation_schema = EvaluationSchema()
    evaluation = models.Evaluation.objects.get(title="Test evaluation schemas")
    serialized_evaluation = evaluation_schema.dump(evaluation)
    assert serialized_evaluation
