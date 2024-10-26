from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from user_account.models import CustomUser
from jdatetime import date, datetime as jdatetime
import random
from django.urls import reverse
from user_account.models import User_Address

# Create your models here.


#! GET DATE & TIME

current_date = jdatetime.now().date()
date = str(current_date).replace("-","/")

#! GET DATE & TIME


#* PRODUCT CATEGORY MODEL

class Product_Category(models.Model):
    name = models.CharField(verbose_name='نام دسته بندی',max_length=1000)
    english_name = models.CharField(verbose_name='نام دسته بندی ( انگلیسی )',max_length=1000)
    image = models.ImageField(verbose_name='تصویر یا ایکون برای نمایش در صغحه اصلی')

    def __str__(self) :
        return (self.name)
    
    class Meta:
        verbose_name="دسته بندی جدید"
        verbose_name_plural="اضافه کردن دسته بندی"

    def get_absolute_url(self):
        return reverse("category_product",args=[self.english_name])

    def save(self, *args, **kwargs):
        if self.english_name:
            self.english_name = self.english_name.replace(' ','-')
        super().save(*args, **kwargs)

#* PRODUCT CATEGORY MODEL

#* PRODUCT MODEL

class Product(models.Model):
    name = models.CharField(verbose_name='نام محصول',max_length=1000)
    english_name = models.CharField(verbose_name='نام محصول ( انگلیسی )',max_length=1000)
    content = RichTextUploadingField(verbose_name='درباره محصول')
    price = models.IntegerField(verbose_name='قیمت نهایی محصول')
    discount_percentage = models.IntegerField(verbose_name='درصد تخفیف',blank=True,null=True)
    off_price = models.CharField(verbose_name='قیمت تخفیف خورده ',null=True,blank=True,max_length=1000)
    category = models.ForeignKey(Product_Category,verbose_name='دسته بندی',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_image',verbose_name='تصویر شاخص محصول')
    buy = models.DecimalField(verbose_name = "تعداد فروش",default = 0 , max_digits=20,decimal_places=0)
    visit = models.DecimalField(verbose_name = "تعداد بازدید", default = 0 , max_digits=20,decimal_places=0)
    ranking_AVG = models.DecimalField(max_digits=20,decimal_places=0,verbose_name = "رنکینگ محصول",null = True,blank = True,default = 0,editable=False)

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


    def save(self, *args, **kwargs):

        #! ADD DISCOUNT 
        
        is_new_product = self.pk is None
    
        if not is_new_product:
            old_product = Product.objects.get(pk=self.pk)
        
        if old_product.price != self.price:
            self.off_price = self.price
            if self.discount_percentage:
                original_price = int(self.price)  
                discount_amount = (self.discount_percentage / 100) * original_price
                self.price = int(original_price - discount_amount)
                self.off_price = original_price  # حفظ قیمت اصلی برای حالت ویرایش
            else:
                self.off_price = None
        else:
            # برای محصولات جدید، محاسبه تخفیف را انجام دهید
            self.off_price = self.price
            if self.discount_percentage:
                original_price = int(self.price)  
                discount_amount = (self.discount_percentage / 100) * original_price
                self.price = int(original_price - discount_amount)
            else:
                self.off_price = None

        super().save(*args, **kwargs)


        #! ADD DISCOUNT 

        #! REPLACE " " ---> " - "

        if self.english_name:
            self.english_name = self.english_name.replace(' ','-')
        super().save(*args, **kwargs) 

        #! REPLACE " " ---> " - "   

    def get_absolute_url(self):
        return reverse("detail_product",args=[self.id,self.english_name])


#! PRODUCT IMAGES

class Product_Images(models.Model):
    product = models.ForeignKey(Product,verbose_name='محصول',on_delete=models.CASCADE,related_name="images")
    image = models.ImageField(upload_to='product_image',verbose_name='تصویر محصول')

    def __str__(self) :
        return (self.product.name)
    
    class Meta:
        verbose_name="تصویر جدید"
        verbose_name_plural="اضافه کردن تصویر محصول"


#! PRODUCT IMAGES


#! PRODUCT ATTRIBUTES

class Product_Attributes(models.Model):
    product = models.ForeignKey(Product,verbose_name='محصول',on_delete=models.CASCADE,related_name="attributes")
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
    created_at = models.CharField(default=date,verbose_name='تاریخ ایجاد',max_length=1000)
    image = models.ImageField(verbose_name='عکس فیش واریزی',blank=True,null=True)
    code = models.CharField(verbose_name='کد سفارش',max_length=1000,blank=True,null=True)
    address = models.ForeignKey(User_Address,verbose_name='ادرس',blank=True,null=True,on_delete=models.CASCADE)
    phone = models.CharField(verbose_name='شماره تماس',max_length=1000,blank=True,null=True)
    name = models.CharField(verbose_name='نام و نام خانوادگی',max_length=1000,blank=True,null=True)
    total_payment = models.IntegerField(verbose_name='مبلغ کل',blank=True,null=True)
    is_paid = models.BooleanField(default=False,verbose_name='پرداخت شده')

    #! TOTAL PRICE

    @property
    def total_price(self):
        total = 0
        for cart_item in self.cartitems.all():
            total += (cart_item.price * cart_item.quantity)
            self.total_payment = total
            self.save()
        return int(total)

    #! TOTAL PRICE

   
    #! FINAL PRICE    

    @property
    def final_price(self):
        total = 0
        for cart_item in self.cartitems.all():
            total += (cart_item.price * cart_item.quantity)
        return int(total + 30000)
    
    #! FINAL PRICE    
    
    
    #! TOTAL DISCOUT   

    @property
    def total_discount(self):
        total_discount = 0
        for cart_item in self.cartitems.all():
            if cart_item.product.off_price:
                total_discount += (int(cart_item.product.off_price) - cart_item.price) * cart_item.quantity
        return int(total_discount)

    #! GENERATE CODE

    def save(self, *args, **kwargs):
        if self.code is None:
            generated_code = random.randint(10000,99999)
            self.code = str(generated_code)
        super().save(*args, **kwargs)

    #! GENERATE CODE

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


#* AMAZING OFFER

class Amazing_Offer(models.Model):
    product = models.ManyToManyField(Product,verbose_name='محصولات')

    class Meta:
        verbose_name="اضافه کردن تخفیف "
        verbose_name_plural="پیشنهاد شگفت انگیز"

    def __str__(self):
          return "پیشنهاد شگفت انگیز"

#* AMAZING OFFER