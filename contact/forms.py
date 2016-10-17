from django import forms

from contact.models import Contact

class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone_number = forms.CharField(label='Phone Number', max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))
    comment = forms.CharField(label='Message', max_length=255, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}))

    def save(self):
	contact = Contact.objects.create(name=self.cleaned_data['name'],
		email=self.cleaned_data['email'],
		phone_number=self.cleaned_data['phone_number'],
		comment=self.cleaned_data['comment'])

	return contact
