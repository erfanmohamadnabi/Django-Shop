from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from user_account.models import CustomUser

# Create your models here.

#* PRODUCT CATEGORY MODEL

class Product_Category(models.Model):
    name = models.CharField(verbose_name='نام دسته بندی',max_length=1000)
    english_name = models.CharField(verbose_name='نام دسته بندی ( انگلیسی )',max_length=1000)

    def __str__(self) :
        return (self.name)
    
    class Meta:
        verbose_name="دسته بندی جدید"
        verbose_name_plural="اضافه کردن دسته بندی"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.english_name = self.title.replace(' ','-')
        super().save(*args, **kwargs)

#* PRODUCT CATEGORY MODEL

#* PRODUCT MODEL

class Product(models.Model):
    name = models.CharField(verbose_name='نام محصول',max_length=1000)
    english_name = models.CharField(verbose_name='نام محصول ( انگلیسی )',max_length=1000)
    content = RichTextUploadingField(verbose_name='درباره محصول')
    price = models.CharField(verbose_name='قیمت نهایی محصول',max_length=1000)
    off_price = models.CharField(verbose_name='قیمت تخفیف خورده ( اختیاری )',null=True,blank=True,max_length=1000)
    category = models.ForeignKey(Product_Category,verbose_name='دسته بندی',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_image',verbose_name='تصویر شاخص محصول')
    buy = models.DecimalField(verbose_name = "تعداد فروش",default = 0 , max_digits=20,decimal_places=0)
    visit = models.DecimalField(verbose_name = "تعداد بازدید", default = 0 , max_digits=20,decimal_places=0)
    ranking_AVG = models.DecimalField(max_digits=20,decimal_places=0,verbose_name = "رنکینگ محصول",null = True,blank = True,default = 0)

    #! SEO FIELD

    title_seo = models.CharField(verbose_name = "عنوان برای سئو",max_length = 500)
    meta_seo = models.TextField(verbose_name = "توضیحات متا برای سئو")
    keywords = models.CharField(max_length=500,verbose_name = "کلیدواژه ها را برای سئو وارد کنید (  با علامت , جدا کنید  )")

    #! SEO FIELD

    def __str__(self) :
        return (self.name)
    
    class Meta:
        verbose_name="محصول جدید"
        verbose_name_plural="اضافه کردن محصول"

    #! REPLACE " " ---> " - "

    def save(self, *args, **kwargs):
        if self.english_name:
            self.english_name = self.english_name.replace(' ','-')
        super().save(*args, **kwargs) 

    #! REPLACE " " ---> " - "   


#! PRODUCT IMAGES

class Product_Images(models.Model):
    product = models.ForeignKey(Product,verbose_name='محصول',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_image',verbose_name='تصویر محصول')

    def __str__(self) :
        return (self.product.name)
    
    class Meta:
        verbose_name="تصویر جدید"
        verbose_name_plural="اضافه کردن تصویر محصول"


#! PRODUCT IMAGES


#! PRODUCT ATTRIBUTES

class Product_Attributes(models.Model):
    product = models.ForeignKey(Product,verbose_name='محصول',on_delete=models.CASCADE)
    attribute = models.CharField(verbose_name='ویژگی',max_length=1000)

    def __str__(self) :
        return (self.product.name)
    
    class Meta:
        verbose_name="ویژگی جدید"
        verbose_name_plural="اضافه کردن ویژگی محصول"

#! PRODUCT ATTRIBUTES

#* PRODUCT MODEL

#* USER CART

class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,verbose_name='کاربر')
    is_paid = models.BooleanField(default=False,verbose_name='پرداخت شده')

    @property
    def total_price(self):
        total = 0
        for cart_item in self.cartitems.all():
            total += (cart_item.price * cart_item.quantity)
        return int(total)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name="اضافه کردن سبد خرید"
        verbose_name_plural="سبد خرید کاربران"


class CartItem(models.Model):
     cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cartitems',verbose_name='سبد خرید')
     product = models.ForeignKey(Product, on_delete=models.CASCADE,verbose_name='محصول')
     price = models.PositiveIntegerField(verbose_name='قیمت') 
     quantity = models.PositiveSmallIntegerField(verbose_name='تعداد')

     @property 
     def total_price(self):
          return int(self.price * self.quantity)  
     
     class Meta:
        verbose_name="اضافه کردن ایتم "
        verbose_name_plural="ایتم های سبد خرید کاربران"

     def __str__(self):
          return self.product.name
     
     

#* USER CART

#* FAVORITES

class Favorites(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,verbose_name='کاربر')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,verbose_name='محصول')


    class Meta:
        verbose_name="اضافه کردن علاقه مندی "
        verbose_name_plural="علاقه مندی های کاربران"

    def __str__(self):
          return self.product.name


#* FAVORITES