from django.conf.urls.defaults import *
from django.views.generic import ListView
from django.conf import settings

from musicbox.models import Album
from musicbox.views import AlbumDetailView

urlpatterns = patterns('musicbox.views',
	url(r'^$', ListView.as_view(
	    model=Album,
	    paginate_by=settings.MUSICBOX_ALBUMS_PAGINATE_BY,
	    ), name='musicbox_home'),
	url(r'^(?P<slug>[-.\w]+)$', AlbumDetailView.as_view(), name='album'),
	url(r'^(?P<album_slug>[-.\w]+)/(?P<track_slug>[-.\w]+)$', 'download', name='track'),
)
