from django.contrib import admin
from django.urls import path
from MyApp import views

urlpatterns = [
    path('',views.index),
    # path('',views.home,name='home'),
    path('events',views.events,name='events'),
    path('vargani',views.vargani,name='vargani'),
]