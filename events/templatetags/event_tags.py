from django import template

from voicebank.events.models import Event

register = template.Library()

@register.inclusion_tag('events/list_of_events.html')
def show_events():
    events = Event.objects.later_than_now()[:2]
    return {'events': events}
