from django import template

register = template.Library()

from sounds.models import SoundCollection

def display_podcast_list(context):
    return context

@register.inclusion_tag('sounds/list_of_sounds.html')
def display_podcast_excluding(sound):
    return {
	    "podcast_list": SoundCollection.objects.filter(sound_type="Podcast").get_three_random_exclude(sound.id)
	    }

@register.inclusion_tag('sounds/list_of_sounds.html')
def display_podcasts(limit=None):
    return {
	    "podcast_list": SoundCollection.objects.filter(sound_type="Podcast")[:limit]
	    }
