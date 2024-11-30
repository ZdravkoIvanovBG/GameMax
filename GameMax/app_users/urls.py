from django.contrib.auth.views import LogoutView
from django.urls import path, include

from GameMax.app_users.views import AppUserLoginView, AppUserRegisterView, ProfileEditView

urlpatterns = [
    path('login/', AppUserLoginView.as_view(), name='login'),
    path('register/', AppUserRegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/<int:pk>/', include([
        path('', ProfileEditView.as_view(), name='profile-details')
    ]))
]
