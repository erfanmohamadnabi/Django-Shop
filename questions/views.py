from django.shortcuts import render
from .models import *

# Create your views here.

#* QUESTIONS VIEW

def Questions(request):
    qestions = Questions_Model.objects.all()
    context = {'qestions':qestions}

    return render(request,'question.html',context)

#* QUESTIONS VIEW