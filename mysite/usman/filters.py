from django_filters.rest_framework import FilterSet
from .models import Category, Food


class CategoryFilter(FilterSet):
    class Meta:
        model = Category
        fields = {
            'category_name': ['exact']
        }


class FoodFilter(FilterSet):
    class Meta:
        model = Food
        fields = {
            'price': ['gt', 'lt']
        }
