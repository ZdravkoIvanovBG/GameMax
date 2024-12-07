from django.views.generic import TemplateView, ListView
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response

from GameMax.interactions.models import Order, Review
from GameMax.interactions.serializers import OrderSerializer, ReviewSerializer
from GameMax.shop.models import CartItem, Game


class OrderPageView(ListView):
    model = Order
    template_name = 'shop/orders.html'

    def get_queryset(self):
        return Order.objects.filter(buyer=self.request.user)


class OrderCreateView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        user = request.user

        cart_items = CartItem.objects.filter(cart__user=user)

        if not cart_items.exists():
            return Response({
                'error': 'Your cart is empty'
            }, status=status.HTTP_400_BAD_REQUEST)

        total_cost = sum(item.game.price for item in cart_items)

        order = Order.objects.create(
            buyer=user,
            total_price=total_cost,
        )

        games = [item.game for item in cart_items]
        order.games.add(*games)

        cart_items.delete()

        serializer = self.get_serializer(order)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


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
