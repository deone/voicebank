from django.views.generic import DetailView
from musicbox.models import Album

class AlbumDetailView(DetailView):

    model = Album

    def get_object(self):
	obj = super(AlbumDetailView, self).get_object()
	return obj

    def get_context_data(self, **kwargs):
	obj = self.get_object()
	context = super(AlbumDetailView, self).get_context_data(**kwargs)
	context['album_list'] = Album.objects.get_three_random_exclude(obj.id)
	return context
