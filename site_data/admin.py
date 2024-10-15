from django.contrib import admin
from .models import Site_Data

# Register your models here.

class Data_Admin(admin.ModelAdmin):
    pass
    # def has_add_permission(self, request, obj=None):
    #     return False


admin.site.register(Site_Data,Data_Admin)

admin.site.site_header = "مدیریت سایت فروشگاهی"

