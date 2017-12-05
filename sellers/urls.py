from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'home/$', views.Home, name='home'),
    url(r'new/$', views.New, name='new'),
    url(r'new2/$', views.TwoNew, name='two_new'),
    url(r'^profile/$', views.Profile, name='profile'),
    url(r'redeem/(?P<pk>\d+)/$', views.redeem, name='redeem'),

]