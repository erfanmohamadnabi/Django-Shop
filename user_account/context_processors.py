from .models import Notice
from site_data.models import Site_Data as data
from products.models import Product_Category,Amazing_Offer,Cart

#* SEND DATA TO ALL VIEWS

def Site_Data(request):
    notice = Notice.objects.all()
    site_data = data.objects.first()
    categorys = Product_Category.objects.all()
    offer = Amazing_Offer.objects.first()
    if request.user.is_authenticated :
        current_cart = Cart.objects.filter(user = request.user,is_paid = False).first()
    else:
        current_cart = 0


    return {"notice":notice,"site_data":site_data,"categorys":categorys,"offer":offer,"current_cart":current_cart}

#* SEND DATA TO ALL VIEWS