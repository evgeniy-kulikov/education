
from rest_framework.decorators import action
from rest_framework import generics, viewsets
from rest_framework.response import Response
from courses.models import Product, Lesson, Progress, Students
from .serializers import LessonSerializer, StudentSerializer

"""
1. Реализовать API для выведения списка всех уроков по всем продуктам к которым пользователь имеет доступ,
с выведением информации о статусе и времени просмотра.
2. Реализовать API с выведением списка уроков по конкретному продукту к которому пользователь имеет доступ,
с выведением информации о статусе и времени просмотра, а также датой последнего просмотра ролика.
3. Реализовать API для отображения статистики по продуктам.
Необходимо отобразить список всех продуктов на платформе, к каждому продукту приложить информацию:
   1. Количество просмотренных уроков от всех учеников.
   2. Сколько в сумме все ученики потратили времени на просмотр роликов.
   3. Количество учеников занимающихся на продукте.
   4. Процент приобретения продукта
   (рассчитывается исходя из количества полученных доступов к продукту
   деленное на общее количество пользователей на платформе).

"""


class LessonViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    @action(methods=['get'], detail=False)
    def course(self, request):
        product = Product.objects.all()
        return Response({'products': [el.name for el in product]})



class StudentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer

    @action(methods=['get'], detail=False)
    def student(self, request):
        student = Students.objects.all()
        return Response({'students': [el.user for el in student]})

