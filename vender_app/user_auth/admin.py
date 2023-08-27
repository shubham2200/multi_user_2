from django.contrib import admin
from user_auth.models.abstacts_user_model import *
from user_auth.models.product_model import Product, Cart

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('id','username','email','is_vendor','is_user')

class CustomTokenAdmin(admin.ModelAdmin):
    list_display = ('user', 'key', 'created') 

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'status') 


class CartAdmin(admin.ModelAdmin):
    list_display = ( 'created_at', 'modified_at') 

admin.site.register(User , UserAdmin)
admin.site.register(CustomToken, CustomTokenAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Cart, CartAdmin)
