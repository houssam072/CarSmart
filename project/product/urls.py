from django.urls import path
from .views import ProductList

app_name = 'products'

urlpatterns = [
    path('productList/', ProductList.as_view(), name='productList')
    
]