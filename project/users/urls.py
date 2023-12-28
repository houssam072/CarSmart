from django.urls import path
from .views import LoginView, Register
from rest_framework_simplejwt.views import (TokenRefreshView)

app_name = 'users'

urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),    
    path('token_refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
