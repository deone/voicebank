from django.views.generic import TemplateView

from core.models import Event


class AboutView(TemplateView):
    
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
	context = super(AboutView, self).get_context_data(**kwargs)
	context['events'] = Event.objects.later_than_now()
	return context

class HowView(TemplateView):

    template_name = 'how.html'

    def get_context_data(self, **kwargs):
	context = super(HowView, self).get_context_data(**kwargs)
	context['events'] = Event.objects.later_than_now()
	return context
