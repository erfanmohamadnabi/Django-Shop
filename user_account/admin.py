from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser,Notice,User_Address

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('user_type','profile_picture')}),
    )
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('user_type','profile_picture')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(Notice)

admin.site.register(User_Address)