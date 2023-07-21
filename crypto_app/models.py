from django.db import models

# Create your models here.

class Crypto(models.Model):
    symbol = models.CharField(max_length=100)
    price = models.FloatField()
    timestamp = models.DateTimeField()
    def __str__(self):
        return self.symbol