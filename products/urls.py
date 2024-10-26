from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path
from .views import Products,Detail_Product,Search_Product,Filter_Product,Category_Product

urlpatterns = [
    path('list-product',Products,name='list_product'),
    path('list-product/search',Search_Product,name='search_product'),
    path('list-product/filter',Filter_Product,name='filter_product'),
    path('list-product/category/<ct>',Category_Product,name='category_product'),



    path('detail-product/<id>/<slug>',Detail_Product,name='detail_product')
]