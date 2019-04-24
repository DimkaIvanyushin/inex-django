from django.contrib import admin
from django import forms
from .models import *

class SpecificationsInline(admin.TabularInline):
    model = Specifications.products.through
    extra = 0
    
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0
    readonly_fields = ('image_tag',)

class ProductAdmin(admin.ModelAdmin):
    inlines = [ ProductImageInline, SpecificationsInline ]
    list_display = ('title', 'group', 'series')
    list_filter = ('group', 'series')

    fieldsets = (
        ('Описание', {
            'fields': ('group',('title', 'series'), 'description')
        }),
        ('Технические характеристики', {
            'fields': ('description_specification', 'spec_specification', 'legend_specification')
        }),
    )


   
admin.site.register(Specifications)
admin.site.register(GroupProduct)
admin.site.register(Product, ProductAdmin)