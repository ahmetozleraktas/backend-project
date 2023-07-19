from django.db import models

# Create your models here.
class Stock(models.Model):
    stock_name = models.CharField(max_length=10)
    open_price = models.FloatField()
    close_price = models.FloatField()
    high_price = models.FloatField()
    low_price = models.FloatField()
    volume = models.IntegerField()
    dividend = models.FloatField()
    split = models.FloatField()
    date = models.DateField()

    def __str__(self):
        return self.stock_name