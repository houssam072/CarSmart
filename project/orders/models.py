from django.db import models
from djmoney.models.fields import MoneyField

import uuid
from django.db.models.signals import post_save
from django.dispatch import receiver
from product.models import Product

    

# Create your models here.
class Order(models.Model):
    order_number = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order_title = models.CharField(max_length = 250)
    order_customers_name = models.CharField(max_length = 250, null = True, unique = True)
    mobile_phone = models.IntegerField(null = True)
    car_plate_number = models.IntegerField( null = True)
    car_type = models.CharField(max_length = 250, null = True)
    car_color = models.CharField(max_length = 250, null = True)
    car_models = models.CharField(max_length = 250, null = True)
    created_at = models.DateTimeField(auto_now_add = True, null = True)
    order_notes = models.CharField(max_length = 1200)


    def __str__(self):
        return self.order_title
    

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
    services_number = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order = models.ForeignKey(Order, on_delete  = models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity_sold = models.PositiveIntegerField()
    unit_price = MoneyField(decimal_places=2,default=0, default_currency='AED', max_digits=11,)
    gross_amount = MoneyField(decimal_places=2,default=0, default_currency='AED', max_digits=11,)
    total_amount = MoneyField(decimal_places=2,default=0, default_currency='AED', max_digits=11,)
    order_part = models.CharField(max_length = 250, choices = car_part)



    def save(self, *args, **kwargs):
        if not self.unit_price:
            self.unit_price = 10
        self.gross_amount = self.unit_price * self.quantity_sold
        self.total_amount = self.gross_amount + ((self.gross_amount * 5) / 100)
        # super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.order.order_customers_name}/{self.order.mobile_phone}/{self.product}/{self.order.created_at}"
    
class TotalService(models.Model):
    order_number = models.OneToOneField(Order, on_delete = models.CASCADE)
    services = models.ManyToManyField(Services)
    total_amount_before_vat = models.DecimalField(max_digits=11, decimal_places=2, default=0)
    total_amount_after_vat = models.DecimalField(max_digits=11, decimal_places=2, default=0)
    first_pay = MoneyField(decimal_places=2,default=0, default_currency='AED', max_digits=11,)

    def __str__(self):
        return f"{self.order_number.order_customers_name}/{self.order_number.mobile_phone}/{self.order_number.created_at}"
    

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.refresh_from_db()
        self.total_amount_before_vat = sum(service.gross_amount.amount for service in self.services.all())
        self.total_amount_after_vat = sum(service.total_amount.amount for service in self.services.all())
        super().save(*args, **kwargs)




@receiver(post_save, sender=Services)
def update_product_quantity_on_sale(sender, instance, created, **kwargs):
    if created:
        instance.product.quantity -= instance.quantity_sold
        instance.product.save()
