from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django.contrib.auth import authenticate

from . import forms


class LoginView(generic.FormView):
    form_class = AuthenticationForm
    success_url = reverse_lazy("g2:home")
    template_name = "accounts/login.html"
    
    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        return form_class(self.request, **self.get_form_kwargs())
    
    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)


class LogoutView(generic.RedirectView):
    url = reverse_lazy("home")
    
    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)


class SignUp(generic.CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("home")
    template_name = "accounts/signup.html"
    def form_valid(self, form):
        valid = super(SignUp, self).form_valid(form)
        email, password = form.cleaned_data.get('email'), form.cleaned_data.get('password1')
        new_user = authenticate(email=email, password=password)
        login(self.request, new_user)
        return valid