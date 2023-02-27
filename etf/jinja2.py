import jinja2
from django.contrib import messages
from django.templatetags.static import static
from django.urls import reverse

from etf.evaluation import models, pages

DEFAULT = object()


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


def is_selected(data, name, value):
    if data.get(name) is value:
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
    if progress_status == pages.EvaluationPageStatus.IN_PROGRESS.name:
        return "bi-fast-forward-circle"
    elif progress_status == pages.EvaluationPageStatus.DONE.name:
        return "bi-check-circle"
    elif progress_status == pages.EvaluationPageStatus.NOT_STARTED.name:
        return "bi-dash-circle"
    else:
        return "bi-question-circle"


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
        }
    )
    return env
