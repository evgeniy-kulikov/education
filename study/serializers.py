from rest_framework import serializers
from study.models import Lesson, LessonViewInfo


# class MyLessonViewInfoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = LessonViewInfo
#         fields = ('status', 'view_time')


class MyLessonSerializer(serializers.ModelSerializer):
    # # Получается избыточное кол-во запросов
    # def get_view_info(self, obj):
    #     view_info = LessonViewInfo.objects.get(user=self.context['user_id'], lesson_id=obj.id)
    #     return MyLessonSerializer(view_info).data

    status = serializers.CharField()
    view_time = serializers.IntegerField()

    class Meta:
        model = Lesson
        fields = ('title', 'status', 'view_time')


class MyLessonsByProductSerializer(serializers.ModelSerializer):
    status = serializers.CharField()
    view_time = serializers.IntegerField()
    last_view_datatime = serializers.DateTimeField()

    class Meta:
        model = Lesson
        fields = ('title', 'status', 'view_time', 'last_view_datatime')

