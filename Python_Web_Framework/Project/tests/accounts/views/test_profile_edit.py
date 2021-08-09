from django.urls import reverse

from tests.base.tests import RecipesProjectTestCase


class ProfileEditTests(RecipesProjectTestCase):
    def test_getEdit_whenNotLoggedIn_shouldRedirect(self):
        response = self.client.get(reverse('profile-edit', kwargs={'pk': self.user.id}))

        self.assertEqual(302, response.status_code)

    def test_postEdit_whenUserChangesNames_shouldChangeNames(self):
        self.client.force_login(self.user)

        response = self.client.post(
            reverse('profile-edit',
                    kwargs={'pk': self.user.id}
                    ),
            data={
                'first_name': 'NewFirstName',
                'last_name': 'NewLastName',
            }
        )

        self.assertEqual(302, response.status_code)

        self.user.refresh_from_db()
        self.assertEqual('NewFirstName', self.user.first_name)
        self.assertEqual('NewLastName', self.user.last_name)

