from django.shortcuts import render
from django.db.models import Q, F, FilteredRelation

from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound
from catalog.models import ProductAccess
from study.models import Lesson
from study.serializers import MyLessonSerializer, MyLessonsByProductSerializer

# Create your views here.


# вывод всех уроков текущего авторизованного  пользователя
class MyLessonsViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = MyLessonSerializer
    permission_classes = (IsAuthenticated,)  # для авторизованных пользователей (пользователь видит только свое)

    # def get_serializer_context(self):
    #     # user_id = self.request.user  # получить 'user_id'
    #     # return user_id
    #     pass

    # Переопределение исходного QuerySet
    def get_queryset(self):
        # текущий пользователь у которого есть разрешение на курс
        accesses = ProductAccess.objects.filter(user=self.request.user, is_valid=True)
        # 'products__in'  несколько значений
        # 'products'  одно значение
        qs = Lesson.objects.filter(products__in=accesses.values('product_id')
        ).alias(
            view_info=FilteredRelation(
                                        'views',
                                       condition=Q(views__user=self.request.user)
                                       )
        ).annotate(
            status=F('view_info__status'),
            view_time=F('view_info__view_time')
        )

        return qs


class MyLessonsByProductViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = MyLessonsByProductSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        product_id = self.kwargs['product_id']
        accesses = ProductAccess.objects.filter(user=self.request.user, is_valid=True)

        if not product_id in accesses.values_list('product_id', flat=True):
            raise exceptions.NotFound

        qs = Lesson.objects.filter(
            products=product_id
        ).alias(
            view_info=FilteredRelation(
                'views',
                condition=Q(views__user=self.request.user)
            )
        ).annotate(
            status=F('view_info__status'),
            view_time=F('view_info__view_time'),
            last_view_datatime=F('view_info__last_view_datatime')
        )

        return qs
