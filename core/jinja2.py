from django.templatetags.static import static
from django.utils.translation import gettext
from django.urls import reverse
from jinja2 import Environment


def environment(**options):
    env = Environment(**options)
    env.globals.update({
        'static': static,
        'url': reverse,
        'trans': gettext
    })
    return env
