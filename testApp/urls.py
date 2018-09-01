from django.conf.urls import url

from testApp import views

urlpatterns = [

    url(r'^hello_django$', views.helloDjango),
    url(r'^hello_python$', views.helloPython)
]