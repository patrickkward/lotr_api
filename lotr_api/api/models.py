from django.db import models


# Create your models here.

class Films(models.Model):
    film_name = models.CharField(max_length=200)
    nominations = models.CharField(max_length=200, default='')
