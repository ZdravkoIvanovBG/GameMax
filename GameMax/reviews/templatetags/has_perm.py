from django import template

register = template.Library()


@register.filter(name="has_permission")
def has_permission(user, perm_name):
    return user.has_perm(perm_name)
