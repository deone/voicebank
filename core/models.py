from django.db import models

class VoiceClip(models.Model):
    user = models.ForeignKey('auth.User')
    voice_clip = models.FileField(upload_to='clips')
