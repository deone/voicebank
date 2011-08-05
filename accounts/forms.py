from django import forms
from django.contrib.auth.models import User
from django.forms.util import ErrorList
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe
from django.utils.encoding import force_unicode
from django.shortcuts import get_object_or_404

from accounts.models import Profile, GENDER_CHOICES
from accounts.models import Interest

import random
import string

class UserJoinForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.Select)
    birthday = forms.DateField(('%d/%m/%Y',),
	    help_text='Enter your birthday in DD/MM/YYYY format'
	    )

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
    location = forms.CharField(max_length=30)
    about = forms.CharField(max_length=255, widget=forms.Textarea, required=False)
    media_interests = forms.ModelMultipleChoiceField(queryset=Interest.objects.all())

    def save(self):
	user = get_object_or_404(User, pk=self.cleaned_data['user'])
	user.first_name = self.cleaned_data['first_name']
	user.last_name = self.cleaned_data['last_name']

	profile = user.get_profile()
	profile.about = self.cleaned_data['about']
	profile.photo = self.cleaned_data['photo']

	user.save()
	profile.save()


class SpanErrorList(ErrorList):
    def __unicode__(self):
	return self.as_spans()

    def as_spans(self):
	if not self:
	    return u''
	return mark_safe(u'%s' % ''.join([u"<span class='help'>%s</span>" %
	    conditional_escape(force_unicode(e)) for e in self]))
