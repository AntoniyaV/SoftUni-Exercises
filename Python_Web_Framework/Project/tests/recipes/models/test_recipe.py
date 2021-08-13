from django.core.exceptions import ValidationError
from django.test import TestCase

from cooking_recipes.accounts.models import RecipesUser
from cooking_recipes.recipes.models import Recipe


class RecipeTests(TestCase):
    def test_createRecipe_whenMissingOrInvalidData_shouldRaiseError(self):
        user = RecipesUser(
            email='valid@mail.com',
            password='V@lidPass123',
        )
        user.save()

        recipe = Recipe.objects.create(
            recipe_type='invalid',
            name='',
            ingredients=['ingredient1', 'ingredient2'],
            instructions='Valid instructions',
            image='',
            user=user,
        )

        try:
            recipe.full_clean()
            recipe.save()
            self.fail()
        except ValidationError as ex:
            self.assertIsNotNone(ex)

    def test_createRecipe_whenValidData_shouldCreateRecipe(self):
        user = RecipesUser(
            email='valid@mail.com',
            password='V@lidPass123',
        )
        user.save()

        recipe = Recipe.objects.create(
            recipe_type=Recipe.MAIN_DISH,
            name='Valid name',
            ingredients=['ingredient1', 'ingredient2'],
            instructions='Valid instructions',
            image='valid/image/path.jpg',
            user=user,
        )

        recipe.full_clean()
        recipe.save()

        self.assertIsNotNone(recipe)

    def test_strRecipe_shouldReturnRecipeName(self):
        user = RecipesUser(
            email='valid@mail.com',
            password='V@lidPass123',
        )
        user.save()

        recipe = Recipe.objects.create(
            recipe_type=Recipe.MAIN_DISH,
            name='Valid name',
            ingredients=['ingredient1', 'ingredient2'],
            instructions='Valid instructions',
            image='valid/image/path.jpg',
            user=user,
        )

        recipe_str = str(recipe)

        self.assertEqual(recipe.name, recipe_str)