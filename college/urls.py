from django.conf.urls import url
from college import views

urlpatterns = [

    url(r'^hello_college$', views.helloCollege)
]