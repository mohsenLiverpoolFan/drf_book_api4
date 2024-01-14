from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class CustomUser(User):
    name = models.CharField(max_length=200)
