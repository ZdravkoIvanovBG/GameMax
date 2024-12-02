from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.generics import RetrieveAPIView, ListAPIView

from GameMax.shop.models import Game
from GameMax.shop.serializers import GameSerializer


class ShopPageView(TemplateView):
    template_name = 'shop/shop.html'


class GameListView(ListAPIView):
    serializer_class = GameSerializer

    def get_queryset(self):
        queryset = Game.objects.all()

        franchise = self.request.query_params.get('franchise')

        if franchise:
            queryset = queryset.filter(franchise__name=franchise)

        return queryset
