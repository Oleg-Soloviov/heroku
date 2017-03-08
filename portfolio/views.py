from django.shortcuts import render
from django.urls import reverse

from portfolio.contact_form import ContactForm
from portfolio.forms import AllDjangoFieldsForm
from django.views.generic.edit import FormView

class ContactView(FormView):
    template_name = 'portfolio/contact.html'
    form_class = ContactForm
    success_url = reverse("portfolio:thanks")

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super(ContactView, self).form_valid(form)


class AllDjangoFieldsView(FormView):
    template_name = 'portfolio/django_forms.html'
    form_class = AllDjangoFieldsForm
    success_url = reverse('portfolio:django_forms')
