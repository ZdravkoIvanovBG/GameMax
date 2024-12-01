from django.shortcuts import render
from django.views.generic import TemplateView


class ShopPageView(TemplateView):
    template_name = 'shop/shop.html'
