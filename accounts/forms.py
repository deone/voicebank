from django import forms
from django.contrib.auth.models import User
from django.forms.util import ErrorList
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe
from django.utils.encoding import force_unicode
from django.shortcuts import get_object_or_404
from django.contrib.admin import widgets
from django.core.exceptions import ValidationError

from accounts.models import *

import random
import string
import re

url_id_re = re.compile(r'^[-.\w]+$')

def validate_url_id(value):
    if not url_id_re.search(value):
	raise ValidationError("Enter a valid 'url_id' consisting of letters, numbers, underscores, dots or hyphens.")

class UserJoinForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.Select)
    # birthday = forms.DateField(widget=widgets.AdminDateWidget())
    birthday = forms.DateField(('%d/%m/%Y',), 
	help_text='Enter your birthday in DD/MM/YYYY format')

    def save(self):
	username = self.cleaned_data['email']
	email = self.cleaned_data['email']
	password = self.cleaned_data['password']
	first_name = self.cleaned_data['first_name']
	last_name = self.cleaned_data['last_name']
	gender = self.cleaned_data['gender']
	birthday = self.cleaned_data['birthday']

	user = User.objects.create_user(username, email, password)
	user.first_name = first_name
	user.last_name = last_name
	user.save()

	email_id = user.email.split('@')[0]
	rand_alphanum = "".join(random.sample('%s%s' % (string.lowercase,
	    string.digits), 4))

	slug = '%s%s' % (email_id, rand_alphanum)

	profile = Profile.objects.create(user=user, slug=slug, gender=gender,
		birthday=birthday)

        return user

class UserProfileForm(forms.Form):
    user = forms.CharField(max_length=5)
    photo = forms.ImageField(required=False)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    about = forms.CharField(max_length=255, widget=forms.Textarea, required=False)
    phone_number = forms.CharField(max_length=15,
	    help_text="Enter phone number in full international format.\
	    Ignore\
	    the leading plus sign. e.g. 2348033344455, 23417745566")
    url_id = forms.CharField(max_length=50, help_text="Ain't it cool to have a\
	    custom URL like http://nigerianvoicebank.com/yournickname?",
	    validators=[validate_url_id])
    country = forms.ModelChoiceField(queryset=Country.objects.all(),
	    empty_label="Select...")
    state = forms.CharField(max_length=50)

    def save(self):
	user = get_object_or_404(User, pk=self.cleaned_data['user'])

	if self.cleaned_data['photo']:
	    user.profile.photo = self.cleaned_data['photo']
	user.first_name = self.cleaned_data['first_name']
	user.last_name = self.cleaned_data['last_name']
	user.save()

	user.profile.about = self.cleaned_data['about']
	user.profile.phone_number = self.cleaned_data['phone_number']
	user.profile.slug = self.cleaned_data['url_id']
	user.profile.country = self.cleaned_data['country']
	user.profile.state = self.cleaned_data['state']
	user.profile.save()
