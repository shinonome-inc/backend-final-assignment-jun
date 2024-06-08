from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField()


# 引数にblank=Falseの指定は不要。デフォルトでFalseになっている。

# class FriendShip(models.Model):
