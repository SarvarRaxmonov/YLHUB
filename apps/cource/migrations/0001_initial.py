# Generated by Django 4.2.5 on 2023-09-14 09:11

import ckeditor_uploader.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, null=True, verbose_name="Created at"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, null=True, verbose_name="Updated at"
                    ),
                ),
                ("title", models.CharField(max_length=250, verbose_name="Title")),
                (
                    "desc",
                    models.TextField(blank=True, null=True, verbose_name="Description"),
                ),
                (
                    "score",
                    models.PositiveIntegerField(
                        blank=True, null=True, verbose_name="Score"
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[("optional", "Optional"), ("mandatory", "Mandatory")],
                        max_length=50,
                        verbose_name="Type",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("choice1", "Choice 1"), ("choice2", "Choice 2")],
                        max_length=50,
                        null=True,
                        verbose_name="Status",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="cource/photos",
                        verbose_name="Image",
                    ),
                ),
                (
                    "duration_days",
                    models.PositiveIntegerField(
                        blank=True, null=True, verbose_name="Duration days"
                    ),
                ),
            ],
            options={
                "verbose_name": "Course",
                "verbose_name_plural": "Courses",
            },
        ),
        migrations.CreateModel(
            name="Language",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, null=True, verbose_name="Created at"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, null=True, verbose_name="Updated at"
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=50, null=True, verbose_name="Language Name"
                    ),
                ),
            ],
            options={
                "verbose_name": "Language",
                "verbose_name_plural": "Languages",
            },
        ),
        migrations.CreateModel(
            name="Lesson",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, null=True, verbose_name="Created at"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, null=True, verbose_name="Updated at"
                    ),
                ),
                ("title", models.CharField(max_length=250, verbose_name="Title")),
                (
                    "desc",
                    models.TextField(blank=True, null=True, verbose_name="Description"),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("video", "Video"),
                            ("task", "Task"),
                            ("exam", "Exam"),
                            ("book", "Book"),
                            ("audiobook", "Audio book"),
                        ],
                        max_length=50,
                        verbose_name="Type",
                    ),
                ),
                ("order", models.PositiveIntegerField(verbose_name="Order")),
                (
                    "course",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="lessons",
                        to="cource.course",
                        verbose_name="Course",
                    ),
                ),
            ],
            options={
                "verbose_name": "Lesson",
                "verbose_name_plural": "Lessons",
            },
        ),
        migrations.CreateModel(
            name="LessonContent",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, null=True, verbose_name="Created at"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, null=True, verbose_name="Updated at"
                    ),
                ),
                (
                    "file",
                    models.FileField(
                        upload_to="lesson_content/",
                        validators=[
                            django.core.validators.FileExtensionValidator(
                                allowed_extensions=["jpg", "jpeg", "png", "gif"],
                                message="Only image files are allowed.",
                            ),
                            django.core.validators.FileExtensionValidator(
                                allowed_extensions=["mp4", "avi", "mkv"],
                                message="Only video files are allowed.",
                            ),
                            django.core.validators.FileExtensionValidator(
                                allowed_extensions=["pdf"],
                                message="Only PDF files are allowed.",
                            ),
                            django.core.validators.FileExtensionValidator(
                                allowed_extensions=["txt"],
                                message="Only text files are allowed.",
                            ),
                        ],
                        verbose_name="File",
                    ),
                ),
                (
                    "text",
                    ckeditor_uploader.fields.RichTextUploadingField(
                        verbose_name="Text"
                    ),
                ),
                (
                    "lesson",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="contents",
                        to="cource.lesson",
                        verbose_name="Lesson",
                    ),
                ),
            ],
            options={
                "verbose_name": "Lesson Content",
                "verbose_name_plural": "Lesson Contents",
            },
        ),
        migrations.AddField(
            model_name="course",
            name="language",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="courses",
                to="cource.language",
                verbose_name="Language",
            ),
        ),
    ]