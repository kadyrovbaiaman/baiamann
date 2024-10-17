from django.urls import path
from .views import *

urlpatterns=[

    path('', CarListViewSet.as_view({'get': 'list', 'post': 'create'}), name='car_list'),
    path('<int:pk>/', CarDetailViewSet.as_view({'get': 'retrieve',
                                                  'put': 'update', 'delete': 'destroy'}), name='car_detail'),

    path('rating', RatingViewSet.as_view({'get': 'list', 'post': 'create'}), name='rating_list'),
    path('rating/<int:pk>/', RatingViewSet.as_view({'get': 'retrieve',
                                                   'put': 'update', 'delete': 'destroy'}), name='rating_detail'),

]

