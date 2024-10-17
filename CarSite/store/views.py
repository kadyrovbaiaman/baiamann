from rest_framework import viewsets
from .models import *
from .serializer import *

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .filters import *


class CarListViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = CarFilter
    search_fields = ['car_name']
    ordering_fields = ['add_date','year']


class CarDetailViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarDetailSerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    filterset_class = FilterSet
