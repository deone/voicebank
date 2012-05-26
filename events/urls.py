from django.conf import settings
from django.conf.urls.defaults import *
from django.views.generic import ListView

from events.models import Event

urlpatterns = patterns('',
	url(r'^$', ListView.as_view(
	    model=Event,
	    paginate_by=settings.EVENTS_PAGINATE_BY,
	    ), name='events'),
)
