from django.contrib import admin
from study import models as study_models
# Register your models here.


@admin.register(study_models.Lesson)
class ProductAccessAdmin(admin.ModelAdmin):
    list_display = ['title', 'video_durution' , 'video_url']
    filter_horizontal = 'products',



@admin.register(study_models.LessonViewInfo)
class LessonViewInfoAdmin(admin.ModelAdmin):
    list_display = ['lesson', 'user', 'status', 'view_time']