from django.conf.urls import url
from form_examples import views

urlpatterns = [

    url(r'^emp_form$',views.empForm)
]