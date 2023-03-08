import datetime

import marshmallow
from nose.tools import assert_raises

from etf.evaluation import utils


def test_get_arguments():
    def flibble(woz, flim="flam"):
        assert False

    result = utils.get_arguments(flibble, "floop")
    assert result == {"woz": "floop", "flim": "flam"}, result

    result = utils.get_arguments(flibble, "foo", "bar")
    assert result == {"woz": "foo", "flim": "bar"}, result

    result = utils.get_arguments(flibble, flim="blam", woz="flooble")
    assert result == {"woz": "flooble", "flim": "blam"}, result


def test_resolve_schema():
    class MySchema(marshmallow.Schema):
        thing = marshmallow.fields.String()

    result = utils.resolve_schema(MySchema)
    assert isinstance(result, marshmallow.Schema)

    result = utils.resolve_schema(MySchema())
    assert isinstance(result, marshmallow.Schema)


def test_process_self():
    def flibble(self, baz):
        return {"self": self, "baz": baz}

    data = {"self": "flam", "bimble": "burble"}
    func, arguments = utils.process_self(flibble, data)
    assert func("floop") == {"self": "flam", "baz": "floop"}
    assert arguments == {"bimble": "burble"}

    data = {"booble": "flooble"}
    func, arguments = utils.process_self(flibble, data)
    assert func("flipp", "floop") == {"self": "flipp", "baz": "floop"}
    assert arguments == {"booble": "flooble"}


def test_apply_schema():
    class MySchema(marshmallow.Schema):
        date = marshmallow.fields.Date()

    result = utils.apply_schema(MySchema, {"date": "2012-04-01"}, "load")
    expected = {"date": datetime.date(2012, 4, 1)}
    assert result == expected

    result = utils.apply_schema(MySchema, {"date": datetime.date(2012, 4, 1)}, "dump")
    expected = {"date": "2012-04-01"}
    assert result == expected

    with assert_raises(ValueError):
        result = utils.apply_schema(MySchema, {"date": datetime.date(2012, 4, 1)}, "wibble")
