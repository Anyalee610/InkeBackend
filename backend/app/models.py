from django.db import models

# Create your models here.
class React(models.Model):
    firstname = models.CharField(max_length=80)
    lastname = models.CharField(max_length=80)
    email = models.CharField(max_length=80)