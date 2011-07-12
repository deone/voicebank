from django.db import models

class VoiceClip(models.Model):
    voice_clip = models.FileField(upload_to='clips')
