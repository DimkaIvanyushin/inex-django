from django.conf.urls import url
from django.conf.urls import include
from . import views

urlpatterns = [
    url(r'^all$', views.showProducts,  name='product-all'),
    url(r'^item/(?P<id>\d+)$', views.showProduct,  name='product-detail'),
    url(r'^item/add/(?P<id>\d+)$', views.addProduct,  name='product-add'),
    url(r'^item/remove/(?P<id>\d+)$', views.removeProduct,  name='product-remove'),
    url(r'^group/(?P<id>\d+)$', views.showGroupProduct,  name='product-group'),
]