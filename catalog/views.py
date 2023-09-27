from django.shortcuts import render
# Create your views here.
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from catalog.models import Product, ProductAccess
from catalog.serializers import ProductStatisticSerializer
from django.db.models import Count, OuterRef, Sum, F
from study.models import LessonViewInfo, LessonStatusEnum
from django.contrib.auth.models import User


class ProductStatisticViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = ProductStatisticSerializer
    permission_classes = (IsAuthenticated,IsAdminUser)  # для авторизованных пользователей

    def get_queryset(self):
        total_users_count=User.objects.all().filter(is_active=True).count()
        qs = Product.objects.all().annotate(
            lesson_view_count=Count(
                LessonViewInfo.objects.filter(
                    lesson__products=OuterRef('id'),
                    status=LessonStatusEnum.VIEWED
                ).values('id')
            ),
            totoal_view_time=Sum(
                    LessonViewInfo.objects.filter(
                    lesson__products=OuterRef('id'),
                ).values('view_time')
            ),
            total_users_on_products=Count(
                ProductAccess.objects.filter(product_id=OuterRef('id')).values('id')
            ),
            percent_purchase=F('total_users_on_products') / float(total_users_count) * 100
        )

        return qs


