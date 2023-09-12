from django.contrib import admin

from apps.user.models import (Document, DocumentName, Profile, SocialNetwork,
                              SocialNetworkName)


@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    list_display = ("id", "full_name")


@admin.register(SocialNetworkName)
class AdminSocialNetworkName(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(SocialNetwork)
class AdminSocialNetwork(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(DocumentName)
class AdminDocumentName(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Document)
class AdminDocument(admin.ModelAdmin):
    list_display = ("id", "name")
