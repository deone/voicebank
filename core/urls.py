from django.conf.urls.defaults import *

urlpatterns = patterns('core.views',
    url(r'^welcome$', 'index', name='welcome'),
    url(r'^dashboard$', 'dashboard', name='dashboard'),
    url(r'^voiceclips$', 'voiceclips', name='voiceclips'),
    url(r'^profile$', 'profile', name='profile'),
    url(r'^following$', 'following', name='following'),
)
