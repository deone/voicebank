import os

from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^', include('accounts.urls')),
    (r'^home/', include('core.urls')),
    (r'^admin/', include(admin.site.urls)),
    url(r'^(?P<slug>[-A-za-z0-9_]+)$', 'accounts.views.profile',
	name='user_profile'),
)

if settings.DEBUG:
	urlpatterns += patterns('',
		(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
			{'document_root': os.path.join(os.path.dirname(__file__), 'site_media')}),
	)
