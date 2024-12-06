from rest_framework import serializers

from GameMax.interactions.serializers import ReviewSerializer
from GameMax.shop.models import Franchise, Game, Cart, CartItem


class FranchiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Franchise
        fields = '__all__'
        read_only_fields = ['id']


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'
        read_only_fields = ['id', 'reviews']


class GameFranchiseSerializer(serializers.ModelSerializer):
    franchise = FranchiseSerializer(read_only=True)

    class Meta:
        model = Game
        fields = '__all__'
        read_only_fields = ['id', 'franchise']


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    total_price = serializers.SerializerMethodField()

    def get_total_price(self, obj):
        return obj.total_price()

    class Meta:
        model = Cart
        fields = ['id', 'user', 'items', 'total_price']
        read_only_fields = ['id', 'items', 'total_price']
