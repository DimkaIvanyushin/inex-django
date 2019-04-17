from django.db import models
from product.models import Product
from django.urls import reverse
from cms.models import CMSPlugin

class Solutions(models.Model):
    industry = models.CharField(max_length=100, default="default")
    short_description = models.CharField(max_length=250, default="default")
    description = models.TextField(default="default")
    implement_period = models.CharField(max_length=100, default="default")
    img = models.ImageField(upload_to = 'images/solutions', default = 'images/def/def.jpg')

    products = models.ManyToManyField(Product)

    def get_absolute_url(self):
        return reverse('solution-detail', args=[str(self.id)])

    def __str__(self):
        return str(self.industry)

class SolutionsPluginModel(CMSPlugin):
    title = models.CharField(max_length=30, default="default")
    descriptoin = models.TextField(default="default")


class BreadcrumbsSolution(CMSPlugin):
    title = models.CharField(max_length=100, default="default")
    title_bold = models.CharField(max_length=100, default="default")
    img = models.ImageField(upload_to = 'images/breadcrumbsSolution', default = 'images/def/def.jpg')