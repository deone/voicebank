from django.conf.urls.defaults import *

urlpatterns = patterns('core.views',
    url(r'^welcome$', 'index', name='welcome'),
    url(r'^dashboard$', 'dashboard', name='dashboard'),
    url(r'^voiceclips$', 'voiceclips', name='voiceclips'),
)

urlpatterns += patterns('',
    url(r'^profile$', 'accounts.views.profile_edit', name='profile_edit'),
)
