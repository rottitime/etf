import jinja2
import pypugjs
from django.templatetags.static import static
from django.urls import reverse
from markdown_it import MarkdownIt

markdown_converter = MarkdownIt()


@pypugjs.register_filter("markdown")
def markdown(text, ast):
    return markdown_converter.render(text)


def finalize(thing):
    if thing is None:
        return ""
    else:
        return thing


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
        }
    )
    return env
