from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status


class UserViewSetTest(APITestCase):
    base_edit_url = reverse("api:user-edit-list")
    base_url_login = reverse("api:login-list")

    data_login = {"password": "12345678", "email": "teast@admin.com"}

    def test_edit(self):

        # Login to retrieve token

        response = self.client.post(f"{self.base_url_login}", data=self.data_login)
        response_data = response.json()

        token = response_data["token"]
        user_id = response_data["user"]["_id"]

        self.client.credentials(HTTP_AUTHORIZATION=token)

        # Edit user

        data = {
            "email": "new@admin.com",
            "userID": user_id,
        }

        response = self.client.post(f"{self.base_edit_url}", data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_data = response.json()

        self.assertEqual(response_data["success"], True)
