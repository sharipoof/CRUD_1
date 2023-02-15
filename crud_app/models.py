from django.db import models

# Create your models here.


class Items(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    price = models.IntegerField()
    category = models.CharField(max_length=50)
    