from django.db import models

# Create your models here.
class UserLogin(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=10)
    email = models.EmailField(max_length=30)
    password1 = models.CharField(max_length=15)
    password2 = models.CharField(max_length=15)
