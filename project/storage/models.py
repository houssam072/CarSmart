from django.db import models
from djmoney.models.fields import MoneyField
from product.models import Product
import uuid
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Purchases(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    product_name = models.CharField(max_length = 250)
    purchase_id= models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add = True, null = True)
    quantity_purchased = models.PositiveIntegerField()
    product_unit_price = MoneyField(decimal_places=2,default=0, default_currency='AED', max_digits=11,)


    def save(self, *args, **kwargs):
        self.product_name = self.product.product_name
        super().save(*args, **kwargs)




    def __str__(self): 
        return self.product_name
    
@receiver(post_save, sender=Purchases)
def update_product_quantity(sender, instance, created, **kwargs):
    if created:
        instance.product.quantity += instance.quantity_purchased
        instance.product.save()


