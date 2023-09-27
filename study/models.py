from django.db import models
from catalog.models import Product
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

# Урок
class Lesson(models.Model):
    title = models.CharField(max_length=128)
    video_url = models.URLField()
    video_duration = models.IntegerField(default=0)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return f'{self.title}: {self.products}'



class LessonStatusEnum(models.TextChoices):
    VIEWED = 'VIEWED', 'Просмотрено'
    NUT_VIEWED = 'NUT_VIEWED', 'Не просмотрено'



class LessonViewInfo(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='views')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(choices=LessonStatusEnum.choices, default=LessonStatusEnum.NUT_VIEWED, max_length=32)
    view_time = models.IntegerField(default=0)
    last_view_datatime = models.DateTimeField(default=datetime.now())

    class Meta:
        unique_together = ('lesson', 'user')  # ставим условие: 'user' смотрит 'lesson' только один раз

    def __str__(self):
        return f'{self.lesson}: {self.view_time}'
