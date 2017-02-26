from django import forms
from django.core.mail import send_mail


class ContactForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email..',}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Subject..',}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Message...'}))

    def send_email(self):
        recipients = ['osoloviov@list.ru',]
        send_mail(self.cleaned_data['subject'],
                  self.cleaned_data['message'],
                  self.cleaned_data['email'],
                  recipients, fail_silently = False)
