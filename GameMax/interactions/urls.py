from django.urls import path

from GameMax.interactions.views import OrderCreateView, OrderPageView

urlpatterns = [
    path('orders/', OrderPageView.as_view(), name='orders-page'),
    path('api/checkout/', OrderCreateView.as_view(), name='checkout'),
]
