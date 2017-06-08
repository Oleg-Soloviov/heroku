from django import forms
from django.utils.translation import ugettext_lazy as _
#import requests
from django.core.mail import send_mail

class ContactForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': _('Email..'),}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'placeholder': _('Subject..'),}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': _('Message...')}))
    
    def send_email(self):
        send_mail(
            self.cleaned_data['subject'],
            self.cleaned_data['message'],
            self.cleaned_data['email'] + " <postmaster@sandbox075b55521f59465c82d4d87856d6f43c.mailgun.org>",
            ["osoloviov@list.ru"],)
