from django import template

register = template.Library()

@register.filter
def inc(value):
    return "0" + str(value + 1)

@register.filter
def cut(value):
    return value[:200] + "..."