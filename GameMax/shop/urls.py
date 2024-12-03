from django.urls import path, include

from GameMax.shop.views import ShopPageView, GameListView, GameDetailView

urlpatterns = [
    path('', ShopPageView.as_view(), name='shop'),
    path('api/games/', GameListView.as_view(), name='games-list'),
    path('game/<slug:slug>/', GameDetailView.as_view(), name='game-details')
]
