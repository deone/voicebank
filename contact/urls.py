from django.conf.urls import url, patterns

urlpatterns = patterns('contact.views',
	url(r'^$', 'index', name='contact'),
)
