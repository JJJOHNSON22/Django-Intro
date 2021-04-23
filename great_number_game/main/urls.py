from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('test_number', views.test),
    path('reset', views.reset),
]