from django.shortcuts import render,redirect
from .forms import Signup,Login_form
from user_account.models import CustomUser
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

#* SIGN UP USER

def SignUp_User(request):

    #! REDIRECT TO HOME PAGE

    if request.user.is_authenticated:
        return redirect('/')
    
    #! REDIRECT TO HOME PAGE

    frm = Signup(request.POST or None)
    context = {"frm":frm}

    if request.POST:

        print("salam")
        if frm.is_valid():
            user_type = request.POST.get("user_type")
            print(user_type)
            print(user_type)
            print(user_type)
            print(user_type)
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
                new_user.user_type = 'user'
                new_user.save()
                return redirect("/login")
            
            elif user_type == 'colleague':
                new_user.user_type = "sender"
                new_user.save()
                return redirect('/signup/success')

    return render(request,'signup.html',context)

#* SIGN UP USER

#* SUCCESS SIGNUP COLLEAGUE

def Success_Signup(request):
    context = {}
    
    return render(request,'success_signup.html',context)

#* SUCCESS SIGNUP COLLEAGUE

#* LOGIN VIEW

def Login_User(request):

    #! REDIRECT TO HOME PAGE

    if request.user.is_authenticated:
        return redirect('/')
    
    #! REDIRECT TO HOME PAGE

    frm = Login_form(request.POST or None)
    context = {"frm":frm}

    if request.POST:
        if frm.is_valid():
            data = frm.cleaned_data
            username = data.get("username")
            password = data.get("password")

            #! VERIFY USER

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/account/dashboard') 
            
            else:
                context['error'] = 'نام کاربری یا رمز عبور اشتباه است'

            #! VERIFY USER

    return render(request,'login.html',context)

#* LOGIN VIEW

#* LOGOUT VIEW

def Logout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("/login")
    
    return redirect("/login")

#* LOGOUT VIEW
