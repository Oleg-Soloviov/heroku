import requests
from django.core.mail.backends.base import BaseEmailBackend

class MailgunEmailBackend(BaseEmailBackend):
    send(self, email_message):
        requests.post(
            "https://api.mailgun.net/v3/sandbox075b55521f59465c82d4d87856d6f43c.mailgun.org/messages",
            auth=("api", "key-e1518fd3e6d897d250e23581f295417c"),
            data={"from": "<postmaster@sandbox075b55521f59465c82d4d87856d6f43c.mailgun.org>",
                  "to": email_message.to,
                  "subject": email_message.subject,
                  "text": email_message.body})
        
