from django.conf.urls.defaults import *

urlpatterns = patterns('contact.views',
	url(r'^$', 'index', name='contact'),
)
