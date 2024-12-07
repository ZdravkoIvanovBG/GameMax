from django.urls import path

from GameMax.orders.views import OrderPageView, OrderCreateView

urlpatterns = [
    path('', OrderPageView.as_view(), name='orders-page'),
    path('api/checkout/', OrderCreateView.as_view(), name='checkout'),
]