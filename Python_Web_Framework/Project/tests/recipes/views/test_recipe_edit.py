from django.urls import reverse

from cooking_recipes.recipes.models import Recipe
from tests.base.tests import RecipesProjectTestCase


class RecipeEditTests(RecipesProjectTestCase):

    def test_getEdit_whenUserNotLoggedIn_shouldRedirect(self):
        response = self.client.get(reverse('recipe-edit', kwargs={'pk': self.recipe.id}))

        self.assertEqual(302, response.status_code)

    def test_getEdit_whenUserLoggedIn_shouldShowForm(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse('recipe-edit', kwargs={'pk': self.recipe.id}))

        self.assertEqual(200, response.status_code)
        self.assertEqual('recipe_edit.html', response.template_name[0])

    def test_postEdit_whenValidData_shouldChangeThatData(self):
        self.client.force_login(self.user)

        response = self.client.post(reverse('recipe-edit', kwargs={'pk': self.recipe.id}),
                                    data={
                                        'recipe_type': Recipe.MAIN_DISH,
                                        'name': 'New name',
                                        'ingredients': ['ingredient1', 'ingredient2'],
                                        'instructions': 'New instructions',
                                        'image': 'image/path.jpg',
                                    })

        self.assertEqual(302, response.status_code)

        self.recipe.refresh_from_db()
        self.assertEqual('New name', self.recipe.name)
        self.assertEqual('New instructions', self.recipe.instructions)
        self.assertEqual(self.user, self.recipe.user)

    def test_postEdit_whenInvalidData_shouldStayOnFormAndNotSaveChanges(self):
        self.client.force_login(self.user)

        response = self.client.post(reverse('recipe-edit', kwargs={'pk': self.recipe.id}),
                                    data={
                                        'recipe_type': 'INVALID',
                                        'name': 'New name',
                                        'ingredients': ['ingredient1', 'ingredient2'],
                                        'instructions': 'New instructions',
                                        'image': 'image/path.jpg',
                                    })

        self.assertEqual(200, response.status_code)

        self.recipe.refresh_from_db()
        self.assertNotEqual('INVALID', self.recipe.recipe_type)
        self.assertNotEqual('New name', self.recipe.name)
        self.assertNotEqual('New instructions', self.recipe.instructions)
