from rest_framework import serializers
from .models import *


class Parking_Spot_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Parking_Spot
        fields = '__all__'


class Parking_Statistics_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Parking_Statistics
        fields = '__all__'


class Parking_Lot_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Parking_Lot
        fields = '__all__'
