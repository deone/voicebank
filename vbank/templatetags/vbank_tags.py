from django import template
from django.conf import settings

from vbank.models import VoiceClip

register = template.Library()

@register.inclusion_tag('vbank/clip.html', takes_context=True)
def display_clip(context, clip):
    return {'STATIC_URL': context['STATIC_URL'], 'MEDIA_URL': context['MEDIA_URL'], 'clip': clip}
