from django.contrib import admin
<<<<<<< HEAD
from .models import Blog,Portfolio, prescription,UserProfile,cashdevlivery
=======
from .models import Blog,Portfolio, cashdevlivery, prescription
>>>>>>> e7bf551d183c050600ec9dcc8286f09bda897751
from .models import Product
from .models import Cart, CartItem

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id','name','is_active')
    readonly_fields = ('slug',)

@admin.register(Portfolio)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id','name','is_active')
    readonly_fields = ('slug',)

class ProductAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product, ProductAdmin) 



class CartAdmin(admin.ModelAdmin):
    list_display = ("cart_id", "date_added",)

admin.site.register(Cart, CartAdmin)


class CartItemAdmin(admin.ModelAdmin):
    list_display = ("product", "cart", "is_active")

admin.site.register(CartItem, CartItemAdmin)

admin.site.register(prescription)
<<<<<<< HEAD
admin.site.register(cashdevlivery)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('id', 'user')

=======

admin.site.register(cashdevlivery)
>>>>>>> e7bf551d183c050600ec9dcc8286f09bda897751
