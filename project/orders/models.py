from django.db import models
import uuid
# from project.services.models import Services
    

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

