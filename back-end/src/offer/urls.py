from django.conf.urls import url
from django.conf.urls import include
from . import views

urlpatterns = [
    url(r'^show$', views.show,  name='offer-show'),
    url(r'^generate/PDF$', views.getOfferPDF,  name='offer-generate-pdf'),
    url(r'^remove/item/(?P<id>\d+)$', views.removeItem,  name='offer-remove-item'),
    url(r'^remove/item/all$', views.removeItemAll,  name='offer-remove-item-all')
]