from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *

# Register your models here.
class UserAdmin(BaseUserAdmin):
    ordering = ['email']
    list_display = ['email','full_name','address','public_visibility','birth_year','age']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('address','full_name','public_visibility','birth_year')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    search_fields = ('email','full_name','address','public_visibility','birth_year')
    
    def age(self, obj):
        return obj.age
    age.short_description = 'Age'
    
class OTPAdmin(admin.ModelAdmin):
    list_display=['user','otp_code','created_at']
    
    
admin.site.register(User, UserAdmin)
admin.site.register(OTP, OTPAdmin)
