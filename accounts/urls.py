from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    # url(r"login/$", views.LoginView.as_view(), name="login"),
    url(r"logout/$", views.LogoutView.as_view(), name="logout"),
    url(r"signup/$", views.SignUp.as_view(), name="signup"),
    url(r'edit/$', views.Edit, name='edit'),
    url(r'^login/$', views.login, name='login'),
    url(r'^profile/$', views.Profile, name='profile'),
]