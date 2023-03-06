import functools
import inspect

import marshmallow

from . import models

event_names = set()


class DuplicateEvent(Exception):
    pass


def get_arguments(func, *args, **kwargs):
    """Calculate what the args would be inside a function"""
    sig = inspect.signature(func)
    bound_args = sig.bind(*args, **kwargs)
    bound_args.apply_defaults()
    arguments = bound_args.arguments
    return arguments


def _register_event(event_name, arguments):
    event_names.add(event_name)
    arguments = {key: value for (key, value) in arguments.items() if key != "self"}
    event = models.Event(name=event_name, data=arguments)
    event.save()


def resolve_schema(schema):
    """Allow either a class or an instance to be passed"""
    if isinstance(schema, marshmallow.schema.SchemaMeta):
        schema = schema()
    return schema


def register_event(event_name):
    def _decorator(func):
        func.event_name = event_name

        @functools.wraps(func)
        def _inner(*args, **kwargs):
            arguments = get_arguments(func, *args, **kwargs)
            _register_event(event_name, arguments)
            return func(*args, **kwargs)

        return _inner

    return _decorator


def process_self(func, arguments):
    """Remove `self` from arguments and bind it to func"""
    if "self" in arguments:
        func = functools.partial(func, arguments["self"])
        arguments = {k: v for k, v in arguments.items() if k != "self"}
    return func, arguments


def apply_schema(schema, data, load_or_dump):
    """Apply a schema to some data"""
    if not schema:
        return data
    if load_or_dump not in ("load", "dump"):
        raise ValueError(f"Unknown value {load_or_dump}")
    if schema:
        schema = resolve_schema(schema)
        arguments = getattr(schema, load_or_dump)(data)
    return arguments


def with_schema(default=None, load=None, dump=None):
    """Applies the load_schema.load on the arguments to the function,
    and dump_schema.dump on the result of the function.

    This ensures that validation has been passed and that the result of the
    function is JSON serialisable"""
    load_schema = load or default
    dump_schema = dump or default

    def _decorator(func):
        @functools.wraps(func)
        def _inner(*args, **kwargs):
            arguments = get_arguments(func, *args, **kwargs)
            bound_func, arguments = process_self(func, arguments)
            arguments = apply_schema(load_schema, arguments, "load")
            result = bound_func(**arguments)
            result = apply_schema(dump_schema, result, "dump")
            return result

        return _inner

    return _decorator


class Facade:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

        all_event_names = tuple(
            event_name for entity in kwargs.values() for event_name in getattr(entity, "event_names", ())
        )
        if len(all_event_names) != len(set(all_event_names)):
            raise DuplicateEvent(all_event_names)
        self.event_names = all_event_names


class Entity:
    def __init__(self):
        possible_methods = (getattr(self, key) for key in dir(self) if not key.startswith("_"))
        possible_event_names = (getattr(item, "event_name", None) for item in possible_methods)
        self.event_names = tuple(item for item in possible_event_names if item)
