from django.db import models

# Create your models here.


#* HOME PAGE SLIDER

class Index_Slider(models.Model):
    titie = models.CharField(verbose_name='عنوان تصویر',max_length=1000)
    image = models.ImageField(upload_to='slider', verbose_name='تصویر')
    link = models.TextField(verbose_name='لینک')

    def __str__(self) :
        return (self.titie)
    

    class Meta:
        verbose_name="اضافه کردن اسلایدر"
        verbose_name_plural="اسلایدر صفحه اصلی"

#* HOME PAGE SLIDER