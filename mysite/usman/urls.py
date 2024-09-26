from django.urls import path
from .views import *


urlpatterns = [
    path('', FoodViewSet.as_view({'get': 'list',
                                 'post': 'create'}), name='food_list'),
    path('<int:pk>/', FoodViewSet.as_view({'get': 'retrieve',
                                          'put': 'update', 'delete': 'destroy'}), name='food_detail'),
    path('courier/', CourierViewSet.as_view({'get': 'list',
                                           'post': 'create'}), name='courier_list'),
    path('order/', OrderViewSet.as_view({'get': 'list',
                                           'post': 'create'}), name='order_list'),
    path('delivery/', DeliveryViewSet.as_view({'get': 'list',
                                           'post': 'create'}), name='delivery_list'),
    path('review/', ReviewViewSet.as_view({'get': 'list',
                                 'post': 'create'}), name='review_list'),
    path('review/<int:pk>/', ReviewViewSet.as_view({'get': 'retrieve',
                                          'put': 'update', 'delete': 'destroy'}), name='review_list'),
]