from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from rest_framework.generics import RetrieveAPIView, ListAPIView

from GameMax.shop.models import Game, Franchise
from GameMax.shop.serializers import GameSerializer


class ShopPageView(ListView):
    model = Franchise
    template_name = 'shop/shop.html'


class GameListView(ListAPIView):
    serializer_class = GameSerializer

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
