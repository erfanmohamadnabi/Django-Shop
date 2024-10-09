from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from .views import Profile
from django.urls import path

urlpatterns = [
    path('account/profile',Profile,name='profile'),
]
