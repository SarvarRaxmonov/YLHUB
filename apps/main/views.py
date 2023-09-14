from itertools import chain

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Announcement, News, Poll, PollChoice, UserChoice
from .serializers import (AnnouncementDetailSerializer, NewsDetailSerializer,
                          NewsSerializer, PollDetailSerializer)


class ContentAPIView(generics.ListAPIView):
    serializer_class = NewsSerializer

    def get_queryset(self):
        news = News.objects.all()
        announcement = Announcement.objects.all()
        poll = Poll.objects.all()

        combine = list(chain(news, announcement, poll))
        sorted_data = sorted(combine, key=lambda item: item.created_at, reverse=True)

        return sorted_data


class ContentDetailAPIView(generics.RetrieveAPIView):
    queryset = None
    serializer_class = None

    def get_queryset(self):
        model_type = self.kwargs.get("model_type")
        pk = self.kwargs.get("pk")

        if model_type.lower() == "news":
            self.queryset = News.objects.filter(pk=pk)
            self.serializer_class = NewsDetailSerializer
        elif model_type.lower() == "announcement":
            self.queryset = Announcement.objects.filter(pk=pk)
            self.serializer_class = AnnouncementDetailSerializer
        elif model_type.lower() == "poll":
            self.queryset = Poll.objects.filter(pk=pk)
            self.serializer_class = PollDetailSerializer
        return super().get_queryset()


class CreateChoiceAPIView(APIView):
    def post(self, request, pk):

        try:
            curr_choice = PollChoice.objects.get(id=pk)
            poll = curr_choice.poll
            for choice in poll.choices.all():
                if choice.user_choice.filter(user=request.user).exists():
                    return Response({"message": "You can only answer once."}, status=status.HTTP_400_BAD_REQUEST)
            UserChoice.objects.create(user=request.user, choice_id=pk)
            return Response({"message": "Poll choice created successfully"}, status=status.HTTP_201_CREATED)
        except PollChoice.DoesNotExist:
            return Response({"message": "Poll Choice does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"message": f"{e}"}, status=status.HTTP_400_BAD_REQUEST)
