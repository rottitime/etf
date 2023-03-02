from collections import defaultdict

import jinja2
from django.contrib import messages
from django.templatetags.static import static
from django.urls import reverse

from etf.evaluation import fields, models, pages

DEFAULT = object()

page_progress_icon_dict = defaultdict(
    lambda: "bi-question-circle",
    {
        pages.EvaluationPageStatus.IN_PROGRESS.name: "bi-fast-forward-circle",
        pages.EvaluationPageStatus.DONE.name: "bi-check-circle",
        pages.EvaluationPageStatus.NOT_STARTED.name: "bi-dash-circle",
    },
)


def finalize(thing):
    if thing is None:
        return ""
    else:
        return thing


def is_empty_selected(data, name):
    if data.get(name) in ("", None):
        return "selected"
    else:
        return ""


# TODO: Add tests for this
def is_selected(data, name, value):
    if str(data.get(name)) == str(value):
        return "selected"
    else:
        return ""


def is_in(data, name, value):
    if value in data.get(name):
        return "selected"
    else:
        return ""


def get_page_name(db_name):
    return pages.page_display_names[db_name]


def get_page_status_name(db_name):
    return models.get_page_status_display_name(db_name)


def get_page_progress_icon(progress_status):
    return page_progress_icon_dict[progress_status]


def list_to_options(iterable):
    result = tuple({"value": item[0], "text": item[1]} for item in iterable)
    return result


def environment(**options):
    extra_options = {"autoescape": True}
    env = jinja2.Environment(
        finalize=finalize,
        **{
            **options,
            **extra_options,
        },
    )
    env.globals.update(
        {
            "static": static,
            "url": reverse,
            "is_selected": is_selected,
            "is_empty_selected": is_empty_selected,
            "DEFAULT": DEFAULT,
            "get_messages": messages.get_messages,
            "is_in": is_in,
            "get_page_display_name": get_page_name,
            "get_page_status_display_name": get_page_status_name,
            "get_page_progress_icon": get_page_progress_icon,
            "list_to_options": list_to_options,
            "get_field_help_text": fields.get_field_help_text,
            "get_field_tooltip_text": fields.get_field_tooltip_text,
        }
    )
    return env
