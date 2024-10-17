from django.contrib import admin
from .models import *

# Register your models here.

class About_Admin(admin.ModelAdmin):
    pass
    # def has_add_permission(self, request, obj=None):
    #     return False

admin.site.register(About_Us,About_Admin)
admin.site.register(About_Gallery)