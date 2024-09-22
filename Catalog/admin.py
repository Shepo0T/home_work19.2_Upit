from django.contrib import admin
from django.contrib.admin.templatetags.admin_urls import admin_urlname

from Catalog.models import Product, Category, Version


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'purchase_price', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'description')

@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('product', 'version_number', 'name_version', 'current_version')
    list_filter = ('product',)
    search_fields = ('product',)