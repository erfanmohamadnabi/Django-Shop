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
        

        #! NEW LIKE USER
        if request.user.is_authenticated:
            product = Product.objects.get(id = product_id)
            like = Favorites.objects.filter(product = product).first()

            if like is None:
                like = Favorites.objects.create(user = request.user,product = product)
                like.save()

            data = {"success":"success"}

            return JsonResponse(data)
    
        else:
            data = {"error":"error"}

            return JsonResponse(data)

        #! NEW LIKE USER
        

    return render(request,'list-product.html',context)

#* PRODUCT LIST VIEW