from django.db import models
from django.contrib import admin
class car (models.Model):
    car_colour=models.CharField(max_length=20)
    car_name=models.CharField(max_length=20)
    car_number=models.IntegerField(primary_key=True)
    car_price=models.IntegerField()
    car_speed=models.IntegerField
class carAdmin(admin.ModelAdmin):
     list_display=["car_colour","car_name","car_number","car_price","car_speed"]
