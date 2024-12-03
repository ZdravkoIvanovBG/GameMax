from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.text import slugify

from GameMax.app_users.validators import MaxFileSizeValidator
from GameMax.home.choices import GenreChoices


class Franchise(models.Model):
    name = models.CharField(
        max_length=50
    )

    franchise_image = models.ImageField(
        upload_to='franchise_images/',
        validators=[
            MaxFileSizeValidator()
        ]
    )

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(
        max_length=200,
        validators=[
            MinLengthValidator(5, 'The Title Is At Least 5 Chaacters Long!'),
        ]
    )

    price = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )

    welcome_message = models.CharField(
        max_length=90
    )

    description = models.TextField()

    game_image = models.ImageField(
        upload_to='game_images/'
    )

    franchise = models.ForeignKey(
        to=Franchise,
        on_delete=models.CASCADE
    )

    pegi = models.CharField(
        max_length=3,
        validators=[
            MinLengthValidator(3)
        ]
    )

    game_abbreviation = models.CharField(
        max_length=15
    )

    genre = models.CharField(
        max_length=20,
        choices=GenreChoices.choices
    )

    slug = models.SlugField(
        unique=True,
        null=True,
        blank=True
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
