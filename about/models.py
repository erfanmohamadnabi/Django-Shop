from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

#* ABOUT US MODEL

class About_Us(models.Model):
    content = RichTextUploadingField(verbose_name='متن درباره ما')

    class Meta:
        verbose_name="درباره ما"
        verbose_name_plural="درباره ما"

    def __str__(self):
        return (self.content)
    
#* ABOUT US MODEL


#* ABOUT US IMAGES MODEL

class About_Gallery(models.Model):
    image = models.ImageField(verbose_name='تصویر')

    class Meta:
        verbose_name=" تصاویر"
        verbose_name_plural="گالری تصاویر"

    def __str__(self):
        return ("تصویر شماره" + str(self.id))

#* ABOUT US IMAGES MODEL