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
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


#! NESHAN API KEY

API_KEY = 'service.dd66b2a61b0642bcb42f5ee57cd83322'

#! NESHAN API KEY


#* USER DASHBOARD

@login_required(login_url="/login")
def Dashboard(request):
    notices = Notice.objects.all()
    cart = Cart.objects.filter(user = request.user)
    
    if cart:
        current_cart = Cart.objects.filter(user = request.user,is_paid = False).first()
        if current_cart:
            current_items = current_cart.cartitems.all()
        else:
            current_items = None
    else:
        current_cart = 0
        current_items = 0

    #! GET NOT PAID ITEMS COUNT

    not_paid = cart.filter(is_paid = False)
    not_paid_items = sum(cart.cartitems.count() for cart in not_paid)

    #! GET NOT PAID ITEMS COUNT

    #! GET PAID ITEMS COUNT

    paid = cart.filter(is_paid = True)
    paid_items = sum(cart.cartitems.count() for cart in paid)

    #! GET PAID ITEMS COUNT


    context = {"cart":cart,"current_items":current_items,"not_paid_items":not_paid_items,"paid_items":paid_items}

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

@login_required(login_url="/login")
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

@login_required(login_url="/login")
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

@login_required(login_url="/login")
def User_Addresses(request):
    addresses = Adresses.objects.filter(user = request.user)
    context = {"addresses":addresses}

    return render(request,'adresses.html',context)


#! DELETE ADDRESS

def Delete_Address(request,address_id):    
    if address_id is not None:
        order_detail = Adresses.objects.get(id = address_id)

        if order_detail is not None:
            order_detail.delete()
            return redirect("/account/addresses")
            
    return redirect("/account/addresses")

#! DELETE ADDRESS

#* USER ADDRESSES


#* USER ADD ADDRESS

@login_required(login_url="/login")
def User_AddAddress(request):

    context = {}

    address = None

    if request.POST:
        city = request.POST.get("city")
        area = request.POST.get("area")
        address = request.POST.get("address")
        


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

        lan = round(float(L[0]), 9)  
        lat = round(float(L[1]), 9)

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


#* USER EDIT ADDRESS

@login_required(login_url="/login")
def User_EditAddress(request,id):
    current_address = Adresses.objects.filter(user = request.user,id = id).first()
    if current_address is None:
        return redirect('/')
    context = {"address":current_address}

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

        lan = round(float(L[0]), 9)  
        lat = round(float(L[1]), 9)

        map_data = f"https://maps.google.com/?q={lat},{lan}"


        print(map_data)

        #! EDIT ADDRESS

        current_address.city = city
        current_address.area = area
        current_address.address = address
        current_address.location = map_data
        current_address.save()
        
        data = {"success":"success"}

        return JsonResponse(data)

        #! EDIT ADDRESS

    #! GET MAP LINK

    

    return render(request,'edit_addres.html',context)

#* USER EDIT ADDRESS

#* 404 VIEW

def Not_Find(request):
    context = {}

    return render(request,'404.html',context)

#* 404 VIEW


#* PRODUCT CHECKOUT VIEW

def CheckOut(request,id):
    paymant = Cart.objects.filter(id = id,user = request.user,is_paid = False).first()
    addresses = Adresses.objects.filter(user = request.user)

    if paymant is None:
        return redirect("/404")

    context = {"addresses":addresses}

    #! PAYMENT 

    if request.POST or request.FILES:
        first_name = request.POST.get("first-name")
        last_name = request.POST.get("last-name")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        image = request.FILES.get("image")

        find_address = Adresses.objects.filter(id = address).first()

        paymant.name = first_name + " " + last_name
        paymant.address = find_address
        paymant.phone = phone
        paymant.image = image
        paymant.is_paid = True
        paymant.save()

    #! PAYMENT 

    #! SEND USER EMAIL 

        send_mail(
            'ثبت سفارش',
            f"سلام کاربر گرامی! 🌟 سفارش شما با کد پیگیری **{paymant.code}** با موفقیت ثبت گردید. پس از تأیید فیش واریزی توسط مدیر، به زودی با شما، مشتری گرامی، تماس خواهیم گرفت. از اعتماد شما به ما سپاسگزاریم و امیدواریم تجربه‌ای عالی را با ما داشته باشید! 💖 با بهترین آرزوها، [الفا میوه]",
            settings.DEFAULT_FROM_EMAIL,
            [request.user.username], 
            fail_silently=False,
        )

    #! SEND USER EMAIL

        return redirect(f"/account/cart/checkout/{paymant.id}/success")

       

    return render(request,'checkout.html',context)

#* PRODUCT CHECKOUT VIEW


#* PRODUCT SUCCESS PAYMENT VIEW

def Success_Payment(request,id):
    paymant = Cart.objects.filter(id = id,user = request.user).first()

    if paymant is None:
        return redirect("/404")
    

    context = {}

    return render(request,'success_payment.html',context)

#* PRODUCT SUCCESS PAYMENT VIEW


#* PRODUCT FACTOR PAYMENT VIEW

def Factor(request,id):
    paymant = Cart.objects.filter(id = id,user = request.user,is_paid = True).first()

    if paymant is None:
        return redirect("/404")
    context = {"paymant":paymant}

    return render(request,'factor.html',context)

#* PRODUCT FACTOR PAYMENT VIEW

