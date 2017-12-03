from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^$', views.bought_listings, name='bought_listings'),
    url(r'^redeem_detail/(?P<pk>\d+)', views.redeem_detail, name='redeem_detail'),
    url(r'redeem/(?P<pk>\d+)', views.redeem, name='redeem'),
    
]