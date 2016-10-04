from django import forms
from django.contrib.auth.models import User
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe
from django.utils.encoding import force_unicode
from django.shortcuts import get_object_or_404
from django.db import IntegrityError
from django.core.validators import validate_slug
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm, AuthenticationForm

from accounts.models import *

import random
import string

class ResetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(label='Confirm New Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class PasswordResetEmailForm(PasswordResetForm):
    email = forms.EmailField(label='Email Address', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))

class LoginForm(AuthenticationForm):
    username = forms.EmailField(label=_('Email'), max_length=254,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label=_('Password'),
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class UserJoinForm(forms.Form):
    first_name = forms.CharField(max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    gender = forms.ChoiceField(choices=GENDER_CHOICES,
	    widget=forms.Select(attrs={'class': 'form-control'}))
    birthday = forms.DateField(('%d/%m/%Y',), widget=forms.DateInput(attrs={'id': 'datepicker', 'class': 'form-control'}))

    def clean_email(self):
	if self.cleaned_data['email'] in [obj.email for obj in
		User.objects.all()]:
	    raise forms.ValidationError("Email belongs to another user.")
	
	return self.cleaned_data['email']

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
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    about = forms.CharField(max_length=255, widget=forms.Textarea(attrs={'class': 'form-control'}), required=False)
    skills = forms.CharField(max_length=100, help_text="Enter multiple skills as\
	    comma-separated values e.g. Broadcasting, Producing.",
	    required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    experience = forms.CharField(max_length=255, widget=forms.Textarea(attrs={'class': 'form-control'}), required=False)
    phone_number = forms.CharField(max_length=11,
	    help_text="e.g. 08033344455, 017745566", widget=forms.TextInput(attrs={'class': 'form-control'}))
    slug = forms.CharField(label="URL ID", max_length=50, help_text="Customize your URL e.g. http://nigerianvoicebank.com/yournickname",
	    validators=[validate_slug], widget=forms.TextInput(attrs={'class': 'form-control'}))
    location = forms.CharField(max_length=50, help_text="e.g. Lagos, Abuja, Port-Harcourt", widget=forms.TextInput(attrs={'class': 'form-control'}))

    def clean_slug(self):
	data = self.cleaned_data['slug']

	try:
	    profile = Profile.objects.get(slug=data)
	except:
	    pass
	else:
	    if profile.slug != data:
		raise forms.ValidationError("""This URL ID is taken. Please choose
		    another.""")

	return data

    def save(self):
	user = get_object_or_404(User, pk=self.cleaned_data['user'])

	if self.cleaned_data['photo']:
	    user.profile.photo = self.cleaned_data['photo']
	user.first_name = self.cleaned_data['first_name']
	user.last_name = self.cleaned_data['last_name']
	user.save()

	user.profile.about = self.cleaned_data['about']
	user.profile.phone_number = self.cleaned_data['phone_number']
	user.profile.slug = self.cleaned_data['slug']
	user.profile.location = self.cleaned_data['location']
	user.profile.skills = self.cleaned_data['skills']
	user.profile.experience = self.cleaned_data['experience']
	user.profile.save()

	return user.profile
