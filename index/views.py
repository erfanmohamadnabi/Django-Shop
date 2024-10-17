from django.shortcuts import render
from .models import *
from weblog.models import Blog
from django.http import JsonResponse
from products.models import *
from django.db.models import Sum

# Create your views here.


#* HOME PAGE VIEW

def Index(request):
    slider = Index_Slider.objects.all()
    weblog = Blog.objects.all()
    best_sellers = Product.objects.all().order_by("-buy")
    new_products = Product.objects.all().order_by("-id")
    suggestions = (Product.objects.order_by('-visit', '-buy'))
    context = {"slider":slider,"weblog":weblog,"best_sellers":best_sellers,"new_products":new_products,"suggestions":suggestions}


    if request.POST.get("product-id"):
        product_id = request.POST.get("product-id")
        request_type = request.POST.get("request-type")
        

        #! NEW LIKE USER

        if request_type == "like":
            if request.user.is_authenticated:
                product = Product.objects.get(id = product_id)
                like = Favorites.objects.filter(product = product).first()

                if like is None:
                    like = Favorites.objects.create(user = request.user,product = product)
                    like.save()

                data = {"add_like":"success"}

                return JsonResponse(data)
        
            else:
                data = {"error":"error"}

                return JsonResponse(data)

        #! NEW LIKE USER


        #! NEW ORDER USER

        if request_type == "order":
            if request.user.is_authenticated:
                product = Product.objects.get(id = product_id)
                cart = Cart.objects.filter(is_paid = False,user = request.user).first()
                cart_item = CartItem.objects.filter(cart = cart,product = product).first()

                if cart:
                    if cart_item:
                        cart_item.quantity +=1
                        cart_item.save()
                    else:
                        cart_item = CartItem.objects.create(cart = cart,product = product,price = product.price,quantity = 1)
                        cart_item.save()

                data = {"add_cart":"success"}

                return JsonResponse(data)
            
            else:
                data = {"error":"error"}

                return JsonResponse(data)

        #! NEW ORDER USER

    return render(request,'index.html',context)

#* HOME PAGE VIEW