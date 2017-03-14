from django import forms
from django.utils.translation import ugettext_lazy as _
import requests


class ContactForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': _('Email..'),}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'placeholder': _('Subject..'),}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': _('Message...')}))
    
    def send_email(self):
        return requests.post(
            "https://api.mailgun.net/v3/sandbox075b55521f59465c82d4d87856d6f43c.mailgun.org/messages",
            auth=("api", "key-e1518fd3e6d897d250e23581f295417c"),
            data={"from": self.cleaned_data['email'] + " <postmaster@sandbox075b55521f59465c82d4d87856d6f43c.mailgun.org>",
                  "to": "Oleg <osoloviov@list.ru>",
                  "subject": self.cleaned_data['subject'],
                  "text": self.cleaned_data['message']})
