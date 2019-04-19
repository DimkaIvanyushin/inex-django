from django.db import models
from cms.models import CMSPlugin
from django.urls import reverse
from djangocms_text_ckeditor.fields import HTMLField


CKEDITOR_SETTINGS_MODEL = {
    'toolbar_HTMLField': [
        ['Undo', 'Redo'],
        ['ShowBlocks'],
        ['Format', 'Styles'],
        ['Bold', 'Italic', 'Underline', '-', 'Subscript', 'Superscript', '-', 'RemoveFormat'],
    ]
}

class GroupProduct(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to = 'images/product', default = 'images/def/def.jpg')

    title_us = models.CharField(max_length=100, default = 'text')
    img_us = models.ImageField(upload_to = 'images/product', default = 'images/def/def.jpg')
    description_us = HTMLField(configuration='CKEDITOR_SETTINGS_MODEL', default = 'text')
    button_text_us = models.CharField(max_length=100, default = 'text')

    title_product = models.CharField(max_length=100, default = 'text')
    description_product = HTMLField(configuration='CKEDITOR_SETTINGS_MODEL', default = 'text')

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('product-group', args=[str(self.id)])

class Product(models.Model):
    group = models.ForeignKey(GroupProduct, on_delete = models.CASCADE)
    title = models.CharField(max_length=100)
    series = models.CharField(max_length=100)
    description = HTMLField(configuration='CKEDITOR_SETTINGS_MODEL', null=True, blank=True)
    description_specification = HTMLField(configuration='CKEDITOR_SETTINGS_MODEL', null=True, blank=True)
    spec_specification = HTMLField(configuration='CKEDITOR_SETTINGS_MODEL', null=True, blank=True)
    legend_specification = HTMLField(configuration='CKEDITOR_SETTINGS_MODEL', null=True, blank=True)

    img = models.ImageField(upload_to = 'images/product', default = 'images/def/def.jpg')
    
    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('product-detail', args=[str(self.id)])

class Specifications(models.Model):
    icon = models.FileField(upload_to= 'images/product/icon', default = 'images/def/def.jpg')
    title = models.CharField(max_length=100)
    description = models.TextField()
    products = models.ManyToManyField(Product)    

    def __str__(self):
        return str(self.title)

class AboutUsImgModel(CMSPlugin):
    text = models.CharField(max_length=100)
    text_bold = models.CharField(max_length=100)
    description = models.TextField()
    text_button = models.CharField(max_length=100)

class ThProductModel(CMSPlugin):
    text = models.CharField(max_length=100)
    description = models.TextField()

class DescProductModel(CMSPlugin):
    text = models.CharField(max_length=100)