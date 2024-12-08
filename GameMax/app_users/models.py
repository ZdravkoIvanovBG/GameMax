from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import MinValueValidator, MinLengthValidator, MaxValueValidator
from django.db import models

from GameMax.app_users.managers import AppUserManager
from GameMax.app_users.validators import MaxFileSizeValidator, OnlyLettersDigitsUnderscoresValidator


class AppUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
        null=True,
        blank=True,
        error_messages={
            'unique': "User with this Email already exists."
        }
    )

    is_active = models.BooleanField(
        default=True
    )

    is_staff = models.BooleanField(
        default=False
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = AppUserManager()

    class Meta:
        verbose_name = 'User'


class Profile(models.Model):
    full_name = models.CharField(
        max_length=100,
        null=True,
        blank=False,
        validators=[
            MinLengthValidator(2, message='Your Name Must Be At Least 2 Characters Long.'),
            OnlyLettersDigitsUnderscoresValidator()
        ]
    )

    age = models.PositiveIntegerField(
        validators=[
            MinValueValidator(15),
            MaxValueValidator(99)
        ]
    )

    phone_number = models.CharField(
        max_length=10,
        null=True,
        blank=True,
        validators=[
            MinLengthValidator(10, message="Phone Number needs to be 10 characters long.")
        ]
    )

    profile_picture = models.ImageField(
        upload_to='profile_pictures',
        null=True,
        blank=True,
        validators=[
            MaxFileSizeValidator()
        ]
    )

    user = models.OneToOneField(
        to=AppUser,
        on_delete=models.CASCADE,
        primary_key=True
    )

    def __str__(self):
        return self.full_name or 'Anonymous'

    def get_name(self):
        return self.full_name.split()[0] or 'Anonymous'
