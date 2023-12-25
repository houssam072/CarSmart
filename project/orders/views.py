from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Order
from .serializers import OrderSerializers

# Create your views here.
class OrderList(APIView):
    def post(self, request):
        data = request.data
        print(data)
        serializer = OrderSerializers(data=data)

        if serializer.is_valid():
            print('4')
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status= status.HTTP_400_BAD_REQUEST)

        
    
        

    def get(self, request, *args, **kwargs):
        service_id = kwargs.get('id')
        phone = kwargs.get('phone')
        if service_id:
            data = Order.objects.filter(id = service_id).first() 
            serializer = OrderSerializers(data)

            return Response(serializer.data)
        
        elif phone:
            data = Order.objects.filter(mobile_phone = phone).first()
            serializer = OrderSerializers(data)

            return Response(serializer.data)
        else:
            data = Order.objects.all()
            serializer = OrderSerializers(data, many = True)
            context = {
                'orders' : serializer.data
            }
            return Response(context, status= status.HTTP_200_OK)

