from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^baltimore.js$', views.baltimore_temperature, name='baltimore_temperature'),
]
