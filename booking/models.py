from django.db import models

class Booking(models.Model):
    user = models.ForeignKey('auth.User')
    name_on_teller = models.CharField(max_length=30)
    date_of_payment = models.DateField()
    bank_name = models.CharField(max_length=30)

    def __unicode__(self):
	return self.name_on_teller
