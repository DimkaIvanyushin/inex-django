from django.db import models
from cms.models import CMSPlugin
from django.urls import reverse
from cms.models.fields import PlaceholderField

class GroupProduct(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to = 'images/product', default = 'images/def/def.jpg')

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('product-group', args=[str(self.id)])

class Product(models.Model):
    group = models.ForeignKey(GroupProduct, on_delete = models.CASCADE)

    title = models.CharField(max_length=100)
    series = models.CharField(max_length=100)
    description = models.TextField()
    img = models.ImageField(upload_to = 'images/product', default = 'images/def/def.jpg')

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('product-detail', args=[str(self.id)])

class AboutUsImgModel(CMSPlugin):
    text = models.CharField(max_length=100)
    text_bold = models.CharField(max_length=100)
    description = models.TextField()
    text_button = models.CharField(max_length=100)
    test =  PlaceholderField('test')

class ThProductModel(CMSPlugin):
    text = models.CharField(max_length=100)
    description = models.TextField()

class DescProductModel(CMSPlugin):
    text = models.CharField(max_length=100)