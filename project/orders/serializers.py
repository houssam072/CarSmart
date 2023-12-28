from rest_framework import serializers
from .models import Order, Services, TotalService


class OrderSerializers(serializers.ModelSerializer):
    class Meta:
            model = Order
            fields = (   
                  
'order_number',
"order_title",
"order_customers_name",
"mobile_phone",
"car_plate_number",
"car_type",
"car_color",
"car_models",
"order_notes",
'created_at',
)
            

            

class ServicesSerializers(serializers.ModelSerializer):
    class Meta:
            model = Services
            fields = (  
'id',
'order',
"product",
"quantity_sold",
# "unit_price",
# "gross_amount",
# "total_amount",
"order_part")           

class TotalServicesSerializers(serializers.ModelSerializer):
    class Meta:
            model = TotalService
            fields = (    
'order_number',
"services",
"total_amount_before_vat",
"total_amount_after_vat",
"first_pay",)

       
