from django.contrib import admin

from .models import Media, Test, TestQuestion, UserAnswer, UserTest, Variant



@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Variant)
class VariantAdmin(admin.ModelAdmin):
    list_display = ("option",)


@admin.register(TestQuestion)
class TestQuestionAdmin(admin.ModelAdmin):
    list_display = ("question", "test", "type")


@admin.register(Media)
class TestMediaAdmin(admin.ModelAdmin):
    list_display = ("file", "type")


@admin.register(UserAnswer)
class UserAnswerAdmin(admin.ModelAdmin):
    list_display = ("user_test", "question", "is_true")


@admin.register(UserTest)
class UserTestAdmin(admin.ModelAdmin):
    list_display = ("user", "test", "is_finished")
