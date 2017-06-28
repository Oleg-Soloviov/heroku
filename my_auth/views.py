import hashlib
import binascii
import hmac

from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth import  login, get_user_model
from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse, Http404
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

from .forms import UserCreationFormWithEmail
from .models import UserProfile

User = get_user_model()


class ProfileView(UpdateView):
    
    success_url = reverse_lazy('my_auth:profile')
    template_name = 'registration/userprofile_form.html'
    
    def get_object(self, queryset=None):
        obj = UserProfile.objects.get(id=self.request.user.pk)
        return obj
    
    fields = ['username', 'first_name', 'last_name', 'email', 'address']

class CreateUserView(CreateView):
    template_name = 'registration/create_user.html'
    success_url = reverse_lazy('my_auth:user_created')
    form_class=UserCreationFormWithEmail

    def form_valid(self, form):
        self.object = form.save()
        self.object.is_active = False
        self.object.save()
        form.send_mail(self.request, self.object)
        self.request.session['username'] = self.object.username
        self.request.session['email'] = self.object.email
        return  HttpResponseRedirect(reverse_lazy('my_auth:user_created'))


class UserEmailConfirm(View):
    
    def dispatch(self, *args, **kwargs):
        if not 'uidb64' in kwargs and 'token' in kwargs:    # just in case
            raise Http404("Miss one of tokens.")

        try:
            uid = force_text(urlsafe_base64_decode(kwargs['uidb64']))
        except Exception as e:
            raise Http404(e)

        if not uid.isdigit():
            raise Http404("Uid is not digit.")
        
        user = get_object_or_404(User, pk=uid)

        if user.is_active:
            raise Http404("User is already active.")
        
        msg = force_bytes(user.email)
        salt = force_bytes(user.date_joined.ctime())
        true_token = hashlib.pbkdf2_hmac('sha256', msg, salt, 100000, dklen=20)
        
        try:
            receved_token = binascii.unhexlify(force_bytes(kwargs['token']))
        except Exception as e:
            raise Http404(e)

        if not hmac.compare_digest(true_token, receved_token):
            raise Http404("Tokens are not even.")
        else:
            user.is_active = True
            user.save()
            return  HttpResponseRedirect(reverse_lazy('my_auth:email_confirm_done'))
