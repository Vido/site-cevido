from django.db import models

# Create your models here.
class FilterKind(models.Model):
    title = models.CharField(max_length=128)
    form_template = models.CharField(max_length=128)
    list_template = models.CharField(max_length=128)

