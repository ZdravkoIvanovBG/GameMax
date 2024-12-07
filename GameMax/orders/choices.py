from django.db import models


class OrderStatusChoices(models.TextChoices):
    PENDING = 'Pending', 'Pending'
    CANCELLED = 'Cancelled', 'Cancelled'
    DELIVERED = 'Delivered', 'Delivered'


class PaidChoices(models.TextChoices):
    PAID = 'Paid', 'Paid'
    NOT_PAID = 'Not Paid', 'Not Paid'
