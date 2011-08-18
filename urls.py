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
    url(r'^help$', 'simple.direct_to_template', {'template':
	'help.html'}, name='help'),
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
    (r'^my_admin/jsi18n', 'django.views.i18n.javascript_catalog'),
    (r'^(?P<slug>[-.\w]+)$', 'accounts.views.profile'),
)

if settings.DEBUG:
	urlpatterns += patterns('',
		(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
			{'document_root': os.path.join(os.path.dirname(__file__), 'site_media')}),
	)
