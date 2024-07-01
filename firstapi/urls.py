from django.urls import path
from . import views

urlpatterns = [
    path('api/hello/', views.hello_view, name='hello_view'),
    path('api/hello1/', views.intro_view, name='intro_view'),
]

