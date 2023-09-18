# Generated by Django 4.2.5 on 2023-09-18 00:31

import apps.student_test.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("student_test", "0009_alter_test_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="test",
            name="time",
            field=models.TimeField(
                validators=[apps.student_test.validators.validate_min_duration]
            ),
        ),
    ]