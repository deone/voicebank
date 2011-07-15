from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserJoinForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email_address = forms.CharField(max_length=30)
