from django.urls import path, include

from GameMax.reviews.views import UserReviewListView, ReviewListView, ReviewCreateView, edit_review, DeleteReview

urlpatterns = [
    path('', UserReviewListView.as_view(), name='reviews-page'),
    path('edit/<int:review_id>/', edit_review, name='edit-review'),
    path('delete/<int:review_id>/', DeleteReview.as_view(), name='delete-review'),
    path('api/reviews/', include([
        path('', ReviewListView.as_view(), name='review-list'),
        path('create/', ReviewCreateView.as_view(), name='review-create'),
    ]))
]
