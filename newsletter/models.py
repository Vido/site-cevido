from django.db import models

# Create your models here.


class Subscriber(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    last_time_send = models.DateTimeField(auto_now=True)
    times_sent = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    email = models.EmailField(unique=True, null=False)

