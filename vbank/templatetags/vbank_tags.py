from django import template
from django.conf import settings

from vbank.models import VoiceClip

register = template.Library()

@register.inclusion_tag('vbank/clip.html', takes_context=True)
def display_clip(context, clip):
    return {'STATIC_URL': context['STATIC_URL'], 'MEDIA_URL': context['MEDIA_URL'], 'clip': clip}

@register.inclusion_tag('vbank/list_of_voiceclips.html', takes_context=True)
def show_user_voiceclips(context, user, template):
    clips = user.voiceclip_set.filter(is_active=True)
    return {'voiceclip_list': clips, 'template': template, 'user': user,
	    'MEDIA_URL': context['MEDIA_URL']}
