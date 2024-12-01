from django.db import models


class GenreChoices(models.TextChoices):
    ACTION = 'Action', 'Action'
    SURVIVAL = 'Survival', 'Survival'
    STRATEGY = 'Strategy', 'Strategy'
    ADVENTURE = 'Adventure', 'Adventure'
    FIRST_PERSON = 'First Person', 'First Person'
    MMO = 'MMO', 'MMO'
    SPORTS = 'Sports', 'Sports'
    OPEN_WORLD = 'Open World', 'Open World'