from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^baltimore.js$', views.baltimore_temperature, name='baltimore_temperature'),
    url(r'^hawi.js$', views.hawi_temperature, name='hawi_temperature'),
    url(r'^woodshole.js$', views.woodshole_temperature, name='woodshole_temperature'),
]
