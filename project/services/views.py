from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Services
from .serializers import ServicesSerializers

# Create your views here.
class ServicesList(APIView):
    def post(self, request):
        data = request.data
        serializer = ServicesSerializers(data= data)
        if serializer.is_valid():
            serializer.save()
            return Response(status= status.HTTP_201_CREATED)
        return Response(status= status.HTTP_400_BAD_REQUEST)
        
        

    def get(self, request):
        data = Services.objects.all()
        serializer = ServicesSerializers(data, many = True)
        context = {
            'orders' : serializer.data
        }
        return Response(context, status= status.HTTP_200_OK)
    
    
