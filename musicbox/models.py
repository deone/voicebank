from django.db import models
from django.template.defaultfilters import slugify

from model_utils.managers import PassThroughManager


class AlbumQuerySet(models.query.QuerySet):
    def get_three_random_exclude(self, album_id):
	return self.exclude(pk=album_id).order_by('?')[:3]

class Album(models.Model):
    artiste = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    art = models.ImageField(upload_to="album_art")
    info = models.CharField(max_length=1000)
    slug = models.SlugField(unique=True, editable=False)

    objects = PassThroughManager.for_queryset_class(AlbumQuerySet)()

    def __unicode__(self):
	return self.title

    def save(self, *args, **kwargs):
	self.slug = slugify(self.title)
	super(Album, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
	return ('album', [self.slug])


class Track(models.Model):
    album = models.ForeignKey(Album)
    title = models.CharField(max_length=30)
    track = models.FileField(upload_to="tracks")

    def __unicode__(self):
	return self.title
