from django.db import models
from django.contrib.auth.models import AbstractUser
from jdatetime import date, datetime as jdatetime

# Create your models here.

#! GET DATE & TIME

current_date = jdatetime.now().date()
date = str(current_date).replace("-","/")

#! GET DATE & TIME

#* CUSTOM USER MODEL

types = {
    "user" : "user",
    "sender" : "sender",
    "cashier" : "cashier",
    "middle_manager" : "middle_manager",

}

class CustomUser(AbstractUser):
    user_type = models.CharField(max_length=1000,verbose_name='نوع کاربر',default='user',choices=types)
    profile_picture = models.ImageField(verbose_name='عکس پروفایل', null=True, blank=True)

#* CUSTOM USER MODEL


#* NOTICE MODEL

class Notice(models.Model):
    title = models.CharField(max_length=1000,verbose_name='عنوان اطلاعیه')
    content = models.TextField(verbose_name='محتوا')
    created_at = models.CharField(default=date,verbose_name='تاریخ ایجاد',max_length=1000)

    def __str__(self):
        return (self.title)
    
    class Meta:
        verbose_name="اطلاعیه جدید"
        verbose_name_plural="ارسال کردن اطلاعیه"

#* NOTICE MODEL


#* USER ADDRESS MODEL

class User_Address(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='کاربر')
    city = models.CharField(max_length=1000,verbose_name='شهر',default='تهران')
    area = models.CharField(max_length=1000,verbose_name='منطقه')
    address = models.TextField(verbose_name='ادرس')
    location = models.TextField(verbose_name='لوکیشن')

    def __str__(self):
        return (self.user.username)
    
    class Meta:
        verbose_name_plural="ادرس کاربران"
        verbose_name="ادرس"


#* USER ADDRESS MODEL