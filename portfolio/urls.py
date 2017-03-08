from django.conf.urls import url
from django.views.generic import TemplateView
from portfolio.views import ContactView, AllDjangoFieldsView

"""
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
"""

app_name = "portfolio"

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="portfolio/home_page.html"), name="home"),
    url(r'^contact/$', ContactView.as_view(), name="contact"),
    url(r'^thanks/$', TemplateView.as_view(template_name="portfolio/thanks.html"), name="thanks"),
    url(r'^django-forms/$', AllDjangoFieldsView.as_view(), name="django_forms")
]
