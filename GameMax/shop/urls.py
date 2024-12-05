from django.urls import path, include

from GameMax.shop.views import ShopPageView, GameListView, GameDetailView, AddToCartView, GameRetrieveView, \
    RemoveFromCart, CartView

urlpatterns = [
    path('', ShopPageView.as_view(), name='shop'),
    path('api/games/', GameListView.as_view(), name='games-list'),
    path('api/games/<int:pk>/', GameRetrieveView.as_view(), name='single-game-details'),
    path('api/cart/remove/<int:pk>/', RemoveFromCart.as_view(), name='remove-from-cart'),
    path('api/cart/', include([
        path('', CartView.as_view(), name='cart'),
        path('add/', AddToCartView.as_view(), name='add-to-cart'),
    ])),
    path('game/<slug:slug>/', GameDetailView.as_view(), name='game-details'),
]
