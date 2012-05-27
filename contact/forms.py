from django import forms

from contact.models import Contact

class ContactForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=15)
    comment = forms.CharField(max_length=255, widget=forms.Textarea)

    def save(self):
	contact = Contact.objects.create(name=self.cleaned_data['name'],
		email=self.cleaned_data['email'],
		phone_number=self.cleaned_data['phone_number'],
		comment=self.cleaned_data['comment'])

	return contact
