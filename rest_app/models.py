from django.db import models
from django.forms import ModelForm
from django.core import validators

# Create your models here.
class NameModel(models.Model):
    name = models.CharField(max_length=140)
    email = models.EmailField(max_length=140)

    def __str__(self):
        return self.name
