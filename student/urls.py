from django.conf.urls import url
from student import views

urlpatterns = [
    url(r'^create$', views.create),
    url(r'^index$', views.index),
    url(r'^view/(?P<id>[0-9]+)$', views.view),
    url(r'^update/(?P<id>[0-9]+)$', views.update),
    url(r'^delete/(?P<id>[0-9]+)$', views.delete),
]
