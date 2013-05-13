import os

from django.conf.urls import patterns, url, include
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import ListView, DetailView, TemplateView

from django.contrib import admin
admin.autodiscover()

from sounds.models import SoundCollection
from vbank.models import VoiceClip, Category

urlpatterns = patterns('',
	url(r'^how$', TemplateView.as_view(template_name='how.html'), name='how'),
	url(r'^about$', TemplateView.as_view(template_name='about.html'), name='about'),
	url(r'^voiceclips$', ListView.as_view(
	    queryset=VoiceClip.objects.active(),
	    paginate_by=settings.VOICECLIP_LIST_PAGINATE_BY
	), name='all_clips'),
	url(r'^podcasts$', ListView.as_view(
	    queryset=SoundCollection.objects.filter(sound_type="Podcast"),
	    paginate_by=settings.PODCAST_CHANNELS_PAGINATE_BY,
	), name='podcasts'),
	url(r'^albums$', ListView.as_view(
	    queryset=SoundCollection.objects.filter(sound_type="Album"),
	    paginate_by=settings.MUSICBOX_ALBUMS_PAGINATE_BY,
	), name='albums'),

	# We commented this out because of the customer care category customization
	# url(r'^categories/(?P<slug>[-.\w]+)$', DetailView.as_view(model=Category), name='category'),
	url(r'^categories/(?P<slug>[-.\w]+)$', 'vbank.views.category_detail', name='category'),

	url(r'^podcasts/(?P<slug>[-.\w]+)$', 'sounds.views.sound_detail', name='sound'),
	url(r'^(?P<soundcoll_slug>[-.\w]+)/(?P<track_slug>[-.\w]+)$', 'sounds.views.download', name='track'),
)

urlpatterns += patterns('',
	(r'^', include('accounts.urls')),
	(r'^ratings/', include('agon_ratings.urls')),
	# (r'^musicbox/', include('musicbox.urls')),
	# (r'^podcast/', include('podcast.urls')),
	(r'^events/', include('events.urls')),
	# (r'^sounds/', include('sounds.urls')),
	(r'^voicebank/', include('vbank.urls')),
	(r'^booking/', include('booking.urls')),
	(r'^contact/', include('contact.urls')),
	(r'^comments/', include('django.contrib.comments.urls')),
	(r'^admin/', include(admin.site.urls)),
	(r'^articles/', include('django.contrib.flatpages.urls')),
)

urlpatterns += staticfiles_urlpatterns()

urlpatterns += patterns('',
	(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
		{'document_root': settings.MEDIA_ROOT}),
)
