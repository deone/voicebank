from django import template

register = template.Library()

@register.inclusion_tag('vbank/list_of_voiceclips.html', takes_context=True)
def display_voiceclip_list(context):
    return context
