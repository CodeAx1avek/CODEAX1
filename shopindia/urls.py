from django.contrib import admin
from django.urls import path
from shopindia import views

urlpatterns = [
    path('',views.index,name='index'),
    path('clients',views.clients,name='clients'),
    path('contact',views.contact,name='contact')
]
