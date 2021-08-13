from django.core.exceptions import ValidationError
from django.test import TestCase

from cooking_recipes.accounts.models import RecipesUser


class RecipesUserTests(TestCase):
    def test_userCreate_whenInvalidEmail_shouldRaiseError(self):
        user = RecipesUser(
            email='invalid',
            password='V@lidPass123',
        )

        try:
            user.full_clean()
            user.save()
            self.fail()
        except ValidationError as ex:
            self.assertIsNotNone(ex)

    def test_userCreate_whenInvalidPass_shouldRaiseError(self):
        user = RecipesUser(
            email='valid@mail.com',
            password='',
        )

        try:
            user.full_clean()
            user.save()
            self.fail()
        except ValidationError as ex:
            self.assertIsNotNone(ex)

    def test_userCreate_whenValidEmailAndPass_shouldCreateUser(self):
        user = RecipesUser(
            email='valid@mail.com',
            password='V@lidPass123',
        )

        user.full_clean()
        user.save()

        self.assertIsNotNone(user)

    def test_userGetFullName_whenCreatedWithNames_shouldReturnFullName(self):
        user = RecipesUser(
            email='valid@mail.com',
            password='V@lidPass123',
            first_name='FirstName',
            last_name='LastName',
        )

        full_name = user.get_full_name()
        expected_full_name = 'FirstName LastName'

        self.assertEqual(expected_full_name, full_name)