from django.db import models
from django.contrib.auth.models import AbstractUser
CHOICES=[('Male','Male'),
         ('Female','Female')]

class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    Image = models.ImageField(upload_to='mypics/%Y/%m/%d',null=True,blank=True)
    Gender = models.CharField(max_length=6,choices=CHOICES)


# class Userprofile(models.Model):
# 	Username=models.ForeignKey(User,on_delete=models.CASCADE)
# 	Image = models.ImageField(upload_to='mypics/%Y/%m/%d',null=True,blank=True)