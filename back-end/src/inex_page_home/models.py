from django.db import models
from cms.models import CMSPlugin

class MenuBarModel(CMSPlugin):
    phone_number = models.CharField(max_length=30, default="0-000-000-000")
    phone_number_2 = models.CharField(max_length=30, default="0-000-000-000")
    email = models.CharField(max_length=30, default="info@admin.org")
    locations = models.CharField(max_length=100, default="default")
    button_text = models.CharField(max_length=30, default="default")

class AboutUsModel(CMSPlugin):
    title = models.CharField(max_length=30, default="default")
    description = models.TextField(default="default")
    text_button = models.CharField(max_length=30, default="default")
    img = models.ImageField(upload_to = 'images/about-us', default = 'images/def/def.jpg')

class SliderModel(CMSPlugin):
    name_slider = models.CharField(max_length=30, default="default.")

class SliderItem(CMSPlugin):
    text_bold = models.CharField(max_length=120, default="default")
    text = models.CharField(max_length=120, default="default.")
    text_button = models.CharField(max_length=30, default="default.")
    img = models.ImageField(upload_to = 'images/slider', default = 'images/def/def.jpg')

class SmallFeaturesModel(CMSPlugin):
    icon_code = models.CharField(max_length=30, default="far fa-user")
    title = models.CharField(max_length=30, default="default.")
    description = models.TextField(default="default.")

class AlertCtaModel(CMSPlugin):
    text = models.CharField(max_length=30, default="default")
    text_button = models.CharField(max_length=30, default="default.")

class ProductSectionModel(CMSPlugin):
    title = models.CharField(max_length=30, default="default")
    text = models.TextField(default="default")

class PriceModel(CMSPlugin):
    title = models.CharField(max_length=30, default="default")

class PriceBoxModel(CMSPlugin):
    title = models.CharField(max_length=30, default="default")
    price = models.CharField(max_length=30, default="default")
    descriptoin = models.TextField(default="default")

class AlertMdlModel(CMSPlugin):
    title = models.CharField(max_length=30, default="default")
    title_bold = models.CharField(max_length=30, default="default")
    descriptoin = models.TextField(default="default")
    button_title = models.CharField(max_length=30, default="default")

class LastBlogModel(CMSPlugin):
    title = models.CharField(max_length=30, default="Latest Blog Posts")

class RecallModel(CMSPlugin):
    title = models.CharField(max_length=30, default="Testimonials")

class RecallBoxModel(CMSPlugin):
    avatar = models.ImageField(upload_to = 'images/recall', default = 'images/def/def.jpg')
    name = models.CharField(max_length=30, default="default")
    post = models.CharField(max_length=30, default="default")
    text = models.TextField(default="default")