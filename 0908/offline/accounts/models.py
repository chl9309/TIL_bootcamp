from operator import mod
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# 내가 모델 만들 것 아님 장고가 기본으로 가진 모델 만들 것
class User(AbstractUser):
    pass
