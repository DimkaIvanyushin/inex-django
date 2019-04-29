from django.db import models
from product.models import Product
from django.urls import reverse
from cms.models import CMSPlugin
from djangocms_text_ckeditor.fields import HTMLField

class Solutions(models.Model):
    industry = models.CharField(max_length=255, verbose_name="Название")
    short_description = models.CharField(max_length=255, verbose_name="Краткое описание")
    description = HTMLField(verbose_name="Полное описание")
    implement_period = models.CharField(max_length=255, verbose_name="Срок реализации")
    img = models.ImageField(verbose_name="Изображение", upload_to = 'images/solutions', default = 'images/def/def.jpg')
    background_img = models.ImageField(upload_to = 'images/product', verbose_name="Фон", default = 'images/def/def.jpg', null=True, blank=True)

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