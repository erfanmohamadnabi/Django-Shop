from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    user_type = models.CharField(max_length=1000,verbose_name='نوع کاربر',default='مشتری')
    profile_picture = models.ImageField(verbose_name='عکس پروفایل', null=True, blank=True)
