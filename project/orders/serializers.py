from rest_framework import serializers
from .models import Order

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
'order_part',
"first_pay",
)

       
