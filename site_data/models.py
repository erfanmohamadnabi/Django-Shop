from django.db import models

# Create your models here.

#* SITE DATA MODEL

class Site_Data(models.Model):
    logo = models.ImageField(verbose_name='لوگو سایت')
    email = models.CharField(max_length=500,verbose_name='ایمیل')
    phone_ceo = models.CharField(max_length=500,verbose_name='تلفن مدیر ( برای دریافت پیامک ثبت سفارش )')
    phone_contact = models.CharField(max_length=500,verbose_name='شماره تلفن ( برای نمایش در سایت )')
    landline_phone = models.CharField(max_length=500,verbose_name='شماره ثابت ( برای نمایش در سایت )')
    working_hours =  models.CharField(max_length=500,verbose_name='ساعت کاری')
    address = models.CharField(max_length=500,verbose_name='آدرس')
    description = models.TextField(verbose_name='توضیحات درباره ما')
    location = models.TextField(verbose_name='لینک لوکیشن')

    instagram = models.CharField(max_length=1000,verbose_name='لینک اینستاگرام',blank=True,null=True)
    youtube = models.CharField(max_length=1000,verbose_name='لینک یوتیوب',blank=True,null=True)
    telegram = models.CharField(max_length=1000,verbose_name='لینک تلگرام',blank=True,null=True)
    twitter = models.CharField(max_length=1000,verbose_name='لینک توییتر',blank=True,null=True)
    facebook = models.CharField(max_length=1000,verbose_name='لینک فیسبوک',blank=True,null=True)

    def __str__(self):
        return ("اطلاعات سایت")
    
    class Meta:
        verbose_name_plural="اطلاعات سایت"
    
#* SITE DATA MODEL