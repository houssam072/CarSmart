from django.urls import path
from .views import OrderList

app_name = 'orders'
urlpatterns = [
    path('orderList/',OrderList.as_view(), name='OrderList'),
    path('orderList/<int:id>/',OrderList.as_view(), name='OrderList'),
    path('orderList/<int:phone>/',OrderList.as_view(), name='OrderList'),
]