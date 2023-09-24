from django.db import models
from users.models import User


class Product(models.Model):
    """ Продукт (курс) """
    name = models.CharField(max_length=256, verbose_name='Название курса')
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products', verbose_name='Автор курса')
    student = models.ManyToManyField(User, blank=True, through='Students', verbose_name='Студент')

    def __str__(self):
        return f'Курс: {self.name} - Автор курса: {self.creator}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    """ Урок (лекция) """
    title = models.CharField(max_length=256, verbose_name='Название урока')
    link = models.URLField(verbose_name='Ссылка на видеоресурс')
    duration = models.PositiveIntegerField(verbose_name='Длительность видео (сек.)')
    products = models.ManyToManyField('Product', related_name='lessons', verbose_name='Название курса')

    def __str__(self):
        return f'Урок: {self.title}'

    class Meta:
        verbose_name = 'Лекция'
        verbose_name_plural = 'Лекциии'


class Students(models.Model):
    """  Студенты курсов (записанные, + имеющие доступ)"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Студент')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='students', verbose_name='Курс')
    access = models.BooleanField(default=False, verbose_name='Доступ к курсу')

    def __str__(self):
        return f'Студент: {self.user} записан на: {self.product}'

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'


class Progress(models.Model):
    """ Контроль просмотра уроков пользователями """

    class Status(models.TextChoices):
        not_viewed = 'N', 'Не просмотрено'
        viewed = 'Y', 'Просмотрено'

    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='Урок')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Ученик')
    viewed_time = models.PositiveIntegerField(default=0, verbose_name='Просмотрено (сек.)')
    view_status = models.TextField(choices=Status.choices, default=Status.not_viewed, verbose_name='Статус просмотра')
    time_updated = models.DateTimeField(auto_now=True, verbose_name='Последний просмотр')

    def __str__(self):
        return f'{self.lesson.title}: {self.user.username}'

    def is_viewed(self):
        """ Статус Просмотрено/Не просмотрено (порог 80 %) """
        return (self.viewed_time / self.lesson.duration) * 100 >= 80

    def save(self, *args, **kwargs):
        if self.is_viewed():
            self.view_status = self.Status.viewed
        else:
            self.view_status = self.Status.not_viewed
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Просмотр лекций'
        verbose_name_plural = 'Просмотр лекций'
