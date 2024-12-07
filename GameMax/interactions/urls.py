from django.urls import path

from GameMax.interactions.views import OrderCreateView, OrderPageView, ReviewCreateView, ReviewListView, \
    UserReviewListView

urlpatterns = [
    path('orders/', OrderPageView.as_view(), name='orders-page'),
    path('reviews/', UserReviewListView.as_view(), name='reviews-page'),
    path('api/checkout/', OrderCreateView.as_view(), name='checkout'),
    path('api/reviews/create/', ReviewCreateView.as_view(), name='review-create'),
    path('api/reviews/', ReviewListView.as_view(), name='review-list'),
]
