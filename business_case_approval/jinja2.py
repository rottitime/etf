import jinja2
from django.templatetags.static import static
from django.urls import reverse
from markdown_it import MarkdownIt
import pypugjs

markdown_converter = MarkdownIt()


@pypugjs.register_filter('markdown')
def markdown(text, ast):
    return markdown_converter.render(text)


def environment(**options):
    extra_options = dict()
    env = jinja2.Environment(
        **{
            **options,
            **extra_options,
        }
    )
    env.globals.update(
        {
            "static": static,
            "url": reverse,
        }
    )
    return env
