from django.contrib import admin
from catalog import models as catalog_models

# Register your models here.
admin.site.register(catalog_models.Product)


@admin.register(catalog_models.ProductAccess)
class ProductAccessAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'is_valid']
