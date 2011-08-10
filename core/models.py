from django.db import models

import datetime

class VoiceClip(models.Model):
    user = models.ForeignKey('auth.User')
    name = models.CharField(max_length=30)
    voice_clip = models.FileField(upload_to='clips')
    language = models.CharField(max_length=30)
    date_added = models.DateTimeField(default=datetime.datetime.now(), editable=False)
    is_active = models.BooleanField(default=False)
    listens = models.IntegerField()

    def __unicode__(self):
	return u'%s by %s' % (self.name, self.user.get_full_name())
