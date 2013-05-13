from django.views.generic import DetailView
from django.http import HttpResponse
from django.template import RequestContext

from sounds.models import *
from events.models import Event

class SoundDetailView(DetailView):

    model = SoundCollection 

    def get_context_data(self, **kwargs):
	obj = super(SoundDetailView, self).get_object()
	context = super(SoundDetailView, self).get_context_data(**kwargs)
	context['events'] = Event.objects.later_than_now()
	return context

def download(request, soundcoll_slug, track_slug):
    """ We can count downloads here """
    sound_collection = SoundCollection.objects.get(slug__exact=soundcoll_slug)
    track = Track.objects.get(sound_collection=sound_collection, slug__exact=track_slug)
    track.download_count = track.download_count + 1
    track.save()

    response = HttpResponse(track.track, mimetype='audio/mp3')
    response['Content-Disposition'] = 'attachment; filename=%s.mp3' % track.title
    return response
