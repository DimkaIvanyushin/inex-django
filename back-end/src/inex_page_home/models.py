from django.db import models
from cms.models import CMSPlugin

class MenuBarModel(CMSPlugin):
    phone_number = models.CharField(max_length=30, default="0-000-000-000")
    phone_number_2 = models.CharField(max_length=30, default="0-000-000-000")
    locations = models.CharField(max_length=30, default="Улица Правды 30, Витебск 210029")

    def __str__(self):
        return self.phone_number

class AboutUsModel(CMSPlugin):
    title = models.CharField(max_length=30, default="Text")
    description = models.TextField(default="Description")
    img = models.ImageField(upload_to = 'media/static/images/', default = 'static/images/work.jpg')

    def __str__(self):
        return self.title