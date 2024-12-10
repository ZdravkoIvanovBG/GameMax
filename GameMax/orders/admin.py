from django.contrib import admin

from GameMax.orders.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'status', 'order_date', 'total_price']
    ordering = ['id']
    list_filter = ['status', 'order_date']