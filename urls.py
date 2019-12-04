from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.authlogin, name='login'),
    ]
