from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'home/$', views.Home, name='home'),
    url(r'^checkouts/(?P<pk>\d+)/', views.new_checkout, name='new_checkout'),
    url(r'new/$', views.New, name='new'),
    url(r'(?P<pk>\d+)/$', views.detail, name='detail'),
    url(r'(?P<pk>\d+)/bought/$', views.bought, name='bought'),
    url(r'(?P<pk>\d+)/edit/$', views.Edit, name='edit'),
    url(r'my/$', views.MyListings, name='my_listings'),
    url(r'^client_token', views.client_token, name='client_token'),
    url(r'^checkouts/create/(?P<pk>\d+)', views.create_checkout, name='create_checkout'),
    url(r'^checkouts/(?P<transaction_id>\w+)/(?P<pk>\d+)', views.show_checkout, name='show_checkout'),
]