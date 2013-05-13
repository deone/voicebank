from django.conf.urls import url, patterns
from django.views.generic import ListView
from django.conf import settings

from sounds.models import SoundCollection
from sounds.views import SoundDetailView

urlpatterns = patterns('',
	url(r'^$', ListView.as_view(
	    queryset=SoundCollection.objects.filter(sound_type="Podcast"),
	    paginate_by=settings.PODCAST_CHANNELS_PAGINATE_BY,
	), name='podcasts'),
	url(r'^(?P<slug>[-.\w]+)$', SoundDetailView.as_view(), name='sound'),
)
