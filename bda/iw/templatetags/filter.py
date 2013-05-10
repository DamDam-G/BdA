from django import template

register = template.Library()

@register.filter
def Modulo(n, v):
    """

    """
    return n % v