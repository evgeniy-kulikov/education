# Generated by Django 4.2.5 on 2023-09-23 08:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        (
            "courses",
            "0005_alter_students_options_rename_owner_product_creator_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="students",
            name="access",
            field=models.BooleanField(default=False, verbose_name="Доступ к курсу"),
        ),
        migrations.AlterField(
            model_name="lesson",
            name="products",
            field=models.ManyToManyField(
                related_name="lessons",
                to="courses.product",
                verbose_name="Название курса",
            ),
        ),
        migrations.AlterField(
            model_name="students",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="students",
                to="courses.product",
                verbose_name="Курс",
            ),
        ),
    ]
