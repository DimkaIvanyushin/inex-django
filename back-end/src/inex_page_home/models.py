from django.db import models
from cms.models import CMSPlugin

class MenuBarModel(CMSPlugin):
    phone_number = models.CharField(max_length=30, default="0-000-000-000")
    phone_number_2 = models.CharField(max_length=30, default="0-000-000-000")
    locations = models.CharField(max_length=30, default="Улица Правды 30, Витебск 210029")
    button_text = models.CharField(max_length=30, default="Заказать звонок")


class AboutUsModel(CMSPlugin):
    title = models.CharField(max_length=30, default="Text")
    description = models.TextField(default="Description")
    img = models.ImageField(upload_to = 'images/about-us', default = 'images/def/def.jpg')


class SliderModel(CMSPlugin):
    name_slider = models.CharField(max_length=30, default="Text.")
    allow_children = True


class SliderItem(CMSPlugin):
    text_bold = models.CharField(max_length=30, default="Text. Text.")
    text = models.CharField(max_length=30, default="Text.")
    img = models.ImageField(upload_to = 'images/slider', default = 'images/def/def.jpg')


class SmallFeaturesModel(CMSPlugin):
    icon_code = models.CharField(max_length=30, default="far fa-user")
    title = models.CharField(max_length=30, default="Text.")
    description = models.TextField(default="Text.")

class AlertCtaModel(CMSPlugin):
    text = models.CharField(max_length=30, default="text")
    text_button = models.CharField(max_length=30, default="Text.")