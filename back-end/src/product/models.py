from django.db import models
from django.urls import reverse

class GroupProduct(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to = 'images/product', default = 'images/def/def.jpg')

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
