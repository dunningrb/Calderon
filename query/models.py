from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified_date = models.DateTimeField(auto_now=True)
    post = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
