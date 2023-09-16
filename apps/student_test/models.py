from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext as _


class Test(models.Model):
    name = models.CharField(max_length=255)
    time = models.DurationField()
    # course = models.ForeignKey(Course, on_delete=models.CASCADE)
    resumbit_attempt_count = models.IntegerField(default=0)
    questions = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class TestQuestion(models.Model):
    class QuestionType(models.TextChoices):
        CHOICE_ORDER = "choice_order", "Choice Order"
        MULTI_SELECT = "multi_select", "Multi-Select"
        SINGLE_SELECT = "single_select", "Single-Select"

    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    question = models.TextField()
    type = models.CharField(max_length=20, choices=QuestionType.choices)

    def __str__(self):
        return self.question


class Media(models.Model):
    file = models.FileField(upload_to="test/files/")
    test_question = models.ForeignKey(TestQuestion, on_delete=models.CASCADE, verbose_name=_("Savolni tanlang"))
    type = models.CharField(max_length=255, choices=[("image", "image"), ("video", "video")])


class Variant(models.Model):
    question = models.ForeignKey(TestQuestion, on_delete=models.CASCADE, verbose_name=_("Savolni tanlang"))
    option = models.CharField(max_length=1000)
    order = models.PositiveIntegerField()
    is_true = models.BooleanField(default=False)

    def __str__(self):
        return self.question


class UserTest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_finished = models.BooleanField(default=False)

    def __str__(self):
        return f"Test : {self.test.name} , Student : {self.user.username}"


class UserAnswer(models.Model):
    user_test = models.ForeignKey(UserTest, on_delete=models.CASCADE)
    question = models.ForeignKey(TestQuestion, on_delete=models.CASCADE)
    selected_variant = models.ManyToManyField(Variant)
    is_true = models.BooleanField(default=False)
