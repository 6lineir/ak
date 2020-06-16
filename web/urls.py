
from django.urls import path
from .views import *


app_name ="web"
urlpatterns = [
    path('', index, name='Home'),
    #path('ads', webAds, name='adslist'),
    path('ads/', webAds, name='ads'),
    path('about', about , name='about'), 
    
]   