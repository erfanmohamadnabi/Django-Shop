from django.db import models

# Create your models here.


class ContactUs(models.Model):
    title = models.CharField(verbose_name='عنوان پیام',max_length=200)
    email = models.EmailField(verbose_name='ایمیل کاربر',max_length=1000)
    message = models.TextField(verbose_name='متن پیام')

    class Meta:
        verbose_name="اضافه کردن پیام"
        verbose_name_plural="ارتباط با ما"

    def __str__(self):
        return (self.title)