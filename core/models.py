from django.db import models
import datetime

class VoiceClip(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey('auth.User')
    voice_clip = models.FileField(upload_to='clips')
    date_added = models.DateTimeField(default=datetime.datetime.now(), editable=False)
    is_active = models.BooleanField(default=False)
    listens = models.IntegerField()
