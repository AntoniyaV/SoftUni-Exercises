from django.contrib.auth import get_user_model
from django.test import TestCase, Client

from cooking_recipes.recipes.models import Recipe

UserModel = get_user_model()


class RecipesProjectTestCase(TestCase):
    user_email = 'user@site.com'
    user_password = 'password123'
    first_name = 'FirstName'
    last_name = 'LastName'

    def setUp(self):
        self.client = Client()

        self.user = UserModel.objects.create_user(
            email=self.user_email,
            password=self.user_password,
            first_name=self.first_name,
            last_name=self.last_name,
        )

        self.recipe = Recipe.objects.create(
            recipe_type=Recipe.MAIN_DISH,
            name='Test name',
            ingredients=['ingredient1', 'ingredient2'],
            instructions='Test instructions',
            image='image/path.jpg',
            user=self.user,
        )

