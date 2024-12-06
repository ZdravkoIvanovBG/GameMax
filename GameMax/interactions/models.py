from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from GameMax.interactions.choices import OrderStatusChoices, PaidChoices
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


class Review(models.Model):
    game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE,
        related_name='reviews'
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    rating = models.IntegerField(
        default=1,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )

    review_text = models.TextField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )
