from django.contrib.auth import get_user_model
from django.urls import reverse

from tests.base.tests import RecipesProjectTestCase


UserModel = get_user_model()


class ProfileDetailsTests(RecipesProjectTestCase):
    def test_getDetails_whenNotLoggedIn_shouldRedirect(self):
        response = self.client.get(reverse('profile-details', kwargs={'pk': self.user.id}))

        self.assertEqual(302, response.status_code)

    def test_getDetails_whenLoggedInWithoutRecipes_shouldGetDetailsWithoutRecipes(self):
        new_user = UserModel.objects.create_user(
            email='email@mail.com',
            password='newpass123',
        )
        self.client.force_login(new_user)

        response = self.client.get(reverse('profile-details', kwargs={'pk': new_user.id}))

        self.assertEqual(200, response.status_code)
        self.assertListEqual([], list(response.context['recipes']))
        self.assertEqual(new_user.id, response.context['profile'].user_id)

    def test_getDetails_whenLoggedInWithRecipes_shouldGetDetailsWithRecipes(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse('profile-details', kwargs={'pk': self.user.id}))

        self.assertEqual(200, response.status_code)
        self.assertListEqual([self.recipe], list(response.context['recipes']))
        self.assertEqual(self.user.id, response.context['profile'].user_id)
