# Generated by Django 4.2.5 on 2023-09-19 18:42

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        (
            "student_test",
            "0022_rename_resumbit_attempt_count_test_resubmit_attempt_count",
        ),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="variant",
            unique_together={("question", "order")},
        ),
    ]
