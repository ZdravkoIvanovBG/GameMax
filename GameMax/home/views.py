from django.views.generic import TemplateView
from rest_framework.generics import RetrieveAPIView

from GameMax.shop.models import Cart
from GameMax.shop.serializers import CartSerializer


class HomePage(TemplateView):
    template_name = 'home/home_page.html'
