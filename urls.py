import os

from django.conf.urls import patterns, url, include
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import ListView, DetailView, TemplateView

from django.contrib import admin
admin.autodiscover()

from vbank.models import VoiceClip, Category

urlpatterns = patterns('',
	url(r'^how$', TemplateView.as_view(template_name='how.html'), name='how'),
	url(r'^about$', TemplateView.as_view(template_name='about.html'), name='about'),
	url(r'^voiceclips$', ListView.as_view(
	    queryset=VoiceClip.objects.active(),
		paginate_by=settings.VOICECLIP_LIST_PAGINATE_BY
		), name='all_clips'),
	# url(r'^categories/(?P<slug>[-.\w]+)$', DetailView.as_view(model=Category), name='category'),
	url(r'^categories/(?P<slug>[-.\w]+)$', 'vbank.views.category_detail', name='category'),
)

urlpatterns += patterns('',
	(r'^', include('accounts.urls')),
	(r'^ratings/', include('agon_ratings.urls')),
	# (r'^musicbox/', include('musicbox.urls')),
	(r'^events/', include('events.urls')),
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
