from django.contrib import messages
from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponseForbidden
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from GameMax.app_users.forms import AppUserCreationForm, AppUserLoginForm, ProfileEditForm
from GameMax.app_users.models import Profile

UserModel = get_user_model()


class AppUserLoginView(LoginView):
    authentication_form = AppUserLoginForm
    template_name = 'app_users/login_page.html'


class AppUserRegisterView(CreateView):
    model = UserModel
    form_class = AppUserCreationForm
    template_name = 'app_users/register_page.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)

        login(self.request, user=self.object)

        return response


class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'app_users/profile_page.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.pk != kwargs['pk']:
            return HttpResponseForbidden  # TODO: Make 403.html page

        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy(
            'profile-details',
            kwargs={'pk': self.object.pk}
        )
