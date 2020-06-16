from django.contrib import admin
from .models import *
# Register your models here.
admin.site.site_header = "داشبورد اصلی وب اپلیکیشن"

admin.site.register(City)
admin.site.register(addAds)
admin.site.register(category)