from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    sex = models.CharField(
        max_length=1,
        choices=(
            ('남', '남자'),
            ('여', '여자'),
        ), verbose_name="성별"
    )
    age = models.IntegerField(null=True, verbose_name="나이")
