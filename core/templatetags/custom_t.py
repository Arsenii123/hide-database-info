from datetime import datetime
from django import template

register = template.Library()


@register.filter
def is_thursday(value):
  current_day = datetime.now().isoweekday()
  if current_day == 4:
    return value - (value * 25 / 100)
  return value


@register.filter
def num53(value):
  try:
    return float(value) / 53
  except (TypeError, ValueError):
    return value


@register.filter
def reverse(value):

  string_value = str(value)


  if 'a' in string_value:
    return string_value[::-1]
  else:
    return value


