from django.urls import path, include

from GameMax.shop.views import ShopPageView, GameListView

urlpatterns = [
    path('', ShopPageView.as_view(), name='shop'),
    path('api/games/', GameListView.as_view(), name='games-list')
]
