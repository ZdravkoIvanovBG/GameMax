from django.urls import path

from GameMax.shop.views import ShopPageView

urlpatterns = [
    path('', ShopPageView.as_view(), name='shop')
]
