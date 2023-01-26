from datetime import date

from marshmallow import Schema

from etf.evaluation.schemas import DateAndBlankField


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


# TODO - add more tests for schemas, esp after validation added
