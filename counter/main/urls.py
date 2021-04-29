from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('destroy_session', views.reset),
    path('plus_two', views.add_two)
]