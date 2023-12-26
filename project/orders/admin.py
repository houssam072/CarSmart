from django.contrib import admin
from .models import Order, Services, TotalService

# Register your models here.
admin.site.register(Order)
admin.site.register(Services)
admin.site.register(TotalService)
