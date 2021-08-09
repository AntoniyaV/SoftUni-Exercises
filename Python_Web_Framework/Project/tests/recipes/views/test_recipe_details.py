from django.contrib.auth import get_user_model
from django.urls import reverse

from cooking_recipes.recipes.models import Recipe
from tests.base.tests import RecipesProjectTestCase

UserModel = get_user_model()


class RecipeDetailsTests(RecipesProjectTestCase):
    def test_getDetails_whenUserIsOwner_shouldReturnDetailsForOwner(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse('recipe-details', kwargs={'pk': self.recipe.id}))

        self.assertEqual(200, response.status_code)
        self.assertEqual(self.recipe.name, response.context['recipe'].name)
        self.assertTrue(response.context['is_owner'])

    def test_getDetails_whenUserIsNotOwner_shouldReturnDetailsForNotOwner(self):
        self.client.force_login(self.user)

        new_user = UserModel.objects.create_user(
            email='email@mail.com',
            password='newpass123',
        )

        new_recipe = Recipe.objects.create(
            recipe_type=Recipe.MAIN_DISH,
            name='Test name',
            ingredients=['ingredient1', 'ingredient2'],
            instructions='Test instructions',
            image='image/path.jpg',
            user=new_user,
        )

        response = self.client.get(reverse('recipe-details', kwargs={'pk': new_recipe.id}))

        self.assertEqual(200, response.status_code)
        self.assertEqual(new_recipe.name, response.context['recipe'].name)
        self.assertFalse(response.context['is_owner'])