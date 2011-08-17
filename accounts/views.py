from django.shortcuts import redirect, render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.sites.models import Site
from django.conf import settings
from core.models import VoiceClip

from accounts.models import Profile
from accounts.forms import UserJoinForm, UserProfileForm

CURRENT_SITE = Site.objects.get_current()

def index(request, template='accounts/index.html'):
    voice_clips = VoiceClip.objects.filter(is_active=True).order_by('-date_added')

    return render_to_response(template, {
	'clips': voice_clips
	}, context_instance=RequestContext(request))

@login_required
def profile_edit(request, id, template='accounts/profile_edit.html', form=UserProfileForm):
    if request.method == "POST":
	form = form(request.POST, request.FILES)
	if form.is_valid():
	    form.save()

	return redirect(request.user.profile.get_absolute_url())

    else:
	form = form(initial={
	    'user': request.user.id, 
	    'first_name': request.user.first_name,
	    'last_name': request.user.last_name,
	    'about': request.user.profile.about,
	    'country': request.user.profile.country,
	    'state': request.user.profile.state,
	    'url_id': request.user.profile.slug
	    })

    return render_to_response(template, {
	    'form': form,
	    'site': CURRENT_SITE.name,
	}, context_instance=RequestContext(request))

def profile(request, slug, template='accounts/profile.html'):
    user_profile = get_object_or_404(Profile, slug__iexact=slug)

    return render_to_response(template, {
	    'user_profile': user_profile,
	    'site': CURRENT_SITE.name,
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
	    
	    return redirect('core.views.index')
    else:
	form = form()

    return render_to_response(template, {'form': form},
	    context_instance=RequestContext(request))

def logout(request):
    auth.logout(request)
    return redirect('accounts.views.index')
