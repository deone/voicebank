from django.db import models
from django.template.defaultfilters import slugify

from model_utils.managers import PassThroughManager

SOUND_TYPE_CHOICES = (
    ("Podcast", "Podcast"),
    ("Album", "Album"),
)

class SoundCollectionQuerySet(models.query.QuerySet):
    def get_three_random_exclude(self, sound_coll_id):
	return self.exclude(pk=sound_coll_id).order_by('?')[:3]

class SoundCollection(models.Model):
    artiste = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    art = models.ImageField(upload_to="sound_art")
    info = models.CharField(max_length=1000)
    slug = models.SlugField(unique=True, editable=False)
    sound_type = models.CharField(max_length=10, choices=SOUND_TYPE_CHOICES)

    objects = PassThroughManager.for_queryset_class(SoundCollectionQuerySet)()

    class Meta:
	verbose_name_plural = 'Sounds'

    def __unicode__(self):
	return self.title

    def save(self, *args, **kwargs):
	self.slug = slugify(self.title)
	super(SoundCollection, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
	return ('sound', [self.slug])


class Track(models.Model):
    sound_collection = models.ForeignKey(SoundCollection)
    title = models.CharField(max_length=30)
    track = models.FileField(upload_to="tracks")
    slug = models.SlugField(unique=True, editable=False)
    download_count = models.IntegerField(default=0, editable=False)

    def __unicode__(self):
	return self.title

    def save(self, *args, **kwargs):
	self.slug = slugify(self.title)
	super(Track, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
	return ('track', [self.sound_collection.slug, self.slug])
