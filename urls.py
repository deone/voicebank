import os

from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

from voicebank import AboutView, HowView
from core.views import VoiceClipListView, CategoryDetailView
from core.models import VoiceClip, Category

urlpatterns = patterns('',
	url(r'^how$', HowView.as_view(), name='how'),
	url(r'^about$', AboutView.as_view(), name='about'),
)

urlpatterns += patterns('django.views.generic',
	url(r'^voiceclips$', VoiceClipListView.as_view(), name='all_clips'),
	url(r'^categories/(?P<slug>[-.\w]+)$', CategoryDetailView.as_view(), name='category'),
)

urlpatterns += patterns('',
	(r'^', include('accounts.urls')),
	(r'^musicbox/', include('musicbox.urls')),
	(r'^events/', include('events.urls')),
	(r'^voicebank/', include('core.urls')), # Change app_name to voicebank later
	(r'^booking/', include('booking.urls')),
	(r'^comments/', include('django.contrib.comments.urls')),
	(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()

urlpatterns += patterns('',
	(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
		{'document_root': settings.MEDIA_ROOT}),
)
