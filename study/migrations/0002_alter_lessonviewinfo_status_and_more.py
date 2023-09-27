# Generated by Django 4.2.5 on 2023-09-27 07:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("study", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lessonviewinfo",
            name="status",
            field=models.CharField(
                choices=[("VIEWED", "Просмотрено"), ("NUT_VIEWED", "Не просмотрено")],
                default="NUT_VIEWED",
                max_length=32,
            ),
        ),
        migrations.AlterUniqueTogether(
            name="lessonviewinfo",
            unique_together={("lesson", "user")},
        ),
    ]