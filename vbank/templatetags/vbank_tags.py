from django import template
from django.conf import settings

from vbank.models import VoiceClip

register = template.Library()

@register.inclusion_tag('vbank/list_of_voiceclips.html', takes_context=True)
def display_voiceclip_list(context):
    return context

@register.inclusion_tag('vbank/list_of_voiceclips.html')
def show_user_voiceclips(user, template):
    clips = user.voiceclip_set.filter(is_active=True)
    return {'voiceclip_list': clips, 'template': template, 'user': user}
