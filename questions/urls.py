from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from .views import Questions
from django.urls import path

urlpatterns = [
    path('questions',Questions,name='questions'),
]
