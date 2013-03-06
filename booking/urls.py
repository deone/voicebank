from django.conf.urls import patterns, url

urlpatterns = patterns('booking.views',
	url(r'^$', 'index', name='booking'),
)
