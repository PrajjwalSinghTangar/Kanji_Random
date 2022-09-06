from django.urls import path
from . import views

urlpatterns = [
    path('', views.redirect, name='redirect'),
    path('index/<str:key>', views.index, name='index'),
    path('random', views.random, name='random')
]