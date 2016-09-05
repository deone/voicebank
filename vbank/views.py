from django.shortcuts import render_to_response, get_list_or_404, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from vbank.forms import * 
from vbank.models import VoiceClip, Category

import datetime

AGE_GROUPS = {
    'K': 'Kids',
    'A': 'Adults'
    }

GENDER_STRING = {
    'M': 'Men',
    'F': 'Women'
    }

def clip_search(request, template='vbank/voiceclip_list.html', form=ClipSearchForm):
    voice_clips_list = VoiceClip.objects.active()

    language_string = 'All'
    category_string = 'all categories'
    gender_string = 'both genders in'
    age_group_string = 'all age groups'

    if request.method == 'POST':
        form = form(request.POST)

        if request.POST['language']:
            language = request.POST['language']
            voice_clips_list = voice_clips_list.filter(language=request.POST['language'])
            language_string = language

        if request.POST['category']:
            category = request.POST['category']
            voice_clips_list = voice_clips_list.filter(category__pk=category)
            category_string = 'the ' + Category.objects.get(pk=category).name + ' Category'

        if request.POST['gender']:
            gender = request.POST['gender']
            voice_clips_list = voice_clips_list.filter(user__profile__gender=gender)
            gender_string = dict(GENDER_STRING)[gender] + ' in'

        if request.POST['age_group']:
            today = datetime.date.today()
            age_group = request.POST['age_group']
            age_group_string = 'the ' + AGE_GROUPS[age_group] + ' age group'

            clips_list = []
            if age_group == 'K':
                for clip in voice_clips_list:
                    if clip.user.profile.birthday.year > (today.year - 15):
                        clips_list.append(clip)
            elif age_group == 'A':
                for clip in voice_clips_list:
                    if clip.user.profile.birthday.year < (today.year - 15):
                        clips_list.append(clip)

            voice_clips_list = clips_list
    else:
        form = form(initial=request.GET)

        try:
            language_string = request.GET['language']
        except:
            pass

        try:
            category_string = 'the ' + Category.objects.get(pk=request.GET['category']).name + ' Category'
        except:
            pass

        try:
            gender_string = dict(GENDER_STRING)[request.GET['gender']] + ' in'
        except:
            pass

        try:
            age_group_string = 'the ' + AGE_GROUPS[request.GET['age_group']] + ' age group'
        except:
            pass

        # page_header = 'All Voice Clips'

    # Page Header
    page_header = '%s voice clips by %s %s in %s' % (language_string, gender_string, age_group_string, category_string)

    paginator = Paginator(voice_clips_list, settings.VOICECLIP_LIST_PAGINATE_BY)

    page = request.GET.get('page')
    try:
        voice_clips = paginator.page(page)
    except PageNotAnInteger:
        voice_clips = paginator.page(1)
    except EmptyPage:
        voice_clips = paginator.page(paginator.num_pages)

    return render_to_response(template, {
	'voiceclip_list': voice_clips,
        'form': form,
        'page_header': page_header
        }, context_instance=RequestContext(request))

@login_required
def voiceclips(request, template='vbank/voiceclips.html', form=VoiceClipForm):
    if request.method == "POST":
	form = form(request.POST, request.FILES)
	if form.is_valid():
	    form.save()
	    messages.success(request, "Audio clip uploaded successfully.")
    else:
	form = form(initial={'user': request.user.id})

    try:
	# Use model_utils here.
	voice_clips = get_list_or_404(VoiceClip, user=request.user,
		is_active=True)
    except Http404:
	voice_clips = None
    
    return render_to_response(template, {
	    'form': form,
	    'voiceclip_list': voice_clips
	}, context_instance=RequestContext(request))

def category_detail(request, slug, template='vbank/category_detail.html'):
    category = get_object_or_404(Category, slug=slug)

    if category.name != 'Customer Care':
	return render_to_response(template, {
	    'category': category,
	}, context_instance=RequestContext(request))
    else:
	english_clips = VoiceClip.objects.filter(category=category).filter(language='English')
	yoruba_clips = VoiceClip.objects.filter(category=category).filter(language='Yoruba')
	igbo_clips = VoiceClip.objects.filter(category=category).filter(language='Igbo')
	hausa_clips = VoiceClip.objects.filter(category=category).filter(language='Hausa')
	pidgin_english_clips= VoiceClip.objects.filter(category=category).filter(language='Pidgin English')

	return render_to_response(template, {
	    'category': category,
	    'english_clips': english_clips,
	    'yoruba_clips': yoruba_clips,
	    'igbo_clips': igbo_clips,
	    'hausa_clips': hausa_clips,
	    'pidgin_english_clips': pidgin_english_clips
	}, context_instance=RequestContext(request)) 
