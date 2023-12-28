from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializers
from .models import Product
from rest_framework.permissions import AllowAny  

# Create your views here.
class ProductList(APIView):
    permission_classes = [AllowAny] 

    def post(self, request):
        data = request.data
        serializer = ProductSerializers(data= data)
        if serializer.is_valid():
            serializer.save()
            return Response(status = status.HTTP_201_CREATED)
        return Response(status = status.HTTP_400_BAD_REQUEST)
        

    
    def get(self, request):
        data = Product.objects.all()
        serializer = ProductSerializers(data, many = True)
        context = {
            'product' : serializer.data
        }
        return Response(context, status= status.HTTP_200_OK)