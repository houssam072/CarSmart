from decimal import Decimal
from django.db import models
from djmoney.models.fields import MoneyField

from django.core.validators import MinValueValidator, MaxValueValidator
PERCENTAGE_VALIDATOR = [MinValueValidator(0), MaxValueValidator(100)]



# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length = 250)
    product_color = models.CharField(max_length = 250)
    product_ratio =  models.DecimalField(max_digits=3, decimal_places=0, default=Decimal(0), validators=PERCENTAGE_VALIDATOR)
    quantity = models.PositiveIntegerField(default=0)



    def __str__(self):
        return self.product_name