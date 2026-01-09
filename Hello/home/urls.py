from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('f_view', views.index,),
    path('about/', views.about,),   
    path('services/', views.services,),
]