from django.contrib import admin
from django.urls import path, include
from mainapp.api import views

urlpatterns = [
    path('list/', views.MovieListAV.as_view(), name='movie-list'),
    path('<int:pk>/', views.MovieDetailAV.as_view() , name='movie_detail'),
    
]
