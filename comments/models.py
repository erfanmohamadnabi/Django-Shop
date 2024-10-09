from django.db import models
from jdatetime import date, datetime as jdatetime
from user_account.models import CustomUser
from weblog.models import Blog

# Create your models here.


# ! GET DATE 

current_date = jdatetime.now().date()
date = str(current_date).replace("-","/")

# ! GET DATE 

# * WEBLOG COMMENTS

class Weblog_Comments(models.Model):
    weblog = models.ForeignKey(Blog,verbose_name='مقاله',on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser,verbose_name='کاربر',on_delete=models.CASCADE)
    date = models.CharField(max_length=100,verbose_name="تاریخ",default=date)
    comment = models.TextField(verbose_name='دیدگاه')

    def __str__(self):
        return (self.user.username)
    
    class Meta:
        verbose_name="دیدگاه"
        verbose_name_plural="دیدگاه های مقالات"

# * WEBLOG COMMENTS