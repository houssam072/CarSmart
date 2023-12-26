from django.urls import path
from .views import PurchasesList

app_name = 'storage'

urlpatterns = [
        path('PurchasesList/', PurchasesList.as_view(), name='PurchasesList'),
        path('PurchasesList/', PurchasesList.as_view(), name='PurchasesList'),

]