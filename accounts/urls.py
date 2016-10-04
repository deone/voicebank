from django.conf.urls.defaults import *
from django.contrib.auth import views as auth_views

from accounts.forms import LoginForm
from accounts.views import ProfileDetailView

from .forms import PasswordResetEmailForm, ResetPasswordForm

urlpatterns = patterns('django.contrib.auth.views',
    url(r'^login/$', auth_views.login,
      {'authentication_form': LoginForm, 'template_name': 'accounts/login.html'}, name='login'),
    url(r'^password_reset/$', auth_views.password_reset, {
      'template_name': 'accounts/password_reset.html',
      'post_reset_redirect': '/password_reset/done/',
      'email_template_name': 'accounts/password_reset_email.html',
      'password_reset_form': PasswordResetEmailForm,
      'subject_template_name': 'accounts/password_reset_subject.txt'
    }, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, {'template_name': 'accounts/password_reset_done.html'}, name='password_reset_done'),
    url(r'^reset/(?P<uidb36>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', auth_views.password_reset_confirm, {
      'post_reset_redirect': '/reset/done/',
      'template_name': 'accounts/password_reset_confirm.html',
      'set_password_form': ResetPasswordForm
    }, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, {'template_name': 'accounts/password_reset_complete.html'}, name='password_reset_complete'),
)

urlpatterns += patterns('accounts.views', 
	url(r'^$', 'index', name='home'), 
	url(r'^join/$', 'join', name='join'),
	url(r'^profile/$', 'profile_edit', name='profile_edit'),
	url(r'^logout/$', 'logout', name='logout'),
	url(r'^(?P<slug>[-.\w]+)/$', ProfileDetailView.as_view(), name='profile'),
)
