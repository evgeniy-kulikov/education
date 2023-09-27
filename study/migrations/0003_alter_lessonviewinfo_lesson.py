# Generated by Django 4.2.5 on 2023-09-27 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("study", "0002_alter_lessonviewinfo_status_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lessonviewinfo",
            name="lesson",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_query_name="views",
                to="study.lesson",
            ),
        ),
    ]
