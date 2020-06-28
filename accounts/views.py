from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from web.models import addAds

# Create your views here.

@login_required
def index(request):
    return render(request, 'panel/index.html')
    
@login_required
def profile(request):
    return render(request, 'panel/profile.html')

@login_required
def Add_Ads(request):
    return render(request, 'panel/add-ads.html')


def Ads_list(request):
    ads_list = addAds.objects.all()
    context = {
        'ads_list' : ads_list
    }
    return render(request, 'panel/Ads-list.html', context)