from django.conf.urls import url, include
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from .views import ContactView, django_fields, CssView
from .my_auth_views import CreateUserView
from .editors_views import tinymceview


app_name = 'portfolio'
urlpatterns = [
    url(r'^contact/$', ContactView.as_view(), name="contact"),
    url(r'^thanks/$', TemplateView.as_view(template_name="portfolio/thanks.html"), name="thanks"),
    url(r'^css/([-\w]+)/$', CssView.as_view(), name="css"),
#    url(r'^my_style_home_page/$', TemplateView.as_view(template_name="portfolio/my_style_home_page.html"), name="my_style_homepage"),
    url(r'^forms/django-fields/([-\w]+)/$', django_fields, name="django_forms"),
    url(r'^forms/rich-text-editors/([-\w]+)/$', tinymceview, name="tinymce"),
    url(r'^home/$', TemplateView.as_view(template_name="portfolio/home_page.html"), name="home"),
    url(r'^django-auth/create_user/$', CreateUserView.as_view(), name="create_user"),
    url(r'^django-auth/user_created/$', TemplateView.as_view(template_name="portfolio/registration/user_created.html"), name="user_created"),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^$', RedirectView.as_view(pattern_name="portfolio:home", permanent=True)),
]
