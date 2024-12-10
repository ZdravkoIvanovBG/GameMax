from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.utils.timezone import now

from GameMax.reviews.models import Review
from GameMax.shop.models import Game, Franchise

UserModel = get_user_model()


class TestReviewDelete(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create_user(
            email='test@test.com',
            password='01560157zZ'
        )

        self.other_user = UserModel.objects.create_user(
            email='test2@test.com',
            password='01560157zZ'
        )

        self.franchise = Franchise.objects.create(
            name='Test franchise',
            franchise_image='test_image.jpg'
        )

        self.game = Game.objects.create(
            title='Test game',
            price=19.99,
            welcome_message='Welcome to test game',
            description='Test game description',
            game_image='test_image.jpg',
            pegi='12+',
            game_abbreviation='TES',
            genre='Action',
            franchise=self.franchise,
            slug='test-game',
        )

        self.review = Review.objects.create(
            rating=5,
            review_text='Test review',
            created_at=now(),
            game=self.game,
            user=self.user
        )

        self.client.login(
            email='test@test.com',
            password='01560157zZ'
        )

    def test_review_delete__from_author_user__expect_success(self):
        self.assertTrue(Review.objects.filter(pk=self.review.pk).exists())

        response = self.client.post(
            reverse('delete-review', kwargs={'review_id': self.review.id})
        )

        self.assertFalse(Review.objects.filter(pk=self.review.pk).exists())
        self.assertEqual(response.status_code, 302)

    def test_review_delete__from_non_author_user__expect_failure(self):
        self.client.login(
            email='test2@test.com',
            password='01560157zZ'
        )

        self.assertTrue(Review.objects.filter(pk=self.review.pk).exists())

        response = self.client.post(
            reverse('delete-review', kwargs={'review_id': self.review.id})
        )

        self.assertTrue(Review.objects.filter(pk=self.review.pk).exists())
        self.assertEqual(response.status_code, 403)

    def test_review_delete__from_anonymous__expect_failure(self):
        self.client.logout()

        self.assertTrue(Review.objects.filter(pk=self.review.pk).exists())

        response = self.client.post(
            reverse('delete-review', kwargs={'review_id': self.review.id})
        )

        self.assertTrue(Review.objects.filter(pk=self.review.pk).exists())
        self.assertEqual(response.status_code, 302)
