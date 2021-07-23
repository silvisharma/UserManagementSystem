from django.db import models
from django.core import validators

class Blog(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=200)


class ShowUser(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)


class MyModel:
    pass