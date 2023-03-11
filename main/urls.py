from django.urls import path
from . import views

urlpatterns = [
    path('Manual/', views.Sobre, name='manual'),
    path('', views.Home, name='home'),
]

