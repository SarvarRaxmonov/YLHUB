from django.contrib.auth.models import User
from django.db import models


class Test(models.Model):
    name = models.CharField(max_length=255)
    time = models.DurationField()
    users = models.ManyToManyField(User, through="UserTest")

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.FileField(upload_to="images/")

    def __str__(self):
        return self.image


class Video(models.Model):
    video = models.FileField(upload_to="videos/")

    def __str__(self):
        return self.video


class Variant(models.Model):
    option = models.CharField(max_length=1000)

    def __str__(self):
        return self.option


class TestQuestion(models.Model):
    class QuestionType(models.TextChoices):
        CHOICE_ORDER = "choice_order", "Choice Order"
        MULTI_SELECT = "multi_select", "Multi-Select"
        SINGLE_SELECT = "single_select", "Single-Select"
        TEXT = "text", "Text"

    question = models.CharField(max_length=255)
    images = models.ManyToManyField(Image)
    videos = models.ManyToManyField(Video)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    variants = models.ManyToManyField(Variant)
    is_text_required = models.BooleanField(default=False)
    text_length = models.IntegerField(default=0)
    answer = models.ManyToManyField(Variant, related_name="question_answer")
    type = models.CharField(max_length=20, choices=QuestionType.choices)

    def __str__(self):
        return self.question


class UserAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(TestQuestion, on_delete=models.CASCADE)
    answer = models.TextField()
    selected_variant = models.ManyToManyField(Variant)
    is_true = models.BooleanField()

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
