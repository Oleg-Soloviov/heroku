from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic.edit import FormView
from portfolio.contact_form import ContactForm
from .forms import ChoiceDjangoFieldsForm, TextInputFieldsForm, TextBasedInputFieldsForm, DateTimeDjangoFieldsForm
from tinymce.widgets import TinyMCE



class ContactView(FormView):
    template_name = 'portfolio/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('portfolio:thanks')

    def form_valid(self, form):
        form.send_email()
        return super(ContactView, self).form_valid(form)

def django_fields(request, fields):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        if fields == "text-input":
            form = TextInputFieldsForm(request.POST)
            form.is_valid()
        elif fields == "html5-input-types":
            form = TextBasedInputFieldsForm(request.POST)
            form.is_valid()
        elif fields == "choice-fields":
            form = ChoiceDjangoFieldsForm(request.POST)
            form.is_valid()
        elif fields == "date-time-fields":
            form = DateTimeDjangoFieldsForm(request.POST)
            form.is_valid()

    # if a GET (or any other method) we'll create a blank form
    else:
        if fields == "text-input":
            form = TextInputFieldsForm()
        elif fields == "html5-input-types":
            form = TextBasedInputFieldsForm()
        elif fields == "choice-fields":
            form = ChoiceDjangoFieldsForm()
        elif fields == "date-time-fields":
            form = DateTimeDjangoFieldsForm()
    return render(request, 'portfolio/django_forms.html', {'form': form})
