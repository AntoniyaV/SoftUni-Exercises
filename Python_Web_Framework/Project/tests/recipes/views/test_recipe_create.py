from django.urls import reverse

from tests.base.tests import RecipesProjectTestCase


class RecipeCreateTests(RecipesProjectTestCase):
    def test_getCreateRecipe_whenUserNotLoggedIn_shouldRedirect(self):
        response = self.client.get(reverse('recipe-create'))

        self.assertEqual(302, response.status_code)

    def test_getCreate_whenUserLoggedIn_shouldShowForm(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse('recipe-create'))

        self.assertEqual(200, response.status_code)
        self.assertEqual('recipe_create.html', response.template_name[0])

