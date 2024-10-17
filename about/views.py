from django.shortcuts import render
from .models import *

# Create your views here.


#* ABOUT US VIEW

def About_US(request):
    about_us = About_Us.objects.first()
    gallery = About_Gallery.objects.all()
    context = {"about_us":about_us,"gallery":gallery}

    return render(request,"about.html",context)

#* ABOUT US VIEW