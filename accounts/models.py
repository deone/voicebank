from django.db import models
from django.contrib.auth.models import User

GENDER_CHOICES = (
	("M", "Male"),
	("F", "Female"),
)

class Profile(models.Model):
    user = models.OneToOneField(User)
    slug = models.SlugField(unique=True, editable=False)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    location = models.CharField(max_length=30)
    about = models.CharField(max_length=255)
    birthday = models.DateField()
    photo = models.ImageField(upload_to="profile_pics")

    def __unicode__(self):
	return self.slug

    @models.permalink
    def get_absolute_url(self):
	return ('user_profile', [self.slug])


class Interest(models.Model):
    interest = models.CharField(max_length=50)

    def __unicode__(self):
	return self.interest


class MediaInterest(models.Model):
    profile = models.ForeignKey(Profile)
    interest = models.ForeignKey(Interest)
