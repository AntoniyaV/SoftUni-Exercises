from django.urls import reverse

from tests.base.tests import RecipesProjectTestCase


class WarningPageTests(RecipesProjectTestCase):
    def test_getWarningPage_whenUserNotLoggedIn_shouldLoadPage(self):
        response = self.client.post(reverse('login-required'))

        self.assertEqual(200, response.status_code)

    def test_getWarningPage_whenUserLoggedIn_shouldLoadPage(self):
        self.client.force_login(self.user)

        response = self.client.post(reverse('login-required'))

        self.assertEqual(200, response.status_code)