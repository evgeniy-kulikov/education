from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    teacher = models.BooleanField(default=False, verbose_name='роль "Преподаватель"')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
