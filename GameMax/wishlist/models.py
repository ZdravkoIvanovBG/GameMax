from django.contrib.auth import get_user_model
from django.db import models

from GameMax.shop.models import Game

UserModel = get_user_model()


class Wishlist(models.Model):
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE
    )

    added_at = models.DateTimeField(
        auto_now_add=True
    )
