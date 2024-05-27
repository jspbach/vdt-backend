from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from .models import Member


class MemberViewSetTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.member = Member.objects.create(
            full_name="Test User", gender="Nam", institution="Test Institution"
        )

    def test_list(self):
        response = self.client.get(reverse("members-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create(self):
        data = {
            "full_name": "New User",
            "gender": "Nữ",
            "institution": "New Institution",
        }
        response = self.client.post(reverse("members-list"), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve(self):
        response = self.client.get(
            reverse("members-detail", kwargs={"unique_id": self.member.unique_id})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update(self):
        data = {
            "full_name": "Updated User",
            "gender": "NB",
            "institution": "Updated Institution",
        }
        response = self.client.put(
            reverse("members-detail", kwargs={"unique_id": self.member.unique_id}), data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_destroy(self):
        response = self.client.delete(
            reverse("members-detail", kwargs={"unique_id": self.member.unique_id})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
