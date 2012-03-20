from django.shortcuts import redirect, render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.sites.models import Site
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib import messages

from accounts.models import Profile
from accounts.forms import UserJoinForm, UserProfileForm
from core.models import VoiceClip, Category, Event

import datetime

CURRENT_SITE = Site.objects.get_current()

events_context_var = [event for event in Event.objects.all() if datetime.datetime.now() < event.date][:settings.EVENTS_DISPLAY_LIMIT]

def index(request, template='accounts/index.html'):
    recent_voice_clips = VoiceClip.objects.filter(is_active=True)[:settings.RECENT_VOICE_CLIPS_DISPLAY_LIMIT]
    top_voice_clips = VoiceClip.objects.filter(is_top=True)
    .order_by('-is_top_timestamp')[settings.TOP_VOICE_CLIPS_DISPLAY_LIMIT]
    categories = Category.objects.all()

    return render_to_response(template, {
	'recent_clips': recent_voice_clips,
	'top_clips': top_voice_clips,
	'categories': categories,
	'events': events_context_var,
	}, context_instance=RequestContext(request))

@login_required
def profile_edit(request, template='accounts/profile_edit.html', form=UserProfileForm):
    if request.method == "POST":
	form = form(request.POST, request.FILES)
	if form.is_valid():
	    form.save()
    else:
	form = form(initial={
	    'user': request.user.id, 
	    'first_name': request.user.first_name,
	    'last_name': request.user.last_name,
	    'about': request.user.profile.about,
	    'skills': request.user.profile.skills,
	    'experience': request.user.profile.experience,
	    'phone_number': request.user.profile.phone_number,
	    'location': request.user.profile.location,
	    'slug': request.user.profile.slug
	    })

    return render_to_response(template, {
	    'form': form,
	    'site': CURRENT_SITE.name,
	    'events': events_context_var,
	    'age': calculate_age(request.user.profile.birthday),
	}, context_instance=RequestContext(request))

def calculate_age(born):
    today = datetime.date.today()
    try:
	birthday = born.replace(year=today.year)
    except ValueError:
	birthday = born.replace(year=today.year, day=born.day-1)

    return today.year - born.year

def profile(request, slug, template='accounts/profile.html'):
    user_profile = get_object_or_404(Profile, slug__iexact=slug)

    return render_to_response(template, {
	    'user_profile': user_profile,
	    'age': calculate_age(user_profile.birthday),
	    'site': CURRENT_SITE.name,
	    'events': events_context_var,
	}, context_instance=RequestContext(request))

def join(request, template='accounts/join.html', form=UserJoinForm):
    if request.method == "POST":
	form = form(request.POST)
	if form.is_valid():
	    form.save()

	    # Authenticate and log user in.
	    email = request.POST['email']
	    password = request.POST['password']

	    user = auth.authenticate(username=email, password=password)

	    if user is not None:
		if user.is_active:
		    auth.login(request, user)
		else:
		    # Do something if we ever need to.
		    pass

	    recipients = []
	    recipients.append(email)

	    context_vars = {}
	    context_vars['login_url'] = "%s%s" % (CURRENT_SITE.name,
		    settings.LOGIN_URL)

	    ###########################

	    html_content = render_to_string("accounts/welcome_mail.html", context_vars)
	    text_content = strip_tags(html_content)

	    msg = EmailMultiAlternatives(settings.WELCOME_MSG_SUBJECT,
		    text_content, settings.EMAIL_SENDER, recipients)

	    msg.attach_alternative(html_content, "text/html")

	    msg.send()

	    ##########################

	    return redirect(settings.LOGIN_REDIRECT_URL)
    else:
	form = form()

    return render_to_response(template, {
	'form': form,
	'events': events_context_var,
	},
	    context_instance=RequestContext(request))

def logout(request):
    auth.logout(request)
    return redirect('accounts.views.index')
