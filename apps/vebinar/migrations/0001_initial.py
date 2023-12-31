# Generated by Django 4.2.5 on 2023-09-11 13:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="VEBINAR",
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
                ("name", models.CharField(max_length=500, verbose_name="nomi")),
                ("url", models.URLField()),
                ("speaker", models.CharField(max_length=255)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("coming", "Coming"),
                            ("now", "Now"),
                            ("finished", "Finished"),
                        ],
                        default="coming",
                        max_length=10,
                    ),
                ),
                (
                    "thumbnail",
                    models.ImageField(
                        upload_to="thumbnails/", verbose_name="Cover Photo"
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[("seminar", "Seminar"), ("lecture", "Lecture")],
                        default="seminar",
                        max_length=100,
                    ),
                ),
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="UserSearchVebinar",
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
                ("keyword", models.CharField(max_length=500)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Complain",
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
                    "type",
                    models.CharField(
                        choices=[
                            ("zararli yoki noqonuniy", "Zararli yoki noqonuniy"),
                            ("shaxsiy malumot", "Shaxsiy malumot"),
                            ("reklama", "Reklama"),
                            ("haqiqatga mos kelmaydi", "Haqiqatga mos kelmaydi"),
                            ("boshqa", "Boshqa"),
                        ],
                        default="boshqa",
                        max_length=100,
                    ),
                ),
                ("text", models.TextField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "vebinar",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="vebinar.vebinar",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Chat",
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
                ("text", models.TextField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "vebinar",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="vebinar.vebinar",
                    ),
                ),
            ],
        ),
    ]
