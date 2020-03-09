import random
from django import template
from django.conf import settings
from django.templatetags.static import static
from django.utils.safestring import mark_safe
from webpack_loader.templatetags.webpack_loader import utils

register = template.Library()


@register.simple_tag
def render_bundle(bundle_name, extension=None, config="DEFAULT", attrs=""):
    bundle = utils._get_bundle(bundle_name, extension, config)
    tags = []
    for chunk in bundle:
        url = chunk["url"]
        if not settings.IS_ENV_LOCAL:
            url = static("{{cookiecutter.vuejs_project_name}}/{}".format(chunk["name"]))

        if chunk["name"].endswith((".js", ".js.gz")):
            tags.append(
                ('<script type="text/javascript" src="{0}" {1}></script>').format(
                    url, attrs
                )
            )
        elif chunk["name"].endswith((".css", ".css.gz")):
            tags.append(
                ('<link type="text/css" href="{0}" rel="stylesheet" {1}/>').format(
                    url, attrs
                )
            )

    return mark_safe("\n".join(tags))
