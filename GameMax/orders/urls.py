from django.urls import path

from GameMax.orders.views import OrderPageView, OrderCreateView, CancelOrderView, PayOrderView

urlpatterns = [
    path('', OrderPageView.as_view(), name='orders-page'),
    path('cancel/<int:pk>/', CancelOrderView.as_view(), name='cancel-order'),
    path('pay/<int:pk>/', PayOrderView.as_view(), name='pay-order'),
    path('api/checkout/', OrderCreateView.as_view(), name='checkout'),
]
