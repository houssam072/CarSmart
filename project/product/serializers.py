from rest_framework import serializers
from .models import Product

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
            model = Product
            fields = (    
                'id',
                "product_name",
                "product_color",
                "product_ratio",
                "quantity",)