from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lotto/<int:num>/<int:max2>/', views.lotto, name='lotto'),
    path('lotto/<int:num>/', views.lotto, name='lotto'),
    path('square/<int:num>/', views.square, name='square')
]