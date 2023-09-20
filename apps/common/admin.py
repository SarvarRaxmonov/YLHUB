from django.contrib import admin
from apps.common.models import TemporaryUser


@admin.register(TemporaryUser)
class TestAdmin(admin.ModelAdmin):
    list_display = ("user", "point")
