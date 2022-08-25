from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    Image = models.ImageField(upload_to='images', blank=True, null=True)
    Name = models.CharField(max_length=50)
    # Username = models.CharField(max_length=40)
    Website = models.CharField(max_length=50, blank=True, null=True)
    Bio = models.CharField(max_length=100, blank=True, null=True)
    Followings = models.ManyToManyField('self', symmetrical=False, related_name='followers', default=0)
