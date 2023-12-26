from rest_framework import serializers
from .models import Purchases

class PurchasesSerializers(serializers.ModelSerializer):
    class Meta:
            model = Purchases
            fields = (  
                'product',  
                "product_name",
                'purchase_id',
                "created_at",
                "quantity_purchased",
                "product_unit_price",)