from django.conf.urls import url
from django.conf.urls import include
from . import views

urlpatterns = [
    url(r'^al$', views.showSolutions, name='solutions'),
    url(r'^group/(?P<id>\d+)$', views.showSolutionId, name='solution-detail'),
]