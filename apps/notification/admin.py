from django.contrib import admin

from apps.notification.models import Notification, UserNotification


@admin.register(Notification)
class AdminNotification(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "text",
        "content_type",
        "object_id",
        "content_object",
    )
    readonly_fields = ("content_object",)


@admin.register(UserNotification)
class AdminUserNotification(admin.ModelAdmin):
    list_display = ("id",)
