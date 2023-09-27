from django.urls import path, include
from rest_framework.routers import SimpleRouter
from study.views import MyLessonsViewSet, MyLessonsByProductViewSet

router = SimpleRouter()
router.register('my-lessons', MyLessonsViewSet, basename='my-lessons')


urlpatterns = [
    path('', include(router.urls)),  # http://127.0.0.1:8000/study/my-lessons/
    path('by-product/<int:product_id>/lessons/', MyLessonsByProductViewSet.as_view({'get': 'list'})),
    # http://127.0.0.1:8000/study/by-product/1/lessons/
]