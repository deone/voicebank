from django import template

from datetime import datetime

register = template.Library()

@register.inclusion_tag('vbank/list_of_voiceclips.html', takes_context=True)
def display_voiceclip_list(context):
    return context

@register.inclusion_tag('vbank/user_voiceclips.html')
def show_voiceclips(user):
    clips = user.voiceclip_set.filter(is_active=True)
    return {'voiceclip_list': clips}
