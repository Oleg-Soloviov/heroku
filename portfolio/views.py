from django.urls import reverse_lazy

from django.views.generic.edit import FormView
from portfolio.contact_form import ContactForm
from portfolio.forms import AllDjangoFieldsForm


class ContactView(FormView):
    template_name = 'portfolio/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('portfolio:thanks')

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super(ContactView, self).form_valid(form)


class AllDjangoFieldsView(FormView):
    template_name = 'portfolio/django_forms.html'
    form_class = AllDjangoFieldsForm
    success_url = reverse_lazy('portfolio:django_forms')
