from django.contrib import admin
from django.urls import path, include
from mainapp.api import views

urlpatterns = [
    path('watchlist/', views.WatchListAV.as_view(), name='watchlist-list'),
    path('watchlist/<int:pk>/', views.WatchListDetailAV.as_view() , name='watchlist-detail'),
    path('stream/', views.StreamPlatformListAV.as_view(), name='streamplatform-list'),
    path('stream/<int:pk>/', views.StreamPlatformDetailAV.as_view() , name='streamplatform-detail'),
    
]
