# Django
from django import template

register = template.Library()

@register.filter
def getattr_filter(obj, attr):
    return getattr(obj, attr)