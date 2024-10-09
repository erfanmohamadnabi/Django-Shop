from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path
from .views import Products

urlpatterns = [
    path('list-product',Products,name='list_product')
]