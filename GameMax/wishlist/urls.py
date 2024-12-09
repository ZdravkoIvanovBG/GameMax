from django.urls import path

from GameMax.wishlist.views import WishlistPage, WishlistItemCreateView, RemoveWishlistItemView

urlpatterns = [
    path('', WishlistPage.as_view(), name='wishlist'),
    path('api/create/', WishlistItemCreateView.as_view(), name='wishlist-item-create'),
    path('api/delete/<int:pk>/', RemoveWishlistItemView.as_view(), name='wishlist-item-delete'),
]
