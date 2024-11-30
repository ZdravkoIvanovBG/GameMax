from django.contrib.auth import get_user_model, login
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from GameMax.app_users.forms import AppUserCreationForm, AppUserLoginForm

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
