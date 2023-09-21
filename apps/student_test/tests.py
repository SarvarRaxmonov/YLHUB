from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from apps.common.models import TemporaryUser
from apps.student_test.models import (
    Test,
    Subject,
    TestQuestion,
    Variant,
    UserTest,
    UserAnswer,
)
from rest_framework.test import APITestCase
from django.utils import timezone


class TestDetailViewSetTest(APITestCase):
    def setUp(self):
        subject = Subject.objects.create(name="A")
        self.time_duration = timezone.timedelta(minutes=12)
        self.question = TestQuestion.objects.create(
            question="hi ?", type="single_select", subject=subject
        )
        self.test = Test.objects.create(
            name="Test Name",
            questions=1,
            time=self.time_duration,
            subject=subject,
            resubmit_attempt_count=2,
            point=10,
        )
        self.new_user = User.objects.create_user(
            username="username 1", password="qwertyui2004?>?8"
        )
        TemporaryUser.objects.create(user=self.new_user)
        self.user_test = UserTest.objects.create(
            user=self.new_user,
            test=self.test,
            start_time=timezone.now(),
            end_time=timezone.now() + self.time_duration,
        )
        self.variant = Variant.objects.create(
            question=self.question, option="A bsj ", is_true=True, order=1
        )
        self.variant_2 = Variant.objects.create(
            question=self.question, option="B bsj ", is_true=False, order=2
        )

    def test_detail_of_test(self):
        self.client.force_login(self.new_user)
        url = reverse("test-detail", kwargs={"pk": self.test.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_question_detail(self):
        self.client.force_login(self.new_user)
        url = reverse("test-question-detail", kwargs={"pk": self.question.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_start_test(self):
        new_user_2 = User.objects.create_user(
            username="username 2", password="qwertyui2004?>?8"
        )
        self.client.force_login(new_user_2)
        url = reverse("start-test")
        data = {
            "test": self.test.id,
            "start_time": timezone.now().strftime("%Y-%m-%dT%H:%M"),
            "end_time": (timezone.now() + self.time_duration).strftime(
                "%Y-%m-%dT%H:%M"
            ),
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_answer_create(self):
        self.client.force_login(self.new_user)
        url = reverse("answer")
        data = {
            "user_test": self.user_test.id,
            "question": self.question.id,
            "selected_variant": [self.variant.id],
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_answer_update(self):
        user_answer = UserAnswer.objects.create(
            user_test=self.user_test, question=self.question
        )
        user_answer.selected_variant.add(self.variant)
        self.client.force_login(self.new_user)
        url = reverse("answer-update", kwargs={"pk": user_answer.id})
        data = {
            "user_test": self.user_test.id,
            "question": self.question.id,
            "selected_variant": [self.variant_2.id],
        }
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_finish_and_get_result(self):
        user_answer = UserAnswer.objects.create(
            user_test=self.user_test, question=self.question, is_true=True
        )
        user_answer.selected_variant.add(self.variant)
        self.client.force_login(self.new_user)
        url = reverse("finish-test", kwargs={"user_test_id": self.user_test.id})
        response = self.client.post(url)
        url_2 = reverse("result-test", kwargs={"id": self.user_test.id})
        response_2 = self.client.get(url_2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_2.status_code, status.HTTP_200_OK)
