from django.urls import path

from . import views

urlpatterns = [
    path('join/', views.join, name='join'),
    path('leave/', views.leave, name='leave'),
    path('', views.index, name='index'),
]