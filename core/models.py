from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify

from model_utils.managers import PassThroughManager

from datetime import datetime

class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="category_pics")
    slug = models.SlugField(unique=True, editable=False)

    class Meta:
	verbose_name_plural = "Voice Clip Categories"
	ordering = ['-name']

    def __unicode__(self):
	return self.name

    def save(self, *args, **kwargs):
	self.slug = slugify(self.name)
	super(Category, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
	return ('category', [self.slug])


class VoiceClipQuerySet(models.query.QuerySet):
    def active(self):
	return self.filter(is_active=True)


class VoiceClip(models.Model):
    user = models.ForeignKey('auth.User')
    name = models.CharField(max_length=30)
    voice_clip = models.FileField(upload_to='clips/%Y/%m/%d')
    language = models.CharField(max_length=30)
    is_active = models.BooleanField('Approval status', default=False)
    is_top = models.BooleanField('Top Clip', default=False)
    category = models.ForeignKey(Category)
    date_added = models.DateTimeField(default=datetime.now(), editable=False)
    is_top_timestamp = models.DateTimeField(default=datetime.now(),
	    editable=False)

    objects = PassThroughManager.for_queryset_class(VoiceClipQuerySet)()

    class Meta:
	ordering = ['-date_added']

    def __unicode__(self):
	return u'%s by %s' % (self.name, self.user.get_full_name())

    def save(self, *args, **kwargs):
	try:
	    orig = VoiceClip.objects.get(pk=self.pk)
	except VoiceClip.DoesNotExist:
	    pass
	else:
	    if not orig.is_top and self.is_top:
		self.is_top_timestamp = datetime.now()
	super(VoiceClip, self).save(*args, **kwargs)


class Booking(models.Model):
    user = models.ForeignKey('auth.User')
    name_on_teller = models.CharField(max_length=30)
    date_of_payment = models.DateField()
    bank_name = models.CharField(max_length=30)

    def __unicode__(self):
	return self.name_on_teller


class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.CharField(max_length=11)
    comment = models.CharField(max_length=255)

    def __unicode__(self):
	return u'%s : %s' % (self.name, self.comment)


class EventQuerySet(models.query.QuerySet):
    def later_than_now(self):
	return self.filter(date__gt=datetime.now())[:settings.EVENTS_DISPLAY_LIMIT]


class Event(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to="event_images")
    description = models.CharField(max_length=255)
    venue = models.CharField(max_length=100)
    date = models.DateTimeField(default=datetime.now)

    objects = PassThroughManager.for_queryset_class(EventQuerySet)()

    class Meta:
	ordering = ['-date']

    def __unicode__(self):
	return self.title
