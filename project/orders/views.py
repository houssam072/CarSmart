from django.shortcuts import render
from rest_framework.decorators import APIView, permission_classes
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Order, Services, TotalService
from .serializers import OrderSerializers, ServicesSerializers, TotalServicesSerializers
from product.models import Product
from rest_framework.permissions import AllowAny  
# Create your views here.

class OrderList(APIView):
    
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        data = request.data
        print(data)
        serializer = OrderSerializers(data=data)

        if serializer.is_valid():
            serializer.save()
            # last_order = Order.objects.last()
            # context = {
            #     'last_order' : last_order
            # }
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


    
    def delete(self, request, order_number):
        try:
            order = Order.objects.get(order_number=order_number)
            order.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Order.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        


class ServicesList(APIView):
    def post(self, request, order):
        try:
            product = Order.objects.get(id=order)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        data = request.data
        serializer = ServicesSerializers(data= data)
        if serializer.is_valid():
            if product.quantity >= serializer.validated_data['quantity_sold']:
                product.quantity -= serializer.validated_data['quantity_sold']
                product.save()
                serializer.save(product=product)
                # serializer.save()
                return Response(status=status.HTTP_201_CREATED)
            else:
                return Response({'error': 'Not enough quantity available for the sale.'}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        
    def get(self, request, *args, **kwargs):
        order = kwargs.get('order')
        
        if order:
            data = Services.objects.filter(order = order)
            serializer = ServicesSerializers(data, many = True)
            return Response(serializer.data)
        else:
            data = Services.objects.all()
            serializer = ServicesSerializers(data, many = True)
            context = {
                'Servicess' : serializer.data
            }
            return Response(context, status= status.HTTP_200_OK)
        
    def delete(self, request, product_id):
        try:
            services = Services.objects.get(pk=product_id)
            services.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Services.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        



class TotalServiceList(APIView):
    def post(self, request):
        data = request.data
        serializer = TotalServicesSerializers(data= data)
        if serializer.is_valid():
            serializer.save()
            return Response(status= status.HTTP_201_CREATED)
        return Response(status= status.HTTP_400_BAD_REQUEST)
    
    
    def get(self, request, *args, **kwargs):
        order_number = kwargs.get('order_number')
        if order_number:
            data = TotalService.objects.filter(order_number = order_number)
            serializer = TotalServicesSerializers(data, many = True)
            return Response(serializer.data)
        else:
            data = TotalService.objects.all()
            serializer = TotalServicesSerializers(data, many = True)
            context = {
                'TotalService' : serializer.data
            }
            return Response(context, status= status.HTTP_200_OK)
        
    def delete(self, request, order_number):
        try:
            services = TotalService.objects.get(order_number=order_number)
            services.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except TotalService.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
