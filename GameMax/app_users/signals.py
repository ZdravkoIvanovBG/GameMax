from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from GameMax.app_users.models import Profile

UserModel = get_user_model()


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile(sender, instance: UserModel, created: bool, **kwargs):
    if created:
        Profile.objects.create(
            user=instance,
            age=18,
        )
