from django.db import models

# Create your models here.

#* QUESTIONS MODEL

class Questions_Model(models.Model):
    title = models.CharField(verbose_name='عنوان سوال',max_length=1000)
    question = models.TextField(verbose_name='متن سوال')

    class Meta:
        verbose_name="اضافه کردن سوال"
        verbose_name_plural="سوالات متداول"

    def __str__(self):
        return (self.title)
    
#* QUESTIONS MODEL