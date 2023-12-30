from django import template
from films.models import Session

register = template.Library()

@register.simple_tag
def get_obj(pk, attr):
    object = getattr(Session.objects.get(pk=int(pk)).film, attr)
    return object