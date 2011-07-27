from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User)
    about = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    photo = models.ImageField(upload_to="profile_pics")
