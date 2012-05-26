from django.db import models
from django.conf import settings

from datetime import datetime

from model_utils.managers import PassThroughManager

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
