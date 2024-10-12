from django.shortcuts import render
from .models import *
from django.http import JsonResponse

# Create your views here.

#* PRODUCT LIST VIEW

def Products(request):
    products = Product.objects.all()
    context = {"products":products}

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
        

    return render(request,'list-product.html',context)

#* PRODUCT LIST VIEW