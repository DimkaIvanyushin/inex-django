from django.db import models
from cms.models import CMSPlugin
from djangocms_text_ckeditor.fields import HTMLField

BG_CHOICES = (
    ('bg-gray', 'Gray'),
    ('bg-primary-darker', 'Darker'),
    ('bg-white', 'White'),
)

class MenuBarModel(CMSPlugin):
    phone_number = models.CharField(max_length=30, default="0-000-000-000")
    phone_number_2 = models.CharField(max_length=30, default="0-000-000-000")
    email = models.CharField(max_length=30, default="info@admin.org")
    locations = models.CharField(max_length=100, default="default")
    button_text = models.CharField(max_length=30, default="default")

class AboutUsModel(CMSPlugin):
    title = models.CharField(max_length=30, default="default", null=True, blank=True)
    description = HTMLField(default="default")
    text_button = models.CharField(max_length=30, default="default")
    img = models.ImageField(upload_to = 'images/about-us', default = 'images/def/def.jpg')
    
    bg_color = models.CharField(max_length=30, choices=BG_CHOICES, default = BG_CHOICES[0])

class SliderModel(CMSPlugin):
    name_slider = models.CharField(max_length=30, default="default.")

class SliderItem(CMSPlugin):
    text_bold = models.CharField(max_length=120, default="default")
    text = models.CharField(max_length=120, default="default.")
    text_button = models.CharField(max_length=30, default="default.")
    img = models.ImageField(upload_to = 'images/slider', default = 'images/def/def.jpg')

class SmallFeaturesModel(CMSPlugin):
    icon_code = models.CharField(max_length=30, default="far fa-user")
    icon_image = models.ImageField(upload_to = 'images/smallFeatures', verbose_name="Изображение", default = 'images/def/def.jpg', null=True, blank=True)
    title = models.CharField(max_length=30, default="default.")
    description = models.TextField(default="default.")
    bg_color = models.CharField(max_length=30, choices=BG_CHOICES, default = BG_CHOICES[0])

class AlertCtaModel(CMSPlugin):
    text = HTMLField(default="default")
    text_button = models.CharField(max_length=30, default="default.")
    bg_color = models.CharField(max_length=30, choices=BG_CHOICES, default = BG_CHOICES[0])

class ProductSectionModel(CMSPlugin):
    title = models.CharField(max_length=30, default="default")
    text = models.TextField(default="default")
    bg_color = models.CharField(max_length=30, choices=BG_CHOICES, default = BG_CHOICES[0])

class SolutionSectionModel(CMSPlugin):
    title = models.CharField(max_length=30, default="default")
    descriptions = models.TextField(default="default text")
    bg_color = models.CharField(max_length=30, choices=BG_CHOICES, default = BG_CHOICES[0])

class PriceModel(CMSPlugin):
    title = models.CharField(max_length=30, default="default")
    bg_color = models.CharField(max_length=30, choices=BG_CHOICES, default = BG_CHOICES[0])

class PriceBoxModel(CMSPlugin):
    title = models.CharField(max_length=30, default="default")
    price = models.CharField(max_length=30, default="default")
    descriptoin = models.TextField(default="default")

class AlertMdlModel(CMSPlugin):
    title = models.CharField(max_length=100, default="default")
    title_bold = models.CharField(max_length=30, default="default")
    descriptoin = models.TextField(default="default")
    button_title = models.CharField(max_length=30, default="default")
    bg_color = models.CharField(max_length=30, choices=BG_CHOICES, default = BG_CHOICES[0])

class ContactUsModel(CMSPlugin):
    bg_color = models.CharField(max_length=30, choices=BG_CHOICES, default = BG_CHOICES[0])

class LastBlogModel(CMSPlugin):
    title = models.CharField(max_length=30, default="Latest Blog Posts")
    bg_color = models.CharField(max_length=30, choices=BG_CHOICES, default = BG_CHOICES[0])

class RecallModel(CMSPlugin):
    title = models.CharField(max_length=30, default="Testimonials")
    bg_color = models.CharField(max_length=30, choices=BG_CHOICES, default = BG_CHOICES[0])

class RecallBoxModel(CMSPlugin):
    avatar = models.ImageField(upload_to = 'images/recall', default = 'images/def/def.jpg')
    name = models.CharField(max_length=30, default="default")
    post = models.CharField(max_length=30, default="default")
    text = models.TextField(default="default")

class FooterModel(CMSPlugin):
    header_1 = models.CharField(max_length=30, default="Testimonials")
    header_2 = models.CharField(max_length=30, default="Testimonials")
    header_3 = models.CharField(max_length=30, default="Testimonials")
    description_1 = models.TextField(default="default")
    description_2 = models.TextField(default="default")