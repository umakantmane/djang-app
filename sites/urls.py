from django.conf.urls import url
from sites import views

urlpatterns = [
    url(r'^signup$', views.UserSignup),
    url(r'^signin$', views.UserSignin),
    url(r'^home$', views.Home),
    url(r'^logout$', views.UserLogout),
]