from .models import Notice

def Site_Data(request):
    notice = Notice.objects.all()


    return {"notice":notice}