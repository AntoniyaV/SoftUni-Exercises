from django.urls import reverse

from tests.base.tests import RecipesProjectTestCase


class LandingPageTests(RecipesProjectTestCase):
    def test_getLandingPage_whenUserNotLoggedIn_shouldLoadPage(self):
        response = self.client.post(reverse('landing'))

        self.assertEqual(200, response.status_code)

    def test_getLandingPage_whenUserLoggedIn_shouldLoadPage(self):
        self.client.force_login(self.user)

        response = self.client.post(reverse('landing'))

        self.assertEqual(200, response.status_code)
