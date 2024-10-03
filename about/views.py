from django.shortcuts import render

# Create your views here.


#* ABOUT US VIEW

def About_US(request):
    context = {}

    return render(request,"about.html")

#* ABOUT US VIEW