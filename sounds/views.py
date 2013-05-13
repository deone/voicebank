from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponse
from django.template import RequestContext

from sounds.models import *
from events.models import Event

def sound_detail(request, slug, template='sounds/soundcollection_detail.html'):
    sound = get_object_or_404(SoundCollection, slug=slug)

    if sound.sound_type == "Podcast":
	return render_to_response(template, {
		'sound': sound,
		'events': Event.objects.later_than_now(),
	    }, context_instance=RequestContext(request))

def download(request, soundcoll_slug, track_slug):
    """ We can count downloads here """
    sound_collection = SoundCollection.objects.get(slug__exact=soundcoll_slug)
    track = Track.objects.get(sound_collection=sound_collection, slug__exact=track_slug)
    track.download_count = track.download_count + 1
    track.save()

    response = HttpResponse(track.track, mimetype='audio/mp3')
    response['Content-Disposition'] = 'attachment; filename=%s.mp3' % track.title
    return response
