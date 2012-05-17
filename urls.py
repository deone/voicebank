import os

from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

from core.models import VoiceClip, Category
from accounts.views import events_context_var

voiceclip_dict = {
	'queryset': VoiceClip.objects.filter(is_active=True),
	'extra_context': {
	    'events': events_context_var
	    }
	}

category_dict = {
	'queryset': Category.objects.all(),
	'extra_context': {
	    'events': events_context_var
	    }
	}

urlpatterns = patterns('django.views.generic',
    url(r'^how$', 'simple.direct_to_template', {'template':
	'how.html', 'extra_context': {
	    'events': events_context_var
	    }}, name='how'),
    url(r'^about$', 'simple.direct_to_template', {'template': 'about.html',
	'extra_context': {
	    'events': events_context_var
	    }},
	name='about'),
    url(r'^voiceclips$', 'list_detail.object_list', voiceclip_dict, name='all_clips'),
    url(r'^categories/(?P<object_id>\d+)$', 'list_detail.object_detail',
	category_dict, name='category'),
)

urlpatterns += patterns('',

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^', include('accounts.urls')),
    (r'^musicbox/', include('musicbox.urls')),
    (r'^home/', include('core.urls')),
    url(r'^booking$', 'core.views.booking', name='booking'),
    url(r'^contact$', 'core.views.contact', name='contact'),
    url(r'^events$', 'core.views.events', name='events'),
    (r'^admin/', include(admin.site.urls)),
    url(r'^(?P<slug>[-.\w]+)$', 'accounts.views.profile', name='profile'),
)

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += patterns('',
	    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
		    {'document_root': settings.MEDIA_ROOT}),
    )
