from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, UpdateView
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from GameMax.orders.models import Order
from GameMax.orders.serializers import OrderSerializer
from GameMax.shop.models import CartItem


class OrderPageView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'orders/orders.html'

    def get_queryset(self):
        return Order.objects.filter(buyer=self.request.user)


class OrderCreateView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

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


class CancelOrderView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Order
    template_name = 'orders/cancel-order.html'
    success_url = reverse_lazy('orders-page')

    def test_func(self):
        order = get_object_or_404(Order, pk=self.kwargs['pk'])

        return self.request.user == order.buyer


class PayOrderView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Order
    fields = []
    context_object_name = 'order'
    template_name = 'orders/pay-order.html'

    def test_func(self):
        order = get_object_or_404(Order, pk=self.kwargs['pk'])

        return self.request.user == order.buyer

    def post(self, request, *args, **kwargs):
        order = self.get_object()

        if order.paid:
            return redirect('home')

        order.paid = True
        order.status = "Delivered"

        order.save()

        return redirect('orders-page')
