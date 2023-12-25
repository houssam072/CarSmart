from rest_framework import serializers
from .models import Services

class ServicesSerializers(serializers.ModelSerializer):
    class Meta:
            model = Services
            fields = (    
"service_title",
'order',
"product",
"service_quant",
"unit_price",
"gross_amount")