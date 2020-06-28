
from django.urls import path
from .views import *


app_name ="web"
urlpatterns = [
    path('', index, name='Home'),
    path('ads/<slug:slug>', Ads_detail, name='ads_detail'),
    path('ads/', webAds, name='ads'),
    path('about', about , name='about'), 
    
]   