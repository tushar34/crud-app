from django.contrib import admin
from django.urls import path
from ap1 import views

urlpatterns = [
  path('', views.car_view, ''),
  path('car_add', views.car_add, ''),
  path('car_delete/<id>', views.car_delete, ''),
  path('car_update/<id>', views.car_update, ''),
]
