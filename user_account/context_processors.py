from .models import Notice
from site_data.models import Site_Data as data
from products.models import Product_Category,Amazing_Offer

#* SEND DATA TO ALL VIEWS

def Site_Data(request):
    notice = Notice.objects.all()
    site_data = data.objects.first()
    categorys = Product_Category.objects.all()
    offer = Amazing_Offer.objects.first()


    return {"notice":notice,"site_data":site_data,"categorys":categorys,"offer":offer}

#* SEND DATA TO ALL VIEWS