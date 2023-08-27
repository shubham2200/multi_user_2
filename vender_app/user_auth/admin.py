from django.contrib import admin
from user_auth.models.abstacts_user_model import *
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('id','username','email','is_vendor','is_user')

class CustomTokenAdmin(admin.ModelAdmin):
    list_display = ('user', 'key', 'created') 

admin.site.register(User , UserAdmin)
admin.site.register(CustomToken, CustomTokenAdmin)