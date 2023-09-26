from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=128)
    owner = models.ForeignKey(User, on_delete=models.PROTECT())
    # owner = models.ForeignKey(User, models.PROTECT())


class ProductAccess(models.Model):
    pass