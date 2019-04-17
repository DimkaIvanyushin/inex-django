from django.conf.urls import url
from django.conf.urls import include
from . import views

urlpatterns = [
    url(r'^$', views.showProducts,  name='product-all'),
    url(r'^(?P<id>\d+)$', views.showProduct,  name='product-detail'),
    url(r'^group/(?P<id>\d+)$', views.showGroupProduct,  name='product-group'),
]