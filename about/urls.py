from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from .views import About_US
from django.urls import path

urlpatterns = [
    path('about-us',About_US,name='about_us'),
]
