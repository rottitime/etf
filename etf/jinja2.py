import jinja2
from django.contrib import messages
from django.templatetags.static import static
from django.urls import reverse
from markdown_it import MarkdownIt

markdown_converter = MarkdownIt()

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


def parse_markdown(raw_markdown):
    return markdown_converter.render(raw_markdown)


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
            "parse_markdown": parse_markdown
        }
    )
    return env
