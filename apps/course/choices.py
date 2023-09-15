from django.db import models
from django.utils.translation import gettext_lazy as _


class CourceTypeChoices(models.TextChoices):
    optional = "optional", _("Optional")
    mandatory = "mandatory", _("Mandatory")


class LessonTypeChoices(models.TextChoices):
    video = "video", _("Video")
    task = "task", _("Task")
    exam = "exam", _("Exam")
    book = "book", _("Book")
    audiobook = "audiobook", _("Audio book")
