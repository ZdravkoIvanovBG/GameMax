from django.contrib import admin

from GameMax.shop.models import Game, Franchise


@admin.register(Franchise)
class FranchiseAdmin(admin.ModelAdmin):
    pass


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'franchise', 'pegi', 'genre']

    list_filter = ['pegi', 'genre']

    search_fields = ['title']