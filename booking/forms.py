from django import forms
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from booking.models import Booking

class BookingForm(forms.Form):
    user = forms.CharField(max_length=5)
    name_on_teller = forms.CharField(max_length=30)
    date_of_payment = forms.DateField(('%d/%m/%Y',), help_text="Enter date in DD/MM/YYYY format")
    bank_name = forms.CharField(max_length=30)

    def save(self):
	user = get_object_or_404(User, pk=self.cleaned_data['user'])
	booking = Booking.objects.create(user=user, 
		name_on_teller=self.cleaned_data['name_on_teller'],
		date_of_payment=self.cleaned_data['date_of_payment'],
		bank_name=self.cleaned_data['bank_name'])

	return booking
