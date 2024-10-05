from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from .views import Contact
from django.urls import path

urlpatterns = [
    path('contact-us',Contact,name='contact'),
]
