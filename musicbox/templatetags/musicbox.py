from django import template

register = template.Library()

@register.inclusion_tag('musicbox/list_of_albums.html', takes_context=True)
def display_album_list(context):
    return context
