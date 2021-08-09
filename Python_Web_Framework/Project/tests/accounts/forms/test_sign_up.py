from django.test import TestCase

from cooking_recipes.accounts.forms import SignUpForm


class SignUpTests(TestCase):
    def test_signUpForm_whenInvalidEmail_shouldNotSave(self):
        data = {
            'email': 'invalid',
            'password1': 'V@lidPass123',
            'password2': 'V@lidPass123',
            'first_name': 'ValidFirst',
            'last_name': 'ValidLast',
        }
        form = SignUpForm(data)

        self.assertFalse(form.is_valid())

    def test_signUpForm_whenDifferentPass_shouldNotSave(self):
        data = {
            'email': 'valid@mail.com',
            'password1': 'V@lidPass123',
            'password2': 'invalid',
            'first_name': 'ValidFirst',
            'last_name': 'ValidLast',
        }
        form = SignUpForm(data)

        self.assertFalse(form.is_valid())

    def test_signUpForm_whenValidEmailAndPassAndNoNames_shouldSave(self):
        data = {
            'email': 'valid@mail.com',
            'password1': 'V@lidPass123',
            'password2': 'V@lidPass123',
            'first_name': '',
            'last_name': '',
        }

        form = SignUpForm(data)

        self.assertTrue(form.is_valid())

    def test_signUpForm_whenValidData_shouldSave(self):
        data = {
            'email': 'valid@mail.com',
            'password1': 'V@lidPass123',
            'password2': 'V@lidPass123',
            'first_name': 'First',
            'last_name': 'Last',
        }

        form = SignUpForm(data)

        self.assertTrue(form.is_valid())
