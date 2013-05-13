from django.conf.urls import url, patterns

from sounds.views import SoundDetailView

urlpatterns = patterns('',
	url(r'^(?P<slug>[-.\w]+)$', SoundDetailView.as_view(), name='sound'),
)
