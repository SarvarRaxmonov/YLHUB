from itertools import chain

from rest_framework import generics

from .models import Announcement, News, Poll
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
