from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='image', null=True, blank=True, default="default.png")
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
