from django.urls import path, include
from .views import ProductStatisticViewSet
from rest_framework import  routers
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('product_statistics/', ProductStatisticViewSet.as_view({'get': 'list'})),
]

# http://127.0.0.1:8000/catalog/product_statistics/
