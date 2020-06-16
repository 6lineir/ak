from django.db import models
from django.contrib.auth.models import AbstractUser


# calss User For Acc's
class User(AbstractUser):
    avatar = models.ImageField(upload_to='upload/avtr', verbose_name='تصویر پروفایل'),
    

