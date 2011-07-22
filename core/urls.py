from django.conf.urls.defaults import *

urlpatterns = patterns('core.views',
    url(r'^$', 'upload', name='upload_voice_clip'),
)
