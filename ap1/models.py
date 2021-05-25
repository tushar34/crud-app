from django.db import models

# Create your models here.

class Car(models.Model):
    car_company=models.CharField(max_length=50)
    car_name=models.CharField(max_length=50)
    car_price=models.CharField(max_length=50)