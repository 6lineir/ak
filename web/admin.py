from django.contrib import admin
from .models import *
# Register your models here.
admin.site.site_header = "داشبورد اصلی وب اپلیکیشن"

class addAdsAdmin(admin.ModelAdmin):
    list_display = ('title','status','jpublish')



admin.site.register(City)
admin.site.register(addAds, addAdsAdmin)
admin.site.register(category)