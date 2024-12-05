from django.urls import path, include

from GameMax.shop.views import ShopPageView, GameListView, GameDetailView, AddToCartView, CartView, GameRetrieveView

urlpatterns = [
    path('', ShopPageView.as_view(), name='shop'),
    path('api/games/', GameListView.as_view(), name='games-list'),
    path('api/games/<int:pk>', GameRetrieveView.as_view(), name='single-game-details'),
    path('api/cart/add/', AddToCartView.as_view(), name='add-to-cart'),
    path('api/cart/', CartView.as_view(), name='cart'),
    path('game/<slug:slug>/', GameDetailView.as_view(), name='game-details')
]
