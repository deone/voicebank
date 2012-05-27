from django.conf.urls.defaults import *

urlpatterns = patterns('core.views',
    url(r'^voiceclips$', 'voiceclips', name='voiceclips'),
)
