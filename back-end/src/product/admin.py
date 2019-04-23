from django.contrib import admin
from django import forms
from .models import *

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    inlines = [ ProductImageInline, ]

admin.site.register(Specifications)
admin.site.register(GroupProduct)
admin.site.register(Product, ProductAdmin)