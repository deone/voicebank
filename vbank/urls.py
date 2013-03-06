from django.conf.urls import patterns, url

urlpatterns = patterns('vbank.views',
    url(r'^voiceclips$', 'voiceclips', name='voiceclips'),
)
