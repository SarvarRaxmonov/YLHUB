from rest_framework import generics, status
from rest_framework.views import Response

from apps.course.models import Course, LessonProgress
from apps.course.serializers import (CourseDetailSerializer,
                                     CourseListSerializer)


class CourseListAPIView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseListSerializer


class CourseDetailAPIView(generics.RetrieveAPIView):
    serializer_class = CourseDetailSerializer
    queryset = Course.objects.all()
    lookup_field = "pk"


class CourseStartAPIView(generics.CreateAPIView):
    def post(self, request, pk, *args, **kwargs):
        try:
            course = Course.objects.get(id=pk)
            first_lesson = course.lessons.first()
            if first_lesson:
                LessonProgress.objects.create(lesson=first_lesson, user=request.user)
                return Response({"message": "Course started successfully."}, status=status.HTTP_201_CREATED)
            else:
                return Response({"message": "No lessons found in this course."}, status=status.HTTP_400_BAD_REQUEST)
        except Course.DoesNotExist:
            return Response({"message": "Course not found."}, status=status.HTTP_404_NOT_FOUND)
