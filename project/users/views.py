from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import login as d_login, authenticate
from .serializers import LoginSerializer, UserSerializer
from django.contrib.auth.models import User
# Create your views here.

class Register(APIView):
    def post(self, request):
        serializer = UserSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data= request.data)
        serializer.is_valid(raise_exception=True)
        username=serializer.validated_data['username']
        password=serializer.validated_data['password']
        user = User.objects.filter(username=username).first()
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({'refresh' : str(refresh), 'access':str(refresh.access_token)})
        else:
            return Response(status= status.HTTP_400_BAD_REQUEST)
        










