import hashlib
import binascii

from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.template import loader
from django.contrib.auth import get_user_model
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode
from django.core.exceptions import ValidationError
from django.forms import Textarea

from .models import UserProfile

User = get_user_model()

class UserCreationFormWithEmail(UserCreationForm):
    """
    Subclass a Django UserCreationForm, add email field to frontend,
    verification of uniqness of the entered email and custom send_email.
    """
    class Meta(UserCreationForm.Meta):
        model = UserProfile
        fields = ("username", "email")
        
        widgets = {
            'address': Textarea(attrs={'cols': 36, 'rows': 5}),
        }
    
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
        
        subject = loader.render_to_string('registration/email_varify_subject.txt', context)
        # Email subject *must not* contain newlines
        subject = ''.join(subject.splitlines())
        body = loader.render_to_string('registration/email_verification_email.html', context)
        
        send_mail(
            subject,
            body,
            "<postmaster@sandbox075b55521f59465c82d4d87856d6f43c.mailgun.org>",
            [user.email])
