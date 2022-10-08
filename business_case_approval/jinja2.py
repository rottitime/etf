import jinja2
from django.templatetags.static import static
from django.urls import reverse
import markdown
import pypugjs




@pypugjs.register_filter('markdown')
def _markdown(text, ast):
  return markdown.markdown(text)

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
