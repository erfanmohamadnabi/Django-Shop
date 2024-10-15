from .models import Notice
from site_data.models import Site_Data as data

#* SEND DATA TO ALL VIEWS

def Site_Data(request):
    notice = Notice.objects.all()
    site_data = data.objects.all()


    return {"notice":notice,"site_data":site_data}

#* SEND DATA TO ALL VIEWS