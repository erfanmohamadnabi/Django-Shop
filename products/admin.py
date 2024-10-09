from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Product_Category)


#* PRODUCT ADMIN

class ProductImagesInline(admin.StackedInline):
    model = Product_Images
    extra = 3 

class ProductAttributesInline(admin.StackedInline):
    model = Product_Attributes
    extra = 3 

class Product_Admin(admin.ModelAdmin):
    inlines = [ProductImagesInline, ProductAttributesInline]

admin.site.register(Product, Product_Admin)

#* PRODUCT ADMIN

#* PRODUCT CART ADMIN

admin.site.register(Cart)
admin.site.register(CartItem)

#* PRODUCT CART ADMIN

#* PRODUCT FAVORITES ADMIN

admin.site.register(Favorites)

#* PRODUCT FAVORITES ADMIN
