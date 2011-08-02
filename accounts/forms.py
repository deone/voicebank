from django import forms
from django.contrib.auth.models import User

from accounts.models import Profile, GENDER_CHOICES

import random
import string

class UserJoinForm(forms.Form):
    username = forms.EmailField(label='Email')
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.Select)
    birthday = forms.DateField(('%d/%m/%Y',),
	    widget=forms.DateInput(format='%d/%m/%Y'),
	    help_text='Enter your birthday in DD/MM/YYYY format'
	    )

    def save(self):
	username = self.cleaned_data['username']
	password = self.cleaned_data['password']
	first_name = self.cleaned_data['first_name']
	last_name = self.cleaned_data['last_name']
	gender = self.cleaned_data['gender']
	birthday = self.cleaned_data['birthday']

	user = User.objects.create(username=username, password=password,
		first_name=first_name, last_name=last_name, email=username)

	email_id = user.email.split('@')[0]
	rand_alphanum = "".join(random.sample('%s%s' % (string.lowercase,
	    string.digits), 4))

	slug = '%s%s' % (email_id, rand_alphanum)

	profile = Profile.objects.create(user=user, slug=slug, gender=gender,
		birthday=birthday)

        return user


class UserProfileForm(forms.Form):
    user = forms.CharField(max_length=5)
    photo = forms.ImageField()
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    birthday = forms.DateField()
    about = forms.CharField(max_length=255, widget=forms.Textarea)
