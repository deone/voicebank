from django.views.generic import DetailView

from musicbox.models import Album
from events.models import Event

class AlbumDetailView(DetailView):

    model = Album

    def get_context_data(self, **kwargs):
	obj = super(AlbumDetailView, self).get_object()
	context = super(AlbumDetailView, self).get_context_data(**kwargs)
	context['album_list'] = Album.objects.get_three_random_exclude(obj.id)
	context['events'] = Event.objects.later_than_now()
	return context
