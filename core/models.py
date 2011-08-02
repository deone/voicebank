from django.db import models

class VoiceClip(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey('auth.User')
    is_active = models.BooleanField(default=False)
    voice_clip = models.FileField(upload_to='clips')
