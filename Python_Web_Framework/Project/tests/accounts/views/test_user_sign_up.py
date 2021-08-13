from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from cooking_recipes.accounts.models import RecipesUserProfile

UserModel = get_user_model()


class SignUpUserTests(TestCase):
    def test_postSignUp_whenValidData_shouldSignUpUser(self):
        client = Client()

        data = {
            'email': 'valid@mail.com',
            'password1': 'V@lidPass123',
            'password2': 'V@lidPass123',
            'first_name': 'FirstName',
            'last_name': 'LastName',
        }

        response = client.post(reverse('sign-up'), data=data)
        new_user = UserModel.objects.last()
        all_users = UserModel.objects.all()

        self.assertEqual(302, response.status_code)
        self.assertQuerysetEqual([new_user], all_users)
        self.assertEqual('valid@mail.com', new_user.email)
        self.assertEqual('FirstName', new_user.first_name)
        self.assertEqual('LastName', new_user.last_name)

    def test_postSignUp_whenValidDataWithNoNames_shouldSignUpUser(self):
        client = Client()

        data = {
            'email': 'valid@mail.com',
            'password1': 'V@lidPass123',
            'password2': 'V@lidPass123',
            'first_name': '',
            'last_name': '',
        }

        response = client.post(reverse('sign-up'), data=data)
        new_user = UserModel.objects.last()
        all_users = UserModel.objects.all()

        self.assertEqual(302, response.status_code)
        self.assertQuerysetEqual([new_user], all_users)
        self.assertEqual('valid@mail.com', new_user.email)
        self.assertEqual('', new_user.first_name)
        self.assertEqual('', new_user.last_name)

    def test_postSignUp_whenValidData_shouldCreateProfile(self):
        client = Client()

        data = {
            'email': 'valid@mail.com',
            'password1': 'V@lidPass123',
            'password2': 'V@lidPass123',
            'first_name': 'FirstName',
            'last_name': 'LastName',
        }

        response = client.post(reverse('sign-up'), data=data)
        new_user = UserModel.objects.last()
        profile = RecipesUserProfile.objects.last()

        self.assertEqual(302, response.status_code)
        self.assertEqual(profile.user_id, new_user.id)

    def test_postSignUp_whenInvalidData_shouldStayOnFormAndNotCreateUserOrProfile(self):
        client = Client()

        data = {
            'email': 'invalid',
            'password1': 'V@lidPass123',
            'password2': 'V@lidPass123',
            'first_name': 'FirstName',
            'last_name': 'LastName',
        }

        response = client.post(reverse('sign-up'), data=data)
        all_users = UserModel.objects.all()
        all_profiles = RecipesUserProfile.objects.all()

        self.assertEqual(200, response.status_code)
        self.assertQuerysetEqual([], all_users)
        self.assertQuerysetEqual([], all_profiles)