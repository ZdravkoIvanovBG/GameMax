from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.utils.timezone import now

from GameMax.reviews.forms import EditReviewForm
from GameMax.reviews.models import Review
from GameMax.shop.models import Game, Franchise

UserModel = get_user_model()


class TestReviewEdit(TestCase):
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

    def test_review_edit__from_author_user__expect_success(self):
        self.assertTrue(Review.objects.filter(pk=self.review.pk).exists())

        response = self.client.post(reverse('edit-review', kwargs={'review_id': self.review.id}), {
            'rating': 4,
            'review_text': 'Updated test review'
        })

        self.assertTrue(Review.objects.get(pk=self.review.pk).rating == 4)
        self.assertTrue(Review.objects.get(pk=self.review.pk).review_text == 'Updated test review')
        self.assertEqual(response.status_code, 302)

    def test_review_edit__from_non_author_user__expect_failure(self):
        self.client.login(
            email='test2@test.com',
            password='01560157zZ'
        )

        self.assertTrue(Review.objects.filter(pk=self.review.pk).exists())

        response = self.client.post(reverse('edit-review', kwargs={'review_id': self.review.id}), {
            'rating': 4,
            'review_text': 'Updated test review'
        })

        self.assertTrue(Review.objects.get(pk=self.review.pk).rating == 5)
        self.assertTrue(Review.objects.get(pk=self.review.pk).review_text == 'Test review')
        self.assertEqual(response.status_code, 403)

    def test_review_edit__with_invalid_rating__expect_failure(self):
        self.assertTrue(Review.objects.filter(pk=self.review.id).exists())

        response = self.client.post(reverse('edit-review', kwargs={'review_id': self.review.id}), {
            'rating': 6,
            'review_text': 'Updated test review'
        })

        self.assertTrue(Review.objects.get(pk=self.review.id).rating == 5)
        self.assertTrue(Review.objects.get(pk=self.review.id).review_text == 'Test review')
        self.assertEqual(response.status_code, 200)

    def test_invalid_rating_form(self):
        form = EditReviewForm(data={'rating': 6, 'review_text': 'Updated review'})
        self.assertFalse(form.is_valid())
        self.assertIn('Rating must be between 1 and 5.', form.errors['rating'])
