from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.CharField(max_length=11)
    comment = models.CharField(max_length=255)

    def __unicode__(self):
	return u'%s : %s' % (self.name, self.comment)
