from django import template

from core.models import Page

register = template.Library()

@register.simple_tag
def get_page(pk: int) -> Page:
    """Returns a Page object with the given pk"""

    return Page.objects.get(pk=pk)