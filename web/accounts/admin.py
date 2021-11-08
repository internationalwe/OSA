from django.contrib import admin
from django.contrib.auth.forms import UsernameField
from django.db import models
from django.db.models import fields
from .models import CustomUser
from .forms import CustomUserForm
from django.contrib.auth.admin import UserAdmin

# Register your models here.


class MyCustomUserAdmin(UserAdmin):
    username = models.CharField(max_length=30, unique=True)
    form = CustomUserForm
    model = CustomUser
    list_display = ['username', 'sex', 'age']


admin.site.register(CustomUser, MyCustomUserAdmin)
