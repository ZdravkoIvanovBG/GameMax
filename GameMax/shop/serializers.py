from rest_framework import serializers

from GameMax.shop.models import Franchise, Game


class FranchiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Franchise
        fields = '__all__'
        read_only_fields = ['id']


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'
        read_only_fields = ['id']


class GameFranchiseSerializer(serializers.ModelSerializer):
    franchise = FranchiseSerializer(read_only=True)

    class Meta:
        model = Game
        fields = '__all__'
        read_only_fields = ['id', 'franchise']
