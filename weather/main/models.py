from django.db import models

# Create your models here.

class Email(models.Model):
    nome = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=200)