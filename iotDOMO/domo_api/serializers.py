from rest_framework import serializers
from .models import *

class Locations_serializer(serializers.ModelSerializer):
    name_locations=serializers.CharField(max_length=255)
    user_id=serializers.IntegerField()
    class Meta:
        model=Locations
        fields=["id","name_locations","user_id"]

class Devices_serializer(serializers.ModelSerializer):
    unit=serializers.CharField(max_length=255)
    name_devices=serializers.CharField(max_length=255)
    location_id=serializers.IntegerField()
    class Meta:
        model=Devices
        fields=["id","unit","name_devices","location_id"]
class Dots_serializer(serializers.ModelSerializer):
    value=serializers.FloatField()
    device_id=serializers.IntegerField()
    class Meta:
        model=Dots
        fields=["value","device_id","date_time"]
