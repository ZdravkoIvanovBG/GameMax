from django.views.generic import ListView
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from GameMax.orders.models import Order
from GameMax.orders.serializers import OrderSerializer
from GameMax.shop.models import CartItem


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
