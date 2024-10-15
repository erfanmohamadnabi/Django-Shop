from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from .views import Profile,User_Favorites,User_Cart,Delete_CartItem,Delete_Favorites,Dashboard,User_Addresses,User_AddAddress,User_EditAddress,Delete_Address,Not_Find
from django.urls import path

urlpatterns = [
    path('account/dashboard',Dashboard,name='dashboard'),
    path('account/profile',Profile,name='profile'),
    path('account/favorites',User_Favorites,name='favorites'),
    path('account/cart',User_Cart,name='cart'),
    path('account/addresses',User_Addresses,name='address'),
    path('account/addresses/add',User_AddAddress,name='add_address'),
    path('account/addresses/edit/<id>',User_EditAddress,name='edit_addres'),

    path('404',Not_Find,name='not_find'),

    path('delete_cartitem/<item_id>',Delete_CartItem),
    path('delete_favorites/<favorite_id>',Delete_Favorites),
    path('delete_addresses/<address_id>',Delete_Address),
]
