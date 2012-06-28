from django import template

from musicbox.models import Album

register = template.Library()

#@register.inclusion_tag('musicbox/list_of_albums.html', takes_context=True)
def display_album_list(context):
    return context

@register.inclusion_tag('musicbox/list_of_albums.html')
def display_albums_excluding(album):
    return {
	    "album_list": Album.objects.get_three_random_exclude(album.id)
	    }

@register.inclusion_tag('musicbox/list_of_albums.html')
def display_albums(limit=None):
    return {
	    "album_list": Album.objects.all()[:limit]
	    }
