from django.urls import path

from GameMax.app_users.views import AppUserLoginView, AppUserRegisterView

urlpatterns = [
    path('login/', AppUserLoginView.as_view(), name='login'),
    path('register/', AppUserRegisterView.as_view(), name='register'),
]