from django.urls import path, re_path
import re

from . import views

urlpatterns = [
    path('', views.index, name="index"), # Ruta del index
    path('index', views.index, name="index"), # Ruta del index
    re_path(r'/[a-zA-Z]*', views.index, name="index"),
]