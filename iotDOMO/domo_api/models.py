from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Locations(models.Model):
    name_locations=models.CharField(max_length=255)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

class Devices(models.Model):
    unit=models.CharField(max_length=255)#Undad de medida
    name_devices=models.CharField(max_length=255)
    location=models.ForeignKey(Locations,on_delete=models.CASCADE)
    Serial=models.CharField(max_length=255)
    
class Dots(models.Model):
    value=models.FloatField()
    device=models.ForeignKey(Devices,on_delete=models.CASCADE)
    date_time=models.DateTimeField(auto_now_add=True)
