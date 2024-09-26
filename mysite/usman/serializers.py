from rest_framework import serializers
from .models import *


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class FoodSerializers(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'


class CourierSerializers(serializers.ModelSerializer):
    class Meta:
        model = Courier
        fields = '__all__'


class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class DeliverySerializers(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = '__all__'


class RatingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
