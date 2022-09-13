from django.db import models

# Create your models here.
class Event(models.Model):
    game = models.CharField(max_length=200)
    date = models.CharField(max_length=20)
    time = models.CharField(max_length=30)