from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'index.html'

class AboutUsPageView(TemplateView):
    template_name = 'about.html'

class NotFondPageView(TemplateView):
    template_name = '404.html'

class ContactPageView(TemplateView):
    template_name = 'contact.html'

class ConsentPageView(TemplateView):
    template_name = 'faq.html'

class Home2PageView(TemplateView):
    template_name = 'index-2.html'

class NewsSinglePageView(TemplateView):
    template_name = 'news-single.html'

class CatalogPageView(TemplateView):
    template_name = 'pricing.html'

class ProjectsPageView(TemplateView):
    template_name = 'projects.html'

class ProjectsSinglePageView(TemplateView):
    template_name = 'projects-single.html'

class ServicesPageView(TemplateView):
    template_name = 'services.html'

class ServicesSinglePageView(TemplateView):
    template_name = 'service-single.html'

class TeamPageView(TemplateView):
    template_name = 'team.html'

class CertificatesPageView(TemplateView):
    template_name = 'testimonials.html'

class MoviesGalleryPageView(TemplateView):
    template_name = 'typography.html'
