from django.urls import path, include

from GameMax.reviews.views import UserReviewListView, ReviewListView, ReviewCreateView

urlpatterns = [
    path('', UserReviewListView.as_view(), name='reviews-page'),
    path('api/reviews/', include([
        path('', ReviewListView.as_view(), name='review-list'),
        path('create/', ReviewCreateView.as_view(), name='review-create'),
    ]))
]