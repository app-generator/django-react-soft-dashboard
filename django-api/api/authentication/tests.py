from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status


class AuthenticationTest(APITestCase):
    base_url_register = reverse("api:register-list")
    base_url_login = reverse("api:login-list")
    base_url_logout = reverse("api:logout-list")
    base_url_check_session = reverse("api:check-session-list")

    data_register = {"username": "test", "password": "pass", "email": "test@appseed.us"}

    data_login = {"password": "12345678", "email": "teast@admin.com"}

    def test_register(self):
        response = self.client.post(
            f"{self.base_url_register}", data=self.data_register
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response_data = response.json()
        self.assertEqual(response_data["success"], True)

    def test_login(self):
        response = self.client.post(f"{self.base_url_login}", data=self.data_login)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = response.json()
        self.assertEqual(response_data["success"], True)

    def test_logout(self):
        # Login to retrieve token

        response = self.client.post(f"{self.base_url_login}", data=self.data_login)
        response_data = response.json()

        token = response_data["token"]

        self.client.credentials(HTTP_AUTHORIZATION=token)

        # Logout

        response = self.client.post(f"{self.base_url_logout}", data={"token": token})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = response.json()
        self.assertEqual(response_data["success"], True)

    def test_check_session(self):
        # Login to retrieve token

        response = self.client.post(f"{self.base_url_login}", data=self.data_login)
        response_data = response.json()

        token = response_data["token"]

        self.client.credentials(HTTP_AUTHORIZATION=token)

        # Check session
        response = self.client.post(f"{self.base_url_check_session}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_data = response.json()
        self.assertEqual(response_data["success"], True)
