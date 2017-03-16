from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic.edit import FormView
from portfolio.contact_form import ContactForm
from .forms import AllDjangoFieldsForm, TextInputFieldsForm, TextBasedInputFieldsForm


class ContactView(FormView):
    template_name = 'portfolio/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('portfolio:thanks')

    def form_valid(self, form):
        form.send_email()
        return super(ContactView, self).form_valid(form)


class AllDjangoFieldsView(FormView):
    template_name = 'portfolio/django_forms.html'
    form_class = AllDjangoFieldsForm
    success_url = reverse_lazy('portfolio:django_forms')





def django_fields(request, fields):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        if fields == "text_input":
            form = TextInputFieldsForm(request.POST)
            form.is_valid()
        elif fields == "text_base_input":
            form = TextBasedInputFieldsForm(request.POST)
            form.is_valid()

    # if a GET (or any other method) we'll create a blank form
    else:
        if fields == "text_input":
            form = TextInputFieldsForm()
        elif fields == "text_base_input":
            form = TextBasedInputFieldsForm()

    return render(request, 'portfolio/django_forms.html', {'form': form})
