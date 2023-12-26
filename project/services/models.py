from django.db import models
from djmoney.models.fields import MoneyField

car_part = (
    ('front glass', 'front glass'),
    ('Back glass', 'Back glass'),
    ('Pair of front windows', 'Pair of front windows'),
    ('Pair of rear windows', 'Pair of rear windows'),
    ('Front lighting', 'Front lighting'),
    ('Backlight', 'Backlight'),
    ('allPart', 'allPart'),
)


# Create your models here.
class Services(models.Model):
    order = models.ForeignKey('orders.Order', on_delete  = models.CASCADE)
    product = models.ForeignKey('product.Product', on_delete = models.CASCADE)
    service_quant = models.IntegerField()
    unit_price = MoneyField(decimal_places=2,default=0, default_currency='AED', max_digits=11,)
    gross_amount = MoneyField(decimal_places=2,default=0, default_currency='AED', max_digits=11,)
    total_amount = MoneyField(decimal_places=2,default=0, default_currency='AED', max_digits=11,)
    first_pay = MoneyField(decimal_places=2,default=0, default_currency='AED', max_digits=11,)
    order_part = models.CharField(max_length = 250, choices = car_part)



    def save(self, *args, **kwargs):
        if not self.unit_price:
            self.unit_price = self.product.product_unit_price
        self.gross_amount = self.unit_price * self.service_quant
        self.total_amount = self.gross_amount + ((self.gross_amount * 5) / 100)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.order.order_customers_name}/{self.order.mobile_phone}/{self.product}/{self.order.created_at}"