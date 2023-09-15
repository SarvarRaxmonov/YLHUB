from django.contrib import admin

from .models import Image, Test, TestQuestion, UserAnswer, UserTest, Variant, Video


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("image",)


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ("video",)


@admin.register(Variant)
class VariantAdmin(admin.ModelAdmin):
    list_display = ("option",)


@admin.register(TestQuestion)
class TestQuestionAdmin(admin.ModelAdmin):
    list_display = ("question", "test", "type")


@admin.register(UserAnswer)
class UserAnswerAdmin(admin.ModelAdmin):
    list_display = ("user", "question", "is_true")


@admin.register(UserTest)
class UserTestAdmin(admin.ModelAdmin):
    list_display = ("user", "test", "is_finished")
