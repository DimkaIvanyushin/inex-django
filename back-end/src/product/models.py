from django.db import models
from cms.models import CMSPlugin
from django.urls import reverse
from djangocms_text_ckeditor.fields import HTMLField
 
class GroupProduct(models.Model):
    title = models.CharField(max_length=255, verbose_name="Наименование", null=True, blank=True)
    img = models.ImageField(upload_to = 'images/product', verbose_name="Изображение", default = 'images/def/def.jpg', null=True, blank=True)
    background_img = models.ImageField(upload_to = 'images/product', verbose_name="Фон", default = 'images/def/def.jpg', null=True, blank=True)
    title_full = models.CharField(max_length=255, verbose_name="Полное наименование", null=True, blank=True)
    description = HTMLField(verbose_name="Описание", null=True, blank=True)

    title_product = models.CharField(max_length=255, verbose_name="Текст", null=True, blank=True)
    description_product = HTMLField(verbose_name="Текст описания", null=True, blank=True)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('product-group', args=[str(self.id)])

class Product(models.Model):
    group = models.ForeignKey(GroupProduct, on_delete = models.CASCADE)
    title = models.CharField(max_length=100, verbose_name="Наименование")
    series = models.CharField(max_length=100, verbose_name="Серия")
    description = models.TextField(null=True, blank=True, verbose_name="Краткое описание")
    description_specification = HTMLField(null=True, blank=True, verbose_name="Полное описание")
    spec_specification = HTMLField(null=True, blank=True, verbose_name="Технические характеристики")
    legend_specification = HTMLField(null=True, blank=True, verbose_name="Условные обозначения")
    price = models.FloatField(default=0, verbose_name="Цена")
    
    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('product-detail', args=[str(self.id)])

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images')
    image = models.ImageField(upload_to = 'images/product', default = 'images/def/def.jpg')

    def image_tag(self):
        return u'<img src="%s" height="100px" />' % self.image.url

    image_tag.short_description = 'Изображение'
    image_tag.allow_tags = True

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

class BreadcrumbsProductModel(CMSPlugin):
    text = models.CharField(max_length=255, verbose_name="Текст", null=True, blank=True)
    text_bold = models.CharField(max_length=255, verbose_name="Жирный текст", null=True, blank=True)
    img = models.ImageField(upload_to = 'images/product', verbose_name="Изображение", default = 'images/def/def.jpg', null=True, blank=True)