from django import forms
from django.utils.translation import ugettext_lazy as _
import requests


class ContactForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': _('Email..'),}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'placeholder': _('Subject..'),}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': _('Message...')}))
    
    error_css_class = 'error'
    
    def send_email(self):
        return requests.post(
            "https://api.mailgun.net/v3/sandbox075b55521f59465c82d4d87856d6f43c.mailgun.org/messages",
            auth=("api", "key-e1518fd3e6d897d250e23581f295417c"),
            data={"from": self.cleaned_data['email'] + " <postmaster@sandbox075b55521f59465c82d4d87856d6f43c.mailgun.org>",
                  "to": "Oleg <osoloviov@list.ru>",
                  "subject": self.cleaned_data['subject'],
                  "text": self.cleaned_data['message']})



#~ HTML5 input types and browser validation
#~ 
#~ If your form includes a URLField, an EmailField or any integer field type, Django will use the url, email and number HTML5 input types. By default, browsers may apply their own validation on these fields, which may be stricter than Django’s validation. If you would like to disable this behavior, set the novalidate attribute on the form tag, or specify a different widget on the field, like TextInput.
