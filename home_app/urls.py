from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Main_page'),
    path('about/', views.about, name='About_me'),
]