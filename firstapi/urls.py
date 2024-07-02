from django.urls import path
from firstapi import views

urlpatterns = [
    path('api/visit/', views.visit, name='visit'),
]

