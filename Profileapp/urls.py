from django.urls import path
from Profileapp import views

urlspatterns = [
    path('', views.home, name='home'),
    path('edu', views.edu, name='edu'),
    path('interests', views.interests, name='interests'),
    path('product', views.product, name='product'),
    path('rolemodel', views.rolemodel, name='rolemodel'),
    path('showdata', views.showdata, name='showdata'),
]