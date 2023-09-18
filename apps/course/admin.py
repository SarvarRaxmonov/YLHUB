from django.contrib import admin

from apps.course.models import (Category, Course, CourseReview, Language,
                                Lesson, LessonContent, LessonProgress)


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Course)
class AdminCourse(admin.ModelAdmin):
    list_display = ("id", "title")


@admin.register(Lesson)
class AdminLesson(admin.ModelAdmin):
    list_display = ("id", "title", "order")


@admin.register(LessonContent)
class AdminLessonContent(admin.ModelAdmin):
    list_display = ("id", "lesson")


@admin.register(Language)
class AdminLanguage(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(LessonProgress)
class AdminLessonProgress(admin.ModelAdmin):
    list_display = ("id", "user", "is_started", "percentage", "is_completed")


@admin.register(CourseReview)
class AdminCourseReview(admin.ModelAdmin):
    list_display = ("id", "course", "user", "rating")
