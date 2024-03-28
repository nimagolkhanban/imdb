from django.contrib import admin
from django.urls import path, include
from mainapp import views

urlpatterns = [
    path('list/', views.movie_list, name='movie-list'),
    path('<int:pk>/', views.movie_detail , name='movie_detail'),
    
]
