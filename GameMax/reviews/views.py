from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from GameMax.reviews.forms import EditReviewForm
from GameMax.reviews.models import Review
from GameMax.reviews.serializers import ReviewSerializer
from GameMax.shop.models import Game


class UserReviewListView(LoginRequiredMixin, ListView):
    model = Review
    template_name = 'reviews/reviews.html'

    def get_queryset(self):
        return Review.objects.filter(user=self.request.user).order_by('-created_at')[:15]


class ReviewListView(ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]


class ReviewCreateView(CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        user = request.user.id
        game_id = request.data.get('game')

        try:
            game = Game.objects.get(id=game_id)
        except Game.DoesNotExist:
            return Response({
                'error': 'Game not found'
            }, status=status.HTTP_404_NOT_FOUND)

        review_data = {
            'user': user,
            'game': game.id,
            'rating': request.data.get('rating'),
            'review_text': request.data.get('review_text')
        }

        serializer = self.get_serializer(data=review_data)

        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


@login_required
def edit_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)

    if review.user != request.user:
        return redirect('home')

    if request.method == "POST":
        form = EditReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('reviews-page')
        else:
            return render(request, 'reviews/edit-review.html', {'form': form, 'review': review})
    else:
        form = EditReviewForm(instance=review)

    return render(request, 'reviews/edit-review.html', {'form': form, 'review': review})


class DeleteReview(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Review
    template_name = 'reviews/delete-review.html'
    pk_url_kwarg = 'review_id'

    def test_func(self):
        review = get_object_or_404(Review, pk=self.kwargs['review_id'])

        if review.user == self.request.user or self.request.user.is_staff or self.request.user.has_perm(
                'reviews.delete_review'):
            return True

        return False

    def get_success_url(self):
        review = get_object_or_404(Review, pk=self.kwargs['review_id'])

        if self.request.user.is_staff or self.request.user.has_perm('reviews.delete_review'):
            return reverse_lazy('game-details', kwargs={'slug': review.game.slug})

        return reverse_lazy('reviews-page')
