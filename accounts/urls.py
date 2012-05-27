from django.conf.urls.defaults import *

urlpatterns = patterns('django.contrib.auth.views',
	url(r'^login$', 'login', {'template_name': 'accounts/login.html'}, 'login'),
)

# We need to remove these later
urlpatterns += patterns('core.views',
	url(r'^contact$', 'contact', name='contact'),
)

urlpatterns += patterns('accounts.views', 
	url(r'^$', 'index', name='home'), 
	url(r'^join$', 'join', name='join'),
	url(r'^profile$', 'profile_edit', name='profile_edit'),
	url(r'^logout$', 'logout', name='logout'),
	url(r'^(?P<slug>[-.\w]+)$', 'profile', name='profile'),
)
