from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('save_flange', views.save_flange, name="save_flange"),
    path('get_torque/<aks_number>/<flange_number>', views.get_torque, name="get_torque")
]