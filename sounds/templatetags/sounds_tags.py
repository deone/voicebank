from django import template

register = template.Library()

from sounds.models import SoundCollection

@register.inclusion_tag('sounds/list_of_sounds.html', takes_context=True)
def display_sounds_list(context):
    return context

@register.inclusion_tag('sounds/list_of_sounds.html')
def display_podcasts(limit=None):
    return {
	    "soundcollection_list": SoundCollection.objects.filter(sound_type="Podcast")[:limit]
	    }

@register.inclusion_tag('sounds/list_of_sounds.html')
def display_sounds_excluding(sound):
    return {
	    "soundcollection_list": SoundCollection.objects.get_three_random_exclude(sound.id)
	    }
