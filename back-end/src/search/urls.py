from django.conf.urls import url
from django.conf.urls import include
from . import views

urlpatterns = [
    url(r'^show$', views.show,  name='search-show'),
]