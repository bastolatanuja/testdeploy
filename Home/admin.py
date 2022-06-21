from django.contrib import admin
from .models import Blog,Portfolio
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

