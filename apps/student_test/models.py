from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import Q
from django.utils.translation import gettext as _
from datetime import timedelta
from apps.student_test.validators import validate_min_duration


class Subject(models.Model):
    name = models.CharField(_("Name"), max_length=800)

    def __str__(self):
        return self.name


class Test(models.Model):
    name = models.CharField(max_length=255)
    time = models.DurationField(validators=[validate_min_duration])
    # course = models.ForeignKey(Course, on_delete=models.CASCADE) # for future releases of yl_hub
    resubmit_attempt_count = models.IntegerField(default=0)
    point = models.BigIntegerField(_("Berilgan Ball"), default=0)
    is_required = models.BooleanField(_("Majburiymi "), default=True)
    questions = models.IntegerField(default=1, validators=[MinValueValidator(1)])
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def clean(self):
        test_questions_to_update = TestQuestion.objects.filter(
            Q(Q(test__isnull=True) | Q(test=self.id)), subject=self.subject.id
        )
        test = Test.objects.filter(id=self.id).first()
        if self.questions > test_questions_to_update.count():
            raise ValidationError(
                _(
                    "%(value)s is greater than the number of questions in Test Questions, please "
                    "create a new test questions in a %(subject)s subject "
                ),
                params={"value": self.questions, "subject": self.subject.name},
            )
        elif test and test.subject != self.subject:
            raise ValidationError("You can not change test subject after creation ")

    def save(self, *args, **kwargs):
        total_seconds = self.time.total_seconds()
        hours, remainder = divmod(total_seconds, 3600)
        minutes, _ = divmod(remainder, 60)
        modified_duration = timedelta(hours=hours, minutes=minutes)
        self.time = modified_duration
        super().save(*args, **kwargs)


class TestQuestion(models.Model):
    class QuestionType(models.TextChoices):
        CHOICE_ORDER = "choice_order", "Choice Order"
        MULTI_SELECT = "multi_select", "Multi-Select"
        SINGLE_SELECT = "single_select", "Single-Select"

    test = models.ForeignKey(
        Test,
        on_delete=models.CASCADE,
        related_name="question_to_test",
        blank=True,
        null=True,
    )
    question = models.TextField()
    type = models.CharField(max_length=20, choices=QuestionType.choices)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.question

    def clean(self):
        if self.test and self.test.subject != self.subject:
            raise ValidationError(
                _(
                    "%(test)s test and question must be in same subject not different ones , please follow the rules of "
                    "subject changes . Change it ' %(question_subject)s ' to %(test_subject)s ."
                ),
                params={
                    "test": self.test.name,
                    "question_subject": self.subject.name,
                    "test_subject": self.test.subject.name,
                },
            )


class Media(models.Model):
    file = models.FileField(upload_to="test/files/")
    test_question = models.ForeignKey(
        TestQuestion, on_delete=models.CASCADE, verbose_name=_("Savolni tanlang")
    )
    type = models.CharField(
        max_length=255, choices=[("image", "image"), ("video", "video")]
    )
    order = models.PositiveIntegerField()


class Variant(models.Model):
    question = models.ForeignKey(
        TestQuestion,
        on_delete=models.CASCADE,
        related_name="variants_to_question",
        verbose_name=_("Savolni tanlang"),
    )
    option = models.CharField(max_length=1000)
    order = models.PositiveIntegerField(blank=True, default=0)
    is_true = models.BooleanField(default=False)

    class Meta:
        unique_together = ("question", "order")

    def __str__(self):
        return self.option

    def save(self, *args, **kwargs):
        if self.question.type == "choice_order":
            self.is_true = True
        super().save(*args, **kwargs)

    def clean(self):
        if self.question.type == "choice_order" and 0 >= self.order:
            raise ValidationError(
                _(
                    "Current chosen question type is Choice Order, you can not set order to 0 , "
                    "please provide a number to order field ."
                ),
            )


class UserTest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(
        Test, on_delete=models.CASCADE, related_name="user_test_to_test"
    )
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_finished = models.BooleanField(default=False)

    def __str__(self):
        return f"Test : {self.test.name} , Student : {self.user.username}"


class UserAnswer(models.Model):
    user_test = models.ForeignKey(
        UserTest, on_delete=models.CASCADE, related_name="user_answer_to_user_test"
    )
    question = models.ForeignKey(TestQuestion, on_delete=models.CASCADE)
    selected_variant = models.ManyToManyField(Variant)
    is_true = models.BooleanField(default=False)

    class Meta:
        unique_together = ("user_test", "question")

    def __str__(self):
        return f"{self.user_test.user.username} {self.question}"
