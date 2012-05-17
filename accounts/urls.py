from django.conf.urls.defaults import *

urlpatterns = patterns('accounts.views', 
	url(r'^$', 'index', name='home'), 
	url(r'^join$', 'join', name='join'),
	url(r'^logout$', 'logout', name='logout'),
)

urlpatterns += patterns('django.contrib.auth.views',
    url(r'^login$', 'login', {'template_name': 'accounts/login.html'}, 'login'),
    """(r'^password_change$', 'password_change'),
    (r'^password_change/done$', 'password_change_done'),
    (r'^password_reset$', 'password_reset'),
    (r'^password_reset/done$', 'password_reset_done'),
    (r'^reset/(?P<uidb36>[0-9A-Za-z]{1,13})-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', 'password_reset_confirm'),
    (r'^reset/done$', 'password_reset_complete'),"""
)
