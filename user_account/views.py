from django.shortcuts import render,redirect
from user_account.models import CustomUser,Notice
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from products.models import Favorites
from products.models import Cart,CartItem
from django.db.models import Sum
from .models import User_Address as Adresses
# Create your views here.

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


#* USER ADDRESS

def User_Address(request):
    addresses = Adresses.objects.filter(user = request.user)
    context = {"addresses":addresses}

    return render(request,'adresses.html',context)

#* USER ADDRESS
