from django.contrib import admin

from .models import Chat, Complain, UserSearchVebinar, Vebinar


@admin.register(Vebinar)
class VEBINARAdmin(admin.ModelAdmin):
    list_display = ("name", "status")


@admin.register(UserSearchVebinar)
class UserSearchVebinarAdmin(admin.ModelAdmin):
    list_display = ("user", "keyword")


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ("user", "vebinar", "text")


@admin.register(Complain)
class ComplainAdmin(admin.ModelAdmin):
    list_display = ("user", "vebinar", "type", "text")
