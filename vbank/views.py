from django.shortcuts import render_to_response, get_list_or_404, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from vbank.forms import * 
from vbank.models import VoiceClip, Category

def clip_search(request, template='vbank/voiceclip_list.html', form=ClipSearchForm):
    voice_clips_list = VoiceClip.objects.active()
    paginator = Paginator(voice_clips_list, settings.VOICECLIP_LIST_PAGINATE_BY)

    page = request.GET.get('page')
    try:
        voice_clips = paginator.page(page)
    except PageNotAnInteger:
        voice_clips = paginator.page(1)
    except EmptyPage:
        voice_clips = paginator.page(paginator.num_pages)

    if request.method == 'POST':
        form = form(request.POST)
    else:
        form = form()

    return render_to_response(template, {
	'voiceclip_list': voice_clips,
        'form': form,
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
