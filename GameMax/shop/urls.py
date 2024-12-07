from django.urls import path, include

from GameMax.shop.views import ShopPageView, GameListView, GameDetailView, AddToCartView, GameRetrieveView, \
    RemoveFromCart, CartView

urlpatterns = [
    # Shop-related URLs
    path('', ShopPageView.as_view(), name='shop'),
    path('game/<slug:slug>/', GameDetailView.as_view(), name='game-details'),

    # Game-related API Paths
    path('api/games/', GameListView.as_view(), name='games-list'),
    path('api/games/<slug:slug>/', GameRetrieveView.as_view(), name='single-game-details'),

    # Cart-related API paths
    path('api/cart/remove/<int:pk>/', RemoveFromCart.as_view(), name='remove-from-cart'),
    path('api/cart/', include([
        # path('', CartView.as_view(), name='cart'),
        path('add/', AddToCartView.as_view(), name='add-to-cart'),
    ])),
]
