from django.conf.urls.defaults import *

urlpatterns = patterns('vbank.views',
    url(r'^voiceclips$', 'voiceclips', name='voiceclips'),
)
