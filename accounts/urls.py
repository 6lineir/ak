
from django.urls import path
from django.contrib.auth import views as auth_views

from .views import index, profile, Ads_list


app_name ="accounts"
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]
urlpatterns += [
    path('', index, name='panel'),
    path('profile', profile, name='profile'),
    path('ads_list', Ads_list, name='ads_list'),
    #path('addAds', addAdds)
]