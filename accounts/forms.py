from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserJoinForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email_address = forms.CharField(max_length=30)

    def save(self, request):
	user = super(UserJoinForm, self).save(commit=True)
	user.first_name = request.POST['first_name']
	user.last_name = request.POST['last_name']
	user.email = request.POST['email_address']
	user.save()
