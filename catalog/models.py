from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Курсы
class Product(models.Model):
    title = models.CharField(max_length=128)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    # owner = models.ForeignKey(User, models.PROTECT())

    def __str__(self):
        return f'{self.title}: {self.user}'



# Доступ к курсам
class ProductAccess(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='accesses')
    is_valid = models.BooleanField(default=True)  # флаг доступа

    def __str__(self):
        return f'{self.user}: {self.is_valid}'


