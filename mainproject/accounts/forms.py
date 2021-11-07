from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.db.models import fields
from .models import CustomUser


class CustomUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'age', 'sex']
