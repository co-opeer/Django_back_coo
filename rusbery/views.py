from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *


class Parking_SpotViewSet(viewsets.ModelViewSet):
    queryset = Parking_Spot.objects.all()
    serializer_class = Parking_Spot_Serializer


class Parking_StatisticsViewSet(viewsets.ModelViewSet):
    queryset = Parking_Statistics.objects.all()
    serializer_class = Parking_Statistics_Serializer


class Parking_LotViewSet(viewsets.ModelViewSet):
    queryset = Parking_Lot.objects.all()
    serializer_class = Parking_Lot_Serializer
