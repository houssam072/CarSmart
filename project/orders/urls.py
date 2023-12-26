from django.urls import path
from .views import OrderList, ServicesList, TotalServiceList

app_name = 'orders'
urlpatterns = [
    path('orderList/',OrderList.as_view(), name='OrderList'),
    path('orderList/<int:product_id>/',OrderList.as_view(), name='OrderList_filter_id'),
    path('orderList/<int:phone>/',OrderList.as_view(), name='OrderList_filter_phone'),
    path('orderList/<str:order_number>/', OrderList.as_view(), name='Order-detail_delete'),
    
    path('servicesList/<int:product_id>/',ServicesList.as_view(), name='ServicesList'),
    path('servicesList/<str:order>/',ServicesList.as_view(), name='ServicesList_filter_order'),
    path('servicesList/delete/<int:product_id>/',ServicesList.as_view(), name='ServicesList_delete'),

    path('TotalServiceList/',TotalServiceList.as_view(), name='TotalServiceList'),
    path('TotalServiceList/<str:order_number>/',TotalServiceList.as_view(), name='TotalServiceList_filter_order'),
    path('TotalServiceList/delete/<str:order_number>/',TotalServiceList.as_view(), name='TotalServiceList_delete'),
]