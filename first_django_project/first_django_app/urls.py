from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('blogs/', views.index),
    path('blogs/new/', views.new),
    path('blogs/create/', views.create),
    path('blogs/json/', views.jsonRedirect),
    path('blogs/<number>/', views.show),
    path('blogs/<number>/edit/', views.edit),
    path('blogs/<number>/delete/', views.destroy),
]
