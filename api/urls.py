from django.urls import path
from api import views

urlpatterns = [
    path('', views.index),
    path('services/', views.services),
    path('download/', views.download),
]
