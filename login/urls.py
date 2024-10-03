from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from .views import SignUp_User,Success_Signup
from django.urls import path

urlpatterns = [
    path('signup/success',Success_Signup,name='success_signup'),
    path('signup',SignUp_User,name='signup'),
]
