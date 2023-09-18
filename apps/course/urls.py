from django.urls import path

from apps.course.views import (CourseDetailAPIView, CourseListAPIView,
                               CourseStartAPIView)

urlpatterns = [
    path("list/", CourseListAPIView.as_view(), name="course_list"),
    path("<int:pk>/detail/", CourseDetailAPIView.as_view(), name="course_detail"),
    path("<int:pk>/start/", CourseStartAPIView.as_view(), name="course_start"),
]
