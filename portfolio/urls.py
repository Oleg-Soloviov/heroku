from django.conf.urls import url
from django.views.generic import TemplateView
from .views import ContactView, AllDjangoFieldsView, django_fields


app_name = 'portfolio'
urlpatterns = [
    url(r'^contact/$', ContactView.as_view(), name="contact"),
    url(r'^thanks/$', TemplateView.as_view(template_name="portfolio/thanks.html"), name="thanks"),
    url(r'^my_style_home_page/$', TemplateView.as_view(template_name="portfolio/my_style_home_page.html"), name="my_style_homepage"),
    #url(r'^django-forms/$', AllDjangoFieldsView.as_view(), name="django_forms"),
    url(r'^django-forms/$', django_fields, name="django_forms"),
    url(r'^$', TemplateView.as_view(template_name="portfolio/home_page.html"), name="home"),
]
