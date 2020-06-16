from django.db import models
from accounts.models import User
from django.utils import timezone
# Create your models here.

class City(models.Model):
    cty = models.CharField(max_length=30, verbose_name='استان')
    def __str__(self):
        return self.cty
    class Meta:
        verbose_name = "استان"
        verbose_name_plural = "استان ها"

class mantg(models.Model):
    mntg = models.CharField(max_length=48, verbose_name='ناحیه')



class category(models.Model):
    category = models.CharField(max_length=30, verbose_name='دسته بندی')
    cat_slug = models.SlugField(verbose_name='لینک دسته بندی')
    def __str__(self):
        return self.category
    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"



class addAds(models.Model):
    STATUS_CHOICES = (
        ('f', "پیش نویس"),
	    ('d', 'درانتظار تایید'),
		('p', "منتشر شده"),
        ('v', 'آگهی ویژه'),
	)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='articles', verbose_name="نویسنده")
    title = models.CharField(max_length=52 , verbose_name='عنوان آگهی')
    category = models.ManyToManyField(category, verbose_name='دسته بندی')
    city = models.ManyToManyField(City, verbose_name='استان')
    body = models.TextField(verbose_name='توضیحات آگهی')
    price = models.BigIntegerField(verbose_name='قیمت')
    Adspic = models.ImageField(upload_to='upload/ads_pic', verbose_name='تصویر آگهی')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name="وضعیت")
    timepub = models.DateTimeField(default=timezone.now, verbose_name='زمان انتشار')
    def __str__(self):
        return self.title
    class Meta:
	    verbose_name = "آگهی"
	    verbose_name_plural = "آگهی ها"