# Generated by Django 4.2.5 on 2023-09-11 16:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("library", "0005_alter_audiobook_options_alter_book_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="audiobook",
            name="cover",
            field=models.ImageField(upload_to=""),
        ),
        migrations.AlterField(
            model_name="book",
            name="cover",
            field=models.ImageField(upload_to=""),
        ),
    ]