from django.db import models

# Create your models here.
class Client(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    name = models.CharField(max_length=200)
