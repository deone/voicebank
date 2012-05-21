from django.conf.urls.defaults import *
from django.views.generic import ListView, DetailView

from musicbox.models import Album

urlpatterns = patterns('musicbox.views',
	url(r'^$', ListView.as_view(
	    model=Album,
	    ), name='musicbox_home'),
	url(r'^(?P<slug>[-.\w]+)$', DetailView.as_view(
	    model=Album,
	    ), name='album'),
)
