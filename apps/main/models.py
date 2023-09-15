from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=250, verbose_name=_("Name"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")


class News(BaseModel):
    title = models.CharField(max_length=250, null=True, verbose_name=_("Title"))
    image = models.ImageField(upload_to="main/blog", null=True, blank=True, verbose_name=_("Image"))
    category = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_("Category"),
    )
    content = RichTextUploadingField(verbose_name=_("Content"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("News")
        verbose_name_plural = _("News")


class Announcement(BaseModel):
    title = models.CharField(max_length=250, null=True, verbose_name=_("Title"))
    image = models.ImageField(upload_to="main/announcement", null=True, blank=True, verbose_name=_("Image"))
    location = models.CharField(max_length=250, null=True, blank=True, verbose_name=_("Location"))
    date = models.DateTimeField(null=True, blank=True, verbose_name=_("Date"))
    content = RichTextUploadingField(verbose_name=_("Content"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Announcement")
        verbose_name_plural = _("Announcements")


class Poll(BaseModel):
    title = models.CharField(max_length=250, null=True, verbose_name=_("Title"))
    image = models.ImageField(upload_to="main/poll", null=True, blank=True, verbose_name=_("Image"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Poll")
        verbose_name_plural = _("Polls")


class PollChoice(BaseModel):
    name = models.CharField(max_length=250, null=True, verbose_name=_("Name"))
    poll = models.ForeignKey(
        "main.Poll",
        on_delete=models.CASCADE,
        related_name="choices",
        verbose_name=_("Poll"),
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Poll Choice")
        verbose_name_plural = _("Poll Choices")


class UserChoice(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="choices", verbose_name=_("User"))
    choice = models.ForeignKey(
        "main.PollChoice",
        on_delete=models.CASCADE,
        related_name="user_choice",
        verbose_name=_("Choice"),
    )

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ("user", "choice")
        verbose_name = _("User Choice")
        verbose_name_plural = _("User Choices")
