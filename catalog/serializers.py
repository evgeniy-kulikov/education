from rest_framework import serializers

class ProductStatisticSerializer(serializers.Serializer):
    title = serializers.CharField()
    lesson_view_count=serializers.IntegerField()
    totoal_view_time=serializers.IntegerField()
    total_users_on_products=serializers.IntegerField()
    percent_purchase=serializers.FloatField()