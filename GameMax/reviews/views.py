from django.views.generic import ListView
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response

from GameMax.reviews.models import Review
from GameMax.reviews.serializers import ReviewSerializer
from GameMax.shop.models import Game


class UserReviewListView(ListView):
    model = Review
    template_name = 'reviews/reviews.html'

    def get_queryset(self):
        return Review.objects.filter(user=self.request.user).order_by('-created_at')[:15]


class ReviewListView(ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewCreateView(CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

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
