from django.db import models

import datetime

class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="category_pics")

    class Meta:
	verbose_name_plural = "Categories"
	ordering = ['-name']

    def __unicode__(self):
	return self.name

    @models.permalink
    def get_absolute_url(self):
	return ('category', [self.id])

class VoiceClip(models.Model):
    user = models.ForeignKey('auth.User')
    name = models.CharField(max_length=30)
    voice_clip = models.FileField(upload_to='clips/%Y/%m/%d')
    language = models.CharField(max_length=30)
    date_added = models.DateTimeField(default=datetime.datetime.now(), editable=False)
    is_active = models.BooleanField(default=False)
    listens = models.IntegerField(default=0)
    category = models.ForeignKey(Category)

    class Meta:
	ordering = ['-date_added']

    def __unicode__(self):
	return u'%s by %s' % (self.name, self.user.get_full_name())


class Booking(models.Model):
    user = models.ForeignKey('auth.User')
    name_on_teller = models.CharField(max_length=30)
    date_of_payment = models.DateField()
    bank_name = models.CharField(max_length=30)

    def __unicode__(self):
	return self.name_on_teller


class Contact(models.Model):
    pass
