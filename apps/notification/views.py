from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.notification.models import Notification, UserNotification
from apps.notification.serializers import (
    NotificationSerializer,
    UserNotificationListSerializer,
)


class NotificationListAPIView(generics.ListAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer


class UserNotificationListAPIView(generics.ListAPIView):
    serializer_class = UserNotificationListSerializer

    def get_queryset(self):
        return UserNotification.objects.filter(user=self.request.user)


class MarkAllUserNotificationsIsReadAPIView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        user = request.user
        UserNotification.objects.filter(user=user, is_read=False).update(is_read=True)
        return Response(
            {"message": "All notifications marked as read."}, status=status.HTTP_200_OK
        )


class NotificationDetailAPIView(generics.RetrieveAPIView):
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()
    lookup_field = "pk"


class UserNotificationIsReadAPIView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, pk):
        user = request.user
        try:
            notification = UserNotification.objects.get(
                user=user, notification_id=pk, is_read=False
            )
            notification.is_read = True
            notification.save()
            return Response(
                {"message": "Notification marked as read."}, status=status.HTTP_200_OK
            )
        except UserNotification.DoesNotExist:
            return Response(
                {"message": "Notification not found or already marked as read."},
                status=status.HTTP_404_NOT_FOUND,
            )
