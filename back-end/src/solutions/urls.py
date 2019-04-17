from django.conf.urls import url
from django.conf.urls import include
from . import views

urlpatterns = [
    url(r'^all', views.showSolutions,  name='solution-all'),
    url(r'^(?P<id>\d+)$', views.showSolutionId,  name='solution-id'),
]