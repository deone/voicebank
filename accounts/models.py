from django.db import models
from django.contrib.auth.models import User

GENDER_CHOICES = (
	("", "Select Gender"),
	("M", "Male"),
	("F", "Female"),
)

class Profile(models.Model):
    user = models.OneToOneField(User)
    slug = models.SlugField(unique=True, editable=False)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    about = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=11, null=True)
    location = models.CharField(max_length=50)
    birthday = models.DateField()
    photo = models.ImageField(upload_to="profile_pics")
    skills = models.CharField(max_length=100)
    experience = models.CharField(max_length=255)

    def __unicode__(self):
	return self.user.email

    @models.permalink
    def get_absolute_url(self):
	return ('accounts.views.profile', [self.slug])
