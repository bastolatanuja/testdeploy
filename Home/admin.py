from django.contrib import admin
from .models import Blog,Portfolio
from .models import Product

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
