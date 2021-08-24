from django.urls import path

#from .views import *
from . import views

urlpatterns=[
path('',views.index,name='index'),
path('about.html',views.about,name='about'),
path('new',views.new,name='index'),
path('new',views.new,name='index'),

]