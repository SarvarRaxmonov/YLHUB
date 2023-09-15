from django.urls import path

from apps.notification.views import (
    MarkAllUserNotificationsIsReadAPIView,
    NotificationDetailAPIView,
    NotificationListAPIView,
    UserNotificationIsReadAPIView,
    UserNotificationListAPIView,
)

urlpatterns = [
    path("main/", NotificationListAPIView.as_view(), name="notification_main_list"),
    path("my/", UserNotificationListAPIView.as_view(), name="notification_my_list"),
    path(
        "read-all/",
        MarkAllUserNotificationsIsReadAPIView.as_view(),
        name="notification_read_all_create",
    ),
    path(
        "<int:pk>/detail/",
        NotificationDetailAPIView.as_view(),
        name="notification_detail",
    ),
    path(
        "<int:pk>/read/",
        UserNotificationIsReadAPIView.as_view(),
        name="notification_read_create",
    ),
]
