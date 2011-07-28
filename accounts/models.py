from django.db import models
from django.contrib.auth.models import User

import random
import string
import datetime

class Profile(models.Model):
    user = models.OneToOneField(User)
    slug = models.SlugField(unique=True, editable=False)
    about = models.CharField(max_length=255)
    date_of_birth = models.DateField(default=datetime.datetime.now())
    photo = models.ImageField(upload_to="profile_pics")

    def save(self, *args, **kwargs):
	email_id = self.user.email.split('@')[0]
	rand_alpha = "".join(random.sample('%s%s' % (string.lowercase,
	    string.digits), 4))

	self.slug = '%s%s' % (email_id, rand_alpha)
	super(Profile, self).save()

def create_profile(sender, **kwargs):
    created = kwargs['created']

    if created:
	Profile.objects.create(user=kwargs['instance'])

models.signals.post_save.connect(create_profile, sender=User)
