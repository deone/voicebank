from django.conf.urls import url, patterns
from django.views.generic import ListView
from django.conf import settings

from sounds.models import SoundCollection

urlpatterns = patterns('',
	url(r'^$', ListView.as_view(
	    queryset=SoundCollection.objects.filter(sound_type="Album"),
	    paginate_by=settings.MUSICBOX_ALBUMS_PAGINATE_BY,
	), name='albums'),
)
