from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from jdatetime import date, datetime as jdatetime


persian_month_names = [
    "فروردین", "اردیبهشت", "خرداد",
    "تیر", "مرداد", "شهریور",
    "مهر", "آبان", "آذر",
    "دی", "بهمن", "اسفند"
]


current_date = jdatetime.today()
month_name = persian_month_names[current_date.month - 1]
date = f"{current_date.day} {month_name}"

# Create your models here.

class Blog_Category(models.Model):
    name = models.CharField(max_length=200,verbose_name="نام فارسی دسته بندی")
    en_name = models.CharField(max_length=200,verbose_name="نام انگلیسی دسته بندی")

    class Meta:
        verbose_name="دسته بندی جدید"
        verbose_name_plural="اضافه کردن دسته بندی مقالات"

    def __str__(self):
        return (self.name)
    
    def get_absolute_url(self):
        return reverse("weblog_category",args=[self.en_name])
    


class Blog(models.Model):
    title = models.CharField(max_length=300,verbose_name="عنوان مقاله")
    slug = models.CharField(max_length=300,verbose_name="اسلاگ",blank=True,null=True)
    date = models.CharField(max_length=100,verbose_name="تاریخ",default=date)
    image = models.ImageField(verbose_name="تصویر مقاله")
    text = RichTextField(verbose_name="متن مقاله")
    category = models.ForeignKey(Blog_Category,verbose_name="دسته بندی",blank=True,null=True,on_delete=models.CASCADE)
    writer = models.CharField(max_length=100,verbose_name="نام نویسنده")
    title_seo = models.CharField(verbose_name = "عنوان برای سئو",max_length = 500)
    meta_seo = models.TextField(verbose_name = "توضیحات متا برای سئو")
    keywords = models.CharField(max_length=500,verbose_name = "کلیدواژه ها را برای سئو وارد کنید (  با علامت , جدا کنید  )")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.title.replace(' ','-')
        super().save(*args, **kwargs)
    

    class Meta:
        verbose_name="مقاله"
        verbose_name_plural="مقالات"

    def __str__(self):
        return (self.title)
    
    def get_absolute_url(self):
        return reverse("detail_weblog",args=[self.id,self.slug])