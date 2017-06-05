from django.conf.urls import url
from django.views.generic import TemplateView
from .views import CreateUserView, UserEmailConfirm


app_name = 'my_auth'
urlpatterns = [
    url(r'^create_user/$', CreateUserView.as_view(), name="create_user"),
    url(r'^user_created/$', TemplateView.as_view(template_name="registration/user_created.html"), name="user_created"),
    url(r'^email_confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{40})/$', UserEmailConfirm.as_view(), name='email_confirm'),
    url(r'^email_confirm_done/$', TemplateView.as_view(template_name="registration/email_confirm_done.html"), name="email_confirm_done"),
]
