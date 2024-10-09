from django.shortcuts import render,redirect
from .forms import Signup
from user_account.models import CustomUser

# Create your views here.

#* SIGN UP USER

def SignUp_User(request):
    frm=Signup(request.POST or None)
    context = {"frm":frm}

    if request.POST:
        if frm.is_valid():
            user_type = request.POST.get("user_type")
            data = frm.cleaned_data
            name = data.get("name")
            email = data.get('email')
            password = data.get("password")

            new_user = CustomUser.objects.create(
                username = email,
                first_name = name,
            )

            new_user.set_password(password)

            if user_type == 'user':
                new_user.save()
            elif user_type == 'colleague':
                new_user.save()
                return redirect('/signup/success')

    return render(request,'signup.html',context)

#* SIGN UP USER

#* SUCCESS SIGNUP COLLEAGUE

def Success_Signup(request):
    context = {}
    
    return render(request,'success_signup.html',context)

#* SUCCESS SIGNUP COLLEAGUE

