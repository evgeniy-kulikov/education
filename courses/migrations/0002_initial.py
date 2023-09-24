# Generated by Django 4.2.5 on 2023-09-21 19:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("courses", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="owner",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="lessonview",
            name="lesson",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="courses.lesson",
                verbose_name="Урок",
            ),
        ),
        migrations.AddField(
            model_name="lessonview",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Зритель",
            ),
        ),
        migrations.AddField(
            model_name="lesson",
            name="products",
            field=models.ManyToManyField(related_name="lessons", to="courses.product"),
        ),
    ]