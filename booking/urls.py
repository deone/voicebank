from django.conf.urls.defaults import *

urlpatterns = patterns('booking.views',
	url(r'^$', 'booking', name='booking'),
)
