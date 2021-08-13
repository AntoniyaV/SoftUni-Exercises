from django.urls import reverse

from cooking_recipes.recipes.models import Recipe
from tests.base.tests import RecipesProjectTestCase


class RecipeDeleteTests(RecipesProjectTestCase):
    def test_getDelete_whenUserNotLoggedIn_shouldRedirect(self):
        response = self.client.get(reverse('recipe-delete', kwargs={'pk': self.recipe.id}))

        self.assertEqual(302, response.status_code)

    def test_getDelete_whenUserLoggedIn_shouldShowForm(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse('recipe-delete', kwargs={'pk': self.recipe.id}))
        all_recipes = Recipe.objects.all()

        self.assertEqual(200, response.status_code)
        self.assertEqual('recipe_delete.html', response.template_name[0])
        self.assertQuerysetEqual([self.recipe], all_recipes)

    def test_postDelete_whenUserLoggedIn_shouldDeleteRecipe(self):
        self.client.force_login(self.user)

        response = self.client.post(reverse('recipe-delete', kwargs={'pk': self.recipe.id}))
        all_recipes = Recipe.objects.all()

        self.assertEqual(302, response.status_code)
        self.assertQuerysetEqual([], all_recipes)