from django.test import TestCase

from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.timezone import now

from GameMax.orders.models import Order

UserModel = get_user_model()


class TestOrderDelete(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create_user(
            email='test@test.com',
            password='01560157zZ'
        )

        self.other_user = UserModel.objects.create_user(
            email='test2@test.com',
            password='01560157zZ'
        )

        self.order = Order.objects.create(
            status='Pending',
            order_date=now(),
            total_price=59.99,
            paid=False,
            buyer=self.user
        )

        self.client.login(
            email='test@test.com',
            password='01560157zZ'
        )

    def test_order_delete__from_buyer__expect_success(self):
        self.assertTrue(Order.objects.filter(pk=self.order.pk).exists())

        response = self.client.post(
            reverse('cancel-order', kwargs={'pk': self.order.pk})
        )

        self.assertFalse(Order.objects.filter(pk=self.order.pk).exists())
        self.assertRedirects(response, reverse('orders-page'))

    def test_order_delete__from_other_user__expect_failure(self):
        self.client.login(
            email='test2@test.com',
            password='01560157zZ'
        )

        response = self.client.post(
            reverse('cancel-order', kwargs={'pk': self.order.pk})
        )

        self.assertTrue(Order.objects.filter(pk=self.order.pk).exists())
        self.assertEqual(response.status_code, 403)

    def test_order_delete__from_anonymous__expect_failure(self):
        self.client.logout()

        response = self.client.post(
            reverse('cancel-order', kwargs={'pk': self.order.pk})
        )

        self.assertTrue(Order.objects.filter(pk=self.order.pk).exists())
        self.assertEqual(response.status_code, 302)