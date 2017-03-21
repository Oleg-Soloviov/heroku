from django.conf.urls import url
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from .views import ContactView, django_fields


app_name = 'portfolio'
urlpatterns = [
    url(r'^contact/$', ContactView.as_view(), name="contact"),
    url(r'^thanks/$', TemplateView.as_view(template_name="portfolio/thanks.html"), name="thanks"),
    url(r'^css3/$', TemplateView.as_view(template_name="portfolio/css3.html"), name="css3"),
    url(r'^my_style_home_page/$', TemplateView.as_view(template_name="portfolio/my_style_home_page.html"), name="my_style_homepage"),
    url(r'^django-forms/([-\w]+)/$', django_fields, name="django_forms"),
    url(r'^home/$', TemplateView.as_view(template_name="portfolio/home_page.html"), name="home"),
    url(r'^$', RedirectView.as_view(pattern_name="portfolio:home", permanent=True)),
]
