from django.shortcuts import render
from user_account.models import CustomUser
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

# Create your views here.

#* USER DATA

@login_required(login_url="/login")
def Profile(request):
    context = {}

    if request.POST:
        user = CustomUser.objects.filter(username = request.user.username).first()
        name = request.POST.get('name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')

        if len(name) > 0 and len(password) == 0 or len(repassword) == 0:
            user.first_name = name
            user.save()
            data = {
                'success':'success'
            }

            return JsonResponse(data)
        
        elif len(name) > 0 and len(password) > 0 and len(repassword) > 0:
            if len(password) >= 8:
                if password == repassword:
                    user.first_name = name
                    user.set_password(password)
                    user.save()
                    data = {
                        'success':'success'
                    }
                else:
                   data = {
                    'error':'error'
                }
                return JsonResponse(data) 
            else:
                data = {
                    'error_len':'error'
                }
                return JsonResponse(data)
             

    return render(request,'account.html',context)

#* USER DATA