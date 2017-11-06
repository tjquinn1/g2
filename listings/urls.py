from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'home/$', views.Home, name='home'),
    url(r'new/$', views.New, name='new'),
    url(r'(?P<pk>\d+)/$', views.detail, name='detail'),
    url(r'(?P<pk>\d+)/bought/$', views.bought, name='bought'),

]