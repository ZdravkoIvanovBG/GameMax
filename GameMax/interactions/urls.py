from django.urls import path

from GameMax.interactions.views import OrderCreateView

urlpatterns = [
    path('api/checkout/', OrderCreateView.as_view(), name='checkout'),
]
