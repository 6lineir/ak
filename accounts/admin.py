from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.

UserAdmin.fieldsets += (
    ("مشخصات کاربری", {'fields' : ('is_author','special_user',)}),
)

admin.site.register(User, UserAdmin)