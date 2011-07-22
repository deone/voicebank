from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'accounts.views.index', name='home'),
    url(r'^join/$', 'accounts.views.join', name='join'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name':
	'accounts/login.html'}, 'login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'accounts/logged_out.html'}, 'logout'),
    (r'^password_change/$', 'django.contrib.auth.views.password_change'),
    (r'^password_change/done/$', 'django.contrib.auth.views.password_change_done'),
    (r'^password_reset/$', 'django.contrib.auth.views.password_reset'),
    (r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done'),
    (r'^reset/(?P<uidb36>[0-9A-Za-z]{1,13})-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', 'django.contrib.auth.views.password_reset_confirm'),
    (r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete'),
)
