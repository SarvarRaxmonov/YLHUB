from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.core.validators import (
    FileExtensionValidator,
    MaxValueValidator,
    MinValueValidator,
)
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel
from apps.course.choices import CourceTypeChoices, LessonTypeChoices


class Language(BaseModel):
    name = models.CharField(max_length=50, null=True, verbose_name=_("Language Name"))

    class Meta:
        verbose_name = _("Language")
        verbose_name_plural = _("Languages")

    def __str__(self):
        return self.name


class Category(BaseModel):
    name = models.CharField(max_length=50, null=True, verbose_name=_("Language Name"))

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name


class Course(BaseModel):
    title = models.CharField(max_length=250, verbose_name=_("Title"))
    desc = models.TextField(null=True, blank=True, verbose_name=_("Description"))
    score = models.PositiveIntegerField(null=True, blank=True, verbose_name=_("Score"))
    language = models.ForeignKey(
        "course.Language",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="courses",
        verbose_name=_("Language"),
    )
    category = models.ForeignKey(
        "course.Category",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="courses",
        verbose_name=_("Category"),
    )
    type = models.CharField(
        max_length=50, choices=CourceTypeChoices.choices, verbose_name=_("Type")
    )
    image = models.ImageField(
        upload_to="course/photos", null=True, blank=True, verbose_name=_("Image")
    )
    duration_days = models.PositiveIntegerField(
        null=True, blank=True, verbose_name=_("Duration days")
    )

    class Meta:
        verbose_name = _("Course")
        verbose_name_plural = _("Courses")

    def __str__(self):
        return self.title


class Lesson(BaseModel):
    title = models.CharField(max_length=250, verbose_name=_("Title"))
    desc = models.TextField(null=True, blank=True, verbose_name=_("Description"))
    course = models.ForeignKey(
        "course.Course",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="lessons",
        verbose_name="Course",
    )
    type = models.CharField(
        max_length=50, choices=LessonTypeChoices.choices, verbose_name=_("Type")
    )
    order = models.PositiveIntegerField(verbose_name=_("Order"))

    class Meta:
        verbose_name = _("Lesson")
        verbose_name_plural = _("Lessons")

    def __str__(self):
        return self.title


class LessonContent(BaseModel):
    lesson = models.ForeignKey(
        "course.Lesson",
        on_delete=models.CASCADE,
        related_name="contents",
        verbose_name=_("Lesson"),
    )
    file = models.FileField(
        upload_to="lesson_content/",
        verbose_name=_("File"),
        null=True,
        blank=True,
        validators=[
            FileExtensionValidator(
                allowed_extensions=[
                    "jpg",
                    "jpeg",
                    "png",
                    "gif",
                    "mp4",
                    "avi",
                    "mkv",
                    "pdf",
                    "mp3",
                ],
            )
        ],
    )

    text = RichTextUploadingField(null=True, blank=True, verbose_name=_("Text"))

    class Meta:
        verbose_name = _("Lesson Content")
        verbose_name_plural = _("Lesson Contents")

    def __str__(self):
        return self.lesson.title


class LessonProgress(BaseModel):
    lesson = models.ForeignKey(
        "course.Lesson",
        on_delete=models.CASCADE,
        related_name="lesson_progress",
        verbose_name=_("Lesson"),
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="lesson_progress",
        verbose_name=_("User"),
    )
    is_started = models.BooleanField(verbose_name=_("lesson is started"), default=False)
    percentage = models.FloatField(verbose_name=_("progress percentage"), default=0)
    is_completed = models.BooleanField(
        verbose_name=_("lesson is completed"), default=False
    )

    class Meta:
        unique_together = ("lesson", "user")
        verbose_name = _("lesson progress")
        verbose_name_plural = _("lesson progress")


class CourseReview(BaseModel):
    course = models.ForeignKey(
        "course.Course",
        verbose_name=_("Course"),
        on_delete=models.CASCADE,
        related_name="reviews",
    )
    user = models.ForeignKey(
        User, verbose_name=_("User"), on_delete=models.CASCADE, related_name="reviews"
    )
    comment = models.TextField(verbose_name=_("Comment"))
    rating = models.PositiveIntegerField(
        verbose_name=_("Rating"),
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(5)],
    )

    class Meta:
        unique_together = ("course", "user")

    def __str__(self):
        return f"{self.user} - {self.course}"
