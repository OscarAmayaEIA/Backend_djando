from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
# Create your views here.
class Aplication_users_method(APIView):
    def get(self,request):
        users_local=Aplication_users.objects.all()
        content={}
        users_list=Apli_users_serializer(users_local,many=True).data
        content={"users":users_list}
        return Response(content,status=status.HTTP_200_OK)
    def post(self,request):
        Name=request.data.get("Name")
        contraseña=request.data.get("contraseña")
        Celular=request.data.get("Celular")
        Aplication_users.objects.create(Name=Name,contraseña=contraseña,Celular=Celular)
        return Response(status=status.HTTP_200_OK) 
    def put(self,request,codigo):
        users_local=Aplication_users.objects.get(id=codigo)
        users_local.Name=request.data["Name"]
        users_local.contraseña=request.data["contraseña"]
        users_local.Celular=request.data["Celular"]
        users_local.save()
        return Response(status=status.HTTP_200_OK)
    def delete(self,request,codigo):
        users_local=Aplication_users.objects.get(id=codigo)
        users_local.delete()
        return Response(status=status.HTTP_200_OK)


class Locations_method(APIView):
    def get(self,request,codigo):
        locations_local=Locations.objects.filter(user_id=codigo)
        content={}
        location_list=Locations_serializer(locations_local,many=True).data
        content={"locations":location_list}
        return Response(content,status=status.HTTP_200_OK)
    def post(self,request):
        name_locations=request.data.get("name_locations")
        user=1
        Locations.objects.create(name_locations=name_locations,user_id=user)
        return Response(status=status.HTTP_200_OK) 
    def put(self,request,codigo):
        locations_local=Locations.objects.get(id=codigo)
        locations_local.name_locations=request.data["name_locations"]
        locations_local.save()
        return Response(status=status.HTTP_200_OK)
    def delete(self,request,codigo):
        locations_local=Locations.objects.get(id=codigo)
        locations_local.delete()
        return Response(status=status.HTTP_200_OK)
    
class Devices_method(APIView):
    def get(self,request,codigo):
        devices_local=Devices.objects.filter(location_id=codigo)
        content={}
        devices_list=Devices_serializer(devices_local,many=True).data
        content={"devices":devices_list}
        return Response(content,status=status.HTTP_200_OK)
    def post(self,request):
        unit=request.data.get("unit")
        name_devices=request.data.get("name_devices")
        location_id=request.data.get("location_id")
        Devices.objects.create(name_devices=name_devices,unit=unit,location_id=location_id)
        return Response(status=status.HTTP_200_OK) 
    def put(self,request,codigo):
        devices_local=Devices.objects.get(id=codigo)
        devices_local.name_devices=request.data["name_devices"]
        devices_local.location_id=request.data["location_id"]
        devices_local.save()
        return Response(status=status.HTTP_200_OK)
    def delete(self,request,codigo):
        devices_local=Devices.objects.get(id=codigo)
        devices_local.delete()
        return Response(status=status.HTTP_200_OK)

class Dots_method(APIView):
    def get(self,request,codigo):
        dots_local=Dots.objects.filter(Serial=codigo)
        content={}
        dots_list=Dots_serializer(dots_local,many=True).data
        content={"dots":dots_list}
        return Response(content,status=status.HTTP_200_OK)
    def post(self,request):
        value=request.data.get("value")
        device_id=request.data.get("device_id")
        Dots.objects.create(value=value,device_id=device_id)
        return Response(status=status.HTTP_200_OK) 
    def delete(self,request,codigo):
        dots_local=Dots.objects.get(id=codigo)
        dots_local.delete()
        return Response(status=status.HTTP_200_OK)
class Dots_mqtt(APIView):
    def post(self,request):
        value=request.data.get("value")
        device_id=request.data.get("topic")
        Dots.objects.create(value=value,device_id=device_id)
        return Response(status=status.HTTP_200_OK)
