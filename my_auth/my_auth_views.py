import requests
import hashlib
import binascii
import hmac

from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django import forms
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, get_user_model
from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse, Http404
from django.core.exceptions import ValidationError
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMultiAlternatives
from django.template import loader
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.shortcuts import get_object_or_404


User = get_user_model()

class UserCreationFormWithEmail(UserCreationForm):
    """
    Subclass a Django UserCreationForm, add email field to frontend,
    verification of uniqness of the entered email and custom send_email.
    """
    class Meta(UserCreationForm.Meta):
        fields = ("username", "email")
    
    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise ValidationError(
                                _('Email %(value)s already exists.'),
                                code='email_exists',
                                params={'value': data},
                            )
        return data
    
    def send_mail(self, request, user):
        """
        Sends a letter `to_email` using my mailgun sandbox.
        """
        current_site = get_current_site(request)
        site_name = current_site.name
        domain = current_site.domain
        
        msg = force_bytes(user.email)
        salt = force_bytes(user.date_joined.ctime())
        
        my_token = hashlib.pbkdf2_hmac('sha256', msg, salt, 100000, dklen=20) # sha256 for Python3.4+
        my_token = binascii.hexlify(my_token)
        my_token = force_text(my_token)
        
        uid = force_text(urlsafe_base64_encode(force_bytes(user.pk)))
        
        context = {
            'email': user.email,
            'domain': domain,
            'site_name': site_name,
            'uid': uid,
            'user': user,
            'token': my_token,
            'protocol': 'http',
        }
        
        subject = loader.render_to_string('portfolio/registration/email_varify_subject.txt', context)
        # Email subject *must not* contain newlines
        subject = ''.join(subject.splitlines())
        body = loader.render_to_string('portfolio/registration/email_verification_email.html', context)
        requests.post(
            "https://api.mailgun.net/v3/sandbox075b55521f59465c82d4d87856d6f43c.mailgun.org/messages",
            auth=("api", "key-e1518fd3e6d897d250e23581f295417c"),
            data={"from": "<postmaster@sandbox075b55521f59465c82d4d87856d6f43c.mailgun.org>",
                  "to": user.email,
                  "subject": subject,
                  "text": body})
    



class CreateUserView(CreateView):
    template_name = 'portfolio/registration/create_user.html'
    success_url = reverse_lazy('portfolio:user_created')
    form_class=UserCreationFormWithEmail
    
    def get_form(self):
        form = super(CreateUserView, self).get_form()
        for f in form.fields.keys():
            form.fields[f].widget.attrs.update({'autofocus': False, 'autocomplete': 'off', 'class':'form-control'})
            if form.has_error(f):
                form.fields[f].widget.attrs.update({'style':'background-color:maroon;color:black;', 'class':'form-control error-item'})
        return form
    
    def form_valid(self, form):
        self.object = form.save()
        self.object.is_active = False
        self.object.save()
        form.send_mail(self.request, self.object)
        self.request.session['username'] = self.object.username
        self.request.session['email'] = self.object.email
        return  HttpResponseRedirect(reverse_lazy('portfolio:user_created'))


class UserEmailConfirm(View):
    
    def dispatch(self, *args, **kwargs):
        if not 'uidb64' in kwargs and 'token' in kwargs:    # just in case
            raise Http404("Miss one of tokens.")

        try:
            uid = force_text(urlsafe_base64_decode(kwargs['uidb64']))
        except Exception as e:
            raise Http404(e)

        if not uid.isdigit():
            raise Http404("Uid is not digit.")
        
        user = get_object_or_404(User, pk=uid)

        if user.is_active:
            raise Http404("User is already active.")
        
        msg = force_bytes(user.email)
        salt = force_bytes(user.date_joined.ctime())
        true_token = hashlib.pbkdf2_hmac('sha256', msg, salt, 100000, dklen=20)
        
        try:
            receved_token = binascii.unhexlify(force_bytes(kwargs['token']))
        except Exception as e:
            raise Http404(e)

        if not hmac.compare_digest(true_token, receved_token):
            raise Http404("Tokens are not even.")
        else:
            user.is_active = True
            user.save()
            return  HttpResponseRedirect(reverse_lazy('portfolio:email_confirm_done'))
