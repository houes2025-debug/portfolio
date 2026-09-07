from django.views.generic import TemplateView
from .models import Skill, Experience

class AboutView(TemplateView):
    template_name = 'about/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['skills'] = Skill.objects.all()
        context['experiences'] = Experience.objects.all()
        return context
