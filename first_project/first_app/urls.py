from django.conf.urls import url
from first_app import views
from django.urls import path

urlpatterns =   [
    path('',views.index,name='index'),
    path('forms/',views.form_name_view,name='form_name'),
]