from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django import forms
from django.views.generic import TemplateView
from django.views.generic.edit import FormView, CreateView
from django.contrib.auth.forms import UserCreationForm


#~ class CreateUserView(FormView):
    #~ template_name = 'portfolio/auth/create_user.html'
    #~ form_class = UserCreationForm
    #~ success_url = reverse_lazy('portfolio:user_created')
    #~ def form_valid(self, form):
        #~ form.save()
        #~ return super(CreateUserView, self).form_valid(form)

class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(help_text=_("Enter a valid email"))
            
    def save(self, commit=True):
        user = super(UserCreationFormWithEmail, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        return super(UserCreationFormWithEmail, self).save()

class CreateUserView(CreateView):
    template_name = 'portfolio/registration/create_user.html'
    success_url = reverse_lazy('portfolio:user_created')
    form_class=UserCreationFormWithEmail
    def get_form(self):
        form = super(CreateUserView, self).get_form()
        for f in form.fields.keys():
            form.fields[f].widget.attrs.update({'autofocus': False, 'autocomplete': 'off', 'class':'form-control'})
            if form.has_error(f):
                form.fields[f].widget.attrs.update({'style':'background-color:maroon;color:black;', 'class':'form-control error-item'})
        return form
