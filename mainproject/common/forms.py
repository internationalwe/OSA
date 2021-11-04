from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#가입할 때 User들이 적어야하는 양식들
class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email")