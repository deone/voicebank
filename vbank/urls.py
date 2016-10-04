from django.conf.urls import patterns, url

urlpatterns = patterns('vbank.views',
    url(r'^$', 'clip_search', name='all_clips'),
    url(r'^upload/$', 'clip_upload', name='clip_upload'),
)
