# Generated by Django 4.2.5 on 2023-09-14 10:47

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("notification", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="usernotification",
            options={
                "verbose_name": "User notification",
                "verbose_name_plural": "User notifications",
            },
        ),
    ]
