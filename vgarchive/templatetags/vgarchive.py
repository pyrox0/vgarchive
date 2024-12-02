from django import template
from django.conf import settings

__all__ = ["settings_value"]

register = template.Library()


# settings value
@register.simple_tag
def settings_value(name):  # noqa
    return getattr(settings, name, "")
