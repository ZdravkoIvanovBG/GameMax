from django import template

register = template.Library()


@register.filter(name='stars_repr')
def stars_repr(value):
    return value * "⭐"
