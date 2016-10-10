from django.shortcuts import redirect, render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.views.generic import DetailView
from django.contrib.sites.models import Site

from accounts import calculate_age
from accounts.models import Profile
from accounts.forms import UserJoinForm, UserProfileForm
from vbank.models import VoiceClip, Category
from articles.models import Article

# This should be CategoryListView
def index(request, template='accounts/index.html'):
    recent_voice_clips = VoiceClip.objects.active()[:settings.RECENT_VOICE_CLIPS_DISPLAY_LIMIT]
    top_voice_clips = VoiceClip.objects.top()[:settings.TOP_VOICE_CLIPS_DISPLAY_LIMIT]
    categories = Category.objects.all()

    featured_articles = Article.objects.filter(featured=True)

    news = Article.objects.filter(article_type='News').order_by('?')[:settings.ARTICLE_LIST_LIMIT]
    voice_tips = Article.objects.filter(article_type='Voice Tips').order_by('?')[:settings.ARTICLE_LIST_LIMIT]
    radio_connect = Article.objects.filter(article_type='Radio Connect').order_by('?')[:settings.ARTICLE_LIST_LIMIT]
    others = Article.objects.filter(article_type='Others').order_by('?')[:settings.ARTICLE_LIST_LIMIT]

    return render_to_response(template, {
	'voiceclip_list': recent_voice_clips,
	'top_clips': top_voice_clips,
	'categories': categories,
        'featured_articles': featured_articles,
	'news': news,
	'voice_tips': voice_tips,
	'radio_connect': radio_connect,
	'others': others,
	}, context_instance=RequestContext(request))

@login_required
def profile_edit(request, template='accounts/profile_edit.html', form=UserProfileForm):
    if request.method == "POST":
	form = form(request.POST, request.FILES)
	if form.is_valid():
	    form.save()
	    messages.success(request, "Profile updated successfully.")
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
	    'site': Site.objects.get_current().domain,
	    'age': calculate_age(request.user.profile.birthday),
	    'profile': request.user.get_profile(),
	}, context_instance=RequestContext(request))


class ProfileDetailView(DetailView):

    model = Profile

    def get_context_data(self, **kwargs):
	obj = super(ProfileDetailView, self).get_object()
	context = super(ProfileDetailView, self).get_context_data(**kwargs)
	context['age'] = calculate_age(obj.birthday)
	context['site'] = Site.objects.get_current().domain
        context['user_clips'] = obj.user.voiceclip_set.filter(is_active=True)
	return context

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
	    context_vars['login_url'] = "%s%s" % (Site.objects.get_current().domain,
		    settings.LOGIN_URL)

	    ###########################

	    html_content = render_to_string("accounts/welcome_mail.html", context_vars)
	    text_content = strip_tags(html_content)

	    msg = EmailMultiAlternatives(settings.WELCOME_MSG_SUBJECT,
		    text_content, settings.DEFAULT_FROM_EMAIL, recipients)

	    msg.attach_alternative(html_content, "text/html")

	    msg.send()

	    ##########################

	    return redirect(settings.LOGIN_REDIRECT_URL)
    else:
	form = form()

    return render_to_response(template, {
	'form': form,
	},
	    context_instance=RequestContext(request))

def logout(request):
    auth.logout(request)
    return redirect('accounts.views.index')
