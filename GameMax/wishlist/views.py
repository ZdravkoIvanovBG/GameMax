from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, JsonResponse
from django.views.generic import ListView
from rest_framework import status
from rest_framework.generics import CreateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from GameMax.shop.models import Game
from GameMax.wishlist.models import Wishlist
from GameMax.wishlist.serializers import WishlistSerializer


class WishlistPage(LoginRequiredMixin, ListView):
    model = Wishlist
    template_name = 'wishlist/wishlist.html'

    def get_queryset(self):
        return Wishlist.objects.filter(user=self.request.user)


class WishlistItemCreateView(CreateAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
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

        if Wishlist.objects.filter(user=request.user, game_id=game_id).exists():
            return JsonResponse({
                'message': 'In Cart'
            }, status=status.HTTP_400_BAD_REQUEST)

        wishlist_data = {
            'user': user,
            'game': game.id
        }

        serializer = self.get_serializer(data=wishlist_data)

        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class RemoveWishlistItemView(DestroyAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer

    def get_object(self):
        wishlist_item_id = self.kwargs['pk']

        try:
            wishlist_item = Wishlist.objects.get(id=wishlist_item_id)

            return wishlist_item
        except Wishlist.DoesNotExist:
            return Http404
