from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.vebinar.models import UserSearchVebinar, Vebinar


class VebinarListViewTest(APITestCase):
    def setUp(self):
        jpg_content = b"Binary content of your MP4 file here"
        uploaded_jpg = SimpleUploadedFile("image.jpg", jpg_content, content_type="image/jpg")
        self.new_user = User.objects.create_user(username="username", password="Password2004?")
        self.vebinar1 = Vebinar.objects.create(
            name="example 1",
            url="https://www.netflix.com/uz/",
            speaker="example",
            status="now",
            thumbnail=uploaded_jpg,
            type="lecture",
            description="examples",
        )

    def test_vebinar_view(self):
        self.client.force_login(self.new_user)
        url = reverse("vebinar-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)

    def test_vebinar_detail(self):
        self.client.force_login(self.new_user)
        response = self.client.get(reverse("vebinar-detail", kwargs={"pk": self.vebinar1.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_complain_create(self):
        self.client.force_login(self.new_user)
        url = reverse("complain-create")
        data = {
            "user": self.new_user.id,
            "vebinar": self.vebinar1.id,
            "type": "zararli yoki noqonuniy",
            "text": "example 1",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class SearchViewTest(APITestCase):
    def setUp(self):
        self.new_user = User.objects.create_user(username="username", password="Password2004?")
        self.search_1 = UserSearchVebinar.objects.create(user=self.new_user, keyword="example")

    def test_search_history(self):
        self.client.force_login(self.new_user)
        response = self.client.get(reverse("search-history", kwargs={"user_id": self.search_1.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_search_history(self):
        self.client.force_login(self.new_user)
        response = self.client.delete(reverse("search-history-delete", kwargs={"user_id": self.search_1.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
