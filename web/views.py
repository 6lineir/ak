
from django.shortcuts import render
from .models import addAds, category
# Create your views here.




def index(request):
    ads_list = addAds.objects.all()[0:6]
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
    
def Ads_detail(request, slug):
    ads_detail = addAds.objects.get(slug=slug)
    ads_cat = category.objects.all()
    context = {
        'ads_detail' : ads_detail,
        'ads_cat' : ads_cat
    }
    print (ads_detail)
    return render(request, 'web/ads-detail.html', context)