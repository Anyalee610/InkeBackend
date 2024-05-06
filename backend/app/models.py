from django.db import models

# Create your models here.
class React(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    message = models.TextField()