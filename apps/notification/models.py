from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel


class Notification(BaseModel):
    title = models.CharField(max_length=250, null=True, blank=True, verbose_name=_("Title"))
    text = models.TextField(null=True, blank=True, verbose_name=_("Text"))
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=_("Content type"),
    )
    object_id = models.PositiveIntegerField(null=True, blank=True, verbose_name=_("Object id"))
    content_object = GenericForeignKey("content_type", "object_id")

    class Meta:
        verbose_name = _("Notification")
        verbose_name_plural = _("Notifications")


class UserNotification(BaseModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user_notification",
        verbose_name=_("User"),
    )
    notification = models.ForeignKey(
        "notification.Notification",
        on_delete=models.CASCADE,
        related_name="user_notification",
        verbose_name=_("Notification"),
    )
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.notification}"

    class Meta:
        unique_together = ("user", "notification")
        verbose_name = _("User notification")
        verbose_name_plural = _("User notifications")
