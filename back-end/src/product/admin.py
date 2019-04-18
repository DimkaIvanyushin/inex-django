from django.contrib import admin
from django import forms

from .models import GroupProduct, Product, Specifications

admin.site.register(Specifications)
admin.site.register(GroupProduct)
admin.site.register(Product)