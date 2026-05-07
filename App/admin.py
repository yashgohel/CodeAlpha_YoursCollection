from django.contrib import admin
from .models import User, AdminUser, Product, Delivery


# Register your models here.
class UserMain(admin.ModelAdmin):
    list_display = ("fname", "lname", "email", "password")


admin.site.register(User, UserMain)


class Admin(admin.ModelAdmin):
    list_display = ("email", "password")


admin.site.register(AdminUser, Admin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ("image", "product_name", "description", "price", "quantity")


admin.site.register(Product, ProductAdmin)


class DeliveryAdmin(admin.ModelAdmin):
    list_display = ("address", "zip", "del_time")


admin.site.register(Delivery, DeliveryAdmin)
