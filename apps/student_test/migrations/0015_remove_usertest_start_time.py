# Generated by Django 4.2.5 on 2023-09-18 11:29

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("student_test", "0014_alter_useranswer_unique_together"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="usertest",
            name="start_time",
        ),
    ]
