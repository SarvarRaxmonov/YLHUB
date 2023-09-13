from django.contrib import admin

from apps.main.models import (Announcement, Category, News, Poll, PollChoice,
                              UserChoice)


@admin.register(News)
class AdminNews(admin.ModelAdmin):
    list_display = ("id", "title")


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Announcement)
class AdminAnnouncement(admin.ModelAdmin):
    list_display = ("id", "title")


@admin.register(Poll)
class AdminPoll(admin.ModelAdmin):
    list_display = ("id", "title")


@admin.register(PollChoice)
class AdminPollChoice(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(UserChoice)
class AdminUserChoice(admin.ModelAdmin):
    list_display = ("id", "user")
