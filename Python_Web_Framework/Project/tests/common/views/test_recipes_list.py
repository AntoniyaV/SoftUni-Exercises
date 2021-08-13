from django.urls import reverse

from tests.base.tests import RecipesProjectTestCase


class RecipesListTests(RecipesProjectTestCase):
    def test_getRecipes_whenRecipesCategoryHasObjects_shouldShowObjects(self):
        response = self.client.get(reverse('main-dishes'))

        self.assertEqual(200, response.status_code)
        self.assertQuerysetEqual(response.context['recipe_list'], [self.recipe])

    def test_getRecipes_whenRecipesCategoryHasNoObjects_shouldNotShowObjects(self):
        response = self.client.get(reverse('soups'))

        self.assertEqual(200, response.status_code)
        self.assertQuerysetEqual(response.context['recipe_list'], [])
