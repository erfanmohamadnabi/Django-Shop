from django.shortcuts import render,redirect
from user_account.models import CustomUser,Notice
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from products.models import Favorites
from products.models import Cart,CartItem
from django.db.models import Sum
from .models import User_Address as Adresses
import requests
import pandas as pd

# Create your views here.


#! NESHAN API KEY

API_KEY = 'service.dd66b2a61b0642bcb42f5ee57cd83322'

#! NESHAN API KEY


#* USER DASHBOARD

def Dashboard(request):
    notices = Notice.objects.all()
    cart = Cart.objects.filter(user = request.user)
    context = {"cart":cart}

    return render(request,'dashboard.html',context)

#* USER DASHBOARD

#* USER DATA

@login_required(login_url="/login")
def Profile(request):
    context = {}

    if request.POST:
        user = CustomUser.objects.filter(username = request.user.username).first()
        name = request.POST.get('name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')

        if len(name) > 0 and len(password) == 0 or len(repassword) == 0:
            user.first_name = name
            user.save()
            data = {
                'success':'success'
            }

            return JsonResponse(data)
        
        elif len(name) > 0 and len(password) > 0 and len(repassword) > 0:
            if len(password) >= 8:
                if password == repassword:
                    user.first_name = name
                    user.set_password(password)
                    user.save()
                    data = {
                        'success':'success'
                    }
                else:
                   data = {
                    'error':'error'
                }
                return JsonResponse(data) 
            else:
                data = {
                    'error_len':'error'
                }
                return JsonResponse(data)
             

    return render(request,'account.html',context)

#* USER DATA


#* USER FAVORITES

def User_Favorites(request):
    favorites = Favorites.objects.filter(user = request.user)
    context = {"favorites":favorites}

    return render(request,"favorites.html",context)

#! DELETE FAVORITES

def Delete_Favorites(request,favorite_id):    
    if favorite_id is not None:
        order_detail =Favorites.objects.get(id = favorite_id)    

        if order_detail is not None:
            order_detail.delete()
            return redirect("/account/favorites")
            
    return redirect("/account/favorites")

#! DELETE FAVORITES

#* USER FAVORITES


#* USER CART

def User_Cart(request):
    cart = Cart.objects.filter(user = request.user,is_paid = False).first()
    total_quantity = 0

    if cart:
        total_quantity = cart.cartitems.aggregate(total=Sum('quantity'))['total'] or 0
    context = {"cart":cart,"total_quantity":total_quantity}

    return render(request,'cart.html',context)

#! DELETE CART ITEMS

def Delete_CartItem(request,item_id):    
    if item_id is not None:
        order_detail =CartItem.objects.get(id = item_id)
        if order_detail.quantity > 1:
            order_detail.quantity -= 1
            order_detail.save()
        else:       
            if order_detail is not None:
                order_detail.delete()
                return redirect("/account/cart")
            
    return redirect("/account/cart")

#! DELETE CART ITEMS

#* USER CART


#* USER ADDRESSES

def User_Addresses(request):
    addresses = Adresses.objects.filter(user = request.user)
    context = {"addresses":addresses}

    return render(request,'adresses.html',context)


#* USER ADDRESSES


#* USER ADD ADDRESS

def User_AddAddress(request):

    context = {}

    address = None

    if request.POST:
        city = request.POST.get("city")
        area = request.POST.get("area")
        address = request.POST.get("address")
        
        print(city + area + address)


    #! GET MAP LINK

    if address :
        headers = {
            'Api-Key' : API_KEY
        }

        response = requests.get(f'https://api.neshan.org/v4/geocoding?address={address} ',headers=headers)

        j = response.json()

        if j['status'] == 'NO_RESULT':
            data = {"error":"error"}

            return JsonResponse(data)
        
        L = []

        print(j['location'].items())

        for i,x in j['location'].items():
            L.append(x)

        lan = round(float(L[0]), 7)  
        lat = round(float(L[1]), 7)

        map_data = f"https://maps.google.com/?q={lat},{lan}"


        print(map_data)

        #! NEW ADDRESS

        new_address = Adresses.objects.create(user = request.user,city = city,area = area,address = address,location = map_data)
        new_address.save()
        
        data = {"success":"success"}

        return JsonResponse(data)

        #! NEW ADDRESS

    #! GET MAP LINK

       

    return render(request,'add_address.html',context)

#* USER ADD ADDRESS
