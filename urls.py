import os

from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

from core.models import VoiceClip, Category

voiceclip_dict = {
	'queryset': VoiceClip.objects.all(),
	}

category_dict = {
	'queryset': Category.objects.all(),
	}

urlpatterns = patterns('django.views.generic',
    url(r'^how_it_works$', 'simple.direct_to_template', {'template':
	'how_it_works.html'}, name='how_it_works'),
    url(r'^registering$', 'simple.direct_to_template', {'template':
	'registering.html'}, name='registering'),
    url(r'^payment_process$', 'simple.direct_to_template', {'template':
	'payment_process.html'}, name='payment_process'),
    url(r'^subscription_cost$', 'simple.direct_to_template', {'template':
	'subscription_cost.html'}, name='subscription_cost'),
    url(r'^booking$', 'simple.direct_to_template', {'template':
	'booking.html'}, name='booking'),
    url(r'^what_to_bring$', 'simple.direct_to_template', {'template':
	'what_to_bring.html'}, name='what_to_bring'),
    url(r'^renewals$', 'simple.direct_to_template', {'template':
	'renewals.html'}, name='renewals'),
    url(r'^voiceclips/all$', 'list_detail.object_list', voiceclip_dict, name='all_clips'),
    url(r'^categories/(?P<object_id>\d+)/voiceclips$', 'list_detail.object_detail',
	category_dict, name='category'),
)

urlpatterns += patterns('',

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^', include('accounts.urls')),
    (r'^home/', include('core.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^(?P<slug>[-.\w]+)$', 'accounts.views.profile'),
)

if settings.DEBUG:
	urlpatterns += patterns('',
		(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
			{'document_root': os.path.join(os.path.dirname(__file__), 'site_media')}),
	)
