from django.urls import path
from . import views

urlpatterns = [
    add *path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]