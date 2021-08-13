from django.test import TestCase

from cooking_recipes.accounts.models import RecipesUser, RecipesUserProfile


class RecipesUserProfileTests(TestCase):
    def test_createUser_shouldCreateUserProfile(self):
        user = RecipesUser(
            email='valid@mail.com',
            password='V@lidPass123',
        )
        user.save()

        profile = RecipesUserProfile.objects.last()
        self.assertEqual(profile.user_id, user.id)
