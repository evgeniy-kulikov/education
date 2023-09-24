from django.contrib import admin
from courses import models as courses_models

# Register your models here.

# admin.site.register(courses_models.Lesson)
# admin.site.register(courses_models.Product)
# admin.site.register(courses_models.Progress)
# admin.site.register(courses_models.Students)

@admin.register(courses_models.Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'link', 'duration']
    filter_horizontal = 'products',


@admin.register(courses_models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(courses_models.Progress)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["lesson", "user", "viewed_time", "time_updated", "view_status"]

@admin.register(courses_models.Students)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["user", "product", "access"]
    list_editable = ("access",)
    ordering = 'product',

