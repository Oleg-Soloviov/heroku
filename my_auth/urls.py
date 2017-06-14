from django.conf.urls import url
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from .views import CreateUserView, UserEmailConfirm


app_name = 'my_auth'
urlpatterns = [
    url(r'^profile/$', login_required(TemplateView.as_view(
        template_name="registration/profile.html")),
        name="profile"),
    url(r'^create_user/$', CreateUserView.as_view(),
        name="create_user"),
    url(r'^user_created/$', TemplateView.as_view(
        template_name="registration/user_created.html"),
        name="user_created"),
    url(r'^email_confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{40})/$',
        UserEmailConfirm.as_view(),
        name='email_confirm'),
    url(r'^email_confirm_done/$', TemplateView.as_view(
        template_name="registration/email_confirm_done.html"),
        name="email_confirm_done"),
    url('^change-password/$', login_required(auth_views.PasswordChangeView.as_view(
        template_name='registration/change_password.html',
        success_url=reverse_lazy('my_auth:my_password_change_done'))),
        name="my_password_change"),
    url('^change-password-done/$', login_required(auth_views.PasswordChangeDoneView.as_view(
        template_name='registration/my_change_password_done.html')),
        name="my_password_change_done"),
    url('^reset_password/$', auth_views.PasswordResetView.as_view(
        template_name='registration/my_password_reset_form.html',
        email_template_name = 'registration/my_password_reset_email.html',
        success_url=reverse_lazy('my_auth:my_password_reset_done')),
        name="my_password_reset"),
    url('^reset_password/done/$', auth_views.PasswordResetDoneView.as_view(
        template_name='registration/my_password_reset_done.html'),
        name="my_password_reset_done"),
    url('^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(
        template_name='registration/my_password_reset_confirm.html',
        success_url=reverse_lazy('my_auth:my_password_reset_complete')),
        name="my_password_reset_confirm"),
    url('^reset/done/$',
        auth_views.PasswordResetCompleteView.as_view(
        template_name='registration/my_password_reset_complete.html',),
        name="my_password_reset_complete"),
]
