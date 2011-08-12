from django.db import models

import datetime

class VoiceClip(models.Model):
    user = models.ForeignKey('auth.User')
    name = models.CharField(max_length=30)
    voice_clip = models.FileField(upload_to='clips/%Y/%m/%d')
    language = models.CharField(max_length=30)
    date_added = models.DateTimeField(default=datetime.datetime.now(), editable=False)
    is_active = models.BooleanField(default=False)
    listens = models.IntegerField(default=0)

    def __unicode__(self):
	return u'%s by %s' % (self.name, self.user.get_full_name())


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
	return self.name


class VoiceClipCategory(models.Model):
    voice_clip = models.ForeignKey(VoiceClip)
    category = models.ForeignKey(Category)

    def __unicode__(self):
	return self.category.name
