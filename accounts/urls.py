from django.conf.urls.defaults import *
from django.contrib.auth import views as auth_views

from accounts.forms import LoginForm
from accounts.views import ProfileDetailView

urlpatterns = patterns('django.contrib.auth.views',
    url(r'^login/$', auth_views.login,
      {'authentication_form': LoginForm, 'template_name': 'accounts/login.html'}, name='login'),
)

urlpatterns += patterns('accounts.views', 
	url(r'^$', 'index', name='home'), 
	url(r'^join/$', 'join', name='join'),
	url(r'^profile/$', 'profile_edit', name='profile_edit'),
	url(r'^logout/$', 'logout', name='logout'),
	url(r'^(?P<slug>[-.\w]+)/$', ProfileDetailView.as_view(), name='profile'),
)
