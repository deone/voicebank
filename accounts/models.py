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
    about = models.CharField(max_length=255)
    birthday = models.DateField()
    photo = models.ImageField(upload_to="profile_pics")

    def __unicode__(self):
	return self.user.username
