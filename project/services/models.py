from django.db import models
from djmoney.models.fields import MoneyField

# Create your models here.
class Services(models.Model):
    service_title = models.CharField(max_length=250,null = True)
    order = models.ForeignKey('orders.Order', on_delete = models.CASCADE)
    product = models.CharField(max_length = 250, null = True)
    service_quant = models.IntegerField()
    unit_price = MoneyField(decimal_places=2,default=0, default_currency='AED', max_digits=11,)
    gross_amount = MoneyField(decimal_places=2,default=0, default_currency='AED', max_digits=11,)
    total_amount = MoneyField(decimal_places=2,default=0, default_currency='AED', max_digits=11,)

    def save(self, *args, **kwargs):
        self.gross_amount = self.unit_price * self.service_quant
        self.total_amount = self.gross_amount - ((self.gross_amount * 5) / 100)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.service_title