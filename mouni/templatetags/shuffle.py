import random
from django import template

register = template.Library()

@register.filter
def shuffle(arg):
	aux = list(arg)[:]
	random.shuffle(aux)
	return aux

@register.filter
def get_item(dictionary, key):
	return dictionary.get(key)