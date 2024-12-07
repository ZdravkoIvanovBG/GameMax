from django.contrib.auth import get_user_model
from django.db import models

from GameMax.orders.choices import OrderStatusChoices, PaidChoices
from GameMax.shop.models import Game

UserModel = get_user_model()


class Order(models.Model):
    status = models.CharField(
        max_length=20,
        choices=OrderStatusChoices.choices,
        default=OrderStatusChoices.PENDING
    )

    order_date = models.DateTimeField(
        auto_now_add=True
    )

    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    paid = models.BooleanField(
        choices=[
            (True, PaidChoices.PAID),
            (False, PaidChoices.NOT_PAID),
        ],
        default=False,
    )

    buyer = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name='orders'
    )

    games = models.ManyToManyField(Game)
