from __future__ import absolute_import

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views import generic
from django.core.urlresolvers import reverse_lazy

from braces import views

from talks.models import TalkList
from estates.models import EstateList

from .forms import RegistrationForm, LoginForm

class HomePageView(generic.TemplateView):
    template_name = 'home.html'


class SignUpView(views.AnonymousRequiredMixin, views.FormValidMessageMixin, generic.CreateView):
    form_class = RegistrationForm
    form_valid_message = 'Thanks for signing up, go ahead and login.'
    model = User
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

    def form_valid(self, form):
        resp = super(SignUpView, self).form_valid(form)
        TalkList.objects.create(user=self.object, name='To Attend')
        EstateList.objects.create(user=self.object, name='Annonces')
        return resp


class LoginView(views.AnonymousRequiredMixin, views.FormValidMessageMixin, generic.FormView):
    form_class = LoginForm
    form_valid_message = 'You are logged in now.'
    success_url = reverse_lazy('home')
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(self.request, user)
            return super(LoginView, self).form_valid(form)
        else:
            return self.form_invalid(form)


class LogOutView(views.LoginRequiredMixin, views.MessageMixin, generic.RedirectView):
    url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        logout(request)
        self.messages.success("You've been logged out. Come back soon!")
        return super(LogOutView, self).get(request, *args, **kwargs)
