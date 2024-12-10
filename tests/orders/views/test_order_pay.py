from django.test import TestCase

from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.timezone import now

from GameMax.orders.models import Order

UserModel = get_user_model()


class TestOrderPay(TestCase):
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

    def test_order_pay__from_buyer__expect_success(self):
        self.assertFalse(self.order.paid)

        response = self.client.post(reverse('pay-order', kwargs={'pk': self.order.pk}))

        self.order.refresh_from_db()
        self.assertTrue(self.order.paid)
        self.assertEqual(response.status_code, 302)

    def test_order_pay__from_non_buyer__expect_failure(self):
        self.client.login(
            email='test2@test.com',
            password='01560157zZ'
        )

        self.assertFalse(self.order.paid)

        response = self.client.post(reverse('pay-order', kwargs={'pk': self.order.pk}))

        self.order.refresh_from_db()
        self.assertFalse(self.order.paid)
        self.assertEqual(response.status_code, 403)
