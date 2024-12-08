from rest_framework import serializers

from GameMax.reviews.models import Review
from GameMax.reviews.serializers import ReviewSerializer
from GameMax.shop.models import Franchise, Game, Cart, CartItem


class FranchiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Franchise
        fields = '__all__'
        read_only_fields = ['id']


class GameSerializer(serializers.ModelSerializer):
    reviews = serializers.SerializerMethodField()

    class Meta:
        model = Game
        fields = ['id', 'title', 'price', 'welcome_message', 'description', 'game_image', 'franchise', 'pegi',
                  'game_abbreviation', 'genre', 'slug', 'reviews']
        read_only_fields = ['id', 'reviews']

    def get_reviews(self, obj):
        reviews = Review.objects.filter(game=obj.id)
        return ReviewSerializer(reviews, many=True).data


class GameFranchiseSerializer(serializers.ModelSerializer):
    franchise = FranchiseSerializer(read_only=True)

    class Meta:
        model = Game
        fields = '__all__'
        read_only_fields = ['id', 'franchise']


class CartItemSerializer(serializers.ModelSerializer):
    game = GameSerializer(read_only=True)

    class Meta:
        model = CartItem
        fields = ['id', 'cart', 'game']
        read_only_fields = ['id']


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    total_price = serializers.SerializerMethodField()

    def get_total_price(self, obj):
        return obj.total_price()

    class Meta:
        model = Cart
        fields = ['id', 'user', 'items', 'total_price']
        read_only_fields = ['id', 'items', 'total_price']
