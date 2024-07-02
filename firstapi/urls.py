from django.urls import path
from firstapi import views

urlpatterns = [
    path('api/hello/', views.hello, name='hello'),
]

