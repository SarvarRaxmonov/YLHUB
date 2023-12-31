# Generated by Django 4.2.5 on 2023-09-12 10:05

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
            name="DocumentName",
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
                ("name", models.CharField(max_length=128, verbose_name="Name")),
            ],
            options={
                "verbose_name": "Document name",
                "verbose_name_plural": "Document names",
            },
        ),
        migrations.CreateModel(
            name="Profile",
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
                    "jshshir",
                    models.IntegerField(
                        blank=True, max_length=14, null=True, verbose_name="Jshshir"
                    ),
                ),
                (
                    "password_seria",
                    models.CharField(
                        blank=True,
                        max_length=9,
                        null=True,
                        verbose_name="Password Seria",
                    ),
                ),
                (
                    "birth_date",
                    models.DateField(blank=True, null=True, verbose_name="Birth Date"),
                ),
                (
                    "nation",
                    models.CharField(
                        blank=True, max_length=32, null=True, verbose_name="Nation"
                    ),
                ),
                (
                    "education",
                    models.CharField(
                        blank=True, max_length=32, null=True, verbose_name="Education"
                    ),
                ),
                (
                    "education_place",
                    models.CharField(
                        blank=True,
                        max_length=256,
                        null=True,
                        verbose_name="Education place",
                    ),
                ),
                (
                    "work_place",
                    models.CharField(
                        blank=True, max_length=256, null=True, verbose_name="Work place"
                    ),
                ),
                (
                    "position",
                    models.CharField(
                        blank=True, max_length=128, null=True, verbose_name="Position"
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="users/photo",
                        verbose_name="Image",
                    ),
                ),
                ("score", models.IntegerField(default=0, verbose_name="Score")),
                ("kpi", models.IntegerField(default=0, verbose_name="KPI")),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_profile",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="User",
                    ),
                ),
            ],
            options={
                "verbose_name": "Profile",
                "verbose_name_plural": "Profiles",
            },
        ),
        migrations.CreateModel(
            name="SocialNetworkName",
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
                ("name", models.CharField(max_length=128, verbose_name="Name")),
                (
                    "icon",
                    models.ImageField(
                        blank=True, null=True, upload_to="users/social_network/icon"
                    ),
                ),
            ],
            options={
                "verbose_name": "Social Network Name",
                "verbose_name_plural": "Social Network Names",
            },
        ),
        migrations.CreateModel(
            name="SocialNetwork",
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
                ("link", models.CharField(verbose_name="Link")),
                (
                    "name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="social_network",
                        to="user.socialnetworkname",
                        verbose_name="Social Network Name",
                    ),
                ),
                (
                    "profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="social_network",
                        to="user.profile",
                        verbose_name="Profile",
                    ),
                ),
            ],
            options={
                "verbose_name": "Social Network",
                "verbose_name_plural": "Social Networks",
            },
        ),
        migrations.CreateModel(
            name="Document",
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
                        blank=True,
                        null=True,
                        upload_to="users/documents",
                        verbose_name="File",
                    ),
                ),
                (
                    "name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="documents",
                        to="user.documentname",
                        verbose_name="Name",
                    ),
                ),
                (
                    "profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="documents",
                        to="user.profile",
                        verbose_name="Profile",
                    ),
                ),
            ],
            options={
                "verbose_name": "Document",
                "verbose_name_plural": "Documents",
            },
        ),
    ]
