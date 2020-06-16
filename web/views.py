
from django.shortcuts import render
from .models import addAds
# Create your views here.




def index(request):
    ads_list = addAds.objects.all()
    context = {
        'ads_list' : ads_list
    }
    return render(request, 'web/index.html', context)

def about(request):
    return render(request, 'web/about.html')

def webAds(request):
    adslist = addAds.objects.all()
    context = {
        'adslist' : adslist
    }
    return render(request, 'web/ads.html', context)