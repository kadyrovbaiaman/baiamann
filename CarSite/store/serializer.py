from rest_framework import serializers
from .models import *


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'


class CarListSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()
    add_date = serializers.DateTimeField(format='%d-%m-%Y  %H:%M')
    ratings = RatingSerializer(many=True, read_only=True)

    class Meta:
        model = Car
        fields = ['id', 'car_name', 'add_date', 'country', 'ratings', 'average_rating', 'image']

        def get_average_rating(self, obj):
            return obj.get_average_rating()


class CarDetailSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()
    add_date = serializers.DateTimeField(format='%d-%m-%Y  %H:%M')
    ratings = RatingSerializer(many=True, read_only=True)

    class Meta:
        model = Car
        fields = ['id', 'car_name', 'description', 'year', 'price', 'add_date', 'country',
                  'mileage', 'with_photo', 'volume', 'image', 'condition', 'customs',
                  'availability', 'body', 'color', 'registration','ratings','average_rating']

        def get_average_rating(self, obj):
            return obj.get_average_rating()
