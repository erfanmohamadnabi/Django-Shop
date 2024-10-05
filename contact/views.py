from django.shortcuts import render
from .models import ContactUs
from django.http import JsonResponse

# Create your views here.

def Contact(request):
    context = {}

    if request.POST:
        title = request.POST.get('title')
        email = request.POST.get('email')
        message = request.POST.get('message')
        if len(title) > 0 and len(email) > 0 and len(message) > 0:
            new_contact = ContactUs.objects.create(title = title,email = email,message = message)
            new_contact.save()
            data = {
                'success':'success'
            }
            
            return JsonResponse(data)
        else:
            data = {
                'error':'error'
            }

            return JsonResponse(data)
    return render(request,'contact.html',context)