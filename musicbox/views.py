from django.views.generic import DetailView
from django.http import HttpResponse
from django.conf import settings

from musicbox.models import *
from events.models import Event

class AlbumDetailView(DetailView):

    model = Album

    def get_context_data(self, **kwargs):
	obj = super(AlbumDetailView, self).get_object()
	context = super(AlbumDetailView, self).get_context_data(**kwargs)
	context['events'] = Event.objects.later_than_now()
	return context

def download(request, album_slug, track_slug):
    """ We can count downloads here """
    album = Album.objects.get(slug__exact=album_slug)
    track = Track.objects.get(album=album, slug__exact=track_slug)
    track.download_count = track.download_count + 1
    track.save()

    response = HttpResponse(track.track, mimetype='audio/mp3')
    response['Content-Disposition'] = 'attachment; filename=%s.mp3' % track.title
    return response
