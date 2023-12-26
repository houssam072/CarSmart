from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Purchases
from .serializers import PurchasesSerializers
from product.models import Product

# Create your views here.
class PurchasesList(APIView):
    def post(self, request):
        
        serializer = PurchasesSerializers(data= request.data)
        if serializer.is_valid():
            # product = serializer.validated_data['product']
            # quantity_purchased = serializer.validated_data['quantity_purchased']
            # product.quantity += quantity_purchased
            # # product.save()

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        data = Purchases.objects.all()
        serializer = PurchasesSerializers(data, many = True)
        context = {
            'purchases' : serializer.data
        }
        return Response(context, status= status.HTTP_200_OK)
