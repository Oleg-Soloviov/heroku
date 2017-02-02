from django.conf.urls import url
from django.views.generic import TemplateView

"""
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
"""

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="my_forms/home_page.html"), name="forms"),
]
