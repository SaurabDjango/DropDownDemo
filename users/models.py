from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    is_admin = models.CharField(max_length=25)
    is_DepAdmin = models.CharField(max_length=25)
    is_Employee = models.CharField(max_length=25)