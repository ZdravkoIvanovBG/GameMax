from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from GameMax.shop.models import Game, Franchise, Cart, CartItem
from GameMax.shop.serializers import GameSerializer, CartItemSerializer, CartSerializer


class ShopPageView(ListView):
    model = Franchise
    template_name = 'shop/shop.html'


class GameListView(ListAPIView):
    serializer_class = GameSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Game.objects.all()

        franchise = self.request.query_params.get('franchise')

        if franchise:
            queryset = queryset.filter(franchise__name=franchise)

        return queryset


class GameDetailView(DetailView):
    model = Game
    template_name = 'products/product-details.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


class GameRetrieveView(RetrieveAPIView):
    serializer_class = GameSerializer
    queryset = Game.objects.all()
    lookup_field = 'slug'


class CartView(RetrieveAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user = self.request.user

        cart, created = Cart.objects.get_or_create(user=user)

        return cart


@extend_schema(
    tags=['shop'],
    summary='Add To Cart',
    request=CartItemSerializer,
)
class AddToCartView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        game_id = request.data.get('game')

        if not game_id:
            return Response({
                'error': 'Game ID is required.'
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            game = Game.objects.get(id=game_id)
        except Game.DoesNotExist:
            return Response({
                'error': 'Game Not Found.'
            }, status=status.HTTP_404_NOT_FOUND)

        cart, created = Cart.objects.get_or_create(user=request.user)

        cart_item, created = CartItem.objects.get_or_create(cart=cart, game=game)

        cart_item_serializer = CartItemSerializer(cart_item)

        return Response({
            'message': 'Game added to the cart.',
            'cart_item': cart_item_serializer.data
        }, status=status.HTTP_201_CREATED)


class RemoveFromCart(DestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        cart_item_id = self.kwargs['pk']

        try:
            cart_item = CartItem.objects.get(id=cart_item_id)

            return cart_item
        except CartItem.DoesNotExist:
            return Http404

    def perform_destroy(self, instance):
        instance.delete()
