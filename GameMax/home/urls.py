from django.urls import path

from GameMax.home.views import HomePage

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
]
