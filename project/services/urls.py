from django.urls import path
from .views import ServicesList

app_name = 'services'

urlpatterns = [
    path('servicesList/', ServicesList.as_view(), name='ServicesList')
]