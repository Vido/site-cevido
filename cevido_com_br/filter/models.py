from django.db import models

# Create your models here.
class FilterKind(models.Model):
    title = models.CharField(max_length=128)
    # Stores a .html file with the custom form
    form_template = models.CharField(max_length=128)
    # Stores a custom property list
    list_template = models.CharField(max_length=128)

