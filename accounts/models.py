from django.db import models
from django.contrib.auth.models import AbstractUser


# calss User For Acc's
class User(AbstractUser):
 #       STATUS_CHOICES = (
  #      ('a', "مدیر"),
	#    ('u', 'کاربر'),
	#	('v', "کاربر ویژه"),
	#)

    avatar = models.ImageField(upload_to='upload/avtr', verbose_name='تصویر پروفایل'),
    #status = .CharField(max_length=1, choices=STATUS_CHOICES, verbose_name="گروه کاربری")
