from rest_framework import status
from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.vebinar.filters import VebinarFilter
from apps.vebinar.models import Complain, UserSearchVebinar, Vebinar
from apps.vebinar.permisions import IsUserOwner
from apps.vebinar.serializers import ComplainSerializer, UserSearchVebinarSerializer, VebinarSerializer


class VebinarListView(ListAPIView):
    queryset = Vebinar.objects.all()
    serializer_class = VebinarSerializer
    filterset_class = VebinarFilter
    permission_classes = (IsAuthenticated,)


class VebinarDetailView(RetrieveAPIView):
    queryset = Vebinar.objects.all()
    serializer_class = VebinarSerializer
    permission_classes = (IsAuthenticated,)


class ComplainCreateView(CreateAPIView):
    queryset = Complain.objects.all()
    serializer_class = ComplainSerializer
    permission_classes = (IsUserOwner,)


class UserVebinarSearchHistoryView(ListAPIView):
    queryset = UserSearchVebinar.objects.all()
    serializer_class = UserSearchVebinarSerializer
    permission_classes = (IsUserOwner,)
    lookup_field = "user_id"

    def get(self, request, user_id=None, *args, **kwargs):
        obj = self.get_queryset().filter(user=user_id).order_by("-id")[:7]
        serializer = self.get_serializer(obj, many=True)
        return Response(serializer.data)


class UserVebinarSearchHistoryDeleteView(DestroyAPIView):
    queryset = UserSearchVebinar.objects.all()
    serializer_class = UserSearchVebinarSerializer
    permission_classes = (IsUserOwner,)
    lookup_field = "user_id"

    def destroy(self, request, user_id=None, *args, **kwargs):
        deleted_count, _ = self.get_queryset().filter(user=user_id).delete()
        if deleted_count > 0:
            return Response(
                {"message": f"Deleted {deleted_count} keywords for device {user_id}"},
                status=status.HTTP_204_NO_CONTENT,
            )
        else:
            return Response(
                {"message": f"No keywords found for device {user_id}"},
                status=status.HTTP_404_NOT_FOUND,
            )
